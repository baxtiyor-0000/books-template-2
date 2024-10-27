from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_form.html', {'book': book})

@login_required
def my_books(request):
    books = Book.objects.filter(author=request.user)
    return render(request, 'my_books.html', {'books': books})

@login_required
def share_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        recipient = request.POST['email']
        send_mail(
            f"Book Recommendation: {book.title}",
            f"Hi, \n\nI wanted to recommend this book to you: {book.title} by {book.author}. \n\nDescription: {book.description} \n\nPublished on: {book.published_date}.",
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
        return redirect('book_detail', pk=pk)
    return render(request, 'share_book.html', {'book': book})