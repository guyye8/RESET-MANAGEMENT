import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django.utils import translation
from django.conf import settings

# ✅ absolute imports
from recipes.models import Recipe
from recipes.helper import to_recipe_data_transfer_objects


@csrf_exempt
def recipe_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"message": "Unauthorized"}, status=401)

    if request.method == "DELETE":
        data = json.loads(request.body)
        if not data.get("id"):
            return JsonResponse({"message": "Id required."}, status=400)

        Recipe.objects.get(pk=data.get("id")).delete()
        return JsonResponse({"message": "Success"}, status=200)

    return JsonResponse({"message": "Method not allowed."}, status=405)


def recipes_api(request, page_no):
    if not request.user.is_authenticated:
        return JsonResponse({"message": "Unauthorized"}, status=401)

    try:
        query_string = request.GET.get("q")
        if query_string:
            recipe_query_set = Recipe.objects.filter(
                models.Q(name__icontains=query_string) |
                models.Q(ingredients__ingredient__icontains=query_string)
            ).distinct()
        else:
            recipe_query_set = Recipe.objects.all()

        paginator = Paginator(recipe_query_set.order_by("name"), settings.RECIPE_ENTRIES_PER_PAGE)
        cur_page = min(page_no, paginator.num_pages)
        page = paginator.page(cur_page)

        recipe_dto_list = to_recipe_data_transfer_objects(page.object_list)

    except EmptyPage:
        return JsonResponse({"message": "Bad request"}, status=400)

    return JsonResponse({
        "recipes": recipe_dto_list,
        "hasNext": page.has_next(),
        "hasPrevious": page.has_previous(),
        "numPages": paginator.num_pages,
        "curPage": cur_page
    }, status=200)


@csrf_exempt
def language_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lang_code = data.get("langCode")

        if not lang_code:
            return JsonResponse({"message": "langCode required."}, status=400)

        translation.activate(lang_code)
        response = JsonResponse({"message": f"Language \"{lang_code}\" set."}, status=200)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response

    return JsonResponse({"message": "Method not allowed."}, status=405)
