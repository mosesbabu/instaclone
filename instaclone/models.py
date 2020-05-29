from django.db import models

# Create your models here.




class Image(models.Model):
    path = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =100)
    caption = models.TextField()
    likes = models.IntegerField(max_length = 20)
    comments = models.TextField()
    
    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
               

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(image_category__name__icontains=search_term)
        return search_result

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

        
    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item


    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object
