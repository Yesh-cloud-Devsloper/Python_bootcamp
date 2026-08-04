**INSTANCE VARIABLE**

**====================**

**-->If the value of variable is varied from object to object then such type of variables are called instance variable.**

**-->For every object a separate copy of instance variable will be created.**



**-->where we can Declare instance variable?**

**===========================================**

* **Inside Constructor by using 'self' variable. (def \_\_init\_\_(self,parameter)**

**def \_\_init\_\_(self,rn,name,dept,number)**

&#x09;**self.rn**

&#x09;**self.name**

&#x09;**self.dept**

&#x09;**self.number**

* 
* **Inside instance method by using self variable.**

**def display(self):**

&#x09;**self.rn=rn**

&#x09;**self.name=name**

&#x09;**print('Instance Method')**

* 
* **Out side of the class by using object reference variable**

**s=Student(101','amir','mech','5656892141')**





**Example:-**

**class Student:**

&#x20; **def \_\_init\_\_(self,rn,name,dept,number)**

&#x09;**self.rn**

&#x09;**self.name**

&#x09;**self.dept**

&#x09;**self.number**

&#x20; **def display(self):**

&#x09;**print('Instance Method')**



**s=Student(101','amir','mech','5656892141')**

**s1=Student(102','aman','mech','5656892142')**

**s2=Student(103','alok','mech','5656892143')**

**s3=Student(104','asish','mech','5656892144')**



**Inside instance method by using self variable.**



**HOW TO ACCESS INSTANCE VARIABLE**

**================================**

**WE CAN ACCESS INSTANCE VARIABLES WIHTIN THE CLASS BY USING SELF VARIABLE AND OUTSIDE OF THE CLASS BY USING OBJECT REFERENCE.**





**How to delete instance variable from the object**

**===============================================**

**syntax-**

**----------**

&#x09;**(del self.variable\_Name)**

**With in a class we can delete instance variable using 'del' keyword.**

**-->from out side of the class we can delete instance variable.**

&#x09;**sYNTAX**

**---------------------**

&#x09;**(del  object\_Reference.variable)**



















