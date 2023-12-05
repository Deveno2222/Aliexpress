## Aliexpress
* Clone the repository: git clone https://github.com/Deveno2222/Aliexpress.git
* Install the dependencies: pipenv install
* pipenv shell
* python manage.py migrate
* Start the development server: python manage.py runserver
  
# Registration

# Admin panel
* python manage.py createsuperuser

# Create Account
* Username
* Email
* Password
* Repeat password

# Create category
Firstly, you need to create *category* of product. 
*Only admin can create category of product*

# Create product
* Category of product (Choose) (Necessary)
* Name of product (Necessary)
* Description of product
* Price of product (Necessary)
* Image of product (Necessary)

# Main page
On main page you can see all products and all categories of products.

# Dashboard 
Dashboard contains all products that you created.

# Product page
On this page you can see image, name, price, description, reviews, recomendation of products.

*Reviews*
Any user can leave comments.
The date is specified automatically.

*Recomendations*
Here are products that have the same category

*Edit*
If you're created that product, you can edit this product. (*Edit* - button)

*Delete*
If you're created that product, you can delete this product. (*Delete* - button)
