actual_password = "MondayTuesdayWednesday"
guess_password = ""

while guess_password != actual_password:
    guess_password = input("Input your password: ")
    if actual_password == guess_password:
        print("Account accessed.")
    else:
        print("Your password is incorrect.")