#시간에 따른 음을 계산하여 풀이하였더니 통과. 4시간걸림;;
def getTime(start, end):
    thisTime = ((int(end[:2])*60)+int(end[-2:])) - ((int(start[:2]) * 60) + int(start[-2:]))
    return thisTime

def getMusic(m, time, tf):
    arr = ["C#", "D#", "F#", "G#", "A#"]
    arr1 = ["c", "d", "f", "g", "a"]
    for i in range(len(arr)):
        while arr[i] in m:
            m = m.replace(arr[i], arr1[i])
    if tf == 0:
        return m
    elif tf == 1:
        if len(m) > time:
            m = m[:time]
        elif len(m) < time:
            m = (m * (time // len(m) + 2))
    return m 
    
def solution(m, musicinfos):
    resultMusic, resultTime = "(None)", 0
    m = getMusic(m, 1, 0)
    for i in range(len(musicinfos)):
        info = musicinfos[i].split(",")
        time = getTime(info[0], info[1])
        musicinfo = getMusic(info[3], time, 1)
        if m in musicinfo:
            if resultTime < time:
                resultTime = time
                resultMusic = info[2]
    return resultMusic

#풀이3 테스트 30번 실패 아마 재생시간에 대한 음악의 길이를 임의적으로 계산해서 그런듯
# def getTime(start, end):
#     thisTime = ((int(end[:2])*60)+int(end[-2:])) - ((int(start[:2]) * 60) + int(start[-2:]))
#     return thisTime

# def getMusic(m, time):
#     arr = ["C#", "D#", "F#", "G#", "A#"]
#     arr1 = ["c", "d", "f", "g", "a"]
#     for i in range(len(arr)):
#         while arr[i] in m:
#             m = m.replace(arr[i], arr1[i])
#     m = (m * (time // len(m) + 2))
#     return m
    
# def solution(m, musicinfos):
#     resultMusic, resultTime = "(None)", 0
#     m = getMusic(m, -1)
#     for i in range(len(musicinfos)):
#         info = musicinfos[i].split(",")
#         time = getTime(info[0], info[1])
#         musicinfo = getMusic(info[3], time)
#         if m in musicinfo:
#             if resultTime < time:
#                 resultTime = time
#                 resultMusic = info[2]
#     return resultMusic
        
#풀이2 시작시간이 무조건 정각인 줄 알아서 실패.
# def solution(m, musicinfos):
#     music = "(None)"
#     time = 0
#     arr = ["C#", "D#", "F#", "G#", "A#"]
#     arr1 = ["c", "d", "f", "g", "a"]
#     for i in range(len(arr)):
#         while arr[i] in m:
#             m = m.replace(arr[i], arr1[i])
#     for i in range(len(musicinfos)):
#         info = musicinfos[i].split(",")
#         len_music = info[3] * ((len(m)//len(info[3]))+2)
#         for i in range(len(arr)):
#             while arr[i] in len_music:
#                 len_music = len_music.replace(arr[i], arr1[i])
#         if m in len_music:
#             if time < int(info[1][-2:]):
#                 time = int(info[1][-2:])
#                 music = info[2]
#         aa = int(info[1][-2:])
#         len_music = len_music[:aa+1]
#         if m in len_music:
#             if time < int(info[1][-2:]):
#                 time = int(info[1][-2:])
#                 music = info[2]
#     return music

#풀이1 "#"에 대해 코딩하지 않아서 실패.
# def solution(m, musicinfos):
#     time = 0
#     result = "(None)"
#     for i in range(len(musicinfos)):
#         music = musicinfos[i].split(",")
#         len_music = (music[3] * ((len(m)//len(music[3]))+2))
#         if m in len_music:
#             if time < int(music[1][-2:]):
#                 time = int(music[1][-2:])
#                 result = music[2]
#     return result
