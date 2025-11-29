import streamlit as st

# Bước 1: Thiết lập trang web và cấu trúc trang web gồm 5 cột
st.set_page_config(
    page_title='Trắc nghiệm tính cách', 
    page_icon=':question:', 
    layout='wide'
)
st.title('Hãy chọn một con vật bạn yêu thích')
col1, col2, col3, col4, col5 = st.columns(5) # Chia 5 cột



# Bước 2: Tạo 1 dictionary với khóa là con vật và giá trị là câu trả lời tương ứng
Personality = {
    'Con mèo': 'Lựa chọn này cho thấy bạn chưa sẵn sàng bắt đầu công việc, bạn khao khát được đi nghỉ.',
    'Con chó': 'Bạn cảm nhận được sự hỗ trợ nhiệt tình của bạn bè và vì thế nên sẵn sàng giải quyết mọi vấn đề xảy ra.',
    'Con sư tử': 'Có thể thấy bạn là người có vẻ ngoài nổi bật. Bạn thu hút mọi người bằng vẻ hào nhoáng,',
    'Con ngựa': 'Có điều gì đó đang hạn chế sự tự do của bạn.',
    'Thiên nga': 'Hiện tại bạn có khoảng thời gian ngọt ngào, hãy cố gắng tận hưởng và kéo dài nó nhé.'
}

---

# Bước 3: Tạo button ở từng cột
# Sử dụng 'with' để đặt button vào từng cột
with col1:
    b1 = st.button('Con mèo')
with col2:
    b2 = st.button('Con chó')
with col3:
    b3 = st.button('Con sư tử')
with col4:
    b4 = st.button('Con ngựa')
with col5:
    b5 = st.button('Thiên nga')

---

# Bước 4: Tạo hộp mở rộng tương ứng với button được bấm
# Sử dụng 'if' để kiểm tra button nào được bấm và hiển thị st.expander() tương ứng
if b1:
    with st.expander('Con mèo'):
        st.write(Personality['Con mèo'])
if b2:
    with st.expander('Con chó'):
        st.write(Personality['Con chó'])
if b3:
    with st.expander('Con sư tử'):
        st.write(Personality['Con sư tử'])
if b4:
    with st.expander('Con ngựa'):
        st.write(Personality['Con ngựa'])
if b5:
    with st.expander('Thiên nga'):
        st.write(Personality['Thiên nga'])

---

# Bước 5: In ra thanh bên con vật mà người dùng chọn
# Sử dụng 'with st.sidebar' để hiển thị kết quả ở thanh bên
with st.sidebar:
    st.title('Trắc nghiệm tính cách')
    if b1:
        st.write('Con vật bạn chọn là con mèo')
    if b2:
        st.write('Con vật bạn chọn là con chó')
    if b3:
        st.write('Con vật bạn chọn là con sư tử')
    if b4:
        st.write('Con vật bạn chọn là con ngựa')
    if b5:
        st.write('Con vật bạn chọn là thiên nga')