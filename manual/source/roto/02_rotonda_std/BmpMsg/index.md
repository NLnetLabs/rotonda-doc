# BmpMsg
`````{roto:type} BmpMsg
BMP message.
`````


````{roto:function} announcements_count(msg: BmpMsg) -> u64
Return the number of announcements in this message.
````

````{roto:function} aspath(msg: BmpMsg) -> Option[AsPath]
Return the [`AsPath`](AsPath).
````

````{roto:function} communities(msg: BmpMsg) -> Option[List[Community]]
Return a [`List`](List[T]) of [`Community`](Community) in this message.
````

````{roto:function} fmt_base64(msg: BgpMsg) -> String
Format this message as base64.
````

````{roto:function} fmt_hex(msg: BgpMsg) -> String
Format this message as hex.
````

````{roto:function} fmt_pcap(msg: BmpMsg) -> String
Format this message as hexadecimal Wireshark input.
````

````{roto:function} has_attribute(msg: BmpMsg, to_match: u8) -> bool
Check whether this message contains the given Path Attribute.
````

````{roto:function} is_ibgp(msg: BmpMsg, asn: Asn) -> bool
Check whether this is an iBGP message based on a given `asn`.

Return true if `asn` matches the asn in the `BmpMsg`.
returns false if no PPH is present.
````

````{roto:function} is_peer_down(msg: BmpMsg) -> bool
Check whether this message is of type 'PeerDownNotification'.
````

````{roto:function} is_peer_up(msg: BmpMsg) -> bool
Check whether this message is of type 'PeerUpNotification'.
````

````{roto:function} is_route_monitoring(msg: BmpMsg) -> bool
Check whether this message is of type 'RouteMonitoring'.
````

````{roto:function} large_communities(msg: BmpMsg) -> Option[List[LargeCommunity]]
Return a [`List`](List[T]) of [`LargeCommunity`](LargeCommunity) in this message.
````

````{roto:function} withdrawals_count(msg: BmpMsg) -> u64
Return the number of withdrawals in this message.
````

