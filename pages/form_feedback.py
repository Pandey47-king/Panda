import streamlit as st

st.title("📚 Book Store with Payment")

# Define books with prices
books = {
    "Bhagavad Gita": {"desc": "A sacred Hindu scripture.", "price": 639},
    "Ramayan": {"desc": "Story of Lord Rama.", "price": 802},
    "Ramcharitmanas": {"desc": "Written by Tulsidas.", "price": 495[]},
    "On the Way of Krishna": {"desc": "Spiritual teachings.", "price": 179}
}

# Select book
selected_book = st.selectbox("📖 Select a Book", list(books.keys()))

# Show details
st.subheader("📌 Book Details")
st.write("Description:", books[selected_book]["desc"])
st.write("Price: ₹", books[selected_book]["price"])

# Payment Section
st.subheader("💳 Payment Section")

name = st.text_input("Enter your name")
payment_method = st.selectbox("Select Payment Method", ["UPI", "Card", "Cash on Delivery"])

# Simulate payment
if st.button("Pay Now"):
    if name == "":
        st.error("❌ Please enter your name")
    else:
        st.success(f"✅ Payment Successful!\n\nThank you {name} for purchasing '{selected_book}'")
        st.balloons()
