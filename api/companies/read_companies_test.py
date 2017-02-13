from api.lib.testutils import BaseTestCase
import unittest

class TestReadCompanies(BaseTestCase):
    def test_read_companies(self):
        resp = self.app.get("/companies")
        assert "exponential" in resp.data

if __name__ == "__main__":
    unittest.main()