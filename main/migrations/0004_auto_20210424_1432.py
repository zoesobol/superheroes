# Generated by Django 3.2 on 2021-04-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_superheroe_heroe_villano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superheroe',
            name='heroe_villano',
            field=models.CharField(choices=[('Heroe', 'Heroe/Heroina'), ('Villano', 'Villano/Villana')], default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='superheroe',
            name='superpower',
            field=models.CharField(blank=True, choices=[('Volar', 'Volar'), ('Superinteligencia', 'Superinteligencia'), ('Vista de rayo láser', 'Vista de rayo láser'), ('Billetera gorda', 'Billetera gorda')], default=None, max_length=19, null=True),
        ),
    ]
