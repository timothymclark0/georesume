from django.shortcuts import render
from django.http import JsonResponse
from .models import JobExperience
from pathlib import Path
import portfolio.settings as settings
import json
import os

def resume_view(request):
    jobs = JobExperience.objects.all()
    return render(request, 'resume/resume.html', {'jobs': jobs})


def job_geojson(request):
    job_id = request.GET.get('job_id')
    if not job_id:
        return JsonResponse({'error': 'No job ID provided'}, status=400)
    
    # Path to your TopoJSON files (adjust as needed)
    filepath = Path(settings.BASE_DIR) / 'topojson' / f'job_{job_id}.json'
    
    # Check if the file exists
    if not os.path.exists(filepath):
        # Return an empty but valid TopoJSON structure instead of an error
        return JsonResponse({
            "type": "Topology",
            "objects": {},
            "arcs": [],
            "transform": {
                "scale": [1, 1],
                "translate": [0, 0]
            }
        })
    
    try:
        with open(filepath, 'r') as f:
            topojson_data = json.load(f)
        
        return JsonResponse(topojson_data)
    except json.JSONDecodeError:
        # Handle malformed JSON files
        return JsonResponse({
            "type": "Topology",
            "objects": {},
            "arcs": [],
            "transform": {
                "scale": [1, 1],
                "translate": [0, 0]
            }
        })
    except Exception as e:
        # Catch any other errors
        return JsonResponse({
            "type": "Topology",
            "objects": {},
            "arcs": [],
            "transform": {
                "scale": [1, 1],
                "translate": [0, 0]
            }
        })

def job_data_json(request):
    """API endpoint to get job data in JSON format for D3"""
    jobs = JobExperience.objects.all()
    data = [{
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'city': job.city,
        'state': job.state,
        'latitude': job.latitude,
        'longitude': job.longitude,
        'start_date': job.start_date.strftime('%Y-%m-%d'),
        'end_date': job.end_date.strftime('%Y-%m-%d') if job.end_date else None,
        'is_current': job.is_current,
    } for job in jobs]
    
    return JsonResponse(data, safe=False)