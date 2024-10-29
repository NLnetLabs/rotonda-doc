Composing the pipeline
======================

So, as said earlier, Rotonda can be though of as a pipeline through which BGP
data will flow. This pipeline consists of units that pass on data. All units
emit data and most of them can specify from which other unit(s) they want to
receive data. Furthermore some units can receive input from users and they can
output data through additional channels.

Let's a look at a very simple pipeline:

.. raw:: html
    
    <svg width="250px" height="60px" viewBox="0 0 250 60" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.5;">
    <g transform="matrix(0.604816,7.54528e-05,7.77417e-05,0.341212,58.818,-93.5881)">
        <path d="M55.498,362.206L183.114,362.236" style="fill:none;stroke:grey;stroke-width:2.71px;"/>
    </g>
    <g transform="matrix(0.312657,-1.91861e-34,1.91861e-34,0.312657,45.1784,-142.696)">
        <g transform="matrix(6.54662e-17,1.06914,-1.06914,6.54662e-17,706.652,426.124)">
            <circle cx="118.063" cy="552.023" r="32.375" style="fill:none;stroke:grey;stroke-width:3.99px;"/>
        </g>
        <g transform="matrix(6.12323e-17,1,-0.95722,5.86128e-17,679.794,407.483)">
            <path d="M144.867,552.35L173.274,609.165L116.46,609.165L144.867,552.35Z" style="fill:none;stroke:grey;stroke-width:4.36px;"/>
        </g>
    </g>
    <g transform="matrix(1.42869e-17,0.233324,-0.233324,1.42869e-17,305.95,2.45858)">
        <circle cx="118.063" cy="552.023" r="32.375" style="fill:none;stroke:grey;stroke-width:5.71px;"/>
    </g>
    <g transform="matrix(1.19785,0,0,1,-22.635,-433.28)">
        <text x="38.699px" y="468.584px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;">west</text>
    </g>
    <g transform="matrix(1.19785,0,0,1,145.022,-433.255)">
        <text x="38.699px" y="468.584px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;">east</text>
    </g>
    </svg>

Here you see an Ingress Unit on the left, the *west* side, and an egress unit on the right, the *east*. The BGP data flows from the west to the east. This pipeline would just take all the BGP data it gets 

A Filter and RIB Pipeline
-------------------------

This pipeline however would just move all the data through its ingress unit to the the egress unit, and that's that.

.. raw:: html

    <svg width="60%" height="60%" viewBox="0 0 350 130" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.5;">
    <path d="M112.829,77.903l36.291,0.009" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
    <path d="M163.904,77.904l25.136,0.007" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M217.384,77.921l36.777,0.009" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <g>
        <path d="M112.829,77.912c-0,7.822 -6.351,14.172 -14.172,14.172c-7.822,0 -14.172,-6.35 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.821,0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M112.829,77.912l-22.267,11.631l-0,-23.262l22.267,11.631Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <g>
        <path d="M112.829,77.912c-0,7.822 -6.351,14.172 -14.172,14.172c-7.822,0 -14.172,-6.35 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.821,0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
        <path d="M112.829,77.912l-22.267,11.631l-0,-23.262l22.267,11.631Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </g>
    <path d="M269.709,77.903c0,4.076 -3.309,7.385 -7.384,7.385c-4.076,-0 -7.385,-3.309 -7.385,-7.385c-0,-4.076 3.309,-7.385 7.385,-7.385c4.075,0 7.384,3.309 7.384,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M163.912,77.909l-14.792,8.419l0,-16.839l14.792,8.42Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <path d="M217.384,71.97c-0,-3.288 -2.67,-5.957 -5.958,-5.957l-16.429,-0c-3.288,-0 -5.957,2.669 -5.957,5.957l-0,11.915c-0,3.288 2.669,5.957 5.957,5.957l16.429,0c3.288,0 5.958,-2.669 5.958,-5.957l-0,-11.915Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    <text x="140.239px" y="49.7px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">ﬁlter</text>
    <text x="190.414px" y="49.828px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">RIB</text>
    <text x="239.729px" y="49.828px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">egress</text>
    <text x="292.406px" y="83.213px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">east</text>
    <text x="30.473px" y="83.213px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">west</text>
    <text x="73.533px" y="49.828px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">ingress</text>
    <path d="M164.217,86.328l-0.305,-16.839" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;stroke-linecap:round;"/>
    </svg>



Changing the Pipeline
---------------------

As we've briefly explained in the <<configuration default>>, Rotonda consists
of units that are connected to form a pipeline, where data flows from sources
to targets.

When you start Rotonda without a configuration file, it will use its built-in
configuration, that features a pipe-line that exists of five units, namely two
connectors (``bmp-in`` and ``bgp-in``), two RIBs (``rib-in-pre`` and
``rib-in-post``) and a terminating connector called ``null``.

The west-east flow of the default pipeline looks schematically like this:


.. raw:: html

    <svg width="276px" height="250px" viewBox="0 0 276 250" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:1.5;">
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
    </svg>

In the last chapter we saw how we could query these RIBs through the HTTP
interface, on their respective endpoints, i.e.
`<https://localhost:8080/rib-in-pre>`_ and
`<https://localhost:8080/rib-in-post/>`_. But there's more that we can do with
our pipeline. We can add and remove units at run-time. For example, we could
add another RIB to our pipeline. Let's do that.

Suppose we want to create a RIB that stores routes that have AS PAThs that
have origins only from certain autonomous systems (ASes). We'll break this down
in a few steps:

1. Start Rotonda with the default configuration, in the right directory.

We will have to make sure first that we are running Rotonda with an on-disk
configuration file, so not the built-in configuration, since the built-in
configuration cannot be changed at run-time.

If you have a Rotonda running then stop that instance, by sending it a SIGKILL
through any means, e.g. `ctrl-c` in the terminal that runs it.

If you have installed by building from source, using the `cargo install`
method (<<here>>), you should first change your working directory to the
directory mentioned in the `warning` at install time. The path probably looks
something like this: `/<USER_DIR>/.cargo/git/checkouts/rotonda-<HEX NUMBER>/<HEX NUMBER>`.

If you have installed from a package this directory is most likely,
`/etc/rotonda`. This `/etc` directory can also be found in the `Rotonda github
repo <https://github.com/nlnetlabs/rotonda>`_. Change your working directory
to one level above this `etc` directory.

You are now ready to start Rotonda by issuing:

.. code:: console

    rotonda -c etc/rotonda.example.conf

You should see output like this:

.. code:: console

    Loading new Roto script etc/bmp-in-filter.roto
    Loading new Roto script etc/rib-in-post-filter.roto
    Loading new Roto script etc/rib-in-pre-filter.roto
    Loading new Roto script etc/bgp-in-filter.roto
    Listening for HTTP connections on 127.0.0.1:8080
    Starting target 'null'
    Starting unit 'bgp-in'
    Starting unit 'rib-in-post'
    Starting unit 'bmp-in'
    Starting unit 'rib-in-pre'
    All components are ready.
    All components are running.
    bgp-in: Listening for connections on 0.0.0.0:11179
    bmp-in: Listening for connections on 0.0.0.0:11019

If you have a browser present on the system you are running Rotonda on, you
can navigate to `<http://localhost:8080/status/graph>`_ and see a graph that
describes the pipeline that we just started.

1. Modify the configuration file that is being used.

Now for the cool stuff. While leaving Rotonda running, fire up your favourite
text editor in another shell, and edit the file that we used for our
configuration, `etc/rotonda.example.conf`. Add a unit at the end of the file
like so:

.. code:: toml

    [units.my-rib]
    type = "rib"
    sources = ["rib-in-pre"]
    rib_type = "Physical"
    filter_name = "my-rib-filter"
    http_api_path = "/my-rib"

... and edit the the ``[targets.null]`` unit, and add `"my-rib"` to the
``sources`` field, like so:

.. code:: toml

    [targets.null]
    type = "null-out"
    sources = ["rib-in-post","my-rib"]

... and save the file.

1. Create the roto filter script.

Now we must still create the roto script we referenced in our modified
``rotonda.exmaple.conf``, namely the file ``my_rib.roto``. So create that
file, and fill it with this:

.. code:: text

    filter my-rib-filter {
        define {
            rx route: Route;
        }

        apply {
            accept;
        }
    }

2. SIGHUP Rotonda.

Now with everything in place we can send the HUP signal to the rotonda process:

.. code:: console

    pgrep rotonda | xargs kill -HUP

You should get new log output like this in the console that is running your Rotonda:

.. code:: console

    SIGHUP signal received, re-reading configuration file '/home/rotonda/.cargo/git/checkouts/rotonda-54306a42d783f077/8e4d152/etc/rotonda.example.conf'
    Loading new Roto script etc/my-rib.roto
    Roto script etc/bmp-in-filter.roto is already loaded and unchanged. Skipping reload
    Roto script etc/rib-in-post-filter.roto is already loaded and unchanged. Skipping reload
    Roto script etc/rib-in-pre-filter.roto is already loaded and unchanged. Skipping reload
    Roto script etc/bgp-in-filter.roto is already loaded and unchanged. Skipping reload
    Reconfiguring target 'null'
    Reconfiguring unit 'rib-in-pre'
    Starting unit 'my-rib'
    Reconfiguring unit 'bgp-in'
    Reconfiguring unit 'bmp-in'
    Reconfiguring unit 'rib-in-post'
    Configuration changes applied
    All components are ready.
    All components are running.

If you now refresh your browser tab that showed the pipeline graph, you'll see
that our new `my-rib` was added!
