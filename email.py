class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


command_line = input()

emails = []
while command_line != 'Stop':
    sender, receiver, content = command_line.split()
    email_info = Email(sender, receiver, content)
    emails.append(email_info)
    command_line = input()

send_emails = [int(digit) for digit in input().split(', ')]

for index in send_emails:
    emails[index].send()

for mail in emails:
    print(mail.get_info())
