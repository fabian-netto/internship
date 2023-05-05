from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import Todo

# Create your views here.
def home(request):
    content = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        b = Todo.objects.create(name=name)
        return redirect(home)
    return render(request, 'index.html', {'content':content})

def delete(request,id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect(home)

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.name = request.POST['name']
        todo.save()
        return redirect('home')
    context = {'todo': todo}
    return render(request, 'update_todo.html', context)

