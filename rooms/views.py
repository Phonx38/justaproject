from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
import rooms.models as room_models


class HomeView(ListView):

    model = room_models.Room
    paginate_by = 10
    orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def room_details(request, pk):
    try:
        room = room_models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", context={"room": room})
    except room_models.Room.DoesNotExist:
        raise Http404()


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     rooms_list = room_models.Room.objects.all()
#     paginator = Paginator(rooms_list, 10, orphans=5)

#     try:
#         rooms = paginator.page(int(page))
#         return render(
#             request,
#             "rooms/home.html",
#             context={
#                 "page": rooms,
#             },
#         )
#     except EmptyPage:
#         return redirect("/")
