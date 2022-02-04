from django.shortcuts import render, redirect
from django.views.generic import View

from .models import CategoryCreation, CommentCreation
from .forms import CommentForm, CategoryForm

class CommentView(View):
    def get(self, request, *args, **kwargs):

        category = CategoryCreation.objects.all()
        comment = CommentCreation.objects.all()

        context = {'category': category,
                   'comment': comment}

        return render(request, 'board/home.html', context)

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST)

        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('board:home')

Home = CommentView.as_view()

class CategoryView(View):
    def post(self, request, *args, **kwargs):

        form = CategoryForm(request.POST)
        if form.is_valid():
            print('バリデーションOK')
            form.save()
        else:
            print('バリデーションNG')
            print(form.errors)

        return redirect('board:home')

Category = CategoryView.as_view()