from django.shortcuts import render
from .models import Board
from django .contrib. auth import (authenticate, login, logout)

def home(request):
    return render(request, "home.html")

def create_board(request):
    title = request.POST["title"]
    author = request.POST["author"]
    content = request.POST["content"]
    board = Board(title=title, author=author, content=content)
    return redirect('home')

def read_board(request):
    boards =Board.objects.all()
    context = {'boards':boards}
    return render(request, "read.html", context)

def read_detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {'board':board}
    return render(request, "detail_read.html", context)

def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('home')

def edit(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST["title"]
    board.writer = request.POST["writer"]
    board.content = request.POST["content"]
    board.create_at = request.POST["create_at"]
    board.save()
    return redirect('home')

def sign_up(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        if password == cpassword:
            user = User.objects.create_user(
                username=username, password=password
            )
            login(request, user)
            return render(request, "home.html")
        else:
            error = "비밀번호가 다릅니다."
            context = {'error': error}
            return render

        user = User.object.create_user(
            username=request.POST["username"], password=request.POST["password"]
        )
        login(request, user)
        return render(request, 'home.html')
    else:
        return render(request, 'signup.html')

