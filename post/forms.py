from django import forms

from post.models import Post


class post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['video_caption', 'video_file', 'video_url', 'video_tags']

        widgets = {
            'video_caption': forms.TextInput(attrs={'class': 'form-control'}),
            'video_file': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.Textarea(attrs={'class': 'form-control'}),
            'video_tags': forms.TextInput(attrs={'class': 'form-control'})
        }
