from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pandas as pd
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from query.models import ResonanceResult

# Create your views here.

def showIntro():
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++---------------------------------BRAINY NOISE QUERY SERVICE-------------------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++")
    print("+++++--------------------------Jessica N. , Estefanía B. , Sebastián V. -----------------------------+++++")
    print("+++++------------------------------------------------------------------------------------------------+++++")


@csrf_exempt
@api_view(['GET'])
def getAllResultsByEmail(request):
    showIntro()
    email = request.GET.get('email')
    results = ResonanceResult.objects.filter(email=email)
    
    if(len(results)>0):
        results_list = [dict(item, **{'_id': str(item['_id'])}) for item in results.values()]
        result_message= {"State":"Success","data":results_list}
        return JsonResponse(result_message,status=200)
    
    else:
        result_message= {"State":"Error","data":"Not data found"}
        return JsonResponse(result_message,status=404)
    
    
    
@csrf_exempt
@api_view(['GET'])
def getAllResultsFileByEmail(request):
    
    showIntro()
    
    email = request.GET.get('email')
    
    results = ResonanceResult.objects.filter(email=email)
    
    if(len(results)>0):
        results_list = [dict(item, **{'_id': str(item['_id'])}) for item in results.values()]
        
        df = pd.DataFrame(results_list)
            
        data_flat = pd.json_normalize(df['metadata'])
        
        data_flat = data_flat.add_prefix('metadata_')
        
        df.drop(columns=["metadata"],inplace=True)

        df= pd.concat([df, data_flat], axis=1)
        
        csv_data = df.to_csv(index=False)

        response = HttpResponse(csv_data, content_type='text/csv',status=200)
        response['Content-Disposition'] = 'attachment; filename="resonance_predictions_results.csv"'

        return response
        
    else:
        result_message= {"State":"Error","data":"Not data found"}
        return JsonResponse(result_message,status=404)    
    
    
    
    
@csrf_exempt
@api_view(['GET'])
def getCurrentResultPrediction(request):
    
    showIntro()
    
    task_id = request.GET.get('task_id')
    
    results = ResonanceResult.objects.filter(task_id=task_id)
    
    if(len(results)>0):
        results_list = [dict(item, **{'_id': str(item['_id'])}) for item in results.values()]
        result_message= {"State":"Success","data":results_list}
        return JsonResponse(result_message,status=200)
    
    else:
        result_message= {"State":"Error","data":"Not data found"}
        return JsonResponse(result_message,status=404)   
    
    

@csrf_exempt
@api_view(['GET'])
def getCurrentResultPredictionFile(request):
    
    showIntro()
    
    task_id = request.GET.get('task_id')
    
    results = ResonanceResult.objects.filter(task_id=task_id)
    
    if(len(results)>0):
        results_list = [dict(item, **{'_id': str(item['_id'])}) for item in results.values()]
        
        df = pd.DataFrame(results_list)
            
        data_flat = pd.json_normalize(df['metadata'])
        
        data_flat = data_flat.add_prefix('metadata_')
        
        df.drop(columns=["metadata"],inplace=True)

        df= pd.concat([df, data_flat], axis=1)
        
        csv_data = df.to_csv(index=False)

        response = HttpResponse(csv_data, content_type='text/csv',status=200)
        response['Content-Disposition'] = 'attachment; filename="resonance_predictions_results.csv"'

        return response
        
    else:
        result_message= {"State":"Error","data":"Not data found"}
        return JsonResponse(result_message,status=404)     