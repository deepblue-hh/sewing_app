from create_db import Project, Material, FinishedImage, session


def add_project(data):
    new_project = Project(**data)
    session.add(new_project)
    session.commit()



# 新しいプロジェクトを作成します
new_project = Project(
    name="プロジェクト1",
    start_date="2023-06-01",
    end_date="2023-06-30",
    reference_type="動画",
    reference_page_num=None,
    size="M",
    thread_used="コットン",
    wearing_sensation="快適",
    tags="夏,子供服",
    difficulty_level="中級"
)

# # データベースに追加します
# session.add(new_project)

# # 変更をコミットします
# session.commit()
