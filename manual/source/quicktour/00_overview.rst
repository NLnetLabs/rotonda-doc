`Rotonda` Overview
==================

Central to Rotonda is the observation that there is no one-size-fits-all
application for a network's BGP routing needs any more. As networks are
growing, so is their complexity, and as a consequence BGP is being used in
more places. Since BGP has reached so many places it has turned into a generic
container for information about network nodes. Pressure on BGP to offer
security features increased the complexity of BGP deployments. By now, the
notion of a 'BGP speaker' (RFC4271) with a fixed set of 'Routing Information
Bases' (RIBs) with prescribed behaviour is only one of many different BGP
functions that we can identify in a network.

A very simple Pipeline
~~~~~~~~~~~~~~~~~~~~~~

So, as said earlier, Rotonda can be thought of as a pipeline through which BGP
data will flow. This pipeline consists of units that pass on data. All units
emit data and most of them can specify from which other unit(s) they want to
receive data. Furthermore some units can receive input from users and they can
output data through additional channels.

Let's take a look at a very simple pipeline:

.. raw:: html
    
    <svg width="242px" height="50px + 10%" viewBox="0 0 242 49" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
    <path d="M78.613,33.76l100.077,0.026" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
    <g>
        <g>
            <path d="M78.613,34.081c0,7.822 -6.35,14.172 -14.172,14.172c-7.822,0 -14.172,-6.35 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.822,0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        </g>
        <path d="M70.654,34.072l-12.426,7.385l0,-14.77l12.426,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <path d="M70.921,41.47l-0.267,-14.769" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
    </g>
    <path d="M193.459,33.778c0,4.076 -3.309,7.385 -7.384,7.385c-4.076,-0 -7.385,-3.309 -7.385,-7.385c-0,-4.076 3.309,-7.385 7.385,-7.385c4.075,0 7.384,3.309 7.384,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
    <text x="39.357px" y="11.672px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">ingress</text>
    <text x="163.479px" y="11.672px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">egress</text>
    <text x="-0.648px" y="39.385px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">west</text>
    <text x="214.603px" y="37.129px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">east</text>
    </svg>

Here you see an Ingress Unit on the left, the *west* side, and an egress unit on the right, the *east*. The BGP data flows from the west to the east. This pipeline would just take all the BGP data it gets 

A Pipeline with a RIB
~~~~~~~~~~~~~~~~~~~~~

This pipeline however would just move all the data through its ingress unit to the the egress unit, and that's that.

.. raw:: html

    <svg width="242px" height="50px" viewBox="0 0 242 49" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
        <path d="M78.613,34.073l30.983,0.008" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <path d="M147.707,33.778l30.983,0.008" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <g>
            <g>
                <path d="M78.613,34.081c0,7.822 -6.35,14.172 -14.172,14.172c-7.822,0 -14.172,-6.35 -14.172,-14.172c-0,-7.822 6.35,-14.172 14.172,-14.172c7.822,0 14.172,6.35 14.172,14.172Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            </g>
            <path d="M70.654,34.072l-12.426,7.385l0,-14.77l12.426,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M70.921,41.47l-0.267,-14.769" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        </g>
        <path d="M193.459,33.778c0,4.076 -3.309,7.385 -7.384,7.385c-4.076,-0 -7.385,-3.309 -7.385,-7.385c-0,-4.076 3.309,-7.385 7.385,-7.385c4.075,0 7.384,3.309 7.384,7.385Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <g>
            <g>
                <path d="M147.707,27.829c0,-3.288 -2.669,-5.958 -5.957,-5.958l-25.204,0c-3.288,0 -5.958,2.67 -5.958,5.958l0,11.914c0,3.288 2.67,5.958 5.958,5.958l25.204,-0c3.288,-0 5.957,-2.67 5.957,-5.958l0,-11.914Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            </g>
            <path d="M126.572,33.786l-10.844,6.445l0,-12.89l10.844,6.445Z" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M126.841,40.231l-0.233,-12.89" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M143.084,30.142c0,-1.546 -1.255,-2.801 -2.8,-2.801l-5.601,0c-1.545,0 -2.8,1.255 -2.8,2.801l-0,7.288c-0,1.546 1.255,2.801 2.8,2.801l5.601,-0c1.545,-0 2.8,-1.255 2.8,-2.801l0,-7.288Z" style="fill-opacity:0;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M131.887,29.85c-0.016,1.306 -0.057,2.24 1.617,2.716c0.827,0.235 2.072,0.358 3.946,0.358c5.666,-0 5.659,-0.875 5.63,-2.716" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        </g>
        <text x="39.357px" y="11.672px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">ingress</text>
        <text x="163.479px" y="11.672px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">egress</text>
        <text x="112.24px" y="11.848px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">pRIB</text>
        <text x="-0.648px" y="39.385px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">west</text>
        <text x="214.603px" y="37.129px" style="font-family:'Lato-Italic', 'Lato', sans-serif;font-style:italic;font-size:16px;fill:rgb(128,128,128);">east</text>
    </svg>

Filters
~~~~~~~

bla bla 

.. raw:: html

    <svg width="350px" height="242px" viewBox="0 0 350 242" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/" style="fill-rule:evenodd;clip-rule:evenodd;stroke-linecap:round;stroke-linejoin:round;stroke-miterlimit:1.5;">
        <rect x="96.58" y="103.133" width="42.412" height="39.911" style="fill:rgb(128,128,128);"/>
        <path d="M126.827,122.867l-18.625,11.068l0,-22.137l18.625,11.069Z" style="fill:none;stroke:white;stroke-width:1.33px;"/>
        <path d="M127.227,133.956l-0.4,-22.137" style="fill:none;stroke:white;stroke-width:1.33px;"/>
        <text x="-1.168px" y="126.073px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">pa<tspan x="15.52px " y="126.073px ">y</tspan>load</text>
        <g transform="matrix(1,0,0,1,48.5167,112.687)">
            <text x="135.051px" y="12.613px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">(tr<tspan x="151.963px " y="12.613px ">a</tspan>nsformed) pa<tspan x="251.691px " y="12.613px ">y</tspan>load +</text>
            <text x="135.051px" y="28.613px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">AcceptReject</text>
        </g>
        <text x="66.938px" y="238.464px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">output stream</text>
        <text x="45.418px" y="11.784px" style="font-family:'Lato-Regular', 'Lato', sans-serif;font-size:16px;fill:rgb(128,128,128);">e<tspan x="53.322px " y="11.784px ">x</tspan>ternal data source</text>
        <path d="M85.764,127.556l4.528,-4.472l-4.472,-4.528" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;stroke-linejoin:miter;stroke-miterlimit:10;"/>
        <path d="M90.292,123.084c-4.841,-0.03 -32.897,-0.204 -32.897,-0.204" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;"/>
        <path d="M173.645,127.353l4.527,-4.473l-4.472,-4.527" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;stroke-linejoin:miter;stroke-miterlimit:10;"/>
        <path d="M178.172,122.88l-33.603,-0.207" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;"/>
        <path d="M113.286,92.773l4.5,4.5l4.5,-4.5" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;stroke-linejoin:miter;stroke-miterlimit:10;"/>
        <path d="M117.786,97.273l-0,-33.605" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;"/>
        <path d="M113.286,177.994l4.5,4.5l4.5,-4.5" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;stroke-linejoin:miter;stroke-miterlimit:10;"/>
        <path d="M117.786,182.494l-0,-33.604" style="fill:none;stroke:rgb(128,128,128);stroke-width:1px;"/>
        <path d="M133.304,28.354c-0,-4.283 -3.477,-7.76 -7.759,-7.76l-15.518,0c-4.283,0 -7.759,3.477 -7.759,7.76l-0,20.194c-0,4.283 3.476,7.76 7.759,7.76l15.518,-0c4.282,-0 7.759,-3.477 7.759,-7.76l-0,-20.194Z" style="fill-opacity:0;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <path d="M102.278,27.546c-0.043,3.617 -0.156,6.207 4.481,7.524c2.291,0.651 5.741,0.991 10.933,0.991c15.701,0 15.68,-2.423 15.602,-7.524" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        <g>
            <rect x="94.134" y="194.352" width="47.303" height="22.028" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M141.437,194.352l-24.343,11.014" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
            <path d="M94.134,194.352l22.96,11.014" style="fill:none;stroke:rgb(128,128,128);stroke-width:1.33px;"/>
        </g>
    </svg>
