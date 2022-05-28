from django.http import HttpResponse


# Поздравляю, это ваш первый контроллер, который может, принять запрос, и отдать ответ с текстом, больше ничего
def main(request):
    return HttpResponse("Hey! It's your main view!!")


def another(request):
    return HttpResponse("It's another page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def regex(request, text):
    return HttpResponse(f"it's regexp with text: {text}")