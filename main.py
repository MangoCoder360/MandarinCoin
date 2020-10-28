import dbConnect, easygui, random
client = dbConnect.connect()
db = client["CryptoCoin"]
users = db["Users"]
chs0 = ["Sign in to an existing account", "Create an account"]
answer = easygui.buttonbox('Welcome to MandarinCoin, please choose a option to get started', choices = chs0)
if answer == "Create an account":
    username = easygui.enterbox('Please choose a username for your account')
    users.insert_one({"username":username, "balance":1})
    easygui.msgbox("Your account has been created!")
if answer == "Sign in to an existing account":
    username = easygui.enterbox('Please enter your username')
    user = users.find_one({"username":username})
    user = user["username"]
chs1 = ['Mine some MandarinCoin', 'Exit', 'Check balance']
answer = easygui.buttonbox('What would you like to do today?', choices = chs1)
if answer == "Check balance":
    balance = users.find_one({"username":username})
    balance = balance["balance"]
    balance = str(balance)
    easygui.msgbox('You balance is: ' + balance + " MandarinCoins")
if answer == "Mine some MandarinCoin":
    rand = random.radint(0,5)
    #WIP
