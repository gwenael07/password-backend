from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request  
from .utils import password_generator


@api_view(['POST'])
def generate_password_api(request: Request):
    """Reçoit les critères en JSON et renvoie le mot de passe généré."""

    length = request.data.get('length', 8)
    use_upper = request.data.get('use_upper', False)
    use_digits = request.data.get('use_digits', False)
    use_special = request.data.get('use_special', False)

    try:
        password = password_generator(
            length=int(length),
            use_upper=use_upper,
            use_digits=use_digits,
            use_special=use_special
        )
        return Response({'password': password}, status=status.HTTP_200_OK)

    except ValueError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)