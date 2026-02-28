import streamlit as st

# 1. CẤU HÌNH TRANG 
st.set_page_config(
    page_title="PhucKing® - Bộ Chuyển Đổi Số", 
    page_icon="🔢",
    initial_sidebar_state="expanded" # Tự động nhảy vào Sidebar
)
# 2. CSS TỔNG HỢP 
st.markdown(
    """
    <style>
    /* 1. Đổi màu chữ bạn NHẬP VÀO ô */
    .stTextInput input {
        color: #32cd32 !important; /* Màu xanh lá cây rực rỡ */
        font-weight: bold !important; /* Làm chữ đậm lên cho dễ nhìn */
        -webkit-text-fill-color: #32cd32 !important; /* Đảm bảo hiển thị trên mọi trình duyệt */
    }
    /* 1.Màu khung Card chính
    .main-card {
        background-color: rgba(0, 255, 0, 0.05); /* Nền xanh cực nhạt */
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #00ff00; /* Viền xanh lá đậm */
        box-shadow: 0 4px 15px rgba(0, 255, 0, 0.2);
        margin-bottom: 20px;
    }

    /* 2. Đổi màu tiêu đề H2 trong các Tab */
    h2 {
        color: #00ff00 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }

    /* 3. Đổi màu các ô nhập liệu */
    .stTextInput div[data-baseweb="input"] {
        border: 1px solid #00ff00 !important;
        background-color: rgba(0, 255, 0, 0.02) !important;
    }

    /* 4. Đổi màu Button */
    .stButton>button {
        background-color: #00ff00 !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: none !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #00cc00 !important; /* Xanh đậm hơn khi di chuột */
        box-shadow: 0 0 10px #00ff00;
    }

    /* 5. Ẩn các thành phần thừa GitHub */
    .viewerBadge_container__1QSob, .stDeployButton {
        display: none !important;
    }
    /* 1. HIỆN Header để giữ Menu 3 gạch nhưng làm Header trong suốt */
    header {
        visibility: visible !important;
        background-color: rgba(0,0,0,0) !important;
    }

    /* 2. ẨN TRIỆT ĐỂ dòng "Fork me on GitHub" và nút Deploy */
    .viewerBadge_container__1QSob, 
    .stDeployButton, 
    [data-testid="stActionButtonIcon"] {
        display: none !important;
    }

    /* 3. HIỆN Menu 3 gạch và ẩn các mục thừa bên trong */
    #MainMenu {visibility: visible !important;}
    
    /* 4. ẨN Footer "Made with Streamlit" */
    footer {visibility: hidden;
    }
    /* Hiện lại Header để hiện tiêu đề khi gửi link */
    header {visibility: visible !important;}
    
    /* Chỉ ẩn Footer và Menu Streamlit để web chuyên nghiệp hơn */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}

    /* Nền App tối và hình nền chuyên nghiệp */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    /* Nền App tối và hình nền chuyên nghiệp */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
     /* 2. Sửa lỗi Sidebar bị trắng: Ép Sidebar luôn có màu tối */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    /* Khung nội dung chính */
    .main .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }
        /* Màu chữ và bóng đổ */
    h1, h2, h3, p, span, label {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 3px black;
    }

    /* Tùy chỉnh ô nhập liệu */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #4CAF50 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HỆ THỐNG ỦNG HỘ PHUCKING® PREMIUM ---
with st.sidebar:
    st.divider()
    st.markdown("### ☕ Ủng hộ dự án")
    
    # Mức tiền gợi ý
    muc_donate = st.radio(
        "Chọn mức bạn muốn mời Phúc:",
        ["5.000 VNĐ", "10.000 VNĐ", "20.000 VNĐ", "Tùy tâm"],
        index=1
    )

    if st.button("Hiện mã QR Donate"):
        if muc_donate == "Tùy tâm":
            st.toast("Mọi sự ủng hộ từ bạn đều là động lực lớn cho Phúc! ❤️")
            loi_nhan = "Để xem tâm bạn như nào nha^^❤️!"
        else:
            st.toast(f"Cảm ơn bạn đã chọn mức {muc_donate}! 💖")
            loi_nhan = f"Vui lòng nhập đúng {muc_donate} khi quét mã ZaloPay/Ngân hàng"
        
        # Hiển thị ảnh QR
        st.image(
            "https://raw.githubusercontent.com/phuckingfco/bo-chuyen-doi-so_phucking-official/main/VCPank.jpg",
            caption=loi_nhan,
            use_container_width=True
        )
        
        st.info(f"Nội dung chuyển khoản: **PhucKing {muc_donate}**")


# 3. TIÊU ĐỀ & SIDEBAR 
st.title("🔢 Ứng dụng Chuyển đổi Hệ số")
st.sidebar.title("👑 Thương Hiệu")
st.sidebar.subheader("PhucKing® System")
st.sidebar.write("Chủ sở hữu: **Hoàng Phúc**")
st.sidebar.info("Phiên bản độc quyền 2026")

# 4. CHIA CÁC TAB
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔢 Chuyển đổi", 
    "📄 Văn bản", 
    "💡 Giải mã", 
    "➕ Cộng", 
    "➖ Trừ",
    "✖️ Nhân",
    "➕ Chia"
])
with tab1:
        st.header("Đổi Số/Chữ sang Nhị Phân")
        with st.container(border=True):
            du_lieu = st.text_input("Nhập vào số hoặc chữ:", key="input1", placeholder="Ví dụ: 36 hoặc Thanh Hoa")
            
            if du_lieu:
                if du_lieu.isdigit():
                    # --- TRƯỜNG HỢP NHẬP SỐ ---
                    so = int(du_lieu)
                    ket_qua = bin(so).replace('0b', '')
                    st.markdown(f"""
                        <div style="background-color: #2b2b2b; padding: 15px; border-radius: 10px; border: 1px solid #555; width: calc(100% + 2px); margin-left: -1px;">
                            <span style="color: #4CAF50; font-weight: bold;">🔢 Kết quả nhị phân:</span>
                            <code style="color: white; font-size: 20px;">{ket_qua}</code>
                        </div>
                    """, unsafe_allow_html=True)
                
                else:
                    # --- TRƯỜNG HỢP NHẬP CHỮ (XỬ LÝ DỮ LIỆU TRƯỚC) ---
                    # Bước 1: Tạo danh sách nhị phân 
                    danh_sach_nhi_phan = []
                    for ky_tu in du_lieu:
                        ma_np = format(ord(ky_tu), '08b')
                        danh_sach_nhi_phan.append(ma_np)

                   
                    # --- 1. CÀI ĐẶT GIAO DIỆN (Chỉnh ở đây để máy tự nhớ, không hiện chữ thừa) ---
                    DO_CAO = "0px"          # 0px là mỏng nhất, 2px là mỏng vừa
                    MAU_CHU = "white"       # Ép chữ mã nhị phân luôn màu trắng
                    KHOANG_CACH_KHUNG = "2px" # Khoảng cách giữa các dòng ký tự
                    
                    # --- 2. HIỂN THỊ TỪNG KÝ TỰ ---
                    st.info(f"Mã nhị phân từng ký tự của '{du_lieu}':")
                    for ky_tu, ma_np in zip(du_lieu, danh_sach_nhi_phan):
                        st.markdown(f"""
                            <div style="
                                background-color: #2b2b2b; 
                                padding: {DO_CAO} 12px; 
                                border-radius: 6px; 
                                border: 1px solid #444; 
                                margin-bottom: {KHOANG_CACH_KHUNG}; 
                                width: fit-content;
                                display: flex;
                                align-items: center;
                                gap: 10px;">
                                <span style="color: #4CAF50; font-weight: bold; font-size: 14px;">{ky_tu} :</span> 
                                <code style="
                                    color: {MAU_CHU} !important; 
                                    background: transparent; 
                                    border: none;
                                    font-size: 14px;
                                    font-family: monospace;">
                                    {ma_np}
                                </code>
                            </div>
                        """, unsafe_allow_html=True)

                    # --- 3. HIỂN THỊ NGUYÊN CÂU 
                    st.markdown("---")
                    ket_qua_nguyen_cau = " ".join(danh_sach_nhi_phan)
                    st.markdown(f"""
                        <div style="
                            background-color: #2b2b2b; 
                            padding: 10px 15px; 
                            border-radius: 10px; 
                            border: 1px solid #555;">
                            <span style="color: #4CAF50; font-weight: bold; font-size: 14px;">✨ Kết quả nguyên câu:</span>
                            <br>
                            <code style="
                                color: {MAU_CHU} !important; 
                                font-size: 16px; 
                                background: transparent;
                                word-break: break-all;">
                                {ket_qua_nguyen_cau}
                            </code>
                        </div>
                    """, unsafe_allow_html=True)


# --- TAB 2: NHỊ PHÂN SANG THẬP PHÂN ---
with tab2:
    st.header("Đổi Nhị Phân sang Thập Phân")
    with st.container(border=True):
        nhi_phan = st.text_input("Nhập mã nhị phân (0 và 1):", key="input2", placeholder="Ví dụ: 101010")
        if nhi_phan:
            try:
                # 1. Chuyển đổi
                so_thap_phan = int(nhi_phan, 2)
                
                # 2. Định dạng khoảng trắng giữa hàng nghìn (187 627 066)
                so_dinh_dang = "{:,}".format(so_thap_phan).replace(",", " ") 
                
                st.markdown("---")
                st.success("Đã xử lý xong!")
                # --- PHẦN HIỂN THỊ KẾT QUẢ DÀI BẰNG KHUNG XANH ---
                st.markdown(f"""
                    <div style="
                        background-color: #111111; 
                        padding: 15px 20px; 
                        border-radius: 8px; 
                        border: 1px solid #333;
                        margin-bottom: 10px;
                        /* Hai dòng dưới đây giúp bảng dài bằng khung xanh */
                        display: flex; 
                        justify-content: flex-start;
                        align-items: center;
                        gap: 15px;">
                        <span style="color: #4CAF50; font-size: 14px; font-weight: bold; white-space: nowrap;">🔢 Kết quả:</span>
                        <span style="color: white; font-size: 24px; font-family: sans-serif; font-weight: bold; word-break: break-all;">
                            {so_dinh_dang}
                        </span>
                    </div>
                """, unsafe_allow_html=True)
                
            
            except ValueError:
                st.error("⚠️ Chỉ nhập 0 và 1 thôi Phúc nhé!")
                
# --- TAB 3: NHỊ PHÂN SANG CHỮ CÁI ---
with tab3:
    st.header("Đổi Nhị Phân sang Chữ cái")
    with st.container(border=True):
        input_nhi_phan = st.text_input("Nhập dãy nhị phân (cách nhau bằng khoảng trắng):", 
                                        key="input3", 
                                        placeholder="Ví dụ: 01010100 01001000")
        
        if input_nhi_phan:
            try:
                # Chuyển đổi nguyên chuỗi
                danh_sach = input_nhi_phan.split()
                chu_ket_qua = "".join([chr(int(b, 2)) for b in danh_sach])
                
               
                 # Hiển thị kết quả nguyên câu
                st.success("✨ Chữ cái tương ứng là:")
                # Tạo khung đen bằng Markdown + HTML
                st.markdown(f"""
                    <div style="background-color: #1a1a1a; color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #333; font-family: monospace; font-size: 20px;">
                        {chu_ket_qua}
                    </div>
                    """, unsafe_allow_html=True)
                
            except Exception:
                st.error("⚠️ Lỗi: Dãy nhị phân không đúng định dạng hoặc chứa ký tự lạ!")

# --- TAB 4: CỘNG ---
with tab4:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("➕ Cộng hai số Nhị phân")
    col1, col2 = st.columns(2)
    with col1:
        bin1 = st.text_input("Nhập số nhị phân thứ nhất:", value="1010", key="add1")
    with col2:
        bin2 = st.text_input("Nhập số nhị phân thứ hai:", value="1100", key="add2")
    
    if st.button("Tính tổng", use_container_width=True):
        try:
            sum_dec = int(bin1, 2) + int(bin2, 2)
            sum_bin = bin(sum_dec)[2:]
            st.success(f"✅ Kết quả nhị phân: **{sum_bin}**")
            st.info(f"🔢 Giá trị thập phân: {sum_dec}")
        except ValueError:
            st.error("❌ Vui lòng chỉ nhập số 0 và 1!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 5: TRỪ ---
with tab5:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("➖ Trừ hai số Nhị phân")
    col1, col2 = st.columns(2)
    with col1:
        bin_sub1 = st.text_input("Nhập số bị trừ:", value="1111", key="sub1")
    with col2:
        bin_sub2 = st.text_input("Nhập số trừ:", value="1010", key="sub2")
    
    if st.button("Tính hiệu", use_container_width=True):
        try:
            val1, val2 = int(bin_sub1, 2), int(bin_sub2, 2)
            sub_dec = val1 - val2
            sub_bin = bin(sub_dec)[2:] if sub_dec >= 0 else "-" + bin(abs(sub_dec))[2:]
            st.success(f"✅ Kết quả nhị phân: **{sub_bin}**")
            st.info(f"🔢 Giá trị thập phân: {sub_dec}")
        except ValueError:
            st.error("❌ Vui lòng chỉ nhập số 0 và 1!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 6: NHÂN ---
with tab6:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("✖️ Nhân hai số Nhị phân")
    c1, c2 = st.columns(2)
    with c1:
        mul1 = st.text_input("Số thứ nhất:", value="101", key="mul1")
    with c2:
        mul2 = st.text_input("Số thứ hai:", value="11", key="mul2")
    
    if st.button("Tính tích", use_container_width=True):
        try:
            res_dec = int(mul1, 2) * int(mul2, 2)
            st.success(f"✅ Kết quả nhị phân: **{bin(res_dec)[2:]}**")
            st.info(f"🔢 Giá trị thập phân: {res_dec:,}")
        except ValueError:
            st.error("❌ Lỗi: Chỉ được nhập 0 và 1!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- TAB 7: CHIA ---
with tab7:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("➕ Chia hai số Nhị phân")
    d1, d2 = st.columns(2)
    with d1:
        div1 = st.text_input("Số bị chia:", value="1100", key="div1")
    with d2:
        div2 = st.text_input("Số chia:", value="10", key="div2")
    
    if st.button("Tính thương", use_container_width=True):
        try:
            v1, v2 = int(div1, 2), int(div2, 2)
            if v2 == 0: st.error("❌ Không thể chia cho số 0!")
            else:
                st.success(f"✅ Thương (nhị phân): **{bin(v1//v2)[2:]}**")
                if v1%v2 > 0: st.warning(f"🔸 Số dư (nhị phân): {bin(v1%v2)[2:]}")
        except ValueError:
            st.error("❌ Lỗi: Chỉ được nhập 0 và 1!")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. CHÂN TRANG ĐỘC QUYỀN
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <h3 style='color: #FFD700; text-shadow: 2px 2px 10px #FFD700;'>
            👑 PhucKing® Premium System 👑
        </h3>
        <p style='color: #4CAF50; font-weight: bold; letter-spacing: 2px;'>
            ALL RIGHTS RESERVED © 2026
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)




