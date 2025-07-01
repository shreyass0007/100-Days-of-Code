import smtplib
import random
import datetime as dt

my_email = "shreshshende.777@gmail.com"
password = "ywsgnsgssomczuce"  # This is an app password, right?

now=dt.datetime.now()
day_of_week=now.weekday()
print(day_of_week)

def get_quote():
    with open("day32/Birthday Wisher (Day 32) start/quotes.txt") as file:
        lines=file.readlines()
        quote=random.choice(lines)
        return quote

quote=get_quote()
print(quote)
# Using SMTP_SSL (port 465) - no need for starttls()
if day_of_week==1:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="shreyasshende.999@gmail.com",
            msg=f"Subject:Hello\n\n{quote}."
        )



