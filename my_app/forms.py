from django import forms
from my_app.models import Ticket


class TicketForm(forms.ModelForm):
    qr = forms.ImageField(label='Upload your QR code')

    class Meta:
        model = Ticket
        fields = (
            'number',
            'qr',
            'photo',
        )