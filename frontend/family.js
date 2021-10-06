function addSchedule() {
    //날짜를 변수로 가져오기
    //월
    var month
    var target = document.getElementById("month");
    month = target.options[target.selectedIndex].value

    //일
    var day
    var target = document.getElementById("day");
    day = target.options[target.selectedIndex].value

    //database에 들어가는 날짜 형식
    var date
    date = "21" + month + day

    //textarea에서 일정 내용 가져오기
    var valueInSchedule = '';
    valueInSchedule = document.getElementById("schedules").value;

    //firebase에 저장되는 일정 형식
    var formatForDB;
    var formatMonth;
    var formatDay;

    //0n월을 n월로 바꾸기
    formatMonth = month.split("");
    if (formatMonth[0] == "0") {
        formatMonth[0] = " ";
    }

    //0n일을 n일로 바꾸기
    formatDay = day.split("");
    if (formatDay[0] == "0") {
        formatDay[0] = " ";
    }

    formatForDB = formatMonth.join('') + "월 " + formatDay.join('') + "일 " + valueInSchedule;

    //firebase에 저장
    var dbRefObject = firebase.database().ref();
    dbRefObject.child("김철수/family/" + date + "/" + valueInSchedule + "/내용").set(formatForDB);
    alert("저장되었습니다!");

}