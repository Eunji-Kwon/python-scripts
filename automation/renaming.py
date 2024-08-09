import os

# 파일이 저장된 디렉토리 경로
# Directory path where the files are stored
directory = '/path/to/your/folder'

# 파일명을 변경할 함수
# Function to rename files
def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            # 기존 파일 경로
            # Existing file path
            old_path = os.path.join(directory, filename)

            # 파일명을 구분하기 위해 사용될 키워드들
            # Keywords used to split the filename
            name_parts = filename.replace(' ', '_').split('_')

            # 여기서 name_parts를 적절히 수정하여 파일명 생성
            # 예시: LastName_FirstName_Resume.pdf 형태로 변경
            # Modify name_parts to create a new filename
            # Example: Changing to LastName_FirstName_Resume.pdf format
            new_name = f"{name_parts[1]}_{name_parts[0]}_Resume{os.path.splitext(filename)[1]}"

            # 새 파일 경로
            # New file path
            new_path = os.path.join(directory, new_name)

            # 파일명 변경
            # Rename the file
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_name}')

# 함수 실행
# Run the function
rename_files(directory)
