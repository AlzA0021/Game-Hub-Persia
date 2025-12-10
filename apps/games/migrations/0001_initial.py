from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('manufacturer', models.CharField(blank=True, max_length=120)),
            ],
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('genre', models.CharField(blank=True, max_length=120)),
                ('developer', models.CharField(blank=True, max_length=120)),
                ('publisher', models.CharField(blank=True, max_length=120)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(blank=True, related_name='games', to='games.genre')),
                ('platforms', models.ManyToManyField(blank=True, related_name='games', to='games.platform')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=80)),
                ('release_date', models.DateField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='games.game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='games.platform')),
            ],
            options={'ordering': ['release_date'], 'unique_together': {('game', 'platform', 'region', 'release_date')}},
        ),
    ]
