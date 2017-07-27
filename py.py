import smtplib

host = "smtp.gmail.com"
port =  587
username = "hoangduchuuvn.images@gmail.com"
password =  "********"
from_email = username;
to_list = ["hoangduchuuvn@gmail.com", "example@gmail.com"]

email_conn = smtplib.SMTP(host, port);
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(username, to_list, "hello huu hoang")
email_conn.quit();

from smtplib import SMTP

email_conn2 = smtplib.SMTP(host, port);
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username,password)
email_conn2.sendmail(username, to_list, "hello huu hoang")
email_conn2.quit();
