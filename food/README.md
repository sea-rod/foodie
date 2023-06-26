# 👋Introduction
Welcome to Foodie, your ultimate destination for online food ordering! Our Django-powered application makes it easy for customers to satisfy their cravings and enjoy a delightful dining experience.

With Foodie, you can explore a diverse menu featuring a wide range of mouthwatering cuisines. From appetizing starters to delectable main courses and tempting desserts, we have something to please every palate. Simply browse through our food categories, select your favorites, and add them to your cart.

Our user-friendly cart system allows you to customize your order and proceed to checkout effortlessly. With just a few clicks, you can have your desired meals on their way to your doorstep. It's quick, convenient, and guarantees a satisfying meal every time.

For restaurant owners and managers, Foodie offers an intuitive admin panel. Take control of your menu by creating food categories, adding new items, and keeping everything up-to-date. Our platform ensures that managing your offerings is a breeze, leaving you more time to focus on delivering exceptional culinary experiences.

At Foodie, we value your security and strive to provide a seamless ordering process. Rest assured that your personal information is protected, and our reliable system ensures timely delivery of your orders.

Discover the joy of online food ordering with Foodie today. Indulge in a world of flavors, convenience, and culinary delights. Place your order now and let us take care of your cravings.
## Features
### Customer Features
- User authentication and authorization
- add food to cart
- order food
### Admin Features
- Admin authentication and authorization for admin pannel
- Add, edit and delete custom Food categories
- Add, edit and delete custom Food items


## 🏃‍♂️Installation
1. Clone the repository

``` bash
git clone https://github.com/sea-rod/Budget-Helper.git
```
2. Change the working directory
```bash
cd Budget-Helper
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
or
```bash
python -m pip insatll -r requirements.txt 
```
4. Then run the `python manage.py migrate` to make create tables in the database
```bash
python manage.py migrate
```
5. Then run the `python manage.py collectstatic` command
```bash
python manage.py collectstatic
```
6. Start the development server
```bash
python manage.py runserver
```
>Note: Do not use the this server for production

7. Open your web browser and navigate to http://127.0.0.1:8000 to use the application.

8. Thats all your good to go. Enjoy the app 💖!!


## 🔨Built with
- [Django](https://www.djangoproject.com/): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## Contributing
Contributions to the Django Budget App are welcome! Please submit a pull request with any changes or improvements you would like to make.

## License
This project is licensed under the MIT license - see [`License`](LICENSE) file for details.