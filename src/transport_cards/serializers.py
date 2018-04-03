# encoding: utf-8

from __future__ import unicode_literals

from rest_framework import serializers

from .models import TransportCard


class TransportCardSerializer(serializers.ModelSerializer):
    VehicleCategory2 = serializers.SerializerMethodField()

    def get_VehicleCategory2(self, obj):
        return obj.get_VehicleCategory2_display()

    class Meta:
        model = TransportCard
        fields = (
            # Паспортные данные
            'FName', 'Name', 'MName', 'Series', 'Number',
            'Organization', 'Date', 'Foreign',

            # Данные о ТС
            'BodyNumber', 'Note', 'RegistrationNumber',
            'VehicleCategory', 'VehicleCategory2', 'VIN', 'Year',
            'FrameNumber', 'EmptyMass', 'MaxMass', 'Fuel', 'Tyres',
            'BrakingSystem', 'Killometrage', 'Make', 'Model',
            'DocumentType', 'Validity',
        )
