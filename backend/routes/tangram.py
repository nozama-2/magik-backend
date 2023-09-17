import json
from flask import request
from hctools import obs

def getTangramImage():
    obj=request.data.decode("utf-8")
    obj = obj.replace("'", '"') # Replace ' with " for json decoding
    obj = json.loads(obj)
    puzzleId = int(obj['puzzle_id'])
    encoded_string = obs.getTangramImage(puzzleId)
    encoded_string = encoded_string.decode('utf-8')
    return json.dumps({'image':encoded_string})
