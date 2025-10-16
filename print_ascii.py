import os

def print_ascii_art(file_path):
    """지정된 파일 경로의 내용을 CMD/PowerShell에 출력합니다."""
    # 인코딩 오류 방지를 위해 'utf-8'로 읽는 것이 안전합니다.
    # 특히 점자 문자가 있는 경우(acsii점자 rehotaesik.txt)에 중요합니다.
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다. 경로를 확인하세요: {file_path}")
    except Exception as e:
        print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

# --- 실행 부분 ---
# 실제 파일이 있는 경로와 파일 이름을 여기에 맞게 수정하세요.
file1_path = "acsii,rehotaesik.txt"
file2_path = "Acsii rehotaesik.txt"
file3_path = "acsii점자 rehotaesik.txt"

print(r"C:\Users\DELL_5080\Desktop\김태호 폴더\n--- acsii,rehotaesik.txt 출력 ---")
print_ascii_art(file1_path)

print(r"C:\Users\DELL_5080\Desktop\김태호 폴더\n--- Acsii rehotaesik.txt 출력 ---")
print_ascii_art(file2_path)

print(r"C:\Users\DELL_5080\Desktop\김태호 폴더\n--- acsii점자 rehotaesik.txt 출력 ---")
print_ascii_art(file3_path)

'''
CMD나 PowerShell을 열고 해당 폴더로 이동합니다.

다음 명령어를 실행합니다:

DOS

python print_ascii.py
'''
