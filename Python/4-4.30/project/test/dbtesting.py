import sys
import unittest
sys.path.append("C:\\Users\\vinitha.muralidharan\\PycharmProjects\\EmployeeDetails\\src\\main")
import mydbconnection


class TestDatabaseConnection(unittest.TestCase):
    def test_connection_db(self):
        self.assertIsNotNone(mydbconnection.Connect.connection_db('dev'))

    # def test_create_table(self):



if __name__ == '__main__':
    unittest.main()
