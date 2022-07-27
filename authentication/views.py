# from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q

from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, SetPasswordForm, PasswordResetForm
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from shop.models import Customer


def index(request):
    return render(request, 'shop/body.html', {'title': 'index'})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(
            request, "Gracias por su confirmación por correo electrónico. Ahora puede iniciar sesión en su cuenta.")
        return redirect('login')
    else:
        messages.error(request, "El enlace de activación no es válido!")

    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject = "Activar cuenta Tecnoelectro Comercio Online"
    message = render_to_string("authentication/activate.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Estimado {user}, vaya a la bandeja de entrada de su correo electrónico: {to_email}y haga clic en \
                recibido el enlace de activación para confirmar y completar el registro. Nota: Revisa tu carpeta de spam.')
    else:
        messages.error(
            request, f'Problema al enviar correo electrónico a {to_email}, verifica si lo escribiste correctamente.')

# send user a forgot password containing a nonce
# subject = 'Reset Password'
# user = some_user_object
# nonce = some_nonce_value

# template_content = []
# message = {
#     'from_email': 'info@sample.com',
#     'from_name': 'Robot',
#     'subject': subject,
#     'to': [{'email': user.email, 'name': user.get_full_name()},],
#     'global_merge_vars': [
#         {'name':'SUBJECT', 'content': subject},
#         {'name':'USER_NAME', 'content': user.first_name},
#         {'name':'NONCE', 'content': nonce},
#         # etc etc
#     ],
# }
# mail = MandrillTemplateMail("Password Reset", template_content, message)
# mail.send()


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # Customer.objects.create(
            #     user=user,
            #     # username=user.username,
            #     email=user.email
            # )
            # Customer.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('index')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="authentication/register.html",
        context={"form": form}
    )


@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Cerrar sesión con éxito!")
    return redirect("index")


@user_not_authenticated
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Hola <b>{user}</b>! has iniciado sesión")
                return redirect("index")

        # else:
        #     for key, error in list(form.errors.items()):
        #         if key == 'captcha' and error[0] == 'This field is required.':
        #             messages.error(request, "You must pass the reCAPTCHA test")
        #             continue

                # messages.error(request, error)

    form = UserLoginForm()

    return render(
        request=request,
        template_name="authentication/login.html",
        context={"form": form}
    )


def profile(request, username):
    Customer.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(
                request, f'{user_form.username}, Tu perfil ha sido actualizado!')
            return redirect("profile", user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        form.fields['description'].widget.attrs = {'rows': 1}
        return render(
            request=request,
            template_name="authentication/profile.html",
            context={"form": form}
        )

    return redirect("index")


@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu contraseña ha sido cambiada")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})


@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[
                                     associated_user.email])
                if email.send():
                    messages.success(request,
                                     """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            Le hemos enviado instrucciones por correo electrónico para establecer su contraseña, si existe una cuenta con el correo electrónico que ingresó.
                            Debería recibirlos en breve.<br>Si no recibe un correo electrónico, asegúrese de haber ingresado la dirección
                            con el que te registraste y revisa tu carpeta de correo no deseado.
                        </p>
                        """
                                     )
                else:
                    messages.error(
                        request, "Problema al enviar el correo electrónico de restablecimiento de contraseña, <b>PROBLEMA DEL SERVIDOR</b>")

            return redirect('index')

        # for key, error in list(form.errors.items()):
        #     if key == 'captcha' and error[0] == 'This field is required.':
        #         messages.error(request, "You must pass the reCAPTCHA test")
        #         continue

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="authentication/password_reset.html",
        context={"form": form}
    )


def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Se ha establecido su contraseña. Puede continuar e <b>iniciar sesión</b> ahora")
                return redirect('index')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Enlace ha expirado")

    messages.error(request, 'Algo salió mal, redirigir de nuevo al inicio')
    return redirect("index")
