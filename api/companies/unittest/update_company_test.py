from api.lib.testutils import BaseTestCase
import api.companies.unittest


class TestUpdateCompany(BaseTestCase):
    def test_update_company(self):
        resp = self.app.put('/companies/exponential',
                             data='{"name": "Exponential.io", "city": "Menlo Park"}',
                             headers={'content-type':'application/json'})
        self.assertEqual(resp.status_code, 200)
        assert 'Palo Alto' not in resp.data
        assert 'Menlo Park' in resp.data


if __name__ == "__main__":
    api.companies.unittest.main()