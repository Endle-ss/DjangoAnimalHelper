# Импорты
from django.contrib import admin
from django import forms
from .models import CustomUser, SearchCard, CardMessage, SearchActivity, Complaint, Statistics, Achievement

# Настройки панели администратора
admin.site.site_header = "Панель администратора Поиска животных"
admin.site.site_title = "Администратор Django"
admin.site.index_title = "Добро пожаловать в панель администратора"

# Действия для обновления статуса поиска
@admin.action(description='Обновить статус на "В процессе поиска"')
def mark_as_in_progress(modeladmin, request, queryset):
    queryset.update(status='В процессе поиска')

@admin.action(description='Обновить статус на "Закрыто"')
def mark_as_lost(modeladmin, request, queryset):
    queryset.update(status='Закрыто')

@admin.action(description='Обновить статус на "Найдено"')
def mark_as_found(modeladmin, request, queryset):
    queryset.update(status='Найдено')

# Админ-панель для модели SearchCard
@admin.register(SearchCard)
class SearchCardAdmin(admin.ModelAdmin):
    list_display = ('name_animal', 'status', 'animal_type', 'last_seen_location', 'created_at')
    search_fields = ('name_animal', 'status', 'last_seen_location')
    list_filter = ('status', 'animal_type', 'created_at')
    actions = [mark_as_in_progress, mark_as_lost, mark_as_found]

# Кастомная форма для CustomUser
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Админ-панель для модели CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm
    list_display = ('user', 'email', 'phone_number', 'role', 'rating')
    search_fields = ('user__username', 'email', 'phone_number', 'role')
    list_filter = ('role',)

# Админ-панель для модели CardMessage
@admin.register(CardMessage)
class CardMessageAdmin(admin.ModelAdmin):
    list_display = ('search_card', 'user', 'created_at')
    ordering = ('-created_at',)

# Админ-панель для модели SearchActivity
@admin.register(SearchActivity)
class SearchActivityAdmin(admin.ModelAdmin):
    list_display = ('search_card', 'user', 'status_activity', 'joined_at')

# Админ-панель для модели Complaint
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_user', 'search_card', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('reason',)

# Админ-панель для модели Statistics
@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'search_card_created', 'animals_found', 'search_count')
    list_filter = ('search_card_created', 'animals_found')

# Админ-панель для модели Achievement
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'points', 'created_at')
    ordering = ('-points',)