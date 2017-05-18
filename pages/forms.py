from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, max_length=100)
    contact_email = forms.EmailField(required=True, max_length=100)
    subject = forms.CharField(required=True, max_length=200)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = 'Your name:'
        self.fields['contact_email'].label = 'Your email:'
        self.fields['subject'].label = 'Subject:'
        self.fields['content'].label = 'Message:'
