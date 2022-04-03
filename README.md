# Cisco_Assignment

## Build Instructions

Install dependencies using pip and requirements file <br>

```
pip install requirements.txt
```

## start the development server

(the dev server will start at localhost and port 8000) <br>

```
python manage.py runserver 127.0.0.1.:8000
```

## For Auth Token: Use the following curlrequest.

```
curl --location --request POST 'http://127.0.0.1:8000/api-token-auth' \ --header 'Content-Type: application/json' \ --data-raw '{"username":"test_user", "password":"testpass"}'
```

## API endpoint: 127.0.0.1/api/router

(This Endpoint serves multiple purpose and accepts (GET,POST,PATCH) typre requests.)

### POST : create new router object.

Content type: application/json
URL: 127.0.0.1:8000/api/router
Required:
sapid: string(18)
hostname: string(17)
loopback: ipv4 (unique)
macaddress: string (macaddress)
Response:
Success : 200 OK

Example: <br>

```
curl --location --request POST 'localhost:8000/api/router' \ --header 'Authorization: Token 0ffc8ccd80d0b2a574f075dfa37722d4d1d6a2fc' \ --header 'Content-Type: application/json' \ --data-raw '{"sapid":"router2", "hostname":"unique@aa.com", "loopback":"192.12.43.44", "macaddress":"2C:54:91:88:C9:E3"}'
```

### GET Request: Retrieve list of all router or filter on basis provided IP range

URL: 127.0.0.1/api/router
Method: GET
Optional:
loopback_start: ipv4 address
loopback_end: ipv4 address
Response:
Success 200 Ok: Application/json
Not Found 404 : Invalid IP addresses
Bad Request 400 : Invalid Requests
Example:

```
curl --location --request GET 'http://127.0.0.1:8000/api/router?loopback_start=192.12.43.22&loopback_end=192.12.43.22' \
--header 'Authorization: Token f207298a533a3e8de4ccfb78125b5a249a5f56bf'
```

### PATCH Request: Partial update of Router object based on unique Loopback

URL: 127.0.0.1/api/router
method: PATCH
Required:
loopback: IP Addresses
Optional: (fields to update)
sapid: string(18)
hostname: string(17)
macaddress: string(17)
Response:
Sucess 200 ok: Application/json
Not Found 404: Loopback Address not Found
Bad request 400: Invalid request dataa

Example:

```
curl --location --request PATCH 'http://127.0.0.1:8000/api/router' \
--header 'Authorization: Token f207298a533a3e8de4ccfb78125b5a249a5f56bf' \
--header 'Content-Type: application/json' \
--data-raw '{

    "loopback": "192.12.43.23",
    "macaddress": "2C:54:91:88:C9:E2"

}'
```
