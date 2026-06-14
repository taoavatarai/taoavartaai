# 📋 WORKFLOW — AvatarAI Spatial

> Cập nhật lần cuối: 2026-06-14  
> Trạng thái tổng thể: 🟢 AI thật + Lịch sử + Sliders hoạt động — Pollinations.ai (Flux model)

---

## ✅ ĐÃ HOÀN THÀNH

### 1. Hạ tầng & Môi trường
- [x] Import dự án lên Replit
- [x] Cài đặt Python 3.11
- [x] Cài đặt Flask + Requests
- [x] `serve.py` → Flask app phục vụ frontend + API tại port 5000
- [x] Cấu hình workflow `Start application` (port 5000, webview)
- [x] Cấu hình deployment target: `static` → nâng lên `autoscale` (có backend)
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

### 3. AI Tích Hợp Thật ✨ MỚI
- [x] Backend Flask endpoint `/api/generate`
- [x] Kết nối **Pollinations.ai** (model Flux) — miễn phí, không cần API key
- [x] Style prompt modifiers: 6 kiểu (Anime, Realistic, Cyberpunk, Fantasy, Oil Paint, Pixel Art)
- [x] Quality suffix tự động thêm vào mọi prompt
- [x] Seed reproducibility — cùng seed + prompt → cùng ảnh
- [x] Animation thông minh: chạy đến 88%, giữ ở "Chờ server AI..." cho đến khi có kết quả
- [x] Khi AI trả về: vẽ ảnh thật lên canvas, finalize
- [x] Fallback: nếu AI lỗi → hiển thị canvas vẽ tay như cũ (không crash)
- [x] Prompt rỗng → tự dùng prompt mặc định
- [x] AI image hiển thị qua `<img>` overlay (tránh canvas CORS taint)

### 4. Lịch Sử Bền Vững (localStorage)
- [x] Lưu tối đa 40 ảnh vào `localStorage` (key: `avatarAI_history`)
- [x] Mỗi item lưu: prompt, style, seed, width, height, timestamp, thumbnail URL
- [x] Tải lại lịch sử khi refresh trang (không mất dữ liệu)
- [x] Hover thumbnail → tooltip hiển thị style, prompt, seed, ngày giờ
- [x] Nút "↩ Khôi phục cài đặt" trong tooltip → restore prompt + style + seed
- [x] Nút "×" xóa từng ảnh / "Xóa tất cả" / badge đếm số ảnh

### 5. Sliders Hoạt Động Thật ✨ MỚI
- [x] **Chất lượng chi tiết (1-10)** → prompt keywords: rough sketch / detailed / ultra detailed / hyper detailed
- [x] **CFG Scale (1.0-20.0)** → mức độ "literal": loose dreamlike / balanced / extremely literal
- [x] **Sức mạnh phong cách (0.00-1.00)** → style intensity: subtle hints / moderate / bold / extreme
- [x] **Độ sáng** → CSS `brightness()` realtime trên ảnh (không cần regenerate)
- [x] **Độ bão hòa** → CSS `saturate()` realtime trên ảnh (không cần regenerate)

### ~~4. Lịch Sử Bền Vững (localStorage) ✨ MỚI~~
- [x] Lưu tối đa 40 ảnh vào `localStorage` (key: `avatarAI_history`)
- [x] Mỗi item lưu: prompt, style, seed, width, height, timestamp, thumbnail URL
- [x] Tải lại lịch sử khi refresh trang (không mất dữ liệu)
- [x] Hover thumbnail → tooltip hiển thị style, prompt, seed, ngày giờ
- [x] Nút "↩ Khôi phục cài đặt" trong tooltip → restore prompt + style + seed
- [x] Nút "×" xóa từng ảnh khỏi lịch sử
- [x] Nút "Xóa tất cả" ở góc dưới phải
- [x] Badge đếm số ảnh trong lịch sử (cạnh chữ "Lịch sử")

---

## 🔄 CẦN LÀM TIẾP

### Ưu tiên cao 🔴

- [ ] **Update deployment config** — Hiện vẫn là `static`, cần đổi sang `autoscale` vì có Flask backend
  - File: `.replit` → thêm `[deployment]` section với run command gunicorn

### Ưu tiên trung bình 🟡

- [x] ~~**Các slider hoạt động thật**~~ ✅ Hoàn thành — xem mục 5 bên dưới

- [ ] **Cài Gunicorn** cho production deploy
  - Dev server Flask không phù hợp production

- [ ] **Model status** trên topbar hiển thị model thật (Flux thay vì SD-XL Turbo)

- [ ] **Error toast** khi AI thất bại (hiện chỉ log console)

### Ưu tiên thấp 🟢

- [ ] **Responsive / Mobile** — Giao diện chưa tối ưu trên màn hình nhỏ
- [ ] **Đa ngôn ngữ** — Toggle EN/VI
- [ ] **Tính năng chia sẻ** — Share URL với seed + prompt
- [ ] **Hệ thống credits thật** — Tích hợp auth + thanh toán
- [ ] **Negative prompt UI** — Ô nhập riêng cho negative prompt

---

## ❌ CÒN THIẾU (Phân tích kỹ thuật)

| Hạng mục | Trạng thái | Ghi chú |
|---|---|---|
| AI image generation | ✅ Có | Pollinations.ai / Flux model |
| Backend API | ✅ Có | Flask server (tĩnh + route) |
| Lịch sử bền vững | ✅ Có | localStorage, tối đa 40 items |
| Slider params ảnh hưởng thật | ❌ Không | CFG/Detail là placeholder |
| Authentication | ❌ Không | Không có user/login |
| Gunicorn production server | ❌ Không | Dùng Flask dev server |
| Error handling UI | ⚠️ Có fallback | Lỗi chỉ log console |
| Mobile responsive | ⚠️ Yếu | Layout cứng 3 cột |
| Tests | ❌ Không | Chưa có test nào |

---

## 📁 CẤU TRÚC FILE HIỆN TẠI

```
/
├── avatar_ai_spatial.html   ← Frontend (HTML + CSS + JS tích hợp AI)
├── serve.py                 ← Flask server: trang web + /api/generate
├── requirements.txt         ← flask, requests (tự sinh bởi pip)
├── WORKFLOW.md              ← File này
└── .replit                  ← Cấu hình Replit
```

### Cấu trúc đề xuất khi mở rộng thêm
```
/
├── avatar_ai_spatial.html
├── serve.py                 ← hoặc tách ra backend/app.py
├── static/                  ← nếu có thêm assets
└── WORKFLOW.md
```

---

## 🚀 LỘ TRÌNH

```
Giai đoạn 1 ✅   UI Prototype hoàn chỉnh
Giai đoạn 2 ✅   Tích hợp AI API thật (Pollinations.ai / Flux)
Giai đoạn 3 ✅   Lịch sử bền vững (localStorage, 40 items, restore settings)
Giai đoạn 4 🔜   Slider params thật + Deploy production (Gunicorn + autoscale)
Giai đoạn 5       Authentication + Credits thật
```

---

*File này được cập nhật mỗi khi có thay đổi lớn trong dự án.*
