# from django.http import HttpResponse
# from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

def check_user(user):
    return not user.is_authenticated

user_logout_required = user_passes_test(check_user, '/', None)

def auth_user_should_not_access(viewfunc):
    return user_logout_required(viewfunc)

# def unauthenticated_user(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect('index')
#         else:
#             return view_func(request, *args, **kwargs)

#     return wrapper_func

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name

#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('No esta autorizado a ver esta pagina')
#         return wrapper_func
#     return decorator


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         if group == 'customer':
#             return redirect('index')

#         if group == 'admin':
#             return view_func(request, *args, **kwargs)

#     return wrapper_function