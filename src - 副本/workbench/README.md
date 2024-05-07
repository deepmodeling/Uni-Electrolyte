# Retro Synthesis Dash Workbench

## TODO
关注点分离，尽量减少副作用。
- controller -- for UI control(maybe triggerred by UI change or topic)
- topic producer -- create topic events
- topic consumer -- consume topic and do business logic
- components