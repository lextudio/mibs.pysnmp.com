# SNMP MIB module (HUAWEI-L3VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L3VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:28 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwL3Vlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL3VlanMIBObjects_ObjectIdentity = ObjectIdentity
hwL3VlanMIBObjects = _HwL3VlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1)
)
_HwSubIfVlanTable_Object = MibTable
hwSubIfVlanTable = _HwSubIfVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwSubIfVlanTable.setStatus("current")
_HwSubIfVlanEntry_Object = MibTableRow
hwSubIfVlanEntry = _HwSubIfVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1, 1)
)
hwSubIfVlanEntry.setIndexNames(
    (0, "HUAWEI-L3VLAN-MIB", "hwSubIfIndex"),
    (0, "HUAWEI-L3VLAN-MIB", "hwSubIfVlanId"),
)
if mibBuilder.loadTexts:
    hwSubIfVlanEntry.setStatus("current")
_HwSubIfIndex_Type = InterfaceIndex
_HwSubIfIndex_Object = MibTableColumn
hwSubIfIndex = _HwSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1, 1, 1),
    _HwSubIfIndex_Type()
)
hwSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSubIfIndex.setStatus("current")


class _HwSubIfVlanId_Type(Integer32):
    """Custom type hwSubIfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwSubIfVlanId_Type.__name__ = "Integer32"
_HwSubIfVlanId_Object = MibTableColumn
hwSubIfVlanId = _HwSubIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1, 1, 2),
    _HwSubIfVlanId_Type()
)
hwSubIfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSubIfVlanId.setStatus("current")


class _HwSubIfVlanType_Type(Integer32):
    """Custom type hwSubIfVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("dot1q", 2)
    )


_HwSubIfVlanType_Type.__name__ = "Integer32"
_HwSubIfVlanType_Object = MibTableColumn
hwSubIfVlanType = _HwSubIfVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1, 1, 3),
    _HwSubIfVlanType_Type()
)
hwSubIfVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanType.setStatus("current")
_HwSubIfVlanStatus_Type = RowStatus
_HwSubIfVlanStatus_Object = MibTableColumn
hwSubIfVlanStatus = _HwSubIfVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 1, 1, 4),
    _HwSubIfVlanStatus_Type()
)
hwSubIfVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanStatus.setStatus("current")
_HwVLANMibRoutertVlanCountTable_Object = MibTable
hwVLANMibRoutertVlanCountTable = _HwVLANMibRoutertVlanCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2)
)
if mibBuilder.loadTexts:
    hwVLANMibRoutertVlanCountTable.setStatus("current")
_HwVLANMibRoutertVlanCountEntry_Object = MibTableRow
hwVLANMibRoutertVlanCountEntry = _HwVLANMibRoutertVlanCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1)
)
hwVLANMibRoutertVlanCountEntry.setIndexNames(
    (0, "HUAWEI-L3VLAN-MIB", "hwVLANMibRouterPort"),
    (0, "HUAWEI-L3VLAN-MIB", "hwVLANMibRouterVID"),
)
if mibBuilder.loadTexts:
    hwVLANMibRoutertVlanCountEntry.setStatus("current")
_HwVLANMibRouterPort_Type = InterfaceIndex
_HwVLANMibRouterPort_Object = MibTableColumn
hwVLANMibRouterPort = _HwVLANMibRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1, 1),
    _HwVLANMibRouterPort_Type()
)
hwVLANMibRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibRouterPort.setStatus("current")


class _HwVLANMibRouterVID_Type(Integer32):
    """Custom type hwVLANMibRouterVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwVLANMibRouterVID_Type.__name__ = "Integer32"
_HwVLANMibRouterVID_Object = MibTableColumn
hwVLANMibRouterVID = _HwVLANMibRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1, 2),
    _HwVLANMibRouterVID_Type()
)
hwVLANMibRouterVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibRouterVID.setStatus("current")
_HwVLANMibRouterVlanPacketTran_Type = Counter32
_HwVLANMibRouterVlanPacketTran_Object = MibTableColumn
hwVLANMibRouterVlanPacketTran = _HwVLANMibRouterVlanPacketTran_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1, 3),
    _HwVLANMibRouterVlanPacketTran_Type()
)
hwVLANMibRouterVlanPacketTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibRouterVlanPacketTran.setStatus("current")
_HwVLANMibRouterVlanPacketSent_Type = Counter32
_HwVLANMibRouterVlanPacketSent_Object = MibTableColumn
hwVLANMibRouterVlanPacketSent = _HwVLANMibRouterVlanPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1, 4),
    _HwVLANMibRouterVlanPacketSent_Type()
)
hwVLANMibRouterVlanPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibRouterVlanPacketSent.setStatus("current")


class _HwVLANMibClearVidStatistics_Type(Integer32):
    """Custom type hwVLANMibClearVidStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unavailable", 0))
    )


_HwVLANMibClearVidStatistics_Type.__name__ = "Integer32"
_HwVLANMibClearVidStatistics_Object = MibTableColumn
hwVLANMibClearVidStatistics = _HwVLANMibClearVidStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 2, 1, 5),
    _HwVLANMibClearVidStatistics_Type()
)
hwVLANMibClearVidStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVLANMibClearVidStatistics.setStatus("current")
_HwSubIfVlanPolicyTable_Object = MibTable
hwSubIfVlanPolicyTable = _HwSubIfVlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3)
)
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyTable.setStatus("current")
_HwSubIfVlanPolicyEntry_Object = MibTableRow
hwSubIfVlanPolicyEntry = _HwSubIfVlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1)
)
hwSubIfVlanPolicyEntry.setIndexNames(
    (0, "HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyIfIndex"),
    (0, "HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyVlanId"),
)
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyEntry.setStatus("current")
_HwSubIfVlanPolicyIfIndex_Type = InterfaceIndex
_HwSubIfVlanPolicyIfIndex_Object = MibTableColumn
hwSubIfVlanPolicyIfIndex = _HwSubIfVlanPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 1),
    _HwSubIfVlanPolicyIfIndex_Type()
)
hwSubIfVlanPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyIfIndex.setStatus("current")


class _HwSubIfVlanPolicyVlanId_Type(Integer32):
    """Custom type hwSubIfVlanPolicyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwSubIfVlanPolicyVlanId_Type.__name__ = "Integer32"
_HwSubIfVlanPolicyVlanId_Object = MibTableColumn
hwSubIfVlanPolicyVlanId = _HwSubIfVlanPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 2),
    _HwSubIfVlanPolicyVlanId_Type()
)
hwSubIfVlanPolicyVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyVlanId.setStatus("current")


class _HwSubIfVlanPolicyIfType_Type(Integer32):
    """Custom type hwSubIfVlanPolicyIfType based on Integer32"""
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
        *(("dot1q", 1),
          ("dot1qTerm", 2),
          ("stacking", 3),
          ("untagged", 4))
    )


_HwSubIfVlanPolicyIfType_Type.__name__ = "Integer32"
_HwSubIfVlanPolicyIfType_Object = MibTableColumn
hwSubIfVlanPolicyIfType = _HwSubIfVlanPolicyIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 3),
    _HwSubIfVlanPolicyIfType_Type()
)
hwSubIfVlanPolicyIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyIfType.setStatus("current")


class _HwSubIfVlanPolicyVlanIdEnd_Type(Integer32):
    """Custom type hwSubIfVlanPolicyVlanIdEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwSubIfVlanPolicyVlanIdEnd_Type.__name__ = "Integer32"
_HwSubIfVlanPolicyVlanIdEnd_Object = MibTableColumn
hwSubIfVlanPolicyVlanIdEnd = _HwSubIfVlanPolicyVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 4),
    _HwSubIfVlanPolicyVlanIdEnd_Type()
)
hwSubIfVlanPolicyVlanIdEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyVlanIdEnd.setStatus("current")


class _HwSubIfVlanPolicyType_Type(Integer32):
    """Custom type hwSubIfVlanPolicyType based on Integer32"""
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
        *(("default", 4),
          ("type8021P", 1),
          ("typeDSCP", 2),
          ("typeEtherType", 3))
    )


_HwSubIfVlanPolicyType_Type.__name__ = "Integer32"
_HwSubIfVlanPolicyType_Object = MibTableColumn
hwSubIfVlanPolicyType = _HwSubIfVlanPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 5),
    _HwSubIfVlanPolicyType_Type()
)
hwSubIfVlanPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyType.setStatus("current")


class _HwSubIfVlanPolicyValue_Type(OctetString):
    """Custom type hwSubIfVlanPolicyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HwSubIfVlanPolicyValue_Type.__name__ = "OctetString"
_HwSubIfVlanPolicyValue_Object = MibTableColumn
hwSubIfVlanPolicyValue = _HwSubIfVlanPolicyValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 6),
    _HwSubIfVlanPolicyValue_Type()
)
hwSubIfVlanPolicyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyValue.setStatus("current")


class _HwSubIfVlanPolicyGroupId_Type(Integer32):
    """Custom type hwSubIfVlanPolicyGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwSubIfVlanPolicyGroupId_Type.__name__ = "Integer32"
_HwSubIfVlanPolicyGroupId_Object = MibTableColumn
hwSubIfVlanPolicyGroupId = _HwSubIfVlanPolicyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 7),
    _HwSubIfVlanPolicyGroupId_Type()
)
hwSubIfVlanPolicyGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyGroupId.setStatus("current")
_HwSubIfVlanPolicyRowStatus_Type = RowStatus
_HwSubIfVlanPolicyRowStatus_Object = MibTableColumn
hwSubIfVlanPolicyRowStatus = _HwSubIfVlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 1, 3, 1, 51),
    _HwSubIfVlanPolicyRowStatus_Type()
)
hwSubIfVlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSubIfVlanPolicyRowStatus.setStatus("current")
_HwL3VlanTraps_ObjectIdentity = ObjectIdentity
hwL3VlanTraps = _HwL3VlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 2)
)
_HwL3VlanConformance_ObjectIdentity = ObjectIdentity
hwL3VlanConformance = _HwL3VlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 3)
)
_HwL3VlanCompliances_ObjectIdentity = ObjectIdentity
hwL3VlanCompliances = _HwL3VlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 3, 1)
)
_HwL3VlanGroups_ObjectIdentity = ObjectIdentity
hwL3VlanGroups = _HwL3VlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 3, 2)
)

# Managed Objects groups

hwSubIfVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 3, 2, 1)
)
hwSubIfVlanGroup.setObjects(
      *(("HUAWEI-L3VLAN-MIB", "hwSubIfVlanType"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanId"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanStatus"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyIfType"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyVlanIdEnd"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyType"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyValue"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyGroupId"),
        ("HUAWEI-L3VLAN-MIB", "hwSubIfVlanPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwSubIfVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwL3VlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 100, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwL3VlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L3VLAN-MIB",
    **{"hwL3Vlan": hwL3Vlan,
       "hwL3VlanMIBObjects": hwL3VlanMIBObjects,
       "hwSubIfVlanTable": hwSubIfVlanTable,
       "hwSubIfVlanEntry": hwSubIfVlanEntry,
       "hwSubIfIndex": hwSubIfIndex,
       "hwSubIfVlanId": hwSubIfVlanId,
       "hwSubIfVlanType": hwSubIfVlanType,
       "hwSubIfVlanStatus": hwSubIfVlanStatus,
       "hwVLANMibRoutertVlanCountTable": hwVLANMibRoutertVlanCountTable,
       "hwVLANMibRoutertVlanCountEntry": hwVLANMibRoutertVlanCountEntry,
       "hwVLANMibRouterPort": hwVLANMibRouterPort,
       "hwVLANMibRouterVID": hwVLANMibRouterVID,
       "hwVLANMibRouterVlanPacketTran": hwVLANMibRouterVlanPacketTran,
       "hwVLANMibRouterVlanPacketSent": hwVLANMibRouterVlanPacketSent,
       "hwVLANMibClearVidStatistics": hwVLANMibClearVidStatistics,
       "hwSubIfVlanPolicyTable": hwSubIfVlanPolicyTable,
       "hwSubIfVlanPolicyEntry": hwSubIfVlanPolicyEntry,
       "hwSubIfVlanPolicyIfIndex": hwSubIfVlanPolicyIfIndex,
       "hwSubIfVlanPolicyVlanId": hwSubIfVlanPolicyVlanId,
       "hwSubIfVlanPolicyIfType": hwSubIfVlanPolicyIfType,
       "hwSubIfVlanPolicyVlanIdEnd": hwSubIfVlanPolicyVlanIdEnd,
       "hwSubIfVlanPolicyType": hwSubIfVlanPolicyType,
       "hwSubIfVlanPolicyValue": hwSubIfVlanPolicyValue,
       "hwSubIfVlanPolicyGroupId": hwSubIfVlanPolicyGroupId,
       "hwSubIfVlanPolicyRowStatus": hwSubIfVlanPolicyRowStatus,
       "hwL3VlanTraps": hwL3VlanTraps,
       "hwL3VlanConformance": hwL3VlanConformance,
       "hwL3VlanCompliances": hwL3VlanCompliances,
       "hwL3VlanCompliance": hwL3VlanCompliance,
       "hwL3VlanGroups": hwL3VlanGroups,
       "hwSubIfVlanGroup": hwSubIfVlanGroup}
)
