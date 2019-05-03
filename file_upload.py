import json, datetime, os

from .views import PC_CLASS

urlpatterns = [ import json, datetime, os
    url(u'^file_upload$', PC.file_upload),


views.py
class PC_CLASS():
    def file_upload(request):
        try:
            f = request.FILES['file']
            imgdir = './image_save_path'
            tmpfile = '%s/%s' % (str(imgdir), str(f))
            with open(tmpfile, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            if not os.path.exists(tmpfile):
                return result
            response['result'] = 'success'
            return response
        except Exception as e:
            response['result'] = 'failed'
            return response

        response = HttpResponse( json.dumps(response), content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"



