from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'title',
        'body',
        'firstcreated',
        'lasteditted',
    )


admin.site.register(Review, ReviewAdmin)
