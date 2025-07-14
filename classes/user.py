from apps.auth.utils import *

def get_ticket():
    """
    user vaqtini, joy sonini o'zi belgilaydi. Bunda time.csvga tushadigan vaqtdan userga nechtadir joy beriladi.orders.csvga append
    U vaqtga joy yo'q bo'lsa avtomatik boshqa bo'sh joyni taklif qilib beriladi.
    Tanlaganidan keyin o'sha vaqtdagi joylar sonidan nechta son kiritgan bo'lsa shuncha ayriladi va orders.csvga append
    tanlagan vaqti,soni haqida info

    :return:
    """
    time = input("what time would you like to have a lunch? Choose from 11 am to 3 pm: ")
    seats = int(input("how many seats do you want to book: "))
    times = read("time")

    for t in times:
        if t[-1] != seats:
            print("Seats for this time are not available, please choose another time")









def show_time():
    pass

def show_all():
    pass