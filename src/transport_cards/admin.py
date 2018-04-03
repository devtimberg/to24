# encoding: utf-8

from __future__ import unicode_literals

from django.contrib.admin import ModelAdmin, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import TransportCard, User, Price, Insurance
from .forms import UserAddForm, UserChangeForm
from .tasks import create_card_on_server


class TransportCardAdmin(ModelAdmin):
    list_display = ('pk', 'user', 'phone', 'status', 'created')
    list_display_links = list_display
    search_fields = ('user__email',)
    fieldsets = (
        ('Общая информация', {
            'fields': (
                ('user', 'status'),
                ('phone'),
                ('created', 'updated'),
                ('payment_sum', 'payment_id'),
                ('pdf', 'exception'),
            )
        }),
        ('Паспортные данные', {
            'fields': (
                ('FName', 'Name'),
                ('MName', 'Foreign'),
                ('Series', 'Number'),
                ('Organization', 'Date'),
            )
        }),
        ('Данные о ТС', {
            'fields': (
                ('EAISTO_code', 'Validity'),
                ('RegistrationNumber', 'specials'),
                ('VehicleCategory', 'VehicleCategory2'),
                ('Make', 'Model'),
                ('EmptyMass', 'MaxMass'),
                ('Year', 'Killometrage'),
                ('BrakingSystem', 'Fuel'),
                ('Tyres', 'VIN'),
                ('BodyNumber', 'FrameNumber'),
                'DocumentType',
                'Note',
            )
        }),
    )
    readonly_fields = (
        'user', 'phone', 'status', 'pdf', 'created', 'updated',
        'Validity', 'exception', 'EAISTO_code', 'payment_sum', 'payment_id'
    )
    actions = ('restart_tasks', )

    def restart_tasks(self, request, queryset):
        for card in queryset.filter(
                status__in=(
                    TransportCard.SENDING_ERROR,
                    TransportCard.RENDER_ERROR
                )):
            create_card_on_server.delay(card.id)
    restart_tasks.short_description = 'Перезапустить'

    def payment_sum(self, obj):
        return obj.payment.sum
    payment_sum.short_description = 'Сумма платежа'

    def payment_id(self, obj):
        return obj.payment.id
    payment_id.short_description = 'ID платежа'

    def has_add_permission(self, request):
        return False


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserAddForm

    list_display = ('pk', 'email', 'is_active', 'is_staff')
    list_display_links = list_display
    list_filter = ('is_active', 'is_staff', 'groups')
    ordering = ('pk', )

    fieldsets = (
        ('Основное', {
            'fields': (
                'email',
                ('new_password', 'password_repeat'),
            )
        }),
        ('Права', {
            'fields': (
                ('is_active', 'is_staff', 'is_superuser'),
            )
        }),
    )
    add_fieldsets = fieldsets


class PriceAdmin(ModelAdmin):
    list_display = ('pk', 'category', 'sum', 'order', )
    list_editable = ('category', 'sum', 'order', )
    fields = (('category', 'sum'), )
    ordering = ('category',)


class InsuranceAdmin(ModelAdmin):
    list_display = ('name', )


site.register(Insurance, InsuranceAdmin)
site.register(TransportCard, TransportCardAdmin)
site.register(User, UserAdmin)
site.register(Price, PriceAdmin)

