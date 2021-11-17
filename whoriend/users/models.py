from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
# Database의 형태를 보여줌


# Model은 필드를 갖고있음 ex) 텍스트필드, 이메일필드 등등
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        
        """ Creates and saves a User with the given email, date of birth and password """
        
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth=models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    country = models.CharField(max_length=20, default="한국")
    pic = models.ImageField(upload_to="pic", blank = True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, null = False)
    interest = models.ManyToManyField("category.Category", blank=False)
    can_teach = models.ManyToManyField("category.Detail_category", blank=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']
    
    def get_full_name(self):
        # The user is identified by their email address
        return self.email
    
    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible ansewer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin