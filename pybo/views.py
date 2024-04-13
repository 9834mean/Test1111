from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from django.utils.safestring import mark_safe
import subprocess
from django.views.decorators.csrf import csrf_exempt
import os
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges
from xml.dom.pulldom import parseString, START_ELEMENT
import requests
import time
AUTHENTICATE_KEY = "p@ssw0rd"

class UserInfo:
    __user_secrets__ = []
    # 클래스 내부의 값을 반환하는 메서드 ==> GETTER
    def get_user_secrets(self):
        return self.__user_secrets__
    # 외부에서 클래스 내부에 값을 설정하는 메서드 ==> SETTER
    def set_user_secrets(self, user_secrets):       
        self.__user_secrets__ = user_secrets

def hello_user(request, user_id):
    UserInfo.user_id = user_id # 요청 파라미터로 전달된 값을 클래스 변수에 설정

    time.sleep(3)               # 다른 내부 처리를 묘사 (3초 딜레이)

    return render(request, 'pybo/success.html', { 'data': f'Hello, {UserInfo.user_id}!!!' }) # 클래스 변수 사용

def __str__(self):
    return self.user_id

def make_user_message(request):
    user_info = UserInfo(request.GET.get('user_id', ''))
    # format_string = request.GET.get('msg_format', '')
    message = "Hello, {user}".format(user=user_info)
    return render(request, 'pybo/success.html', {'data': message})

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = { 'question_list': question_list }

    return render(request, 'pybo/question_list.html', context)


def get_site(request):
    url = request.GET.get('url')
    res = requests.get(url)
    return render(request, 'pybo/error.html', {'data' : mark_safe(res.text)})

ALLOW_PROGRAM = ['notepad', 'calc']

def execute_app(request, app_name):
    if app_name in ALLOW_PROGRAM:
        os.system(app_name)
        return render(request, 'pybo/success.html', {'data': f'{app_name}을 실행했습니다.'})
    else:
        return render(request, 'pybo/error.html', {'error': f'{app_name}을 실행할 수 없습니다.'})

ALLOW_PROGRAM = ['dir','whoami']

def execute_cmd(request):
    cmd = request.GET.get('cmd','')
    if cmd in ALLOW_PROGRAM:
        result = subprocess.check_output(cmd, shell=True, encoding='MS949')
        data = mark_safe(f'<pre>{cmd}을 실행했습니다.\n {result}</pre>')
        return render(request, 'pybo/success.html', {'data': data})
    else:
        return render(request, 'pybo/error.html',{'error': f'{cmd}는 실행할 수 없습니다.'})

def download(request):
    request_file = request.GET.get('request_file')
    (filename, file_ext) = os.path.splitext(request_file)
    file_ext = file_ext.lower()
    if file_ext not in ['.txt', '.csv']:
        return render(request, 'pybo/error.html', {'error':'파일을 열 수 없습니다.'})


    filename = filename.replace('.', '')
    filename = filename.replace('/', '')
    filename = filename.replace('\\', '')

    rrequest_file = f"c:\\temp\\{filename}{file_ext}"
    with open(request_file) as f:
        data = f.read()
        return render(request, 'pybo/success.html', {'data':data})


def execute_xml(request):
    parser = make_parser()
    parser.setFeature(feature_external_ges, False)

    doc = parseString(request.GET.get('xml'), parser=parser)
    for event, node in doc:
        if event == START_ELEMENT and node.tagName == "foo":
            doc.expandNode(node)
            text = node.toxml()
            return render(request, 'pybo/success.html', {'data': text})

    return render(request, 'pybo/error.html', {'error': f'출력할 내용이 없습니다.'})

def detail(request, question_id): 
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)

    msg = "<script> alert('xss') </script>"
    msg = mark_safe(msg)
    context = { 'question': question, 'msg': msg }

    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)	
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())

    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'pybo/question_form.html', { 'form': form })
    elif request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')