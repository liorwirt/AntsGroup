import numpy as np
class MapFileLoader(object):
    def __init__(self, map_name):
        self.in_map = self._read_map(map_name)
        self.occupancy_map = self._map_2_occupancy_map()
        self.initial_node = (int(np.where(self.in_map ==
                                          'S')[0]), int(np.where(self.in_map ==
                                                                 'S')[1]))
        self.final_node = (int(np.where(self.in_map ==
                                        'F')[0]), int(np.where(self.in_map ==
                                                               'F')[1]))

    def _read_map(self, map_name):
        ''' Reads data from an input map txt file'''
        map_planning = np.loadtxt('./maps/' + map_name, dtype="str")
        return map_planning

    def _map_2_occupancy_map(self):
        ''' Takes the matrix and converts it into a float array '''
        map_arr = np.copy(self.in_map)
        map_arr[map_arr == 'O'] = 0
        map_arr[map_arr == 'E'] = 1
        map_arr[map_arr == 'S'] = 1
        map_arr[map_arr == 'F'] = 1
        return map_arr.astype(np.int)