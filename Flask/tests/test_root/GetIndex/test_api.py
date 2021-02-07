import unittest
import requests

from tests import server, rep
from tests.test_root.GetIndex import api


class TestGetIndex(unittest.TestCase):

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Recipe Deleted.
        """
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        #response_body = response.json()
        print(url)
        print(response.text)
        #print(response_body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], "")
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))


if __name__ == '__main__':
    unittest.main()
