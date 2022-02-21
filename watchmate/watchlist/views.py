# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Movie
# # Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all()
#     context = {
#         'data': list(movies.values())
#     }
#     return JsonResponse(context)

# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk = pk)
#     context = {
#         "name": movie.name,
#         "desc": movie.desc,
#         "active": movie.active
#     }
#     return JsonResponse(context)
    
