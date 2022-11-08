# Generated by Django 3.2.16 on 2022-11-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0012_alter_customer_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Province',
            field=models.CharField(choices=[('Bagmati', 'Bagmati'), ('Bheri', 'Bheri'), ('Dhawalagiri', 'Dhawalagiri'), ('Gandaki', 'Gandaki'), ('Janakpur', 'Janakpur'), ('Karnali', 'Karnali'), ('Koshi', 'Koshi'), ('Lumbini', 'Lumbini'), ('Mahakali', 'Mahakali'), ('Mechi', 'Mechi'), ('Narayani', 'Narayani'), ('Rapti', 'Rapti'), ('Sagarmatha', 'Sagarmatha'), ('Seti', 'Seti')], max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('Achham', 'Achham'), ('Arghakhanchi', 'Arghakhanchi'), ('Baglung', 'Baglung'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'), ('Bajura', 'Bajura'), ('Banke', 'Banke'), ('Bara', 'Bara'), ('Bardiya', 'Bardiya'), ('Bhaktapur', 'Bhaktapur'), ('Bhojpur', 'Bhojpur'), ('Chitwan', 'Chitwan'), ('Dadeldhura', 'Dadeldhura'), ('Dailekh', 'Dailekh'), ('Dang deukhuri', 'Dang deukhuri'), ('Darchula', 'Darchula'), ('Dhading', 'Dhading'), ('Dhankuta', 'Dhankuta'), ('Dhanusa', 'Dhanusa'), ('Dholkha', 'Dholkha'), ('Dolpa', 'Dolpa'), ('Doti', 'Doti'), ('Gorkha', 'Gorkha'), ('Gulmi', 'Gulmi'), ('Humla', 'Humla'), ('Ilam', 'Ilam'), ('Jajarkot', 'Jajarkot'), ('Jhapa', 'Jhapa'), ('Jumla', 'Jumla'), ('Kailali', 'Kailali'), ('Kalikot', 'Kalikot'), ('Kanchanpur', 'Kanchanpur'), ('Kapilvastu', 'Kapilvastu'), ('Kaski', 'Kaski'), ('Kathmandu', 'Kathmandu'), ('Kavrepalanchok', 'Kavrepalanchok'), ('Khotang', 'Khotang'), ('Lalitpur', 'Lalitpur'), ('Lamjung', 'Lamjung'), ('Makwanpur', 'Makwanpur'), ('Manang', 'Manang'), ('Mahottari', 'Mahottari'), ('Morang', 'Morang'), ('Mugu', 'Mugu'), ('MustMang', 'MustMang'), ('Myagdi', 'Myagdi'), ('Nawalparasi', 'Nawalparasi'), ('Nuwakot', 'Nuwakot'), ('Okhaldhunga', 'Okhaldhunga'), ('Palpa', 'Palpa'), ('Panchthar', 'Panchthar'), ('Parbat', 'Parbat'), ('Parsa', 'Parsa'), ('Pyuthan', 'Pyuthan'), ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), ('Rautahat', 'Rautahat'), ('Rolpa', 'Rolpa'), ('Rukum', 'Rukum'), ('Rupandehi', 'Rupandehi'), ('Salyan', 'Salyan'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'), ('Sindhuli', 'Sindhuli'), ('Sindhupalchok', 'Sindhupalchok'), ('Siraha', 'Siraha'), ('Solukhumbu', 'Solukhumbu'), ('Sunsari', 'Sunsari'), ('Surkhet', 'Surkhet'), ('Syangja', 'Syangja'), ('Tanahu', 'Tanahu'), ('Taplejung', 'Taplejung'), ('Terhathum', 'Terhathum'), ('Udayapur', 'Udayapur')], max_length=30),
        ),
    ]
