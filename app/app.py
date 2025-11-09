from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # Пример данных о товарах
    products = [
        {
            'id': 1,
            'name': 'Ноутбук Pro',
            'description': 'Мощный ноутбук для работы и развлечений',
            'price': 89999,
            'image': 'https://via.placeholder.com/300x200?text=Laptop'
        },
        {
            'id': 2,
            'name': 'Смартфон Ultra',
            'description': 'Современный смартфон с отличной камерой',
            'price': 49999,
            'image': 'https://via.placeholder.com/300x200?text=Phone'
        },
        {
            'id': 3,
            'name': 'Наушники Wireless',
            'description': 'Беспроводные наушники с шумоподавлением',
            'price': 12999,
            'image': 'https://via.placeholder.com/300x200?text=Headphones'
        },
        {
            'id': 4,
            'name': 'Планшет Mini',
            'description': 'Компактный планшет для чтения и работы',
            'price': 24999,
            'image': 'https://via.placeholder.com/300x200?text=Tablet'
        },
        {
            'id': 5,
            'name': 'Часы Smart',
            'description': 'Умные часы с отслеживанием активности',
            'price': 19999,
            'image': 'https://via.placeholder.com/300x200?text=Watch'
        },
        {
            'id': 6,
            'name': 'Клавиатура Mechanical',
            'description': 'Механическая клавиатура для геймеров',
            'price': 8999,
            'image': 'https://via.placeholder.com/300x200?text=Keyboard'
        }
    ]

    @app.route('/')
    def index():
        return render_template('products.html', products=products)

    @app.route('/products')
    def products_page():
        return render_template('products.html', products=products)

    return app

# Для локального запуска
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

