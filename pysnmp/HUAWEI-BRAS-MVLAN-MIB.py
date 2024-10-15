# SNMP MIB module (HUAWEI-BRAS-MVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-MVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:03 2024
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

(VlanId,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIndex")

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

hwMVLAN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwhwMVLANMibObjects_ObjectIdentity = ObjectIdentity
hwhwMVLANMibObjects = _HwhwMVLANMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1)
)
_HwMulticastVlanTable_Object = MibTable
hwMulticastVlanTable = _HwMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1)
)
if mibBuilder.loadTexts:
    hwMulticastVlanTable.setStatus("current")
_HwMulticastVlanEntry_Object = MibTableRow
hwMulticastVlanEntry = _HwMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1)
)
hwMulticastVlanEntry.setIndexNames(
    (0, "HUAWEI-BRAS-MVLAN-MIB", "hwMulticastVlanIfIndex"),
)
if mibBuilder.loadTexts:
    hwMulticastVlanEntry.setStatus("current")
_HwMulticastVlanIfIndex_Type = VlanIndex
_HwMulticastVlanIfIndex_Object = MibTableColumn
hwMulticastVlanIfIndex = _HwMulticastVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 1),
    _HwMulticastVlanIfIndex_Type()
)
hwMulticastVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMulticastVlanIfIndex.setStatus("current")
_HwMulticastInnerVlan_Type = VlanId
_HwMulticastInnerVlan_Object = MibTableColumn
hwMulticastInnerVlan = _HwMulticastInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 2),
    _HwMulticastInnerVlan_Type()
)
hwMulticastInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastInnerVlan.setStatus("current")
_HwMulticastOuterVlan_Type = VlanId
_HwMulticastOuterVlan_Object = MibTableColumn
hwMulticastOuterVlan = _HwMulticastOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 3),
    _HwMulticastOuterVlan_Type()
)
hwMulticastOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastOuterVlan.setStatus("current")


class _HwMulticastOpType_Type(Integer32):
    """Custom type hwMulticastOpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("set", 0),
          ("undo", 1))
    )


_HwMulticastOpType_Type.__name__ = "Integer32"
_HwMulticastOpType_Object = MibTableColumn
hwMulticastOpType = _HwMulticastOpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 1, 1, 1, 4),
    _HwMulticastOpType_Type()
)
hwMulticastOpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastOpType.setStatus("current")
_HwMVlanMIBConformance_ObjectIdentity = ObjectIdentity
hwMVlanMIBConformance = _HwMVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2)
)
_HwMVlanMIBCompliances_ObjectIdentity = ObjectIdentity
hwMVlanMIBCompliances = _HwMVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 1)
)
_HwMVlanMIBGroups_ObjectIdentity = ObjectIdentity
hwMVlanMIBGroups = _HwMVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 2)
)

# Managed Objects groups

hwMVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 2, 1)
)
hwMVlanGroup.setObjects(
      *(("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastVlanIfIndex"),
        ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastInnerVlan"),
        ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastOuterVlan"),
        ("HUAWEI-BRAS-MVLAN-MIB", "hwMulticastOpType"))
)
if mibBuilder.loadTexts:
    hwMVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwMVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-MVLAN-MIB",
    **{"hwMVLAN": hwMVLAN,
       "hwhwMVLANMibObjects": hwhwMVLANMibObjects,
       "hwMulticastVlanTable": hwMulticastVlanTable,
       "hwMulticastVlanEntry": hwMulticastVlanEntry,
       "hwMulticastVlanIfIndex": hwMulticastVlanIfIndex,
       "hwMulticastInnerVlan": hwMulticastInnerVlan,
       "hwMulticastOuterVlan": hwMulticastOuterVlan,
       "hwMulticastOpType": hwMulticastOpType,
       "hwMVlanMIBConformance": hwMVlanMIBConformance,
       "hwMVlanMIBCompliances": hwMVlanMIBCompliances,
       "hwMVlanMIBCompliance": hwMVlanMIBCompliance,
       "hwMVlanMIBGroups": hwMVlanMIBGroups,
       "hwMVlanGroup": hwMVlanGroup}
)
