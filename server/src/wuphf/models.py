from django.db import models
from wuphf.sinks import phone_call, text_message


class WuphfReceiver(models.Model):
    """Class for representing a person who can receive a wuphf"""
    name = models.CharField(max_length=50)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    cell_phone = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    printer = models.CharField(max_length=250, null=True, blank=True)
    desktop_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def call_home_phone(self, sender, message):
        """Calls the home phone if available"""
        if self.home_phone:
            phone_call.call(sender, message, self.home_phone)

    def call_cell_phone(self, sender, message):
        """Calls the cell phone if available"""
        if self.cell_phone:
            phone_call.call(sender, message, self.cell_phone)

    def text_cell_phone(self, sender, message):
        """Texts the cell phone if available"""
        if self.cell_phone:
            text_message.send_sms(sender, message, self.cell_phone)


class Wuphf(models.Model):
    """Class for representing a person who can receive a wuphf"""
    sender = models.CharField(max_length=50)
    message = models.CharField(max_length=100, null=True, blank=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.message
