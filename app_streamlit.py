# import streamlit as st
# import streamlit.components.v1 as components  # Import Streamlit

# with open('Customer_WebPage.html', 'r') as file:
#     html_content = file.read()
# # Render the HTML
# components.html(html_content, height=600)
import streamlit as st
import pickle as pkl
import pandas as pd

def predict_cluster(X_data : pd.DataFrame):
    with open("C:\src\Project\Final_Project\customer_classification_model.pkl","rb") as f:
        model = pkl.load(f)
        return model.predict(X_data)
    
def input_fields():
    st.title("Customer Classification Model")
    is_submitted = False
    kidhome = 0
    teenhome = 0
    if not is_submitted:
        # Define a list of fruits
        selector = ["Select","Yes","No"]
        maritial_status = ["Select","Married","Single"]
        # Create a dropdown button to select a fruit
        is_parent = st.selectbox("Are you a Parent?", selector)
        is_married = st.selectbox("What is your maritial Status",maritial_status)
        if is_parent == "Yes":
            teenhome = st.number_input("Do you have any teenager?", min_value=0, max_value=5, step=1,format="%d")
            kidhome = st.number_input("Do you have any kid?", min_value=0, max_value=5, step=1,format="%d")

        age = st.number_input("Enter your age", min_value=0, max_value=90, step=1,format="%d")

        income = st.number_input("Enter Income:")
        if is_parent == "Yes":
            teenhome = st.number_input("Do you have any teenager?", min_value=0, max_value=5, step=1,format="%d")
            kidhome = st.number_input("Do you have any kid?", min_value=0, max_value=5, step=1,format="%d")

        family_size = kidhome + teenhome + 2 if is_married == "Married" else kidhome + teenhome + 1

        is_parent = 0 if is_parent == "No" else 1

        data = [[is_parent,income,teenhome,kidhome,age,family_size]]

        X_data = pd.DataFrame(data,columns=["Is_Parent","Income","Teenhome","Kidhome","Age","Family_Member_Count"])
    
        # is_submitted = st.button("Submit")   
        if st.button("Submit"):
            st.session_state["Input_Data"] = X_data
            st.session_state.page = "Display Data"  

def show_result():
        st.title("Result")
        if "input_data" in st.session_state:
            X_data = st.session_state["input_data"]
            st.write(X_data)
                
            st.write(predict_cluster(X_data=X_data))   
        else:
            st.write("Data not received")
        
        if st.button("Home Page"):
            st.session_state.page = "Input_Data"

def main():
#    if "page" n   
    if 'page' not in st.session_state:
        st.session_state.page = 'Input Data'

    if st.session_state.page == 'Input Data':
        input_fields()
    elif st.session_state.page == 'Display Data':
        show_result ()
    


    # # Create two columns
    # col1, col2 = st.columns(2)

    # # Add elements to the first column
    # with col1:
    #     st.write("This is column 1")

    # # Add elements to the second column
    # with col2:
    #     st.write("This is column 2")

    # # Create a container
    # with st.container():
    #     st.write("This is inside a container")
    # a = """This is my textasdjhkjashdkjahskdj kjahds kajshdkjhk kajsdhkaj sdkjhas akjshdkajs dk jashdkja sdashgdasgd hagsdhags """ 
    # # Create an expander
    # with st.expander("Business Insights"):
    #     st.write(a)

    # Display information based on the selected fruit
    # if selected_fruit == 'Apple':
    #     st.write("Apples are a great source of fiber and vitamin C.")
    #     st.image("apple.jpg", caption="An apple", use_column_width=True)
    # elif selected_fruit == 'Banana':
    #     st.write("Bananas are rich in potassium and provide quick energy.")
    #     st.image("banana.jpg", caption="A banana", use_column_width=True)
    # elif selected_fruit == 'Orange':
    #     st.write("Oranges are known for their high vitamin C content.")
    #     st.image("orange.jpg", caption="An orange", use_column_width=True)
if __name__ == "__main__":
    main()
