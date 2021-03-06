## Project MyShop

### 1| Setup & Templates
#### Part 1| Configure App
- Install Django
- Start Project
- Create App
- Add app to settings.py
#### Part 2| Templates
- Create Templates Folder
- Create Templates: base.html, index.html, cart.html, checkout.html
#### Part 3| Views & URLs
- Create Views: index, cart, checkout
- URLs
- Base URLs Configuration
#### Part 4| Static Files
- Static Folder
- CSS file
- STATICFILES_DIRES
- Add static files to pages
- Add image
#### Part 5| Base Template
- Add HTML boilerplate to base.html
- Add Viewport & Static
- Add Bootstrap
- Container/Navbar placeholder
- HTML Inheritance
#### Part 6| Navbar
- Bootstrap Navbar
- Dark Theme
- Customize Navbar
- Custom CSS
#### Part 7| index.html
- Layout
- Placeholder Content
#### Part 8| cart.html
- Layout
- Cart Headers
- Cart Rows
#### Part 9| checkout.html
- Layout
- Form
- Payment Option
- Order Summary

### 2| Data Models
#### Part 1| Models
- Import User Model
- Customer Model
- Product, Order, OrderItrm Models
- Shipping Model
- Migrate Database
- admin.py
#### Part 2| Render Products
- Query Products
- Render Products
#### Part 3| Product Image Field
- ImageField()
- MEDIA_ROOT
- MEDIA_URL
- urls.py Configuration
- Render Images
- Image Error Solution
#### Part 4| User Cart
- Add data (Admin Panel)
- Query data (Cart)
- Render data (cart.html)
- Calculate Totals (Model)
- Query Totals (View)
- Render Totals (Template)
- Checkout Page Data

### 3| Site Functionality
#### Part 1| Add to Cart
- cart.js
- Add Event Handler
- Use Type Logic
- updateItem View
- updateUserOrder()
- CSRF Token
- updateItem view logic
- Cart Total
#### Part 2| Update Cart
- Add & Remove Clikes
#### Part 3| Shipping Address
- Shipping Method
- Order Shipping Status
- Hide Shipping Form
- Payment Option
- Trigger Payment Action
#### Part 4| Checkout Form
- Hide Form or Fields
- Form Data
#### Part 5| Process Order
- Process Order View & URL
- Send POST Data
- Transaction ID
- Set Data
- Confirm Total
- Shipping Logic

### 4| Guest Checkout
#### Part 1| Set Cookies
- Create Cart in Cookie
- Adding/Removing Items
#### Part 2| Render Cart Total
- Query Cart in views.py
- Build Cart Total
#### Part 3| Build Order
- Order Total
- Items QuerySet
- Shipping Information
- Product Does Not Exist
#### Part 4| cookieCart()
- utils.py
- Copy Cart Logic
- User cookieCart in views
#### Part 5| cartData()
- Add cartData()
- Move View Logic
- User cartData() in views
#### Part 6| Checkout
- Clear Cart
- Guest Checkout Logic
- Create Guest Checkout Function
- Clean Up processOrder View

### 5| Payment Integration
#### Part 1| Payment Buttons
#### Part 2| Sandbox Account
#### Part 3| Making Payments