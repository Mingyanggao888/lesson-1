# first program - Personalized Birthday Wishes

Recipient_s_name = input("What's Recipient's name? ")
Year_of_birth = input("Which Year is the Recipient's birth year? ")
Year_of_birth = int(Year_of_birth)
Personalized_message = input("What personalized message would you like to leave on the card? ")
Sender_s_name = input("What's your name? ")

Current_year = 2023
The_age_of_the_Recipient = Current_year - Year_of_birth

Line1 = ("{}! let's celebrate your {} years of awesomeness!")
Line2 = ("Wishing you a day filled with joy and laughter as you turn {}!")
Line3 = ("{}")
Line4 = ("With love and best wishes,")
Line5 = ("{}")

print(Line1.format(Recipient_s_name, The_age_of_the_Recipient,))
print(Line2.format(The_age_of_the_Recipient,))
print(Line3.format(Personalized_message))
print(Line4)
print(Line5.format(Sender_s_name))