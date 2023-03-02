import requests  # εισαγωγή της βιβλιοθήκης
import datetime #Import datetime so you can read the expdate... you're welcome <3

url = input("please insert a url\n")  # προσδιορισμός του url

with requests.get(url) as re:  # το αντικείμενο response
    header = re.headers #read headers
  #  print(header,'\n\n') #print headers

    server = header.get("Server") #read server
    if server != None: #check if server exists in header
        print("Software used:", server , "\n") #print server
    else:
        print("there is no Server in header")

    cookies = re.cookies #read cookies
    if re.cookies : #check if cookies exist
        print("The website uses cookies.\n")
        for i in cookies: #for each cookie
            name = i.name #read the name
            expdate = i.expires #read expiration date
            if expdate != None:
                expdate = datetime.datetime.fromtimestamp(i.expires) #if expdate exists make it readable to human brains
            else:
                expdate = "doesn't expire"
            print("cookie:",name,"expires:",expdate)
        
    else:
        print("The website doesn't use cookies.\n")
