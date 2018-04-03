# encoding: utf-8

from __future__ import unicode_literals

from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время последнего изменения'
    )

    class Meta:
        abstract = True


class CATEGORIES(object):
    A, B, C, D, E = ('A', 'B', 'C', 'D', 'E')
    L, M1, M2, M3, N1, N2, N3, O1, O2, O3, O4 = (
        'L', 'M1', 'M2', 'M3', 'N1', 'N2', 'N3', 'O1', 'O2', 'O3', 'O4'
    )
    PTS = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
        (E, 'E'),
    )
    OKP = (
        ('A', (
            (L, 'Мототранспорт L'),
        )),
        ('B', (
            (M1, 'Легковой M1'),
            (N1, 'Грузовой до 3.5 тонн N1'),
        )),
        ('C', (
            (N2, 'Грузовой до 12 тонн N2'),
            (N3, 'Грузовой более 12 тонн N3'),
        )),
        ('D', (
            (M2, 'Автобусы до 5 тонн M2'),
            (M3, 'Автобусы более 5 тонн M3'),
        )),
        ('E', (
            (O1, 'Прицепы до 150 кг O1'),
            (O2, 'Прицепы до 3.5 тонн O2'),
            (O3, 'Прицепы до 10 тонн O3'),
            (O4, 'Прицепы более 10 тонн O4'),
        )),
    )
    LINKED = {
        L: A,
        M1: B,
        N1: B,
        N2: C,
        N3: C,
        M2: D,
        M3: D,
        O1: E,
        O2: E,
        O3: E,
        O4: E,
    }

    TAXI, LEARNING_OR_MVD = ('taxi', 'MVD')
    SPECIAL = (
        (TAXI, 'Является cпецтехникой или такси'),
        (LEARNING_OR_MVD, 'Является учебной или принадлежит ГИБДД или МВД'),
    )
