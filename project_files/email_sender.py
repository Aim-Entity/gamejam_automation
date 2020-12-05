import smtplib


def email():
    try:
        userEmail = input("Enter Your Email: ")
        userAppPassword = input("Enter App Password (https://www.youtube.com/watch?v=RbJ-1VJX-yE): ")
    except smtplib.SMTPAuthenticationError:
        pass
    
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()  # Calls the email host

    # Password code (cant be used)
    # # # MODIFY SO IT WORKS ON ANY EMAIL AND CODE
    server.login(userEmail, userAppPassword)

    # # # MODIFY SO USER CAN ADD TARGETS
    target = []  # List of targets
    stopAdding = ""
    while stopAdding != "N":
        targetUser = input("Enter Target's Gmail: ")
        target.append(targetUser)
        stopAdding = input("Add Another Target? (Y / N): ").upper()
        print("")

    massSubject = input("Enter The Subject Of The Email: ")
    print("")
    massBody = input("Enter The Body Of The Email: ")

    # # # MODIFY SO THE SUBJECT AND BODY IS VARIED
    for email in target:
        subject = massBody
        body = f"""
    {massBody}
        """  # No indentation to match the email

        msg = f"Subject: {subject} \n\n{body}"

        server.sendmail(
            'bu7861456@gmail.com',
            email,
            msg
        )

        print(f"Email has been sent to {email}")

    server.quit()
