from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import (
    JWTStatelessUserAuthentication)
from .models import User, Paragraphs


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data['password'])
            serializer.save()
            return Response({
                "message": "Registered User Successfully"
            })
        else:
            return Response({
                "message": "Registration Failed"
            })


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(name=serializer.data['name'])
            if user is not None:
                correct_passwd = check_password(
                    serializer.data['password'], user.password)
                if correct_passwd:
                    refresh = RefreshToken.for_user(user)
                    data = {"access_token": str(refresh.access_token)}
                    return Response(
                        {
                            "message": "Login Successfull",
                            "data": data
                        },

                        status=status.HTTP_200_OK
                    )
                else:
                    return Response({
                        "message": "Invalid password"
                    })
            else:
                return Response(
                    {
                        "message": "Invalid username or password"
                    },
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {
                    "message": "Incorrect username or password were provided",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class WordSearch(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JWTStatelessUserAuthentication, )

    def post(self, request):
        word = request.data["word"]
        word = word.lower()
        print(word)
        """
        find all paragraphs of the containing word
        """
        word_search = Paragraphs.objects.filter(paragraph__contains=word)
        para_count = []
        print(word_search)
        for words in word_search:
            wordname = f"Paragraph {words.id}"
            para_count.append(wordname)

        if len(para_count) > 1:
            return Response({
                "message": "Found Words In",
                "paragraphs": para_count
            })
        else:
            return Response({
                "message": "Words not found"
            })
