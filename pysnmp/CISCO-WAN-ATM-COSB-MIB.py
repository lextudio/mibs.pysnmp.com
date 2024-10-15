# SNMP MIB module (CISCO-WAN-ATM-COSB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-COSB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:48 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWanAtmCosbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16)
)
ciscoWanAtmCosbMIB.setRevisions(
        ("2003-03-21 00:00",
         "2002-06-10 00:00",
         "2000-04-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWanAtmCosbMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanAtmCosbMIBObjects = _CiscoWanAtmCosbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1)
)
_CwacConfig_ObjectIdentity = ObjectIdentity
cwacConfig = _CwacConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 1)
)
_CwacStatistics_ObjectIdentity = ObjectIdentity
cwacStatistics = _CwacStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2)
)
_CwacStatsAlarmConfgTable_Object = MibTable
cwacStatsAlarmConfgTable = _CwacStatsAlarmConfgTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwacStatsAlarmConfgTable.setStatus("current")
_CwacStatsAlarmConfgEntry_Object = MibTableRow
cwacStatsAlarmConfgEntry = _CwacStatsAlarmConfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1)
)
cwacStatsAlarmConfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-COSB-MIB", "cwacCosbIndex"),
)
if mibBuilder.loadTexts:
    cwacStatsAlarmConfgEntry.setStatus("current")


class _CwacCosbIndex_Type(Integer32):
    """Custom type cwacCosbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CwacCosbIndex_Type.__name__ = "Integer32"
_CwacCosbIndex_Object = MibTableColumn
cwacCosbIndex = _CwacCosbIndex_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 1),
    _CwacCosbIndex_Type()
)
cwacCosbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwacCosbIndex.setStatus("current")


class _CwacCosbCurrentCellsDiscThres_Type(Integer32):
    """Custom type cwacCosbCurrentCellsDiscThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwacCosbCurrentCellsDiscThres_Type.__name__ = "Integer32"
_CwacCosbCurrentCellsDiscThres_Object = MibTableColumn
cwacCosbCurrentCellsDiscThres = _CwacCosbCurrentCellsDiscThres_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 2),
    _CwacCosbCurrentCellsDiscThres_Type()
)
cwacCosbCurrentCellsDiscThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwacCosbCurrentCellsDiscThres.setStatus("current")


class _CwacStatsAlarmStatus_Type(Integer32):
    """Custom type cwacStatsAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwacStatsAlarmStatus_Type.__name__ = "Integer32"
_CwacStatsAlarmStatus_Object = MibTableColumn
cwacStatsAlarmStatus = _CwacStatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 3),
    _CwacStatsAlarmStatus_Type()
)
cwacStatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacStatsAlarmStatus.setStatus("current")


class _CwacValidIntervals_Type(Integer32):
    """Custom type cwacValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CwacValidIntervals_Type.__name__ = "Integer32"
_CwacValidIntervals_Object = MibTableColumn
cwacValidIntervals = _CwacValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 1, 1, 4),
    _CwacValidIntervals_Type()
)
cwacValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacValidIntervals.setStatus("current")
_CwacIntervalTable_Object = MibTable
cwacIntervalTable = _CwacIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwacIntervalTable.setStatus("current")
_CwacIntervalEntry_Object = MibTableRow
cwacIntervalEntry = _CwacIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1)
)
cwacIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WAN-ATM-COSB-MIB", "cwacCosbIndex"),
    (0, "CISCO-WAN-ATM-COSB-MIB", "cwacIntervalNumber"),
)
if mibBuilder.loadTexts:
    cwacIntervalEntry.setStatus("current")


class _CwacIntervalNumber_Type(Integer32):
    """Custom type cwacIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CwacIntervalNumber_Type.__name__ = "Integer32"
_CwacIntervalNumber_Object = MibTableColumn
cwacIntervalNumber = _CwacIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 1),
    _CwacIntervalNumber_Type()
)
cwacIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwacIntervalNumber.setStatus("current")
_CwacIntCellArrivals_Type = Counter32
_CwacIntCellArrivals_Object = MibTableColumn
cwacIntCellArrivals = _CwacIntCellArrivals_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 2),
    _CwacIntCellArrivals_Type()
)
cwacIntCellArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacIntCellArrivals.setStatus("current")
_CwacIntCellDiscards_Type = Counter32
_CwacIntCellDiscards_Object = MibTableColumn
cwacIntCellDiscards = _CwacIntCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 3),
    _CwacIntCellDiscards_Type()
)
cwacIntCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacIntCellDiscards.setStatus("current")
_CwacIntCellDeparts_Type = Counter32
_CwacIntCellDeparts_Object = MibTableColumn
cwacIntCellDeparts = _CwacIntCellDeparts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 4),
    _CwacIntCellDeparts_Type()
)
cwacIntCellDeparts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacIntCellDeparts.setStatus("current")
_CwacHighIntCellArrivals_Type = Counter32
_CwacHighIntCellArrivals_Object = MibTableColumn
cwacHighIntCellArrivals = _CwacHighIntCellArrivals_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 5),
    _CwacHighIntCellArrivals_Type()
)
cwacHighIntCellArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHighIntCellArrivals.setStatus("current")
_CwacHighIntCellDiscards_Type = Counter32
_CwacHighIntCellDiscards_Object = MibTableColumn
cwacHighIntCellDiscards = _CwacHighIntCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 6),
    _CwacHighIntCellDiscards_Type()
)
cwacHighIntCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHighIntCellDiscards.setStatus("current")
_CwacHighIntCellDeparts_Type = Counter32
_CwacHighIntCellDeparts_Object = MibTableColumn
cwacHighIntCellDeparts = _CwacHighIntCellDeparts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 7),
    _CwacHighIntCellDeparts_Type()
)
cwacHighIntCellDeparts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHighIntCellDeparts.setStatus("current")
_CwacHCIntCellArrivals_Type = Counter64
_CwacHCIntCellArrivals_Object = MibTableColumn
cwacHCIntCellArrivals = _CwacHCIntCellArrivals_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 8),
    _CwacHCIntCellArrivals_Type()
)
cwacHCIntCellArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHCIntCellArrivals.setStatus("current")
_CwacHCIntCellDiscards_Type = Counter64
_CwacHCIntCellDiscards_Object = MibTableColumn
cwacHCIntCellDiscards = _CwacHCIntCellDiscards_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 9),
    _CwacHCIntCellDiscards_Type()
)
cwacHCIntCellDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHCIntCellDiscards.setStatus("current")
_CwacHCIntCellDeparts_Type = Counter64
_CwacHCIntCellDeparts_Object = MibTableColumn
cwacHCIntCellDeparts = _CwacHCIntCellDeparts_Object(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 1, 2, 2, 1, 10),
    _CwacHCIntCellDeparts_Type()
)
cwacHCIntCellDeparts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwacHCIntCellDeparts.setStatus("current")
_CiscoWanAtmCosbMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanAtmCosbMIBConformance = _CiscoWanAtmCosbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2)
)
_CiscoWanAtmCosbMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanAtmCosbMIBCompliances = _CiscoWanAtmCosbMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1)
)
_CiscoWanAtmCosbMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanAtmCosbMIBGroups = _CiscoWanAtmCosbMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2)
)

# Managed Objects groups

ciscoWanAtmCosbAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 1)
)
ciscoWanAtmCosbAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-ATM-COSB-MIB", "cwacCosbCurrentCellsDiscThres"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacStatsAlarmStatus"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacValidIntervals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellArrivals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDiscards"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDeparts"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmCosbAlarmMIBGroup.setStatus("deprecated")

ciscoWanAtmCosbAlarmMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 2)
)
ciscoWanAtmCosbAlarmMIBGroup1.setObjects(
      *(("CISCO-WAN-ATM-COSB-MIB", "cwacCosbCurrentCellsDiscThres"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacStatsAlarmStatus"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacValidIntervals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellArrivals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDiscards"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacIntCellDeparts"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellArrivals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellDiscards"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacHighIntCellDeparts"))
)
if mibBuilder.loadTexts:
    ciscoWanAtmCosbAlarmMIBGroup1.setStatus("current")

ciscoHCWanAtmCosbAlarmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 2, 3)
)
ciscoHCWanAtmCosbAlarmMIBGroup.setObjects(
      *(("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellArrivals"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellDiscards"),
        ("CISCO-WAN-ATM-COSB-MIB", "cwacHCIntCellDeparts"))
)
if mibBuilder.loadTexts:
    ciscoHCWanAtmCosbAlarmMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanAtmCosbMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanAtmCosbMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWanAtmCosbMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 16, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWanAtmCosbMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-COSB-MIB",
    **{"ciscoWanAtmCosbMIB": ciscoWanAtmCosbMIB,
       "ciscoWanAtmCosbMIBObjects": ciscoWanAtmCosbMIBObjects,
       "cwacConfig": cwacConfig,
       "cwacStatistics": cwacStatistics,
       "cwacStatsAlarmConfgTable": cwacStatsAlarmConfgTable,
       "cwacStatsAlarmConfgEntry": cwacStatsAlarmConfgEntry,
       "cwacCosbIndex": cwacCosbIndex,
       "cwacCosbCurrentCellsDiscThres": cwacCosbCurrentCellsDiscThres,
       "cwacStatsAlarmStatus": cwacStatsAlarmStatus,
       "cwacValidIntervals": cwacValidIntervals,
       "cwacIntervalTable": cwacIntervalTable,
       "cwacIntervalEntry": cwacIntervalEntry,
       "cwacIntervalNumber": cwacIntervalNumber,
       "cwacIntCellArrivals": cwacIntCellArrivals,
       "cwacIntCellDiscards": cwacIntCellDiscards,
       "cwacIntCellDeparts": cwacIntCellDeparts,
       "cwacHighIntCellArrivals": cwacHighIntCellArrivals,
       "cwacHighIntCellDiscards": cwacHighIntCellDiscards,
       "cwacHighIntCellDeparts": cwacHighIntCellDeparts,
       "cwacHCIntCellArrivals": cwacHCIntCellArrivals,
       "cwacHCIntCellDiscards": cwacHCIntCellDiscards,
       "cwacHCIntCellDeparts": cwacHCIntCellDeparts,
       "ciscoWanAtmCosbMIBConformance": ciscoWanAtmCosbMIBConformance,
       "ciscoWanAtmCosbMIBCompliances": ciscoWanAtmCosbMIBCompliances,
       "ciscoWanAtmCosbMIBCompliance": ciscoWanAtmCosbMIBCompliance,
       "ciscoWanAtmCosbMIBCompliance1": ciscoWanAtmCosbMIBCompliance1,
       "ciscoWanAtmCosbMIBGroups": ciscoWanAtmCosbMIBGroups,
       "ciscoWanAtmCosbAlarmMIBGroup": ciscoWanAtmCosbAlarmMIBGroup,
       "ciscoWanAtmCosbAlarmMIBGroup1": ciscoWanAtmCosbAlarmMIBGroup1,
       "ciscoHCWanAtmCosbAlarmMIBGroup": ciscoHCWanAtmCosbAlarmMIBGroup}
)
