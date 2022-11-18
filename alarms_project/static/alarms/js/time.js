const currentTimeId = "time";
const alarmTimeClass = "alarm-time";
const alarmRelativeToCurrentTimeClass = "alarm-relative";
const alarmWarningClass = "alarm-warning";
const alarmSoundClass = "alarm-sound";
const alarm = new Audio();

refreshTimes = () => {
    if (!document.body.contains(document.getElementById(currentTimeId))) return;
    var timeDisplay = document.getElementById(currentTimeId);
    setCurrentTime(timeDisplay);
    var alarmTimes = document.getElementsByClassName(alarmTimeClass);
    var relativeToCurrentTimeAlarmTimes = document.getElementsByClassName(alarmRelativeToCurrentTimeClass);
    var alarmWarnings = document.getElementsByClassName(alarmWarningClass);
    var alarmSounds = document.getElementsByClassName(alarmSoundClass);
    for (let i = 0; i < alarmTimes.length; i++) {
        addRelativeTime(formatDateDisplay(alarmTimes[i].textContent), relativeToCurrentTimeAlarmTimes[i]);
        addWarning(formatDateDisplay(alarmTimes[i].textContent), alarmWarnings[i]);
        checkAlarm(formatDateDisplay(alarmTimes[i].textContent), alarmSounds[i].textContent, i);
    }

}

addAlarm = () => {
    var alarmTimes = document.getElementsByClassName(alarmTimeClass);
    for (let i = 0; i < alarmTimes.length; i++) {
        console.log(alarmTimes[i])
    }
}

checkAlarm = (alarmTime, sound, popupIndex) => {
    if (moment(alarmTime).isSame(moment(), 'second')) {
        playAlarm(sound);
        sendSignal(1); 
        displayPopup(popupIndex);
    } else {
        var curr_time = moment().format('HH:mm:ss')
        console.log(curr_time); 
        displaySetAlarm();
        // displaySetAlarm();
        //if (curr_time === "13:47:22") {
            
        //}
    }
}

addRelativeTime = (alarmTime, relativeToCurrentTimeAlarmTime) => relativeToCurrentTimeAlarmTime.innerHTML = moment(alarmTime).fromNow();

addWarning = (alarmTime, alarmWarningDisplay) => (moment(alarmTime).isBefore(moment())) ? alarmWarningDisplay.innerHTML = 'Alarm time has passed, please update alarm to future time, or dismiss the alarm' : null;
playAlarm = (sound) => {
    stopAlarm();
    alarm.src = sound;
    alarm.load();
    alarm.play();
};

stopAlarm = () => {
    alarm.pause();
    alarm.currentTime = 0;
    alarm.src = '';
}
displayPopup = (popupIndex) => {
    console.log(`hey ${popupIndex}`);
    $(`#modal-alarm-${popupIndex}`).modal('show');
    $(`#modal-alarm-${popupIndex}`).on('hidden.bs.modal', (e) => addAlarm());
}

displaySetAlarm = () => {
    console.log("display alarm"); 
    $(`#modal-alarm-auto`).modal('show');
    $(`#modal-alarm-auto`).on('hidden.bs.modal', (e) => {
        console.log("dismiss"); 
    });
}
setCurrentTime = (placeholder) => placeholder.innerHTML = moment().format("HH:mm:ss");
formatDateDisplay = (dateDisplay) => {
    dateDisplay = dateDisplay.replace(/\./g, '');
    if (!dateDisplay.includes(":")) {
        strList = dateDisplay.split(" ");
        strList[strList.length - 2] += ":00";
        dateDisplay = strList.join(" ");
    }
    return dateDisplay;
}

setInterval(refreshTimes, 1000);

sendSignal = (signal) => {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "controller/send/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        signal: signal
    }));
    console.log(`hey im herre`);
}