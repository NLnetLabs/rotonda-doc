# BgpMsg
`````{roto:type} BgpMsg
BGP UPDATE message.
`````


````{roto:function} announcements_count(msg: BgpMsg) -> u64
Return the number of announcements in this message.
````

````{roto:function} aspath(msg: BgpMsg) -> Option[AsPath]
Return the [`AsPath`](AsPath) in this message.
````

````{roto:function} communities(msg: BgpMsg) -> Option[List[Community]]
Return a [`List`](List[T]) of [`Community`](Community) in this message.
````

````{roto:function} fmt_base64(msg: BgpMsg) -> String
Format this message as base64.
````

````{roto:function} fmt_hex(msg: BgpMsg) -> String
Format this message as hex.
````

````{roto:function} fmt_pcap(msg: BgpMsg) -> String
Format this message as hexadecimal Wireshark input.
````

````{roto:function} has_attribute(msg: BgpMsg, to_match: u8) -> bool
Check whether this message contains the given Path Attribute.
````

````{roto:function} large_communities(msg: BgpMsg) -> Option[List[LargeCommunity]]
Return a [`List`](List[T]) of [`LargeCommunity`](LargeCommunity) in this message.
````

````{roto:function} withdrawals_count(msg: BgpMsg) -> u64
Return the number of withdrawals in this message.
````

