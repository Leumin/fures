# Generated by Django 2.1.7 on 2019-04-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una descripcion', 'max_length': 'Este campo no puede exceder los 45 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una descripcion'}, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPlato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una categoria para el plato', 'max_length': 'La descripcion  de la categoria del plato no puede contener mas de 100 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una categoria para el plato'}, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPlatoPlato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaRestaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(100 de caracteres)'}, max_length=100)),
                ('puntuacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImagenUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fures/img')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_menu', models.TextField(error_messages={'blank': 'El nombre del menu no puede quedar vacio,por favor proporcione el nombre del nemu', 'max_length': 'Al parecer ha sobrepasado la cantidad de caracteres permitidos(30)', 'null': ' El nombre del menu no puede quedar null, por favor proporcione el nombre del menu'}, max_length=30)),
                ('descripcion', models.TextField(blank=True, error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(50) de caracteres'}, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuSucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_plato', models.TextField(error_messages={'blank': 'El nombre del plato no puede quedar vacío, por favor proporcione el nombre del plato', 'max_length': 'Al parecer ha sobrepasado la cantidad permitida(45) de caracteres', 'null': 'El nombre del plato no puede quedar null, por favor proporcione el nombre del plato'}, max_length=45)),
                ('precio', models.DecimalField(decimal_places=2, error_messages={'blank': 'Este campo no puede quedar vacio, por favor ingrese una cantidad para el precio', 'null': 'Por favor ingrese una cantidad para el precio'}, max_digits=6)),
                ('estado', models.BooleanField(default=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('descripcion', models.TextField(error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(5000) de caracteres'}, max_length=5000)),
                ('fecha_inicio', models.DateField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'})),
                ('fecha_final', models.DateField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'})),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(max_length=11, primary_key=True, serialize=False)),
                ('hora_fecha_reserva', models.DateTimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'})),
                ('estado_reserva', models.BooleanField()),
                ('cantidad_personas', models.IntegerField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'})),
                ('motivo_cancelacion', models.TextField(blank=True, error_messages={'max_length': 'Al parecer a sobrepasado la cantidad permitida(1000) de caracteres'}, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favr proporcione un nombre para el restaurante', 'max_length': 'Este campo no puede contener mas de 300 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione un nombre para el restaurante'}, max_length=300)),
                ('descripcion', models.TextField(error_messages={'max_length': 'Este campo no puede contener mas de 1000 caracteres'}, max_length=1000)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(error_messages={'blank': 'Este campo no puede quedar blank, por favor proporcione una descripcion para este rol', 'max_length': 'Este campo no puede contener mas de 45 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una descripcion para este rol'}, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(error_messages={'max_length': 'Este campo no puede contener mas de 45 caracteres'}, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(error_messages={'blank': ' Este campo no puede quedar vacío, por favor proporcione una direccion para la sucursal', 'max_length': 'Ha excedido la cantidad permitida(700) de caracteres en la direccion de la sucursal', 'null': ' Este campo no puede quedar null, por favor proporcione una direccion para la sucursal'}, max_length=700)),
                ('telefono', models.CharField(error_messages={'blank': ' Este campo no puede quedar vacío, por favor proporcione un numero de telefono', 'max_length': 'Ha excedido la cantidad permitida(8) de caracteres en el telefono', 'null': 'Este campo no puede quedar null, por favor proporcione un numero de telefono'}, max_length=8)),
                ('hora_inicio', models.TimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de inicio', 'null': 'Este campo no puede quedar null, por favor proporcione una hora de inicio'})),
                ('hora_cierre', models.TimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de cierre', 'null': 'Este campo no puede quedar null, por favor proporcione una hora de cierre'})),
                ('capacidad', models.IntegerField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor ingrese una cantidad para la capacidad', 'null': 'Es necesario ingresar una cantidad para la capacidad'})),
                ('estado', models.BooleanField(default=True)),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Restaurante')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_persona', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario', 'max_length': 'El Nombre no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione un Nombre de Usuario'}, max_length=45)),
                ('apellido_persona', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Apellido ', 'max_length': 'EL Apellido no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione un Apellido '}, max_length=45)),
                ('direccion', models.TextField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una direccion de Usuario', 'max_length': 'La direccion de Usuario no puede ser mayor a 700  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione una direccion de Usuario'}, max_length=700)),
                ('nombre_usuario', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario', 'max_length': 'El nombre de Usuario no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione Nombre de Usuario'}, max_length=45)),
                ('contrasena', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una contraseña de Usuario', 'max_length': 'La contraseña de Usuario no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione una contraseña de Usuario'}, max_length=45)),
                ('correo', models.EmailField(error_messages={'invalid': 'Correo no valido'}, max_length=254)),
                ('telefono', models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un telefono', 'max_length': 'El telefono no puede contener mas de 8 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione un telefono'}, max_length=8)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='servicio',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Usuario'),
        ),
        migrations.AddField(
            model_name='promocion',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal'),
        ),
        migrations.AddField(
            model_name='imagenusuario',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal'),
        ),
    ]
