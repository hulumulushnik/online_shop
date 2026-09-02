from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ім'я",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': "Ваше ім'я",
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': "your@email.com",
        })
    )
    subject = forms.CharField(
        max_length=200,
        label="Тема",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': "Тема повідомлення",
        })
    )
    message = forms.CharField(
        label="Повідомлення",
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'placeholder': "Ваше повідомлення...",
            'rows': 6,
        })
    )
