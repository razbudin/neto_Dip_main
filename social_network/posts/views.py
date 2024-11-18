from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Comment, Like
from posts.serializers import CommentSerializer, PostSerializer
from posts.permission import IsOwnerOrReadOnly


# Класс для вывода поста
class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    lst_methods = ['create', 'update', 'pertial_update', 'destroy']

    # Метод получения прав доступа для действий с объектом
    def get_permissions(self):
        if self.action in self.lst_methods:

            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]

    # Метод создания постов с применением токена
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Класс для вывода комментария
class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # Метод создания комментария с применением токена
    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_id'],
                        author=self.request.user)


# Класс лайков
class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    # Метод создания лайков в посте
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if not Like.objects.filter(post=post, author=request.user).exists():
            Like.objects.create(post=post, author=request.user)
        return Response(status=status.HTTP_200_OK)

    # Метод удаления лайков
    def delete(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if Like.objects.filter(post=post, author=request.user).exists():
            Like.objects.filter(post=post, author=request.user).delete()
        return Response(status=status.HTTP_200_OK)
