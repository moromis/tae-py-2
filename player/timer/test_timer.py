import unittest
from unittest.mock import MagicMock, Mock

from player.timer.timer import Timer


class TestTimer(unittest.TestCase):
    def setUp(self) -> None:
        Timer.reset()
        return super().setUp()

    def test_tick(self):
        self.assertEqual(Timer.get_current_time(), 0)
        Timer.tick()
        self.assertEqual(Timer.get_current_time(), 1)

    def test_reset(self):
        Timer.reset()
        self.assertEqual(Timer.get_current_time(), 0)
        Timer.tick()
        self.assertEqual(Timer.get_current_time(), 1)
        Timer.reset()
        self.assertEqual(Timer.get_current_time(), 0)

    def test_add_single_occurrence_event(self):
        test_event = MagicMock()
        Timer.add_event(test_event, num_ticks=2, recurring=False)
        Timer.tick(1)
        self.assertEqual(len(Timer.event_queue), 1)
        Timer.tick(1)
        self.assertEqual(len(Timer.event_queue), 0)
        test_event.assert_called_once()

    def test_add_repeating_event(self):
        test_event = Mock()
        Timer.add_event(test_event, num_ticks=2, recurring=True)
        Timer.tick(2)
        test_event.assert_called_once()
        Timer.tick(1)
        test_event.assert_called_once()
        Timer.tick(1)
        self.assertEqual(len(test_event.mock_calls), 2)

    def test_add_multiple_events(self):
        test_event = Mock()
        test_event_2 = Mock()
        Timer.add_event(test_event, num_ticks=1, recurring=False)
        Timer.add_event(test_event_2, num_ticks=1, recurring=True)
        Timer.tick(2)
        test_event.assert_called_once()
        self.assertEqual(len(test_event_2.mock_calls), 2)

    def test_stop_single_occurrence_event(self):
        test_event = Mock()
        id = Timer.add_event(test_event, num_ticks=1, recurring=False)
        Timer.add_event(test_event, num_ticks=2, recurring=False, id=id)
        Timer.add_event(test_event, num_ticks=3, recurring=False, id=id)

        self.assertEqual(Timer.get_event_queue_size(), 3)

        Timer.stop_event(id)

        self.assertEqual(Timer.get_event_queue_size(), 2)
        self.assertNotIn(1, Timer.event_queue)
        self.assertIn(2, Timer.event_queue)
        self.assertIn(3, Timer.event_queue)

    def test_stop_all_single_occurrence_event(self):
        test_event = Mock()
        id = Timer.add_event(test_event, num_ticks=1, recurring=False)
        Timer.add_event(test_event, num_ticks=2, recurring=False, id=id)
        Timer.add_event(test_event, num_ticks=3, recurring=False, id=id)

        self.assertEqual(Timer.get_event_queue_size(), 3)

        Timer.stop_events(id)

        self.assertEqual(Timer.get_event_queue_size(), 0)

    def test_stop_recurring_event(self):
        test_event = Mock()
        id = Timer.add_event(test_event, num_ticks=2, recurring=True)

        self.assertEqual(Timer.get_event_queue_size(), 1)

        Timer.stop_events(id)
        Timer.delete_recurring_event(id)

        self.assertEqual(Timer.get_event_queue_size(), 0)
        self.assertEqual(len(Timer.recurring_events), 0)
