all: stl/end-event.stl stl/exclusive-gateway.stl stl/end-event.stl stl/exclusive-gateway.stl stl/inclusive-gateway.stl stl/service-task.stl stl/start-event.stl stl/user-task.stl

stl/%.stl: %.scad
	flatpak-spawn --host flatpak run org.openscad.OpenSCAD -o $@ $<
