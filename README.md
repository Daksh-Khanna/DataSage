# 🚀 Summer Project - Interactive Data Dashboard

## 📌 Overview
This project is a **Streamlit-powered interactive dashboard** that connects to a PostgreSQL database, retrieves session data, and enables users to apply dynamic filters for a seamless experience.

## 🔥 Features
- **Database Integration** → Uses PostgreSQL for efficient data retrieval  
- **Dynamic Filtering** → Apply multiple filters at the **query level** for optimized results  
- **Secure Configuration** → Stores credentials securely using environment variables  
- **Session State Management** → Preserves user selections for a better experience  
- **Optimized UI** → Custom sidebar layout with interactive elements  

## 🛠️ Installation
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/Daksh-Khanna/Summer_Project_2025.git
cd Summer_Project_2025
```

Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Configure Environment Variables
Create a .env file:
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_secure_password
DB_HOST=your_host


🚨 Do NOT share actual credentials in public repositories!
✅ Ensure .env is added to .gitignore to prevent accidental uploads.
5️⃣ Run the Streamlit App
streamlit run app.py


🎯 Project Structure
├── backend/
│   ├── config.py        # Loads environment variables
│   ├── db_connector.py  # Handles PostgreSQL connection
│   ├── queries.py       # Dynamically builds SQL queries
│   ├── data_fetcher.py  # Fetches filtered data
│
├── frontend/
│   ├── ui_manager.py    # Manages UI rendering (filters, sidebar)
│
├── .env                 # Environment file (credentials)
├── app.py               # Entry point for Streamlit app
├── requirements.txt     # Required dependencies
├── README.md            # Documentation file
├── config.py			 # Configuration file


🔒 Security Best Practices
- Never expose .env files in public repositories (ensure .gitignore includes .env).
- Use parameterized queries to prevent SQL injection (%s placeholders).
- Restrict database user permissions to prevent unauthorized modifications.

🤝 Contributing
If you'd like to contribute:
- Fork the repository and create a feature branch.
- Submit a pull request after making enhancements.
- Ensure code follows modular best practices.

🏆 Acknowledgments
Thanks to Streamlit, PostgreSQL, and the amazing Python community for making interactive data applications easy!