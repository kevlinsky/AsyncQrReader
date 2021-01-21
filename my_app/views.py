from django.shortcuts import render, redirect
from pyzbar import pyzbar
from django.views.generic import CreateView
from my_app.forms import TicketForm
from my_app.models import Ticket


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets_create.html'

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            qr_image = request.FILES.get('qr')
            data = pyzbar.decode(qr_image)
            qr_data = data[0].data.decode('utf-8')
            photo = request.FILES.get('photo')
            number = request.POST.get('number')
            Ticket.objects.create(qr=qr_data, photo=photo, number=number)
            return redirect('qr:success')
        else:
            return render(request, 'tickets_create.html', {'form': TicketForm, 'errors': form.errors})


def success(request):
    return render(request, 'tickets_create_success.html')
