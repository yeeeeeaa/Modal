// MonthlyCalendar의 함수

    var countWeek=null;	//몇 주인지 세는 변수
    var today = null;
    var year = null;
    var month = null;
    var firstDay = null;
    var lastDay = null;
    var $tdDay = null;
    var $tdSche = null;

    //calendar 그리기
    function drawCalendar(){
        var setTableHTML = "";
        setTableHTML+='<table class="calendar">';
        setTableHTML+='<tr><th align=center>일</th><th align=center>월</th><th align=center>화</th><th align=center>수</th><th align=center>목</th><th align=center>금</th><th align=center>토</th></tr>';
        for(var i=0;i<6;i++){
            setTableHTML+='<tr height="130">';
            for(var j=0;j<7;j++){
                setTableHTML+='<td style="text-overflow:ellipsis;overflow:hidden;white-space:nowrap">';
                setTableHTML+='    <div class="cal-day"></div>';
                setTableHTML+='    <div class="cal-schedule"></div>';
                setTableHTML+='</td>';
            }
            setTableHTML+='</tr>';
        }
        setTableHTML+='</table>';
        $("#cal_tab").html(setTableHTML);
    }


    //날짜 초기화
    function initDate(){
        $tdDay = $("td div.cal-day")
        $tdSche = $("td div.cal-schedule")
        dayCount = 0;
        today = new Date();
        year = today.getFullYear();
        month = today.getMonth()+1;
        firstDay = new Date(year,month-1,1);
        lastDay = new Date(year,month,0);
    }

    
    //calendar 날짜표시
    function drawDays(){
        $("#cal_top_year").text(year);
        $("#cal_top_month").text(month);
        for(var i=firstDay.getDay();i<firstDay.getDay()+lastDay.getDate();i++){
            $tdDay.eq(i).text(++dayCount);
        }
        for(var i=0;i<42;i+=7){
            $tdDay.eq(i).css("color","red");
        }
        for(var i=6;i<42;i+=7){
            $tdDay.eq(i).css("color","blue");
            countWeek+=1;	//일단은 일요일마다 1주 추가로
        }
    }


   //calendar 월 이동
    function movePrevMonth(){
        month--;
        if(month<=0){
            month=12;
            year--;
        }
        if(month<10){
            month=String("0"+month);
        }
        getNewInfo();
        }
    

   function moveNextMonth(){
        month++;
        if(month>12){
            month=1;
            year++;
        }
        if(month<10){
            month=String("0"+month);
        }
        getNewInfo();
    }


    function getNewInfo(){
        for(var i=0;i<42;i++){
            $tdDay.eq(i).text("");
        }
        dayCount=0;
        firstDay = new Date(year,month-1,1);
        lastDay = new Date(year,month,0);
        drawDays();
    }

    

    //정보갱신
    function getNewInfo(){
        for(var i=0;i<42;i++){
            $tdDay.eq(i).text("");
            $tdSche.eq(i).text("");
        }
        dayCount=0;
        firstDay = new Date(year,month-1,1);
        lastDay = new Date(year,month,0);
        drawDays();
        drawSche();
    }
   

    //데이터 등록
    function setData(){
        jsonData = 
        {
            "2021":{
                "07":{
                    "17":"제헌절"
                }
                ,"08":{
                    "15":"광복절"
                }
                ,"09":{
                    "13":"추석"
                }
            }
        }
    }
  

    //스케줄 그리기
    function drawSche(){
        setData();
        var dateMatch = null;
        for(var i=firstDay.getDay();i<firstDay.getDay()+lastDay.getDate();i++){
            var txt = "";
            txt =jsonData[year];
            if(txt){
                txt = jsonData[year][month];
                if(txt){
                    txt = jsonData[year][month][i];
                    dateMatch = firstDay.getDay() + i -1; 
                    $tdSche.eq(dateMatch).text(txt);
                }
            }
        }
    }
    
//Weekly 함수
var weeknum;
var day = new Date();
day.setDate(day.getDate()-day.getDay());

function week_calandar(week) {
    day.setDate(day.getDate()+week*7);
    var title = day.getFullYear() + "년" + (day.getMonth()+1) +"월";
    var data = ""
    
    var fb_location=0;
    var fb_location_1="";    

    var fb_route = (day.getFullYear()-2000)*10000+(day.getMonth()+1)*100+(day.getDate()-day.getDay())*1;
   
        for(var i=0 ; i<7 ; i++) {
            var ment = ""

            fb_location = firebase.database().ref("박철수"+"/"+String(fb_route)+"/"+"내용");
            fb_location.on('value', snap =>{ fb_location_1 = snap.val();});
                  
            if(fb_location_1 != null){
                ment=fb_location_1;
            }

            data += day.getDate() + "   "+ ment +"<br />"+"<hr />";
            if(day.getDate() == 1)
                title += " ~ " + day.getFullYear() + "/" + (day.getMonth()+1);
            day.setDate(day.getDate()+1);
            fb_route+=1;
            }
    day.setDate(day.getDate()-7);
    document.getElementById("calandar").innerHTML = title + "<br />" + data;
    }

    function set_day() {
    	day = new Date();
    	day.setDate(day.getDate()-day.getDay());
    	week_calandar(0);
    	}
    
    //Weekly와 Monthly 연결
    function connect_weekly_monthly(){	
    	week_calendar();	
    }
