#***(1)Returns all customers from customer table
from Staff import models
from appoinment.models import Booking
from home.models import register

customers = register.objects.all()

#(2)Returns first customer in table
firstCustomer = register.objects.first()

#(3)Returns last customer in table
lastCustomer = register.objects.last()

#(4)Returns single customer by name
customerByName = register.objects.get(name='Vini')

#***(5)Returns single customer by name
customerById = register.objects.get(id=1)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.Booking_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = Booking.objects.first()
parentName = Booking.customer.name


'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
  
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.Booking_set.filter(service__name="Hair Cut").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()
