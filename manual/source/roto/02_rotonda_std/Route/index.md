# Route
`````{roto:type} Route
A single announced or withdrawn path.
`````


````{roto:function} aspath(rr: Route) -> Option[AsPath]
Return the [`AsPath`](AsPath).
````

````{roto:function} communities(rr: Route) -> Option[List[Community]]
Return a `List` of `Community`s.
````

````{roto:function} fmt_base64(rr: Route) -> String
Format the path attributes as base64.
````

````{roto:function} fmt_hex(rr: Route) -> String
Format the path attributes as hex.
````

````{roto:function} fmt_json(rr: Route) -> String
Format the NLRI and path attributes as JSON.
````

````{roto:function} has_attribute(rr: Route, to_match: u8) -> bool
Check whether this `RotondaRoute` contains the given Path
Attribute.
````

````{roto:function} large_communities(rr: Route) -> Option[List[LargeCommunity]]
Return a `List` of `LargeCommunity`s.
````

````{roto:function} prefix(rr: Route) -> Prefix
Return the prefix for this `RotondaRoute`.
````

````{roto:function} prefix_matches(rr: Route, to_match: Prefix) -> bool
Check whether the prefix for this `RotondaRoute` matches.
````

````{roto:function} rov_status(rr: Route) -> RovStatus
Return the RPKI [`RovStatus`] for this Route.
````

