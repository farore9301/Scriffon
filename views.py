from django.utils import simplejson
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime, os
 
def static_page(response, template):
	template = "%s.html" % (template)
	return render_to_response(template)

def envoi_autorisation(request):
	if not request.GET:
		return render_to_response('error.html')
	a,b,c = os.getloadavg()
	if a > 75 or b > 75 or c > 75:
		reponse={'reponse':false}
	else:
		reponse={'reponse':true}
	json = simplejson.dumps(reponse)
	return HttpResponse(json, mimetype='application/json')