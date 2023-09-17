import base64
import subprocess

""" FIXED NAMES OF BUCKETS OR DATABSES """
TANGRAM_GENERATION = 'tangram-generation'

""" PREFIXES IS FOR RUNNING OF HUAWEI LIBRARY COMMANDS """
""" OBS INSTALLATION: https://support.huaweicloud.com/intl/en-us/utiltg-obs/obs_11_0003.html """
"""
Setup steps for OBS
- Run ./obsutil config -interactive
- Generate ECS IAM User to get access key (ak) and secret access key (sak)
- Get endpoint from https://developer.huaweicloud.com/intl/en-us/endpoint
- Endpoint should be obs.ap-southeast-3.myhuaweicloud.com
- Can leave token blank
"""
OBSUTIL_PREFIX = '~/obsutil/obsutil'

def getTangramImage(id):
    ''' Gets image for the generated tangram puzzle id and returns b64 string '''
    filename = f'image{id}.jpg'
    cmd = f'{OBSUTIL_PREFIX} cp obs://{TANGRAM_GENERATION}/{filename} {filename}'
    process = subprocess.run(cmd, shell=True, capture_output=True)

    with open(filename, "rb") as image:
        encoded_string = base64.b64encode(image.read())

    ''' CLEANUP ''' 
    cmd = f'rm {filename}'
    process = subprocess.run(cmd, shell=True, capture_output=True)

    return encoded_string

if __name__ == '__main__':
    getTangramImage(52)
