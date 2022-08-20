'''list_1=['mango','apple',]
for ind ,ele in enumerate(list_1):
    print(ind)




car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)




fruits={"name":"gowthami","age":27,"place":"hyderabad"}
fruits.pop("place")
print(fruits)        

fruits={"name":"gowthami","age":27,"place":"hyderabad"}
print(len(fruits))

fruits={"name":"gowthami","age":27,"place":"hyderabad"}
fruits.update({"mango":"sweet"})
print(fruits)


dict_1={"name":"gowthami","age":27,"place":"hyderabad"}
dict_2={"name":"gowthami","age":27}
print cmp((dict_1,dict_2))



a={"name","gowthami","age",27,"place","hyderabad"}
b={"name","gowthami","age",27}
c=a-b
print(c)



###
s1="green"
s2="yellow"
s3="red"
light=input("enter current status of light:")
lst=['green','yellow','red']
for i in lst:
    if i=='red':
        print("The changed light is :",lst[0])
    elif light==i:
        t=lst.index(i)+1
        print("The changed light is :",lst[t])
        break'''


###You're writing code to control your town's traffic lights.
You need a function to handle each change from green, to yellow, to red, and then to green again.



Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.



For example, when the input is green, output should be yellow.



Test Case 1
Input
Green
Output
Yellow



Test Case 2
Input
Red
Output
Green


##
color=input("enter the traffic signal light color:")
lst_1=['green','yellow','red']
for i in lst_1:
    if i=='red':
        print("the color of light to:",lst_1[0])
    elif color==i:
        s=lst_1.index(i)+1
        print("the color of light to:",lst_1[s])
        break



##output:
enter the traffic signal light color:green
the color of light to: yellow

================ RESTART: C:/Users/gk22204/Desktop/enumarate.py ================
enter the traffic signal light color:red
the color of light to: green


































