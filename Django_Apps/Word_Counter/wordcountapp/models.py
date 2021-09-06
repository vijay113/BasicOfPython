from django.db import models


class MyText:
    text = str
    text_count = int
    def __init__(self,text,count=0) :
        self.text = text
        self.text_count = count

    
    def get_count(self):
        # process anything
        return self.text_count
    
    
    def get_text(self):
        #process anything
        return self.text

