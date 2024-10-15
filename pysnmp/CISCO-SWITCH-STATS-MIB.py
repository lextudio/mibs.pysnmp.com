# SNMP MIB module (CISCO-SWITCH-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:19 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSwitchStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652)
)
ciscoSwitchStatsMIB.setRevisions(
        ("2013-01-30 00:00",
         "2009-10-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchStatsMIBNotifs = _CiscoSwitchStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 0)
)
_CiscoSwitchStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchStatsMIBObjects = _CiscoSwitchStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1)
)
_CsstConfigurableStats_ObjectIdentity = ObjectIdentity
csstConfigurableStats = _CsstConfigurableStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1)
)
_CsstConfigStatsOptionTable_Object = MibTable
csstConfigStatsOptionTable = _CsstConfigStatsOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csstConfigStatsOptionTable.setStatus("current")
_CsstConfigStatsOptionEntry_Object = MibTableRow
csstConfigStatsOptionEntry = _CsstConfigStatsOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 1, 1)
)
csstConfigStatsOptionEntry.setIndexNames(
    (0, "CISCO-SWITCH-STATS-MIB", "csstConfigStatsOptionIndex"),
)
if mibBuilder.loadTexts:
    csstConfigStatsOptionEntry.setStatus("current")


class _CsstConfigStatsOptionIndex_Type(Unsigned32):
    """Custom type csstConfigStatsOptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsstConfigStatsOptionIndex_Type.__name__ = "Unsigned32"
_CsstConfigStatsOptionIndex_Object = MibTableColumn
csstConfigStatsOptionIndex = _CsstConfigStatsOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 1, 1, 1),
    _CsstConfigStatsOptionIndex_Type()
)
csstConfigStatsOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstConfigStatsOptionIndex.setStatus("current")
_CsstConfigStatsOptionDesc_Type = SnmpAdminString
_CsstConfigStatsOptionDesc_Object = MibTableColumn
csstConfigStatsOptionDesc = _CsstConfigStatsOptionDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 1, 1, 2),
    _CsstConfigStatsOptionDesc_Type()
)
csstConfigStatsOptionDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsOptionDesc.setStatus("current")
_CsstConfigStatsMapSize_Type = Unsigned32
_CsstConfigStatsMapSize_Object = MibScalar
csstConfigStatsMapSize = _CsstConfigStatsMapSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 2),
    _CsstConfigStatsMapSize_Type()
)
csstConfigStatsMapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsMapSize.setStatus("current")


class _CsstConfigStatsMap_Type(OctetString):
    """Custom type csstConfigStatsMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CsstConfigStatsMap_Type.__name__ = "OctetString"
_CsstConfigStatsMap_Object = MibScalar
csstConfigStatsMap = _CsstConfigStatsMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 3),
    _CsstConfigStatsMap_Type()
)
csstConfigStatsMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csstConfigStatsMap.setStatus("current")
_CsstConfigStatsIfTable_Object = MibTable
csstConfigStatsIfTable = _CsstConfigStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4)
)
if mibBuilder.loadTexts:
    csstConfigStatsIfTable.setStatus("current")
_CsstConfigStatsIfEntry_Object = MibTableRow
csstConfigStatsIfEntry = _CsstConfigStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1)
)
csstConfigStatsIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csstConfigStatsIfEntry.setStatus("current")
_CsstConfigStatsIfPackets1_Type = Counter64
_CsstConfigStatsIfPackets1_Object = MibTableColumn
csstConfigStatsIfPackets1 = _CsstConfigStatsIfPackets1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 1),
    _CsstConfigStatsIfPackets1_Type()
)
csstConfigStatsIfPackets1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets1.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets1.setUnits("packets")
_CsstConfigStatsIfOctets1_Type = Counter64
_CsstConfigStatsIfOctets1_Object = MibTableColumn
csstConfigStatsIfOctets1 = _CsstConfigStatsIfOctets1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 2),
    _CsstConfigStatsIfOctets1_Type()
)
csstConfigStatsIfOctets1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets1.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets1.setUnits("octets")
_CsstConfigStatsIfPackets2_Type = Counter64
_CsstConfigStatsIfPackets2_Object = MibTableColumn
csstConfigStatsIfPackets2 = _CsstConfigStatsIfPackets2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 3),
    _CsstConfigStatsIfPackets2_Type()
)
csstConfigStatsIfPackets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets2.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets2.setUnits("packets")
_CsstConfigStatsIfOctets2_Type = Counter64
_CsstConfigStatsIfOctets2_Object = MibTableColumn
csstConfigStatsIfOctets2 = _CsstConfigStatsIfOctets2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 4),
    _CsstConfigStatsIfOctets2_Type()
)
csstConfigStatsIfOctets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets2.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets2.setUnits("octets")
_CsstConfigStatsIfPackets3_Type = Counter64
_CsstConfigStatsIfPackets3_Object = MibTableColumn
csstConfigStatsIfPackets3 = _CsstConfigStatsIfPackets3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 5),
    _CsstConfigStatsIfPackets3_Type()
)
csstConfigStatsIfPackets3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets3.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets3.setUnits("packets")
_CsstConfigStatsIfOctets3_Type = Counter64
_CsstConfigStatsIfOctets3_Object = MibTableColumn
csstConfigStatsIfOctets3 = _CsstConfigStatsIfOctets3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 6),
    _CsstConfigStatsIfOctets3_Type()
)
csstConfigStatsIfOctets3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets3.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets3.setUnits("octets")
_CsstConfigStatsIfPackets4_Type = Counter64
_CsstConfigStatsIfPackets4_Object = MibTableColumn
csstConfigStatsIfPackets4 = _CsstConfigStatsIfPackets4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 7),
    _CsstConfigStatsIfPackets4_Type()
)
csstConfigStatsIfPackets4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets4.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets4.setUnits("packets")
_CsstConfigStatsIfOctets4_Type = Counter64
_CsstConfigStatsIfOctets4_Object = MibTableColumn
csstConfigStatsIfOctets4 = _CsstConfigStatsIfOctets4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 8),
    _CsstConfigStatsIfOctets4_Type()
)
csstConfigStatsIfOctets4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets4.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets4.setUnits("octets")
_CsstConfigStatsIfPackets5_Type = Counter64
_CsstConfigStatsIfPackets5_Object = MibTableColumn
csstConfigStatsIfPackets5 = _CsstConfigStatsIfPackets5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 9),
    _CsstConfigStatsIfPackets5_Type()
)
csstConfigStatsIfPackets5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets5.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets5.setUnits("packets")
_CsstConfigStatsIfOctets5_Type = Counter64
_CsstConfigStatsIfOctets5_Object = MibTableColumn
csstConfigStatsIfOctets5 = _CsstConfigStatsIfOctets5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 10),
    _CsstConfigStatsIfOctets5_Type()
)
csstConfigStatsIfOctets5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets5.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets5.setUnits("octets")
_CsstConfigStatsIfPackets6_Type = Counter64
_CsstConfigStatsIfPackets6_Object = MibTableColumn
csstConfigStatsIfPackets6 = _CsstConfigStatsIfPackets6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 11),
    _CsstConfigStatsIfPackets6_Type()
)
csstConfigStatsIfPackets6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets6.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets6.setUnits("packets")
_CsstConfigStatsIfOctets6_Type = Counter64
_CsstConfigStatsIfOctets6_Object = MibTableColumn
csstConfigStatsIfOctets6 = _CsstConfigStatsIfOctets6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 12),
    _CsstConfigStatsIfOctets6_Type()
)
csstConfigStatsIfOctets6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets6.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets6.setUnits("octets")
_CsstConfigStatsIfPackets7_Type = Counter64
_CsstConfigStatsIfPackets7_Object = MibTableColumn
csstConfigStatsIfPackets7 = _CsstConfigStatsIfPackets7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 13),
    _CsstConfigStatsIfPackets7_Type()
)
csstConfigStatsIfPackets7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets7.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets7.setUnits("packets")
_CsstConfigStatsIfOctets7_Type = Counter64
_CsstConfigStatsIfOctets7_Object = MibTableColumn
csstConfigStatsIfOctets7 = _CsstConfigStatsIfOctets7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 14),
    _CsstConfigStatsIfOctets7_Type()
)
csstConfigStatsIfOctets7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets7.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets7.setUnits("octets")
_CsstConfigStatsIfPackets8_Type = Counter64
_CsstConfigStatsIfPackets8_Object = MibTableColumn
csstConfigStatsIfPackets8 = _CsstConfigStatsIfPackets8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 15),
    _CsstConfigStatsIfPackets8_Type()
)
csstConfigStatsIfPackets8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets8.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfPackets8.setUnits("packets")
_CsstConfigStatsIfOctets8_Type = Counter64
_CsstConfigStatsIfOctets8_Object = MibTableColumn
csstConfigStatsIfOctets8 = _CsstConfigStatsIfOctets8_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 1, 4, 1, 16),
    _CsstConfigStatsIfOctets8_Type()
)
csstConfigStatsIfOctets8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets8.setStatus("current")
if mibBuilder.loadTexts:
    csstConfigStatsIfOctets8.setUnits("octets")
_CsstVlanStats_ObjectIdentity = ObjectIdentity
csstVlanStats = _CsstVlanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2)
)
_CsstVlanStatsTable_Object = MibTable
csstVlanStatsTable = _CsstVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csstVlanStatsTable.setStatus("current")
_CsstVlanStatsEntry_Object = MibTableRow
csstVlanStatsEntry = _CsstVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1)
)
csstVlanStatsEntry.setIndexNames(
    (0, "CISCO-SWITCH-STATS-MIB", "csstVlanIndex"),
)
if mibBuilder.loadTexts:
    csstVlanStatsEntry.setStatus("current")
_CsstVlanIndex_Type = VlanIndex
_CsstVlanIndex_Object = MibTableColumn
csstVlanIndex = _CsstVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1, 1),
    _CsstVlanIndex_Type()
)
csstVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstVlanIndex.setStatus("current")
_CsstVlanKnownBridgedUcastPkts_Type = Counter64
_CsstVlanKnownBridgedUcastPkts_Object = MibTableColumn
csstVlanKnownBridgedUcastPkts = _CsstVlanKnownBridgedUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1, 2),
    _CsstVlanKnownBridgedUcastPkts_Type()
)
csstVlanKnownBridgedUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedUcastPkts.setUnits("packets")
_CsstVlanKnownBridgedUcastOctets_Type = Counter64
_CsstVlanKnownBridgedUcastOctets_Object = MibTableColumn
csstVlanKnownBridgedUcastOctets = _CsstVlanKnownBridgedUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1, 3),
    _CsstVlanKnownBridgedUcastOctets_Type()
)
csstVlanKnownBridgedUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedUcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedUcastOctets.setUnits("octets")
_CsstVlanKnownBridgedNUcastPkts_Type = Counter64
_CsstVlanKnownBridgedNUcastPkts_Object = MibTableColumn
csstVlanKnownBridgedNUcastPkts = _CsstVlanKnownBridgedNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1, 4),
    _CsstVlanKnownBridgedNUcastPkts_Type()
)
csstVlanKnownBridgedNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedNUcastPkts.setUnits("packets")
_CsstVlanKnownBridgedNUcastOctets_Type = Counter64
_CsstVlanKnownBridgedNUcastOctets_Object = MibTableColumn
csstVlanKnownBridgedNUcastOctets = _CsstVlanKnownBridgedNUcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 2, 1, 1, 5),
    _CsstVlanKnownBridgedNUcastOctets_Type()
)
csstVlanKnownBridgedNUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedNUcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    csstVlanKnownBridgedNUcastOctets.setUnits("octets")
_CsstSwitchTrafficStats_ObjectIdentity = ObjectIdentity
csstSwitchTrafficStats = _CsstSwitchTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3)
)
_CsstSwitchStatsTable_Object = MibTable
csstSwitchStatsTable = _CsstSwitchStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csstSwitchStatsTable.setStatus("current")
_CsstSwitchStatsEntry_Object = MibTableRow
csstSwitchStatsEntry = _CsstSwitchStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1)
)
csstSwitchStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    csstSwitchStatsEntry.setStatus("current")
_CsstL2TotalBridgedPkts_Type = Counter32
_CsstL2TotalBridgedPkts_Object = MibTableColumn
csstL2TotalBridgedPkts = _CsstL2TotalBridgedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 1),
    _CsstL2TotalBridgedPkts_Type()
)
csstL2TotalBridgedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL2TotalBridgedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL2TotalBridgedPkts.setUnits("packets")
_CsstL3FibSwitchedIpv4UcastPkts_Type = Counter32
_CsstL3FibSwitchedIpv4UcastPkts_Object = MibTableColumn
csstL3FibSwitchedIpv4UcastPkts = _CsstL3FibSwitchedIpv4UcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 2),
    _CsstL3FibSwitchedIpv4UcastPkts_Type()
)
csstL3FibSwitchedIpv4UcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3FibSwitchedIpv4UcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3FibSwitchedIpv4UcastPkts.setUnits("packets")
_CsstL3FibSwitchedIpv6UcastPkts_Type = Counter32
_CsstL3FibSwitchedIpv6UcastPkts_Object = MibTableColumn
csstL3FibSwitchedIpv6UcastPkts = _CsstL3FibSwitchedIpv6UcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 3),
    _CsstL3FibSwitchedIpv6UcastPkts_Type()
)
csstL3FibSwitchedIpv6UcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3FibSwitchedIpv6UcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3FibSwitchedIpv6UcastPkts.setUnits("packets")
_CsstL3FibSwitchedEoMplsPkts_Type = Counter32
_CsstL3FibSwitchedEoMplsPkts_Object = MibTableColumn
csstL3FibSwitchedEoMplsPkts = _CsstL3FibSwitchedEoMplsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 4),
    _CsstL3FibSwitchedEoMplsPkts_Type()
)
csstL3FibSwitchedEoMplsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3FibSwitchedEoMplsPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3FibSwitchedEoMplsPkts.setUnits("packets")
_CsstL3FibSwitchedMplsPkts_Type = Counter32
_CsstL3FibSwitchedMplsPkts_Object = MibTableColumn
csstL3FibSwitchedMplsPkts = _CsstL3FibSwitchedMplsPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 5),
    _CsstL3FibSwitchedMplsPkts_Type()
)
csstL3FibSwitchedMplsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3FibSwitchedMplsPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3FibSwitchedMplsPkts.setUnits("packets")
_CsstL3TotalMulticastPkts_Type = Counter32
_CsstL3TotalMulticastPkts_Object = MibTableColumn
csstL3TotalMulticastPkts = _CsstL3TotalMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 6),
    _CsstL3TotalMulticastPkts_Type()
)
csstL3TotalMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3TotalMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3TotalMulticastPkts.setUnits("packets")
_CsstL3IgmpMldPkts_Type = Counter32
_CsstL3IgmpMldPkts_Object = MibTableColumn
csstL3IgmpMldPkts = _CsstL3IgmpMldPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 7),
    _CsstL3IgmpMldPkts_Type()
)
csstL3IgmpMldPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3IgmpMldPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3IgmpMldPkts.setUnits("packets")
_CsstL3Ipv4MulticastPkts_Type = Counter32
_CsstL3Ipv4MulticastPkts_Object = MibTableColumn
csstL3Ipv4MulticastPkts = _CsstL3Ipv4MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 8),
    _CsstL3Ipv4MulticastPkts_Type()
)
csstL3Ipv4MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3Ipv4MulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3Ipv4MulticastPkts.setUnits("packets")
_CsstL3Ipv6MulticastPkts_Type = Counter32
_CsstL3Ipv6MulticastPkts_Object = MibTableColumn
csstL3Ipv6MulticastPkts = _CsstL3Ipv6MulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 9),
    _CsstL3Ipv6MulticastPkts_Type()
)
csstL3Ipv6MulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3Ipv6MulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3Ipv6MulticastPkts.setUnits("packets")
_CsstL3MulticastLeakPkts_Type = Counter32
_CsstL3MulticastLeakPkts_Object = MibTableColumn
csstL3MulticastLeakPkts = _CsstL3MulticastLeakPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 10),
    _CsstL3MulticastLeakPkts_Type()
)
csstL3MulticastLeakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3MulticastLeakPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3MulticastLeakPkts.setUnits("packets")
_CsstL3InputAclRoutedPkts_Type = Counter32
_CsstL3InputAclRoutedPkts_Object = MibTableColumn
csstL3InputAclRoutedPkts = _CsstL3InputAclRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 11),
    _CsstL3InputAclRoutedPkts_Type()
)
csstL3InputAclRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3InputAclRoutedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3InputAclRoutedPkts.setUnits("packets")
_CsstL3OutputAclRoutedPkts_Type = Counter32
_CsstL3OutputAclRoutedPkts_Object = MibTableColumn
csstL3OutputAclRoutedPkts = _CsstL3OutputAclRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 12),
    _CsstL3OutputAclRoutedPkts_Type()
)
csstL3OutputAclRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3OutputAclRoutedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3OutputAclRoutedPkts.setUnits("packets")
_CsstL3InputNetflowSwitchedPkts_Type = Counter32
_CsstL3InputNetflowSwitchedPkts_Object = MibTableColumn
csstL3InputNetflowSwitchedPkts = _CsstL3InputNetflowSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 13),
    _CsstL3InputNetflowSwitchedPkts_Type()
)
csstL3InputNetflowSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3InputNetflowSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3InputNetflowSwitchedPkts.setUnits("packets")
_CsstL3OutputNetflowSwitchedPkts_Type = Counter32
_CsstL3OutputNetflowSwitchedPkts_Object = MibTableColumn
csstL3OutputNetflowSwitchedPkts = _CsstL3OutputNetflowSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 14),
    _CsstL3OutputNetflowSwitchedPkts_Type()
)
csstL3OutputNetflowSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3OutputNetflowSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3OutputNetflowSwitchedPkts.setUnits("packets")
_CsstL3InExceptionRedirectPkts_Type = Counter32
_CsstL3InExceptionRedirectPkts_Object = MibTableColumn
csstL3InExceptionRedirectPkts = _CsstL3InExceptionRedirectPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 15),
    _CsstL3InExceptionRedirectPkts_Type()
)
csstL3InExceptionRedirectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3InExceptionRedirectPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3InExceptionRedirectPkts.setUnits("packets")
_CsstL3OutExceptionRedirectPkts_Type = Counter32
_CsstL3OutExceptionRedirectPkts_Object = MibTableColumn
csstL3OutExceptionRedirectPkts = _CsstL3OutExceptionRedirectPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 16),
    _CsstL3OutExceptionRedirectPkts_Type()
)
csstL3OutExceptionRedirectPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3OutExceptionRedirectPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3OutExceptionRedirectPkts.setUnits("packets")
_CsstL3TotalNetflowSwitchedPkts_Type = Counter32
_CsstL3TotalNetflowSwitchedPkts_Object = MibTableColumn
csstL3TotalNetflowSwitchedPkts = _CsstL3TotalNetflowSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 17),
    _CsstL3TotalNetflowSwitchedPkts_Type()
)
csstL3TotalNetflowSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3TotalNetflowSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3TotalNetflowSwitchedPkts.setUnits("packets")
_CsstL3TotalAclRoutedPkts_Type = Counter32
_CsstL3TotalAclRoutedPkts_Object = MibTableColumn
csstL3TotalAclRoutedPkts = _CsstL3TotalAclRoutedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 18),
    _CsstL3TotalAclRoutedPkts_Type()
)
csstL3TotalAclRoutedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstL3TotalAclRoutedPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstL3TotalAclRoutedPkts.setUnits("packets")
_CsstTotalAclDenyPkts_Type = Counter32
_CsstTotalAclDenyPkts_Object = MibTableColumn
csstTotalAclDenyPkts = _CsstTotalAclDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 3, 1, 1, 19),
    _CsstTotalAclDenyPkts_Type()
)
csstTotalAclDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstTotalAclDenyPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstTotalAclDenyPkts.setUnits("packets")
_CsstHwInternalStats_ObjectIdentity = ObjectIdentity
csstHwInternalStats = _CsstHwInternalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4)
)
_CsstHwInternalStatsTable_Object = MibTable
csstHwInternalStatsTable = _CsstHwInternalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1)
)
if mibBuilder.loadTexts:
    csstHwInternalStatsTable.setStatus("current")
_CsstHwInternalStatsEntry_Object = MibTableRow
csstHwInternalStatsEntry = _CsstHwInternalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1)
)
csstHwInternalStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsDeviceId"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsInstanceNum"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsDirection"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsType"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsIndex"),
)
if mibBuilder.loadTexts:
    csstHwInternalStatsEntry.setStatus("current")
_CsstHwInternalStatsDeviceId_Type = Unsigned32
_CsstHwInternalStatsDeviceId_Object = MibTableColumn
csstHwInternalStatsDeviceId = _CsstHwInternalStatsDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 1),
    _CsstHwInternalStatsDeviceId_Type()
)
csstHwInternalStatsDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalStatsDeviceId.setStatus("current")
_CsstHwInternalStatsInstanceNum_Type = Unsigned32
_CsstHwInternalStatsInstanceNum_Object = MibTableColumn
csstHwInternalStatsInstanceNum = _CsstHwInternalStatsInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 2),
    _CsstHwInternalStatsInstanceNum_Type()
)
csstHwInternalStatsInstanceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalStatsInstanceNum.setStatus("current")


class _CsstHwInternalStatsDirection_Type(Integer32):
    """Custom type csstHwInternalStatsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("egressIn", 3),
          ("egressOut", 4),
          ("ingressIn", 1),
          ("ingressOut", 2))
    )


_CsstHwInternalStatsDirection_Type.__name__ = "Integer32"
_CsstHwInternalStatsDirection_Object = MibTableColumn
csstHwInternalStatsDirection = _CsstHwInternalStatsDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 3),
    _CsstHwInternalStatsDirection_Type()
)
csstHwInternalStatsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalStatsDirection.setStatus("current")


class _CsstHwInternalStatsType_Type(Integer32):
    """Custom type csstHwInternalStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytesPerSec", 2),
          ("packetsPerSec", 1))
    )


_CsstHwInternalStatsType_Type.__name__ = "Integer32"
_CsstHwInternalStatsType_Object = MibTableColumn
csstHwInternalStatsType = _CsstHwInternalStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 4),
    _CsstHwInternalStatsType_Type()
)
csstHwInternalStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalStatsType.setStatus("current")
_CsstHwInternalStatsIndex_Type = Unsigned32
_CsstHwInternalStatsIndex_Object = MibTableColumn
csstHwInternalStatsIndex = _CsstHwInternalStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 5),
    _CsstHwInternalStatsIndex_Type()
)
csstHwInternalStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalStatsIndex.setStatus("current")
_CsstHwInternalStatsDescr_Type = SnmpAdminString
_CsstHwInternalStatsDescr_Object = MibTableColumn
csstHwInternalStatsDescr = _CsstHwInternalStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 6),
    _CsstHwInternalStatsDescr_Type()
)
csstHwInternalStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalStatsDescr.setStatus("current")
_CsstHwInternalStatsRate_Type = Gauge32
_CsstHwInternalStatsRate_Object = MibTableColumn
csstHwInternalStatsRate = _CsstHwInternalStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 1, 1, 7),
    _CsstHwInternalStatsRate_Type()
)
csstHwInternalStatsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalStatsRate.setStatus("current")
_CsstHwInternalErrorTable_Object = MibTable
csstHwInternalErrorTable = _CsstHwInternalErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2)
)
if mibBuilder.loadTexts:
    csstHwInternalErrorTable.setStatus("current")
_CsstHwInternalErrorEntry_Object = MibTableRow
csstHwInternalErrorEntry = _CsstHwInternalErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2, 1)
)
csstHwInternalErrorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorDeviceId"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorCategory"),
)
if mibBuilder.loadTexts:
    csstHwInternalErrorEntry.setStatus("current")
_CsstHwInternalErrorDeviceId_Type = Unsigned32
_CsstHwInternalErrorDeviceId_Object = MibTableColumn
csstHwInternalErrorDeviceId = _CsstHwInternalErrorDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2, 1, 1),
    _CsstHwInternalErrorDeviceId_Type()
)
csstHwInternalErrorDeviceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalErrorDeviceId.setStatus("current")


class _CsstHwInternalErrorCategory_Type(Integer32):
    """Custom type csstHwInternalErrorCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("congestion", 2),
          ("error", 1),
          ("qos", 3))
    )


_CsstHwInternalErrorCategory_Type.__name__ = "Integer32"
_CsstHwInternalErrorCategory_Object = MibTableColumn
csstHwInternalErrorCategory = _CsstHwInternalErrorCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2, 1, 2),
    _CsstHwInternalErrorCategory_Type()
)
csstHwInternalErrorCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalErrorCategory.setStatus("current")
_CsstHwInternalErrorDeviceInfo_Type = SnmpAdminString
_CsstHwInternalErrorDeviceInfo_Object = MibTableColumn
csstHwInternalErrorDeviceInfo = _CsstHwInternalErrorDeviceInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2, 1, 3),
    _CsstHwInternalErrorDeviceInfo_Type()
)
csstHwInternalErrorDeviceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalErrorDeviceInfo.setStatus("current")
_CsstHwInternalErrorLastCleared_Type = DateAndTime
_CsstHwInternalErrorLastCleared_Object = MibTableColumn
csstHwInternalErrorLastCleared = _CsstHwInternalErrorLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 2, 1, 4),
    _CsstHwInternalErrorLastCleared_Type()
)
csstHwInternalErrorLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalErrorLastCleared.setStatus("current")
_CsstHwInternalErrorInstTable_Object = MibTable
csstHwInternalErrorInstTable = _CsstHwInternalErrorInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3)
)
if mibBuilder.loadTexts:
    csstHwInternalErrorInstTable.setStatus("current")
_CsstHwInternalErrorInstEntry_Object = MibTableRow
csstHwInternalErrorInstEntry = _CsstHwInternalErrorInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1)
)
csstHwInternalErrorInstEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorDeviceId"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorCategory"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorInstNum"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorInstErrorId"),
)
if mibBuilder.loadTexts:
    csstHwInternalErrorInstEntry.setStatus("current")
_CsstHwInternalErrorInstNum_Type = Unsigned32
_CsstHwInternalErrorInstNum_Object = MibTableColumn
csstHwInternalErrorInstNum = _CsstHwInternalErrorInstNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1, 1),
    _CsstHwInternalErrorInstNum_Type()
)
csstHwInternalErrorInstNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalErrorInstNum.setStatus("current")
_CsstHwInternalErrorInstErrorId_Type = Unsigned32
_CsstHwInternalErrorInstErrorId_Object = MibTableColumn
csstHwInternalErrorInstErrorId = _CsstHwInternalErrorInstErrorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1, 2),
    _CsstHwInternalErrorInstErrorId_Type()
)
csstHwInternalErrorInstErrorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstHwInternalErrorInstErrorId.setStatus("current")
_CsstHwInternalErrorInstDescr_Type = SnmpAdminString
_CsstHwInternalErrorInstDescr_Object = MibTableColumn
csstHwInternalErrorInstDescr = _CsstHwInternalErrorInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1, 3),
    _CsstHwInternalErrorInstDescr_Type()
)
csstHwInternalErrorInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalErrorInstDescr.setStatus("current")
_CsstHwInternalErrorInstCount_Type = Counter64
_CsstHwInternalErrorInstCount_Object = MibTableColumn
csstHwInternalErrorInstCount = _CsstHwInternalErrorInstCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1, 4),
    _CsstHwInternalErrorInstCount_Type()
)
csstHwInternalErrorInstCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalErrorInstCount.setStatus("current")
_CsstHwInternalErrorInstPorts_Type = SnmpAdminString
_CsstHwInternalErrorInstPorts_Object = MibTableColumn
csstHwInternalErrorInstPorts = _CsstHwInternalErrorInstPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 4, 3, 1, 5),
    _CsstHwInternalErrorInstPorts_Type()
)
csstHwInternalErrorInstPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstHwInternalErrorInstPorts.setStatus("current")
_CsstRewriteEngineStats_ObjectIdentity = ObjectIdentity
csstRewriteEngineStats = _CsstRewriteEngineStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5)
)
_CsstRewriteEnginePktDropStatsTable_Object = MibTable
csstRewriteEnginePktDropStatsTable = _CsstRewriteEnginePktDropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5, 1)
)
if mibBuilder.loadTexts:
    csstRewriteEnginePktDropStatsTable.setStatus("current")
_CsstRewriteEnginePktDropStatsEntry_Object = MibTableRow
csstRewriteEnginePktDropStatsEntry = _CsstRewriteEnginePktDropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5, 1, 1)
)
csstRewriteEnginePktDropStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-STATS-MIB", "csstRewriteEngineChannelIndex"),
)
if mibBuilder.loadTexts:
    csstRewriteEnginePktDropStatsEntry.setStatus("current")
_CsstRewriteEngineChannelIndex_Type = Unsigned32
_CsstRewriteEngineChannelIndex_Object = MibTableColumn
csstRewriteEngineChannelIndex = _CsstRewriteEngineChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5, 1, 1, 1),
    _CsstRewriteEngineChannelIndex_Type()
)
csstRewriteEngineChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csstRewriteEngineChannelIndex.setStatus("current")
_CsstRewriteEngineDropPkts_Type = Counter64
_CsstRewriteEngineDropPkts_Object = MibTableColumn
csstRewriteEngineDropPkts = _CsstRewriteEngineDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5, 1, 1, 2),
    _CsstRewriteEngineDropPkts_Type()
)
csstRewriteEngineDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstRewriteEngineDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    csstRewriteEngineDropPkts.setUnits("packets")
_CsstRewriteEngineTotalOverruns_Type = Counter32
_CsstRewriteEngineTotalOverruns_Object = MibTableColumn
csstRewriteEngineTotalOverruns = _CsstRewriteEngineTotalOverruns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 1, 5, 1, 1, 3),
    _CsstRewriteEngineTotalOverruns_Type()
)
csstRewriteEngineTotalOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csstRewriteEngineTotalOverruns.setStatus("current")
_CiscoSwitchStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoSwitchStatsMIBConform = _CiscoSwitchStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2)
)
_CsstSwitchStatsMIBCompliances_ObjectIdentity = ObjectIdentity
csstSwitchStatsMIBCompliances = _CsstSwitchStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 1)
)
_CsstSwitchStatsMIBGroups_ObjectIdentity = ObjectIdentity
csstSwitchStatsMIBGroups = _CsstSwitchStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2)
)

# Managed Objects groups

ciscoSwitchStatsConfOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 1)
)
ciscoSwitchStatsConfOptionGroup.setObjects(
    ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsOptionDesc")
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsConfOptionGroup.setStatus("current")

ciscoSwitchStatsConfMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 2)
)
ciscoSwitchStatsConfMapGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstConfigStatsMapSize"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsMap"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsConfMapGroup.setStatus("current")

ciscoSwitchStatsConfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 3)
)
ciscoSwitchStatsConfIfGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets1"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets1"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets2"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets2"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets3"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets3"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets4"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets4"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets5"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets5"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets6"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets6"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets7"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets7"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfPackets8"),
        ("CISCO-SWITCH-STATS-MIB", "csstConfigStatsIfOctets8"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsConfIfGroup.setStatus("current")

ciscoSwitchStatsVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 4)
)
ciscoSwitchStatsVlanGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstVlanKnownBridgedUcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstVlanKnownBridgedUcastOctets"),
        ("CISCO-SWITCH-STATS-MIB", "csstVlanKnownBridgedNUcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstVlanKnownBridgedNUcastOctets"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsVlanGroup.setStatus("current")

ciscoSwitchStatsL2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 5)
)
ciscoSwitchStatsL2Group.setObjects(
    ("CISCO-SWITCH-STATS-MIB", "csstL2TotalBridgedPkts")
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsL2Group.setStatus("current")

ciscoSwitchStatsL3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 6)
)
ciscoSwitchStatsL3Group.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedIpv4UcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedIpv6UcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedEoMplsPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedMplsPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3TotalMulticastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3IgmpMldPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3Ipv4MulticastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3Ipv6MulticastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3MulticastLeakPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InputAclRoutedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutputAclRoutedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InputNetflowSwitchedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutputNetflowSwitchedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InExceptionRedirectPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutExceptionRedirectPkts"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsL3Group.setStatus("deprecated")

ciscoSwitchStatsLayer3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 7)
)
ciscoSwitchStatsLayer3Group.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedIpv4UcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedIpv6UcastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedEoMplsPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3FibSwitchedMplsPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3IgmpMldPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3Ipv4MulticastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3Ipv6MulticastPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3MulticastLeakPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InputAclRoutedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutputAclRoutedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InputNetflowSwitchedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutputNetflowSwitchedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3InExceptionRedirectPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3OutExceptionRedirectPkts"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsLayer3Group.setStatus("current")

ciscoSwitchStatsLayer3ExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 8)
)
ciscoSwitchStatsLayer3ExtGroup.setObjects(
    ("CISCO-SWITCH-STATS-MIB", "csstL3TotalMulticastPkts")
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsLayer3ExtGroup.setStatus("current")

ciscoSwitchStatsTotalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 9)
)
ciscoSwitchStatsTotalGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstL3TotalNetflowSwitchedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstL3TotalAclRoutedPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstTotalAclDenyPkts"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsTotalGroup.setStatus("current")

ciscoSwitchStatsInternalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 10)
)
ciscoSwitchStatsInternalStatsGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsDescr"),
        ("CISCO-SWITCH-STATS-MIB", "csstHwInternalStatsRate"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsInternalStatsGroup.setStatus("current")

ciscoSwitchStatsInternalErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 11)
)
ciscoSwitchStatsInternalErrorGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorDeviceInfo"),
        ("CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorLastCleared"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsInternalErrorGroup.setStatus("current")

ciscoSwitchStatsInternalInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 12)
)
ciscoSwitchStatsInternalInstanceGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorInstDescr"),
        ("CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorInstCount"),
        ("CISCO-SWITCH-STATS-MIB", "csstHwInternalErrorInstPorts"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsInternalInstanceGroup.setStatus("current")

ciscoSwitchStatsRewriteEngineStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 2, 13)
)
ciscoSwitchStatsRewriteEngineStatsGroup.setObjects(
      *(("CISCO-SWITCH-STATS-MIB", "csstRewriteEngineDropPkts"),
        ("CISCO-SWITCH-STATS-MIB", "csstRewriteEngineTotalOverruns"))
)
if mibBuilder.loadTexts:
    ciscoSwitchStatsRewriteEngineStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csstSwitchStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csstSwitchStatsMIBCompliance.setStatus(
        "deprecated"
    )

csstSwitchStatsMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 652, 2, 1, 2)
)
if mibBuilder.loadTexts:
    csstSwitchStatsMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-STATS-MIB",
    **{"ciscoSwitchStatsMIB": ciscoSwitchStatsMIB,
       "ciscoSwitchStatsMIBNotifs": ciscoSwitchStatsMIBNotifs,
       "ciscoSwitchStatsMIBObjects": ciscoSwitchStatsMIBObjects,
       "csstConfigurableStats": csstConfigurableStats,
       "csstConfigStatsOptionTable": csstConfigStatsOptionTable,
       "csstConfigStatsOptionEntry": csstConfigStatsOptionEntry,
       "csstConfigStatsOptionIndex": csstConfigStatsOptionIndex,
       "csstConfigStatsOptionDesc": csstConfigStatsOptionDesc,
       "csstConfigStatsMapSize": csstConfigStatsMapSize,
       "csstConfigStatsMap": csstConfigStatsMap,
       "csstConfigStatsIfTable": csstConfigStatsIfTable,
       "csstConfigStatsIfEntry": csstConfigStatsIfEntry,
       "csstConfigStatsIfPackets1": csstConfigStatsIfPackets1,
       "csstConfigStatsIfOctets1": csstConfigStatsIfOctets1,
       "csstConfigStatsIfPackets2": csstConfigStatsIfPackets2,
       "csstConfigStatsIfOctets2": csstConfigStatsIfOctets2,
       "csstConfigStatsIfPackets3": csstConfigStatsIfPackets3,
       "csstConfigStatsIfOctets3": csstConfigStatsIfOctets3,
       "csstConfigStatsIfPackets4": csstConfigStatsIfPackets4,
       "csstConfigStatsIfOctets4": csstConfigStatsIfOctets4,
       "csstConfigStatsIfPackets5": csstConfigStatsIfPackets5,
       "csstConfigStatsIfOctets5": csstConfigStatsIfOctets5,
       "csstConfigStatsIfPackets6": csstConfigStatsIfPackets6,
       "csstConfigStatsIfOctets6": csstConfigStatsIfOctets6,
       "csstConfigStatsIfPackets7": csstConfigStatsIfPackets7,
       "csstConfigStatsIfOctets7": csstConfigStatsIfOctets7,
       "csstConfigStatsIfPackets8": csstConfigStatsIfPackets8,
       "csstConfigStatsIfOctets8": csstConfigStatsIfOctets8,
       "csstVlanStats": csstVlanStats,
       "csstVlanStatsTable": csstVlanStatsTable,
       "csstVlanStatsEntry": csstVlanStatsEntry,
       "csstVlanIndex": csstVlanIndex,
       "csstVlanKnownBridgedUcastPkts": csstVlanKnownBridgedUcastPkts,
       "csstVlanKnownBridgedUcastOctets": csstVlanKnownBridgedUcastOctets,
       "csstVlanKnownBridgedNUcastPkts": csstVlanKnownBridgedNUcastPkts,
       "csstVlanKnownBridgedNUcastOctets": csstVlanKnownBridgedNUcastOctets,
       "csstSwitchTrafficStats": csstSwitchTrafficStats,
       "csstSwitchStatsTable": csstSwitchStatsTable,
       "csstSwitchStatsEntry": csstSwitchStatsEntry,
       "csstL2TotalBridgedPkts": csstL2TotalBridgedPkts,
       "csstL3FibSwitchedIpv4UcastPkts": csstL3FibSwitchedIpv4UcastPkts,
       "csstL3FibSwitchedIpv6UcastPkts": csstL3FibSwitchedIpv6UcastPkts,
       "csstL3FibSwitchedEoMplsPkts": csstL3FibSwitchedEoMplsPkts,
       "csstL3FibSwitchedMplsPkts": csstL3FibSwitchedMplsPkts,
       "csstL3TotalMulticastPkts": csstL3TotalMulticastPkts,
       "csstL3IgmpMldPkts": csstL3IgmpMldPkts,
       "csstL3Ipv4MulticastPkts": csstL3Ipv4MulticastPkts,
       "csstL3Ipv6MulticastPkts": csstL3Ipv6MulticastPkts,
       "csstL3MulticastLeakPkts": csstL3MulticastLeakPkts,
       "csstL3InputAclRoutedPkts": csstL3InputAclRoutedPkts,
       "csstL3OutputAclRoutedPkts": csstL3OutputAclRoutedPkts,
       "csstL3InputNetflowSwitchedPkts": csstL3InputNetflowSwitchedPkts,
       "csstL3OutputNetflowSwitchedPkts": csstL3OutputNetflowSwitchedPkts,
       "csstL3InExceptionRedirectPkts": csstL3InExceptionRedirectPkts,
       "csstL3OutExceptionRedirectPkts": csstL3OutExceptionRedirectPkts,
       "csstL3TotalNetflowSwitchedPkts": csstL3TotalNetflowSwitchedPkts,
       "csstL3TotalAclRoutedPkts": csstL3TotalAclRoutedPkts,
       "csstTotalAclDenyPkts": csstTotalAclDenyPkts,
       "csstHwInternalStats": csstHwInternalStats,
       "csstHwInternalStatsTable": csstHwInternalStatsTable,
       "csstHwInternalStatsEntry": csstHwInternalStatsEntry,
       "csstHwInternalStatsDeviceId": csstHwInternalStatsDeviceId,
       "csstHwInternalStatsInstanceNum": csstHwInternalStatsInstanceNum,
       "csstHwInternalStatsDirection": csstHwInternalStatsDirection,
       "csstHwInternalStatsType": csstHwInternalStatsType,
       "csstHwInternalStatsIndex": csstHwInternalStatsIndex,
       "csstHwInternalStatsDescr": csstHwInternalStatsDescr,
       "csstHwInternalStatsRate": csstHwInternalStatsRate,
       "csstHwInternalErrorTable": csstHwInternalErrorTable,
       "csstHwInternalErrorEntry": csstHwInternalErrorEntry,
       "csstHwInternalErrorDeviceId": csstHwInternalErrorDeviceId,
       "csstHwInternalErrorCategory": csstHwInternalErrorCategory,
       "csstHwInternalErrorDeviceInfo": csstHwInternalErrorDeviceInfo,
       "csstHwInternalErrorLastCleared": csstHwInternalErrorLastCleared,
       "csstHwInternalErrorInstTable": csstHwInternalErrorInstTable,
       "csstHwInternalErrorInstEntry": csstHwInternalErrorInstEntry,
       "csstHwInternalErrorInstNum": csstHwInternalErrorInstNum,
       "csstHwInternalErrorInstErrorId": csstHwInternalErrorInstErrorId,
       "csstHwInternalErrorInstDescr": csstHwInternalErrorInstDescr,
       "csstHwInternalErrorInstCount": csstHwInternalErrorInstCount,
       "csstHwInternalErrorInstPorts": csstHwInternalErrorInstPorts,
       "csstRewriteEngineStats": csstRewriteEngineStats,
       "csstRewriteEnginePktDropStatsTable": csstRewriteEnginePktDropStatsTable,
       "csstRewriteEnginePktDropStatsEntry": csstRewriteEnginePktDropStatsEntry,
       "csstRewriteEngineChannelIndex": csstRewriteEngineChannelIndex,
       "csstRewriteEngineDropPkts": csstRewriteEngineDropPkts,
       "csstRewriteEngineTotalOverruns": csstRewriteEngineTotalOverruns,
       "ciscoSwitchStatsMIBConform": ciscoSwitchStatsMIBConform,
       "csstSwitchStatsMIBCompliances": csstSwitchStatsMIBCompliances,
       "csstSwitchStatsMIBCompliance": csstSwitchStatsMIBCompliance,
       "csstSwitchStatsMIBCompliance2": csstSwitchStatsMIBCompliance2,
       "csstSwitchStatsMIBGroups": csstSwitchStatsMIBGroups,
       "ciscoSwitchStatsConfOptionGroup": ciscoSwitchStatsConfOptionGroup,
       "ciscoSwitchStatsConfMapGroup": ciscoSwitchStatsConfMapGroup,
       "ciscoSwitchStatsConfIfGroup": ciscoSwitchStatsConfIfGroup,
       "ciscoSwitchStatsVlanGroup": ciscoSwitchStatsVlanGroup,
       "ciscoSwitchStatsL2Group": ciscoSwitchStatsL2Group,
       "ciscoSwitchStatsL3Group": ciscoSwitchStatsL3Group,
       "ciscoSwitchStatsLayer3Group": ciscoSwitchStatsLayer3Group,
       "ciscoSwitchStatsLayer3ExtGroup": ciscoSwitchStatsLayer3ExtGroup,
       "ciscoSwitchStatsTotalGroup": ciscoSwitchStatsTotalGroup,
       "ciscoSwitchStatsInternalStatsGroup": ciscoSwitchStatsInternalStatsGroup,
       "ciscoSwitchStatsInternalErrorGroup": ciscoSwitchStatsInternalErrorGroup,
       "ciscoSwitchStatsInternalInstanceGroup": ciscoSwitchStatsInternalInstanceGroup,
       "ciscoSwitchStatsRewriteEngineStatsGroup": ciscoSwitchStatsRewriteEngineStatsGroup}
)
