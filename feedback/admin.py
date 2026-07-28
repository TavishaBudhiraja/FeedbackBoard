from django.contrib import admin
from .models import Feedback

# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "service_quality",
        "response_time",
        "staff_behavior",
        "overall_experience",
        "created_at",
    )

    search_fields = ("name", "email", "comments")
    list_filter = ("created_at",)