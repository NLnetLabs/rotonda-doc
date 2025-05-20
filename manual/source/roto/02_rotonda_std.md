# Standard Library

````{roto:function} community(raw: u32) -> Community
````

`````{roto:context} output: Log
`````

`````{roto:context} rpki: Rpki
`````

`````{roto:context} asn_lists: AsnLists
`````

`````{roto:context} prefix_lists: PrefixLists
`````

`````{roto:constant} NO_EXPORT_SUBCONFED: Community
The well-known NO_EXPORT_SUBCONFED community (RFC1997)
`````

`````{roto:constant} NO_PEER: Community
The well-known NO_PEER community (RFC3765)
`````

`````{roto:constant} LOCALHOSTV4: IpAddr
The IPv4 address pointing to localhost: `127.0.0.1`
`````

`````{roto:constant} LOCALHOSTV6: IpAddr
The IPv6 address pointing to localhost: `::1`
`````

`````{roto:constant} NO_EXPORT: Community
The well-known NO_EXPORT community (RFC1997)
`````

`````{roto:constant} NO_ADVERTISE: Community
The well-known NO_ADVERTISE community (RFC1997)
`````

`````{roto:type} Unit
The unit type that has just one possible value. It can be used when there is nothing meaningful to be returned.

`````

`````{roto:type} bool
The boolean type

This type has two possible values: `true` and `false`. Several boolean operations can be used with booleans, such as `&&` (logical and), `||` (logical or) and `not`.

`````

`````{roto:type} u8
The unsigned 8-bit integer type

This type can represent integers from 0 up to (and including) 255.

`````

`````{roto:type} u16
The unsigned 16-bit integer type

This type can represent integers from 0 up to (and including) 65535.

`````

`````{roto:type} u32
The unsigned 32-bit integer type

This type can represent integers from 0 up to (and including) 4294967295.

````{roto:method} u32.fmt() -> String
````

`````

`````{roto:type} u64
The unsigned 64-bit integer type

This type can represent integers from 0 up to (and including) 18446744073709551615.

`````

`````{roto:type} i8
The signed 8-bit integer type

This type can represent integers from -128 up to (and including) 127.

`````

`````{roto:type} i16
The signed 16-bit integer type

This type can represent integers from -32768 up to (and including) 32767.

`````

`````{roto:type} i32
The signed 32-bit integer type

This type can represent integers from -2147483648 up to (and including) 2147483647.

`````

`````{roto:type} i64
The signed 64-bit integer type

This type can represent integers from -9223372036854775808 up to (and including) 9223372036854775807.

`````

`````{roto:type} f32
The 4-bit floating point type

````{roto:method} f32.floor() -> f32
Returns the largest integer less than or equal to self.
````

````{roto:method} f32.ceil() -> f32
Returns the smallest integer greater than or equal to self.
````

````{roto:method} f32.round() -> f32
Returns the nearest integer to self. If a value is half-way between two integers, round away from 0.0.
````

````{roto:method} f32.abs() -> f32
Computes the absolute value of self.
````

````{roto:method} f32.sqrt() -> f32
Returns the square root of a number.
````

````{roto:method} f32.pow(y: f32) -> f32
Raises a number to a floating point power.
````

````{roto:method} f32.is_nan() -> bool
Returns true if this value is NaN.
````

````{roto:method} f32.is_infinite() -> bool
Returns true if this value is positive infinity or negative infinity, and false otherwise.
````

````{roto:method} f32.is_finite() -> bool
Returns true if this number is neither infinite nor NaN.
````

`````

`````{roto:type} f64
The 8-bit floating point type

````{roto:method} f64.floor() -> f64
Returns the largest integer less than or equal to self.
````

````{roto:method} f64.ceil() -> f64
Returns the smallest integer greater than or equal to self.
````

````{roto:method} f64.round() -> f64
Returns the nearest integer to self. If a value is half-way between two integers, round away from 0.0.
````

````{roto:method} f64.abs() -> f64
Computes the absolute value of self.
````

````{roto:method} f64.sqrt() -> f64
Returns the square root of a number.
````

````{roto:method} f64.pow(y: f64) -> f64
Raises a number to a floating point power.
````

````{roto:method} f64.is_nan() -> bool
Returns true if this value is NaN.
````

````{roto:method} f64.is_infinite() -> bool
Returns true if this value is positive infinity or negative infinity, and false otherwise.
````

````{roto:method} f64.is_finite() -> bool
Returns true if this number is neither infinite nor NaN.
````

`````

`````{roto:type} Asn
An ASN: an Autonomous System Number

An AS number can contain a number of 32-bits and is therefore similar to a [`u32`](u32). However, AS numbers cannot be manipulated with arithmetic operations. An AS number is constructed with the `AS` prefix followed by a number.

```roto
AS0
AS1010
AS4294967295
```

````{roto:method} Asn.fmt() -> String
Return the formatted string for `asn`
````

`````

`````{roto:type} IpAddr
An IP address

Can be either IPv4 or IPv6.

```roto
# IPv4 examples
127.0.0.1
0.0.0.0
255.255.255.255

# IPv6 examples
0:0:0:0:0:0:0:1
::1
::
```

````{roto:method} IpAddr.eq(b: IpAddr) -> bool
Check whether two IP addresses are equal

A more convenient but equivalent method for checking equality is via the `==` operator.

An IPv4 address is never equal to an IPv6 address. IP addresses are considered equal if
all their bits are equal.

```roto
192.0.0.0 == 192.0.0.0   # -> true
::0 == ::0               # -> true
192.0.0.0 == 192.0.0.1   # -> false
0.0.0.0 == 0::0          # -> false

# or equivalently:
192.0.0.0.eq(192.0.0.0)  # -> true
```
````

````{roto:method} IpAddr.is_ipv4() -> bool
Returns true if this address is an IPv4 address, and false otherwise.

```roto
1.1.1.1.is_ipv4() # -> true
::.is_ipv4()      # -> false
```
````

````{roto:method} IpAddr.is_ipv6() -> bool
Returns true if this address is an IPv6 address, and false otherwise.

```roto
1.1.1.1.is_ipv6() # -> false
::.is_ipv6()      # -> true
```
````

````{roto:method} IpAddr.to_canonical() -> IpAddr
Converts this address to an IPv4 if it is an IPv4-mapped IPv6 address, otherwise it returns self as-is.
````

`````

`````{roto:type} Prefix
An IP address prefix: the combination of an IP address and a prefix length

A prefix can be constructed with the `/` operator or with the [`Prefix.new`](Prefix.new) function. This operator takes an [`IpAddr`](IpAddr) and a [`u8`](u8) as operands.

            
```roto
1.1.1.0 / 8
192.0.0.0.0 / 24
```

````{roto:static_method} Prefix.new(ip: IpAddr, len: u8) -> Prefix
Construct a new prefix

A prefix can also be constructed with the `/` operator.

```roto
Prefix.new(192.169.0.0, 16)

# or equivalently
192.169.0.0 / 16
```
````

`````

`````{roto:type} String
The string type

````{roto:method} String.append(b: String) -> String
Append a string to another, creating a new string

```roto
"hello".append(" ").append("world") # -> "hello world"
```
````

````{roto:method} String.contains(needle: String) -> bool
Check whether a string contains another string

```roto
"haystack".contains("hay")  # -> true
"haystack".contains("corn") # -> false
```
````

````{roto:method} String.starts_with(prefix: String) -> bool
Check whether a string starts with a given prefix

```roto
"haystack".contains("hay")   # -> true
"haystack".contains("trees") # -> false
```
````

````{roto:method} String.ends_with(suffix: String) -> bool
Check whether a string end with a given suffix

```roto
"haystack".contains("stack") # -> true
"haystack".contains("black") # -> false
```
````

````{roto:method} String.to_lowercase() -> String
Create a new string with all characters converted to lowercase

```roto
"LOUD".to_lowercase() # -> "loud"
```
````

````{roto:method} String.to_uppercase() -> String
Create a new string with all characters converted to lowercase

```roto
"quiet".to_uppercase() # -> "QUIET"
```
````

````{roto:method} String.repeat(n: u32) -> String
Repeat a string `n` times and join them

```roto
"ha".repeat(6) # -> "hahahahahaha"
```
````

`````

`````{roto:type} Route
A single announced or withdrawn path

````{roto:method} Route.prefix() -> Prefix
Return the prefix for this `RotondaRoute`
````

````{roto:method} Route.prefix_matches(to_match: Prefix) -> bool
Check whether the prefix for this `RotondaRoute` matches
````

````{roto:method} Route.aspath_contains(to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:method} Route.match_aspath_origin(to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:method} Route.contains_community(to_match: Community) -> bool
Check whether this `RotondaRoute` contains the given Standard Community
````

````{roto:method} Route.contains_large_community(to_match: LargeCommunity) -> bool
Check whether this `RotondaRoute` contains the given Large Community
````

````{roto:method} Route.has_attribute(to_match: u8) -> bool
Check whether this `RotondaRoute` contains the given Path Attribute
````

````{roto:method} Route.fmt_prefix() -> String
Return a formatted string for the prefix
````

````{roto:method} Route.fmt_rov_status() -> String
Return a formatted string for the ROV status
````

````{roto:method} Route.fmt_aspath() -> String
Return a formatted string for the AS_PATH
````

````{roto:method} Route.fmt_aspath_origin() -> String
Return a formatted string for the AS_PATH origin
````

````{roto:method} Route.fmt_communities() -> String
Return a formatted string for the Standard Communities
````

````{roto:method} Route.fmt_large_communities() -> String
Return a formatted string for the Large Communities
````

`````

`````{roto:type} RouteContext
Contextual information pertaining to the Route

`````

`````{roto:type} Provenance
Session/state information

````{roto:method} Provenance.peer_asn() -> Asn
Return the peer ASN
````

`````

`````{roto:type} Log
Machinery to create output entries

````{roto:method} Log.log_prefix(prefix: Prefix) -> Unit
Log the given prefix (NB: this method will likely be removed)
````

````{roto:method} Log.log_matched_asn(asn: Asn) -> Unit
Log the given ASN (NB: this method will likely be removed)
````

````{roto:method} Log.log_matched_origin(origin: Asn) -> Unit
Log the given ASN as origin (NB: this method will likely be removed)
````

````{roto:method} Log.log_matched_community(community: Community) -> Unit
Log the given community (NB: this method will likely be removed)
````

````{roto:method} Log.log_peer_down() -> Unit
Log a PeerDown event
````

````{roto:method} Log.log_custom(id: u32, local: u32) -> Unit
Log a custom entry in forms of a tuple (NB: this method will likely be removed)
````

````{roto:method} Log.print(msg: String) -> Unit
Print a message to standard error
````

````{roto:method} Log.timestamped_print(msg: String) -> Unit
Print a timestamped message to standard error
````

````{roto:method} Log.entry() -> LogEntry
Get the current/new entry

A `LogEntry` is only written to the output if [`write_entry`] is
called on it after populating its fields.
````

````{roto:method} Log.write_entry() -> Unit
Finalize this entry and ensure it will be written to the output

Calling this method will close the log entry that is currently being
composed, and ensures a subsequent call to [`entry`] returns a new,
empty `LogEntry`.
````

`````

`````{roto:type} Rpki
RPKI information retrieved via RTR

````{roto:method} Rpki.check_rov(rr: Route) -> RovStatus
Perform Route Origin Validation on the route

This sets the 'rpki_info' for this Route to Valid, Invalid or
NotFound (RFC6811).

In order for this method to have effect, a 'rtr-in' connector should
be configured, and it should have received VRP data from the connected
RP software.
````

`````

`````{roto:type} VrpUpdate
A single announced or withdrawn VRP

````{roto:method} VrpUpdate.asn() -> Asn
Returns the `Asn` for this `VrpUpdate`
````

````{roto:method} VrpUpdate.prefix() -> Prefix
Returns the prefix of the updated route
````

````{roto:method} VrpUpdate.fmt() -> String
Return a formatted string for `vrp_update`
````

`````

`````{roto:type} OriginAsn
Origin ASN

Represents an optional ASN.
        

`````

`````{roto:type} AsnLists
Named lists of ASNs

````{roto:method} AsnLists.add(name: String, s: String) -> Unit
Add a named ASN list
````

````{roto:method} AsnLists.contains(name: String, asn: Asn) -> bool
Returns 'true' if `asn` is in the named list
````

````{roto:method} AsnLists.contains_origin(name: String, origin: OriginAsn) -> bool
Returns 'true' if the named list contains `origin`

This method returns false if the list does not exist, or if `origin`
does not actually contain an `Asn`. The latter could occur for
announcements with an empty 'AS_PATH' attribute (iBGP).
````

`````

`````{roto:type} PrefixLists
Named lists of prefixes

````{roto:method} PrefixLists.add(name: String, s: String) -> Unit
Add a named prefix list
````

````{roto:method} PrefixLists.contains(name: String, prefix: Prefix) -> bool
Returns 'true' if `prefix` is in the named list
````

````{roto:method} PrefixLists.covers(name: String, prefix: Prefix) -> bool
Returns 'true' if `prefix` or a less-specific is in the named list
````

`````

`````{roto:type} InsertionInfo
Information from the RIB on an inserted route

`````

`````{roto:type} LogEntry
Entry to log to file/mqtt

````{roto:method} LogEntry.custom(custom_msg: String) -> Unit
Log a custom message based on the given string

By setting a custom message for a `LogEntry`, all other fields are
ignored when the entry is written to the output. Combining the custom
message with the built-in fields is currently not possible.
````

````{roto:method} LogEntry.timestamped_custom(custom_msg: String) -> Unit
Log a custom, timestamped message based on the given string

Also see [`custom`].
````

````{roto:method} LogEntry.origin_as(msg: BmpMsg) -> LogEntry
Log the AS_PATH origin ASN for the given message
````

````{roto:method} LogEntry.peer_as(msg: BmpMsg) -> LogEntry
Log the peer ASN for the given message
````

````{roto:method} LogEntry.as_path_hops(msg: BmpMsg) -> LogEntry
Log the number of AS_PATH hops for the given message
````

````{roto:method} LogEntry.conventional_reach(msg: BmpMsg) -> LogEntry
Log the number of conventional announcements for the given message
````

````{roto:method} LogEntry.conventional_unreach(msg: BmpMsg) -> LogEntry
Log the number of conventional withdrawals for the given message
````

````{roto:method} LogEntry.mp_reach(msg: BmpMsg) -> LogEntry
Log the number of MultiProtocol announcements for the given message
````

````{roto:method} LogEntry.mp_unreach(msg: BmpMsg) -> LogEntry
Log the number of MultiProtocol withdrawals for the given message
````

````{roto:method} LogEntry.log_all(msg: BmpMsg) -> LogEntry
Log all the built-in features for the given message
````

`````

`````{roto:type} BgpMsg
BGP UPDATE message

````{roto:method} BgpMsg.aspath_contains(to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:method} BgpMsg.aspath_origin() -> OriginAsn
Returns the right-most `Asn` in the 'AS_PATH' attribute

Note that the returned value is of type `OriginAsn`, which optionally
contains an `Asn`. In case of empty an 'AS_PATH' (e.g. in iBGP) this
method will still return an `OriginAsn`, though representing 'None'.
````

````{roto:method} BgpMsg.match_aspath_origin(to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:method} BgpMsg.contains_community(to_match: Community) -> bool
Check whether this message contains the given Standard Community
````

````{roto:method} BgpMsg.contains_large_community(to_match: LargeCommunity) -> bool
Check whether this message contains the given Large Community
````

````{roto:method} BgpMsg.has_attribute(to_match: u8) -> bool
Check whether this message contains the given Path Attribute
````

````{roto:method} BgpMsg.announcements_count() -> u32
Return the number of announcements in this message
````

````{roto:method} BgpMsg.withdrawals_count() -> u32
Return the number of withdrawals in this message
````

````{roto:method} BgpMsg.fmt_aspath() -> String
Return a formatted string for the AS_PATH
````

````{roto:method} BgpMsg.fmt_aspath_origin() -> String
Return a formatted string for the AS_PATH origin
````

````{roto:method} BgpMsg.fmt_communities() -> String
Return a formatted string for the Standard Communities
````

````{roto:method} BgpMsg.fmt_large_communities() -> String
Return a formatted string for the Large Communities
````

````{roto:method} BgpMsg.fmt_pcap() -> String
Format this message as hexadecimal Wireshark input
````

`````

`````{roto:type} Community
A BGP Standard Community (RFC1997)

````{roto:static_method} Community.new(raw: u32) -> Community
````

`````

`````{roto:type} LargeCommunity
A BGP Large Community (RFC8092)

`````

`````{roto:type} BmpMsg
BMP Message

````{roto:method} BmpMsg.is_ibgp(asn: Asn) -> bool
Check whether this is an iBGP message based on a given `asn`

Return true if `asn` matches the asn in the `BmpMsg`.
returns false if no PPH is present.
````

````{roto:method} BmpMsg.is_route_monitoring() -> bool
Check whether this message is of type 'RouteMonitoring'
````

````{roto:method} BmpMsg.is_peer_down() -> bool
Check whether this message is of type 'PeerDownNotification'
````

````{roto:method} BmpMsg.aspath_contains(to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:method} BmpMsg.aspath_origin() -> OriginAsn
Returns the right-most `Asn` in the 'AS_PATH' attribute

Note that the returned value is of type `OriginAsn`, which optionally
contains an `Asn`. In case of empty an 'AS_PATH' (e.g. in iBGP) this
method will still return an `OriginAsn`, though representing 'None'.

When called on BMP messages not of type 'RouteMonitoring', the
'None'-variant is returned as well.
````

````{roto:method} BmpMsg.match_aspath_origin(to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:method} BmpMsg.contains_community(to_match: Community) -> bool
Check whether this message contains the given Standard Community
````

````{roto:method} BmpMsg.contains_large_community(to_match: LargeCommunity) -> bool
Check whether this message contains the given Large Community
````

````{roto:method} BmpMsg.has_attribute(to_match: u8) -> bool
Check whether this message contains the given Path Attribute
````

````{roto:method} BmpMsg.announcements_count() -> u32
Return the number of announcements in this message
````

````{roto:method} BmpMsg.withdrawals_count() -> u32
Return the number of withdrawals in this message
````

````{roto:method} BmpMsg.fmt_aspath() -> String
Return a formatted string for the AS_PATH
````

````{roto:method} BmpMsg.fmt_aspath_origin() -> String
Return a string of the AS_PATH origin for this `BmpMsg`.
````

````{roto:method} BmpMsg.fmt_communities() -> String
Return a string for the Standard Communities in this `BmpMsg`.
````

````{roto:method} BmpMsg.fmt_large_communities() -> String
Return a string for the Large Communities in this `BmpMsg`.
````

````{roto:method} BmpMsg.fmt_pcap() -> String
Format this message as hexadecimal Wireshark input
````

`````

`````{roto:type} PerPeerHeader
BMP Per Peer Header

`````

`````{roto:type} RovStatus
ROV status of a `Route`

````{roto:method} RovStatus.is_valid() -> bool
Returns 'true' if the status is 'Valid'
````

````{roto:method} RovStatus.is_invalid() -> bool
Returns 'true' if the status is 'Invalid'
````

````{roto:method} RovStatus.is_not_found() -> bool
Returns 'true' if the status is 'NotFound'
````

`````

`````{roto:type} RovStatusUpdate
ROV update of a `Route`

````{roto:method} RovStatusUpdate.prefix() -> Prefix
Returns the prefix of the updated route
````

````{roto:method} RovStatusUpdate.origin() -> Asn
Returns the origin `asn` from the 'AS_PATH' of the updated route
````

````{roto:method} RovStatusUpdate.peer_asn() -> Asn
Returns the peer `asn` from which the route was received
````

````{roto:method} RovStatusUpdate.has_changed() -> bool
Returns 'true' if the new status differs from the old status
````

````{roto:method} RovStatusUpdate.previous_status() -> RovStatus
Returns the old status of the route
````

````{roto:method} RovStatusUpdate.current_status() -> RovStatus
Returns the new status of the route
````

````{roto:method} RovStatusUpdate.fmt() -> String
Return a formatted string for `rov_update`
````

`````

