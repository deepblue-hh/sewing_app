from create_db import Project, session
# projects テーブルからすべてのプロジェクトを検索します
projects = session.query(Project).all()

# 検索結果を表示します
for project in projects:
    print(f"作品名: {project.name}, 開始日: {project.start_date}, 終了日: {project.end_date}")
