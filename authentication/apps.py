from django.apps import AppConfig
from django.conf import settings

class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender, **kwargs):
            user = kwargs["instance"]
            if kwargs['created']:
                group, ok = Group.objects.get_or_create(name="default")
                group.user_set.add(user)
            post_save.connect(add_to_default_group,
                                sender=settings.AUTH_USER_MODEL)
