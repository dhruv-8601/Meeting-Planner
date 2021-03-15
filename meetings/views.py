from django.shortcuts import render, get_list_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
from meetings.models import Meeting, Room


def detail(request, id):
    meeting = get_list_or_404(Meeting, pk=id)[0]  # Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meetings": meeting})
    # adding something before meetings in the middle will not change because of url template tag
    # when not using url tag there must be no dictionary {meetings:meeting}


def rooms_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Room.objects.all()})


# This will create html template using Meeting method/model
# and exclude will create all the fields for Meeting variables as we create it as empty list
MeetingForm = modelform_factory(Meeting, exclude=[])    # here MeetingForm is a class


def new(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})


# PLease add a new page that shows a list of all rooms objects
# (Just text, no links)

# Create a:
# - view
# - template
# - url mapping
