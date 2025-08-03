pyurlquerycli
=============

Description
-----------
A simple script to interact with urlquery.net APIs from cli.


Usage
-----
```
$ python3 -Wall pyurlquerycli/pyurlquerycli.py -h
usage: pyurlquerycli.py [-h] -i INPUT_FILE [-k API_KEY] [{submit,check}]

version: 1.0

positional arguments:
  {submit,check}        Action to do on urlquery.net (default 'submit')

optional arguments:
  -h, --help            show this help message and exit

common parameters:
  -i INPUT_FILE, --input-file INPUT_FILE
                        Input file (either list of newline-separated FQDN or URL (for submitting) || submission UUID (for
                        checking reports)
  -k API_KEY, --api-key API_KEY
                        API key (could either be provided in the "SECRET_URLQUERY_APIKEY" env var)
```
  

Changelog
---------
* version 1.0 - 2025-08-03: Initial commit

Copyright and license
---------------------

pyurlquerycli is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

pyurlquerycli is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License along with pyurlquerycli. 
If not, see http://www.gnu.org/licenses/.

Contact
-------
* Thomas Debize < tdebize at mail d0t com >