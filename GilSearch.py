import streamlit as st
import pandas as pd

# Dummy data
hospitals_data = pd.DataFrame({
    'Hospital Name': ['City Hospital', 'Regional Medical Center', 'National Health Clinic'],
    'Location': ['Lagos, Nigeria', 'Accra, Ghana', 'Nairobi, Kenya'],
    'Services': [
        'Emergency Care, Surgery, Maternity',
        'Pediatrics, Radiology, Oncology',
        'Cardiology, Orthopedics, Maternity'
    ],
    'Cost Estimate': [
        'Low, Medium, High',
        'Medium, High, Medium',
        'High, Medium, Low'
    ],
    'Contact Info': [
        '123-456-7890, cityhospital@example.com',
        '987-654-3210, regionalmed@example.com',
        '555-123-4567, nationalclinic@example.com'
    ]
})

# Homepage
def homepage():
    st.title("Hospital Finder - Africa")
    st.write("Search for hospitals, view services, and compare costs.")

    search_query = st.text_input("Search by Hospital Name, Location, or Service")

    if search_query:
        results = hospitals_data[hospitals_data.apply(lambda row: search_query.lower() in row.astype(str).str.lower().to_list(), axis=1)]
        if not results.empty:
            st.write("Search Results:")
            for index, row in results.iterrows():
                st.write(f"**{row['Hospital Name']}** - {row['Location']}")
                st.write(f"Services: {row['Services']}")
                st.write(f"Cost Estimate: {row['Cost Estimate']}")
                st.write(f"Contact: {row['Contact Info']}")
                st.write("------")
        else:
            st.write("No results found. Please try another search term.")
    else:
        st.write("Use the search bar above to find hospitals.")

# Hospital Profile Page
def hospital_profile(hospital_name):
    hospital = hospitals_data[hospitals_data['Hospital Name'] == hospital_name].iloc[0]
    st.title(hospital_name)
    st.write(f"**Location:** {hospital['Location']}")
    st.write(f"**Services Offered:** {hospital['Services']}")
    st.write(f"**Cost Estimate:** {hospital['Cost Estimate']}")
    st.write(f"**Contact Info:** {hospital['Contact Info']}")
    st.write("**Patient Reviews:**")
    st.write("This feature will allow users to leave reviews and ratings.")

# Main App Navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "View Hospital"])

    if page == "Home":
        homepage()
    elif page == "View Hospital":
        hospital_name = st.sidebar.selectbox("Select Hospital", hospitals_data['Hospital Name'])
        hospital_profile(hospital_name)

if __name__ == "__main__":
    main()
