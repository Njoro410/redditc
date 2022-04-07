from rest_framework.response import Response
from rest_framework.decorators import api_view
from reddit.models import Articles, Rooms
from .serializers import ArticleSerializer, RoomSerializer

@api_view(['GET'])
def getArticles(request):
    articles = Articles.objects.all()
    serializer = ArticleSerializer(articles, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getRooms(request):
    rooms = Rooms.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def roomCreate(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def articleDetail(request,pk):
    article = Articles.objects.get(id=pk)
    serializer = ArticleSerializer(article, many = False)
    return Response(serializer.data)


@api_view(['POST'])
def articleUpdate(request,pk):
    article = Articles.objects.get(id=pk)
    serializer = ArticleSerializer(instance=article,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def articleDelete(request,pk):
    article = Articles.objects.get(id=pk)
    article.delete()
    return Response('deleted successfully')