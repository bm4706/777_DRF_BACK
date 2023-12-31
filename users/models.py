from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        # if not nickname:
        #     raise ValueError('must have user nickname')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            nickname=nickname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=100, unique=True)
    
    image = models.ImageField(upload_to="", null=True, blank=True) # blank=True면 Optional 필드
    
    
    followings = models.ManyToManyField('self',related_name="followers", blank=True, symmetrical=False)
    
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property # @property를 사용하면 클래스의 내부 데이터를 숨기고 접근자 메서드(getter)를 통해 데이터에 접근할 수 있습니다. 이를 통해 데이터의 무결성을 보호하고 외부에서 직접 접근하지 못하도록 할 수 있습니다.
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

