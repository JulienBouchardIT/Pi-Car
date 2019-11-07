

function send_command(power, key){
    switch(key){
        case 87: // w : UP
            alert("UP "+power)
            break;
        case 83: // s : DOWN
            alert("DOWN "+power)
            break;
        case 65: // a : LEFT
            alert("LEFT "+power)
            break;
        case 68: // d : RIGHT
            alert("RIGHT "+power)
            break;
        default:
            break;
    }
}

function down(event){
    send_command(false, event.keyCode);
}

function up(event){
    send_command(true, event.keyCode);
}