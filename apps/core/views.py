from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to BankTap!")  # Simple response for the root path
