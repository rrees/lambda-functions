
m __future__ import print_function

import os

from datetime import datetime
from urllib2 import urlopen

SITE = os.environ['SITE']  # URL of the site to check
EXPECTED = os.environ['EXPECTED']  # String expected to be on the page


def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    return EXPECTED in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        result = urlopen(SITE).read()
        print(result)
        if not validate(result):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))

