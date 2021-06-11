from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#Creating a custom user profile manager for our custom user DB model
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name , password=None): #This functions is used by the django CLI when createing users
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        #Normalizing the email address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) #Encrypting the password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name , password):
        """Create and save a new super-user profile"""
        user = self.create_user(email, name , password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



#Creating a custom user DB model;
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database models for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #Creating custom model manager
    objects = UserProfileManager()

    #Some extra fields to work with the django-admin and the django authentication system

    USERNAME_FIELD = 'email' #instead of usernames model will ask to give email for authentication
    REQUIRED_FIELDS = ['name']


    #Creating some functions which django will use to interact to our custom user model;
    def get_full_name(self):
        """Retrieve full name of the user"""
        return self.name


    def get_full_name(self):
        """Retrieve short name of the user"""
        return self.name

    def __str__(self):
        """Return string repr of our user"""
        return self.email
