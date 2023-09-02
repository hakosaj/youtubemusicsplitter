from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import get_playlist_from_url
import json

class StringView(APIView):
    def post(self, request):
        received_string = request.data.get('inputString', None)
        if received_string:
            try:
                playlist_itemdata,playlist_name,playlist_channel, thumbnail_url, playlist_length=get_playlist_from_url(received_string)

                
                return Response({"playlist_name": playlist_name, "playlist_channel": playlist_channel, "thumbnail_url":thumbnail_url, "playlist_length":playlist_length},status=status.HTTP_200_OK)
            
            except Exception as e:
                return Response({"error": "Failed to fetch the playlist statistics"},status=status.HTTP_400_BAD_REQUEST)
            
        return Response({"error": "No string provided."}, status=status.HTTP_400_BAD_REQUEST)
