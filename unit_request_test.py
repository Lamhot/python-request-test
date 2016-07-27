import requests
import unittest

url = "http://mkapioauth2.modalku.co.id/api/Account"
headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6InJvbmFsZC5pLndpamF5YUBnbWFpbC5jb20iLCJzdWIiOiJyb25hbGQuaS53aWpheWFAZ21haWwuY29tIiwicm9sZSI6IkludmVzdG9yIiwiaXNzIjoiaHR0cDovL2F1dGhzdGFnaW5nLm1vZGFsa3UuY28uaWQvIiwiYXVkIjoiSXBob25lIiwiZXhwIjoxNDY5NjAwMTE3LCJuYmYiOjE0Njk1OTgzMTd9.65FMfde6hjPBxjOT_Q8jrPx1kMCmrrmx-a05vcXY2dM"
}

response = requests.request("GET", url, headers=headers)
state = response.status_code
unittest.assertEqual(200, state)
print(response.text)
