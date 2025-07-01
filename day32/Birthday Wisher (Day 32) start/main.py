# import smtplib

# my_email = "shreshshende.777@gmail.com"
# password = "ywsgnsgssomczuce"  # This is an app password, right?

# # Using SMTP_SSL (port 465) - no need for starttls()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="shreyasshende.999@gmail.com",
#         msg="Subject:Hello\n\nThis is the email body."
#     )

import datetime as dt
now=dt.datetime.now()
year=now.year
day_of_week=now.weekday()
print(day_of_week)
date_of_birth=dt.datetime(year=1995,month=12,day=15)
print(date_of_birth)

