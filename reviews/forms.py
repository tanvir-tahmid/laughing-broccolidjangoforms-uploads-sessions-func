from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Name",
            "review_text": "Feedback",
            "rating": "Rating"
        }
        error_messages = {
            "user_name": {
              "required": "Name must not be empty!",
              "max_length": "Name must be under 100 characters"
            }
        }