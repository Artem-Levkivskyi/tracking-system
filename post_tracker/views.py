from django.shortcuts import render
from post_tracker.forms import TrackForm
from .models import Track, TrackPoint, Country, City, Statuses


# Представление для рендеринга главного окна
def track_page(request):
    return render(request, 'track_page.html', {})


# Представление для рендеринга окна результатов поиска
def search_track(request):
    # Проверяем запрос к представлению на метод запроса GET и на валидность
    # Забираем значение, которое в форму ввел пользователь
    track_id = "not defined"

    if request.method == "GET":
        check_track_form = TrackForm(request.GET)

        if check_track_form.is_valid():
            track_id = check_track_form.cleaned_data['track_id']

    # На основании полученного от пользователя id получаем объекты, атрибут track_id которых ищет пользователь
    track_box = Track.objects.filter(track_id=track_id).order_by('track_date')

    track_history = []

    # Обрабатываем циклом полученный кортеж значений и извлекаем из связанных таблиц нужную для вывода информацию
    # В конце каждой итерации упорядочено ложим полученные значения в список track_history
    for point in track_box:
        datetime = point.track_date

        post = TrackPoint.objects.filter(point_id=point.point_id).values_list('country_short', 'city_id')

        country = Country.objects.filter(id=post[0][0]).values_list('english', flat=True)
        city = City.objects.filter(id=post[0][1]).values_list('english', flat=True)

        status = Statuses.objects.filter(status_id=point.status_id).values_list('english', flat=True)

        track_history.append((datetime.date(), datetime.time(), country[0], city[0], status[0]))

    # Рендерим шаблон и накладіваем шаблон на ранее сформированный список track_history
    return render(request, 'search_track.html', {'track': track_history})
