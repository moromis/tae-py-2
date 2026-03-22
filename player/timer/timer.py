import uuid


class Timer:

    current_time = 0
    event_queue = {}
    recurring_events = {}

    @classmethod
    def tick(cls, num_ticks=1):
        for _ in range(num_ticks):
            cls.current_time += 1
            if cls.current_time in cls.event_queue:
                # execute all events at the given time
                for id, (e, num_ticks) in cls.event_queue[cls.current_time].items():
                    e()
                    if id in cls.recurring_events:
                        cls.add_event(e, num_ticks=num_ticks, id=id)
                del cls.event_queue[cls.current_time]

    @classmethod
    def reset(cls):
        cls.current_time = 0
        cls.event_queue = {}
        cls.recurring_events = {}

    @classmethod
    def add_event(cls, event, num_ticks=1, recurring=False, id=None):
        if not id:
            id = uuid.uuid4()
        if recurring:
            cls.recurring_events[id] = (event, num_ticks)
        timeslot = cls.current_time + num_ticks
        if not timeslot in cls.event_queue:
            cls.event_queue[timeslot] = {}
        cls.event_queue[timeslot][id] = (event, num_ticks)
        return id

    @classmethod
    def get_event_queue_size(cls):
        return len(cls.event_queue)

    @classmethod
    def get_current_time(cls):
        return cls.current_time

    @classmethod
    # stops soonest matching event
    def stop_event(cls, event_id):
        for i in cls.event_queue.keys():
            if event_id in cls.event_queue[i]:
                del cls.event_queue[i][event_id]
                if len(cls.event_queue[i]) == 0:
                    del cls.event_queue[i]
                break

    @classmethod
    # stops all matching events
    def stop_events(cls, event_id):
        keys_to_del = []
        for i in cls.event_queue.keys():
            if event_id in cls.event_queue[i]:
                del cls.event_queue[i][event_id]
                if len(cls.event_queue[i]) == 0:
                    keys_to_del.append(i)
        for i in keys_to_del:
            del cls.event_queue[i]

    @classmethod
    def delete_recurring_event(cls, event_id):
        if event_id in cls.recurring_events:
            del cls.recurring_events[event_id]
