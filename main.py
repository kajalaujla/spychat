from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography


STATUS_MESSAGE = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

print 'Let\'s get started'

question = "Do you want to continue as " + spy.salutation + " " + spy.name + "[Y/N]? "
existing = raw_input(question)


def add_status(current_status_message):
    updated_status_message = None
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("what status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGE.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGE:
            print '%d,%s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\n Choose from the above messages"))

        if len(STATUS_MESSAGE) >= message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection - 1]

        else:
            print 'The option you chose is not valid!Press either y or n.'

        if updated_status_message:
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print 'You did not update your status message'

        return updated_status_message

    def add_friend():
        new_friend = Spy('', '', 0, 0.0)

        new_friend.name = raw_input("Please add your friend's name: ")
        new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
        new_friend.name = new_friend.salutation + " " + new_friend.name

        new_friend.age = raw_input("Age?")
        new_age = int(new_friend.age)

        new_friend.rating = raw_input("Spy rating?")
        new_friend.rating = float(new_friend.rating)

        if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
            friends.append(new_friend)
            print 'Friend Added!'
            print friends
        else:
            print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

        return len(friends)

    def select_friend():
        item_number = 0

        for friend in friends:
            print '%d.%s aged %d with rating %.2f is online' % (
            item_number + 1, friend.salutation, friend.name, friend.age, friend.rating)

            item_number = item_number + 1
        friend_choice = raw_input("Choose from your friends")
        friend_choice_position = int(friend_choice) - 1
        return friend_choice_position

    def send_message():
        friend_choice = select_friend()

        original_image = raw_input('What is the name of the image?')
        if len(original_image) == 0:
            print 'Invalid Image Path'
        else:

            output_path = 'C:\Users\admin\PycharmProjects\spycht\output.jpg'
            text = raw_input("What do you want to spy?")
            Steganography.encode(original_image, output_path, text)
            new_chat = ChatMessage(text, True)
            friends[friend_choice].chats.append(new_chat)
            print 'Your secret message image is ready !'
            print friends

    def read_message():
        sender = select_friend()

        output_path = raw_input("What is the name of the file?")
        secret_text = Steganography.decode(output_path)
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chat.append(new_chat)

        if len(secret_text) == 0:
            print 'Sorry ! no secret message to be displayed'
        elif secret_text.upper() == 'SOS':
            print 'Emergency'
        elif secret_text.upper() == 'SAVE ME' or secret_text.upper() == 'SAVEME':
            print 'Hold On'
        elif len(secret_text) > 100:
            friends.remove(friends[sender])
            print 'Spy is removed!!'
        else:
            print secret_text

    def read_chat_history():
        read_for = select_friend()

        for chat in friends[read_for].chats:
            if chat.send_by_me:
                print '[%s] %s: %s' % (chat.time.strftime, ('you_said').chat.message)

            else:
                print '[%s] %s: %s' % (chat.time.strftime , (friends[read_for].name), chat.message)

    def start_chat(spy):


        current_status_message = None

        if spy.age > 12 and spy.age < 50:
            print "Authentication complete.welcome " + spy.name + " age: " + str(
                spy.age) + " and rating of:" + str(spy.rating) + "proud to have you on board "

            show_menu = True


        while show_menu:
                menu_choices = "What do you want to do? \n 1. Add a status update \n2. Add a friend\n3. Send a secret message \n4. Read a secret message \n5. Read chats from a user \n6. Close Application\n"
                menu_choice = raw_input(menu_choices)

                if len(menu_choice) > 0:
                    menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()

                else:
                    show_menu = False
                    print 'Invalid selection'


        else:
            print 'Sorry you are not of the correct age to be a spy'

    if existing == "Y":
        start_chat(Spy)
    else:
        spy = Spy('', '', 0, 0.0)

        spy.name = raw_input('Welcome to spy chat, you must tell me your spy name first: ')

        if len(spy.name) > 0:
            spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

            spy.age = raw_input("What is your age?")
            spy.age = int(spy.age)

            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)

            start_chat(spy)

        else:
            print 'Please add a valid spy name'
