from datetime import datetime
#create a spy profile

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#send chat message
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#friend list
spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('A', 'Mr.', 5.1, 27)
friend_two = Spy('B', 'Ms.', 5.3, 21)
friend_three = Spy('C', 'Dr.', 4.9, 37)


friends = [friend_one, friend_two, friend_three]