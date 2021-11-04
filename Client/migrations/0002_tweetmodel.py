from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='TweetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(max_length=500)),
                ('topics', models.CharField(max_length=300)),
                ('sentiment', models.CharField(max_length=300)),
                ('images', models.FileField(upload_to='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Userregister_Model')),
            ],
        ),
    ]
