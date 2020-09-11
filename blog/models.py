from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail

# pip freeze > requirements.txt
# pip install -r requirements.txt 这是一键部署命令
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=25)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # 标记 是否删除
    is_delete = models.BooleanField(default=False)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后跟新时间
    last_update_time = models.DateTimeField(auto_now=True)
    # 阅读数量
    # read_num = models.IntegerField(default=0)
    read_details = GenericRelation(ReadDetail)

    def get_url(self):
        return reverse('blog_detail',kwargs = {'blog_pk':self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog: %s>"%self.title

    class Meta:
        ordering = ['-create_time']


