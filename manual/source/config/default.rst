Default Configuration (MVP)
===========================

The default Pipeline
~~~~~~~~~~~~~~~~~~~~

Now about the actual pipeline that was started. A Rotonda pipeline is loosely based on the way BGP packets flow through a BGP speaker according to :RFC:`4271`, but without the prescribed RIBs. In Rotonda RIBs can be added or  omitted at will by the user. You can read more about the concept of the Rotonda pipelines, and the units that it is comprised of in the <<introduction>>.

Now, our the default pipeline looks like this:

Fig 1. The MVP default Pipeline

.. raw:: html

    <svg width="276px" height="250px" style="margin-bottom: 12px;" viewBox="0 0 276 250" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.5;">
    <rect x="137.904" y="80.036" width="137.904" height="169.683" style="fill:white;"/>
    <path d="M36.627,14.829l54.011,0.014" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
    <path d="M127.757,14.844l39.806,0.01" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M204.882,14.844l51.468,0.013" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <path d="M36.627,14.839c-0,7.821 -6.35,14.172 -14.172,14.172c-7.822,-0 -14.172,-6.351 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.822,-0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <g>
        <path d="M36.627,86.476c-0,7.821 -6.35,14.172 -14.172,14.172c-7.822,-0 -14.172,-6.351 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.822,-0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <path d="M271.12,14.844c-0,4.076 -3.309,7.385 -7.385,7.385c-4.076,-0 -7.385,-3.309 -7.385,-7.385c0,-4.076 3.309,-7.385 7.385,-7.385c4.076,0 7.385,3.309 7.385,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <path d="M199.814,12.973c-0,2.517 -2.044,4.56 -4.561,4.56c-2.517,0 -4.56,-2.043 -4.56,-4.56c-0,-2.517 2.043,-4.561 4.56,-4.561c2.517,0 4.561,2.044 4.561,4.561Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M191.645,16.581l-4.803,4.803" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <g>
        <path d="M180.469,205.333c-0,2.021 -1.744,3.662 -3.892,3.662c-2.148,-0 -3.892,-1.641 -3.892,-3.662c0,-2.021 1.744,-3.661 3.892,-3.661c2.148,-0 3.892,1.64 3.892,3.661Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M173.498,208.23l-4.099,3.856" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <path d="M174.598,229.29c-0,3.286 -2.668,5.954 -5.954,5.954c-3.286,0 -5.953,-2.668 -5.953,-5.954c-0,-3.285 2.667,-5.953 5.953,-5.953c3.286,-0 5.954,2.668 5.954,5.953Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <path d="M127.757,8.899c0,-3.288 -2.669,-5.957 -5.957,-5.957l-25.204,0c-3.288,0 -5.958,2.669 -5.958,5.957l0,11.915c0,3.288 2.67,5.958 5.958,5.958l25.204,-0c3.288,-0 5.957,-2.67 5.957,-5.958l0,-11.915Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <path d="M28.668,14.829l-12.426,7.385l-0,-14.769l12.426,7.384Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M28.935,22.228l-0.267,-14.769" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <path d="M28.534,86.469l-12.426,7.384l0,-14.769l12.426,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M28.802,93.867l-0.268,-14.769" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <g>
        <path d="M28.534,86.469l-12.426,7.384l0,-14.769l12.426,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M28.802,93.867l-0.268,-14.769" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <g>
        <g>
            <path d="M177.976,153.558c-0,6.306 -5.12,11.426 -11.426,11.426c-6.305,-0 -11.425,-5.12 -11.425,-11.426c-0,-6.306 5.12,-11.425 11.425,-11.425c6.306,-0 11.426,5.119 11.426,11.425Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        </g>
        <g>
            <path d="M171.452,153.553l-10.018,5.953l-0,-11.907l10.018,5.954Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
            <path d="M171.667,159.517l-0.215,-11.907" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        </g>
        <g>
            <path d="M171.452,153.553l-10.018,5.953l-0,-11.907l10.018,5.954Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
            <path d="M171.667,159.517l-0.215,-11.907" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        </g>
    </g>
    <g>
        <path d="M172.708,129.804l-10.017,5.953l-0,-11.907l10.017,5.954Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M172.924,135.768l-0.216,-11.907" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <text x="192.285px" y="132.075px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">ﬁlter</text>
    <g transform="matrix(1,0,0,1,56.9538,91.282)">
        <text x="135.051px" y="12.613px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">UNITS</text>
        <rect x="135.051" y="13.453" width="34.956" height="0.72" style="fill:rgb(128,128,128);"/>
    </g>
    <text x="191.997px" y="232.382px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">egress</text>
    <text x="191.437px" y="156.116px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">ingress</text>
    <text x="191.285px" y="184.074px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">ph<tspan x="204.389px " y="184.074px ">y</tspan>sical RIB</text>
    <text x="192.333px" y="210.515px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:12px;fill:rgb(128,128,128);">virtual RIB</text>
    <path d="M183.348,14.857l-10.844,6.444l-0,-12.889l10.844,6.445Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M183.348,14.857l-10.844,6.444l-0,-12.889l10.844,6.445Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M204.682,8.899c0,-3.288 -2.669,-5.957 -5.957,-5.957l-25.204,0c-3.288,0 -5.958,2.669 -5.958,5.957l0,11.915c0,3.288 2.67,5.958 5.958,5.958l25.204,-0c3.288,-0 5.957,-2.67 5.957,-5.958l0,-11.915Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M183.617,21.301l-0.233,-12.889" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M106.668,14.857l-10.844,6.444l-0,-12.889l10.844,6.445Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M106.937,21.301l-0.234,-12.889" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <text x="-0.632px" y="47.922px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">bmp-in</text>
    <text x="-0.632px" y="121.269px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">bgp-in</text>
    <text x="79.35px" y="47.922px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">rib-in-pr<tspan x="133.414px " y="47.922px ">e</tspan></text>
    <text x="152.802px" y="47.922px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">rib-in-post</text>
    <text x="251.655px" y="47.922px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">null</text>
    <g>
        <path d="M166.85,206.891l-8.742,5.195l-0,-10.391l8.742,5.196Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M166.85,206.891l-8.742,5.195l-0,-10.391l8.742,5.196Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M184.05,202.088c-0,-2.651 -2.152,-4.803 -4.803,-4.803l-20.319,0c-2.651,0 -4.803,2.152 -4.803,4.803l-0,9.606c-0,2.65 2.152,4.803 4.803,4.803l20.319,-0c2.651,-0 4.803,-2.153 4.803,-4.803l-0,-9.606Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M167.067,212.086l-0.188,-10.391" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <path d="M36.627,86.474c54.885,0.605 -0.825,-72.131 54.011,-71.617" style="fill-opacity:0;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M123.179,11.213c0,-1.546 -1.254,-2.801 -2.8,-2.801l-5.601,0c-1.545,0 -2.8,1.255 -2.8,2.801l0,7.288c0,1.546 1.255,2.8 2.8,2.8l5.601,0c1.546,0 2.8,-1.254 2.8,-2.8l0,-7.288Z" style="fill-opacity:0;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M111.982,10.921c-0.016,1.305 -0.057,2.24 1.617,2.716c0.827,0.235 2.072,0.357 3.946,0.357c5.667,0 5.659,-0.874 5.631,-2.715" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <g>
            <path d="M183.05,176.612c-0,-2.651 -2.152,-4.803 -4.803,-4.803l-20.319,-0c-2.651,-0 -4.803,2.152 -4.803,4.803l-0,9.605c-0,2.651 2.152,4.803 4.803,4.803l20.319,0c2.651,0 4.803,-2.152 4.803,-4.803l-0,-9.605Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        </g>
        <path d="M166.048,181.415l-8.743,5.195l0,-10.391l8.743,5.196Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M166.264,186.61l-0.188,-10.391" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M179.359,178.477c0,-1.246 -1.011,-2.258 -2.257,-2.258l-4.515,-0c-1.246,-0 -2.258,1.012 -2.258,2.258l-0,5.876c-0,1.246 1.012,2.257 2.258,2.257l4.515,0c1.246,0 2.257,-1.011 2.257,-2.257l0,-5.876Z" style="fill-opacity:0;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M170.332,178.242c-0.013,1.052 -0.046,1.805 1.304,2.189c0.666,0.189 1.67,0.288 3.181,0.288c4.568,0 4.562,-0.705 4.539,-2.189" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>

The pipeline flows from the west to the east. On the west it has two ingress connectors, one for BMP sessions and one for BGP sessions. The RIB labeled ``rib-in-pre`` gets its input from those two connectors. Furthermore, it is a physical RIB, a RIB that actually stores the routes that come in. It passes the routes it receives on to ``rib-in-post``, which is a Virtual RIB: A RIB that doesn’t store anything itself, but just queries the physical RIB to the west with the requested prefix and then applies its only filter to it. Each connector and RIB, be it physical or virtual, has its own filter defined: the filters mentioned in the log lines on STDOUT that we saw earlier on. A total of 4 filters are thus used.

Both the RIBs can queried through a HTTP JSON API 

API endpoints
~~~~~~~~~~~~~

/metrics
/status
/status/graph

/bmp-routers
/rib-in-pre/{prefix}/[?include=moreSpecifics/lessSpecifics]
/rib-in-post/