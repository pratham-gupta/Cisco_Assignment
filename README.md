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

<br>Content type: application/json
<br>URL: 127.0.0.1:8000/api/router
<br>Required:
<br>sapid: string(18)
<br>hostname: string(17)
<br>loopback: ipv4 (unique)
<br>macaddress: string (macaddress)
<br>Response:
<br>Success : 200 OK

Example: <br>

```
curl --location --request POST 'localhost:8000/api/router' \ --header 'Authorization: Token 0ffc8ccd80d0b2a574f075dfa37722d4d1d6a2fc' \ --header 'Content-Type: application/json' \ --data-raw '{"sapid":"router2", "hostname":"unique@aa.com", "loopback":"192.12.43.44", "macaddress":"2C:54:91:88:C9:E3"}'
```

### GET Request: Retrieve list of all router or filter on basis provided IP range

<br>URL: 127.0.0.1/api/router
<br>Method: GET
<br>Optional:
<br>loopback_start: ipv4 address
<br>loopback_end: ipv4 address
<br>Response:
<br>Success 200 Ok: Application/json
<br>Not Found 404 : Invalid IP addresses
<br>Bad Request 400 : Invalid Requests
<br>Example:

```
curl --location --request GET 'http://127.0.0.1:8000/api/router?loopback_start=192.12.43.22&loopback_end=192.12.43.22' \
--header 'Authorization: Token f207298a533a3e8de4ccfb78125b5a249a5f56bf'
```

### PATCH Request: Partial update of Router object based on unique Loopback

<br>URL: 127.0.0.1/api/router
<br>method: PATCH
<br>Required:
<br>loopback: IP Addresses
<br>Optional: (fields to update)
<br>sapid: string(18)
<br>hostname: string(17)
<br>macaddress: string(17)
<br>Response:
<br>Sucess 200 ok: Application/json
<br>Not Found 404: Loopback Address not Found
<br>Bad request 400: Invalid request dataa

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
