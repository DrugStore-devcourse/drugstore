# 💉마약 기사 크롤링과 데이터 시각화📰

## :technologist:프로젝트 소개 
### 1. 내용
 최근 증가하는 마약사범 문제를 다루기 위해, 뉴스 기사를 분석하여 가장 많이 언급된 10개 마약 성분을 도출하고,   
해당 마약 성분에 대한 특성을 파악한 후, 언급된 기사들을 분석하여 시각화하는 프로젝트입니다.  

<br> 

 마약사범의 증가와 함께 마약 관련 정보 파악이 중요한 시대입니다.  
이에 따라 뉴스 기사의 키워드를 분석하여 마약 관련 정보를 시각적으로 제공하고자 합니다.   
이 프로젝트를 통해 마약 관련 정보 파악의 효율성을 높이고, 예방에 기여하는 것이 주요 목표입니다.  

<br> 

> __기대효과__
> - 마약의 종류와 특징을 쉽게 파악할 수 있게 됩니다. 
> - 가장 화제성 높은 마약을 알 수 있어, 이를 예방하고 대처하는 데에도 큰 도움이 됩니다.
> - 마약별 연관된 키워드를 파악할 수 있어, 마약 관련 정보를 더욱 쉽게 이해할 수 있게 됩니다.


<br> 

### 2. 팀원
|                                                                  ![](https://ca.slack-edge.com/T04T8V1DKG9-U05209406F7-4c684b0ccd91-512)                                                                   |                                                                    ![](https://ca.slack-edge.com/T04T8V1DKG9-U0522MUCQ58-fb5e28d1fdb8-512)                                                                    |                                                                       ![](https://ca.slack-edge.com/T04T8V1DKG9-U052H9VPSUR-ef4dd2a09f8d-512)                                                                        |                                                                   ![](https://ca.slack-edge.com/T04T8V1DKG9-U0522J1CSUS-38dee3162b48-512)                                                                    |                                                                       ![](https://ca.slack-edge.com/T04T8V1DKG9-U05227DJ2CB-967cd36757ce-512)
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
|                                                            **김창민**                                                                                  |                                                                                   **김혜민**                                                                                    |                                                                                  **이성희**                                                                                  |                                                                               **박정우**                                                                                |                                                                                 **남윤아**
|                                                                            **프론트/백엔드**                                                                            |                                                                            **데이터 ETL 개발**                                                                            |                                                                          **시각화/환경구축**                                                                          |                                                                          **프론트/백엔드**                                                                          |                                                                         **시각화/환경구축**                                                                          |
|                                                                            **[@pstar314](https://github.com/pstar314)**                                                                            |                                                                            **[@HyeM207](https://github.com/HyeM207)**                                                                            |                                                                           **[@gracia10](https://github.com/gracia10)**                                                                          |                                                                          **[@pjw74](https://github.com/pjw74)**                                                                          |                                                                         **[@namuna309](https://github.com/namuna309)**                                                                          |



<br> 

### 3. 기술스택

| 분야        | Stack  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 언어 | <img src="https://img.shields.io/badge/python-3.8-3776AB?style=flat&logo=python&logoColor=white"> |
| 백엔드 |<img src="https://img.shields.io/badge/django-4.2-092E20?style=flat&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/sqlite3-003B57?style=flat&logo=sqlite&logoColor=white"/> |
| 프론트 | <img src="https://img.shields.io/badge/html-F05132?style=flat&logo=html5&logoColor=black">  <img src="https://img.shields.io/badge/css-61DAFB?style=flat&logo=css3&logoColor=black"> |
| 라이브러리 | <img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"/> <img src="https://img.shields.io/badge/selenium-43B02A?style=flat&logo=selenium&logoColor=white"/> <img src="https://img.shields.io/badge/beautifulsoup-3776AB?style=flat&logo=beautifulsoup&logoColor=white"/> <img src="https://img.shields.io/badge/pyecharts-3776AB?style=flat&logo=pyecharts&logoColor=white"/> |
| 버전 관리 | <img src="https://img.shields.io/badge/git-F05032?style=fflat&logo=git&logoColor=black">  <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white">  |
| 협업 도구 |  <img alt="Slack" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=flat&logo=slack&logoColor=white"/> <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/notion-000000?style=flat&logo=notion&logoColor=white"/> <img src="https://img.shields.io/badge/gather-380953?style=flat&logo=gather&logoColor=white"/>

<br> 

### 4. 워크플로우 및 데이터 모델링
#### 데이터베이스 스키마
<img src="https://user-images.githubusercontent.com/131341085/237012454-f30ea1a0-85af-4b1b-9357-01d1307e60f0.png" width="300" height="300">

#### 프로젝트 아키텍쳐 및 워크플로우
<img src="https://user-images.githubusercontent.com/131341085/237011578-b4d2446b-5e45-4693-a4ce-74f880d5f959.png" width="70%" height="70%">

<br> 

### 5. 시연

![example](https://user-images.githubusercontent.com/70009161/237039158-cc59bc3d-8279-4a30-a777-c2a83674274d.gif)

<br> 
      
## 🏃‍♂프로젝트 구현
- 공공데이터 [마약류 약물 및 오남용 정보 API](https://www.data.go.kr/data/15058963/openapi.do)를 호출하여 약물 정보를 적재한다.
- 다음 검색창에 '마약' 키워드로 검색하여 조선일보, 연합뉴스, KBS 언론사의 전일 뉴스 기사를 크롤링한다.
- 기사 본문을 분석하여 가장 많이 언급된 10개의 마약류 약물을 도출해 pie chart로 시각화 한다.
- 마약류 약물별로 해당 약물이 언급된 기사 본문을 분석하여 word cloud로 시각화 한다.  
- 마약류 약물 목록 페이지와 상세 페이지를 구현하여 관련 차트와 연결한다.

<br> 

## :memo:참고사항
- 프로젝트 실행 방법
  1. 프로젝트 checkout
  2. 루트 경로(drugsiore/) 에서 shell 실행후 가상환경 생성
      ```
      python -m venv venv
      source venv/bin/activate
      ``` 
  3. 패키지 다운로드
      ```
      pip install -r requirements.txt
      ```
  4. 테이블 생성
      ```
      python manage.py makemigrations
      python manage.py migrate
      ```
  5. 마약 뉴스 크롤러 실행
      ```
      # article, words 초기화 후 적재
      python manage.py crawldata
      ```
  6. 서버 실행
      ```
      python manage.py runserver
      ```
