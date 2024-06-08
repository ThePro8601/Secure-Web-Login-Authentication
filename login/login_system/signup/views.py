from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

def signup(request):
    if request.method == "POST":
        # Connect to the database
        m = sql.connect(host="localhost", user="root", password='12345', database='website')
        cursor = m.cursor()

        # Get form data
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        gender = request.POST.get('Gender', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Insert data into the database
        cursor.execute("INSERT INTO users (first_name, last_name, gender, email, password) VALUES (%s, %s, %s, %s, %s)",
                       (first_name, last_name, gender, email, password))
        
        # Commit changes and close the database connection
        m.commit()
        m.close()

    return render(request, 'signup_page.html')
