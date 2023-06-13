from rest_framework.test import APITestCase


class LogoutRouteTest(APITestCase):
    def test_logout_route(self):
        response = self.client.post("/dj-rest-auth/logout/")

        '''
        response status code is 200 (OK)
        '''
        self.assertEqual(response.status_code, 200)

        '''
        JWT_AUTH_COOKIE and JWT_AUTH_REFRESH_COOKIE cookies are cleared
        '''
        self.assertEqual(response.cookies['app-auth'].value, "")
        self.assertEqual(response.cookies['refresh-token'].value, "")

        '''
        cookies have the expected attributes
        '''
        self.assertTrue(response.cookies['app-auth']["httponly"])
        self.assertEqual(
            response.cookies['app-auth']['expires'],
            'Thu, 01 Jan 1970 00:00:00 GMT')
        self.assertEqual(response.cookies['app-auth']['max-age'], 0)
        self.assertEqual(response.cookies['app-auth']['samesite'], 'None')
        self.assertEqual(response.cookies['app-auth']['secure'], True)

        self.assertTrue(response.cookies['refresh-token']["httponly"])
        self.assertEqual(
            response.cookies['refresh-token']['expires'],
            'Thu, 01 Jan 1970 00:00:00 GMT')
        self.assertEqual(response.cookies['refresh-token']['max-age'], 0)
        self.assertEqual(response.cookies['refresh-token']['samesite'], 'None')
        self.assertEqual(response.cookies['refresh-token']['secure'], True)
