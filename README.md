# 28-11-2023-python-django-views-templates
Certainly! Here's an exercise for working with Django models, views, and templates:

### Exercise: Django Models, Views, and Templates

#### Task 1: Create Models
1. Create a Django app called "myshop" Inside the app, define two models: `Category` and `Product`. `Category` should have fields like `name` and `description`, and `Product` should have fields like `name`, `price`,`available` and a foreign key to `Category`.
2. Use the `fakedataloader` to generate the data

#### Task 2: Views
1. Create a view that displays a list of all categories.
2. Create a view that displays details of a specific category, including the products associated with that category.
3. Create a view that shows a list of all products.
4. Create a view that shows a specefic product

#### Task 3: Templates
1. Create a template for displaying the list of categories. Iterate through the categories and display their names and descriptions.
2. Create a template for displaying the details of a category. Show the category name, description, and a list of associated products.
3. Create a template for displaying the list of products. Display the product name and price.


#### Task 4: Extended Templates
1. Create a base template that includes common HTML structure like the header and footer.
2. Extend the base template in the templates created in Task 3 to inherit the common structure.

#### Task 5: If Statement in Template
1. In one of the templates (either category details or product list), use an if statement to check if there are any items to display. If there are, display them; otherwise, show a message like "No items available."
2. In the template of the product details if it is available and if not just display "Sorry this product is not available"
#### Task 6: Add CSS styling
1. Add some css styling of your choice
### Note:
- Make sure to set up the URLs to connect your views.
- You can use Django's built-in views like `ListView` and `DetailView` for some tasks.

