from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class CustomSerializer(RegisterSerializer):
    is_blog_admin = serializers.BooleanField(default=False)
    is_qa = serializers.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Call the parent save method to create the user
        user = super().save(*args, **kwargs)

        # Set the custom field based on the validated data
        user.is_blog_admin = self.validated_data.get('is_blog_admin', False)
        user.is_qa = self.validated_data.get('is_qa', False)
        user.save() # Save the updated user instance
        return user
