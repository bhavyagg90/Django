from django.shortcuts import render, HttpResponse

# Create your views here.
context = {
  "variable":"harry"
}
def index(request):
  return render(request,'index.html',context)
  # return HttpResponse("this is homepage")
def about(request):
  return HttpResponse("this is aboutpage")
def contact(request):
  return HttpResponse("this is contactpage")
def services(request):
  return HttpResponse("this is servicespage")
