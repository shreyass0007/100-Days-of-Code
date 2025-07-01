# import smtplib
# my_email="shreshshende.777@gmail.com"
# password="ywsgnsgssomczuce"
# connection=smtplib.SMTP_SSL("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="shreshshende.999@gmail.com")
# connection.close()

import smtplib

my_email = "shreshshende.777@gmail.com"
password = "ywsgnsgssomczuce"  # This is an app password, right?

# Using SMTP_SSL (port 465) - no need for starttls()
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="shreyasshende.999@gmail.com",
        msg="Subject:Hello\n\nThis is the email body."
    )