from todo_list.models import todo
from django.shortcuts import HttpResponse , render , redirect

def home(request):
    data= todo.objects.all()   
    if request.method == 'POST':
        var1 = request.POST.get('taskInput')
        var2 = request.POST.get('startInput')
        var3 = request.POST.get('endInput')
        test_instance=todo(taskInput=var1,startInput=var2,endInput=var3)
        test_instance.save()
        return redirect('home')
    return render(request,'todo.html', {'data':data})

def edit(request, id):
    data = todo.objects.get(id=id)   
    if request.method == 'POST':
        var1 = request.POST.get('taskInput')
        var2 = request.POST.get('startInput')
        var3 = request.POST.get('endInput')
        data.taskInput = var1
        data.startInput = var2
        data.endInput = var3
        data.save()  # Save updated task
        return redirect('home')
    return render(request, 'update.html', {'data': data})


def delete(request,id):
    data= todo.objects.get(id=id)
    data.delete()
    return redirect('home')
    