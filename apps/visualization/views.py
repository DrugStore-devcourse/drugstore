import logging

from pyecharts import options as opts
from pyecharts.charts import Pie

from django.shortcuts import render
from django.http import Http404

from apps.data_api.models import Drug
from apps.data_collection.models import Word
from apps.visualization.constants import *
from django.db import connection


def top10_pie_chart(request):
    """
    마약 뉴스에서 많이 조회되는 마약 상위 10개를 가져와 pie chart 를 생성
    :param request:
    :return:
    """

    try:
        if not Drug.objects.exists() or not Word.objects.exists():
            logging.warning(ROWS_NOT_EXIST)
            context = {'error_message': CHART_CREATION_REJECT}
        else:
            with connection.cursor() as cursor:
                query = "SELECT text, SUM(frequecny) " \
                        "FROM words " \
                        "WHERE text IN (SELECT drfstf FROM drugs GROUP BY drfstf) " \
                        "GROUP BY text " \
                        "ORDER BY 2 DESC"
                cursor.execute(query)
                drugs_tuple = cursor.fetchall()
                drugs = [[x, y] for x, y in drugs_tuple]
            context = _render_pie_chart(datas=drugs, title=TOP10_CHART_TITLE)
    except (Drug.DoesNotExist, Word.DoesNotExist):
        logging.warning(TABLE_NOT_EXIST)
        raise Http404(CHART_CREATION_FAILED)

    return render(request, f'visualization/{TOP10_PIE_CHART}.html', context)


def _render_pie_chart(datas: list, title: str) -> dict:
    """
    파이차트를 생성하는 내부 메서드
    :param datas: [['option1','29'],['option2', '32']]
    :param title: 차트의 제목
    :return: 차트 html
    """
    c = (
        Pie()
        .add(
            "",
            datas,
            radius=["30%", "75%"],  # 중앙원
            center=["50%", "50%"],  # 차트 위치
            rosetype="area",
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(  # 타이틀
                title=title,
                pos_left="center",
                pos_top="20",
            ),
            legend_opts=opts.LegendOpts(  # 옵션표
                orient="vertical",
                pos_top="15%",
                pos_left="10%"
            ),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(
                formatter="{b} {per|{d}%}",
                font_style="bold",
                font_size=15,
                rich={
                    "per": {
                        "backgroundColor": "#d3cdbfa3",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}: {c} ({d}%)"
            ),
        )
    )
    chart = c.render_embed()
    return {'chart': chart}
