### 🐍 Додаткова реалізація Decorator на Python

```python
def email_notifier(func):
    def wrapper():
        print("Надіслано email.")
        func()
    return wrapper

def sms_notifier(func):
    def wrapper():
        func()
        print("Надіслано SMS.")
    return wrapper

@email_notifier
@sms_notifier
def notify():
    print("Основне повідомлення.")

notify()
