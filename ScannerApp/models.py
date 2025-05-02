from django.db import models

class Estudiantes(models.Model):
    idestudiante = models.AutoField(
        db_column='idEstudiante',
        primary_key=True,
        verbose_name='ID de Estudiante',
        help_text='Identificador único del estudiante.'
    )
    id_programa = models.IntegerField(
        db_column='id_Programa',
        verbose_name='ID de Programa',
        help_text='Identificador del programa académico al que pertenece el estudiante.',
        error_messages={
            'invalid': 'Debe ingresar un número válido para el ID del programa.',
            'blank': 'Debe especificar el ID del programa.'
        }
    )
    nombres = models.CharField(
        db_column='Nombres',
        max_length=100,
        verbose_name='Nombres completos',
        help_text='Nombres y apellidos del estudiante.',
        error_messages={
            'max_length': 'Los nombres no pueden exceder 100 caracteres.',
            'blank': 'Debe ingresar los nombres completos del estudiante.'
        }
    )
    edad = models.IntegerField(
        db_column='Edad',
        verbose_name='Edad',
        help_text='Edad actual del estudiante.',
        error_messages={
            'invalid': 'Debe ingresar un número válido para la edad.',
            'blank': 'Debe ingresar la edad del estudiante.'
        }
    )
    codigo = models.CharField(
        db_column='Codigo',
        max_length=20,
        verbose_name='Código de estudiante',
        help_text='Código único asignado al estudiante por la universidad.',
        error_messages={
            'max_length': 'El código no puede exceder los 20 caracteres.',
            'blank': 'Debe ingresar un código de estudiante.'
        }
    )
    correo = models.CharField(
        db_column='Correo',
        max_length=100,
        verbose_name='Correo electrónico',
        help_text='Correo electrónico institucional del estudiante.',
        error_messages={
            'max_length': 'El correo no puede exceder 100 caracteres.',
            'blank': 'Debe ingresar el correo electrónico del estudiante.'
        }
    )
    semestre = models.IntegerField(
        db_column='Semestre',
        verbose_name='Semestre académico',
        help_text='Semestre actual que cursa el estudiante.',
        error_messages={
            'invalid': 'Debe ingresar un número válido para el semestre.',
            'blank': 'Debe ingresar el semestre actual del estudiante.'
        }
    )
    contraseña = models.CharField(
        db_column='Contraseña',
        max_length=45,
        verbose_name='Contraseña',
        help_text='Contraseña para acceso al sistema.',
        error_messages={
            'max_length': 'La contraseña no puede exceder los 45 caracteres.',
            'blank': 'Debe ingresar una contraseña.'
        }
    )

    class Meta:
        managed = False
        db_table = 'estudiantes'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return f"{self.nombres} ({self.codigo})"


class Ingreso(models.Model):
    idingreso = models.AutoField(
        db_column='idIngreso',
        primary_key=True,
        verbose_name='ID de Ingreso',
        help_text='Identificador único del registro de ingreso.'
    )
    idestudiante = models.ForeignKey(
        Estudiantes,
        models.DO_NOTHING,
        db_column='idEstudiante',
        verbose_name='Estudiante',
        help_text='Estudiante que realizó el ingreso.'
    )
    fecha_ingreso = models.DateField(
        db_column='Fecha_Ingreso',
        verbose_name='Fecha de ingreso',
        help_text='Fecha en la que el estudiante ingresó.'
    )
    hora_ingreso = models.TimeField(
        db_column='Hora_Ingreso',
        verbose_name='Hora de ingreso',
        help_text='Hora exacta en la que el estudiante ingresó.'
    )

    class Meta:
        managed = False
        db_table = 'ingreso'
        verbose_name_plural = 'Ingresos'

    def __str__(self):
        return f"Ingreso de {self.idestudiante.nombres} el {self.fecha_ingreso} a las {self.hora_ingreso}"

