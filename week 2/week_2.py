from datetime import datetime
import os

total_fee=0    # total vehicles of the day
fee=0          #for each vehicle
discount=0
check_number=0
check_digit=0
extra_hour=0
current_day=''
current_time=0
p_hour=0

def start():
    global p_hour
    # current date and time
    current_datetime = datetime.now()
    # Extracting the current day and time
    current_day = current_datetime.strftime("%A")  # Day of the week
    current_time = current_datetime.hour  # Time in HH format of type int
    print("Current Day :", current_day)
    print("Current Time:", current_time)
    p_hour=int(input('***enter number of hours to be parked: *** '))
    print('\n\n')

def check_modulo(check_number):
    thousands=(check_number%1000)
    hundreds=(check_number//100)%10
    tens=(check_number//10)%10
    ones=check_number%10
    check_digit=(5*ones+4*tens+3*hundreds+2*thousands)%11  #11 modulo with a complex algoritham a bit difficult to guess
    return check_digit

def fee_calculate():
    #task 3 extension
    global p_hour, current_time, current_day, fee, extra_hour
    if current_time+p_hour>16:
        extra_hour=(current_time+p_hour)-16  #seprating hour after 16:00 to decrease charges
        p_hour-=extra_hour                   #it will limit that we only charge for hour befor 16:00


    if current_time>=8 and current_time<=16:
        if current_day=='Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday':
            if p_hour<=2:
                fee=10*p_hour
            else:
                print('       !!! you entered invalid timespace!!!\n!!! so we decided to allow you the mximum permitted time !!!\n\n')
                fee=2*10
        elif current_day=='Sunday':
            if p_hour<=8:
                fee=2*p_hour
            else:
                print('       !!! you entered invalid timespace!!!\n!!! so we decided to allow you the mximum permitted time !!!\n\n')
                fee=2*8
        else:
            if p_hour<=4:
                fee=p_hour*3
            else:
                print('       !!! you entered invalid timespace!!!\n!!! so we decided to allow you the mximum permitted time !!!\n\n')
                fee=2*4

    elif current_time>=16:
         fee=2*p_hour

    else:
        print('!!! during this time parking is not allowed !!!\n\n')


    fee=fee+extra_hour*2

#allocating discount based on check number
def discount_parking():
    global fee,discount
    check_number=int(input('\n\nenter frequent parking number : '))
    check_digit=int(input('enter cross check digit : '))  
    if check_modulo(check_number)==check_digit:
        if current_time>=16:
            discount=fee/2
            fee-=discount
            print('!!! 50% of discounted allocated !!!')
        else:
            discount=fee/10
            fee-=discount
            print('!!! 10% of discounted allocated !!!')
    else:
        print('!!! no discount allocated !!!\n\n')
    fee=int(fee)
    print('your parking fee is : ',fee)


def display():
    global fee,total_fee
    pay=int(input('enter amount to send (change not available) : '))
    if pay>=fee:
        total_fee+=fee
        print('!!! Parking fee payed successfully !!!')
    else:
        print('!!! Transaction failed !!!\n***try raising fee***\n')

    print('\n\nday     : ',current_day,'\nParking hour: ',current_time,'\nParked hour : ',p_hour,'\nparking fee : ',fee,'\nDiscount    : ',discount,'\n\n')

while True:
    os.system('cls')
    num=int(input('enter 0 to stop (otherwise continues) : '))
    if num==0:
        break;
    start()
    fee_calculate()
    discount_parking()
    display()

print('\n\n***Total parking fee of ',current_day,' is ',total_fee)