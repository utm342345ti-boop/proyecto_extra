from django import forms
from .models import ProviderSubmission, Comment

class ProviderSubmissionForm(forms.ModelForm):
    class Meta:
        model = ProviderSubmission
        fields = ['provider_name', 'message', 'file']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3})
        }
