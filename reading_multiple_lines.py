with open('emails.txt', 'r') as emails:
    emails = emails.readlines()

for email in emails:
    if "yahoo" in email:
        print(email.rstrip())

#reads the files from emails.txt for emails with the string "yahoo" and print multiple lines of the emails