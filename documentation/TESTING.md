# W3C Validation

To validate every page of the project, that there were no syntax errors, these two Validators were used, W3C Validator and W3C CSS Validator.
To make make it easier to validate html code, since using jinja templating language throughout all pages, which results in errors in online validators. I used URL address.
For W3C Css Validator I copied css code directly.

* [W3C Validator](project_files/validators/w3c.jpg "W3C Validator")
* [W3C CSS Validator](project_files/validators/W3c_css.pdf "W3C CSS Validator")

# Jshint Validation

For this project I used jQuery - JavaScript Library for MaterializeCSS initialization: "Write less, do more."
Jshint were used to validate jQuery file of this project. [Click](project_files/validators/jshint.jpg) to view report.

# PEP8 Validation

Python code checked for PEP8 requirements. [Click](project_files/validators/pep8.jpg) to view report.

# User stories testing
   
1. As a user to this website, I want to view a list of products, so that I can select some to purchase.

The Navigation bar is implemented into the website, so that any user is able to find list of products quick and easy navigating through th website.

This Navigation bar is implemented on the desktop and laptop view:

![Crystal Energy](user_stories/u11111.jpg "Crystal Energy")
![Crystal Energy](user_stories/u11.jpg "Crystal Energy")
![Crystal Energy](user_stories/u1.jpg "Crystal Energy")
![Crystal Energy](user_stories/u111.jpg "Crystal Energy")

This Navigation bar is implemented on tablet and mobile view:

![Crystal Energy](user_stories/u111111.jpg "Crystal Energy")
![Crystal Energy](user_stories/u1111.jpg "Crystal Energy")

2. As a user to this website, I want to view individual product details, so that I can identify the price, description, product rating, product image and available sizes (if applicable).



3. As a user to this website, I want to easily view the total of my purchases at any time, so that I can avoid spending too much.



4. As a user to this website, I want to easily register for an account, so that I can have a personal account and be able to view my profile.



5. As a user to this website, I want to easily login or logout, so that I can access my personal account information.



6. As a user to this website, I want to receive an email confirmation after registering, so that I can verify that my account registration was successful.



7. As a user to this website, I want to have a personalized user profile, so that I can view my personal order history and order confirmations, and save my payment information.



8. As a user to this website, I want to sort the list of available products, so that I can easily identify the best rated, best price and categorically sorted products.



9. As a user to this website, I want to sort a specific category of product, so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.



10. As a user to this website, I want to search for a product by name or description, so that I can find a specific product I’d like to purchase.



11. As a user to this website, I want to add product into wishlist, so that I can look at it later and decide if I want to purchase or remove it from wishlist.



12. As a user to this website, I want to add review on product, so that I can show others my experience with product.



13. As a user to this website, I want to easily select quantity and size (if applicable) of a product when purchasing it, so that I can ensure I don’t accidentally select the wrong product, quantity or size.



14. As a user to this website, I want to view items in my bag to be purchased, so that I can identify the total cost of my purchase and all items I will receive.



15. As a user to this website, I want to adjust the quantity of individual items in my bag, so that I can easily make changes to my purchase before checkout.



16. As a user to this website, I want to easily enter my payment information, so that I can checkout quickly.



17. As a user to this website, I want to view an order confirmation after checkout, so that I can verify that I haven’t made any mistakes.



18. As a user to this website, I want to receive an email confirmation after checking out, so that I can keep the confirmation of what I’ve purchased for my records.



19. As an admin to this website, I want to add a product, so that I can add new products to my store.



20. As an admin to this website, I want to edit/update a product, so that I can change product prices, descriptions, images, and other product criteria.



21. As an admin to this website, I want to delete a product, so that I can remove products that are no longer available.


# Functional testing

Throughout the website every link, field and icon was tested and all results are displayed on the table below:

| Location | Type | Expected Result | Actual Result | Pass/Fail/Not executed|
| :----: | :----: | :----: | :----: | :----: |
| Navbar | *Home* link | Click on *Home* link navigates to Home page | Navigates to Home page | Pass |
| Navbar | *All Products* link | Click on *All Products* link opens nav dropdown | Opens nav dropdown | Pass |
| Navbar | Crystal Energy Logo | Click on Crystal Energy Logo navigates to Home page | Navigates to Home page | Pass |
| Navbar | *Crystals* link | Click on *Crystals* link opens nav dropdown | Opens nav dropdown | Pass |
| Navbar | *Gifts* link | Click on *Gifts* link opens nav dropdown | Opens nav dropdown | Pass |
| Navbar | *Reviews* link | Click on *Reviews* link navigates to Reviews page | Navigates to Reviews page | Pass |
| Navbar | *By Price* dropdown link | Click on *By Price* dropdown link navigates to Products page with products sorted by price | Navigates to Products page with products sorted by price | Pass |
| Navbar | *By Rating* dropdown link | Click on *By Rating* dropdown link navigates to Products page with products sorted by rating | Navigates to Products page with products sorted by rating | Pass |
| Navbar | *By Category* dropdown link | Click on *By Category* dropdown link navigates to Products page with products sorted by category | Navigates to Products page with products sorted by category | Pass |
| Navbar | *All Products* dropdown link | Click on *All Products* dropdown link navigates to Products page | Navigates to Products page | Pass |
| Navbar | *Angel Healing Crystals* dropdown link | Click on *Angel Healing Crystals* dropdown link navigates to Angel Healing Crystals products | Navigates to Angel Healing Crystals products | Pass |
| Navbar | *Chakra Healing Crystals* dropdown link | Click on *Chakra Healing Crystals* dropdown link navigates to Chakra Healing Crystals products | Navigates to Chakra Healing Crystals products | Pass |
| Navbar | *Best Healing Crystals* dropdown link | Click on *Best Healing Crystals* dropdown link navigates to Best Healing Crystals products | Navigates to Best Healing Crystals products | Pass |
| Navbar | *All Crystals* dropdown link | Click on *All Crystals* dropdown link navigates to All Healing Crystals products | Navigates to All Healing Crystals products | Pass |
| Navbar | *Home* dropdown link | Click on *Home* dropdown link navigates to products categorized for home | Navigates to products categorized for home | Pass |
| Navbar | *Women* dropdown link | Click on *Women* dropdown link navigates to products categorized for women | Navigates to products categorized for women | Pass |
| Navbar | *Men* dropdown link | Click on *Men* dropdown link navigates to products categorized for men | Navigates to products categorized for men | Pass |
| Navbar | *Shop Now* button | Click on *Shop Now* button navigates to Product page | Navigates to Product page | Pass |
| Navbar | *Log In* link | Click on *Log In* link navigates to Log In page | Navigates to Log In page | Pass |
| Navbar | *Register* link | Click on *Register* link navigates to Register page | Navigates to Register page | Pass |
| Navbar | *Profile* link | Click on *Profile* link navigates to Profile page | Navigates to Profile page | Pass |
| Navbar | *Log Out* link | Click on *Log Out* link navigates to Log In page | Navigates to Log In page | Pass |
| Navbar | Search form input field | Search form input field allows to type a text | Allows to type a text | Pass |
| Navbar | Search form *Search* button | Search form *Search* button search for text from input field throughout products and display matching product | Search for text from input field throughout all products and display matching product | Pass |
| Navbar | "Wishlist" icon | Click on *Wishlist* icon navigates to Wishlist page | Navigates to Wishlist page | Pass |
| Navbar | "My Account" icon | Click on *My Account* opens dropdown nav | Opens dropdown nav | Pass |
| Navbar | "Bag" icon | Click on *Bag* icon navigates to Shopping bag page | Navigates to Shopping bag page | Pass |
| Product page | Product image | Click on Product image navigates to Product details page | Navigates to Product details page | Pass |
| Product page | *Heart* icon | Click on *Heart* icon adds product to Wishlist page | Adds product to Wishlist page | Pass |
| Product page | *Edit* link | Click on *Edit* link navigates to Product Management page (only for admin) | Navigates to Product Management page (only for admin) | Pass |
| Product page | *Remove* link | Click on *Remove* link delete product (only for admin) | Delete product (only for admin) | Pass |
| Reviews page | *Add Review* button | Click on *Add Review* button navigates to Add Review page (only for admin and registered user) | Navigates to Add Review page (only for admin and registered user) | Pass |
| Reviews page | *Remove* button | Click on *Remove* button delete review (only for admin and registered user) | Delete review (only for admin and registered user) | Pass |
| Wishlist page | *Add to Bag* button | Click on *Add to Bag* navigates to Product detail page (only for admin and registered user) | Navigates to product detail page (only for admin and registered user) | Pass |
| Wishlist page | *Remove* button | Click on *Remove* button delete product from Wishlist (only for admin and registered user) | Delete product from Wishlist (only for admin and registered user) | Pass |
| Wishlist page | *Keep Shopping* button | Click on *Keep Shopping* button navigates to Product page | Navigates to Product page | Pass |
| Shopping bag page | *Secure Checkout* button | Click on *Secure Checkout* button navigates to Checkout page page | Navigates to Checkout page | Pass |
| Login page | Login form username input field | Log In form username input field allows to type and validate a username | Allows to type and validate a username | Pass |
| Login page | Login form password input field | Log In form password input field allows to type and validate a password | Allows to type and validate a password | Pass |
| Login page | Login form *Log In* button | Log In form *Log In* button verify username, password and redirect to user profile page | Verify username, password and redirect to user profile page | Pass |
| Login page | Login form *Register Account* link | Log In form *Register Account* link navigates user to Register page | Navigates user to Register page | Pass |
| Register page | Register form email input field | Register form email input field allows to validate a email | Allows to validate a email | Pass |
| Register page | Register form username input field | Register form username input field allows to create and validate a username | Allows to create and validate a username | Pass |
| Register page | Register form *Log In* link | Register form *Log In* link navigates user to Log In page | Navigates user to Log In page | Pass |
| Footer | *GitHub* icon | Click on *GitHub* icon navigates to [GitHub repository](https://github.com/Sandra-Be/crystal_energy_alfa) | Navigates to [GitHub repository](https://github.com/Sandra-Be/crystal_energy_alfa) | Pass |

Back to [MAIN](README.md/#Testing) file.