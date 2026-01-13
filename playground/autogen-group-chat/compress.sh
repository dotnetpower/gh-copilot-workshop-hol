#!/bin/bash

# 현재 폴더를 .sh 파일 제외하고 암호화 압축하는 스크립트

ARCHIVE_NAME="autogen-group-chat.7z"

# 7z 명령 존재 확인
if ! command -v 7z &> /dev/null; then
    echo "Error: 7z 명령이 설치되어 있지 않습니다."
    echo "설치: sudo apt install p7zip-full"
    exit 1
fi

# 암호 입력 (화면에 표시되지 않음)
echo "압축 파일에 설정할 암호를 입력하세요:"
read -s PASSWORD
echo

echo "암호를 다시 한 번 입력하세요:"
read -s PASSWORD_CONFIRM
echo

# 암호 확인
if [ "$PASSWORD" != "$PASSWORD_CONFIRM" ]; then
    echo "❌ 암호가 일치하지 않습니다."
    exit 1
fi

# 기존 압축 파일이 있으면 백업
if [ -f "$ARCHIVE_NAME" ]; then
    BACKUP="${ARCHIVE_NAME}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "기존 파일을 백업합니다: $BACKUP"
    mv "$ARCHIVE_NAME" "$BACKUP"
fi

# 압축 시작
echo "압축 중... (.sh 파일 제외)"
7z a -p"$PASSWORD" -mhe=on "$ARCHIVE_NAME" * -xr!*.sh -xr!*.7z -xr!*.backup.*

if [ $? -eq 0 ]; then
    echo "✅ 압축 완료: $ARCHIVE_NAME"
    echo "📦 파일 크기: $(du -h "$ARCHIVE_NAME" | cut -f1)"
else
    echo "❌ 압축 실패"
    exit 1
fi
