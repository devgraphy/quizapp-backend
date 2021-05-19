from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random
# Create your views here.
# 문자열을 반환하는 API
@api_view(['GET'])
def helloAPI(request):
    return Response ("hello world!")

# 주어진 개수만큼 랜던함 퀴즈를 반환하는 API
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    serializer = QuizSerializer(randomQuizs, many=True) # many=True : 다수 데이터 직렬화
    return Response(serializer.data)

