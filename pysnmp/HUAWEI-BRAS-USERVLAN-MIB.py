# SNMP MIB module (HUAWEI-BRAS-USERVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-USERVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:13 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

hwUSERVLAN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwhwUSERVLANMibObjects_ObjectIdentity = ObjectIdentity
hwhwUSERVLANMibObjects = _HwhwUSERVLANMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1)
)
_HwUserVlanTable_ObjectIdentity = ObjectIdentity
hwUserVlanTable = _HwUserVlanTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1)
)
_HwUserVlanIfIndex_Type = InterfaceIndex
_HwUserVlanIfIndex_Object = MibScalar
hwUserVlanIfIndex = _HwUserVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 1),
    _HwUserVlanIfIndex_Type()
)
hwUserVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserVlanIfIndex.setStatus("current")
_HwUserInnerStartVlan_Type = VlanId
_HwUserInnerStartVlan_Object = MibScalar
hwUserInnerStartVlan = _HwUserInnerStartVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 2),
    _HwUserInnerStartVlan_Type()
)
hwUserInnerStartVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserInnerStartVlan.setStatus("current")
_HwUserInnerEndVlan_Type = VlanId
_HwUserInnerEndVlan_Object = MibScalar
hwUserInnerEndVlan = _HwUserInnerEndVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 3),
    _HwUserInnerEndVlan_Type()
)
hwUserInnerEndVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserInnerEndVlan.setStatus("current")
_HwUserVlanOuterVlan_Type = VlanId
_HwUserVlanOuterVlan_Object = MibScalar
hwUserVlanOuterVlan = _HwUserVlanOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 4),
    _HwUserVlanOuterVlan_Type()
)
hwUserVlanOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserVlanOuterVlan.setStatus("current")


class _HwUserVlanOpType_Type(Integer32):
    """Custom type hwUserVlanOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("undo", 2))
    )


_HwUserVlanOpType_Type.__name__ = "Integer32"
_HwUserVlanOpType_Object = MibScalar
hwUserVlanOpType = _HwUserVlanOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 1, 5),
    _HwUserVlanOpType_Type()
)
hwUserVlanOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserVlanOpType.setStatus("current")
_HwQueryUserVlanTable_Object = MibTable
hwQueryUserVlanTable = _HwQueryUserVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2)
)
if mibBuilder.loadTexts:
    hwQueryUserVlanTable.setStatus("current")
_HwQueryUserVlanEntry_Object = MibTableRow
hwQueryUserVlanEntry = _HwQueryUserVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1)
)
hwQueryUserVlanEntry.setIndexNames(
    (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"),
    (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"),
    (0, "HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"),
)
if mibBuilder.loadTexts:
    hwQueryUserVlanEntry.setStatus("current")
_HwQueryUserVlanIfIndex_Type = Integer32
_HwQueryUserVlanIfIndex_Object = MibTableColumn
hwQueryUserVlanIfIndex = _HwQueryUserVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 1),
    _HwQueryUserVlanIfIndex_Type()
)
hwQueryUserVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryUserVlanIfIndex.setStatus("current")
_HwQueryUserInnerVlan_Type = VlanIdOrNone
_HwQueryUserInnerVlan_Object = MibTableColumn
hwQueryUserInnerVlan = _HwQueryUserInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 2),
    _HwQueryUserInnerVlan_Type()
)
hwQueryUserInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryUserInnerVlan.setStatus("current")
_HwQueryUserOuterVlan_Type = VlanIdOrNone
_HwQueryUserOuterVlan_Object = MibTableColumn
hwQueryUserOuterVlan = _HwQueryUserOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 1, 2, 1, 3),
    _HwQueryUserOuterVlan_Type()
)
hwQueryUserOuterVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueryUserOuterVlan.setStatus("current")
_HwUserVlanConformance_ObjectIdentity = ObjectIdentity
hwUserVlanConformance = _HwUserVlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2)
)
_HwUserVlanCompliances_ObjectIdentity = ObjectIdentity
hwUserVlanCompliances = _HwUserVlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1)
)
_HwUserVlanObjectGroups_ObjectIdentity = ObjectIdentity
hwUserVlanObjectGroups = _HwUserVlanObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2)
)

# Managed Objects groups

hwUserVlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 1)
)
hwUserVlanTableGroup.setObjects(
      *(("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanIfIndex"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerStartVlan"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserInnerEndVlan"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOuterVlan"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwUserVlanOpType"))
)
if mibBuilder.loadTexts:
    hwUserVlanTableGroup.setStatus("current")

hwQueryUserVlanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 2, 2)
)
hwQueryUserVlanTableGroup.setObjects(
      *(("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserVlanIfIndex"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserInnerVlan"),
        ("HUAWEI-BRAS-USERVLAN-MIB", "hwQueryUserOuterVlan"))
)
if mibBuilder.loadTexts:
    hwQueryUserVlanTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwUserVlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwUserVlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-USERVLAN-MIB",
    **{"hwUSERVLAN": hwUSERVLAN,
       "hwhwUSERVLANMibObjects": hwhwUSERVLANMibObjects,
       "hwUserVlanTable": hwUserVlanTable,
       "hwUserVlanIfIndex": hwUserVlanIfIndex,
       "hwUserInnerStartVlan": hwUserInnerStartVlan,
       "hwUserInnerEndVlan": hwUserInnerEndVlan,
       "hwUserVlanOuterVlan": hwUserVlanOuterVlan,
       "hwUserVlanOpType": hwUserVlanOpType,
       "hwQueryUserVlanTable": hwQueryUserVlanTable,
       "hwQueryUserVlanEntry": hwQueryUserVlanEntry,
       "hwQueryUserVlanIfIndex": hwQueryUserVlanIfIndex,
       "hwQueryUserInnerVlan": hwQueryUserInnerVlan,
       "hwQueryUserOuterVlan": hwQueryUserOuterVlan,
       "hwUserVlanConformance": hwUserVlanConformance,
       "hwUserVlanCompliances": hwUserVlanCompliances,
       "hwUserVlanCompliance": hwUserVlanCompliance,
       "hwUserVlanObjectGroups": hwUserVlanObjectGroups,
       "hwUserVlanTableGroup": hwUserVlanTableGroup,
       "hwQueryUserVlanTableGroup": hwQueryUserVlanTableGroup}
)
