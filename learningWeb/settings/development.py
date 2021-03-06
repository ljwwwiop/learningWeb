"""
Django settings for learningWeb project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# 本地测试
import os
from .base import *



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+2&_^w3dm^87f$%xy^dj&@&j4a(8+q5f2ug2j$l$0ziv=!9y_8'
# SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# ALLOWED_HOSTS = ['ljw.pythonanywhere.com']
ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER':'ljw',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# 发送邮箱设置
EMAIL_BACKED = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_POST = 25
EMAIL_HOST_USER = '1206957838@qq.com'
EMAIL_HOST_PASSWORD = 'btbaedwwwtgijeia'    # 授码权
EMAIL_SUBJECT_PREFIX = '[ ljw的博客 ]'
EMAIL_USE_TLS = True      # SMTP通信时，是否启用 安全连接



