# 💉마약 기사 크롤링과 데이터 시각화📰

## :technologist:프로젝트 소개 
### 1. 내용
최근 국내에 마약사범이 급속도로 증가함에 따라, 현 상황을 뉴스 기사의 키워드를 통해 분석해보고자 한다.    

마약 관련 기사의 데이터(제목 및 내용)을 분석하여 가장 많이 언급된 10개 마약 성분을 도출 후 bar-chart로 시각화한 후, \
해당 마약 성분의 상세 내용과 언급된 기사들에 대한 데이터 분석을 word cloud로 시각화한다.  

기사 수집은 다음 뉴스에 '마약' 키워드로 검색 시 조회된 조선일보, 연합뉴스, KBS 언론사의 전날 뉴스 기사를 크롤링하는 방식으로 진행된다. 

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
| 프론트 | <img src="https://img.shields.io/badge/html-F05132?style=flat&logo=html5&logoColor=black">  <img src="https://img.shields.io/badge/css-61DAFB?style=flat&logo=css3&logoColor=black"> |
| 백엔드 |<img src="https://img.shields.io/badge/django-092E20?style=flat&logo=django&logoColor=white"/>  <img src="https://img.shields.io/badge/sqlite-003B57?style=flat&logo=sqlite&logoColor=white"/> |
| 데이터 크롤링 및 시각화 | <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"> |
| 버전 관리 | <img src="https://img.shields.io/badge/git-F05032?style=fflat&logo=git&logoColor=black">  <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white">  |
| 협업 도구 |  <img alt="Slack" src ="https://img.shields.io/badge/Slack-4A154B.svg?&style=flat&logo=github&logoColor=white"/>     <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white">

<br> 

### 4. 워크플로우 및 데이터 모델링

![ERDCloud_drug](https://user-images.githubusercontent.com/70009161/236844952-2a153da7-fada-481c-9129-662ef25a2661.PNG)

      
## 🏃‍♂프로젝트 구현
- 가장 많이 언급된 상위 10개 마약류 차트
- 마약 상세 소개 및 관련 기사 Word Cloud 차트

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
