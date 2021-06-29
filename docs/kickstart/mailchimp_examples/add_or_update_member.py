import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

try:
  client = MailchimpMarketing.Client()
  client.set_config({
    "api_key": "YOUR_API_KEY",
    "server": "YOUR_SERVER_PREFIX"
  })

  response = client.lists.set_list_member("list_id", "subscriber_hash", {
      "email_address": "Rick70@gmail.com",
      "status_if_new": "subscribed",
      "file": file_uri})
  print(response)
except ApiClientError as error:
  print("Error: {}".format(error.text))