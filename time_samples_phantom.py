"""Replay HDF5 time sample data like a live measurement source."""

from time import sleep

import acoular as ac
from traits.api import Bool, Float


class TimeSamplesPhantom(ac.MaskedTimeSamples):
    """TimeSamples source that yields stored data block by block."""

    #: Delay between yielded blocks. If unset, the delay follows the sample rate.
    time_delay = Float(desc="Time interval between individual blocks of data")

    #: Set to False to stop the result generator.
    collect_samples = Bool(True, desc="Indicates if result function is running")

    def result(self, num=128):
        """Yield samples in blocks of shape ``(num, num_channels)``."""
        if self.num_samples == 0:
            raise OSError("no samples available")

        if self.time_delay:
            sleep_time = self.time_delay
        else:
            sleep_time = (1 / self.sample_freq) * num

        idx = 0
        while idx < self.num_samples and self.collect_samples:
            yield self.data[idx : idx + num]
            sleep(sleep_time)
            idx += num

    def close(self):
        """Close the underlying HDF5 file handle."""
        for attr in ("_h5f", "h5f"):
            h5f = getattr(self, attr, None)
            if h5f is not None:
                h5f.close()


__all__ = ["TimeSamplesPhantom"]
