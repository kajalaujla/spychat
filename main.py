print 'Let\'s get started'

spy_name = raw_input('Welcome to spy chat, you must tell me your spy name first: ')

if len(spy_name) > 0:

    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("Should I call you Mister or Miss?: ")

    spy_name = spy_salutation + " " + spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = input("What is your age?")

    spy_age = int(spy_age)

    if spy_age > 12 and spy_age < 50:

        spy_rating = input("What is your spy rating?")
        spy_rating = float(spy_rating)

        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'

        spy_is_online = True

        # This will work, it will not throw an error
        assert instance(spy_name, spy_age)
        print "Authentication complete. Welcome " + spy_name + ' age: ' + spy_age;



    else:
        print 'Sorry you are not of the correct age to be a spy'


else:

    print "A spy needs to have a valid name. Try again please."