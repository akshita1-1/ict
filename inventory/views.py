from inventory.models import invt
from django.shortcuts import render, redirect

def inventory(request):
    data = invt.objects.all()
    if request.method == 'POST':
        var1 = request.POST.get('product')
        var2 = request.POST.get('price')
        var3 = request.POST.get('quantity')
        var4 = request.POST.get('discount')

        # Save new inventory item
        test_instance = invt(
            product=var1,
            price=var2,
            quantity=var3,
            discount=var4
        )
        test_instance.save()
        return redirect('inventory')

    return render(request, 'inventory.html', {'data': data})


def edit(request, id):
    data = invt.objects.get(id=id)
    if request.method == 'POST':
        data.product = request.POST.get('product')
        data.price = request.POST.get('price')
        data.quantity = request.POST.get('quantity')
        data.discount = request.POST.get('discount')
        data.save()
        return redirect('inventory')

    return render(request, 'update.html', {'data': data})


def delete(request, id):
    data = invt.objects.get(id=id)
    data.delete()
    return redirect('inventory')
