from rest_framework.permissions import BasePermission


# Класс проверки пользователя на доступ к постам и комментариям
class IsOwnerOrReadOnly(BasePermission):

    # Метод проверки прав на конкретный объект
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.author
