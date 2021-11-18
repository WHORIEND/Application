from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
# Database의 형태를 보여줌


# Model은 필드를 갖고있음 ex) 텍스트필드, 이메일필드 등등
class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
  
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )
    
    COUNTRY_KO = "korea"
    COUNTRY_EN = "America"
    COUNTRY_JA = "Japan"
    COUNTRY_CH = "China"
    
    COUNTRY_CHOICES = (
        (COUNTRY_KO ,"korea"),
        ( COUNTRY_EN, "America"),
        ( COUNTRY_JA, "Japan"),
        ( COUNTRY_CH, "China"),
    
    )
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    name = models.CharField(max_length=100, blank=False, default="")
    nickname = models.CharField(max_length=10, blank=False, unique=True, default="")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default=GENDER_FEMALE)
    age = models.IntegerField(default=20, null=True)
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=20, blank=False, default="")
    interest = models.ManyToManyField("category.Category") 
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin