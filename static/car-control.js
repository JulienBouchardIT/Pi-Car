
function send_command(power, command){
    var form = new FormData();
    form.append("command", command);
    form.append("power", power);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "http://98.143.215.223/api/command",
      "method": "POST",
      "headers": {
        "User-Agent": "PostmanRuntime/7.19.0",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
        "Postman-Token": "fd09bab5-0983-4a82-8021-d614d42ece87,69c0e70a-3062-4223-9e13-1d9060c2797f",
        "Host": "98.143.215.223",
        "Content-Type": "multipart/form-data; boundary=--------------------------339503257207581453269352",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "273",
        "Connection": "keep-alive",
        "cache-control": "no-cache"
      },
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
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