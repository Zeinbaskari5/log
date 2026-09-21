with open ("logs.txt","r") as file:
    logs=[]
    for line in file:
        parts=line.split()
        details={}
        for item in parts[5:]:
            k,v =item.split("=")
            details[k]=v
        log={
            "date":parts[0],
            "time":parts[1],
            "event":parts[2],
            "username":parts[3],
            "status":parts[4],
            "details":details
        }
        logs.append(log)
    login={}
    logout={}
    buy={}
    buy_count={}
    buy_price={}
    first_login_time={}
    first_login_date={}
    last_login_time={}
    last_login_date={}
    Sold_products={}
    error_count={}
    Total_revenue_product={}
    for i in logs:
        username=i["username"]

        if username not in login:
            login[username]=0
        if i["event"]=="LOGIN":
            login[username]+=1
            if username not in first_login_time and username not in first_login_date:
                first_login_time[username]=i["time"]
                first_login_date[username]=i["date"]

            last_login_time[username]=i["time"]
            last_login_date[username]=i["date"]

        if username not in logout:
            logout[username]=0
        if i["event"]=="LOGOUT":
            logout[username]+=1 
            
        if username not in buy:
            buy[username]=0
        if i["event"]=="BUY":
            product=i["details"]["PRODUCT"]
            buy[username]+=1
            if username not in buy_count:
                buy_count[username]=0
            buy_count[username]+=int(i["details"]["COUNT"])
            if  username not in  buy_price:
                buy_price[username]=0
            buy_price[username]+=int(i["details"]["PRICE"])
            if product not in Sold_products:
                Sold_products[product]=0
            Sold_products[product]+=int(i["details"]["COUNT"])
            if product not in Total_revenue_product:
                Total_revenue_product[product]=0
            Total_revenue_product[product]+=int(i["details"]["PRICE"])
        if i["event"]=="ERROR":
            error=i["details"]["ERROR_CODE"]
            if error not in error_count:
                error_count[error]=0
            error_count[error]+=1
    Best_selling_product=0
    name_Best_selling_product=""
    name_Lowest_selling_product=""
    first=True
    for j in Sold_products:
        if first== True:
            Lowest_selling_product=Sold_products[j]
            name_Lowest_selling_product=j
            first=False
        if Sold_products[j] >Best_selling_product:
            Best_selling_product=Sold_products[j]
            name_Best_selling_product=j
        if Sold_products[j]<Lowest_selling_product:
            Lowest_selling_product=Sold_products[j]
            name_Lowest_selling_product=j
    
    print("_________User Reports__________")        
    print("login count:",login)
    print("\n")
    print("logout count:",logout)
    print("\n")
    print("buy count:",buy)
    print("\n")
    print("Number of products purchased:",buy_count)
    print("\n")
    print("total price:", buy_price)
    print("\n")
    print("first login date",first_login_date)
    print("\n")
    print("first login time:",first_login_time)
    print("\n")
    print("last login date:",last_login_date)
    print("\n")
    print("last login time:",last_login_time)
    print("_________Product Analysis__________") 
    print("Best selling product:",name_Best_selling_product)
    print("Lowest_selling_product:",name_Lowest_selling_product)
    print("Sold products:",Sold_products)
    print("Total revenue product:",Total_revenue_product)
    print("_________Error Analysis__________") 
    for i in error_count:
        print("ERROR",i)
        print(error_count[i],"Times")
        print("____________")
   
   