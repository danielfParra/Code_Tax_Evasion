        let theWheel = new Winwheel({
        'numSegments'    : 10,
        'textAlignment'  : 'center',  // Set alignment: inner, outer, center.
        'outerRadius'    : 170,
        'segments'       :
        [
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Do not take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'},
           {'fillStyle' : '#F78888', 'text' : 'Take'}
        ],
        'animation' :
        {
            'type'          : 'spinToStop',
            'duration'      : 5,
            'spins'         : 8,
            'callbackAfter' : 'drawTriangle()',
            'callbackFinished' : alertPrize
        }
    });

    // Function with formula to work out stopAngle before spinning animation.
    // Called from Click of the Spin button.
    function calculatePrize()
    {
        // This formula always makes the wheel stop somewhere inside prize 3 at least
        // 1 degree away from the start and end edges of the segment.
        // the first number is the angle where I am aiming. In this case starting the 3rd segment. Then
        // each segment has 36 of width and I multuplied 36*4 minus 2 to avoid to go to the line.
        let stopAt = (73 + Math.floor((Math.random() * 142)))

        // Important thing is to set the stopAngle of the animation before stating the spin.
        theWheel.animation.stopAngle = stopAt;

        // May as well start the spin from here.
        theWheel.startAnimation();
    }

    // Usual pointer drawing code.
    drawTriangle();

    function drawTriangle()
    {
        // Get the canvas context the wheel uses.
        let ctx = theWheel.ctx;

        ctx.strokeStyle = '#24305E';     // Set line colour.
        ctx.fillStyle   = '#F8E9A1';     // Set fill colour.
        ctx.lineWidth   = 2;
        ctx.beginPath();              // Begin path.
        ctx.moveTo(170, 5);           // Move to initial position.
        ctx.lineTo(230, 5);           // Draw lines to make the shape.
        ctx.lineTo(200, 40);
        ctx.lineTo(171, 5);
        ctx.stroke();                 // Complete the path by stroking (draw lines).
        ctx.fill();                   // Then fill.
    }

    function alertPrize(indicatedSegment)
    {
        // Do basic alert of the segment text. You would probably want to do something more interesting with this information.
        alert("You were matched with a Public Official who decided to take the money");
        document.getElementById("finish").style.display="block";
    }

       function buttonAppear() {
    { $('#next').show();
    }


};