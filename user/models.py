from django.conf import settings
from django.db import models
from django.utils.text import slugify  # Import slugify function
from django.urls import reverse
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Default Name")
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    #joined = models.DateTimeField("Date Joined", default=timezone.now)
    email = models.EmailField(default='your email')
    job = models.CharField(max_length=100, default='your degree')
    phone_number = models.CharField(
        max_length=15,  # Assuming you want to store phone numbers like '123-456-7890'
        help_text="Enter your phone number in the format '123-456-7890'",
        unique=True,  # Optional, if you want each phone number to be unique
        blank=True,   # Optional, allows the field to be empty
        null=True     # Optional, allows the field to be null in the database
    )
    picture = models.ImageField(
        upload_to='profiles/',
        default='default.png',
        null=True,
        blank=True,
    )

    def __str__(self):
        if self.picture:
            return f"Image - {self.picture.name}"
        else:
            return "No Image"
    
    def __str__(self):
        return self.phone_number

    def __str__(self):
        return self.user.get_username() 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
         return reverse('public_profile', kwargs={'slug': self.slug})
    
    def get_update_url(self):
	    return reverse('profile_update') 




    


    
    
    
    
    
    
    
    
    
