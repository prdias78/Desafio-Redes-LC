# app2.py
import requests
import time

# set address request
address_request = "http://srv1-aws.empresa.com:8080"
interval_request = 2

def httpget(address):
    request_start = time.time()
    response = requests.get(address)
    response_latency = time.time() - request_start
    http_status_code = response.status_code
    print('Request:', address, 'HTTP Response:', http_status_code, 'Request Time:', '{:.2f}'.format(response_latency), 'ms')
    #print(response.headers)
    #print(response.text)

if __name__ == '__main__':
    while True:
        time.sleep(interval_request)
        httpget(address_request)
