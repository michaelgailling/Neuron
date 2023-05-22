import pymongo


class DBHandler:
    def __init__(self, db_name: str, default_collection: str):
        """
        This function initializes a MongoDB client and sets the default database and collection to be used.

        :param db_name: The name of the MongoDB database that the client will connect to
        :type db_name: str
        :param default_collection: The default collection is the name of the MongoDB collection that will be used by default
        if no specific collection is specified. A collection in MongoDB is similar to a table in a relational database and
        is used to store documents
        :type default_collection: str
        """
        self._db_name = db_name
        self._col_name = default_collection

        self._client = pymongo.MongoClient("mongodb://localhost:27017/")
        self._db = self._client[db_name]
        self._col = self._db[default_collection]

    @property
    def db_name(self):
        """
        This function returns the value of the private variable `_db_name`.
        :return: The method `db_name` is being defined to return the value of the private attribute `_db_name`.
        """
        return self._db_name

    @db_name.setter
    def db_name(self, val: str):
        """
        This function sets the name of a database and assigns it to a client object.

        :param val: val is a string parameter that represents the name of a database. It is used to set the value of the
        private variable `_db_name` and to access the database using the `_client` object
        :type val: str
        """
        self._db_name = val
        self._db = self._client[val]

    @property
    def col(self):
        """
        This function returns the value of the private variable `_col`.
        :return: The method `col` is being defined for a class, and it returns the value of the private attribute `_col`.
        However, without more context it is difficult to determine what type of object this class is and what the purpose of
        the `col` method is.
        """
        return self._col

    @col.setter
    def col(self, val: str):
        """
        This function sets the name of a column and assigns it to a variable in a database object.

        :param val: val is a parameter of type str that represents the name of a column in a database. This parameter is
        used in the method to set the value of the instance variable _col_name to the value of val and to assign the
        corresponding column in the database to the instance variable _col
        :type val: str
        """
        self._col_name = val
        self._col = self._db[val]

    def select_collection(self, collection: str):
        """
        This function selects a collection in a database and returns it, or returns the default collection if none is
        specified.

        :param collection: The parameter "collection" is a string that represents the name of a MongoDB collection. It is
        used in the method to select a specific collection in the database. If the parameter is None, the method will select
        the default collection specified in the class constructor
        :type collection: str
        :return: a MongoDB collection object. If the input parameter `collection` is `None`, it returns the default
        collection of the current database. If `collection` is not `None`, it returns the collection with the specified
        name. If there is an error, the function returns `None`.
        """
        try:
            if collection is None:
                col = self.col
            else:
                col = self._db[collection]
            return col
        except Exception as e:
            print(e)
            return None

    def insert_record(self, record: dict, collection: str = None):
        """
        This function inserts a record into a specified collection in a MongoDB database and returns the ID of the inserted
        record.

        :param record: A dictionary containing the data to be inserted into the collection
        :type record: dict
        :param collection: The name of the collection in which the record is to be inserted. If no collection is specified,
        the default collection will be used
        :type collection: str
        :return: the inserted ID of the record that was added to the specified collection.
        """
        col = self.select_collection(collection)
        if col is None:
            return None

        res = col.insert_one(record)

        return res.inserted_id

    def find_by_id(self, rec_id: str, collection: str = None):
        """
        This function finds a record by its ID in a specified collection.

        :param rec_id: The ID of the record to be found in the database
        :type rec_id: str
        :param collection: The name of the collection in the database where the record with the given ID will be searched
        for. If no collection is specified, the default collection will be used
        :type collection: str
        :return: the result of the query to find a record with the given ID in the specified collection. The result is a
        cursor object that can be iterated over to access the matching documents.
        """
        col = self.select_collection(collection)
        if col is None:
            return None

        query = {"_id": rec_id}
        res = col.find(query)

        return res

    def update_by_id(self, rec_id: str, updated_rec: dict, collection: str = None):
        """
        This function updates a record in a MongoDB collection by its ID.

        :param rec_id: The ID of the record to be updated
        :type rec_id: str
        :param updated_rec: The updated record is a dictionary containing the new values that you want to update for the
        record with the given ID. The keys of the dictionary should correspond to the field names of the record, and the
        values should be the new values that you want to set for those fields
        :type updated_rec: dict
        :param collection: The name of the collection in the database where the record with the given ID will be updated. If
        no collection is specified, the default collection will be used
        :type collection: str
        :return: the result of the update operation performed on the record with the specified ID in the specified
        collection. The result is a MongoDB UpdateResult object, which contains information about the update operation such
        as the number of documents matched and modified.
        """
        col = self.select_collection(collection)
        if col is None:
            return None

        query = {"_id": rec_id}
        res = col.update_one(query, updated_rec)

        return res

    def delete_by_id(self, rec_id: str, collection: str = None):
        """
        This function deletes a record from a specified collection based on its ID.

        :param rec_id: The ID of the record to be deleted from the collection
        :type rec_id: str
        :param collection: The name of the collection in which the record with the specified ID will be deleted. If no
        collection is specified, the method will try to delete the record from the default collection
        :type collection: str
        :return: the result of the delete operation, which is an instance of the DeleteResult class from the PyMongo
        library. This object contains information about the number of documents deleted and other details about the
        operation.
        """
        col = self.select_collection(collection)
        if col is None:
            return None

        query = {"_id": rec_id}
        res = col.delete_one(query)

        return res


