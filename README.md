# GreenSite

A collaborative Django web project focused on green/environment-friendly technologies, built by a 5-member team as part of a university course.

## 🌱 Project Description
GreenSite is a platform for sharing and discovering green technologies, eco-friendly products, and environmental news. The site features user authentication, file uploads, search, user history tracking, and more, all styled with Bootstrap for a modern, green-themed look.

## 🚀 Features
- User authentication: login, logout, forgot password
- Different interfaces for registered/unregistered users
- Search bar with dropdown suggestions
- User visit history (sessions & cookies)
- File upload (photo, document, etc.)
- Class-based views for index/detail pages
- Bootstrap-styled, responsive design
- Footer with useful links
- Extra pages: About Us, Contact Us, Team Details
- Initial data loaded via JSON fixtures

## 👥 Group Responsibilities
| Member | Main Area(s) | Models (2) | Views (2+) | Templates (2+) | Forms (2+) | Special Features |
|--------|--------------|------------|------------|----------------|------------|------------------|
| 1      | Articles & News | Article, Category | ArticleList, ArticleDetail (CBV) | article_list, article_detail | ArticleForm, CategoryForm | Search bar, CBV |
| 2      | Products & Reviews | Product, Review | ProductList, ProductDetail (CBV) | product_list, product_detail | ProductForm, ReviewForm | File upload |
| 3      | User Management & History | UserProfile, VisitHistory | Register, Login, Logout, UserHistory | register, login, user_history | RegisterForm, LoginForm | Sessions, cookies, Auth |
| 4      | Team & Contact | TeamMember, ContactMessage | TeamView, ContactView | team, contact | TeamForm, ContactForm | Footer, About us, Contact us |
| 5      | Events & Uploads | Event, Upload | EventList, UploadView | event_list, upload | EventForm, UploadForm | Reg/Unreg logic, Extra pages |

## 🛠️ Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/greensite.git
   cd greensite
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations and load initial data:**
   ```bash
   python manage.py migrate
   python manage.py loaddata main/fixtures/initial_data.json
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the site:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 📁 Project Structure
- `main/models.py` — All models
- `main/views.py` — All views (including class-based views)
- `main/forms.py` — All forms
- `main/templates/` — All templates (Bootstrap-based)
- `main/fixtures/initial_data.json` — Initial data

## 🤝 Contribution Guidelines
- Each member works on their assigned features and submits pull requests for review.
- All code must be original and written by group members.
- Weekly meetings to review progress and integrate features.
- All group members must contribute to views and core logic.

## 📄 Documentation & Presentation
- Screenshots, code, and a table of group member contributions will be included in the final Word document and PowerPoint presentation.
- All group members must participate in the oral presentation and Q&A.

---

> **Note:** This project is for educational purposes. All code is original and written by the group members as per course requirements. 