import random
from Recognition import RecognitionService
from Storage import StorageService

class ObjectDetectionDemo() :
    
    def __init__(self) :
        ''' '''
        
    def demo(self, bname) :
        
        storage = StorageService()
        recog = RecognitionService()
        
        flist = storage.get_all_files(bname)
        file = random.choice(flist)
        filename = file['file_name']
        
        response = recog.detect_objects_from_S3(bname, filename)
        
        return filename, response


