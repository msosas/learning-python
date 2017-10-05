from django.http import Http404, HttpResponse
import datetime

HTML = """ 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
<meta http­equiv="content­type" content="text/html;  charset=utf­8"> 
<meta name="robots" content="NONE,NOARCHIVE"> 
<title>Hola mundo</title> 
<style type="text/css"> 
html * { padding:0; margin:0; } 
body * { padding:10px 20px; } 
body * * { padding:0; } 
body { font:small sans­serif; } 
body>div { border­bottom:1px solid #ddd; } 
h1 { font­weight:normal; } 
#summary { background: #e0ebff; } 
</style> 
</head> 
<body> 
<div id="summary"> 
<h1>¡Hola Mundo!</h1> 
</div> 
</body></html> """ 

def hola(request):
	return HttpResponse(HTML)

def fecha_actual(request):
	ahora = datetime.datetime.now()
	html = "<html><head><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'></head><body><h1>Fecha:</h1><h3>%s<h/3></body></html>" % ahora
	return HttpResponse(html)

def horas_adelante(request,offset,test):
	print(test)
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt)
	return HttpResponse(html)