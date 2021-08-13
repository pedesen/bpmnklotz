include <./lib/bpmn-coasters.scad>

task("service task", "", aruco=[ // 1
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
]);
