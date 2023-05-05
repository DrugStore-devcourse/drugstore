import os

import requests
import json
import pandas as pd
from datetime import datetime

from drugstore import settings
from env.keys import API_CONFIG

"""
openAPI로부터 drugs 데이터 추출

조건
- 데이터 갯수 316개(json.body.totalCount)
- API 호출 시 한번에 가져올 수 있는 데이터 수 100개
- 4번 호출하여 316개 추출 후 concat
- 데이터 경로 : json.body.items
- null인 경우 : ""
"""


def get_All_Data(key, url):
    data = []
    params = {'serviceKey': key, 'pageNo': '1', 'numOfRows': '1', 'Drfstf': '', 'Drfstf_eng': '', 'type': 'json'}

    # 전체 데이터 수 탐색
    loading = json.loads(requests.get(url, params=params).text)
    cnt = loading['body']['totalCount']

    pages = (cnt // 100) + 1
    params['numOfRows'] = str(100)
    loading['body']['items'].pop()
    all_json = loading

    for i in range(1, pages + 1):
        if i == pages:
            params['numOfRows'] = str(cnt % 100)
        params['pageNo'] = str(i)
        sub_data = json.loads(requests.get(url, params=params).text)
        data += sub_data['body']['items']
    all_json['body']['items'] = data
    return data, all_json


def raw_2_modelformat(all_data):
    # 4개 fields 추가
    all_data1 = all_data
    for i in range(len(all_data1)):
        all_data1[i]['DEL_FIELD'] = False
        all_data1[i]['ID'] = i + 1
        all_data1[i]['created_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        all_data1[i]['updated_at'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # fields명 소문자로 변경
    all_data2 = []
    for i in range(len(all_data1)):
        dic = {}
        for key, value in all_data1[i].items():
            lowkey = key.lower()
            dic[lowkey] = all_data1[i][key]
        all_data2.append(dic)

    # 결측치 처리, 중복 제거, fields 순서 변경
    df = pd.DataFrame(all_data2)
    df = df.fillna("")
    df = df.drop_duplicates(['drfstf'], keep='last', ignore_index=True)
    df = df[['id', 'drug_no', 'drfstf', 'drfstf_eng', 'type_code', 'pharm', 'side_effect', 'medication', 'del_field',
             'created_at', 'updated_at']]
    all_data3 = df.to_dict('index')

    # format 변경
    jslist = []
    for i in range(len(all_data3)):
        dic = {"model": 'data_api.Drug', "fields": all_data3[i]}
        jslist.append(dic)

    fixture_dir = os.path.join(settings.BASE_DIR, 'drugstore', 'fixtures')
    file_path = os.path.join(fixture_dir, 'drug.json')

    with open(file_path, 'w', encoding='UTF-8') as f:
        json.dump(jslist, f, indent=2, ensure_ascii=False)


def run():
    apikey = API_CONFIG['key']
    url = API_CONFIG['url']

    all_data, all_json = get_All_Data(apikey, url)
    raw_2_modelformat(all_data)


def main():
    run()


if __name__ == "__main__":
    main()
