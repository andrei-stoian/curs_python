from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, reverse, HttpResponse, redirect
from django.template.loader import get_template
from django.utils.decorators import decorator_from_middleware
from users.middlewares.activation_middleware import ActivationMiddleware

from django.shortcuts import get_object_or_404

from django.utils import timezone
from users.models import Activation, AVAILABILITY
from users.forms import PasswordForm

from users.utils.constants import ACTIVATION_AVAILABILITY


@decorator_from_middleware(ActivationMiddleware)
def activate_user(request, token):
    activation = get_object_or_404(Activation, token=token)
    user = activation.user

    if request.method == 'GET':
        form = PasswordForm(user)
    else:
        form = PasswordForm(user, request.POST)

        if form.is_valid():
            form.save()

            user.is_active = True
            user.save()

            activation.activated_at = timezone.now()
            activation.save()

            return redirect(reverse('home'))

    return render(request, 'users/activation/set_password.html', {
        'token': token,
        'form': form
    })


@decorator_from_middleware(ActivationMiddleware)
def reset_token_view(request, token):
    if request.method == 'GET':
        return render(request, 'users/activation/reset_token.html', {
            'token': token
        })

    activation = get_object_or_404(Activation, token=token)
    activation.expires_at = timezone.now() + timezone.timedelta(**AVAILABILITY)
    activation.save()
    send_activation_email(activation.user)

    return HttpResponse(
        'Token has been reset.'
        'Please follow the instructions received on your'
        'email in order to activate your account'
    )
    # return render(request, 'users/activation/reset_token_success.html', {
    #     'user': activation.user
    # })


def send_activation_email(user):
    domain = Site.objects.get_current().domain
    url = reverse('users:activation:activate', args=(user.activation.token,))

    activation_url = f'{domain}{url}'

    print('!!! activation_url is', activation_url)


    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'activation_url': activation_url,
        'availability': ACTIVATION_AVAILABILITY
    }

    template = get_template('email/activation.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject='Your account has been created',
        body=content,
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()


