# Asn
`````{roto:type} Asn
An ASN: an Autonomous System Number.

An AS number can contain a number of 32-bits and is therefore similar to a [`u32`](u32).
However, AS numbers cannot be manipulated with arithmetic operations. An AS number
is constructed with the `AS` prefix followed by a number.

Can be used to store both 2-byte and 4-byte ASNs.

```roto
let a = AS0;
let b = AS1010;
let c = AS4294967295;
```
`````


````{roto:function} appears_on(asn: Asn, list: List[AsnRange]) -> bool
Check whether this ASN is in `list`.
````

````{roto:function} from_u32(v: u32) -> Asn
Create an `Asn` from a [`u32`](u32).
````

````{roto:function} to_string(self: Asn) -> String
Convert this value into a `String`.
````

