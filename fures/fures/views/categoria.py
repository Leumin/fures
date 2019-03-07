from django.http import HttpResponse,JsonResponse
from ..models import Categoria
from django.core import serializers
from django.core.exceptions import ValidationError
