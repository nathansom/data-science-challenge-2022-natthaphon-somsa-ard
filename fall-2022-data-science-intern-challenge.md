# Fall 2022 Data Science Intern Challenge

## Question 1

Please refer to the program [question1.py](/question1.py)

### a.	Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.

The cause of calculation error is the inclusion of outliers in the dataset that causes the AOV, or the mean value of order amount, to be highly skewed to the right. The first step a data scientist should take when analyzing data is to clean up the data. In this question, the skewness of the data should be calculated and the maximum value, as well as 25%, and 75% percentiles, should be identified. 
At the first glance, it may be tempting to filter out the orders with the maximum order amount value. However, the resulting “cleaned” data set could still be rightly skewed. Cleaning up the data by repeatedly filtering out the maximum and re-checking the skewness can become very inefficient. Hence, the Interquartile Range (IQR) method should be used instead to eliminate the outliers. The IQR value is simply the third quantile (75% percentile), Q3, minuses the first quantile (25% percentile), Q1. The values outside the range of  (Q1 – 1.5 x IQR, Q3 + 1.5 x IQR) are suspected to be outliers, which should be filtered accordingly before calculating the mean value to determine the AOV.

### b.	What metric would you report for this dataset?

As the goal of this analysis is to find the AOV of sneaker shops, the order amount would be the most appropriate metric and the mean of order amount values for filtered orders should be reported for AOV.

### c.	What is its value?

The AOV (mean value of order amount) is $293.72.

## Question 2

### a. How many orders were shipped by Speedy Express in total?**

`SELECT Count(Orders.OrderID) 
FROM Orders
INNER JOIN Shippers
ON Orders.ShipperID = Shippers.ShipperID
WHERE ShipperName="Speedy Express";`

**Answer: 54**

### b. What is the last name of the employee with the most orders?

`SELECT LastName
FROM Employees
WHERE EmployeeID = (SELECT EmployeeID
 FROM Orders
 GROUP BY EmployeeID
 ORDER BY
 COUNT(EmployeeID) DESC
 LIMIT(1));`

 **Answer: Peacock**

 ### c. What product was ordered the most by customers in Germany?

 **Step 1: Filter the orders for customers based in Germany and calculate the frequency of ProductID**

`SELECT Orders.OrderID, OrderDetails.ProductID, Customers.Country, COUNT(OrderDetails.ProductID)AS Frequency
FROM Orders
INNER JOIN Customers, OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
WHERE Country="Germany"
GROUP BY ProductID
ORDER BY
COUNT(ProductID) DESC;`

**Step 2: Select the product ID(s) with highest frequency**
`SELECT ProductID
FROM (SELECT Orders.OrderID, OrderDetails.ProductID, Customers.Country
FROM Orders
INNER JOIN Customers, OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
WHERE Country="Germany"
GROUP BY ProductID
ORDER BY
COUNT(ProductID) DESC
LIMIT(3));`

**Step 4 (Complete SQL Query): Get the product name for the most frqequently ordered product ID(s)**

 `SELECT ProductName
FROM Products
WHERE ProductID IN (
SELECT ProductID
FROM (SELECT Orders.OrderID, OrderDetails.ProductID, Customers.Country
FROM Orders
INNER JOIN Customers, OrderDetails
ON Orders.OrderID = OrderDetails.OrderID
WHERE Country="Germany"
GROUP BY ProductID
ORDER BY
COUNT(ProductID) DESC
LIMIT(1)));`

 **Answer: Mozzarella di Giovanni (also tied with Raclette Courdavault and Gorgonzola Telino)**

