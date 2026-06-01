# Log
`````{roto:type} Log
Machinery to create output entries.
`````


````{roto:function} entry(stream: Log) -> LogEntry
Get the current/new entry.

A `LogEntry` is only written to the output if [`write_entry`]
is called on it after populating its fields.
````

````{roto:function} log_custom(stream: Log, id: u32, local: u32)
Log a custom entry in forms of a tuple (NB: this method will
likely be removed).
````

````{roto:function} log_matched_asn(stream: Log, asn: Asn)
Log the given ASN (NB: this method will likely be removed).
````

````{roto:function} log_matched_community(stream: Log, community: Community)
Log the given community (NB: this method will likely be
removed).
````

````{roto:function} log_matched_origin(stream: Log, origin: Asn)
Log the given ASN as origin (NB: this method will likely be
removed).
````

````{roto:function} log_peer_down(stream: Log)
Log a PeerDown event.
````

````{roto:function} log_prefix(stream: Log, prefix: Prefix)
Log the given prefix (NB: this method will likely be removed).
````

````{roto:function} print(stream: Log, msg: String)
Print a message to standard error.
````

````{roto:function} timestamped_print(stream: Log, msg: String)
Print a timestamped message to standard error.
````

````{roto:function} write_entry(stream: Log)
Finalize this entry and ensure it will be written to the
output.

Calling this method will close the log entry that is currently
being composed, and ensures a subsequent call to [`entry`]
returns a new, empty `LogEntry`.
````

