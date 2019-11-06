function send_command(){

}

function interpret_command(power, key){
    switch(key){
        case 87: // w : UP

            break;
        case 83: // s : DOWN

            break;
        case 65: // a : LEFT

            break;
        case 68: // d : RIGHT

            break:
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