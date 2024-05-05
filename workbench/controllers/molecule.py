# from loguru import logger
# from dash import callback
# from dash import Input, Output, ctx, ALL, State
#
# from views.molecule import render_target_molecule, render_selected_molecule
# from topics import Topics
#
#
# @callback(
#     Output(
#         "target_molecule_view",
#         "children"
#     ),
#     Topics.Slots.target_molecule.get_input("data"),
#     State(
#         "viewport",
#         "data"
#     ),
# )
# def input_molecule(molecule, viewport):
#     logger.info(f"input molecule {molecule}")
#     return render_target_molecule(molecule, viewport)
#
#
# @callback(
#     Output(
#         "selected_molecule_view",
#         "children"
#     ),
#     Input(
#         {
#             "view": "editor-main",
#             "job": ALL,
#             "route": ALL
#         },
#         "selectionEvent"
#     ),
#     State("viewport", "data"),
#     prevent_initial_call=True
# )
# def select_event(events, viewport):
#     logger.info(f"selected event {events}")
#     if (
#             events and
#             events[0]
#     ):
#         event = events[0]
#         event_type = event.get('type')
#         if event_type != "node":
#             logger.info(f"skip type {event_type} event for now.")
#         nodes = event.get("nodes")
#         if not nodes or len(nodes) < 1:
#             logger.warning(f"skip type {event_type} event due to no nodes found.")
#             return
#         return render_selected_molecule(nodes[0], viewport)
