from api.lib.testutils import BaseTestCase
import api.companies.unittest

class TestReadCompany(BaseTestCase):
    def test_read_company(self):
        resp = self.app.get('/companies/exponential')
        assert 'Palo Alto' in resp.data

if __name__ == "__main__":
    api.companies.unittest.main()