# 1. Identify person who has subscriber and visitor
# 2.Indentify My subscriber and visitor to get the total impresion for the day
# 3. Identify those member who are not my subscriber but they visited my shop
# 4 Identify members who are either subscriber or visitors but not both
visitor_list=set(["Divya","Rohan","Anushree"])
subscriber=set(["Divya","Mahak","Priya","Rohan"])
print("Common People Visitors and subscriber:",visitor_list  & subscriber)
print("Total name of  Subscriber:",visitor_list | subscriber)
print("Total name of visitor:",visitor_list- subscriber)
print("Total name of visitor/subscriber but not both:",visitor_list ^  subscriber)

