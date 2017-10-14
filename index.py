import json
import datetime


def handler(event, context):
    data = {
        'output': 'My First Django Project using Python 2.7',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
