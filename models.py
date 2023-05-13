# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    cod_user = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    pass_field = models.CharField(db_column='pass', max_length=100)  # Field renamed because it was a Python reserved word.
    per_est_rut_pe = models.ForeignKey('PerEst', models.DO_NOTHING, db_column='per_est_rut_pe')
    per_est_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    apod_rut_apo = models.ForeignKey('Apod', models.DO_NOTHING, db_column='apod_rut_apo')
    apod_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    tipo_us_cod_tip = models.ForeignKey('TipoUs', models.DO_NOTHING, db_column='tipo_us_cod_tip')

    class Meta:
        managed = False
        db_table = 'USER'
        unique_together = (('cod_user', 'per_est_rut_pe', 'per_est_cod_jar', 'apod_rut_apo', 'apod_cod_jar', 'tipo_us_cod_tip'),)


class Alumno(models.Model):
    rut_alu = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    dv_alu = models.CharField(max_length=1)
    nom_alu = models.CharField(max_length=100)
    ap_pat_alu = models.CharField(max_length=100)
    ap_mat_alu = models.CharField(max_length=100)
    dir_alu = models.CharField(max_length=100)
    apod_rut_apo = models.ForeignKey('Apod', models.DO_NOTHING, db_column='apod_rut_apo')
    apod_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    fc_est_cod_fc = models.OneToOneField('FcEst', models.DO_NOTHING, db_column='fc_est_cod_fc')
    curso_cod_cur = models.ForeignKey('Curso', models.DO_NOTHING, db_column='curso_cod_cur')
    curso_cod_niv = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'alumno'
        unique_together = (('rut_alu', 'apod_rut_apo', 'apod_cod_jar', 'curso_cod_cur', 'curso_cod_niv'),)


class Apod(models.Model):
    rut_apo = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    dv = models.CharField(max_length=1)
    nom_apo = models.CharField(max_length=100)
    ap_pat_apo = models.CharField(max_length=100)
    ap_mat_apo = models.CharField(max_length=100)
    dir_apo = models.CharField(max_length=100)
    tel_apo = models.DecimalField(max_digits=9, decimal_places=0)
    mail_apo = models.CharField(max_length=100)
    jardin_cod_jar = models.ForeignKey('Jardin', models.DO_NOTHING, db_column='jardin_cod_jar')

    class Meta:
        managed = False
        db_table = 'apod'
        unique_together = (('rut_apo', 'jardin_cod_jar'),)


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

    class Meta:
        managed = False
        db_table = 'curso'
        unique_together = (('cod_cur', 'nivel_cod_niv'),)


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


class FcDoc(models.Model):
    cod_fc_dc = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    fec_cre = models.DateField()
    img_fc = models.BinaryField(blank=True, null=True)
    nom_dc = models.CharField(max_length=100)
    con_fc_dc = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fc_doc'


class FcEst(models.Model):
    cod_fc = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    nom_alu = models.CharField(max_length=100)
    ap_pat_alu = models.CharField(max_length=100)
    ap_mat_alu = models.CharField(max_length=100)
    fec_cre = models.DateField()
    con_fc = models.CharField(max_length=3000)
    img_est = models.BinaryField(blank=True, null=True)
    alumno_rut_alu = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='alumno_rut_alu')
    alumno_rut_apo = models.DecimalField(max_digits=8, decimal_places=0)
    alumno_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    alumno_cod_cur = models.DecimalField(max_digits=4, decimal_places=0)
    alumno_cod_niv = models.DecimalField(max_digits=4, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'fc_est'
        unique_together = (('alumno_rut_alu', 'alumno_rut_apo', 'alumno_cod_jar', 'alumno_cod_cur', 'alumno_cod_niv'),)


class Jardin(models.Model):
    cod_jar = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_jar = models.CharField(max_length=200)
    comuna_cod_com = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_cod_com')
    comuna_pvcia_cod_prov = models.DecimalField(max_digits=4, decimal_places=0)
    comuna_pvcia_region_cod_reg = models.DecimalField(max_digits=2, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'jardin'


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
    user_cod_user = models.ForeignKey(User, models.DO_NOTHING, db_column='user_cod_user')
    user_per_est_rut_pe = models.DecimalField(max_digits=8, decimal_places=0)
    user_per_est_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    user_apod_rut_apo = models.DecimalField(max_digits=8, decimal_places=0)
    user_apod_cod_jar = models.DecimalField(max_digits=2, decimal_places=0)
    user_tipo_us_cod_tip = models.DecimalField(max_digits=2, decimal_places=0)
    tip_msj_cod_tip_m = models.ForeignKey('TipMsj', models.DO_NOTHING, db_column='tip_msj_cod_tip_m')

    class Meta:
        managed = False
        db_table = 'msje'
        unique_together = (('cod_mensaje', 'user_cod_user', 'user_per_est_rut_pe', 'user_per_est_cod_jar', 'user_apod_rut_apo', 'user_apod_cod_jar', 'user_tipo_us_cod_tip', 'tip_msj_cod_tip_m'),)


class Nivel(models.Model):
    cod_niv = models.DecimalField(primary_key=True, max_digits=4, decimal_places=0)
    nom_niv = models.CharField(max_length=50)
    jardin_cod_jar = models.ForeignKey(Jardin, models.DO_NOTHING, db_column='jardin_cod_jar')

    class Meta:
        managed = False
        db_table = 'nivel'


class PerEst(models.Model):
    rut_pe = models.DecimalField(primary_key=True, max_digits=8, decimal_places=0)
    dv_pe = models.CharField(max_length=1)
    nom_pe = models.CharField(max_length=100)
    ap_pat_pe = models.CharField(max_length=100)
    ap_mat_pe = models.CharField(max_length=100)
    dir_pe = models.CharField(max_length=100)
    tel_pe = models.DecimalField(max_digits=9, decimal_places=0)
    mail_pe = models.CharField(max_length=100)
    jardin_cod_jar = models.ForeignKey(Jardin, models.DO_NOTHING, db_column='jardin_cod_jar')

    class Meta:
        managed = False
        db_table = 'per_est'
        unique_together = (('rut_pe', 'jardin_cod_jar'),)


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
    nom_tip_m = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tip_msj'


class TipoUs(models.Model):
    cod_tip = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nom_tip = models.CharField(max_length=100)
    fc_doc_cod_fc_dc = models.OneToOneField(FcDoc, models.DO_NOTHING, db_column='fc_doc_cod_fc_dc')

    class Meta:
        managed = False
        db_table = 'tipo_us'
