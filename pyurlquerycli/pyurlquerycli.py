#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import functools
import concurrent.futures
import requests
import time

import code
import pprint

from w3lib.url import safe_url_string
import validators

# Script version
VERSION = '1.3'

# Options definition
parser = argparse.ArgumentParser(description="version: " + VERSION)
parser.add_argument('scope', help = 'Action to do on urlquery.net (default \'submit\')', nargs = '?', choices = ['submit', 'check'], type = str.lower, default = 'submit')

common_group = parser.add_argument_group('common parameters')
common_group.add_argument('-i', '--input-file', help='Input file (either list of newline-separated FQDN or URL (for submitting) || submission UUID (for checking reports)', required = True)
common_group.add_argument('-k', '--api-key', help='API key (could either be provided in the "SECRET_URLQUERY_APIKEY" env var)', type = str)

# Globals
API_BASE_URL = 'https://api.urlquery.net/public/v1'
API_ENV_VAR = 'SECRET_URLQUERY_APIKEY'

def urlquery_check(options):
    retval = os.EX_OK
    
    url_endpoint = API_BASE_URL + '/report/%s'
        
    reports = []
    
    if os.path.isfile(options.input_file):
        with open(options.input_file, mode='r', encoding='utf-8') as fd_input:
            for line in fd_input:
                line = line.strip()
                if line:
                    if validators.uuid(line):
                        reports.append(line)
        
        if reports:
            #pprint.pprint(reports)
            
            for report in reports:
                req = requests.get(url_endpoint % report, headers=options.api_key)
                if req.ok:
                    req_json = req.json()
                    print("[+] urlquery check request successful")
                    pprint.pprint(req_json)
                
                else:
                    if req.status_code == 429:
                        print("[!] error while submitting urlquery URLs : rate limiting, retrying in 60 seconds")
                        pprint.pprint(req.status_code)
                        print(req.content)
                        print(req.headers)
                    
                        time.sleep(60)
                        req = requests.get(url_endpoint % report, headers=options.api_key)
                        
                    else:
                        print("[!] error while submitting urlquery URLs")
                        pprint.pprint(req.status_code)
                        print(req.content)
                
                print('-------------------')
        else:
            retval = os.EX_NOINPUT
            
    else:
        retval = os.EX_NOINPUT
        
    return retval

def urlquery_submit(options):
    retval = os.EX_OK
    
    url_endpoint = API_BASE_URL + '/submit/url'
        
    malicious_urls = []
    
    if os.path.isfile(options.input_file):
        with open(options.input_file, mode='r', encoding='utf-8') as fd_input:
            for line in fd_input:
                line = line.strip()
                if line:
                    if line.startswith(('http://', 'https://')):
                        entries = [safe_url_string(line)]
                    else:
                        entries = [safe_url_string('http://'+line), safe_url_string('https://'+line)]
                    
                    for entry in entries:
                        if validators.url(entry):
                            malicious_urls.append(entry)
        
        if malicious_urls:
            #pprint.pprint(malicious_urls)
            
            for malicious_url in malicious_urls:
                req_data = { "url": malicious_url,
                             "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
                             "referer": "",
                             "access": "public"
                }
                
                req = requests.post(url_endpoint, headers=options.api_key, json=req_data)
                if req.ok:
                    req_json = req.json()
                    print("[+] urlquery submit request successful")
                    pprint.pprint(req_json)
                
                else:
                    if req.status_code == 429:
                        print("[!] error while submitting urlquery URLs : rate limiting, retrying in 60 seconds")
                        pprint.pprint(req.status_code)
                        print(req.content)
                        print(req.headers)
                    
                        time.sleep(60)
                        req = requests.post(url_endpoint, headers=options.api_key, json=req_data)
                        
                    else:
                        print("[!] error while submitting urlquery URLs")
                        pprint.pprint(req.status_code)
                        print(req.content)
                
                print('-------------------')
        else:
            retval = os.EX_NOINPUT
            
    else:
        retval = os.EX_NOINPUT
        
    return retval

def main():
    global parser
    options = parser.parse_args()
    
    api_key = options.api_key
    if not(api_key):
        if API_ENV_VAR in os.environ:
            api_key = os.environ[API_ENV_VAR]
        else:
            parser.error('[!] No API key has been provided, exiting.')
            
    options.api_key = {"x-apikey": api_key}
    
    if options.scope == 'submit':
        sys.exit(urlquery_submit(options))
    
    elif options.scope == 'check':
        sys.exit(urlquery_check(options))

if __name__ == "__main__" :
    main()
