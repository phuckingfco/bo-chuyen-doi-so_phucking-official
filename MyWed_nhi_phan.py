import streamlit as st

# 1. CẤU HÌNH TRANG
st.set_page_config(
    page_title="PhucKing® - Bộ Chuyển Đổi Số", 
    page_icon="🔢",
    menu_items={
        'Get Help': 'https://www.facebook.com/hoang.phuc.554411', # Link cá nhân
        'Report a bug': None,
        'About': "# 👑 PhucKing® Premium Edition\nBản quyền thuộc về Hoàng Phúc © 2026"
    }
)
# 2. CSS TỔNG HỢP
st.markdown(
    """
    <style>
    /* Ẩn Menu ba gạch, Footer Streamlit và dòng Fork GitHub */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob {display: none !important;}

    /* Nền App tối và hình nền chuyên nghiệp */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                    url("https://img.freepik.com/free-vector/abstract-binary-code-techno-background_1048-12836.jpg");
        background-size: cover;
        background-attachment: fixed;
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

# 3. TIÊU ĐỀ & SIDEBAR 
st.title("🔢 Ứng dụng Chuyển đổi Hệ số")
st.sidebar.title("👑 Thương Hiệu")
st.sidebar.subheader("PhucKing® System")
st.sidebar.write("Chủ sở hữu: **Hoàng Phúc**")
st.sidebar.info("Phiên bản độc quyền 2026")

# Nút Donate
with st.sidebar:
    st.divider()
    st.markdown("### ☕ Ủng hộ PhucKing®")
    
    # Nút bấm để hiện mã QR
    if st.button("Mời tác giả ly cà phê"):
        st.info("Cảm ơn bạn đã ủng hộ dự án!")
        
        # Link donate
        link_qr = "https://raw.githubusercontent.com/phuckingfco/bo-chuyen-doi-so_phucking-official/main/VCPank.jpg"
        
        st.image(link_qr, 
                 caption="Quét mã để mời Hoàng Phúc ly cà phê nha",
                 use_container_width=True)
        
        st.caption("Nội dung: [Ten cua ban] ung ho PhucKing")

# 4. CHIA CÁC TAB
tab1, tab2, tab3 = st.tabs(["➡️ Sang Nhị Phân", "⬅️ Sang Thập Phân", "🔠 Sang Chữ Cái"])

with tab1:
    st.header("Đổi sang Nhị Phân")
    du_lieu = st.text_input("Nhập vào số hoặc chữ:", key="input1")
    if du_lieu:
        if du_lieu.isdigit():
            ket_qua = bin(int(du_lieu)).replace('0b', '')
            st.markdown(f"<div style='background:#111; padding:15px; border-radius:10px; border:1px solid #4CAF50;'>Kết quả: {ket_qua}</div>", unsafe_allow_html=True)
        else:
            for ky_tu in du_lieu:
                ma_np = format(ord(ky_tu), '08b')
                st.write(f"**{ky_tu}** : `{ma_np}`")

with tab2:
    st.header("Đổi sang Thập Phân")
    nhi_phan = st.text_input("Nhập mã nhị phân:", key="input2")
    if nhi_phan:
        try:
            so_thap_phan = int(nhi_phan, 2)
            st.markdown(f"<div style='background:#111; color:#00FF00; padding:15px; border-radius:10px; border:1px solid #333; font-size:24px;'>{so_thap_phan:,}</div>", unsafe_allow_html=True)
        except:
            st.error("Chỉ nhập 0 và 1!")

with tab3:
    st.header("Đổi sang Chữ cái")
    input_nhi_phan = st.text_input("Nhập dãy nhị phân:", key="input3")
    if input_nhi_phan:
        try:
            danh_sach = input_nhi_phan.split()
            chu_ket_qua = "".join([chr(int(b, 2)) for b in danh_sach])
            st.success("Kết quả:")
            st.markdown(f"""
                <div style="background-color: #1a1a1a; color: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #4CAF50; font-family: monospace; font-size: 20px; width: 100%;">
                    {chu_ket_qua}
                </div>
            """, unsafe_allow_html=True)
        except:
            st.error("Lỗi định dạng!")

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






