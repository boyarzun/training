from abc import ABC, abstractmethod
from typing import List

"""
Following DIP
Dependency Inversion Principle

In this example, the EmailSenderInterface class represents the abstraction or interface
for sending emails. The SmtpEmailSender class is a concrete implementation of the
EmailSenderInterface that sends emails using SMTP. The EmailService class depends on the
EmailSenderInterface abstraction instead of the concrete SmtpEmailSender implementation.
This allows for the EmailService class to be decoupled from the specific implementation
details of sending emails and makes it easier to swap out different email sending
implementations in the future.
"""


class EmailSenderInterface(ABC):
    @abstractmethod
    def send(self, to_address: str, subject: str, body: str) -> bool:
        pass


class SmtpEmailSender(EmailSenderInterface):
    def __init__(self, smtp_host: str, smtp_port: int):
        self._smtp_host = smtp_host
        self._smtp_port = smtp_port

    def send(self, to_address: str, subject: str, body: str) -> bool:
        # Code to send email using SMTP
        return True


class EmailService:
    def __init__(self, email_sender: EmailSenderInterface):
        self._email_sender = email_sender

    def send_email(self, to_address: str, subject: str, body: str) -> bool:
        return self._email_sender.send(to_address, subject, body)


# Example usage
smtp_email_sender = SmtpEmailSender(smtp_host="smtp.gmail.com", smtp_port=587)
email_service = EmailService(email_sender=smtp_email_sender)
email_service.send_email(
    to_address="example@example.com", subject="Test Email", body="Hello, World!"
)

"""
NOT Following DIP
Dependency Inversion Principle


In this example, the EmailService class depends directly on the SmtpEmailSender concrete
implementation instead of depending on the EmailSenderInterface abstraction. This makes
the EmailService class tightly coupled to the specific implementation details of sending
emails using SMTP. This violates the Dependency Inversion Principle because the high-level
module (EmailService) depends on the low-level module (SmtpEmailSender) and is tightly
coupled to it. This can make it more difficult to swap out different email sending
implementations in the future.
"""


class SmtpEmailSender:
    def __init__(self, smtp_host: str, smtp_port: int):
        self._smtp_host = smtp_host
        self._smtp_port = smtp_port

    def send_email(self, to_address: str, subject: str, body: str) -> bool:
        # Code to send email using SMTP
        return True


class EmailService:
    def __init__(self):
        self._email_sender = SmtpEmailSender(smtp_host="smtp.gmail.com", smtp_port=587)

    def send_email(self, to_address: str, subject: str, body: str) -> bool:
        return self._email_sender.send_email(to_address, subject, body)


# Example usage
email_service = EmailService()
email_service.send_email(
    to_address="example@example.com", subject="Test Email", body="Hello, World!"
)
