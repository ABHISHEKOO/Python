def create_letter():
    """Create a letter based o user input"""

#Get user input 
f = open("letter.txt","w")
sender_name = input("Enter your name:")
sender_address = input("Enter your address :")
recipient_name= input("Enter the recipent namer :")
recipent_address = input("Enter the recipent address :")
date = input("Enter the date :")
salutation = input("Enter the salutation :")
body = input("Enter the body of the letter :")
closing = input("enter the closing :")

#format the letter
letter = f"""
{sender_name}
{sender_address}
 
{date}

{recipient_name}
{recipent_address}

{salutation}

{body}

{closing}

{sender_name}
"""
print(letter)

create_letter()

