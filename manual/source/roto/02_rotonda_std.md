# Standard Library

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

`````{roto:type} Asn
An ASN: an Autonomous System Number

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
An IP address prefix: an IP address and a prefix length

A prefix can be constructed with the `/` operator or with the `Prefix.new` function.

```roto
1.1.1.0 / 8
192.0.0.0.0 / 24
```

````{roto:static_method} Prefix.new(ip: IpAddr, len: u8) -> Prefix
Construct a new prefix

A prefix can also be constructed with a prefix literal.

```roto
Prefix.new(192.169.0.0)
```
````

`````

`````{roto:type} Route
A single announced or withdrawn path

````{roto:method} Route.prefix_matches(to_match: Prefix) -> bool
````

````{roto:method} Route.aspath_origin(to_match: Asn) -> bool
````

````{roto:method} Route.has_attribute(to_match: u8) -> bool
````

`````

`````{roto:type} RouteContext
Contextual information pertaining to the Route

`````

`````{roto:type} Provenance
Session/state information

`````

`````{roto:type} Log
Machinery to create output entries

````{roto:method} Log.log_prefix(prefix: Prefix) -> Unit
````

````{roto:method} Log.log_matched_asn(asn: Asn) -> Unit
````

````{roto:method} Log.log_matched_origin(origin: Asn) -> Unit
````

````{roto:method} Log.log_matched_community(community: u32) -> Unit
````

````{roto:method} Log.log_peer_down() -> Unit
````

````{roto:method} Log.log_custom(id: u32, local: u32) -> Unit
````

`````

`````{roto:type} InsertionInfo
Information from the RIB on an inserted route

````{roto:method} InsertionInfo.new_peer() -> bool
````

````{roto:method} InsertionInfo.prefix_new() -> bool
````

`````

`````{roto:type} BgpMsg
BGP UPDATE message

````{roto:method} BgpMsg.aspath_contains(to_match: Asn) -> bool
````

````{roto:method} BgpMsg.aspath_origin(to_match: Asn) -> bool
````

````{roto:method} BgpMsg.contains_community(to_match: u32) -> bool
````

````{roto:method} BgpMsg.has_attribute(to_match: u8) -> bool
````

`````

`````{roto:type} BmpMsg
BMP Message

````{roto:method} BmpMsg.is_ibgp(asn: Asn) -> bool
````

````{roto:method} BmpMsg.is_peer_down() -> bool
````

````{roto:method} BmpMsg.aspath_contains(to_match: Asn) -> bool
````

````{roto:method} BmpMsg.aspath_origin(to_match: Asn) -> bool
````

````{roto:method} BmpMsg.contains_community(to_match: u32) -> bool
````

````{roto:method} BmpMsg.has_attribute(to_match: u8) -> bool
````

`````

`````{roto:type} PerPeerHeader
BMP Per Peer Header

`````

