'''
author:T
create by:2021.10
function:T's AI model research lab
'''

# config
from platform import release
import streamlit as st
import pandas as pd
import numpy as np
import json
import base64
import datetime
from PIL import Image

# latest update:
releasemark = '2021-10-10'

st.sidebar.header('TAI-Lab|人工智能实验室')
st.sidebar.markdown('https://github.com/tqthooo2021/TAI-Lab')
st.sidebar.markdown('Latest release:'+str(releasemark)+' | (Contact: tqthooo2021@163.com)')

labfunc = st.sidebar.selectbox('Lab Functions:',
[
    '[1] 测试模块1',
    '[2] 测试模块2',
])

if labfunc == '[1] 测试模块1':
    st.markdown('module1 test')

    # data upload
    uploaded_files1 = st.sidebar.file_uploader('test:')

elif labfunc == '[2] 测试模块2':
    st.markdown('module2 test')

else:
    nothing = 'do nothing'