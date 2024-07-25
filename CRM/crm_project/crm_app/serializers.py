from rest_framework import serializers
from .models import Organization, Contact, Deal

class OrganizationSerializer(serializers.ModelSerializer):
    last_deal_date = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields = '__all__'

    def get_last_deal_date(self, obj):
        last_deal = obj.deals.order_by('-date_created').first()
        return last_deal.date_created if last_deal else None

class ContactSerializer(serializers.ModelSerializer):
    last_deal_date = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = '__all__'

    def get_last_deal_date(self, obj):
        last_deal = obj.deals.order_by('-date_created').first()
        return last_deal.date_created if last_deal else None

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
