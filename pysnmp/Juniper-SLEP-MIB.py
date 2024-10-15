# SNMP MIB module (Juniper-SLEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SLEP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:17 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniNextIfIndex")

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


# MODULE-IDENTITY

juniSlepMIBS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15)
)
juniSlepMIBS.setRevisions(
        ("2002-09-16 21:44",
         "2001-04-03 19:10",
         "2000-01-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniSlepObjects_ObjectIdentity = ObjectIdentity
juniSlepObjects = _JuniSlepObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1)
)
_JuniSlepIfLayer_ObjectIdentity = ObjectIdentity
juniSlepIfLayer = _JuniSlepIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1)
)
_JuniSlepNextIfIndex_Type = JuniNextIfIndex
_JuniSlepNextIfIndex_Object = MibScalar
juniSlepNextIfIndex = _JuniSlepNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 1),
    _JuniSlepNextIfIndex_Type()
)
juniSlepNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSlepNextIfIndex.setStatus("current")
_JuniSlepIfTable_Object = MibTable
juniSlepIfTable = _JuniSlepIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniSlepIfTable.setStatus("current")
_JuniSlepIfEntry_Object = MibTableRow
juniSlepIfEntry = _JuniSlepIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1)
)
juniSlepIfEntry.setIndexNames(
    (0, "Juniper-SLEP-MIB", "juniSlepIfIndex"),
)
if mibBuilder.loadTexts:
    juniSlepIfEntry.setStatus("current")
_JuniSlepIfIndex_Type = InterfaceIndex
_JuniSlepIfIndex_Object = MibTableColumn
juniSlepIfIndex = _JuniSlepIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 1),
    _JuniSlepIfIndex_Type()
)
juniSlepIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSlepIfIndex.setStatus("current")


class _JuniSlepKeepAliveTimer_Type(Integer32):
    """Custom type juniSlepKeepAliveTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553),
    )


_JuniSlepKeepAliveTimer_Type.__name__ = "Integer32"
_JuniSlepKeepAliveTimer_Object = MibTableColumn
juniSlepKeepAliveTimer = _JuniSlepKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 2),
    _JuniSlepKeepAliveTimer_Type()
)
juniSlepKeepAliveTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSlepKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniSlepKeepAliveTimer.setUnits("seconds")
_JuniSlepIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniSlepIfLowerIfIndex_Object = MibTableColumn
juniSlepIfLowerIfIndex = _JuniSlepIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 3),
    _JuniSlepIfLowerIfIndex_Type()
)
juniSlepIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSlepIfLowerIfIndex.setStatus("current")
_JuniSlepIfRowStatus_Type = RowStatus
_JuniSlepIfRowStatus_Object = MibTableColumn
juniSlepIfRowStatus = _JuniSlepIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 4),
    _JuniSlepIfRowStatus_Type()
)
juniSlepIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSlepIfRowStatus.setStatus("current")


class _JuniSlepDownWhenLooped_Type(JuniEnable):
    """Custom type juniSlepDownWhenLooped based on JuniEnable"""


_JuniSlepDownWhenLooped_Object = MibTableColumn
juniSlepDownWhenLooped = _JuniSlepDownWhenLooped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 2, 1, 5),
    _JuniSlepDownWhenLooped_Type()
)
juniSlepDownWhenLooped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSlepDownWhenLooped.setStatus("current")
_JuniSlepIfStatisticsTable_Object = MibTable
juniSlepIfStatisticsTable = _JuniSlepIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniSlepIfStatisticsTable.setStatus("current")
_JuniSlepIfStatisticsEntry_Object = MibTableRow
juniSlepIfStatisticsEntry = _JuniSlepIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1)
)
juniSlepIfStatisticsEntry.setIndexNames(
    (0, "Juniper-SLEP-MIB", "juniSlepIfStatsIndex"),
)
if mibBuilder.loadTexts:
    juniSlepIfStatisticsEntry.setStatus("current")
_JuniSlepIfStatsIndex_Type = InterfaceIndex
_JuniSlepIfStatsIndex_Object = MibTableColumn
juniSlepIfStatsIndex = _JuniSlepIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 1),
    _JuniSlepIfStatsIndex_Type()
)
juniSlepIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSlepIfStatsIndex.setStatus("current")
_JuniSlepKeepAliveFailures_Type = Counter32
_JuniSlepKeepAliveFailures_Object = MibTableColumn
juniSlepKeepAliveFailures = _JuniSlepKeepAliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 2),
    _JuniSlepKeepAliveFailures_Type()
)
juniSlepKeepAliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSlepKeepAliveFailures.setStatus("current")
_JuniSlepLinkStatusTooLongPackets_Type = Counter32
_JuniSlepLinkStatusTooLongPackets_Object = MibTableColumn
juniSlepLinkStatusTooLongPackets = _JuniSlepLinkStatusTooLongPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 3),
    _JuniSlepLinkStatusTooLongPackets_Type()
)
juniSlepLinkStatusTooLongPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSlepLinkStatusTooLongPackets.setStatus("current")
_JuniSlepLinkStatusBadFCSs_Type = Counter32
_JuniSlepLinkStatusBadFCSs_Object = MibTableColumn
juniSlepLinkStatusBadFCSs = _JuniSlepLinkStatusBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 1, 1, 3, 1, 4),
    _JuniSlepLinkStatusBadFCSs_Type()
)
juniSlepLinkStatusBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSlepLinkStatusBadFCSs.setStatus("current")
_JuniSlepConformance_ObjectIdentity = ObjectIdentity
juniSlepConformance = _JuniSlepConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4)
)
_JuniSlepCompliances_ObjectIdentity = ObjectIdentity
juniSlepCompliances = _JuniSlepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1)
)
_JuniSlepGroups_ObjectIdentity = ObjectIdentity
juniSlepGroups = _JuniSlepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2)
)

# Managed Objects groups

juniSlepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2, 1)
)
juniSlepGroup.setObjects(
      *(("Juniper-SLEP-MIB", "juniSlepNextIfIndex"),
        ("Juniper-SLEP-MIB", "juniSlepKeepAliveTimer"),
        ("Juniper-SLEP-MIB", "juniSlepIfLowerIfIndex"),
        ("Juniper-SLEP-MIB", "juniSlepIfRowStatus"),
        ("Juniper-SLEP-MIB", "juniSlepKeepAliveFailures"),
        ("Juniper-SLEP-MIB", "juniSlepLinkStatusTooLongPackets"),
        ("Juniper-SLEP-MIB", "juniSlepLinkStatusBadFCSs"))
)
if mibBuilder.loadTexts:
    juniSlepGroup.setStatus("obsolete")

juniSlepGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 2, 2)
)
juniSlepGroup2.setObjects(
      *(("Juniper-SLEP-MIB", "juniSlepNextIfIndex"),
        ("Juniper-SLEP-MIB", "juniSlepKeepAliveTimer"),
        ("Juniper-SLEP-MIB", "juniSlepIfLowerIfIndex"),
        ("Juniper-SLEP-MIB", "juniSlepIfRowStatus"),
        ("Juniper-SLEP-MIB", "juniSlepDownWhenLooped"),
        ("Juniper-SLEP-MIB", "juniSlepKeepAliveFailures"),
        ("Juniper-SLEP-MIB", "juniSlepLinkStatusTooLongPackets"),
        ("Juniper-SLEP-MIB", "juniSlepLinkStatusBadFCSs"))
)
if mibBuilder.loadTexts:
    juniSlepGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniSlepCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniSlepCompliance.setStatus(
        "obsolete"
    )

juniSlepCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 15, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniSlepCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SLEP-MIB",
    **{"juniSlepMIBS": juniSlepMIBS,
       "juniSlepObjects": juniSlepObjects,
       "juniSlepIfLayer": juniSlepIfLayer,
       "juniSlepNextIfIndex": juniSlepNextIfIndex,
       "juniSlepIfTable": juniSlepIfTable,
       "juniSlepIfEntry": juniSlepIfEntry,
       "juniSlepIfIndex": juniSlepIfIndex,
       "juniSlepKeepAliveTimer": juniSlepKeepAliveTimer,
       "juniSlepIfLowerIfIndex": juniSlepIfLowerIfIndex,
       "juniSlepIfRowStatus": juniSlepIfRowStatus,
       "juniSlepDownWhenLooped": juniSlepDownWhenLooped,
       "juniSlepIfStatisticsTable": juniSlepIfStatisticsTable,
       "juniSlepIfStatisticsEntry": juniSlepIfStatisticsEntry,
       "juniSlepIfStatsIndex": juniSlepIfStatsIndex,
       "juniSlepKeepAliveFailures": juniSlepKeepAliveFailures,
       "juniSlepLinkStatusTooLongPackets": juniSlepLinkStatusTooLongPackets,
       "juniSlepLinkStatusBadFCSs": juniSlepLinkStatusBadFCSs,
       "juniSlepConformance": juniSlepConformance,
       "juniSlepCompliances": juniSlepCompliances,
       "juniSlepCompliance": juniSlepCompliance,
       "juniSlepCompliance2": juniSlepCompliance2,
       "juniSlepGroups": juniSlepGroups,
       "juniSlepGroup": juniSlepGroup,
       "juniSlepGroup2": juniSlepGroup2}
)
