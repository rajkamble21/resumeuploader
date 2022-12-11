from myapp.models import Resume
from rest_framework import serializers


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']

        


    