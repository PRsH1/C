"""
주제:os모듈을 이용한 파일 폴더 삭제
작성자:이승현
작성일:2017.12.04.
"""
import os
dict=input("경로를 입력하세요:")#경로를 입력하라는 메세지 출력,경로를 입력받는다
os.chdir(dict)#입력한 경로로 이동
while(1):#반복문
    permit = os.getcwd()#현재 작업 폴더 permit에 저장
    print("현재 작업 디렉토리는:"+permit+"입니다")#안내문 출력
    list = os.listdir(permit)#현재 작업 디렉터리 하위 폴더와 파일 리스트화
    if len(list)!=0:#리스트 길이가 0이 아니면
        for i in list:#반복문
            join = os.path.join(permit, i)#join함수를 사용해 경로 병합
            print("현재 병합된 경로:",join)
            if os.path.isdir(join):#만약 경로가 폴더이면
                if len(os.listdir(join))==0:#조인 경로를 리스화해 길이 검사,만약 0이라면
                    print("이 디렉터리는 하위 경로에 폴더,파일이 없습니다 그러므로 삭제합니다")#삭제 메세지 출력
                    os.removedirs(join)#경로 삭제
                    os.chdir(dict)#처음으로 돌아간다
                    break
                else:#아니면
                    os.chdir(os.path.join(permit,i))#이동한다 (i)
                    print(os.getcwd() +"디렉터리로 이동함")#이동 메세지 출력
                    continue
        if os.path.isfile(join):#경로가 파일이면
            os.remove(join)#파일 삭제
            print(join+"파일이 삭제되었습니다")#삭제 메세지 출력
            os.chdir(dict)#처음으로
            continue
    elif len(list)==0:#리스트 길이가 0이면
        print("리스트의 길이가 0이므로 파일과 디렉터리는 없습니다")#하위 폴더와 파일이 없으므로 없다는 메세지 출력
        break

