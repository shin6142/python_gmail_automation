from email.mime import multipart
from email.mime import text
from email.mime.image import MIMEImage
from email.utils import formatdate

import shutil
import smtplib
import configparser
import os
import imghdr

from mailAutomation_dir.templates import contents
from mailAutomation_dir import setting


class ConfigClass(object):
    def __init__(self):
        self.config_file = setting.CONFIG_FILE
        self.gmail_account_name = setting.gmail_account_name
        self.gmail_account_password = setting.gmail_account_password

    def create_config_file(self):
        config = configparser.ConfigParser()
        config['GMAIL_ACCOUNT_INFO'] = {
            'gmail_account_name': self.gmail_account_name,
            'gmail_account_password': self.gmail_account_password
        }
        with open(self.config_file, 'w') as config_file:
            config.write(config_file)
            return config_file

    def read_config_file(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config


class AutoMail(ConfigClass):
    def __init__(self):
        super().__init__()
        self.msg = None
        self.gmail_account_name = self.read_config_file()['GMAIL_ACCOUNT_INFO']['gmail_account_name']
        self.gmail_account_password = self.read_config_file()['GMAIL_ACCOUNT_INFO']['gmail_account_password']
        self.from_email = contents.from_email
        self.to_email = contents.to_email
        self.msg_subject = contents.msg_subject
        self.msg_text = contents.msg_text
        self.attachment_item_dir = contents.attachment_item_dir
        self.attachment_item_name = contents.attachment_item_name

    def add_header(self):
        msg = multipart.MIMEMultipart()
        msg["From"] = self.from_email
        msg["To"] = self.to_email
        msg["Subject"] = self.msg_subject
        msg["Date"] = formatdate(localtime=True)
        return msg

    def add_text(self):
        msg = self.add_header()
        attachment_text = text.MIMEText(self.msg_text, 'html', 'utf-8')
        msg.attach(attachment_text)
        return msg

    def find_image(self):
        attachment_items_list = []
        attachment_items = os.listdir(self.attachment_item_dir)
        for attachment_item in attachment_items:
            image_type = imghdr.what(self.attachment_item_dir + attachment_item)
            if image_type:
                attachment_items_list.append(attachment_item)
        return attachment_items_list

    def add_images(self):
        msg = self.add_text()
        image_list = self.find_image()
        image_name = self.attachment_item_name
        for image in image_list:
            image_path = str(contents.attachment_item_dir + image)
            with open(image_path, 'rb') as f:
                img = f.read()
                image = MIMEImage(img, name=image_name)
                msg.attach(image)
        return msg

    def send_mail(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.gmail_account_name, self.gmail_account_password)
        msg = self.add_images()
        server.send_message(msg)
        server.quit()

    def remove_dir(self):
        shutil.rmtree(self.attachment_item_dir)

    def create_dir(self):
        os.mkdir(self.attachment_item_dir)



