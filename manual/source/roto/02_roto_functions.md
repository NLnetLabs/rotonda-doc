# Standard Library

`````{roto:type} Unit
The unit type that has just 1 value.

`````

`````{roto:type} bool
The boolean type

The size of this type is 1 byte and it has two possible values: `true` and `false`.

`````

`````{roto:type} u8
An unsigned 8-bit integer

`````

`````{roto:type} u16
An unsigned 16-bit integer

`````

`````{roto:type} u32
An unsigned 32-bit integer

`````

`````{roto:type} u64
An unsigned 64-bit integer

`````

`````{roto:type} i8
A signed 8-bit integer

`````

`````{roto:type} i16
A signed 16-bit integer

`````

`````{roto:type} i32
A signed 32-bit integer

`````

`````{roto:type} i64
A signed 64-bit integer

`````

`````{roto:type} Asn
An ASN: an Autonomous System Number

`````

`````{roto:type} IpAddr
An IP address

Can be both IPv4 or IPv6.

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

````{roto:static_method} Prefix.new(ip: IpAddr, len: u8) -> Prefix
Construct a new prefix
````

`````

