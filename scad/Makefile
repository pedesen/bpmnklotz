SCAD=$(wildcard *-event.scad) $(wildcard *-task.scad) $(wildcard *-gateway.scad)
STL=$(addprefix stl/,$(addsuffix .stl,$(basename $(SCAD))))

all: $(STL)

stl/%.stl: %.scad
	flatpak-spawn --host flatpak run org.openscad.OpenSCAD -o $@ $<
