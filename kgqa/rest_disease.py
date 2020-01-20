
from kgqa.KB_query import query_main

from django.http import JsonResponse

def search_question(request):
    question = request.GET['q']

    ret = query_main.query_function(question)

    responseData = {
        'code': 0,
        'message': 'ok',
        'data': ret,
    }

    return JsonResponse(responseData)

