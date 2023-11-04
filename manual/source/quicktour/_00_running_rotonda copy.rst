
A very simple Pipeline
~~~~~~~~~~~~~~~~~~~~~~

So, as said earlier, Rotonda can be though of as a pipeline through which BGP data will flow. This pipeline consists of units that pass on data. All units emit data and most of them can specify from which other unit(s) they want to receive data. Furthermore some units can receive input from users and they can output data through additional channels.

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
~~~~~~~~~~~~~~~~~~~~~~~~~

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