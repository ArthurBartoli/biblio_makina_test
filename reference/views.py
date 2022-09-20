from django.shortcuts import render

# Create your views here.
def book_view(request):
    return render(request, 'reference/book_view.html', {})