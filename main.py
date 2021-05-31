import mailAutomation_dir.controllers.mail_controller


def start():
    main = mailAutomation_dir.controllers.mail_controller.MailBot()
    main.run()


if __name__ == '__main__':
    start()