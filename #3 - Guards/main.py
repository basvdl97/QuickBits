













def main():
    
    # describe a user
    user = {
        'name': "Stephan",
        'age': 28,
        'banned': False,
        'ban_reason': None,
        'balance': 100
    }

    # guard banned users
    if user['banned']:
        kick_from_casino(user)

    # guard for names not starting with an s
    if not user['name'].lower()[0] == 's':
        kick_from_casino(user)

    # guard for the age
    if user['age'] < 18:
        kick_from_casino(user)

    # guard user balnce
    if user['balance'] <= 0:
        kick_from_casino(user)

    # if user passed all guards let in casino
    let_user_inside_casino(user)

    













def let_user_inside_casino(user):
    pass

def kick_from_casino(user):
    pass

if __name__ == "__main__":
    main()