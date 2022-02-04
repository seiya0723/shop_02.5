from django.db import models

#TODO:カスタムユーザーモデルを使う時、この呼び出し方は使えない。
#from accounts.models import CustomUser

#TODO:下記のようにsettings.pyにてAUTH_USER_MODELを指定して、ForeignKeyに指定する。
from django.conf import settings

from django.utils import timezone

import uuid

class CategoryCreation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(verbose_name='カテゴリー名', unique=True, max_length=15)

    def __str__(self):
        return self.name

class CommentCreation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)


    #TODO:settings.AUTH_USER_MODELを指定する。
    #user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, verbose_name='投稿ユーザ')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='投稿ユーザ')


    post_dt = models.DateTimeField(verbose_name='投稿日時', default=timezone.now)
    category = models.ForeignKey(CategoryCreation, on_delete=models.PROTECT, verbose_name='カテゴリー')

    #TODO:この指定はできない(settings.AUTH_USER_MODELは文字列型であるため)
    #username = models.CharField(verbose_name='ユーザー名', max_length=30, blank=False, default=CustomUser.username)
    username = models.CharField(verbose_name='ユーザー名', max_length=30, blank=False, default="匿名")

    topic = models.CharField(verbose_name='タイトル', max_length=100, blank=False)
    comment = models.CharField(verbose_name='内容', max_length=2000, blank=False)

    def __str__(self):
        return self.username
