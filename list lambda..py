l=[1,2,3,4,5] 
output=dict(map(lambda x:(x,x*2),l))
print(output)
##
l=[1,2,3,4,5]
output={i:i*2 for i in l}
print(output)
##
prices=[15,25,10,30,50]
price_below_20=[price for price in prices if price<20]
print(price_below_20)
##
customers=['Rahul','Antony','Salaman','Arun','kiran']
customer_startwith_A=[customer for customer in customers if customer.startswith('A')]
print(customer_startwith_A)
##
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
categorized_employees={name:'high' if salary>50000 else 'low' for name,salary in employees.items()} 
print(categorized_employees)
###
words=['apple','banana','apple','orange','banana','apple']
word_count={word:words.count(word) for word in set(words)}    
print(word_count)

