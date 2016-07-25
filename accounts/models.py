# encoding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):

    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError(u'É necessário um e-mail para criar um usuário')
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
    nome = models.CharField(max_length=100, db_column='nome_usuario')
    email = models.EmailField(
        max_length=100,
        unique=True,
        db_column='email_usuario'
    )
    regiao = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        db_column='regiao_usuario'
    )
    ativo = models.BooleanField(default=True, db_column='ativa_usuario')
    is_admin = models.BooleanField(default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        db_table = 'tb_usuario'
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
