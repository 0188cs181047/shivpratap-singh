from django.shortcuts import render

# Create your views here.


def index1(request):
    return render(request,"testapp/index.html")

def moviesinfo(request):
    head_msg = "latest movie information"
    msg1 = "sonali going to slowly getting cured"
    msg2 = "salman going to marrige soon "
    msg3 = "prabhash will have release new movie"


    my_dict = {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3}
    return render (request , "testapp/demo.html" , {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3})

def newsinfo(request):
    head_msg = "latest news information"
    msg1 = "narendra modi have gone to another country "
    msg2 = "this schime have very unplcent in this the life  "
    msg3 = "the politics haave very essencial part of this "


    my_dict = {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3}
    return render (request , "testapp/demo.html" , {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3})


def cricketinfo(request):
    head_msg = "latest crickest information"
    msg1 = "the dinesh kartik have tha best player in the india human"
    msg2 = "rishab pant is the nice wiket kipar "
    msg3 = "rohi sharma moat important player in the country"


    my_dict = {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3}
    return render (request , "testapp/demo.html" , {'head_msg':head_msg, 'msg1':msg1 ,'msg2':msg2 , 'msg3':msg3})
