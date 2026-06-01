import decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EquipInfo, EquipInfoEdit, UpdateEquipInfo, IncreaseGlobal, InstallMaterial, MaterialSearch, Custinfo, \
    DupConInfo, CustinfoB, EquipmentSelect, Coninfo, ConinfoB, EquipmentSelect1, EquipInfo2, FormatForm, BidSelect, OSR, \
    Package1, \
    Package2, Package3, Package4, Package5, Package6, Package7, Package8, Package9, Package10, Package11, Package12, \
    Package13, \
    Package14, Package15, Package16, Package1a, Package1b, InfoPackage, Package2a, Package2b, Package3a, Package3b, \
    Package4a, \
    Package4b, Package5a, Package5b, Package6a, Package6b, Package7a, Package7b, Package8a, Package8b, Package9a, \
    Package9b, \
    Package10a, Package10b, Package11a, Package11b, Package12a, Package12b, Package13a, Package13b, Package14a, \
    Package14b, \
    Package15a, Package15b, Package16a, Package16b, ContractForm, JobInfoCurrent, Costjob, NetprofitTarget, EquipmentSelect2
from .models import (Equipment, Equipment2, Man, Type, Gasvivfurn, Gasvivcond, Gasvivevap, Motortypefurn, Motortypecond, \
    Motortypeevap, Descriptionfurn, Descriptioncond, Descriptionevap, Refrigfurn, Refrigcond, Refrigevap, \
    BTUfurn, BTUcond, BTUevap, Outputstg1furn, Outputstg1cond, Outputstg1evap, Outputstg2, Outputstg3, Warr, Addnew, \
    EquipUpdate, GlobalIncrease, MatUpdate, \
    Material, Manufacturer, Vendor, MaterialType, CustomerInfo, ContractorInfo, Bidding, EquipSelection, Contract, \
    Mfgmodeldescripcond, Mfgmodeldescripevap, CurrentJobInfo, Efficiency2, ConfigFurn, ConfigCond, ConfigEvap, Furneff, \
    Evapeff, Condeff, Mfgmodeldescripfurn, Filtereff, FilterMfgmodeldescrip, ManFilter, EffFilter, Config, Eff, \
    Mfgmodeldescrip, Description, Gasviv, Motortype, Refrig, Btu, Outputstg1, Outputstg2, Outputstg3, Filtertype, \
    Filtermfg, MfgmodeldescripFilter, JobLocation, FurnaceType, OutsideUnitType, FilterCondEff, FilterCondbtu, \
    FilterCondDescrip, FilterCondModelnum, FilterFurnbtu, FilterFurnConfig, FilterFurnEff, FilterFurnDescrip, \
    FilterFurnModelnum, FilterCoilbtu, FilterCoilConfig, FilterCoilModelnum, FilterCoilAll, FilterThermostat, \
    FilterThermostatModnum, NicorRebate1, NicorRebate2, NicorRebate3, NicorRebate4, NicorRebate5, RebateInfo, \
    FilterCoiltype, FilterEquipType, FilterTypeDescrip, OutsideResource, MatTypeBid, TechLevel, TechHours, \
    InstallPackage1, \
    InstallPackage2, InstallPackage3, InstallPackage4, InstallPackage5, InstallPackage6, InstallPackage7, \
    InstallPackage8, \
    InstallPackage9, InstallPackage10, InstallPackage11, InstallPackage12, InstallPackage13, InstallPackage14, \
    InstallPackage15, \
    InstallPackage16, PackageInfo, Package, TotalJobCost, SelectedEquip, Option, Custpagelocation, multiformA, \
    multiformB, \
    multiformC, multiformD, multiformE, MatCost, OSRCost, laborCost, EquipmentCost, JobCost, Tax, Calculation, \
    Profitincrease, TargetProfit, Mfgmodeldescriptherm, Descriptiontherm, ConfigTherm, Thermeff, Gasvivtherm,
    Motortypetherm, Refrigetherm, BTUtherm, Outputstg1therm, Outputstg2furn, Outputstg3furn, Filtermodelnum, \
                     SmartThermostat, FilterPlenumWidth, ExistFurnConfig, YesNo, DetailTable, Terms)
from django.db.models import Q, Sum, F, Value
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from num2words import num2words
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.db.models.functions import Coalesce


class PostsListView(ListView, FormView):
    model = Equipment2
    template_name = 'mha/export.html'
    form_class = FormatForm


#   def post(self, request, **kwargs):
#       qs = self.get_queryset()
#       dataset = Equipment2Resource().export(qs)
#
#       format = request.POST.get('format')
#
#       if format == 'xls':
#           ds = dataset.xls
#       elif format == 'csv':
#           ds = dataset.csv
#       else:
#           ds = dataset.jsonee
#
#       responce = HttpResponse(ds, content_type=F"{format}")
#       responce['Content-Disposition'] = F"attachment: filename=posts.{format}"
#       return responce


def welcome(request):
    return render(request, 'mha/welcome.html')


def main(request):
    return render(request, 'mha/main.html')


def installbidingpage(request):
    return render(request, 'mha/installbidingpage.html')


def equipmat(request):
    return render(request, 'mha/equipmat.html')


def openequip(request):
    return render(request, 'mha/openequip.html')


def addnewequip(request):
    form = EquipInfo(request.POST)
    a = Equipment.objects.create(modelnum="Add Model Number")
    b = Equipment.objects.values_list('id', flat=True).last()
    Equipment.objects.filter(id=b).update(idA=b)
    c = Equipment2.objects.create(modelnum="Add Model Number")
    d = Equipment2.objects.values_list('id', flat=True).last()
    Equipment2.objects.filter(id=d).update(idA=d)

    context = {
        "form": form,
        "a": a,
        "c": c,

    }
    return render(request, 'mha/addnewequip.html', context)


def addnewequip2(request):
    form = EquipInfo2()
    a = Equipment2.objects.values_list('id', flat=True).last()
    a1 = a + 1
    b = Equipment2.objects.create(id=a1, modelnum="Add Model Number")
    instance = Equipment2.objects.get(id=a1)
    Equipment2.objects.filter(id=a1).update(idA=a1)
    context = {
        "form": form,
        "instance": instance,
        "b": b,
    }
    return render(request, 'mha/addnewequip2.html', context)


def addnewequip1(request):
    form = EquipInfo()
    return render(request, 'mha/addnewequip.html', {'form': form})


def deleteequip(request):
    form = EquipInfo(request.POST)
    a = Equipment.objects.values_list('id', flat=True).last()
    Equipment.objects.filter(id=a).delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    Equipment2.objects.filter(id=b).delete()
    context = {
        "form": form,

    }
    return render(request, 'mha/openequip.html', context)


def duplicate2(request):
    form = EquipInfoEdit(request.POST or None)
    a = Equipment2.objects.all()
    b = Equipment2.objects.values_list('id', flat=True).last()
    b2 = b + 1
    c = a.values_list('modelnum', flat=True).get(id=b)
    d = a.values_list('cost', flat=True).get(id=b)
    e = a.values_list('mfg', flat=True).get(id=b)
    f = a.values_list('type', flat=True).get(id=b)
    g = a.values_list('config', flat=True).get(id=b)
    h = a.values_list('height', flat=True).get(id=b)
    i = a.values_list('width', flat=True).get(id=b)
    j = a.values_list('depth', flat=True).get(id=b)
    k = a.values_list('eff', flat=True).get(id=b)
    l = a.values_list('mfgmodeldescrip', flat=True).get(id=b)
    m = a.values_list('gasviv', flat=True).get(id=b)
    n = a.values_list('motortype', flat=True).get(id=b)
    o = a.values_list('description', flat=True).get(id=b)
    p = a.values_list('refrig', flat=True).get(id=b)
    q = a.values_list('btu', flat=True).get(id=b)
    r = a.values_list('outputstg1', flat=True).get(id=b)
    s = a.values_list('outputstg2', flat=True).get(id=b)
    t = a.values_list('outputstg3', flat=True).get(id=b)
    u = a.values_list('warr', flat=True).get(id=b)
    c = a.values_list('modelnum', flat=True).get(id=b)
    v = a.create(id=b2, idA=b2, modelnum=c, cost=d, mfg=e, type=f, config=g, height=h, width=i, depth=j, eff=k,
                 mfgmodeldescrip=l, gasviv=m, motortype=n, description=o, refrig=p, btu=q, outputstg1=r,
                 outputstg2=s, outputstg3=t, warr=u)

    context = {
        "form": form,
        "v": v,

    }
    return render(request, 'mha/addnewequip2.html', context)


def duplicate22(request):
    form = EquipInfoEdit(request.POST or None)
    a = Equipment2.objects.all()
    b = Equipment2.objects.values_list('id', flat=True).last()
    b2 = b + 1
    c = a.values_list('modelnum', flat=True).get(id=b)
    d = a.values_list('cost', flat=True).get(id=b)
    e = a.values_list('mfg', flat=True).get(id=b)
    f = a.values_list('type', flat=True).get(id=b)
    g = a.values_list('config', flat=True).get(id=b)
    h = a.values_list('height', flat=True).get(id=b)
    i = a.values_list('width', flat=True).get(id=b)
    j = a.values_list('depth', flat=True).get(id=b)
    k = a.values_list('eff', flat=True).get(id=b)
    l = a.values_list('mfgmodeldescrip', flat=True).get(id=b)
    m = a.values_list('gasviv', flat=True).get(id=b)
    n = a.values_list('motortype', flat=True).get(id=b)
    o = a.values_list('description', flat=True).get(id=b)
    p = a.values_list('refrig', flat=True).get(id=b)
    q = a.values_list('btu', flat=True).get(id=b)
    r = a.values_list('outputstg1', flat=True).get(id=b)
    s = a.values_list('outputstg2', flat=True).get(id=b)
    t = a.values_list('outputstg3', flat=True).get(id=b)
    u = a.values_list('warr', flat=True).get(id=b)
    c = a.values_list('modelnum', flat=True).get(id=b)
    v = a.create(id=b2, idA=b2, modelnum=c, cost=d, mfg=e, type=f, config=g, height=h, width=i, depth=j, eff=k,
                 mfgmodeldescrip=l, gasviv=m, motortype=n, description=o, refrig=p, btu=q, outputstg1=r,
                 outputstg2=s, outputstg3=t, warr=u)

    context = {
        "form": form,
        "v": v,

    }
    return render(request, 'mha/duplicate2.html', context)




################################## Add New Equipment old Queries #################################
#def model(request):
#    form = EquipInfo(request.POST)
#    b = Equipment2.objects.values_list('id', flat=True).last()
#    d = request.POST['modelnum_id']
#    Equipment2.objects.filter(id=b).update(modelnum=d)
#    context = {
#        "form": form,
#
#    }
#    return render(request, 'mha/addnewequip.html', context)

def load_2model(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfo2(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    modelnum = a.values('modelnum').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "modelnum": modelnum,
        "form": form,
    }
    return render(request, 'mha/modelnum3_1.html', context)


def load_model2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    modelnum = a.values('modelnum').get(id=b)
    context = {
        "instance": instance,
        "modelnum": modelnum,
        "form": form,
    }
    return render(request, 'mha/modelnum2_1.html', context)




def addnew2(request):
    form = EquipInfo(request.POST)
    a = request.POST['addnew_id']
    d = Equipment.objects.values_list('id', flat=True).last()
    e = Equipment.objects.filter(id=d).update(addnew=a, modelnum=a)
    context = {
        "form": form,
        "a": a,
        "e": e,
    }
    return render(request, 'mha/addnewequip.html', context)


def load_addnew(request):
    a = Equipment.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment.objects.get(id=b)
    form = EquipInfo(request.POST or None, instance=instance)
    addnew = a.values('addnew').get(id=b)
    context = {
        "instance": instance,
        "addnew": addnew,
        "form": form,
    }
    return render(request, 'mha/addnew_1.html', context)


def type2(request):
    form = EquipInfo2(request.POST)
    Config.objects.all().delete()
    Eff.objects.all().delete()
    Mfgmodeldescrip.objects.all().delete()
    Gasviv.objects.all().delete()
    Motortype.objects.all().delete()
    Description.objects.all().delete()
    Refrig.objects.all().delete()
    Btu.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_type2']
    Equipment2.objects.filter(id=b).update(type=d, config='Add New Configuration', eff='Add New Efficiency',
                                           mfgmodeldescrip='Add New Model Description', gasviv='Add New Gas VIv',
                                           motortype='Add New Motor Type', description='Add New Description',
                                           refrig='Add New Refrig.', btu='Add New BTU',
                                           outputstg1='Add New Output Stage 1',
                                           outputstg2='Add New Output Stage 2', outputstg3='Add New Output Stage 3',
                                           warr=' Add New Warranty')
    e = Type.objects.create(types=d)
   # f = Equipment2.objects.filter(id=b).update(type2="")
    g = Equipment2.objects.filter(type=d).annotate(configA=F('config'))
    h = list(g.values_list('config', flat=True).distinct())
    try:
        h1 = Config.objects.create(id=1, configs=h[0])
    except Exception:
        h1 = 0
    try:
        h2 = Config.objects.create(id=2, configs=h[1])
    except Exception:
        h2 = 0
    try:
        h3 = Config.objects.create(id=3, configs=h[2])
    except Exception:
        h3 = 0
    try:
        h4 = Config.objects.create(id=4, configs=h[3])
    except Exception:
        h4 = 0
    try:
        h5 = Config.objects.create(id=5, configs=h[4])
    except Exception:
        h5 = 0
    try:
        h6 = Config.objects.create(id=6, configs=h[5])
    except Exception:
        h6 = 0
    try:
        h7 = Config.objects.create(id=7, configs=h[6])
    except Exception:
        h7 = 0
    try:
        h8 = Config.objects.create(id=8, configs=h[7])
    except Exception:
        h8 = 0
    context = {
        "form": form,
       # "f": f,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_type2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    type = a.values('type').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "type": type,
        "form": form,
    }
    return render(request, 'mha/type_1.html', context)


def load_type(request):
    form = EquipInfo2(request.POST or None)
    type = Type.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "type": type,
        "form": form,
    }
    return render(request, 'mha/type_1.html', context)




################################## Add New Equipment #################################

def load_model(request):
   a = Equipment2.objects.all()
   b = a.values_list('id', flat=True).last()
   instance = Equipment2.objects.get(id=b)
   form = EquipInfo2(request.POST or None, instance=instance)
   modelnum = a.values('modelnum').get(id=b)
   context = {
       "instance": instance,
       "modelnum": modelnum,
       "form": form,
   }
   return render(request, 'mha/modelnum_1.html', context)


def load_cost(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    cost = a.values('cost').get(id=b)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_1.html', context)


def load_warr(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    warr = a.values('warr').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "warr": warr,
        "form": form,
    }
    return render(request, 'mha/warr_1.html', context)


def load_height(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    height = a.values('height').get(id=b)
    context = {
        "instance": instance,
        "height": height,
        "form": form,
    }
    return render(request, 'mha/height_1.html', context)


def load_width(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    width = a.values('width').get(id=b)
    context = {
        "instance": instance,
        "width": width,
        "form": form,
    }
    return render(request, 'mha/width_1.html', context)


def load_depth(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    depth = a.values('depth').get(id=b)
    context = {
        "instance": instance,
        "depth": depth,
        "form": form,
    }
    return render(request, 'mha/depth_1.html', context)


def model(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['modelnum_id']
    Equipment2.objects.filter(id=b).update(modelnum=d)
    context = {
        "form": form,

    }
    return render(request, 'mha/addnewequip2.html', context)


def modeldup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_modelnum']
    Equipment2.objects.filter(id=b).update(modelnum=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def descriptiondup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_description']
    Equipment2.objects.filter(id=b).update(description=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def btudup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_btu']
    Equipment2.objects.filter(id=b).update(btu=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def costdup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_cost']
    Equipment2.objects.filter(id=b).update(cost=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def heightdup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_height']
    Equipment2.objects.filter(id=b).update(height=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def widthdup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_width']
    Equipment2.objects.filter(id=b).update(width=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)


def depthdup(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_depth']
    Equipment2.objects.filter(id=b).update(depth=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)

def mfg(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_mfg']
    Equipment2.objects.filter(id=b).update(mfg=d)
    e = Man.objects.all().order_by('manufacturer').values()
    context = {
        "form": form,
        "e": e,
    }
    return render(request, 'mha/addnewequip2.html', context)


def mfg22(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_mfg2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(mfg=a)
    e = Man.objects.create(manufacturer=a)
    f = Equipment2.objects.filter(id=b).update(mfg2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_mfg2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    mfg = a.values('mfg').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/mfg_1.html', context)


def load_mfg(request):
    form = EquipInfo2(request.POST or None)
    mfg = Man.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/mfg_1.html', context)

def type(request):
    form = EquipInfo2(request.POST)
    Config.objects.all().delete()
    Eff.objects.all().delete()
    Mfgmodeldescrip.objects.all().delete()
    Gasviv.objects.all().delete()
    Motortype.objects.all().delete()
    Description.objects.all().delete()
    Refrig.objects.all().delete()
    Btu.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_type']
    Equipment2.objects.filter(id=b).update(type=d,config='Add New Configuration',eff='Add New Efficiency',
                                           mfgmodeldescrip='Add New Model Description', gasviv='Add New Gas VIv',
                                           motortype='Add New Motor Type', description='Add New Description',
                                           refrig='Add New Refrig.', btu='Add New BTU', outputstg1='Add New Output Stage 1',
                                           outputstg2='Add New Output Stage 2', outputstg3='Add New Output Stage 3',
                                           warr=' Add New Warranty')

    g = Equipment2.objects.filter(type=d).annotate(configA=F('config'))
    h = list(g.values_list('config', flat=True).distinct().exclude(config='Add New Configuration'))
    try:
        h1 = Config.objects.create(id=1, configs='Add New Configuration')
    except Exception:
        h1 = 0
    try:
        h2 = Config.objects.create(id=2, configs=h[0])
    except Exception:
        h2 = 0
    try:
        h3 = Config.objects.create(id=3, configs=h[1])
    except Exception:
        h3 = 0
    try:
        h4 = Config.objects.create(id=4, configs=h[2])
    except Exception:
        h4 = 0
    try:
        h5 = Config.objects.create(id=5, configs=h[3])
    except Exception:
        h5 = 0
    try:
        h6 = Config.objects.create(id=6, configs=h[4])
    except Exception:
        h6 = 0
    try:
        h7 = Config.objects.create(id=7, configs=h[5])
    except Exception:
        h7 = 0
    try:
        h8 = Config.objects.create(id=8, configs=h[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_config(request):
    form = EquipInfo2(request.POST or None)
    config = Config.objects.all().order_by('configs').values()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "config": config,
        "form": form,
    }
    return render(request, 'mha/config_1.html', context)


def smart(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    Equipment2.objects.filter(id=b).update(smart="1")
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def notsmart(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    Equipment2.objects.filter(id=b).update(smart="2")
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)

def config(request):
    form = EquipInfo2(request.POST)
    Eff.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_config']
    Equipment2.objects.filter(id=b).update(config=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e).annotate(effA=F('eff'))
    g = list(f.values_list('eff', flat=True).distinct().exclude(eff='Add New Efficiency'))
    try:
        h1 = Eff.objects.create(id=1, effs='Add New Efficiency')
    except Exception:
        h1 = 0
    try:
        h2 = Eff.objects.create(id=2, effs=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Eff.objects.create(id=3, effs=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Eff.objects.create(id=4, effs=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Eff.objects.create(id=5, effs=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Eff.objects.create(id=6, effs=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Eff.objects.create(id=7, effs=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Eff.objects.create(id=8, effs=g[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)

def load_eff(request):
    form = EquipInfo2(request.POST or None)
    eff = Eff.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "eff": eff,
        "form": form,
    }
    return render(request, 'mha/eff_1.html', context)


def eff(request):
    form = EquipInfo2(request.POST)
    Mfgmodeldescrip.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_eff']
    Equipment2.objects.filter(id=b).update(eff=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
#    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=c).annotate(mfgmodeldescripA=F('mfgmodeldescrip'))
    g = list(f.values_list('mfgmodeldescrip', flat=True).distinct().exclude(mfgmodeldescrip='Add New Model Description'))
    try:
        h1 = Mfgmodeldescrip.objects.create(id=1, mfgmodeldescrips='Add New Model Description')
    except Exception:
        h1 = 0
    try:
        h2 = Mfgmodeldescrip.objects.create(id=2, mfgmodeldescrips=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Mfgmodeldescrip.objects.create(id=3, mfgmodeldescrips=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Mfgmodeldescrip.objects.create(id=4, mfgmodeldescrips=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Mfgmodeldescrip.objects.create(id=5, mfgmodeldescrips=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Mfgmodeldescrip.objects.create(id=6, mfgmodeldescrips=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Mfgmodeldescrip.objects.create(id=7, mfgmodeldescrips=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Mfgmodeldescrip.objects.create(id=8, mfgmodeldescrips=g[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def eff2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_eff2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(eff=a)
    c1 = Eff.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    e = Eff.objects.create(id=d1, effs=a)
    f = Equipment2.objects.filter(id=b).update(eff2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_eff2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    eff = a.values('eff').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "eff": eff,
        "form": form,
    }
    return render(request, 'mha/eff_1.html', context)





def load_mfgmodeldescrip(request):
    form = EquipInfo2(request.POST or None)
    mfgmodeldescrip = Mfgmodeldescrip.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)

def mfgmodeldescrip(request):
    form = EquipInfo2(request.POST)
    Gasviv.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_mfgmodeldescrip']
    Equipment2.objects.filter(id=b).update(mfgmodeldescrip=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1, mfgmodeldescrip=c).annotate(gasvivA=F('gasviv'))
    g = list(f.values_list('gasviv', flat=True).distinct().exclude(gasviv='Add New Gas VIv'))
    try:
        h1 = Gasviv.objects.create(id=1, gasvivs='Add New Gas VIv')
    except Exception:
        h1 = 0
    try:
        h2 = Gasviv.objects.create(id=2, gasvivs=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Gasviv.objects.create(id=3, gasvivs=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Gasviv.objects.create(id=4, gasvivs=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Gasviv.objects.create(id=5, gasvivs=g[3])
    except Exception:
        h5 = 0

    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,

    }
    return render(request, 'mha/addnewequip2.html', context)


def load_gasviv(request):
    form = EquipInfo2(request.POST or None)
    gasviv = Gasviv.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "gasviv": gasviv,
        "form": form,
    }
    return render(request, 'mha/gasviv_1.html', context)


def gasviv(request):
    form = EquipInfo2(request.POST)
    Motortype.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_gasviv']
    Equipment2.objects.filter(id=b).update(gasviv=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(motortypeA=F('motortype'))
    g = list(f.values_list('motortype', flat=True).distinct().exclude(motortype='Add New Motor Type'))
    try:
        h1 = Motortype.objects.create(id=1, motortypes='Add New Motor Type')
    except Exception:
        h1 = 0
    try:
        h2 = Motortype.objects.create(id=2, motortypes=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Motortype.objects.create(id=3, motortypes=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Motortype.objects.create(id=4, motortypes=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Motortype.objects.create(id=5, motortypes=g[3])
    except Exception:
        h5 = 0

    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,

    }
    return render(request, 'mha/addnewequip2.html', context)


def load_motortype(request):
    form = EquipInfo2(request.POST or None)
    motortype = Motortype.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "motortype": motortype,
        "form": form,
    }
    return render(request, 'mha/motortype_1.html', context)


def motortype(request):
    form = EquipInfo2(request.POST)
    Description.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_motortype']
    Equipment2.objects.filter(id=b).update(motortype=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(descriptionA=F('description'))
    g = list(f.values_list('description', flat=True).distinct().exclude(description='Add New Description'))
    try:
        h1 = Description.objects.create(id=1, descriptions='Add New Description')
    except Exception:
        h1 = 0
    try:
        h2 = Description.objects.create(id=2, descriptions=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Description.objects.create(id=3, descriptions=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Description.objects.create(id=4, descriptions=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Description.objects.create(id=5, descriptions=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Description.objects.create(id=6, descriptions=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Description.objects.create(id=7, descriptions=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Description.objects.create(id=8, descriptions=g[6])
    except Exception:
        h8 = 0
    try:
        h9 = Description.objects.create(id=9, descriptions=g[7])
    except Exception:
        h9 = 0
    try:
        h10 = Description.objects.create(id=10, descriptions=g[8])
    except Exception:
        h10 = 0
    try:
        h11 = Description.objects.create(id=11, descriptions=g[9])
    except Exception:
        h11 = 0
    try:
        h12 = Description.objects.create(id=12, descriptions=g[10])
    except Exception:
        h12 = 0
    try:
        h13 = Description.objects.create(id=13, descriptions=g[11])
    except Exception:
        h13 = 0
    try:
        h14 = Description.objects.create(id=14, descriptions=g[12])
    except Exception:
        h14 = 0
    try:
        h15 = Description.objects.create(id=15, descriptions=g[13])
    except Exception:
        h15 = 0
    try:
        h16 = Description.objects.create(id=16, descriptions=g[14])
    except Exception:
        h16 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "h12": h12,
        "h13": h13,
        "h14": h14,
        "h15": h15,
        "h16": h16,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_description(request):
    form = EquipInfo2(request.POST or None)
    description = Description.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "description": description,
        "form": form,
    }
    return render(request, 'mha/description_1.html', context)


def description(request):
    form = EquipInfo2(request.POST)
    Refrig.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_description']
    Equipment2.objects.filter(id=b).update(description=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(refrigA=F('refrig'))
    g = list(f.values_list('refrig', flat=True).distinct().exclude(refrig='Add New Refrig.'))
    try:
        h1 = Refrig.objects.create(id=1, refrigs='Add New Refrig.')
    except Exception:
        h1 = 0
    try:
        h2 = Refrig.objects.create(id=2, refrigs=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Refrig.objects.create(id=3, refrigs=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Refrig.objects.create(id=4, refrigs=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Refrig.objects.create(id=5, refrigs=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Refrig.objects.create(id=6, refrigs=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Refrig.objects.create(id=7, refrigs=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Refrig.objects.create(id=8, refrigs=g[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_refrig(request):
    form = EquipInfo2(request.POST or None)
    refrig = Refrig.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "refrig": refrig,
        "form": form,
    }
    return render(request, 'mha/refrig_1.html', context)


def refrig(request):
    form = EquipInfo2(request.POST)
    Btu.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_refrig']
    Equipment2.objects.filter(id=b).update(refrig=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(btuA=F('btu'))
    g = list(f.values_list('btu', flat=True).distinct().exclude(btu='Add New BTU'))
    try:
        h1 = Btu.objects.create(id=1, btus='Add New BTU')
    except Exception:
        h1 = 0
    try:
        h2 = Btu.objects.create(id=2, btus=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Btu.objects.create(id=3, btus=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Btu.objects.create(id=4, btus=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Btu.objects.create(id=5, btus=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Btu.objects.create(id=6, btus=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Btu.objects.create(id=7, btus=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Btu.objects.create(id=8, btus=g[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_btu(request):
    form = EquipInfo2(request.POST or None)
    btu = Btu.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "btu": btu,
        "form": form,
    }
    return render(request, 'mha/btu_1.html', context)



def btu(request):
    form = EquipInfo2(request.POST)
    Outputstg1.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_btu']
    Equipment2.objects.filter(id=b).update(btu=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(outputstg1A=F('outputstg1'))
    g = list(f.values_list('outputstg1', flat=True).distinct().exclude(outputstg1='Add New Output Stage 1'))
    try:
        h1 = Outputstg1.objects.create(id=1, outputstg1s='Add New Output Stage 1')
    except Exception:
        h1 = 0
    try:
        h2 = Outputstg1.objects.create(id=2, outputstg1s=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Outputstg1.objects.create(id=3, outputstg1s=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Outputstg1.objects.create(id=4, outputstg1s=g[2])
    except Exception:
        h4 = 0
    try:
        h5 = Outputstg1.objects.create(id=5, outputstg1s=g[3])
    except Exception:
        h5 = 0
    try:
        h6 = Outputstg1.objects.create(id=6, outputstg1s=g[4])
    except Exception:
        h6 = 0
    try:
        h7 = Outputstg1.objects.create(id=7, outputstg1s=g[5])
    except Exception:
        h7 = 0
    try:
        h8 = Outputstg1.objects.create(id=8, outputstg1s=g[6])
    except Exception:
        h8 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_outputstg1(request):
    form = EquipInfo2(request.POST or None)
    outputstg1 = Outputstg1.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "outputstg1": outputstg1,
        "form": form,
    }
    return render(request, 'mha/outputstg1_1.html', context)


def outputstg1(request):
    form = EquipInfo2(request.POST)
    Outputstg2.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_outputstg1']
    Equipment2.objects.filter(id=b).update(outputstg1=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(outputstg2A=F('outputstg2'))
    g = list(f.values_list('outputstg2', flat=True).distinct().exclude(outputstg2='Add New Output Stage 2'))
    try:
        h1 = Outputstg2.objects.create(id=1, outputstg2s='Add New Output Stage 2')
    except Exception:
        h1 = 0
    try:
        h2 = Outputstg2.objects.create(id=2, outputstg2s=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Outputstg2.objects.create(id=3, outputstg2s=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Outputstg2.objects.create(id=4, outputstg2s=g[2])
    except Exception:
        h4 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_outputstg2(request):
    form = EquipInfo2(request.POST or None)
    outputstg2 = Outputstg2.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "outputstg2": outputstg2,
        "form": form,
    }
    return render(request, 'mha/outputstg2_1.html', context)


def outputstg2(request):
    form = EquipInfo2(request.POST)
    Outputstg3.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_outputstg2']
    Equipment2.objects.filter(id=b).update(outputstg2=c)
    d = Equipment2.objects.values_list('type', flat=True).last()
    e = Equipment2.objects.values_list('config', flat=True).last()
    e1 = Equipment2.objects.values_list('eff', flat=True).last()
    f = Equipment2.objects.filter(type=d, config=e, eff=e1).annotate(outputstg3A=F('outputstg3'))
    g = list(f.values_list('outputstg3', flat=True).distinct().exclude(outputstg3='Add New Output Stage 3'))
    try:
        h1 = Outputstg3.objects.create(id=1, outputstg3s='Add New Output Stage 3')
    except Exception:
        h1 = 0
    try:
        h2 = Outputstg3.objects.create(id=2, outputstg3s=g[0])
    except Exception:
        h2 = 0
    try:
        h3 = Outputstg3.objects.create(id=3, outputstg3s=g[1])
    except Exception:
        h3 = 0
    try:
        h4 = Outputstg3.objects.create(id=4, outputstg3s=g[2])
    except Exception:
        h4 = 0
    context = {
        "form": form,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
    }
    return render(request, 'mha/addnewequip2.html', context)



def load_outputstg3(request):
    form = EquipInfo2(request.POST or None)
    outputstg3 = Outputstg3.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "outputstg3": outputstg3,
        "form": form,
    }
    return render(request, 'mha/outputstg3_1.html', context)


def outputstg3(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['id_outputstg3']
    Equipment2.objects.filter(id=b).update(outputstg3=c)

    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)






def config2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_config2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(config=a)
    c1 = Config.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    e = Config.objects.create(id=d1, configs=a)
    f = Equipment2.objects.filter(id=b).update(config2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_config2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    config = a.values('config').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "config": config,
        "form": form,
    }
    return render(request, 'mha/config_1.html', context)


#def load_configfurn2(request):
#    form = EquipInfo2(request.POST or None)
#    Config.objects.all().delete()
#    e = ConfigFurn.objects.annotate(configsA=F('configs'))
#    g = list(e.values_list('configs', flat=True).distinct())
#    try:
#        h = Config.objects.create(id=1, configs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h1 = Config.objects.create(id=2, configs=g[1])
#    except Exception:
#        h1 = 0
#    try:
#        h2 = Config.objects.create(id=3, configs=g[2])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Config.objects.create(id=4, configs=g[3])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Config.objects.create(id=5, configs=g[4])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Config.objects.create(id=6, configs=g[5])
#    except Exception:
#        h5 = 0
#    config = Config.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "config": config,
#        "form": form,
#    }
#    return render(request, 'mha/config_1.html', context)
#
#
def load_2config(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    config = a.values('config').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "config": config,
        "form": form,
    }
    return render(request, 'mha/config_1.html', context)


def duplicateequip(request, id=None):
    a = Equipment2.objects.values_list('id', flat=True).last()
    instance = get_object_or_404(Equipment2, id=a)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute7_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/duplicate2.html', context)



#def load_configcond2(request):
#    form = EquipInfo2(request.POST or None)
#    Config.objects.all().delete()
#    e = ConfigCond.objects.annotate(configsA=F('configs'))
#    g = list(e.values_list('configs', flat=True).distinct())
#    try:
#        h = Config.objects.create(id=1, configs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h1 = Config.objects.create(id=2, configs=g[1])
#    except Exception:
#        h1 = 0
#    try:
#        h2 = Config.objects.create(id=3, configs=g[2])
#    except Exception:
#        h2 = 0
#    config = Config.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "config": config,
#        "form": form,
#    }
#    return render(request, 'mha/config_1.html', context)
#
#
#def config2cond(request):
#    form = EquipInfo2(request.POST)
#    a = request.POST['id_config3']
#    b = Equipment2.objects.values_list('id', flat=True).last()
#    c = Equipment2.objects.filter(id=b).update(config=a)
#    e = ConfigCond.objects.create(configs=a)
#    e1 = Config.objects.create(configs=a)
#    f = Equipment2.objects.filter(id=b).update(config3="")
#    context = {
#        "form": form,
#        "a":a,
#        "c": c,
#        "e": e,
#        "e1": e1,
#        "f": f,
#    }
#    return render(request, 'mha/addnewequip2.html', context)
#
#
#
#
#def load_configevap2(request):
#    form = EquipInfo2(request.POST or None)
#    Config.objects.all().delete()
#    e = ConfigEvap.objects.annotate(configsA=F('configs'))
#    g = list(e.values_list('configs', flat=True).distinct())
#    try:
#        h = Config.objects.create(id=1, configs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h1 = Config.objects.create(id=2, configs=g[1])
#    except Exception:
#        h1 = 0
#    try:
#        h2 = Config.objects.create(id=3, configs=g[2])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Config.objects.create(id=4, configs=g[3])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Config.objects.create(id=5, configs=g[4])
#    except Exception:
#        h4 = 0
#    config = Config.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "config": config,
#        "form": form,
#    }
#    return render(request, 'mha/config_1.html', context)
#
#
#def config2evap(request):
#    form = EquipInfo2(request.POST)
#    a = request.POST['id_config4']
#    b = Equipment2.objects.values_list('id', flat=True).last()
#    c = Equipment2.objects.filter(id=b).update(config=a)
#    c1 = ConfigEvap.objects.values_list('id', flat=True).last()
#    c2 = Config.objects.values_list('id', flat=True).last()
#    d1 = c1 + 1
#    d2 = c2 + 1
#    e = ConfigEvap.objects.create(id=d1, configs=a)
#    e1 = Config.objects.create(id=d2, configs=a)
#    f = Equipment2.objects.filter(id=b).update(config4="")
#    context = {
#        "form": form,
#        "a":a,
#        "c": c,
#        "e": e,
#        "e1": e1,
#        "f": f,
#    }
#    return render(request, 'mha/addnewequip2.html', context)
#
#
#
#
#def load_furneff2(request):
#    form = EquipInfo2(request.POST or None)
#    Eff.objects.all().delete()
#    e = Furneff.objects.annotate(efffurnA=F('efffurn'))
#    g = list(e.values_list('efffurn', flat=True).distinct())
#    try:
#        h = Eff.objects.create(id=1, effs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Eff.objects.create(id=2, effs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Eff.objects.create(id=3, effs=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Eff.objects.create(id=4, effs=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Eff.objects.create(id=5, effs=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Eff.objects.create(id=6, effs=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Eff.objects.create(id=7, effs=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Eff.objects.create(id=8, effs=g[7])
#    except Exception:
#        h8 = 0
#    eff = Eff.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "eff": eff,
#        "form": form,
#    }
#    return render(request, 'mha/eff_1.html', context)
#
#
#def load_condeff2(request):
#    form = EquipInfo2(request.POST or None)
#    Eff.objects.all().delete()
#    e = Condeff.objects.annotate(effcondA=F('effcond'))
#    g = list(e.values_list('effcond', flat=True).distinct())
#    try:
#        h = Eff.objects.create(id=1, effs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Eff.objects.create(id=2, effs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Eff.objects.create(id=3, effs=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Eff.objects.create(id=4, effs=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Eff.objects.create(id=5, effs=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Eff.objects.create(id=6, effs=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Eff.objects.create(id=7, effs=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Eff.objects.create(id=8, effs=g[7])
#    except Exception:
#        h8 = 0
#    eff = Eff.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "eff": eff,
#        "form": form,
#    }
#    return render(request, 'mha/eff_1.html', context)
#
#
#def load_evapeff2(request):
#    form = EquipInfo2(request.POST or None)
#    Eff.objects.all().delete()
#    e = Evapeff.objects.annotate(effevapA=F('effevap'))
#    g = list(e.values_list('effevap', flat=True).distinct())
#    try:
#        h = Eff.objects.create(id=1, effs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Eff.objects.create(id=2, effs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Eff.objects.create(id=3, effs=g[2])
#    except Exception:
#        h3 = 0
#    eff = Eff.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "eff": eff,
#        "form": form,
#    }
#    return render(request, 'mha/eff_1.html', context)
#
#
#
#def load_furnmfgmodeldescrip2(request):
#    form = EquipInfo2(request.POST or None)
#    Mfgmodeldescrip.objects.all().delete()
#    e = Mfgmodeldescripfurn.objects.annotate(furnmfgmodeldescripA=F('furnmfgmodeldescrip'))
#    g = list(e.values_list('furnmfgmodeldescrip', flat=True).distinct())
#    try:
#        h = Mfgmodeldescrip.objects.create(id=1, mfgmodeldescrips=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Mfgmodeldescrip.objects.create(id=2, mfgmodeldescrips=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Mfgmodeldescrip.objects.create(id=3, mfgmodeldescrips=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Mfgmodeldescrip.objects.create(id=4, mfgmodeldescrips=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Mfgmodeldescrip.objects.create(id=5, mfgmodeldescrips=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Mfgmodeldescrip.objects.create(id=6, mfgmodeldescrips=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Mfgmodeldescrip.objects.create(id=7, mfgmodeldescrips=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Mfgmodeldescrip.objects.create(id=8, mfgmodeldescrips=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Mfgmodeldescrip.objects.create(id=9, mfgmodeldescrips=g[8])
#    except Exception:
#        h9 = 0
#    try:
#        h10 = Mfgmodeldescrip.objects.create(id=10, mfgmodeldescrips=g[9])
#    except Exception:
#        h10 = 0
#    try:
#        h11 = Mfgmodeldescrip.objects.create(id=11, mfgmodeldescrips=g[10])
#    except Exception:
#        h11 = 0
#    try:
#        h12 = Mfgmodeldescrip.objects.create(id=12, mfgmodeldescrips=g[11])
#    except Exception:
#        h12 = 0
#    try:
#        h13 = Mfgmodeldescrip.objects.create(id=13, mfgmodeldescrips=g[12])
#    except Exception:
#        h13 = 0
#    try:
#        h14 = Mfgmodeldescrip.objects.create(id=14, efmfgmodeldescripss=g[13])
#    except Exception:
#        h14 = 0
#    try:
#        h15 = Mfgmodeldescrip.objects.create(id=15, mfgmodeldescrips=g[14])
#    except Exception:
#        h15 = 0
#    try:
#        h16 = Mfgmodeldescrip.objects.create(id=16, mfgmodeldescrips=g[15])
#    except Exception:
#        h16 = 0
#    mfgmodeldescrip = Mfgmodeldescrip.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "mfgmodeldescrip": mfgmodeldescrip,
#        "form": form,
#    }
#    return render(request, 'mha/mfgmodeldescrip_1.html', context)
#
#
#def load_condmfgmodeldescrip2(request):
#    form = EquipInfo2(request.POST or None)
#    Mfgmodeldescrip.objects.all().delete()
#    e = Mfgmodeldescripcond.objects.annotate(condmfgmodeldescripA=F('condmfgmodeldescrip'))
#    g = list(e.values_list('condmfgmodeldescrip', flat=True).distinct())
#    try:
#        h = Mfgmodeldescrip.objects.create(id=1, mfgmodeldescrips=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Mfgmodeldescrip.objects.create(id=2, mfgmodeldescrips=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Mfgmodeldescrip.objects.create(id=3, mfgmodeldescrips=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Mfgmodeldescrip.objects.create(id=4, mfgmodeldescrips=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Mfgmodeldescrip.objects.create(id=5, mfgmodeldescrips=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Mfgmodeldescrip.objects.create(id=6, mfgmodeldescrips=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Mfgmodeldescrip.objects.create(id=7, mfgmodeldescrips=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Mfgmodeldescrip.objects.create(id=8, mfgmodeldescrips=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Mfgmodeldescrip.objects.create(id=9, mfgmodeldescrips=g[8])
#    except Exception:
#        h9 = 0
#    try:
#        h10 = Mfgmodeldescrip.objects.create(id=10, mfgmodeldescrips=g[9])
#    except Exception:
#        h10 = 0
#    try:
#        h11 = Mfgmodeldescrip.objects.create(id=11, mfgmodeldescrips=g[10])
#    except Exception:
#        h11 = 0
#    try:
#        h12 = Mfgmodeldescrip.objects.create(id=12, mfgmodeldescrips=g[11])
#    except Exception:
#        h12 = 0
#    try:
#        h13 = Mfgmodeldescrip.objects.create(id=13, mfgmodeldescrips=g[12])
#    except Exception:
#        h13 = 0
#    try:
#        h14 = Mfgmodeldescrip.objects.create(id=14, efmfgmodeldescripss=g[13])
#    except Exception:
#        h14 = 0
#    try:
#        h15 = Mfgmodeldescrip.objects.create(id=15, mfgmodeldescrips=g[14])
#    except Exception:
#        h15 = 0
#    try:
#        h16 = Mfgmodeldescrip.objects.create(id=16, mfgmodeldescrips=g[15])
#    except Exception:
#        h16 = 0
#    mfgmodeldescrip = Mfgmodeldescrip.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "mfgmodeldescrip": mfgmodeldescrip,
#        "form": form,
#    }
#    return render(request, 'mha/mfgmodeldescrip_1.html', context)
#
#
#def load_evapmfgmodeldescrip2(request):
#    form = EquipInfo2(request.POST or None)
#    Mfgmodeldescrip.objects.all().delete()
#    e = Mfgmodeldescripevap.objects.annotate(evapmfgmodeldescripA=F('evapmfgmodeldescrip'))
#    g = list(e.values_list('evapmfgmodeldescrip', flat=True).distinct())
#    try:
#        h = Mfgmodeldescrip.objects.create(id=1, mfgmodeldescrips=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Mfgmodeldescrip.objects.create(id=2, mfgmodeldescrips=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Mfgmodeldescrip.objects.create(id=3, mfgmodeldescrips=g[2])
#    except Exception:
#        h3 = 0
#    mfgmodeldescrip = Mfgmodeldescrip.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "mfgmodeldescrip": mfgmodeldescrip,
#        "form": form,
#    }
#    return render(request, 'mha/mfgmodeldescrip_1.html', context)
#
#
#def load_thermmfgmodeldescrip2(request):
#    form = EquipInfo2(request.POST or None)
#    Mfgmodeldescrip.objects.all().delete()
#    e = Mfgmodeldescriptherm.objects.annotate(thermmfgmodeldescripA=F('thermmfgmodeldescrip'))
#    g = list(e.values_list('thermmfgmodeldescrip', flat=True).distinct())
#    try:
#        h = Mfgmodeldescrip.objects.create(id=1, mfgmodeldescrips=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Mfgmodeldescrip.objects.create(id=2, mfgmodeldescrips=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Mfgmodeldescrip.objects.create(id=3, mfgmodeldescrips=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Mfgmodeldescrip.objects.create(id=4, mfgmodeldescrips=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Mfgmodeldescrip.objects.create(id=5, mfgmodeldescrips=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Mfgmodeldescrip.objects.create(id=6, mfgmodeldescrips=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Mfgmodeldescrip.objects.create(id=7, mfgmodeldescrips=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Mfgmodeldescrip.objects.create(id=8, mfgmodeldescrips=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Mfgmodeldescrip.objects.create(id=9, mfgmodeldescrips=g[8])
#    except Exception:
#        h9 = 0
#    try:
#        h10 = Mfgmodeldescrip.objects.create(id=10, mfgmodeldescrips=g[9])
#    except Exception:
#        h10 = 0
#    try:
#        h11 = Mfgmodeldescrip.objects.create(id=11, mfgmodeldescrips=g[10])
#    except Exception:
#        h11 = 0
#    try:
#        h12 = Mfgmodeldescrip.objects.create(id=12, mfgmodeldescrips=g[11])
#    except Exception:
#        h12 = 0
#    try:
#        h13 = Mfgmodeldescrip.objects.create(id=13, mfgmodeldescrips=g[12])
#    except Exception:
#        h13 = 0
#    try:
#        h14 = Mfgmodeldescrip.objects.create(id=14, efmfgmodeldescripss=g[13])
#    except Exception:
#        h14 = 0
#    try:
#        h15 = Mfgmodeldescrip.objects.create(id=15, mfgmodeldescrips=g[14])
#    except Exception:
#        h15 = 0
#    try:
#        h16 = Mfgmodeldescrip.objects.create(id=16, mfgmodeldescrips=g[15])
#    except Exception:
#        h16 = 0
#    mfgmodeldescrip = Mfgmodeldescrip.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "mfgmodeldescrip": mfgmodeldescrip,
#        "form": form,
#    }
#    return render(request, 'mha/mfgmodeldescrip_1.html', context)
#
#
#
#def load_furngasviv2(request):
#    form = EquipInfo2(request.POST or None)
#    Gasviv.objects.all().delete()
#    e = Gasvivfurn.objects.annotate(furngasvivsA=F('furngasvivs'))
#    g = list(e.values_list('furngasvivs', flat=True).distinct())
#    try:
#        h = Gasviv.objects.create(id=1, gasvivs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Gasviv.objects.create(id=2, gasvivs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Gasviv.objects.create(id=3, gasvivs=g[2])
#    except Exception:
#        h3 = 0
#    gasviv = Gasviv.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "gasviv": gasviv,
#        "form": form,
#    }
#    return render(request, 'mha/gasviv_1.html', context)
#
#
#
#def load_condgasviv2(request):
#    form = EquipInfo2(request.POST or None)
#    Gasviv.objects.all().delete()
#    e = Gasvivcond.objects.annotate(condgasvivsA=F('condgasvivs'))
#    g = list(e.values_list('condgasvivs', flat=True).distinct())
#    try:
#        h = Gasviv.objects.create(id=1, gasvivs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Gasviv.objects.create(id=2, gasvivs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Gasviv.objects.create(id=3, gasvivs=g[2])
#    except Exception:
#        h3 = 0
#    gasviv = Gasviv.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "gasviv": gasviv,
#        "form": form,
#    }
#    return render(request, 'mha/gasviv_1.html', context)
#
#
#
#def load_evapgasviv2(request):
#    form = EquipInfo2(request.POST or None)
#    Gasviv.objects.all().delete()
#    e = Gasvivevap.objects.annotate(evapgasvivsA=F('evapgasvivs'))
#    g = list(e.values_list('evapgasvivs', flat=True).distinct())
#    try:
#        h = Gasviv.objects.create(id=1, gasvivs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Gasviv.objects.create(id=2, gasvivs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Gasviv.objects.create(id=3, gasvivs=g[2])
#    except Exception:
#        h3 = 0
#    gasviv = Gasviv.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "gasviv": gasviv,
#        "form": form,
#    }
#    return render(request, 'mha/gasviv_1.html', context)
#
#
#def load_furnmotortype2(request):
#    form = EquipInfo2(request.POST or None)
#    Motortype.objects.all().delete()
#    e = Motortypefurn.objects.annotate(furnmotortypesA=F('furnmotortypes'))
#    g = list(e.values_list('furnmotortypes', flat=True).distinct())
#    try:
#        h = Motortype.objects.create(id=1, motortypes=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Motortype.objects.create(id=2, motortypes=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Motortype.objects.create(id=3, motortypes=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Motortype.objects.create(id=4, motortypes=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Motortype.objects.create(id=5, motortypes=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Motortype.objects.create(id=6, motortypes=g[5])
#    except Exception:
#        h6 = 0
#    motortype = Motortype.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "motortype": motortype,
#        "form": form,
#    }
#    return render(request, 'mha/motortype_1.html', context)
#
#
#def load_condmotortype2(request):
#    form = EquipInfo2(request.POST or None)
#    Motortype.objects.all().delete()
#    e = Motortypecond.objects.annotate(condmotortypesA=F('condmotortypes'))
#    g = list(e.values_list('condmotortypes', flat=True).distinct())
#    try:
#        h = Motortype.objects.create(id=1, motortypes=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Motortype.objects.create(id=2, motortypes=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Motortype.objects.create(id=3, motortypes=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Motortype.objects.create(id=4, motortypes=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Motortype.objects.create(id=5, motortypes=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Motortype.objects.create(id=6, motortypes=g[5])
#    except Exception:
#        h6 = 0
#    motortype = Motortype.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "motortype": motortype,
#        "form": form,
#    }
#    return render(request, 'mha/motortype_1.html', context)
#
#
#def load_evapmotortype2(request):
#    form = EquipInfo2(request.POST or None)
#    Motortype.objects.all().delete()
#    e = Motortypeevap.objects.annotate(evapmotortypesA=F('evapmotortypes'))
#    g = list(e.values_list('evapmotortypes', flat=True).distinct())
#    try:
#        h = Motortype.objects.create(id=1, motortypes=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Motortype.objects.create(id=2, motortypes=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Motortype.objects.create(id=3, motortypes=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Motortype.objects.create(id=4, motortypes=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Motortype.objects.create(id=5, motortypes=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Motortype.objects.create(id=6, motortypes=g[5])
#    except Exception:
#        h6 = 0
#    motortype = Motortype.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "motortype": motortype,
#        "form": form,
#    }
#    return render(request, 'mha/motortype_1.html', context)
#
#
#def load_Thermmotortype2(request):
#    form = EquipInfo2(request.POST or None)
#    Motortype.objects.all().delete()
#    e = Motortypetherm.objects.annotate(thermmotortypesA=F('thermmotortypes'))
#    g = list(e.values_list('thermmotortypes', flat=True).distinct())
#    try:
#        h = Motortype.objects.create(id=1, motortypes=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Motortype.objects.create(id=2, motortypes=g[1])
#    except Exception:
#        h2 = 0
#    motortype = Motortype.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "motortype": motortype,
#        "form": form,
#    }
#    return render(request, 'mha/motortype_1.html', context)
#
#
#def load_furndescription2(request):
#    form = EquipInfo2(request.POST or None)
#    Description.objects.all().delete()
#    e = Descriptionfurn.objects.annotate(furndescriptionA=F('furndescription'))
#    g = list(e.values_list('furndescription', flat=True).distinct())
#    try:
#        h = Description.objects.create(id=1, descriptions=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Description.objects.create(id=2, descriptions=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Description.objects.create(id=3, descriptions=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Description.objects.create(id=4, descriptions=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Description.objects.create(id=5, descriptions=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Description.objects.create(id=6, descriptions=g[5])
#    except Exception:
#        h6 = 0
#    description = Description.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "description": description,
#        "form": form,
#    }
#    return render(request, 'mha/description_1.html', context)
#
#
#def load_conddescription2(request):
#    form = EquipInfo2(request.POST or None)
#    Description.objects.all().delete()
#    e = Descriptioncond.objects.annotate(conddescriptionsA=F('conddescriptions'))
#    g = list(e.values_list('conddescriptions', flat=True).distinct())
#    try:
#        h = Description.objects.create(id=1, descriptions=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Description.objects.create(id=2, descriptions=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Description.objects.create(id=3, descriptions=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Description.objects.create(id=4, descriptions=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Description.objects.create(id=5, descriptions=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Description.objects.create(id=6, descriptions=g[5])
#    except Exception:
#        h6 = 0
#    description = Description.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "description": description,
#        "form": form,
#    }
#    return render(request, 'mha/description_1.html', context)
#
#
#def load_evapdescription2(request):
#    form = EquipInfo2(request.POST or None)
#    Description.objects.all().delete()
#    e = Descriptionevap.objects.annotate(evapdescriptionsA=F('evapdescriptions'))
#    g = list(e.values_list('evapdescriptions', flat=True).distinct())
#    try:
#        h = Description.objects.create(id=1, descriptions=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Description.objects.create(id=2, descriptions=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Description.objects.create(id=3, descriptions=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Description.objects.create(id=4, descriptions=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Description.objects.create(id=5, descriptions=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Description.objects.create(id=6, descriptions=g[5])
#    except Exception:
#        h6 = 0
#    description = Description.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "description": description,
#        "form": form,
#    }
#    return render(request, 'mha/description_1.html', context)
#
#
#def load_thermdescription2(request):
#    form = EquipInfo2(request.POST or None)
#    Description.objects.all().delete()
#    e = Descriptiontherm.objects.annotate(thermdescriptionsA=F('thermdescriptions'))
#    g = list(e.values_list('thermdescriptions', flat=True).distinct())
#    try:
#        h = Description.objects.create(id=1, descriptions=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Description.objects.create(id=2, descriptions=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Description.objects.create(id=3, descriptions=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Description.objects.create(id=4, descriptions=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Description.objects.create(id=5, descriptions=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Description.objects.create(id=6, descriptions=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Description.objects.create(id=1, descriptions=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Description.objects.create(id=2, descriptions=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Description.objects.create(id=3, descriptions=g[8])
#    except Exception:
#        h9 = 0
#    try:
#        h10 = Description.objects.create(id=4, descriptions=g[9])
#    except Exception:
#        h10 = 0
#    try:
#        h11 = Description.objects.create(id=5, descriptions=g[10])
#    except Exception:
#        h11 = 0
#    try:
#        h12 = Description.objects.create(id=6, descriptions=g[11])
#    except Exception:
#        h12 = 0
#    description = Description.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "description": description,
#        "form": form,
#    }
#    return render(request, 'mha/description_1.html', context)
#
#def load_Thermrefrig2(request):
#    form = EquipInfo2(request.POST or None)
#    Refrig.objects.all().delete()
#    e = Refrigetherm.objects.annotate(thermrefrigsA=F('thermrefrigs'))
#    g = list(e.values_list('thermrefrigs', flat=True).distinct())
#    try:
#        h = Refrig.objects.create(id=1, refrigs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Refrig.objects.create(id=2, refrigs=g[1])
#    except Exception:
#        h2 = 0
#    refrig = Refrig.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "refrig": refrig,
#        "form": form,
#    }
#    return render(request, 'mha/refrig_1.html', context)
#
#
#def load_thermbtu2(request):
#    form = EquipInfo2(request.POST or None)
#    Btu.objects.all().delete()
#    e = BTUtherm.objects.annotate(thermbtusA=F('thermbtus'))
#    g = list(e.values_list('thermbtus', flat=True).distinct())
#    try:
#        h = Btu.objects.create(id=1, btus=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Btu.objects.create(id=2, btus=g[1])
#    except Exception:
#        h2 = 0
#    btu = Btu.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "btu": btu,
#        "form": form,
#    }
#    return render(request, 'mha/btu_1.html', context)
#
#
#def load_thermoutputstg12(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg1.objects.all().delete()
#    e = Outputstg1therm.objects.annotate(thermoutputstg1sA=F('thermoutputstg1s'))
#    g = list(e.values_list('thermoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg1.objects.create(id=1, outputstg1s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg1.objects.create(id=2, outputstg1s=g[1])
#    except Exception:
#        h2 = 0
#    outputstg1 = Outputstg1.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg1": outputstg1,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg1_1.html', context)
#
#
#def load_thermoutputstg22(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg2.objects.all().delete()
#    e = Outputstg1therm.objects.annotate(thermoutputstg1sA=F('thermoutputstg1s'))
#    g = list(e.values_list('thermoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg2.objects.create(id=1, outputstg2s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg2.objects.create(id=2, outputstg2s=g[1])
#    except Exception:
#        h2 = 0
#    outputstg2 = Outputstg2.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg2": outputstg2,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg2_1.html', context)
#
#
#def load_thermoutputstg32(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg3.objects.all().delete()
#    e = Outputstg1therm.objects.annotate(thermoutputstg1sA=F('thermoutputstg1s'))
#    g = list(e.values_list('thermoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg3.objects.create(id=1, outputstg3s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg3.objects.create(id=2, outputstg3s=g[1])
#    except Exception:
#        h2 = 0
#    outputstg3 = Outputstg3.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg3": outputstg3,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg3_1.html', context)
#
#
#
#def load_furnrefrig2(request):
#    form = EquipInfo2(request.POST or None)
#    Refrig.objects.all().delete()
#    e = Refrigfurn.objects.annotate(furnrefrigsA=F('furnrefrigs'))
#    g = list(e.values_list('furnrefrigs', flat=True).distinct())
#    try:
#        h = Refrig.objects.create(id=1, refrigs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Refrig.objects.create(id=2, refrigs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Refrig.objects.create(id=3, refrigs=g[2])
#    except Exception:
#        h3 = 0
#    refrig = Refrig.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "refrig": refrig,
#        "form": form,
#    }
#    return render(request, 'mha/refrig_1.html', context)
#
#
#def load_condrefrig2(request):
#    form = EquipInfo2(request.POST or None)
#    Refrig.objects.all().delete()
#    e = Refrigcond.objects.annotate(condrefrigsA=F('condrefrigs'))
#    g = list(e.values_list('condrefrigs', flat=True).distinct())
#    try:
#        h = Refrig.objects.create(id=1, refrigs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Refrig.objects.create(id=2, refrigs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Refrig.objects.create(id=3, refrigs=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Refrig.objects.create(id=4, refrigs=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Refrig.objects.create(id=5, refrigs=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Refrig.objects.create(id=6, refrigs=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Refrig.objects.create(id=7, refrigs=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Refrig.objects.create(id=8, refrigs=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Refrig.objects.create(id=9, refrigs=g[8])
#    except Exception:
#        h9 = 0
#    refrig = Refrig.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "refrig": refrig,
#        "form": form,
#    }
#    return render(request, 'mha/refrig_1.html', context)
#
#
#def load_evaprefrig2(request):
#    form = EquipInfo2(request.POST or None)
#    Refrig.objects.all().delete()
#    e = Refrigevap.objects.annotate(evaprefrigsA=F('evaprefrigs'))
#    g = list(e.values_list('evaprefrigs', flat=True).distinct())
#    try:
#        h = Refrig.objects.create(id=1, refrigs=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Refrig.objects.create(id=2, refrigs=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Refrig.objects.create(id=3, refrigs=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Refrig.objects.create(id=4, refrigs=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Refrig.objects.create(id=5, refrigs=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Refrig.objects.create(id=6, refrigs=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Refrig.objects.create(id=7, refrigs=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Refrig.objects.create(id=8, refrigs=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Refrig.objects.create(id=9, refrigs=g[8])
#    except Exception:
#        h9 = 0
#    refrig = Refrig.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "refrig": refrig,
#        "form": form,
#    }
#    return render(request, 'mha/refrig_1.html', context)
#
#
#def load_furnbtu2(request):
#    form = EquipInfo2(request.POST or None)
#    Btu.objects.all().delete()
#    e = BTUfurn.objects.annotate(furnbtusA=F('furnbtus'))
#    g = list(e.values_list('furnbtus', flat=True).distinct())
#    try:
#        h = Btu.objects.create(id=1, btus=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Btu.objects.create(id=2, btus=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Btu.objects.create(id=3, btus=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Btu.objects.create(id=4, btus=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Btu.objects.create(id=5, btus=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Btu.objects.create(id=6, btus=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Btu.objects.create(id=7, btus=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Btu.objects.create(id=8, btus=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Btu.objects.create(id=9, btus=g[8])
#    except Exception:
#        h9 = 0
#    btu = Btu.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "btu": btu,
#        "form": form,
#    }
#    return render(request, 'mha/btu_1.html', context)
#
#
#def load_condbtu2(request):
#    form = EquipInfo2(request.POST or None)
#    Btu.objects.all().delete()
#    e = BTUcond.objects.annotate(condbtusA=F('condbtus'))
#    g = list(e.values_list('condbtus', flat=True).distinct())
#    try:
#        h = Btu.objects.create(id=1, btus=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Btu.objects.create(id=2, btus=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Btu.objects.create(id=3, btus=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Btu.objects.create(id=4, btus=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Btu.objects.create(id=5, btus=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Btu.objects.create(id=6, btus=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Btu.objects.create(id=7, btus=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Btu.objects.create(id=8, btus=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Btu.objects.create(id=9, btus=g[8])
#    except Exception:
#        h9 = 0
#    btu = Btu.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "btu": btu,
#        "form": form,
#    }
#    return render(request, 'mha/btu_1.html', context)
#
#
#def load_evapbtu2(request):
#    form = EquipInfo2(request.POST or None)
#    Btu.objects.all().delete()
#    e = BTUevap.objects.annotate(evapbtusA=F('evapbtus'))
#    g = list(e.values_list('evapbtus', flat=True).distinct())
#    try:
#        h = Btu.objects.create(id=1, btus=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Btu.objects.create(id=2, btus=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Btu.objects.create(id=3, btus=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Btu.objects.create(id=4, btus=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Btu.objects.create(id=5, btus=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Btu.objects.create(id=6, btus=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Btu.objects.create(id=7, btus=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Btu.objects.create(id=8, btus=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Btu.objects.create(id=9, btus=g[8])
#    except Exception:
#        h9 = 0
#    btu = Btu.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "btu": btu,
#        "form": form,
#    }
#    return render(request, 'mha/btu_1.html', context)
#
#
#def load_furnoutputstg12(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg1.objects.all().delete()
#    e = Outputstg1furn.objects.annotate(furnoutputstg1sA=F('furnoutputstg1s'))
#    g = list(e.values_list('furnoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg1.objects.create(id=1, outputstg1s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg1.objects.create(id=2, outputstg1s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg1.objects.create(id=3, outputstg1s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg1.objects.create(id=4, outputstg1s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg1.objects.create(id=5, outputstg1s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg1.objects.create(id=6, outputstg1s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg1.objects.create(id=7, outputstg1s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg1.objects.create(id=8, outputstg1s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg1.objects.create(id=9, outputstg1s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg1 = Outputstg1.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg1": outputstg1,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg1_1.html', context)
#
#
#
#def load_condoutputstg12(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg1.objects.all().delete()
#    e = Outputstg1cond.objects.annotate(condoutputstg1sA=F('condoutputstg1s'))
#    g = list(e.values_list('condoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg1.objects.create(id=1, outputstg1s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg1.objects.create(id=2, outputstg1s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg1.objects.create(id=3, outputstg1s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg1.objects.create(id=4, outputstg1s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg1.objects.create(id=5, outputstg1s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg1.objects.create(id=6, outputstg1s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg1.objects.create(id=7, outputstg1s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg1.objects.create(id=8, outputstg1s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg1.objects.create(id=9, outputstg1s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg1 = Outputstg1.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg1": outputstg1,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg1_1.html', context)
#
#
#def load_evapoutputstg12(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg1.objects.all().delete()
#    e = Outputstg1evap.objects.annotate(evapoutputstg1sA=F('evapoutputstg1s'))
#    g = list(e.values_list('evapoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg1.objects.create(id=1, outputstg1s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg1.objects.create(id=2, outputstg1s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg1.objects.create(id=3, outputstg1s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg1.objects.create(id=4, outputstg1s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg1.objects.create(id=5, outputstg1s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg1.objects.create(id=6, outputstg1s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg1.objects.create(id=7, outputstg1s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg1.objects.create(id=8, outputstg1s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg1.objects.create(id=9, outputstg1s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg1 = Outputstg1.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg1": outputstg1,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg1_1.html', context)
#
#
#def load_furnoutputstg22(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg2.objects.all().delete()
#    e = Outputstg2furn.objects.annotate(outputstg2furnsA=F('outputstg2furns'))
#    g = list(e.values_list('outputstg2furns', flat=True).distinct())
#    try:
#        h = Outputstg2.objects.create(id=1, outputstg2s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg2.objects.create(id=2, outputstg2s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg2.objects.create(id=3, outputstg2s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg2.objects.create(id=4, outputstg2s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg2.objects.create(id=5, outputstg2s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg2.objects.create(id=6, outputstg2s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg2.objects.create(id=7, outputstg2s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg2.objects.create(id=8, outputstg2s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg2.objects.create(id=9, outputstg2s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg2 = Outputstg2.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg2": outputstg2,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg2_1.html', context)
#
#
#def load_condoutputstg22(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg2.objects.all().delete()
#    e = Outputstg1cond.objects.annotate(condoutputstg1sA=F('condoutputstg1s'))
#    g = list(e.values_list('condoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg2.objects.create(id=1, outputstg2s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg2.objects.create(id=2, outputstg2s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg2.objects.create(id=3, outputstg2s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg2.objects.create(id=4, outputstg2s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg2.objects.create(id=5, outputstg2s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg2.objects.create(id=6, outputstg2s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg2.objects.create(id=7, outputstg2s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg2.objects.create(id=8, outputstg2s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg2.objects.create(id=9, outputstg2s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg2 = Outputstg2.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg2": outputstg2,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg2_1.html', context)
#
#
#def load_evapoutputstg22(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg2.objects.all().delete()
#    e = Outputstg1evap.objects.annotate(evapoutputstg1sA=F('evapoutputstg1s'))
#    g = list(e.values_list('evapoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg2.objects.create(id=1, outputstg2s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg2.objects.create(id=2, outputstg2s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg2.objects.create(id=3, outputstg2s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg2.objects.create(id=4, outputstg2s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg2.objects.create(id=5, outputstg2s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg2.objects.create(id=6, outputstg2s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg2.objects.create(id=7, outputstg2s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg2.objects.create(id=8, outputstg2s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg2.objects.create(id=9, outputstg2s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg2 = Outputstg2.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg2": outputstg2,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg2_1.html', context)
#
#
#def load_furnoutputstg32(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg3.objects.all().delete()
#    e = Outputstg3furn.objects.annotate(outputstg3furnsA=F('outputstg3furns'))
#    g = list(e.values_list('outputstg3furns', flat=True).distinct())
#    try:
#        h = Outputstg3.objects.create(id=1, outputstg3s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg3.objects.create(id=2, outputstg3s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg3.objects.create(id=3, outputstg3s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg3.objects.create(id=4, outputstg3s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg3.objects.create(id=5, outputstg3s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg3.objects.create(id=6, outputstg3s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg3.objects.create(id=7, outputstg3s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg3.objects.create(id=8, outputstg3s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg3.objects.create(id=9, outputstg3s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg3 = Outputstg3.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg3": outputstg3,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg3_1.html', context)
#
#
#def load_condoutputstg32(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg3.objects.all().delete()
#    e = Outputstg1cond.objects.annotate(condoutputstg1sA=F('condoutputstg1s'))
#    g = list(e.values_list('condoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg3.objects.create(id=1, outputstg3s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg3.objects.create(id=2, outputstg3s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg3.objects.create(id=3, outputstg3s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg3.objects.create(id=4, outputstg3s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg3.objects.create(id=5, outputstg3s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg3.objects.create(id=6, outputstg3s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg3.objects.create(id=7, outputstg3s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg3.objects.create(id=8, outputstg3s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg3.objects.create(id=9, outputstg3s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg3 = Outputstg3.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg3": outputstg3,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg3_1.html', context)
#
#
#def load_evapoutputstg32(request):
#    form = EquipInfo2(request.POST or None)
#    Outputstg3.objects.all().delete()
#    e = Outputstg1evap.objects.annotate(evapoutputstg1sA=F('evapoutputstg1s'))
#    g = list(e.values_list('evapoutputstg1s', flat=True).distinct())
#    try:
#        h = Outputstg3.objects.create(id=1, outputstg3s=g[0])
#    except Exception:
#        h = 0
#    try:
#        h2 = Outputstg3.objects.create(id=2, outputstg3s=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Outputstg3.objects.create(id=3, outputstg3s=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Outputstg3.objects.create(id=4, outputstg3s=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Outputstg3.objects.create(id=5, outputstg3s=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Outputstg3.objects.create(id=6, outputstg3s=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Outputstg3.objects.create(id=7, outputstg3s=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Outputstg3.objects.create(id=8, outputstg3s=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Outputstg3.objects.create(id=9, outputstg3s=g[8])
#    except Exception:
#        h9 = 0
#    outputstg3 = Outputstg3.objects.all()
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return HttpResponseRedirect(instance.get_absolute3_url())
#    context = {
#        "outputstg3": outputstg3,
#        "form": form,
#    }
#    return render(request, 'mha/outputstg3_1.html', context)
#
#

















def load_2cost(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    cost = a.values('cost').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_1edit.html', context)


def load_2height(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    height = a.values('height').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "height": height,
        "form": form,
    }
    return render(request, 'mha/height_1.html', context)


def load_2width(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    width = a.values('width').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "width": width,
        "form": form,
    }
    return render(request, 'mha/width_1.html', context)


def load_2depth(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    depth = a.values('depth').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "depth": depth,
        "form": form,
    }
    return render(request, 'mha/depth_1.html', context)


def load_2warr(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    warr = a.values('warr').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "warr": warr,
        "form": form,
    }
    return render(request, 'mha/warr_1.html', context)




#def eff(request):
#    form = EquipInfo2(request.POST)
#    Mfgmodeldescrip.objects.all().delete()
#    b = Equipment2.objects.values_list('id', flat=True).last()
#    c = Equipment2.objects.values_list('mfg', flat=True).last()
#    d = Equipment2.objects.values_list('type', flat=True).last()
#    e = request.POST['id_eff']
#    Equipment2.objects.filter(id=b).update(eff=e)
#    queryset = Equipment2.objects.filter(mfg=c, type=d).exclude(mfgmodeldescrip=None)
#    if queryset:
#        Mfgmodeldescrip.objects.create(mfgmodeldescrips='Add New Model Description')
#        mfgmodeldescrip_list = list(queryset)
#        for mfgmodeldescrip in mfgmodeldescrip_list:
#            Mfgmodeldescrip.objects.create(mfgmodeldescrips=mfgmodeldescrip.mfgmodeldescrip)
#    else:
#        Mfgmodeldescrip.objects.create(mfgmodeldescrips='Add New Model Description')
#
#
#
#    context = {
#        "form": form,
#    }
#    return render(request, 'mha/addnewequip2.html', context)








def eff2cond(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_eff3']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(eff=a)
    e = Condeff.objects.create(effcond=a)
    e1 = Eff.objects.create(effs=a)
    f = Equipment2.objects.filter(id=b).update(eff3="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_effcond(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    eff = a.values('eff').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "eff": eff,
        "form": form,
    }
    return render(request, 'mha/eff_1.html', context)


def eff2evap(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_eff4']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(eff=a)
    e = Evapeff.objects.create(effevap=a)
    e1 = Eff.objects.create(effs=a)
    f = Equipment2.objects.filter(id=b).update(eff4="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_effevap(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    eff = a.values('eff').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "eff": eff,
        "form": form,
    }
    return render(request, 'mha/eff_1.html', context)






#def mfgmodeldescrip(request):
#    form = EquipInfo2(request.POST)
#    Gasviv.objects.all().delete()
#    Description.objects.all().delete()
#    b = Equipment2.objects.values_list('id', flat=True).last()
#    c = Equipment2.objects.values_list('mfg', flat=True).last()
#    d = Equipment2.objects.values_list('type', flat=True).last()
#    e = request.POST['id_mfgmodeldescrip']
#    Equipment2.objects.filter(id=b).update(mfgmodeldescrip=e)
#    queryset = Equipment2.objects.filter(mfg=c, type=d).exclude(gasviv=None)
#
#    if queryset:
#        Gasviv.objects.create(gasvivs='Add New Gas VIv')
#        gasviv_list = list(queryset)
#        for gasviv in gasviv_list:
#            Gasviv.objects.create(gasvivs=gasviv.gasviv)
#    else:
#        Gasviv.objects.create(gasvivs='Add New Gas VIv')
#
#    e = Equipment2.objects.filter(type='Thermostat').annotate(descriptionA=F('description'))
#    g = list(e.values_list('description', flat=True).distinct())
#    try:
#        h = Description.objects.create(id=1, descriptions="Add New Model Description")
#    except Exception:
#        h = 0
#    try:
#        h1 = Description.objects.create(id=2, descriptions=g[0])
#    except Exception:
#        h1 = 0
#    try:
#        h2 = Description.objects.create(id=3, descriptions=g[1])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = Description.objects.create(id=4, descriptions=g[2])
#    except Exception:
#        h3 = 0
#    try:
#        h4 = Description.objects.create(id=5, descriptions=g[3])
#    except Exception:
#        h4 = 0
#    try:
#        h5 = Description.objects.create(id=6, descriptions=g[4])
#    except Exception:
#        h5 = 0
#    try:
#        h6 = Description.objects.create(id=7, descriptions=g[5])
#    except Exception:
#        h6 = 0
#    try:
#        h7 = Description.objects.create(id=8, descriptions=g[6])
#    except Exception:
#        h7 = 0
#    try:
#        h8 = Description.objects.create(id=9, descriptions=g[7])
#    except Exception:
#        h8 = 0
#    try:
#        h9 = Description.objects.create(id=10, descriptions=g[8])
#    except Exception:
#        h9 = 0
#    try:
#        h10 = Description.objects.create(id=11, descriptions=g[9])
#    except Exception:
#        h10 = 0
#
#    context = {
#        "form": form,
#        "h": h,
#        "h1": h1,
#        "h2": h2,
#        "h3": h3,
#        "h4": h4,
#        "h5": h5,
#        "h6": h6,
#        "h7": h7,
#        "h8": h8,
#        "h9": h9,
#        "h10": h10,
#    }
#    return render(request, 'mha/addnewequip2.html', context)


def mfgmodeldescrip2(request):
    form = EquipInfo(request.POST)
    a = request.POST['id_mfgmodeldescrip2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(mfgmodeldescrip=a)
    c2 = Mfgmodeldescrip.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Mfgmodeldescrip.objects.create(id=d2, mfgmodeldescrips=a)
    f = Equipment2.objects.filter(id=b).update(mfgmodeldescrip2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_mfgmodeldescrip2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    mfgmodeldescrip = a.values('mfgmodeldescrip').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)



def mfgmodeldescrip2cond(request):
    form = EquipInfo(request.POST)
    a = request.POST['id_mfgmodeldescrip3']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(mfgmodeldescrip=a)
    c1 = Mfgmodeldescripcond.objects.values_list('id', flat=True).last()
    c2 = Mfgmodeldescrip.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Mfgmodeldescripcond.objects.create(id=d1, condmfgmodeldescrip=a)
    e1 = Mfgmodeldescrip.objects.create(id=d2,mfgmodeldescrips=a)
    f = Equipment2.objects.filter(id=b).update(mfgmodeldescrip2="")

    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_mfgmodeldescripcond(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    mfgmodeldescrip = a.values('mfgmodeldescrip').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)

def mfgmodeldescrip2evap(request):
    form = EquipInfo(request.POST)
    a = request.POST['id_mfgmodeldescrip4']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(mfgmodeldescrip=a)
    c1 = Mfgmodeldescripevap.objects.values_list('id', flat=True).last()
    c2 = Mfgmodeldescrip.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Mfgmodeldescripevap.objects.create(id=d1, evapmfgmodeldescrip=a)
    e1 = Mfgmodeldescrip.objects.create(id=d2, mfgmodeldescrips=a)
    f = Equipment2.objects.filter(id=b).update(mfgmodeldescrip4="")

    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_mfgmodeldescripevap(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    mfgmodeldescrip = a.values('mfgmodeldescrip').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)

def mfgmodeldescrip2therm(request):
    form = EquipInfo(request.POST)
    a = request.POST['id_mfgmodeldescrip5']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(mfgmodeldescrip=a)
    c1 = Mfgmodeldescriptherm.objects.values_list('id', flat=True).last()
    c2 = Mfgmodeldescrip.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Mfgmodeldescriptherm.objects.create(id=d1, thermmfgmodeldescrip=a)
    e1 = Mfgmodeldescrip.objects.create(id=d2, mfgmodeldescrips=a)
    f = Equipment2.objects.filter(id=b).update(mfgmodeldescrip5="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_mfgmodeldescriptherm(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    mfgmodeldescrip = a.values('mfgmodeldescrip').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)



def gasviv2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_gasviv2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(gasviv=a)
    c2 = Mfgmodeldescrip.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Gasviv.objects.create(id=d2, gasvivs=a)
    f = Equipment2.objects.filter(id=b).update(gasviv2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_gasviv2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    gasviv = a.values('gasviv').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "gasviv": gasviv,
        "form": form,
    }
    return render(request, 'mha/gasviv_1.html', context)





def load_motortypeedit(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfo2(request.POST or None, instance=instance)
    motortype = Equipment2.objects.values('motortype').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "motortype": motortype,
        "form": form,
    }
    return render(request, 'mha/motortype_1.html', context)





def motortype2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_motortype2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(motortype=a)
    c2 = Motortype.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Motortype.objects.create(id=d2, motortypes=a)
    f = Equipment2.objects.filter(id=b).update(motortype2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_motortype2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    motortype = a.values('motortype').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "motortype": motortype,
        "form": form,
    }
    return render(request, 'mha/motortype_1.html', context)







def description2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_description2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(description=a)
    c2 = Description.objects.values_list('id', flat=True).last()
    d1 = c2 + 1
    e = Description.objects.create(id=d1, descriptions=a)
#    f = Equipment2.objects.filter(id=b).update(description2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
#        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_description2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    description = a.values('description').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "description": description,
        "form": form,
    }
    return render(request, 'mha/description_1.html', context)




def description2cond(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_description3']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(description=a)
    c1 = Descriptioncond.objects.values_list('id', flat=True).last()
    c2 = Description.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Descriptioncond.objects.create(id=d1, conddescriptions=a)
    e1 = Description.objects.create(id=d2, descriptions=a)
    f = Equipment2.objects.filter(id=b).update(description2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_descriptioncond(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    description = a.values('description').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "description": description,
        "form": form,
    }
    return render(request, 'mha/description_1.html', context)


def description2evap(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_description4']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(description=a)
    c1 = Descriptionevap.objects.values_list('id', flat=True).last()
    c2 = Description.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Descriptionevap.objects.create(id=d1, evapdescriptions=a)
    e1 = Description.objects.create(id=d2, descriptions=a)
    f = Equipment2.objects.filter(id=b).update(description4="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_descriptionevap(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    description = a.values('description').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "description": description,
        "form": form,
    }
    return render(request, 'mha/description_1.html', context)

def description2therm(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_description5']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(description=a)
    c1 = Descriptiontherm.objects.values_list('id', flat=True).last()
    c2 = Description.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Descriptiontherm.objects.create(id=d1, thermdescriptions=a)
    e1 = Description.objects.create(id=d2, descriptions=a)
    f = Equipment2.objects.filter(id=b).update(description5="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_descriptiontherm(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    description = a.values('description').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "description": description,
        "form": form,
    }
    return render(request, 'mha/description_1.html', context)



def refrig2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_refrig2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(refrig=a)
    c2 = Refrig.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Refrig.objects.create(id=d2, refrigs=a)
    f = Equipment2.objects.filter(id=b).update(refrig2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_refrig2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    refrig = a.values('refrig').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "refrig": refrig,
        "form": form,
    }
    return render(request, 'mha/refrig_1.html', context)





def load_refrigedit(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    refrig = Equipment2.objects.values('refrig').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "refrig": refrig,
        "form": form,
    }
    return render(request, 'mha/refrig_1.html', context)


def refrig2cond(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_refrig3']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(refrig=a)
    c1 = Refrigcond.objects.values_list('id', flat=True).last()
    c2 = Refrig.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Refrigcond.objects.create(id=d1, condrefrigs=a)
    e1 = Refrig.objects.create(id=d2, refrigs=a)
    f = Equipment2.objects.filter(id=b).update(refrig3="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)

def load_refrigcond(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    refrig = a.values('refrig').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "refrig": refrig,
        "form": form,
    }
    return render(request, 'mha/refrig_1.html', context)


def refrig2evap(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_refrig4']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(refrig=a)
    c1 = Refrigevap.objects.values_list('id', flat=True).last()
    c2 = Refrig.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = Refrigevap.objects.create(id=d1, evaprefrigs=a)
    e1 = Refrig.objects.create(id=d2, refrigs=a)
    f = Equipment2.objects.filter(id=b).update(refrig3="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)

def load_refrigevap(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    refrig = a.values('refrig').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "refrig": refrig,
        "form": form,
    }
    return render(request, 'mha/refrig_1.html', context)



def btu2cond(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_btu3']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(btu=a)
    c1 = BTUcond.objects.values_list('id', flat=True).last()
    c2 = Btu.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = BTUcond.objects.create(id=d1, condbtus=a)
    e1 = Btu.objects.create(id=d2, btus=a)
    f = Equipment2.objects.filter(id=b).update(btu3="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)

def load_btucond(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    btu = a.values('btu').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "btu": btu,
        "form": form,
    }
    return render(request, 'mha/btu_1.html', context)


def btu2evap(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_btu4']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(btu=a)
    c1 = BTUevap.objects.values_list('id', flat=True).last()
    c2 = Btu.objects.values_list('id', flat=True).last()
    d1 = c1 + 1
    d2 = c2 + 1
    e = BTUevap.objects.create(id=d1, evapbtus=a)
    e1 = Btu.objects.create(id=d2, btus=a)
    f = Equipment2.objects.filter(id=b).update(btu4="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "e1": e1,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)

def load_btuevap(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    btu = a.values('btu').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "btu": btu,
        "form": form,
    }
    return render(request, 'mha/btu_1.html', context)



def btu2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_btu2']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(btu=a)
    c2 = Btu.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Btu.objects.create(id=d2, btus=a)
    f = Equipment2.objects.filter(id=b).update(btu2="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_btu2(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    btu = a.values('btu').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "btu": btu,
        "form": form,
    }
    return render(request, 'mha/btu_1.html', context)





def load_btuedit(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    btu = Equipment2.objects.values('btu').get(modelnum=modelnum)
    context = {
        "instance": instance,
        "btu": btu,
        "form": form,
    }
    return render(request, 'mha/btu_1.html', context)


def outputstg12(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_outputstg12']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(outputstg1=a)
    c2 = Outputstg1.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Outputstg1.objects.create(id=d2, outputstg1s=a)
    f = Equipment2.objects.filter(id=b).update(outputstg12="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_outputstg12(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    outputstg1 = a.values('outputstg1').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "outputstg1": outputstg1,
        "form": form,
    }
    return render(request, 'mha/outputstg1_1.html', context)








def outputstg22(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_outputstg22']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(outputstg2=a)
    c2 = Outputstg2.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Outputstg2.objects.create(id=d2, outputstg2s=a)
    f = Equipment2.objects.filter(id=b).update(outputstg22="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_outputstg22(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    outputstg2 = a.values('outputstg2').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "outputstg2": outputstg2,
        "form": form,
    }
    return render(request, 'mha/outputstg2_1.html', context)


def outputstg32(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_outputstg32']
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = Equipment2.objects.filter(id=b).update(outputstg3=a)
    c2 = Outputstg3.objects.values_list('id', flat=True).last()
    d2 = c2 + 1
    e = Outputstg3.objects.create(id=d2, outputstg3s=a)
    f = Equipment2.objects.filter(id=b).update(outputstg32="")
    context = {
        "form": form,
        "c": c,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewequip2.html', context)


def load_outputstg32(request):
    a = Equipment2.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment2.objects.get(id=b)
    form = EquipInfo2(request.POST or None, instance=instance)
    outputstg3 = a.values('outputstg3').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "outputstg3": outputstg3,
        "form": form,
    }
    return render(request, 'mha/outputstg3_1.html', context)






def cost(request):
    form = EquipInfo2(request.POST)
    Warr.objects.all().delete()
    b = Equipment2.objects.values_list('id', flat=True).last()
    c = request.POST['cost_id']
    Equipment2.objects.filter(id=b).update(cost=c)

    e = Equipment2.objects.filter(type='Thermostat').annotate(warrA=F('warr'))
    g = list(e.values_list('warr', flat=True).distinct().exclude(warr='Add New Warranty'))
    try:
        h = Warr.objects.create(id=1, warrs="Add New Warranty")
    except Exception:
        h = 0
    try:
        h1 = Warr.objects.create(id=2, warrs=g[0])
    except Exception:
        h1 = 0
    try:
        h2 = Warr.objects.create(id=3, warrs=g[1])
    except Exception:
        h2 = 0
    try:
        h3 = Warr.objects.create(id=4, warrs=g[2])
    except Exception:
        h3 = 0
    try:
        h4 = Warr.objects.create(id=5, warrs=g[3])
    except Exception:
        h4 = 0
    try:
        h5 = Warr.objects.create(id=6, warrs=g[4])
    except Exception:
        h5 = 0
    try:
        h6 = Warr.objects.create(id=7, warrs=g[5])
    except Exception:
        h6 = 0
    try:
        h7 = Warr.objects.create(id=8, warrs=g[6])
    except Exception:
        h7 = 0
    try:
        h8 = Warr.objects.create(id=9, warrs=g[7])
    except Exception:
        h8 = 0
    try:
        h9 = Warr.objects.create(id=10, warrs=g[8])
    except Exception:
        h9 = 0
    try:
        h10 = Warr.objects.create(id=11, warrs=g[9])
    except Exception:
        h10 = 0

    context = {
        "form": form,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
    }
    return render(request, 'mha/addnewequip2.html', context)


def costA(request):
    form = EquipInfo(request.POST)
    a = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    d = request.POST['cost_id']
    Equipment.objects.filter(id=a).update(cost=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def cost2(request):
    form = EquipInfo(request.POST)
    a = Equipment.objects.values_list('id', flat=True).last()
    d = request.POST['cost_id']
    Equipment.objects.filter(id=a).update(cost=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)

def load_costedit2(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfoEdit(request.POST or None, instance=instance)

    cost = Equipment2.objects.values('cost').get(id=id)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_1edit.html', context)



def load_costedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    cost = Equipment2.objects.values('cost').get(id=id)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_1edit.html', context)


def load_cost2(request):
    a = Equipment.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Equipment.objects.get(id=b)
    form = EquipInfo(request.POST or None, instance=instance)
    cost = a.values('cost').get(id=b)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_2.html', context)


def load_cost3(request):
    a = Equipment.objects.all()
    b = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    instance = Equipment.objects.get(id=b)
    form = EquipInfo(request.POST or None, instance=instance)
    cost = a.values('cost').get(id=b)
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/cost_2.html', context)


def load_coilheightedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    height = Equipment2.objects.values('height').get(id=id)
    context = {
        "instance": instance,
        "height": height,
        "form": form,
    }
    return render(request, 'mha/coilheightedit_1.html', context)


def load_coilwidthedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    width = Equipment2.objects.values('width').get(id=id)
    context = {
        "instance": instance,
        "width": width,
        "form": form,
    }
    return render(request, 'mha/coilwidthedit_1.html', context)


def load_coildepthedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    depth = Equipment2.objects.values('depth').get(id=id)
    context = {
        "instance": instance,
        "depth": depth,
        "form": form,
    }
    return render(request, 'mha/coildepthedit_1.html', context)


def warr(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['id_warr']
    #   e = Warr.objects.filter(id=d).values_list('warrs', flat=True)
    Equipment2.objects.filter(id=b).update(warr=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def warrA(request):
    form = EquipInfo(request.POST)
    a = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    d = request.POST['id_warr']
    Equipment.objects.filter(id=a).update(warr_id=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip.html', context)


def warr2(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_warr2']
    b = Warr.objects.create(warrs=a)
    c = Warr.objects.values_list('id', flat=True).last()
    e = Equipment2.objects.values_list('id', flat=True).last()
    g = Equipment2.objects.filter(id=e).update(warr=a)
    context = {
        "form": form,
        "b": b,
        "e": e,
        "c": c,
        "g": g,
    }
    return render(request, 'mha/addnewequip2.html', context)


def warr3(request):
    form = EquipInfo2(request.POST)
    a = request.POST['id_warr2']
    b = Warr.objects.create(warrs=a)
    c = Warr.objects.values_list('id', flat=True).last()
    d = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    e = Equipment.objects.filter(id=d).update(warr_id=c)
    context = {
        "form": form,
        "b": b,
        "e": e,
    }
    return render(request, 'mha/editquip.html', context)


def warredit(request, modelnum=None):
    instance = Equipment2.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    d = request.POST['id_warr']
    Equipment.objects.filter(modelnum=modelnum).update(warr_id=d)
    Equipment2.objects.filter(modelnum=modelnum).update(warr=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)





def load_warr2(request):
    form = EquipInfo2(request.POST or None)
    warr = Warr.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "warr": warr,
        "form": form,
    }
    return render(request, 'mha/warr_1.html', context)


def height(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['height_id']
    Equipment2.objects.filter(id=b).update(height=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def heightA(request):
    form = EquipInfo(request.POST)
    a = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    d = request.POST['height_id']
    Equipment.objects.filter(id=a).update(height=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)





def load_height2(request):
    a = Equipment2.objects.all()
    instance = Equipment2.objects.get(id=a)
    form = EquipInfo2(request.POST or None, instance=instance)
    height = a.values('height').get(id=a)
    context = {
        "instance": instance,
        "height": height,
        "form": form,
    }
    return render(request, 'mha/height_2.html', context)


def width(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['width_id']
    Equipment2.objects.filter(id=b).update(width=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def widthA(request):
    form = EquipInfo(request.POST)
    a = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    d = request.POST['width_id']
    Equipment.objects.filter(id=a).update(width=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)



def load_width2(request):
    a = Equipment2.objects.all()
    b = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    instance = Equipment.objects.get(id=b)
    form = EquipInfo(request.POST or None, instance=instance)
    width = a.values('width').get(id=b)
    context = {
        "instance": instance,
        "width": width,
        "form": form,
    }
    return render(request, 'mha/width_2.html', context)


def depth(request):
    form = EquipInfo2(request.POST)
    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['depth_id']
    Equipment2.objects.filter(id=b).update(depth=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)


def depthA(request):
    form = EquipInfo(request.POST)
    a = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    d = request.POST['depth_id']
    Equipment.objects.filter(id=a).update(depth=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addnewequip2.html', context)



def load_depth2(request):
    a = Equipment.objects.all()
    b = EquipUpdate.objects.values_list('modelnum', flat=True).first()
    instance = Equipment.objects.get(id=b)
    form = EquipInfo(request.POST or None, instance=instance)
    depth = a.values('depth').get(id=b)
    context = {
        "instance": instance,
        "depth": depth,
        "form": form,
    }
    return render(request, 'mha/depth_2.html', context)


def modequip(request):
    form = EquipInfo(request.POST)

    context = {
        "form": form,
    }
    return render(request, 'mha/modequip.html', context)


def updateequip(request):
    form = UpdateEquipInfo(request.POST)
    a = EquipUpdate.objects.filter(id=1).update(type="", mfg="", eff="", mfgmodeldescrip="", modelnum="")

    context = {
        "form": form,
        "a": a,
    }
    return render(request, 'mha/updateequip.html', context)


def typeupdate(request):
    form = UpdateEquipInfo(request.POST)
    Filtertype.objects.all().delete()
    a = request.POST['id_type']
    a1 = EquipUpdate.objects.filter(id=1).update(type=a)
    b = Filtertype.objects.create(id=1, typefilter=a)
    c = ManFilter.objects.all().delete()
    aa = Filtertype.objects.values_list('typefilter', flat=True).first()
    d = Equipment2.objects.filter(type=aa).annotate(mfgG=F('mfg'))
    dd = list(d.values_list('mfg', flat=True))
    ee = list(set(dd))
    try:
        e = ManFilter.objects.create(manufacturer=ee[0])
    except Exception as ee:
        e = 0
    try:
        e1 = ManFilter.objects.create(manufacturer=ee[1])
    except Exception as ee:
        e1 = 0
    try:
        e2 = ManFilter.objects.create(manufacturer=ee[2])
    except Exception as ee:
        e2 = 0
    try:
        e3 = ManFilter.objects.create(manufacturer=ee[3])
    except Exception as ee:
        e3 = 0
    try:
        e4 = ManFilter.objects.create(manufacturer=ee[4])
    except Exception as ee:
        e4 = 0

    context = {
        "form": form,
        "a1": a1,
        "b": b,
        "c": c,
        "e": e,
        "e1": e1,
        "e2": e2,
        "e3": e3,
        "e4": e4,

    }
    return render(request, 'mha/updateequip.html', context)


def load_typeupdate(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    type = a.values('type_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "type": type,
        "form": form,
    }
    return render(request, 'mha/typeupdate_1.html', context)


def mfgupdate(request):
    form = UpdateEquipInfo(request.POST)
    Filtermfg.objects.all().delete()
    a = request.POST['id_mfg']
    a1 = EquipUpdate.objects.filter(id=1).update(mfg=a)
    b = Filtermfg.objects.create(id=1, mfgfilter=a)
    c = EffFilter.objects.all().delete()
    d = Filtertype.objects.values_list('typefilter', flat=True).first()
    dd = Filtermfg.objects.values_list('mfgfilter', flat=True).first()
    d1 = Equipment2.objects.filter(type=d, mfg=dd).annotate(effG=F('eff'))
    d2 = list(d1.values_list('eff', flat=True))
    ee = list(set(d2))
    try:
        e = EffFilter.objects.create(eff=ee[0])
    except Exception as ee:
        e = 0
    try:
        e1 = EffFilter.objects.create(eff=ee[1])
    except Exception as ee:
        e1 = 0
    try:
        e2 = EffFilter.objects.create(eff=ee[2])
    except Exception as ee:
        e2 = 0
    try:
        e3 = EffFilter.objects.create(eff=ee[3])
    except Exception as ee:
        e3 = 0
    try:
        e4 = EffFilter.objects.create(eff=ee[4])
    except Exception as ee:
        e4 = 0

    context = {
        "form": form,
        "a1": a1,
        "b": b,
        "c": c,
        "e": e,
        "e1": e1,
        "e2": e2,
        "e3": e3,
        "e4": e4,

    }
    return render(request, 'mha/updateequip.html', context)


def mfgupdateload(request):
    a = ManFilter.objects.all()
    form = UpdateEquipInfo(request.POST)
    mfg = a.values('manufacturer')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/mfg_1.html', context)


def modnumupdate(request):
    form = UpdateEquipInfo(request.POST)
    a = request.POST['id_modelnum']
    a1 = EquipUpdate.objects.filter(id=1).update(modelnum=a)
    context = {
        "form": form,
        "a1": a1,
    }
    return render(request, 'mha/updateequip.html', context)


def load_mfgupdate(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    mfg = a.values('mfg').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/mfgupdate_1.html', context)


def load_mfgupdate2(request):
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    mfg = ManFilter.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/mfgupdate_1.html', context)


def effupdate(request):
    form = UpdateEquipInfo(request.POST)
    Filtereff.objects.all().delete()
    a = request.POST['id_eff']
    a1 = EquipUpdate.objects.filter(id=1).update(eff=a)
    b = Filtereff.objects.create(id=1, efffilter=a)
    c = MfgmodeldescripFilter.objects.all().delete()
    d = Filtertype.objects.values_list('typefilter', flat=True).first()
    e = Filtermfg.objects.values_list('mfgfilter', flat=True).first()
    f = Filtereff.objects.values_list('efffilter', flat=True).first()
    f1 = Equipment2.objects.filter(type=d, mfg=e, eff=f).annotate(mfgmodeldescripG=F('mfgmodeldescrip'))
    f2 = list(f1.values_list('mfgmodeldescrip', flat=True))
    ee = list(set(f2))
    try:
        e1 = MfgmodeldescripFilter.objects.create(mfgmodeldescrip=ee[0])
    except Exception as ee:
        e1 = 0
    try:
        e2 = MfgmodeldescripFilter.objects.create(mfgmodeldescrip=ee[1])
    except Exception as ee:
        e2 = 0
    try:
        e3 = MfgmodeldescripFilter.objects.create(mfgmodeldescrip=ee[2])
    except Exception as ee:
        e3 = 0
    try:
        e4 = MfgmodeldescripFilter.objects.create(mfgmodeldescrip=ee[3])
    except Exception as ee:
        e4 = 0
    try:
        e5 = MfgmodeldescripFilter.objects.create(mfgmodeldescrip=ee[4])
    except Exception as ee:
        e5 = 0
    context = {
        "form": form,
        "a1": a1,
        "b": b,
        "c": c,
        "e": e,
        "e1": e1,
        "e2": e2,
        "e3": e3,
        "e4": e4,
        "e5": e5,
    }
    return render(request, 'mha/updateequip.html', context)


def effupdateload(request):
    a = EffFilter.objects.all()
    form = UpdateEquipInfo(request.POST)
    eff = a.values('eff')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "eff": eff,
        "form": form,
    }
    return render(request, 'mha/eff_1.html', context)


def load_efficiencyupdatefurn(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    efficiency = a.values('efficiencyfurn_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "efficiency": efficiency,
        "form": form,
    }
    return render(request, 'mha/efficiencyupdatefurn_1.html', context)


def load_efficiencyupdatefurn2(request):
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    efficiencyfurn = EffFilter.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "efficiencyfurn": efficiencyfurn,
        "form": form,
    }
    return render(request, 'mha/efficiencyupdatefurn_1.html', context)


def load_efficiencyupdatecond2(request):
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    efficiencycond = EffFilter.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "efficiencycond": efficiencycond,
        "form": form,
    }
    return render(request, 'mha/efficiencyupdatecond_1.html', context)


def mfgmodeldescripload(request):
    a = MfgmodeldescripFilter.objects.all()
    form = UpdateEquipInfo(request.POST)
    mfgmodeldescrip = a.values('mfgmodeldescrip')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "mfgmodeldescrip": mfgmodeldescrip,
        "form": form,
    }
    return render(request, 'mha/mfgmodeldescrip_1.html', context)


def modeldescripupdate(request):
    form = UpdateEquipInfo(request.POST)
    FilterMfgmodeldescrip.objects.all().delete()
    a = request.POST['id_mfgmodeldescrip']
    a1 = EquipUpdate.objects.filter(id=1).update(mfgmodeldescrip=a)
    b = FilterMfgmodeldescrip.objects.create(id=1, Mfgmodeldescripfilter=a)

    context = {
        "form": form,
        "a1": a1,
        "b": b,
    }
    return render(request, 'mha/updateequip.html', context)


def load_modeldescripupdate(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    modeldescrip = a.values('mfgmodeldescripfurn_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "modeldescrip": modeldescrip,
        "form": form,
    }
    return render(request, 'mha/modeldescripupdate_1.html', context)


def load_modeldescripupdate2(request):
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    mfgmodeldescripfurn = FilterMfgmodeldescrip.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "mfgmodeldescripfurn": mfgmodeldescripfurn,
        "form": form,
    }
    return render(request, 'mha/modeldescripupdate_1.html', context)


def efficiencyupdatecond(request):
    form = UpdateEquipInfo(request.POST)
    a = request.POST['id_efficiencycond']
    b = EquipUpdate.objects.filter(id=1).update(efficiencycond_id=a)
    c = FilterMfgmodeldescrip.objects.all().delete()
    d = EquipUpdate.objects.values_list('type', flat=True).first()
    e = EquipUpdate.objects.values_list('mfg_id', flat=True).first()
    f1 = Equipment.objects.filter(type_id=d, mfg_id=e, effcond=a).annotate(
        mfgmodeldescripcondG=F('mfgmodeldescripcond'))
    f2 = list(f1.values_list('mfgmodeldescripcond', flat=True))
    ee = list(set(f2))
    try:
        e = Mfgmodeldescripcond.objects.values_list('id', flat=True).get(id=ee[0])
        f = Mfgmodeldescripcond.objects.values_list('condmfgmodeldescrip', flat=True).get(id=ee[0])
        g = FilterMfgmodeldescrip.objects.create(id=e, Mfgmodeldescripfilter=f)
    except Exception as ee:
        e = 0
        g = 0

    try:
        e1 = Mfgmodeldescripcond.objects.values_list('id', flat=True).get(id=ee[1])
        f1 = Mfgmodeldescripcond.objects.values_list('condmfgmodeldescrip', flat=True).get(id=ee[1])
        g1 = FilterMfgmodeldescrip.objects.create(id=e1, Mfgmodeldescripfilter=f1)
    except Exception as ee:
        e1 = 0
        g1 = 0

    try:
        e2 = Mfgmodeldescripcond.objects.values_list('id', flat=True).get(id=ee[2])
        f2 = Mfgmodeldescripcond.objects.values_list('condmfgmodeldescrip', flat=True).get(id=ee[2])
        g2 = FilterMfgmodeldescrip.objects.create(id=e2, Mfgmodeldescripfilter=f2)
    except Exception as ee:
        e2 = 0
        g2 = 0

    try:
        e3 = Mfgmodeldescripcond.objects.values_list('id', flat=True).get(id=ee[3])
        f3 = Mfgmodeldescripcond.objects.values_list('condmfgmodeldescrip', flat=True).get(id=ee[3])
        g3 = FilterMfgmodeldescrip.objects.create(id=e3, Mfgmodeldescripfilter=f3)
    except Exception as ee:
        e3 = 0
        g3 = 0

    try:
        e4 = Mfgmodeldescripcond.objects.values_list('id', flat=True).get(id=ee[4])
        f4 = Mfgmodeldescripcond.objects.values_list('condmfgmodeldescrip', flat=True).get(id=ee[4])
        g4 = FilterMfgmodeldescrip.objects.create(id=e4, Mfgmodeldescripfilter=f4)
    except Exception as ee:
        e4 = 0
        g4 = 0
    context = {
        "form": form,
        "b": b,
        "c": c,
        "e": e,
        "g": g,
        "e1": e1,
        "g1": g1,
        "e2": e2,
        "g2": g2,
        "e3": e3,
        "g3": g3,
        "e4": e4,
        "g4": g4,
    }
    return render(request, 'mha/updateequip.html', context)


def load_efficiencyupdatecond(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    efficiency = a.values('efficiencycond_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "efficiency": efficiency,
        "form": form,
    }
    return render(request, 'mha/efficiencyupdatecond_1.html', context)


def modeldescripupdatecond(request):
    form = UpdateEquipInfo(request.POST)
    a = request.POST['id_mfgmodeldescripcond']
    b = EquipUpdate.objects.filter(id=1).update(mfgmodeldescripcond_id=a)
    context = {
        "form": form,
        "b": b,
    }
    return render(request, 'mha/updateequip.html', context)


def load_modeldescripupdatecond(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    modeldescrip = a.values('mfgmodeldescripcond_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "modeldescrip": modeldescrip,
        "form": form,
    }
    return render(request, 'mha/modeldescripupdatecond_1.html', context)


def load_modeldescripupdatecond2(request):
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    mfgmodeldescripcond = FilterMfgmodeldescrip.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "mfgmodeldescripcond": mfgmodeldescripcond,
        "form": form,
    }
    return render(request, 'mha/modeldescripupdatecond_1.html', context)


def configupdate(request):
    form = UpdateEquipInfo(request.POST)
    a = request.POST['id_config']
    b = EquipUpdate.objects.filter(id=1).update(config_id=a)
    context = {
        "form": form,
        "b": b,
    }
    return render(request, 'mha/updateequip.html', context)


def load_configupdate(request):
    a = EquipUpdate.objects.all()
    instance = EquipUpdate.objects.get(id=1)
    form = UpdateEquipInfo(request.POST or None, instance=instance)
    config = a.values('config_id').get(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "config": config,
        "form": form,
    }
    return render(request, 'mha/configupdate_1.html', context)


def update1(request):
    a = Filtertype.objects.values_list('typefilter', flat=True).first()
    queryset = Equipment2.objects.filter(type=a)
    b = EquipUpdate.objects.filter(id=1).update(update=1)
    queryset2 = EquipUpdate.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))

    paginator = Paginator(queryset, 16)  # Show 16 contacts per page
    page_number = request.GET.get('page')
    try:
        queryset = paginator.get_page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"object_list": queryset,
               "object_list2": queryset2,
               "search_term": search_term,
               "b": b,
               }
    return render(request, 'mha/update1.html', context)


def update2(request):
    a = Filtertype.objects.values_list('typefilter', flat=True).first()
    b = Filtermfg.objects.values_list('mfgfilter', flat=True).first()
    queryset = Equipment2.objects.all().filter(type=a, mfg=b)
    b = EquipUpdate.objects.filter(id=1).update(update=2)
    queryset2 = EquipUpdate.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))

    paginator = Paginator(queryset, 16)  # Show 16 contacts per page
    page_number = request.GET.get('page')
    try:
        queryset = paginator.get_page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"object_list": queryset,
               "search_term": search_term,
               "object_list2": queryset2,
               "b": b,
               }
    return render(request, 'mha/update1.html', context)


def update3(request):
    a = Filtertype.objects.values_list('typefilter', flat=True).first()
    b = Filtermfg.objects.values_list('mfgfilter', flat=True).first()
    c = Filtereff.objects.values_list('efffilter', flat=True).first()
    queryset = Equipment2.objects.all().filter(type=a, mfg=b, eff=c)
    b = EquipUpdate.objects.filter(id=1).update(update=3)
    queryset2 = EquipUpdate.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))

    paginator = Paginator(queryset, 16)  # Show 16 contacts per page
    page_number = request.GET.get('page')
    try:
        queryset = paginator.get_page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"object_list": queryset,
               "search_term": search_term,
               "object_list2": queryset2,
               "b": b,

               }
    return render(request, 'mha/update1.html', context)


def update4(request):
    a = Filtertype.objects.values_list('typefilter', flat=True).first()
    b = Filtermfg.objects.values_list('mfgfilter', flat=True).first()
    c = Filtereff.objects.values_list('efffilter', flat=True).first()
    d = FilterMfgmodeldescrip.objects.values_list('Mfgmodeldescripfilter', flat=True).first()
    queryset = Equipment2.objects.all().filter(type=a, mfg=b, eff=c, mfgmodeldescrip=d)
    b = EquipUpdate.objects.filter(id=1).update(update=4)
    queryset2 = EquipUpdate.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))

    paginator = Paginator(queryset, 16)  # Show 16 contacts per page
    page_number = request.GET.get('page')
    try:
        queryset = paginator.get_page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"object_list": queryset,
               "search_term": search_term,
               "object_list2": queryset2,
               "b": b,
               }
    return render(request, 'mha/update1.html', context)


def filtermodelnum(request):
    Filtermodelnum.objects.filter(id=1).delete()
    form = EquipInfo(request.POST)
#    b = Equipment2.objects.values_list('id', flat=True).last()
    d = request.POST['modelnum_id']
    Filtermodelnum.objects.create(id=1, modelnumfilter=d)
    context = {
        "form": form,

    }
    return render(request, 'mha/update1.html', context)





def update5(request):
    a = Filtermodelnum.objects.values_list('modelnumfilter', flat=True).first()
    queryset = Equipment2.objects.all().filter(modelnum=a)
    b = EquipUpdate.objects.filter(id=1).update(update=5)
    queryset2 = EquipUpdate.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))

    paginator = Paginator(queryset, 16)  # Show 16 contacts per page
    page_number = request.GET.get('page')
    try:
        queryset = paginator.get_page(page_number)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {"object_list": queryset,
               "search_term": search_term,
               "object_list2": queryset2,
               "b": b,
               }
    return render(request, 'mha/update1.html', context)


def editquip(request, id=None):
    instance = get_object_or_404(Equipment2, id=id)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    #    b = Equipment2.objects.values_list('modelnum', flat=True).get(modelnum=modelnum)
    #    c = EquipUpdate.objects.update(modelnum=b)
    #    if form.is_valid():
    #        instance = form.save(commit=False)
    #        instance.save()
    #        return redirect(instance.get_absolute4_url())
    context = {
        "instance": instance,
        "form": form,
        #       "c": c,
    }
    return render(request, 'mha/editquip.html', context)


def editquip2(request, modelnum=None):
    instance = get_object_or_404(Equipment2, modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    #    b = Equipment2.objects.values_list('modelnum', flat=True).get(modelnum=modelnum)
    #    c = EquipUpdate.objects.update(modelnum=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('mha/updateequip.html')
    context = {
        "instance": instance,
        "form": form,
        #       "c": c,
    }
    return render(request, 'mha/editquip2.html', context)


def editfurnequip(request, modelnum=None):
    instance = Equipment.objects.get(modelnum=modelnum)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    b = Equipment.objects.values_list('id', flat=True).get(modelnum=modelnum)
    c = EquipUpdate.objects.update(modelnum=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute4_url())
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/editfurnequip.html', context)


def deleteeditequip(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    Equipment.objects.filter(id=instance).delete()
    context = {
        "form": form,

    }
    return render(request, 'mha/openequip.html', context)


def costedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    d = request.POST['cost_id']
    #    Equipment.objects.filter(modelnum=modelnum).update(cost=d)
    Equipment2.objects.filter(id=id).update(cost=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)


def heightedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    d = request.POST['height_id']
    #    Equipment.objects.filter(modelnum=modelnum).update(cost=d)
    Equipment2.objects.filter(id=id).update(height=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)


def widthedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    d = request.POST['width_id']
    #    Equipment.objects.filter(modelnum=modelnum).update(cost=d)
    Equipment2.objects.filter(id=id).update(width=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)


def depthedit(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    d = request.POST['depth_id']
    #    Equipment.objects.filter(modelnum=modelnum).update(cost=d)
    Equipment2.objects.filter(id=id).update(depth=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)


def smarttherm(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfoEdit(request.POST or None, instance=instance)
    d = request.POST['id_smart']
#    e = SmartThermostat.objects.filter(id=id).values_list('smart', flat=True)
    Equipment2.objects.filter(id=id).update(smart=d)
    context = {
        "d": d,
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editquip.html', context)



def deleteediteequip(request, id=None):
    instance = Equipment2.objects.get(id=id)
    form = EquipInfo2(request.POST or None, instance=instance)
    a = Equipment2.objects.all()
    a.filter(id=id).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute6_url(), context)


def furnglobalincrease1(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease1.html', {'percentages': formatted_percentages})


def globalincrease1(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease1.html', {'percentages': formatted_percentages})


def globalincrease2(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease2.html', {'percentages': formatted_percentages})


def globalincrease3(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease3.html', {'percentages': formatted_percentages})


def globalincrease4(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease4.html', {'percentages': formatted_percentages})


def globalincrease5(request):
    percentages = GlobalIncrease.objects.all()
    formatted_percentages = [{'id': p.id, 'value': f'{p.increaseglobal * 100:.0f}%'} for p in percentages]

    return render(request, 'mha/globalincrease5.html', {'percentages': formatted_percentages})


def updateprice1(request):
    a = EquipUpdate.objects.values_list('type', flat=True).first()
    bb = Equipment2.objects.filter(type=a).update(increasecost=F('cost') * F('increasepercent'))
    cc = Equipment2.objects.filter(type=a).update(total_cost_value=F('cost') + F('increasecost'))
    dd = Equipment2.objects.filter(type=a).update(cost=F('total_cost_value'))
    ee = Equipment2.objects.filter(type=a).update(increasepercent=0.00, increasecost=0.00, total_cost_value=0.00)
    form = EquipInfo2(request.POST)
    queryset = Equipment2.objects.all().filter(type=a)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "bb": bb,
               "cc": cc,
               "dd": dd,
               "ee": ee,

               }
    return render(request, 'mha/update1.html', context)


def updateprice2(request):
    a = EquipUpdate.objects.values_list('type', flat=True).first()
    a2 = EquipUpdate.objects.values_list('mfg', flat=True).first()
    b = Equipment2.objects.filter(type=a, mfg=a2).update(increasecost=F('cost') * F('increasepercent'))
    c = Equipment2.objects.filter(type=a, mfg=a2).update(total_cost_value=F('cost') + F('increasecost'))
    d = Equipment2.objects.filter(type=a, mfg=a2).update(cost=F('total_cost_value'))
    e = Equipment2.objects.filter(type=a, mfg=a2).update(increasepercent=0.00, increasecost=0.00, total_cost_value=0.00)
    form = EquipInfo(request.POST)
    queryset = Equipment2.objects.all().filter(type=a, mfg=a2)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "b": b,
               "c": c,
               "d": d,
               "e": e,
               }
    return render(request, 'mha/equiptoupdate2.html', context)


def updateprice3(request):
    a = EquipUpdate.objects.values_list('type', flat=True).first()
    a2 = EquipUpdate.objects.values_list('mfg', flat=True).first()
    a3 = EquipUpdate.objects.values_list('eff', flat=True).first()
    b = Equipment2.objects.filter(type=a, mfg=a2, eff=a3).update(increasecost=F('cost') * F('increasepercent'))
    c = Equipment2.objects.filter(type=a, mfg=a2, eff=a3).update(total_cost_value=F('cost') + F('increasecost'))
    d = Equipment2.objects.filter(type=a, mfg=a2, eff=a3).update(cost=F('total_cost_value'))
    e = Equipment2.objects.filter(type=a, mfg=a2, eff=a3).update(increasepercent=0.00, increasecost=0.00,
                                                                 total_cost_value=0.00)
    form = EquipInfo(request.POST)
    queryset = Equipment2.objects.all().filter(type=a, mfg=a2, eff=a3)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "b": b,
               "c": c,
               "d": d,
               "e": e,
               }
    return render(request, 'mha/equiptoupdate3.html', context)


def updateprice4(request):
    a = EquipUpdate.objects.values_list('type', flat=True).first()
    a2 = EquipUpdate.objects.values_list('mfg', flat=True).first()
    a3 = EquipUpdate.objects.values_list('eff', flat=True).first()
    a4 = EquipUpdate.objects.values_list('mfgmodeldescrip', flat=True).first()
    b = Equipment2.objects.filter(type=a, mfg=a2, eff=a3, mfgmodeldescrip=a4).update(
        increasecost=F('cost') * F('increasepercent'))
    c = Equipment2.objects.filter(type=a, mfg=a2, eff=a3, mfgmodeldescrip=a4).update(
        total_cost_value=F('cost') + F('increasecost'))
    d = Equipment2.objects.filter(type=a, mfg=a2, eff=a3, mfgmodeldescrip=a4).update(cost=F('total_cost_value'))
    e = Equipment2.objects.filter(type=a, mfg=a2, eff=a3, mfgmodeldescrip=a4).update(increasepercent=0.00,
                                                                                     increasecost=0.00,
                                                                                     total_cost_value=0.00)
    form = EquipInfo(request.POST)
    queryset = Equipment2.objects.all().filter(type=a, mfg=a2, eff=a3, mfgmodeldescrip=a4)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "b": b,
               "c": c,
               "d": d,
               "e": e,
               }
    return render(request, 'mha/equiptoupdate4.html', context)


def updateprice5(request):
    a = EquipUpdate.objects.values_list('type', flat=True).first()
    a2 = EquipUpdate.objects.values_list('mfg', flat=True).first()
    a3 = EquipUpdate.objects.values_list('eff', flat=True).first()
    a4 = EquipUpdate.objects.values_list('mfgmodeldescrip', flat=True).first()
    a5 = EquipUpdate.objects.values_list('config', flat=True).first()
    b = Equipment2.objects.filter(type=a, mfg=a2, efficienc=a3, mfgmodeldescrip=a4, config=a5).update(
        increasecost=F('cost') * F('increasepercent'))
    c = Equipment2.objects.filter(type=a, mfg=a2, efficiency=a3, mfgmodeldescrip=a4, config=a5).update(
        total_cost_value=F('cost') + F('increasecost'))
    d = Equipment2.objects.filter(type=a, mfg=a2, efficiency=a3, mfgmodeldescrip=a4, config=a5).update(
        cost=F('total_cost_value'))
    e = Equipment2.objects.filter(type=a, mfg=a2, efficiency=a3, mfgmodeldescrip=a4, config=a5).update(
        increasepercent=0.00, increasecost=0.00, total_cost_value=0.00)
    form = EquipInfo(request.POST)
    queryset = Equipment2.objects.all().filter(type=a, mfg=a2, efficiency=a3, mfgmodeldescrip=a4,
                                              config=a5)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(modelnum__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(type__icontains=search_term)
                                   | Q(config__icontains=search_term)
                                   | Q(mfgmodeldescrip__icontains=search_term)
                                   | Q(motortype__icontains=search_term)
                                   | Q(eff__icontains=search_term)
                                   | Q(btu__icontains=search_term)
                                   | Q(cost__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "b": b,
               "c": c,
               "d": d,
               "e": e,
               }
    return render(request, 'mha/equiptoupdate5.html', context)


def percentincrease1(request):
    form = IncreaseGlobal(request.POST)
    a = request.POST['id_percentage']
    b = GlobalIncrease.objects.values_list('increaseglobal', flat=True).filter(id=a)
    c = EquipUpdate.objects.values_list('type', flat=True).first()
    e = Equipment2.objects.filter(type=c).update(increasepercent=b)
    context = {
        "form": form,
        "e": e,
    }
    return render(request, 'mha/globalincrease1.html', context)


def percentincrease2(request):
    form = IncreaseGlobal(request.POST)
    a = request.POST['id_percentage']
    b = GlobalIncrease.objects.values_list('increaseglobal', flat=True).filter(id=a)
    c = EquipUpdate.objects.values_list('type', flat=True).first()
    e = EquipUpdate.objects.values_list('mfg', flat=True).first()
    d = Equipment2.objects.filter(type=c, mfg=e).update(increasepercent=b)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/globalincrease2.html', context)


def percentincrease3(request):
    form = IncreaseGlobal(request.POST)
    a = request.POST['id_percentage']
    b = GlobalIncrease.objects.values_list('increaseglobal', flat=True).filter(id=a)
    c = EquipUpdate.objects.values_list('type', flat=True).first()
    e = EquipUpdate.objects.values_list('mfg', flat=True).first()
    f = EquipUpdate.objects.values_list('eff', flat=True).first()
    d = Equipment2.objects.filter(type=c, mfg=e, eff=f).update(increasepercent=b)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/globalincrease3.html', context)


def percentincrease4(request):
    form = IncreaseGlobal(request.POST)
    a = request.POST['id_percentage']
    b = GlobalIncrease.objects.values_list('increaseglobal', flat=True).filter(id=a)
    c = EquipUpdate.objects.values_list('type', flat=True).first()
    e = EquipUpdate.objects.values_list('mfg', flat=True).first()
    f = EquipUpdate.objects.values_list('eff', flat=True).first()
    g = EquipUpdate.objects.values_list('mfgmodeldescrip', flat=True).first()
    d = Equipment2.objects.filter(type=c, mfg=e, eff=f, mfgmodeldescrip=g).update(increasepercent=b)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/globalincrease4.html', context)


def percentincrease5(request):
    form = IncreaseGlobal(request.POST)
    a = request.POST['id_percentage']
    b = GlobalIncrease.objects.values_list('increaseglobal', flat=True).filter(id=a)
    c = EquipUpdate.objects.values_list('type_id', flat=True).first()
    e = EquipUpdate.objects.values_list('mfg_id', flat=True).first()
    f = EquipUpdate.objects.values_list('efficiency_id', flat=True).first()
    g = EquipUpdate.objects.values_list('mfgmodeldescrip_id', flat=True).first()
    h = EquipUpdate.objects.values_list('config_id', flat=True).first()
    d = Equipment.objects.filter(type=c, mfg_id=e, efficiency_id=f, mfgmodeldescrip_id=g, config_id=h).update(
        increasepercent=b)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/globalincrease5.html', context)


def mattoupdate(request):
    form = InstallMaterial(request.POST)
    queryset = Material.objects.all().exclude(id=1)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(descrip__icontains=search_term)
                                   | Q(cost__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(vendor__icontains=search_term)
                                   | Q(vendornum__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               }
    return render(request, 'mha/mattoupdate.html', context)


def addnewmat(request):
    form = InstallMaterial(request.POST)
    a = Material.objects.values_list('id', flat=True).last()
    b = 1
    c = a + b
    d = Material.objects.create(id=c, idA=c)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/addnewmat.html', context)


def adddescrip(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_descrip']
    b = Material.objects.values_list('id', flat=True).last()
    c = Material.objects.filter(id=b).update(descrip=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/addnewmat.html', context)


def addcost(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_cost']
    b = Material.objects.values_list('id', flat=True).last()
    c = Material.objects.filter(id=b).update(cost=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/addnewmat.html', context)


def addmatmfg(request):
    form = InstallMaterial(request.POST or None)
    a = Material.objects.values_list('id', flat=True).last()
    b = request.POST['id_matmfg']
    c = Material.objects.filter(id=a).update(matmfg_id=b)
    context = {
        "form": form,
        "c": c,
        "b": b,
    }
    return render(request, 'mha/addnewmat.html', context)


def matmfg2(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_matmfg2']
    b = Manufacturer.objects.create(mfg=a)
    c = Manufacturer.objects.values_list('id', flat=True).last()
    d = Material.objects.values_list('id', flat=True).last()
    e = Material.objects.filter(id=d).update(matmfg_id=c)

    context = {
        "form": form,
        "b": b,
        "e": e,
    }
    return render(request, 'mha/addnewequip.html', context)


def load_matmfg2(request):
    a = Material.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Material.objects.get(id=b)
    form = InstallMaterial(request.POST or None, instance=instance)
    matmfg = a.values('matmfg_id').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "instance": instance,
        "matmfg": matmfg,
        "form": form,
    }
    return render(request, 'mha/matmfg_1.html', context)


def matvendor(request):
    form = InstallMaterial(request.POST)
    a = Material.objects.values_list('id', flat=True).last()
    b = request.POST['id_vendor']
    c = Material.objects.filter(id=a).update(vendor_id=b)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/addnewmat.html', context)


def matvendor2(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_vendor2']
    b = Vendor.objects.create(vnr=a)
    c = Vendor.objects.values_list('id', flat=True).last()
    d = Material.objects.values_list('id', flat=True).last()
    e = Material.objects.filter(id=d).update(vendor_id=c)

    context = {
        "form": form,
        "b": b,
        "e": e,
    }
    return render(request, 'mha/addnewequip.html', context)


def load_matvendor2(request):
    a = Material.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Material.objects.get(id=b)
    form = InstallMaterial(request.POST or None, instance=instance)
    matvendor = a.values('vendor_id').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute10_url())
    context = {
        "instance": instance,
        "matvendor": matvendor,
        "form": form,
    }
    return render(request, 'mha/matvendor_1.html', context)


def vendornum(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_vendornum']
    b = Material.objects.values_list('id', flat=True).last()
    c = Material.objects.filter(id=b).update(vendornum=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/addnewmat.html', context)


def mattype(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_materialtype']
    b = Material.objects.values_list('id', flat=True).last()
    c = Material.objects.filter(id=b).update(materialtype_id=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/addnewmat.html', context)


def mattype2(request):
    form = InstallMaterial(request.POST)
    a = request.POST['id_materialtype2']
    b = MaterialType.objects.create(type=a)
    c = MaterialType.objects.values_list('id', flat=True).last()
    d = Material.objects.values_list('id', flat=True).last()
    e = Material.objects.filter(id=d).update(materialtype_id=c)

    context = {
        "form": form,
        "b": b,
        "e": e,
    }
    return render(request, 'mha/addnewequip.html', context)


def load_mattype2(request):
    a = Material.objects.all()
    b = a.values_list('id', flat=True).last()
    instance = Material.objects.get(id=b)
    form = InstallMaterial(request.POST or None, instance=instance)
    mattype = a.values('materialtype_id').get(id=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute10_url())
    context = {
        "instance": instance,
        "mattype": mattype,
        "form": form,
    }
    return render(request, 'mha/mattype_1.html', context)


def deletemat(request):
    form = InstallMaterial(request.POST)
    b = Material.objects.values_list('id', flat=True).last()
    c = Material.objects.filter(id=b).delete()
    queryset = Material.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(descrip__icontains=search_term)
                                   | Q(cost__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(vendor__icontains=search_term)
                                   | Q(vendornum__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               "c": c,
               }
    return render(request, 'mha/mattoupdate.html', context)


def deletemat1(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute11_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/deletemat1.html', context)


def matsearch(request):
    form = MaterialSearch(request.POST)
    context = {
        "form": form,
    }
    return render(request, 'mha/matsearch.html', context)


def mfgsearch(request):
    form = MaterialSearch(request.POST)
    a = request.POST['id_matmfg']
    c = MatUpdate.objects.filter(id=1).update(mfg=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/matsearch.html', context)


def vendorsearch(request):
    form = MaterialSearch(request.POST)
    a = request.POST['id_vendor']
    c = MatUpdate.objects.filter(id=1).update(vendor=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/matsearch.html', context)


def typesearch(request):
    form = MaterialSearch(request.POST)
    a = request.POST['id_materialtype']
    c = MatUpdate.objects.filter(id=1).update(materialtype=a)
    context = {
        "form": form,
        "c": c,
    }
    return render(request, 'mha/matsearch.html', context)


def filtermfg(request):
    a = MatUpdate.objects.values_list('mfg', flat=True).first()
    form = InstallMaterial(request.POST)
    queryset = Material.objects.filter(matmfg=a).exclude(id=1)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(descrip__icontains=search_term)
                                   | Q(cost__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(vendor__icontains=search_term)
                                   | Q(vendornum__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               }
    return render(request, 'mha/mattoupdate.html', context)


def filtervendor(request):
    a = MatUpdate.objects.values_list('vendor', flat=True).first()
    form = InstallMaterial(request.POST)
    queryset = Material.objects.filter(vendor_id=a).exclude(id=1)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(descrip__icontains=search_term)
                                   | Q(cost__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(vendor__icontains=search_term)
                                   | Q(vendornum__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               }
    return render(request, 'mha/mattoupdate.html', context)


def filtertype(request):
    a = MatUpdate.objects.values_list('materialtype', flat=True).first()
    form = InstallMaterial(request.POST)
    queryset = Material.objects.filter(materialtype_id=a).exclude(id=1)
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(descrip__icontains=search_term)
                                   | Q(cost__icontains=search_term)
                                   | Q(mfg__icontains=search_term)
                                   | Q(vendor__icontains=search_term)
                                   | Q(vendornum__icontains=search_term))
    #    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    #    page = request.GET.get('page')
    #    queryset = paginator.get_page(page)
    context = {"object_list": queryset,
               "search_term": search_term,
               "form": form,
               }
    return render(request, 'mha/mattoupdate.html', context)


def editmat(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute12_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/editmat.html', context)


def costmat(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = request.POST['cost_id']
    Material.objects.filter(idA=idA).update(cost=a)
    context = {
        "form": form,
    }
    return render(request, 'mha/matcostload_1.html', context)


def matcostload(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = Material.objects.all()
    cost = a.values('cost').get(idA=idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute12_url())
    context = {
        "instance": instance,
        "cost": cost,
        "form": form,
    }
    return render(request, 'mha/matcostload_1.html', context)


def mfgmat(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = request.POST['id_matmfg']
    Material.objects.filter(idA=idA).update(matmfg_id=a)
    context = {
        "form": form,
    }
    return render(request, 'mha/matmfgload_1.html', context)


def matmfgload(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = Material.objects.all()
    mfg = a.values('matmfg_id').get(idA=idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute12_url())
    context = {
        "instance": instance,
        "mfg": mfg,
        "form": form,
    }
    return render(request, 'mha/matmfgload_1.html', context)


def mfgvendor(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = request.POST['id_vendor']
    Material.objects.filter(idA=idA).update(vendor_id=a)
    context = {
        "form": form,
    }
    return render(request, 'mha/matvendorload_1.html', context)


def matvendorload(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = Material.objects.all()
    vendor = a.values('vendor_id').get(idA=idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute12_url())
    context = {
        "instance": instance,
        "vendor": vendor,
        "form": form,
    }
    return render(request, 'mha/matvendorload_1.html', context)


def mfgvennum(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = request.POST['vendornum_id']
    Material.objects.filter(idA=idA).update(vendornum=a)
    context = {
        "form": form,
    }
    return render(request, 'mha/matvennumload_1.html', context)


def matvennumload(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = Material.objects.all()
    vennum = a.values('vendornum').get(idA=idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute12_url())
    context = {
        "instance": instance,
        "vennum": vennum,
        "form": form,
    }
    return render(request, 'mha/matvennumload_1.html', context)


def mfgtype(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = request.POST['id_materialtype']
    Material.objects.filter(idA=idA).update(materialtype_id=a)
    context = {
        "form": form,
    }
    return render(request, 'mha/mattypeload_1.html', context)


def mattypeload(request, idA=None):
    instance = Material.objects.get(idA=idA)
    form = InstallMaterial(request.POST or None, instance=instance)
    a = Material.objects.all()
    mattype = a.values('materialtype_id').get(idA=idA)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute12_url())
    context = {
        "instance": instance,
        "mattype": mattype,
        "form": form,
    }
    return render(request, 'mha/mattypeload_1.html', context)


def customer(request):
    return render(request, 'mha/customer.html')



def deletecon(request, id=None):
    instance = get_object_or_404(ContractorInfo, conid=id)
    form = Coninfo(request.POST or None, instance=instance)
    Bidding.objects.filter(conid=id).delete()
    Contract.objects.filter(conid=id).delete()
    CurrentJobInfo.objects.filter(conid=id).delete()
    CustomerInfo.objects.filter(conid=id).delete()
    Custpagelocation.objects.filter(conid=id).delete()
    EquipmentCost.objects.filter(conid=id).delete()
    EquipSelection.objects.filter(conid=id).delete()
    JobCost.objects.filter(conid=id).delete()
    laborCost.objects.filter(conid=id).delete()
    MatCost.objects.filter(conid=id).delete()
    OSRCost.objects.filter(conid=id).delete()
    SelectedEquip.objects.filter(conid=id).delete()
    TotalJobCost.objects.filter(conid=id).delete()
    TargetProfit.objects.filter(conid=id).delete()
    ContractorInfo.objects.filter(conid=id).delete()
    context = {
        "form": form,
    }
    return redirect(instance.get_absolute5_url(), context)
#    return render(request, 'mha/customer.html', context)



def deletecust(request, id=None):
    instance = get_object_or_404(CustomerInfo, custid=id)
    form = Custinfo(request.POST or None, instance=instance)
    Bidding.objects.filter(custid=id).delete()
    Contract.objects.filter(custid=id).delete()
    CurrentJobInfo.objects.filter(custid=id).delete()
    Custpagelocation.objects.filter(custid=id).delete()
    EquipmentCost.objects.filter(custid=id).delete()
    EquipSelection.objects.filter(custid=id).delete()
    JobCost.objects.filter(custid=id).delete()
    laborCost.objects.filter(custid=id).delete()
    MatCost.objects.filter(custid=id).delete()
    OSRCost.objects.filter(custid=id).delete()
    SelectedEquip.objects.filter(custid=id).delete()
    TotalJobCost.objects.filter(custid=id).delete()
    TargetProfit.objects.filter(custid=id).delete()
    CustomerInfo.objects.filter(custid=id).delete()
    context = {
        "form": form,
    }
    return redirect(instance.get_absolute5_url(), context)
#    return render(request, 'mha/customer.html', context)



def addnewcust(request, id=None):
    instance = ContractorInfo.objects.get(id=id)
    form = Coninfo(request.POST or None, instance=instance)
    instance = form.save(commit=False)
    instance.save()
    a = ContractorInfo.objects.all()
    b = CustomerInfo.objects.all()
    instance2 = ContractorInfo.objects.values_list('id', flat=True).get(id=id)
    c = CustomerInfo.objects.create(conid=instance2)
    instance6 = CustomerInfo.objects.order_by('id').last()
    d = b.values_list('id', flat=True).last()
    CustomerInfo.objects.filter(id=d).update(custid=d)
    b = CustomerInfo.objects.filter(id=id).update(custid=instance2)
    context2 = {
        "instance2": instance2,
        "instance6": instance6,
        "a": a,
        "b": b,
        "c": c,
        "d": d,
    }

    return redirect(instance6.get_absolute7_url(), context2)


def newcon(request):
    if request.method == 'POST':
        form = ConinfoB(request.POST)
        if form.is_valid():
            form.save()
            a = ContractorInfo.objects.all()
            #            d = CustomerInfo.objects.all()
            instance2 = ContractorInfo.objects.order_by('id').last()
            b = a.values_list('id', flat=True).last()
            #            c = CustomerInfo.objects.create(conid=b)
            #            instance6 = CustomerInfo.objects.order_by('id').last()
            #            e = d.values_list('id', flat=True).last()
            ContractorInfo.objects.filter(id=b).update(conid=b)
            #            CustomerInfo.objects.filter(id=e).update(custid=e)
            context2 = {
                "instance2": instance2,
                #                "instance6": instance6,
                #                "a": a,
                #                "b": b,
                #                "c": c,

                #                "e": e,
            }
            return redirect(instance2.get_absolute2_url(), context2)
        else:
            form = ConinfoB()
            return render(request, 'mha/conerror.html', {'form': form})
    else:
        form = ConinfoB()
        return render(request, 'mha/newcon.html', {'form': form})


def conerror(request):
    return render(request, 'mha/conerror.html')


def custerror(request):
    return render(request, 'mha/custerror.html')


def dupconinfo(request, id=None):
    instance = CustomerInfo.objects.filter(id=id).last()
    form = DupConInfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute6_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/dupconinfo.html', context)


def newcust(request, id=None):
    if request.method == 'POST':
        instance = CustomerInfo.objects.filter(id=id).last()
        form = CustinfoB(request.POST or None, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            instance2 = CustomerInfo.objects.order_by('id').last()
            context2 = {
                "instance": instance,
                "instance2": instance2,
                "form": form,

            }
            return redirect(instance2.get_absolute12_url(), context2)
        else:
            instance = CustomerInfo.objects.filter(id=id).last()
            form = CustinfoB(request.POST or None, instance=instance)
            context = {
                'form': form,
                #                'instance2': instance2,
            }
            return render(request, 'mha/custerror.html', context)

    else:
        instance = CustomerInfo.objects.filter(id=id).last()
        form = CustinfoB(request.POST or None, instance=instance)
        context = {
            'form': form,
        }
        return render(request, 'mha/newcust.html', context)


def yesdupcon(request, custid=None):
    instance = get_object_or_404(CustomerInfo, custid=custid)
    form = DupConInfo(request.POST or None, instance=instance)
    a = ContractorInfo.objects.all()
    b = CustomerInfo.objects.order_by('conid').last()
    c = CustomerInfo.objects.values_list('conid', flat=True).last()
    d = a.values_list('concompanytname', flat=True).get(id=c)
    e = a.values_list('confirstname', flat=True).get(id=c)
    f = a.values_list('conlastname', flat=True).get(id=c)
    g = a.values_list('conadd1', flat=True).get(id=c)
    h = a.values_list('conadd2', flat=True).get(id=c)
    i = a.values_list('concity', flat=True).get(id=c)
    j = a.values_list('const', flat=True).get(id=c)
    k = a.values_list('conzipcode', flat=True).get(id=c)
    l = a.values_list('conwork1', flat=True).get(id=c)
    m = a.values_list('conwork2', flat=True).get(id=c)
    n = a.values_list('concell1', flat=True).get(id=c)
    o = a.values_list('concell2', flat=True).get(id=c)
    p = a.values_list('conhome', flat=True).get(id=c)
    q = a.values_list('conemail1', flat=True).get(id=c)
    r = a.values_list('conemail2', flat=True).get(id=c)
    t = CustomerInfo.objects.all()
    s = CustomerInfo.objects.filter(conid=c).update(custcompanytname=d, custfirstname=e, custlastname=f, custadd1=g,
                                                    custadd2=h, custcity=i, custst=j, custzipcode=k, custwork1=l,
                                                    custwork2=m, custcell1=n, custcell2=o, custhome=p, custemail1=q,
                                                    custemail2=r)
    u = CustomerInfo.objects.values_list('custid', flat=True).last()
    v = CustomerInfo.objects.values_list('conid', flat=True).last()

    s1 = Contract.objects.create(custid=u, conid=v)
    s2 = Bidding.objects.create(custid=u, conid=v)
    s3 = EquipSelection.objects.create(custid=u, conid=v)
    uu = Contract.objects.values_list('id', flat=True).last()
    vv = Bidding.objects.values_list('id', flat=True).last()
    ww = EquipSelection.objects.values_list('id', flat=True).last()
    xx = CurrentJobInfo.objects.values_list('id', flat=True).last() or 0
    aa = CurrentJobInfo.objects.filter(id=xx).delete()
    xx1 = xx + 1
    CurrentJobInfo.objects.create(id=xx1, custid=u, conid=v, bidid=vv, jobid=ww)
    s4 = Contract.objects.filter(id=uu).update(jobid=ww)
    s5 = EquipSelection.objects.filter(id=ww).update(jobid=ww)
    s6 = Bidding.objects.filter(id=vv).update(jobid=ww)

    instance2 = EquipSelection.objects.order_by('custid').last()

    context = {
        "aa": aa,
        "uu": uu,
        "b": b,
        "s": s,
        "t": t,
        'v': v,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "s4": s4,
        "s5": s5,
        "s6": s6,
        "instance": instance,
        "form": form,
    }
    return redirect(instance2.get_absolute16_url(), context)


def addnewproject(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    a = CustomerInfo.objects.values_list('custid', flat=True).last()
    b = CustomerInfo.objects.values_list('conid', flat=True).last()
    c = Bidding.objects.create(custid=a, conid=b)
    d  = Bidding.objects.values_list('id', flat=True).last()
    d1 = Bidding.objects.filter(id=d).update(bidid=d)
    e = Contract.objects.create(custid=a, conid=b, bidid=d)
    f = CurrentJobInfo.objects.create(custid=a, conid=b, bidid=d)
    g = Custpagelocation.objects.create(custid=a, conid=b, bidid=d)
    h = EquipmentCost.objects.create(custid=a, conid=b, bidid=d)
    i = EquipSelection.objects.create(custid=a, conid=b, bidid=d)
    j = JobCost.objects.create(custid=a, conid=b, bidid=d)
    k = laborCost.objects.create(custid=a, conid=b, bidid=d)
    l = MatCost.objects.create(custid=a, conid=b, bidid=d)
    ww = EquipSelection.objects.values_list('id', flat=True).last()
    xx = Contract.objects.values_list('id', flat=True).last()
    m = OSRCost.objects.create(custid=a, conid=b, bidid=d)
    m1 = SelectedEquip.objects.values_list('id', flat=True).last()
    m2 = m1 + 1
    n = SelectedEquip.objects.create(id=m2, custid=a, conid=b, bidid=d)
    o = TotalJobCost.objects.create(custid=a, conid=b, bidid=d)
    s6 = Bidding.objects.filter(id=d).update(jobid=ww)
    s7 = Contract.objects.filter(id=xx).update(jobid=ww)
    context = {
        "instance": instance,

        "form": form,
        "c": c,
        "d1": d1,
        "e": e,
        "f": f,
        "g": g,
        "h": h,
        "i": i,
        "j": j,
        "k": k,
        "l": l,
        "m": m,
        "n": n,
        "o": o,
        "s6": s6,
        "s7": s7,
    }
    return redirect(instance.get_absolute14_url(), context)





def jobselection(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = EquipmentSelect(request.POST or None, instance=instance)
    uu = Contract.objects.values_list('id', flat=True).last()
    vv = Bidding.objects.values_list('id', flat=True).last()
    ww = EquipSelection.objects.values_list('id', flat=True).last()
    Bidding.objects.filter(id=vv).update(bidid=vv)
    EquipSelection.objects.filter(id=ww).update(bidid=vv, jobid=ww)
    Contract.objects.filter(id=uu).update(bidid=vv)
    instance2 = get_object_or_404(EquipSelection, jobid=ww)

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
    }
    return render(request, 'mha/jobselection.html', context)


def jobselection2(request, bidid=None):
    instance = get_object_or_404(EquipSelection, bidid=bidid)
    form = EquipmentSelect(request.POST or None, instance=instance)

    a = EquipSelection.objects.values_list('conid', flat=True).get(bidid=bidid)
    b = EquipSelection.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = EquipSelection.objects.values_list('optionid', flat=True).get(bidid=bidid)
    c1 = EquipSelection.objects.values_list('jobid', flat=True).get(bidid=bidid)
    d = c + 1
    e = Option.objects.values_list('option', flat=True).get(id=d)
    f = EquipSelection.objects.create(custid=b, conid=a, optionid=d, options=e, jobid=c1)
    g = EquipSelection.objects.values_list('id', flat=True).last()

    j = Bidding.objects.create(custid=b, conid=a, jobid=c1, optionsid=d, options=e)
    j1 = Bidding.objects.values_list('id', flat=True).last()
    j2 = Bidding.objects.filter(id=j1).update(bidid=j1)
    k = CurrentJobInfo.objects.create(custid=b, conid=a, bidid=j1, jobid=c1, optionid=d, options=e)
    l = EquipSelection.objects.filter(id=g).update(bidid=j1)
    i = Contract.objects.create(custid=b, conid=a, jobid=c1, bidid=j1)
    queryset = EquipSelection.objects.filter(id=g)
    instance2 = get_object_or_404(EquipSelection, id=g)

    j3 = Bidding.objects.filter(jobid=c1).count()
    k1 = Bidding.objects.filter(jobid=c1).update(count=j3)

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        'f': f,
        'g': g,
        'i': i,
        'j': j,
        'k': k,
        "j2": j2,
        "l": l,
        'k1': k1,
    }
    return render(request, 'mha/jobselection2.html', context)


def jobselection3(request, bidid=None):
    instance = get_object_or_404(EquipSelection, bidid=bidid)
    form = EquipmentSelect(request.POST or None, instance=instance)

    a = EquipSelection.objects.values_list('conid', flat=True).get(bidid=bidid)
    b = EquipSelection.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = EquipSelection.objects.values_list('optionid', flat=True).get(bidid=bidid)
    c1 = EquipSelection.objects.values_list('jobid', flat=True).get(bidid=bidid)
    c2 = EquipSelection.objects.values_list('joblocation', flat=True).get(bidid=bidid)
    d = c + 1
    e = Option.objects.values_list('option', flat=True).get(id=d)
    f = EquipSelection.objects.create(custid=b, conid=a, optionid=d, options=e, jobid=c1)
    g = EquipSelection.objects.values_list('id', flat=True).last()

    j = Bidding.objects.create(custid=b, conid=a, jobid=c1, optionsid=d, options=e, joblocation=c2)
    j1 = Bidding.objects.values_list('id', flat=True).last()
    j2 = Bidding.objects.filter(id=j1).update(bidid=j1)
    k = CurrentJobInfo.objects.create(custid=b, conid=a, bidid=j1, jobid=c1, optionid=d, options=e)
    l = EquipSelection.objects.filter(id=g).update(bidid=j1, joblocation=c2)
    i = Contract.objects.create(custid=b, conid=a, jobid=c1, bidid=j1)
    queryset = EquipSelection.objects.filter(id=g)
    instance2 = get_object_or_404(EquipSelection, id=g)

    c3 = Bidding.objects.filter(jobid=c1).count()
    d1 = Bidding.objects.filter(jobid=c1).update(count=c3)

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "d1": d1,
        'f': f,
        'g': g,
        'i': i,
        'j': j,
        'k': k,
        "j2": j2,
        "l": l,
    }
    return render(request, 'mha/jobselection3.html', context)


def jobselection4(request, bidid=None):
    instance = get_object_or_404(EquipSelection, bidid=bidid)
    form = EquipmentSelect(request.POST or None, instance=instance)

    a = EquipSelection.objects.values_list('conid', flat=True).get(bidid=bidid)
    b = EquipSelection.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = EquipSelection.objects.values_list('optionid', flat=True).get(bidid=bidid)
    c1 = EquipSelection.objects.values_list('jobid', flat=True).get(bidid=bidid)
    c2 = EquipSelection.objects.values_list('joblocation', flat=True).get(bidid=bidid)
    d = c + 1
    e = Option.objects.values_list('option', flat=True).get(id=d)
    f = EquipSelection.objects.create(custid=b, conid=a, optionid=d, options=e, jobid=c1)
    g = EquipSelection.objects.values_list('id', flat=True).last()

    j = Bidding.objects.create(custid=b, conid=a, jobid=c1, optionsid=d, options=e, joblocation=c2)
    j1 = Bidding.objects.values_list('id', flat=True).last()
    j2 = Bidding.objects.filter(id=j1).update(bidid=j1)
    k = CurrentJobInfo.objects.create(custid=b, conid=a, bidid=j1, jobid=c1, optionid=d, options=e)
    l = EquipSelection.objects.filter(id=g).update(bidid=j1, joblocation=c2)
    i = Contract.objects.create(custid=b, conid=a, jobid=c1, bidid=j1)
    queryset = EquipSelection.objects.filter(id=g)
    instance2 = get_object_or_404(EquipSelection, id=g)

    c3 = Bidding.objects.filter(jobid=c1).count()
    d1 = Bidding.objects.filter(jobid=c1).update(count=c3)

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "d1": d1,
        'f': f,
        'g': g,
        'i': i,
        'j': j,
        'k': k,
        "j2": j2,
        "l": l,
    }
    return render(request, 'mha/jobselection4.html', context)


def jobselection5(request, bidid=None):
    instance = get_object_or_404(EquipSelection, bidid=bidid)
    form = EquipmentSelect(request.POST or None, instance=instance)

    a = EquipSelection.objects.values_list('conid', flat=True).get(bidid=bidid)
    b = EquipSelection.objects.values_list('custid', flat=True).get(bidid=bidid)
    c = EquipSelection.objects.values_list('optionid', flat=True).get(bidid=bidid)
    c1 = EquipSelection.objects.values_list('jobid', flat=True).get(bidid=bidid)
    c2 = EquipSelection.objects.values_list('joblocation', flat=True).get(bidid=bidid)
    d = c + 1
    e = Option.objects.values_list('option', flat=True).get(id=d)
    f = EquipSelection.objects.create(custid=b, conid=a, optionid=d, options=e, jobid=c1)
    g = EquipSelection.objects.values_list('id', flat=True).last()

    j = Bidding.objects.create(custid=b, conid=a, jobid=c1, optionsid=d, options=e, joblocation=c2)
    j1 = Bidding.objects.values_list('id', flat=True).last()
    j2 = Bidding.objects.filter(id=j1).update(bidid=j1)
    k = CurrentJobInfo.objects.create(custid=b, conid=a, bidid=j1, jobid=c1, optionid=d, options=e)
    l = EquipSelection.objects.filter(id=g).update(bidid=j1, joblocation=c2)
    i = Contract.objects.create(custid=b, conid=a, jobid=c1, bidid=j1)
    queryset = EquipSelection.objects.filter(id=g)
    instance2 = get_object_or_404(EquipSelection, id=g)

    c3 = Bidding.objects.filter(jobid=c1).count()
    d1 = Bidding.objects.filter(jobid=c1).update(count=c3)

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "d1": d1,
        'f': f,
        'g': g,
        'i': i,
        'j': j,
        'k': k,
        "j2": j2,
        "l": l,
    }
    return render(request, 'mha/jobselection5.html', context)


def contractorpage(request, id=None):
    instance = get_object_or_404(ContractorInfo, id=id)
    form = Coninfo(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(conid=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
    }
    return render(request, 'mha/contractorpage.html', context)


def customerinfo(request, custid=None):
    instance = get_object_or_404(CustomerInfo, custid=custid)
    form = Custinfo(request.POST or None, instance=instance)
    a = EquipSelection.objects.filter(custid=custid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(custid=a)
    b = EquipSelection.objects.filter(custid=custid).values_list('bidid', flat=True)[0]
    c1 = CurrentJobInfo.objects.filter(custid=custid).values_list('jobid', flat=True).count()
    d1 = CurrentJobInfo.objects.filter(custid=custid).update(count=c1)
    instance2 = get_object_or_404(EquipSelection, bidid=b)
    instance1 = get_object_or_404(JobCost, bidid=b)
    queryset2 = CurrentJobInfo.objects.filter(bidid=b)

    f1 = EquipSelection.objects.filter(custid=custid).annotate(bididG=F('bidid'))
    f2 = list(f1.values_list('bidid', flat=True))
    ee = list(set(f2))
    try:
        c = EquipSelection.objects.filter(custid=custid).values_list('bidid', flat=True)[1]
        instance3 = get_object_or_404(EquipSelection, bidid=c)
    except Exception as ee:
        c = 0
        instance3 = 0
    try:
        d = EquipSelection.objects.filter(custid=custid).values_list('bidid', flat=True)[2]
        instance4 = get_object_or_404(EquipSelection, bidid=d)
    except Exception as ee:
        d = 0
        instance4 = 0
    try:
        e = EquipSelection.objects.filter(custid=custid).values_list('bidid', flat=True)[3]
        instance5 = get_object_or_404(EquipSelection, bidid=e)
    except Exception as ee:
        e = 0
        instance5 = 0
    try:
        f = EquipSelection.objects.filter(custid=custid).values_list('bidid', flat=True)[4]
        instance6 = get_object_or_404(EquipSelection, bidid=f)
    except Exception as ee:
        f = 0
        instance6 = 0

    queryset3 = CurrentJobInfo.objects.filter(bidid=c)
    queryset4 = CurrentJobInfo.objects.filter(bidid=d)
    queryset5 = CurrentJobInfo.objects.filter(bidid=e)
    queryset6 = CurrentJobInfo.objects.filter(bidid=f)

    context = {
        "instance": instance,
        "instance1": instance1,
        "instance2": instance2,
        "instance3": instance3,
        "instance4": instance4,
        "instance5": instance5,
        "instance6": instance6,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "d1": d1,
    }
    return render(request, 'mha/customerinfo.html', context)


def customerpage(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = Custinfo(request.POST or None, instance=instance)
    queryset = CurrentJobInfo.objects.filter(custid=id)
    #    queryset2 = EquipSelection.objects.filter(custid=id)
    queryset2 = Custpagelocation.objects.filter(custid=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
    }
    return render(request, 'mha/customerpage.html', context)


def addcustconfirm(request, id=None):
    instance = CustomerInfo.objects.filter(id=id).last()
    form = DupConInfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute10_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/addcustconfirm.html', context)


def addcust(request, id=None):
    a = CustomerInfo.objects.create(conid=id)
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.filter(id=b).update(custid=b)
    instance2 = get_object_or_404(ContractorInfo, id=id)
    instance = get_object_or_404(CustomerInfo, conid=id)
    form = CustinfoB(request.POST or None, instance=instance, prefix='form1')
    form2 = Coninfo(request.POST or None, instance=instance2, prefix='form2')
    queryset = ContractorInfo.objects.filter(conid=id).values()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute10_url(), context2)
    context = {
        "a": a,
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "form2": form2,
        "object_list": queryset,
    }
    return render(request, 'mha/addcust.html', context)


def custcompany(request):
    form = CustinfoB(request.POST)
    a = CustomerInfo.objects.values_list('id', flat=True).last()
    d = request.POST['id_form1-custcompanytname']
    CustomerInfo.objects.filter(id=a).update(custcompanytname=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addcust.html', context)


def conedit(request, id=None):
    instance = get_object_or_404(ContractorInfo, id=id)
    form = Coninfo(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute2_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/conedit.html', context)


def con_info_existing(request):
    queryset = ContractorInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(concompanytname__icontains=search_term)
                                   | Q(confirstname__icontains=search_term)
                                   | Q(conlastname__icontains=search_term)
                                   | Q(conadd1__icontains=search_term)
                                   | Q(conadd2__icontains=search_term)
                                   | Q(concity__icontains=search_term)
                                   | Q(const__icontains=search_term)
                                   | Q(conzipcode__icontains=search_term)
                                   | Q(conwork1__icontains=search_term)
                                   | Q(conwork2__icontains=search_term)
                                   | Q(concell1__icontains=search_term)
                                   | Q(concell2__icontains=search_term)
                                   | Q(conhome__icontains=search_term)
                                   | Q(conemail1__icontains=search_term)
                                   | Q(conemail2__icontains=search_term))

    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'mha/con_info_existing.html', context)


def cust_info_existing(request):
    queryset = CustomerInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(custcompanytname__icontains=search_term)
                                   | Q(custfirstname__icontains=search_term)
                                   | Q(custlastname__icontains=search_term)
                                   | Q(custadd1__icontains=search_term)
                                   | Q(custadd2__icontains=search_term)
                                   | Q(custcity__icontains=search_term)
                                   | Q(custst__icontains=search_term)
                                   | Q(custzipcode__icontains=search_term)
                                   | Q(custwork1__icontains=search_term)
                                   | Q(custwork2__icontains=search_term)
                                   | Q(custcell1__icontains=search_term)
                                   | Q(custcell2__icontains=search_term)
                                   | Q(custhome__icontains=search_term)
                                   | Q(custemail1__icontains=search_term)
                                   | Q(custemail2__icontains=search_term))
    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'mha/cust_info_existing.html', context)


def custedit(request, id=None):
    instance = get_object_or_404(CustomerInfo, id=id)
    form = CustinfoB(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute13_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/custedit.html', context)


def custcompany(request):
    form = CustinfoB(request.POST)
    a = CustomerInfo.objects.values_list('id', flat=True).last()
    d = request.POST['id_form1-custcompanytname']
    CustomerInfo.objects.filter(id=a).update(custcompanytname=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/addcust.html', context)


############################################  Equip. Selection 1 ###########################################################



def equipselection1(request, id=None):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(jobid=a).update(optionid=1, options='Option A')
    ab = Bidding.objects.filter(jobid=a).update(optionsid=1, options='Option A')
    ac = CurrentJobInfo.objects.filter(jobid=a).update(optionid=1, options='Option A')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    c = SelectedEquip.objects.values_list('id', flat=True).last()or 0
    d1 = c + 1
    d2 = c + 2
    d3 = c + 3
    d4 = c + 4
    d5 = c + 5
    d6 = c + 6
    d7 = c + 7

    SelectedEquip.objects.create(id = d1, equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d2, equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d3, equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d4, equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d5, equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d6, equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d7, equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, jobid=a)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect1(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()

    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)


def equipselection2A(request, id=None):
    FilterPlenumWidth.objects.all().delete()
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(jobid=a).update(optionid=1, options='Option A')
    ab = Bidding.objects.filter(jobid=a).update(optionsid=1, options='Option A')
    ac = CurrentJobInfo.objects.filter(jobid=a).update(optionid=1, options='Option A')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    c = SelectedEquip.objects.values_list('id', flat=True).last()or 0
    d1 = c + 1
    d2 = c + 2
    d3 = c + 3
    d4 = c + 4
    d5 = c + 5
    d6 = c + 6
    d7 = c + 7

    SelectedEquip.objects.create(id = d1, equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d2, equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d3, equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d4, equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d5, equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d6, equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(id = d7, equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, jobid=a)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect2(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()
    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)
    f = Equipment2.objects.filter(type='Furnace').annotate(widthA=F('width'))
    g = list(f.values_list('width', flat=True).distinct())
    try:
        h1 = FilterPlenumWidth.objects.create(id=1, furnplenumwidth=g[0])
    except Exception:
        h1 = 0
    try:
        h2 = FilterPlenumWidth.objects.create(id=2, furnplenumwidth=g[1])
    except Exception:
        h2 = 0
    try:
        h3 = FilterPlenumWidth.objects.create(id=3, furnplenumwidth=g[2])
    except Exception:
        h3 = 0
    try:
        h4 = FilterPlenumWidth.objects.create(id=4, outputsfurnplenumwidthtg3s=g[3])
    except Exception:
        h4 = 0
    try:
        h5 = FilterPlenumWidth.objects.create(id=5, outputsfurnplenumwidthtg3s=g[4])
    except Exception:
        h5 = 0
    try:
        h6 = FilterPlenumWidth.objects.create(id=6, outputsfurnplenumwidthtg3s=g[5])
    except Exception:
        h6 = 0
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_furnwidth(request):
    form = EquipmentSelect1(request.POST or None)
    furnwidth = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    context = {
        "furnwidth": furnwidth,
        "form": form,
    }
    return render(request, 'mha/furnwidth_1.html', context)


def load_furnwidth2(request):
    form = EquipmentSelect1(request.POST or None)
    furnwidth = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    context = {
        "furnwidth": furnwidth,
        "form": form,
    }
    return render(request, 'mha/furnwidth_2.html', context)


def load_furndepth(request):
    form = EquipmentSelect1(request.POST or None)
    furndepth = EquipSelection.objects.values_list('furndepth', flat=True).last()
    context = {
        "furndepth": furndepth,
        "form": form,
    }
    return render(request, 'mha/furndepth_1.html', context)


def load_furndepth2(request):
    form = EquipmentSelect1(request.POST or None)
    furndepth = EquipSelection.objects.values_list('furndepth', flat=True).last()
    context = {
        "furndepth": furndepth,
        "form": form,
    }
    return render(request, 'mha/furndepth_2.html', context)


def load_coilwidth(request):
    form = EquipmentSelect1(request.POST or None)
    coilwidth = EquipSelection.objects.values_list('coilwidth', flat=True).last()
    context = {
        "coilwidth": coilwidth,
        "form": form,
    }
    return render(request, 'mha/coilwidth_1.html', context)


def load_coilheight(request):
    form = EquipmentSelect1(request.POST or None)
    coilheight = EquipSelection.objects.values_list('coilheight', flat=True).last()
    context = {
        "coilheight": coilheight,
        "form": form,
    }
    return render(request, 'mha/coilheight_1.html', context)


def load_furnheight(request):
    form = EquipmentSelect1(request.POST or None)
    furnheight = EquipSelection.objects.values_list('furnheight', flat=True).last()
    context = {
        "furnheight": furnheight,
        "form": form,
    }
    return render(request, 'mha/furnheight_1.html', context)


def load_furncoilheight(request):
    form = EquipmentSelect1(request.POST or None)
    furncoilheight = EquipSelection.objects.values_list('furncoilheight', flat=True).last()
    context = {
        "furncoilheight": furncoilheight,
        "form": form,
    }
    return render(request, 'mha/furncoilheight_1.html', context)


def joblocation(request):
    a1 = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_joblocation']
    c = JobLocation.objects.filter(id=b).values_list('jobloc', flat=True)
    d = EquipSelection.objects.filter(bidid=a1).update(joblocation=c)
    e = CurrentJobInfo.objects.filter(bidid=a1).update(currentlocrm=c)
    f = Bidding.objects.filter(bidid=a1).update(joblocation=c)
    context = {
        "form": form,
        "d": d,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/equipselection1.html', context)


def airhandler(request):
    a1 = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_furntype'] or 0
    c = FurnaceType.objects.filter(id=b).values_list('furntype', flat=True) or 0
    d = EquipSelection.objects.filter(bidid=a1).update(airhandlertype=c)
    context = {
        "form": form,
        "d": d,
    }
    return render(request, 'mha/equipselection1.html', context)


def outsideunit(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondEff.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_outsideunittype'] or 0
    c = OutsideUnitType.objects.filter(id=b).values_list('outsidetype', flat=True) or 0
    d = EquipSelection.objects.filter(bidid=a).update(outsideunittype=c)
    e = Equipment2.objects.filter(type='Condenser').annotate(effA=F('eff'))
    g = list(e.values_list('eff', flat=True).distinct())
    try:
        h = FilterCondEff.objects.create(id=1, condefffilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondEff.objects.create(id=2, condefffilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondEff.objects.create(id=3, condefffilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondEff.objects.create(id=4, condefffilter=g[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCondEff.objects.create(id=5, condefffilter=g[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCondEff.objects.create(id=6, condefffilter=g[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCondEff.objects.create(id=7, condefffilter=g[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCondEff.objects.create(id=8, condefffilter=g[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCondEff.objects.create(id=9, condefffilter=g[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCondEff.objects.create(id=10, condefffilter=g[9])
    except Exception:
        h9 = 0

    context = {
        "form": form,
        "d": d,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_condeff(request):
    a = FilterCondEff.objects.all()
    form = EquipmentSelect1(request.POST or None)
    condeff = a.values('condefffilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "condeff": condeff,
        "warr": warr,
        "form": form,
    }
    return render(request, 'mha/condeff_1.html', context)

def condeff(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondbtu.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    #    SelectedEquip.objects.filter(equipid=1, bidid=a).delete()
    b = request.POST['id_condeff']
    b1 = EquipSelection.objects.filter(bidid=a).update(condbtu='', conddescript='', condmodnum='', furnbtu='',
                                                       furnconfig='', furneff='', furndescript='', furnmodnum='',
                                                       furnheight=0.00, furnwidth=0.00, coilbtu='', coilconfig='',
                                                       coilmodnum='', coilwidth=0.00, coilheight=0.00,
                                                       furncoilheight=0.00)
    c = FilterCondEff.objects.filter(id=b).values_list('condefffilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(condeff=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(type='Condenser', eff=d1)
    e = Equipment2.objects.filter(type='Condenser', eff=d1).annotate(btuA=F('btu'))
    g = list(e.values_list('btu', flat=True).distinct())
    try:
        h = FilterCondbtu.objects.create(id=1, condbtufilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondbtu.objects.create(id=2, condbtufilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondbtu.objects.create(id=3, condbtufilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondbtu.objects.create(id=4, condbtufilter=g[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCondbtu.objects.create(id=5, condbtufilter=g[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCondbtu.objects.create(id=6, condbtufilter=g[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCondbtu.objects.create(id=7, condbtufilter=g[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCondbtu.objects.create(id=8, condbtufilter=g[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCondbtu.objects.create(id=9, condbtufilter=g[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCondbtu.objects.create(id=10, condbtufilter=g[9])
    except Exception:
        h9 = 0

    context = {
        "form": form,
        "d": d,
        "b1": b1,
        "d2": d2,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_condbtu(request):
    a = FilterCondbtu.objects.all()
    form = EquipmentSelect1(request.POST or None)
    condbtu = a.values('condbtufilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "condbtu": condbtu,
        "form": form,
    }
    return render(request, 'mha/condbtu_1.html', context)


def condeff2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondbtu.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    #    SelectedEquip.objects.filter(equipid=1, bidid=a).delete()
    b = request.POST['id_condeff']
    c = FilterCondEff.objects.filter(id=b).values_list('condefffilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(condeff=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(type='Condenser', eff=d1)
    d3 = EquipSelection.objects.filter(bidid=a).update(condmodnum='')
    e = Equipment2.objects.filter(type='Condenser', eff=d1).annotate(btuA=F('btu'))
    g = list(e.values_list('btu', flat=True).distinct())
    try:
        h = FilterCondbtu.objects.create(id=1, condbtufilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondbtu.objects.create(id=2, condbtufilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondbtu.objects.create(id=3, condbtufilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondbtu.objects.create(id=4, condbtufilter=g[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCondbtu.objects.create(id=5, condbtufilter=g[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCondbtu.objects.create(id=6, condbtufilter=g[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCondbtu.objects.create(id=7, condbtufilter=g[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCondbtu.objects.create(id=8, condbtufilter=g[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCondbtu.objects.create(id=9, condbtufilter=g[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCondbtu.objects.create(id=10, condbtufilter=g[9])
    except Exception:
        h9 = 0

    context = {
        "form": form,
        "d": d,
        "d2": d2,
        "d3": d3,

    }
    return render(request, 'mha/equipselection2A.html', context)



def load_condbtu2A(request):
    a = FilterCondbtu.objects.all()
    form = EquipmentSelect1(request.POST or None)
    condbtu = a.values('condbtufilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute24_url())
    context = {
        "condbtu": condbtu,
        "form": form,
    }
    return render(request, 'mha/condbtu_1.html', context)


def condbtu2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondDescrip.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_condbtu']
   # b1 = EquipSelection.objects.filter(bidid=a).update(conddescript='', condmodnum='', furnbtu='',
   #                                                    furnconfig='', furneff='', furndescript='', furnmodnum='',
   #                                                    furnheight=0.00, furnwidth=0.00, coilbtu='', coilconfig='',
   #                                                    coilmodnum='', coilwidth=0.00, coilheight=0.00,
   #                                                    furncoilheight=0.00)
    c = FilterCondbtu.objects.filter(id=b).values_list('condbtufilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(condbtu=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = EquipSelection.objects.values_list('condbtu', flat=True).last()
    d3 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(btu=d2)
    e = Equipment2.objects.filter(type='Condenser', eff=d1, btu=d2).annotate(mfgmodeldescripA=F('mfgmodeldescrip'))
    g = list(e.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        h = FilterCondDescrip.objects.create(id=1, conddescripfilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondDescrip.objects.create(id=2, conddescripfilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondDescrip.objects.create(id=3, conddescripfilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondDescrip.objects.create(id=4, conddescripfilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
    #    "b1": b1,
        "d3": d3,

    }
    return render(request, 'mha/equipselection2A.html', context)


def condbtu(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondDescrip.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_condbtu']
    b1 = EquipSelection.objects.filter(bidid=a).update(conddescript='', condmodnum='', furnbtu='',
                                                       furnconfig='', furneff='', furndescript='', furnmodnum='',
                                                       furnheight=0.00, furnwidth=0.00, coilbtu='', coilconfig='',
                                                       coilmodnum='', coilwidth=0.00, coilheight=0.00,
                                                       furncoilheight=0.00)
    c = FilterCondbtu.objects.filter(id=b).values_list('condbtufilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(condbtu=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = EquipSelection.objects.values_list('condbtu', flat=True).last()
    d3 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(btu=d2)
    e = Equipment2.objects.filter(type='Condenser', eff=d1, btu=d2).annotate(mfgmodeldescripA=F('mfgmodeldescrip'))
    g = list(e.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        h = FilterCondDescrip.objects.create(id=1, conddescripfilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondDescrip.objects.create(id=2, conddescripfilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondDescrip.objects.create(id=3, conddescripfilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondDescrip.objects.create(id=4, conddescripfilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "b1": b1,
        "d3": d3,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_conddescript(request):
    a = FilterCondDescrip.objects.all()
    form = EquipmentSelect1(request.POST or None)
    conddescript = a.values('conddescripfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "conddescript": conddescript,
        "form": form,
    }
    return render(request, 'mha/conddescript_1.html', context)


def load_conddescript2A(request):
    a = FilterCondDescrip.objects.all()
    form = EquipmentSelect1(request.POST or None)
    conddescript = a.values('conddescripfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute24_url())
    context = {
        "conddescript": conddescript,
        "form": form,
    }
    return render(request, 'mha/conddescript2A_1.html', context)


def conddescrip2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_conddescript']
    c = FilterCondDescrip.objects.filter(id=b).values_list('conddescripfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(conddescript=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = EquipSelection.objects.values_list('condbtu', flat=True).last()
    d3 = EquipSelection.objects.values_list('conddescript', flat=True).last()
    d4 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(mfgmodeldescrip=d3)
    e = Equipment2.objects.filter(type='Condenser', eff=d1, btu=d2, mfgmodeldescrip=d3).values_list('modelnum', flat=True).last()
    e2 = EquipSelection.objects.filter(bidid=a).update(condmodnum=e)
    a3 = EquipSelection.objects.values_list('bidid', flat=True).last()
    b3 = EquipSelection.objects.filter(bidid=a3).values_list('existfurnwidth', flat=True).last()
    b3a = EquipSelection.objects.filter(bidid=a3).values_list('existfurnconfig', flat=True).last()
    c3 = Equipment2.objects.filter(type='Evap. Coil', width=b3, config=b3a).annotate(configA=F('config'))
    d5 = list(c3.values_list('config', flat=True).distinct())
    try:
        h = FilterCoilConfig.objects.create(id=1, coilconfigfilter=d5[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilConfig.objects.create(id=2, coilconfigfilter=d5[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilConfig.objects.create(id=3, coilconfigfilter=d5[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilConfig.objects.create(id=4, coilconfigfilter=d5[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCoilConfig.objects.create(id=5, coilconfigfilter=d5[4])
    except Exception:
        h4 = 0

    context = {
        "form": form,
        "d3": d3,
        "d": d,
        "e": e,
        "e2": e2,
        "d4": d4,
        "a3": a3,
        "b3": b3,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
    }
    return render(request, 'mha/equipselection2A.html', context)


def coilconfig2up(request):
    FilterCoilConfig.objects.all().delete()
    form = EquipmentSelect2(request.POST)
    a3 = EquipSelection.objects.values_list('bidid', flat=True).last()
    b3 = EquipSelection.objects.filter(bidid=a3).values_list('existfurnwidth', flat=True).last()
    b3a = EquipSelection.objects.filter(bidid=a3).values_list('existfurnconfig', flat=True).last()
    c3 = Equipment2.objects.filter(type='Evap. Coil', width=b3, config=b3a).annotate(configA=F('config'))
    d5 = list(c3.values_list('config', flat=True).distinct())
    try:
        h = FilterCoilConfig.objects.create(id=1, coilconfigfilter=d5[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilConfig.objects.create(id=2, coilconfigfilter=d5[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilConfig.objects.create(id=3, coilconfigfilter=d5[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilConfig.objects.create(id=4, coilconfigfilter=d5[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCoilConfig.objects.create(id=5, coilconfigfilter=d5[4])
    except Exception:
        h4 = 0

    c3a = Equipment2.objects.filter(type='Evap. Coil', width__lte=b3, config='Uncased').annotate(configA=F('config'))
    d5a = list(c3a.values_list('config', flat=True).distinct())
    try:
        h5 = FilterCoilConfig.objects.create(id=6, coilconfigfilter=d5a[0])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCoilConfig.objects.create(id=7, coilconfigfilter=d5a[1])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCoilConfig.objects.create(id=8, coilconfigfilter=d5a[2])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCoilConfig.objects.create(id=9, coilconfigfilter=d5a[3])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCoilConfig.objects.create(id=10, coilconfigfilter=d5a[4])
    except Exception:
        h9 = 0

    c3b = Equipment2.objects.filter(type='Evap. Coil', width=b3, config='Upflow/Downflow').annotate(configA=F('config'))
    d5b = list(c3b.values_list('config', flat=True).distinct())
    try:
        h10 = FilterCoilConfig.objects.create(id=11, coilconfigfilter=d5b[0])
    except Exception:
        h10 = 0
    try:
        h11 = FilterCoilConfig.objects.create(id=12, coilconfigfilter=d5b[1])
    except Exception:
        h11 = 0
    try:
        h12 = FilterCoilConfig.objects.create(id=13, coilconfigfilter=d5b[2])
    except Exception:
        h12 = 0
    try:
        h13 = FilterCoilConfig.objects.create(id=14, coilconfigfilter=d5b[3])
    except Exception:
        h13 = 0
    try:
        h14 = FilterCoilConfig.objects.create(id=15, coilconfigfilter=d5b[4])
    except Exception:
        h14 = 0

    c3c = Equipment2.objects.filter(type='Evap. Coil', width=b3, config='Upflow/Downflow/Horizontal').annotate(configA=F('config'))
    d5c = list(c3c.values_list('config', flat=True).distinct())
    try:
        h15 = FilterCoilConfig.objects.create(id=16, coilconfigfilter=d5c[0])
    except Exception:
        h15 = 0
    try:
        h16 = FilterCoilConfig.objects.create(id=17, coilconfigfilter=d5c[1])
    except Exception:
        h16 = 0
    try:
        h17 = FilterCoilConfig.objects.create(id=18, coilconfigfilter=d5c[2])
    except Exception:
        h17 = 0
    try:
        h18 = FilterCoilConfig.objects.create(id=19, coilconfigfilter=d5c[3])
    except Exception:
        h18 = 0
    try:
        h19 = FilterCoilConfig.objects.create(id=20, coilconfigfilter=d5c[4])
    except Exception:
        h19 = 0

    context = {
        "form": form,
        "a3": a3,
        "b3": b3,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "h12": h12,
        "h13": h13,
        "h14": h14,
        "h15": h15,
        "h16": h16,
        "h17": h17,
        "h18": h18,
        "h19": h19,

    }
    return render(request, 'mha/coilconfig2A_1.html', context)


def load_coilbtu2A(request):
    a = FilterCoilbtu.objects.all()
    form = EquipmentSelect2(request.POST or None)
    coilbtu = a.values('coilbtufilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute24_url())
    context = {
        "coilbtu": coilbtu,
        "form": form,
    }
    return render(request, 'mha/coilbtu_1.html', context)


def coilconfig2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCoilbtu.objects.all().delete()
    form = EquipmentSelect2(request.POST)
    b = request.POST['id_coilconfig']
    c = FilterCoilConfig.objects.filter(id=b).values_list('coilconfigfilter', flat=True).last()
    d = EquipSelection.objects.filter(bidid=a).update(coilconfig=c)
    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('plenumwidth', flat=True).last()
    if d2 == 'Uncased':
        e = Equipment2.objects.filter(type='Evap. Coil', config=d2, width__lte=d3).annotate(btuA=F('btu'))
        g = list(e.values_list('btu', flat=True).distinct())
        try:
            h = FilterCoilbtu.objects.create(id=1, coilbtufilter=g[0])
        except Exception:
            h = 0
        try:
            h1 = FilterCoilbtu.objects.create(id=2, coilbtufilter=g[1])
        except Exception:
            h1 = 0
        try:
            h2 = FilterCoilbtu.objects.create(id=3, coilbtufilter=g[2])
        except Exception:
            h2 = 0
        try:
            h3 = FilterCoilbtu.objects.create(id=4, coilbtufilter=g[3])
        except Exception:
            h3 = 0
        try:
            h4 = FilterCoilbtu.objects.create(id=5, coilbtufilter=g[4])
        except Exception:
            h4 = 0
        try:
            h5 = FilterCoilbtu.objects.create(id=6, coilbtufilter=g[5])
        except Exception:
            h5 = 0
        try:
            h6 = FilterCoilbtu.objects.create(id=7, coilbtufilter=g[6])
        except Exception:
            h6 = 0
        try:
            h7 = FilterCoilbtu.objects.create(id=8, coilbtufilter=g[7])
        except Exception:
            h7 = 0
        try:
            h8 = FilterCoilbtu.objects.create(id=9, coilbtufilter=g[8])
        except Exception:
            h8 = 0
        try:
            h9 = FilterCoilbtu.objects.create(id=10, coilbtufilter=g[9])
        except Exception:
            h9 = 0
    else:
        e = Equipment2.objects.filter(type='Evap. Coil', config=d2, width=d3).annotate(btuA=F('btu'))
        g = list(e.values_list('btu', flat=True).distinct())
        try:
            h = FilterCoilbtu.objects.create(id=1, coilbtufilter=g[0])
        except Exception:
            h = 0
        try:
            h1 = FilterCoilbtu.objects.create(id=2, coilbtufilter=g[1])
        except Exception:
            h1 = 0
        try:
            h2 = FilterCoilbtu.objects.create(id=3, coilbtufilter=g[2])
        except Exception:
            h2 = 0
        try:
            h3 = FilterCoilbtu.objects.create(id=4, coilbtufilter=g[3])
        except Exception:
            h3 = 0
        try:
            h4 = FilterCoilbtu.objects.create(id=5, coilbtufilter=g[4])
        except Exception:
            h4 = 0
        try:
            h5 = FilterCoilbtu.objects.create(id=6, coilbtufilter=g[5])
        except Exception:
            h5 = 0
        try:
            h6 = FilterCoilbtu.objects.create(id=7, coilbtufilter=g[6])
        except Exception:
            h6 = 0
        try:
            h7 = FilterCoilbtu.objects.create(id=8, coilbtufilter=g[7])
        except Exception:
            h7 = 0
        try:
            h8 = FilterCoilbtu.objects.create(id=9, coilbtufilter=g[8])
        except Exception:
            h8 = 0
        try:
            h9 = FilterCoilbtu.objects.create(id=10, coilbtufilter=g[9])
        except Exception:
            h9 = 0

    context = {
        "form": form,
        "d": d,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,

    }
    return render(request, 'mha/equipselection2A.html', context)



def coilbtu2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCoiltype.objects.all().delete()
    form = EquipmentSelect2(request.POST)
    b = request.POST['id_coilbtu']
    c = FilterCoilbtu.objects.filter(id=b).values_list('coilbtufilter', flat=True).last()
    d = EquipSelection.objects.filter(bidid=a).update(coilbtu=c)
    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('coilbtu', flat=True).last()
    d4 = Equipment2.objects.filter(type='Evap. Coil', config=d2, btu=d3).annotate(mfgmodeldescripA=F('mfgmodeldescrip'))
    d5 = list(d4.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        h = FilterCoiltype.objects.create(id=1, coiltypefilter=d5[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoiltype.objects.create(id=2, coiltypefilter=d5[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoiltype.objects.create(id=3, coiltypefilter=d5[2])
    except Exception:
        h2 = 0

    context = {
        "form": form,
        "d": d,
        "h": h,
        "h1": h1,
        "h2": h2,


    }
    return render(request, 'mha/equipselection2A.html', context)


def load_coiltype2A(request):
    a = FilterCoiltype.objects.all()
    form = EquipmentSelect2(request.POST or None)
    coiltype = a.values('coiltypefilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute24_url())
    context = {
        "coiltype": coiltype,
        "form": form,
    }
    return render(request, 'mha/coiltype2A_1.html', context)


def coiltype2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCoilModelnum.objects.all().delete()
    form = EquipmentSelect2(request.POST)
    b = request.POST['id_coiltype']
    c = FilterCoiltype.objects.filter(id=b).values_list('coiltypefilter', flat=True).last()
    d = EquipSelection.objects.filter(bidid=a).update(coiltype=c)
    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('coilbtu', flat=True).last()
    d3a = EquipSelection.objects.values_list('coiltype', flat=True).last()
    d4 = Equipment2.objects.filter(type='Evap. Coil', config=d2, btu=d3, mfgmodeldescrip=d3a)
    d5 = d4.values_list('modelnum', flat=True).distinct().last()
    d6 = d4.values_list('height', flat=True).distinct().last()
    d7 = d4.values_list('width', flat=True).distinct().last()
    d8 = d4.values_list('depth', flat=True).distinct().last()
    d9 = EquipSelection.objects.filter(bidid=a).update(coilmodnum=d5,coilheight=d6,coilwidth=d7,coildepth=d8)

    context = {
        "form": form,
        "d": d,
        "d9": d9,
    }
    return render(request, 'mha/equipselection2A.html', context)



def load_coilmodnum2A(request):
    form = EquipmentSelect2(request.POST or None)
    coilmodnum = EquipSelection.objects.values_list('coilmodnum', flat=True).last()
    context = {
        "coilmodnum": coilmodnum,
        "form": form,
    }
    return render(request, 'mha/coilmodnum2A_1.html', context)


def load_coilheight2A(request):
    form = EquipmentSelect2(request.POST or None)
    coilheight = EquipSelection.objects.values_list('coilheight', flat=True).last()
    context = {
        "coilheight": coilheight,
        "form": form,
    }
    return render(request, 'mha/coilheight2A_1.html', context)


def load_coilwidth2A(request):
    form = EquipmentSelect2(request.POST or None)
    coilwidth = EquipSelection.objects.values_list('coilwidth', flat=True).last()
    context = {
        "coilwidth": coilwidth,
        "form": form,
    }
    return render(request, 'mha/coilwidth2A_1.html', context)


def load_coildepth2A(request):
    form = EquipmentSelect2(request.POST or None)
    coildepth = EquipSelection.objects.values_list('coildepth', flat=True).last()
    context = {
        "coildepth": coildepth,
        "form": form,
    }
    return render(request, 'mha/coildepth2A_1.html', context)


def addthermostat1(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_addthermostat']
    c = YesNo.objects.filter(id=b).values_list('noyes', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(addthermostat=c)
    context = {
        "form": form,
        "d": d,

    }
    return render(request, 'mha/equipselection1.html', context)



def addthermostat2A(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect2(request.POST)
    b = request.POST['id_addthermostat']
    c = YesNo.objects.filter(id=b).values_list('noyes', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(addthermostat=c)
    context = {
        "form": form,
        "d": d,

    }
    return render(request, 'mha/equipselection2A.html', context)




def conddescrip(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCondModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_conddescript']
    c = FilterCondDescrip.objects.filter(id=b).values_list('conddescripfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(conddescript=c)
    d1 = EquipSelection.objects.values_list('condeff', flat=True).last()
    d2 = EquipSelection.objects.values_list('condbtu', flat=True).last()
    d3 = EquipSelection.objects.values_list('conddescript', flat=True).last()
    d4 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(mfgmodeldescrip=d3)
    e = Equipment2.objects.filter(type='Condenser', eff=d1, btu=d2, mfgmodeldescrip=d3).annotate(
        modelnumA=F('modelnum'))
    g = list(e.values_list('modelnum', flat=True).distinct())
    try:
        h = FilterCondModelnum.objects.create(id=1, condmodelnumfilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCondModelnum.objects.create(id=2, condmodelnumfilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCondModelnum.objects.create(id=3, condmodelnumfilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCondModelnum.objects.create(id=4, condmodelnumfilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "d4": d4,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_condmodnum(request):
    a = FilterCondModelnum.objects.all()
    form = EquipmentSelect1(request.POST or None)
    condmodnum = a.values('condmodelnumfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "condmodnum": condmodnum,
        "form": form,
    }
    return render(request, 'mha/condmodnum_1.html', context)


def load_condmodnum2A(request):
    form = EquipmentSelect2(request.POST or None)
    FilterCoilConfig.objects.all().delete()
    condmodnum = EquipSelection.objects.values_list('condmodnum', flat=True).last()

    context = {
        "condmodnum": condmodnum,
        "form": form,

    }
    return render(request, 'mha/condmodnum2A_1.html', context)



def load_coilconfig2A(request):
    form = EquipmentSelect2(request.POST or None)
    FilterCoilConfig.objects.all().delete()
    coilconfig = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    context = {
        "coilconfig": coilconfig,
        "form": form,

    }
    return render(request, 'mha/coilconfig2A_1.html', context)


def condmodnum(request):
    FilterFurnbtu.objects.all().delete()
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    aa = Bidding.objects.values_list('bidid', flat=True).last()
    ab = Bidding.objects.values_list('conid', flat=True).last()
    ac = Bidding.objects.values_list('custid', flat=True).last()
    #    TotalJobCost.objects.filter(bidid=a,descripid=1).delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_condmodnum']
    c = FilterCondModelnum.objects.filter(id=b).values_list('condmodelnumfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(condmodnum=c)
    d1 = c.first()
    d2 = Equipment2.objects.filter(modelnum=d1).values_list('mfg', flat=True)
    d2a = Equipment2.objects.filter(modelnum=d1).values_list('warr', flat=True)
    d2b = Equipment2.objects.filter(modelnum=d1).values_list('cost', flat=True)
    d3 = SelectedEquip.objects.filter(equipid=1, bidid=a).update(quanity=1, mfg=d2, modelnum=d1, warr=d2a, cost=d2b)
    d4 = Bidding.objects.filter(bidid=aa).update(cost1total=d2b, quanity1=1)
    d5 = TotalJobCost.objects.create(bidid=a, conid=ab, custid=ac, jobcost=d2b, descripid=1)
    e = Equipment2.objects.filter(type='Furnace').annotate(btuA=F('btu'))
    g = list(e.values_list('btu', flat=True).distinct())
    try:
        h = FilterFurnbtu.objects.create(id=1, furnbtufilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterFurnbtu.objects.create(id=2, furnbtufilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterFurnbtu.objects.create(id=3, furnbtufilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterFurnbtu.objects.create(id=4, furnbtufilter=g[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterFurnbtu.objects.create(id=5, furnbtufilter=g[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterFurnbtu.objects.create(id=6, furnbtufilter=g[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterFurnbtu.objects.create(id=7, furnbtufilter=g[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterFurnbtu.objects.create(id=8, furnbtufilter=g[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterFurnbtu.objects.create(id=9, furnbtufilter=g[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterFurnbtu.objects.create(id=10, furnbtufilter=g[9])
    except Exception:
        h9 = 0
    context = {
        "form": form,
        "d": d,
        "d3": d3,
        "d4": d4,
        "d5": d5,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_furnbtu(request):
    a = FilterFurnbtu.objects.all()
    form = EquipmentSelect1(request.POST or None)
    furnbtu = a.values('furnbtufilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "furnbtu": furnbtu,
        "form": form,
    }
    return render(request, 'mha/furnbtu_1.html', context)


def furnbtu(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterFurnConfig.objects.all().delete()
    FilterFurnModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    #    SelectedEquip.objects.filter(equipid=2, bidid=a).delete()
    b = request.POST['id_furnbtu']
    c = FilterFurnbtu.objects.filter(id=b).values_list('furnbtufilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(furnbtu=c, furnconfig='', furneff='', furndescript='',
                                                      furnmodnum='', furnwidth='0.00', furnheight='0.00')
    d1 = EquipSelection.objects.values_list('furnbtu', flat=True).last()
    d2 = FilterFurnModelnum.objects.create(id=1, furnmodelnumfilter="", furnheight=0.00, furnwidth=0.00)
    d3 = SelectedEquip.objects.filter(equipid=2, bidid=a).update(type='Furnace', btu=d1)
    e = Equipment2.objects.filter(type='Furnace', btu=d1).annotate(configA=F('config'))
    g = list(e.values_list('config', flat=True).distinct())
    try:
        h = FilterFurnConfig.objects.create(id=1, furnconfigfilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterFurnConfig.objects.create(id=2, furnconfigfilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterFurnConfig.objects.create(id=3, furnconfigfilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterFurnConfig.objects.create(id=4, furnconfigfilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "d2": d2,
        "d3": d3,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_furnconfig(request):
    a = FilterFurnConfig.objects.all()
    form = EquipmentSelect1(request.POST or None)
    furnconfig = a.values('furnconfigfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "furnconfig": furnconfig,
        "form": form,
    }
    return render(request, 'mha/furnconfig_1.html', context)


def load_furnconfig2(request):
    form = EquipmentSelect2(request.POST or None)
    furnconfig = EquipSelection.objects.values_list('furnconfig', flat=True).last()
    context = {
        "furnconfig": furnconfig,
        "form": form,
    }
    return render(request, 'mha/furnconfig_2.html', context)


def furnconfig(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterFurnEff.objects.all().delete()
    FilterFurnModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_furnconfig']
   # c = FilterFurnConfig.objects.filter(id=b).values_list('furnconfigfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(furnconfig=b, furneff='', furndescript='',
                                                      furnmodnum='', furnwidth='0.00', furnheight='0.00')
    d1 = EquipSelection.objects.values_list('furnbtu', flat=True).last()
    d2 = EquipSelection.objects.values_list('furnconfig', flat=True).last()
    d3 = FilterFurnModelnum.objects.create(id=1, furnmodelnumfilter="", furnheight=0.00, furnwidth=0.00)
    e = Equipment2.objects.filter(type='Furnace', btu=d1, config=d2).annotate(effA=F('eff'))
    g = list(e.values_list('eff', flat=True).distinct())
    try:
        h = FilterFurnEff.objects.create(id=1, furnefffilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterFurnEff.objects.create(id=2, furnefffilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterFurnEff.objects.create(id=3, furnefffilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterFurnEff.objects.create(id=4, furnefffilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "d3": d3,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_furneff(request):
    a = FilterFurnEff.objects.all()
    form = EquipmentSelect1(request.POST or None)
    furneff = a.values('furnefffilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "furneff": furneff,
        "form": form,
    }
    return render(request, 'mha/furneff_1.html', context)


def furneff(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterFurnDescrip.objects.all().delete()
    FilterFurnModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_furneff']
    c = FilterFurnEff.objects.filter(id=b).values_list('furnefffilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(furneff=c, furndescript='',
                                                      furnmodnum='', furnwidth='0.00', furnheight='0.00')
    d1 = EquipSelection.objects.values_list('furnbtu', flat=True).last()
    d2 = EquipSelection.objects.values_list('furnconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('furneff', flat=True).last()
    d4 = FilterFurnModelnum.objects.create(id=1, furnmodelnumfilter="", furnheight=0.00, furnwidth=0.00)
    e = Equipment2.objects.filter(type='Furnace', btu=d1, config=d2, eff=d3).annotate(
        mfgmodeldescripA=F('mfgmodeldescrip'))
    g = list(e.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        h = FilterFurnDescrip.objects.create(id=1, furndescripfilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterFurnDescrip.objects.create(id=2, furndescripfilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterFurnDescrip.objects.create(id=3, furndescripfilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterFurnDescrip.objects.create(id=4, furndescripfilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "d4": d4,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_furndescript(request):
    a = FilterFurnDescrip.objects.all()
    form = EquipmentSelect1(request.POST or None)
    furndescript = a.values('furndescripfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "furndescript": furndescript,
        "form": form,
    }
    return render(request, 'mha/furndescript_1.html', context)


def furndescript(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterFurnModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_furndescript']
    c = FilterFurnDescrip.objects.filter(id=b).values_list('furndescripfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(furndescript=c,
                                                      furnmodnum='', furnwidth='0.00', furnheight='0.00')
    d1 = EquipSelection.objects.values_list('furnbtu', flat=True).last()
    d2 = EquipSelection.objects.values_list('furnconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('furneff', flat=True).last()
    d4 = EquipSelection.objects.values_list('furndescript', flat=True).last()
    #    d5 = SelectedEquip.objects.filter(id=2).update(mfgmodeldescrip=d4)
    e = Equipment2.objects.filter(type='Furnace', btu=d1, config=d2, eff=d3, mfgmodeldescrip=d4).annotate(
        modelnumA=F('modelnum'), heightA=F('height'), widthA=F('width'))
    g = list(e.values_list('modelnum', flat=True).distinct())
    g1 = list(e.values_list('height', flat=True).distinct())
    g2 = list(e.values_list('width', flat=True).distinct())
    try:
        h = FilterFurnModelnum.objects.create(id=1, furnmodelnumfilter=g[0], furnheight=g1[0], furnwidth=g2[0])
    except Exception:
        h = 0
    try:
        h1 = FilterFurnModelnum.objects.create(id=2, furnmodelnumfilter=g[1], furnheight=g1[1], furnwidth=g2[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterFurnModelnum.objects.create(id=3, furnmodelnumfilter=g[2], furnheight=g1[2], furnwidth=g2[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterFurnModelnum.objects.create(id=4, furnmodelnumfilter=g[3], furnheight=g1[3], furnwidth=g2[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        #        "d5": d5,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_furnmodnum(request):
    a = FilterFurnModelnum.objects.all()
    form = EquipmentSelect1(request.POST or None)
    furnmodnum = a.values('furnmodelnumfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "furnmodnum": furnmodnum,
        "form": form,
    }
    return render(request, 'mha/furnmodnum_1.html', context)


def furnmodnum(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    aa = Bidding.objects.values_list('bidid', flat=True).last()
    ab = Bidding.objects.values_list('conid', flat=True).last()
    ac = Bidding.objects.values_list('custid', flat=True).last()
    TotalJobCost.objects.filter(bidid=a, descripid=2).delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_furnmodnum']
    c = FilterFurnModelnum.objects.filter(id=b).values_list('furnmodelnumfilter', flat=True)
    c1 = FilterFurnModelnum.objects.filter(id=b).values_list('furnheight', flat=True)
    c2 = FilterFurnModelnum.objects.filter(id=b).values_list('furnwidth', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(furnmodnum=c, furnheight=c1, furnwidth=c2)
    d1 = c.first()
    d2 = Equipment2.objects.filter(modelnum=d1).values_list('mfg', flat=True)
    d2a = Equipment2.objects.filter(modelnum=d1).values_list('warr', flat=True)
    d2b = Equipment2.objects.filter(modelnum=d1).values_list('cost', flat=True)
    d2c = Equipment2.objects.filter(modelnum=d1).values_list('eff', flat=True)
    d2d = Equipment2.objects.filter(modelnum=d1).values_list('mfgmodeldescrip', flat=True)
    d3 = SelectedEquip.objects.filter(equipid=2, bidid=a).update(quanity=1, eff=d2c, mfg=d2, modelnum=d1,
                                                                 mfgmodeldescrip=d2d, warr=d2a, cost=d2b)
    d4 = Bidding.objects.filter(bidid=aa).update(cost2total=d2b, quanity2=1)
    d5 = TotalJobCost.objects.create(bidid=a, conid=ab, custid=ac, jobcost=d2b, descripid=2)
    context = {
        "form": form,
        "d": d,
        "d3": d3,
        "d4": d4,
        "d5": d5,

    }
    return render(request, 'mha/equipselection1.html', context)


def furnmodnum2A(request, bidid=None):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['id_furnmodnum']
    e = Equipment2.objects.filter(id=d).values_list('modelnum', flat=True)
    f = Equipment2.objects.filter(id=d).values_list('config', flat=True)
    g = Equipment2.objects.filter(id=d).values_list('height', flat=True)
    h = Equipment2.objects.filter(id=d).values_list('width', flat=True)
    i = Equipment2.objects.filter(id=d).values_list('depth', flat=True)
    EquipSelection.objects.filter(id=b).update(furnmodnum=e, furnconfig=f,furnheight=g, furnwidth=h, furndepth=i)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_furnconfig2A(request):
    form = EquipmentSelect2(request.POST or None)
    furnconfig = EquipSelection.objects.values_list('furnconfig', flat=True).last()
    context = {
        "furnconfig": furnconfig,
        "form": form,
    }
    return render(request, 'mha/furnconfig2A_1.html', context)


def load_furnheight2A(request):
    form = EquipmentSelect1(request.POST or None)
    furnheight = EquipSelection.objects.values_list('furnheight', flat=True).last()
    context = {
        "furnheight": furnheight,
        "form": form,
    }
    return render(request, 'mha/furnheight2A_1.html', context)


def load_furnwidth2A(request):
    form = EquipmentSelect1(request.POST or None)
    furnwidth = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    context = {
        "furnwidth": furnwidth,
        "form": form,
    }
    return render(request, 'mha/furnwidth2A_1.html', context)


def load_furndepth2A(request):
    form = EquipmentSelect1(request.POST or None)
    furndepth = EquipSelection.objects.values_list('furndepth', flat=True).last()
    context = {
        "furndepth": furndepth,
        "form": form,
    }
    return render(request, 'mha/furndepth2A_1.html', context)

def furnmodnum2up(request):
    FilterCoilAll.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    a = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    b = Equipment2.objects.filter(type='Evap. Coil', width=a).annotate(configA=F('config'))
    c = list(b.values_list('config', flat=True).exclude(config='Downflow'))
    d = list(b.values_list('btu', flat=True))
    e = list(b.values_list('modelnum', flat=True))
    f = list(b.values_list('mfgmodeldescrip', flat=True))
    g = list(b.values_list('width', flat=True))
    j = list(b.values_list('height', flat=True))
    try:
        h = FilterCoilAll.objects.create(id=1, type='Evap. Coil', coilconfig=c[0], coilbtu=d[0], coilmodnum=e[0], coiltype=f[0], coilwidth=g[0], coilheight=j[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilAll.objects.create(id=2, type='Evap. Coil',  coilconfig=c[1], coilbtu=d[1], coilmodnum=e[1], coiltype=f[1], coilwidth=g[1], coilheight=j[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilAll.objects.create(id=3, type='Evap. Coil',  coilconfig=c[2], coilbtu=d[2], coilmodnum=e[2], coiltype=f[2], coilwidth=g[2], coilheight=j[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilAll.objects.create(id=4, type='Evap. Coil',  coilconfig=c[3], coilbtu=d[3], coilmodnum=e[3], coiltype=f[3], coilwidth=g[3], coilheight=j[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCoilAll.objects.create(id=5, type='Evap. Coil',  coilconfig=c[4], coilbtu=d[4], coilmodnum=e[4], coiltype=f[4], coilwidth=g[4], coilheight=j[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCoilAll.objects.create(id=6, type='Evap. Coil',  coilconfig=c[5], coilbtu=d[5], coilmodnum=e[5], coiltype=f[5], coilwidth=g[5], coilheight=j[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCoilAll.objects.create(id=7, type='Evap. Coil',  coilconfig=c[6], coilbtu=d[6], coilmodnum=e[6], coiltype=f[6], coilwidth=g[6], coilheight=j[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCoilAll.objects.create(id=8, type='Evap. Coil',  coilconfig=c[7], coilbtu=d[7], coilmodnum=e[7], coiltype=f[7], coilwidth=g[7], coilheight=j[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCoilAll.objects.create(id=9, type='Evap. Coil',  coilconfig=c[8], coilbtu=d[8], coilmodnum=e[8], coiltype=f[8], coilwidth=g[8], coilheight=j[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCoilAll.objects.create(id=10, type='Evap. Coil',  coilconfig=c[9], coilbtu=d[9], coilmodnum=e[9], coiltype=f[9], coilwidth=g[9], coilheight=j[9])
    except Exception:
        h9 = 0
    try:
        h10 = FilterCoilAll.objects.create(id=11, type='Evap. Coil',  coilconfig=c[10], coilbtu=d[10], coilmodnum=e[10], coiltype=f[10], coilwidth=g[10], coilheight=j[10])
    except Exception:
        h10 = 0
    try:
        h11 = FilterCoilAll.objects.create(id=12, type='Evap. Coil',  coilconfig=c[11], coilbtu=d[11], coilmodnum=e[11], coiltype=f[11], coilwidth=g[11], coilheight=j[11])
    except Exception:
        h11 = 0

    b1 = Equipment2.objects.filter(type='Evap. Coil', config='Uncased', width__lte=a, ).annotate(
        configA=F('config'))
    c1 = list(b1.values_list('config', flat=True))
    d1 = list(b1.values_list('btu', flat=True))
    e1 = list(b1.values_list('modelnum', flat=True))
    f1 = list(b1.values_list('mfgmodeldescrip', flat=True))
    g1 = list(b1.values_list('width', flat=True))
    j1 = list(b1.values_list('height', flat=True))
    try:
        i = FilterCoilAll.objects.create(id=13, type='Evap. Coil',  coilconfig=c1[0], coilbtu=d1[0], coilmodnum=e1[0], coiltype=f1[0],
                                         coilwidth=g1[0], coilheight=j1[0])
    except Exception:
        i = 0
    try:
        i1 = FilterCoilAll.objects.create(id=14, type='Evap. Coil',  coilconfig=c1[1], coilbtu=d1[1], coilmodnum=e1[1], coiltype=f1[1],
                                          coilwidth=g1[1], coilheight=j1[1])
    except Exception:
        i1 = 0
    try:
        i2 = FilterCoilAll.objects.create(id=15, type='Evap. Coil',  coilconfig=c1[2], coilbtu=d1[2], coilmodnum=e1[2], coiltype=f1[2],
                                          coilwidth=g1[2], coilheight=j1[2])
    except Exception:
        i2 = 0
    try:
        i3 = FilterCoilAll.objects.create(id=16, type='Evap. Coil',  coilconfig=c1[3], coilbtu=d1[3], coilmodnum=e1[3], coiltype=f1[3],
                                          coilwidth=g1[3], coilheight=j1[3])
    except Exception:
        i3 = 0
    try:
        i4 = FilterCoilAll.objects.create(id=17, type='Evap. Coil',  coilconfig=c1[4], coilbtu=d1[4], coilmodnum=e1[4], coiltype=f1[4],
                                          coilwidth=g1[4], coilheight=j1[4])
    except Exception:
        i4 = 0
    try:
        i5 = FilterCoilAll.objects.create(id=18, type='Evap. Coil',  coilconfig=c1[5], coilbtu=d1[5], coilmodnum=e1[5], coiltype=f1[5],
                                          coilwidth=g1[5], coilheight=j1[5])
    except Exception:
        i5 = 0
    try:
        i6 = FilterCoilAll.objects.create(id=19, type='Evap. Coil',  coilconfig=c1[6], coilbtu=d1[6], coilmodnum=e1[6], coiltype=f1[6],
                                          coilwidth=g1[6], coilheight=j1[6])
    except Exception:
        i6 = 0
    try:
        i7 = FilterCoilAll.objects.create(id=20, type='Evap. Coil',  coilconfig=c1[7], coilbtu=d1[7], coilmodnum=e1[7], coiltype=f1[7],
                                          coilwidth=g1[7], coilheight=j1[7])
    except Exception:
        i7 = 0
    try:
        i8 = FilterCoilAll.objects.create(id=21, type='Evap. Coil',  coilconfig=c1[8], coilbtu=d1[8], coilmodnum=e1[8], coiltype=f1[8],
                                          coilwidth=g1[8], coilheight=j1[8])
    except Exception:
        i8 = 0
    try:
        i9 = FilterCoilAll.objects.create(id=22, type='Evap. Coil',  coilconfig=c1[9], coilbtu=d1[9], coilmodnum=e1[9], coiltype=f1[9],
                                          coilwidth=g1[9], coilheight=j1[9])
    except Exception:
        i9 = 0
    try:
        i10 = FilterCoilAll.objects.create(id=23, type='Evap. Coil',  coilconfig=c1[10], coilbtu=d1[10], coilmodnum=e1[10], coiltype=f1[10],
                                           coilwidth=g1[10], coilheight=j1[10])
    except Exception:
        i10 = 0
    try:
        i11 = FilterCoilAll.objects.create(id=24, type='Evap. Coil',  coilconfig=c1[11], coilbtu=d1[11], coilmodnum=e1[11], coiltype=f1[11],
                                           coilwidth=g1[11], coilheight=j1[11])
    except Exception:
            i11 = 0
    FilterCoilConfig.objects.all().delete()
    aa = FilterCoilAll.objects.annotate(coilconfigA=F('coilconfig'))
    bb = list(aa.values_list('coilconfig', flat=True).distinct())
    try:
        j = FilterCoilConfig.objects.create(id=1, coilconfigfilter=bb[0])
    except Exception:
        j = 0
    try:
        j1 = FilterCoilConfig.objects.create(id=2, coilconfigfilter=bb[1])
    except Exception:
        j1 = 0
    try:
        j2 = FilterCoilConfig.objects.create(id=3, coilconfigfilter=bb[2])
    except Exception:
        j2 = 0
    try:
        j3 = FilterCoilConfig.objects.create(id=4, coilconfigfilter=bb[3])
    except Exception:
        j3 = 0
    try:
        j4 = FilterCoilConfig.objects.create(id=5, coilconfigfilter=bb[4])
    except Exception:
        j4 = 0
    try:
        j5 = FilterCoilConfig.objects.create(id=6, coilconfigfilter=bb[5])
    except Exception:
        j5 = 0


    context = {
        "form": form,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "j": j,
        "j1": j1,
        "j2": j2,
        "j3": j3,
        "j4": j4,
        "j5": j5,
        "i": i,
        "i1": i1,
        "i2": i2,
        "i3": i3,
        "i4": i4,
        "i5": i5,
        "i6": i6,
        "i7": i7,
        "i8": i8,
        "i9": i9,
        "i10": i10,
        "i11": i11,

    }
    return render(request, 'mha/equipselection1.html', context)


def furnmodnum2all(request):
    FilterCoilAll.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    a = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    b = Equipment2.objects.filter(type='Evap. Coil', width=a).annotate(configA=F('config'))
    c = list(b.values_list('config', flat=True))
    d = list(b.values_list('btu', flat=True))
    e = list(b.values_list('modelnum', flat=True))
    f = list(b.values_list('mfgmodeldescrip', flat=True))
    g = list(b.values_list('width', flat=True))
    j = list(b.values_list('height', flat=True))
    try:
        h = FilterCoilAll.objects.create(id=1, type='Evap. Coil', coilconfig=c[0], coilbtu=d[0], coilmodnum=e[0], coiltype=f[0], coilwidth=g[0], coilheight=j[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilAll.objects.create(id=2, type='Evap. Coil',  coilconfig=c[1], coilbtu=d[1], coilmodnum=e[1], coiltype=f[1], coilwidth=g[1], coilheight=j[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilAll.objects.create(id=3, type='Evap. Coil',  coilconfig=c[2], coilbtu=d[2], coilmodnum=e[2], coiltype=f[2], coilwidth=g[2], coilheight=j[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilAll.objects.create(id=4, type='Evap. Coil',  coilconfig=c[3], coilbtu=d[3], coilmodnum=e[3], coiltype=f[3], coilwidth=g[3], coilheight=j[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCoilAll.objects.create(id=5, type='Evap. Coil',  coilconfig=c[4], coilbtu=d[4], coilmodnum=e[4], coiltype=f[4], coilwidth=g[4], coilheight=j[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCoilAll.objects.create(id=6, type='Evap. Coil',  coilconfig=c[5], coilbtu=d[5], coilmodnum=e[5], coiltype=f[5], coilwidth=g[5], coilheight=j[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCoilAll.objects.create(id=7, type='Evap. Coil',  coilconfig=c[6], coilbtu=d[6], coilmodnum=e[6], coiltype=f[6], coilwidth=g[6], coilheight=j[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCoilAll.objects.create(id=8, type='Evap. Coil',  coilconfig=c[7], coilbtu=d[7], coilmodnum=e[7], coiltype=f[7], coilwidth=g[7], coilheight=j[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCoilAll.objects.create(id=9, type='Evap. Coil',  coilconfig=c[8], coilbtu=d[8], coilmodnum=e[8], coiltype=f[8], coilwidth=g[8], coilheight=j[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCoilAll.objects.create(id=10, type='Evap. Coil',  coilconfig=c[9], coilbtu=d[9], coilmodnum=e[9], coiltype=f[9], coilwidth=g[9], coilheight=j[9])
    except Exception:
        h9 = 0
    try:
        h10 = FilterCoilAll.objects.create(id=11, type='Evap. Coil',  coilconfig=c[10], coilbtu=d[10], coilmodnum=e[10], coiltype=f[10], coilwidth=g[10], coilheight=j[10])
    except Exception:
        h10 = 0
    try:
        h11 = FilterCoilAll.objects.create(id=12, type='Evap. Coil',  coilconfig=c[11], coilbtu=d[11], coilmodnum=e[11], coiltype=f[11], coilwidth=g[11], coilheight=j[11])
    except Exception:
        h11 = 0
    try:
        h12 = FilterCoilAll.objects.create(id=13, type='Evap. Coil', coilconfig=c[12], coilbtu=d[12], coilmodnum=e[12],
                                         coiltype=f[12], coilwidth=g[12], coilheight=j[12])
    except Exception:
        h12 = 0
    try:
        h13 = FilterCoilAll.objects.create(id=14, type='Evap. Coil', coilconfig=c[13], coilbtu=d[13], coilmodnum=e[13],
                                          coiltype=f[13], coilwidth=g[13], coilheight=j[13])
    except Exception:
        h13 = 0
    try:
        h14 = FilterCoilAll.objects.create(id=15, type='Evap. Coil', coilconfig=c[14], coilbtu=d[14], coilmodnum=e[14],
                                          coiltype=f[14], coilwidth=g[14], coilheight=j[14])
    except Exception:
        h14 = 0
    try:
        h15 = FilterCoilAll.objects.create(id=16, type='Evap. Coil', coilconfig=c[15], coilbtu=d[15], coilmodnum=e[15],
                                          coiltype=f[15], coilwidth=g[15], coilheight=j[15])
    except Exception:
        h15 = 0
    try:
        h16 = FilterCoilAll.objects.create(id=17, type='Evap. Coil', coilconfig=c[16], coilbtu=d[16], coilmodnum=e[16],
                                          coiltype=f[16], coilwidth=g[16], coilheight=j[16])
    except Exception:
        h16 = 0
    try:
        h17 = FilterCoilAll.objects.create(id=17, type='Evap. Coil', coilconfig=c[17], coilbtu=d[17], coilmodnum=e[17],
                                          coiltype=f[17], coilwidth=g[17], coilheight=j[17])
    except Exception:
        h17 = 0
    try:
        h18 = FilterCoilAll.objects.create(id=18, type='Evap. Coil', coilconfig=c[18], coilbtu=d[18], coilmodnum=e[18],
                                          coiltype=f[18], coilwidth=g[18], coilheight=j[18])
    except Exception:
        h18 = 0
    try:
        h19 = FilterCoilAll.objects.create(id=18, type='Evap. Coil', coilconfig=c[19], coilbtu=d[19], coilmodnum=e[19],
                                          coiltype=f[19], coilwidth=g[19], coilheight=j[19])
    except Exception:
        h19 = 0
    try:
        h20 = FilterCoilAll.objects.create(id=19, type='Evap. Coil', coilconfig=c[20], coilbtu=d[20], coilmodnum=e[20],
                                          coiltype=f[20], coilwidth=g[20], coilheight=j[20])
    except Exception:
        h20 = 0
    try:
        h21 = FilterCoilAll.objects.create(id=20, type='Evap. Coil', coilconfig=c[21], coilbtu=d[21], coilmodnum=e[21],
                                          coiltype=f[21], coilwidth=g[21], coilheight=j[21])
    except Exception:
        h21 = 0
    try:
        h22 = FilterCoilAll.objects.create(id=21, type='Evap. Coil', coilconfig=c[22], coilbtu=d[22], coilmodnum=e[22],
                                           coiltype=f[22], coilwidth=g[22], coilheight=j[22])
    except Exception:
        h22 = 0
    try:
        h23 = FilterCoilAll.objects.create(id=22, type='Evap. Coil', coilconfig=c[23], coilbtu=d[23], coilmodnum=e[23],
                                           coiltype=f[23], coilwidth=g[23], coilheight=j[23])
    except Exception:
        h23 = 0

    b1 = Equipment2.objects.filter(type='Evap. Coil', config='Uncased', width__lte=a, ).annotate(
        configA=F('config'))
    c1 = list(b1.values_list('config', flat=True))
    d1 = list(b1.values_list('btu', flat=True))
    e1 = list(b1.values_list('modelnum', flat=True))
    f1 = list(b1.values_list('mfgmodeldescrip', flat=True))
    g1 = list(b1.values_list('width', flat=True))
    j1 = list(b1.values_list('height', flat=True))
    try:
        i = FilterCoilAll.objects.create(id=13, type='Evap. Coil',  coilconfig=c1[0], coilbtu=d1[0], coilmodnum=e1[0], coiltype=f1[0],
                                         coilwidth=g1[0], coilheight=j1[0])
    except Exception:
        i = 0
    try:
        i1 = FilterCoilAll.objects.create(id=14, type='Evap. Coil',  coilconfig=c1[1], coilbtu=d1[1], coilmodnum=e1[1], coiltype=f1[1],
                                          coilwidth=g1[1], coilheight=j1[1])
    except Exception:
        i1 = 0
    try:
        i2 = FilterCoilAll.objects.create(id=15, type='Evap. Coil',  coilconfig=c1[2], coilbtu=d1[2], coilmodnum=e1[2], coiltype=f1[2],
                                          coilwidth=g1[2], coilheight=j1[2])
    except Exception:
        i2 = 0
    try:
        i3 = FilterCoilAll.objects.create(id=16, type='Evap. Coil',  coilconfig=c1[3], coilbtu=d1[3], coilmodnum=e1[3], coiltype=f1[3],
                                          coilwidth=g1[3], coilheight=j1[3])
    except Exception:
        i3 = 0
    try:
        i4 = FilterCoilAll.objects.create(id=17, type='Evap. Coil',  coilconfig=c1[4], coilbtu=d1[4], coilmodnum=e1[4], coiltype=f1[4],
                                          coilwidth=g1[4], coilheight=j1[4])
    except Exception:
        i4 = 0
    try:
        i5 = FilterCoilAll.objects.create(id=18, type='Evap. Coil',  coilconfig=c1[5], coilbtu=d1[5], coilmodnum=e1[5], coiltype=f1[5],
                                          coilwidth=g1[5], coilheight=j1[5])
    except Exception:
        i5 = 0
    try:
        i6 = FilterCoilAll.objects.create(id=19, type='Evap. Coil',  coilconfig=c1[6], coilbtu=d1[6], coilmodnum=e1[6], coiltype=f1[6],
                                          coilwidth=g1[6], coilheight=j1[6])
    except Exception:
        i6 = 0
    try:
        i7 = FilterCoilAll.objects.create(id=20, type='Evap. Coil',  coilconfig=c1[7], coilbtu=d1[7], coilmodnum=e1[7], coiltype=f1[7],
                                          coilwidth=g1[7], coilheight=j1[7])
    except Exception:
        i7 = 0
    try:
        i8 = FilterCoilAll.objects.create(id=21, type='Evap. Coil',  coilconfig=c1[8], coilbtu=d1[8], coilmodnum=e1[8], coiltype=f1[8],
                                          coilwidth=g1[8], coilheight=j1[8])
    except Exception:
        i8 = 0
    try:
        i9 = FilterCoilAll.objects.create(id=22, type='Evap. Coil',  coilconfig=c1[9], coilbtu=d1[9], coilmodnum=e1[9], coiltype=f1[9],
                                          coilwidth=g1[9], coilheight=j1[9])
    except Exception:
        i9 = 0
    try:
        i10 = FilterCoilAll.objects.create(id=23, type='Evap. Coil',  coilconfig=c1[10], coilbtu=d1[10], coilmodnum=e1[10], coiltype=f1[10],
                                           coilwidth=g1[10], coilheight=j1[10])
    except Exception:
        i10 = 0
    try:
        i11 = FilterCoilAll.objects.create(id=24, type='Evap. Coil',  coilconfig=c1[11], coilbtu=d1[11], coilmodnum=e1[11], coiltype=f1[11],
                                           coilwidth=g1[11], coilheight=j1[11])
    except Exception:
            i11 = 0
    FilterCoilConfig.objects.all().delete()
    aa = FilterCoilAll.objects.annotate(coilconfigA=F('coilconfig'))
    bb = list(aa.values_list('coilconfig', flat=True).distinct())
    try:
        j = FilterCoilConfig.objects.create(id=1, coilconfigfilter=bb[0])
    except Exception:
        j = 0
    try:
        j1 = FilterCoilConfig.objects.create(id=2, coilconfigfilter=bb[1])
    except Exception:
        j1 = 0
    try:
        j2 = FilterCoilConfig.objects.create(id=3, coilconfigfilter=bb[2])
    except Exception:
        j2 = 0
    try:
        j3 = FilterCoilConfig.objects.create(id=4, coilconfigfilter=bb[3])
    except Exception:
        j3 = 0
    try:
        j4 = FilterCoilConfig.objects.create(id=5, coilconfigfilter=bb[4])
    except Exception:
        j4 = 0
    try:
        j5 = FilterCoilConfig.objects.create(id=6, coilconfigfilter=bb[5])
    except Exception:
        j5 = 0


    context = {
        "form": form,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "j": j,
        "j1": j1,
        "j2": j2,
        "j3": j3,
        "j4": j4,
        "j5": j5,
        "i": i,
        "i1": i1,
        "i2": i2,
        "i3": i3,
        "i4": i4,
        "i5": i5,
        "i6": i6,
        "i7": i7,
        "i8": i8,
        "i9": i9,
        "i10": i10,
        "i11": i11,

    }
    return render(request, 'mha/equipselection1.html', context)



def furnmodnum2down(request):
    FilterCoilAll.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    a = EquipSelection.objects.values_list('furnwidth', flat=True).last()
    b = Equipment2.objects.filter(type='Evap. Coil', width=a).annotate(configA=F('config'))
    c = list(b.values_list('config', flat=True).exclude(config='Upflow'))
    d = list(b.values_list('btu', flat=True))
    e = list(b.values_list('modelnum', flat=True))
    f = list(b.values_list('mfgmodeldescrip', flat=True))
    g = list(b.values_list('width', flat=True))
    j = list(b.values_list('height', flat=True))
    try:
        h = FilterCoilAll.objects.create(id=1, type='Evap. Coil', coilconfig=c[0], coilbtu=d[0], coilmodnum=e[0], coiltype=f[0], coilwidth=g[0], coilheight=j[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilAll.objects.create(id=2, type='Evap. Coil',  coilconfig=c[1], coilbtu=d[1], coilmodnum=e[1], coiltype=f[1], coilwidth=g[1], coilheight=j[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilAll.objects.create(id=3, type='Evap. Coil',  coilconfig=c[2], coilbtu=d[2], coilmodnum=e[2], coiltype=f[2], coilwidth=g[2], coilheight=j[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilAll.objects.create(id=4, type='Evap. Coil',  coilconfig=c[3], coilbtu=d[3], coilmodnum=e[3], coiltype=f[3], coilwidth=g[3], coilheight=j[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterCoilAll.objects.create(id=5, type='Evap. Coil',  coilconfig=c[4], coilbtu=d[4], coilmodnum=e[4], coiltype=f[4], coilwidth=g[4], coilheight=j[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterCoilAll.objects.create(id=6, type='Evap. Coil',  coilconfig=c[5], coilbtu=d[5], coilmodnum=e[5], coiltype=f[5], coilwidth=g[5], coilheight=j[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterCoilAll.objects.create(id=7, type='Evap. Coil',  coilconfig=c[6], coilbtu=d[6], coilmodnum=e[6], coiltype=f[6], coilwidth=g[6], coilheight=j[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterCoilAll.objects.create(id=8, type='Evap. Coil',  coilconfig=c[7], coilbtu=d[7], coilmodnum=e[7], coiltype=f[7], coilwidth=g[7], coilheight=j[7])
    except Exception:
        h7 = 0
    try:
        h8 = FilterCoilAll.objects.create(id=9, type='Evap. Coil',  coilconfig=c[8], coilbtu=d[8], coilmodnum=e[8], coiltype=f[8], coilwidth=g[8], coilheight=j[8])
    except Exception:
        h8 = 0
    try:
        h9 = FilterCoilAll.objects.create(id=10, type='Evap. Coil',  coilconfig=c[9], coilbtu=d[9], coilmodnum=e[9], coiltype=f[9], coilwidth=g[9], coilheight=j[9])
    except Exception:
        h9 = 0
    try:
        h10 = FilterCoilAll.objects.create(id=11, type='Evap. Coil',  coilconfig=c[10], coilbtu=d[10], coilmodnum=e[10], coiltype=f[10], coilwidth=g[10], coilheight=j[10])
    except Exception:
        h10 = 0
    try:
        h11 = FilterCoilAll.objects.create(id=12, type='Evap. Coil',  coilconfig=c[11], coilbtu=d[11], coilmodnum=e[11], coiltype=f[11], coilwidth=g[11], coilheight=j[11])
    except Exception:
        h11 = 0

    b1 = Equipment2.objects.filter(type='Evap. Coil', config='Uncased', width__lte=a, ).annotate(
        configA=F('config'))
    c1 = list(b1.values_list('config', flat=True))
    d1 = list(b1.values_list('btu', flat=True))
    e1 = list(b1.values_list('modelnum', flat=True))
    f1 = list(b1.values_list('mfgmodeldescrip', flat=True))
    g1 = list(b1.values_list('width', flat=True))
    j1 = list(b1.values_list('height', flat=True))
    try:
        i = FilterCoilAll.objects.create(id=13, type='Evap. Coil',  coilconfig=c1[0], coilbtu=d1[0], coilmodnum=e1[0], coiltype=f1[0],
                                         coilwidth=g1[0], coilheight=j1[0])
    except Exception:
        i = 0
    try:
        i1 = FilterCoilAll.objects.create(id=14, type='Evap. Coil',  coilconfig=c1[1], coilbtu=d1[1], coilmodnum=e1[1], coiltype=f1[1],
                                          coilwidth=g1[1], coilheight=j1[1])
    except Exception:
        i1 = 0
    try:
        i2 = FilterCoilAll.objects.create(id=15, type='Evap. Coil',  coilconfig=c1[2], coilbtu=d1[2], coilmodnum=e1[2], coiltype=f1[2],
                                          coilwidth=g1[2], coilheight=j1[2])
    except Exception:
        i2 = 0
    try:
        i3 = FilterCoilAll.objects.create(id=16, type='Evap. Coil',  coilconfig=c1[3], coilbtu=d1[3], coilmodnum=e1[3], coiltype=f1[3],
                                          coilwidth=g1[3], coilheight=j1[3])
    except Exception:
        i3 = 0
    try:
        i4 = FilterCoilAll.objects.create(id=17, type='Evap. Coil',  coilconfig=c1[4], coilbtu=d1[4], coilmodnum=e1[4], coiltype=f1[4],
                                          coilwidth=g1[4], coilheight=j1[4])
    except Exception:
        i4 = 0
    try:
        i5 = FilterCoilAll.objects.create(id=18, type='Evap. Coil',  coilconfig=c1[5], coilbtu=d1[5], coilmodnum=e1[5], coiltype=f1[5],
                                          coilwidth=g1[5], coilheight=j1[5])
    except Exception:
        i5 = 0
    try:
        i6 = FilterCoilAll.objects.create(id=19, type='Evap. Coil',  coilconfig=c1[6], coilbtu=d1[6], coilmodnum=e1[6], coiltype=f1[6],
                                          coilwidth=g1[6], coilheight=j1[6])
    except Exception:
        i6 = 0
    try:
        i7 = FilterCoilAll.objects.create(id=20, type='Evap. Coil',  coilconfig=c1[7], coilbtu=d1[7], coilmodnum=e1[7], coiltype=f1[7],
                                          coilwidth=g1[7], coilheight=j1[7])
    except Exception:
        i7 = 0
    try:
        i8 = FilterCoilAll.objects.create(id=21, type='Evap. Coil',  coilconfig=c1[8], coilbtu=d1[8], coilmodnum=e1[8], coiltype=f1[8],
                                          coilwidth=g1[8], coilheight=j1[8])
    except Exception:
        i8 = 0
    try:
        i9 = FilterCoilAll.objects.create(id=22, type='Evap. Coil',  coilconfig=c1[9], coilbtu=d1[9], coilmodnum=e1[9], coiltype=f1[9],
                                          coilwidth=g1[9], coilheight=j1[9])
    except Exception:
        i9 = 0
    try:
        i10 = FilterCoilAll.objects.create(id=23, type='Evap. Coil',  coilconfig=c1[10], coilbtu=d1[10], coilmodnum=e1[10], coiltype=f1[10],
                                           coilwidth=g1[10], coilheight=j1[10])
    except Exception:
        i10 = 0
    try:
        i11 = FilterCoilAll.objects.create(id=24, type='Evap. Coil',  coilconfig=c1[11], coilbtu=d1[11], coilmodnum=e1[11], coiltype=f1[11],
                                           coilwidth=g1[11], coilheight=j1[11])
    except Exception:
            i11 = 0
    FilterCoilConfig.objects.all().delete()
    aa = FilterCoilAll.objects.annotate(coilconfigA=F('coilconfig'))
    bb = list(aa.values_list('coilconfig', flat=True).distinct())
    try:
        j = FilterCoilConfig.objects.create(id=1, coilconfigfilter=bb[0])
    except Exception:
        j = 0
    try:
        j1 = FilterCoilConfig.objects.create(id=2, coilconfigfilter=bb[1])
    except Exception:
        j1 = 0
    try:
        j2 = FilterCoilConfig.objects.create(id=3, coilconfigfilter=bb[2])
    except Exception:
        j2 = 0
    try:
        j3 = FilterCoilConfig.objects.create(id=4, coilconfigfilter=bb[3])
    except Exception:
        j3 = 0
    try:
        j4 = FilterCoilConfig.objects.create(id=5, coilconfigfilter=bb[4])
    except Exception:
        j4 = 0
    try:
        j5 = FilterCoilConfig.objects.create(id=6, coilconfigfilter=bb[5])
    except Exception:
        j5 = 0


    context = {
        "form": form,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "h5": h5,
        "h6": h6,
        "h7": h7,
        "h8": h8,
        "h9": h9,
        "h10": h10,
        "h11": h11,
        "j": j,
        "j1": j1,
        "j2": j2,
        "j3": j3,
        "j4": j4,
        "j5": j5,
        "i": i,
        "i1": i1,
        "i2": i2,
        "i3": i3,
        "i4": i4,
        "i5": i5,
        "i6": i6,
        "i7": i7,
        "i8": i8,
        "i9": i9,
        "i10": i10,
        "i11": i11,

    }
    return render(request, 'mha/equipselection1.html', context)




def load_furnmodnum2(request):
    form = EquipmentSelect1(request.POST or None)
    furnmodnum = EquipSelection.objects.values_list('furnmodnum', flat=True).last()
    context = {
        "furnmodnum": furnmodnum,
        "form": form,
    }
    return render(request, 'mha/furnmodnum_2.html', context)


def load_furnheight(request):
    form = EquipmentSelect1(request.POST or None)
    furnheight = EquipSelection.objects.values_list('furnheight', flat=True).last()
    context = {
        "furnheight": furnheight,
        "form": form,
    }
    return render(request, 'mha/furnheight_1.html', context)


def load_plenumheight(request):
    form = EquipmentSelect1(request.POST or None)
    plenumheight = EquipSelection.objects.values_list('plenumheight', flat=True).last()
    context = {
        "plenumheight": plenumheight,
        "form": form,
    }
    return render(request, 'mha/plenumheight_1.html', context)


def plenumheight(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['plenumheight_id']
    EquipSelection.objects.filter(id=b).update(plenumheight=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_plenumwidth(request):
    form = EquipmentSelect1(request.POST or None)
    plenumwidth = EquipSelection.objects.values_list('plenumwidth', flat=True).last()
    context = {
        "plenumwidth": plenumwidth,
        "form": form,
    }
    return render(request, 'mha/plenumwidth_1.html', context)


def plenumwidth(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['id_plenumwidth']
    e = FilterPlenumWidth.objects.filter(id=d).values_list('furnplenumwidth', flat=True)
    EquipSelection.objects.filter(id=b).update(plenumwidth=e)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_plenumdepth(request):
    form = EquipmentSelect1(request.POST or None)
    plenumdepth = EquipSelection.objects.values_list('plenumdepth', flat=True).last()
    context = {
        "plenumdepth": plenumdepth,
        "form": form,
    }
    return render(request, 'mha/plenumdepth_1.html', context)


def plenumdepth(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['plenumdepth_id']
    EquipSelection.objects.filter(id=b).update(plenumdepth=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)





def existfurnheight(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['existfurnheight_id']
    EquipSelection.objects.filter(id=b).update(existfurnheight=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_existfurnheight(request):
    form = EquipmentSelect1(request.POST or None)
    existfurnheight = EquipSelection.objects.values_list('existfurnheight', flat=True).last()
    context = {
        "existfurnheight": existfurnheight,
        "form": form,
    }
    return render(request, 'mha/existfurnheight_1.html', context)


def existfurnwidth(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['id_existfurnwidth']
    e = FilterPlenumWidth.objects.filter(id=d).values_list('furnplenumwidth', flat=True)
    EquipSelection.objects.filter(id=b).update(existfurnwidth=e)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def existfurndepth(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['existfurndepth_id']
    EquipSelection.objects.filter(id=b).update(existfurndepth=d)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)


def load_existfurndepth(request):
    form = EquipmentSelect1(request.POST or None)
    existfurndepth = EquipSelection.objects.values_list('existfurndepth', flat=True).last()
    context = {
        "existfurndepth": existfurndepth,
        "form": form,
    }
    return render(request, 'mha/existfurndepth_1.html', context)


def existfurnconfig(request):
    form = EquipmentSelect1(request.POST)
    b = EquipSelection.objects.values_list('id', flat=True).last()
    d = request.POST['id_existfurnconfig']
    e = ExistFurnConfig.objects.filter(id=d).values_list('furnconfig', flat=True)
    EquipSelection.objects.filter(id=b).update(existfurnconfig=e)
    context = {
        "form": form,
    }
    return render(request, 'mha/equipselection2A.html', context)




def load_coiltype(request):
    a = FilterCoilAll.objects.all()
    form = EquipmentSelect1(request.POST or None)
    coiltype = a.values('coiltype')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "coiltype": coiltype,
        "form": form,
    }
    return render(request, 'mha/coiltype_1.html', context)


def coiltype(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterCoilModelnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    #    SelectedEquip.objects.filter(equipid=3, bidid=a).delete()
    b = request.POST['id_coiltype']
    c = FilterCoiltype.objects.filter(id=b).values_list('coiltypefilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(coiltype=c, coilwidth=0.00, coilheight=0.00, furncoilheight=0.00)
    d1 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    d2 = EquipSelection.objects.values_list('coilbtu', flat=True).last()
    d3 = EquipSelection.objects.values_list('coiltype', flat=True).last()
    d4 = SelectedEquip.objects.filter(equipid=3, bidid=a).update(type='Evap. Coil')

    e = FilterCoilAll.objects.filter(type='Evap. Coil', coilconfig=d1, coilbtu=d2).annotate(coilmodnumA=F('coilmodnum'))
    g = list(e.values_list('coilmodnum', flat=True).distinct())
    g1 = list(e.values_list('coilwidth', flat=True).distinct())
    g2 = list(e.values_list('coilheight', flat=True).distinct())
    try:
        h = FilterCoilModelnum.objects.create(id=1, coilmodelnumfilter=g[0], coilwidth=g1[0], coilheight=g2[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilModelnum.objects.create(id=2, coilmodelnumfilter=g[1], coilwidth=g1[1], coilheight=g2[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilModelnum.objects.create(id=3, coilmodelnumfilter=g[2], coilwidth=g1[2], coilheight=g2[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilModelnum.objects.create(id=4, coilmodelnumfilter=g[3], coilwidth=g1[3], coilheight=g2[3])
    except Exception:
        h3 = 0

    context = {
        "form": form,
        "d": d,
        "d2": d2,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,

    }
    return render(request, 'mha/equipselection1.html', context)



def load_coilconfig(request):
    a = FilterCoilConfig.objects.all()
    form = EquipmentSelect1(request.POST or None)
    coilconfig = a.values('coilconfigfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "coilconfig": coilconfig,
        "form": form,
    }
    return render(request, 'mha/coilconfig_1.html', context)



def coilconfig(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    FilterCoilbtu.objects.all().delete()
    b = request.POST['id_coilconfig']
    c = FilterCoilConfig.objects.filter(id=b).values_list('coilconfigfilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(coilconfig=c, coilwidth='0.00',
                                                      coilheight='0.00', furncoilheight='0.00')
    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    e = FilterCoilAll.objects.filter(coilconfig=d2).annotate(coilbtuA=F('coilbtu'))
    g = list(e.values_list('coilbtu', flat=True).distinct())
    try:
        h = FilterCoilbtu.objects.create(id=1, coilbtufilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoilbtu.objects.create(id=2, coilbtufilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoilbtu.objects.create(id=3, coilbtufilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoilbtu.objects.create(id=4, coilbtufilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_coilbtu(request):
    a = FilterCoilbtu.objects.all()
    form = EquipmentSelect1(request.POST or None)
    coilbtu = a.values('coilbtufilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "coilbtu": coilbtu,
        "form": form,
    }
    return render(request, 'mha/coilbtu_1.html', context)


def coilbtu(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    FilterCoiltype.objects.all().delete()
    b = request.POST['id_coilbtu']
    c = FilterCoilbtu.objects.filter(id=b).values_list('coilbtufilter', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(coilbtu=c, coilwidth=0.00, coilheight=0.00, furncoilheight=0.00)
    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
    d3 = EquipSelection.objects.values_list('coilbtu', flat=True).last()

    e = FilterCoilAll.objects.filter(coilconfig=d2, coilbtu=d3).annotate(coiltypeA=F('coiltype'))
    g = list(e.values_list('coiltype', flat=True).distinct())
    try:
        h = FilterCoiltype.objects.create(id=1, coiltypefilter=g[0])
    except Exception:
        h = 0
    try:
        h1 = FilterCoiltype.objects.create(id=2, coiltypefilter=g[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterCoiltype.objects.create(id=3, coiltypefilter=g[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterCoiltype.objects.create(id=4, coiltypefilter=g[3])
    except Exception:
        h3 = 0
    context = {
        "form": form,
        "d": d,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,

    }
    return render(request, 'mha/equipselection1.html', context)




#def coilbtu(request):
#    a = EquipSelection.objects.values_list('bidid', flat=True).last()
#    FilterCoilModelnum.objects.all().delete()
#    form = EquipmentSelect1(request.POST)
#    b = request.POST['id_coilbtu']
#    c = FilterCoilAll.objects.filter(id=b).values_list('coilbtu', flat=True)
#    d = EquipSelection.objects.filter(bidid=a).update(coilbtu=c, coilwidth=0.00, coilheight=0.00, furncoilheight=0.00)
#    d1 = EquipSelection.objects.values_list('coiltype', flat=True).last()
#    d2 = EquipSelection.objects.values_list('coilconfig', flat=True).last()
#    d3 = EquipSelection.objects.values_list('coilbtu', flat=True).last()
#
#    e = FilterCoilAll.objects.filter(coilconfig=d2, coilbtu=d3).annotate(coiltypeA=F('coiltype'))
#    g = list(e.values_list('coilmodnum', flat=True).distinct())
#    g1 = list(e.values_list('coilheight', flat=True).distinct())
#    g2 = list(e.values_list('coilwidth', flat=True).distinct())
#    try:
#        h = FilterCoilModelnum.objects.create(id=1, coilmodelnumfilter=g[0], coilwidth=g1[0], coilheight=g2[0])
#    except Exception:
#        h = 0
#    try:
#        h1 = FilterCoilModelnum.objects.create(id=2, coilmodelnumfilter=g[1], coilwidth=g1[1], coilheight=g2[1])
#    except Exception:
#        h1 = 0
#    try:
#        h2 = FilterCoilModelnum.objects.create(id=3, coilmodelnumfilter=g[2], coilwidth=g1[2], coilheight=g2[2])
#    except Exception:
#        h2 = 0
#    try:
#        h3 = FilterCoilModelnum.objects.create(id=4, coilmodelnumfilter=g[3], coilwidth=g1[3], coilheight=g2[3])
#    except Exception:
#        h3 = 0
#    context = {
#        "form": form,
#        "d": d,
#
#    }
#    return render(request, 'mha/equipselection1.html', context)


def load_coilmodnum(request):
    a = FilterCoilModelnum.objects.all()
    form = EquipmentSelect1(request.POST or None)
    coilmodnum = a.values('coilmodelnumfilter')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "coilmodnum": coilmodnum,
        "form": form,
    }
    return render(request, 'mha/coilmodnum_1.html', context)


def coilmodnum(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    aa = Bidding.objects.values_list('bidid', flat=True).last()
    ab = Bidding.objects.values_list('conid', flat=True).last()
    ac = Bidding.objects.values_list('custid', flat=True).last()
    FilterThermostat.objects.all().delete()
    #    TotalJobCost.objects.filter(bidid=a, descripid=3).delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_coilmodnum']
    c = FilterCoilModelnum.objects.filter(id=b).values_list('coilmodelnumfilter', flat=True)
    c1 = FilterCoilModelnum.objects.filter(id=b).values_list('coilheight', flat=True)
    c2 = FilterCoilModelnum.objects.filter(id=b).values_list('coilwidth', flat=True)
    d = EquipSelection.objects.filter(bidid=a).update(coilmodnum=c, coilheight=c1, coilwidth=c2)

    d1 = c.first()
    d2 = Equipment2.objects.filter(modelnum=d1).values_list('mfg', flat=True)
    d2a = Equipment2.objects.filter(modelnum=d1).values_list('warr', flat=True)
    d2b = Equipment2.objects.filter(modelnum=d1).values_list('cost', flat=True)
    d2c = Equipment2.objects.filter(modelnum=d1).values_list('eff', flat=True)
    d2d = Equipment2.objects.filter(modelnum=d1).values_list('btu', flat=True)
    d2e = Equipment2.objects.filter(modelnum=d1).values_list('mfgmodeldescrip', flat=True)
    d3 = SelectedEquip.objects.filter(equipid=3, bidid=a).update(quanity=1, eff=d2c, mfg=d2, modelnum=d1,
                                                                 mfgmodeldescrip=d2e, btu=d2d, warr=d2a, cost=d2b)
    d4 = Bidding.objects.filter(bidid=aa).update(cost3total=d2b, quanity3=1)
    d5 = TotalJobCost.objects.create(bidid=a, conid=ab, custid=ac, jobcost=d2b, descripid=3)

    e = EquipSelection.objects.values_list('furnheight', flat=True).last()
    f = EquipSelection.objects.values_list('coilheight', flat=True).last()
    g = e + f
    h = EquipSelection.objects.filter(bidid=a).update(furncoilheight=g)

    j = Equipment2.objects.filter(type='Thermostat').annotate(modelnumA=F('modelnum'))
    j1 = list(j.values_list('mfg', flat=True).distinct())
    try:
        k = FilterThermostat.objects.create(id=1, thermomfg=j1[0])
    except Exception:
        k = 0
    try:
        k1 = FilterThermostat.objects.create(id=2, thermomfg=j1[1])
    except Exception:
        k1 = 0
    try:
        k2 = FilterThermostat.objects.create(id=3, thermomfg=j1[2])
    except Exception:
        k2 = 0
    try:
        k3 = FilterThermostat.objects.create(id=4, thermomfg=j1[3])
    except Exception:
        k3 = 0
    try:
        k4 = FilterThermostat.objects.create(id=5, thermomfg=j1[4])
    except Exception:
        k4 = 0
    try:
        k5 = FilterThermostat.objects.create(id=6, thermomfg=j1[5])
    except Exception:
        k5 = 0
    try:
        k6 = FilterThermostat.objects.create(id=7, thermomfg=j1[6])
    except Exception:
        k6 = 0
    try:
        k7 = FilterThermostat.objects.create(id=8, thermomfg=j1[7])
    except Exception:
        k7 = 0

    context = {
        "form": form,
        "d": d,
        "d3": d3,
        "d4": d4,
        "d5": d5,
        "h": h,
        "k": k,
        "k1": k1,
        "k2": k2,
        "k3": k3,
        "k4": k4,
        "k5": k5,
        "k6": k6,
        "k7": k7,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_coilheight(request):
    form = EquipmentSelect1(request.POST or None)
    coilheight = EquipSelection.objects.values_list('coilheight', flat=True).last()
    context = {
        "coilheight": coilheight,
        "form": form,
    }
    return render(request, 'mha/coilheight_1.html', context)





def furncoilheight(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    form = EquipmentSelect1(request.POST)
    c = EquipSelection.objects.values_list('furnheight', flat=True).last()
    c1 = EquipSelection.objects.values_list('coilheight', flat=True).last()
    c2 = c + c1
    d = EquipSelection.objects.filter(bidid=a).update(furncoilheight=c2)
    context = {
        "form": form,
        "d": d,

    }
    return render(request, 'mha/equipselection1.html', context)





def load_thermomfg(request):
    a = FilterThermostat.objects.all()
    form = EquipmentSelect1(request.POST or None)
    thermomfg = a.values('thermomfg')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "thermomfg": thermomfg,
        "form": form,
    }
    return render(request, 'mha/thermomfg_1.html', context)


def thermomfg(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    FilterThermostatModnum.objects.all().delete()
    form = EquipmentSelect1(request.POST)
    #    SelectedEquip.objects.filter(equipid=4, bidid=a).delete()
    b = request.POST['id_thermostat']
    c = FilterThermostat.objects.filter(id=b).values_list('thermomfg')
    d = EquipSelection.objects.filter(bidid=a).update(thermostat=c)
    d1 = EquipSelection.objects.values_list('thermostat', flat=True).last()
    d3 = SelectedEquip.objects.filter(equipid=4, bidid=a).update(type='Thermostat', mfg=d1)

    e = Equipment2.objects.filter(mfg=d1, type='Thermostat').annotate(modelnumA=F('modelnum'))
    g = list(e.values_list('modelnum', flat=True).distinct())
    gg = list(e.values_list('smart', flat=True))
    try:
        h = FilterThermostatModnum.objects.create(id=1, thermomodnum=g[0], smart=gg[0])
    except Exception:
        h = 0
    try:
        h1 = FilterThermostatModnum.objects.create(id=2, thermomodnum=g[1], smart=gg[1])
    except Exception:
        h1 = 0
    try:
        h2 = FilterThermostatModnum.objects.create(id=3, thermomodnum=g[2], smart=gg[2])
    except Exception:
        h2 = 0
    try:
        h3 = FilterThermostatModnum.objects.create(id=4, thermomodnum=g[3], smart=gg[3])
    except Exception:
        h3 = 0
    try:
        h4 = FilterThermostatModnum.objects.create(id=5, thermomodnum=g[4], smart=gg[4])
    except Exception:
        h4 = 0
    try:
        h5 = FilterThermostatModnum.objects.create(id=6, thermomodnum=g[5], smart=gg[5])
    except Exception:
        h5 = 0
    try:
        h6 = FilterThermostatModnum.objects.create(id=3, thermomodnum=g[6], smart=gg[6])
    except Exception:
        h6 = 0
    try:
        h7 = FilterThermostatModnum.objects.create(id=4, thermomodnum=g[7], smart=gg[7])
    except Exception:
        h7 = 0

    context = {
        "form": form,
        "d": d,
        "d3": d3,
        "h": h,
        "h1": h1,
        "h2": h2,
        "h3": h3,

    }
    return render(request, 'mha/equipselection1.html', context)


def load_thermeff2(request):
    form = EquipInfo2(request.POST or None)
    Eff.objects.all().delete()
    e = Thermeff.objects.annotate(effthermA=F('efftherm'))
    g = list(e.values_list('efftherm', flat=True).distinct())
    try:
        h = Config.objects.create(id=1, configs=g[0])
    except Exception:
        h = 0
    config = Config.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "config": config,
        "form": form,
    }
    return render(request, 'mha/config_1.html', context)


def load_configtherm2(request):
    form = EquipInfo2(request.POST or None)
    Config.objects.all().delete()
    e = ConfigTherm.objects.annotate(thermsA=F('therms'))
    g = list(e.values_list('therms', flat=True).distinct())
    try:
        h = Config.objects.create(id=1, configs=g[0])
    except Exception:
        h = 0
    config = Config.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "config": config,
        "form": form,
    }
    return render(request, 'mha/config_1.html', context)




def load_thermomodnum(request):
    a = FilterThermostatModnum.objects.all()
    form = EquipmentSelect1(request.POST or None)
    thermostatmodnum = a.values('thermomodnum')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute17_url())
    context = {
        "thermostatmodnum": thermostatmodnum,
        "form": form,
    }
    return render(request, 'mha/thermostatmodnum_1.html', context)


def thermostatmodnum(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    aa = Bidding.objects.values_list('bidid', flat=True).last()
    ab = Bidding.objects.values_list('conid', flat=True).last()
    ac = Bidding.objects.values_list('custid', flat=True).last()
    TotalJobCost.objects.filter(bidid=a, descripid=4).delete()
    form = EquipmentSelect1(request.POST)
    b = request.POST['id_thermostatmodnum']
    b1 = SmartThermostat.objects.filter(id=b).values_list('smart', flat=True).last()
    c = FilterThermostatModnum.objects.filter(id=b).values_list('thermomodnum', flat=True)
    c1 = FilterThermostatModnum.objects.filter(id=b).values_list('smart')
    d = EquipSelection.objects.filter(bidid=a).update(thermostatmodnum=c, smart=b1)

    a3 = EquipSelection.objects.filter(bidid=a).values_list('furneff', flat=True).first()
    b3 = NicorRebate1.objects.values_list('rebate1eff', flat=True).first()
    c3 = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()

    d1 = c.first()
    d2a = Equipment2.objects.filter(modelnum=d1).values_list('warr', flat=True)
    d2b = Equipment2.objects.filter(modelnum=d1).values_list('cost', flat=True)
    d2c = Equipment2.objects.filter(modelnum=d1).values_list('eff', flat=True)
    d2d = Equipment2.objects.filter(modelnum=d1).values_list('mfgmodeldescrip', flat=True)
    d2 = SelectedEquip.objects.filter(equipid=4, bidid=aa).update(quanity=1, mfgmodeldescrip=d2d, modelnum=d1,
                                                                  btu='N/A', eff=d2c, warr=d2a, cost=d2b)
    d4 = Bidding.objects.filter(bidid=aa).update(cost4total=d2b, quanity4=1)
    d5 = TotalJobCost.objects.create(bidid=a, conid=ab, custid=ac, jobcost=d2b, descripid=4)
    d3 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
    e3 = RebateInfo.objects.values_list('furntherm97', flat=True).first()
    if a3 == b3 and c3 == d3:
        EquipSelection.objects.filter(bidid=a).update(vendor1rebate=e3)
    else:

        a2 = EquipSelection.objects.filter(bidid=a).values_list('furneff', flat=True).first()
        b2 = NicorRebate2.objects.values_list('rebate2eff', flat=True).first()
        c2 = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()
        d2 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
        e2 = RebateInfo.objects.values_list('furntherm95', flat=True).first()
        if a2 == b2 and c2 == d2:
            EquipSelection.objects.filter(bidid=a).update(vendor1rebate=e2)
        else:
            aa = EquipSelection.objects.filter(bidid=a).values_list('furneff', flat=True).first()
            bb = NicorRebate1.objects.values_list('rebate1eff', flat=True).first()
            cc = RebateInfo.objects.values_list('furn97', flat=True).first()
            dd = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()
            if aa == bb:
                EquipSelection.objects.filter(bidid=a).update(vendor1rebate=cc)
            else:

                b1 = NicorRebate2.objects.values_list('rebate2eff', flat=True).first()
                c1 = RebateInfo.objects.values_list('furn95', flat=True).first()
                if aa == b1:
                    EquipSelection.objects.filter(bidid=a).update(vendor1rebate=c1)
                else:
                    b2 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
                    c2 = RebateInfo.objects.values_list('smartthermnicor', flat=True).first()
                    if dd == b2:
                        EquipSelection.objects.filter(bidid=a).update(vendor1rebate=c2)
                    else:
                        EquipSelection.objects.filter(bidid=a).update(vendor1rebate=0.00)
    dd3 = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()
    b3 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
    c3 = RebateInfo.objects.values_list('smartthermcomed', flat=True).first()
    if dd3 == b3:
        EquipSelection.objects.filter(bidid=a).update(vendor2rebate=c3)
    else:
        EquipSelection.objects.filter(bidid=a).update(vendor2rebate=0.00)
    h = EquipSelection.objects.filter(bidid=a).values_list('vendor1rebate', flat=True).first()
    i = EquipSelection.objects.filter(bidid=a).values_list('vendor2rebate', flat=True).first()
    j = h + i
    k = EquipSelection.objects.filter(bidid=a).update(totalrebate=j)
    context = {
        "form": form,
        "d": d,
        "d1": d1,
        "d2": d2,
        "d4": d4,
        "k": k,
    }
    return render(request, 'mha/equipselection1.html', context)


def nothermostatmodnum(request):
    a = EquipSelection.objects.values_list('bidid', flat=True).last()
    b = Bidding.objects.values_list('bidid', flat=True).last()
    c = Bidding.objects.values_list('conid', flat=True).last()
    d = Bidding.objects.values_list('custid', flat=True).last()
    TotalJobCost.objects.filter(bidid=a, descripid=4).delete()
    form = EquipmentSelect1(request.POST)
    a3 = EquipSelection.objects.filter(bidid=a).values_list('furneff', flat=True).first()
    b3 = NicorRebate1.objects.values_list('rebate1eff', flat=True).first()
    aa = EquipSelection.objects.filter(bidid=a).values_list('furneff', flat=True).first()
    bb = NicorRebate1.objects.values_list('rebate1eff', flat=True).first()
    cc = RebateInfo.objects.values_list('furn97', flat=True).first()
    dd = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()
    if aa == bb:
        EquipSelection.objects.filter(bidid=a).update(vendor1rebate=cc)
    else:

        b1 = NicorRebate2.objects.values_list('rebate2eff', flat=True).first()
        c1 = RebateInfo.objects.values_list('furn95', flat=True).first()
        if aa == b1:
            EquipSelection.objects.filter(bidid=a).update(vendor1rebate=c1)
        else:
            b2 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
            c2 = RebateInfo.objects.values_list('smartthermnicor', flat=True).first()
            if dd == b2:
                EquipSelection.objects.filter(bidid=a).update(vendor1rebate=c2)
            else:
                EquipSelection.objects.filter(bidid=a).update(vendor1rebate=0.00)
    dd3 = EquipSelection.objects.filter(bidid=a).values_list('smart', flat=True).first()
    b3 = NicorRebate3.objects.values_list('rebate3eff', flat=True).first()
    c3 = RebateInfo.objects.values_list('smartthermcomed', flat=True).first()
    if dd3 == b3:
        EquipSelection.objects.filter(bidid=a).update(vendor2rebate=c3)
    else:
        EquipSelection.objects.filter(bidid=a).update(vendor2rebate=0.00)
    h = EquipSelection.objects.filter(bidid=a).values_list('vendor1rebate', flat=True).first()
    i = EquipSelection.objects.filter(bidid=a).values_list('vendor2rebate', flat=True).first()
    j = h + i
    k = EquipSelection.objects.filter(bidid=a).update(totalrebate=j)
    context = {
        "form": form,
        "d": d,
        "d1": d1,
        "d2": d2,
        "d4": d4,
        "k": k,
    }
    return render(request, 'mha/equipselection1.html', context)



def load_thermgasviv2(request):
    form = EquipInfo2(request.POST or None)
    Gasviv.objects.all().delete()
    e = Gasvivtherm.objects.annotate(thermgasvivsA=F('thermgasvivs'))
    g = list(e.values_list('thermgasvivs', flat=True).distinct())
    try:
        h = Gasviv.objects.create(id=1, gasvivs=g[0])
    except Exception:
        h = 0
    try:
        h2 = Gasviv.objects.create(id=2, gasvivs=g[1])
    except Exception:
        h2 = 0
    try:
        h3 = Gasviv.objects.create(id=3, gasvivs=g[2])
    except Exception:
        h3 = 0
    gasviv = Gasviv.objects.all()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute3_url())
    context = {
        "gasviv": gasviv,
        "form": form,
    }
    return render(request, 'mha/gasviv_1.html', context)




def load_vendor1(request):
    form = EquipmentSelect1(request.POST or None)
    vendor1rebate = EquipSelection.objects.values_list('vendor1rebate', flat=True).last()
    context = {
        "vendor1rebate": vendor1rebate,
        "form": form,
    }
    return render(request, 'mha/vendor1_1.html', context)


def load_vendor2(request):
    form = EquipmentSelect1(request.POST or None)
    vendor2rebate = EquipSelection.objects.values_list('vendor2rebate', flat=True).last()
    context = {
        "vendor2rebate": vendor2rebate,
        "form": form,
    }
    return render(request, 'mha/vendor2_1.html', context)


def load_totalrebate(request):
    form = EquipmentSelect1(request.POST or None)
    totalrebate = EquipSelection.objects.values_list('totalrebate', flat=True).last()
    context = {
        "totalrebate": totalrebate,
        "form": form,
    }
    return render(request, 'mha/totalrebate_1.html', context)

















############################################  Equip. Selection 2 ###########################################################


def equipselection2(request, id=None):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(bidid=a2).update(optionid=2, options='Option B')
    ab = Bidding.objects.filter(bidid=a2).update(optionsid=2, options='Option B')
    ac = CurrentJobInfo.objects.filter(bidid=a2).update(optionid=2, options='Option B')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    SelectedEquip.objects.create(equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, bidid=a2)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect1(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()

    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)


#def equipselection2(request, id=None):
#    a = EquipSelection.objects.values_list('id', flat=True).last()
#    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
#    b = CustomerInfo.objects.values_list('id', flat=True).last()
#    SelectedEquip.objects.filter(id=1).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=2).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=3).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=4).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=5).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=6).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    SelectedEquip.objects.filter(id=7).update(type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
#    instance = get_object_or_404(EquipSelection, id=a)
#    instance2 = get_object_or_404(EquipSelection, bidid=a2)
#    form = EquipmentSelect1(request.POST or None, instance=instance)
#    queryset = CustomerInfo.objects.filter(id=b).values()
#
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return redirect(instance.get_absolute20_url())
#
#    context = {
#        "instance": instance,
#        "instance2": instance2,
#        "form": form,
#        "object_list": queryset,
#        #    "aa": aa,
#        #    "ab": ab,
#        #    "ac": ac,
#    }
#    return render(request, 'mha/equipselection1.html', context)


def equipselection3(request, id=None):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(bidid=a2).update(optionid=3, options='Option C')
    ab = Bidding.objects.filter(bidid=a2).update(optionsid=3, options='Option C')
    ac = CurrentJobInfo.objects.filter(bidid=a2).update(optionid=3, options='Option C')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    SelectedEquip.objects.create(equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, bidid=a2)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect1(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()

    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)


def equipselection4(request, id=None):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(bidid=a2).update(optionid=4, options='Option D')
    ab = Bidding.objects.filter(bidid=a2).update(optionsid=4, options='Option D')
    ac = CurrentJobInfo.objects.filter(bidid=a2).update(optionid=4, options='Option D')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    SelectedEquip.objects.create(equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, bidid=a2)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect1(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()

    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)


def equipselection5(request, id=None):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    a2 = EquipSelection.objects.values_list('bidid', flat=True).last()
    a3 = EquipSelection.objects.values_list('conid', flat=True).last()
    a4 = EquipSelection.objects.values_list('custid', flat=True).last()
    aa = EquipSelection.objects.filter(bidid=a2).update(optionid=5, options='Option E')
    ab = Bidding.objects.filter(bidid=a2).update(optionsid=5, options='Option E')
    ac = CurrentJobInfo.objects.filter(bidid=a2).update(optionid=5, options='Option E')
    b = CustomerInfo.objects.values_list('id', flat=True).last()
    CustomerInfo.objects.values_list('id', flat=True).last()
    SelectedEquip.objects.create(equipid=1, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=2, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=3, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=4, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=5, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=6, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    SelectedEquip.objects.create(equipid=7, bidid=a2, conid=a3, custid=a4, jobid=a, type='', mfg='', modelnum='', mfgmodeldescrip='', btu='', warr='')
    instance = get_object_or_404(EquipSelection, bidid=a2)
    instance2 = get_object_or_404(EquipSelection, bidid=a2)
    form = EquipmentSelect1(request.POST or None, instance=instance)
    queryset = CustomerInfo.objects.filter(id=b).values()

    c = Bidding.objects.filter(jobid=a).count()
    d = Bidding.objects.filter(bidid=a2).update(count=c)
    e = TargetProfit.objects.create(conid=a3, custid=a4, jobid=a, bidid=a2, targetprofit_id=0.15)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "instance2": instance2,
        "form": form,
        "object_list": queryset,
        "aa": aa,
        "ab": ab,
        "ac": ac,
        "d": d,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)











def deleteequipselection(request):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    b = EquipSelection.objects.values_list('custid', flat=True).last()
    b1 = EquipSelection.objects.values_list('bidid', flat=True).last()
    instance = CustomerInfo.objects.get(custid=b)
    c = EquipSelection.objects.filter(jobid=a).delete()
    c1 = Custpagelocation.objects.filter(bidid=b1).delete()
    context = {
        "c": c,
        "c1": c1,
        "b1": b1,
    }
    return redirect(instance.get_absolute12_url(), context)


# def bidpage(request):
#    FilterEquipType.objects.all().delete()
#    a = Bidding.objects.values_list('jobid', flat=True).last()
#    instance = Bidding.objects.get(jobid=a)
#    form = BidSelect(request.POST or None, instance=instance)
#    b = Bidding.objects.filter(jobid=a).values_list('custid', flat=True).last()
#    queryset = CustomerInfo.objects.filter(id=b).values()
#    queryset2 = EquipSelection.objects.filter(jobid=a).values()
#    queryset3 = PackageInfo.objects.all()
#    queryset4 = InstallPackage1.objects.all()
#    queryset5 = InstallPackage2.objects.all()
#    queryset6 = InstallPackage3.objects.all()
#    queryset7 = InstallPackage4.objects.all()
#    queryset8 = InstallPackage5.objects.all()
#    queryset9 = InstallPackage6.objects.all()
#    queryset10 = InstallPackage7.objects.all()
#    queryset11 = InstallPackage8.objects.all()
#    queryset12 = InstallPackage9.objects.all()
#    queryset13 = InstallPackage10.objects.all()
#    queryset14 = InstallPackage11.objects.all()
#    queryset15 = InstallPackage12.objects.all()
#    queryset16 = InstallPackage13.objects.all()
#    queryset17 = InstallPackage14.objects.all()
#    queryset18 = InstallPackage15.objects.all()
#    queryset19 = InstallPackage16.objects.all()
#    c = Equipment2.objects.all().annotate(typeA=F('type'))
#    j1 = list(c.values_list('type', flat=True).distinct())
#    try:
#        k = FilterEquipType.objects.create(id=1, typeequip=j1[0])
#    except Exception:
#        k = 0
#    try:
#        k1 = FilterEquipType.objects.create(id=2, typeequip=j1[1])
#    except Exception:
#        k1 = 0
#    try:
#        k2 = FilterEquipType.objects.create(id=3, typeequip=j1[2])
#    except Exception:
#        k2 = 0
#    try:
#        k3 = FilterEquipType.objects.create(id=4, typeequip=j1[3])
#    except Exception:
#        k3 = 0
#    try:
#        k4 = FilterEquipType.objects.create(id=5, typeequip=j1[4])
#    except Exception:
#        k4 = 0
#    try:
#        k5 = FilterEquipType.objects.create(id=6, typeequip=j1[5])
#    except Exception:
#        k5 = 0
#    try:
#        k6 = FilterEquipType.objects.create(id=7, typeequip=j1[6])
#    except Exception:
#        k6 = 0
#    try:
#        k7 = FilterEquipType.objects.create(id=8, typeequip=j1[7])
#    except Exception:
#        k7 = 0
#    try:
#        k8 = FilterEquipType.objects.create(id=9, typeequip=j1[8])
#    except Exception:
#        k8 = 0
#    try:
#        k9 = FilterEquipType.objects.create(id=10, typeequip=j1[9])
#    except Exception:
#        k9 = 0
#    try:
#        k10 = FilterEquipType.objects.create(id=11, typeequip=j1[10])
#    except Exception:
#        k10 = 0
#    try:
#        k11 = FilterEquipType.objects.create(id=12, typeequip=j1[11])
#    except Exception:
#        k11 = 0
#    try:
#        k12 = FilterEquipType.objects.create(id=13, typeequip=j1[12])
#    except Exception:
#        k12 = 0
#    try:
#        k13 = FilterEquipType.objects.create(id=14, typeequip=j1[13])
#    except Exception:
#        k13 = 0
#    try:
#        k14 = FilterEquipType.objects.create(id=15, typeequip=j1[14])
#    except Exception:
#        k14 = 0
#    try:
#        k15 = FilterEquipType.objects.create(id=16, typeequip=j1[15])
#    except Exception:
#        k15 = 0
#    try:
#        k16 = FilterEquipType.objects.create(id=17, typeequip=j1[16])
#    except Exception:
#        k16 = 0
#    try:
#        k17 = FilterEquipType.objects.create(id=18, typeequip=j1[17])
#    except Exception:
#        k17 = 0
#    try:
#        k18 = FilterEquipType.objects.create(id=19, typeequip=j1[18])
#    except Exception:
#        k18 = 0
#    try:
#        k19 = FilterEquipType.objects.create(id=20, typeequip=j1[19])
#    except Exception:
#        k19 = 0
#
#    d = EquipSelection.objects.filter(jobid=a).values_list('outsideunittype', flat=True)
#    d1 = Bidding.objects.filter(jobid=a).update(jobtype1=d)
#    e = EquipSelection.objects.filter(jobid=a).values_list('condmodnum', flat=True)
#    e1 = Bidding.objects.filter(jobid=a).update(descript1=e)
#    f = EquipSelection.objects.filter(jobid=a).values_list('airhandlertype', flat=True)
#    f1 = Bidding.objects.filter(jobid=a).update(jobtype2=f)
#    g = EquipSelection.objects.filter(jobid=a).values_list('furnmodnum', flat=True)
#    g1 = Bidding.objects.filter(jobid=a).update(descript2=g)
#    h = 'Coil'
#    h1 = Bidding.objects.filter(jobid=a).update(jobtype3=h)
#    i = EquipSelection.objects.filter(jobid=a).values_list('coilmodnum', flat=True)
#    i1 = Bidding.objects.filter(jobid=a).update(descript3=i)
#    j = 'Thermostat'
#    j1 = Bidding.objects.filter(jobid=a).update(jobtype4=j)
#    k = EquipSelection.objects.filter(jobid=a).values_list('thermostatmodnum', flat=True)
#    k1 = Bidding.objects.filter(jobid=a).update(descript4=k)
#    l = EquipSelection.objects.filter(jobid=a).values_list('optionid', flat=True)
#    l1 = EquipSelection.objects.filter(jobid=a).values_list('options', flat=True)
#    m = CurrentJobInfo.objects.filter(jobid=a).update(optionid=l, options=l1)
#    if form.is_valid():
#        instance = form.save(commit=False)
#        instance.save()
#        return redirect(instance.get_absolute17_url())
#
#    context = {
#        "instance": instance,
#        "form": form,
#        "object_list": queryset,
#        "object_list2": queryset2,
#        "object_list3": queryset3,
#        "object_list4": queryset4,
#        "object_list5": queryset5,
#        "object_list6": queryset6,
#        "object_list7": queryset7,
#        "object_list8": queryset8,
#        "object_list9": queryset9,
#        "object_list10": queryset10,
#        "object_list11": queryset11,
#        "object_list12": queryset12,
#        "object_list13": queryset13,
#        "object_list14": queryset14,
#        "object_list15": queryset15,
#        "object_list16": queryset16,
#        "object_list17": queryset17,
#        "object_list18": queryset18,
#        "object_list19": queryset19,
#        "d1": d1,
#        "e1": e1,
#        "f1": f1,
#        "g1": g1,
#        "h1": h1,
#        "i1": i1,
#        "j1": j1,
#        "k1": k1,
#        "m": m,
#    }
#    return render(request, 'mha/bidpage.html', context)


def bidpage(request, bidid=None):
    FilterEquipType.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    b = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=b).values()
    queryset2 = EquipSelection.objects.filter(bidid=bidid).values()
    queryset3 = PackageInfo.objects.all()
    queryset4 = InstallPackage1.objects.all()
    queryset5 = InstallPackage2.objects.all()
    queryset6 = InstallPackage3.objects.all()
    queryset7 = InstallPackage4.objects.all()
    queryset8 = InstallPackage5.objects.all()
    queryset9 = InstallPackage6.objects.all()
    queryset10 = InstallPackage7.objects.all()
    queryset11 = InstallPackage8.objects.all()
    queryset12 = InstallPackage9.objects.all()
    queryset13 = InstallPackage10.objects.all()
    queryset14 = InstallPackage11.objects.all()
    queryset15 = InstallPackage12.objects.all()
    queryset16 = InstallPackage13.objects.all()
    queryset17 = InstallPackage14.objects.all()
    queryset18 = InstallPackage15.objects.all()
    queryset19 = InstallPackage16.objects.all()
    c = Equipment2.objects.all().annotate(typeA=F('type'))
    j1 = list(c.values_list('type', flat=True).distinct())
    try:
        k = FilterEquipType.objects.create(id=1, typeequip=j1[0])
    except Exception:
        k = 0
    try:
        k1 = FilterEquipType.objects.create(id=2, typeequip=j1[1])
    except Exception:
        k1 = 0
    try:
        k2 = FilterEquipType.objects.create(id=3, typeequip=j1[2])
    except Exception:
        k2 = 0
    try:
        k3 = FilterEquipType.objects.create(id=4, typeequip=j1[3])
    except Exception:
        k3 = 0
    try:
        k4 = FilterEquipType.objects.create(id=5, typeequip=j1[4])
    except Exception:
        k4 = 0
    try:
        k5 = FilterEquipType.objects.create(id=6, typeequip=j1[5])
    except Exception:
        k5 = 0
    try:
        k6 = FilterEquipType.objects.create(id=7, typeequip=j1[6])
    except Exception:
        k6 = 0
    try:
        k7 = FilterEquipType.objects.create(id=8, typeequip=j1[7])
    except Exception:
        k7 = 0

    d = EquipSelection.objects.filter(bidid=bidid).values_list('outsideunittype', flat=True)
    d1 = Bidding.objects.filter(bidid=bidid).update(jobtype1=d)
    e = EquipSelection.objects.filter(bidid=bidid).values_list('condmodnum', flat=True)
    e1 = Bidding.objects.filter(bidid=bidid).update(descript1=e)

    f = EquipSelection.objects.filter(bidid=bidid).values_list('airhandlertype', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).update(jobtype2=f)
    g = EquipSelection.objects.filter(bidid=bidid).values_list('furnmodnum', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).update(descript2=g)

    h = 'Coil'
    h1 = Bidding.objects.filter(bidid=bidid).update(jobtype3=h)
    i = EquipSelection.objects.filter(bidid=bidid).values_list('coilmodnum', flat=True)
    i1 = Bidding.objects.filter(bidid=bidid).update(descript3=i)

    j = 'Thermostat'
    j1 = Bidding.objects.filter(bidid=bidid).update(jobtype4=j)
    k = EquipSelection.objects.filter(bidid=bidid).values_list('thermostatmodnum', flat=True)
    k1 = Bidding.objects.filter(bidid=bidid).update(descript4=k)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "object_list11": queryset11,
        "object_list12": queryset12,
        "object_list13": queryset13,
        "object_list14": queryset14,
        "object_list15": queryset15,
        "object_list16": queryset16,
        "object_list17": queryset17,
        "object_list18": queryset18,
        "object_list19": queryset19,
        "d1": d1,
        "e1": e1,
        "f1": f1,
        "g1": g1,
        "h1": h1,
        "i1": i1,
        "j1": j1,
        "k1": k1,

    }
    return render(request, 'mha/bidpage.html', context)

def bidpageno(request, bidid=None):
    FilterEquipType.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    b = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=b).values()
    queryset2 = EquipSelection.objects.filter(bidid=bidid).values()
    queryset3 = PackageInfo.objects.all()
    queryset4 = InstallPackage1.objects.all()
    queryset5 = InstallPackage2.objects.all()
    queryset6 = InstallPackage3.objects.all()
    queryset7 = InstallPackage4.objects.all()
    queryset8 = InstallPackage5.objects.all()
    queryset9 = InstallPackage6.objects.all()
    queryset10 = InstallPackage7.objects.all()
    queryset11 = InstallPackage8.objects.all()
    queryset12 = InstallPackage9.objects.all()
    queryset13 = InstallPackage10.objects.all()
    queryset14 = InstallPackage11.objects.all()
    queryset15 = InstallPackage12.objects.all()
    queryset16 = InstallPackage13.objects.all()
    queryset17 = InstallPackage14.objects.all()
    queryset18 = InstallPackage15.objects.all()
    queryset19 = InstallPackage16.objects.all()
    c = Equipment2.objects.all().annotate(typeA=F('type'))
    j1 = list(c.values_list('type', flat=True).distinct())
    try:
        k = FilterEquipType.objects.create(id=1, typeequip=j1[0])
    except Exception:
        k = 0
    try:
        k1 = FilterEquipType.objects.create(id=2, typeequip=j1[1])
    except Exception:
        k1 = 0
    try:
        k2 = FilterEquipType.objects.create(id=3, typeequip=j1[2])
    except Exception:
        k2 = 0
    try:
        k3 = FilterEquipType.objects.create(id=4, typeequip=j1[3])
    except Exception:
        k3 = 0
    try:
        k4 = FilterEquipType.objects.create(id=5, typeequip=j1[4])
    except Exception:
        k4 = 0
    try:
        k5 = FilterEquipType.objects.create(id=6, typeequip=j1[5])
    except Exception:
        k5 = 0
    try:
        k6 = FilterEquipType.objects.create(id=7, typeequip=j1[6])
    except Exception:
        k6 = 0
    try:
        k7 = FilterEquipType.objects.create(id=8, typeequip=j1[7])
    except Exception:
        k7 = 0


    d = EquipSelection.objects.filter(bidid=bidid).values_list('outsideunittype', flat=True)
    d1 = Bidding.objects.filter(bidid=bidid).update(jobtype1=d)
    e = EquipSelection.objects.filter(bidid=bidid).values_list('condmodnum', flat=True)
    e1 = Bidding.objects.filter(bidid=bidid).update(descript1=e)

    f = EquipSelection.objects.filter(bidid=bidid).values_list('airhandlertype', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).update(jobtype2=f)
    g = EquipSelection.objects.filter(bidid=bidid).values_list('furnmodnum', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).update(descript2=g)

    h = 'Coil'
    h1 = Bidding.objects.filter(bidid=bidid).update(jobtype3=h)
    i = EquipSelection.objects.filter(bidid=bidid).values_list('coilmodnum', flat=True)
    i1 = Bidding.objects.filter(bidid=bidid).update(descript3=i)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute17_url())

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "object_list11": queryset11,
        "object_list12": queryset12,
        "object_list13": queryset13,
        "object_list14": queryset14,
        "object_list15": queryset15,
        "object_list16": queryset16,
        "object_list17": queryset17,
        "object_list18": queryset18,
        "object_list19": queryset19,
        "d1": d1,
        "e1": e1,
        "f1": f1,
        "g1": g1,
        "h1": h1,
        "i1": i1,
        "j1": j1,

    }
    return render(request, 'mha/bidpage.html', context)


def load_jobtype1(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype1 = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True).last()
    context = {
        "instance": instance,
        "jobtype1": jobtype1,
        "form": form,
    }
    return render(request, 'mha/jobtype1_1.html', context)


def load_jobtype2(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype2 = Bidding.objects.filter(bidid=bidid).values_list('jobtype2', flat=True).last()
    context = {
        "instance": instance,
        "jobtype2": jobtype2,
        "form": form,
    }
    return render(request, 'mha/jobtype2_1.html', context)


def load_jobtype3(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype3 = Bidding.objects.filter(bidid=bidid).values_list('jobtype3', flat=True).last()
    context = {
        "instance": instance,
        "jobtype3": jobtype3,
        "form": form,
    }
    return render(request, 'mha/jobtype3_1.html', context)


def load_jobtype4(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype4 = Bidding.objects.filter(bidid=bidid).values_list('jobtype4', flat=True).last()
    context = {
        "instance": instance,
        "jobtype4": jobtype4,
        "form": form,
    }
    return render(request, 'mha/jobtype4_1.html', context)


def load_jobtype4b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype4b = Bidding.objects.values_list('jobtype4b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype4b": jobtype4b,
        "form": form,
    }
    return render(request, 'mha/jobtype4b_1.html', context)


def load_descrip1(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript1 = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True).last()
    context = {
        "instance": instance,
        "descript1": descript1,
        "form": form,
    }
    return render(request, 'mha/descrip1_1.html', context)


def load_quanity1(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None)
    quanity1 = Bidding.objects.filter(jobid=jobid).values_list('quanity1', flat=True).last()
    context = {
        "instance": instance,
        "quanity1": quanity1,
        "form": form,
    }
    return render(request, 'mha/quan1_1.html', context)


def load_descrip2(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript2 = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True).last()
    context = {
        "instance": instance,
        "descript2": descript2,
        "form": form,
    }
    return render(request, 'mha/descrip2_1.html', context)


def load_descrip3(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript3 = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True).last()
    context = {
        "instance": instance,
        "descript3": descript3,
        "form": form,
    }
    return render(request, 'mha/descrip3_1.html', context)


def load_descrip4(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript4 = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True).last()
    context = {
        "instance": instance,
        "descript4": descript4,
        "form": form,
    }
    return render(request, 'mha/descrip4_1.html', context)


def jobtype4(request, bidid=None):
    FilterTypeDescrip.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_jobtype4']
    b = FilterEquipType.objects.filter(id=a).values_list("typeequip", flat=True).first()
    Bidding.objects.filter(bidid=bidid).update(jobtype4b=b, quanity4=0)
    e1 = Equipment2.objects.filter(type=b).annotate(modelnumA=F('modelnum'))

    d3 = SelectedEquip.objects.filter(id=4).update(type=b)

    g17 = list(e1.values_list('mfg', flat=True))
    g1 = list(e1.values_list('modelnum', flat=True).distinct())
    g12 = list(e1.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        w1 = 1
        i = FilterTypeDescrip.objects.create(id=w1, mfg=g17[0], modnum=g1[0], mfgdescrip=g12[0])
    except Exception:
        i = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w2 = w + 1
        i1 = FilterTypeDescrip.objects.create(id=w2, mfg=g17[1], modnum=g1[1], mfgdescrip=g12[1])
    except Exception:
        i1 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w3 = w + 1
        i2 = FilterTypeDescrip.objects.create(id=w3, mfg=g17[2], modnum=g1[2], mfgdescrip=g12[2])
    except Exception:
        i2 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w4 = w + 1
        i3 = FilterTypeDescrip.objects.create(id=w4, mfg=g17[3], modnum=g1[3], mfgdescrip=g12[3])
    except Exception:
        i3 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w5 = w + 1
        i4 = FilterTypeDescrip.objects.create(id=w5, mfg=g17[4], modnum=g1[4], mfgdescrip=g12[4])
    except Exception:
        i4 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w6 = w + 1
        i5 = FilterTypeDescrip.objects.create(id=w6, mfg=g17[5], modnum=g1[5], mfgdescrip=g12[5])
    except Exception:
        i5 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w7 = w + 1
        i6 = FilterTypeDescrip.objects.create(id=w7, mfg=g17[6], modnum=g1[6], mfgdescrip=g12[6])
    except Exception:
        i6 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w8 = w + 1
        i7 = FilterTypeDescrip.objects.create(id=w8, mfg=g17[7], modnum=g1[7], mfgdescrip=g12[7])
    except Exception:
        i7 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w9 = w + 1
        i8 = FilterTypeDescrip.objects.create(id=w9, mfg=g17[8], modnum=g1[8], mfgdescrip=g12[8])
    except Exception:
        i8 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w10 = w + 1
        i9 = FilterTypeDescrip.objects.create(id=w10, mfg=g17[9], modnum=g1[9], mfgdescrip=g12[9])
    except Exception:
        i9 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w11 = w + 1
        i10 = FilterTypeDescrip.objects.create(id=w11, mfg=g17[10], modnum=g1[10], mfgdescrip=g12[10])
    except Exception:
        i10 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w12 = w + 1
        i11 = FilterTypeDescrip.objects.create(id=w12, mfg=g17[11], modnum=g1[11], mfgdescrip=g12[11])
    except Exception:
        i11 = 0

    context = {
        "instance": instance,
        "form": form,
        "d3": d3,
        "i": i,
        "i1": i1,
        "i2": i2,
        "i3": i3,
        "i4": i4,
        "i5": i5,
        "i6": i6,
        "i7": i7,
        "i8": i8,
        "i9": i9,
        "i10": i10,
        "i11": i11,
    }
    return render(request, 'mha/bidpage.html', context)



def jobtype5(request, bidid=None):
    FilterTypeDescrip.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_jobtype5']
    b = FilterEquipType.objects.filter(id=a).values_list("typeequip", flat=True).first()
    Bidding.objects.filter(bidid=bidid).update(jobtype5b=b, quanity5=0)
    e1 = Equipment2.objects.filter(type=b).annotate(modelnumA=F('modelnum'))

    d3 = SelectedEquip.objects.filter(id=5).update(type=b)

    g17 = list(e1.values_list('mfg', flat=True))
    g1 = list(e1.values_list('modelnum', flat=True).distinct())
    g12 = list(e1.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        w1 = 1
        i = FilterTypeDescrip.objects.create(id=w1, mfg=g17[0], modnum=g1[0], mfgdescrip=g12[0])
    except Exception:
        i = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w2 = w + 1
        i1 = FilterTypeDescrip.objects.create(id=w2, mfg=g17[1], modnum=g1[1], mfgdescrip=g12[1])
    except Exception:
        i1 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w3 = w + 1
        i2 = FilterTypeDescrip.objects.create(id=w3, mfg=g17[2], modnum=g1[2], mfgdescrip=g12[2])
    except Exception:
        i2 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w4 = w + 1
        i3 = FilterTypeDescrip.objects.create(id=w4, mfg=g17[3], modnum=g1[3], mfgdescrip=g12[3])
    except Exception:
        i3 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w5 = w + 1
        i4 = FilterTypeDescrip.objects.create(id=w5, mfg=g17[4], modnum=g1[4], mfgdescrip=g12[4])
    except Exception:
        i4 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w6 = w + 1
        i5 = FilterTypeDescrip.objects.create(id=w6, mfg=g17[5], modnum=g1[5], mfgdescrip=g12[5])
    except Exception:
        i5 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w7 = w + 1
        i6 = FilterTypeDescrip.objects.create(id=w7, mfg=g17[6], modnum=g1[6], mfgdescrip=g12[6])
    except Exception:
        i6 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w8 = w + 1
        i7 = FilterTypeDescrip.objects.create(id=w8, mfg=g17[7], modnum=g1[7], mfgdescrip=g12[7])
    except Exception:
        i7 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w9 = w + 1
        i8 = FilterTypeDescrip.objects.create(id=w9, mfg=g17[8], modnum=g1[8], mfgdescrip=g12[8])
    except Exception:
        i8 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w10 = w + 1
        i9 = FilterTypeDescrip.objects.create(id=w10, mfg=g17[9], modnum=g1[9], mfgdescrip=g12[9])
    except Exception:
        i9 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w11 = w + 1
        i10 = FilterTypeDescrip.objects.create(id=w11, mfg=g17[10], modnum=g1[10], mfgdescrip=g12[10])
    except Exception:
        i10 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w12 = w + 1
        i11 = FilterTypeDescrip.objects.create(id=w12, mfg=g17[11], modnum=g1[11], mfgdescrip=g12[11])
    except Exception:
        i11 = 0

    context = {
        "instance": instance,
        "form": form,
        "d3": d3,
        "i": i,
        "i1": i1,
        "i2": i2,
        "i3": i3,
        "i4": i4,
        "i5": i5,
        "i6": i6,
        "i7": i7,
        "i8": i8,
        "i9": i9,
        "i10": i10,
        "i11": i11,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobtype5b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype5b = Bidding.objects.values_list('jobtype5b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype5b": jobtype5b,
        "form": form,
    }
    return render(request, 'mha/jobtype5b_1.html', context)


def load_jobtype5(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype5 = Bidding.objects.values_list('jobtype5', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype5": jobtype5,
        "form": form,
    }
    return render(request, 'mha/jobtype5_1.html', context)


def jobdescrip5(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript5']
    b = FilterTypeDescrip.objects.filter(id=a).values_list("modnum", flat=True)
    d = b.first()
    d1 = Equipment2.objects.filter(modelnum=d).values_list("mfg")
    d2 = Equipment2.objects.filter(modelnum=d).values_list("btu")
    d3 = Equipment2.objects.filter(modelnum=d).values_list("mfgmodeldescrip")
    d4 = Equipment2.objects.filter(modelnum=d).values_list("warr")
    d4a = Equipment2.objects.filter(modelnum=d).values_list("eff") or 0
    d4b = Equipment2.objects.filter(modelnum=d).values_list("type")
    d5 = SelectedEquip.objects.filter(equipid=5, bidid=bidid).update(type=d4b, modelnum=d, mfg=d1, mfgmodeldescrip=d3,
                                                                     btu=d2, eff=d4a, warr=d4)
    Bidding.objects.filter(bidid=bidid).update(descript5=b)
    context = {
        "instance": instance,
        "form": form,
        "d5": d5,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobdescrip5b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript5b = Bidding.objects.values_list('descript5b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript5b": descript5b,
        "form": form,
    }
    return render(request, 'mha/descript5b_1.html', context)


def load_jobdescrip5(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript5 = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True)
    context = {
        "instance": instance,
        "descript5": descript5,
        "form": form,
    }
    return render(request, 'mha/descrip5_1.html', context)


def load_quanity5(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity5 = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True)
    context = {
        "instance": instance,
        "quanity5": quanity5,
        "form": form,
    }
    return render(request, 'mha/quan5_1.html', context)


def delete5(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity5=0, descript5="", jobtype5b="", cost5total=0)
    SelectedEquip.objects.filter(equipid=5, bidid=bidid).update(quanity=None, type="", modelnum="", mfg="",
                                                                mfgmodeldescrip="", btu="", eff="", warr="", cost=0.00)
    #    SelectedEquip.objects.filter(equipid=5, bidid=bidid).delete()
    TotalJobCost.objects.filter(descripid=5).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def jobtype6(request, bidid=None):
    FilterTypeDescrip.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_jobtype6']
    b = FilterEquipType.objects.filter(id=a).values_list("typeequip", flat=True).first()
    Bidding.objects.filter(bidid=bidid).update(jobtype6b=b, quanity6=0)
    e1 = Equipment2.objects.filter(type=b).annotate(modelnumA=F('modelnum'))
    d3 = SelectedEquip.objects.filter(id=6).update(type=b)
    g17 = list(e1.values_list('mfg', flat=True))
    g1 = list(e1.values_list('modelnum', flat=True).distinct())
    g12 = list(e1.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        w1 = 1
        i = FilterTypeDescrip.objects.create(id=w1, mfg=g17[0], modnum=g1[0], mfgdescrip=g12[0])
    except Exception:
        i = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w2 = w + 1
        i1 = FilterTypeDescrip.objects.create(id=w2, mfg=g17[1], modnum=g1[1], mfgdescrip=g12[1])
    except Exception:
        i1 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w3 = w + 1
        i2 = FilterTypeDescrip.objects.create(id=w3, mfg=g17[2], modnum=g1[2], mfgdescrip=g12[2])
    except Exception:
        i2 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w4 = w + 1
        i3 = FilterTypeDescrip.objects.create(id=w4, mfg=g17[3], modnum=g1[3], mfgdescrip=g12[3])
    except Exception:
        i3 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w5 = w + 1
        i4 = FilterTypeDescrip.objects.create(id=w5, mfg=g17[4], modnum=g1[4], mfgdescrip=g12[4])
    except Exception:
        i4 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w6 = w + 1
        i5 = FilterTypeDescrip.objects.create(id=w6, mfg=g17[5], modnum=g1[5], mfgdescrip=g12[5])
    except Exception:
        i5 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w7 = w + 1
        i6 = FilterTypeDescrip.objects.create(id=w7, mfg=g17[6], modnum=g1[6], mfgdescrip=g12[6])
    except Exception:
        i6 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w8 = w + 1
        i7 = FilterTypeDescrip.objects.create(id=w8, mfg=g17[7], modnum=g1[7], mfgdescrip=g12[7])
    except Exception:
        i7 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w9 = w + 1
        i8 = FilterTypeDescrip.objects.create(id=w9, mfg=g17[8], modnum=g1[8], mfgdescrip=g12[8])
    except Exception:
        i8 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w10 = w + 1
        i9 = FilterTypeDescrip.objects.create(id=w10, mfg=g17[9], modnum=g1[9], mfgdescrip=g12[9])
    except Exception:
        i9 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w11 = w + 1
        i10 = FilterTypeDescrip.objects.create(id=w11, mfg=g17[10], modnum=g1[10], mfgdescrip=g12[10])
    except Exception:
        i10 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w12 = w + 1
        i11 = FilterTypeDescrip.objects.create(id=w12, mfg=g17[11], modnum=g1[11], mfgdescrip=g12[11])
    except Exception:
        i11 = 0

    context = {
        "instance": instance,
        "form": form,
        "d3": d3,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobtype6b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype6b = Bidding.objects.values_list('jobtype6b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype6b": jobtype6b,
        "form": form,
    }
    return render(request, 'mha/jobtype6b_1.html', context)


def load_jobtype6(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype6 = Bidding.objects.values_list('jobtype6', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype6": jobtype6,
        "form": form,
    }
    return render(request, 'mha/jobtype6_1.html', context)


def jobdescrip6(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript6']
    b = FilterTypeDescrip.objects.filter(id=a).values_list("modnum", flat=True)
    d = b.first()
    d1 = Equipment2.objects.filter(modelnum=d).values_list("mfg")
    d2 = Equipment2.objects.filter(modelnum=d).values_list("btu")
    d3 = Equipment2.objects.filter(modelnum=d).values_list("mfgmodeldescrip")
    d4 = Equipment2.objects.filter(modelnum=d).values_list("warr")
    d4a = Equipment2.objects.filter(modelnum=d).values_list("type")
    d4b = Equipment2.objects.filter(modelnum=d).values_list("eff")
    d5 = SelectedEquip.objects.filter(equipid=6, bidid=bidid).update(type=d4a, modelnum=d, mfg=d1, mfgmodeldescrip=d3,
                                                                     btu=d2, eff=d4b, warr=d4)
    Bidding.objects.filter(bidid=bidid).update(descript5=b)
    context = {
        "instance": instance,
        "form": form,
        "d5": d5,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobdescrip6b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript6b = Bidding.objects.values_list('descript6b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript6b": descript6b,
        "form": form,
    }
    return render(request, 'mha/descript6b_1.html', context)


def load_jobdescrip6(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript6 = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True)
    context = {
        "instance": instance,
        "descript6": descript6,
        "form": form,
    }
    return render(request, 'mha/descrip6_1.html', context)


def load_quanity6(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity6 = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True)
    context = {
        "instance": instance,
        "quanity6": quanity6,
        "form": form,
    }
    return render(request, 'mha/quan6_1.html', context)


def delete6(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity6=0, descript6="", jobtype6b="", cost6total=0)
    SelectedEquip.objects.filter(equipid=6, bidid=bidid).update(quanity=None, type="", modelnum="", mfg="",
                                                                mfgmodeldescrip="", btu="", eff="", warr="", cost=0.00)
    #    SelectedEquip.objects.filter(equipid=6, bidid=bidid).delete()
    TotalJobCost.objects.filter(descripid=6).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def jobtype7(request, bidid=None):
    FilterTypeDescrip.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_jobtype7']
    b = FilterEquipType.objects.filter(id=a).values_list("typeequip", flat=True).first()
    Bidding.objects.filter(bidid=bidid).update(jobtype7b=b, quanity7=0)
    e1 = Equipment2.objects.filter(type=b).annotate(modelnumA=F('modelnum'))
    d3 = SelectedEquip.objects.filter(id=7).update(type=b)
    g17 = list(e1.values_list('mfg', flat=True))
    g1 = list(e1.values_list('modelnum', flat=True).distinct())
    g12 = list(e1.values_list('mfgmodeldescrip', flat=True).distinct())
    try:
        w1 = 1
        i = FilterTypeDescrip.objects.create(id=w1, mfg=g17[0], modnum=g1[0], mfgdescrip=g12[0])
    except Exception:
        i = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w2 = w + 1
        i1 = FilterTypeDescrip.objects.create(id=w2, mfg=g17[1], modnum=g1[1], mfgdescrip=g12[1])
    except Exception:
        i1 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w3 = w + 1
        i2 = FilterTypeDescrip.objects.create(id=w3, mfg=g17[2], modnum=g1[2], mfgdescrip=g12[2])
    except Exception:
        i2 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w4 = w + 1
        i3 = FilterTypeDescrip.objects.create(id=w4, mfg=g17[3], modnum=g1[3], mfgdescrip=g12[3])
    except Exception:
        i3 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w5 = w + 1
        i4 = FilterTypeDescrip.objects.create(id=w5, mfg=g17[4], modnum=g1[4], mfgdescrip=g12[4])
    except Exception:
        i4 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w6 = w + 1
        i5 = FilterTypeDescrip.objects.create(id=w6, mfg=g17[5], modnum=g1[5], mfgdescrip=g12[5])
    except Exception:
        i5 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w7 = w + 1
        i6 = FilterTypeDescrip.objects.create(id=w7, mfg=g17[6], modnum=g1[6], mfgdescrip=g12[6])
    except Exception:
        i6 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w8 = w + 1
        i7 = FilterTypeDescrip.objects.create(id=w8, mfg=g17[7], modnum=g1[7], mfgdescrip=g12[7])
    except Exception:
        i7 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w9 = w + 1
        i8 = FilterTypeDescrip.objects.create(id=w9, mfg=g17[8], modnum=g1[8], mfgdescrip=g12[8])
    except Exception:
        i8 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w10 = w + 1
        i9 = FilterTypeDescrip.objects.create(id=w10, mfg=g17[9], modnum=g1[9], mfgdescrip=g12[9])
    except Exception:
        i9 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w11 = w + 1
        i10 = FilterTypeDescrip.objects.create(id=w11, mfg=g17[10], modnum=g1[10], mfgdescrip=g12[10])
    except Exception:
        i10 = 0
    try:
        w = FilterTypeDescrip.objects.values_list('id', flat=True).last()
        w12 = w + 1
        i11 = FilterTypeDescrip.objects.create(id=w12, mfg=g17[11], modnum=g1[11], mfgdescrip=g12[11])
    except Exception:
        i11 = 0

    context = {
        "instance": instance,
        "form": form,
        "d3": d3,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobtype7b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype7b = Bidding.objects.values_list('jobtype7b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype7b": jobtype7b,
        "form": form,
    }
    return render(request, 'mha/jobtype7b_1.html', context)


def load_jobtype7(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    jobtype7 = Bidding.objects.values_list('jobtype7', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "jobtype7": jobtype7,
        "form": form,
    }
    return render(request, 'mha/jobtype7_1.html', context)


def jobdescrip7(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript7']
    b = FilterTypeDescrip.objects.filter(id=a).values_list("modnum", flat=True)
    d = b.first()
    d1 = Equipment2.objects.filter(modelnum=d).values_list("mfg")
    d2 = Equipment2.objects.filter(modelnum=d).values_list("btu")
    d3 = Equipment2.objects.filter(modelnum=d).values_list("mfgmodeldescrip")
    d4 = Equipment2.objects.filter(modelnum=d).values_list("warr")
    d4a = Equipment2.objects.filter(modelnum=d).values_list("eff")
    d4b = Equipment2.objects.filter(modelnum=d).values_list("type")
    d5 = SelectedEquip.objects.filter(equipid=7, bidid=bidid).update(type=d4b, modelnum=d, mfg=d1, mfgmodeldescrip=d3,
                                                                     btu=d2, eff=d4a, warr=d4)
    Bidding.objects.filter(bidid=bidid).update(descript5=b)
    context = {
        "instance": instance,
        "form": form,
        "d5": d5,
    }
    Bidding.objects.filter(bidid=bidid).update(descript7=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_jobdescrip7b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript7b = Bidding.objects.values_list('descript7b', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript7b": descript7b,
        "form": form,
    }
    return render(request, 'mha/descript7b_1.html', context)


def load_jobdescrip7(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript7 = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True)
    context = {
        "instance": instance,
        "descript7": descript7,
        "form": form,
    }
    return render(request, 'mha/descrip7_1.html', context)


def load_quanity7(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity7 = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True)
    context = {
        "instance": instance,
        "quanity7": quanity7,
        "form": form,
    }
    return render(request, 'mha/quan7_1.html', context)


def delete7(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity7=0, descript7="", jobtype7b="", cost7total=0)
    #    SelectedEquip.objects.filter(equipid=7, bidid=bidid).delete()
    SelectedEquip.objects.filter(equipid=7, bidid=bidid).update(quanity=None, type="", modelnum="", mfg="",
                                                                mfgmodeldescrip="", btu="", eff="", warr="", cost=0.00)
    TotalJobCost.objects.filter(descripid=7).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def newvendordescript(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_osrdescrip']
    b = OutsideResource.objects.values_list("id", flat=True).last()
    c = 1
    d = b + c
    e = OutsideResource.objects.create(id=d, osrdescrip=a)
    f = Bidding.objects.filter(jobid=jobid).update(descript40b=a, descript40="")
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "f": f,
    }
    return render(request, 'mha/addnewosr.html', context)


def newvendorprice(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_osrunitprice']
    b = OutsideResource.objects.values_list("id", flat=True).last()
    e = OutsideResource.objects.filter(id=b).update(osrunitprice=a)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'mha/addnewosr.html', context)


def newvendor(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_osrvendor']
    b = OutsideResource.objects.values_list("id", flat=True).last()
    e = OutsideResource.objects.filter(id=b).update(osrvendor=a)
    context = {
        "instance": instance,
        "form": form,
        "e": e,
    }
    return render(request, 'mha/addnewosr.html', context)


#    return redirect(instance.get_absolute27_url(), context)


def addnewosr(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/addnewosr.html', context)


def deletenewvendor(request, jobid=None):
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    a = OutsideResource.objects.values_list('id', flat=True).last()
    c = OutsideResource.objects.filter(id=a).delete()
    context = {
        "form": form,
        'c': c,
    }
    return redirect(instance.get_absolute27_url(), context)


def quan1(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=1).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity1']
    Bidding.objects.filter(bidid=bidid).update(quanity1=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost1total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=1, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=1, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan2(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=2).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity2']
    Bidding.objects.filter(bidid=bidid).update(quanity2=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity2', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost2total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=2, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=2, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan3(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=3).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity3']
    Bidding.objects.filter(bidid=bidid).update(quanity3=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity3', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost3total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=3, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=3, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan4(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=4).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity4']
    Bidding.objects.filter(bidid=bidid).update(quanity4=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity4', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost4total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=4, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=4, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan5(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=5).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity5']
    Bidding.objects.filter(bidid=bidid).update(quanity5=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost5total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=5, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=5, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan6(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=6).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity6']
    Bidding.objects.filter(bidid=bidid).update(quanity6=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost6total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=6, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=6, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def quan7(request, bidid=None):
    FilterEquipType.objects.all().delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=7).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity7']
    Bidding.objects.filter(bidid=bidid).update(quanity7=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost7total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(id=h, bidid=bidid, descripid=7, jobcost=e)
    j = SelectedEquip.objects.filter(equipid=7, bidid=bidid).update(quanity=a, cost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'j': j,
    }
    return render(request, 'mha/bidpage.html', context)


def descript8(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript8'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript8b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript8(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript8 = Bidding.objects.values_list('descript8', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript8": descript8,
        "form": form,
    }
    return render(request, 'mha/descript8_1.html', context)


def load_descript8b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript8b = Bidding.objects.values_list('descript8b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript8b": descript8b,
        "form": form,
    }
    return render(request, 'mha/descript8b_1.html', context)


def quant8(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=8).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=8).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity8']
    Bidding.objects.filter(bidid=bidid).update(quanity8=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript8b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity8', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=8, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=8, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity8=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript8b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity8', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost8total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=8, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=8, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity8(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity8 = Bidding.objects.filter(bidid=bidid).values_list('quanity8', flat=True)
    context = {
        "instance": instance,
        "quanity8": quanity8,
        "form": form,
    }
    return render(request, 'mha/quan8_1.html', context)


def delete8(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity8=0, descript8b="", cost8total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=8).delete()
    MatCost.objects.filter(bidid=bidid, descript=8).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript9(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript9'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript9b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript9(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript9 = Bidding.objects.values_list('descript9', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript9": descript9,
        "form": form,
    }
    return render(request, 'mha/descript9_1.html', context)


def load_descript9b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript9b = Bidding.objects.values_list('descript9b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript9b": descript9b,
        "form": form,
    }
    return render(request, 'mha/descript9b_1.html', context)


def quant9(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=9).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=9).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity9']
    Bidding.objects.filter(bidid=bidid).update(quanity9=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript9b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity9', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=9, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=9, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity9=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript9b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity9', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost9total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=9, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=9, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity9(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity9 = Bidding.objects.filter(bidid=bidid).values_list('quanity9', flat=True)
    context = {
        "instance": instance,
        "quanity9": quanity9,
        "form": form,
    }
    return render(request, 'mha/quan9_1.html', context)


def delete9(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity9=0, descript9b="", cost9total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=9).delete()
    MatCost.objects.filter(bidid=bidid, descript=9).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript10(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript10'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript10b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript10(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript10 = Bidding.objects.values_list('descript10', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript10": descript10,
        "form": form,
    }
    return render(request, 'mha/descript10_1.html', context)


def load_descript10b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript10b = Bidding.objects.values_list('descript10b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript10b": descript10b,
        "form": form,
    }
    return render(request, 'mha/descript10b_1.html', context)


def quant10(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=10).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=10).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity10']
    Bidding.objects.filter(bidid=bidid).update(quanity10=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript10b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity10', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=10, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=10, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity10=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript10b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity10', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost10total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=10, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=10, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity10(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity10 = Bidding.objects.filter(bidid=bidid).values_list('quanity10', flat=True)
    context = {
        "instance": instance,
        "quanity10": quanity10,
        "form": form,
    }
    return render(request, 'mha/quan10_1.html', context)


def delete10(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity10=0, descript10b="", cost10total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=10).delete()
    MatCost.objects.filter(bidid=bidid, descript=10).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript11(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript11'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript11b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript11(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript11 = Bidding.objects.values_list('descript11', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript11": descript11,
        "form": form,
    }
    return render(request, 'mha/descript11_1.html', context)


def load_descript11b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript11b = Bidding.objects.values_list('descript11b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript11b": descript11b,
        "form": form,
    }
    return render(request, 'mha/descript11b_1.html', context)


def quant11(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=11).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=11).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity11']
    Bidding.objects.filter(bidid=bidid).update(quanity11=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript11b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity11', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=11, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=11, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity11=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript11b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity11', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost11total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=11, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=11, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity11(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity11 = Bidding.objects.filter(bidid=bidid).values_list('quanity11', flat=True)
    context = {
        "instance": instance,
        "quanity11": quanity11,
        "form": form,
    }
    return render(request, 'mha/quan11_1.html', context)


def delete11(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity11=0, descript11b="", cost11total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=11).delete()
    MatCost.objects.filter(bidid=bidid, descript=11).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript12(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript12'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript12b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript12(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript12 = Bidding.objects.values_list('descript12', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript12": descript12,
        "form": form,
    }
    return render(request, 'mha/descript12_1.html', context)


def load_descript12b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript12b = Bidding.objects.values_list('descript12b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript12b": descript12b,
        "form": form,
    }
    return render(request, 'mha/descript12b_1.html', context)


def quant12(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=12).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=12).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity12']
    Bidding.objects.filter(bidid=bidid).update(quanity12=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript12b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity12', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=12, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=12, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity12=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript12b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity12', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost12total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=12, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=12, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity12(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity12 = Bidding.objects.filter(bidid=bidid).values_list('quanity12', flat=True)
    context = {
        "instance": instance,
        "quanity12": quanity12,
        "form": form,
    }
    return render(request, 'mha/quan12_1.html', context)


def delete12(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity12=0, descript12b="", cost12total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=12).delete()
    MatCost.objects.filter(bidid=bidid, descript=12).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript13(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript13'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript13b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript13(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript13 = Bidding.objects.values_list('descript13', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript13": descript13,
        "form": form,
    }
    return render(request, 'mha/descript13_1.html', context)


def load_descript13b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript13b = Bidding.objects.values_list('descript13b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript13b": descript13b,
        "form": form,
    }
    return render(request, 'mha/descript13b_1.html', context)


def quant13(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=13).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=13).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity13']
    Bidding.objects.filter(bidid=bidid).update(quanity13=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript13b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity13', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=13, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=13, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity13=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript13b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity13', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost13total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=13, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=13, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity13(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity13 = Bidding.objects.filter(bidid=bidid).values_list('quanity13', flat=True)
    context = {
        "instance": instance,
        "quanity13": quanity13,
        "form": form,
    }
    return render(request, 'mha/quan13_1.html', context)


def delete13(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity13=0, descript13b="", cost13total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=13).delete()
    MatCost.objects.filter(bidid=bidid, descript=13).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript14(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript14'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript14b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript14(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript14 = Bidding.objects.values_list('descript14', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript14": descript14,
        "form": form,
    }
    return render(request, 'mha/descript14_1.html', context)


def load_descript14b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript14b = Bidding.objects.values_list('descript14b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript14b": descript14b,
        "form": form,
    }
    return render(request, 'mha/descript14b_1.html', context)


def quant14(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=14).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=14).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity14']
    Bidding.objects.filter(bidid=bidid).update(quanity14=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript14b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity14', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=14, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=14, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity14=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript14b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity14', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost14total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=14, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=14, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity14(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity14 = Bidding.objects.filter(bidid=bidid).values_list('quanity14', flat=True)
    context = {
        "instance": instance,
        "quanity14": quanity14,
        "form": form,
    }
    return render(request, 'mha/quan14_1.html', context)


def delete14(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity14=0, descript14b="", cost14total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=14).delete()
    MatCost.objects.filter(bidid=bidid, descript=14).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript15(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript15'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript15b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript15(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript15 = Bidding.objects.values_list('descript15', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript15": descript15,
        "form": form,
    }
    return render(request, 'mha/descript15_1.html', context)


def load_descript15b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript15b = Bidding.objects.values_list('descript15b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript15b": descript15b,
        "form": form,
    }
    return render(request, 'mha/descript15b_1.html', context)


def quant15(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=15).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=15).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity15']
    Bidding.objects.filter(bidid=bidid).update(quanity15=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript15b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity15', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=15, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=15, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity15=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript15b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity15', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost15total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=15, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=15, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity15(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity15 = Bidding.objects.filter(bidid=bidid).values_list('quanity15', flat=True)
    context = {
        "instance": instance,
        "quanity15": quanity15,
        "form": form,
    }
    return render(request, 'mha/quan15_1.html', context)


def delete15(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity15=0, descript15b="", cost15total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=15).delete()
    MatCost.objects.filter(bidid=bidid, descript=15).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript16(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript16'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript16b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript16(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript16 = Bidding.objects.values_list('descript16', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript16": descript16,
        "form": form,
    }
    return render(request, 'mha/descript16_1.html', context)


def load_descript16b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript16b = Bidding.objects.values_list('descript16b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript16b": descript16b,
        "form": form,
    }
    return render(request, 'mha/descript16b_1.html', context)


def quant16(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=16).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=16).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity16']
    Bidding.objects.filter(bidid=bidid).update(quanity16=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript16b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity16', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=16, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=16, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity16=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript16b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity16', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost16total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=16, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=16, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity16(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity16 = Bidding.objects.filter(bidid=bidid).values_list('quanity16', flat=True)
    context = {
        "instance": instance,
        "quanity16": quanity16,
        "form": form,
    }
    return render(request, 'mha/quan16_1.html', context)


def delete16(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity16=0, descript16b="", cost16total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=16).delete()
    MatCost.objects.filter(bidid=bidid, descript=16).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript17(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript17'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript17b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript17(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript17 = Bidding.objects.values_list('descript17', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript17": descript17,
        "form": form,
    }
    return render(request, 'mha/descript17_1.html', context)


def load_descript17b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript17b = Bidding.objects.values_list('descript17b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript17b": descript17b,
        "form": form,
    }
    return render(request, 'mha/descript17b_1.html', context)


def quant17(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=17).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=17).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity17']
    Bidding.objects.filter(bidid=bidid).update(quanity17=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript17b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity17', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=17, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=17, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity17=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript17b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity17', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost17total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=17, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=17, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity17(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity17 = Bidding.objects.filter(bidid=bidid).values_list('quanity17', flat=True)
    context = {
        "instance": instance,
        "quanity17": quanity17,
        "form": form,
    }
    return render(request, 'mha/quan17_1.html', context)


def delete17(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity17=0, descript17b="", cost17total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=17).delete()
    MatCost.objects.filter(bidid=bidid, descript=17).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript18(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript18'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript18b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript18(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript18 = Bidding.objects.values_list('descript18', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript18": descript18,
        "form": form,
    }
    return render(request, 'mha/descript18_1.html', context)


def load_descript18b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript18b = Bidding.objects.values_list('descript18b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript18b": descript18b,
        "form": form,
    }
    return render(request, 'mha/descript18b_1.html', context)


def quant18(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=18).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=18).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity18']
    Bidding.objects.filter(bidid=bidid).update(quanity18=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript18b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity18', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=18, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=18, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity18=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript18b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity18', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost18total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=18, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=18, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity18(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity18 = Bidding.objects.filter(bidid=bidid).values_list('quanity18', flat=True)
    context = {
        "instance": instance,
        "quanity18": quanity18,
        "form": form,
    }
    return render(request, 'mha/quan18_1.html', context)


def delete18(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity18=0, descript18b="", cost18total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=18).delete()
    MatCost.objects.filter(bidid=bidid, descript=18).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript19(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript19'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript19b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript19(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript19 = Bidding.objects.values_list('descript19', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript19": descript19,
        "form": form,
    }
    return render(request, 'mha/descript19_1.html', context)


def load_descript19b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript19b = Bidding.objects.values_list('descript19b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript19b": descript19b,
        "form": form,
    }
    return render(request, 'mha/descript19b_1.html', context)


def quant19(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=19).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=19).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity19']
    Bidding.objects.filter(bidid=bidid).update(quanity19=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript19b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity19', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=19, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=19, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity19=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript19b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity19', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost19total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=19, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=19, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity19(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity19 = Bidding.objects.filter(bidid=bidid).values_list('quanity19', flat=True)
    context = {
        "instance": instance,
        "quanity19": quanity19,
        "form": form,
    }
    return render(request, 'mha/quan19_1.html', context)


def delete19(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity19=0, descript19b="", cost19total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=19).delete()
    MatCost.objects.filter(bidid=bidid, descript=19).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript20(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript20'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript20b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript20(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript20 = Bidding.objects.values_list('descript20', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript20": descript20,
        "form": form,
    }
    return render(request, 'mha/descript20_1.html', context)


def load_descript20b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript20b = Bidding.objects.values_list('descript20b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript20b": descript20b,
        "form": form,
    }
    return render(request, 'mha/descript20b_1.html', context)


def quant20(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=20).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=20).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity20']
    Bidding.objects.filter(bidid=bidid).update(quanity20=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript20b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity20', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=20, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=20, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity20=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript20b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity20', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost20total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=20, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=20, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity20(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity20 = Bidding.objects.filter(bidid=bidid).values_list('quanity20', flat=True)
    context = {
        "instance": instance,
        "quanity20": quanity20,
        "form": form,
    }
    return render(request, 'mha/quan20_1.html', context)


def delete20(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity20=0, descript20b="", cost20total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=20).delete()
    MatCost.objects.filter(bidid=bidid, descript=20).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript21(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript21'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript21b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript21(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript21 = Bidding.objects.values_list('descript21', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript21": descript21,
        "form": form,
    }
    return render(request, 'mha/descript21_1.html', context)


def load_descript21b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript21b = Bidding.objects.values_list('descript21b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript21b": descript21b,
        "form": form,
    }
    return render(request, 'mha/descript21b_1.html', context)


def quant21(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=21).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=21).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity21']
    Bidding.objects.filter(bidid=bidid).update(quanity21=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript21b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity21', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=21, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=21, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity21=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript21b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity21', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost21total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=21, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=21, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity21(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity21 = Bidding.objects.filter(bidid=bidid).values_list('quanity21', flat=True)
    context = {
        "instance": instance,
        "quanity21": quanity21,
        "form": form,
    }
    return render(request, 'mha/quan21_1.html', context)


def delete21(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity21=0, descript21b="", cost21total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=21).delete()
    MatCost.objects.filter(bidid=bidid, descript=21).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript22(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript22'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript22b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript22(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript22 = Bidding.objects.values_list('descript22', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript22": descript22,
        "form": form,
    }
    return render(request, 'mha/descript22_1.html', context)


def load_descript22b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript22b = Bidding.objects.values_list('descript22b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript22b": descript22b,
        "form": form,
    }
    return render(request, 'mha/descript22b_1.html', context)


def quant22(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=22).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=22).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity22']
    Bidding.objects.filter(bidid=bidid).update(quanity22=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript22b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity22', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=22, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=22, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity22=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript22b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity22', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost22total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=22, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=22, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity22(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity22 = Bidding.objects.filter(bidid=bidid).values_list('quanity22', flat=True)
    context = {
        "instance": instance,
        "quanity22": quanity22,
        "form": form,
    }
    return render(request, 'mha/quan22_1.html', context)


def delete22(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity22=0, descript22b="", cost22total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=22).delete()
    MatCost.objects.filter(bidid=bidid, descript=22).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript23(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript23'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript23b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript23(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript23 = Bidding.objects.values_list('descript23', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript23": descript23,
        "form": form,
    }
    return render(request, 'mha/descript23_1.html', context)


def load_descript23b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript23b = Bidding.objects.values_list('descript23b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript23b": descript23b,
        "form": form,
    }
    return render(request, 'mha/descript23b_1.html', context)


def quant23(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=23).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=23).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity23']
    Bidding.objects.filter(bidid=bidid).update(quanity23=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript23b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity23', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=23, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=23, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity23=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript23b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity23', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost23total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=23, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=23, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity23(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity23 = Bidding.objects.filter(bidid=bidid).values_list('quanity23', flat=True)
    context = {
        "instance": instance,
        "quanity23": quanity23,
        "form": form,
    }
    return render(request, 'mha/quan23_1.html', context)


def delete23(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity23=0, descript23b="", cost23total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=23).delete()
    MatCost.objects.filter(bidid=bidid, descript=23).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript24(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript24'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript24b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript24(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript24 = Bidding.objects.values_list('descript24', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript24": descript24,
        "form": form,
    }
    return render(request, 'mha/descript24_1.html', context)


def load_descript24b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript24b = Bidding.objects.values_list('descript24b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript24b": descript24b,
        "form": form,
    }
    return render(request, 'mha/descript24b_1.html', context)


def quant24(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=24).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=24).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity24']
    Bidding.objects.filter(bidid=bidid).update(quanity24=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript24b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity24', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=24, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=24, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity24=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript24b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity24', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost24total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=24, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=24, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity24(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity24 = Bidding.objects.filter(bidid=bidid).values_list('quanity24', flat=True)
    context = {
        "instance": instance,
        "quanity24": quanity24,
        "form": form,
    }
    return render(request, 'mha/quan24_1.html', context)


def delete24(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity24=0, descript24b="", cost24total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=24).delete()
    MatCost.objects.filter(bidid=bidid, descript=24).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript25(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript25'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript25b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript25(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript25 = Bidding.objects.values_list('descript25', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript25": descript25,
        "form": form,
    }
    return render(request, 'mha/descript25_1.html', context)


def load_descript25b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript25b = Bidding.objects.values_list('descript25b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript25b": descript25b,
        "form": form,
    }
    return render(request, 'mha/descript25b_1.html', context)


def quant25(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=25).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=25).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity25']
    Bidding.objects.filter(bidid=bidid).update(quanity25=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript25b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity25', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=25, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=25, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity25=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript25b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity25', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost25total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=25, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=25, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity25(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity25 = Bidding.objects.filter(bidid=bidid).values_list('quanity25', flat=True)
    context = {
        "instance": instance,
        "quanity25": quanity25,
        "form": form,
    }
    return render(request, 'mha/quan25_1.html', context)


def delete25(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity25=0, descript25b="", cost25total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=25).delete()
    MatCost.objects.filter(bidid=bidid, descript=25).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript26(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript26'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript26b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript26(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript26 = Bidding.objects.values_list('descript26', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript26": descript26,
        "form": form,
    }
    return render(request, 'mha/descript26_1.html', context)


def load_descript26b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript26b = Bidding.objects.values_list('descript26b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript26b": descript26b,
        "form": form,
    }
    return render(request, 'mha/descript26b_1.html', context)


def quant26(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=26).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=26).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity26']
    Bidding.objects.filter(bidid=bidid).update(quanity26=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript26b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity26', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=26, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=26, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity26=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript26b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity26', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost26total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=26, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=26, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity26(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity26 = Bidding.objects.filter(bidid=bidid).values_list('quanity26', flat=True)
    context = {
        "instance": instance,
        "quanity26": quanity26,
        "form": form,
    }
    return render(request, 'mha/quan26_1.html', context)


def delete26(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity26=0, descript26b="", cost26total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=26).delete()
    MatCost.objects.filter(bidid=bidid, descript=26).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript27(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript27'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript27b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript27(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript27 = Bidding.objects.values_list('descript27', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript27": descript27,
        "form": form,
    }
    return render(request, 'mha/descript27_1.html', context)


def load_descript27b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript27b = Bidding.objects.values_list('descript27b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript27b": descript27b,
        "form": form,
    }
    return render(request, 'mha/descript27b_1.html', context)


def quant27(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=27).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=27).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity27']
    Bidding.objects.filter(bidid=bidid).update(quanity27=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript27b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity27', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=27, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=27, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity27=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript27b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity27', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost27total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=27, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=27, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity27(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity27 = Bidding.objects.filter(bidid=bidid).values_list('quanity27', flat=True)
    context = {
        "instance": instance,
        "quanity27": quanity27,
        "form": form,
    }
    return render(request, 'mha/quan27_1.html', context)


def delete27(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity27=0, descript27b="", cost27total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=27).delete()
    MatCost.objects.filter(bidid=bidid, descript=27).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript28(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript28'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript28b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript28(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript28 = Bidding.objects.values_list('descript28', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript28": descript28,
        "form": form,
    }
    return render(request, 'mha/descript28_1.html', context)


def load_descript28b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript28b = Bidding.objects.values_list('descript28b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript28b": descript28b,
        "form": form,
    }
    return render(request, 'mha/descript28b_1.html', context)


def quant28(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=28).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=28).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity28']
    Bidding.objects.filter(bidid=bidid).update(quanity28=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript28b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity28', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=28, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=28, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity28=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript28b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity28', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost28total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=28, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=28, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity28(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity28 = Bidding.objects.filter(bidid=bidid).values_list('quanity28', flat=True)
    context = {
        "instance": instance,
        "quanity28": quanity28,
        "form": form,
    }
    return render(request, 'mha/quan28_1.html', context)


def delete28(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity28=0, descript28b="", cost28total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=28).delete()
    MatCost.objects.filter(bidid=bidid, descript=28).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript29(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript29'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript29b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript29(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript29 = Bidding.objects.values_list('descript29', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript29": descript29,
        "form": form,
    }
    return render(request, 'mha/descript29_1.html', context)


def load_descript29b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript29b = Bidding.objects.values_list('descript29b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript29b": descript29b,
        "form": form,
    }
    return render(request, 'mha/descript29b_1.html', context)


def quant29(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=29).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=29).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity29']
    Bidding.objects.filter(bidid=bidid).update(quanity29=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript29b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity29', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=29, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=29, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity29=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript29b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity29', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost29total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=29, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=29, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity29(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity29 = Bidding.objects.filter(bidid=bidid).values_list('quanity29', flat=True)
    context = {
        "instance": instance,
        "quanity29": quanity29,
        "form": form,
    }
    return render(request, 'mha/quan29_1.html', context)


def delete29(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity29=0, descript29b="", cost29total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=29).delete()
    MatCost.objects.filter(bidid=bidid, descript=29).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript30(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript30'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript30b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript30(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript30 = Bidding.objects.values_list('descript30', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript30": descript30,
        "form": form,
    }
    return render(request, 'mha/descript30_1.html', context)


def load_descript30b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript30b = Bidding.objects.values_list('descript30b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript30b": descript30b,
        "form": form,
    }
    return render(request, 'mha/descript30b_1.html', context)


def quant30(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=30).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=30).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity30']
    Bidding.objects.filter(bidid=bidid).update(quanity30=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript30b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity30', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=30, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=30, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity30=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript30b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity30', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost30total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=30, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=30, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity30(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity30 = Bidding.objects.filter(bidid=bidid).values_list('quanity30', flat=True)
    context = {
        "instance": instance,
        "quanity30": quanity30,
        "form": form,
    }
    return render(request, 'mha/quan30_1.html', context)


def delete30(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity30=0, descript30b="", cost30total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=30).delete()
    MatCost.objects.filter(bidid=bidid, descript=30).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript31(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript31'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript31b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript31(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript31 = Bidding.objects.values_list('descript31', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript31": descript31,
        "form": form,
    }
    return render(request, 'mha/descript31_1.html', context)


def load_descript31b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript31b = Bidding.objects.values_list('descript31b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript31b": descript31b,
        "form": form,
    }
    return render(request, 'mha/descript31b_1.html', context)


def quant31(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=31).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=31).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity31']
    Bidding.objects.filter(bidid=bidid).update(quanity31=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript31b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity31', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=31, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=31, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity31=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript31b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity31', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost31total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=31, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=31, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity31(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity31 = Bidding.objects.filter(bidid=bidid).values_list('quanity31', flat=True)
    context = {
        "instance": instance,
        "quanity31": quanity31,
        "form": form,
    }
    return render(request, 'mha/quan31_1.html', context)


def delete31(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity31=0, descript31b="", cost31total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=31).delete()
    MatCost.objects.filter(bidid=bidid, descript=31).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript32(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript32'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript32b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript32(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript32 = Bidding.objects.values_list('descript32', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript32": descript32,
        "form": form,
    }
    return render(request, 'mha/descript32_1.html', context)


def load_descript32b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript32b = Bidding.objects.values_list('descript32b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript32b": descript32b,
        "form": form,
    }
    return render(request, 'mha/descript32b_1.html', context)


def quant32(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=32).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=32).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity32']
    Bidding.objects.filter(bidid=bidid).update(quanity32=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript32b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity32', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=32, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=32, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity32=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript32b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity32', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost32total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=32, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=32, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity32(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity32 = Bidding.objects.filter(bidid=bidid).values_list('quanity32', flat=True)
    context = {
        "instance": instance,
        "quanity32": quanity32,
        "form": form,
    }
    return render(request, 'mha/quan32_1.html', context)


def delete32(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity32=0, descript32b="", cost32total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=32).delete()
    MatCost.objects.filter(bidid=bidid, descript=32).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript33(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript33'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript33b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript33(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript33 = Bidding.objects.values_list('descript33', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript33": descript33,
        "form": form,
    }
    return render(request, 'mha/descript33_1.html', context)


def load_descript33b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript33b = Bidding.objects.values_list('descript33b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript33b": descript33b,
        "form": form,
    }
    return render(request, 'mha/descript33b_1.html', context)


def quant33(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=33).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=33).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity33']
    Bidding.objects.filter(bidid=bidid).update(quanity33=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript33b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity33', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=33, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=33, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity33=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript33b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity33', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost33total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=33, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=33, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity33(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity33 = Bidding.objects.filter(bidid=bidid).values_list('quanity33', flat=True)
    context = {
        "instance": instance,
        "quanity33": quanity33,
        "form": form,
    }
    return render(request, 'mha/quan33_1.html', context)


def delete33(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity33=0, descript33b="", cost33total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=33).delete()
    MatCost.objects.filter(bidid=bidid, descript=33).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript34(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript34'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript34b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript34(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript34 = Bidding.objects.values_list('descript34', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript34": descript34,
        "form": form,
    }
    return render(request, 'mha/descript34_1.html', context)


def load_descript34b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript34b = Bidding.objects.values_list('descript34b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript34b": descript34b,
        "form": form,
    }
    return render(request, 'mha/descript34b_1.html', context)


def quant34(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=34).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=34).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity34']
    Bidding.objects.filter(bidid=bidid).update(quanity34=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript34b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity34', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=34, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=34, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity34=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript34b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity34', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost34total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=34, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=34, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity34(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity34 = Bidding.objects.filter(bidid=bidid).values_list('quanity34', flat=True)
    context = {
        "instance": instance,
        "quanity34": quanity34,
        "form": form,
    }
    return render(request, 'mha/quan34_1.html', context)


def delete34(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity34=0, descript34b="", cost34total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=34).delete()
    MatCost.objects.filter(bidid=bidid, descript=34).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript35(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript35'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript35b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript35(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript35 = Bidding.objects.values_list('descript35', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript35": descript35,
        "form": form,
    }
    return render(request, 'mha/descript35_1.html', context)


def load_descript35b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript35b = Bidding.objects.values_list('descript35b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript35b": descript35b,
        "form": form,
    }
    return render(request, 'mha/descript35b_1.html', context)


def quant35(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=35).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=35).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity35']
    Bidding.objects.filter(bidid=bidid).update(quanity35=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript35b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity35', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=35, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=35, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity35=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript35b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity35', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost35total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=35, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=35, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity35(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity35 = Bidding.objects.filter(bidid=bidid).values_list('quanity35', flat=True)
    context = {
        "instance": instance,
        "quanity35": quanity35,
        "form": form,
    }
    return render(request, 'mha/quan35_1.html', context)


def delete35(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity35=0, descript35b="", cost35total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=35).delete()
    MatCost.objects.filter(bidid=bidid, descript=35).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript36(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript36'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript36b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript36(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript36 = Bidding.objects.values_list('descript36', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript36": descript36,
        "form": form,
    }
    return render(request, 'mha/descript36_1.html', context)


def load_descript36b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript36b = Bidding.objects.values_list('descript36b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript36b": descript36b,
        "form": form,
    }
    return render(request, 'mha/descript36b_1.html', context)


def quant36(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=36).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=36).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity36']
    Bidding.objects.filter(bidid=bidid).update(quanity36=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript36b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity36', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=36, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=36, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity36=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript36b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity36', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost36total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=36, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=36, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity36(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity36 = Bidding.objects.filter(bidid=bidid).values_list('quanity36', flat=True)
    context = {
        "instance": instance,
        "quanity36": quanity36,
        "form": form,
    }
    return render(request, 'mha/quan36_1.html', context)


def delete36(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity36=0, descript36b="", cost36total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=36).delete()
    MatCost.objects.filter(bidid=bidid, descript=36).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript37(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript37'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript37b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript37(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript37 = Bidding.objects.values_list('descript37', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript37": descript37,
        "form": form,
    }
    return render(request, 'mha/descript37_1.html', context)


def load_descript37b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript37b = Bidding.objects.values_list('descript37b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript37b": descript37b,
        "form": form,
    }
    return render(request, 'mha/descript37b_1.html', context)


def quant37(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=37).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=37).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity37']
    Bidding.objects.filter(bidid=bidid).update(quanity37=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript37b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity37', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=37, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=37, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity37=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript37b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity37', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost37total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=37, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=37, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity37(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity37 = Bidding.objects.filter(bidid=bidid).values_list('quanity37', flat=True)
    context = {
        "instance": instance,
        "quanity37": quanity37,
        "form": form,
    }
    return render(request, 'mha/quan37_1.html', context)


def delete37(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity37=0, descript37b="", cost37total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=37).delete()
    MatCost.objects.filter(bidid=bidid, descript=37).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript38(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript38'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript38b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript38(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript38 = Bidding.objects.values_list('descript38', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript38": descript38,
        "form": form,
    }
    return render(request, 'mha/descript38_1.html', context)


def load_descript38b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript38b = Bidding.objects.values_list('descript38b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript38b": descript38b,
        "form": form,
    }
    return render(request, 'mha/descript38b_1.html', context)


def quant38(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=38).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=38).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity38']
    Bidding.objects.filter(bidid=bidid).update(quanity38=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript38b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity38', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=38, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=38, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity38=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript38b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity38', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost38total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=38, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=38, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity38(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity38 = Bidding.objects.filter(bidid=bidid).values_list('quanity38', flat=True)
    context = {
        "instance": instance,
        "quanity38": quanity38,
        "form": form,
    }
    return render(request, 'mha/quan38_1.html', context)


def delete38(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity38=0, descript38b="", cost38total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=38).delete()
    MatCost.objects.filter(bidid=bidid, descript=38).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript39(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript39'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript39b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript39(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript39 = Bidding.objects.values_list('descript39', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript39": descript39,
        "form": form,
    }
    return render(request, 'mha/descript39_1.html', context)


def load_descript39b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript39b = Bidding.objects.values_list('descript39b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript39b": descript39b,
        "form": form,
    }
    return render(request, 'mha/descript39b_1.html', context)


def quant39(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=39).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=39).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity39']
    Bidding.objects.filter(bidid=bidid).update(quanity39=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript39b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity39', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=39, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=39, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity39=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript39b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity39', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost39total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=39, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=39, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity39(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity39 = Bidding.objects.filter(bidid=bidid).values_list('quanity39', flat=True)
    context = {
        "instance": instance,
        "quanity39": quanity39,
        "form": form,
    }
    return render(request, 'mha/quan39_1.html', context)


def delete39(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity39=0, descript39b="", cost39total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=39).delete()
    MatCost.objects.filter(bidid=bidid, descript=39).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descript46(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript46'] or 0
    b = MatTypeBid.objects.filter(id=a).values_list("type")
    Bidding.objects.filter(bidid=bidid).update(descript46b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def load_descript46(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript46 = Bidding.objects.values_list('descript46', flat=True).get(bidid=bidid)
    context = {
        "instance": instance,
        "descript46": descript46,
        "form": form,
    }
    return render(request, 'mha/descript46_1.html', context)


def load_descript46b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript46b = Bidding.objects.values_list('descript46b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript46b": descript46b,
        "form": form,
    }
    return render(request, 'mha/descript46b_1.html', context)


def quant46(request, bidid=None):
    MatCost.objects.filter(bidid=bidid, descript=46).delete()
    TotalJobCost.objects.filter(bidid=bidid, descripid=46).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity46']
    Bidding.objects.filter(bidid=bidid).update(quanity46=a)
    aa = Bidding.objects.filter(bidid=bidid).values_list('mattype', flat=True).first()
    if aa == '2':
        bb = Bidding.objects.filter(bidid=bidid).values_list('descript46b', flat=True).first()
        cc = MatTypeBid.objects.filter(type=bb).values_list('unitcost', flat=True).first()
        dd = Bidding.objects.filter(bidid=bidid).values_list('quanity46', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        ee = cc * dd
        ff = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        gg = ff + 1
        hh = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=gg, bidid=bidid, descripid=46, jobcost=ee)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=46, matcost=ee)
        context = {
            "instance": instance,
            "form": form,
            'hh': hh,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)
    else:
        Bidding.objects.filter(bidid=bidid).update(quanity46=a)
        b = Bidding.objects.filter(bidid=bidid).values_list('descript46b', flat=True).first()
        c = Material.objects.filter(descrip=b).values_list('cost', flat=True).first()
        d = Bidding.objects.filter(bidid=bidid).values_list('quanity46', flat=True).first()
        dd1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
        dd2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
        dd3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
        e = c * d
        f = Bidding.objects.filter(bidid=bidid).update(cost46total=e)
        g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
        h = g + 1
        i = TotalJobCost.objects.create(conid=dd1, custid=dd2, id=h, bidid=bidid, descripid=46, jobcost=e)
        ii = MatCost.objects.create(conid=dd1, custid=dd2, jobid=dd3, bidid=bidid, descript=46, matcost=e)
        context = {
            "instance": instance,
            "form": form,
            'f': f,
            'i': i,
            'ii': ii,
        }
        return render(request, 'mha/bidpage.html', context)


def load_quanity46(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity46 = Bidding.objects.filter(bidid=bidid).values_list('quanity46', flat=True)
    context = {
        "instance": instance,
        "quanity46": quanity46,
        "form": form,
    }
    return render(request, 'mha/quan46_1.html', context)


def delete46(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity46=0, descript46b="", cost46total=0)
    TotalJobCost.objects.filter(bidid=bidid, descripid=46).delete()
    MatCost.objects.filter(bidid=bidid, descript=46).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def descrip40(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript40']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript40b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip40b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript40']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript40=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan40(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=40).delete()
    OSRCost.objects.filter(bidid=bidid, descript=40).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity40']
    Bidding.objects.filter(bidid=bidid).update(quanity40=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript40b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity40', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost40total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=40, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=40, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete40(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity40=0, descript40="", descript40b="", cost40total=0)
    TotalJobCost.objects.filter(descripid=40).delete()
    OSRCost.objects.filter(bidid=bidid, descript=40).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript40(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript40 = Bidding.objects.filter(bidid=bidid).values_list('descript40', flat=True)
    context = {
        "instance": instance,
        "descript40": descript40,
        "form": form,
    }
    return render(request, 'mha/descript40_1.html', context)


def load_descript40b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript40b = Bidding.objects.values_list('descript40b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript40b": descript40b,
        "form": form,
    }
    return render(request, 'mha/descript40b_1.html', context)


def load_quanity40(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity40 = Bidding.objects.filter(bidid=bidid).values_list('quanity40', flat=True)
    context = {
        "instance": instance,
        "quanity40": quanity40,
        "form": form,
    }
    return render(request, 'mha/quan40_1.html', context)


def descrip41(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript41']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript41b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip41b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript41']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript41=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan41(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=41).delete()
    OSRCost.objects.filter(bidid=bidid, descript=41).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity41']
    Bidding.objects.filter(bidid=bidid).update(quanity41=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript41b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity41', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost41total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=41, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=41, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete41(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity41=0, descript41="", descript41b="", cost41total=0)
    TotalJobCost.objects.filter(descripid=41).delete()
    OSRCost.objects.filter(bidid=bidid, descript=41).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript41(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript41 = Bidding.objects.filter(bidid=bidid).values_list('descript41', flat=True)
    context = {
        "instance": instance,
        "descript41": descript41,
        "form": form,
    }
    return render(request, 'mha/descript41_1.html', context)


def load_descript41b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript41b = Bidding.objects.values_list('descript41b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript41b": descript41b,
        "form": form,
    }
    return render(request, 'mha/descript41b_1.html', context)


def load_quanity41(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity41 = Bidding.objects.filter(bidid=bidid).values_list('quanity41', flat=True)
    context = {
        "instance": instance,
        "quanity41": quanity41,
        "form": form,
    }
    return render(request, 'mha/quan41_1.html', context)


def descrip42(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript42']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript42b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip42b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript42']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript42=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan42(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=42).delete()
    OSRCost.objects.filter(bidid=bidid, descript=42).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity42']
    Bidding.objects.filter(bidid=bidid).update(quanity42=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript42b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity42', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost42total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=42, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=42, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete42(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity42=0, descript42="", descript42b="", cost42total=0)
    TotalJobCost.objects.filter(descripid=42).delete()
    OSRCost.objects.filter(bidid=bidid, descript=42).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript42(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript42 = Bidding.objects.filter(bidid=bidid).values_list('descript42', flat=True)
    context = {
        "instance": instance,
        "descript42": descript42,
        "form": form,
    }
    return render(request, 'mha/descript42_1.html', context)


def load_descript42b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript42b = Bidding.objects.values_list('descript42b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript42b": descript42b,
        "form": form,
    }
    return render(request, 'mha/descript42b_1.html', context)


def load_quanity42(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity42 = Bidding.objects.filter(bidid=bidid).values_list('quanity42', flat=True)
    context = {
        "instance": instance,
        "quanity42": quanity42,
        "form": form,
    }
    return render(request, 'mha/quan42_1.html', context)


def descrip43(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript43']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript43b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip43b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript43']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript43=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan43(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=43).delete()
    OSRCost.objects.filter(bidid=bidid, descript=43).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity43']
    Bidding.objects.filter(bidid=bidid).update(quanity43=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript43b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity43', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost43total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=43, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=43, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete43(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity43=0, descript43="", descript43b="", cost43total=0)
    TotalJobCost.objects.filter(descripid=43).delete()
    OSRCost.objects.filter(bidid=bidid, descript=43).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript43(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript43 = Bidding.objects.filter(bidid=bidid).values_list('descript43', flat=True)
    context = {
        "instance": instance,
        "descript43": descript43,
        "form": form,
    }
    return render(request, 'mha/descript43_1.html', context)


def load_descript43b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript43b = Bidding.objects.values_list('descript43b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript43b": descript43b,
        "form": form,
    }
    return render(request, 'mha/descript43b_1.html', context)


def load_quanity43(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity43 = Bidding.objects.filter(bidid=bidid).values_list('quanity43', flat=True)
    context = {
        "instance": instance,
        "quanity43": quanity43,
        "form": form,
    }
    return render(request, 'mha/quan43_1.html', context)


def descrip44(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript44']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript44b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip44b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript44']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript44=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan44(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=44).delete()
    OSRCost.objects.filter(bidid=bidid, descript=44).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity44']
    Bidding.objects.filter(bidid=bidid).update(quanity44=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript44b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity44', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost44total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=44, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=44, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete44(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity44=0, descript44="", descript44b="", cost44total=0)
    TotalJobCost.objects.filter(descripid=44).delete()
    OSRCost.objects.filter(bidid=bidid, descript=44).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript44(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript44 = Bidding.objects.filter(bidid=bidid).values_list('descript44', flat=True)
    context = {
        "instance": instance,
        "descript44": descript44,
        "form": form,
    }
    return render(request, 'mha/descript44_1.html', context)


def load_descript44b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript44b = Bidding.objects.values_list('descript44b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript44b": descript44b,
        "form": form,
    }
    return render(request, 'mha/descript44b_1.html', context)


def load_quanity44(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity44 = Bidding.objects.filter(bidid=bidid).values_list('quanity44', flat=True)
    context = {
        "instance": instance,
        "quanity44": quanity44,
        "form": form,
    }
    return render(request, 'mha/quan44_1.html', context)


def descrip45(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript45']
    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    Bidding.objects.filter(bidid=bidid).update(descript45b=b)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/bidpage.html', context)


def descrip45b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_descript45']
    #    b = OutsideResource.objects.filter(id=a).values_list("osrdescrip")
    c = Bidding.objects.filter(bidid=bidid).update(descript45=a)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
    }
    return render(request, 'mha/bidpage.html', context)


def quan45(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid=45).delete()
    OSRCost.objects.filter(bidid=bidid, descript=45).delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity45']
    Bidding.objects.filter(bidid=bidid).update(quanity45=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript45b', flat=True).first()
    c = OutsideResource.objects.filter(osrdescrip=b).values_list('osrunitprice', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity45', flat=True).first()
    d1 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).first()
    d2 = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).first()
    d3 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost45total=e)
    g = TotalJobCost.objects.values_list("id", flat=True).last() or 0
    h = g + 1
    i = TotalJobCost.objects.create(conid=d1, custid=d2, id=h, bidid=bidid, descripid=45, jobcost=e)
    ii = OSRCost.objects.create(conid=d1, custid=d2, jobid=d3, bidid=bidid, descript=45, OSRcost=e)
    context = {
        "instance": instance,
        "form": form,
        'f': f,
        'i': i,
        'ii': ii,
    }
    return render(request, 'mha/bidpage.html', context)


def delete45(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).update(quanity45=0, descript45="", descript45b="", cost45total=0)
    TotalJobCost.objects.filter(descripid=45).delete()
    OSRCost.objects.filter(bidid=bidid, descript=45).delete()
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute27_url(), context)


def load_descript45(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript45 = Bidding.objects.filter(bidid=bidid).values_list('descript45', flat=True)
    context = {
        "instance": instance,
        "descript45": descript45,
        "form": form,
    }
    return render(request, 'mha/descript45_1.html', context)


def load_descript45b(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    descript45b = Bidding.objects.values_list('descript45b', flat=True).get(bidid=bidid) or ""
    context = {
        "instance": instance,
        "descript45b": descript45b,
        "form": form,
    }
    return render(request, 'mha/descript45b_1.html', context)


def load_quanity45(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    quanity45 = Bidding.objects.filter(bidid=bidid).values_list('quanity45', flat=True)
    context = {
        "instance": instance,
        "quanity45": quanity45,
        "form": form,
    }
    return render(request, 'mha/quan45_1.html', context)


def quan46(request, bidid=None):
    FilterEquipType.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_quanity46']
    Bidding.objects.filter(bidid=bidid).update(quanity46=a)
    b = Bidding.objects.filter(bidid=bidid).values_list('descript46', flat=True).first()
    c = Equipment2.objects.filter(modelnum=b).values_list('cost', flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).values_list('quanity46', flat=True).first()
    e = c * d
    f = Bidding.objects.filter(bidid=bidid).update(cost46total=e)

    context = {
        "instance": instance,
        "form": form,
        'f': f,
    }
    return render(request, 'mha/bidpage.html', context)


def materialtype(request, bidid=None):
    MatTypeBid.objects.all().delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    a = request.POST['id_mattype']
    b = Bidding.objects.filter(bidid=bidid).update(mattype=a)
    c = MaterialType.objects.filter(id=a).values_list('type', flat=True).first()
    if c == 'Packages':
        c1 = Package.objects.annotate(packageA=F('package'))
        try:
            w1 = 1
            i1 = Package.objects.filter(package=c1[0]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w1, type=c1[0], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[1]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[1], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[2]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[2], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[3]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[3], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[4]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[4], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[5]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[5], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[6]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[6], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[7]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[7], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[8]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[8], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[9]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[9], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[10]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[10], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[11]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[11], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[12]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[12], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[13]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[13], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[14]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[14], unitcost=i1)
        except Exception:
            j1 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i1 = Package.objects.filter(package=c1[15]).values_list('packagecost', flat=True).first()
            j1 = MatTypeBid.objects.create(id=w2, type=c1[15], unitcost=i1)
        except Exception:
            j1 = 0
    else:
        e1 = Material.objects.filter(materialtype_id=a).annotate(descripA=F('descrip'))
        try:
            w1 = 1
            i = MatTypeBid.objects.create(id=w1, type=e1[0])
        except Exception:
            i = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w2 = w + 1
            i2 = MatTypeBid.objects.create(id=w2, type=e1[1])
        except Exception:
            i2 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w3 = w + 1
            i3 = MatTypeBid.objects.create(id=w3, type=e1[2])
        except Exception:
            i3 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w4 = w + 1
            i4 = MatTypeBid.objects.create(id=w4, type=e1[3])
        except Exception:
            i4 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w5 = w + 1
            i5 = MatTypeBid.objects.create(id=w5, type=e1[4])
        except Exception:
            i5 = 0

        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w6 = w + 1
            i6 = MatTypeBid.objects.create(id=w6, type=e1[5])
        except Exception:
            i6 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w7 = w + 1
            i7 = MatTypeBid.objects.create(id=w7, type=e1[6])
        except Exception:
            i7 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w8 = w + 1
            i8 = MatTypeBid.objects.create(id=w8, type=e1[7])
        except Exception:
            i8 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w9 = w + 1
            i9 = MatTypeBid.objects.create(id=w9, type=e1[8])
        except Exception:
            i9 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w10 = w + 1
            i10 = MatTypeBid.objects.create(id=w10, type=e1[9])
        except Exception:
            i10 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w11 = w + 1
            i11 = MatTypeBid.objects.create(id=w11, type=e1[10])
        except Exception:
            i11 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w12 = w + 1
            i12 = MatTypeBid.objects.create(id=w12, type=e1[11])
        except Exception:
            i12 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w13 = w + 1
            i13 = MatTypeBid.objects.create(id=w13, type=e1[12])
        except Exception:
            i13 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w14 = w + 1
            i14 = MatTypeBid.objects.create(id=w14, type=e1[13])
        except Exception:
            i14 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w15 = w + 1
            i15 = MatTypeBid.objects.create(id=w15, type=e1[14])
        except Exception:
            i15 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w16 = w + 1
            i16 = MatTypeBid.objects.create(id=w16, type=e1[15])
        except Exception:
            i16 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w17 = w + 1
            i17 = MatTypeBid.objects.create(id=w17, type=e1[16])
        except Exception:
            i17 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w18 = w + 1
            i18 = MatTypeBid.objects.create(id=w18, type=e1[17])
        except Exception:
            i18 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w19 = w + 1
            i19 = MatTypeBid.objects.create(id=w19, type=e1[18])
        except Exception:
            i19 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w20 = w + 1
            i20 = MatTypeBid.objects.create(id=w20, type=e1[19])
        except Exception:
            i20 = 0
        try:
            w = MatTypeBid.objects.values_list('id', flat=True).last()
            w21 = w + 1
            i21 = MatTypeBid.objects.create(id=w21, type=e1[20])
        except Exception:
            i21 = 0
    context = {
        "instance": instance,
        "form": form,
        "b": b,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevel(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techlevel']
    b = Bidding.objects.filter(bidid=bidid).update(techlevel=a)
    c = TechLevel.objects.filter(id=a).values_list("rate", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techrate=c)

    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevelhrs(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid='TechHrs1').delete()
    laborCost.objects.filter(bidid=bidid, descript='TechHrs1').delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techhrs']
    c = TechHours.objects.filter(id=a).values_list("hrstech", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techhrs=c)
    e = Bidding.objects.filter(bidid=bidid).values_list("techrate", flat=True).first()
    e1 = Bidding.objects.filter(bidid=bidid).values_list("conid", flat=True).first()
    e2 = Bidding.objects.filter(bidid=bidid).values_list("custid", flat=True).first()
    e3 = Bidding.objects.filter(bidid=bidid).values_list("jobid", flat=True).first()
    f = c * e
    g = Bidding.objects.filter(bidid=bidid).update(directlaborcost1=f)
    h = TotalJobCost.objects.create(conid=e1, custid=e2, bidid=bidid, descripid='TechHrs1', jobcost=f)
    i = laborCost.objects.create(conid=e1, custid=e2, jobid=e3, bidid=bidid, descript='TechHrs1', laborcost=f)

    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "g": g,
        "h": h,
        "i": i,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevel2(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techlevel2']
    b = Bidding.objects.filter(bidid=bidid).update(techlevel2=a)
    c = TechLevel.objects.filter(id=a).values_list("rate", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techrate2=c)

    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevelhrs2(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid='TechHrs2').delete()
    laborCost.objects.filter(bidid=bidid, descript='TechHrs2').delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techhrs2']
    c = TechHours.objects.filter(id=a).values_list("hrstech", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techhrs2=c)
    e = Bidding.objects.filter(bidid=bidid).values_list("techrate2", flat=True).first()
    e1 = Bidding.objects.filter(bidid=bidid).values_list("conid", flat=True).first()
    e2 = Bidding.objects.filter(bidid=bidid).values_list("custid", flat=True).first()
    e3 = Bidding.objects.filter(bidid=bidid).values_list("jobid", flat=True).first()
    f = c * e
    g = Bidding.objects.filter(bidid=bidid).update(directlaborcost2=f)
    h = TotalJobCost.objects.create(conid=e1, custid=e2, bidid=bidid, descripid='TechHrs2', jobcost=f)
    i = laborCost.objects.create(conid=e1, custid=e2, jobid=e3, bidid=bidid, descript='TechHrs2', laborcost=f)

    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "g": g,
        "h": h,
        "i": i,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevel3(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techlevel3']
    b = Bidding.objects.filter(bidid=bidid).update(techlevel3=a)
    c = TechLevel.objects.filter(id=a).values_list("rate", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techrate3=c)

    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevelhrs3(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid='TechHrs3').delete()
    laborCost.objects.filter(bidid=bidid, descript='TechHrs3').delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techhrs3']
    c = TechHours.objects.filter(id=a).values_list("hrstech", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techhrs3=c)
    e = Bidding.objects.filter(bidid=bidid).values_list("techrate3", flat=True).first()
    e1 = Bidding.objects.filter(bidid=bidid).values_list("conid", flat=True).first()
    e2 = Bidding.objects.filter(bidid=bidid).values_list("custid", flat=True).first()
    e3 = Bidding.objects.filter(bidid=bidid).values_list("jobid", flat=True).first()
    f = c * e
    g = Bidding.objects.filter(bidid=bidid).update(directlaborcost3=f)
    h = TotalJobCost.objects.create(conid=e1, custid=e2, bidid=bidid, descripid='TechHrs3', jobcost=f)
    i = laborCost.objects.create(conid=e1, custid=e2, jobid=e3, bidid=bidid, descript='TechHrs3', laborcost=f)

    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "g": g,
        "h": h,
        "i": i,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevel4(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techlevel4']
    b = Bidding.objects.filter(bidid=bidid).update(techlevel4=a)
    c = TechLevel.objects.filter(id=a).values_list("rate", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techrate4=c)

    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
    }
    return render(request, 'mha/bidpage.html', context)


def techlevelhrs4(request, bidid=None):
    TotalJobCost.objects.filter(bidid=bidid, descripid='TechHrs4').delete()
    laborCost.objects.filter(bidid=bidid, descript='TechHrs4').delete()
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None, instance=instance)
    a = request.POST['id_techhrs4']
    c = TechHours.objects.filter(id=a).values_list("hrstech", flat=True).first()
    d = Bidding.objects.filter(bidid=bidid).update(techhrs4=c)
    e = Bidding.objects.filter(bidid=bidid).values_list("techrate4", flat=True).first()
    e1 = Bidding.objects.filter(bidid=bidid).values_list("conid", flat=True).first()
    e2 = Bidding.objects.filter(bidid=bidid).values_list("custid", flat=True).first()
    e3 = Bidding.objects.filter(bidid=bidid).values_list("jobid", flat=True).first()
    f = c * e
    g = Bidding.objects.filter(bidid=bidid).update(directlaborcost4=f)
    h = TotalJobCost.objects.create(conid=e1, custid=e2, bidid=bidid, descripid='TechHrs4', jobcost=f)
    i = laborCost.objects.create(conid=e1, custid=e2, jobid=e3, bidid=bidid, descript='TechHrs4', laborcost=f)

    context = {
        "instance": instance,
        "form": form,
        "d": d,
        "g": g,
        "h": h,
        "i": i,
    }
    return render(request, 'mha/bidpage.html', context)


def package1(request):
    queryset = InstallPackage1.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage1.html', context)


def package1a(request):
    form = Package1b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage1.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage1.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage1.html', context)


def package1b(request):
    form = Package1b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage1.objects.values_list("id", flat=True).last()
    g = InstallPackage1.objects.filter(id=e).update(quant=a)
    h = InstallPackage1.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage1.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage1.objects.filter(id=e).update(cost=k)
    m = InstallPackage1.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage1.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost1=q)
    s = Package.objects.filter(packagenum=1).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage1.html', context)


def package1add(request):
    if request.method == 'POST':
        formset = Package1a(request.POST)
        new_form = Package1b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package1a()
        new_form = Package1b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage1.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package1add.html', context)


def deletepackage1(request, id=None):
    instance = InstallPackage1.objects.get(id=id)
    form = Package1b(request.POST or None, instance=instance)
    queryset = InstallPackage1.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage1.html', context)


def deletepackage1a(request, id=None):
    instance = InstallPackage1.objects.get(id=id)
    form = Package1b(request.POST or None, instance=instance)
    c = InstallPackage1.objects.filter(id=id).delete()
    m = InstallPackage1.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage1.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost1=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute1c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage1.html', context)


def package2(request):
    queryset = InstallPackage2.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage1.html', context)


def package2a(request):
    form = Package2b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage2.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage2.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage1.html', context)


def package2b(request):
    form = Package2b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage2.objects.values_list("id", flat=True).last()
    g = InstallPackage2.objects.filter(id=e).update(quant=a)
    h = InstallPackage2.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage2.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage2.objects.filter(id=e).update(cost=k)
    m = InstallPackage2.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage2.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost2=q)
    s = Package.objects.filter(packagenum=2).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage1.html', context)


def package2add(request):
    if request.method == 'POST':
        formset = Package2b(request.POST)
        new_form = Package2b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package2a()
        new_form = Package2b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage2.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package2add.html', context)


def deletepackage2(request, id=None):
    instance = InstallPackage2.objects.get(id=id)
    form = Package2b(request.POST or None, instance=instance)
    queryset = InstallPackage2.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage2.html', context)


def deletepackage2a(request, id=None):
    instance = InstallPackage2.objects.get(id=id)
    form = Package2b(request.POST or None, instance=instance)
    c = InstallPackage2.objects.filter(id=id).delete()
    m = InstallPackage2.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage2.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost2=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute2c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage2.html', context)


def package3(request):
    queryset = InstallPackage3.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage1.html', context)


def package3a(request):
    form = Package3b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage3.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage3.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage1.html', context)


def package3b(request):
    form = Package3b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage3.objects.values_list("id", flat=True).last()
    g = InstallPackage3.objects.filter(id=e).update(quant=a)
    h = InstallPackage3.objects.values_list("unitprice", flat=True).last() or 0
    i = InstallPackage3.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage3.objects.filter(id=e).update(cost=k)
    m = InstallPackage3.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage3.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost3=q)
    s = Package.objects.filter(packagenum=3).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage1.html', context)


def package3add(request):
    if request.method == 'POST':
        formset = Package3b(request.POST)
        new_form = Package3b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package3a()
        new_form = Package3b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage3.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package3add.html', context)


def deletepackage3(request, id=None):
    instance = InstallPackage3.objects.get(id=id)
    form = Package3b(request.POST or None, instance=instance)
    queryset = InstallPackage3.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage3.html', context)


def deletepackage3a(request, id=None):
    instance = InstallPackage3.objects.get(id=id)
    form = Package3b(request.POST or None, instance=instance)
    c = InstallPackage3.objects.filter(id=id).delete()
    m = InstallPackage3.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage3.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost3=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute3c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage3.html', context)


def package4(request):
    queryset = InstallPackage4.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage1.html', context)


def package4a(request):
    form = Package4b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage4.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage4.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage1.html', context)


def package4b(request):
    form = Package4b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage4.objects.values_list("id", flat=True).last()
    g = InstallPackage4.objects.filter(id=e).update(quant=a)
    h = InstallPackage4.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage4.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage4.objects.filter(id=e).update(cost=k)
    m = InstallPackage4.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage4.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost4=q)
    s = Package.objects.filter(packagenum=4).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage1.html', context)


def package4add(request):
    if request.method == 'POST':
        formset = Package4b(request.POST)
        new_form = Package4b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package4a()
        new_form = Package4b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage4.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package4add.html', context)


def deletepackage4(request, id=None):
    instance = InstallPackage4.objects.get(id=id)
    form = Package4b(request.POST or None, instance=instance)
    queryset = InstallPackage4.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage4.html', context)


def deletepackage4a(request, id=None):
    instance = InstallPackage4.objects.get(id=id)
    form = Package4b(request.POST or None, instance=instance)
    c = InstallPackage4.objects.filter(id=id).delete()
    m = InstallPackage4.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage4.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost4=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute4c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage4.html', context)


def package5(request):
    queryset = InstallPackage5.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage2.html', context)


def package5a(request):
    form = Package5b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage5.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage5.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage2.html', context)


def package5b(request):
    form = Package5b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage5.objects.values_list("id", flat=True).last()
    g = InstallPackage5.objects.filter(id=e).update(quant=a)
    h = InstallPackage5.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage5.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage5.objects.filter(id=e).update(cost=k)
    m = InstallPackage5.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage5.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost5=q)
    s = Package.objects.filter(packagenum=5).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage2.html', context)


def package5add(request):
    if request.method == 'POST':
        formset = Package5b(request.POST)
        new_form = Package5b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package5a()
        new_form = Package5b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage5.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package5add.html', context)


def deletepackage5(request, id=None):
    instance = InstallPackage5.objects.get(id=id)
    form = Package5b(request.POST or None, instance=instance)
    queryset = InstallPackage5.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage5.html', context)


def deletepackage5a(request, id=None):
    instance = InstallPackage5.objects.get(id=id)
    form = Package5b(request.POST or None, instance=instance)
    c = InstallPackage5.objects.filter(id=id).delete()
    m = InstallPackage5.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage5.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost5=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute5c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage5.html', context)


def package6(request):
    queryset = InstallPackage6.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage2.html', context)


def package6a(request):
    form = Package6b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage6.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage6.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage2.html', context)


def package6b(request):
    form = Package6b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage6.objects.values_list("id", flat=True).last()
    g = InstallPackage6.objects.filter(id=e).update(quant=a)
    h = InstallPackage6.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage6.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage6.objects.filter(id=e).update(cost=k)
    m = InstallPackage6.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage6.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost6=q)
    s = Package.objects.filter(packagenum=6).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage2.html', context)


def package6add(request):
    if request.method == 'POST':
        formset = Package6b(request.POST)
        new_form = Package6b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package6a()
        new_form = Package6b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage6.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package6add.html', context)


def deletepackage6(request, id=None):
    instance = InstallPackage6.objects.get(id=id)
    form = Package6b(request.POST or None, instance=instance)
    queryset = InstallPackage6.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage6.html', context)


def deletepackage6a(request, id=None):
    instance = InstallPackage6.objects.get(id=id)
    form = Package6b(request.POST or None, instance=instance)
    c = InstallPackage6.objects.filter(id=id).delete()
    m = InstallPackage6.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage6.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost6=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute6c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage6.html', context)


def package7(request):
    queryset = InstallPackage7.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage2.html', context)


def package7a(request):
    form = Package7b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage7.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage7.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage2.html', context)


def package7b(request):
    form = Package7b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage7.objects.values_list("id", flat=True).last()
    g = InstallPackage7.objects.filter(id=e).update(quant=a)
    h = InstallPackage7.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage7.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage7.objects.filter(id=e).update(cost=k)
    m = InstallPackage7.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage7.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost7=q)
    s = Package.objects.filter(packagenum=7).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage2.html', context)


def package7add(request):
    if request.method == 'POST':
        formset = Package7b(request.POST)
        new_form = Package7b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package7a()
        new_form = Package7b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage7.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package7add.html', context)


def deletepackage7(request, id=None):
    instance = InstallPackage7.objects.get(id=id)
    form = Package7b(request.POST or None, instance=instance)
    queryset = InstallPackage7.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage7.html', context)


def deletepackage7a(request, id=None):
    instance = InstallPackage7.objects.get(id=id)
    form = Package7b(request.POST or None, instance=instance)
    c = InstallPackage7.objects.filter(id=id).delete()
    m = InstallPackage7.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage7.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost7=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute7c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage7.html', context)


def package8(request):
    queryset = InstallPackage8.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage2.html', context)


def package8a(request):
    form = Package8b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage8.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage8.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage2.html', context)


def package8b(request):
    form = Package8b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage8.objects.values_list("id", flat=True).last()
    g = InstallPackage8.objects.filter(id=e).update(quant=a)
    h = InstallPackage8.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage8.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage8.objects.filter(id=e).update(cost=k)
    m = InstallPackage8.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage8.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost8=q)
    s = Package.objects.filter(packagenum=8).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage2.html', context)


def package8add(request):
    if request.method == 'POST':
        formset = Package8b(request.POST)
        new_form = Package8b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package8a()
        new_form = Package8b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage8.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package8add.html', context)


def deletepackage8(request, id=None):
    instance = InstallPackage8.objects.get(id=id)
    form = Package8b(request.POST or None, instance=instance)
    queryset = InstallPackage8.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage8.html', context)


def deletepackage8a(request, id=None):
    instance = InstallPackage8.objects.get(id=id)
    form = Package8b(request.POST or None, instance=instance)
    c = InstallPackage8.objects.filter(id=id).delete()
    m = InstallPackage8.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage8.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost8=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute8c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage8.html', context)


def package9(request):
    queryset = InstallPackage9.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage3.html', context)


def package9a(request):
    form = Package9b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage9.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage9.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage3.html', context)


def package9b(request):
    form = Package9b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage9.objects.values_list("id", flat=True).last()
    g = InstallPackage9.objects.filter(id=e).update(quant=a)
    h = InstallPackage9.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage9.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage9.objects.filter(id=e).update(cost=k)
    m = InstallPackage9.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage9.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost9=q)
    s = Package.objects.filter(packagenum=9).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage3.html', context)


def package9add(request):
    if request.method == 'POST':
        formset = Package9b(request.POST)
        new_form = Package9b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package9a()
        new_form = Package9b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage9.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package9add.html', context)


def deletepackage9(request, id=None):
    instance = InstallPackage9.objects.get(id=id)
    form = Package9b(request.POST or None, instance=instance)
    queryset = InstallPackage9.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage9.html', context)


def deletepackage9a(request, id=None):
    instance = InstallPackage9.objects.get(id=id)
    form = Package9b(request.POST or None, instance=instance)
    c = InstallPackage9.objects.filter(id=id).delete()
    m = InstallPackage9.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage9.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost9=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute9c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage9.html', context)


def package10(request):
    queryset = InstallPackage10.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage3.html', context)


def package10a(request):
    form = Package10b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage10.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage10.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage3.html', context)


def package10b(request):
    form = Package10b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage10.objects.values_list("id", flat=True).last()
    g = InstallPackage10.objects.filter(id=e).update(quant=a)
    h = InstallPackage10.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage10.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage10.objects.filter(id=e).update(cost=k)
    m = InstallPackage10.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage10.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost10=q)
    s = Package.objects.filter(packagenum=10).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage3.html', context)


def package10add(request):
    if request.method == 'POST':
        formset = Package10b(request.POST)
        new_form = Package10b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package10a()
        new_form = Package10b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage10.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package10add.html', context)


def deletepackage10(request, id=None):
    instance = InstallPackage10.objects.get(id=id)
    form = Package10b(request.POST or None, instance=instance)
    queryset = InstallPackage10.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage10.html', context)


def deletepackage10a(request, id=None):
    instance = InstallPackage10.objects.get(id=id)
    form = Package10b(request.POST or None, instance=instance)
    c = InstallPackage10.objects.filter(id=id).delete()
    m = InstallPackage10.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage10.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost10=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute10c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage10.html', context)


def package11(request):
    queryset = InstallPackage11.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage3.html', context)


def package11a(request):
    form = Package11b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage11.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage11.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage3.html', context)


def package11b(request):
    form = Package11b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage11.objects.values_list("id", flat=True).last()
    g = InstallPackage11.objects.filter(id=e).update(quant=a)
    h = InstallPackage11.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage11.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage11.objects.filter(id=e).update(cost=k)
    m = InstallPackage11.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage11.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost11=q)
    s = Package.objects.filter(packagenum=11).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage3.html', context)


def package11add(request):
    if request.method == 'POST':
        formset = Package11b(request.POST)
        new_form = Package11b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package11a()
        new_form = Package11b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage11.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package11add.html', context)


def deletepackage11(request, id=None):
    instance = InstallPackage11.objects.get(id=id)
    form = Package11b(request.POST or None, instance=instance)
    queryset = InstallPackage11.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage11.html', context)


def deletepackage11a(request, id=None):
    instance = InstallPackage11.objects.get(id=id)
    form = Package11b(request.POST or None, instance=instance)
    c = InstallPackage11.objects.filter(id=id).delete()
    m = InstallPackage11.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage11.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost11=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute11c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage11.html', context)


def package12(request):
    queryset = InstallPackage12.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage3.html', context)


def package12a(request):
    form = Package12b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage12.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage12.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage3.html', context)


def package12b(request):
    form = Package12b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage12.objects.values_list("id", flat=True).last()
    g = InstallPackage12.objects.filter(id=e).update(quant=a)
    h = InstallPackage12.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage12.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage12.objects.filter(id=e).update(cost=k)
    m = InstallPackage12.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage12.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost12=q)
    s = Package.objects.filter(packagenum=12).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage3.html', context)


def package12add(request):
    if request.method == 'POST':
        formset = Package12b(request.POST)
        new_form = Package12b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package12a()
        new_form = Package12b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage12.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package12add.html', context)


def deletepackage12(request, id=None):
    instance = InstallPackage12.objects.get(id=id)
    form = Package12b(request.POST or None, instance=instance)
    queryset = InstallPackage12.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage12.html', context)


def deletepackage12a(request, id=None):
    instance = InstallPackage12.objects.get(id=id)
    form = Package12b(request.POST or None, instance=instance)
    c = InstallPackage12.objects.filter(id=id).delete()
    m = InstallPackage12.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage12.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost12=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute12c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage12.html', context)


def package13(request):
    queryset = InstallPackage13.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage3.html', context)


def package13a(request):
    form = Package13b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage13.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage13.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage3.html', context)


def package13b(request):
    form = Package13b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage13.objects.values_list("id", flat=True).last()
    g = InstallPackage13.objects.filter(id=e).update(quant=a)
    h = InstallPackage13.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage13.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage13.objects.filter(id=e).update(cost=k)
    m = InstallPackage13.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage13.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost13=q)
    s = Package.objects.filter(packagenum=13).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage3.html', context)


def package13add(request):
    if request.method == 'POST':
        formset = Package13b(request.POST)
        new_form = Package13b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package13a()
        new_form = Package13b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage13.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package13add.html', context)


def deletepackage13(request, id=None):
    instance = InstallPackage13.objects.get(id=id)
    form = Package13b(request.POST or None, instance=instance)
    queryset = InstallPackage13.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage13.html', context)


def deletepackage13a(request, id=None):
    instance = InstallPackage13.objects.get(id=id)
    form = Package13b(request.POST or None, instance=instance)
    c = InstallPackage13.objects.filter(id=id).delete()
    m = InstallPackage13.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage13.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost13=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute13c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage13.html', context)


def package14(request):
    queryset = InstallPackage14.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage4.html', context)


def package14a(request):
    form = Package14b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage14.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage14.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage4.html', context)


def package14b(request):
    form = Package14b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage14.objects.values_list("id", flat=True).last()
    g = InstallPackage14.objects.filter(id=e).update(quant=a)
    h = InstallPackage14.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage14.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage14.objects.filter(id=e).update(cost=k)
    m = InstallPackage14.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage14.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost14=q)
    s = Package.objects.filter(packagenum=14).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage4.html', context)


def package14add(request):
    if request.method == 'POST':
        formset = Package14b(request.POST)
        new_form = Package14b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package14a()
        new_form = Package14b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage14.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package14add.html', context)


def deletepackage14(request, id=None):
    instance = InstallPackage14.objects.get(id=id)
    form = Package14b(request.POST or None, instance=instance)
    queryset = InstallPackage14.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage14.html', context)


def deletepackage14a(request, id=None):
    instance = InstallPackage14.objects.get(id=id)
    form = Package14b(request.POST or None, instance=instance)
    c = InstallPackage14.objects.filter(id=id).delete()
    m = InstallPackage14.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage14.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost14=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute14c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage14.html', context)


def package15(request):
    queryset = InstallPackage15.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage4.html', context)


def package15a(request):
    form = Package15b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage15.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage15.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage4.html', context)


def package15b(request):
    form = Package15b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage15.objects.values_list("id", flat=True).last()
    g = InstallPackage15.objects.filter(id=e).update(quant=a)
    h = InstallPackage15.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage15.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage15.objects.filter(id=e).update(cost=k)
    m = InstallPackage15.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage15.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost15=q)
    s = Package.objects.filter(packagenum=15).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage4.html', context)


def package15add(request):
    if request.method == 'POST':
        formset = Package15b(request.POST)
        new_form = Package15b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package15a()
        new_form = Package15b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage15.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package15add.html', context)


def deletepackage15(request, id=None):
    instance = InstallPackage15.objects.get(id=id)
    form = Package15b(request.POST or None, instance=instance)
    queryset = InstallPackage15.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage15.html', context)


def deletepackage15a(request, id=None):
    instance = InstallPackage15.objects.get(id=id)
    form = Package15b(request.POST or None, instance=instance)
    c = InstallPackage15.objects.filter(id=id).delete()
    m = InstallPackage15.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage15.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost15=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute15c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage15.html', context)


def package16(request):
    queryset = InstallPackage16.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))
        paginator = Paginator(queryset, 2)  # Show 16 contacts per page
        page_number = request.GET.get('page')
        try:
            queryset = paginator.get_page(page_number)
        except PageNotAnInteger:
            queryset = paginator.page(1)
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)
    context = {"object_list": queryset,
               "search_term": search_term,
               }
    return render(request, 'mha/packagepage4.html', context)


def package16a(request):
    form = Package16b(request.POST or None)
    a = request.POST['id_description']
    b = Material.objects.filter(id=a).values_list("descrip", flat=True).first()
    c = Material.objects.filter(id=a).values_list("cost", flat=True).first()
    d = Material.objects.filter(id=a).values_list("id", flat=True).first()
    e = InstallPackage16.objects.values_list("id", flat=True).last() or 0
    f = e + 1
    g = InstallPackage16.objects.create(id=f, description=b, unitprice=c, matid=d)
    context = {
        "form": form,
        "g": g,

    }
    return render(request, 'mha/packagepage4.html', context)


def package16b(request):
    form = Package16b(request.POST or None)
    a = request.POST['id_quant']
    e = InstallPackage16.objects.values_list("id", flat=True).last()
    g = InstallPackage16.objects.filter(id=e).update(quant=a)
    h = InstallPackage16.objects.values_list("unitprice", flat=True).last()
    i = InstallPackage16.objects.values_list("quant", flat=True).last()
    k = h * i
    l = InstallPackage16.objects.filter(id=e).update(cost=k)
    m = InstallPackage16.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage16.objects.all().aggregate(p=Sum('cost'))
    q = o['p']
    r = PackageInfo.objects.filter(id=1).update(cost16=q)
    s = Package.objects.filter(packagenum=16).update(packagecost=q)
    context = {
        "form": form,
        "g": g,
        "l": l,
        "o": o,
        "n": n,
        "r": r,
        "s": s,
    }
    return render(request, 'mha/packagepage4.html', context)


def package16add(request):
    if request.method == 'POST':
        formset = Package16b(request.POST)
        new_form = Package16b(request.POST)
        if formset.is_valid():
            formset.save()  # Saves any changes made to existing records
        if new_form.is_valid():
            new_form.save()  # Creates a new record
        # Redirect to the same page or another view after successful submission
        return redirect(request.path_info)
    else:
        # Display the forms
        formset = Package16a()
        new_form = Package16b()
    context = {
        'formset': formset,
        'new_form': new_form,
        'records': InstallPackage16.objects.all(),  # Retrieve all records to display
    }
    return render(request, 'mha/package16add.html', context)


def deletepackage16(request, id=None):
    instance = InstallPackage16.objects.get(id=id)
    form = Package16b(request.POST or None, instance=instance)
    queryset = InstallPackage16.objects.filter(id=id)
    context = {
        "object_list": queryset,
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/deletepackage16.html', context)


def deletepackage16a(request, id=None):
    instance = InstallPackage16.objects.get(id=id)
    form = Package16b(request.POST or None, instance=instance)
    c = InstallPackage16.objects.filter(id=id).delete()
    m = InstallPackage16.objects.all().aggregate(Sum('cost'))
    n = m['cost__sum']
    o = InstallPackage16.objects.all().aggregate(p=Sum('cost'))
    q = o['p'] or 0
    r = PackageInfo.objects.filter(id=1).update(cost16=q)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute16c_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "c": c,
        "n": n,
        "r": r,
    }
    return render(request, 'mha/deletepackage16.html', context)


def mainsettingpage(request):
    return render(request, 'mha/mainsettingpage.html')


def packagepage1(request):
    queryset5 = PackageInfo.objects.all()
    queryset = InstallPackage1.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term)
                                   | Q(unitprice__icontains=search_term)
                                   | Q(quant__icontains=search_term))

    queryset2 = InstallPackage2.objects.all()
    search_term2 = ''
    if 'search' in request.GET:
        search_term2 = request.GET['search']
        queryset2 = queryset.filter(Q(id__icontains=search_term)
                                    | Q(description__icontains=search_term)
                                    | Q(unitprice__icontains=search_term)
                                    | Q(quant__icontains=search_term))
    queryset3 = InstallPackage3.objects.all()
    search_term3 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset3 = queryset.filter(Q(id__icontains=search_term)
                                    | Q(description__icontains=search_term)
                                    | Q(unitprice__icontains=search_term)
                                    | Q(quant__icontains=search_term))

    queryset4 = InstallPackage4.objects.all()
    search_term4 = ''
    if 'search' in request.GET:
        search_term2 = request.GET['search']
        queryset4 = queryset.filter(Q(id__icontains=search_term)
                                    | Q(description__icontains=search_term)
                                    | Q(unitprice__icontains=search_term)
                                    | Q(quant__icontains=search_term))

    context = {
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "search_term": search_term,
        "search_term2": search_term2,
        "search_term3": search_term3,
        "search_term4": search_term4,
    }
    return render(request, 'mha/packagepage1.html', context)


def packagepage2(request):
    queryset4 = PackageInfo.objects.all()
    queryset5 = InstallPackage5.objects.all()
    search_term5 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset5 = queryset5.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset6 = InstallPackage6.objects.all()
    search_term6 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset6 = queryset6.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))
    queryset7 = InstallPackage7.objects.all()
    search_term7 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset7 = queryset7.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset8 = InstallPackage8.objects.all()
    search_term8 = ''
    if 'search' in request.GET:
        search_term2 = request.GET['search']
        queryset8 = queryset8.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    context = {
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list4": queryset4,
        "search_term5": search_term5,
        "search_term6": search_term6,
        "search_term7": search_term7,
        "search_term8": search_term8,
    }
    return render(request, 'mha/packagepage2.html', context)


def packagepage3(request):
    queryset5 = PackageInfo.objects.all()
    queryset9 = InstallPackage9.objects.all()
    search_term9 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset9 = queryset9.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset10 = InstallPackage10.objects.all()
    search_term10 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset10 = queryset10.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))
    queryset11 = InstallPackage11.objects.all()
    search_term11 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset11 = queryset11.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))

    queryset12 = InstallPackage12.objects.all()
    search_term12 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset12 = queryset12.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))

    context = {
        "object_list9": queryset9,
        "object_list10": queryset10,
        "object_list11": queryset11,
        "object_list12": queryset12,
        "object_list5": queryset5,
        "search_term9": search_term9,
        "search_term10": search_term10,
        "search_term11": search_term11,
        "search_term12": search_term12,
    }
    return render(request, 'mha/packagepage3.html', context)


def packagepage4(request):
    queryset5 = PackageInfo.objects.all()
    queryset13 = InstallPackage13.objects.all()
    search_term13 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset13 = queryset13.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))

    queryset14 = InstallPackage14.objects.all()
    search_term14 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset14 = queryset14.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))
    queryset15 = InstallPackage15.objects.all()
    search_term15 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset15 = queryset15.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))

    queryset16 = InstallPackage16.objects.all()
    search_term16 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset16 = queryset16.filter(Q(id__icontains=search_term)
                                       | Q(description__icontains=search_term)
                                       | Q(unitprice__icontains=search_term)
                                       | Q(quant__icontains=search_term))

    context = {
        "object_list13": queryset13,
        "object_list14": queryset14,
        "object_list15": queryset15,
        "object_list16": queryset16,
        "object_list5": queryset5,
        "search_term13": search_term13,
        "search_term14": search_term14,
        "search_term15": search_term15,
        "search_term16": search_term16,
    }
    return render(request, 'mha/packagepage4.html', context)


def packagepage1(request):
    queryset5 = PackageInfo.objects.all()
    queryset1 = InstallPackage1.objects.all()
    search_term1 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset1 = queryset1.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset2 = InstallPackage2.objects.all()
    search_term2 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset2 = queryset2.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset3 = InstallPackage3.objects.all()
    search_term3 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset3 = queryset3.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))

    queryset4 = InstallPackage4.objects.all()
    search_term4 = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset4 = queryset3.filter(Q(id__icontains=search_term)
                                     | Q(description__icontains=search_term)
                                     | Q(unitprice__icontains=search_term)
                                     | Q(quant__icontains=search_term))
    context = {
        "object_list1": queryset1,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,

        "search_term1": search_term1,
        "search_term2": search_term2,
        "search_term3": search_term3,
        "search_term4": search_term4,

    }
    return render(request, 'mha/packagepage1.html', context)


def packagenamechange(request):
    queryset1 = PackageInfo.objects.all()
    context = {
        "object_list1": queryset1,
    }

    return render(request, 'mha/packagenamechange.html', context)


def changename1(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset1 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list1": queryset1,

    }
    return render(request, 'mha/changename1.html', context)


def acceptchangename1(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name1b']
    PackageInfo.objects.filter(id=id).update(name1=a)
    Package.objects.filter(id=1).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename1.html', context)


def changename2(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset2 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list2": queryset2,

    }
    return render(request, 'mha/changename2.html', context)


def acceptchangename2(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name2b']
    PackageInfo.objects.filter(id=id).update(name2=a)
    Package.objects.filter(id=2).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename2.html', context)


def changename3(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset3 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list3": queryset3,

    }
    return render(request, 'mha/changename3.html', context)


def acceptchangename3(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name3b']
    PackageInfo.objects.filter(id=id).update(name3=a)
    Package.objects.filter(id=3).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename3.html', context)


def changename4(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset4 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list4": queryset4,

    }
    return render(request, 'mha/changename4.html', context)


def acceptchangename4(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name4b']
    PackageInfo.objects.filter(id=id).update(name4=a)
    Package.objects.filter(id=4).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename4.html', context)


def changename5(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset5 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list5": queryset5,

    }
    return render(request, 'mha/changename5.html', context)


def acceptchangename5(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name5b']
    PackageInfo.objects.filter(id=id).update(name5=a)
    Package.objects.filter(id=5).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename5.html', context)


def changename6(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset6 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list6": queryset6,

    }
    return render(request, 'mha/changename6.html', context)


def acceptchangename6(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name6b']
    PackageInfo.objects.filter(id=id).update(name6=a)
    Package.objects.filter(id=6).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename6.html', context)


def changename7(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset7 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list7": queryset7,

    }
    return render(request, 'mha/changename7.html', context)


def acceptchangename7(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name7b']
    PackageInfo.objects.filter(id=id).update(name7=a)
    Package.objects.filter(id=7).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename7.html', context)


def changename8(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset8 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list8": queryset8,

    }
    return render(request, 'mha/changename8.html', context)


def acceptchangename8(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name8b']
    PackageInfo.objects.filter(id=id).update(name8=a)
    Package.objects.filter(id=8).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename8.html', context)


def changename9(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset9 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list9": queryset9,

    }
    return render(request, 'mha/changename9.html', context)


def acceptchangename9(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name9b']
    PackageInfo.objects.filter(id=id).update(name9=a)
    Package.objects.filter(id=9).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename9.html', context)


def changename10(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset10 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list10": queryset10,

    }
    return render(request, 'mha/changename10.html', context)


def acceptchangename10(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name10b']
    PackageInfo.objects.filter(id=id).update(name10=a)
    Package.objects.filter(id=10).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename10.html', context)


def changename11(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset11 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list11": queryset11,

    }
    return render(request, 'mha/changename11.html', context)


def acceptchangename11(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name11b']
    PackageInfo.objects.filter(id=id).update(name11=a)
    Package.objects.filter(id=11).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename11.html', context)


def changename12(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset12 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list12": queryset12,

    }
    return render(request, 'mha/changename12.html', context)


def acceptchangename12(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name12b']
    PackageInfo.objects.filter(id=id).update(name12=a)
    Package.objects.filter(id=12).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename12.html', context)


def changename13(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset13 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list13": queryset13,

    }
    return render(request, 'mha/changename13.html', context)


def acceptchangename13(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name13b']
    PackageInfo.objects.filter(id=id).update(name13=a)
    Package.objects.filter(id=13).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename13.html', context)


def changename14(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset14 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list14": queryset14,

    }
    return render(request, 'mha/changename14.html', context)


def acceptchangename14(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name14b']
    PackageInfo.objects.filter(id=id).update(name14=a)
    Package.objects.filter(id=14).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename14.html', context)


def changename15(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset15 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list15": queryset15,

    }
    return render(request, 'mha/changename15.html', context)


def acceptchangename15(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name15b']
    PackageInfo.objects.filter(id=id).update(name15=a)
    Package.objects.filter(id=15).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename15.html', context)


def changename16(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    queryset16 = PackageInfo.objects.filter(id=id)
    context = {
        "instance": instance,
        "form": form,
        "object_list16": queryset16,

    }
    return render(request, 'mha/changename16.html', context)


def acceptchangename16(request, id=None):
    instance = PackageInfo.objects.get(id=id)
    form = InfoPackage(request.POST or None, instance=instance)
    a = request.POST['id_name16b']
    PackageInfo.objects.filter(id=id).update(name16=a)
    Package.objects.filter(id=16).update(package=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/changename16.html', context)


def reviewpackages(request):
    queryset1 = PackageInfo.objects.all()
    context = {
        "object_list1": queryset1,
    }

    return render(request, 'mha/reviewpackages.html', context)


def totaljobcost(request, jobid=None):
    TotalJobCost.objects.all().delete()
    instance = Bidding.objects.get(jobid=jobid)
    form = BidSelect(request.POST or None, instance=instance)
    a = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    b = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    c = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    d = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    e = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    f = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    g = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    h = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    i = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    j = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()

    k = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    l = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    m = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    n = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    o = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    p = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    q = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    r = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    s = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    t = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()

    u = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    v = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    w = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    x = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    y = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    z = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    a1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    b1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    c1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    d1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()

    e1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    f1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    g1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    h1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    i1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    j1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    k1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    l1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    m1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()
    n1 = Bidding.objects.filter(jobid=jobid).values_list('cost1total', flat=True).first()

    context = {
        "instance": instance,
        "form": form,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'j': j,
        'k': k,
        'l': l,
        'm': m,
        'n': n,
        'o': o,
        'p': p,
        'q': q,
        'r': r,
        's': s,
        't': t,
        'u': u,
        'v': v,
        'w': w,
        'x': x,
        'y': y,
        'z': z,
        'a1': a1,
        'b1': b1,
        'c1': c1,
        'd1': d1,
        'e1': e1,
        'f1': f1,
        'g1': g1,
        'h1': h1,
        'i1': i1,
        'j1': j1,
        'k1': k1,
        'l1': l1,
        'm1': m1,
        'n1': n1,

    }
    return render(request, 'mha/bidpage.html', context)


def cancelbid(request, bidid=None):
    instance = Bidding.objects.get(bidid=bidid)
    form = BidSelect(request.POST or None)
    Bidding.objects.filter(bidid=bidid).delete()
    TotalJobCost.objects.filter(bidid=bidid).delete()
    EquipSelection.objects.filter(bidid=bidid).delete()

    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute28_url(), context)


def print(request, jobid=None):
    instance = Contract.objects.get(jobid=jobid)
    form = ContractForm(request.POST or None)
    print(form)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/contract.html', context)


def contract(request, bidid=None):
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    JobCost.objects.filter(bidid=bidid).delete()
    a = Bidding.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    a2 = Bidding.objects.filter(bidid=bidid).values_list('conid', flat=True).last()
    a3 = Bidding.objects.filter(bidid=bidid).values_list('bidid', flat=True).last()
    a4 = Bidding.objects.filter(bidid=bidid).values_list('jobid', flat=True).last()
    a5 = JobCost.objects.create(conid=a2, custid=a, bidid=a3, jobid=a4)

    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset1 = ContractorInfo.objects.filter(id=a4).all()
    queryset2 = SelectedEquip.objects.filter(equipid=1, bidid=bidid).all()
    queryset2a = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    queryset3 = SelectedEquip.objects.filter(equipid=2, bidid=bidid).all()
    queryset4 = SelectedEquip.objects.filter(equipid=3, bidid=bidid).all()
    queryset5 = SelectedEquip.objects.filter(equipid=4, bidid=bidid).all()
    queryset6 = SelectedEquip.objects.filter(equipid=5, bidid=bidid).all()
    queryset7 = SelectedEquip.objects.filter(equipid=6, bidid=bidid).all()
    queryset8 = SelectedEquip.objects.filter(equipid=7, bidid=bidid).all()
    queryset9 = EquipSelection.objects.filter(bidid=bidid).all()
    queryset10 = Contract.objects.filter(bidid=bidid).all()

    a6 = MatCost.objects.filter(bidid=bidid).aggregate(mat_cost=Sum('matcost'))
    a7 = a6['mat_cost']
    b6 = SelectedEquip.objects.filter(bidid=bidid).aggregate(mat_cost=Sum('cost'))
    b7 = b6['mat_cost']
    b8 = a7 + b7
    a8 = Tax.objects.values_list('taxrate', flat=True).last()
    a9 = JobCost.objects.filter(bidid=bidid).update(matcost=b8, taxrate=a8)
    a10 = b8 * a8
    a11 = JobCost.objects.filter(bidid=bidid).update(salestax=a10)
    a12 = b8 + a10
    a13 = JobCost.objects.filter(bidid=bidid).update(totalmatcost=a12)

    a14 = laborCost.objects.filter(bidid=bidid).aggregate(labor_cost=Sum('laborcost'))
    a15 = a14['labor_cost']
    a16 = JobCost.objects.filter(bidid=bidid).update(directlaborcost=a15)
    a17 = Calculation.objects.values_list('ohlabor', flat=True).last()
    a18 = JobCost.objects.filter(bidid=bidid).update(ohlabor=a17)
    a19 = a15 * a17
    a20 = a15 + a19
    a21 = JobCost.objects.filter(bidid=bidid).update(totallaborcost=a20)
    a22 = a12 + a20
    a23 = JobCost.objects.filter(bidid=bidid).update(netjobcost=a22)

    a24 = TargetProfit.objects.filter(bidid=bidid).values_list('targetprofit_id', flat=True)
    a25 = JobCost.objects.filter(bidid=bidid).update(netprofit=a24)
    a26 = JobCost.objects.values_list('netprofit', flat=True).last()
    a27 = a22 * a26
    a28 = JobCost.objects.filter(bidid=bidid).update(netprofitcost=a27)
    a29 = a22 + a27
    a30 = JobCost.objects.filter(bidid=bidid).update(netjobcost2=a29)
    a31 = OSRCost.objects.filter(bidid=bidid).aggregate(OSR_cost=Sum('OSRcost'))
    a32 = a31['OSR_cost'] or 0
    a33 = JobCost.objects.filter(bidid=bidid).update(OSRcost=a32)
    a34 = a32 + a29
    a35 = JobCost.objects.filter(bidid=bidid).update(netjobcost3=a34)
    a36 = EquipSelection.objects.filter(bidid=bidid).values_list('vendor1rebate', flat=True)
    a37 = a36.first()
    a38 = EquipSelection.objects.filter(bidid=bidid).values_list('vendor2rebate', flat=True)
    a39 = a38.first()
    a40 = JobCost.objects.filter(bidid=bidid).update(instantrebate1=a37, instantrebate2=a39)
    a41 = a37 + a39
    a42 = JobCost.objects.filter(bidid=bidid).update(rebateamouint=a41)
    a43 = a34 - a41
    a44 = JobCost.objects.filter(bidid=bidid).update(finaljobcost=a43)

#    b = TotalJobCost.objects.filter(bidid=bidid).aggregate(total_price=Sum('jobcost'))
#    c = b['total_price']
#    d = EquipSelection.objects.filter(bidid=bidid).values_list('totalrebate', flat=True)
#    e = d.first()
#    f = c - e
    g = Contract.objects.filter(bidid=bidid).update(costbeforrebate=a34, totalrebate=a41, totaljobcost=a43, grandtotalcost=a43)
    grandtotalcost = num2words(a43, to='currency', currency='USD')
    h = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=a34, rebatetotal=a41, loccostafterrebate=a43)

    bb = multiformA.objects.filter(bidid=bidid, options='Option A').values_list('cost', flat=True)
    #    cb = bb[0]
    #    queryset13 = float(cb)
    #    queryset11A = multiformA.objects.filter(bidid=bidid).all()
    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list1": queryset1,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        #        "object_list13" : queryset13,
        #        "object_list11A": queryset11A,
        "object_list112a": queryset2a,
        "a5": a5,
        "a11": a11,
        "a13": a13,
        "g": g,
        "h": h,
        "a9": a9,
        "grandtotalcost": grandtotalcost,
    }
    return render(request, 'mha/contract.html', context)



def contractB(request, bidid=None):
    multiformB.objects.filter(bidid=bidid).delete()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(id=1).all()
    queryset3 = SelectedEquip.objects.filter(id=2).all()
    queryset4 = SelectedEquip.objects.filter(id=3).all()
    queryset5 = SelectedEquip.objects.filter(id=4).all()
    queryset6 = SelectedEquip.objects.filter(id=5).all()
    queryset7 = SelectedEquip.objects.filter(id=6).all()
    queryset8 = SelectedEquip.objects.filter(id=7).all()
    queryset9 = EquipSelection.objects.filter(bidid=bidid).all()
    queryset10 = Contract.objects.filter(bidid=bidid).all()
    b = TotalJobCost.objects.filter(bidid=bidid).aggregate(total_price=Sum('jobcost'))
    c = b['total_price']
    d = EquipSelection.objects.filter(bidid=bidid).values_list('totalrebate', flat=True)
    e = d.first()
    f = c - e
    g = Contract.objects.filter(bidid=bidid).update(costbeforrebate=c, totalrebate=e, totaljobcost=f)
    grandtotalcost = num2words(f, to='currency', currency='USD')

    h = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=c, rebatetotal=e, loccostafterrebate=f)

    aa = EquipSelection.objects.filter(bidid=bidid).values_list('custid', flat=True)
    bb = EquipSelection.objects.filter(bidid=bidid).values_list('jobid', flat=True)
    cc = EquipSelection.objects.filter(bidid=bidid).values_list('bidid', flat=True)
    dd1 = EquipSelection.objects.filter(bidid=bidid).values_list('optionid', flat=True)
    dd = EquipSelection.objects.filter(bidid=bidid).values_list('options', flat=True)

    e1 = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True)
    gg1 = g1.first()
    i1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfg', flat=True).first()
    j1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfgmodeldescrip', flat=True)
    k1 = Equipment2.objects.filter(modelnum=gg1).values_list('eff', flat=True)
    l1 = Equipment2.objects.filter(modelnum=gg1).values_list('btu', flat=True)
    m1 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n1 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e1, type=f1, mfg=i1,
                                   modelnum=g1,
                                   description=j1, eff=k1, btu=l1, cost=m1)

    e2 = Bidding.objects.filter(bidid=bidid).values_list('quanity2', flat=True)
    f2 = Bidding.objects.filter(bidid=bidid).values_list('jobtype2', flat=True)
    g2 = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True)
    gg2 = g2.first()
    i2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfg', flat=True).first()
    j2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfgmodeldescrip', flat=True)
    k2 = Equipment2.objects.filter(modelnum=gg2).values_list('eff', flat=True)
    l2 = Equipment2.objects.filter(modelnum=gg2).values_list('btu', flat=True)
    m2 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n2 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e2, type=f2, mfg=i2,
                                   modelnum=g2,
                                   description=j2, eff=k2, btu=l2, cost=m2)

    e3 = Bidding.objects.filter(bidid=bidid).values_list('quanity3', flat=True)
    f3 = Bidding.objects.filter(bidid=bidid).values_list('jobtype3', flat=True)
    g3 = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True)
    gg3 = g3.first()
    i3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfg', flat=True).first()
    j3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfgmodeldescrip', flat=True)
    k3 = Equipment2.objects.filter(modelnum=gg3).values_list('eff', flat=True)
    l3 = Equipment2.objects.filter(modelnum=gg3).values_list('btu', flat=True)
    m3 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n3 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e3, type=f3, mfg=i3,
                                   modelnum=g3,
                                   description=j3, eff=k3, btu=l3, cost=m3)

    e4 = Bidding.objects.filter(bidid=bidid).values_list('quanity4', flat=True)
    f4 = Bidding.objects.filter(bidid=bidid).values_list('jobtype4', flat=True)
    g4 = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True)
    gg4 = g4.first()
    i4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfg', flat=True).first()
    j4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfgmodeldescrip', flat=True)
    k4 = Equipment2.objects.filter(modelnum=gg4).values_list('eff', flat=True)
    l4 = Equipment2.objects.filter(modelnum=gg4).values_list('btu', flat=True)
    m4 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n4 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e4, type=f4, mfg=i4,
                                   modelnum=g4,
                                   description=j4, eff=k4, btu=l4, cost=m4)

    e5 = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True)
    f5 = Bidding.objects.filter(bidid=bidid).values_list('jobtype5', flat=True)
    g5 = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True)
    gg5 = g5.first()
    i5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfg', flat=True).first()
    j5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfgmodeldescrip', flat=True)
    k5 = Equipment2.objects.filter(modelnum=gg5).values_list('eff', flat=True)
    l5 = Equipment2.objects.filter(modelnum=gg5).values_list('btu', flat=True)
    m5 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n5 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e5, type=f5, mfg=i5,
                                   modelnum=g5,
                                   description=j5, eff=k5, btu=l5, cost=m5)

    e6 = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True)
    f6 = Bidding.objects.filter(bidid=bidid).values_list('jobtype6', flat=True)
    g6 = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True)
    gg6 = g6.first()
    i6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfg', flat=True).first()
    j6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfgmodeldescrip', flat=True)
    k6 = Equipment2.objects.filter(modelnum=gg6).values_list('eff', flat=True)
    l6 = Equipment2.objects.filter(modelnum=gg6).values_list('btu', flat=True)
    m6 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n6 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e6, type=f6, mfg=i6,
                                   modelnum=g6,
                                   description=j6, eff=k6, btu=l6, cost=m6)

    e7 = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True)
    f7 = Bidding.objects.filter(bidid=bidid).values_list('jobtype7', flat=True)
    g7 = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True)
    gg7 = g7.first()
    i7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfg', flat=True).first()
    j7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfgmodeldescrip', flat=True)
    k7 = Equipment2.objects.filter(modelnum=gg7).values_list('eff', flat=True)
    l7 = Equipment2.objects.filter(modelnum=gg7).values_list('btu', flat=True)
    m7 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n7 = multiformB.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e7, type=f7, mfg=i7,
                                   modelnum=g7,
                                   description=j7, eff=k7, btu=l7, cost=m7)

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "g": g,
        "h": h,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "n5": n5,
        "n6": n6,
        "n7": n7,
        "grandtotalcost": grandtotalcost,
    }
    return render(request, 'mha/contract.html', context)


def contractC(request, bidid=None):
    multiformC.objects.filter(bidid=bidid).delete()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(id=1).all()
    queryset3 = SelectedEquip.objects.filter(id=2).all()
    queryset4 = SelectedEquip.objects.filter(id=3).all()
    queryset5 = SelectedEquip.objects.filter(id=4).all()
    queryset6 = SelectedEquip.objects.filter(id=5).all()
    queryset7 = SelectedEquip.objects.filter(id=6).all()
    queryset8 = SelectedEquip.objects.filter(id=7).all()
    queryset9 = EquipSelection.objects.filter(bidid=bidid).all()
    queryset10 = Contract.objects.filter(bidid=bidid).all()
    b = TotalJobCost.objects.filter(bidid=bidid).aggregate(total_price=Sum('jobcost'))
    c = b['total_price']
    d = EquipSelection.objects.filter(bidid=bidid).values_list('totalrebate', flat=True)
    e = d.first()
    f = c - e
    g = Contract.objects.filter(bidid=bidid).update(costbeforrebate=c, totalrebate=e, totaljobcost=f)
    grandtotalcost = num2words(f, to='currency', currency='USD')

    h = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=c, rebatetotal=e, loccostafterrebate=f)

    aa = EquipSelection.objects.filter(bidid=bidid).values_list('custid', flat=True)
    bb = EquipSelection.objects.filter(bidid=bidid).values_list('jobid', flat=True)
    cc = EquipSelection.objects.filter(bidid=bidid).values_list('bidid', flat=True)
    dd1 = EquipSelection.objects.filter(bidid=bidid).values_list('optionid', flat=True)
    dd = EquipSelection.objects.filter(bidid=bidid).values_list('options', flat=True)

    e1 = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True)
    gg1 = g1.first()
    i1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfg', flat=True).first()
    j1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfgmodeldescrip', flat=True)
    k1 = Equipment2.objects.filter(modelnum=gg1).values_list('eff', flat=True)
    l1 = Equipment2.objects.filter(modelnum=gg1).values_list('btu', flat=True)
    m1 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n1 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e1, type=f1, mfg=i1,
                                   modelnum=g1,
                                   description=j1, eff=k1, btu=l1, cost=m1)

    e2 = Bidding.objects.filter(bidid=bidid).values_list('quanity2', flat=True)
    f2 = Bidding.objects.filter(bidid=bidid).values_list('jobtype2', flat=True)
    g2 = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True)
    gg2 = g2.first()
    i2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfg', flat=True).first()
    j2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfgmodeldescrip', flat=True)
    k2 = Equipment2.objects.filter(modelnum=gg2).values_list('eff', flat=True)
    l2 = Equipment2.objects.filter(modelnum=gg2).values_list('btu', flat=True)
    m2 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n2 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e2, type=f2, mfg=i2,
                                   modelnum=g2,
                                   description=j2, eff=k2, btu=l2, cost=m2)

    e3 = Bidding.objects.filter(bidid=bidid).values_list('quanity3', flat=True)
    f3 = Bidding.objects.filter(bidid=bidid).values_list('jobtype3', flat=True)
    g3 = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True)
    gg3 = g3.first()
    i3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfg', flat=True).first()
    j3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfgmodeldescrip', flat=True)
    k3 = Equipment2.objects.filter(modelnum=gg3).values_list('eff', flat=True)
    l3 = Equipment2.objects.filter(modelnum=gg3).values_list('btu', flat=True)
    m3 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n3 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e3, type=f3, mfg=i3,
                                   modelnum=g3,
                                   description=j3, eff=k3, btu=l3, cost=m3)

    e4 = Bidding.objects.filter(bidid=bidid).values_list('quanity4', flat=True)
    f4 = Bidding.objects.filter(bidid=bidid).values_list('jobtype4', flat=True)
    g4 = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True)
    gg4 = g4.first()
    i4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfg', flat=True).first()
    j4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfgmodeldescrip', flat=True)
    k4 = Equipment2.objects.filter(modelnum=gg4).values_list('eff', flat=True)
    l4 = Equipment2.objects.filter(modelnum=gg4).values_list('btu', flat=True)
    m4 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n4 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e4, type=f4, mfg=i4,
                                   modelnum=g4,
                                   description=j4, eff=k4, btu=l4, cost=m4)

    e5 = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True)
    f5 = Bidding.objects.filter(bidid=bidid).values_list('jobtype5', flat=True)
    g5 = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True)
    gg5 = g5.first()
    i5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfg', flat=True).first()
    j5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfgmodeldescrip', flat=True)
    k5 = Equipment2.objects.filter(modelnum=gg5).values_list('eff', flat=True)
    l5 = Equipment2.objects.filter(modelnum=gg5).values_list('btu', flat=True)
    m5 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n5 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e5, type=f5, mfg=i5,
                                   modelnum=g5,
                                   description=j5, eff=k5, btu=l5, cost=m5)

    e6 = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True)
    f6 = Bidding.objects.filter(bidid=bidid).values_list('jobtype6', flat=True)
    g6 = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True)
    gg6 = g6.first()
    i6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfg', flat=True).first()
    j6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfgmodeldescrip', flat=True)
    k6 = Equipment2.objects.filter(modelnum=gg6).values_list('eff', flat=True)
    l6 = Equipment2.objects.filter(modelnum=gg6).values_list('btu', flat=True)
    m6 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n6 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e6, type=f6, mfg=i6,
                                   modelnum=g6,
                                   description=j6, eff=k6, btu=l6, cost=m6)

    e7 = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True)
    f7 = Bidding.objects.filter(bidid=bidid).values_list('jobtype7', flat=True)
    g7 = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True)
    gg7 = g7.first()
    i7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfg', flat=True).first()
    j7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfgmodeldescrip', flat=True)
    k7 = Equipment2.objects.filter(modelnum=gg7).values_list('eff', flat=True)
    l7 = Equipment2.objects.filter(modelnum=gg7).values_list('btu', flat=True)
    m7 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n7 = multiformC.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e7, type=f7, mfg=i7,
                                   modelnum=g7,
                                   description=j7, eff=k7, btu=l7, cost=m7)

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "g": g,
        "h": h,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "n5": n5,
        "n6": n6,
        "n7": n7,
        "grandtotalcost": grandtotalcost,
    }
    return render(request, 'mha/contract.html', context)


def contractD(request, bidid=None):
    multiformC.objects.filter(bidid=bidid).delete()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(id=1).all()
    queryset3 = SelectedEquip.objects.filter(id=2).all()
    queryset4 = SelectedEquip.objects.filter(id=3).all()
    queryset5 = SelectedEquip.objects.filter(id=4).all()
    queryset6 = SelectedEquip.objects.filter(id=5).all()
    queryset7 = SelectedEquip.objects.filter(id=6).all()
    queryset8 = SelectedEquip.objects.filter(id=7).all()
    queryset9 = EquipSelection.objects.filter(bidid=bidid).all()
    queryset10 = Contract.objects.filter(bidid=bidid).all()
    b = TotalJobCost.objects.filter(bidid=bidid).aggregate(total_price=Sum('jobcost'))
    c = b['total_price']
    d = EquipSelection.objects.filter(bidid=bidid).values_list('totalrebate', flat=True)
    e = d.first()
    f = c - e
    g = Contract.objects.filter(bidid=bidid).update(costbeforrebate=c, totalrebate=e, totaljobcost=f)
    grandtotalcost = num2words(f, to='currency', currency='USD')

    h = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=c, rebatetotal=e, loccostafterrebate=f)

    aa = EquipSelection.objects.filter(bidid=bidid).values_list('custid', flat=True)
    bb = EquipSelection.objects.filter(bidid=bidid).values_list('jobid', flat=True)
    cc = EquipSelection.objects.filter(bidid=bidid).values_list('bidid', flat=True)
    dd1 = EquipSelection.objects.filter(bidid=bidid).values_list('optionid', flat=True)
    dd = EquipSelection.objects.filter(bidid=bidid).values_list('options', flat=True)

    e1 = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True)
    gg1 = g1.first()
    i1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfg', flat=True).first()
    j1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfgmodeldescrip', flat=True)
    k1 = Equipment2.objects.filter(modelnum=gg1).values_list('eff', flat=True)
    l1 = Equipment2.objects.filter(modelnum=gg1).values_list('btu', flat=True)
    m1 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n1 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e1, type=f1, mfg=i1,
                                   modelnum=g1,
                                   description=j1, eff=k1, btu=l1, cost=m1)

    e2 = Bidding.objects.filter(bidid=bidid).values_list('quanity2', flat=True)
    f2 = Bidding.objects.filter(bidid=bidid).values_list('jobtype2', flat=True)
    g2 = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True)
    gg2 = g2.first()
    i2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfg', flat=True).first()
    j2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfgmodeldescrip', flat=True)
    k2 = Equipment2.objects.filter(modelnum=gg2).values_list('eff', flat=True)
    l2 = Equipment2.objects.filter(modelnum=gg2).values_list('btu', flat=True)
    m2 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n2 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e2, type=f2, mfg=i2,
                                   modelnum=g2,
                                   description=j2, eff=k2, btu=l2, cost=m2)

    e3 = Bidding.objects.filter(bidid=bidid).values_list('quanity3', flat=True)
    f3 = Bidding.objects.filter(bidid=bidid).values_list('jobtype3', flat=True)
    g3 = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True)
    gg3 = g3.first()
    i3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfg', flat=True).first()
    j3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfgmodeldescrip', flat=True)
    k3 = Equipment2.objects.filter(modelnum=gg3).values_list('eff', flat=True)
    l3 = Equipment2.objects.filter(modelnum=gg3).values_list('btu', flat=True)
    m3 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n3 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e3, type=f3, mfg=i3,
                                   modelnum=g3,
                                   description=j3, eff=k3, btu=l3, cost=m3)

    e4 = Bidding.objects.filter(bidid=bidid).values_list('quanity4', flat=True)
    f4 = Bidding.objects.filter(bidid=bidid).values_list('jobtype4', flat=True)
    g4 = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True)
    gg4 = g4.first()
    i4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfg', flat=True).first()
    j4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfgmodeldescrip', flat=True)
    k4 = Equipment2.objects.filter(modelnum=gg4).values_list('eff', flat=True)
    l4 = Equipment2.objects.filter(modelnum=gg4).values_list('btu', flat=True)
    m4 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n4 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e4, type=f4, mfg=i4,
                                   modelnum=g4,
                                   description=j4, eff=k4, btu=l4, cost=m4)

    e5 = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True)
    f5 = Bidding.objects.filter(bidid=bidid).values_list('jobtype5', flat=True)
    g5 = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True)
    gg5 = g5.first()
    i5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfg', flat=True).first()
    j5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfgmodeldescrip', flat=True)
    k5 = Equipment2.objects.filter(modelnum=gg5).values_list('eff', flat=True)
    l5 = Equipment2.objects.filter(modelnum=gg5).values_list('btu', flat=True)
    m5 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n5 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e5, type=f5, mfg=i5,
                                   modelnum=g5,
                                   description=j5, eff=k5, btu=l5, cost=m5)

    e6 = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True)
    f6 = Bidding.objects.filter(bidid=bidid).values_list('jobtype6', flat=True)
    g6 = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True)
    gg6 = g6.first()
    i6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfg', flat=True).first()
    j6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfgmodeldescrip', flat=True)
    k6 = Equipment2.objects.filter(modelnum=gg6).values_list('eff', flat=True)
    l6 = Equipment2.objects.filter(modelnum=gg6).values_list('btu', flat=True)
    m6 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n6 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e6, type=f6, mfg=i6,
                                   modelnum=g6,
                                   description=j6, eff=k6, btu=l6, cost=m6)

    e7 = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True)
    f7 = Bidding.objects.filter(bidid=bidid).values_list('jobtype7', flat=True)
    g7 = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True)
    gg7 = g7.first()
    i7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfg', flat=True).first()
    j7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfgmodeldescrip', flat=True)
    k7 = Equipment2.objects.filter(modelnum=gg7).values_list('eff', flat=True)
    l7 = Equipment2.objects.filter(modelnum=gg7).values_list('btu', flat=True)
    m7 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n7 = multiformD.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e7, type=f7, mfg=i7,
                                   modelnum=g7,
                                   description=j7, eff=k7, btu=l7, cost=m7)

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "g": g,
        "h": h,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "n5": n5,
        "n6": n6,
        "n7": n7,
        "grandtotalcost": grandtotalcost,
    }
    return render(request, 'mha/contract.html', context)


def contractE(request, bidid=None):
    multiformC.objects.filter(bidid=bidid).delete()
    instance = get_object_or_404(Contract, bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = Contract.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(id=1).all()
    queryset3 = SelectedEquip.objects.filter(id=2).all()
    queryset4 = SelectedEquip.objects.filter(id=3).all()
    queryset5 = SelectedEquip.objects.filter(id=4).all()
    queryset6 = SelectedEquip.objects.filter(id=5).all()
    queryset7 = SelectedEquip.objects.filter(id=6).all()
    queryset8 = SelectedEquip.objects.filter(id=7).all()
    queryset9 = EquipSelection.objects.filter(bidid=bidid).all()
    queryset10 = Contract.objects.filter(bidid=bidid).all()
    b = TotalJobCost.objects.filter(bidid=bidid).aggregate(total_price=Sum('jobcost'))
    c = b['total_price']
    d = EquipSelection.objects.filter(bidid=bidid).values_list('totalrebate', flat=True)
    e = d.first()
    f = c - e
    g = Contract.objects.filter(bidid=bidid).update(costbeforrebate=c, totalrebate=e, totaljobcost=f)
    grandtotalcost = num2words(f, to='currency', currency='USD')

    h = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=c, rebatetotal=e, loccostafterrebate=f)

    aa = EquipSelection.objects.filter(bidid=bidid).values_list('custid', flat=True)
    bb = EquipSelection.objects.filter(bidid=bidid).values_list('jobid', flat=True)
    cc = EquipSelection.objects.filter(bidid=bidid).values_list('bidid', flat=True)
    dd1 = EquipSelection.objects.filter(bidid=bidid).values_list('optionid', flat=True)
    dd = EquipSelection.objects.filter(bidid=bidid).values_list('options', flat=True)

    e1 = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    f1 = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True)
    g1 = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True)
    gg1 = g1.first()
    i1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfg', flat=True).first()
    j1 = Equipment2.objects.filter(modelnum=gg1).values_list('mfgmodeldescrip', flat=True)
    k1 = Equipment2.objects.filter(modelnum=gg1).values_list('eff', flat=True)
    l1 = Equipment2.objects.filter(modelnum=gg1).values_list('btu', flat=True)
    m1 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n1 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e1, type=f1, mfg=i1,
                                   modelnum=g1,
                                   description=j1, eff=k1, btu=l1, cost=m1)

    e2 = Bidding.objects.filter(bidid=bidid).values_list('quanity2', flat=True)
    f2 = Bidding.objects.filter(bidid=bidid).values_list('jobtype2', flat=True)
    g2 = Bidding.objects.filter(bidid=bidid).values_list('descript2', flat=True)
    gg2 = g2.first()
    i2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfg', flat=True).first()
    j2 = Equipment2.objects.filter(modelnum=gg2).values_list('mfgmodeldescrip', flat=True)
    k2 = Equipment2.objects.filter(modelnum=gg2).values_list('eff', flat=True)
    l2 = Equipment2.objects.filter(modelnum=gg2).values_list('btu', flat=True)
    m2 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n2 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e2, type=f2, mfg=i2,
                                   modelnum=g2,
                                   description=j2, eff=k2, btu=l2, cost=m2)

    e3 = Bidding.objects.filter(bidid=bidid).values_list('quanity3', flat=True)
    f3 = Bidding.objects.filter(bidid=bidid).values_list('jobtype3', flat=True)
    g3 = Bidding.objects.filter(bidid=bidid).values_list('descript3', flat=True)
    gg3 = g3.first()
    i3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfg', flat=True).first()
    j3 = Equipment2.objects.filter(modelnum=gg3).values_list('mfgmodeldescrip', flat=True)
    k3 = Equipment2.objects.filter(modelnum=gg3).values_list('eff', flat=True)
    l3 = Equipment2.objects.filter(modelnum=gg3).values_list('btu', flat=True)
    m3 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n3 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e3, type=f3, mfg=i3,
                                   modelnum=g3,
                                   description=j3, eff=k3, btu=l3, cost=m3)

    e4 = Bidding.objects.filter(bidid=bidid).values_list('quanity4', flat=True)
    f4 = Bidding.objects.filter(bidid=bidid).values_list('jobtype4', flat=True)
    g4 = Bidding.objects.filter(bidid=bidid).values_list('descript4', flat=True)
    gg4 = g4.first()
    i4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfg', flat=True).first()
    j4 = Equipment2.objects.filter(modelnum=gg4).values_list('mfgmodeldescrip', flat=True)
    k4 = Equipment2.objects.filter(modelnum=gg4).values_list('eff', flat=True)
    l4 = Equipment2.objects.filter(modelnum=gg4).values_list('btu', flat=True)
    m4 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n4 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e4, type=f4, mfg=i4,
                                   modelnum=g4,
                                   description=j4, eff=k4, btu=l4, cost=m4)

    e5 = Bidding.objects.filter(bidid=bidid).values_list('quanity5', flat=True)
    f5 = Bidding.objects.filter(bidid=bidid).values_list('jobtype5', flat=True)
    g5 = Bidding.objects.filter(bidid=bidid).values_list('descript5', flat=True)
    gg5 = g5.first()
    i5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfg', flat=True).first()
    j5 = Equipment2.objects.filter(modelnum=gg5).values_list('mfgmodeldescrip', flat=True)
    k5 = Equipment2.objects.filter(modelnum=gg5).values_list('eff', flat=True)
    l5 = Equipment2.objects.filter(modelnum=gg5).values_list('btu', flat=True)
    m5 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n5 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e5, type=f5, mfg=i5,
                                   modelnum=g5,
                                   description=j5, eff=k5, btu=l5, cost=m5)

    e6 = Bidding.objects.filter(bidid=bidid).values_list('quanity6', flat=True)
    f6 = Bidding.objects.filter(bidid=bidid).values_list('jobtype6', flat=True)
    g6 = Bidding.objects.filter(bidid=bidid).values_list('descript6', flat=True)
    gg6 = g6.first()
    i6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfg', flat=True).first()
    j6 = Equipment2.objects.filter(modelnum=gg6).values_list('mfgmodeldescrip', flat=True)
    k6 = Equipment2.objects.filter(modelnum=gg6).values_list('eff', flat=True)
    l6 = Equipment2.objects.filter(modelnum=gg6).values_list('btu', flat=True)
    m6 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n6 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e6, type=f6, mfg=i6,
                                   modelnum=g6,
                                   description=j6, eff=k6, btu=l6, cost=m6)

    e7 = Bidding.objects.filter(bidid=bidid).values_list('quanity7', flat=True)
    f7 = Bidding.objects.filter(bidid=bidid).values_list('jobtype7', flat=True)
    g7 = Bidding.objects.filter(bidid=bidid).values_list('descript7', flat=True)
    gg7 = g7.first()
    i7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfg', flat=True).first()
    j7 = Equipment2.objects.filter(modelnum=gg7).values_list('mfgmodeldescrip', flat=True)
    k7 = Equipment2.objects.filter(modelnum=gg7).values_list('eff', flat=True)
    l7 = Equipment2.objects.filter(modelnum=gg7).values_list('btu', flat=True)
    m7 = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n7 = multiformE.objects.create(custid=aa, jobid=bb, bidid=cc, optionid=dd1, options=dd, quanity=e7, type=f7, mfg=i7,
                                   modelnum=g7,
                                   description=j7, eff=k7, btu=l7, cost=m7)

    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,
        "g": g,
        "h": h,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "n5": n5,
        "n6": n6,
        "n7": n7,
        "grandtotalcost": grandtotalcost,
    }
    return render(request, 'mha/contract.html', context)


def contractmulti2(request, jobid=None):
    instance = Contract.objects.filter(jobid=jobid).first()
    form = ContractForm(request.POST or None, instance=instance)
    a = Bidding.objects.filter(jobid=jobid).values_list('custid', flat=True).last()
    a4 = Bidding.objects.filter(jobid=jobid).values_list('jobid', flat=True).last()

    d = SelectedEquip.objects.filter(jobid=a4).annotate(bididG=F('bidid'))
    dd = list(d.values_list('bidid', flat=True))
    ee = sorted(list(set(dd)), reverse=False) 

    try:
        e = ee[0]
    except Exception as ee:
        e = 0

    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(equipid=1, bidid=e).all()
    queryset3 = SelectedEquip.objects.filter(equipid=2, bidid=e, jobid=a4).all()
    queryset4 = SelectedEquip.objects.filter(equipid=3, bidid=e, jobid=a4).all()
    queryset5 = SelectedEquip.objects.filter(equipid=4, bidid=e, jobid=a4).all()
    queryset6 = SelectedEquip.objects.filter(equipid=5, bidid=e, jobid=a4).all()
    queryset7 = SelectedEquip.objects.filter(equipid=6, bidid=e, jobid=a4).all()
    queryset8 = SelectedEquip.objects.filter(equipid=7, bidid=e, jobid=a4).all()
    queryset9 = EquipSelection.objects.filter(bidid=e).all()
    queryset10 = Contract.objects.filter(bidid=e).all()

    try:
        e1 = ee[1]
    except Exception as ee:
        e1 = 0
    querysetb = CustomerInfo.objects.filter(id=a).all()
    queryset2b = SelectedEquip.objects.filter(equipid=1, bidid=e1).all()
    queryset3b = SelectedEquip.objects.filter(equipid=2, bidid=e1, jobid=a4).all()
    queryset4b = SelectedEquip.objects.filter(equipid=3, bidid=e1, jobid=a4).all()
    queryset5b = SelectedEquip.objects.filter(equipid=4, bidid=e1, jobid=a4).all()
    queryset6b = SelectedEquip.objects.filter(equipid=5, bidid=e1, jobid=a4).all()
    queryset7b = SelectedEquip.objects.filter(equipid=6, bidid=e1, jobid=a4).all()
    queryset8b = SelectedEquip.objects.filter(equipid=7, bidid=e1, jobid=a4).all()
    queryset9b = EquipSelection.objects.filter(bidid=e1).all()
    queryset10b = Contract.objects.filter(bidid=e1).all()

#    try:
#        e2 = ee[2]
#    except Exception as ee:
#        e2 = 0
#    querysetc = CustomerInfo.objects.filter(id=a).all()
#    queryset2c = SelectedEquip.objects.filter(equipid=1, bidid=e2).all()
#    queryset3c = SelectedEquip.objects.filter(equipid=2, bidid=e2, jobid=a4).all()
#    queryset4c = SelectedEquip.objects.filter(equipid=3, bidid=e2, jobid=a4).all()
#    queryset5c = SelectedEquip.objects.filter(equipid=4, bidid=e2, jobid=a4).all()
#    queryset6c = SelectedEquip.objects.filter(equipid=5, bidid=e2, jobid=a4).all()
#    queryset7c = SelectedEquip.objects.filter(equipid=6, bidid=e2, jobid=a4).all()
#    queryset8c = SelectedEquip.objects.filter(equipid=7, bidid=e2, jobid=a4).all()
#    queryset9c = EquipSelection.objects.filter(bidid=e2).all()
#    queryset10c = Contract.objects.filter(bidid=e2).all()
#
#
#    try:
#        e3 = ee[3]
#    except Exception as ee:
#        e3 = 0
#    querysetd = CustomerInfo.objects.filter(id=a).all()
#    queryset2d = SelectedEquip.objects.filter(equipid=1, bidid=e3).all()
#    queryset3d = SelectedEquip.objects.filter(equipid=2, bidid=e3, jobid=a4).all()
#    queryset4d = SelectedEquip.objects.filter(equipid=3, bidid=e3, jobid=a4).all()
#    queryset5d = SelectedEquip.objects.filter(equipid=4, bidid=e3, jobid=a4).all()
#    queryset6d = SelectedEquip.objects.filter(equipid=5, bidid=e3, jobid=a4).all()
#    queryset7d = SelectedEquip.objects.filter(equipid=6, bidid=e3, jobid=a4).all()
#    queryset8d = SelectedEquip.objects.filter(equipid=7, bidid=e3, jobid=a4).all()
#    queryset9d = EquipSelection.objects.filter(bidid=e3).all()
#    queryset10d = Contract.objects.filter(bidid=e3).all()
#
#
#    try:
#        e4 = ee[4]
#    except Exception as ee:
#        e4 = 0
#    querysete = CustomerInfo.objects.filter(id=a).all()
#    queryset2e = SelectedEquip.objects.filter(equipid=1, bidid=e4).all()
#    queryset3e = SelectedEquip.objects.filter(equipid=2, bidid=e4, jobid=a4).all()
#    queryset4e = SelectedEquip.objects.filter(equipid=3, bidid=e4, jobid=a4).all()
#    queryset5e = SelectedEquip.objects.filter(equipid=4, bidid=e4, jobid=a4).all()
#    queryset6e = SelectedEquip.objects.filter(equipid=5, bidid=e4, jobid=a4).all()
#    queryset7e = SelectedEquip.objects.filter(equipid=6, bidid=e4, jobid=a4).all()
#    queryset8e = SelectedEquip.objects.filter(equipid=7, bidid=e4, jobid=a4).all()
#    queryset9e = EquipSelection.objects.filter(bidid=e4).all()
#    queryset10e = Contract.objects.filter(bidid=e4).all()


    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,

        "object_lisbt": querysetb,
        "object_list2b": queryset2b,
        "object_list3b": queryset3b,
        "object_list4b": queryset4b,
        "object_list5b": queryset5b,
        "object_list6b": queryset6b,
        "object_list7b": queryset7b,
        "object_list8b": queryset8b,
        "object_list9b": queryset9b,
        "object_list10b": queryset10b,

#        "object_lisbt": querysetc,
#        "object_list2c": queryset2c,
#        "object_list3c": queryset3c,
#        "object_list4c": queryset4c,
#        "object_list5c": queryset5c,
#        "object_list6c": queryset6c,
#        "object_list7c": queryset7c,
#        "object_list8c": queryset8c,
#        "object_list9c": queryset9c,
#        "object_list10c": queryset10c,
#
#        "object_lisbt": querysetd,
#        "object_list2d": queryset2d,
#        "object_list3d": queryset3d,
#        "object_list4d": queryset4d,
#        "object_list5d": queryset5d,
#        "object_list6d": queryset6d,
#        "object_list7d": queryset7d,
#        "object_list8d": queryset8d,
#        "object_list9d": queryset9d,
#        "object_list10d": queryset10d,
#
#        "object_lisbt": querysete,
#        "object_list2e": queryset2e,
#        "object_list3e": queryset3e,
#        "object_list4e": queryset4e,
#        "object_list5e": queryset5e,
#        "object_list6e": queryset6e,
#        "object_list7e": queryset7e,
#        "object_list8e": queryset8e,
#        "object_list9e": queryset9e,
#        "object_list10e": queryset10e,
    }
    return render(request, 'mha/contractmulti2.html', context)


def contractmulti3(request, jobid=None):
    instance = Contract.objects.filter(jobid=jobid).first()
    form = ContractForm(request.POST or None, instance=instance)
#    JobCost.objects.filter(jobid=jobid).delete()
    a = Bidding.objects.filter(jobid=jobid).values_list('custid', flat=True).last()
    a2 = Bidding.objects.filter(jobid=jobid).values_list('conid', flat=True).last()
    a3 = Bidding.objects.filter(jobid=jobid).values_list('bidid', flat=True).last()
    a4 = Bidding.objects.filter(jobid=jobid).values_list('jobid', flat=True).last()
 #   a5 = JobCost.objects.create(conid=a2, custid=a, bidid=a3, jobid=a4)

    d = SelectedEquip.objects.filter(jobid=a4).annotate(bididG=F('bidid'))
    dd = list(d.values_list('bidid', flat=True))
    ee = sorted(list(set(dd)), reverse=False)

    try:
        e = ee[0]
    except Exception as ee:
        e = 0

    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(equipid=1, bidid=e).all()
    queryset3 = SelectedEquip.objects.filter(equipid=2, bidid=e, jobid=a4).all()
    queryset4 = SelectedEquip.objects.filter(equipid=3, bidid=e, jobid=a4).all()
    queryset5 = SelectedEquip.objects.filter(equipid=4, bidid=e, jobid=a4).all()
    queryset6 = SelectedEquip.objects.filter(equipid=5, bidid=e, jobid=a4).all()
    queryset7 = SelectedEquip.objects.filter(equipid=6, bidid=e, jobid=a4).all()
    queryset8 = SelectedEquip.objects.filter(equipid=7, bidid=e, jobid=a4).all()
    queryset9 = EquipSelection.objects.filter(bidid=e).all()
    queryset10 = Contract.objects.filter(bidid=e).all()

    try:
        e1 = ee[1]
    except Exception as ee:
        e1 = 0
    querysetb = CustomerInfo.objects.filter(id=a).all()
    queryset2b = SelectedEquip.objects.filter(equipid=1, bidid=e1).all()
    queryset3b = SelectedEquip.objects.filter(equipid=2, bidid=e1, jobid=a4).all()
    queryset4b = SelectedEquip.objects.filter(equipid=3, bidid=e1, jobid=a4).all()
    queryset5b = SelectedEquip.objects.filter(equipid=4, bidid=e1, jobid=a4).all()
    queryset6b = SelectedEquip.objects.filter(equipid=5, bidid=e1, jobid=a4).all()
    queryset7b = SelectedEquip.objects.filter(equipid=6, bidid=e1, jobid=a4).all()
    queryset8b = SelectedEquip.objects.filter(equipid=7, bidid=e1, jobid=a4).all()
    queryset9b = EquipSelection.objects.filter(bidid=e1).all()
    queryset10b = Contract.objects.filter(bidid=e1).all()

    try:
        e2 = ee[2]
    except Exception as ee:
        e2 = 0
    querysetc = CustomerInfo.objects.filter(id=a).all()
    queryset2c = SelectedEquip.objects.filter(equipid=1, bidid=e2).all()
    queryset3c = SelectedEquip.objects.filter(equipid=2, bidid=e2, jobid=a4).all()
    queryset4c = SelectedEquip.objects.filter(equipid=3, bidid=e2, jobid=a4).all()
    queryset5c = SelectedEquip.objects.filter(equipid=4, bidid=e2, jobid=a4).all()
    queryset6c = SelectedEquip.objects.filter(equipid=5, bidid=e2, jobid=a4).all()
    queryset7c = SelectedEquip.objects.filter(equipid=6, bidid=e2, jobid=a4).all()
    queryset8c = SelectedEquip.objects.filter(equipid=7, bidid=e2, jobid=a4).all()
    queryset9c = EquipSelection.objects.filter(bidid=e2).all()
    queryset10c = Contract.objects.filter(bidid=e2).all()


#    try:
#        e3 = ee[3]
#    except Exception as ee:
#        e3 = 0
#    querysetd = CustomerInfo.objects.filter(id=a).all()
#    queryset2d = SelectedEquip.objects.filter(equipid=1, bidid=e3).all()
#    queryset3d = SelectedEquip.objects.filter(equipid=2, bidid=e3, jobid=a4).all()
#    queryset4d = SelectedEquip.objects.filter(equipid=3, bidid=e3, jobid=a4).all()
#    queryset5d = SelectedEquip.objects.filter(equipid=4, bidid=e3, jobid=a4).all()
#    queryset6d = SelectedEquip.objects.filter(equipid=5, bidid=e3, jobid=a4).all()
#    queryset7d = SelectedEquip.objects.filter(equipid=6, bidid=e3, jobid=a4).all()
#    queryset8d = SelectedEquip.objects.filter(equipid=7, bidid=e3, jobid=a4).all()
#    queryset9d = EquipSelection.objects.filter(bidid=e3).all()
#    queryset10d = Contract.objects.filter(bidid=e3).all()
#
#
#    try:
#        e4 = ee[4]
#    except Exception as ee:
#        e4 = 0
#    querysete = CustomerInfo.objects.filter(id=a).all()
#    queryset2e = SelectedEquip.objects.filter(equipid=1, bidid=e4).all()
#    queryset3e = SelectedEquip.objects.filter(equipid=2, bidid=e4, jobid=a4).all()
#    queryset4e = SelectedEquip.objects.filter(equipid=3, bidid=e4, jobid=a4).all()
#    queryset5e = SelectedEquip.objects.filter(equipid=4, bidid=e4, jobid=a4).all()
#    queryset6e = SelectedEquip.objects.filter(equipid=5, bidid=e4, jobid=a4).all()
#    queryset7e = SelectedEquip.objects.filter(equipid=6, bidid=e4, jobid=a4).all()
#    queryset8e = SelectedEquip.objects.filter(equipid=7, bidid=e4, jobid=a4).all()
#    queryset9e = EquipSelection.objects.filter(bidid=e4).all()
#    queryset10e = Contract.objects.filter(bidid=e4).all()


    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,

        "object_lisbt": querysetb,
        "object_list2b": queryset2b,
        "object_list3b": queryset3b,
        "object_list4b": queryset4b,
        "object_list5b": queryset5b,
        "object_list6b": queryset6b,
        "object_list7b": queryset7b,
        "object_list8b": queryset8b,
        "object_list9b": queryset9b,
        "object_list10b": queryset10b,

        "object_lisbt": querysetc,
        "object_list2c": queryset2c,
        "object_list3c": queryset3c,
        "object_list4c": queryset4c,
        "object_list5c": queryset5c,
        "object_list6c": queryset6c,
        "object_list7c": queryset7c,
        "object_list8c": queryset8c,
        "object_list9c": queryset9c,
        "object_list10c": queryset10c,

#        "object_lisbt": querysetd,
#        "object_list2d": queryset2d,
#        "object_list3d": queryset3d,
#        "object_list4d": queryset4d,
#        "object_list5d": queryset5d,
#        "object_list6d": queryset6d,
#        "object_list7d": queryset7d,
#        "object_list8d": queryset8d,
#        "object_list9d": queryset9d,
#        "object_list10d": queryset10d,
#
#        "object_lisbt": querysete,
#        "object_list2e": queryset2e,
#        "object_list3e": queryset3e,
#        "object_list4e": queryset4e,
#        "object_list5e": queryset5e,
#        "object_list6e": queryset6e,
#        "object_list7e": queryset7e,
#        "object_list8e": queryset8e,
#        "object_list9e": queryset9e,
#        "object_list10e": queryset10e,
    }
    return render(request, 'mha/contractmulti3.html', context)


def contractmulti4(request, jobid=None):
    instance = Contract.objects.filter(jobid=jobid).first()
    form = ContractForm(request.POST or None, instance=instance)
#    JobCost.objects.filter(jobid=jobid).delete()
    a = Bidding.objects.filter(jobid=jobid).values_list('custid', flat=True).last()
    a2 = Bidding.objects.filter(jobid=jobid).values_list('conid', flat=True).last()
    a3 = Bidding.objects.filter(jobid=jobid).values_list('bidid', flat=True).last()
    a4 = Bidding.objects.filter(jobid=jobid).values_list('jobid', flat=True).last()
 #   a5 = JobCost.objects.create(conid=a2, custid=a, bidid=a3, jobid=a4)

    d = SelectedEquip.objects.filter(jobid=a4).annotate(bididG=F('bidid'))
    dd = list(d.values_list('bidid', flat=True))
    ee = sorted(list(set(dd)), reverse=False)

    try:
        e = ee[0]
    except Exception as ee:
        e = 0

    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(equipid=1, bidid=e).all()
    queryset3 = SelectedEquip.objects.filter(equipid=2, bidid=e, jobid=a4).all()
    queryset4 = SelectedEquip.objects.filter(equipid=3, bidid=e, jobid=a4).all()
    queryset5 = SelectedEquip.objects.filter(equipid=4, bidid=e, jobid=a4).all()
    queryset6 = SelectedEquip.objects.filter(equipid=5, bidid=e, jobid=a4).all()
    queryset7 = SelectedEquip.objects.filter(equipid=6, bidid=e, jobid=a4).all()
    queryset8 = SelectedEquip.objects.filter(equipid=7, bidid=e, jobid=a4).all()
    queryset9 = EquipSelection.objects.filter(bidid=e).all()
    queryset10 = Contract.objects.filter(bidid=e).all()

    try:
        e1 = ee[1]
    except Exception as ee:
        e1 = 0
    querysetb = CustomerInfo.objects.filter(id=a).all()
    queryset2b = SelectedEquip.objects.filter(equipid=1, bidid=e1).all()
    queryset3b = SelectedEquip.objects.filter(equipid=2, bidid=e1, jobid=a4).all()
    queryset4b = SelectedEquip.objects.filter(equipid=3, bidid=e1, jobid=a4).all()
    queryset5b = SelectedEquip.objects.filter(equipid=4, bidid=e1, jobid=a4).all()
    queryset6b = SelectedEquip.objects.filter(equipid=5, bidid=e1, jobid=a4).all()
    queryset7b = SelectedEquip.objects.filter(equipid=6, bidid=e1, jobid=a4).all()
    queryset8b = SelectedEquip.objects.filter(equipid=7, bidid=e1, jobid=a4).all()
    queryset9b = EquipSelection.objects.filter(bidid=e1).all()
    queryset10b = Contract.objects.filter(bidid=e1).all()

    try:
        e2 = ee[2]
    except Exception as ee:
        e2 = 0
    querysetc = CustomerInfo.objects.filter(id=a).all()
    queryset2c = SelectedEquip.objects.filter(equipid=1, bidid=e2).all()
    queryset3c = SelectedEquip.objects.filter(equipid=2, bidid=e2, jobid=a4).all()
    queryset4c = SelectedEquip.objects.filter(equipid=3, bidid=e2, jobid=a4).all()
    queryset5c = SelectedEquip.objects.filter(equipid=4, bidid=e2, jobid=a4).all()
    queryset6c = SelectedEquip.objects.filter(equipid=5, bidid=e2, jobid=a4).all()
    queryset7c = SelectedEquip.objects.filter(equipid=6, bidid=e2, jobid=a4).all()
    queryset8c = SelectedEquip.objects.filter(equipid=7, bidid=e2, jobid=a4).all()
    queryset9c = EquipSelection.objects.filter(bidid=e2).all()
    queryset10c = Contract.objects.filter(bidid=e2).all()


    try:
        e3 = ee[3]
    except Exception as ee:
        e3 = 0
    querysetd = CustomerInfo.objects.filter(id=a).all()
    queryset2d = SelectedEquip.objects.filter(equipid=1, bidid=e3).all()
    queryset3d = SelectedEquip.objects.filter(equipid=2, bidid=e3, jobid=a4).all()
    queryset4d = SelectedEquip.objects.filter(equipid=3, bidid=e3, jobid=a4).all()
    queryset5d = SelectedEquip.objects.filter(equipid=4, bidid=e3, jobid=a4).all()
    queryset6d = SelectedEquip.objects.filter(equipid=5, bidid=e3, jobid=a4).all()
    queryset7d = SelectedEquip.objects.filter(equipid=6, bidid=e3, jobid=a4).all()
    queryset8d = SelectedEquip.objects.filter(equipid=7, bidid=e3, jobid=a4).all()
    queryset9d = EquipSelection.objects.filter(bidid=e3).all()
    queryset10d = Contract.objects.filter(bidid=e3).all()


#    try:
#        e4 = ee[4]
#    except Exception as ee:
#        e4 = 0
#    querysete = CustomerInfo.objects.filter(id=a).all()
#    queryset2e = SelectedEquip.objects.filter(equipid=1, bidid=e4).all()
#    queryset3e = SelectedEquip.objects.filter(equipid=2, bidid=e4, jobid=a4).all()
#    queryset4e = SelectedEquip.objects.filter(equipid=3, bidid=e4, jobid=a4).all()
#    queryset5e = SelectedEquip.objects.filter(equipid=4, bidid=e4, jobid=a4).all()
#    queryset6e = SelectedEquip.objects.filter(equipid=5, bidid=e4, jobid=a4).all()
#    queryset7e = SelectedEquip.objects.filter(equipid=6, bidid=e4, jobid=a4).all()
#    queryset8e = SelectedEquip.objects.filter(equipid=7, bidid=e4, jobid=a4).all()
#    queryset9e = EquipSelection.objects.filter(bidid=e4).all()
#    queryset10e = Contract.objects.filter(bidid=e4).all()


    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,

        "object_lisbt": querysetb,
        "object_list2b": queryset2b,
        "object_list3b": queryset3b,
        "object_list4b": queryset4b,
        "object_list5b": queryset5b,
        "object_list6b": queryset6b,
        "object_list7b": queryset7b,
        "object_list8b": queryset8b,
        "object_list9b": queryset9b,
        "object_list10b": queryset10b,

        "object_lisbt": querysetc,
        "object_list2c": queryset2c,
        "object_list3c": queryset3c,
        "object_list4c": queryset4c,
        "object_list5c": queryset5c,
        "object_list6c": queryset6c,
        "object_list7c": queryset7c,
        "object_list8c": queryset8c,
        "object_list9c": queryset9c,
        "object_list10c": queryset10c,

        "object_lisbt": querysetd,
        "object_list2d": queryset2d,
        "object_list3d": queryset3d,
        "object_list4d": queryset4d,
        "object_list5d": queryset5d,
        "object_list6d": queryset6d,
        "object_list7d": queryset7d,
        "object_list8d": queryset8d,
        "object_list9d": queryset9d,
        "object_list10d": queryset10d,

#        "object_lisbt": querysete,
#        "object_list2e": queryset2e,
#        "object_list3e": queryset3e,
#        "object_list4e": queryset4e,
#        "object_list5e": queryset5e,
#        "object_list6e": queryset6e,
#        "object_list7e": queryset7e,
#        "object_list8e": queryset8e,
#        "object_list9e": queryset9e,
#        "object_list10e": queryset10e,
    }
    return render(request, 'mha/contractmulti4.html', context)



def contractmulti5(request, jobid=None):
    instance = Contract.objects.filter(jobid=jobid).first()
    form = ContractForm(request.POST or None, instance=instance)
#    JobCost.objects.filter(jobid=jobid).delete()
    a = Bidding.objects.filter(jobid=jobid).values_list('custid', flat=True).last()
    a2 = Bidding.objects.filter(jobid=jobid).values_list('conid', flat=True).last()
    a3 = Bidding.objects.filter(jobid=jobid).values_list('bidid', flat=True).last()
    a4 = Bidding.objects.filter(jobid=jobid).values_list('jobid', flat=True).last()
 #   a5 = JobCost.objects.create(conid=a2, custid=a, bidid=a3, jobid=a4)

    d = SelectedEquip.objects.filter(jobid=a4).annotate(bididG=F('bidid'))
    dd = list(d.values_list('bidid', flat=True))
    ee = sorted(list(set(dd)), reverse=False)

    try:
        e = ee[0]
    except Exception as ee:
        e = 0

    queryset = CustomerInfo.objects.filter(id=a).all()
    queryset2 = SelectedEquip.objects.filter(equipid=1, bidid=e).all()
    queryset3 = SelectedEquip.objects.filter(equipid=2, bidid=e, jobid=a4).all()
    queryset4 = SelectedEquip.objects.filter(equipid=3, bidid=e, jobid=a4).all()
    queryset5 = SelectedEquip.objects.filter(equipid=4, bidid=e, jobid=a4).all()
    queryset6 = SelectedEquip.objects.filter(equipid=5, bidid=e, jobid=a4).all()
    queryset7 = SelectedEquip.objects.filter(equipid=6, bidid=e, jobid=a4).all()
    queryset8 = SelectedEquip.objects.filter(equipid=7, bidid=e, jobid=a4).all()
    queryset9 = EquipSelection.objects.filter(bidid=e).all()
    queryset10 = Contract.objects.filter(bidid=e).all()

    try:
        e1 = ee[1]
    except Exception as ee:
        e1 = 0
    querysetb = CustomerInfo.objects.filter(id=a).all()
    queryset2b = SelectedEquip.objects.filter(equipid=1, bidid=e1).all()
    queryset3b = SelectedEquip.objects.filter(equipid=2, bidid=e1, jobid=a4).all()
    queryset4b = SelectedEquip.objects.filter(equipid=3, bidid=e1, jobid=a4).all()
    queryset5b = SelectedEquip.objects.filter(equipid=4, bidid=e1, jobid=a4).all()
    queryset6b = SelectedEquip.objects.filter(equipid=5, bidid=e1, jobid=a4).all()
    queryset7b = SelectedEquip.objects.filter(equipid=6, bidid=e1, jobid=a4).all()
    queryset8b = SelectedEquip.objects.filter(equipid=7, bidid=e1, jobid=a4).all()
    queryset9b = EquipSelection.objects.filter(bidid=e1).all()
    queryset10b = Contract.objects.filter(bidid=e1).all()

    try:
        e2 = ee[2]
    except Exception as ee:
        e2 = 0
    querysetc = CustomerInfo.objects.filter(id=a).all()
    queryset2c = SelectedEquip.objects.filter(equipid=1, bidid=e2).all()
    queryset3c = SelectedEquip.objects.filter(equipid=2, bidid=e2, jobid=a4).all()
    queryset4c = SelectedEquip.objects.filter(equipid=3, bidid=e2, jobid=a4).all()
    queryset5c = SelectedEquip.objects.filter(equipid=4, bidid=e2, jobid=a4).all()
    queryset6c = SelectedEquip.objects.filter(equipid=5, bidid=e2, jobid=a4).all()
    queryset7c = SelectedEquip.objects.filter(equipid=6, bidid=e2, jobid=a4).all()
    queryset8c = SelectedEquip.objects.filter(equipid=7, bidid=e2, jobid=a4).all()
    queryset9c = EquipSelection.objects.filter(bidid=e2).all()
    queryset10c = Contract.objects.filter(bidid=e2).all()


    try:
        e3 = ee[3]
    except Exception as ee:
        e3 = 0
    querysetd = CustomerInfo.objects.filter(id=a).all()
    queryset2d = SelectedEquip.objects.filter(equipid=1, bidid=e3).all()
    queryset3d = SelectedEquip.objects.filter(equipid=2, bidid=e3, jobid=a4).all()
    queryset4d = SelectedEquip.objects.filter(equipid=3, bidid=e3, jobid=a4).all()
    queryset5d = SelectedEquip.objects.filter(equipid=4, bidid=e3, jobid=a4).all()
    queryset6d = SelectedEquip.objects.filter(equipid=5, bidid=e3, jobid=a4).all()
    queryset7d = SelectedEquip.objects.filter(equipid=6, bidid=e3, jobid=a4).all()
    queryset8d = SelectedEquip.objects.filter(equipid=7, bidid=e3, jobid=a4).all()
    queryset9d = EquipSelection.objects.filter(bidid=e3).all()
    queryset10d = Contract.objects.filter(bidid=e3).all()


    try:
        e4 = ee[4]
    except Exception as ee:
        e4 = 0
    querysete = CustomerInfo.objects.filter(id=a).all()
    queryset2e = SelectedEquip.objects.filter(equipid=1, bidid=e4).all()
    queryset3e = SelectedEquip.objects.filter(equipid=2, bidid=e4, jobid=a4).all()
    queryset4e = SelectedEquip.objects.filter(equipid=3, bidid=e4, jobid=a4).all()
    queryset5e = SelectedEquip.objects.filter(equipid=4, bidid=e4, jobid=a4).all()
    queryset6e = SelectedEquip.objects.filter(equipid=5, bidid=e4, jobid=a4).all()
    queryset7e = SelectedEquip.objects.filter(equipid=6, bidid=e4, jobid=a4).all()
    queryset8e = SelectedEquip.objects.filter(equipid=7, bidid=e4, jobid=a4).all()
    queryset9e = EquipSelection.objects.filter(bidid=e4).all()
    queryset10e = Contract.objects.filter(bidid=e4).all()


    context = {
        "instance": instance,
        "form": form,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,
        "object_list6": queryset6,
        "object_list7": queryset7,
        "object_list8": queryset8,
        "object_list9": queryset9,
        "object_list10": queryset10,

        "object_lisbt": querysetb,
        "object_list2b": queryset2b,
        "object_list3b": queryset3b,
        "object_list4b": queryset4b,
        "object_list5b": queryset5b,
        "object_list6b": queryset6b,
        "object_list7b": queryset7b,
        "object_list8b": queryset8b,
        "object_list9b": queryset9b,
        "object_list10b": queryset10b,

        "object_lisbt": querysetc,
        "object_list2c": queryset2c,
        "object_list3c": queryset3c,
        "object_list4c": queryset4c,
        "object_list5c": queryset5c,
        "object_list6c": queryset6c,
        "object_list7c": queryset7c,
        "object_list8c": queryset8c,
        "object_list9c": queryset9c,
        "object_list10c": queryset10c,

        "object_lisbt": querysetd,
        "object_list2d": queryset2d,
        "object_list3d": queryset3d,
        "object_list4d": queryset4d,
        "object_list5d": queryset5d,
        "object_list6d": queryset6d,
        "object_list7d": queryset7d,
        "object_list8d": queryset8d,
        "object_list9d": queryset9d,
        "object_list10d": queryset10d,

        "object_lisbt": querysete,
        "object_list2e": queryset2e,
        "object_list3e": queryset3e,
        "object_list4e": queryset4e,
        "object_list5e": queryset5e,
        "object_list6e": queryset6e,
        "object_list7e": queryset7e,
        "object_list8e": queryset8e,
        "object_list9e": queryset9e,
        "object_list10e": queryset10e,
    }
    return render(request, 'mha/contractmulti5.html', context)


def contractdate(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_contractdate']
    Contract.objects.filter(bidid=bidid).update(contractdate=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_contractdate(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    c = a.values('contractdate').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/contract_date.html', context)


def downpaymentdate(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_downpaymentdate']
    Contract.objects.filter(bidid=bidid).update(downpaymentdate=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_downpaymentdate(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    c = a.values('downpaymentdate').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/downpayment_date.html', context)

def finalpaymentdate(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_finalpaymentdate']
    Contract.objects.filter(bidid=bidid).update(finalpaymentdate=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_finalpaymentdate(request, bidid=None):
    a = Contract.objects.all()
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    c = a.values('finalpaymentdate').get(bidid=bidid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute13_url())
    context = {
        "c": c,
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/finalpayment_date.html', context)

def memo31(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo31']
    Contract.objects.filter(bidid=bidid).update(memo31=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo1(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo1']
    Contract.objects.filter(bidid=bidid).update(memo1=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo1a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo1a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo1=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo1a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo1 = Contract.objects.values('memo1').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo1": memo1,
        "form": form,
    }
    return render(request, 'mha/memo1_1.html', context)


def memo2(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo2']
    Contract.objects.filter(bidid=bidid).update(memo2=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo2a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo2a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo2=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo2a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo2 = Contract.objects.values('memo2').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo2": memo2,
        "form": form,
    }
    return render(request, 'mha/memo2_1.html', context)


def memo3(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo3']
    Contract.objects.filter(bidid=bidid).update(memo3=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo3a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo3a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo3=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo3a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo3 = Contract.objects.values('memo3').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo3": memo3,
        "form": form,
    }
    return render(request, 'mha/memo3_1.html', context)


def memo4(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo4']
    Contract.objects.filter(bidid=bidid).update(memo4=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo4a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo4a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo4=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo4a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo4 = Contract.objects.values('memo4').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo4": memo4,
        "form": form,
    }
    return render(request, 'mha/memo4_1.html', context)


def memo5(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo5']
    Contract.objects.filter(bidid=bidid).update(memo5=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo5a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo5a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo5=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo5a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo5 = Contract.objects.values('memo5').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo5": memo5,
        "form": form,
    }
    return render(request, 'mha/memo5_1.html', context)


def memo6(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo6']
    Contract.objects.filter(bidid=bidid).update(memo6=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo6a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo6a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo6=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo6a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo6 = Contract.objects.values('memo6').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo6": memo6,
        "form": form,
    }
    return render(request, 'mha/memo6_1.html', context)


def memo7(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo7']
    Contract.objects.filter(bidid=bidid).update(memo7=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo7a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo7a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo7=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo7a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo7 = Contract.objects.values('memo7').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo7": memo7,
        "form": form,
    }
    return render(request, 'mha/memo7_1.html', context)


def memo8(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo8']
    Contract.objects.filter(bidid=bidid).update(memo8=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo8a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo8a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo8=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo8a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo8 = Contract.objects.values('memo8').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo8": memo8,
        "form": form,
    }
    return render(request, 'mha/memo8_1.html', context)


def memo9(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo9']
    Contract.objects.filter(bidid=bidid).update(memo9=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo9a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo9a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo9=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo9a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo9 = Contract.objects.values('memo9').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo9": memo9,
        "form": form,
    }
    return render(request, 'mha/memo9_1.html', context)


def memo10(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo10']
    Contract.objects.filter(bidid=bidid).update(memo10=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo10a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo10a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo10=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo10a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo10 = Contract.objects.values('memo10').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo10": memo10,
        "form": form,
    }
    return render(request, 'mha/memo10_1.html', context)


def memo11(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo11']
    Contract.objects.filter(bidid=bidid).update(memo11=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo11a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo11a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo11=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo11a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo11 = Contract.objects.values('memo11').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo11": memo11,
        "form": form,
    }
    return render(request, 'mha/memo11_1.html', context)


def memo12(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo12']
    Contract.objects.filter(bidid=bidid).update(memo12=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo12a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo12a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo12=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo12a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo12 = Contract.objects.values('memo12').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo12": memo12,
        "form": form,
    }
    return render(request, 'mha/memo12_1.html', context)


def memo13(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo13']
    Contract.objects.filter(bidid=bidid).update(memo13=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo13a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo13a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo13=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo13a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo13 = Contract.objects.values('memo13').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo13": memo13,
        "form": form,
    }
    return render(request, 'mha/memo13_1.html', context)


def memo14(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo14']
    Contract.objects.filter(bidid=bidid).update(memo14=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo14a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo14a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo14=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo14a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo14 = Contract.objects.values('memo14').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo14": memo14,
        "form": form,
    }
    return render(request, 'mha/memo14_1.html', context)


def memo15(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo15']
    Contract.objects.filter(bidid=bidid).update(memo15=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo15a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo15a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo15=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo15a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo15 = Contract.objects.values('memo15').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo15": memo15,
        "form": form,
    }
    return render(request, 'mha/memo15_1.html', context)


def memo16(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo16']
    Contract.objects.filter(bidid=bidid).update(memo16=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo16a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo16a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo16=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo16a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo16 = Contract.objects.values('memo16').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo16": memo16,
        "form": form,
    }
    return render(request, 'mha/memo16_1.html', context)


def memo17(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo17']
    Contract.objects.filter(bidid=bidid).update(memo17=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo17a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo17a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo17=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo17a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo17 = Contract.objects.values('memo17').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo17": memo17,
        "form": form,
    }
    return render(request, 'mha/memo17_1.html', context)


def memo18(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo18']
    Contract.objects.filter(bidid=bidid).update(memo18=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def memo18a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_memo18a']
    b = DetailTable.objects.values_list('id', flat=True).last()
    c = b+1
    DetailTable.objects.create(id=c, details=a)
    Contract.objects.filter(bidid=bidid).update(memo18=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_memo18a(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    memo18 = Contract.objects.values('memo18').get(bidid=bidid)
    context = {
        "instance": instance,
        "memo18": memo18,
        "form": form,
    }
    return render(request, 'mha/memo18_1.html', context)


def custpageloc(request):
    a = EquipSelection.objects.values_list('jobid', flat=True).last()
    form = EquipmentSelect1(request.POST or None)
    b = EquipSelection.objects.filter(jobid=a).values_list('custid', flat=True)
    bb = EquipSelection.objects.filter(jobid=a).values_list('conid', flat=True)
    c = EquipSelection.objects.filter(jobid=a).values_list('joblocation', flat=True)
    d = EquipSelection.objects.filter(jobid=a).values_list('created_at', flat=True)
    e = Custpagelocation.objects.create(jobid=a, custid=b, conid=bb, joblocation=c, created_at=d)
    context = {
        "form": form,
        "e": e,
    }
    return render(request, 'mha/equipselection1.html', context)


def multiformb(request, bidid=None):
    multiformB.objects.filter(bidid=bidid).delete()
    a = EquipSelection.objects.filter(bidid=bidid).values_list('custid', flat=True)
    b = EquipSelection.objects.filter(bidid=bidid).values_list('jobid', flat=True)
    c = EquipSelection.objects.filter(bidid=bidid).values_list('bidid', flat=True)
    d = EquipSelection.objects.filter(bidid=bidid).values_list('options', flat=True)
    e = Bidding.objects.filter(bidid=bidid).values_list('quanity1', flat=True)
    f = Bidding.objects.filter(bidid=bidid).values_list('jobtype1', flat=True)
    g = Bidding.objects.filter(bidid=bidid).values_list('descript1', flat=True)
    i = Equipment2.objects.filter(modelnum=g).values_list('mfg', flat=True)
    j = Equipment2.objects.filter(modelnum=g).values_list('mfgmodeldescrip', flat=True)
    k = Equipment2.objects.filter(modelnum=g).values_list('eff', flat=True)
    l = Equipment2.objects.filter(modelnum=g).values_list('btu', flat=True)
    m = Contract.objects.filter(bidid=bidid).values_list('totaljobcost', flat=True)
    n = multiformB.objects.create(custid=a, jobid=b, bidid=c, options=d, quanity=e, type=f, mfg=i, modelnum=g,
                                  description=j, eff=k, btu=l, cost=m)
    context = {

        'n': n,

    }
    return render(request, 'mha/contractmulti2.html', context)



def targetnet(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = NetprofitTarget(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'mha/targetnetprofit.html', context)


def changetargetnet(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = NetprofitTarget(request.POST or None, instance=instance)
    a = request.POST['id_targetprofit']
    TargetProfit.objects.filter(bidid=bidid).update(targetprofit_id=a)
    JobCost.objects.filter(bidid=bidid).update(netprofit=a)
    c = JobCost.objects.filter(bidid=bidid).values_list('netjobcost', flat=True).last()
    c1 = JobCost.objects.filter(bidid=bidid).values_list('netprofit', flat=True).last()
    d = c * c1
    e = JobCost.objects.filter(bidid=bidid).update(netprofitcost=d)
    f = JobCost.objects.filter(bidid=bidid).values_list('netprofitcost', flat=True).last()
    g = f + c
    h = JobCost.objects.filter(bidid=bidid).update(netjobcost2=g)
    i = JobCost.objects.filter(bidid=bidid).values_list('OSRcost', flat=True).last()
    j = JobCost.objects.filter(bidid=bidid).values_list('netjobcost2', flat=True).last()
    k = i + j
    l = JobCost.objects.filter(bidid=bidid).update(netjobcost3=g)
    m = JobCost.objects.filter(bidid=bidid).values_list('rebateamouint', flat=True).last()
    n = JobCost.objects.filter(bidid=bidid).values_list('netjobcost3', flat=True).last()
    o = n - m
    p = JobCost.objects.filter(bidid=bidid).update(finaljobcost=o)

    q = CurrentJobInfo.objects.filter(bidid=bidid).update(locationcost=j, loccostafterrebate=o)

    context = {
        "instance": instance,
        "form": form,
        #        "a": a,
        "h": h,
        "e": e,
        "k": k,
        "l": l,
        "p": p,
        "q": q,

    }

    return render(request, 'mha/targetnetprofit.html', context)


#def changetargetnet(request, bidid=None):
#    instance = JobCost.objects.get(bidid=bidid)
#    form = NetprofitTarget(request.POST or None, instance=instance)
#    a = request.POST['id_targetprofit']
#    TargetProfit.objects.filter(bidid=bidid).update(targetprofit_id=a)
#    JobCost.objects.filter(bidid=bidid).update(netprofit=a)
#    context = {
#        "instance": instance,
#        "form": form,
#    }
#    return render(request, 'mha/targetnetprofit.html', context)


def jobcost(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    a = JobCost.objects.filter(bidid=bidid).values_list('conid', flat=True).last()
    b = JobCost.objects.filter(bidid=bidid).values_list('custid', flat=True).last()
    queryset = ContractorInfo.objects.filter(conid=a).all()
    queryset2 = CustomerInfo.objects.filter(custid=b).all()
    queryset3 = Bidding.objects.filter(bidid=bidid).all()
    queryset4 = JobCost.objects.filter(bidid=bidid).all()
    queryset5 = TargetProfit.objects.filter(bidid=bidid).all()

    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "b": b,
        "object_list": queryset,
        "object_list2": queryset2,
        "object_list3": queryset3,
        "object_list4": queryset4,
        "object_list5": queryset5,

    }
    return render(request, 'mha/jobcost.html', context)


def targetnetprofit(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
#    a = TargetProfit.objects.filter(bidid=bidid).values_list('netjobcost', flat=True).last()
#    b = JobCost.objects.filter(bidid=bidid).update(netprofit=a)
    c = JobCost.objects.filter(bidid=bidid).values_list('netjobcost', flat=True).last()
    c1 = JobCost.objects.filter(bidid=bidid).values_list('netprofit', flat=True).last()
    d = c * c1
    e =  JobCost.objects.filter(bidid=bidid).update(netprofitcost=d)
    f = JobCost.objects.filter(bidid=bidid).values_list('netprofitcost', flat=True).last()
    g = f + c
    h = JobCost.objects.filter(bidid=bidid).update(netjobcost2=g)
    i = JobCost.objects.filter(bidid=bidid).values_list('OSRcost', flat=True).last()
    j = JobCost.objects.filter(bidid=bidid).values_list('netjobcost2', flat=True).last()
    k = i + j
    l = JobCost.objects.filter(bidid=bidid).update(netjobcost3=g)
    m = JobCost.objects.filter(bidid=bidid).values_list('rebateamouint', flat=True).last()
    n = JobCost.objects.filter(bidid=bidid).values_list('netjobcost3', flat=True).last()
    o = n - m
    p = JobCost.objects.filter(bidid=bidid).update(finaljobcost=o)


    context = {
        "instance": instance,
        "form": form,
#        "a": a,
#        "b": b,
        "e": e,
        "k": k,
        "l": l,
        "p": p,

    }
    return render(request, 'mha/jobcost.html', context)


#def targetnetprofit(request, bidid=None):
#    instance = JobCost.objects.get(bidid=bidid)
#    form = Costjob(request.POST or None, instance=instance)
#    a = request.POST['id_netprofit']
#    b = JobCost.objects.filter(bidid=bidid).update(netprofit=a)
#    c = JobCost.objects.filter(bidid=bidid).values_list('netjobcost', flat=True).last()
#    c1 = JobCost.objects.filter(bidid=bidid).values_list('netprofit', flat=True).last()
#    d = c * c1
#    e =  JobCost.objects.filter(bidid=bidid).update(netprofitcost=d)
#    f = JobCost.objects.filter(bidid=bidid).values_list('netprofitcost', flat=True).last()
#    g = f + c
#    h = JobCost.objects.filter(bidid=bidid).update(netjobcost2=g)
#    i = JobCost.objects.filter(bidid=bidid).values_list('OSRcost', flat=True).last()
#    j = JobCost.objects.filter(bidid=bidid).values_list('netjobcost2', flat=True).last()
#    k = i + j
#    l = JobCost.objects.filter(bidid=bidid).update(netjobcost3=g)
#    m = JobCost.objects.filter(bidid=bidid).values_list('rebateamouint', flat=True).last()
#    n = JobCost.objects.filter(bidid=bidid).values_list('netjobcost3', flat=True).last()
#    o = n - m
#    p = JobCost.objects.filter(bidid=bidid).update(finaljobcost=o)
#
#
#    context = {
#        "instance": instance,
#        "form": form,
#        "a": a,
#        "b": b,
#        "e": e,
#        "k": k,
#        "l": l,
#        "p": p,
#
#    }
#    return render(request, 'mha/jobcost.html', context)


def netprofit(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    a = JobCost.objects.values_list('netprofit', flat=True).last()
    b = JobCost.objects.values_list('netjobcost', flat=True).last()
    c = b * a
    d = JobCost.objects.filter(bidid=bidid).update(netprofitcost=c)
    context = {
        "instance": instance,
        "form": form,
        "d": d,

    }
    return render(request, 'mha/jobcost.html', context)


def load_profit(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    netprofit = JobCost.objects.values('netprofit').get(bidid=bidid)
    context = {
        "instance": instance,
        "form": form,
        "netprofit": netprofit,

    }
    return render(request, 'mha/netprofit_1.html', context)


def load_netprofit(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    netprofitcost = JobCost.objects.values('netprofitcost').get(bidid=bidid)
    context = {
        "instance": instance,
        "form": form,
        "netprofitcost": netprofitcost,

    }
    return render(request, 'mha/netprofitcost_1.html', context)


def load_costplusprofit(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    netjobcost2 = JobCost.objects.values('netjobcost2').get(bidid=bidid)
    context = {
        "instance": instance,
        "form": form,
        "netjobcost2": netjobcost2,

    }
    return render(request, 'mha/costplusprofit_1.html', context)


def load_totalsubcost(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    netjobcost3 = JobCost.objects.values('netjobcost3').get(bidid=bidid)
    context = {
        "instance": instance,
        "form": form,
        "netjobcost3": netjobcost3,

    }
    return render(request, 'mha/totalsubcost_1.html', context)


def load_finaljobcost(request, bidid=None):
    instance = JobCost.objects.get(bidid=bidid)
    form = Costjob(request.POST or None, instance=instance)
    finaljobcost = JobCost.objects.values('finaljobcost').get(bidid=bidid)
    context = {
        "instance": instance,
        "form": form,
        "finaljobcost": finaljobcost,

    }
    return render(request, 'mha/finaljobcost_1.html', context)


def deposit(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_balance']
    Contract.objects.filter(bidid=bidid).update(deposit=a)
    b = Contract.objects.filter(bidid=bidid).values_list('deposit', flat=True).last()
    c = Contract.objects.filter(bidid=bidid).values_list('grandtotalcost', flat=True).last()
    d = c - b
    e = Contract.objects.filter(bidid=bidid).update(finalpayment=d)
    context = {
        "instance": instance,
        "form": form,
        'e': e,

    }
    return render(request, 'mha/contract.html', context)



def load_finalpayment(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    finalpayment = Contract.objects.filter(bidid=bidid).values_list('finalpayment', flat=True).last()

    context = {
        "instance": instance,
        "finalpayment": finalpayment,
        "form": form,
    }
    return render(request, 'mha/finalpayment_1.html', context)


def load_deposit(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    deposit = Contract.objects.filter(bidid=bidid).values_list('deposit', flat=True).last()

    context = {
        "instance": instance,
        "deposit": deposit,
        "form": form,
    }
    return render(request, 'mha/deposit_1.html', context)


def depositterms(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_depositterms']
    Contract.objects.filter(bidid=bidid).update(depositterms=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)



def deposittermsa(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_deposittermsa']
    b = Terms.objects.values_list('id', flat=True).last()
    c = b+1
    Terms.objects.create(id=c, term=a)
    Contract.objects.filter(bidid=bidid).update(depositterms=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_deposittermsa(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    depositterms = Contract.objects.values('depositterms').get(bidid=bidid)
    context = {
        "instance": instance,
        "depositterms": depositterms,
        "form": form,
    }
    return render(request, 'mha/deposittermsa_1.html', context)


def finalterms(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_finalterms']
    Contract.objects.filter(bidid=bidid).update(finalterms=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)



def finaltermsa(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_finaltermsa']
    b = Terms.objects.values_list('id', flat=True).last()
    c = b+1
    Terms.objects.create(id=c, term=a)
    Contract.objects.filter(bidid=bidid).update(finalterms=c)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def load_finaltermsa(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    finalterms = Contract.objects.values('finalterms').get(bidid=bidid)
    context = {
        "instance": instance,
        "finalterms": finalterms,
        "form": form,
    }
    return render(request, 'mha/finaltermsa_1.html', context)


def depositdate(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_downpaymentdate']
    Contract.objects.filter(bidid=bidid).update(downpaymentdate=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)


def finalpaymentdate(request, bidid=None):
    instance = Contract.objects.get(bidid=bidid)
    form = ContractForm(request.POST or None, instance=instance)
    a = request.POST['id_finalpaymentdate']
    Contract.objects.filter(bidid=bidid).update(finalpaymentdate=a)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'mha/contract.html', context)