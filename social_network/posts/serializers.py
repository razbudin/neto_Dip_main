from rest_framework import serializers
from posts.models import Post, Comment


# Сериализатор комментария
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']
        read_only_fields = ['author']


# Сериализатор поста
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments']

    # Сериализатор лайка
    def to_representation(self, post):
        representation = super().to_representation(post)
        representation['likes_count'] = post.likes.count()
        return representation
