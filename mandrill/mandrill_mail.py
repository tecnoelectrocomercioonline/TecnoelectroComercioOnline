from django_mandrill.mail import MandrillTemplateMail
# import mandrill

# m = mandrill.Mandrill('YOUR_API_KEY')
# print m.users.ping()


def send_mandrill_email(template_name, email_to, context=None, curr_site=None):
    if context is None:
        context = {}
    message = {
        'to': [],
        'global_merge_vars': []
    }
    for em in email_to:
        message['to'].append({'email': em})

    for k, v in context.items():
        message['global_merge_vars'].append(
            {'name': k, 'content': v}
        )
    MandrillTemplateMail(template_name, [], message).send()


send_mandrill_email(
    'template-1', ["sendto@email.com"], context={'Name': "Test User"})
