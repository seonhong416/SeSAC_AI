import boto3

class RecognitionService() :
    
    def __init__(self) :
        ''' '''
        
    def detect_objects_from_S3(self, bname, filename) :
        
        client = boto3.client('rekognition',region_name='ap-northeast-2')

        res = client.detect_labels(Image={
                                    'S3Object':{
                                        'Bucket' : bname,
                                        'Name' : filename}})['Labels']    
        
        response = [{'label' : i['Name'], 'confidence' : i['Confidence']} for i in res]
        
        return response