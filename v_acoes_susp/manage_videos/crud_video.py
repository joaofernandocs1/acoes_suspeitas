import boto3
from pprint import pprint
 
def insert_video(number, local, data, hora, duracao, arquivo, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            #'dynamodb', endpoint_url="http://localhost:8000")
            'dynamodb', region_name="us-east-1")
 
    table = dynamodb.Table('FlaggedVideos')
    response = table.put_item(
        Item={
            'number': number,
            'local': local,
            'data': data,
            'hora': hora,
            'duracao': duracao,
            'arquivo': arquivo
        }
    )
    return response
 
if __name__ == '__main__':
    video_resp = insert_video("1", "ponto xyz", "21/03/2022", "17h49", "34", "video_exemplo_1234.avi")
    print("Insert video succeeded:")
    pprint(video_resp, sort_dicts=False)