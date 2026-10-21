# 🚀 Vercel Deployment Guide (Digital Dokan Fullstack)

এই প্রজেক্টটি Vercel-এ ডিপ্লয় করার জন্য সমস্ত কনফিগারেশন ফাইল প্রস্তুত করা হয়েছে।

---

## 📁 তৈরি করা কনফিগারেশন ফাইলসমূহ:

1. **Root `vercel.json`**: ফ্রন্টএন্ড এবং ব্যাকএন্ড একসাথে মনোরিপো (All-in-One) হিসেবে ডিপ্লয় করার কনফিগারেশন।
2. **Root `api/index.py`**: Vercel Serverless Function হিসেবে Django WSGI হ্যান্ডলার।
3. **`frontend/vercel.json`**: React Router SPA রিরাইট (যাতে পেজ রিফ্রেশ করলে ৪MD/404 এরর না আসে)।
4. **`frontend/src/api/axios.js`**: স্বয়ংক্রিয়ভাবে `VITE_API_BASE_URL` অথবা লোকাল `/api` ডিটেকশন।
5. **`backend/requirements.txt` & Root `requirements.txt`**: প্রোডাকশন ডিপেন্ডেন্সি (Django, DRF, Whitenoise, dj-database-url, psycopg2-binary ইত্যাদি)।
6. **`backend/config/settings.py`**: Whitenoise স্ট্যাটিক ফাইলস, CORS, CSRF, এবং ক্লাউড PostgreSQL ডাটাবেজ সাপোর্ট।
7. **`backend/api/index.py` & `backend/vercel.json`**: ব্যাকএন্ড আলাদাভাবে ডিপ্লয় করার জন্য হ্যান্ডলার।
8. **`.gitignore`**: অপ্রয়োজনীয় নোড মডিউল এবং ক্যাশ ফাইল ব্লক করার রুলস।

---

## 🌟 পদ্ধতি ১: All-in-One (Monorepo) ডিপ্লয়মেন্ট (সবচেয়ে সহজ ও রেকমেন্ডেড)

এই পদ্ধতিতে আপনার ফ্রন্টএন্ড ও ব্যাকএন্ড একই Vercel ডোমেইনে চলবে (যেমন: `digital-dokan.vercel.app` এবং API হবে `digital-dokan.vercel.app/api`). এতে কোনো CORS ইস্যু তৈরি হয় না।

### ধাপসমূহ:
1. পুরো প্রজেক্টটি গিটহাবে (GitHub) পুশ করুন:
   ```bash
   git init
   git add .
   git commit -m "Setup for Vercel deployment"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo.git
   git push -u origin main
   ```
2. [Vercel Dashboard](https://vercel.com)-এ যান এবং **Add New... > Project** সিলেক্ট করুন।
3. আপনার গিটহাব রিপোজিটরিটি সিলেক্ট করে **Import** করুন।
4. **Environment Variables** সেকশনে নিচের ভেরিয়েবলগুলো যোগ করুন:
   - `SECRET_KEY` = `django-insecure-mowsw5^t15)du*)r&%u%wel4kdz2j^*+dzo*lsds=@c4dgs&#n` (বা যেকোনো শক্তিশালী স্ট্রিং)
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `*`
   - `DATABASE_URL` = *(যদি ক্লাউড PostgreSQL ব্যবহার করেন, নিচে দেখুন)*
5. **Deploy** বাটনে ক্লিক করুন!

---

## 🌟 পদ্ধতি ২: ফ্রন্টএন্ড ও ব্যাকএন্ড আলাদা ডিপ্লয় করা

আপনি চাইলে ফ্রন্টএন্ড এবং ব্যাকএন্ড দুটি আলাদা Vercel প্রজেক্ট হিসেবেও ডিপ্লয় করতে পারেন:

### ক. Backend ডিপ্লয়:
1. Vercel-এ রিপোজিটরিটি Import করার সময় **Root Directory** হিসেবে `backend` সিলেক্ট করুন।
2. Environment Variables দিন (`SECRET_KEY`, `DEBUG`, `DATABASE_URL`)।
3. Deploy হলে ব্যাকএন্ডের একটি URL পাবেন (যেমন: `https://your-backend.vercel.app`).

### খ. Frontend ডিপ্লয়:
1. Vercel-এ আরেকটি প্রজেক্ট তৈরি করে **Root Directory** হিসেবে `frontend` সিলেক্ট করুন।
2. **Environment Variables**-এ যোগ করুন:
   - `VITE_API_BASE_URL` = `https://your-backend.vercel.app/api`
3. Deploy করুন।

---

## 🗄️ ডাটাবেজ (Database) সংক্রান্ত তথ্য:

> [!IMPORTANT]
> **Vercel সার্ভারলেস ফাইলসিস্টেম Read-Only:**
> প্রজেক্টের সাথে থাকা `db.sqlite3` ফাইলটি Vercel-এ রিড-অনলি হিসেবে রান হবে (অর্থাৎ আপনার বর্তমান প্রোডাক্ট ও ক্যাটাগরিগুলো ব্রাউজারে দেখা যাবে)। কিন্তু নতুন প্রোডাক্ট তৈরি, ইউজার রেজিস্ট্রেশন বা অর্ডার ডাটা স্থায়ীভাবে সেভ রাখতে একটি ফ্রি ক্লাউড PostgreSQL ডাটাবেজ ব্যবহার করা উত্তম।

### ফ্রি ক্লাউড PostgreSQL ডাটাবেজ কানেক্ট করার উপায়:
1. [Neon.tech](https://neon.tech) অথবা [Supabase](https://supabase.com)-এ একটি ফ্রি অ্যাকাউন্ট খুলে ১ ক্লিকে একটি PostgreSQL ডাটাবেজ তৈরি করুন।
2. সেখান থেকে **Connection String** কপি করুন (উদাহরণ: `postgresql://user:password@ep-cool-123.neon.tech/neondb?sslmode=require`).
3. Vercel ড্যাশবোর্ডের Environment Variables-এ `DATABASE_URL` নামে সেই স্ট্রিংটি পেস্ট করে দিন।
4. ব্যস! Django স্বয়ংক্রিয়ভাবে ক্লাউড ডাটাবেজ ব্যবহার করা শুরু করবে।

---

## 🔑 Environment Variables রিক্যাপ:

| Variable Name | Required? | Description |
|---|---|---|
| `SECRET_KEY` | হ্যাঁ | Django সিকিউরিটি কি |
| `DEBUG` | না (Default: False) | প্রোডাকশনে `False` রাখা আবশ্যক |
| `ALLOWED_HOSTS` | না (Default: `*`) | অনুমোদিত হোস্ট ডোমেইন |
| `DATABASE_URL` | রিকমেন্ডেড | PostgreSQL কানেকশন লিংক (Neon / Supabase) |
| `VITE_API_BASE_URL` | শুধু পদ্ধতি ২-এ | ব্যাকএন্ডের পূর্ণাঙ্গ API URL |

