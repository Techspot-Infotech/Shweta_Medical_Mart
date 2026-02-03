import os
from flask import Flask, render_template, request, session, redirect, url_for
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = 'shweta-medical-mart-secret-key'

@app.before_request
def set_default_language():
    if 'lang' not in session:
        session['lang'] = 'en'

@app.context_processor
def inject_translations():
    lang = session.get('lang', 'en')
    return dict(_=lambda key: TRANSLATIONS.get(lang, {}).get(key, key))

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['lang'] = lang
    return redirect(request.referrer or url_for('home'))

@app.route('/')
def home():
    videos = []
    # Categorized Image Lists
    cafe_images = []
    shop_images = []
    medicine_images = []
    
    # Define folder paths
    base_image_folder = os.path.join(app.static_folder, 'images')
    cafe_folder = os.path.join(base_image_folder, 'Cafe+Interior')
    shop_folder = os.path.join(base_image_folder, 'Gift_shop+Articles')
    medicine_folder = os.path.join(base_image_folder, 'Medicine')
    
    # Helper to get images from a folder
    def get_images_from_folder(folder_path):
        if os.path.exists(folder_path):
            return sorted([f for f in os.listdir(folder_path) 
                         if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))])
        return []

    cafe_images = get_images_from_folder(cafe_folder)
    shop_images = get_images_from_folder(shop_folder)
    medicine_images = get_images_from_folder(medicine_folder)
                 
    return render_template('home.html', 
                         videos=videos, 
                         cafe_images=cafe_images, 
                         shop_images=shop_images, 
                         medicine_images=medicine_images)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/opd')
def opd():
    return render_template('opd.html')

@app.route('/gallery')
def gallery():
    # Categorized Image Lists
    cafe_images = []
    shop_images = []
    medicine_images = []
    
    # Define folder paths
    base_image_folder = os.path.join(app.static_folder, 'images')
    cafe_folder = os.path.join(base_image_folder, 'Cafe+Interior')
    shop_folder = os.path.join(base_image_folder, 'Gift_shop+Articles')
    medicine_folder = os.path.join(base_image_folder, 'Medicine')
    
    # Helper to get images from a folder
    def get_images_from_folder(folder_path):
        if os.path.exists(folder_path):
            return sorted([f for f in os.listdir(folder_path) 
                         if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))])
        return []

    cafe_images = get_images_from_folder(cafe_folder)
    shop_images = get_images_from_folder(shop_folder)
    medicine_images = get_images_from_folder(medicine_folder)
                 
    return render_template('gallery.html', 
                         cafe_images=cafe_images, 
                         shop_images=shop_images, 
                         medicine_images=medicine_images)

@app.route('/gallery/<category>')
def gallery_category(category):
    # Map URL category to Folder Name and Display Title
    category_map = {
        'cafe': {'folder': 'Cafe+Interior', 'title': 'Cafe / Interior'},
        'shop': {'folder': 'Gift_shop+Articles', 'title': 'Gift Shop / Article'},
        'medicine': {'folder': 'Medicine', 'title': 'Medicine'}
    }
    
    if category not in category_map:
        return redirect(url_for('gallery'))
        
    info = category_map[category]
    folder_path = os.path.join(app.static_folder, 'images', info['folder'])
    
    images = []
    if os.path.exists(folder_path):
        images = sorted([f for f in os.listdir(folder_path) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))])
    
    return render_template('category.html', 
                         images=images, 
                         category_title=info['title'],
                         folder_name=info['folder'])

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

if __name__ == '__main__':
    app.run(debug=True)
