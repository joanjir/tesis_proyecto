from typing import re

from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

# autenticarse por ususario y contraseña

    # request.session.flush()
    del request.session['user_id']    
    return HttpResponseRedirect(reverse('home'))