# drugstore

(23.05.02) runserver시 drugs 데이터가 생성되도록 추가하였습니다



---

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

---
(선택) 더미 데이터 생성 및 삭제 (`{ }`로 표시된 커맨드는 옵션입니다)

```
python manage.py dummydata add {--num 100}
python manage.py dummydate remove
```
