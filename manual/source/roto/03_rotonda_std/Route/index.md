# Route
`````{roto:type} Route
A single announced or withdrawn path
`````


````{roto:function} aspath_contains(rr: Route, to_match: Asn) -> bool
Check whether the AS_PATH contains the given `Asn`
````

````{roto:function} contains_community(rr: Route, to_match: Community) -> bool
Check whether this `RotondaRoute` contains the given Standard Community
````

````{roto:function} contains_large_community(rr: Route, to_match: LargeCommunity) -> bool
Check whether this `RotondaRoute` contains the given Large Community
````

````{roto:function} fmt_aspath(rr: Route) -> String
Return a formatted string for the AS_PATH
````

````{roto:function} fmt_aspath_origin(rr: Route) -> String
Return a formatted string for the AS_PATH origin
````

````{roto:function} fmt_communities(rr: Route) -> String
Return a formatted string for the Standard Communities
````

````{roto:function} fmt_large_communities(rr: Route) -> String
Return a formatted string for the Large Communities
````

````{roto:function} fmt_prefix(rr: Route) -> String
Return a formatted string for the prefix
````

````{roto:function} fmt_rov_status(rr: Route) -> String
Return a formatted string for the ROV status
````

````{roto:function} has_attribute(rr: Route, to_match: u8) -> bool
Check whether this `RotondaRoute` contains the given Path Attribute
````

````{roto:function} match_aspath_origin(rr: Route, to_match: Asn) -> bool
Check whether the AS_PATH origin matches the given `Asn`
````

````{roto:function} prefix(rr: Route) -> Prefix
Return the prefix for this `RotondaRoute`
````

````{roto:function} prefix_matches(rr: Route, to_match: Prefix) -> bool
Check whether the prefix for this `RotondaRoute` matches
````

