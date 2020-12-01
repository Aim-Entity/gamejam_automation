import smtplib


def email():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()  # Calls the email host

    # Password code (cant be used)
    # # # MODIFY SO IT WORKS ON ANY EMAIL AND CODE
    server.login('bu7861456@gmail.com', 'izzgrprhzzgmzwsi')

    # # # MODIFY SO USER CAN ADD TARGETS
    target = ["bilaluddin474@gmail.com",
              "bilal7861456@gmail.com"]  # List of targets

    # # # MODIFY SO THE SUBJECT AND BODY IS VARIED
    for email in target:
        subject = "Subject goes on top"
        body = f"""
    This is a youtube example 
        """  # No indentation to match the email

        msg = f"Subject: {subject} \n\n{body}"

        server.sendmail(
            'bu7861456@gmail.com',
            email,
            msg
        )

        print(f"Email has been sent to {email}")

    server.quit()
