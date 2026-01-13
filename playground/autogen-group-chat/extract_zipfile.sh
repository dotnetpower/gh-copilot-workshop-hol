#!/bin/bash

# autogen-group-chat.zip 압축 해제 스크립트

ZIP_FILE="autogen-group-chat.7z"

# zip 파일 존재 확인
if [ ! -f "$ZIP_FILE" ]; then
    echo "Error: $ZIP_FILE 파일을 찾을 수 없습니다."
    exit 1
fi

# 7z 명령 존재 확인
if ! command -v 7z &> /dev/null; then
    echo "Error: 7z 명령이 설치되어 있지 않습니다."
    echo "설치: sudo apt install p7zip-full"
    exit 1
fi

# 암호 입력 (화면에 표시되지 않음)
echo "압축 파일 암호를 입력하세요:"
read -s PASSWORD
echo

# 압축 해제
echo "압축 해제 중..."
7z x -p"$PASSWORD" -y "$ZIP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ 압축 해제 완료!"
else
    echo "❌ 압축 해제 실패. 암호가 틀렸거나 파일이 손상되었습니다."
    exit 1
fi
