from django.shortcuts import render
from .models import Question, Answer, Tag, Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    questions = Question.objects.all().order_by('-created_at')
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)
    
    page = paginate(questions, request, 5)

    return render(
        request, 
        'index.html', 
        context={
            'questions':page.object_list, 
            'page_obj':page,
            'popular_tags': popular_tags, 
            'top_users': top_users,
        }
    )


def hot(request):
    hot_questions = Question.objects.get_best_questions()
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)


    page = paginate(hot_questions, request, 5)

    return render(
        request,
        'hot.html',
        context={
            'questions': page.object_list, 
            'page_obj': page,
            'popular_tags': popular_tags, 
            'top_users': top_users
        }
    )

def question(request, question_id):
    questions = Question.objects.get_best_questions()

    #if (question_id < 0) or (question_id >= len(questions)):
    #    return question_not_found(request)

    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)

    return render(
        request,
        "question.html",
        context={
            'question': Question.objects.get_question_by_id(question_id),
            'answers': Answer.objects.get_answers_by_question_id(question_id),
            'popular_tags': popular_tags,
            'top_users': top_users
        }
    )

def tag(request, tag_name):
    questions = Question.objects.get_questions_by_tag_name(tag_name)
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)


    page = paginate(questions, request, 5)
    return render(
        request,
        template_name="tag.html",
        context={
            'page_obj': page,
            'questions': page.object_list,

            'tag_name': tag_name,

            'popular_tags': popular_tags,
            'top_users': top_users
        }
    )

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)

    return render(
        request, 
        'ask.html',
        context={
            'popular_tags': popular_tags,
            'top_users': top_users,
        }
    )

def setting(request):
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)

    return render(
        request, 
        'setting.html',
        context={
            'popular_tags': popular_tags,
            'top_users': top_users,
        }
    )


def question_not_found(request):
    popular_tags = Tag.objects.get_popular_n_tags()
    top_users = Profile.objects.top_users(5)


    return render(
        request,
        'question_not_found.html',
        status=404,
        context={
            'popular_tags': popular_tags,
            'top_users': top_users
        }
    )