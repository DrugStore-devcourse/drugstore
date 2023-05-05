import logging

from pyecharts import options as opts
from pyecharts.charts import Pie

from wordcloud import WordCloud

from django.shortcuts import render
from django.http import Http404

from apps.data_api.models import Drug
from apps.data_collection.models import *
from apps.visualization.constants import *
from django.db import connection

from io import BytesIO
import base64
import os
from django.conf import settings


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
                query = "SELECT text, SUM(frequency) " \
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
                pos_left="5%"
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


def _drug_count(article_id):  # 워드클라우드 생성을 위한 text 갯수 파악
    count = {}
    for id in article_id:
        words = Word.objects.filter(article_id_id__exact=id)
        for word in words:
            if word.text not in count:
                count[word.text] = word.frequency
            else:
                count[word.text] += word.frequency
    return count


def _word_cloud_maker(count):  # 워드클라우드 생성

    font_path = 'static/font/gothic.ttf'

    wc = WordCloud(font_path=font_path, background_color='white',
                   max_words=1000, max_font_size=100).generate_from_frequencies(count)

    # 워드클라우드 이미지를 BytesIO 객체에 저장
    img_file = BytesIO()
    wc.to_image().save(img_file, format='PNG')
    img_file.seek(0)

    # BytesIO 객체에 저장된 이미지 파일을 base64로 인코딩하여 웹 페이지에 전달
    return base64.b64encode(img_file.read()).decode('utf-8')


def wordcloud_chart(request, id):
    try:
        drug = Drug.objects.get(id__exact=id)
        article_id = [word.article_id.article_id for word in Word.objects.filter(
            text__exact=drug.drfstf)]

        count = _drug_count(article_id)
        img_base64 = _word_cloud_maker(count)
        context = {'img_base64': img_base64}

    except (Drug.DoesNotExist, Word.DoesNotExist, AttributeError):
        logging.warning(ROWS_NOT_EXIST)
        context = {'error_message': CHART_CREATION_REJECT}
    except FileNotFoundError:
        context = {'error_message': FILE_NOT_FOUND}
    except:
        context = {'error_message': CHART_CREATION_FAILED}

    return render(request, 'visualization/wordcloud.html', context)