from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
import face_recognition
import numpy as np
import base64
from PIL import Image
import io
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Basic view functions
def index(request):
    return render(request, 'home/welcome.html')

def login(request):
    return render(request, 'session/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('/login')

def success(request):
    return render(request, 'home/welcome.html')

# User management
def addUser(request):
    return render(request, 'home/add_user.html')

def add_user(request):
    # Implementation for adding a user
    return redirect('/success')

def viewUsers(request):
    # Implementation for viewing users
    return render(request, 'home/view_users.html')

def delete_user(request, user_id):
    # Implementation for deleting a user
    return redirect('/view_users')

# Citizen management
def addCitizen(request):
    return render(request, 'home/add_citizen.html')

def saveCitizen(request):
    # Implementation for saving a citizen
    return redirect('/success')

def viewCitizens(request):
    # Implementation for viewing citizens
    return render(request, 'home/view_citizenz.html')

def wantedCitizen(request, citizen_id):
    # Implementation for marking a citizen as wanted
    return redirect('/view_citizens')

def freeCitizen(request, citizen_id):
    # Implementation for marking a citizen as free
    return redirect('/view_citizens')

# Detection functions
def detectImage(request):
    if request.method == 'POST':
        # Implementation for detecting faces in an uploaded image
        return redirect('/success')
    return render(request, 'home/upload_pic.html')

def detectWithWebcam(request):
    return render(request, 'home/webcam.html')

@csrf_exempt
def process_frame(request):
    if request.method == 'POST':
        try:
            # Get the frame data from the request
            frame_data = request.POST.get('frame_data')
            
            # Remove the data URL prefix
            frame_data = frame_data.split(',')[1]
            
            # Convert base64 to image
            image_data = base64.b64decode(frame_data)
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to numpy array
            frame = np.array(image)
            
            # Detect faces in the frame
            face_locations = face_recognition.face_locations(frame)
            
            # Draw boxes around faces
            for (top, right, bottom, left) in face_locations:
                # Draw a box around the face
                for y in range(top, bottom):
                    frame[y, left] = [255, 0, 0]  # Red line on left
                    frame[y, right] = [255, 0, 0]  # Red line on right
                for x in range(left, right):
                    frame[top, x] = [255, 0, 0]  # Red line on top
                    frame[bottom, x] = [255, 0, 0]  # Red line on bottom
            
            # Convert the processed frame back to base64
            processed_image = Image.fromarray(frame)
            buffered = io.BytesIO()
            processed_image.save(buffered, format="JPEG")
            processed_frame = base64.b64encode(buffered.getvalue()).decode()
            
            return JsonResponse({
                'success': True,
                'processed_frame': processed_frame
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    })

# Thief tracking
def spottedCriminals(request):
    # Implementation for viewing spotted criminals
    return render(request, 'home/spotted_thiefs.html')

def viewThiefLocation(request, thief_id):
    # Implementation for viewing a thief's location
    return render(request, 'home/view_location.html')

def foundThief(request, thief_id):
    # Implementation for marking a thief as found
    return redirect('/spotted_criminals')

# Reports
def viewReports(request):
    # Implementation for viewing reports
    return render(request, 'home/reports.html')

# File upload
class FileView(View):
    def get(self, request):
        return render(request, 'home/upload_pic.html')
    
    def post(self, request):
        # Implementation for file upload
        return redirect('/success') 