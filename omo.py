
import smtplib
my_email = "mr.huntcon5@gmail.com"
passwd = "gqgi nqqj mbrf rqqf"

connection = smtplib.SMTP("smtp.gmail.com") 
connection.starttls()
connection.login(user= my_email, password= passwd)
connection.sendmail(from_addr= my_email, 
                    to_addrs= "vcthrieearikpo@gmail.com",
                     msg= "subject:HELLO THERE \n\n this is a test msg.")
connection.close()