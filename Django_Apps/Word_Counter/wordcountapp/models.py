from django.db import models


class MyText:
    text = str
    text_count = int
    def __init__(self,text,count=0) :
        self.text = text
        self.text_count = count

    @property
    def get_count(self):
        return self.text_count
    
    @property
    def get_text(self):
        return self.text
 