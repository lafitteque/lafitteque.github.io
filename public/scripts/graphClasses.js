export class MathFunction {
    constructor(f, deleteDataTimer = 0, visualizationType = "") {
        this.f = f;
        this.visualizationType = visualizationType;
    }

    plot(info) {
        var minX = info.minX;
        var maxX = info.maxX;
        var maxY = info.maxY;
        var resolution = info.resolution;
        var unitStepX = info.unitStepX;
        var unitStepY = info.unitStepY;
        var origin = info.origin;

        const step = (maxX - minX) / resolution;

        var xPosPrev = origin[0] + minX * unitStepX;
        var yPosPrev = origin[1] - this.f(minX) * unitStepY;
        for (let x = 1; x <= resolution; x++) {
            var xValue = minX + x * step;
            var xPos = origin[0] + xValue * unitStepX;
            var yPos = origin[1] - this.f(xValue) * unitStepY;
            if (this.f(xValue) > maxY) {
                continue;
            }
            line(xPos, yPos, xPosPrev, yPosPrev);
            xPosPrev = xPos;
            yPosPrev = yPos;
        }
    }

    visualisationContinuite(info, graph, a, epsilon, color = "red") {
        a =
            min(info.maxX, max(info.minX, a)) ||
            (info.minX + info.maxX) / 2;

        var delta = 1 / info.unitStepX;
        var xCount = 0.01;
        var ref = this.f(a);
        while (
            Math.abs(this.f(a - xCount) - ref) < epsilon &&
            Math.abs(this.f(a + xCount) - ref) < epsilon && xCount < 2
        ) {
            xCount += delta;
        }
        for (let x = a - xCount; x < a + xCount - 2 * delta; x += 2 * delta) {
            stroke(color);
            strokeWeight(2);
            line(x, this.f(x), x + 2 * delta, this.f(x + 2 * delta));
            var current = graph.coordToGraph(x, this.f(x));
            var next = graph.coordToGraph(x + 2 * delta, this.f(x + 2 * delta));
            line(current[0], current[1], next[0], next[1]);
        }
        graph.plotInterval(a - xCount, a + xCount, color, 2);
        push();
        strokeWeight(2);
        stroke("white");
        graph.plotPointProjections(a, this.f(a));
        //graph.plotPointProjections(a - xCount, this.f(a - xCount));
        //graph.plotPointProjections(a + xCount, this.f(a + xCount));
        pop();
    }
}
export class Graph {
    constructor(info) {
        this.info = info;
        this.functions = [];
    }

    coordToGraph(x, y) {
        return (
            [this.info.origin[0] + x * this.info.unitStepX,
            this.info.origin[1] - y * this.info.unitStepY]
        );
    }

    graphToCoord(x, y) {
        console.log("graph to coords", (x - this.info.origin[0]) / this.info.unitStepX, -(y + this.info.origin[1]) / this.info.unitStepY);
        return [(x - this.info.origin[0]) / this.info.unitStepX, -(y + this.info.origin[1]) / this.info.unitStepY];
    }

    plotPoint(x, y, pointStyle = "x", color = "white", weight = "2") {
        var newCoords = this.coordToGraph(x, y);
        push();
        stroke(color);
        if (pointStyle === "x") {
            line(
                newCoords[0] - 5,
                newCoords[1] - 5,
                newCoords[0] + 5,
                newCoords[1] + 5,
            );
            line(
                newCoords[0] + 5,
                newCoords[1] - 5,
                newCoords[0] - 5,
                newCoords[1] + 5,
            );
        } else if (pointStyle === ".") {
            strokeWeight(weight);
            point(newCoords[0], newCoords[1]);
        } else if (pointStyle === "[") {
            line(
                newCoords[0],
                newCoords[1] - 5,
                newCoords[0],
                newCoords[1] + 5,
            );
            line(
                newCoords[0],
                newCoords[1] - 5,
                newCoords[0] + 3,
                newCoords[1] - 5,
            );
            line(
                newCoords[0],
                newCoords[1] + 5,
                newCoords[0] + 3,
                newCoords[1] + 5,
            );
        } else if (pointStyle === "]") {
            line(
                newCoords[0],
                newCoords[1] - 5,
                newCoords[0],
                newCoords[1] + 5,
            );
            line(
                newCoords[0],
                newCoords[1] - 5,
                newCoords[0] - 3,
                newCoords[1] - 5,
            );
            line(
                newCoords[0],
                newCoords[1] + 5,
                newCoords[0] - 3,
                newCoords[1] + 5,
            );
        }
        pop();
    }

    plotPointProjections(x, y) {
        var newCoords = this.coordToGraph(x, y);
        line(this.info.origin[0], newCoords[1], newCoords[0], newCoords[1]);
        line(newCoords[0], newCoords[1], newCoords[0], this.info.origin[1]);
        this.plotPoint(x, y, "x", "red", "2");
    }
    plotInterval(xBegin, xEnd, color = "red", weight = 2) {
        var graphPosBegin = this.info.origin[0] + xBegin * this.info.unitStepX;
        var graphPosEnd = this.info.origin[0] + xEnd * this.info.unitStepX;
        push();
        stroke(color);
        line(graphPosBegin, this.info.origin[1], graphPosEnd, this.info.origin[1]);
        this.plotPoint(xBegin, 0, "[", color, weight);
        this.plotPoint(xEnd, 0, "]", color, weight);
        pop();
    }

    plotFunction(f, color = "blue") {
        var mathF = new MathFunction(f);
        push();
        stroke(color);
        mathF.plot(this.info);
        pop();
        if (!this.functions.includes(mathF)) {
            this.functions.push(mathF);
        }
    }

    drawGraphAxes() {
        var info = this.info;
        var minX = info.minX;
        var maxX = info.maxX;
        var minY = info.minY;
        var maxY = info.maxY;
        var offset = info.offset;
        var tickOffset = info.tickOffset;
        var gridSubdivision = info.gridSubdivision;
        var width2 = info.width2;
        var height2 = info.height2;
        var unitStepX = info.unitStepX;
        var unitStepY = info.unitStepY;
        var origin = info.origin;

        push();
        stroke(255);
        strokeWeight(2);
        //Axis
        line(offset, origin[1], width2 + offset, origin[1]);
        line(origin[0], offset, origin[0], height2 + offset);
        // Arrows
        line(width2 + offset, origin[1], width2, origin[1] + 5);
        line(width2 + offset, origin[1], width2, origin[1] - 5);
        line(origin[0], offset, origin[0] + 5, 2 * offset);
        line(origin[0], offset, origin[0] - 5, 2 * offset);
        pop();

        const tickLength = 5;
        for (let i = minX; i <= maxX; i++) {
            if (i === 0) {
                continue;
            }
            var xPos = origin[0] + i * unitStepX;
            stroke(255);
            strokeWeight(2);
            line(
                xPos,
                origin[1] - tickLength,
                xPos,
                origin[1] + tickLength,
            );
            strokeWeight(1);
            fill("white")
            text(i.toString(), xPos - 5, origin[1] + tickLength + 15);
        }
        for (let i = minY; i <= maxY; i++) {
            if (i === 0) {
                continue;
            }
            var yPos = origin[1] - i * unitStepY;
            stroke(255);
            strokeWeight(2);
            line(
                origin[0] - tickLength,
                yPos,
                origin[0] + tickLength,
                yPos,
            );
            strokeWeight(1);
            fill("white")
            text(i.toString(), origin[0] - tickLength - 15, yPos);
        }

        if (gridSubdivision === 0) {
            return;
        }

        var subUnitStepX =
            (width2 - 2 * tickOffset) / ((maxX - minX) * gridSubdivision);
        var subUnitStepY =
            (height2 - 2 * tickOffset) / ((maxY - minY) * gridSubdivision);

        for (
            let i = minX * gridSubdivision;
            i <= maxX * gridSubdivision;
            i++
        ) {
            if (i === 0) {
                continue;
            }
            var xPos = origin[0] + i * subUnitStepX;
            stroke(150);
            strokeWeight(1);
            line(xPos, tickOffset, xPos, height - tickOffset);
        }
        for (
            let i = minY * gridSubdivision;
            i <= maxY * gridSubdivision;
            i++
        ) {
            if (i === 0) {
                continue;
            }
            var yPos = origin[1] - i * subUnitStepY;
            stroke(150);
            strokeWeight(1);
            line(tickOffset, yPos, width - tickOffset, yPos);
        }
    }
}

export class GraphInfo {
    constructor(
        minX,
        maxX,
        minY,
        maxY,
        offset,
        tickOffset,
        gridSubdivision,
    ) {
        this.minX = minX;
        this.maxX = maxX;
        this.minY = minY;
        this.maxY = maxY;

        this.offset = offset;
        this.tickOffset = tickOffset;
        this.gridSubdivision = gridSubdivision;

        this.resolution = Math.floor(window.innerWidth / 2);
        this.width2 = width - 2 * offset;
        this.height2 = height - 2 * offset;
        this.unitStepX = (this.width2 - 2 * tickOffset) / (maxX - minX);
        this.unitStepY = (this.height2 - 2 * tickOffset) / (maxY - minY);

        this.origin = Array(2).fill(0);
        this.origin[0] =
            offset +
            tickOffset +
            (Math.abs(minX) / (maxX - minX)) *
            (this.width2 - 2 * tickOffset);
        this.origin[1] =
            height -
            (offset +
                tickOffset +
                (Math.abs(minY) / (maxY - minY)) *
                (this.height2 - 2 * tickOffset));
    }
}