import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar with option menu
with st.sidebar:
    selected = option_menu(
        menu_title="Data Planet",
        options=["📊 Projects", "📁 Folders", "📝 Template", "🔍 Data", "📱 Apps"],
        default_index=0,
    )

# Main content based on selected option
if selected == "📊 Projects":
    st.title("")
elif selected == "📁 Folders":
    st.title("")
elif selected == "📝 Template":
    st.title("")
elif selected == "🔍 Data":
    st.title("")
elif selected == "📱 Apps":
    st.title("")

# Navbar
import streamlit as st

# Navbar
nav_items = {
    "Partners": "/Partners",
    "shared": "/shared",
    "operations": "/operations",
    "Account": "/Account",
    "Message": "/Message",
    "profile": "/profile",
    "open": "/open",
}

navbar_template = """
    <style>
        .navbar {
            background-color: #2C3E50;
            overflow: hidden;
            display: flex;
            justify-content: flex-start;
            align-items: center;
        }

        .navbar a {
            color: #f2f2f2;
            text-align: center;
            text-decoration: none;
            font-size: 17px;
            padding: 14px 20px;
            margin-right: 20px; /* Add margin to the right side of each link */
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
    </style>
    <div class="navbar">
        %s
    </div>
"""

# Define the URL for the new file or section for Partners
partners_url = "pathner.py"  # Replace with the actual URL of the new file

# Add onclick event to the "Partners" link to open the new file
nav_links = ''.join(f'<a href="{partners_url}">{label}</a>' if label != "Partners" else f'<a href="{partners_url}" onclick="location.href=this.href+\'?selected={label}\';return false;">{label}</a>' for label, url in nav_items.items())
st.markdown(navbar_template % nav_links, unsafe_allow_html=True)

# Footer
footer_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #09ab3b ;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        <p>This is a Streamlit footer</p>
    </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

