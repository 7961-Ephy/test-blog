from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    # Define the author field as a dropdown menu of authors
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")

    class Meta:
        model = Blog
        fields = ['author', 'title', 'content']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Customize the form's appearance or behavior here if needed

    def clean(self):
        cleaned_data = super().clean()
        # Additional form validation can be performed here
        return cleaned_data
    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        # Customize the form's appearance or behavior here if needed
        
    def clean(self):
        cleaned_data = super().clean()
        # You can add custom validation here if necessary
        return cleaned_data