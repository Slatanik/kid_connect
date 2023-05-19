from django.db import models

# Create your models here.
class Evento(models.Model):
    name = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return self.name
    
class Alumno(models.Model):
    rut_alu = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    dv_alu = models.CharField(max_length=1)
    nom_alu = models.CharField(max_length=100)
    ap_pat_alu = models.CharField(max_length=100)
    ap_mat_alu = models.CharField(max_length=100)
    dir_alu = models.CharField(max_length=100)
    curso_cod_cur = models.DecimalField(max_digits=4, decimal_places=0)
    curso_cod_niv = models.DecimalField(max_digits=4, decimal_places=0)
    usuario_rut_us = models.DecimalField(max_digits=8, decimal_places=0)
    usuario_jardin_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    usuario_cod_tip = models.DecimalField(max_digits=2, decimal_places=0)
    curso_cod_jor = models.DecimalField(max_digits=2, decimal_places=0)
    curso_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'alumno'
        unique_together = (('rut_alu', 'curso_cod_cur', 'curso_cod_niv', 'curso_cod_jor', 'curso_cod_jar', 'usuario_rut_us', 'usuario_jardin_cod_jar', 'usuario_cod_tip'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comuna(models.Model):
    cod_com = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    nom_com = models.CharField(max_length=50)
    pvcia_cod_prov = models.ForeignKey('Pvcia', models.DO_NOTHING, db_column='pvcia_cod_prov')
    pvcia_region_cod_reg = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'comuna'
        unique_together = (('cod_com', 'pvcia_cod_prov', 'pvcia_region_cod_reg'),)


class Curso(models.Model):
    cod_cur = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nom_cur = models.CharField(max_length=50)
    nivel_cod_niv = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel_cod_niv')
    nivel_cod_jor = models.DecimalField(max_digits=2, decimal_places=0)
    nivel_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'curso'
        unique_together = (('cod_cur', 'nivel_cod_niv', 'nivel_cod_jor', 'nivel_cod_jar'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FcEst(models.Model):
    cod_fc = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    nom_alu = models.CharField(max_length=100)
    ap_pat_alu = models.CharField(max_length=100)
    ap_mat_alu = models.CharField(max_length=100)
    fec_cre = models.DateField()
    con_fc = models.CharField(max_length=3000, blank=True, null=True)
    img_est = models.BinaryField(blank=True, null=True)
    alumno_rut_alu = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    alumno_cod_cur = models.DecimalField(max_digits=4, decimal_places=0)
    alumno_cod_niv = models.DecimalField(max_digits=4, decimal_places=0)
    alumno_rut_us = models.DecimalField(max_digits=8, decimal_places=0)
    alumno_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    alumno_cod_tip = models.DecimalField(max_digits=2, decimal_places=0)
    alumno_cod_jor = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'fc_est'


class Jardin(models.Model):
    cod_jar = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_jar = models.CharField(max_length=200)
    comuna_cod_com = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_cod_com')
    comuna_pvcia_cod_prov = models.DecimalField(max_digits=4, decimal_places=0)
    comuna_pvcia_region_cod_reg = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'jardin'


class Jornada(models.Model):
    cod_jor = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_jor = models.CharField(max_length=50)
    jardin_cod_jar = models.ForeignKey(Jardin, models.DO_NOTHING, db_column='jardin_cod_jar')

    class Meta:
        managed = False
        db_table = 'jornada'
        unique_together = (('cod_jor', 'jardin_cod_jar'),)


class KidconnectEvento(models.Model):
    name = models.CharField(max_length=100)
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'kidconnect_evento'


class Msje(models.Model):
    cod_mensaje = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    fch_crea = models.DateField()
    img_msj = models.BinaryField(blank=True, null=True)
    cont_msj = models.CharField(max_length=4000)
    tip_msj_cod_tip_m = models.ForeignKey('TipMsj', models.DO_NOTHING, db_column='tip_msj_cod_tip_m')
    usuario_rut_us = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_us')
    usuario_jardin_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    usuario_tipo_us_cod_tip = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'msje'
        unique_together = (('cod_mensaje', 'tip_msj_cod_tip_m', 'usuario_rut_us', 'usuario_jardin_cod_jar', 'usuario_tipo_us_cod_tip'),)


class Nivel(models.Model):
    cod_niv = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nom_niv = models.CharField(max_length=50)
    jornada_cod_jor = models.ForeignKey(Jornada, models.DO_NOTHING, db_column='jornada_cod_jor')
    jornada_jardin_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'nivel'
        unique_together = (('cod_niv', 'jornada_cod_jor', 'jornada_jardin_cod_jar'),)


class Pvcia(models.Model):
    cod_prov = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nom_prov = models.CharField(max_length=50)
    region_cod_reg = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_cod_reg')

    class Meta:
        managed = False
        db_table = 'pvcia'
        unique_together = (('cod_prov', 'region_cod_reg'),)


class Region(models.Model):
    cod_reg = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_reg = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class TipMsj(models.Model):
    cod_tip_m = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    nom_tip_m = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tip_msj'


class TipoUs(models.Model):
    cod_tip = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_tip = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_us'


class UserPass(models.Model):
    rut_user = models.CharField(primary_key=True, max_length=8)
    pass_user = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'user_pass'


class Usuario(models.Model):
    rut_us = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    dv_us = models.CharField(max_length=1)
    nom_us = models.CharField(max_length=50)
    ap_pat_us = models.CharField(max_length=100)
    ap_mat_us = models.CharField(max_length=100)
    dir_us = models.CharField(max_length=100)
    tel_us = models.DecimalField(max_digits=9, decimal_places=0)
    mail_us = models.CharField(max_length=100)
    jardin_cod_jar = models.ForeignKey(Jardin, models.DO_NOTHING, db_column='jardin_cod_jar')
    tipo_us_cod_tip = models.ForeignKey(TipoUs, models.DO_NOTHING, db_column='tipo_us_cod_tip')

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('rut_us', 'jardin_cod_jar', 'tipo_us_cod_tip'),)
