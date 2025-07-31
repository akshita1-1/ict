from django.shortcuts import render, redirect
from bill.models import Customer, Product
from inventory.models import invt  # inventory model

def home(request):
    inventory_products = invt.objects.all()  # fetch all inventory products

    if request.method == 'POST':
        # 1️⃣ Save Customer
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        if name and phone and email and address:
            customer = Customer.objects.create(
                name=name,
                phoneno=phone,
                email=email,
                address=address
            )

            # 2️⃣ Save selected products for this customer
            for i in range(1, 6):  # 5 product rows in HTML
                product_id = request.POST.get(f'product_{i}')
                quantity = request.POST.get(f'quantity_{i}')

                if product_id and quantity:
                    try:
                        inventory_item = invt.objects.get(id=product_id)
                        quantity = int(quantity)

                        Product.objects.create(
                            customer=customer,
                            product=inventory_item.product,
                            quantity=quantity,
                            price=inventory_item.price,
                            discount=inventory_item.discount
                        )
                    except invt.DoesNotExist:
                        pass

            return redirect('home')  # reload page

    return render(request, 'bill.html', {'products': inventory_products})
