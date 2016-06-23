# Communications with the Raspberry Pi

## Communication

*Get system information*

Could display some stuff like uptime and...

*Get available podcasts*

List the episodes available. This should include stuff like time played and duration.

*Play podcast*

Trigger the starting of a episode.

*Update play status*

The Pi should send updates to clients every X seconds when playing.

## Flow

1. Client connects and is registered by server.
2. Server sends initial status (available methods and info).
3. Client asks for podcast list for example.
4. Client sends play/pause command to server.
5. While clients are connected, server sends status updates.

1. Client -> connect -> server
2. Server -> status -> client
3. Server -> play-status -> client
4. Client -> play/pause/change -> server


## React App

Would be much more awesome to have a app for controlling everything.

1. Scan network for rPi.
2. Connect
3. Get information.
