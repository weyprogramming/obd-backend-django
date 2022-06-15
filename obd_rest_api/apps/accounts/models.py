from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Car(models.Model):
    manufacturer = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    construction_year = models.IntegerField()
    
    BENZIN = 'benzin'
    DIESEL = 'diesel'

    FUEL_TYPE_CHOICES = [
        (BENZIN, 'benzin'),
        (DIESEL, 'diesel'),
    ]

    fuel_type = models.CharField(max_length=6, choices=FUEL_TYPE_CHOICES, default=BENZIN)

    mass_kg = models.IntegerField()
    engine_displacement_l = models.FloatField()
    number_of_cylinders = models.IntegerField()
    milage_km = models.IntegerField()
    power_ps = models.IntegerField()

    def __str__(self):
        return self.manufacturer + " " + self.model_name

class AccountManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an username.")
        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username    
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_raspberry = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    driving_license_since = models.DateField(blank=True, null=True)

    MALE = 'male'
    FEMALE = 'female'
    DIVERSE = 'diverse'

    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
        (DIVERSE, 'diverse'),
    ]

    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=MALE)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, related_name="account", null=True, blank=True)

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
