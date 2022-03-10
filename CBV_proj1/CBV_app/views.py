from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from .models import Book


class Hello_view(View):
    def get(self, request):
        return HttpResponse('<h1>vishal is best doing in CBV projects</h1>')


class Hello_template_view(TemplateView):
    template_name = 'CBV_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'vishal'
        context['age'] = 30
        context['subject'] = 'python'
        return context


class Booklist_view(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'CBV_app/book_list.html'


class BookDetails_view(DetailView):
    model = Book
    context_object_name = 'books'
    template_name = 'CBV_app/books_info.html'
