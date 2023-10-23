from asciimatics.widgets import Layout, MultiColumnListBox, Widget

from aiko_services import *

__all__ = []

class RegistrarFrame(ServiceFrame):
    def __init__(self, screen, dashboard):
        super(RegistrarFrame, self).__init__(
            screen, dashboard, name="registrar_frame")

        self.services_cache = services_cache_create_singleton(
            aiko.process, True, history_limit=screen.height)

        self._registrar_widget = MultiColumnListBox(
            Widget.FILL_FRAME,
            ["<0"],
            options=[],
            titles=["Registrar: Discovered Services topic paths"]
        )
        layout_0 = Layout([1], fill_frame=True)
        self.add_layout(layout_0)
        layout_0.add_widget(self._registrar_widget)
        self.fix()  # Prepare Frame for use
        self._value_width = self._registrar_widget.width

    def _update(self, frame_no):
        super(RegistrarFrame, self)._update(frame_no)

        services = self.services_cache.get_services().copy()
        services_formatted = []
        for service in services:
            topic_path = str(ServiceTopicPath.parse(service[0]))
            protocol = service[2]  # self._short_name(service[2])
            services_formatted.append(
                (topic_path, service[1], service[4], protocol, service[3]))
        self._registrar_widget.options = [
            (service_info, row_index)
            for row_index, service_info in enumerate(services_formatted)
        ]

# plugin key can be either the Service "name" or "protocol"

plugins = {
    "registrar": RegistrarFrame
}