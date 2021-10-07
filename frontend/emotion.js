emotion_anger = 0; //분노
emotion_happiness = 0; //행복
emotion_excited = 0; //신남
emotion_gloomy = 0; //우울
emotion_soso = 0; //평범
emotion_sad = 0; //슬픔

//감정 카운트 값 파이어베이스 전송
function anger() { //분노
    emotion_anger += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/anger").set(emotion_anger);
    alert("분노에 차 있을 땐 1부터 10까지 세어 보세요^^");
    return (emotion_anger);
}

function happiness() { //행복
    emotion_happiness += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/happiness").set(emotion_happiness);
    alert("행복하시다니 저도 행복합니다^^");
    return (emotion_happiness);
}

function excited() { //신남
    emotion_excited += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/excited").set(emotion_excited);
    alert("신나는 하루입니다!");
    return (emotion_excited);
}

function gloomy() { //우울
    emotion_gloomy += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/gloomy").set(emotion_gloomy);
    alert("말로 슬픔을 덜 순 없겠지만, 힘내세요.");
    return (emotion_gloomy);
}

function soso() { //평범
    emotion_soso += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/soso").set(emotion_soso);
    alert("내일은 행복한 하루가 되시길 바라겠습니다^^");
    return (emotion_soso);
}

function sad() { //슬픔
    emotion_sad += 1;
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("emotion/sad").set(emotion_sad);
    alert("웃음도 눈물도 그리 오래 가는 것은 아닙니다.");
    return (emotion_sad);
}