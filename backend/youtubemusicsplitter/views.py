from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import get_playlist_from_url
import json

class StringView(APIView):
    def post(self, request):
        received_string = request.data.get('inputString', None)
        if received_string:
            playlist_itemdata,playlist_name,playlist_channel=get_playlist_from_url(received_string)

            return Response({"message": f"URL received successfully! Playlist in question: {playlist_name} by {playlist_channel}"}, status=status.HTTP_200_OK)
        return Response({"error": "No string provided."}, status=status.HTTP_400_BAD_REQUEST)
