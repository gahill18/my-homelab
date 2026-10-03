# My Homelab

## Storage

### FreeNAS - TODO

### Proton Drive - TODO

Managed using cronjobs in ``` ~/Homelab/protondrive/proton-drive.sh ```

## Applications 

### Jellyfin

To run:

``` cd jellyfin && sudo docker compose up ```

To access:

* From local device: Open browser and go to 127.0.0.1:8096

* From separate device: TODO

### Pi-Hole

To run:

``` cd pi-hole && sudo socker compose up ```

### Minecraft Server

To run:

``` cd minecraft-server && sudo socker compose up ```

To access:

1. Open Minecraft client on device connected to Tailscale VPN

2. Multiplayer > Direct Connection or Add Server > [SERVER IP]:25565

## Networking

### Tailscale

To install:

``` curl -fsSL https://tailscale.com/install.sh | sh ```

To run:

``` sudo tailscale up ```

To connect:

1. From another device, connect to the Tailscale webclient

2. Log in

3. Navigate to "Machines"

4. Under "Fedora", select "SSH"
