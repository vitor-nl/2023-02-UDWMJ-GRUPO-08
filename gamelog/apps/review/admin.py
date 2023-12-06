from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from user.models import User
from .models import Review

# Register your models here.
admin.site.is_registered(User)

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by',)

    def save_model(self, request, obj, form, change):
        user = request.user
        obj.review = user
        super(ReviewAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request): 
       qs = super(ReviewAdmin, self).get_queryset(request)
       qs = qs.filter(created_by=request.user)
       return qs


admin.site.register(Review, ReviewAdmin)