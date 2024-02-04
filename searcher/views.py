from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import ResumeForm
from django.contrib import messages

@login_required
def create_resume(request):
    # Перевіряємо, чи користувач має роль "пошуковець"
    if request.user.role != 'JS':  # Припустимо, що 'JS' - це код для ролі "пошуковець"
        return HttpResponseForbidden("You are not allowed to create a resume")

    if hasattr(request.user, 'resume'):
        messages.error(request, "You already have a resume")
        return redirect('some-view-name')  # Перенаправлення користувача, якщо він вже має резюме

    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # Автоматично прив'язуємо резюме до поточного користувача
            resume.save()
            messages.success(request, "Your resume has been created successfully")
            return redirect('some-view-name')  # Перенаправлення користувача після успішного створення резюме
    else:
        form = ResumeForm()
    
    user_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'phone': request.user.phone,
        'date_of_birth': request.user.date_of_birth,
    }
    context = {
        'form': form,
        'user_data': user_data
    }
    return render(request, 'searcher/create_resume.html', context)