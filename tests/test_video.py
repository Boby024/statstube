import statstube as st


def test_get_video_by_id():
    assert st.get_video_by_id(2) == 4
