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
    success,resp,key = database().query_data_user(path,data)

    return success,resp['username']


def category(category):

    path = "digital-deals/category/"+category 
    success,resp = database().read(path)
    print(resp)
    return success,resp

def showCart(data):
    path = "digital-deals/users"

    success,resp,key = database().query_data_user(path,data)
    print(resp)
    if 'cart' not in resp or len(resp['cart']) == 0:
        return 0,"Your cart is empty."
    return success,resp['cart']

def addToCart(cart_item,data):
    path = "digital-deals/users"

    success,resp,key = database().query_data_user(path,data)

    if success == 1 :
        path = "digital-deals/users/"+key+"/cart" 
        resp = database().create(path,cart_item)
        print(resp)
        return 1,resp
    else:
        return 0,resp

def addToOrders(orders,data):
    path = "digital-deals/users"

    success,resp,key = database().query_data_user(path,data)

    if success == 1 :
        processed_keys = set()

        # Iterate over each order
        for order in orders:
            order_key = order['key']
            if order_key in processed_keys:
                continue  # Skip if the key has already been processed
            processed_keys.add(order_key)

            path = "digital-deals/users/"+key+"/orders" 
            create = database().create(path,order)

            print(create)

            path = "digital-deals/users/"+key+"/cart" 
            delete = database().delete_by_key(path,order_key)

            print(delete)
            
        return 1,"success"
    else:
        return 0,"Failed"
    

