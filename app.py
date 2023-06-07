import streamlit as st
from add_data import add_project
from fetch_data import fetch_projects, delete_project, search_projects


# タイトルの設定
st.title('My Sewing App')

# テキストの表示
st.write('Welcome to my sewing app!')

with st.form(key='my_form'):
    project_name = st.text_input(label='item title')
    # 他の入力項目も同様に追加
    dif_level = st.text_input(label='difficulty level')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    data = {'name': project_name, 'difficulty_level': dif_level}  # 他の入力項目も同様に追加
    add_project(data)
    st.write('Project added to the database.')

# keyword = st.text_input('Enter keyword for search')
# if keyword:
#     projects = search_projects(keyword)
# else:
#     projects = fetch_projects()

# for project in projects:
#     st.write(project.id, project.name)

# projects = fetch_projects()

# for project in projects:
#     col1, col2 = st.columns([4,1])
#     col1.text(project.name)  # プロジェクト名を表示

#     if col2.button("Delete", key=project.id):
#         delete_project(project.id)
#         st.write(f"Deleted project: {project.name}")
#         projects = fetch_projects()  # 更新されたプロジェクトリストを取得
#         st.experimental_rerun()  # ページをリロードして削除を反映

keyword = st.text_input('Enter keyword for search')
if keyword:
    projects = search_projects(keyword)
    for index, project in enumerate(projects):
        st.write(project.id, project.name)
        # 各プロジェクトに対して削除ボタンを追加
        if st.button(f"Delete {project.name}", key=f"button_{index}"):
            delete_project(project.id)
            st.write('Project deleted from the database.')
            st.experimental_rerun()  # ページをリロードして削除を反映
else:
    projects = fetch_projects()
    for project in projects:
        col1, col2 = st.columns([4,1])
        col1.text(project.name)  # プロジェクト名を表示


    