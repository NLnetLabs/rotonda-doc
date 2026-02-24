# RovStatusUpdate
`````{roto:type} RovStatusUpdate
ROV update of a `Route`
`````


````{roto:function} current_status(rov_update: RovStatusUpdate) -> RovStatus
Returns the new status of the route
````

````{roto:function} fmt(rov_update: RovStatusUpdate) -> String
Return a formatted string for `rov_update`
````

````{roto:function} has_changed(rov_update: RovStatusUpdate) -> bool
Returns 'true' if the new status differs from the old status
````

````{roto:function} origin(rov_update: RovStatusUpdate) -> Asn
Returns the origin `asn` from the 'AS_PATH' of the updated route
````

````{roto:function} peer_asn(rov_update: RovStatusUpdate) -> Asn
Returns the peer `asn` from which the route was received
````

````{roto:function} prefix(rov_update: RovStatusUpdate) -> Prefix
Returns the prefix of the updated route
````

````{roto:function} previous_status(rov_update: RovStatusUpdate) -> RovStatus
Returns the old status of the route
````

