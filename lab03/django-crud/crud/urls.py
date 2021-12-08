from django.urls import path
from crud import views

urlpatterns = [
    path('', views.index, name='index'),

    path('save/', views.saveAction, name='save'),

    path('edittodo/<int:pk>', views.editTodo, name='edittodo'),

    path('delete/<int:pk>', views.deleteAction, name='delete')
]
