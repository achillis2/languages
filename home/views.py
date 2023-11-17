from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import activate


# Create your views here.
def index(request):
    # activate("en")
    text = _("this is some random text")
    return render(request, "home.html", {"text": text})
