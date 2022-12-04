from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('logout/', RedirectView.as_view(url = '/admin/logout/')),
    path('index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('', views.landingpage, name='landingpage'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('present_student', views.present_student, name='present_student'),
    path('Attendance', views.Attendance, name='Attendance'),
    path('class_room', views.class_room, name='class_room'),
     path('TakeAttendance', views.attn, name='attn'),
    path('searchc', views.searchc, name='searchc'),
    path('searchm', views.searchm, name='searchm'),
    path('searcha', views.searcha, name='searcha'),
    path('contactus', views.contactus, name='contactus'),
    # path('indexe', views.indexe, name='indexe'),

    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),



    path('students', views.students, name="students"),
    path('add-student/', views.add_student, name="add_student"),
    path('view_student/<str:pk>', views.view_student, name="view_student"),
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
    path('delete-product/<str:pk>', views.deleteProduct, name="delete-prod")
]