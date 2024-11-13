import copy
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

QUESTIONS = [
    {
        'title': f'title {i}',
        'id': i,
        'text': f'This is text for question # {i}'
    } for i in range(30)
]

def paginate(obj_list, req, per_page=4):
    try:
        page_num = int(req.GET.get('page', 1))
    except ValueError:
        page_num = 1
    
    paginator = Paginator(obj_list, per_page)
    
    try:
        return paginator.page(page_num)

    except EmptyPage:
        return paginator.page(paginator.num_pages)

    

def index(request):
    page = paginate(QUESTIONS, request, 5)
    
    return render(
        request, 
        'index.html', 
        context={'questions':page.object_list, 'page_obj':page}
    )


def hot(request):
    hoy_questions = copy.deepcopy(QUESTIONS)
    hoy_questions.reverse()
    page = paginate(hoy_questions, request, 5)

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

def tag(request):
    return render(request, 'tag.html')