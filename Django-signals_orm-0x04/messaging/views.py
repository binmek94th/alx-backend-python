from rest_framework.response import Response
from rest_framework.views import APIView


class UserAPiView(APIView):
    def delete(self, request):
        user = request.user
        if not user:
            return Response({"error": "User not found."}, status=404)
        if not user.is_authenticated:
            return Response({"error": "User not authenticated."}, status=401)
        user.delete()
        return Response({"message": "User account deleted successfully."}, status=204)
