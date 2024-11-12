import copy
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(30)
]


def index(request):
    page_num = int(request.GET.get('page', 1))
    questions = Question.objects.all().order_by('-created_at')
    paginator = Paginator(questions, 5)
    
    try:
        page = paginator.page(page_num)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    
    return render(
        request, 
        'index.html', 
        context={'questions':page.object_list, 'page_obj':page}
    )


def hot(request):
    hoy_questions = copy.deepcopy(QUESTIONS)
    hoy_questions.reverse()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(hoy_questions, 5)
    
    try:
        page = paginator.page(page_num)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        'hot.html',
        context={'questions': page.object_list, 'page_obj': page}
    )

def question(request, question_id):
    one_question = QUESTIONS[question_id]
    return render(request, 'one_question.html', 
                {'item': one_question})


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')

def setting(request):
    return render(request, 'setting.html')