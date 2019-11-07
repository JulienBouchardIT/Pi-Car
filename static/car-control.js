
function send_command(power, command){
    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "http://192.168.0.102:80/api/command",
      "method": "POST",
      "headers": {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Host": "192.168.0.102:80",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "23",
        "Connection": "keep-alive",
        "cache-control": "no-cache"
      },
      "data": {
        "command": command,
        "power": power
      }
    }

    $.ajax(settings).done(function (response) {
      console.log(response);
    });
}

function key_to_command(key){
    switch(key){
        case 87: // w : UP
            return "up";
        case 83: // s : DOWN
            return "down";
        case 65: // a : LEFT
            return "left";
        case 68: // d : RIGHT
            return "right";
        default:
            break;
    }
}

function down(event){
    console.log(event);
    var keyCode = (window.event) ? event.which : event.keyCode;
    send_command(false, key_to_command(keyCode));
}

function up(event){
    var keyCode = (window.event) ? event.which : event.keyCode;
    send_command(true, key_to_command(keyCode));
}