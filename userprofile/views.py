from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from .serializers import UserProfileSerializers






class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user

            userprofile = UserProfile.objects.get(user=user)
            userprofile = UserProfileSerializers(userprofile)

            return Response(
                {'profile': userprofile.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving profile'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user

            data = self.request.data
            address_line_1 = data['address_line_1']
            address_line_2 = data['address_line_2']
            city = data['city']
            state_province_region = data['state_province_region']
            zipcode = data['zipcode']
            phone = data['phone']
          

            UserProfile.objects.filter(user=user).update(
                address_line_1=address_line_1,
                address_line_2=address_line_2,
                city=city,
                state_province_region=state_province_region,
                zipcode=zipcode,
                phone=phone,
             
            )

            userprofile = UserProfile.objects.get(user=user)
            userprofile = UserProfileSerializers(userprofile)

            return Response(
                {'profile': userprofile.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when updating profile'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )