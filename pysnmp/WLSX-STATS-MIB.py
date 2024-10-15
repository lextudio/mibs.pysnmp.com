# SNMP MIB module (WLSX-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WLSX-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:13 2024
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15)
)
wlsxStatsMIB.setRevisions(
        ("1907-12-10 00:06",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxStatsOpGroup_ObjectIdentity = ObjectIdentity
wlsxStatsOpGroup = _WlsxStatsOpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1)
)
_WlsxStatsRequestTable_Object = MibTable
wlsxStatsRequestTable = _WlsxStatsRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxStatsRequestTable.setStatus("current")
_WlsxStatsRequestEntry_Object = MibTableRow
wlsxStatsRequestEntry = _WlsxStatsRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1)
)
wlsxStatsRequestEntry.setIndexNames(
    (0, "WLSX-STATS-MIB", "wlsxStatsIndex"),
)
if mibBuilder.loadTexts:
    wlsxStatsRequestEntry.setStatus("current")
_WlsxStatsIndex_Type = Integer32
_WlsxStatsIndex_Object = MibTableColumn
wlsxStatsIndex = _WlsxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 1),
    _WlsxStatsIndex_Type()
)
wlsxStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxStatsIndex.setStatus("current")
_WlsxStatsReqType_Type = Integer32
_WlsxStatsReqType_Object = MibTableColumn
wlsxStatsReqType = _WlsxStatsReqType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 2),
    _WlsxStatsReqType_Type()
)
wlsxStatsReqType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxStatsReqType.setStatus("current")
_WlsxStatsInterval_Type = Integer32
_WlsxStatsInterval_Object = MibTableColumn
wlsxStatsInterval = _WlsxStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 3),
    _WlsxStatsInterval_Type()
)
wlsxStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxStatsInterval.setStatus("current")
_WlsxStatsCookie_Type = DisplayString
_WlsxStatsCookie_Object = MibTableColumn
wlsxStatsCookie = _WlsxStatsCookie_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 15, 1, 1, 1, 4),
    _WlsxStatsCookie_Type()
)
wlsxStatsCookie.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlsxStatsCookie.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-STATS-MIB",
    **{"wlsxStatsMIB": wlsxStatsMIB,
       "wlsxStatsOpGroup": wlsxStatsOpGroup,
       "wlsxStatsRequestTable": wlsxStatsRequestTable,
       "wlsxStatsRequestEntry": wlsxStatsRequestEntry,
       "wlsxStatsIndex": wlsxStatsIndex,
       "wlsxStatsReqType": wlsxStatsReqType,
       "wlsxStatsInterval": wlsxStatsInterval,
       "wlsxStatsCookie": wlsxStatsCookie}
)
