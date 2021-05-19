from django.contrib import admin
from .models import Quiz

# 관리자 페이지에서 명시한 모델을 관리할 수 있다.
# Register your models here.
admin.site.register(Quiz)