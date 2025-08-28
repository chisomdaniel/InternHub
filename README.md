# InternHub 🚀

**A comprehensive internship posting and search platform built with Flask, MySQL, and modern web technologies.**

InternHub is a full-stack web application that connects companies with potential interns by providing a platform to post, search, and manage internship opportunities. The platform features a RESTful API backend, responsive web interface, and robust database management.

## ✨ Features

- **Internship Management**: Post, edit, delete, and search internship opportunities
- **RESTful API**: Complete CRUD operations for internship data
- **Responsive Web Interface**: Modern, user-friendly design with search functionality
- **Database Integration**: MySQL database with SQLAlchemy ORM
- **Multi-Application Architecture**: Separate API and web applications
- **CORS Support**: Cross-origin resource sharing for API access

## 🏗️ Architecture

The project follows a modular architecture with clear separation of concerns:

```
InternHub/
├── api/                    # RESTful API application
│   └── version1/          # API version 1
├── web_flask/             # Web interface application
├── models/                # Database models and engine
├── web_files/             # Static web assets
├── bash/                  # Database setup scripts
└── static assets/         # Images and stylesheets
```

## 🛠️ Technology Stack

- **Backend**: Python 3, Flask, SQLAlchemy
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: RESTful with JSON responses
- **Environment**: Linux/Unix compatible

## 📋 Prerequisites

Before running InternHub, ensure you have:

- Python 3.6+
- MySQL Server
- pip (Python package manager)

### Install Prerequisites for mysqlclient (if on Linux/macOS):
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

### Required Python Packages
```bash
pip install flask flask-cors sqlalchemy mysqlclient
```

## 🚀 Quick Start

### 1. Database Setup

First, set up the MySQL database:

```bash
# Log into MySQL as root
mysql -u root -p

# Run the setup script
mysql -u root -p < bash/setup_database.sql
```

This creates:
- Database: `internhub_db`
- User: `internhub` with password `internhub_dev`
- Appropriate permissions

### 2. Environment Configuration

Set the required environment variable:

```bash
export DB_PASS=internhub_dev
```

### 3. Start the API Server

```bash
# From the project root directory
DB_PASS=internhub_dev python3 -m api.version1.app
```

The API will be available at `http://localhost:5000`

### 4. Start the Web Application

```bash
# In a separate terminal
DB_PASS=internhub_dev python3 -m web_flask.pages
```

The web interface will be available at `http://localhost:5001`

## 🔗 API Endpoints

### Internships

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/version1/jobs` | Retrieve all internship postings |
| `GET` | `/api/version1/jobs/<job_id>` | Retrieve a specific internship |
| `POST` | `/api/version1/jobs` | Create a new internship posting |
| `PUT` | `/api/version1/jobs/<job_id>` | Update an existing internship |
| `DELETE` | `/api/version1/jobs/<job_id>` | Delete an internship posting |

### Example API Usage

**Get all internships:**
```bash
curl -X GET http://localhost:5000/api/version1/jobs
```

**Create a new internship:**
```bash
curl -X POST http://localhost:5000/api/version1/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Software Engineering Intern",
    "company": "Tech Corp",
    "company_website": "https://techcorp.com",
    "company_email": "hr@techcorp.com",
    "city": "San Francisco",
    "state": "California",
    "country": "USA",
    "position_type": "Internship",
    "description": "Join our team as a software engineering intern...",
    "responsibility": "Develop web applications...",
    "requirement": "Computer Science student...",
    "skill": "Python, JavaScript, SQL",
    "apply": "Send resume to hr@techcorp.com"
  }'
```

## 🌐 Web Interface

The web application provides:

- **Search Page** (`/`): Browse and search internship opportunities
- **Post Page** (`/post.html`): Submit new internship postings
- **Individual Internship Pages** (`/internship/<id>`): Detailed view of specific opportunities

## 🗄️ Database Schema

### Internship Model

| Field | Type | Description |
|-------|------|-------------|
| `id` | String | Unique identifier |
| `title` | String(50) | Internship title |
| `company` | String(50) | Company name |
| `company_website` | String(50) | Company website URL |
| `company_email` | String(50) | Contact email |
| `phone_number` | Integer | Contact phone (optional) |
| `city` | String(50) | Location city |
| `state` | String(50) | Location state |
| `country` | String(50) | Location country |
| `position_type` | String(50) | Type of position |
| `description` | String(1000) | Job description |
| `responsibility` | String(1000) | Job responsibilities |
| `requirement` | String(1000) | Requirements |
| `skill` | String(1000) | Required skills |
| `benefit` | String(1000) | Benefits (optional) |
| `apply` | String(1000) | Application instructions |
| `expire` | String(50) | Application deadline (optional) |
| `note` | String(1000) | Additional notes (optional) |
| `closing` | String(1000) | Closing statement (optional) |
| `created_at` | DateTime | Creation timestamp |
| `updated_at` | DateTime | Last update timestamp |

## 🚀 Deployment

### Production Deployment

1. **Update API endpoints**: Modify JavaScript files to use production URLs instead of `localhost:5000`

2. **Environment Variables**: Set production environment variables:
   ```bash
   export INTERNHUB_API_HOST=0.0.0.0
   export INTERNHUB_API_PORT=5000
   export DB_PASS=your_production_password
   ```

3. **Web Server Configuration**: Configure nginx or Apache to serve the application

4. **Database**: Set up MySQL in production environment

### Example nginx configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location /api/ {
        proxy_pass http://localhost:5000/;
    }
    
    location / {
        proxy_pass http://localhost:5001/;
    }
}
```

## 🔧 Configuration

### Environment Variables

- `DB_PASS`: MySQL database password (required)
- `INTERNHUB_API_HOST`: API host (default: 0.0.0.0)
- `INTERNHUB_API_PORT`: API port (default: 5000)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of a portfolio demonstration and is available for educational purposes.

## 🐛 Troubleshooting

### Common Issues

**Database Connection Error:**
- Ensure MySQL is running
- Verify database credentials
- Check that `DB_PASS` environment variable is set

**Import Errors:**
- Verify all required packages are installed
- Ensure Python path includes project directory

**API Not Accessible:**
- Check that the API server is running on the correct port
- Verify firewall settings allow connections

## 📞 Support

For questions or issues, please check the troubleshooting section above or refer to the project documentation.

---

Built with ❤️ for connecting companies with talented interns.
