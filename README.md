# Game Hub Persia

پلتفرم وب چندزبانه برای فهرست بازی‌ها، اخبار، بررسی‌ها و تعاملات کاربران. این مخزن یک نمونه ساده از جنگو + DRF با قالب‌های RTL و درگاه API ارائه می‌کند.

## راه‌اندازی سریع
1. ساخت محیط مجازی و نصب وابستگی‌ها:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. اعمال مایگریشن‌ها و ایجاد ابرکاربر:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. اجرای سرور توسعه:
   ```bash
   python manage.py runserver
   ```

## نکات استقرار
- متغیرهای محیطی `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, و `DJANGO_ALLOWED_HOSTS` را مقداردهی کنید.
- فایل‌های استاتیک را با اجرای `collectstatic` گردآوری کنید.
- برای امنیت بیشتر از لایه‌های WAF/SSL و هدرهای امنیتی استفاده کنید.
