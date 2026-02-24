# BgpMsg
`````{roto:type} BgpMsg
BGP UPDATE message
`````


````{roto:function} announcements_count(msg: BgpMsg) -> u64
Return the number of announcements in this message
````

````{roto:function} aspath_contains(msg: BgpMsg, to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:function} aspath_origin(msg: BgpMsg) -> OriginAsn
Returns the right-most `Asn` in the 'AS_PATH' attribute

Note that the returned value is of type `OriginAsn`, which optionally
contains an `Asn`. In case of empty an 'AS_PATH' (e.g. in iBGP) this
method will still return an `OriginAsn`, though representing 'None'.
````

````{roto:function} contains_community(msg: BgpMsg, to_match: Community) -> bool
Check whether this message contains the given Standard Community
````

````{roto:function} contains_large_community(msg: BgpMsg, to_match: LargeCommunity) -> bool
Check whether this message contains the given Large Community
````

````{roto:function} fmt_aspath(msg: BgpMsg) -> String
Return a formatted string for the AS_PATH
````

````{roto:function} fmt_aspath_origin(msg: BgpMsg) -> String
Return a formatted string for the AS_PATH origin
````

````{roto:function} fmt_communities(msg: BgpMsg) -> String
Return a formatted string for the Standard Communities
````

````{roto:function} fmt_large_communities(msg: BgpMsg) -> String
Return a formatted string for the Large Communities
````

````{roto:function} fmt_pcap(msg: BgpMsg) -> String
Format this message as hexadecimal Wireshark input
````

````{roto:function} has_attribute(msg: BgpMsg, to_match: u8) -> bool
Check whether this message contains the given Path Attribute
````

````{roto:function} match_aspath_origin(msg: BgpMsg, to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:function} withdrawals_count(msg: BgpMsg) -> u64
Return the number of withdrawals in this message
````

