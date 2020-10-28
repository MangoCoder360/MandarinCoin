def connect():
    import pymongo
    client = pymongo.MongoClient("mongodb+srv://MangoCoder360:mangomongo321@cluster0.vtnzz.mongodb.net/CryptoCoin?retryWrites=true&w=majority")
    return client
