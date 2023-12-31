# Generated by Django 4.2.7 on 2023-11-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('tilte', models.CharField(max_length=50)),
                ('head0', models.CharField(default='', max_length=500)),
                ('chead0', models.TextField(default='')),
                ('head1', models.CharField(default='', max_length=500)),
                ('chead1', models.TextField(default='')),
                ('head2', models.CharField(default='', max_length=500)),
                ('chead2', models.TextField(default='')),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
