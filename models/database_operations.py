from models.connection import Connection 

class database_operations:
    def create(self, path, data):
        """
        Create a document in Firebase Realtime Database.
        :param collection_name: Name of the collection (path)
        :param data: Data to be stored in the document
        :return: Key of the created document
        """
        db = Connection.get_connection()
        new_ref = db.child(path).push(data)
        return new_ref.key

    def read(self, path):
        """
        Retrieve a document from Firebase Realtime Database.
        :param collection_name: Name of the collection (path)
        :param path: ID of the document to retrieve
        :return: Document data if found, None otherwise
        """
        db = Connection.get_connection()
        snapshot = db.child(path).get()
        if snapshot:
            return 1, snapshot
        else:
            return 0,"Something went wrong"

    def update(self, path, data):
        """
        Update a document in Firebase Realtime Database.
        :param collection_name: Name of the collection (path)
        :param path: ID of the document to update
        :param data: Data to update in the document
        :return: True if update successful, False otherwise
        """
        db = Connection.get_connection()
        # ref = db.reference(collection_name)
        path = "digital-deals/users/users2"
        db.child(path).update(data)
        return True

    def delete(self, path):
        """
        Delete a document from Firebase Realtime Database.
        :param collection_name: Name of the collection (path)
        :param path: ID of the document to delete
        :return: True if delete successful, False otherwise
        """
        db = Connection.get_connection()
        db.child(path).delete()
        return True
    
    def query_data(self,path,data):
        """
        Query data from Firebase Realtime Database.
        :param path: Path to the collection/node in the database
        :param data: Data to query (assuming it has a 'username' field)
        :return: None
        """
        db = Connection.get_connection()
        query = db.child(path).order_by_child('username').equal_to(data['username']).get()
        if len(query) > 0 :
            for key, val in query.items():
                print(key, val)
        else :
            return 0,"User Doesn't Exists"

        return 1,val['username']
