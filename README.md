# 🎂 Birthday Check System

একটি সম্পূর্ণ **User Authentication & Birthday Management System** Python Flask দিয়ে তৈরি।

## ✨ Features

- ✅ User Registration (নতুন অ্যাকাউন্ট তৈরি)
- ✅ User Login (লগইন সিস্টেম)
- ✅ Password Hashing (সুরক্ষিত পাসওয়ার্ড)
- ✅ Birthday Storage (জন্মদিন সংরক্ষণ)
- ✅ Age Calculation (বয়স ক্যালকুলেশন)
- ✅ Birthday Alert (জন্মদিন আজ কিনা)
- ✅ User Profile (ব্যবহারকারী প্রোফাইল)
- ✅ Session Management (সেশন ম্যানেজমেন্ট)

## 📋 প্রয়োজনীয় জিনিস

- Python 3.7+
- pip (Python Package Manager)

## 🚀 Installation

### 1. Repository Clone করুন

```bash
git clone https://github.com/mrbx001/birthday-check.git
cd birthday-check
```

### 2. Virtual Environment তৈরি করুন

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Dependencies Install করুন

```bash
pip install -r requirements.txt
```

## ▶️ চালানোর নিয়ম

```bash
python app.py
```

তারপর ব্রাউজার এ যান: **http://localhost:5000**

## 📝 ব্যবহার

### Registration (রেজিস্টার করুন)
1. "এখানে ক্লিক করুন" link এ ক্লিক করুন
2. সব তথ্য ভরুন:
   - সম্পূর্ণ নাম
   - Username
   - ইমেইল
   - জন্মদিন (YYYY-MM-DD)
   - Password

### Login (লগইন করুন)
1. Username এবং Password দিয়ে লগইন করুন
2. আপনার প্রোফাইল দেখুন

### Profile (প্রোফাইল দেখুন)
- আপনার সব তথ্য দেখা যাবে
- আপনার বয়স অটোম্যাটিক ক্যালকুলেট হবে
- যদি আজ আপনার জন্মদিন হয় তাহলে বিশেষ মেসেজ দেখাবে

## 📁 File Structure

```
birthday-check/
├── app.py                 # Main Flask Application
├── requirements.txt       # Python Dependencies
├── users.db              # SQLite Database (Auto-created)
├── templates/
│   ├── base.html        # Base Template
│   ├── login.html       # Login Page
│   ├── register.html    # Registration Page
│   └── profile.html     # Profile Page
└── README.md            # এই ফাইল
```

## 🔐 নিরাপত্তা টিপস

⚠️ **Production এ ব্যবহারের আগে:**

1. `app.py` এ `SECRET_KEY` পরিবর্তন করুন
2. `debug=True` কে `debug=False` করুন
3. আরও শক্তিশালী database ব্যবহার করুন (PostgreSQL)
4. HTTPS ব্যবহার করুন

## 📚 ব্যবহৃত প্রযুক্তি

- **Flask** - Web Framework
- **SQLAlchemy** - ORM
- **SQLite** - Database
- **Werkzeug** - Password Hashing

## 🐛 সমস্যা সমাধান

### Port 5000 ইতিমধ্যে ব্যবহৃত?
```bash
python app.py --port 5001
```

### Database Reset করতে চান?
```bash
# users.db ফাইল ডিলিট করুন এবং আবার চালান
rm users.db
python app.py
```

## 📧 Contact

এই প্রজেক্টে কোনো সমস্যা বা পরামর্শ থাকলে জানান!

## 📄 License

এটি একটি শেখার প্রজেক্ট। স্বাধীনভাবে ব্যবহার করুন!

---

**Happy Coding! 🎉**
