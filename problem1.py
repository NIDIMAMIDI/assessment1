"""
Question 1 - 

Description - 

Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00
Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00
"""


                #code
try:                                 
    book1_nos = int(input("Enter the number of books of book1 type : "))
    book2_nos = int(input("Enter the number of books of book2 type : "))
    book3_nos = int(input("Enter the number of books of book3 type : "))
except ValueError as err:
    print("PLEASE, ENTER ONLY INTEGERS")
cost_of_book1 = 499.00
cost_of_book2 = 855.00
cost_of_book3 = 645.00
gst = 0.12
delivary_charges = 250.00
total = (book1_nos*cost_of_book1)+(book2_nos*cost_of_book2)+(book3_nos*cost_of_book3)
gst_amount = total * gst
total_invoice = total + gst_amount + delivary_charges
print("Total Invoice Amount is : ", total_invoice)


"""
            OUTPUT
TESTCASE-1:

Enter the number of books of book1 type : 4
Enter the number of books of book2 type : 5
Enter the number of books of book3 type : 6
Total Invoice Amount is :  11607.92

TESTCASE-2:

Enter the number of books of book1 type : 80
Enter the number of books of book2 type : 43
Enter the number of books of book3 type : 13
Total Invoice Amount is :  95528.4
"""

