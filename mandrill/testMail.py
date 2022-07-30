import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError

def run():
  try:
    mailchimp = MailchimpTransactional.Client('YOUR_API_KEY')
    response = mailchimp.users.ping()
    print('API called successfully: {}'.format(response))
  except ApiClientError as error:
    print('An exception occurred: {}'.format(error.text))

run()