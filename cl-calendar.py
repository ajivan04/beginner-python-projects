# This program will be an event calendar that will allow the user to: view an event, add an event to the calendar, update an existing event, or delete an existing event. The program will not terminate unless the user decides to exit. 

from time import sleep, strftime

USER_NAME = "Abbas"

calendar = {

}

def welcome():
  print("Welcome " + USER_NAME)
  print("The calendar is opening...")
  sleep(1)
  print("Toady is " + strftime("%A %B %d, %Y"))
  print("The time is " + strftime("%H: %M: %S"))
  sleep(1)
  print("What would you like to do?")

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("The calendar is empty.")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print("Your event has been added to the calendar.")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10) or int(date[6:] < int(strftime("%Y"))):
        print("Invalid date!")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else: 
        calendar[date] = event
        print("New event has been successfully added to the calendar!")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("Calendar is empty.")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("Event successfully deleted!")
            print(calendar)
          else:
            print("Incorrect event entered.")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid Command.")
      start = False


start_calendar()
