import streamlit as st
# import pickle as pkl
# import numpy as np



class MultiPage:

    def __init__(self):
        self.pages = []


    def add_page(self, title, func):
        self.pages.append({
            "title":title,
            "function":func
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Pages',
            self.pages,
            format_func=lambda page: page['title']
        )

        st.markdown(
            """
            <style>
            .stApp {
                max-width: 100%;
                margin: 0 auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        page['function']()


multi_page = MultiPage()

def layout_streamlit():
    st.set_page_config(layout='wide')

    light = '''
        <style>
            .stApp {
            background-color: white;
            }
        </style>
        '''
    st.markdown(light, unsafe_allow_html=True)


layout = layout_streamlit()

def responsive_iframe(url):
    code = f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>
    """
    st.markdown(code, unsafe_allow_html=True)


def page_one():
    st.title('Dashboard')
    responsive_iframe("https://lookerstudio.google.com/embed/reporting/3353d767-3ca3-4d16-9f84-acf901dfd18c/page/hxIrD")

# def page_three():
#     st.title('Churn Prediction :writing_hand:')

#     with st.form('Feature Audio Analysis'):
#         st.write('Input Features')
#         tenure_month = st.number_input('Tenure Month: ', value=0, step=1)
#         location = st.radio(
#             "Lokasi User", ("Jakarta", "Bandung")
#         )
#         device_class = st.number_input('Device Class: ', value=0, step=1)
#         game = st.number_input('Game Product: ', value=0, step=1)
#         music = st.number_input('Music Product: ', value=0, step=1)
#         education = st.number_input('Education: ', value=0, step=1)
#         call_center = st.number_input('Call Center: ', value=0, step=1)
#         payment_method = st.number_input('Payment Method: ', value=0, step=1)
#         monthly_purchase = st.number_input('Monthly Purchase: ', value=0, step=1)
#         cltv = st.number_input('CLTV: ', value=0, step=1)

#         data = np.array([tenure_month, location, device_class, game, music, education, call_center, payment_method, monthly_purchase, cltv]).reshape(1, -1)

#         if st.form_submit_button('Generate'):
#             file_name = 'D:/DSW/xgboost_model.pkl'

#             with open(file_name, 'rb') as file:
#                 loaded_model = pkl.load(file)

#             prediction = loaded_model.predict(data)
#             st.write(f"Prediction: {prediction[0]}")

def page_two():
    st.title('Home')

multi_page.add_page('Dashboard', page_one)
multi_page.add_page('Prediction', page_two)
# multi_page.add_page('Churn Prediction', page_three)

multi_page.run()
