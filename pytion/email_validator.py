def email_valid(email):
    return "@" in email and "." in email

emails = ["user@example.com", "user@example"]

for email in emails:
    print(f"이메일 주소: {email}")
    if email_valid(email):
        print("유효함")
    else:
        print("유효하지 않음")