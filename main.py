import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "mummaneni.nikhil@gmail.com"
MY_PASSWORD= "vxfxsbpkdmkchmkh"

today = (dt.datetime.now().month,dt.datetime.now().day)

data=pandas.read_csv("birthdays.csv")

birthdays_dict={(data_row.month,data_row.day):data_row for(index,data_row)in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"/Users/nikhilmummaneni/Documents/100 days of code/DAY-32-PROJECT-BIRTHDAY WISHER/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents=letter.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )



