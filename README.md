# python_gmail_automation

###Note: This project is for python practice purpose.

##Overview
- [Introduction](#introduction)
- [Technical overview](#Technical Overview)
- [Usage](#Usage) 
- [How it works](#How it works)
- [Background (Why this project was build)](#Background(Why this project was build))

##Introduction
###This program automates a fixed email submission with images(png).
* If you need to send a fixed email regularly, for example reports to the company at the beginning 
  or the end oof working hour, this system will help reduce your repetitive work.
![readme01](https://user-images.githubusercontent.com/62780815/120142817-ec569400-c219-11eb-94e5-14f28e14dd5d.png)
![スクリーンショット 2021-05-31 14 14 09](https://user-images.githubusercontent.com/62780815/120143113-7bfc4280-c21a-11eb-8cc2-95b17a553d18.png)

##Technical overview
* Language
  - Python 3.8.5
* API 
  - Gmail API
* Development environment
  - Pycharm Professional
  
### File tree
<pre>
.
├── README.md
├── config.ini
├── mailAutomation_dir
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── setting.cpython-38.pyc
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── mail_controller.cpython-38.pyc
│   │   └── mail_controller.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── mail_automation.cpython-38.pyc
│   │   └── mail_automation.py
│   ├── setting.py
│   └── templates
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-38.pyc
│       │   └── contents.cpython-38.pyc
│       └── contents.py
└── main.py


</pre>
##Usage
1. Create Directory to save images that you attach to the email, and put any images in the directory.
2. Go to /mailAutomation_dir/setting.py and set your gmail_account_name and gmail_account_password.
3. Go to /mailAutomation_dir/templates/contents.py and set the contents of the email, path for the directory that has the attachment image, and set the time when the email is automatically sent.
4. Run /mailAutomation_dir/main.py so that the system is executed.

##How it works
1. While /mailAutomation_dir/main.py is running, the email is automatically submitted when the time set in /mailAutomation_dir/templates/contents.py.
   * If any file exist in the dir, the submission executed.   
2. The images attached to the email are automatically removed from its directory after the automatic submission.
##Background(Why this project was build)
* Problems 
  * I have to send an e-mail at the end of the work.
  The email is fixed sentences, so I have typed same sentences every time.
  * An attachment file is an anomalous part in the e-mails. In my case, the file is a screenshot
* Solutions
  * I want to automate the email submission.
  * I do not want to send an email without any attachment.
  * Once the email is successfully submitted, I want to remove the attachment file from the directory.
