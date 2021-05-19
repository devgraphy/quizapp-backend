


# 초기 작업 순서
1. 가상환경 구성 및 DRF 설치
2. 장고 프로젝트 생성
3. APP 생성
4. settings.py
    - ALLOWED_HOSTS=['*']: 모든 접근에 대해서 허용
    - TIME_ZONE
    - STATIC_ROOT
    - INSTALLED_APPS 에 'rest_framework', 생성한 app 추가
5. 서버 정상 동작 확인
    - python manage.py runserver
6. models.py
7. serializers.py
8. views.py
9. 프로젝트 urls.py
10. App urls.py