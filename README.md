# 📘 HƯỚNG DẪN CÀI ĐẶT VÀ CHẠY ỨNG DỤNG MULTI-PURPOSE LLM TOOL

## 📋 MỤC LÚC
1. [Giới thiệu](#giới-thiệu)
2. [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
3. [Các bước cài đặt](#các-bước-cài-đặt)
4. [Chạy ứng dụng](#chạy-ứng-dụng)
5. [Sử dụng ứng dụng](#sử-dụng-ứng-dụng)
6. [Cấu trúc dự án](#cấu-trúc-dự-án)
7. [Khắc phục sự cố](#khắc-phục-sự-cố)

---

## 📖 GIỚI THIỆU

**Multi-Purpose LLM Tool** là một ứng dụng web single-page sử dụng Large Language Model (LLM) thông qua Ollama để thực hiện các tác vụ xử lý văn bản khác nhau.

### Chức năng chính:
- 📝 **Summarize**: Tóm tắt văn bản
- 🇫🇷 **Translate to French**: Dịch sang tiếng Pháp
- 👶 **Explain Like I'm 5**: Giải thích đơn giản
- 🔑 **Extract Keywords**: Trích xuất từ khóa
- 💻 **Generate Python Code**: Tạo code Python

### Công nghệ sử dụng:
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **LLM**: Ollama (llama3.2)
- **Database**: Không sử dụng

---

## 💻 YÊU CẦU HỆ THỐNG

### Phần cứng tối thiểu:
- **CPU**: Intel Core i5 hoặc tương đương
- **RAM**: 8GB (khuyến nghị 16GB)
- **Ổ cứng**: 5GB trống (cho Ollama và model)
- **Kết nối**: Không cần internet (chạy offline)

### Phần mềm:
- **Hệ điều hành**: Windows 10/11
- **Python**: 3.8 trở lên
- **Ollama**: Phiên bản mới nhất
- **Trình duyệt**: Chrome, Firefox, hoặc Edge

---

## 🔧 CÁC BƯỚC CÀI ĐẶT

### BƯỚC 1: Cài đặt Python

1. Tải Python từ: https://www.python.org/downloads/
2. Chạy file cài đặt
3. ✅ **QUAN TRỌNG**: Tick vào "Add Python to PATH"
4. Click "Install Now"
5. Kiểm tra cài đặt:
   ```powershell
   python --version
   ```

### BƯỚC 2: Cài đặt Ollama

1. Truy cập: https://ollama.ai/download
2. Tải phiên bản Windows
3. Chạy file `OllamaSetup.exe`
4. Làm theo hướng dẫn cài đặt
5. Ollama sẽ tự động chạy sau khi cài đặt

### BƯỚC 3: Tải Model LLM

Mở PowerShell và chạy lệnh:
```powershell
ollama pull llama3.2
```

**Lưu ý**: Model llama3.2 có dung lượng khoảng 2GB, quá trình tải có thể mất vài phút tùy theo tốc độ internet.

Kiểm tra model đã tải:
```powershell
ollama list
```

Kết quả mong đợi:
```
NAME               ID              SIZE      MODIFIED
llama3.2:latest    xxxxx           2.0 GB    X minutes ago
```

### BƯỚC 4: Tạo Virtual Environment

1. Mở PowerShell
2. Di chuyển đến thư mục dự án:
   ```powershell
   cd d:\thacsiUTE\nlp\llm
   ```

3. Tạo virtual environment:
   ```powershell
   python -m venv venv
   ```

4. Kích hoạt virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   **Lưu ý**: Nếu gặp lỗi "cannot be loaded because running scripts is disabled", chạy:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Sau đó thử lại bước 4.

5. Xác nhận đã kích hoạt (sẽ thấy `(venv)` ở đầu dòng lệnh):
   ```
   (venv) PS D:\thacsiUTE\nlp\llm>
   ```

### BƯỚC 5: Cài đặt Dependencies

Với virtual environment đã kích hoạt, chạy:
```powershell
pip install -r requirements.txt
```

Các package sẽ được cài đặt:
- Flask==3.0.0
- python-dotenv==1.0.0
- requests==2.31.0

### BƯỚC 6: Cấu hình Environment Variables

File `.env` đã được tạo sẵn với cấu hình:
```
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

**Không cần chỉnh sửa gì thêm** nếu bạn sử dụng cấu hình mặc định.

---

## 🚀 CHẠY ỨNG DỤNG

### Các bước chạy:

1. **Mở PowerShell**

2. **Di chuyển đến thư mục dự án**:
   ```powershell
   cd d:\thacsiUTE\nlp\llm
   ```

3. **Kích hoạt virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. **Khởi động Flask server**:
   ```powershell
   python app.py
   ```

5. **Xác nhận server đang chạy**, bạn sẽ thấy:
   ```
   * Serving Flask app 'app'
   * Debug mode: on
   * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
   ```

6. **Mở trình duyệt** và truy cập:
   ```
   http://127.0.0.1:5000
   ```
   hoặc
   ```
   http://localhost:5000
   ```

### Dừng ứng dụng:
Nhấn `Ctrl + C` trong cửa sổ PowerShell để dừng server.

---

## 📱 SỬ DỤNG ỨNG DỤNG

### Giao diện chính:

1. **Ô nhập liệu**: Nhập văn bản cần xử lý
2. **5 nút chức năng**:
   - 📝 Summarize
   - 🇫🇷 Translate to French
   - 👶 Explain Like I'm 5
   - 🔑 Extract Keywords
   - 💻 Generate Python Code
3. **Ô kết quả**: Hiển thị kết quả từ LLM

### Cách sử dụng:

**Ví dụ 1: Tóm tắt văn bản**
1. Nhập văn bản vào ô input:
   ```
   Artificial intelligence is transforming healthcare. Machine learning 
   algorithms can detect diseases from medical images with high accuracy. 
   AI helps doctors make better treatment decisions.
   ```
2. Click nút **"📝 Summarize"**
3. Đợi vài giây
4. Xem kết quả tóm tắt

**Ví dụ 2: Tạo Python code**
1. Nhập mô tả:
   ```
   Create a function that calculates the factorial of a number
   ```
2. Click nút **"💻 Generate Python Code"**
3. Nhận code Python

**Ví dụ 3: Dịch sang tiếng Pháp**
1. Nhập văn bản tiếng Anh:
   ```
   Hello! How are you today?
   ```
2. Click nút **"🇫🇷 Translate to French"**
3. Nhận bản dịch tiếng Pháp

### Thời gian xử lý:
- Model chạy local trên máy
- Mỗi request mất khoảng 5-15 giây tùy độ phức tạp
- Không tốn phí API, hoàn toàn miễn phí

---

## 📁 CẤU TRÚC DỰ ÁN

```
llm/
│
├── app.py                      # Flask backend server
│   ├── Route '/'              # Trang chính
│   ├── Route '/process'       # Xử lý request từ user
│   └── Route '/health'        # Health check
│
├── templates/
│   └── index.html             # Giao diện web (HTML + CSS + JS)
│
├── venv/                      # Virtual environment (tự tạo)
│   ├── Scripts/
│   └── Lib/
│
├── .env                       # Cấu hình môi trường
├── .env.example              # Mẫu cấu hình
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── README.md                 # Tài liệu tổng quan
├── EXAMPLES.md               # Các ví dụ sử dụng
├── SETUP_GUIDE.md            # Hướng dẫn setup
└── INSTALLATION_GUIDE.md     # File này
```

### Giải thích các file chính:

**app.py**:
- Backend Flask server
- Xử lý HTTP requests
- Gọi Ollama API
- Trả về kết quả JSON

**templates/index.html**:
- Giao diện người dùng
- HTML structure
- CSS styling (gradient, animations)
- JavaScript (AJAX requests)

**requirements.txt**:
```
Flask==3.0.0          # Web framework
python-dotenv==1.0.0  # Load environment variables
requests==2.31.0      # HTTP library
```

**.env**:
```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

---

## 🛠️ KHẮC PHỤC SỰ CỐ

### Lỗi 1: "python is not recognized"
**Nguyên nhân**: Python chưa được thêm vào PATH

**Giải pháp**:
1. Gỡ cài đặt Python
2. Cài lại và tick "Add Python to PATH"
3. Hoặc thêm thủ công vào Environment Variables

### Lỗi 2: "ollama is not recognized"
**Nguyên nhân**: Ollama chưa cài đặt hoặc chưa có trong PATH

**Giải pháp**:
1. Cài đặt Ollama từ https://ollama.ai
2. Restart PowerShell
3. Hoặc restart máy tính

### Lỗi 3: "Scripts cannot be loaded"
**Nguyên nhân**: PowerShell chặn chạy scripts

**Giải pháp**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Lỗi 4: "Connection refused" khi gọi Ollama
**Nguyên nhân**: Ollama service chưa chạy

**Giải pháp**:
1. Mở Task Manager
2. Tìm "ollama" process
3. Nếu không có, chạy Ollama từ Start Menu
4. Hoặc chạy: `ollama serve`

### Lỗi 5: "Port 5000 already in use"
**Nguyên nhân**: Port 5000 đang được sử dụng

**Giải pháp**:
Sửa file `app.py`, dòng cuối:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Sau đó truy cập: http://localhost:5001

### Lỗi 6: Model trả về kết quả chậm
**Nguyên nhân**: Model lớn, máy yếu

**Giải pháp**:
Sử dụng model nhỏ hơn:
```powershell
ollama pull phi3
```
Sửa file `.env`:
```
OLLAMA_MODEL=phi3
```

### Lỗi 7: "ModuleNotFoundError"
**Nguyên nhân**: Chưa cài đặt dependencies

**Giải pháp**:
```powershell
pip install -r requirements.txt
```

---

## 📊 KIỂM TRA HỆ THỐNG

### Checklist trước khi chạy:

- [ ] Python đã cài đặt (kiểm tra: `python --version`)
- [ ] Ollama đã cài đặt (kiểm tra: `ollama --version`)
- [ ] Model llama3.2 đã tải (kiểm tra: `ollama list`)
- [ ] Virtual environment đã tạo (folder `venv` tồn tại)
- [ ] Virtual environment đã kích hoạt (thấy `(venv)` ở terminal)
- [ ] Dependencies đã cài đặt (chạy: `pip list`)
- [ ] File `.env` đã tồn tại và cấu hình đúng

### Test cơ bản:

1. **Test Ollama**:
   ```powershell
   ollama run llama3.2 "Hello, how are you?"
   ```
   Nếu thấy phản hồi → Ollama hoạt động ✅

2. **Test Flask**:
   ```powershell
   python app.py
   ```
   Nếu thấy "Running on http://127.0.0.1:5000" → Flask hoạt động ✅

3. **Test Web Interface**:
   - Mở http://localhost:5000
   - Nhập text: "Hello world"
   - Click "Summarize"
   - Nếu có kết quả → Ứng dụng hoạt động hoàn hảo ✅

---

## 📈 DEMO NHANH (5 PHÚT)

Để demo nhanh cho thầy:

### 1. Mở PowerShell:
```powershell
cd d:\thacsiUTE\nlp\llm
.\venv\Scripts\Activate.ps1
python app.py
```

### 2. Mở trình duyệt: http://localhost:5000

### 3. Demo 5 chức năng:

**Chức năng 1 - Summarize**:
```
Input: Artificial intelligence is transforming healthcare. Machine 
learning algorithms can detect diseases from medical images with high 
accuracy. AI helps doctors make better treatment decisions.
Output: [Tóm tắt ngắn gọn]
```

**Chức năng 2 - Translate to French**:
```
Input: Hello! How are you today?
Output: [Bản dịch tiếng Pháp]
```

**Chức năng 3 - Explain Like I'm 5**:
```
Input: Explain how the internet works
Output: [Giải thích đơn giản như cho trẻ 5 tuổi]
```

**Chức năng 4 - Extract Keywords**:
```
Input: Machine learning engineer position. Required: Python, 
TensorFlow, deep learning, data science. Location: San Francisco.
Output: [Danh sách keywords]
```

**Chức năng 5 - Generate Python Code**:
```
Input: Create a function that calculates factorial
Output: [Python code hoàn chỉnh]
```

---

## 🎯 KẾT LUẬN

Ứng dụng Multi-Purpose LLM Tool đã được cài đặt và cấu hình thành công với các đặc điểm:

### ✅ Ưu điểm:
- Chạy hoàn toàn offline, không cần internet
- Miễn phí 100%, không tốn phí API
- Giao diện đẹp, hiện đại, dễ sử dụng
- Hỗ trợ 5 chức năng xử lý văn bản khác nhau
- Sử dụng công nghệ LLM tiên tiến (llama3.2)
- Code rõ ràng, dễ bảo trì

### 📚 Tài liệu tham khảo:
- README.md: Tổng quan dự án
- EXAMPLES.md: Hơn 50 ví dụ sử dụng
- SETUP_GUIDE.md: Hướng dẫn setup chi tiết
- INSTALLATION_GUIDE.md: File này

### 👨‍💻 Thông tin kỹ thuật:
- **Framework**: Flask 3.0.0
- **LLM Provider**: Ollama
- **Model**: llama3.2 (2GB)
- **Language**: Python 3.12.8
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **API**: RESTful API

---

**Chúc bạn demo thành công! 🎉**

*Nếu có câu hỏi, vui lòng tham khảo file README.md hoặc EXAMPLES.md*
