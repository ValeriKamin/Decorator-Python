
def email_notifier(func):
    def wrapper():
        print("Email")
        func()
    return wrapper

def sms_notifier(func):
    def wrapper():
        func()
        print("SMS")
    return wrapper

@email_notifier
@sms_notifier
def notify():
    print("Povidomlena")

notify()