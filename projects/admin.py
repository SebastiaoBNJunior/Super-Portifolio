from django.contrib import admin
from .models import CertifyingInstitution, Profile
from .models import Certificate


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Profile)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
