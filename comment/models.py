import threading
from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.template.loader import render_to_string
# from django.shortcuts import render

class SendMail(threading.Thread):
    # 使用多线程回复邮件，但是量比较少
    # 安全措施做的比较少，比如锁，条件变量
    def __init__(self,subject,text,email,fail_silently=False):
        self.subject = subject
        self.text = text
        self.email = email
        self.fail_silently = fail_silently
        threading.Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            '',
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=self.fail_silently,
            html_message = self.text
        )

# Create your models here.
class Comment(models.Model):

    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)

    # 记录评论的根
    root = models.ForeignKey('self',related_name='root_comment',null=True,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',related_name='parent_comment',null=True,on_delete=models.CASCADE)
    reply_to = models.ForeignKey(User,related_name="replies",null=True,on_delete=models.CASCADE)

    def send_mail(self):
        # 发送邮件通知
        if self.parent is None:
            # 评论我的blog
            subject = '有人评论你的博客'
            # 内容 + 链接
            email = self.content_object.get_email()
            # 判断email
        else:
            # 回复评论
            subject = '有人回复你的评论'
            email = self.reply_to.email
        if email != '':
            # text = '%s\n<a href = "%s">%s</a>'%(self.text,self.content_object.get_url(),"点击查看")
            context = {}
            context['comment_text'] = self.text
            context['url'] = self.content_object.get_url()
            # render .content.decode('utf-8')
            text = render_to_string('comment/send_mail.html',context)

            # 把send_mail 进行异步处理，不影响下面操作
            send_mail = SendMail(subject,text,email)
            send_mail.start()


    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-comment_time']


