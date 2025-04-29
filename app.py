
import streamlit as st
import pandas as pd

# تحميل البيانات من ملف Excel
@st.cache_data
def load_data():
    df = pd.read_excel("تقرير العهد 1000.xlsx", sheet_name="Sheet1", skiprows=2)
    df.columns = ['Employee Name', 'Asset Description', 'Tag Number', 'Current Location']
    df = df.dropna(subset=['Tag Number'])
    df['Tag Number'] = df['Tag Number'].astype(str).str.strip()
    return df

data = load_data()

# واجهة المستخدم
st.title("📋 برنامج استعلام عن العهد")

tag_input = st.text_input("أدخل رقم الجهاز (Tag Number):")

if tag_input:
    result = data[data['Tag Number'] == tag_input.strip()]
    
    if not result.empty:
        for idx, row in result.iterrows():
            st.success("✅ تم العثور على الجهاز")
            st.write("**اسم الموظف:**", row['Employee Name'] if pd.notna(row['Employee Name']) else "غير محدد")
            st.write("**وصف الجهاز:**", row['Asset Description'])
            st.write("**الموقع الحالي:**", row['Current Location'])
    else:
        st.error("❌ لم يتم العثور على الجهاز بهذا الرقم.")
