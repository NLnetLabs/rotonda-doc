# PrefixLists
`````{roto:type} PrefixLists
Named lists of prefixes
`````


````{roto:function} add(lists: PrefixLists, name: String, s: String)
Add a named prefix list
````

````{roto:function} contains(prefix_list: PrefixLists, name: String, prefix: Prefix) -> bool
Returns 'true' if `prefix` is in the named list
````

````{roto:function} covers(prefix_list: PrefixLists, name: String, prefix: Prefix) -> bool
Returns 'true' if `prefix` or a less-specific is in the named list 
````

