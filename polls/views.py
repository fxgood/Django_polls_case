from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import *
from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list,
             'name':'余丰旭'}
    return render(request,'polls/index.html',context)

    # question_id=34 由 urls中的<int:question_id> 匹配生成
def detail(request,question_id):
    # 从Question表中获取主键为url中<int:question_id>的一项
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question,'message':'用来测试的message'})

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"你没有选择一个选项"
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        # 返回一个重定向，防止用户点了回退，然后两次提交post
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
        # 这里的reverse作用是将参数转换为 polls/3/results/
