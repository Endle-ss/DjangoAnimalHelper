from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, CustomUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import SearchCard

def index(request):
    return render(request, 'main/index.html')

def cards(request):
    query = request.GET.get('q', '')  
    status = request.GET.get('status', '')
    
    cards = SearchCard.objects.all()
    if query:
        cards = cards.filter(name_animal__icontains=query)
    if status:
        cards = cards.filter(status=status)

    return render(request, 'main/cards.html', {'cards': cards})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        custom_user_form = CustomUserForm(request.POST)

        if user_form.is_valid() and custom_user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            custom_user = custom_user_form.save(commit=False)
            custom_user.user = user
            custom_user.email = user.email
            custom_user.save()

            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        user_form = UserRegistrationForm()
        custom_user_form = CustomUserForm()

    return render(request, 'register.html', {'user_form': user_form, 'custom_user_form': custom_user_form})

def auth_view(request):
    login_form = AuthenticationForm()
    register_form = UserRegistrationForm()
    custom_register_form = CustomUserForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Если пользователь отправил форму входа
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('index')  # Перенаправление на главную страницу

        elif 'register' in request.POST:  # Если пользователь отправил форму регистрации
            register_form = UserRegistrationForm(request.POST)
            custom_register_form = CustomUserForm(request.POST)
            if register_form.is_valid() and custom_register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data['password'])
                user.save()

                custom_user = custom_register_form.save(commit=False)
                custom_user.user = user
                custom_user.email = user.email
                custom_user.save()

                login(request, user)
                return redirect('index')  # Перенаправление на главную страницу

    return render(request, 'main/auth.html', {
        'login_form': login_form,
        'register_form': register_form,
        'custom_register_form': custom_register_form,
    })

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def profile_view(request):
    user = request.user  # Получаем текущего аутентифицированного пользователя
    return render(request, 'main/profile.html', {'user': user})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def search_cards(request):
    query = request.GET.get('q', '')  # Получаем запрос из строки поиска
    if query:
        # Фильтруем карточки по имени животного или другим параметрам
        cards = SearchCard.objects.filter(name_animal__icontains=query)
    else:
        cards = SearchCard.objects.all()  # Показываем все карточки, если нет запроса
    return render(request, 'main/cards.html', {'cards': cards, 'query': query})

def card_detail(request, card_id):
    card = get_object_or_404(SearchCard, id=card_id)
    return render(request, 'main/card_detail.html', {'card': card})

