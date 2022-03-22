import boto3
 
def create_users_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            #'dynamodb', endpoint_url="http://localhost:8000")
            'dynamodb', region_name="us-east-1")
 
    table = dynamodb.create_table(
        TableName='FlaggedVideos',
        KeySchema=[
            {
                'AttributeName': 'number',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'duracao',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'number',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'duracao',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 4, # colunas que podem ser acrescentadas sem ter sido declaradas na criação da tabela
            'WriteCapacityUnits': 4 # colunas que podem ser acrescentadas sem ter sido declaradas na criação da tabela
        }
    )
    return table
 
if __name__ == '__main__':
    users_table = create_users_table()
    print("Table status:", users_table.table_status)