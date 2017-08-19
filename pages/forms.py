from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=100)
    contact_email = forms.EmailField(required=True, max_length=100)
    subject = forms.CharField(required=True, max_length=200)
    content = forms.CharField(required=True, widget=forms.Textarea)

    labels = {
        'contact_name': 'Your name:',
        'contact_email': 'Your email:',
        'subject': 'Subject:',
        'content': 'Message:',
    }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs.update({
            'placeholder': 'Name',
            'class': 'form-control'
        })
        self.fields['contact_email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-control'
        })
        self.fields['subject'].widget.attrs.update({
            'placeholder': 'Subject',
            'class': 'form-control'
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Message',
            'class': 'form-control'
        })
