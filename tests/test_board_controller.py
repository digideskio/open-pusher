import unittest
from mock import MagicMock
from boards import BoardsController


class BoardsControllerTest(unittest.TestCase):

    def setUp(self):
        self.boards_controller = BoardsController()

    def test_register(self):
        channel_id = "xxx"
        handle = MagicMock()

        self.boards_controller.register(channel_id, handle)

        assert handle in self.boards_controller.get_board_handles(channel_id)

    def test_unregister_handle_from_channel(self):
        channel_id = "xxx"
        handle = MagicMock()
        self.boards_controller.register(channel_id, handle)

        self.boards_controller.unregister(handle, channel_id)

        assert handle not in self.boards_controller.get_board_handles(channel_id)

    def test_unregister_handle(self):
        channel_id = "xxx"
        handle = MagicMock()
        self.boards_controller.register(channel_id, handle)

        self.boards_controller.unregister(handle)

        assert handle not in self.boards_controller.get_board_handles(channel_id)

    def test_routing_move_message_to_right_channel(self):
        sender_handle = MagicMock()
        handle = MagicMock()

        expected_channel_id = 1
        self.boards_controller.register(expected_channel_id, handle)

        self.boards_controller.on_message(sender_handle, '{"type":"move", "args": {"channel_id":1, "postit_id":1, "x":10, "y":20}}')

        assert handle.send.call_count == 1

