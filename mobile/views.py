from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import modelformset_factory
from base.forms import JmSubmitForm, GmSubmitForm, PersonForm, SjSubmitForm, SjPersonForm
from base.models import Submit, Person


def m_home(request):
    return render(request, 'mobile/m_home.html')

def m_sub_intro(request):
    return render(request, 'mobile/m_sub_intro.html')

def m_about_jm(request):
    return render(request, 'mobile/m_about_jm.html')

def m_certification(request):
    return render(request, 'mobile/m_certification.html')


def m_submit_jm(request):
    if request.method == "POST":
        form1 = JmSubmitForm(request.POST)
        form2 = PersonForm(request.POST)
        if all([form1.is_valid(),form2.is_valid()]):
            obj = form1.save(commit=False)
            obj.category = "신생아작명"
            obj.save()
            person = form2.save(commit=False)
            person.submit = obj
            person.save()
            context = {'submit':obj,'person':person}
            return render(request,'mobile/m_submit_complete.html',context)
    form1 = JmSubmitForm()
    form2 = PersonForm()
    context = {'form1': form1, 'form2':form2}
    return render(request, 'mobile/m_submit_jm.html',context)

def m_submit_gm(request):
    if request.method == "POST":
        form1 = GmSubmitForm(request.POST)
        form2 = PersonForm(request.POST)
        if all([form1.is_valid(),form2.is_valid()]):
            obj = form1.save(commit=False)
            obj.category = "개명"
            obj.save()
            person = form2.save(commit=False)
            person.submit = obj
            person.save()
            context = {'submit':obj,'person':person}
            return render(request,'mobile/m_submit_complete.html',context)
    form1 = GmSubmitForm()
    form2 = PersonForm()
    context = {'form1': form1, 'form2':form2}
    return render(request, 'mobile/m_submit_gm.html',context)

def m_edit_submit(request):
    obj1 = get_object_or_404(Submit, id=request.GET.get('pk'))
    if obj1.category == "신생아작명":
        obj2 = Person.objects.get(submit__id=obj1.id)
        form1 = JmSubmitForm(request.POST or None, instance=obj1)
        form2 = PersonForm(request.POST or None, instance=obj2)
    elif obj1.category == "개명":
        obj2 = Person.objects.get(submit__id=obj1.id)
        form1 = GmSubmitForm(request.POST or None, instance=obj1)
        form2 = PersonForm(request.POST or None, instance=obj2)
    context = {'form1': form1,'form2': form2,'submit': obj1,'person': obj2}
    if all([form1.is_valid(),form2.is_valid()]):
        parent = form1.save(commit=False)
        parent.save()
        child = form2.save(commit=False)
        child.submit = parent
        child.save()
        return render(request,'mobile/m_submit_complete.html',context)
    if obj1.category == "신생아작명":
        return render(request,'mobile/m_submit_jm.html', context)
    elif obj1.category == "개명":
        return render(request,'mobile/m_submit_gm.html', context)

def m_delete_submit(request):
    if request.method == "POST":
        obj1 = get_object_or_404(Submit, id=request.POST.get('pk'))
        obj1.delete()
        return redirect('m-home')
    obj1 = get_object_or_404(Submit, id=request.GET.get('pk'))
    context = {"submit": obj1}
    return render(request,'mobile/m_delete_submit.html', context)

def m_find_submit(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        f_number = request.POST.get('f_number')
        obj_count = Submit.objects.filter(name=f_name, phonnumber=f_number).count()
        if obj_count == 0:
            context = { 'name': f_name, 'number': f_number}
            return render(request,'mobile/m_find_submit.html',context)

        elif obj_count == 1:
            obj1 = Submit.objects.get(name=f_name, phonnumber=f_number)
            if obj1.category == "신생아작명" or obj1.category == "개명":
                obj2 = Person.objects.get(submit__id=obj1.id)
                context = { 'submit': obj1, 'person': obj2}
            elif obj1.category == "사주상담" or obj1.category == "궁합":
                persons = obj1.persons.all()
                context = { 'submit': obj1, 'persons': persons}
            return render(request,'mobile/m_submit_check.html', context)

        else:
            obj1 = Submit.objects.filter(name=f_name, phonnumber=f_number)
            context = { 'submits': obj1 }
            return render(request,'mobile/m_find_submit_list.html', context)

    return render(request,'mobile/m_find_submit.html')


def m_submit_sj(request):
    PersonFormset = modelformset_factory(Person,form=SjPersonForm,extra=1)
    if request.method == "POST":
        form = SjSubmitForm(request.POST)
        formset = PersonFormset(request.POST)
        if all([form.is_valid(),formset.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for each in formset:
                child = each.save(commit=False)
                child.submit = parent
                child.save()
            persons = parent.persons.all()
            context = {
            'submit': parent,
            'persons': persons,
            }
            return render(request,'mobile/m_submit_complete.html',context)
        
    form = SjSubmitForm()
    formset = PersonFormset(queryset=Person.objects.none())
    context = {
        'form': form,
        'formset': formset,
        }
    return render(request,'mobile/m_submit_sj.html', context)


def m_edit_submit_sj(request):
    obj = get_object_or_404(Submit, id=request.GET.get('pk'))
    PersonFormset = modelformset_factory(Person, form=SjPersonForm, extra=0,can_delete=True, min_num=1)
    persons = obj.persons.all()
    type = "edit"

    if request.method == "POST":
        form = SjSubmitForm(request.POST,instance=obj)
        formset = PersonFormset(request.POST,queryset=persons)
        
        if all([form.is_valid(),formset.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for each in formset:
                child = each.save(commit=False)
                if each.cleaned_data["DELETE"]:
                    child.delete()
                else:
                    child.submit = parent
                    child.save()
            context = {
                'submit': obj,
                'persons':persons,
                'type' : type
                }
            return render(request,'mobile/m_submit_complete.html',context)

    form = SjSubmitForm(instance=obj)
    formset = PersonFormset(queryset=persons)
    context = {
            'form': form,
            'formset': formset,
            'type' : type
            }
    return render(request,'mobile/m_submit_sj.html', context)