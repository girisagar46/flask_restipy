from api.lib.testutils import BaseTestCase
import api.companies.unittest

class TestCreateCompany(BaseTestCase):
    def test_create_company(self):
        resp = self.app.post('/companies',
                             data='{"google": {"name": "Google Inc.", "city": "Mountain View"}}',
                             headers={'content-type': 'application/json'})
        self.assertEqual(resp.status_code, 201)
        assert "apple" not in resp.data
        assert "google" in resp.data

if __name__ == "__main__":
    api.companies.unittest.main()