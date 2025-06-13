# 🪑 Streamlit Restaurant Booking System

This is a web-based restaurant table booking application built with **Python** and **Streamlit**.  
The project was developed as a final assignment for the Python Programming course at HSE University.

## 🚀 Features

- Add and manage restaurant tables through an intuitive web interface
- Bookings are allowed only for the **following day or later**
- Bookings **cannot be made if less than 3 hours remain** before the reservation time
- Ensures **at least 1 hour** between any two bookings for the same table
- A table is considered **unavailable only if it is occupied**
- Tables **cannot be deleted** if they are occupied or have any upcoming bookings

## 🖥️ How to Run the App

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Launch the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Add tables on the first screen and begin creating bookings.

## 🗂️ Project Structure

- `app.py` — Streamlit user interface
- `main.py` — optional CLI-based interface (legacy)
- `restaurant.py` — core restaurant logic
- `table.py` — table class and status handling
- `booking.py` — booking rules and time constraints
- `guest.py` — guest-related functionality
- `requirements.txt` — Python dependencies

## 📸 Interface Preview

You can add a screenshot here once available:

```markdown
![App Screenshot](screenshots/demo.png)
```

## 🧾 Requirements

- Python 3.7+
- Tested with Streamlit 1.40+

## 🎓 About the Project

This application was developed as part of the final project for the **Python Programming** course at the **National Research University Higher School of Economics (HSE)**.
