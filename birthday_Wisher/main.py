from calendar import month
from datetime import datetime
import pandas
import random
import smtplib

from pandas.core.arrays.categorical import contains

today = datetime.now()
today_tuple =(today.month,today.day)
data = pandas.read_csv("birthdays.csv")
for index, data_row in data.iterrows():
    if today.month == data_row["month"] and today.day == data_row["day"]:
        file_template_path= f"letter_{random.randint(1,3)}.txt"
        try:
            with open(file_template_path) as letter_file:
                content = letter_file.read()
                content = content.replace("[name]",data_row["name"])
        except Exception as e:
            print(e)
        try:
            with smtplib.SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login("testemail12344123123@gmail.com","fzfx ldli wzxn ccfx")
                connection.sendmail(from_addr="testemail12344123123@gmail.com",to_addrs=data_row["email"], msg=f"Subject:Happy Birthday!\n\n{content}")
        except Exception as e:
            print(e)