import json
from flask import Response
 
def ResponseJsonApi(data, statusCode):
    return Response( 
        response=json.dumps(data,ensure_ascii=False), 
        mimetype='application/json', 
        status=statusCode 
    )