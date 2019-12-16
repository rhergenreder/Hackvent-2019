function MQTTconnect() {
if (typeof path == "undefined") {
	path = '';
}
mqtt = new Paho.MQTT.Client(
		host,
		port,
		path,
		clientid
);
    var options = {
        timeout: 3,
        keepAliveInterval: 60,
        useSSL: useTLS,
        cleanSession: cleansession,
        onSuccess: onConnect,
        onFailure: function (message) {
            $('#status').val("Connection failed: " + message.errorMessage + "Retrying");
            setTimeout(MQTTconnect, reconnectTimeout);
        }
    };

    mqtt.onConnectionLost = onConnectionLost;
    mqtt.onMessageArrived = onMessageArrived;

    if (username != null) {
        options.userName = username;
        options.password = password;
    }
    mqtt.connect(options);
}

function onConnect() {
    mqtt.subscribe(topic, {qos: 0});
}

function onConnectionLost(response) {
    setTimeout(MQTTconnect, reconnectTimeout);
    $('#alert').html('<div class="alert alert-warning" role="alert">Uhm.. somebody is currently messing with me. Try refreshing the page. I lost connection but why? 🤔</div>');
};

function onMessageArrived(message) {

    //var topic = message.destinationName;
    var payload = message.payloadString;
    countUp.update(payload);
};
