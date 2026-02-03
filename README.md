# Shweta Medical Mart 🏥

Welcome to the official repository for **Shweta Medical Mart**, a comprehensive web application designed for a pharmacy and healthcare provider based in Sangli. This platform connects customers with quality generic medicines, surgical items, and dedicated healthcare services.

## 📖 Project Overview

Shweta Medical Mart is more than just a pharmacy website. It serves as a digital gateway to a multi-faceted healthcare and lifestyle center that includes:
*   **Pharmacy**: Generic and branded medicines.
*   **OPD**: Outpatient Department services.
*   **Gift Shop**: A variety of articles and gifts.
*   **Cafe**: A relaxing space for visitors.

The website provides a seamless user experience for browsing services, viewing product galleries, and booking appointments.

## ✨ Key Features

*   **🌐 Multilingual Support**: Accessible in **English**, **Marathi**, and **Hindi** to serve a diverse local audience.
*   **🏥 Green Theme Identity**: A consistent **Medical Green** theme across the site (Home, About, Contact) to build trust.
*   **🖼️ Smart Gallery**: Organized into **Cafe, Gift Shop, and Medicine** categories with a premium focus-blur effect.
*   **📅 WhatsApp Appointments**: Direct WhatsApp integration for fast and personal booking confirmation.
*   **🆔 Unique OPD Card**: A specialized **Business Card Style** design for the OPD section to highlight doctor details.
*   **📱 Responsive & Modern**: Built with **Bootstrap 5** and custom CSS for a "Glassmorphism" feel.
*   **📍 Location & Contact**: Integrated Google Maps and one-click floating action buttons.

## 🛠️ Technology Stack

*   **Backend**: Python (Flask Framework)
*   **Frontend**: HTML5, CSS3, JavaScript
*   **Styling**: Bootstrap 5, Custom CSS
*   **Templating**: Jinja2
*   **Animations**: AOS (Animate On Scroll) Library
*   **Icons**: FontAwesome

## 🚀 Installation & Usage

Follow these steps to set up the project locally:

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd Shweta_Medical_Mart
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**

    **Option 1: Using the Startup Script (Windows)**
    Simply double-click `run.bat` or run it from the command line:
    ```bash
    run.bat
    ```

    **Option 2: Manual Start**
    ```bash
    python app.py
    ```

5.  **Access the Website**
    Open your browser and navigate to: `http://127.0.0.1:5000/`

## 📂 Project Structure

```
Medical_Mart/
├── app.py                # Main Flask application file
├── translations.py       # Dictionary for multilingual text
├── requirements.txt      # Project dependencies
├── run.bat               # Windows startup script
├── static/               # Static assets (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/            # HTML templates
    ├── base.html         # Base layout with navbar and footer
    ├── home.html         # Landing page
    ├── about.html        # About Us page
    ├── gallery.html      # Main gallery page
    ├── category.html     # Specific category gallery
    ├── opd.html          # OPD services page
    ├── appointment.html  # Booking form
    └── contact.html      # Contact information
```

## 📞 Contact

**Shweta Medical Mart**
*   **Address**: Sangli, Maharashtra
*   **Phone**: +91 99233 46656
*   **Email**: info@shwetamedicalmart.in

---
*Developed with ❤️ for Shweta Medical Mart.*
