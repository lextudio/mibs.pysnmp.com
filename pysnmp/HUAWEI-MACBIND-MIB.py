# SNMP MIB module (HUAWEI-MACBIND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MACBIND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:52 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwMACBIND = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMacBindMibObjects_ObjectIdentity = ObjectIdentity
hwMacBindMibObjects = _HwMacBindMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1)
)


class _HwMacBindEnableFlag_Type(TruthValue):
    """Custom type hwMacBindEnableFlag based on TruthValue"""


_HwMacBindEnableFlag_Object = MibScalar
hwMacBindEnableFlag = _HwMacBindEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 1),
    _HwMacBindEnableFlag_Type()
)
hwMacBindEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacBindEnableFlag.setStatus("current")
_HwMacBindTable_Object = MibTable
hwMacBindTable = _HwMacBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hwMacBindTable.setStatus("current")
_HwMacBindEntry_Object = MibTableRow
hwMacBindEntry = _HwMacBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 2, 1)
)
hwMacBindEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-MACBIND-MIB", "hwMacBindIPAddress"),
)
if mibBuilder.loadTexts:
    hwMacBindEntry.setStatus("current")
_HwMacBindIPAddress_Type = IpAddress
_HwMacBindIPAddress_Object = MibTableColumn
hwMacBindIPAddress = _HwMacBindIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 2, 1, 1),
    _HwMacBindIPAddress_Type()
)
hwMacBindIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBindIPAddress.setStatus("current")
_HwMacBindMacAddress_Type = MacAddress
_HwMacBindMacAddress_Object = MibTableColumn
hwMacBindMacAddress = _HwMacBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 2, 1, 2),
    _HwMacBindMacAddress_Type()
)
hwMacBindMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacBindMacAddress.setStatus("current")
_HwMacBindRowStatus_Type = RowStatus
_HwMacBindRowStatus_Object = MibTableColumn
hwMacBindRowStatus = _HwMacBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 1, 2, 1, 3),
    _HwMacBindRowStatus_Type()
)
hwMacBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacBindRowStatus.setStatus("current")
_HwMacBindMibConformance_ObjectIdentity = ObjectIdentity
hwMacBindMibConformance = _HwMacBindMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 2)
)
_HwMacBindMibGroup_ObjectIdentity = ObjectIdentity
hwMacBindMibGroup = _HwMacBindMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 2, 1)
)

# Managed Objects groups

hwMacBindTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 2, 1, 1)
)
hwMacBindTableGroup.setObjects(
      *(("HUAWEI-MACBIND-MIB", "hwMacBindIPAddress"),
        ("HUAWEI-MACBIND-MIB", "hwMacBindMacAddress"),
        ("HUAWEI-MACBIND-MIB", "hwMacBindRowStatus"))
)
if mibBuilder.loadTexts:
    hwMacBindTableGroup.setStatus("current")

hwMacBindEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 9, 2, 1, 2)
)
hwMacBindEnableGroup.setObjects(
    ("HUAWEI-MACBIND-MIB", "hwMacBindEnableFlag")
)
if mibBuilder.loadTexts:
    hwMacBindEnableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MACBIND-MIB",
    **{"hwMACBIND": hwMACBIND,
       "hwMacBindMibObjects": hwMacBindMibObjects,
       "hwMacBindEnableFlag": hwMacBindEnableFlag,
       "hwMacBindTable": hwMacBindTable,
       "hwMacBindEntry": hwMacBindEntry,
       "hwMacBindIPAddress": hwMacBindIPAddress,
       "hwMacBindMacAddress": hwMacBindMacAddress,
       "hwMacBindRowStatus": hwMacBindRowStatus,
       "hwMacBindMibConformance": hwMacBindMibConformance,
       "hwMacBindMibGroup": hwMacBindMibGroup,
       "hwMacBindTableGroup": hwMacBindTableGroup,
       "hwMacBindEnableGroup": hwMacBindEnableGroup}
)
