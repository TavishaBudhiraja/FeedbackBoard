import json

from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Feedback
# Create your views here.


def home(request):
    if request.method == "POST":
        Feedback.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            service_quality=int(request.POST.get("service_quality")),
            response_time=int(request.POST.get("response_time")),
            staff_behavior=int(request.POST.get("staff_behavior")),
            overall_experience=int(request.POST.get("overall_experience")),
            comments=request.POST.get("comments", "").strip(),
        )

        return redirect("thank_you")

    return render(request, "feedback/home.html")


def thank_you(request):
    return render(request, "feedback/thank_you.html")

@staff_member_required
def dashboard(request):
    feedbacks = Feedback.objects.all().order_by("-created_at")
    total_feedbacks = feedbacks.count()

    if total_feedbacks > 0:
        avg_service_quality = round(
            sum(item.service_quality for item in feedbacks) / total_feedbacks, 2
        )
        avg_response_time = round(
            sum(item.response_time for item in feedbacks) / total_feedbacks, 2
        )
        avg_staff_behavior = round(
            sum(item.staff_behavior for item in feedbacks) / total_feedbacks, 2
        )
        avg_overall_experience = round(
            sum(item.overall_experience for item in feedbacks) / total_feedbacks, 2
        )

        overall_average = round(
            (
                avg_service_quality
                + avg_response_time
                + avg_staff_behavior
                + avg_overall_experience
            )
            / 4,
            2,
        )
    else:
        avg_service_quality = 0
        avg_response_time = 0
        avg_staff_behavior = 0
        avg_overall_experience = 0
        overall_average = 0

    question_average_data = [
        ["Question", "Average Rating"],
        ["Service Quality", avg_service_quality],
        ["Response Time", avg_response_time],
        ["Staff Behavior", avg_staff_behavior],
        ["Overall Experience", avg_overall_experience],
    ]

    rating_distribution_data = [
        ["Rating", "Count"],
        ["1 Star", 0],
        ["2 Stars", 0],
        ["3 Stars", 0],
        ["4 Stars", 0],
        ["5 Stars", 0],
    ]

    satisfaction_data = [
        ["Category", "Count"],
        ["Satisfied", 0],
        ["Neutral", 0],
        ["Dissatisfied", 0],
    ]

    for item in feedbacks:
        average = item.average_rating()

        rating_index = round(average)
        rating_distribution_data[rating_index][1] += 1

        if average >= 4:
            satisfaction_data[1][1] += 1
        elif average >= 3:
            satisfaction_data[2][1] += 1
        else:
            satisfaction_data[3][1] += 1

    context = {
        "feedbacks": feedbacks,
        "total_feedbacks": total_feedbacks,
        "overall_average": overall_average,
        "question_average_data": json.dumps(question_average_data),
        "rating_distribution_data": json.dumps(rating_distribution_data),
        "satisfaction_data": json.dumps(satisfaction_data),
    }

    return render(request, "feedback/dashboard.html", context)