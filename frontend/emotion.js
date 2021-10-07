emotion_anger = 0; //분노
emotion_happiness = 0; //행복
emotion_excited = 0; //신남
emotion_gloomy = 0; //우울
emotion_soso = 0; //평범
emotion_sad = 0; //슬픔

function anger() { //분노
    emotion_anger += 1;
    alert(emotion_anger);
    return (emotion_anger);
}

function happiness() { //행복
    emotion_happiness += 1;
    return (emotion_happiness);
}

function excited() { //신남
    emotion_excited += 1;
    return (emotion_excited);
}

function gloomy() { //우울
    emotion_gloomy += 1;
    return (emotion_gloomy);
}

function soso() { //평범
    emotion_soso += 1;
    return (emotion_soso);
}

function sad() { //슬픔
    emotion_sad += 1;
    return (emotion_sad);
}