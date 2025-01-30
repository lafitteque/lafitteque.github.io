const xv = 10,
        yv = 10;

    function setup() {
        createCanvas(401, 401);
        canvas.parent("sketch-holder");
        let int = createInput("x*x");
        int.elt.id = "eq";
    }

    function draw() {
        background(0);
        noFill();
        stroke(0);
        graphAxis();
        equation(select("#eq").value());
    }

    function graphAxis() {
        line(width / 2, 0, width / 2, height);
        line(0, height / 2, width, height / 2);
        var x = Math.floor(width / xv);
        var y = Math.floor(height / yv);

        for (var i = 0; i < x; i++) {
            line(i * xv, 0, i * xv, height);
        }
        for (var j = 0; j < x; j++) {
            line(0, j * yv, width, j * yv);
        }
        rect(0, 0, width - 1, height - 1);
    }

    function equation(str) {
        push();
        stroke(255, 0, 0);
        strokeWeight(3);
        translate(width / 2, height / 2);
        let w = width / xv / 2;
        beginShape();
        for (let i = -w; i < w; i += 0.01) {
            try {
                let y = eval(str.replaceAll("x", i));
                curveVertex(i * xv, -y * yv);
            } catch (e) {
                break;
            }
        }
        endShape();
        pop();
    }