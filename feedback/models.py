from django.db import models

# Create your models here.


class Feedback(models.Model):
    RATING_CHOICES = [
        (1, "Very Poor"),
        (2, "Poor"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent"),
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    service_quality = models.IntegerField(choices=RATING_CHOICES)
    response_time = models.IntegerField(choices=RATING_CHOICES)
    staff_behavior = models.IntegerField(choices=RATING_CHOICES)
    overall_experience = models.IntegerField(choices=RATING_CHOICES)

    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        total = (
            self.service_quality
            + self.response_time
            + self.staff_behavior
            + self.overall_experience
        )
        return round(total / 4, 2)

    def __str__(self):
        return self.name if self.name else "Anonymous Feedback"