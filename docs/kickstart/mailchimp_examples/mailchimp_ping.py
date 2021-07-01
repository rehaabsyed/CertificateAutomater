from mailchimp_marketing import Client

mailchimp = Client()
mailchimp.set_config({
  "api_key": "YOUR_API_KEY",
  "server": "YOUR_SERVER_PREFIX"
})

response = mailchimp.ping.get()
print(response)