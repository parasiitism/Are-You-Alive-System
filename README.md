# 🫀 LifeCheck – Inactivity-Based Safety Alert System

LifeCheck is a safety-focused mobile backend system that monitors user inactivity.
If a user does not check in within a configured time window, the system can escalate
alerts to emergency contacts.

> ⚠️ Disclaimer:  
> This application is NOT a medical or emergency service.  
> Alerts are informational only.

---

## 🧠 Problem Statement

Many individuals live alone or face health risks.
If they become inactive for long periods, there is no automatic way to check their safety.

LifeCheck solves this by:
- Tracking user activity ("I'm Safe")
- Detecting prolonged inactivity
- Escalating alerts responsibly

---

## 🏗️ High-Level Architecture

```text
+------------------+
|  Mobile App      |
|  (Flutter)       |
|                  |
| - Register       |
| - Verify OTP     |
| - "I'm Safe"     |
+--------+---------+
         |
         | HTTPS (REST APIs)
         v
+----------------------------+
|        FastAPI Backend     |
|----------------------------|
|  /auth/register            |
|  /otp/send                 |
|  /otp/verify               |
|  /heartbeat                |
|                            |
|  Business Logic:           |
|  - Consent validation      |
|  - OTP verification        |
|  - Activity tracking       |
+-------------+--------------+
              |
              |
              v
+----------------------------+
|        Database            |
|   (SQLite / PostgreSQL)    |
|----------------------------|
|  users table               |
|  - phone numbers           |
|  - consent flag            |
|  - is_verified             |
|  - last_active_at          |
+----------------------------+




## 📸 Screenshots

![Render Dashboard](images\render.png)

![Home Screen](images\home.jpeg)

![Landing Page](landing_page.jpeg)

![Registration Page](images\registration_page.jpeg)

![Execution Page](images\exection_page.jpeg)