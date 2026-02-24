# AsnLists
`````{roto:type} AsnLists
Named lists of ASNs
`````


````{roto:function} add(lists: AsnLists, name: String, s: String)
Add a named ASN list
````

````{roto:function} contains(asn_list: AsnLists, name: String, asn: Asn) -> bool
Returns 'true' if `asn` is in the named list
````

````{roto:function} contains_origin(asn_list: AsnLists, name: String, origin: OriginAsn) -> bool
Returns 'true' if the named list contains `origin`

This method returns false if the list does not exist, or if `origin`
does not actually contain an `Asn`. The latter could occur for
announcements with an empty 'AS_PATH' attribute (iBGP).
````

