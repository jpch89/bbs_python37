import functools
import time

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.template import Context, RequestContext, Template
from django.template.loader import get_template
from django.urls import reverse
from django.urls.converters import IntConverter
# 团子注：method_decorator 方法装饰器，可以让函数装饰器能够装饰方法
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (DetailView, ListView, RedirectView,
                                  TemplateView)

from post.forms import TopicModelForm, TopicSearchForm
from post.models import Comment, Topic
from post.post_service import build_topic_base_info, build_topic_detail_info


def hello_django_bbs(request):
    html = '<h1>Hello Django BBS</h1>'
    response = HttpResponse(html)
    response['project'] = 'BBS'
    response['app'] = 'post'

def hello_django_bbs(request):
    t = Template('<h1>Hello {{ project }}</h1>')
    c = Context({'project': 'Django BBS'})
    html = t.render(c)
    return HttpResponse(html)

def hello_django_bbs(request):
    t = get_template('post/hello_django_bbs.html')
    html = t.render({'project': 'Django BBS'})
    return HttpResponse(html)

def hello_django_bbs(request):
    return render(request, 'post/hello_django_bbs.html', {'project': 'Django BBS'})


def exec_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print('%ss elapsed for %s' % (time.time() - start, func.__name__))
        return res
    return wrapper


class ExecTimeMixin(object):
    @method_decorator(csrf_exempt)
    @method_decorator(exec_time)
    def dispatch(self, request, *args, **kwargs):
        return super(ExecTimeMixin, self).dispatch(request, *args, **kwargs)


class FirstView(ExecTimeMixin, View):
    html = '(%s) Hello Django BBS'

    def get(self, request):
        return HttpResponse(self.html % 'GET')

    def post(self, request):
        return HttpResponse()


def dynamic_hello(request, year, month, day=15):
    html = '<h1>(%s) Hello Django BBS</h1>'
    return HttpResponse(html % ('%s-%s-%s' % (year, month, day)))


class MonthConverter(IntConverter):
    regex = '0?[1-9]|1[0-2]'


def topic_list_view(request):
    """
    话题列表
    :param request:
    :return:
    """
    topic_qs = Topic.objects.all()
    result = {
        'count': topic_qs.count(),
        'info': [build_topic_base_info(topic) for topic in topic_qs]
    }

    return JsonResponse(result)


def topic_list_view(request):
    """
    话题列表
    :params request:
    :return:
    """
    topic_qs = Topic.objects.all()
    result = {
        'count': topic_qs.count(),
        'info': [build_topic_base_info(topic) for topic in topic_qs]
    }
    return render(request, 'post/topic_list.html', result)


@login_required
def topic_detail_view(request, topic_id):
    """
    话题详细信息
    :param request:
    :param topic_id:
    :return:
    """
    result = {}
    try:
        result = build_topic_detail_info(Topic.objects.get(pk=topic_id))
    except Topic.DoesNotExist:
        pass
    return JsonResponse(result)


@csrf_exempt
def add_comment_to_topic_view(request):
    """
    给话题添加评论
    :param request:
    :return:
    """
    topic_id = int(request.POST.get('id', 0))
    content = request.POST.get('content', '')
    topic = None
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        pass
    if topic and content:
        return JsonResponse({
            'id': add_comment_to_topic_view(topic, content).id
        })

    return JsonResponse({})


def dynamic_hello_reverse(request):
    return HttpResponseRedirect(
        reverse('post:dynamic_hello', args=(2018, 9, 16),
                current_app=request.resolver_match.namespace)
    )


"""
def hello_redirect(request):
    class A:
        @classmethod
        def get_absolute_url(cls):
            return '/post/topic_list/'
    return redirect(A)
"""


def hello_redirect(request):
    return redirect('post:dynamic_hello', 2018, 9, 16)


class IndexView(TemplateView):
    template_name = 'post/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['hello'] = 'Hello Django BBS'
        return context


class CommentUpRedirectView(RedirectView):
    pattern_name = 'post:topic_detail'
    query_string = False  # 这个默认就是 False，可以不用写

    def get_redirect_url(self, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['comment_id'])
        comment.up = F('up') + 1
        comment.save()
        del kwargs['comment_id']
        kwargs['topic_id'] = comment.topic_id
        return super(CommentUpRedirectView, self).get_redirect_url(*args, **kwargs)


class TopicList(ListView):
    # model = Topic
    queryset = Topic.objects.all()

"""
class TopicList(ListView):
    queryset = Topic.objects.filter(pk__gt=10)
    allow_empty = False
"""


class TopicDetailView(DetailView):
    model = Topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context.update({
            'comment_list': Comment.objects.filter(topic=pk)
        })
        return context


def project_signature(request):
    """
    上下文处理器。
    """
    return {'project': 'Django BBS'}


def hello_django_bbs(request):
    t = Template('<h1>Hello {{ project }}, {{ user.username }}</h1>')
    c = RequestContext(request, processors=[project_signature])
    html = t.render(c)
    return HttpResponse(html)


def hello_django_bbs(request):
    return render(request, 'post/hello_django_bbs.html')

"""
def search_topic_form(request):
    return render(request, 'post/search_topic.html')
"""


"""
def search_topic(request):
    if not request.GET.get('title', ''):
        errors = ['title is invalid']
        return render(request, 'post/search_topic.html', context={'errors': errors})
    topic_qs = Topic.objects.filter(title__contains=request.GET['title'])
    return render(request, 'post/topic_list.html', context={'object_list': topic_qs})
"""


def search_topic(request):
    """接收 form 的 action 的视图函数"""
    # 团子注：注意这里，request.GET 是一个 QueryDict 对象，之前在 Shell 中使用的是字典对象
    form = TopicSearchForm(request.GET)
    if form.is_valid():
        topic_qs = Topic.objects.filter(title__contains=form.cleaned_data['title'])
        return render(request, 'post/topic_list.html', context={'object_list': topic_qs})
    else:
        return render(request, 'post/search_topic.html', context={'form': form})

def search_topic_form(request):
    """渲染表单"""
    return render(request, 'post/search_topic.html', context={'form': TopicSearchForm()})


def topic_model_form(request):
    if request.method == 'POST':
        topic = TopicModelForm(request.POST)
        if topic.is_valid():
            topic = Topic.objects.create(title=topic.cleaned_data['title'], content=topic.cleaned_data['content'], user=request.user)
            # 团子注：第一次看到这种用法，还可以不经过路由直接访问视图函数的吗？
            return topic_detail_view(request, topic.id)
        else:
            return render(request, 'post/topic_model_form.html', context={'form': topic})
    else:
        return render(request, 'post/topic_model_form.html', context={'form': TopicModelForm()})
