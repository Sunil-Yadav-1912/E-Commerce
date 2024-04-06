from models.database_operations import database_operations as database


def index():

    path = "digital-deals/category" 
    success,resp = database().read(path)
    print(resp)
    return success,resp

def Signup(username, password):
    data = {
        "username": username,
        "password": password
    }

    path = "digital-deals/users" 
    resp = database().create(path,data)
    print(resp)
    return 1,resp

def Login(username, password):
    data = {
        "username": username,
        "password": password
    }

    path = "digital-deals/users" 
    success,resp = database().query_data(path,data)

    return success,resp


def category(category):

    path = "digital-deals/category/"+category 
    success,resp = database().read(path)
    print(resp)
    return success,resp