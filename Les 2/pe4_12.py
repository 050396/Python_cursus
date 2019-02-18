oldpassword = input('Voer je oude wachtwoord in:')
newpassword = input('Voer je nieuwe wachtwoord in:')
def new_password (wachtwoord):
    if str(oldpassword) != str(wachtwoord) and len(wachtwoord) >= 6:
        print('True')
    else:
        print('False')
    return new_password
new_password(newpassword)
