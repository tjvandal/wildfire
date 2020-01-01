"""Wrapper around the a single band's data from a GOES satellite scan."""


class GoesBand:
    """Wrapper around the a single band's data from a GOES satellite scan.

    Attributes
    ----------
    dataset : xr.core.dataset.DataSet
    scan_time_utc : datetime.datetime
        Datetime of the scan's start time.
    satellite : str
        In the set (G16, G17). The satellite the scan was made by.
    region : str
        In the set (C, F, M1, M2). The region over which the scan was made.
    """

    def __init__(self, dataset):
        """Initialize.

        Parameters
        ----------
        dataset : xr.core.dataset.DataSet
        """
        self.dataset = dataset
        # scan time
        # satellite
        # region

    def plot(self, use_radiance=False):
        """Plot the band.

        If not plotting the radiance, will plot the reflectance factor for bands 1 - 6,
        and the brightness temperature for bands 7 - 16.

        Parameters
        ----------
        use_radiance : bool
            Optional, whether to plot the spectral radiance. Defaults to `False`, which
            will plot either the reflectance factor or the brightness temperature
            depending on the band.

        Returns
        -------
        plt.axes._subplots.AxesSubplot
        """
        raise NotImplementedError

    def normalize(self, use_radiance=False):
        """Normalize data to be centered around 0.

        If not normalizing the radiance, will normalize the reflectance factor for bands
        1 - 6, and the brightness temperature for bands 7 - 16.

        Parameters
        ----------
        use_radiance : bool
            Optional, whether to plot the spectral radiance. Defaults to `False`, which
            will normalize either the reflectance factor or the brightness temperature
            depending on the band.
        """
        raise NotImplementedError

    @property
    def reflectance_factor(self):
        """Calculate the reflectance factor from spectral radiance.

        For more information, see the Reflective Channels section at
        https://github.com/joyprojects/wildfire/blob/master/documentation/notebooks/noaa_goes_documentation.ipynb

        Raises
        ------
        ValueError
            If the band is not between 1 and 6 inclusive.
        """
        raise NotImplementedError

    @property
    def brightness_temperature(self):
        """Calculate the brightness temperature from spectral radiance.

        For more information, see the Emissive Channels section at
        https://github.com/joyprojects/wildfire/blob/master/documentation/notebooks/noaa_goes_documentation.ipynb

        Raises
        ------
        ValueError
            If the band is not between 7 and 16 inclusive.
        """
        raise NotImplementedError

    def to_lat_lon(self):
        """Convert the X and Y of the ABI fixed grid to latitude and longitude."""
        raise NotImplementedError

    def filter_bad_pixels(self):
        """Use the Data Quality Flag (DQF) to filter out bad pixels.

        Each pixel (value according to a specific X-Y coordinate) has a DQF, which ranges
        from 0 (good) to 3 (no value). We follow NOAA's suggestion of filtering out all
        pixes with a flag of 2 or 3.

        Returns
        -------
        GoesBand
            A `GoesBand` object of data with a 0 or 1 DQF.
        """
        raise NotImplementedError

    def to_netcdf(self):
        """Persist to netcdf4.

        Persists file in a form matching the file struture in Amazon S3:
            {local_directory}/{s3_bucket_name}/{s3_key}
        For example:
            {local_directory}/noaa-goes17/ABI-L1b-RadM/2019/300/20/
        OR_ABI-L1b-RadM1-M6C14_G17_s20193002048275_e20193002048332_c20193002048405.nc

        Parameters
        ----------
        directory : str
            Path to local directory in which to persist.

        Returns
        -------
        str
            The filepath of the persisted file.
        """
        raise NotImplementedError


def get_goes_band(satellite, region, band, scan_time_utc):
    """Get the GoesBand corresponding the input.

    Parameters
    ----------
    satellite : str
        Must be in the set (G16, G17).
    region : str
        Must be in the set (C, F, M1, M2).
    band : int
        Must be between 1 and 16 inclusive.
    scan_time_utc : datetime.datetime
        Datetime of the scan. Must be specified to the minute.

    Returns
    -------
    GoesBand
    """
    raise NotImplementedError


def from_netcdf(filepath):
    """Read a GoesBand from the filepath.

    Parameters
    ----------
    filepath : str
        May either be a local filepath, or an Amazon S3 URI.

    Returns
    -------
    GoesBand
    """
    raise NotImplementedError
