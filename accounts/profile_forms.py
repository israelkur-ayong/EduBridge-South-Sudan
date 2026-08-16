from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = [
            "profile_picture",
            "phone_number",
            "country",
            "university",
            "course",
            "skills",
            "bio",
            "linkedin",
            "github",
        ]

        widgets = {
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),

            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your country"
            }),

            "university": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "University or institution"
            }),

            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Course or field of study"
            }),

            "skills": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "e.g. Python, Web Development, Graphic Design"
            }),

            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Tell us a little about yourself"
            }),

            "linkedin": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "LinkedIn profile URL"
            }),

            "github": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "GitHub profile URL"
            }),
        }