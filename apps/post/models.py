from django.db import models


class Post(models.Model):
    post_id 	= models.CharField(max_length=10, blank=False, null=False, unique=True)
    author 		= models.CharField(max_length=30, blank=True, null=True)
    title 		= models.CharField(max_length=200, blank=True, null=True)
    url 		= models.URLField(max_length=220, blank=True, null=True)
    comments 	= models.CharField(max_length=6, blank=True, null=True)
    created_at 	= models.IntegerField(blank=True, null=True)
    image 		= models.URLField(max_length=250, blank=True, null=True)
    readed	 	= models.BooleanField(default=False)
    is_fav 		= models.BooleanField(default=False)

    def __str__(self):
        return self.post_id