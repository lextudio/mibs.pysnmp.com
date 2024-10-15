# SNMP MIB module (Unisphere-Data-SLEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SLEP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:33 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdSlepMIBS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15)
)
usdSlepMIBS.setRevisions(
        ("2001-04-03 19:10",
         "2000-01-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdSlepObjects_ObjectIdentity = ObjectIdentity
usdSlepObjects = _UsdSlepObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1)
)
_UsdSlepIfLayer_ObjectIdentity = ObjectIdentity
usdSlepIfLayer = _UsdSlepIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1)
)
_UsdSlepNextIfIndex_Type = UsdNextIfIndex
_UsdSlepNextIfIndex_Object = MibScalar
usdSlepNextIfIndex = _UsdSlepNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 1),
    _UsdSlepNextIfIndex_Type()
)
usdSlepNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSlepNextIfIndex.setStatus("current")
_UsdSlepIfTable_Object = MibTable
usdSlepIfTable = _UsdSlepIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdSlepIfTable.setStatus("current")
_UsdSlepIfEntry_Object = MibTableRow
usdSlepIfEntry = _UsdSlepIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1)
)
usdSlepIfEntry.setIndexNames(
    (0, "Unisphere-Data-SLEP-MIB", "usdSlepIfIndex"),
)
if mibBuilder.loadTexts:
    usdSlepIfEntry.setStatus("current")
_UsdSlepIfIndex_Type = InterfaceIndex
_UsdSlepIfIndex_Object = MibTableColumn
usdSlepIfIndex = _UsdSlepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 1),
    _UsdSlepIfIndex_Type()
)
usdSlepIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSlepIfIndex.setStatus("current")


class _UsdSlepKeepAliveTimer_Type(Integer32):
    """Custom type usdSlepKeepAliveTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553),
    )


_UsdSlepKeepAliveTimer_Type.__name__ = "Integer32"
_UsdSlepKeepAliveTimer_Object = MibTableColumn
usdSlepKeepAliveTimer = _UsdSlepKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 2),
    _UsdSlepKeepAliveTimer_Type()
)
usdSlepKeepAliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSlepKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    usdSlepKeepAliveTimer.setUnits("seconds")
_UsdSlepIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdSlepIfLowerIfIndex_Object = MibTableColumn
usdSlepIfLowerIfIndex = _UsdSlepIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 3),
    _UsdSlepIfLowerIfIndex_Type()
)
usdSlepIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSlepIfLowerIfIndex.setStatus("current")
_UsdSlepIfRowStatus_Type = RowStatus
_UsdSlepIfRowStatus_Object = MibTableColumn
usdSlepIfRowStatus = _UsdSlepIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 4),
    _UsdSlepIfRowStatus_Type()
)
usdSlepIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSlepIfRowStatus.setStatus("current")


class _UsdSlepDownWhenLooped_Type(UsdEnable):
    """Custom type usdSlepDownWhenLooped based on UsdEnable"""


_UsdSlepDownWhenLooped_Object = MibTableColumn
usdSlepDownWhenLooped = _UsdSlepDownWhenLooped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 5),
    _UsdSlepDownWhenLooped_Type()
)
usdSlepDownWhenLooped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSlepDownWhenLooped.setStatus("current")
_UsdSlepIfStatisticsTable_Object = MibTable
usdSlepIfStatisticsTable = _UsdSlepIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    usdSlepIfStatisticsTable.setStatus("current")
_UsdSlepIfStatisticsEntry_Object = MibTableRow
usdSlepIfStatisticsEntry = _UsdSlepIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1)
)
usdSlepIfStatisticsEntry.setIndexNames(
    (0, "Unisphere-Data-SLEP-MIB", "usdSlepIfStatsIndex"),
)
if mibBuilder.loadTexts:
    usdSlepIfStatisticsEntry.setStatus("current")
_UsdSlepIfStatsIndex_Type = InterfaceIndex
_UsdSlepIfStatsIndex_Object = MibTableColumn
usdSlepIfStatsIndex = _UsdSlepIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 1),
    _UsdSlepIfStatsIndex_Type()
)
usdSlepIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSlepIfStatsIndex.setStatus("current")
_UsdSlepKeepAliveFailures_Type = Counter32
_UsdSlepKeepAliveFailures_Object = MibTableColumn
usdSlepKeepAliveFailures = _UsdSlepKeepAliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 2),
    _UsdSlepKeepAliveFailures_Type()
)
usdSlepKeepAliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSlepKeepAliveFailures.setStatus("current")
_UsdSlepLinkStatusTooLongPackets_Type = Counter32
_UsdSlepLinkStatusTooLongPackets_Object = MibTableColumn
usdSlepLinkStatusTooLongPackets = _UsdSlepLinkStatusTooLongPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 3),
    _UsdSlepLinkStatusTooLongPackets_Type()
)
usdSlepLinkStatusTooLongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSlepLinkStatusTooLongPackets.setStatus("current")
_UsdSlepLinkStatusBadFCSs_Type = Counter32
_UsdSlepLinkStatusBadFCSs_Object = MibTableColumn
usdSlepLinkStatusBadFCSs = _UsdSlepLinkStatusBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 4),
    _UsdSlepLinkStatusBadFCSs_Type()
)
usdSlepLinkStatusBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSlepLinkStatusBadFCSs.setStatus("current")
_UsdSlepConformance_ObjectIdentity = ObjectIdentity
usdSlepConformance = _UsdSlepConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4)
)
_UsdSlepCompliances_ObjectIdentity = ObjectIdentity
usdSlepCompliances = _UsdSlepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1)
)
_UsdSlepGroups_ObjectIdentity = ObjectIdentity
usdSlepGroups = _UsdSlepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2)
)

# Managed Objects groups

usdSlepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2, 1)
)
usdSlepGroup.setObjects(
      *(("Unisphere-Data-SLEP-MIB", "usdSlepNextIfIndex"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepKeepAliveTimer"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepIfLowerIfIndex"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepIfRowStatus"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepKeepAliveFailures"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepLinkStatusTooLongPackets"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepLinkStatusBadFCSs"))
)
if mibBuilder.loadTexts:
    usdSlepGroup.setStatus("obsolete")

usdSlepGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2, 2)
)
usdSlepGroup2.setObjects(
      *(("Unisphere-Data-SLEP-MIB", "usdSlepNextIfIndex"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepKeepAliveTimer"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepIfLowerIfIndex"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepIfRowStatus"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepDownWhenLooped"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepKeepAliveFailures"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepLinkStatusTooLongPackets"),
        ("Unisphere-Data-SLEP-MIB", "usdSlepLinkStatusBadFCSs"))
)
if mibBuilder.loadTexts:
    usdSlepGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSlepCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdSlepCompliance.setStatus(
        "obsolete"
    )

usdSlepCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdSlepCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SLEP-MIB",
    **{"usdSlepMIBS": usdSlepMIBS,
       "usdSlepObjects": usdSlepObjects,
       "usdSlepIfLayer": usdSlepIfLayer,
       "usdSlepNextIfIndex": usdSlepNextIfIndex,
       "usdSlepIfTable": usdSlepIfTable,
       "usdSlepIfEntry": usdSlepIfEntry,
       "usdSlepIfIndex": usdSlepIfIndex,
       "usdSlepKeepAliveTimer": usdSlepKeepAliveTimer,
       "usdSlepIfLowerIfIndex": usdSlepIfLowerIfIndex,
       "usdSlepIfRowStatus": usdSlepIfRowStatus,
       "usdSlepDownWhenLooped": usdSlepDownWhenLooped,
       "usdSlepIfStatisticsTable": usdSlepIfStatisticsTable,
       "usdSlepIfStatisticsEntry": usdSlepIfStatisticsEntry,
       "usdSlepIfStatsIndex": usdSlepIfStatsIndex,
       "usdSlepKeepAliveFailures": usdSlepKeepAliveFailures,
       "usdSlepLinkStatusTooLongPackets": usdSlepLinkStatusTooLongPackets,
       "usdSlepLinkStatusBadFCSs": usdSlepLinkStatusBadFCSs,
       "usdSlepConformance": usdSlepConformance,
       "usdSlepCompliances": usdSlepCompliances,
       "usdSlepCompliance": usdSlepCompliance,
       "usdSlepCompliance2": usdSlepCompliance2,
       "usdSlepGroups": usdSlepGroups,
       "usdSlepGroup": usdSlepGroup,
       "usdSlepGroup2": usdSlepGroup2}
)
