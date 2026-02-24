# BmpMsg
`````{roto:type} BmpMsg
BMP message
`````


````{roto:function} announcements_count(msg: BmpMsg) -> u64
Return the number of announcements in this message
````

````{roto:function} aspath_contains(msg: BmpMsg, to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:function} aspath_origin(msg: BmpMsg) -> OriginAsn
Returns the right-most `Asn` in the 'AS_PATH' attribute

Note that the returned value is of type `OriginAsn`, which optionally
contains an `Asn`. In case of empty an 'AS_PATH' (e.g. in iBGP) this
method will still return an `OriginAsn`, though representing 'None'.

When called on BMP messages not of type 'RouteMonitoring', the
'None'-variant is returned as well.
````

````{roto:function} contains_community(msg: BmpMsg, to_match: Community) -> bool
Check whether this message contains the given Standard Community
````

````{roto:function} contains_large_community(msg: BmpMsg, to_match: LargeCommunity) -> bool
Check whether this message contains the given Large Community
````

````{roto:function} fmt_aspath(msg: BmpMsg) -> String
Return a formatted string for the AS_PATH
````

````{roto:function} fmt_aspath_origin(msg: BmpMsg) -> String
Return a string of the AS_PATH origin for this `BmpMsg`.
````

````{roto:function} fmt_communities(msg: BmpMsg) -> String
Return a string for the Standard Communities in this `BmpMsg`.
````

````{roto:function} fmt_large_communities(msg: BmpMsg) -> String
Return a string for the Large Communities in this `BmpMsg`.
````

````{roto:function} fmt_pcap(msg: BmpMsg) -> String
Format this message as hexadecimal Wireshark input
````

````{roto:function} has_attribute(msg: BmpMsg, to_match: u8) -> bool
Check whether this message contains the given Path Attribute
````

````{roto:function} is_ibgp(msg: BmpMsg, asn: Asn) -> bool
Check whether this is an iBGP message based on a given `asn`

Return true if `asn` matches the asn in the `BmpMsg`.
returns false if no PPH is present.
````

````{roto:function} is_peer_down(msg: BmpMsg) -> bool
Check whether this message is of type 'PeerDownNotification'
````

````{roto:function} is_peer_up(msg: BmpMsg) -> bool
Check whether this message is of type 'PeerUpNotification'
````

````{roto:function} is_route_monitoring(msg: BmpMsg) -> bool
Check whether this message is of type 'RouteMonitoring'
````

````{roto:function} match_aspath_origin(msg: BmpMsg, to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:function} withdrawals_count(msg: BmpMsg) -> u64
Return the number of withdrawals in this message
````

