import streamlit as st
from setup import * 

# insert path to pre-req dataset
pre_req_data = pd.read_csv("data/Pre_Req.csv")

# Streamlit Heading 
st.title('Yale Interactive Prerequisite Dataset')
st.sidebar.text("Filter by:")

data_filter = st.sidebar.selectbox('Select Filter', ["Majors", "Courses", "Concentrations"])

if data_filter == "Concentrations":
    with st.sidebar.expander("Concentrations"):
        primary_con = st.multiselect('Select Primary Concentation', np.unique(pre_req_data["Concentration"]))
        concen_show = st.selectbox('Show', ["Major", "Courses", "ALL"])

        indexes = []
        if len(primary_con) != 0: 
            for concentration in primary_con:
                ind, = np.where(pre_req_data["Concentration"] == concentration)
                indexes.append(ind)
            indexes = np.unique(np.concatenate((indexes),0))
    if concen_show == "ALL":
        st.subheader('Complete List of Yale Majors and Courses by Concentration')
        df = pre_req_data.iloc[np.unique(indexes)]
    elif concen_show == "Courses": 
        st.subheader('List of Yale Courses in Concentration')
        df = pd.DataFrame(np.array(pre_req_data["Course"].iloc[np.unique(indexes)].drop_duplicates()), columns = ['Courses'])
    elif concen_show == "Major": 
        st.subheader('List of Yale Majors in Concentration')
        df = pd.DataFrame(np.array(pre_req_data["Major"].iloc[np.unique(indexes)].drop_duplicates()), columns = ['Major'])

if data_filter == "Majors":
    with st.sidebar.expander("Majors"):
        majors = st.multiselect('Select Major', np.unique(pre_req_data["Major"]))
        major_show = st.selectbox('Show', ["Course", "ALL"])

        indexes = []
        if len(majors) != 0: 
            for major in majors:
                ind, = np.where(pre_req_data["Major"] == major)
                indexes.append(ind)
            indexes = np.unique(np.concatenate((indexes),0))
    if major_show == "ALL": 
        st.subheader('Complete List of Yale Concentrations and Courses by Major')
        df = pre_req_data.iloc[np.unique(indexes)]
    elif major_show == "Course": 
        st.subheader('List of Prerequisite Courses Needed for Major(s)')
        df = pd.DataFrame(np.array(pre_req_data["Course"].iloc[np.unique(indexes)].drop_duplicates()), columns = ['Major'])

if data_filter == "Courses":   
    with st.sidebar.expander("Courses"):
        st.subheader("Put in the Classes you have taken and see what majors need those Pre-Reqs")
        courses = st.multiselect('Select Courses', np.unique(pre_req_data["Course"]))
        course_show = st.selectbox('Show', ["Major", "Concentration", "ALL"])

        indexes = []
        if len(courses) != 0: 
            for course in courses:
                ind, = np.where(pre_req_data["Course"] == course)
                indexes.append(ind)
            indexes = np.unique(np.concatenate((indexes),0))

    if course_show == "ALL": 
        st.subheader('Complete List of Yale Majors and Courses by Courses')
        df = pre_req_data.iloc[np.unique(indexes)]
    elif course_show == "Major": 
        st.subheader('List of Yale Majors by Courses')
        df = pd.DataFrame(np.array(pre_req_data["Major"].iloc[np.unique(indexes)].drop_duplicates()), columns = ['Major'])
    elif course_show == "Concentration": 
        st.subheader('List of Yale Courses by Major')
        df = pd.DataFrame(np.array(pre_req_data["Concentration"].iloc[np.unique(indexes)].drop_duplicates()), columns = ['Major'])

        
        
st.table(df)

## CODE TO HIDE ROW NUMBERS 
        
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
