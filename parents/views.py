from django.shortcuts import render, redirect
from parents.models import Child, Parent


def home_page(request):
    return render(request, 'home.html')


def new_child(request):
    parent_ = Parent.objects.create()
    Child.objects.create(name=request.POST['child_name'], parent=parent_)
    return redirect(f'/parents/{parent_.id}/')


def view_child_list(request, parent_id):
    parent_ = Parent.objects.get(id=parent_id)
    return render(request, 'child_list.html', {'child_list': parent_})


def add_child(request, parent_id):
    parent_ = Parent.objects.get(id=parent_id)
    Child.objects.create(name=request.POST["child_name"], parent=parent_)
    return redirect(f'/parents/{parent_.id}/')
