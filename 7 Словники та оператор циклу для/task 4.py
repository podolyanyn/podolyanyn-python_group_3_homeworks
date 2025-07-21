
weak = ['Monday' , 'Tuesday' , 'Wednesday' ,'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
a_dict=dict()
reverse_dict=dict()
for n , d in enumerate(weak):

    a_dict.update({n : d})
    reverse_dict.update({d : n})
print(a_dict)
print(reverse_dict)

