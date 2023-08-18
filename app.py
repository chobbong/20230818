import streamlit as st


# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query("SELECT `매매대금_평균` FROM estate_data WHERE 시군구='충청북도 충주시 호암동-221' AND 단지명='호암리버빌(1단지)';", ttl=600)


# Print results.
for row in df.itertuples():
    st.write(row)

