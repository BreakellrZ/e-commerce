from django.contrib import admin
from .models import Faq, Question

# Register your models here.


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'question_asked',
    )


admin.site.register(Faq)
admin.site.register(Question)
