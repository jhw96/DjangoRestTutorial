from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

# View : Queryset을 컨트롤하고 데이터를 조작해 Serializer을 통해 매핑시켜주는 역할
# Create your views here.

class PostView(viewsets.ModelViewSet) :
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes  = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)