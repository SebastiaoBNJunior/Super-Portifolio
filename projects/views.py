from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Certificate, CertifyingInstitution, Profile, Project
from .serializers import (CertificateSerializer,
                          CertifyingInstitutionSerializer,
                          ProfileSerializer, ProjectSerializer)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    authentication_classes = [JWTAuthentication]


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    authentication_classes = [JWTAuthentication]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile = get_object_or_404(Profile, id=kwargs["pk"])
            certificates = Certificate.objects.filter(profiles=profile)
            projects = Project.objects.filter(profile=profile)
            return render(request, "profile_detail.html", {
                "profile": profile, "certificates": certificates,
                "projects": projects})
       
        return super().retrieve(request, *args, **kwargs)
