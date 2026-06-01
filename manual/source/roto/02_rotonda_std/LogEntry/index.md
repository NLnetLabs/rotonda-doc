# LogEntry
`````{roto:type} LogEntry
Entry to log to file/mqtt.
`````


````{roto:function} as_path_hops(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the number of AS_PATH hops for the given message.
````

````{roto:function} conventional_reach(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the number of conventional announcements for the given
message.
````

````{roto:function} conventional_unreach(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the number of conventional withdrawals for the given
message.
````

````{roto:function} custom(entry_ptr: LogEntry, custom_msg: String)
Log a custom message based on the given string.

By setting a custom message for a `LogEntry`, all other fields
are ignored when the entry is written to the output. Combining
the custom message with the built-in fields is currently not
possible.
````

````{roto:function} log_all(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log all the built-in features for the given message.
````

````{roto:function} mp_reach(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the number of MultiProtocol announcements for the given
message.
````

````{roto:function} mp_unreach(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the number of MultiProtocol withdrawals for the given
message.
````

````{roto:function} origin_as(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the AS_PATH origin ASN for the given message.
````

````{roto:function} peer_as(entry_ptr: LogEntry, msg: BmpMsg) -> LogEntry
Log the peer ASN for the given message.
````

````{roto:function} timestamped_custom(entry_ptr: LogEntry, custom_msg: String)
Log a custom, timestamped message based on the given string.

Also see [`custom`].
````

