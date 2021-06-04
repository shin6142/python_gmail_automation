import os
import schedule
import time
import glob

from mailAutomation_dir.models import mail_automation
from mailAutomation_dir.templates import contents
from mailAutomation_dir import setting


class MailBot(object):
    def __init__(self):
        self.dir_path = contents.attachment_item_dir
        self.config_file = setting.CONFIG_FILE

    def count_file(self):
        file_count = len(os.listdir(self.dir_path))
        return file_count

    def execute_create_config(self):
        c = mail_automation.ConfigClass()
        c.create_config_file()

    def execute_send_mail(self):
        if self.count_file() >= 1:
            c = mail_automation.ConfigClass()
            c.read_config_file()
            mail_bot = mail_automation.AutoMail()
            mail_bot.send_mail()
            mail_bot.remove_dir()
            mail_bot.create_dir()

        elif self.count_file() == 0:
            print('The directory exists, but file does not exist')
        else:
            raise Exception

    def run(self):
        if not os.path.exists(self.config_file):
            self.execute_create_config()
        schedule.every().day.at(contents.send_time).do(self.execute_send_mail)
        while True:
            schedule.run_pending()
            time.sleep(1)


