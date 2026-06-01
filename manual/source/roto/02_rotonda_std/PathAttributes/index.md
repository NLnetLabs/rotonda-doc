# PathAttributes
`````{roto:type} PathAttributes
The Path attributes pertaining to a certain Route.

Currently only used in custom HTTP endpoint `filter`s.
`````


````{roto:function} aspath(pamap: PathAttributes) -> Option[AsPath]
Return the [`AsPath`](AsPath).
````

````{roto:function} communities(pamap: PathAttributes) -> Option[List[Community]]
Return a [`List[T]`](List) of [`Community`](Community).
````

````{roto:function} large_communities(pamap: PathAttributes) -> Option[List[LargeCommunity]]
Return a [`List[T]`](List) of [`LargeCommunity`](LargeCommunity).
````

````{roto:function} otc(pamap: PathAttributes) -> Option[Asn]
Return the OTC attribute.
````

