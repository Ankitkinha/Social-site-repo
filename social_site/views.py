from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Post
from .serializers import UserSerializer, PostSerializer


@api_view(['POST'])
def signup(request):
    """
    API endpoint to create a new user (signup) and generate a token.
    """
    data = request.data
    try:
        user = User.objects.create(
            email=data['email'],
            mobile_no=data['mobile_no'],
            name=data['name'],
            password=data['password']
        )
        serializer = UserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    """
    API endpoint to authenticate a user (login) and generate a token.
    """
    data = request.data
    email = data.get('email')
    password = data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please provide both email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email, password=password)
    if user is not None:
        serializer = UserSerializer(user[0])
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def get_user(self, request):
        query = request.query_params.get('name', '')
        users = User.objects.filter(name__icontains=query)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['put'])
    def update_user(self, request):
        """
        API endpoint to update the user's name, email, and mobile number.
        """
        data = request.data
        current_email = data.get('email')
        current_mobile_no = data.get('mobile_no')
        new_name = data.get('name')
        new_email = data.get('new_email')
        new_mobile_no = data.get('new_mobile_no')

        if not current_email or not current_mobile_no:
            return Response({'error': 'Current email and mobile number are required.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not new_name and not new_email and not new_mobile_no:
            return Response({'error': 'At least one field to update must be provided.'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=current_email, mobile_no=current_mobile_no)

            if new_email and User.objects.exclude(pk=user.pk).filter(email=new_email).exists():
                return Response({'error': 'Email already in use.'}, status=status.HTTP_400_BAD_REQUEST)
            if new_mobile_no and User.objects.exclude(pk=user.pk).filter(mobile_no=new_mobile_no).exists():
                return Response({'error': 'Mobile number already in use.'}, status=status.HTTP_400_BAD_REQUEST)

            if new_name:
                user.name = new_name
            if new_email:
                user.email = new_email
            if new_mobile_no:
                user.mobile_no = new_mobile_no

            user.save()
            serializer = UserSerializer(user)
            return Response({'message': 'Successfully Updated', 'user': serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'])
    def delete_user(self, request):
        """
        API endpoint to delete user.
        """
        data = request.data
        email = data.get('email')
        mobile_no = data.get('mobile_no')

        if not email or not mobile_no:
            return Response({'error': 'Current email and mobile number are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user_obj = User.objects.filter(email=email, mobile_no=mobile_no)
            user_obj.delete()
            return Response({'message': 'Successfully Deleted'},  status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def list_users(self, request):
        """
        API endpoint to list all users.
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=False, methods=['post'], url_path='post_create')
    def create_post(self, request, *args, **kwargs):
        data = request.data
        user_id = data.get('user')
        print("USER ID ============= :", user_id)

        if not user_id:
            return Response({'error': 'User ID must be provided in the request data.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        data['user'] = user.id  # Set the user to the user provided in the request

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['put'], url_path='update_post')
    def update_post(self, request):
        data = request.data
        pk = data.get('post')
        try:
            post = Post.objects.get(pk=pk)
            if 'text' in data:
                post.text = data['text']
            if 'image' in data:
                post.image = data['image']
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'], url_path='delete_post')
    def delete_post(self, request):
        data = request.data
        pk = data.get('post')
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'message': 'Post deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='posts_tag')
    def get_posts_by_tag(self, request):
        tag = request.query_params.get('tag')
        if not tag:
            return Response({'error': 'Tag parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        posts = Post.objects.filter(post_hashtags__hashtag__tag=tag)
        if not posts:
            return Response({'error': 'Post for this Tag DoesNotExists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='posts_text')
    def get_posts_by_text(self, request):
        text = request.query_params.get('text')
        if not text:
            return Response({'error': 'Text parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        posts = Post.objects.filter(text__icontains=text)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


