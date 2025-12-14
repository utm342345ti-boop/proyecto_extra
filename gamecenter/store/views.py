from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProviderSubmissionForm, CommentForm
from django.core.paginator import Paginator

def index(request):
    featured = Product.objects.order_by('-created_at')[:6]
    return render(request, 'store/index.html', {'featured': featured})

def catalog(request):
    qs = Product.objects.all().select_related('category')
    q = request.GET.get('q')
    category = request.GET.get('category')
    if q:
        qs = qs.filter(name__icontains=q)
    if category:
        qs = qs.filter(category__slug=category)
    paginator = Paginator(qs, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'store/catalog.html', {'products': products, 'categories': categories})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    comments = product.comments.filter(approved=True).order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('store:product_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'store/product_detail.html', {'product': product, 'comments': comments, 'form': form})

def contact_provider(request):
    if request.method == 'POST':
        form = ProviderSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'store/contact_provider.html', {'form': ProviderSubmissionForm(), 'success': True})
    else:
        form = ProviderSubmissionForm()
    return render(request, 'store/contact_provider.html', {'form': form})


def comments(request):
    comments = Comment.objects.all()
    return render(request, 'store/comments.html', {
        'comments': comments
    })


def home(request):
    return render(request, 'store/home.html')