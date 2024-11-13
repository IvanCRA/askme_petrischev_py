import copy
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Answer, Tag, Profile
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
    popular_tags = Tag.objects.get_popular_n_tags()
    #top_users = Profile.objects.get_top_n_users_by_number_of_answers(5)

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
        context={
            'questions':page.object_list, 
            'page_obj':page,
            'popular_tags': popular_tags, 
            #'top_users': top_users,
        }
    )


def hot(request):
    hot_questions = Question.objects.get_best_questions()
    popular_tags = Tag.objects.get_popular_n_tags()
    #top_users = Profile.objects.get_top_n_users_by_number_of_answers(5)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(hot_questions, 5)
    
    try:
        page = paginator.page(page_num)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        'hot.html',
        context={
            'questions': page.object_list, 
            'page_obj': page,
            'popular_tags': popular_tags, 
            #'top_users': top_users
        }
    )

def question(request, question_id):
    questions = Question.objects.get_best_questions()

    #if (question_id < 0) or (question_id >= len(questions)):
    #    return question_not_found(request)

    popular_tags = Tag.objects.get_popular_n_tags()
    #top_users = Profile.objects.get_top_n_users_by_number_of_answers(5)

    return render(
        request,
        "question.html",
        context={
            'question': Question.objects.get_question_by_id(question_id),
            'answers': Answer.objects.get_answers_by_question_id(question_id),
            'popular_tags': popular_tags,
            #'top_users': top_users
        }
    )

def tag(request, tag_name):
    questions = Question.objects.get_questions_by_tag_name(tag_name)
    popular_tags = Tag.objects.get_popular_n_tags()
    #top_users = Profile.objects.get_top_n_users_by_number_of_answers(5)

    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(questions, 5)
    
    try:
        page = paginator.page(page_num)

    except PageNotAnInteger:
        page = paginator.page(1)

    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(
        request,
        template_name="tag.html",
        context={
            'page_obj': page,
            'questions': page.object_list,

            'tag_name': tag_name,

            'popular_tags': popular_tags,
           # 'top_users': top_users
        }
    )

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')

def setting(request):
    return render(request, 'setting.html')


def question_not_found(request):
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.get_top_n_users_by_number_of_answers(5)

    return render(
            request,
            'question_not_found.html',
            status=404,
            context={
                'popular_tags': popular_tags,
                'top_users': top_users
            }
        )