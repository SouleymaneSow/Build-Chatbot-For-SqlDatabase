import vanna as vn # provides the infrastructure to use an LLM (i.e. AI) to generate SQL
import streamlit as st 

# Vanna clsSetup
from vanna.remote import VannaDefault
vn = VannaDefault(model='chinook', api_key='vanna_api_key')

#Connect to the Database
vn.connect_to_sqlite('https://vanna.ai/Chinook.sqlite')

# TextBox
my_question = st.session_state.get("my_question", default=None)
if my_question is None:
    my_question = st.text_input("Ask me a question that I can turn into SQL", key="my_question")
else:
    st.title(my_question)
    #Generate SQL using AI
    sql = vn.generate_sql(my_question)
    st.code(sql, language='sql')
    # Show the Table
    df = vn.run_sql(sql)    
    st.dataframe(df, use_container_width=True)
    # Use AI to Generate a Chart and Display It
    fig = vn.get_plotly_figure(plotly_code=vn.generate_plotly_code(question=my_question, sql=sql, df=df), df=df)
    st.plotly_chart(fig, use_container_width=True)
    st.button("Ask another question", on_click=lambda: st.session_state.clear())
