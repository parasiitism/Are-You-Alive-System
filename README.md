


![exection_page](https://github.com/user-attachments/assets/45216a51-a850-4185-8cd9-e926957decd7)

![home](https://github.com/user-attachments/assets/d64f228b-406c-4e96-9559-4d6858248631)
![landing_page](https://github.com/user-attachments/assets/b32187a2-a32c-43d0-bee3-b63458a85c50)

![registration_page](https://github.com/user-attachments/assets/24f1a895-3f1d-4adf-a11d-82d9292e649c)
<img width="1888" height="825" alt="render" src="https://github.com/user-attachments/assets/c1b7ef13-90aa-485f-9c02-ea4d9bce3fd8" />


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

