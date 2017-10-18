from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
import csv
from termcolor import colored

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

SPECIAL_WORDS = ['SOS', 'SAVE ME', 'NEED HELP']
new_friend = Spy('', '', 0, 0.0)


def add_status(current_status_message):
    if current_status_message != None:
        print 'Your current status message is %s \n' + current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("what status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d.%s' % (item_position, message)
            item_position = item_position + 1

        message_selection = raw_input("\n Choose from the above messages")

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

        else:
            print 'You did not update your status message'

        if updated_status_message:
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print 'please tell your status'

        return updated_status_message

    def add_friend():

        new_friend.name = raw_input("Please add your friend's name: ")
        new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

        new_friend.age = raw_input("Age?")

        new_friend.rating = raw_input("Spy rating?")

        if new_friend.age > 12 and new_friend.rating >= 4 and len(new_friend.name) > 0:
            friends.append(new_friend)
            with open('friends.csv', 'b') as friends_data:
                writer = csv.writer(friends_data)
                writer.writerow(
                    [new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, new_friend.is_online])

            print 'Friend Added!'

        else:
            print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
        new_friend.name = new_friend.salutation + " " + new_friend.name

        return len(friends)

    def load_friends():
        with open('friends.csv', 'rb') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                # spy = Spy(row[1],row[2],row[2], row[4])
                print row
                # friends.append(new_friend)

    print 'Lets started'
    print 'Welcome to spychat'
    question = "Continue as " + spy.salutation + " " + spy.name + "(Y/N)?"
    existing = raw_input(question)

    def select_a_friend():
        friend_item_number = 0

        for friend in friends:
            print '%d %s aged %d with rating %2f is online' % (
                friend_item_number + 1, friend.salutation, friend.name, friend.age, friend.rating)

            friend_item_number = friend_item_number + 1
        friend_choice = raw_input("Choose from your friends")
        friend_choice_position = friend_choice - 1
        return friend_choice_position

    def send_message():
        friend_choice = select_a_friend()

        original_image = raw_input('What is the name of the image?')
        output_path = 'C:\Users\admin\PycharmProjects\spycht\output.jpg'
        text = raw_input("What do you want to spy?")
        with open('chats.csv', 'b') as chats_data:
            writer = csv.writer(chats_data)
            writer.writerow([text, datetime.now()])
        Steganography.encode(original_image, output_path, text)
        new_chat = ChatMessage(text, True)
        print 'Secret message is ready'
        friends[friend_choice].chats.append(new_chat)

    def load_chats():
        with open('friends.csv', 'rb') as chats_data:
            reader = csv.reader(chats_data)
            for row in reader:
                # spy = Spy(row[1],row[2],row[2], row[4])
                print row

    def read_message():
        sender = select_a_friend()

        output_path = raw_input("What is the name of the file?")
        secret_text = Steganography.decode(output_path)
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chat.append(new_chat)
        print 'Sorry ! no secret message to be displayed'
        print secret_text
        text_length = len(secret_text) - secret_text.count(" ")
        if text_length > 100:
            del friends[sender]
            if "save me".upper() in secret_text:
                print "need help"
            if "alert".upper() in secret_text:
                print "be active "
            if "sos".upper() in secret_text:
                print "Emergency call"

    def read_chat_history():
        read_for = select_a_friend()
        print '/n'

        for chat in friends[read_for].chats:
            if chat.sent_by_me:
                print colored('[%s]' % (chat.time.strftime('%d %B %Y')), 'blue')
                print colored('You said:%s' % chat.message, "grey")
            else:
                print colored('[%s]  ' % (chat.time.strftime('%d %B %Y')), "blue")
                print colored('%s' % (friends[read_for].name), "red")
                print colored('%s' % (chat.message), "grey")

    def start_chat(spy):

        current_status_message = None

        if spy.age > 12 and spy.age < 50:
            print "Authentication complete.welcome " + spy.name + " age: " + str(
                spy.age) + " and rating of:" + str(spy.rating) + "proud to have you on board "
            print 'Welcome %s. Nice to  meet u.' % spy.name
            show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n2. Add a friend\n3. Send a secret message \n4. Read a secret message \n5. Read chats from a user \n6. Close Application\n"
            menu_choice = raw_input(menu_choices)

            # if len(menu_choice) > 0:
            # menu_choice = int(menu_choice)

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



        else:
            print 'Sorry you are not of the correct age to be a spy'
            exit()

    if existing.upper() == "Y":
        load_friends()
        load_chats()

        start_chat(Spy)
    elif existing.upper() == "N":
        spy = Spy('', '', 0, 0.0)
        spy.name = raw_input('Welcome to spy chat, you must tell me your spy name first: ')
        if len(spy.name) > 0:

            spy.salutation = raw_input("Should I call you Mister or Miss?: ")
            spy.name = spy.salutation + " " + spy.name

            print 'Alright ' + spy.name + '.I would like to knw little more about you better  '
            spy_age = input('What is your age ?')
            if spy_age > 12 and spy_age < 50:

                print 'you are perfect for a spy'
                if spy.rating >= 4.5:
                    print 'Great Ace'
                elif spy.rating >= 3.5 and spy.rating < 4.5:
                    print 'You are a good one!'
                elif spy.rating >= 2.5 and spy.rating < 3.5:
                    print 'You can always do Better'

                spy_online = True

                start_chat(spy)

                print 'Authentication Completed! Welcome %s Your age is %d and Your Spy Rating is %.1f' % (
                    spy.name, spy.age, spy.rating)

            else:
                print 'tu chhod de moh maya tumse na ho paega '
                exit()
        else:
            print 'Sorry! You are not of correct Age to be a Spy :-('
    else:
        print ' please try with valid name'
