# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class JobDiversity(models.Model):
    msa = models.ForeignKey('Unemployment', models.DO_NOTHING, primary_key=True)
    msa_name = models.CharField(max_length=255, blank=True, null=True)
    agriculture_pe = models.FloatField(db_column='agriculture_PE', blank=True, null=True)  # Field name made lowercase.
    construction_pe = models.FloatField(db_column='construction_PE', blank=True, null=True)  # Field name made lowercase.
    manufacturing_pe = models.FloatField(db_column='manufacturing_PE', blank=True, null=True)  # Field name made lowercase.
    wholesale_pe = models.FloatField(db_column='wholesale_PE', blank=True, null=True)  # Field name made lowercase.
    retail_pe = models.FloatField(db_column='retail_PE', blank=True, null=True)  # Field name made lowercase.
    transportation_pe = models.FloatField(db_column='transportation_PE', blank=True, null=True)  # Field name made lowercase.
    it_pe = models.FloatField(db_column='IT_PE', blank=True, null=True)  # Field name made lowercase.
    business_pe = models.FloatField(db_column='business_PE', blank=True, null=True)  # Field name made lowercase.
    scientific_pe = models.FloatField(db_column='scientific_PE', blank=True, null=True)  # Field name made lowercase.
    educational_pe = models.FloatField(db_column='educational_PE', blank=True, null=True)  # Field name made lowercase.
    entertainment_pe = models.FloatField(db_column='entertainment_PE', blank=True, null=True)  # Field name made lowercase.
    other_pe = models.FloatField(db_column='other_PE', blank=True, null=True)  # Field name made lowercase.
    public_admin_pe = models.FloatField(db_column='public_admin_PE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'job_diversity'


class MedianRent(models.Model):
    msa = models.ForeignKey('Unemployment', models.DO_NOTHING, primary_key=True)
    msa_name = models.CharField(max_length=255, blank=True, null=True)
    median_rent = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'median_rent'


class Population(models.Model):
    msa = models.ForeignKey('Unemployment', models.DO_NOTHING, primary_key=True)
    msa_name = models.CharField(max_length=255, blank=True, null=True)
    total_ppl = models.IntegerField(blank=True, null=True)
    ppl_lessthan5_pe = models.FloatField(db_column='ppl_lessthan5_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_5to9_pe = models.FloatField(db_column='ppl_5to9_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_10to14_pe = models.FloatField(db_column='ppl_10to14_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_15to19_pe = models.FloatField(db_column='ppl_15to19_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_20to24_pe = models.FloatField(db_column='ppl_20to24_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_25to34_pe = models.FloatField(db_column='ppl_25to34_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_35to44_pe = models.FloatField(db_column='ppl_35to44_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_45to54_pe = models.FloatField(db_column='ppl_45to54_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_55to59_pe = models.FloatField(db_column='ppl_55to59_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_60to64_pe = models.FloatField(db_column='ppl_60to64_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_65to74_pe = models.FloatField(db_column='ppl_65to74_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_75to84_pe = models.FloatField(db_column='ppl_75to84_PE', blank=True, null=True)  # Field name made lowercase.
    ppl_morethan85_pe = models.FloatField(db_column='ppl_morethan85_PE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'population'


class RentalVacancy(models.Model):
    msa = models.ForeignKey('Unemployment', models.DO_NOTHING, primary_key=True)
    msa_name = models.CharField(max_length=255, blank=True, null=True)
    rental_vacancy_pe = models.FloatField(db_column='rental_vacancy_PE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'rental_vacancy'


class Unemployment(models.Model):
    msa = models.CharField(primary_key=True, max_length=255)
    msa_name = models.CharField(max_length=255, blank=True, null=True)
    unemployed_pe = models.FloatField(db_column='unemployed_PE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'unemployment'
