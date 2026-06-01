# AsPath
`````{roto:type} AsPath
AS_PATH path attribute.
`````


````{roto:function} contains(hoppath: AsPath, asn: Asn) -> bool
Return true if `asn` occurs in this [`AsPath`](AsPath).
````

````{roto:function} origin(hoppath: AsPath) -> Option[Asn]
Return the (right-most) originator [`Asn`](Asn).
````

````{roto:function} to_string(hoppath: AsPath) -> String
Return a string representation.
````

