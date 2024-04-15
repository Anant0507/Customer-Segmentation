# import streamlit as st
# import streamlit.components.v1 as components  # Import Streamlit

# with open('Customer_WebPage.html', 'r') as file:
#     html_content = file.read()
# # Render the HTML
# components.html(html_content, height=600)
import streamlit as st
import pickle as pkl
import pandas as pd
from streamlit_card import card
from sklearn.preprocessing import StandardScaler
def predict_cluster(X_data : pd.DataFrame):
    with open("C:\src\Project\Final_Project\customer_classification_model.pkl","rb") as f:
        model = pkl.load(f)
        return model.predict(X_data)

def set_page(page):
    st.session_state.page = page

def input_fields():
    
    st.title("Customer Classification Model")
    kidhome = 0
    teenhome = 0
    selector = ["Select","Yes","No"]
    maritial_status = ["Select","Married","Single"]

    is_parent = st.selectbox("Are you a Parent?", selector)
    is_married = st.selectbox("What is your maritial Status",maritial_status)
    if is_parent == "Yes":
        teenhome = st.number_input("Do you have any teenager?", min_value=0, max_value=5, step=1,format="%d")
        kidhome = st.number_input("Do you have any kid?", min_value=0, max_value=5, step=1,format="%d")

    age = st.number_input("Enter your age", min_value=0, max_value=90, step=1,format="%d")

    income = st.number_input("Enter Income:")
    
    family_size = kidhome + teenhome + 2 if is_married == "Married" else kidhome + teenhome + 1

    spent = st.number_input("Enter Total Spent Amount:")

    is_parent = 0 if is_parent == "No" else 1

    data = [[is_parent,income,teenhome,kidhome,age,family_size,spent]]

    X_data = pd.DataFrame(data,columns=["Is_Parent","Income","Teenhome","Kidhome","Age","Family_Member_Count","Spent"])
    
    st.session_state["Input_Data"] = X_data
    st.button('Submit', on_click=set_page, args=["Display Data"])  
        

def show_result():
        st.title("Result")
        if "Input_Data" in st.session_state:
            insights = {
                0:["Insight 1 for Class 0","Insight 2 for class 0"],
                1:["Insight 1 for Class 1","Insight 2 for class 1"],
                2:["Insight 1 for Class 2","Insight 2 for class 2"],
                3:["Insight 1 for Class 3","Insight 2 for class 3"],
            }
            X_data = st.session_state["Input_Data"]
            st.write(X_data)

            # scaler = StandardScaler()
            # Scaled_X_data = pd.DataFrame(scaler.fit_transform(X_data),columns = X_data.columns)

            # label = predict_cluster(X_data=Scaled_X_data)
            label = predict_cluster(X_data=X_data)
            label_no = label[0].item()
            st.write(f"Cluster:{label[0]}")
            insights_new = insights[label_no]
            # with st.expander("Business Insights",expanded=True):
            #     st.write(insights_new)
            # res = card(
            #     title="Personality Analysis",
            #     text=insights[label[0].item()],
            #     styles={
            #         "card": {
            #             "width": "100%",
            #             "height": "100px",
            #             "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            #         },
            #         "text": {
            #             "font-family": "serif",
            #         }
            #     }
            # )
            col1 = st.columns(1)
            col1[0].header("Personality Analysis")
            col1[0].text(insights[label[0].item()])
        else:
            st.write("Data not received")
        
        st.button('Home', on_click=set_page, args=["Input Data"])

def main():
    if 'page' not in st.session_state:
        st.session_state.page = 'Input Data'

    if st.session_state.page == 'Input Data':
        input_fields()
    elif st.session_state.page == 'Display Data':
        show_result ()
if __name__ == "__main__":
    main()
