from django.shortcuts import redirect, reverse, Http404, render
from django.views.generic import ListView
from django.core.paginator import Paginator
from stores.models import Pizza
from stores.forms.filter import SearchAndFilterPizza
from utils.cart import Cart


class PizzaList(ListView):
    model = Pizza
    context_object_name = 'pizza_list'
    template_name = 'stores/pizza/list.html'
    paginate_by = 6

# def list_view(request):
#     pizza_list = Pizza.objects.all()
#     paginator = Paginator(pizza_list, 6)
#     page_nr = request.GET.get('page')
#     page_obj = paginator.get_page(page_nr)
#     return render(request, 'stores/pizza/list.html', {
#         'page_obj': page_obj
#     })


# SearchAndFilterPizza
def list_view(request):
    form = SearchAndFilterPizza(request.GET)
    pizza_list = form.get_filtered_pizza()
    paginator = Paginator(pizza_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'stores/pizza/list.html', {
        'page_obj': page_obj,
        'form': form,
    })


def add_to_cart(request, pizza_id):
    page = request.POST.get('page', 1)
    next_url = request.GET.get('next')

    try:
        quantity = int(request.POST['quantity'])
    except ValueError as e:
        raise Http404(e)

    cart = Cart(request.user, request.session)
    cart.update(pizza_id, quantity)
        
    if next_url:
        return redirect(next_url)

    return redirect('%s?page=%s' % (
        reverse('stores:pizza:list'),
        page
    ))
