import streamlit as st
import json

st.set_page_config(
    page_title="AI App Compiler",
    layout="wide"
)

st.title("🚀 AI Generated Application")

try:

    with open(
        "output/generated_schema.json",
        "r",
        encoding="utf-8"
    ) as f:

        schema = json.load(f)

    pages = schema["ui_schema"]["pages"]

    page_names = []

    for page in pages:
        page_names.append(page["name"])

    selected_page = st.sidebar.selectbox(
        "Navigation",
        page_names
    )

    st.header(selected_page)

    for page in pages:

        if page["name"] == selected_page:

            if "components" in page:

                for component in page["components"]:

                    comp = component.lower()

                    # Login Components

                    if "email" in comp:

                        st.text_input("Email")

                    elif "password" in comp:

                        st.text_input(
                            "Password",
                            type="password"
                        )

                    elif "loginbutton" in comp:

                        st.button("Login")

                    # Search

                    elif "search" in comp:

                        st.text_input("Search")

                    # Contacts

                    elif "contactlist" in comp:

                        st.dataframe([
                            {
                                "Name": "John",
                                "Email": "john@test.com"
                            },
                            {
                                "Name": "Mary",
                                "Email": "mary@test.com"
                            }
                        ])

                    elif "addcontactbutton" in comp:

                        st.button("Add Contact")

                    # Payments

                    elif "paymenthistory" in comp:

                        st.table([
                            {
                                "Amount": 1000,
                                "Status": "Paid"
                            },
                            {
                                "Amount": 500,
                                "Status": "Pending"
                            }
                        ])

                    elif "newpaymentform" in comp:

                        st.number_input(
                            "Amount",
                            min_value=0
                        )

                        st.button("Submit Payment")

                    # Dashboard

                    elif "statsoverview" in comp:

                        col1, col2, col3 = st.columns(3)

                        col1.metric(
                            "Contacts",
                            "120"
                        )

                        col2.metric(
                            "Payments",
                            "₹50,000"
                        )

                        col3.metric(
                            "Users",
                            "35"
                        )

                    elif "recentactivity" in comp:

                        st.write(
                            "Recent activity feed"
                        )

                    elif "quickactions" in comp:

                        st.button("New Contact")
                        st.button("New Payment")

                    # Default

                    else:

                        st.write(component)

except Exception as e:

    st.error(str(e))