from django.db import models


# Create your models here.
class File(models.Model):
    number = models.CharField(u'序号', max_length=10, default="1")
    title = models.CharField(u'标题', max_length=20)
    content = models.TextField(u'内容', default="请添加内容")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文案模版'


class Profile(models.Model):
    number = models.CharField(u'编号', max_length=10)
    series = models.CharField(u'系列', max_length=10)
    self = models.CharField(u'自称', max_length=10)
    fans = models.CharField(u'粉丝', max_length=10)
    greeting = models.CharField(u'打招呼', max_length=30)
    question = models.CharField(u'提问', max_length=20)
    praise = models.CharField(u'称赞', max_length=10)
    tucao = models.CharField(u'吐槽', max_length=10)
    koupi = models.CharField(u'口癖', max_length=10)
    next = models.CharField(u'下集预告', max_length=20)
    end = models.CharField(u'关注点赞', max_length=30)

    def __str__(self):
        return self.series

    class Meta:
        verbose_name_plural = '人设模版'


class PartTimer(models.Model):
    account = models.CharField(u'用户名', max_length=30)
    passowrd = models.CharField(u'密码', max_length=20)
    name = models.CharField(u'名称', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '兼职人员'


class UploadList(models.Model):
    parttimer_id = models.ForeignKey(PartTimer, on_delete=models.CASCADE, verbose_name="兼职ID")
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="人设")
    createdate = models.DateTimeField(u'上传时间', auto_now_add=True)
    status = models.BooleanField(u'状态', choices=((0, '未审核'), (1, '已审核')), null=True)

    # def __str__(self):
    #     return self.createdate

    class Meta:
        verbose_name_plural = '上传列表'


class UploadFile(models.Model):
    upload_id = models.ForeignKey(UploadList, on_delete=models.CASCADE, verbose_name="上传ID")
    template_id = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name="文案模版")
    content = models.TextField(u'内容', default='请添加内容')
    status = models.BooleanField(u'状态', choices=((0, '通过'), (1, '不通过')), null=True)

    # def __str__(self):
    #     return self.id

    class Meta:
        verbose_name_plural = '上传内容'


class Newfile(models.Model):
    title = models.CharField(u'标题', max_length=20)
    template_id = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name="文案模版")
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="人设")
    content = models.TextField(u'内容', default="请添加内容")
    status = models.BooleanField(u'状态', choices=((0, '通过'), (1, '不通过')), null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '新文案'
