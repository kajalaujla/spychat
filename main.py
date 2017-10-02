from spy_details import spy_name, spy_salutation, spy_rating, spy_age

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

friends_name = []
friends_age = []
friends_rating = []
friends_is_online = []

print "Hello! lets\'s get started"

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)

def add_status(current_status_message):
    update_status_message = None

    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y' :

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            update_status_message = STATUS_MESSAGES[message_selection -1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if update_status_message:
         print 'Your updated status message is: %s' % (updated_status_message)

    else:
         print 'You did not update your status message'

    return updated_status_message

def add_friend():
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")

    new_name = new_name + " " + new_salutation

    new_age = raw_input("Age?")
    new_age = int(new_age)

    new_rating = raw_input("Spy rating?")
    new_rating = float(new_rating)

    if len(new_name) > 0 and new_age > 12 and new_rating >= spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

     return len(friends_name)

def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:
        print "Authentication complete. Welcome " + spy_name + "age:" + str(spy_age) + " and rating of: " + str( spy_rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read secret message"
            menu_choice = int(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the crrect age to be spy'

if existing == "Y":
    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name =raw_input("Welcome to spy chat, you must tell me yur spy name first: ")

    if len(spy_name) > 0:
        spy_salutation =input("Should I call you Mr. or Ms.?: ")

        spy_age = input("What is your age?")

        spy_rating = input("What is your spy rating?")

        spy_is_online = True