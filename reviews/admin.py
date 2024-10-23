from django.contrib import admin
from .models import Reviews

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'body',
        'rating',
        'created_on',
        'updated_on',
        'author'

    )


admin.site.register(Reviews)
