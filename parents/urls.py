from django.urls import path
from parents import views


urlpatterns = [
    path("new", views.new_child, name='new_child'),
    path("<int:parent_id>/", views.view_child_list, name='child_list'),
    path("<int:parent_id>/add_child", views.add_child, name='add_child')
]
