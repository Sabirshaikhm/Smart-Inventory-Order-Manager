from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from models import db, Product, Order, OrderItem
from forms import ProductForm, OrderForm
from utils import generate_invoice_pdf
import io
import os

def create_app(db_path='sqlite:///smart_inventory.db'):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.jinja_env.globals['low_stock_threshold'] = 5

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        products = Product.query.order_by(Product.name).all()
        return render_template("index.html", products=products)

    @app.route('/product/new', methods=['GET','POST'])
    def new_product():
        form = ProductForm()
        if form.validate_on_submit():
            p = Product(name=form.name.data, description=form.description.data,
                        price=float(form.price.data), qty=int(form.qty.data))
            db.session.add(p)
            db.session.commit()
            flash('Product added.')
            return redirect(url_for('index'))
        return render_template("product_form.html", form=form, title='Add Product')

    @app.route('/product/<int:pid>/edit', methods=['GET','POST'])
    def edit_product(pid):
        p = Product.query.get_or_404(pid)
        form = ProductForm(obj=p)
        if form.validate_on_submit():
            p.name = form.name.data
            p.description = form.description.data
            p.price = float(form.price.data)
            p.qty = int(form.qty.data)
            db.session.commit()
            flash('Product updated.')
            return redirect(url_for('index'))
        return render_template("product_form.html", form=form, title='Edit Product')

    @app.route('/product/<int:pid>/delete')
    def delete_product(pid):
        p = Product.query.get_or_404(pid)
        db.session.delete(p)
        db.session.commit()
        flash('Product deleted.')
        return redirect(url_for('index'))

    @app.route('/order/new', methods=['GET','POST'])
    def new_order():
        products = Product.query.order_by(Product.name).all()
        form = OrderForm()
        if form.validate_on_submit():
            items = []
            for p in products:
                key = f'qty_{p.id}'
                try:
                    q = int(request.form.get(key, '0'))
                except:
                    q = 0
                if q > 0:
                    if q > p.qty:
                        flash(f'Not enough stock for {p.name}')
                        return redirect(url_for('new_order'))
                    items.append((p, q))
            if not items:
                flash('No items selected.')
                return redirect(url_for('new_order'))
            order = Order(customer_name=form.customer_name.data,
                          customer_email=form.customer_email.data)
            db.session.add(order)
            db.session.commit()
            order_items = []
            for p, q in items:
                oi = OrderItem(order_id=order.id, product_id=p.id,
                               product_name=p.name, price=p.price, qty=q)
                order_items.append(dict(product_name=p.name, price=p.price, qty=q))
                p.qty -= q
                db.session.add(oi)
            db.session.commit()
            pdf = generate_invoice_pdf(order, order_items, company_info={'name':'Intact Media'})
            return send_file(io.BytesIO(pdf), as_attachment=True,
                             download_name=f'invoice_{order.id}.pdf',
                             mimetype='application/pdf')
        return render_template("order_form.html", form=form, products=products)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
