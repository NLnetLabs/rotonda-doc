# Community
`````{roto:type} Community
A BGP Standard Community (RFC1997).
`````


`````{roto:constant} BLACKHOLE: Community
`````

`````{roto:constant} NO_ADVERTISE: Community
`````

`````{roto:constant} NO_EXPORT: Community
`````

`````{roto:constant} NO_EXPORT_SUBCONFED: Community
`````

`````{roto:constant} NO_PEER: Community
`````

````{roto:function} from(s: String) -> Community
Parse a `Community` from a string.
````

````{roto:function} to_string(c: Community) -> String
Return the string representation.
````

