# https://leetcode.com/problems/bus-routes/

from collections import defaultdict, deque
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        stop_bus = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_bus[stop].append(bus)

        visited_stops = {source}
        visited_buses = set()
        queue = deque([(source, 0)])
        while queue:
            _source, _bus_stage = queue.popleft()
            for bus in stop_bus[_source]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for stop in routes[bus]:
                    if stop == target:
                        return _bus_stage+1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop,_bus_stage+1))
        return -1


"""
SKZBIC PETQ E AYS DATA N VERACEL GRAPH I VOR KAROGHANANQ
EFFECTIVE PTTVEL AYD INFORMACIAYI VRAYOV U GTNEL AMENAKARCH CHANAPAHRY
HASNELU A IC B KET
GRAPH Y KUNENA AYS TESYQ:
VORPES NODE KNDUNENQ STOP Y
ISK VALUE NRY KLINEN BUS RY
MYUS KOXMIC AYS GRAPH Y HETAQRIR E NRANOV
VOR VOCH MIAYN UNENQ STOP AYL NAYEV BUS
AYSINQN 1 HAT SET OV CHENQ PRCNI
EV VORPES SKZBNAKAN KET VERNCUM ENQ SOURCE Y EV DRAN HAMAPATASXAN
BUS RY QANAKY MER DEPQUM 0 QANI VOR DER CHENQ POXEL
SKSUM ENQ BFS QANI VOR AYN TUYL E TALIS GTNEL KARCHAGUYN Y
VERCNUM ENQ SOURCE I TAK GTNVOX BUS RY
PTTVUM ENQ VRAYOV ETE ARDEN PTTVEL EINQ BAC ENQ TOXNUM
HAKARAK DEPQUM VERCNUM ENQ AYD BUS I HAMAR NAXATESVAC BOLOR STOPNERY
AYSINQN IREN HAMAPATASXAN ROUTE Y
ETE STOP Y == TARGET I UREMN HASANQ TEX EV POXECIN + 1 BUS
HAKARAK DEPQUM STUGUM ENQ ARDYOQ KA AYCELVAC STOPNERI MEJ
ETE CHE AVELACNUM ENQ QUEUE I MEJ
"""

