from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Position, Sale
from .forms import SalesSearchForm
from reports.forms import ReportForm
import pandas as pd
from .utils import get_chart,get_customer_from_id,get_salesman_from_id

# Create your views here.

def home_view(request):
    search_form = SalesSearchForm(request.POST or None)
    report_form = ReportForm()
    sale_df = None
    position_df = None
    merged_df = None
    df = None
    chart = None
    no_data = None

    if request.method == "POST":
        date_from = request.POST.get("date_from")
        date_to = request.POST.get("date_to")
        chart_type = request.POST.get("chart_type")
        result_by = request.POST.get("results_by")

        # qs = Sale.objects.all()
         #obj = Sale.objects.get(id = 1)
       
        qs = Sale.objects.filter(created__date__lte = date_to,created__date__gte = date_from)
        if len(qs)>0:           
            sale_df = pd.DataFrame(qs.values())
            sale_df["customer_id"]= sale_df["customer_id"].apply(get_customer_from_id)
            sale_df["salesman_id"] = sale_df["salesman_id"].apply(get_salesman_from_id)
            
            sale_df["created"]= sale_df["created"].apply(lambda x:x.strftime('%Y-%m-%d'))
            sale_df["updated"] = sale_df["updated"].apply(lambda x:x.strftime("%Y-%m-%d"))
           
            
            sale_df.rename({"customer_id":"customer","salesman_id":"salesman","id":"sales_id"},axis=1,inplace=True)
            
            #sale_df["sales_id_1"]=sale_df["sales_id"]

            position_data = []
            for sale in qs:
                for pos in sale.get_positions():
                    obj = {
                        "position_id":pos.id,
                        "product":pos.product.name,
                        "quantity":pos.quantity,
                        "price":pos.price,
                        "sales_id":pos.get_sales_id()
                    }
                    position_data.append(obj)
        
            position_df = pd.DataFrame(position_data)

            merged_df = pd.merge(sale_df,position_df,on="sales_id")

            df = merged_df.groupby("transaction_id", as_index=False)["price"].agg("sum")

            chart = get_chart(chart_type,sale_df,result_by)
            #chart = get_chart(chart_type,df,labels=df["transaction_id"].values)

            sale_df = sale_df.to_html()
            position_df = position_df.to_html()
            merged_df = merged_df.to_html()
            df = df.to_html()
        else:
            print("no data")
            no_data = "No Data is available in these selected days."

    

    context = {
        "search_form":search_form,
        "report_form":report_form,
        "sale_df":sale_df,
        "position_df":position_df,
        "merged_df":merged_df,
        "df":df,
        "chart":chart,
        "no_data":no_data
    }
    return render(request,"sales/home.html",context)




class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html"
    #context_object_name = "sales_list"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"


def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request,"sales/main.html",{"qs":qs})


def sale_detail_view(request,**kwargs):
    pk = kwargs.get("pk")
    obj = Sale.objects.get(pk = pk)

    return render(request,"sales/detail.html",{"object":obj})





