'''
author:T
create by:2021.10
function:T's AI model research lab
'''

# requirements
import streamlit as st
import pandas as pd
import numpy as np
import json
import base64
import datetime
from PIL import Image

# latest update:
releasemark = '2021-10-10'

st.sidebar.header('TAI-Lab')
st.sidebar.markdown('https://github.com/tqthooo2021/TAI-Lab')
st.sidebar.markdown('Latest release:'+str(releasemark)+' | (Contact: tqthooo2021@163.com)')

labfunc = st.sidebar.selectbox('Lab Functions:',
[
    '[1] VisualTest',
    '[2] 测试模块2',
])

if labfunc == '[1] VisualTest':
    st.markdown('简单可视化应用测试')
    # import pandas as pd
    # import numpy as np
    
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    st.area_chart(chart_data)
    st.bar_chart(chart_data)
    st.line_chart(chart_data)
    
    
    

elif labfunc == '[2] 测试模块2':
    st.markdown('module2 test')

    # data upload
    uploaded_files1 = st.sidebar.file_uploader('test2:')

else:
    nothing = 'do nothing'