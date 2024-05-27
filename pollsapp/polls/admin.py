from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoinInline(admin.TabularInline):
    model = Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoinInline]