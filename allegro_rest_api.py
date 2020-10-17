import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

class getAccessToken(): 

    authUrl = "https://allegro.pl.allegrosandbox.pl/auth/oauth/token?grant_type=client_credentials";
    clientId = "07e406aa9455432bb29806aceb0ebea0"
    clientSecret = "6fnrkF5gGd73wGoCPrmZxlva8GgjaxuTHDo7hraNJqkSGNFySFbr1mlXXvXtnZ2N"

    ch = curl_init(authUrl)

    curl_setopt(ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
    curl_setopt(ch, CURLOPT_USERNAME, clientId);
    curl_setopt(ch, CURLOPT_PASSWORD, clientSecret);
    curl_setopt(ch, CURLOPT_RETURNTRANSFER, 1);

    tokenResult = curl_exec(ch);
    resultCode = curl_getinfo(ch, CURLINFO_HTTP_CODE);
    curl_close(ch);

    if (tokenResult == false and resultCode != 200): 
        print("Something went wrong")
    

    tokenObject = json_decode(tokenResult)

    tokenObject = access_token


class main():

    print("access_token = ", getAccessToken())


main();