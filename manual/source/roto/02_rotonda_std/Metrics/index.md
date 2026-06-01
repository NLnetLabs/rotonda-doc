# Metrics
`````{roto:type} Metrics
User-defined Prometheus style metrics.
`````


````{roto:function} increase_counter(metrics: Metrics, name: String, value: u64)
Increase the counter for key `name` with `value`.
````

````{roto:function} set_gauge(metrics: Metrics, name: String, value: u64)
Set the gauge for key `name` to `value`.
````

