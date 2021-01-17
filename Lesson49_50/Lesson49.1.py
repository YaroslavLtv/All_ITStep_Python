class Car:
    message1 = "Start engine"

    def start(self):
        message2 = "Start car"  # Доступу до message2 ззовні немає,
        # бо message2 поза областю видимості (в локальній області функції)
        # треба звертатися до методу start
        return message2


car1 = Car()
print(car1.message1)
print(car1.start())
