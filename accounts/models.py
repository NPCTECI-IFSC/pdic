# encoding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):

    def create_user(self, email, nome, password=None):
        user = self.model(
            email=self.normalize_email(email),
            nome=nome
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(
            email,
            nome,
            password=password
        )
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True, db_column='id_usuario')
    nome = models.CharField(
        verbose_name=u'Nome',
        max_length=100,
        db_column='nome_usuario'
    )
    email = models.EmailField(
        verbose_name=u'E-mail',
        max_length=100,
        unique=True,
        db_column='email_usuario'
    )
    regiao = models.CharField(
        verbose_name=u'Região',
        max_length=100,
        blank=True,
        null=True,
        db_column='regiao_usuario'
    )
    ativo = models.BooleanField(
        verbose_name=u'Ativo',
        default=True,
        db_column='ativa_usuario'
    )
    is_admin = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        db_table = 'tb_usuario'
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
