from django.db import connection
from django.db import utils
from django.shortcuts import render, redirect, HttpResponse

def my_custom_sql(request):
    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW nopension")
    return HttpResponse("refresh")
    
        