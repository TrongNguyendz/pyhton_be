À ok hiểu rồi 🙌, bạn làm **backend bằng Python** (mình thấy bạn có `app.py`, `dss_logic.py`, `models.py`, DB SQLite `cosmetics.db`).

Mình sẽ viết cho bạn một file **`README.md`** chuẩn cho project Python này.

---

## 📄 README.md (gợi ý cho dự án của bạn)

```markdown
# Cosmetic DSS - Backend (Python)

## 🚀 Giới thiệu
Đây là backend API cho hệ thống **Cosmetic Decision Support System**.  
Dự án được viết bằng **Python (Flask)** và sử dụng **SQLite** để lưu trữ dữ liệu.

---

## 📂 Cấu trúc thư mục
```

/cosmetic-dss
┣ app.py          # Flask API chính
┣ dss\_logic.py    # Xử lý logic DSS (gợi ý sản phẩm)
┣ models.py       # Khởi tạo DB và models
┣ cosmetics.db    # CSDL SQLite (demo)
┗ README.md       # Tài liệu

````

---

## ⚙️ Yêu cầu hệ thống
- Python 3.9+  
- pip (Python package manager)  

---

## 📦 Cài đặt

### 1️⃣ Clone repo
```bash
git clone https://github.com/TrongNguyendz/pyhton_be.git
cd pyhton_be
````

### 2️⃣ Tạo môi trường ảo (tuỳ chọn nhưng khuyến khích)

```bash
python -m venv venv
source venv/bin/activate   # Trên Linux/macOS
venv\Scripts\activate      # Trên Windows
```

### 3️⃣ Cài dependencies

```bash
pip install flask werkzeug
```

### 4️⃣ Khởi tạo database (nếu cần reset DB)

```bash
python models.py
```

---

## ▶️ Chạy server

```bash
python app.py
```

API sẽ chạy tại:
👉 `http://127.0.0.1:5000/`

---

## 📌 Các API chính

### 🔹 Auth

* `POST /register` → đăng ký user mới
* `POST /login` → đăng nhập

### 🔹 DSS

* `GET /recommend?skin_type=oily&problem=acne&budget=300`
  → trả về danh sách sản phẩm gợi ý (theo `dss_logic.py`)

---

## ✅ Demo dữ liệu

CSDL có sẵn một số sản phẩm mẫu:

* Cleanser A (BrandX, oily, acne)
* Moisturizer B (BrandY, dry, wrinkles)
* Serum C (BrandZ, oily, dark spots)
* Toner D (BrandX, sensitive, redness)
* Sunscreen E (BrandY, all, prevention)

---

## 👤 Tác giả

* **Tên**: Phú Trọng
* **GitHub**: [TrongNguyendz](https://github.com/TrongNguyendz)

```

---

👉 Bạn có muốn mình viết thêm đoạn **hướng dẫn test API bằng Postman hoặc curl** vào README luôn không?
```
