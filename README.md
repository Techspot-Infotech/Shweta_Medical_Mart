# Shweta Medical Mart 🏥

Welcome to the official repository for **Shweta Medical Mart**, a comprehensive static web application designed for a pharmacy and healthcare provider based in Sangli. This platform connects customers with quality generic medicines, surgical items, and dedicated healthcare services.

## 📖 Project Overview

Shweta Medical Mart is a modern, responsive website built with a **pure static architecture**. It serves as a digital gateway to a multi-faceted healthcare center:
*   **Pharmacy**: Generic and branded medicines.
*   **OPD**: Outpatient Department services with doctor schedules.
*   **Gift Shop**: A variety of articles and gifts.
*   **Cafe**: A relaxing space for visitors.

The website provides a seamless user experience for browsing services, viewing product galleries, and booking appointments, with no backend dependencies required.

## ✨ Key Features

*   **🌐 Complete Multilingual Support**: 
    *   Fully localized in **English**, **Marathi**, and **Hindi**.
    *   Instant language switching using `localStorage` persistence.
    *   Covers all pages including Gallery, Testimonials, and FAQs.
*   **🏃 Fast & Static**: No server-side processing required. Pages load instantly and can be hosted freely on platforms like GitHub Pages.
*   **🏥 Trusted Identity**: A consistent **Medical Green** theme across the site to build trust and brand recognition.
*   **🖼️ Dynamic Gallery**: 
    *   Organized into **Cafe, Gift Shop, and Medicine** categories.
    *   Features a premium **focus-blur effect** and lightbox viewer.
    *   Fully translatable category titles and messaging.
*   **📅 WhatsApp Integration**: 
    *   **Direct Booking**: Appointment forms send structured WhatsApp messages.
    *   **Enquiry Forms**: General enquiries are also routed to WhatsApp for quick response.
*   **❓ Testimonials & FAQ**: Dedicated sections to build credibility and answer common customer questions.
*   **📱 Responsive & Modern**: Built with **Bootstrap 5** and custom CSS for a "Glassmorphism" feel that works on all devices.
*   **📍 Location & Contact**: Integrated Google Maps and one-click floating action buttons for Call, WhatsApp, and Email.

## 🛠️ Technology Stack

*   **Frontend**: HTML5, CSS3 (Bootstrap 5 + Custom), JavaScript (ES6+)
*   **Localization**: Custom JS-based translation engine (`translations.js`, `localization.js`)
*   **Animations**: AOS (Animate On Scroll) Library
*   **Icons**: FontAwesome


## 🚀 Installation & Usage

**No installation required!** This is a static site.

### Option 1: Live Preview (Local)
1.  **Clone or Download** the repository.
2.  Double-click `index.html` to open it in your browser.
    *   *Note: For the best experience (avoiding CORS issues), use a local server.*

### Option 2: Local Server (Recommended)
If you have Python installed or use VS Code:

1.  Open text terminal in the project folder.
2.  Run:
    ```bash
    python -m http.server
    ```
3.  Visit `http://localhost:8000` in your browser.

## 📂 Project Structure

```
Shweta_Medical_Mart/
├── index.html            # Main Landing Page (Hero, Features, Testimonials, FAQ)
├── about.html            # About Us Page
├── gallery.html          # Gallery Overview Page
├── category.html         # Dynamic Category Gallery Page (handles ?cat=x)
├── opd.html              # OPD Services & Business Card
├── appointment.html      # Appointment Booking Form
├── contact.html          # Contact Form & Information
│
├── static/               # Assets
│   ├── css/
│   │   └── style.css     # Global Stylesheet
│   ├── js/
│   │   ├── main.js       # UI Interaction Scripts
│   │   ├── translations.js # Translation Dictionary (En, Mr, Hi)
│   │   ├── localization.js # Localization Logic
│   │   └── images.js     # Centralized Image List
│   └── images/           # Images (Sorted by category)
│
└── README.md             # Documentation
```

## 🌐 Localization System

The project uses a lightweight, custom localization engine:
1.  **Dictionary**: `static/js/translations.js` contains all text keys.
2.  **HTML Marking**: Elements are marked with `data-i18n="key"`.
3.  **Placeholders**: Inputs use `data-i18n="[placeholder]key"`.
4.  **Auto-Detect**: The system remembers the user's last selected language.

## 📞 Contact

**Shweta Medical Mart**
*   **Address**: Near Civil Hospital, Sangli–Miraj Road, Sangli, Maharashtra
*   **Phone**: +91 99233 46656
*   **Email**: info@shwetamedicalmart.in

---
*Developed by Techspot Infotech LLP*
