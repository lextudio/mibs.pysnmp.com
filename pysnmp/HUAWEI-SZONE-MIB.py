# SNMP MIB module (HUAWEI-SZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SZONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:08 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSZONE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSZoneZoneCfg_ObjectIdentity = ObjectIdentity
hwSZoneZoneCfg = _HwSZoneZoneCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1)
)
_HwSZoneZoneTable_Object = MibTable
hwSZoneZoneTable = _HwSZoneZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hwSZoneZoneTable.setStatus("current")
_HwSZoneZoneEntry_Object = MibTableRow
hwSZoneZoneEntry = _HwSZoneZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1)
)
hwSZoneZoneEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-SZONE-MIB", "hwSZoneZoneID"),
)
if mibBuilder.loadTexts:
    hwSZoneZoneEntry.setStatus("current")


class _HwSZoneZoneID_Type(Integer32):
    """Custom type hwSZoneZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSZoneZoneID_Type.__name__ = "Integer32"
_HwSZoneZoneID_Object = MibTableColumn
hwSZoneZoneID = _HwSZoneZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 1),
    _HwSZoneZoneID_Type()
)
hwSZoneZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSZoneZoneID.setStatus("current")


class _HwSZoneZoneName_Type(OctetString):
    """Custom type hwSZoneZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwSZoneZoneName_Type.__name__ = "OctetString"
_HwSZoneZoneName_Object = MibTableColumn
hwSZoneZoneName = _HwSZoneZoneName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 2),
    _HwSZoneZoneName_Type()
)
hwSZoneZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneZoneName.setStatus("current")


class _HwSZoneSecPriority_Type(Integer32):
    """Custom type hwSZoneSecPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_HwSZoneSecPriority_Type.__name__ = "Integer32"
_HwSZoneSecPriority_Object = MibTableColumn
hwSZoneSecPriority = _HwSZoneSecPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 3),
    _HwSZoneSecPriority_Type()
)
hwSZoneSecPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneSecPriority.setStatus("current")
_HwSZoneZoneStatus_Type = RowStatus
_HwSZoneZoneStatus_Object = MibTableColumn
hwSZoneZoneStatus = _HwSZoneZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 1, 1, 4),
    _HwSZoneZoneStatus_Type()
)
hwSZoneZoneStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneZoneStatus.setStatus("current")
_HwSZoneZoneIFTable_Object = MibTable
hwSZoneZoneIFTable = _HwSZoneZoneIFTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hwSZoneZoneIFTable.setStatus("current")
_HwSZoneZoneIFEntry_Object = MibTableRow
hwSZoneZoneIFEntry = _HwSZoneZoneIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1)
)
hwSZoneZoneIFEntry.setIndexNames(
    (0, "HUAWEI-SZONE-MIB", "hwSZoneIFZoneID"),
    (0, "HUAWEI-SZONE-MIB", "hwSZoneZoneIFIndex"),
)
if mibBuilder.loadTexts:
    hwSZoneZoneIFEntry.setStatus("current")


class _HwSZoneIFZoneID_Type(Integer32):
    """Custom type hwSZoneIFZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSZoneIFZoneID_Type.__name__ = "Integer32"
_HwSZoneIFZoneID_Object = MibTableColumn
hwSZoneIFZoneID = _HwSZoneIFZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 1),
    _HwSZoneIFZoneID_Type()
)
hwSZoneIFZoneID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSZoneIFZoneID.setStatus("current")
_HwSZoneZoneIFIndex_Type = Gauge32
_HwSZoneZoneIFIndex_Object = MibTableColumn
hwSZoneZoneIFIndex = _HwSZoneZoneIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 2),
    _HwSZoneZoneIFIndex_Type()
)
hwSZoneZoneIFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSZoneZoneIFIndex.setStatus("current")
_HwSZoneZoneIFStatus_Type = RowStatus
_HwSZoneZoneIFStatus_Object = MibTableColumn
hwSZoneZoneIFStatus = _HwSZoneZoneIFStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 1, 2, 1, 3),
    _HwSZoneZoneIFStatus_Type()
)
hwSZoneZoneIFStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneZoneIFStatus.setStatus("current")
_HwSZoneInterZoneCfg_ObjectIdentity = ObjectIdentity
hwSZoneInterZoneCfg = _HwSZoneInterZoneCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2)
)
_HwSZoneInterZoneTable_Object = MibTable
hwSZoneInterZoneTable = _HwSZoneInterZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1)
)
if mibBuilder.loadTexts:
    hwSZoneInterZoneTable.setStatus("current")
_HwSZoneInterZoneEntry_Object = MibTableRow
hwSZoneInterZoneEntry = _HwSZoneInterZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1)
)
hwSZoneInterZoneEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID1"),
    (0, "HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID2"),
)
if mibBuilder.loadTexts:
    hwSZoneInterZoneEntry.setStatus("current")


class _HwSZoneInterZoneZoneID1_Type(Integer32):
    """Custom type hwSZoneInterZoneZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSZoneInterZoneZoneID1_Type.__name__ = "Integer32"
_HwSZoneInterZoneZoneID1_Object = MibTableColumn
hwSZoneInterZoneZoneID1 = _HwSZoneInterZoneZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 1),
    _HwSZoneInterZoneZoneID1_Type()
)
hwSZoneInterZoneZoneID1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSZoneInterZoneZoneID1.setStatus("current")


class _HwSZoneInterZoneZoneID2_Type(Integer32):
    """Custom type hwSZoneInterZoneZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwSZoneInterZoneZoneID2_Type.__name__ = "Integer32"
_HwSZoneInterZoneZoneID2_Object = MibTableColumn
hwSZoneInterZoneZoneID2 = _HwSZoneInterZoneZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 2),
    _HwSZoneInterZoneZoneID2_Type()
)
hwSZoneInterZoneZoneID2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSZoneInterZoneZoneID2.setStatus("current")


class _HwSZoneInterZoneEnableFW_Type(TruthValue):
    """Custom type hwSZoneInterZoneEnableFW based on TruthValue"""


_HwSZoneInterZoneEnableFW_Object = MibTableColumn
hwSZoneInterZoneEnableFW = _HwSZoneInterZoneEnableFW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 3),
    _HwSZoneInterZoneEnableFW_Type()
)
hwSZoneInterZoneEnableFW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneInterZoneEnableFW.setStatus("current")
_HwSZoneInterZoneStatus_Type = RowStatus
_HwSZoneInterZoneStatus_Object = MibTableColumn
hwSZoneInterZoneStatus = _HwSZoneInterZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 2, 1, 1, 4),
    _HwSZoneInterZoneStatus_Type()
)
hwSZoneInterZoneStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSZoneInterZoneStatus.setStatus("current")
_HwSZoneConformance_ObjectIdentity = ObjectIdentity
hwSZoneConformance = _HwSZoneConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3)
)
_HwSZoneCompliance_ObjectIdentity = ObjectIdentity
hwSZoneCompliance = _HwSZoneCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 1)
)
_HwSZoneMibGroups_ObjectIdentity = ObjectIdentity
hwSZoneMibGroups = _HwSZoneMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2)
)

# Managed Objects groups

hwSZoneZoneCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2, 1)
)
hwSZoneZoneCfgGroup.setObjects(
      *(("HUAWEI-SZONE-MIB", "hwSZoneZoneName"),
        ("HUAWEI-SZONE-MIB", "hwSZoneSecPriority"),
        ("HUAWEI-SZONE-MIB", "hwSZoneZoneStatus"),
        ("HUAWEI-SZONE-MIB", "hwSZoneZoneIFIndex"),
        ("HUAWEI-SZONE-MIB", "hwSZoneZoneIFStatus"),
        ("HUAWEI-SZONE-MIB", "hwSZoneZoneID"),
        ("HUAWEI-SZONE-MIB", "hwSZoneIFZoneID"))
)
if mibBuilder.loadTexts:
    hwSZoneZoneCfgGroup.setStatus("current")

hwSZoneInterZoneCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 15, 3, 2, 2)
)
hwSZoneInterZoneCfgGroup.setObjects(
      *(("HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID1"),
        ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneZoneID2"),
        ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneEnableFW"),
        ("HUAWEI-SZONE-MIB", "hwSZoneInterZoneStatus"))
)
if mibBuilder.loadTexts:
    hwSZoneInterZoneCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SZONE-MIB",
    **{"hwSZONE": hwSZONE,
       "hwSZoneZoneCfg": hwSZoneZoneCfg,
       "hwSZoneZoneTable": hwSZoneZoneTable,
       "hwSZoneZoneEntry": hwSZoneZoneEntry,
       "hwSZoneZoneID": hwSZoneZoneID,
       "hwSZoneZoneName": hwSZoneZoneName,
       "hwSZoneSecPriority": hwSZoneSecPriority,
       "hwSZoneZoneStatus": hwSZoneZoneStatus,
       "hwSZoneZoneIFTable": hwSZoneZoneIFTable,
       "hwSZoneZoneIFEntry": hwSZoneZoneIFEntry,
       "hwSZoneIFZoneID": hwSZoneIFZoneID,
       "hwSZoneZoneIFIndex": hwSZoneZoneIFIndex,
       "hwSZoneZoneIFStatus": hwSZoneZoneIFStatus,
       "hwSZoneInterZoneCfg": hwSZoneInterZoneCfg,
       "hwSZoneInterZoneTable": hwSZoneInterZoneTable,
       "hwSZoneInterZoneEntry": hwSZoneInterZoneEntry,
       "hwSZoneInterZoneZoneID1": hwSZoneInterZoneZoneID1,
       "hwSZoneInterZoneZoneID2": hwSZoneInterZoneZoneID2,
       "hwSZoneInterZoneEnableFW": hwSZoneInterZoneEnableFW,
       "hwSZoneInterZoneStatus": hwSZoneInterZoneStatus,
       "hwSZoneConformance": hwSZoneConformance,
       "hwSZoneCompliance": hwSZoneCompliance,
       "hwSZoneMibGroups": hwSZoneMibGroups,
       "hwSZoneZoneCfgGroup": hwSZoneZoneCfgGroup,
       "hwSZoneInterZoneCfgGroup": hwSZoneInterZoneCfgGroup}
)
