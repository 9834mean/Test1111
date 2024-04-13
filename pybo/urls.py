from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name="detail"),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('download/' , views.download, name= 'download'),
    path('execute/app/<str:app_name>', views.execute_app, name='execute_app'), 
    path('execute/cmd/', views.execute_cmd, name='execute_cmd' ),
    path('execute/xml/', views.execute_xml, name='execute_xml'), 
    path('get/site/', views.get_site, name='get_site'),
    path('get/userinfo/', views.make_user_message, name='make_user_message'),
    path('hello/user/<str:user_id>', views.hello_user, name='hello_user'),
]

