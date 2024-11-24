from CodeBase.fileIO.CommonFormat.CFLayer.CFShapes.cf_curve_parent import CFCurveParent


class CFCircle(CFCurveParent):
    def __init__(self, unit, center_pt, radius, inner_radius=None):
        # SEE CurrentCFCheatSheat.PNG in
        # ...CFLayer/Additive/AdditiveTrace/Trace/CurrentCFCheatSheat.png
        list_of_points = 30
        super().__init__(unit, list_of_points)
        self.type = "cir"
        self.center_pt = center_pt
        self.radius = radius
        # If = 0, entire circle is filled. If else, there is a hole in the middle of circle
        if inner_radius > radius:
            raise ValueError(f"CFCircle: Inner Radius of {inner_radius} is larger than the outer radius of {radius}.")
        self.inner_radius = inner_radius

        self.list_of_inner_pts = []

    def _calculate_extreme_points(self):
        #
        if self.extreme_points is None:
            self._calculate_points_on_curve()
        self.extreme_points.append(self.list_of_outer_pts)
        self.extreme_points.append(self.list_of_inner_pts)

    def _calculate_points_on_curve(self):
        self.list_of_outer_pts = self._generate_circular_points(self.center_pt, self.radius)
        if self.inner_radius is not None:
            self.list_of_inner_pts = self._generate_circular_points(self.center_pt, self.radius)

    def change_unit(self, new_unit):
        conversion_factor = None
        if new_unit == "mm":
            conversion_factor = 0.0393701
        else:
            conversion_factor: 25.4
        self.center_pt = tuple(element * conversion_factor for element in self.center_pt)
        self.radius = self.radius * conversion_factor
        self.inner_radius = self.inner_radius * conversion_factor
        self.list_of_inner_pts = tuple(element * conversion_factor for element in self.list_of_inner_pts)
        self.list_of_outer_pts = tuple(element * conversion_factor for element in self.list_of_outer_pts)
        self.unit = new_unit
