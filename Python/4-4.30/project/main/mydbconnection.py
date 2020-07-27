"""Main production file"""
import csv
import sys
import os
import mysql.connector
import devconfig
import loghandler


class Connect:
    """
    Class to establish the connection to the database
    """
    def connection_db(env):
        """

        :return:
        Returns the connector variable
        """
        try:
            host, user, password, db1 = devconfig.connect(env)
            db = mysql.connector.connect(host=host, user=user, password=password, db=db1)
            # logger.info("Database connection established {}@{} with password {}".format
            #             (user, host, '*'*len(password)))
            return db
        except Exception as error:
            print(error)


class EmployeeDetails:
    """
    Class to define all the DDL statement in SQL
    """
    def __init__(self, db1, logger):
        self.db = db1
        self.logger = logger
        self.cursor = db1.cursor()

    def file_path(self):
        """

        :return:
        Returns the path to the DDL folder
        """
        try:
            folder_path = os.getcwd()
            file_path = os.path.join('\\'.join(folder_path.split('\\')[:-1]), 'files')
            self.logger.info("Path of the DDL folder is fetched")
            return file_path
        except FileNotFoundError as error:
            print(error)
        except Exception as error:
            print(error)
            self.logger.exception("Exception occurred!!!")

    def create_table(self):
        """

        :param
         name: name of the table to create
        :return:
        return the function to insert values into the table
        """
        try:
            file_path1 = self.file_path()
            for filename in os.listdir(file_path1):
                if filename.split('.')[1] == 'txt':
                    file_open = open(os.path.join(file_path1, filename))
                    lines = file_open.read().split(';')
                    self.cursor.execute(lines[0])
                    self.db.commit()
                    self.logger.info(filename.split('.')[0]+" table created")
            self.logger.info("Table creation completed!!")
        except Exception as error:
            print(error)
        self.insert_db()

    def insert_db(self):
        """
        :return:
        A function to fetch records from CSV and put it into the database
        """

        try:
            file_path1 = self.file_path()
            self.cursor.execute("SELECT table_name FROM information_schema.tables"
                                " WHERE table_schema='mymodel'")
            table_name = self.cursor.fetchall()
            table_names = []
            for i in table_name:
                for j in i:
                    table_names.append(j)
            num1 = len(table_names)
            for i in range(num1):
                for filename in os.listdir(file_path1):
                    if filename.split('.')[1] == 'csv' and filename.split('.')[0] == table_names[i]:
                        self.cursor.execute("SELECT column_name FROM information_schema.columns"
                                            " where table_schema='mymodel' and table_name='{}'".format(table_names[i]))
                        len_ins = self.cursor.fetchall()
                        ins_len = len(len_ins)
                        file_open = open(os.path.join(file_path1, filename))
                        data = csv.reader(file_open)
                        for datas in data:
                            self.cursor.execute("INSERT INTO {} VALUES ({})".
                                                format(table_names[i], ','.join(['%s' for num in range(ins_len)])), datas)
                            self.db.commit()
                        self.logger.info("Values inserted in table - "+ filename.split('.')[0])
            self.logger.info("Insertion completed!!")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    logger = loghandler.logfile()
    envi = sys.argv[1]

    db1 = Connect.connection_db(envi)
    c_obj = EmployeeDetails(db1, logger)
    c_obj.create_table()