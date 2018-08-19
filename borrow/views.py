from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render,HttpResponseRedirect



# Create your views here.
def index(request):
    # User has to login then view the site
    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:
        return render(request, 'borrow/homepage.html')


def BorrowRequest(request, book_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('borrow/login')
    else:    
        user = request.user
        form = BorrowRecordForm(request.POST or None, request.FILES or None)
        print(form)
        if form.is_valid(): 
            record = form.save(commit=False)
            record.borrower = request.user
            record.book = get_object_or_404(Book, pk=book_id)
            record.save()
            return HttpResponseRedirect("/book/%d/profile" % user.id)
        return HttpResponseRedirect('borrow/')