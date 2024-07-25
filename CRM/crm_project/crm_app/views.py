from rest_framework import viewsets
from .models import Organization, Contact, Deal
from .serializers import OrganizationSerializer, ContactSerializer, DealSerializer

"""
Username: admin
Email address: admin@example.com
Password: adminuser

"""
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
