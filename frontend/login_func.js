function login(form){

    if (form.id.value==DB_id_1) {
        if(form.pw.value==DB_pw_1){
            if(DB_user_1=="본인"){
                location='DailyCalender.html' 
            }
            else location='familyCalendar.html'
        }
        else alert("비밀번호가 틀렸습니다.")
    } 
    else if (form.id.value==DB_id_2) {
        if(form.pw.value==DB_pw_2){
            if(DB_user_2=="본인"){
                location='DailyCalender.html' 
            }
            else location='familyCalendar.html'
        }
        else alert("비밀번호가 틀렸습니다.")
    }
    else if (form.id.value==DB_id_3) {
        if(form.pw.value==DB_pw_3){
            if(DB_user_3=="본인"){
                location='DailyCalender.html' 
            }
            else location='familyCalendar.html'
        }
        else alert("비밀번호가 틀렸습니다.")
    }
    else if (form.id.value==DB_id_4) {
        if(form.pw.value==DB_pw_4){
            if(DB_user_4=="본인"){
                location='DailyCalender.html' 
            }
            else location='familyCalendar.html'
        }
        else alert("비밀번호가 틀렸습니다.")
    }
    else if (form.id.value==DB_id_5) {
        if(form.pw.value==DB_pw_5){
            if(DB_user_5=="본인"){
                location='DailyCalender.html' 
            }
            else location='familyCalendar.html'
        }
        else alert("비밀번호가 틀렸습니다.")
    }
    else alert("아이디가 틀렸습니다.")
}


function login_join(form){
    if (form.id.value!=DB_id_1) {
        if(form.id.value!=DB_id_2){
            if(form.id.value!=DB_id_3){
                if(form.id.value!=DB_id_4){
                    if(form.id.value!=DB_id_5){
                        var line_set='member_profile'+'/'+form.id.value;
                        var fb_profile = firebase.database().ref(line_set);
                        
                        fb_profile.child("id").set(form.id.value);
                        fb_profile.child("pw").set(form.pswd1.value);
                        fb_profile.child("name").set(form.name.value);
                        fb_profile.child("email").set(form.email.value);
                        fb_profile.child("emotion_email").set(form.e_email.value);
                        fb_profile.child("구분").set(form.user.value);
                        
                        alert("회원가입이 완료되었습니다.")
                        location.replace('login.html');

                        if(DB_id_1==null){
                            var fb_set='login'+'/'+1
                            var fb_profile = firebase.database().ref(fb_set);
                            fb_profile.child("id").set(form.id.value);
                            fb_profile.child("pw").set(form.pswd1.value);
                            fb_profile.child("구분").set(form.user.value);

                        }
                        else if(DB_id_2==null){
                            var fb_set='login'+'/'+2
                            var fb_profile = firebase.database().ref(fb_set);
                            fb_profile.child("id").set(form.id.value);
                            fb_profile.child("pw").set(form.pswd1.value);
                            fb_profile.child("구분").set(form.user.value);
                        }
                        else if(DB_id_3==null){
                            var fb_set='login'+'/'+3
                            var fb_profile = firebase.database().ref(fb_set);
                            fb_profile.child("id").set(form.id.value);
                            fb_profile.child("pw").set(form.pswd1.value);
                            fb_profile.child("구분").set(form.user.value);
                        }
                        else if(DB_id_4==null){
                            var fb_set='login'+'/'+4
                            var fb_profile = firebase.database().ref(fb_set);
                            fb_profile.child("id").set(form.id.value);
                            fb_profile.child("pw").set(form.pswd1.value);
                            fb_profile.child("구분").set(form.user.value);
                        }
                        else if(DB_id_5==null){
                            var fb_set='login'+'/'+5
                            var fb_profile = firebase.database().ref(fb_set);
                            fb_profile.child("id").set(form.id.value);
                            fb_profile.child("pw").set(form.pswd1.value);
                            fb_profile.child("구분").set(form.user.value);
                        }
                    }
                    else alert("이미 가입된 아이디입니다.");
                } 
                else alert("이미 가입된 아이디입니다.");
            }
            else alert("이미 가입된 아이디입니다.");
        }
        else alert("이미 가입된 아이디입니다.");
    }
    else alert("이미 가입된 아이디입니다.");
}