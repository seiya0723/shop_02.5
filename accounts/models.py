from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#TODO:PermissionsMixinとUserManagerが存在しないため、追加。
from django.contrib.auth.models import PermissionsMixin, UserManager

from django.utils import timezone

import uuid


# 一般ユーザーおよびスーパーユーザーを作成するクラス
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


# カスタムユーザーモデルを指定するクラス
class CustomUser(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(verbose_name='ユーザー名', max_length=100,
                                unique=True,
                                error_messages={
                                    'unique': ("同一のユーザー名が既に登録されています"),
                                }, )
    email = models.EmailField(verbose_name='メールアドレス', unique=True,
                              error_messages={
                                  'unique': ("同一のメールアドレスが既に登録されています"),
                              }, )
    name = models.CharField(verbose_name='名前', blank=False, max_length=30)
    name_kana = models.CharField(verbose_name='名前(ふりがな)', blank=False, max_length=60)
    join_dt = models.DateTimeField(verbose_name='登録日時', default=timezone.now)
    is_admin = models.BooleanField(verbose_name='管理者', default=False)
    is_active = models.BooleanField(verbose_name='有効', default=True)

    EMAIL_FIELD = 'email'


    #TODO:USERNAME_FIELDはusernameを指定する。
    #USERNAME_FIELD = 'email'
    USERNAME_FIELD = 'username'

    #TODO:usernameは既に追加されている。入力必須のemail,name,name_kana,を指定
    #REQUIRED_FIELDS = ['username']
    REQUIRED_FIELDS = [ "email","name","name_kana", ]

    objects = CustomUserManager()


    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.name
