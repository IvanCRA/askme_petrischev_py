import copy
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(30)
]


def index(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(
        request, 
        'index.html', 
        context={'questions':page.object_list, 'page_obj':page}
    )


def hot(request):
    hoy_questions = copy.deepcopy(QUESTIONS)
    hoy_questions.reverse()
    return render(
        request, 
        'hot.html', 
        context={'questions':hoy_questions}
    )

def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(request, 'one_question.html', 
                {'item': one_question})