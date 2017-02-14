from api.lib.testutils import BaseTestCase
import api.companies.unittest

class TestDeleteCompany(BaseTestCase):
    def test_delete_company(self):
        resp = self.app.delete('/companies/deerwalk',
                             headers={'content-type': 'application/json'})
        self.assertEqual(resp.status_code, 200)
        assert "deerwalk" in resp.data

if __name__ == "__main__":
    api.companies.unittest.main()