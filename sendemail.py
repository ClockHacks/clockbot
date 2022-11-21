import requests
import random

def sendemail(receiver: str, name: str):
    print('sent email to ' + receiver)
    code = random.randint(11111,99999)

    return requests.post(
		"https://api.mailgun.net/v3/clockhacks.ca/messages",
		auth=("api", "cd1afe9291a9a989a4a6bdc279afedbd-b0ed5083-7493501d"),
		data={"from": "Hello ClockHacks <hello.clockhacks@gmail.ca>",
			"to": receiver,
			"subject": "Confirm your registration",
			"text": f"Hi {name}! Thanks for registering for ClockHacks! Here\'s a code that I generated that doesn\'t do anything!\n\n{code}"})
# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain so you can send 10000 emails/month for free.