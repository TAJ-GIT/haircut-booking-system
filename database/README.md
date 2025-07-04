---

## 🧰 MySQL Workbench (RDS Setup)

Used **MySQL Workbench** to manage the Amazon RDS MySQL database.

### ✅ SQL Commands Used:

```sql
CREATE DATABASE haircut_db;
USE haircut_db;

CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

SELECT * FROM appointments;
