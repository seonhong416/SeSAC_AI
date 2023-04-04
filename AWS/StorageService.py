import boto3
import random

class StorageService() :
    
    def __init__(self) :
        ''' '''
    
    def get_all_files(self, buck_name) :
        buck = boto3.client('s3', region_name='ap-northeast-2')
        response = buck.list_objects_v2(Bucket=buck_name)

        ## file_list 만들기
        file_list = response['Contents']
        
        ## file_list에서 file_name뽑아서 list에 담기
        file_names = [i['Key'] for i in file_list]
                
        ## region 뽑기
        region = response['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']
        
        ## url 형식 만들기
        url = f'http://s3.{region}.amazonaws.com/{buck_name}/'
        
        
        flist = [{'location' : buck_name, 'file_name' : fname, 'url' : url + fname} for fname in file_names]
        
        return flist