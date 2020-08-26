# Generated by Django 3.1 on 2020-08-20 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_file_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='content',
            field=models.TextField(default='请添加内容', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='newfile',
            name='content',
            field=models.TextField(default='请添加内容', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='newfile',
            name='status',
            field=models.BooleanField(null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='newfile',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='end',
            field=models.CharField(max_length=30, verbose_name='关注点赞'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fans',
            field=models.CharField(max_length=10, verbose_name='粉丝'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='greeting',
            field=models.CharField(max_length=30, verbose_name='打招呼'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='koupi1',
            field=models.CharField(max_length=10, verbose_name='口癖1'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='koupi2',
            field=models.CharField(max_length=10, verbose_name='口癖2'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='next',
            field=models.CharField(max_length=20, verbose_name='下集预告'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='praise',
            field=models.CharField(max_length=10, verbose_name='称赞'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='question',
            field=models.CharField(max_length=20, verbose_name='提问'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='self',
            field=models.CharField(max_length=10, verbose_name='自称'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='series',
            field=models.CharField(max_length=10, verbose_name='系列'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tucao',
            field=models.CharField(max_length=10, verbose_name='吐槽'),
        ),
    ]