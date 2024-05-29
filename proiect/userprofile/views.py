import random
import string

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from userprofile.forms import NewAccountForm


# from aplicatie.models import Transactions


# Create your views here.
class CreateNewAccount(CreateView):
    # model = Transactions
    template_name = 'aplicatie/transactions_form.html'
    # template_name = 'registration/invite_user.html'
    form_class = NewAccountForm

    def get_success_url(self):
        psw = ''.join(random.SystemRandom()
                      .choice(string.ascii_uppercase +
                              string.ascii_lowercase +
                              string.digits + '!@#$%&') for _ in range(8))
        if User.objects.filter(id=self.object.id).exists():
            user_instance = User.objects.filter(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content = f'Datele tale de autentificare sunt: \n {user_instance.username} \n {psw}'
            msg_html = render_to_string('registration/invite_user.html',
                                        {'content_email': content})
            email = EmailMultiAlternatives(subject='Date conec tare aplicatie', body=content,
                                           from_email='contact@test.ro', to=[user_instance.email])
            email.attach_alternative(msg_html, 'text/html')
            email.send()
        return reverse('transactions:transactions_list')

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateNewAccount, self).form_invalid(form)
