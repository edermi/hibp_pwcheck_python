#!/usr/bin/env python3

# requires requests

import sys
import hashlib
import requests
    
HIBP_ENDPOINT = "https://api.pwnedpasswords.com/range/"
REQ_HEADERS = { 'User-Agent': 'FSMPI User Passwordcheck for fs.tum.de' }

class HIBP_API_Error(Exception):
   def __init__(self, value):
      self.response_code = value
   def __str__(self):
       return(f"HIBP API Error Code: {self.response_code}")

def hibp_check_pwned(candidate):
    '''
    Checks a password candidate against HIBP API
    If a password has been found in a breach, the function returns True and the count 
    Otherwise, False and 0 is returned
    '''
    hash_digest = hashlib.sha1(candidate.encode('utf-8')).hexdigest().upper()
    prefix = hash_digest[:5]

    resp = requests.get(f"{HIBP_ENDPOINT}{prefix}", headers=REQ_HEADERS)
    if resp.status_code != 200:
        raise HIBP_API_Error(resp.status_code) 
    hashes = resp.content.decode('utf-8').split('\r\n')

    for breached in hashes:
        if (prefix + breached).startswith(hash_digest):
            breachcount = breached.split(':')[1]
            return True, int(breachcount)

    return False, 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: hibp_check.py <pw_to_check>")
        sys.exit(2)
    else:
        candidate = sys.argv[1]
        try:
            pwned, times = hibp_check_pwned(candidate)
        except HIBP_API_Error as e:
            print(e)
            sys.exit(3)
        if pwned:
            print(f"{candidate} has been pwned {times} times")
            sys.exit(1)
        else:
            print(f"{candidate} was not found in the pwned PW database")
            sys.exit(0)
