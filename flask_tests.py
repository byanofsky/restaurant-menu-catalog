import os
import final_project
import unittest
import tempfile


class final_projectTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, final_project.app.config['DATABASE'] = tempfile.mkstemp()
        final_project.app.config['TESTING'] = True
        self.app = final_project.app.test_client()
        with final_project.app.app_context():
            # final_project.init_db()
            pass

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(final_project.app.config['DATABASE'])

    def test_routing(self):
        rv = self.app.get('/')
        assert b'All Restaurants' in rv.data
        rv = self.app.get('/restaurants/')
        assert b'All Restaurants' in rv.data
        rv = self.app.get('/restaurant/1/')
        assert b'<h1>Blue Burgers</h1>' in rv.data
        rv = self.app.get('/restaurant/new/')
        assert b'New Restaurant' in rv.data
        rv = self.app.get('/restaurant/1/edit/')
        assert b'<h1>Edit Blue Burgers</h1>' in rv.data
        rv = self.app.get('/restaurant/1/delete/')
        assert b'Are you sure you\'d like to delete "Blue Burgers"?' in rv.data
        rv = self.app.get('/restaurant/1/menu/new/')
        assert b"<h1>New Menu Item</h1>" in rv.data
        rv = self.app.get('/restaurant/1/menu/1/edit/')
        assert b"<h1>Edit Chocolate Cake</h1>" in rv.data
        rv = self.app.get('/restaurant/1/menu/1/delete/')
        assert b"Are you sure you'd like to delete \"Chocolate Cake\"?" in rv.data


if __name__ == '__main__':
    unittest.main()
