from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required

@login_required(login_url='handleLogin')
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        book = Book.objects.create(user=request.user, title=title, text=text)
        return redirect('book_detail', book_id=book.id)
    return render(request, 'bookmark/create_book.html')

@login_required(login_url='/')
def book_list(request):
    book_list = Book.objects.filter(user=request.user)
    book_list = list(book_list)[: : -1]
    return render(request, 'bookmark/book_list.html', {'book_list': book_list})

@login_required(login_url='handleLogin')
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        if book.user == request.user:
            book.delete()
            return redirect('book_list')
        else:
            return render(request, 'bookmark/book_detail.html', {'book': book, 'error_message': 'You are not the owner of this book'})
    return render(request, 'bookmark/book_detail.html', {'book': book})
