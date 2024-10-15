# SNMP MIB module (HM2-L2MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-L2MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:00 2024
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

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PortList,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "dot1qVlanIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

hm2L2McastMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33)
)
hm2L2McastMib.setRevisions(
        ("2012-01-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2L2McastMibNotifications_ObjectIdentity = ObjectIdentity
hm2L2McastMibNotifications = _Hm2L2McastMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 0)
)
_Hm2L2McastMibObjects_ObjectIdentity = ObjectIdentity
hm2L2McastMibObjects = _Hm2L2McastMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1)
)
_Hm2L2McastSnoopingObjects_ObjectIdentity = ObjectIdentity
hm2L2McastSnoopingObjects = _Hm2L2McastSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1)
)
_Hm2L2McastSnoopingGroup_ObjectIdentity = ObjectIdentity
hm2L2McastSnoopingGroup = _Hm2L2McastSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1)
)
_Hm2L2McastSnoopingQuerierTable_Object = MibTable
hm2L2McastSnoopingQuerierTable = _Hm2L2McastSnoopingQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQuerierTable.setStatus("current")
_Hm2L2McastSnoopingQuerierEntry_Object = MibTableRow
hm2L2McastSnoopingQuerierEntry = _Hm2L2McastSnoopingQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1, 1)
)
hm2L2McastSnoopingQuerierEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQuerierEntry.setStatus("current")
_Hm2L2McastSnoopingQueryPorts_Type = PortList
_Hm2L2McastSnoopingQueryPorts_Object = MibTableColumn
hm2L2McastSnoopingQueryPorts = _Hm2L2McastSnoopingQueryPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1, 1, 1),
    _Hm2L2McastSnoopingQueryPorts_Type()
)
hm2L2McastSnoopingQueryPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQueryPorts.setStatus("current")
_Hm2L2McastSnoopingQueryStaticPorts_Type = PortList
_Hm2L2McastSnoopingQueryStaticPorts_Object = MibTableColumn
hm2L2McastSnoopingQueryStaticPorts = _Hm2L2McastSnoopingQueryStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1, 1, 2),
    _Hm2L2McastSnoopingQueryStaticPorts_Type()
)
hm2L2McastSnoopingQueryStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQueryStaticPorts.setStatus("current")
_Hm2L2McastSnoopingQueryPortsAutoPorts_Type = PortList
_Hm2L2McastSnoopingQueryPortsAutoPorts_Object = MibTableColumn
hm2L2McastSnoopingQueryPortsAutoPorts = _Hm2L2McastSnoopingQueryPortsAutoPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1, 1, 3),
    _Hm2L2McastSnoopingQueryPortsAutoPorts_Type()
)
hm2L2McastSnoopingQueryPortsAutoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQueryPortsAutoPorts.setStatus("current")
_Hm2L2McastSnoopingQueryPortsAutoPortsState_Type = PortList
_Hm2L2McastSnoopingQueryPortsAutoPortsState_Object = MibTableColumn
hm2L2McastSnoopingQueryPortsAutoPortsState = _Hm2L2McastSnoopingQueryPortsAutoPortsState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 1, 1, 4),
    _Hm2L2McastSnoopingQueryPortsAutoPortsState_Type()
)
hm2L2McastSnoopingQueryPortsAutoPortsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingQueryPortsAutoPortsState.setStatus("current")
_Hm2L2McastSnoopingForwardAllTable_Object = MibTable
hm2L2McastSnoopingForwardAllTable = _Hm2L2McastSnoopingForwardAllTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingForwardAllTable.setStatus("current")
_Hm2L2McastSnoopingForwardAllEntry_Object = MibTableRow
hm2L2McastSnoopingForwardAllEntry = _Hm2L2McastSnoopingForwardAllEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 2, 1)
)
hm2L2McastSnoopingForwardAllEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingForwardAllEntry.setStatus("current")
_Hm2L2McastSnoopingForwardAllStaticPorts_Type = PortList
_Hm2L2McastSnoopingForwardAllStaticPorts_Object = MibTableColumn
hm2L2McastSnoopingForwardAllStaticPorts = _Hm2L2McastSnoopingForwardAllStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 1, 1, 2, 1, 1),
    _Hm2L2McastSnoopingForwardAllStaticPorts_Type()
)
hm2L2McastSnoopingForwardAllStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingForwardAllStaticPorts.setStatus("current")
_Hm2L2McastFilteringObjects_ObjectIdentity = ObjectIdentity
hm2L2McastFilteringObjects = _Hm2L2McastFilteringObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2)
)
_Hm2L2McastFilteringGroup_ObjectIdentity = ObjectIdentity
hm2L2McastFilteringGroup = _Hm2L2McastFilteringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2, 1)
)
_Hm2L2McastFilteringTable_Object = MibTable
hm2L2McastFilteringTable = _Hm2L2McastFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2L2McastFilteringTable.setStatus("current")
_Hm2L2McastFilteringEntry_Object = MibTableRow
hm2L2McastFilteringEntry = _Hm2L2McastFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2, 1, 1, 1)
)
hm2L2McastFilteringEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2L2McastFilteringEntry.setStatus("current")


class _Hm2L2McastFilteringKnownMode_Type(Integer32):
    """Custom type hm2L2McastFilteringKnownMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("query-and-registered-ports", 1),
          ("registered-ports-only", 2))
    )


_Hm2L2McastFilteringKnownMode_Type.__name__ = "Integer32"
_Hm2L2McastFilteringKnownMode_Object = MibTableColumn
hm2L2McastFilteringKnownMode = _Hm2L2McastFilteringKnownMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2, 1, 1, 1, 1),
    _Hm2L2McastFilteringKnownMode_Type()
)
hm2L2McastFilteringKnownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2McastFilteringKnownMode.setStatus("current")


class _Hm2L2McastFilteringUnknownMode_Type(Integer32):
    """Custom type hm2L2McastFilteringUnknownMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("flood", 2),
          ("query-ports", 3))
    )


_Hm2L2McastFilteringUnknownMode_Type.__name__ = "Integer32"
_Hm2L2McastFilteringUnknownMode_Object = MibScalar
hm2L2McastFilteringUnknownMode = _Hm2L2McastFilteringUnknownMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 2, 1, 2),
    _Hm2L2McastFilteringUnknownMode_Type()
)
hm2L2McastFilteringUnknownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2L2McastFilteringUnknownMode.setStatus("current")
_Hm2L2McastSnoopingStatistics_ObjectIdentity = ObjectIdentity
hm2L2McastSnoopingStatistics = _Hm2L2McastSnoopingStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3)
)
_Hm2L2McastSnoopingStatisticsGroup_ObjectIdentity = ObjectIdentity
hm2L2McastSnoopingStatisticsGroup = _Hm2L2McastSnoopingStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1)
)
_Hm2L2McastSnoopingIgmpReportsFramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIgmpReportsFramesProcessed_Object = MibScalar
hm2L2McastSnoopingIgmpReportsFramesProcessed = _Hm2L2McastSnoopingIgmpReportsFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 1),
    _Hm2L2McastSnoopingIgmpReportsFramesProcessed_Type()
)
hm2L2McastSnoopingIgmpReportsFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIgmpReportsFramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIgmpQueriesV1FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIgmpQueriesV1FramesProcessed_Object = MibScalar
hm2L2McastSnoopingIgmpQueriesV1FramesProcessed = _Hm2L2McastSnoopingIgmpQueriesV1FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 2),
    _Hm2L2McastSnoopingIgmpQueriesV1FramesProcessed_Type()
)
hm2L2McastSnoopingIgmpQueriesV1FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIgmpQueriesV1FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIgmpQueriesV2FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIgmpQueriesV2FramesProcessed_Object = MibScalar
hm2L2McastSnoopingIgmpQueriesV2FramesProcessed = _Hm2L2McastSnoopingIgmpQueriesV2FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 3),
    _Hm2L2McastSnoopingIgmpQueriesV2FramesProcessed_Type()
)
hm2L2McastSnoopingIgmpQueriesV2FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIgmpQueriesV2FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIgmpQueriesV3FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIgmpQueriesV3FramesProcessed_Object = MibScalar
hm2L2McastSnoopingIgmpQueriesV3FramesProcessed = _Hm2L2McastSnoopingIgmpQueriesV3FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 4),
    _Hm2L2McastSnoopingIgmpQueriesV3FramesProcessed_Type()
)
hm2L2McastSnoopingIgmpQueriesV3FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIgmpQueriesV3FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIgmpWrongVersionQueries_Type = Counter32
_Hm2L2McastSnoopingIgmpWrongVersionQueries_Object = MibScalar
hm2L2McastSnoopingIgmpWrongVersionQueries = _Hm2L2McastSnoopingIgmpWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 5),
    _Hm2L2McastSnoopingIgmpWrongVersionQueries_Type()
)
hm2L2McastSnoopingIgmpWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIgmpWrongVersionQueries.setStatus("current")
_Hm2L2McastSnoopingPimDvmrpFramesProcessed_Type = Counter32
_Hm2L2McastSnoopingPimDvmrpFramesProcessed_Object = MibScalar
hm2L2McastSnoopingPimDvmrpFramesProcessed = _Hm2L2McastSnoopingPimDvmrpFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 6),
    _Hm2L2McastSnoopingPimDvmrpFramesProcessed_Type()
)
hm2L2McastSnoopingPimDvmrpFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingPimDvmrpFramesProcessed.setStatus("current")
_Hm2L2McastSnoopingStatisticsTable_Object = MibTable
hm2L2McastSnoopingStatisticsTable = _Hm2L2McastSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingStatisticsTable.setStatus("current")
_Hm2L2McastSnoopingStatisticsEntry_Object = MibTableRow
hm2L2McastSnoopingStatisticsEntry = _Hm2L2McastSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1)
)
hm2L2McastSnoopingStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2L2McastSnoopingStatisticsEntry.setStatus("current")
_Hm2L2McastSnoopingIntfIgmpReportsFramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIntfIgmpReportsFramesProcessed_Object = MibTableColumn
hm2L2McastSnoopingIntfIgmpReportsFramesProcessed = _Hm2L2McastSnoopingIntfIgmpReportsFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 2),
    _Hm2L2McastSnoopingIntfIgmpReportsFramesProcessed_Type()
)
hm2L2McastSnoopingIntfIgmpReportsFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfIgmpReportsFramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed_Object = MibTableColumn
hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed = _Hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 3),
    _Hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed_Type()
)
hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed_Object = MibTableColumn
hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed = _Hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 4),
    _Hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed_Type()
)
hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed_Object = MibTableColumn
hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed = _Hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 5),
    _Hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed_Type()
)
hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed.setStatus("current")
_Hm2L2McastSnoopingIntfIgmpWrongVersionQueries_Type = Counter32
_Hm2L2McastSnoopingIntfIgmpWrongVersionQueries_Object = MibTableColumn
hm2L2McastSnoopingIntfIgmpWrongVersionQueries = _Hm2L2McastSnoopingIntfIgmpWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 6),
    _Hm2L2McastSnoopingIntfIgmpWrongVersionQueries_Type()
)
hm2L2McastSnoopingIntfIgmpWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfIgmpWrongVersionQueries.setStatus("current")
_Hm2L2McastSnoopingIntfPimDvmrpFramesProcessed_Type = Counter32
_Hm2L2McastSnoopingIntfPimDvmrpFramesProcessed_Object = MibTableColumn
hm2L2McastSnoopingIntfPimDvmrpFramesProcessed = _Hm2L2McastSnoopingIntfPimDvmrpFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 1, 3, 1, 10, 1, 7),
    _Hm2L2McastSnoopingIntfPimDvmrpFramesProcessed_Type()
)
hm2L2McastSnoopingIntfPimDvmrpFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2L2McastSnoopingIntfPimDvmrpFramesProcessed.setStatus("current")
_Hm2L2McastSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2L2McastSNMPExtensionGroup = _Hm2L2McastSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 3)
)
_Hm2L2McastGroupMembershipErrorReturn_ObjectIdentity = ObjectIdentity
hm2L2McastGroupMembershipErrorReturn = _Hm2L2McastGroupMembershipErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 33, 3, 1)
)
if mibBuilder.loadTexts:
    hm2L2McastGroupMembershipErrorReturn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-L2MCAST-MIB",
    **{"hm2L2McastMib": hm2L2McastMib,
       "hm2L2McastMibNotifications": hm2L2McastMibNotifications,
       "hm2L2McastMibObjects": hm2L2McastMibObjects,
       "hm2L2McastSnoopingObjects": hm2L2McastSnoopingObjects,
       "hm2L2McastSnoopingGroup": hm2L2McastSnoopingGroup,
       "hm2L2McastSnoopingQuerierTable": hm2L2McastSnoopingQuerierTable,
       "hm2L2McastSnoopingQuerierEntry": hm2L2McastSnoopingQuerierEntry,
       "hm2L2McastSnoopingQueryPorts": hm2L2McastSnoopingQueryPorts,
       "hm2L2McastSnoopingQueryStaticPorts": hm2L2McastSnoopingQueryStaticPorts,
       "hm2L2McastSnoopingQueryPortsAutoPorts": hm2L2McastSnoopingQueryPortsAutoPorts,
       "hm2L2McastSnoopingQueryPortsAutoPortsState": hm2L2McastSnoopingQueryPortsAutoPortsState,
       "hm2L2McastSnoopingForwardAllTable": hm2L2McastSnoopingForwardAllTable,
       "hm2L2McastSnoopingForwardAllEntry": hm2L2McastSnoopingForwardAllEntry,
       "hm2L2McastSnoopingForwardAllStaticPorts": hm2L2McastSnoopingForwardAllStaticPorts,
       "hm2L2McastFilteringObjects": hm2L2McastFilteringObjects,
       "hm2L2McastFilteringGroup": hm2L2McastFilteringGroup,
       "hm2L2McastFilteringTable": hm2L2McastFilteringTable,
       "hm2L2McastFilteringEntry": hm2L2McastFilteringEntry,
       "hm2L2McastFilteringKnownMode": hm2L2McastFilteringKnownMode,
       "hm2L2McastFilteringUnknownMode": hm2L2McastFilteringUnknownMode,
       "hm2L2McastSnoopingStatistics": hm2L2McastSnoopingStatistics,
       "hm2L2McastSnoopingStatisticsGroup": hm2L2McastSnoopingStatisticsGroup,
       "hm2L2McastSnoopingIgmpReportsFramesProcessed": hm2L2McastSnoopingIgmpReportsFramesProcessed,
       "hm2L2McastSnoopingIgmpQueriesV1FramesProcessed": hm2L2McastSnoopingIgmpQueriesV1FramesProcessed,
       "hm2L2McastSnoopingIgmpQueriesV2FramesProcessed": hm2L2McastSnoopingIgmpQueriesV2FramesProcessed,
       "hm2L2McastSnoopingIgmpQueriesV3FramesProcessed": hm2L2McastSnoopingIgmpQueriesV3FramesProcessed,
       "hm2L2McastSnoopingIgmpWrongVersionQueries": hm2L2McastSnoopingIgmpWrongVersionQueries,
       "hm2L2McastSnoopingPimDvmrpFramesProcessed": hm2L2McastSnoopingPimDvmrpFramesProcessed,
       "hm2L2McastSnoopingStatisticsTable": hm2L2McastSnoopingStatisticsTable,
       "hm2L2McastSnoopingStatisticsEntry": hm2L2McastSnoopingStatisticsEntry,
       "hm2L2McastSnoopingIntfIgmpReportsFramesProcessed": hm2L2McastSnoopingIntfIgmpReportsFramesProcessed,
       "hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed": hm2L2McastSnoopingIntfIgmpQueriesV1FramesProcessed,
       "hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed": hm2L2McastSnoopingIntfIgmpQueriesV2FramesProcessed,
       "hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed": hm2L2McastSnoopingIntfIgmpQueriesV3FramesProcessed,
       "hm2L2McastSnoopingIntfIgmpWrongVersionQueries": hm2L2McastSnoopingIntfIgmpWrongVersionQueries,
       "hm2L2McastSnoopingIntfPimDvmrpFramesProcessed": hm2L2McastSnoopingIntfPimDvmrpFramesProcessed,
       "hm2L2McastSNMPExtensionGroup": hm2L2McastSNMPExtensionGroup,
       "hm2L2McastGroupMembershipErrorReturn": hm2L2McastGroupMembershipErrorReturn}
)
