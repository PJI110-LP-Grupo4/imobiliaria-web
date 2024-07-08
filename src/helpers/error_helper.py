from django.shortcuts import redirect
from django.contrib import messages


def tratar_errors(form, request):
    for field in form:
        for error in field.errors:
            messages.warning(request, error)
