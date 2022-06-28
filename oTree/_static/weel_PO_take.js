        let theWheel = new Winwheel({
        'numSegments'    : 20,
        'textAlignment'  : 'outer',  // Set alignment: inner, outer, center.
        'textFontSize'   : 24,
        'textOrientation' : 'vertical', // Make text vertial so goes down from the outside of wheel.
        'outerRadius'    : 170,
        'segments'       :
        [
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'},
           {'fillStyle' : '#F78888', 'text' : 'Win'},
           {'fillStyle' : '#A8D0E6', 'text' : 'Lose'}
        ],
        'animation' :
        {
            'type'          : 'spinToStop',
            'duration'      : 10,
            'spins'         : 5,
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
        let stopAt = (181 + Math.floor((Math.random() * 16)))

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
        document.getElementById("finish").style.display="block";
    }

       function buttonAppear() {
    { $('#next').show();
    }


};