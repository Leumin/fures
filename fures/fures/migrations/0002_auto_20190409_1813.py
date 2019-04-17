# Generated by Django 2.1.5 on 2019-04-10 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fures', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
        migrations.DeleteModel(
            name='UsuarioTipoUsuario',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='id_categoria',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='categoriaplato',
            old_name='id_categoria_plato',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='id_menu',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='plato',
            old_name='id_plato',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='promocion',
            old_name='id_promocion',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='promocion',
            old_name='id_sucursal',
            new_name='sucursal',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='id_reserva',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='restaurante',
            old_name='id_restaurante',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='rol',
            old_name='id_rol',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='id_servicio',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='id_sucursal',
            new_name='sucursal',
        ),
        migrations.RenameField(
            model_name='sucursal',
            old_name='id_sucursal',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='id_usuario',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='codigo_rol',
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=' ', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una descripcion', 'max_length': 'Este campo no puede exceder los 45 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una descripcion'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='categoriaplato',
            name='descripcion',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una categoria para el plato', 'max_length': 'La descripcion  de la categoria del plato no puede contener mas de 100 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una categoria para el plato'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(100 de caracteres)'}, max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='descripcion',
            field=models.TextField(blank=True, error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(50) de caracteres'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='nombre_menu',
            field=models.TextField(error_messages={'blank': 'El nombre del menu no puede quedar vacio,por favor proporcione el nombre del nemu', 'max_length': 'Al parecer ha sobrepasado la cantidad de caracteres permitidos(30)', 'null': ' El nombre del menu no puede quedar null, por favor proporcione el nombre del menu'}, max_length=30),
        ),
        migrations.AlterField(
            model_name='plato',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Menu', to_field='id_menu'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='nombre_plato',
            field=models.TextField(error_messages={'blank': 'El nombre del plato no puede quedar vacío, por favor proporcione el nombre del plato', 'max_length': 'Al parecer ha sobrepasado la cantidad permitida(45) de caracteres', 'null': 'El nombre del plato no puede quedar null, por favor proporcione el nombre del plato'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='plato',
            name='precio',
            field=models.DecimalField(decimal_places=2, error_messages={'blank': 'Este campo no puede quedar vacio, por favor ingrese una cantidad para el precio', 'null': 'Por favor ingrese una cantidad para el precio'}, max_digits=6),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='descripcion',
            field=models.TextField(error_messages={'max_length': 'Al parecer ha sobrepasado la cantidad permitida(5000) de caracteres'}, max_length=5000),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_final',
            field=models.DateField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'}),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha_inicio',
            field=models.DateField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'}),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal', to_field='id_sucursal'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.IntegerField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'}),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_fecha_reserva',
            field=models.DateTimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione los datos que se piden', 'null': 'Este campo no puede quedar null, por favor proporcione los datos que se piden'}),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='motivo_cancelacion',
            field=models.TextField(blank=True, error_messages={'max_length': 'Al parecer a sobrepasado la cantidad permitida(1000) de caracteres'}, max_length=1000),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal', to_field='id_sucursal'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Usuario', to_field='id_usuario'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='descripcion',
            field=models.TextField(error_messages={'max_length': 'Este campo no puede contener mas de 1000 caracteres'}, max_length=1000),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='nombre',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favr proporcione un nombre para el restaurante', 'max_length': 'Este campo no puede contener mas de 300 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione un nombre para el restaurante'}, max_length=300),
        ),
        migrations.AlterField(
            model_name='rol',
            name='descripcion',
            field=models.TextField(error_messages={'blank': 'Este campo no puede quedar blank, por favor proporcione una descripcion para este rol', 'max_length': 'Este campo no puede contener mas de 45 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione una descripcion para este rol'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.TextField(error_messages={'max_length': 'Este campo no puede contener mas de 45 caracteres'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Sucursal', to_field='id_sucursal'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='capacidad',
            field=models.IntegerField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor ingrese una cantidad para la capacidad', 'null': 'Es necesario ingresar una cantidad para la capacidad'}),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='direccion',
            field=models.CharField(error_messages={'blank': ' Este campo no puede quedar vacío, por favor proporcione una direccion para la sucursal', 'max_length': 'Ha excedido la cantidad permitida(700) de caracteres en la direccion de la sucursal', 'null': ' Este campo no puede quedar null, por favor proporcione una direccion para la sucursal'}, max_length=700),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='hora_cierre',
            field=models.TimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de cierre', 'null': 'Este campo no puede quedar null, por favor proporcione una hora de cierre'}),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='hora_inicio',
            field=models.TimeField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una hora de inicio', 'null': 'Este campo no puede quedar null, por favor proporcione una hora de inicio'}),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fures.Restaurante', to_field='id_restaurante'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='telefono',
            field=models.CharField(error_messages={'blank': ' Este campo no puede quedar vacío, por favor proporcione un numero de telefono', 'max_length': 'Ha excedido la cantidad permitida(8) de caracteres en el telefono', 'null': 'Este campo no puede quedar null, por favor proporcione un numero de telefono'}, max_length=8),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='apellido_persona',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Apellido ', 'max_length': 'EL Apellido no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione un Apellido '}, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una contraseña de Usuario', 'max_length': 'La contraseña de Usuario no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione una contraseña de Usuario'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(error_messages={'invalid': 'Correo no valido'}, max_length=254),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.TextField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione una direccion de Usuario', 'max_length': 'La direccion de Usuario no puede ser mayor a 700  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione una direccion de Usuario'}, max_length=700),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_persona',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario', 'max_length': 'El Nombre no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione un Nombre de Usuario'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un Nombre de Usuario', 'max_length': 'El nombre de Usuario no puede ser mayor a 45  caracteres ', 'null': 'Este campo no puede quedar null, por favor proporcione Nombre de Usuario'}, max_length=45),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(error_messages={'blank': 'Este campo no puede quedar vacío, por favor proporcione un telefono', 'max_length': 'El telefono no puede contener mas de 8 caracteres', 'null': 'Este campo no puede quedar null, por favor proporcione un telefono'}, max_length=8),
        ),
    ]
