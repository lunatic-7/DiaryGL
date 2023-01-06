import openai
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from bookmark.models import *

openai.api_key = "hackerbro"

def generate_text(request):

    if request.method == 'POST':
        # Get the prompt from the request data
        prompt = request.POST.get("prompt", "")

        # Generate text using the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=1.0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=['asdd', 'sbdbd']
        )
        generated_text = response["choices"][0]["text"]
        return render(request, 'generate_text.html', {'message': generated_text, 'prompt': prompt})
    else:
        return render(request, 'main.html')

def handleSignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    return redirect("/")