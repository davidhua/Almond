from django.http import HttpResponse

from AlmondApp.models import AlmondTable
from django.shortcuts import render_to_response

def main(request):
    return render_to_response('index.html', {'content': AlmondTable.objects.get(timestamp=6).angle})
    #return render_to_response('index.html', context_instance=RequestContext(request))
    #currentRow = AlmondTable.objects.get(timestamp=6).angle
    #return HttpResponse(currentRow)