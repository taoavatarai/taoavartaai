# 📋 WORKFLOW — AvatarAI Spatial

> Cập nhật lần cuối: 2026-06-14  
> Trạng thái tổng thể: 🟡 Prototype UI hoàn chỉnh — Chưa có AI thật

---

## ✅ ĐÃ HOÀN THÀNH

### 1. Hạ tầng & Môi trường
- [x] Import dự án lên Replit
- [x] Cài đặt Python 3.11
- [x] Tạo `serve.py` — HTTP server phục vụ file HTML tĩnh tại port 5000
- [x] Cấu hình workflow `Start application` (port 5000, webview)
- [x] Cấu hình deployment target: `static`
- [x] Ứng dụng chạy ổn định, preview hoạt động

### 2. Giao diện (Frontend)
- [x] Layout 3 cột: Left Panel / Main Canvas / Right Panel
- [x] Top bar: logo, trạng thái model, credits
- [x] Left panel: ô nhập prompt, quick tags, chọn style (6 kiểu), sliders thông số
- [x] Main panel: hologram canvas, animation scanline, vòng orbit
- [x] Right panel: character presets (6 nhân vật), seed input, thông tin metadata
- [x] Bottom bar: lịch sử generation (history reel)
- [x] Hiệu ứng: glassmorphism, gradient vàng/đen, animation CSS
- [x] Nút "Tạo Avatar" với thanh tiến trình giả lập
- [x] Nút Download PNG, nút Save

### 3. Logic Canvas (Giả lập AI)
- [x] Vẽ nhân vật bằng HTML5 Canvas API (không dùng AI thật)
- [x] 6 bảng màu theo style: Anime, Realistic, Cyberpunk, Fantasy, Oil Paint, Pixel Art
- [x] Animation denoising giả lập (~3.5 giây)
- [x] Session history lưu thumbnail tạm thời

---

## 🔄 ĐANG LÀM / CẦN LÀM TIẾP

### Ưu tiên cao 🔴

- [ ] **Tích hợp AI thật** — Kết nối API sinh ảnh thực (Stable Diffusion / DALL-E / Replicate)
  - Prompt hiện không ảnh hưởng kết quả
  - Cần: API key, backend endpoint, xử lý response base64/URL
  - File cần tạo: `api_handler.py` hoặc gọi từ JS fetch()

- [ ] **Backend API server** — Tách logic server ra riêng
  - Hiện tại chỉ có HTTP server tĩnh
  - Cần: Flask/FastAPI để xử lý request sinh ảnh
  - Port backend: 8000 (không trùng frontend 5000)

### Ưu tiên trung bình 🟡

- [ ] **Lưu trữ lịch sử** — Hiện mất khi refresh
  - Cần: Database (SQLite / Replit DB) hoặc localStorage
  - Lưu: prompt, style, seed, ảnh thumbnail, timestamp

- [ ] **Các slider hoạt động thật**
  - CFG Scale, Detail Quality, Style Strength hiện là UI placeholder
  - Cần truyền giá trị vào lúc gọi API

- [ ] **Tính năng Download** thực sự
  - Hiện download canvas procedural
  - Cần: download ảnh AI thật khi có API

- [ ] **Seed reproducibility** — Nhập cùng seed + prompt → ra cùng ảnh
  - Cần truyền seed vào API call

### Ưu tiên thấp 🟢

- [ ] **Responsive / Mobile** — Giao diện chưa tối ưu trên màn hình nhỏ
- [ ] **Đa ngôn ngữ** — Hiện dùng tiếng Việt, có thể thêm toggle EN/VI
- [ ] **Dark/Light mode** toggle
- [ ] **Tính năng chia sẻ** — Share URL với tham số seed + prompt
- [ ] **Hệ thống credits thật** — Hiện là con số fake (248 credits)
- [ ] **Aspect ratio** thực sự ảnh hưởng kích thước output

---

## ❌ CÒN THIẾU (Phân tích kỹ thuật)

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| AI image generation | ❌ Không có | Chỉ vẽ tay bằng Canvas |
| Backend API | ❌ Không có | Chỉ có static HTTP server |
| Database | ❌ Không có | Lịch sử mất khi refresh |
| Authentication | ❌ Không có | Không có user/login |
| API key management | ❌ Không có | Cần khi tích hợp AI |
| Error handling | ⚠️ Một phần | Chưa xử lý lỗi API |
| Loading states | ✅ Có | Animation giả lập tốt |
| Input validation | ⚠️ Một phần | Prompt limit 500 ký tự |
| Mobile responsive | ⚠️ Yếu | Layout cứng 3 cột |
| Tests | ❌ Không có | Chưa có test nào |

---

## 📁 CẤU TRÚC FILE HIỆN TẠI

```
/
├── avatar_ai_spatial.html   ← Toàn bộ frontend (HTML + CSS + JS, ~1200 dòng)
├── serve.py                 ← Python HTTP server đơn giản
├── WORKFLOW.md              ← File này (cập nhật thủ công/tự động)
└── .replit                  ← Cấu hình Replit
```

### Cấu trúc đề xuất khi mở rộng
```
/
├── index.html               ← Tách HTML thuần
├── static/
│   ├── style.css            ← Tách CSS
│   └── app.js               ← Tách JavaScript
├── backend/
│   ├── app.py               ← Flask/FastAPI server
│   └── ai_handler.py        ← Logic gọi AI API
├── serve.py                 ← Dev server (giữ nguyên)
└── WORKFLOW.md
```

---

## 🚀 LỘ TRÌNH ĐỀ XUẤT

```
Giai đoạn 1 (Hiện tại)   → UI Prototype hoàn chỉnh ✅
Giai đoạn 2 (Tiếp theo)  → Tích hợp AI API thật
Giai đoạn 3              → Thêm database lưu lịch sử
Giai đoạn 4              → Authentication + Credits thật
Giai đoạn 5              → Deploy production + Custom domain
```

---

*File này được cập nhật mỗi khi có thay đổi lớn trong dự án.*
