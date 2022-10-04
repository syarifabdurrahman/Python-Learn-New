users=[
{
    'id':1,
    'name': "Leanne Graham",
    'username': "Bret",
    'email': "Sincere@april.biz",
     'address':
    {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": 
        {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
},
{
    
    'id':2,
    'name': "Leanne Gruhum",
    'username': "Bret",
    'email': "Sincere@april.biz",
}
]

print(users[0]["address"]["street"])
print(type(users[0]))
print("\nUbah dict ke json")
import json

result = json.dumps(users[0])
print(type(result))
print(result)


with open('result.json','w') as file:
     json.dump(users[0],file)
