# SNMP MIB module (HUAWEI-L2VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:24 2024
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

(hwBaseTrapEventType,
 hwBaseTrapProbableCause,
 hwBaseTrapSeverity) = mibBuilder.importSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    "hwBaseTrapEventType",
    "hwBaseTrapProbableCause",
    "hwBaseTrapSeverity")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanId,
 VlanIdOrNone,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIdOrNone",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwL2Vlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Mgmt_ObjectIdentity = ObjectIdentity
hwL2Mgmt = _HwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42)
)
_HwL2VlanMngObjects_ObjectIdentity = ObjectIdentity
hwL2VlanMngObjects = _HwL2VlanMngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1)
)
_HwL2VlanBase_ObjectIdentity = ObjectIdentity
hwL2VlanBase = _HwL2VlanBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1)
)
_HwL2VlanMIBTable_Object = MibTable
hwL2VlanMIBTable = _HwL2VlanMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwL2VlanMIBTable.setStatus("current")
_HwL2VlanMIBEntry_Object = MibTableRow
hwL2VlanMIBEntry = _HwL2VlanMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1)
)
hwL2VlanMIBEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanMIBEntry.setStatus("current")
_HwL2VlanIndex_Type = VlanId
_HwL2VlanIndex_Object = MibTableColumn
hwL2VlanIndex = _HwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 1),
    _HwL2VlanIndex_Type()
)
hwL2VlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanIndex.setStatus("current")


class _HwL2VlanDescr_Type(OctetString):
    """Custom type hwL2VlanDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwL2VlanDescr_Type.__name__ = "OctetString"
_HwL2VlanDescr_Object = MibTableColumn
hwL2VlanDescr = _HwL2VlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 2),
    _HwL2VlanDescr_Type()
)
hwL2VlanDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanDescr.setStatus("current")
_HwL2VlanPortList_Type = PortList
_HwL2VlanPortList_Object = MibTableColumn
hwL2VlanPortList = _HwL2VlanPortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 3),
    _HwL2VlanPortList_Type()
)
hwL2VlanPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPortList.setStatus("current")


class _HwL2VlanType_Type(Integer32):
    """Custom type hwL2VlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("commonVlan", 2),
          ("muxSubVlan", 5),
          ("muxVlan", 4),
          ("protocolTransVlan", 6),
          ("subVlan", 3),
          ("superVlan", 1))
    )


_HwL2VlanType_Type.__name__ = "Integer32"
_HwL2VlanType_Object = MibTableColumn
hwL2VlanType = _HwL2VlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 4),
    _HwL2VlanType_Type()
)
hwL2VlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanType.setStatus("current")


class _HwL2VlanUnknownUnicastProcessing_Type(Integer32):
    """Custom type hwL2VlanUnknownUnicastProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("discard", 2))
    )


_HwL2VlanUnknownUnicastProcessing_Type.__name__ = "Integer32"
_HwL2VlanUnknownUnicastProcessing_Object = MibTableColumn
hwL2VlanUnknownUnicastProcessing = _HwL2VlanUnknownUnicastProcessing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 5),
    _HwL2VlanUnknownUnicastProcessing_Type()
)
hwL2VlanUnknownUnicastProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanUnknownUnicastProcessing.setStatus("current")
_HwL2VlanIfIndex_Type = Integer32
_HwL2VlanIfIndex_Object = MibTableColumn
hwL2VlanIfIndex = _HwL2VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 6),
    _HwL2VlanIfIndex_Type()
)
hwL2VlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanIfIndex.setStatus("current")
_HwL2VlanMacLearn_Type = EnabledStatus
_HwL2VlanMacLearn_Object = MibTableColumn
hwL2VlanMacLearn = _HwL2VlanMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 7),
    _HwL2VlanMacLearn_Type()
)
hwL2VlanMacLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacLearn.setStatus("current")
_HwL2VlanMulticast_Type = EnabledStatus
_HwL2VlanMulticast_Object = MibTableColumn
hwL2VlanMulticast = _HwL2VlanMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 8),
    _HwL2VlanMulticast_Type()
)
hwL2VlanMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanMulticast.setStatus("current")


class _HwL2VlanAdminStatus_Type(EnabledStatus):
    """Custom type hwL2VlanAdminStatus based on EnabledStatus"""
    defaultValue = 1


_HwL2VlanAdminStatus_Object = MibTableColumn
hwL2VlanAdminStatus = _HwL2VlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 9),
    _HwL2VlanAdminStatus_Type()
)
hwL2VlanAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanAdminStatus.setStatus("current")


class _HwL2VlanStatisStatus_Type(EnabledStatus):
    """Custom type hwL2VlanStatisStatus based on EnabledStatus"""
    defaultValue = 2


_HwL2VlanStatisStatus_Object = MibTableColumn
hwL2VlanStatisStatus = _HwL2VlanStatisStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 10),
    _HwL2VlanStatisStatus_Type()
)
hwL2VlanStatisStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStatisStatus.setStatus("current")


class _HwL2VlanCreateStatus_Type(Integer32):
    """Custom type hwL2VlanCreateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("other", 1),
          ("static", 2))
    )


_HwL2VlanCreateStatus_Type.__name__ = "Integer32"
_HwL2VlanCreateStatus_Object = MibTableColumn
hwL2VlanCreateStatus = _HwL2VlanCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 11),
    _HwL2VlanCreateStatus_Type()
)
hwL2VlanCreateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanCreateStatus.setStatus("current")
_HwL2VlanRowStatus_Type = RowStatus
_HwL2VlanRowStatus_Object = MibTableColumn
hwL2VlanRowStatus = _HwL2VlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 12),
    _HwL2VlanRowStatus_Type()
)
hwL2VlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanRowStatus.setStatus("current")
_HwL2VlanBcast_Type = EnabledStatus
_HwL2VlanBcast_Object = MibTableColumn
hwL2VlanBcast = _HwL2VlanBcast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 13),
    _HwL2VlanBcast_Type()
)
hwL2VlanBcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanBcast.setStatus("current")


class _HwL2VlanUnknownMulticastProcessing_Type(Integer32):
    """Custom type hwL2VlanUnknownMulticastProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("discard", 2))
    )


_HwL2VlanUnknownMulticastProcessing_Type.__name__ = "Integer32"
_HwL2VlanUnknownMulticastProcessing_Object = MibTableColumn
hwL2VlanUnknownMulticastProcessing = _HwL2VlanUnknownMulticastProcessing_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 14),
    _HwL2VlanUnknownMulticastProcessing_Type()
)
hwL2VlanUnknownMulticastProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanUnknownMulticastProcessing.setStatus("current")


class _HwL2VlanProperty_Type(Integer32):
    """Custom type hwL2VlanProperty based on Integer32"""
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
        *(("backboneVlan", 2),
          ("default", 1),
          ("mutilcastVlan", 3),
          ("userVlan", 4))
    )


_HwL2VlanProperty_Type.__name__ = "Integer32"
_HwL2VlanProperty_Object = MibTableColumn
hwL2VlanProperty = _HwL2VlanProperty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 15),
    _HwL2VlanProperty_Type()
)
hwL2VlanProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanProperty.setStatus("current")


class _HwL2VlanAgingTime_Type(Integer32):
    """Custom type hwL2VlanAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000000),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(-1, -1),
    )


_HwL2VlanAgingTime_Type.__name__ = "Integer32"
_HwL2VlanAgingTime_Object = MibTableColumn
hwL2VlanAgingTime = _HwL2VlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 16),
    _HwL2VlanAgingTime_Type()
)
hwL2VlanAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanAgingTime.setStatus("current")


class _HwL2VlanName_Type(OctetString):
    """Custom type hwL2VlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2VlanName_Type.__name__ = "OctetString"
_HwL2VlanName_Object = MibTableColumn
hwL2VlanName = _HwL2VlanName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 17),
    _HwL2VlanName_Type()
)
hwL2VlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanName.setStatus("current")
_HwL2VlanSmartMacLearn_Type = EnabledStatus
_HwL2VlanSmartMacLearn_Object = MibTableColumn
hwL2VlanSmartMacLearn = _HwL2VlanSmartMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 18),
    _HwL2VlanSmartMacLearn_Type()
)
hwL2VlanSmartMacLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSmartMacLearn.setStatus("current")


class _HwL2VlanServiceName_Type(OctetString):
    """Custom type hwL2VlanServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HwL2VlanServiceName_Type.__name__ = "OctetString"
_HwL2VlanServiceName_Object = MibTableColumn
hwL2VlanServiceName = _HwL2VlanServiceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 19),
    _HwL2VlanServiceName_Type()
)
hwL2VlanServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanServiceName.setStatus("current")
_HwL2VlanManagementVlan_Type = EnabledStatus
_HwL2VlanManagementVlan_Object = MibTableColumn
hwL2VlanManagementVlan = _HwL2VlanManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 20),
    _HwL2VlanManagementVlan_Type()
)
hwL2VlanManagementVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanManagementVlan.setStatus("current")
_HwL2VlanDynamicVlan_Type = EnabledStatus
_HwL2VlanDynamicVlan_Object = MibTableColumn
hwL2VlanDynamicVlan = _HwL2VlanDynamicVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 1, 1, 1, 21),
    _HwL2VlanDynamicVlan_Type()
)
hwL2VlanDynamicVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanDynamicVlan.setStatus("current")
_HwL2VlanApply_ObjectIdentity = ObjectIdentity
hwL2VlanApply = _HwL2VlanApply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2)
)
_HwL2VlanStackingTable_Object = MibTable
hwL2VlanStackingTable = _HwL2VlanStackingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwL2VlanStackingTable.setStatus("current")
_HwL2VlanStackingEntry_Object = MibTableRow
hwL2VlanStackingEntry = _HwL2VlanStackingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1)
)
hwL2VlanStackingEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingInsideVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanStackingEntry.setStatus("current")


class _HwL2VlanStackingPortIndex_Type(Integer32):
    """Custom type hwL2VlanStackingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanStackingPortIndex_Type.__name__ = "Integer32"
_HwL2VlanStackingPortIndex_Object = MibTableColumn
hwL2VlanStackingPortIndex = _HwL2VlanStackingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1, 1),
    _HwL2VlanStackingPortIndex_Type()
)
hwL2VlanStackingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingPortIndex.setStatus("current")
_HwL2VlanStackingInsideVlanId_Type = VlanId
_HwL2VlanStackingInsideVlanId_Object = MibTableColumn
hwL2VlanStackingInsideVlanId = _HwL2VlanStackingInsideVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1, 2),
    _HwL2VlanStackingInsideVlanId_Type()
)
hwL2VlanStackingInsideVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingInsideVlanId.setStatus("current")


class _HwL2VlanStackingOutsideVlanListLow_Type(OctetString):
    """Custom type hwL2VlanStackingOutsideVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingOutsideVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanStackingOutsideVlanListLow_Object = MibTableColumn
hwL2VlanStackingOutsideVlanListLow = _HwL2VlanStackingOutsideVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1, 3),
    _HwL2VlanStackingOutsideVlanListLow_Type()
)
hwL2VlanStackingOutsideVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingOutsideVlanListLow.setStatus("current")


class _HwL2VlanStackingOutsideVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanStackingOutsideVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingOutsideVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanStackingOutsideVlanListHigh_Object = MibTableColumn
hwL2VlanStackingOutsideVlanListHigh = _HwL2VlanStackingOutsideVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1, 4),
    _HwL2VlanStackingOutsideVlanListHigh_Type()
)
hwL2VlanStackingOutsideVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingOutsideVlanListHigh.setStatus("current")
_HwL2VlanStackingRowStatus_Type = RowStatus
_HwL2VlanStackingRowStatus_Object = MibTableColumn
hwL2VlanStackingRowStatus = _HwL2VlanStackingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 1, 1, 5),
    _HwL2VlanStackingRowStatus_Type()
)
hwL2VlanStackingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingRowStatus.setStatus("current")
_HwL2VlanMappingTable_Object = MibTable
hwL2VlanMappingTable = _HwL2VlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwL2VlanMappingTable.setStatus("current")
_HwL2VlanMappingEntry_Object = MibTableRow
hwL2VlanMappingEntry = _HwL2VlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1)
)
hwL2VlanMappingEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingInsideVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanMappingEntry.setStatus("current")


class _HwL2VlanMappingPortIndex_Type(Integer32):
    """Custom type hwL2VlanMappingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanMappingPortIndex_Type.__name__ = "Integer32"
_HwL2VlanMappingPortIndex_Object = MibTableColumn
hwL2VlanMappingPortIndex = _HwL2VlanMappingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1, 1),
    _HwL2VlanMappingPortIndex_Type()
)
hwL2VlanMappingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingPortIndex.setStatus("current")
_HwL2VlanMappingInsideVlanId_Type = VlanId
_HwL2VlanMappingInsideVlanId_Object = MibTableColumn
hwL2VlanMappingInsideVlanId = _HwL2VlanMappingInsideVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1, 2),
    _HwL2VlanMappingInsideVlanId_Type()
)
hwL2VlanMappingInsideVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingInsideVlanId.setStatus("current")


class _HwL2VlanMappingOutsideVlanListLow_Type(OctetString):
    """Custom type hwL2VlanMappingOutsideVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingOutsideVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanMappingOutsideVlanListLow_Object = MibTableColumn
hwL2VlanMappingOutsideVlanListLow = _HwL2VlanMappingOutsideVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1, 3),
    _HwL2VlanMappingOutsideVlanListLow_Type()
)
hwL2VlanMappingOutsideVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingOutsideVlanListLow.setStatus("current")


class _HwL2VlanMappingOutsideVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanMappingOutsideVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingOutsideVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanMappingOutsideVlanListHigh_Object = MibTableColumn
hwL2VlanMappingOutsideVlanListHigh = _HwL2VlanMappingOutsideVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1, 4),
    _HwL2VlanMappingOutsideVlanListHigh_Type()
)
hwL2VlanMappingOutsideVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingOutsideVlanListHigh.setStatus("current")
_HwL2VlanMappingRowStatus_Type = RowStatus
_HwL2VlanMappingRowStatus_Object = MibTableColumn
hwL2VlanMappingRowStatus = _HwL2VlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 2, 1, 5),
    _HwL2VlanMappingRowStatus_Type()
)
hwL2VlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingRowStatus.setStatus("current")
_HwSuperVlanTable_Object = MibTable
hwSuperVlanTable = _HwSuperVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwSuperVlanTable.setStatus("current")
_HwSuperVlanEntry_Object = MibTableRow
hwSuperVlanEntry = _HwSuperVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 3, 1)
)
hwSuperVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwSuperVlanId"),
)
if mibBuilder.loadTexts:
    hwSuperVlanEntry.setStatus("current")
_HwSuperVlanId_Type = VlanId
_HwSuperVlanId_Object = MibTableColumn
hwSuperVlanId = _HwSuperVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 3, 1, 1),
    _HwSuperVlanId_Type()
)
hwSuperVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSuperVlanId.setStatus("current")


class _HwSubVlanListLow_Type(OctetString):
    """Custom type hwSubVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwSubVlanListLow_Type.__name__ = "OctetString"
_HwSubVlanListLow_Object = MibTableColumn
hwSubVlanListLow = _HwSubVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 3, 1, 2),
    _HwSubVlanListLow_Type()
)
hwSubVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSubVlanListLow.setStatus("current")


class _HwSubVlanListHigh_Type(OctetString):
    """Custom type hwSubVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwSubVlanListHigh_Type.__name__ = "OctetString"
_HwSubVlanListHigh_Object = MibTableColumn
hwSubVlanListHigh = _HwSubVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 3, 1, 3),
    _HwSubVlanListHigh_Type()
)
hwSubVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSubVlanListHigh.setStatus("current")
_HwL2InterfIsolateTable_Object = MibTable
hwL2InterfIsolateTable = _HwL2InterfIsolateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwL2InterfIsolateTable.setStatus("current")
_HwL2InterfIsolateEntry_Object = MibTableRow
hwL2InterfIsolateEntry = _HwL2InterfIsolateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 4, 1)
)
hwL2InterfIsolateEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2InterfIsolateVlanId"),
)
if mibBuilder.loadTexts:
    hwL2InterfIsolateEntry.setStatus("current")
_HwL2InterfIsolateVlanId_Type = VlanId
_HwL2InterfIsolateVlanId_Object = MibTableColumn
hwL2InterfIsolateVlanId = _HwL2InterfIsolateVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 4, 1, 1),
    _HwL2InterfIsolateVlanId_Type()
)
hwL2InterfIsolateVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2InterfIsolateVlanId.setStatus("current")


class _HwL2InterfIsolateInterflistLow_Type(OctetString):
    """Custom type hwL2InterfIsolateInterflistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )


_HwL2InterfIsolateInterflistLow_Type.__name__ = "OctetString"
_HwL2InterfIsolateInterflistLow_Object = MibTableColumn
hwL2InterfIsolateInterflistLow = _HwL2InterfIsolateInterflistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 4, 1, 2),
    _HwL2InterfIsolateInterflistLow_Type()
)
hwL2InterfIsolateInterflistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2InterfIsolateInterflistLow.setStatus("current")


class _HwL2InterfIsolateInterflistHigh_Type(OctetString):
    """Custom type hwL2InterfIsolateInterflistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )


_HwL2InterfIsolateInterflistHigh_Type.__name__ = "OctetString"
_HwL2InterfIsolateInterflistHigh_Object = MibTableColumn
hwL2InterfIsolateInterflistHigh = _HwL2InterfIsolateInterflistHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 4, 1, 3),
    _HwL2InterfIsolateInterflistHigh_Type()
)
hwL2InterfIsolateInterflistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2InterfIsolateInterflistHigh.setStatus("current")
_HwL2IsolatemappingTable_Object = MibTable
hwL2IsolatemappingTable = _HwL2IsolatemappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwL2IsolatemappingTable.setStatus("current")
_HwL2IsolatemappingEntry_Object = MibTableRow
hwL2IsolatemappingEntry = _HwL2IsolatemappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 5, 1)
)
hwL2IsolatemappingEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IsolatemappingPortNum"),
)
if mibBuilder.loadTexts:
    hwL2IsolatemappingEntry.setStatus("current")


class _HwL2IsolatemappingPortNum_Type(Integer32):
    """Custom type hwL2IsolatemappingPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwL2IsolatemappingPortNum_Type.__name__ = "Integer32"
_HwL2IsolatemappingPortNum_Object = MibTableColumn
hwL2IsolatemappingPortNum = _HwL2IsolatemappingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 5, 1, 1),
    _HwL2IsolatemappingPortNum_Type()
)
hwL2IsolatemappingPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IsolatemappingPortNum.setStatus("current")


class _HwL2IsolateInterflistLow_Type(OctetString):
    """Custom type hwL2IsolateInterflistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IsolateInterflistLow_Type.__name__ = "OctetString"
_HwL2IsolateInterflistLow_Object = MibTableColumn
hwL2IsolateInterflistLow = _HwL2IsolateInterflistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 5, 1, 2),
    _HwL2IsolateInterflistLow_Type()
)
hwL2IsolateInterflistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IsolateInterflistLow.setStatus("current")


class _HwL2IsolateInterflistHigh_Type(OctetString):
    """Custom type hwL2IsolateInterflistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2IsolateInterflistHigh_Type.__name__ = "OctetString"
_HwL2IsolateInterflistHigh_Object = MibTableColumn
hwL2IsolateInterflistHigh = _HwL2IsolateInterflistHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 5, 1, 3),
    _HwL2IsolateInterflistHigh_Type()
)
hwL2IsolateInterflistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IsolateInterflistHigh.setStatus("current")
_HwL2VlanStackingExtTable_Object = MibTable
hwL2VlanStackingExtTable = _HwL2VlanStackingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwL2VlanStackingExtTable.setStatus("current")
_HwL2VlanStackingExtEntry_Object = MibTableRow
hwL2VlanStackingExtEntry = _HwL2VlanStackingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1)
)
hwL2VlanStackingExtEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtAction"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanStackingExtEntry.setStatus("current")
_HwL2VlanStackingExtPortIndex_Type = InterfaceIndex
_HwL2VlanStackingExtPortIndex_Object = MibTableColumn
hwL2VlanStackingExtPortIndex = _HwL2VlanStackingExtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 1),
    _HwL2VlanStackingExtPortIndex_Type()
)
hwL2VlanStackingExtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtPortIndex.setStatus("current")
_HwL2VlanStackingExtVlanId_Type = VlanIdOrNone
_HwL2VlanStackingExtVlanId_Object = MibTableColumn
hwL2VlanStackingExtVlanId = _HwL2VlanStackingExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 2),
    _HwL2VlanStackingExtVlanId_Type()
)
hwL2VlanStackingExtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtVlanId.setStatus("current")


class _HwL2VlanStackingExtAction_Type(Integer32):
    """Custom type hwL2VlanStackingExtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pop", 1),
          ("push", 2))
    )


_HwL2VlanStackingExtAction_Type.__name__ = "Integer32"
_HwL2VlanStackingExtAction_Object = MibTableColumn
hwL2VlanStackingExtAction = _HwL2VlanStackingExtAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 3),
    _HwL2VlanStackingExtAction_Type()
)
hwL2VlanStackingExtAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtAction.setStatus("current")


class _HwL2VlanStackingExtDirection_Type(Integer32):
    """Custom type hwL2VlanStackingExtDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2))
    )


_HwL2VlanStackingExtDirection_Type.__name__ = "Integer32"
_HwL2VlanStackingExtDirection_Object = MibTableColumn
hwL2VlanStackingExtDirection = _HwL2VlanStackingExtDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 4),
    _HwL2VlanStackingExtDirection_Type()
)
hwL2VlanStackingExtDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtDirection.setStatus("current")


class _HwL2VlanStackingExtVlanListLow_Type(OctetString):
    """Custom type hwL2VlanStackingExtVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingExtVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanStackingExtVlanListLow_Object = MibTableColumn
hwL2VlanStackingExtVlanListLow = _HwL2VlanStackingExtVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 5),
    _HwL2VlanStackingExtVlanListLow_Type()
)
hwL2VlanStackingExtVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtVlanListLow.setStatus("current")


class _HwL2VlanStackingExtVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanStackingExtVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingExtVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanStackingExtVlanListHigh_Object = MibTableColumn
hwL2VlanStackingExtVlanListHigh = _HwL2VlanStackingExtVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 6),
    _HwL2VlanStackingExtVlanListHigh_Type()
)
hwL2VlanStackingExtVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtVlanListHigh.setStatus("current")
_HwL2VlanStackingExtRowStatus_Type = RowStatus
_HwL2VlanStackingExtRowStatus_Object = MibTableColumn
hwL2VlanStackingExtRowStatus = _HwL2VlanStackingExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 7),
    _HwL2VlanStackingExtRowStatus_Type()
)
hwL2VlanStackingExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtRowStatus.setStatus("current")


class _HwL2VlanStackingExtPriorityMode_Type(Integer32):
    """Custom type hwL2VlanStackingExtPriorityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityInherit", 1),
          ("remark8021p", 2))
    )


_HwL2VlanStackingExtPriorityMode_Type.__name__ = "Integer32"
_HwL2VlanStackingExtPriorityMode_Object = MibTableColumn
hwL2VlanStackingExtPriorityMode = _HwL2VlanStackingExtPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 8),
    _HwL2VlanStackingExtPriorityMode_Type()
)
hwL2VlanStackingExtPriorityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtPriorityMode.setStatus("current")


class _HwL2VlanStackingExtVlan8021p_Type(Integer32):
    """Custom type hwL2VlanStackingExtVlan8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanStackingExtVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanStackingExtVlan8021p_Object = MibTableColumn
hwL2VlanStackingExtVlan8021p = _HwL2VlanStackingExtVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 6, 1, 9),
    _HwL2VlanStackingExtVlan8021p_Type()
)
hwL2VlanStackingExtVlan8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingExtVlan8021p.setStatus("current")
_HwL2VlanQinQTable_Object = MibTable
hwL2VlanQinQTable = _HwL2VlanQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwL2VlanQinQTable.setStatus("current")
_HwL2VlanQinQEntry_Object = MibTableRow
hwL2VlanQinQEntry = _HwL2VlanQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7, 1)
)
hwL2VlanQinQEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanQinQEntry.setStatus("current")


class _HwL2VlanQinQIndex_Type(Integer32):
    """Custom type hwL2VlanQinQIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HwL2VlanQinQIndex_Type.__name__ = "Integer32"
_HwL2VlanQinQIndex_Object = MibTableColumn
hwL2VlanQinQIndex = _HwL2VlanQinQIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7, 1, 1),
    _HwL2VlanQinQIndex_Type()
)
hwL2VlanQinQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinQIndex.setStatus("current")


class _HwL2VlanQinQDirection_Type(Integer32):
    """Custom type hwL2VlanQinQDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwL2VlanQinQDirection_Type.__name__ = "Integer32"
_HwL2VlanQinQDirection_Object = MibTableColumn
hwL2VlanQinQDirection = _HwL2VlanQinQDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7, 1, 2),
    _HwL2VlanQinQDirection_Type()
)
hwL2VlanQinQDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinQDirection.setStatus("current")
_HwL2VlanQinQOutSideVlanId_Type = VlanId
_HwL2VlanQinQOutSideVlanId_Object = MibTableColumn
hwL2VlanQinQOutSideVlanId = _HwL2VlanQinQOutSideVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7, 1, 3),
    _HwL2VlanQinQOutSideVlanId_Type()
)
hwL2VlanQinQOutSideVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinQOutSideVlanId.setStatus("current")
_HwL2VlanSysQinQRowStatus_Type = RowStatus
_HwL2VlanSysQinQRowStatus_Object = MibTableColumn
hwL2VlanSysQinQRowStatus = _HwL2VlanSysQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 7, 1, 4),
    _HwL2VlanSysQinQRowStatus_Type()
)
hwL2VlanSysQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSysQinQRowStatus.setStatus("current")
_HwL2VlanInterfaceQinQTable_Object = MibTable
hwL2VlanInterfaceQinQTable = _HwL2VlanInterfaceQinQTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8)
)
if mibBuilder.loadTexts:
    hwL2VlanInterfaceQinQTable.setStatus("current")
_HwL2VlanInterfaceQinQEntry_Object = MibTableRow
hwL2VlanInterfaceQinQEntry = _HwL2VlanInterfaceQinQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1)
)
hwL2VlanInterfaceQinQEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQInterfaceIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQCVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinQDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanInterfaceQinQEntry.setStatus("current")
_HwL2VlanQinQInterfaceIndex_Type = InterfaceIndex
_HwL2VlanQinQInterfaceIndex_Object = MibTableColumn
hwL2VlanQinQInterfaceIndex = _HwL2VlanQinQInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 1),
    _HwL2VlanQinQInterfaceIndex_Type()
)
hwL2VlanQinQInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinQInterfaceIndex.setStatus("current")
_HwL2VlanQinQCVlanId_Type = VlanId
_HwL2VlanQinQCVlanId_Object = MibTableColumn
hwL2VlanQinQCVlanId = _HwL2VlanQinQCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 2),
    _HwL2VlanQinQCVlanId_Type()
)
hwL2VlanQinQCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinQCVlanId.setStatus("current")
_HwL2VlanQinQSVlanId_Type = VlanId
_HwL2VlanQinQSVlanId_Object = MibTableColumn
hwL2VlanQinQSVlanId = _HwL2VlanQinQSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 3),
    _HwL2VlanQinQSVlanId_Type()
)
hwL2VlanQinQSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinQSVlanId.setStatus("current")


class _HwL2VlanQinQAction_Type(Integer32):
    """Custom type hwL2VlanQinQAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nop", 2),
          ("push", 1))
    )


_HwL2VlanQinQAction_Type.__name__ = "Integer32"
_HwL2VlanQinQAction_Object = MibTableColumn
hwL2VlanQinQAction = _HwL2VlanQinQAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 4),
    _HwL2VlanQinQAction_Type()
)
hwL2VlanQinQAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinQAction.setStatus("current")
_HwL2VlanQinQNewCVlanId_Type = VlanId
_HwL2VlanQinQNewCVlanId_Object = MibTableColumn
hwL2VlanQinQNewCVlanId = _HwL2VlanQinQNewCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 5),
    _HwL2VlanQinQNewCVlanId_Type()
)
hwL2VlanQinQNewCVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinQNewCVlanId.setStatus("current")
_HwL2VlanInterfaceQinQRowStatus_Type = RowStatus
_HwL2VlanInterfaceQinQRowStatus_Object = MibTableColumn
hwL2VlanInterfaceQinQRowStatus = _HwL2VlanInterfaceQinQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 8, 1, 6),
    _HwL2VlanInterfaceQinQRowStatus_Type()
)
hwL2VlanInterfaceQinQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanInterfaceQinQRowStatus.setStatus("current")
_HwL2DVlanMappingTable_Object = MibTable
hwL2DVlanMappingTable = _HwL2DVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9)
)
if mibBuilder.loadTexts:
    hwL2DVlanMappingTable.setStatus("current")
_HwL2DVlanMappingEntry_Object = MibTableRow
hwL2DVlanMappingEntry = _HwL2DVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1)
)
hwL2DVlanMappingEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingInterfaceIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingExternalVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingInternalVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingDirection"),
)
if mibBuilder.loadTexts:
    hwL2DVlanMappingEntry.setStatus("current")
_HwL2DVlanMappingInterfaceIndex_Type = InterfaceIndex
_HwL2DVlanMappingInterfaceIndex_Object = MibTableColumn
hwL2DVlanMappingInterfaceIndex = _HwL2DVlanMappingInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 1),
    _HwL2DVlanMappingInterfaceIndex_Type()
)
hwL2DVlanMappingInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2DVlanMappingInterfaceIndex.setStatus("current")
_HwL2DVlanMappingExternalVlanId_Type = VlanId
_HwL2DVlanMappingExternalVlanId_Object = MibTableColumn
hwL2DVlanMappingExternalVlanId = _HwL2DVlanMappingExternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 2),
    _HwL2DVlanMappingExternalVlanId_Type()
)
hwL2DVlanMappingExternalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2DVlanMappingExternalVlanId.setStatus("current")
_HwL2DVlanMappingInternalVlanId_Type = VlanId
_HwL2DVlanMappingInternalVlanId_Object = MibTableColumn
hwL2DVlanMappingInternalVlanId = _HwL2DVlanMappingInternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 3),
    _HwL2DVlanMappingInternalVlanId_Type()
)
hwL2DVlanMappingInternalVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2DVlanMappingInternalVlanId.setStatus("current")


class _HwL2DVlanMappingDirection_Type(Integer32):
    """Custom type hwL2DVlanMappingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwL2DVlanMappingDirection_Type.__name__ = "Integer32"
_HwL2DVlanMappingDirection_Object = MibTableColumn
hwL2DVlanMappingDirection = _HwL2DVlanMappingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 4),
    _HwL2DVlanMappingDirection_Type()
)
hwL2DVlanMappingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2DVlanMappingDirection.setStatus("current")
_HwL2DVlanMappingMapExternalVlanId_Type = VlanId
_HwL2DVlanMappingMapExternalVlanId_Object = MibTableColumn
hwL2DVlanMappingMapExternalVlanId = _HwL2DVlanMappingMapExternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 5),
    _HwL2DVlanMappingMapExternalVlanId_Type()
)
hwL2DVlanMappingMapExternalVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2DVlanMappingMapExternalVlanId.setStatus("current")
_HwL2DVlanMappingMapInternalVlanId_Type = VlanId
_HwL2DVlanMappingMapInternalVlanId_Object = MibTableColumn
hwL2DVlanMappingMapInternalVlanId = _HwL2DVlanMappingMapInternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 6),
    _HwL2DVlanMappingMapInternalVlanId_Type()
)
hwL2DVlanMappingMapInternalVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2DVlanMappingMapInternalVlanId.setStatus("current")


class _HwL2DVlanMappingAction_Type(Integer32):
    """Custom type hwL2DVlanMappingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("popExternalVlan", 2),
          ("swap", 1))
    )


_HwL2DVlanMappingAction_Type.__name__ = "Integer32"
_HwL2DVlanMappingAction_Object = MibTableColumn
hwL2DVlanMappingAction = _HwL2DVlanMappingAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 7),
    _HwL2DVlanMappingAction_Type()
)
hwL2DVlanMappingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2DVlanMappingAction.setStatus("current")
_HwL2DVlanMappingRowStatus_Type = RowStatus
_HwL2DVlanMappingRowStatus_Object = MibTableColumn
hwL2DVlanMappingRowStatus = _HwL2DVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 9, 1, 8),
    _HwL2DVlanMappingRowStatus_Type()
)
hwL2DVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2DVlanMappingRowStatus.setStatus("current")
_HwL2VlanMappingExtTable_Object = MibTable
hwL2VlanMappingExtTable = _HwL2VlanMappingExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10)
)
if mibBuilder.loadTexts:
    hwL2VlanMappingExtTable.setStatus("current")
_HwL2VlanMappingExtEntry_Object = MibTableRow
hwL2VlanMappingExtEntry = _HwL2VlanMappingExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1)
)
hwL2VlanMappingExtEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtDirection"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanMappingExtEntry.setStatus("current")


class _HwL2VlanMappingExtPortIndex_Type(Integer32):
    """Custom type hwL2VlanMappingExtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanMappingExtPortIndex_Type.__name__ = "Integer32"
_HwL2VlanMappingExtPortIndex_Object = MibTableColumn
hwL2VlanMappingExtPortIndex = _HwL2VlanMappingExtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 1),
    _HwL2VlanMappingExtPortIndex_Type()
)
hwL2VlanMappingExtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtPortIndex.setStatus("current")


class _HwL2VlanMappingExtDirection_Type(Integer32):
    """Custom type hwL2VlanMappingExtDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwL2VlanMappingExtDirection_Type.__name__ = "Integer32"
_HwL2VlanMappingExtDirection_Object = MibTableColumn
hwL2VlanMappingExtDirection = _HwL2VlanMappingExtDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 2),
    _HwL2VlanMappingExtDirection_Type()
)
hwL2VlanMappingExtDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtDirection.setStatus("current")
_HwL2VlanMappingExtVlanId_Type = VlanId
_HwL2VlanMappingExtVlanId_Object = MibTableColumn
hwL2VlanMappingExtVlanId = _HwL2VlanMappingExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 3),
    _HwL2VlanMappingExtVlanId_Type()
)
hwL2VlanMappingExtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtVlanId.setStatus("current")


class _HwL2VlanMappingExtVlanListLow_Type(OctetString):
    """Custom type hwL2VlanMappingExtVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingExtVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanMappingExtVlanListLow_Object = MibTableColumn
hwL2VlanMappingExtVlanListLow = _HwL2VlanMappingExtVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 4),
    _HwL2VlanMappingExtVlanListLow_Type()
)
hwL2VlanMappingExtVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtVlanListLow.setStatus("current")


class _HwL2VlanMappingExtVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanMappingExtVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingExtVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanMappingExtVlanListHigh_Object = MibTableColumn
hwL2VlanMappingExtVlanListHigh = _HwL2VlanMappingExtVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 5),
    _HwL2VlanMappingExtVlanListHigh_Type()
)
hwL2VlanMappingExtVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtVlanListHigh.setStatus("current")
_HwL2VlanMappingExtRowStatus_Type = RowStatus
_HwL2VlanMappingExtRowStatus_Object = MibTableColumn
hwL2VlanMappingExtRowStatus = _HwL2VlanMappingExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 6),
    _HwL2VlanMappingExtRowStatus_Type()
)
hwL2VlanMappingExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtRowStatus.setStatus("current")


class _HwL2VlanMappingExtPriorityMode_Type(Integer32):
    """Custom type hwL2VlanMappingExtPriorityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityInherit", 1),
          ("remark8021p", 2))
    )


_HwL2VlanMappingExtPriorityMode_Type.__name__ = "Integer32"
_HwL2VlanMappingExtPriorityMode_Object = MibTableColumn
hwL2VlanMappingExtPriorityMode = _HwL2VlanMappingExtPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 7),
    _HwL2VlanMappingExtPriorityMode_Type()
)
hwL2VlanMappingExtPriorityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtPriorityMode.setStatus("current")


class _HwL2VlanMappingExtVlan8021p_Type(Integer32):
    """Custom type hwL2VlanMappingExtVlan8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanMappingExtVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanMappingExtVlan8021p_Object = MibTableColumn
hwL2VlanMappingExtVlan8021p = _HwL2VlanMappingExtVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 10, 1, 8),
    _HwL2VlanMappingExtVlan8021p_Type()
)
hwL2VlanMappingExtVlan8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingExtVlan8021p.setStatus("current")
_HwL2VlanStackingAdvTable_Object = MibTable
hwL2VlanStackingAdvTable = _HwL2VlanStackingAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11)
)
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvTable.setStatus("current")
_HwL2VlanStackingAdvEntry_Object = MibTableRow
hwL2VlanStackingAdvEntry = _HwL2VlanStackingAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1)
)
hwL2VlanStackingAdvEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvOutside8021p"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvStackVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvStack8021p"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvMapVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvEntry.setStatus("current")


class _HwL2VlanStackingAdvPortIndex_Type(Integer32):
    """Custom type hwL2VlanStackingAdvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanStackingAdvPortIndex_Type.__name__ = "Integer32"
_HwL2VlanStackingAdvPortIndex_Object = MibTableColumn
hwL2VlanStackingAdvPortIndex = _HwL2VlanStackingAdvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 1),
    _HwL2VlanStackingAdvPortIndex_Type()
)
hwL2VlanStackingAdvPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvPortIndex.setStatus("current")


class _HwL2VlanStackingAdvOutside8021p_Type(Integer32):
    """Custom type hwL2VlanStackingAdvOutside8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanStackingAdvOutside8021p_Type.__name__ = "Integer32"
_HwL2VlanStackingAdvOutside8021p_Object = MibTableColumn
hwL2VlanStackingAdvOutside8021p = _HwL2VlanStackingAdvOutside8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 2),
    _HwL2VlanStackingAdvOutside8021p_Type()
)
hwL2VlanStackingAdvOutside8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvOutside8021p.setStatus("current")
_HwL2VlanStackingAdvStackVlanId_Type = VlanId
_HwL2VlanStackingAdvStackVlanId_Object = MibTableColumn
hwL2VlanStackingAdvStackVlanId = _HwL2VlanStackingAdvStackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 3),
    _HwL2VlanStackingAdvStackVlanId_Type()
)
hwL2VlanStackingAdvStackVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvStackVlanId.setStatus("current")


class _HwL2VlanStackingAdvStack8021p_Type(Integer32):
    """Custom type hwL2VlanStackingAdvStack8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanStackingAdvStack8021p_Type.__name__ = "Integer32"
_HwL2VlanStackingAdvStack8021p_Object = MibTableColumn
hwL2VlanStackingAdvStack8021p = _HwL2VlanStackingAdvStack8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 4),
    _HwL2VlanStackingAdvStack8021p_Type()
)
hwL2VlanStackingAdvStack8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvStack8021p.setStatus("current")
_HwL2VlanStackingAdvMapVlanId_Type = VlanIdOrNone
_HwL2VlanStackingAdvMapVlanId_Object = MibTableColumn
hwL2VlanStackingAdvMapVlanId = _HwL2VlanStackingAdvMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 5),
    _HwL2VlanStackingAdvMapVlanId_Type()
)
hwL2VlanStackingAdvMapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvMapVlanId.setStatus("current")


class _HwL2VlanStackingAdvOutsideVlanListLow_Type(OctetString):
    """Custom type hwL2VlanStackingAdvOutsideVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingAdvOutsideVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanStackingAdvOutsideVlanListLow_Object = MibTableColumn
hwL2VlanStackingAdvOutsideVlanListLow = _HwL2VlanStackingAdvOutsideVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 6),
    _HwL2VlanStackingAdvOutsideVlanListLow_Type()
)
hwL2VlanStackingAdvOutsideVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvOutsideVlanListLow.setStatus("current")


class _HwL2VlanStackingAdvOutsideVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanStackingAdvOutsideVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingAdvOutsideVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanStackingAdvOutsideVlanListHigh_Object = MibTableColumn
hwL2VlanStackingAdvOutsideVlanListHigh = _HwL2VlanStackingAdvOutsideVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 7),
    _HwL2VlanStackingAdvOutsideVlanListHigh_Type()
)
hwL2VlanStackingAdvOutsideVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvOutsideVlanListHigh.setStatus("current")
_HwL2VlanStackingAdvRowStatus_Type = RowStatus
_HwL2VlanStackingAdvRowStatus_Object = MibTableColumn
hwL2VlanStackingAdvRowStatus = _HwL2VlanStackingAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 11, 1, 8),
    _HwL2VlanStackingAdvRowStatus_Type()
)
hwL2VlanStackingAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvRowStatus.setStatus("current")
_HwL2VlanMappingAdvTable_Object = MibTable
hwL2VlanMappingAdvTable = _HwL2VlanMappingAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvTable.setStatus("current")
_HwL2VlanMappingAdvEntry_Object = MibTableRow
hwL2VlanMappingAdvEntry = _HwL2VlanMappingAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1)
)
hwL2VlanMappingAdvEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvOutsideVlan8021p"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvMapVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvMapVlan8021p"),
)
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvEntry.setStatus("current")


class _HwL2VlanMappingAdvPortIndex_Type(Integer32):
    """Custom type hwL2VlanMappingAdvPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanMappingAdvPortIndex_Type.__name__ = "Integer32"
_HwL2VlanMappingAdvPortIndex_Object = MibTableColumn
hwL2VlanMappingAdvPortIndex = _HwL2VlanMappingAdvPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 1),
    _HwL2VlanMappingAdvPortIndex_Type()
)
hwL2VlanMappingAdvPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvPortIndex.setStatus("current")


class _HwL2VlanMappingAdvOutsideVlan8021p_Type(Integer32):
    """Custom type hwL2VlanMappingAdvOutsideVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanMappingAdvOutsideVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanMappingAdvOutsideVlan8021p_Object = MibTableColumn
hwL2VlanMappingAdvOutsideVlan8021p = _HwL2VlanMappingAdvOutsideVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 2),
    _HwL2VlanMappingAdvOutsideVlan8021p_Type()
)
hwL2VlanMappingAdvOutsideVlan8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvOutsideVlan8021p.setStatus("current")
_HwL2VlanMappingAdvMapVlanId_Type = VlanId
_HwL2VlanMappingAdvMapVlanId_Object = MibTableColumn
hwL2VlanMappingAdvMapVlanId = _HwL2VlanMappingAdvMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 3),
    _HwL2VlanMappingAdvMapVlanId_Type()
)
hwL2VlanMappingAdvMapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvMapVlanId.setStatus("current")


class _HwL2VlanMappingAdvMapVlan8021p_Type(Integer32):
    """Custom type hwL2VlanMappingAdvMapVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanMappingAdvMapVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanMappingAdvMapVlan8021p_Object = MibTableColumn
hwL2VlanMappingAdvMapVlan8021p = _HwL2VlanMappingAdvMapVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 4),
    _HwL2VlanMappingAdvMapVlan8021p_Type()
)
hwL2VlanMappingAdvMapVlan8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvMapVlan8021p.setStatus("current")


class _HwL2VlanMappingAdvOutsideVlanListLow_Type(OctetString):
    """Custom type hwL2VlanMappingAdvOutsideVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingAdvOutsideVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanMappingAdvOutsideVlanListLow_Object = MibTableColumn
hwL2VlanMappingAdvOutsideVlanListLow = _HwL2VlanMappingAdvOutsideVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 5),
    _HwL2VlanMappingAdvOutsideVlanListLow_Type()
)
hwL2VlanMappingAdvOutsideVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvOutsideVlanListLow.setStatus("current")


class _HwL2VlanMappingAdvOutsideVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanMappingAdvOutsideVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingAdvOutsideVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanMappingAdvOutsideVlanListHigh_Object = MibTableColumn
hwL2VlanMappingAdvOutsideVlanListHigh = _HwL2VlanMappingAdvOutsideVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 6),
    _HwL2VlanMappingAdvOutsideVlanListHigh_Type()
)
hwL2VlanMappingAdvOutsideVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvOutsideVlanListHigh.setStatus("current")
_HwL2VlanMappingAdvRowStatus_Type = RowStatus
_HwL2VlanMappingAdvRowStatus_Object = MibTableColumn
hwL2VlanMappingAdvRowStatus = _HwL2VlanMappingAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 12, 1, 7),
    _HwL2VlanMappingAdvRowStatus_Type()
)
hwL2VlanMappingAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvRowStatus.setStatus("current")
_HwL2VlanSwitchTable_Object = MibTable
hwL2VlanSwitchTable = _HwL2VlanSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchTable.setStatus("current")
_HwL2VlanSwitchEntry_Object = MibTableRow
hwL2VlanSwitchEntry = _HwL2VlanSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1)
)
hwL2VlanSwitchEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchIfIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchOuterVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchInnerVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchEntry.setStatus("current")
_HwL2VlanSwitchIfIndex_Type = InterfaceIndex
_HwL2VlanSwitchIfIndex_Object = MibTableColumn
hwL2VlanSwitchIfIndex = _HwL2VlanSwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 1),
    _HwL2VlanSwitchIfIndex_Type()
)
hwL2VlanSwitchIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchIfIndex.setStatus("current")
_HwL2VlanSwitchOuterVlanId_Type = VlanIdOrNone
_HwL2VlanSwitchOuterVlanId_Object = MibTableColumn
hwL2VlanSwitchOuterVlanId = _HwL2VlanSwitchOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 2),
    _HwL2VlanSwitchOuterVlanId_Type()
)
hwL2VlanSwitchOuterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchOuterVlanId.setStatus("current")
_HwL2VlanSwitchInnerVlanId_Type = VlanIdOrNone
_HwL2VlanSwitchInnerVlanId_Object = MibTableColumn
hwL2VlanSwitchInnerVlanId = _HwL2VlanSwitchInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 3),
    _HwL2VlanSwitchInnerVlanId_Type()
)
hwL2VlanSwitchInnerVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchInnerVlanId.setStatus("current")


class _HwL2VlanSwitchMode_Type(Integer32):
    """Custom type hwL2VlanSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("oneToOne", 4),
          ("oneToTwo", 5),
          ("oneToZero", 3),
          ("twoToOne", 7),
          ("twoToTwo", 8),
          ("twoToZero", 6),
          ("zeroToOne", 1),
          ("zeroToTwo", 2))
    )


_HwL2VlanSwitchMode_Type.__name__ = "Integer32"
_HwL2VlanSwitchMode_Object = MibTableColumn
hwL2VlanSwitchMode = _HwL2VlanSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 4),
    _HwL2VlanSwitchMode_Type()
)
hwL2VlanSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMode.setStatus("current")
_HwL2VlanSwitchOuterSwitchVlanId_Type = VlanIdOrNone
_HwL2VlanSwitchOuterSwitchVlanId_Object = MibTableColumn
hwL2VlanSwitchOuterSwitchVlanId = _HwL2VlanSwitchOuterSwitchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 5),
    _HwL2VlanSwitchOuterSwitchVlanId_Type()
)
hwL2VlanSwitchOuterSwitchVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchOuterSwitchVlanId.setStatus("current")
_HwL2VlanSwitchInnerSwitchVlanId_Type = VlanIdOrNone
_HwL2VlanSwitchInnerSwitchVlanId_Object = MibTableColumn
hwL2VlanSwitchInnerSwitchVlanId = _HwL2VlanSwitchInnerSwitchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 6),
    _HwL2VlanSwitchInnerSwitchVlanId_Type()
)
hwL2VlanSwitchInnerSwitchVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchInnerSwitchVlanId.setStatus("current")


class _HwL2VlanSwitch8021pRemark_Type(Integer32):
    """Custom type hwL2VlanSwitch8021pRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanSwitch8021pRemark_Type.__name__ = "Integer32"
_HwL2VlanSwitch8021pRemark_Object = MibTableColumn
hwL2VlanSwitch8021pRemark = _HwL2VlanSwitch8021pRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 7),
    _HwL2VlanSwitch8021pRemark_Type()
)
hwL2VlanSwitch8021pRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitch8021pRemark.setStatus("current")
_HwL2VlanSwitchOutIfIndex_Type = InterfaceIndex
_HwL2VlanSwitchOutIfIndex_Object = MibTableColumn
hwL2VlanSwitchOutIfIndex = _HwL2VlanSwitchOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 8),
    _HwL2VlanSwitchOutIfIndex_Type()
)
hwL2VlanSwitchOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchOutIfIndex.setStatus("current")
_HwL2VlanSwitchMtu_Type = Integer32
_HwL2VlanSwitchMtu_Object = MibTableColumn
hwL2VlanSwitchMtu = _HwL2VlanSwitchMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 9),
    _HwL2VlanSwitchMtu_Type()
)
hwL2VlanSwitchMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMtu.setStatus("current")
_HwL2VlanSwitchMtuDiscardPkts_Type = Counter64
_HwL2VlanSwitchMtuDiscardPkts_Object = MibTableColumn
hwL2VlanSwitchMtuDiscardPkts = _HwL2VlanSwitchMtuDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 10),
    _HwL2VlanSwitchMtuDiscardPkts_Type()
)
hwL2VlanSwitchMtuDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMtuDiscardPkts.setStatus("current")
_HwL2VlanSwitchMtuDiscardBytes_Type = Counter64
_HwL2VlanSwitchMtuDiscardBytes_Object = MibTableColumn
hwL2VlanSwitchMtuDiscardBytes = _HwL2VlanSwitchMtuDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 11),
    _HwL2VlanSwitchMtuDiscardBytes_Type()
)
hwL2VlanSwitchMtuDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMtuDiscardBytes.setStatus("current")
_HwL2VlanSwitchMtuResetFlag_Type = EnabledStatus
_HwL2VlanSwitchMtuResetFlag_Object = MibTableColumn
hwL2VlanSwitchMtuResetFlag = _HwL2VlanSwitchMtuResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 12),
    _HwL2VlanSwitchMtuResetFlag_Type()
)
hwL2VlanSwitchMtuResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMtuResetFlag.setStatus("current")
_HwL2VlanSwitchMtuEnableFlag_Type = EnabledStatus
_HwL2VlanSwitchMtuEnableFlag_Object = MibTableColumn
hwL2VlanSwitchMtuEnableFlag = _HwL2VlanSwitchMtuEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 13),
    _HwL2VlanSwitchMtuEnableFlag_Type()
)
hwL2VlanSwitchMtuEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanSwitchMtuEnableFlag.setStatus("current")
_HwL2VlanSwitchRowStatus_Type = RowStatus
_HwL2VlanSwitchRowStatus_Object = MibTableColumn
hwL2VlanSwitchRowStatus = _HwL2VlanSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 13, 1, 14),
    _HwL2VlanSwitchRowStatus_Type()
)
hwL2VlanSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchRowStatus.setStatus("current")
_HwL2VlanQinqVlanTransEnaTable_Object = MibTable
hwL2VlanQinqVlanTransEnaTable = _HwL2VlanQinqVlanTransEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 14)
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEnaTable.setStatus("current")
_HwL2VlanQinqVlanTransEnaEntry_Object = MibTableRow
hwL2VlanQinqVlanTransEnaEntry = _HwL2VlanQinqVlanTransEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 14, 1)
)
hwL2VlanQinqVlanTransEnaEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransEnaPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEnaEntry.setStatus("current")


class _HwL2VlanQinqVlanTransEnaPortIndex_Type(Integer32):
    """Custom type hwL2VlanQinqVlanTransEnaPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanQinqVlanTransEnaPortIndex_Type.__name__ = "Integer32"
_HwL2VlanQinqVlanTransEnaPortIndex_Object = MibTableColumn
hwL2VlanQinqVlanTransEnaPortIndex = _HwL2VlanQinqVlanTransEnaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 14, 1, 1),
    _HwL2VlanQinqVlanTransEnaPortIndex_Type()
)
hwL2VlanQinqVlanTransEnaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEnaPortIndex.setStatus("current")


class _HwL2VlanQinqVlanTransEna_Type(EnabledStatus):
    """Custom type hwL2VlanQinqVlanTransEna based on EnabledStatus"""
    defaultValue = 2


_HwL2VlanQinqVlanTransEna_Object = MibTableColumn
hwL2VlanQinqVlanTransEna = _HwL2VlanQinqVlanTransEna_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 14, 1, 2),
    _HwL2VlanQinqVlanTransEna_Type()
)
hwL2VlanQinqVlanTransEna.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEna.setStatus("current")
_HwL2VlanQinqVlanTransEnaRowStatus_Type = RowStatus
_HwL2VlanQinqVlanTransEnaRowStatus_Object = MibTableColumn
hwL2VlanQinqVlanTransEnaRowStatus = _HwL2VlanQinqVlanTransEnaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 14, 1, 3),
    _HwL2VlanQinqVlanTransEnaRowStatus_Type()
)
hwL2VlanQinqVlanTransEnaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEnaRowStatus.setStatus("current")
_HwL2VlanQinqVlanTransMissDropTable_Object = MibTable
hwL2VlanQinqVlanTransMissDropTable = _HwL2VlanQinqVlanTransMissDropTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 15)
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDropTable.setStatus("current")
_HwL2VlanQinqVlanTransMissDropEntry_Object = MibTableRow
hwL2VlanQinqVlanTransMissDropEntry = _HwL2VlanQinqVlanTransMissDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 15, 1)
)
hwL2VlanQinqVlanTransMissDropEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransMissDropPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDropEntry.setStatus("current")


class _HwL2VlanQinqVlanTransMissDropPortIndex_Type(Integer32):
    """Custom type hwL2VlanQinqVlanTransMissDropPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanQinqVlanTransMissDropPortIndex_Type.__name__ = "Integer32"
_HwL2VlanQinqVlanTransMissDropPortIndex_Object = MibTableColumn
hwL2VlanQinqVlanTransMissDropPortIndex = _HwL2VlanQinqVlanTransMissDropPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 15, 1, 1),
    _HwL2VlanQinqVlanTransMissDropPortIndex_Type()
)
hwL2VlanQinqVlanTransMissDropPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDropPortIndex.setStatus("current")


class _HwL2VlanQinqVlanTransMissDrop_Type(Integer32):
    """Custom type hwL2VlanQinqVlanTransMissDrop based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("noDrop", 1))
    )


_HwL2VlanQinqVlanTransMissDrop_Type.__name__ = "Integer32"
_HwL2VlanQinqVlanTransMissDrop_Object = MibTableColumn
hwL2VlanQinqVlanTransMissDrop = _HwL2VlanQinqVlanTransMissDrop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 15, 1, 2),
    _HwL2VlanQinqVlanTransMissDrop_Type()
)
hwL2VlanQinqVlanTransMissDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDrop.setStatus("current")
_HwL2VlanQinqVlanTransMissDropRowStatus_Type = RowStatus
_HwL2VlanQinqVlanTransMissDropRowStatus_Object = MibTableColumn
hwL2VlanQinqVlanTransMissDropRowStatus = _HwL2VlanQinqVlanTransMissDropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 15, 1, 3),
    _HwL2VlanQinqVlanTransMissDropRowStatus_Type()
)
hwL2VlanQinqVlanTransMissDropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDropRowStatus.setStatus("current")
_HwL2VlanViewMappingTable_Object = MibTable
hwL2VlanViewMappingTable = _HwL2VlanViewMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16)
)
if mibBuilder.loadTexts:
    hwL2VlanViewMappingTable.setStatus("current")
_HwL2VlanViewMappingEntry_Object = MibTableRow
hwL2VlanViewMappingEntry = _HwL2VlanViewMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1)
)
hwL2VlanViewMappingEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanViewMappingEntry.setStatus("current")
_HwL2VlanViewMappingVlanId_Type = VlanId
_HwL2VlanViewMappingVlanId_Object = MibTableColumn
hwL2VlanViewMappingVlanId = _HwL2VlanViewMappingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 1),
    _HwL2VlanViewMappingVlanId_Type()
)
hwL2VlanViewMappingVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingVlanId.setStatus("current")


class _HwL2VlanViewMappingDirection_Type(Integer32):
    """Custom type hwL2VlanViewMappingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HwL2VlanViewMappingDirection_Type.__name__ = "Integer32"
_HwL2VlanViewMappingDirection_Object = MibTableColumn
hwL2VlanViewMappingDirection = _HwL2VlanViewMappingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 2),
    _HwL2VlanViewMappingDirection_Type()
)
hwL2VlanViewMappingDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingDirection.setStatus("current")
_HwL2VlanViewMappingMapVlanId_Type = VlanId
_HwL2VlanViewMappingMapVlanId_Object = MibTableColumn
hwL2VlanViewMappingMapVlanId = _HwL2VlanViewMappingMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 3),
    _HwL2VlanViewMappingMapVlanId_Type()
)
hwL2VlanViewMappingMapVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingMapVlanId.setStatus("current")


class _HwL2VlanViewMappingPriorityMode_Type(Integer32):
    """Custom type hwL2VlanViewMappingPriorityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityInherit", 1),
          ("remark8021p", 2))
    )


_HwL2VlanViewMappingPriorityMode_Type.__name__ = "Integer32"
_HwL2VlanViewMappingPriorityMode_Object = MibTableColumn
hwL2VlanViewMappingPriorityMode = _HwL2VlanViewMappingPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 4),
    _HwL2VlanViewMappingPriorityMode_Type()
)
hwL2VlanViewMappingPriorityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingPriorityMode.setStatus("current")


class _HwL2VlanViewMappingVlan8021p_Type(Integer32):
    """Custom type hwL2VlanViewMappingVlan8021p based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanViewMappingVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanViewMappingVlan8021p_Object = MibTableColumn
hwL2VlanViewMappingVlan8021p = _HwL2VlanViewMappingVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 5),
    _HwL2VlanViewMappingVlan8021p_Type()
)
hwL2VlanViewMappingVlan8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingVlan8021p.setStatus("current")
_HwL2VlanViewMappingRowStatus_Type = RowStatus
_HwL2VlanViewMappingRowStatus_Object = MibTableColumn
hwL2VlanViewMappingRowStatus = _HwL2VlanViewMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 16, 1, 6),
    _HwL2VlanViewMappingRowStatus_Type()
)
hwL2VlanViewMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanViewMappingRowStatus.setStatus("current")
_HwL2VlanStackingMaskTable_Object = MibTable
hwL2VlanStackingMaskTable = _HwL2VlanStackingMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17)
)
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskTable.setStatus("current")
_HwL2VlanStackingMaskEntry_Object = MibTableRow
hwL2VlanStackingMaskEntry = _HwL2VlanStackingMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1)
)
hwL2VlanStackingMaskEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskStackVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskStack8021p"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskAction"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskEntry.setStatus("current")
_HwL2VlanStackingMaskPortIndex_Type = InterfaceIndex
_HwL2VlanStackingMaskPortIndex_Object = MibTableColumn
hwL2VlanStackingMaskPortIndex = _HwL2VlanStackingMaskPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 1),
    _HwL2VlanStackingMaskPortIndex_Type()
)
hwL2VlanStackingMaskPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskPortIndex.setStatus("current")
_HwL2VlanStackingMaskStackVlanId_Type = VlanIdOrNone
_HwL2VlanStackingMaskStackVlanId_Object = MibTableColumn
hwL2VlanStackingMaskStackVlanId = _HwL2VlanStackingMaskStackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 2),
    _HwL2VlanStackingMaskStackVlanId_Type()
)
hwL2VlanStackingMaskStackVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskStackVlanId.setStatus("current")


class _HwL2VlanStackingMaskStack8021p_Type(Integer32):
    """Custom type hwL2VlanStackingMaskStack8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanStackingMaskStack8021p_Type.__name__ = "Integer32"
_HwL2VlanStackingMaskStack8021p_Object = MibTableColumn
hwL2VlanStackingMaskStack8021p = _HwL2VlanStackingMaskStack8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 3),
    _HwL2VlanStackingMaskStack8021p_Type()
)
hwL2VlanStackingMaskStack8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskStack8021p.setStatus("current")


class _HwL2VlanStackingMaskAction_Type(Integer32):
    """Custom type hwL2VlanStackingMaskAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pop", 1),
          ("push", 2))
    )


_HwL2VlanStackingMaskAction_Type.__name__ = "Integer32"
_HwL2VlanStackingMaskAction_Object = MibTableColumn
hwL2VlanStackingMaskAction = _HwL2VlanStackingMaskAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 4),
    _HwL2VlanStackingMaskAction_Type()
)
hwL2VlanStackingMaskAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskAction.setStatus("current")


class _HwL2VlanStackingMaskDirection_Type(Integer32):
    """Custom type hwL2VlanStackingMaskDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inside", 1),
          ("outside", 2))
    )


_HwL2VlanStackingMaskDirection_Type.__name__ = "Integer32"
_HwL2VlanStackingMaskDirection_Object = MibTableColumn
hwL2VlanStackingMaskDirection = _HwL2VlanStackingMaskDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 5),
    _HwL2VlanStackingMaskDirection_Type()
)
hwL2VlanStackingMaskDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskDirection.setStatus("current")


class _HwL2VlanStackingMaskVlanListLow_Type(OctetString):
    """Custom type hwL2VlanStackingMaskVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingMaskVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanStackingMaskVlanListLow_Object = MibTableColumn
hwL2VlanStackingMaskVlanListLow = _HwL2VlanStackingMaskVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 6),
    _HwL2VlanStackingMaskVlanListLow_Type()
)
hwL2VlanStackingMaskVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskVlanListLow.setStatus("current")


class _HwL2VlanStackingMaskVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanStackingMaskVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanStackingMaskVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanStackingMaskVlanListHigh_Object = MibTableColumn
hwL2VlanStackingMaskVlanListHigh = _HwL2VlanStackingMaskVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 7),
    _HwL2VlanStackingMaskVlanListHigh_Type()
)
hwL2VlanStackingMaskVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskVlanListHigh.setStatus("current")
_HwL2VlanStackingMaskRowStatus_Type = RowStatus
_HwL2VlanStackingMaskRowStatus_Object = MibTableColumn
hwL2VlanStackingMaskRowStatus = _HwL2VlanStackingMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 17, 1, 8),
    _HwL2VlanStackingMaskRowStatus_Type()
)
hwL2VlanStackingMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskRowStatus.setStatus("current")
_HwL2VlanIpSubnetVlanTable_Object = MibTable
hwL2VlanIpSubnetVlanTable = _HwL2VlanIpSubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18)
)
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanTable.setStatus("current")
_HwL2VlanIpSubnetVlanEntry_Object = MibTableRow
hwL2VlanIpSubnetVlanEntry = _HwL2VlanIpSubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1)
)
hwL2VlanIpSubnetVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanIpSubnetIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanEntry.setStatus("current")
_HwL2VlanIpSubnetVlanVlanId_Type = VlanId
_HwL2VlanIpSubnetVlanVlanId_Object = MibTableColumn
hwL2VlanIpSubnetVlanVlanId = _HwL2VlanIpSubnetVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 1),
    _HwL2VlanIpSubnetVlanVlanId_Type()
)
hwL2VlanIpSubnetVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanVlanId.setStatus("current")


class _HwL2VlanIpSubnetVlanIpSubnetIndex_Type(Integer32):
    """Custom type hwL2VlanIpSubnetVlanIpSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HwL2VlanIpSubnetVlanIpSubnetIndex_Type.__name__ = "Integer32"
_HwL2VlanIpSubnetVlanIpSubnetIndex_Object = MibTableColumn
hwL2VlanIpSubnetVlanIpSubnetIndex = _HwL2VlanIpSubnetVlanIpSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 2),
    _HwL2VlanIpSubnetVlanIpSubnetIndex_Type()
)
hwL2VlanIpSubnetVlanIpSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanIpSubnetIndex.setStatus("current")
_HwL2VlanIpSubnetVlanIpAddress_Type = IpAddress
_HwL2VlanIpSubnetVlanIpAddress_Object = MibTableColumn
hwL2VlanIpSubnetVlanIpAddress = _HwL2VlanIpSubnetVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 3),
    _HwL2VlanIpSubnetVlanIpAddress_Type()
)
hwL2VlanIpSubnetVlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanIpAddress.setStatus("current")
_HwL2VlanIpSubnetVlanIpSubnetMask_Type = IpAddress
_HwL2VlanIpSubnetVlanIpSubnetMask_Object = MibTableColumn
hwL2VlanIpSubnetVlanIpSubnetMask = _HwL2VlanIpSubnetVlanIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 4),
    _HwL2VlanIpSubnetVlanIpSubnetMask_Type()
)
hwL2VlanIpSubnetVlanIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanIpSubnetMask.setStatus("current")


class _HwL2VlanIpSubnetVlanPriority_Type(Integer32):
    """Custom type hwL2VlanIpSubnetVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanIpSubnetVlanPriority_Type.__name__ = "Integer32"
_HwL2VlanIpSubnetVlanPriority_Object = MibTableColumn
hwL2VlanIpSubnetVlanPriority = _HwL2VlanIpSubnetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 5),
    _HwL2VlanIpSubnetVlanPriority_Type()
)
hwL2VlanIpSubnetVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanPriority.setStatus("current")
_HwL2VlanIpSubnetVlanRowStatus_Type = RowStatus
_HwL2VlanIpSubnetVlanRowStatus_Object = MibTableColumn
hwL2VlanIpSubnetVlanRowStatus = _HwL2VlanIpSubnetVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 18, 1, 6),
    _HwL2VlanIpSubnetVlanRowStatus_Type()
)
hwL2VlanIpSubnetVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanRowStatus.setStatus("current")
_HwL2VlanMacVlanTable_Object = MibTable
hwL2VlanMacVlanTable = _HwL2VlanMacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19)
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanTable.setStatus("current")
_HwL2VlanMacVlanEntry_Object = MibTableRow
hwL2VlanMacVlanEntry = _HwL2VlanMacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19, 1)
)
hwL2VlanMacVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanEntry.setStatus("current")
_HwL2VlanMacVlanVlanId_Type = VlanId
_HwL2VlanMacVlanVlanId_Object = MibTableColumn
hwL2VlanMacVlanVlanId = _HwL2VlanMacVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19, 1, 1),
    _HwL2VlanMacVlanVlanId_Type()
)
hwL2VlanMacVlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanVlanId.setStatus("current")
_HwL2VlanMacVlanMac_Type = MacAddress
_HwL2VlanMacVlanMac_Object = MibTableColumn
hwL2VlanMacVlanMac = _HwL2VlanMacVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19, 1, 2),
    _HwL2VlanMacVlanMac_Type()
)
hwL2VlanMacVlanMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanMac.setStatus("current")


class _HwL2VlanMacVlanVlanPriority_Type(Integer32):
    """Custom type hwL2VlanMacVlanVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanMacVlanVlanPriority_Type.__name__ = "Integer32"
_HwL2VlanMacVlanVlanPriority_Object = MibTableColumn
hwL2VlanMacVlanVlanPriority = _HwL2VlanMacVlanVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19, 1, 3),
    _HwL2VlanMacVlanVlanPriority_Type()
)
hwL2VlanMacVlanVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanVlanPriority.setStatus("current")
_HwL2VlanMacVlanMacRowStatus_Type = RowStatus
_HwL2VlanMacVlanMacRowStatus_Object = MibTableColumn
hwL2VlanMacVlanMacRowStatus = _HwL2VlanMacVlanMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 19, 1, 4),
    _HwL2VlanMacVlanMacRowStatus_Type()
)
hwL2VlanMacVlanMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanMacRowStatus.setStatus("current")
_HwL2VlanProtocolVlanTable_Object = MibTable
hwL2VlanProtocolVlanTable = _HwL2VlanProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20)
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanTable.setStatus("current")
_HwL2VlanProtocolVlanEntry_Object = MibTableRow
hwL2VlanProtocolVlanEntry = _HwL2VlanProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1)
)
hwL2VlanProtocolVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanEntry.setStatus("current")
_HwL2VlanProtocolVlanVlanId_Type = VlanId
_HwL2VlanProtocolVlanVlanId_Object = MibTableColumn
hwL2VlanProtocolVlanVlanId = _HwL2VlanProtocolVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1, 1),
    _HwL2VlanProtocolVlanVlanId_Type()
)
hwL2VlanProtocolVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanVlanId.setStatus("current")


class _HwL2VlanProtocolVlanProtocolIndex_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwL2VlanProtocolVlanProtocolIndex_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanProtocolIndex_Object = MibTableColumn
hwL2VlanProtocolVlanProtocolIndex = _HwL2VlanProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1, 2),
    _HwL2VlanProtocolVlanProtocolIndex_Type()
)
hwL2VlanProtocolVlanProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanProtocolIndex.setStatus("current")
_HwL2VlanProtocolVlanProtocolType_Type = Integer32
_HwL2VlanProtocolVlanProtocolType_Object = MibTableColumn
hwL2VlanProtocolVlanProtocolType = _HwL2VlanProtocolVlanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1, 3),
    _HwL2VlanProtocolVlanProtocolType_Type()
)
hwL2VlanProtocolVlanProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanProtocolType.setStatus("current")


class _HwL2VlanProtocolVlanEncapType_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etherii", 1),
          ("llc", 3),
          ("snap", 2))
    )


_HwL2VlanProtocolVlanEncapType_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanEncapType_Object = MibTableColumn
hwL2VlanProtocolVlanEncapType = _HwL2VlanProtocolVlanEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1, 4),
    _HwL2VlanProtocolVlanEncapType_Type()
)
hwL2VlanProtocolVlanEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanEncapType.setStatus("current")
_HwL2VlanProtocolVlanRowStatus_Type = RowStatus
_HwL2VlanProtocolVlanRowStatus_Object = MibTableColumn
hwL2VlanProtocolVlanRowStatus = _HwL2VlanProtocolVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 20, 1, 5),
    _HwL2VlanProtocolVlanRowStatus_Type()
)
hwL2VlanProtocolVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanRowStatus.setStatus("current")
_HwL2VlanPolicyVlanTable_Object = MibTable
hwL2VlanPolicyVlanTable = _HwL2VlanPolicyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21)
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanTable.setStatus("current")
_HwL2VlanPolicyVlanEntry_Object = MibTableRow
hwL2VlanPolicyVlanEntry = _HwL2VlanPolicyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1)
)
hwL2VlanPolicyVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanEntry.setStatus("current")
_HwL2VlanPolicyVlanMac_Type = MacAddress
_HwL2VlanPolicyVlanMac_Object = MibTableColumn
hwL2VlanPolicyVlanMac = _HwL2VlanPolicyVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 1),
    _HwL2VlanPolicyVlanMac_Type()
)
hwL2VlanPolicyVlanMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanMac.setStatus("current")
_HwL2VlanPolicyVlanIp_Type = IpAddress
_HwL2VlanPolicyVlanIp_Object = MibTableColumn
hwL2VlanPolicyVlanIp = _HwL2VlanPolicyVlanIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 2),
    _HwL2VlanPolicyVlanIp_Type()
)
hwL2VlanPolicyVlanIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanIp.setStatus("current")


class _HwL2VlanPolicyVlanPort_Type(Integer32):
    """Custom type hwL2VlanPolicyVlanPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanPolicyVlanPort_Type.__name__ = "Integer32"
_HwL2VlanPolicyVlanPort_Object = MibTableColumn
hwL2VlanPolicyVlanPort = _HwL2VlanPolicyVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 3),
    _HwL2VlanPolicyVlanPort_Type()
)
hwL2VlanPolicyVlanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanPort.setStatus("current")
_HwL2VlanPolicyVlanVlanId_Type = VlanId
_HwL2VlanPolicyVlanVlanId_Object = MibTableColumn
hwL2VlanPolicyVlanVlanId = _HwL2VlanPolicyVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 4),
    _HwL2VlanPolicyVlanVlanId_Type()
)
hwL2VlanPolicyVlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanVlanId.setStatus("current")
_HwL2VlanPolicyVlanVlanPriority_Type = Integer32
_HwL2VlanPolicyVlanVlanPriority_Object = MibTableColumn
hwL2VlanPolicyVlanVlanPriority = _HwL2VlanPolicyVlanVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 5),
    _HwL2VlanPolicyVlanVlanPriority_Type()
)
hwL2VlanPolicyVlanVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanVlanPriority.setStatus("current")
_HwL2VlanPolicyVlanRowStatus_Type = RowStatus
_HwL2VlanPolicyVlanRowStatus_Object = MibTableColumn
hwL2VlanPolicyVlanRowStatus = _HwL2VlanPolicyVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 21, 1, 6),
    _HwL2VlanPolicyVlanRowStatus_Type()
)
hwL2VlanPolicyVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanRowStatus.setStatus("current")


class _HwL2VlanVoiceVlanEnabledVlanId_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanEnabledVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwL2VlanVoiceVlanEnabledVlanId_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanEnabledVlanId_Object = MibScalar
hwL2VlanVoiceVlanEnabledVlanId = _HwL2VlanVoiceVlanEnabledVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 22),
    _HwL2VlanVoiceVlanEnabledVlanId_Type()
)
hwL2VlanVoiceVlanEnabledVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanEnabledVlanId.setStatus("current")


class _HwL2VlanVoiceVlanAgingTime_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_HwL2VlanVoiceVlanAgingTime_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanAgingTime_Object = MibScalar
hwL2VlanVoiceVlanAgingTime = _HwL2VlanVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 23),
    _HwL2VlanVoiceVlanAgingTime_Type()
)
hwL2VlanVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanAgingTime.setStatus("current")


class _HwL2VlanVoiceVlanSecurityMode_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("security", 1))
    )


_HwL2VlanVoiceVlanSecurityMode_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanSecurityMode_Object = MibScalar
hwL2VlanVoiceVlanSecurityMode = _HwL2VlanVoiceVlanSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 24),
    _HwL2VlanVoiceVlanSecurityMode_Type()
)
hwL2VlanVoiceVlanSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanSecurityMode.setStatus("current")
_HwL2VlanVoiceVlanPortTable_Object = MibTable
hwL2VlanVoiceVlanPortTable = _HwL2VlanVoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25)
)
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortTable.setStatus("current")
_HwL2VlanVoiceVlanPortEntry_Object = MibTableRow
hwL2VlanVoiceVlanPortEntry = _HwL2VlanVoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1)
)
hwL2VlanVoiceVlanPortEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortEntry.setStatus("current")


class _HwL2VlanVoiceVlanPortIndex_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanVoiceVlanPortIndex_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanPortIndex_Object = MibTableColumn
hwL2VlanVoiceVlanPortIndex = _HwL2VlanVoiceVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1, 1),
    _HwL2VlanVoiceVlanPortIndex_Type()
)
hwL2VlanVoiceVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortIndex.setStatus("current")
_HwL2VlanVoiceVlanPortEnable_Type = EnabledStatus
_HwL2VlanVoiceVlanPortEnable_Object = MibTableColumn
hwL2VlanVoiceVlanPortEnable = _HwL2VlanVoiceVlanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1, 2),
    _HwL2VlanVoiceVlanPortEnable_Type()
)
hwL2VlanVoiceVlanPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortEnable.setStatus("current")


class _HwL2VlanVoiceVlanPortMode_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_HwL2VlanVoiceVlanPortMode_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanPortMode_Object = MibTableColumn
hwL2VlanVoiceVlanPortMode = _HwL2VlanVoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1, 3),
    _HwL2VlanVoiceVlanPortMode_Type()
)
hwL2VlanVoiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortMode.setStatus("current")
_HwL2VlanVoiceVlanPortLegacy_Type = EnabledStatus
_HwL2VlanVoiceVlanPortLegacy_Object = MibTableColumn
hwL2VlanVoiceVlanPortLegacy = _HwL2VlanVoiceVlanPortLegacy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1, 4),
    _HwL2VlanVoiceVlanPortLegacy_Type()
)
hwL2VlanVoiceVlanPortLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortLegacy.setStatus("current")


class _HwL2VlanVoiceVlanPortSecurityMode_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("security", 1))
    )


_HwL2VlanVoiceVlanPortSecurityMode_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanPortSecurityMode_Object = MibTableColumn
hwL2VlanVoiceVlanPortSecurityMode = _HwL2VlanVoiceVlanPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 25, 1, 5),
    _HwL2VlanVoiceVlanPortSecurityMode_Type()
)
hwL2VlanVoiceVlanPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanPortSecurityMode.setStatus("current")
_HwL2VlanVoiceVlanOuiTable_Object = MibTable
hwL2VlanVoiceVlanOuiTable = _HwL2VlanVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26)
)
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiTable.setStatus("current")
_HwL2VlanVoiceVlanOuiEntry_Object = MibTableRow
hwL2VlanVoiceVlanOuiEntry = _HwL2VlanVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26, 1)
)
hwL2VlanVoiceVlanOuiEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanOuiAddress"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanOuiMask"),
)
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiEntry.setStatus("current")
_HwL2VlanVoiceVlanOuiAddress_Type = MacAddress
_HwL2VlanVoiceVlanOuiAddress_Object = MibTableColumn
hwL2VlanVoiceVlanOuiAddress = _HwL2VlanVoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26, 1, 1),
    _HwL2VlanVoiceVlanOuiAddress_Type()
)
hwL2VlanVoiceVlanOuiAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiAddress.setStatus("current")
_HwL2VlanVoiceVlanOuiMask_Type = MacAddress
_HwL2VlanVoiceVlanOuiMask_Object = MibTableColumn
hwL2VlanVoiceVlanOuiMask = _HwL2VlanVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26, 1, 2),
    _HwL2VlanVoiceVlanOuiMask_Type()
)
hwL2VlanVoiceVlanOuiMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiMask.setStatus("current")


class _HwL2VlanVoiceVlanOuiDescription_Type(OctetString):
    """Custom type hwL2VlanVoiceVlanOuiDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwL2VlanVoiceVlanOuiDescription_Type.__name__ = "OctetString"
_HwL2VlanVoiceVlanOuiDescription_Object = MibTableColumn
hwL2VlanVoiceVlanOuiDescription = _HwL2VlanVoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26, 1, 3),
    _HwL2VlanVoiceVlanOuiDescription_Type()
)
hwL2VlanVoiceVlanOuiDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiDescription.setStatus("current")
_HwL2VlanVoiceVlanOuiRowStatus_Type = RowStatus
_HwL2VlanVoiceVlanOuiRowStatus_Object = MibTableColumn
hwL2VlanVoiceVlanOuiRowStatus = _HwL2VlanVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 26, 1, 4),
    _HwL2VlanVoiceVlanOuiRowStatus_Type()
)
hwL2VlanVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanOuiRowStatus.setStatus("current")
_HwL2VlanMappingMultiTable_Object = MibTable
hwL2VlanMappingMultiTable = _HwL2VlanMappingMultiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27)
)
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiTable.setStatus("current")
_HwL2VlanMappingMultiEntry_Object = MibTableRow
hwL2VlanMappingMultiEntry = _HwL2VlanMappingMultiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1)
)
hwL2VlanMappingMultiEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiDirection"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiVlan8021p"),
)
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiEntry.setStatus("current")


class _HwL2VlanMappingMultiPortIndex_Type(Integer32):
    """Custom type hwL2VlanMappingMultiPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanMappingMultiPortIndex_Type.__name__ = "Integer32"
_HwL2VlanMappingMultiPortIndex_Object = MibTableColumn
hwL2VlanMappingMultiPortIndex = _HwL2VlanMappingMultiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 1),
    _HwL2VlanMappingMultiPortIndex_Type()
)
hwL2VlanMappingMultiPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiPortIndex.setStatus("current")


class _HwL2VlanMappingMultiDirection_Type(Integer32):
    """Custom type hwL2VlanMappingMultiDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HwL2VlanMappingMultiDirection_Type.__name__ = "Integer32"
_HwL2VlanMappingMultiDirection_Object = MibTableColumn
hwL2VlanMappingMultiDirection = _HwL2VlanMappingMultiDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 2),
    _HwL2VlanMappingMultiDirection_Type()
)
hwL2VlanMappingMultiDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiDirection.setStatus("current")
_HwL2VlanMappingMultiVlanId_Type = VlanId
_HwL2VlanMappingMultiVlanId_Object = MibTableColumn
hwL2VlanMappingMultiVlanId = _HwL2VlanMappingMultiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 3),
    _HwL2VlanMappingMultiVlanId_Type()
)
hwL2VlanMappingMultiVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiVlanId.setStatus("current")


class _HwL2VlanMappingMultiVlan8021p_Type(Integer32):
    """Custom type hwL2VlanMappingMultiVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanMappingMultiVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanMappingMultiVlan8021p_Object = MibTableColumn
hwL2VlanMappingMultiVlan8021p = _HwL2VlanMappingMultiVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 4),
    _HwL2VlanMappingMultiVlan8021p_Type()
)
hwL2VlanMappingMultiVlan8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiVlan8021p.setStatus("current")


class _HwL2VlanMappingMultiVlanListLow_Type(OctetString):
    """Custom type hwL2VlanMappingMultiVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingMultiVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanMappingMultiVlanListLow_Object = MibTableColumn
hwL2VlanMappingMultiVlanListLow = _HwL2VlanMappingMultiVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 5),
    _HwL2VlanMappingMultiVlanListLow_Type()
)
hwL2VlanMappingMultiVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiVlanListLow.setStatus("current")


class _HwL2VlanMappingMultiVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanMappingMultiVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanMappingMultiVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanMappingMultiVlanListHigh_Object = MibTableColumn
hwL2VlanMappingMultiVlanListHigh = _HwL2VlanMappingMultiVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 6),
    _HwL2VlanMappingMultiVlanListHigh_Type()
)
hwL2VlanMappingMultiVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiVlanListHigh.setStatus("current")
_HwL2VlanMappingMultiRowStatus_Type = RowStatus
_HwL2VlanMappingMultiRowStatus_Object = MibTableColumn
hwL2VlanMappingMultiRowStatus = _HwL2VlanMappingMultiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 27, 1, 7),
    _HwL2VlanMappingMultiRowStatus_Type()
)
hwL2VlanMappingMultiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiRowStatus.setStatus("current")
_HwL2VlanMacVlanNewTable_Object = MibTable
hwL2VlanMacVlanNewTable = _HwL2VlanMacVlanNewTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28)
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewTable.setStatus("current")
_HwL2VlanMacVlanNewEntry_Object = MibTableRow
hwL2VlanMacVlanNewEntry = _HwL2VlanMacVlanNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28, 1)
)
hwL2VlanMacVlanNewEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanNewMac"),
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewEntry.setStatus("current")
_HwL2VlanMacVlanNewMac_Type = MacAddress
_HwL2VlanMacVlanNewMac_Object = MibTableColumn
hwL2VlanMacVlanNewMac = _HwL2VlanMacVlanNewMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28, 1, 1),
    _HwL2VlanMacVlanNewMac_Type()
)
hwL2VlanMacVlanNewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewMac.setStatus("current")
_HwL2VlanMacVlanNewVlanId_Type = VlanId
_HwL2VlanMacVlanNewVlanId_Object = MibTableColumn
hwL2VlanMacVlanNewVlanId = _HwL2VlanMacVlanNewVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28, 1, 2),
    _HwL2VlanMacVlanNewVlanId_Type()
)
hwL2VlanMacVlanNewVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewVlanId.setStatus("current")


class _HwL2VlanMacVlanNewVlanPriority_Type(Integer32):
    """Custom type hwL2VlanMacVlanNewVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanMacVlanNewVlanPriority_Type.__name__ = "Integer32"
_HwL2VlanMacVlanNewVlanPriority_Object = MibTableColumn
hwL2VlanMacVlanNewVlanPriority = _HwL2VlanMacVlanNewVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28, 1, 3),
    _HwL2VlanMacVlanNewVlanPriority_Type()
)
hwL2VlanMacVlanNewVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewVlanPriority.setStatus("current")
_HwL2VlanMacVlanNewMacRowStatus_Type = RowStatus
_HwL2VlanMacVlanNewMacRowStatus_Object = MibTableColumn
hwL2VlanMacVlanNewMacRowStatus = _HwL2VlanMacVlanNewMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 28, 1, 4),
    _HwL2VlanMacVlanNewMacRowStatus_Type()
)
hwL2VlanMacVlanNewMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewMacRowStatus.setStatus("current")
_HwL2VlanProtocolVlanNewTable_Object = MibTable
hwL2VlanProtocolVlanNewTable = _HwL2VlanProtocolVlanNewTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29)
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewTable.setStatus("current")
_HwL2VlanProtocolVlanNewEntry_Object = MibTableRow
hwL2VlanProtocolVlanNewEntry = _HwL2VlanProtocolVlanNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1)
)
hwL2VlanProtocolVlanNewEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanNewVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanNewProtocolIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewEntry.setStatus("current")
_HwL2VlanProtocolVlanNewVlanId_Type = VlanId
_HwL2VlanProtocolVlanNewVlanId_Object = MibTableColumn
hwL2VlanProtocolVlanNewVlanId = _HwL2VlanProtocolVlanNewVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1, 1),
    _HwL2VlanProtocolVlanNewVlanId_Type()
)
hwL2VlanProtocolVlanNewVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewVlanId.setStatus("current")


class _HwL2VlanProtocolVlanNewProtocolIndex_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanNewProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwL2VlanProtocolVlanNewProtocolIndex_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanNewProtocolIndex_Object = MibTableColumn
hwL2VlanProtocolVlanNewProtocolIndex = _HwL2VlanProtocolVlanNewProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1, 2),
    _HwL2VlanProtocolVlanNewProtocolIndex_Type()
)
hwL2VlanProtocolVlanNewProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewProtocolIndex.setStatus("current")


class _HwL2VlanProtocolVlanNewProtocolType_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanNewProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("at", 1),
          ("ipv4", 2),
          ("ipv6", 3),
          ("ipxEthernetii", 4),
          ("ipxLlc", 5),
          ("ipxRaw", 6),
          ("ipxSnap", 7),
          ("modeEthernetii", 8),
          ("modeLlc", 9),
          ("modeSnap", 10))
    )


_HwL2VlanProtocolVlanNewProtocolType_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanNewProtocolType_Object = MibTableColumn
hwL2VlanProtocolVlanNewProtocolType = _HwL2VlanProtocolVlanNewProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1, 3),
    _HwL2VlanProtocolVlanNewProtocolType_Type()
)
hwL2VlanProtocolVlanNewProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewProtocolType.setStatus("current")


class _HwL2VlanProtocolVlanNewProtocolTypeValue_Type(OctetString):
    """Custom type hwL2VlanProtocolVlanNewProtocolTypeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwL2VlanProtocolVlanNewProtocolTypeValue_Type.__name__ = "OctetString"
_HwL2VlanProtocolVlanNewProtocolTypeValue_Object = MibTableColumn
hwL2VlanProtocolVlanNewProtocolTypeValue = _HwL2VlanProtocolVlanNewProtocolTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1, 4),
    _HwL2VlanProtocolVlanNewProtocolTypeValue_Type()
)
hwL2VlanProtocolVlanNewProtocolTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewProtocolTypeValue.setStatus("current")
_HwL2VlanProtocolVlanNewRowStatus_Type = RowStatus
_HwL2VlanProtocolVlanNewRowStatus_Object = MibTableColumn
hwL2VlanProtocolVlanNewRowStatus = _HwL2VlanProtocolVlanNewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 29, 1, 5),
    _HwL2VlanProtocolVlanNewRowStatus_Type()
)
hwL2VlanProtocolVlanNewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewRowStatus.setStatus("current")
_HwL2VlanPolicyVlanNewTable_Object = MibTable
hwL2VlanPolicyVlanNewTable = _HwL2VlanPolicyVlanNewTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30)
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewTable.setStatus("current")
_HwL2VlanPolicyVlanNewEntry_Object = MibTableRow
hwL2VlanPolicyVlanNewEntry = _HwL2VlanPolicyVlanNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1)
)
hwL2VlanPolicyVlanNewEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewMac"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewIp"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewPort"),
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewEntry.setStatus("current")
_HwL2VlanPolicyVlanNewMac_Type = MacAddress
_HwL2VlanPolicyVlanNewMac_Object = MibTableColumn
hwL2VlanPolicyVlanNewMac = _HwL2VlanPolicyVlanNewMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 1),
    _HwL2VlanPolicyVlanNewMac_Type()
)
hwL2VlanPolicyVlanNewMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewMac.setStatus("current")
_HwL2VlanPolicyVlanNewIp_Type = IpAddress
_HwL2VlanPolicyVlanNewIp_Object = MibTableColumn
hwL2VlanPolicyVlanNewIp = _HwL2VlanPolicyVlanNewIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 2),
    _HwL2VlanPolicyVlanNewIp_Type()
)
hwL2VlanPolicyVlanNewIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewIp.setStatus("current")
_HwL2VlanPolicyVlanNewPort_Type = Integer32
_HwL2VlanPolicyVlanNewPort_Object = MibTableColumn
hwL2VlanPolicyVlanNewPort = _HwL2VlanPolicyVlanNewPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 3),
    _HwL2VlanPolicyVlanNewPort_Type()
)
hwL2VlanPolicyVlanNewPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewPort.setStatus("current")
_HwL2VlanPolicyVlanNewVlanId_Type = VlanId
_HwL2VlanPolicyVlanNewVlanId_Object = MibTableColumn
hwL2VlanPolicyVlanNewVlanId = _HwL2VlanPolicyVlanNewVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 4),
    _HwL2VlanPolicyVlanNewVlanId_Type()
)
hwL2VlanPolicyVlanNewVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewVlanId.setStatus("current")


class _HwL2VlanPolicyVlanNewVlanPriority_Type(Integer32):
    """Custom type hwL2VlanPolicyVlanNewVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanPolicyVlanNewVlanPriority_Type.__name__ = "Integer32"
_HwL2VlanPolicyVlanNewVlanPriority_Object = MibTableColumn
hwL2VlanPolicyVlanNewVlanPriority = _HwL2VlanPolicyVlanNewVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 5),
    _HwL2VlanPolicyVlanNewVlanPriority_Type()
)
hwL2VlanPolicyVlanNewVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewVlanPriority.setStatus("current")
_HwL2VlanPolicyVlanNewRowStatus_Type = RowStatus
_HwL2VlanPolicyVlanNewRowStatus_Object = MibTableColumn
hwL2VlanPolicyVlanNewRowStatus = _HwL2VlanPolicyVlanNewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 30, 1, 6),
    _HwL2VlanPolicyVlanNewRowStatus_Type()
)
hwL2VlanPolicyVlanNewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewRowStatus.setStatus("current")
_HwL2VlanProtocolVlanPortNewTable_Object = MibTable
hwL2VlanProtocolVlanPortNewTable = _HwL2VlanProtocolVlanPortNewTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31)
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewTable.setStatus("current")
_HwL2VlanProtocolVlanPortNewEntry_Object = MibTableRow
hwL2VlanProtocolVlanPortNewEntry = _HwL2VlanProtocolVlanPortNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1)
)
hwL2VlanProtocolVlanPortNewEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanPortNewIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanPortNewVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanPortNewProtocolIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewEntry.setStatus("current")


class _HwL2VlanProtocolVlanPortNewIndex_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanPortNewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2VlanProtocolVlanPortNewIndex_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanPortNewIndex_Object = MibTableColumn
hwL2VlanProtocolVlanPortNewIndex = _HwL2VlanProtocolVlanPortNewIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1, 1),
    _HwL2VlanProtocolVlanPortNewIndex_Type()
)
hwL2VlanProtocolVlanPortNewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewIndex.setStatus("current")
_HwL2VlanProtocolVlanPortNewVlanId_Type = VlanId
_HwL2VlanProtocolVlanPortNewVlanId_Object = MibTableColumn
hwL2VlanProtocolVlanPortNewVlanId = _HwL2VlanProtocolVlanPortNewVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1, 2),
    _HwL2VlanProtocolVlanPortNewVlanId_Type()
)
hwL2VlanProtocolVlanPortNewVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewVlanId.setStatus("current")


class _HwL2VlanProtocolVlanPortNewProtocolIndex_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanPortNewProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwL2VlanProtocolVlanPortNewProtocolIndex_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanPortNewProtocolIndex_Object = MibTableColumn
hwL2VlanProtocolVlanPortNewProtocolIndex = _HwL2VlanProtocolVlanPortNewProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1, 3),
    _HwL2VlanProtocolVlanPortNewProtocolIndex_Type()
)
hwL2VlanProtocolVlanPortNewProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewProtocolIndex.setStatus("current")


class _HwL2VlanProtocolVlanPortNewPriority_Type(Integer32):
    """Custom type hwL2VlanProtocolVlanPortNewPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanProtocolVlanPortNewPriority_Type.__name__ = "Integer32"
_HwL2VlanProtocolVlanPortNewPriority_Object = MibTableColumn
hwL2VlanProtocolVlanPortNewPriority = _HwL2VlanProtocolVlanPortNewPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1, 4),
    _HwL2VlanProtocolVlanPortNewPriority_Type()
)
hwL2VlanProtocolVlanPortNewPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewPriority.setStatus("current")
_HwL2VlanProtocolVlanPortNewRowStatus_Type = RowStatus
_HwL2VlanProtocolVlanPortNewRowStatus_Object = MibTableColumn
hwL2VlanProtocolVlanPortNewRowStatus = _HwL2VlanProtocolVlanPortNewRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 31, 1, 5),
    _HwL2VlanProtocolVlanPortNewRowStatus_Type()
)
hwL2VlanProtocolVlanPortNewRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewRowStatus.setStatus("current")
_HwL2VlanMultiVoiceVlanPortTable_Object = MibTable
hwL2VlanMultiVoiceVlanPortTable = _HwL2VlanMultiVoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 32)
)
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanPortTable.setStatus("current")
_HwL2VlanMultiVoiceVlanPortEntry_Object = MibTableRow
hwL2VlanMultiVoiceVlanPortEntry = _HwL2VlanMultiVoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 32, 1)
)
hwL2VlanMultiVoiceVlanPortEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanMultiVoiceVlanIfIndex"),
)
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanPortEntry.setStatus("current")
_HwL2VlanMultiVoiceVlanIfIndex_Type = InterfaceIndex
_HwL2VlanMultiVoiceVlanIfIndex_Object = MibTableColumn
hwL2VlanMultiVoiceVlanIfIndex = _HwL2VlanMultiVoiceVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 32, 1, 1),
    _HwL2VlanMultiVoiceVlanIfIndex_Type()
)
hwL2VlanMultiVoiceVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanIfIndex.setStatus("current")
_HwL2VlanMultiVoiceVlanPortVLanId_Type = VlanId
_HwL2VlanMultiVoiceVlanPortVLanId_Object = MibTableColumn
hwL2VlanMultiVoiceVlanPortVLanId = _HwL2VlanMultiVoiceVlanPortVLanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 32, 1, 2),
    _HwL2VlanMultiVoiceVlanPortVLanId_Type()
)
hwL2VlanMultiVoiceVlanPortVLanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanPortVLanId.setStatus("current")
_HwL2VlanMultiVoiceVlanPortRowStatus_Type = RowStatus
_HwL2VlanMultiVoiceVlanPortRowStatus_Object = MibTableColumn
hwL2VlanMultiVoiceVlanPortRowStatus = _HwL2VlanMultiVoiceVlanPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 32, 1, 51),
    _HwL2VlanMultiVoiceVlanPortRowStatus_Type()
)
hwL2VlanMultiVoiceVlanPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanPortRowStatus.setStatus("current")
_HwL2VlanSwitchExtTable_Object = MibTable
hwL2VlanSwitchExtTable = _HwL2VlanSwitchExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33)
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtTable.setStatus("current")
_HwL2VlanSwitchExtEntry_Object = MibTableRow
hwL2VlanSwitchExtEntry = _HwL2VlanSwitchExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1)
)
hwL2VlanSwitchExtEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtName"),
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtEntry.setStatus("current")


class _HwL2VlanSwitchExtName_Type(OctetString):
    """Custom type hwL2VlanSwitchExtName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwL2VlanSwitchExtName_Type.__name__ = "OctetString"
_HwL2VlanSwitchExtName_Object = MibTableColumn
hwL2VlanSwitchExtName = _HwL2VlanSwitchExtName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 1),
    _HwL2VlanSwitchExtName_Type()
)
hwL2VlanSwitchExtName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtName.setStatus("current")
_HwL2VlanSwitchExtSrcIfIndex_Type = InterfaceIndex
_HwL2VlanSwitchExtSrcIfIndex_Object = MibTableColumn
hwL2VlanSwitchExtSrcIfIndex = _HwL2VlanSwitchExtSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 2),
    _HwL2VlanSwitchExtSrcIfIndex_Type()
)
hwL2VlanSwitchExtSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtSrcIfIndex.setStatus("current")


class _HwL2VlanSwitchExtOuterVlanId_Type(Integer32):
    """Custom type hwL2VlanSwitchExtOuterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwL2VlanSwitchExtOuterVlanId_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtOuterVlanId_Object = MibTableColumn
hwL2VlanSwitchExtOuterVlanId = _HwL2VlanSwitchExtOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 3),
    _HwL2VlanSwitchExtOuterVlanId_Type()
)
hwL2VlanSwitchExtOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtOuterVlanId.setStatus("current")


class _HwL2VlanSwitchExtVlanListLow_Type(OctetString):
    """Custom type hwL2VlanSwitchExtVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanSwitchExtVlanListLow_Type.__name__ = "OctetString"
_HwL2VlanSwitchExtVlanListLow_Object = MibTableColumn
hwL2VlanSwitchExtVlanListLow = _HwL2VlanSwitchExtVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 4),
    _HwL2VlanSwitchExtVlanListLow_Type()
)
hwL2VlanSwitchExtVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtVlanListLow.setStatus("current")


class _HwL2VlanSwitchExtVlanListHigh_Type(OctetString):
    """Custom type hwL2VlanSwitchExtVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2VlanSwitchExtVlanListHigh_Type.__name__ = "OctetString"
_HwL2VlanSwitchExtVlanListHigh_Object = MibTableColumn
hwL2VlanSwitchExtVlanListHigh = _HwL2VlanSwitchExtVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 5),
    _HwL2VlanSwitchExtVlanListHigh_Type()
)
hwL2VlanSwitchExtVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtVlanListHigh.setStatus("current")
_HwL2VlanSwitchExtDstIfIndex_Type = InterfaceIndex
_HwL2VlanSwitchExtDstIfIndex_Object = MibTableColumn
hwL2VlanSwitchExtDstIfIndex = _HwL2VlanSwitchExtDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 6),
    _HwL2VlanSwitchExtDstIfIndex_Type()
)
hwL2VlanSwitchExtDstIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtDstIfIndex.setStatus("current")


class _HwL2VlanSwitchExtVlanXlateAction_Type(Integer32):
    """Custom type hwL2VlanSwitchExtVlanXlateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("push", 3),
          ("switch", 2),
          ("unchange", 1))
    )


_HwL2VlanSwitchExtVlanXlateAction_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtVlanXlateAction_Object = MibTableColumn
hwL2VlanSwitchExtVlanXlateAction = _HwL2VlanSwitchExtVlanXlateAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 7),
    _HwL2VlanSwitchExtVlanXlateAction_Type()
)
hwL2VlanSwitchExtVlanXlateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtVlanXlateAction.setStatus("current")


class _HwL2VlanSwitchExtDstVlan_Type(Integer32):
    """Custom type hwL2VlanSwitchExtDstVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwL2VlanSwitchExtDstVlan_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtDstVlan_Object = MibTableColumn
hwL2VlanSwitchExtDstVlan = _HwL2VlanSwitchExtDstVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 8),
    _HwL2VlanSwitchExtDstVlan_Type()
)
hwL2VlanSwitchExtDstVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtDstVlan.setStatus("current")


class _HwL2VlanSwitchExtDstInnerVlan_Type(Integer32):
    """Custom type hwL2VlanSwitchExtDstInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwL2VlanSwitchExtDstInnerVlan_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtDstInnerVlan_Object = MibTableColumn
hwL2VlanSwitchExtDstInnerVlan = _HwL2VlanSwitchExtDstInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 9),
    _HwL2VlanSwitchExtDstInnerVlan_Type()
)
hwL2VlanSwitchExtDstInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtDstInnerVlan.setStatus("current")


class _HwL2VlanSwitchExtRemark_Type(Integer32):
    """Custom type hwL2VlanSwitchExtRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanSwitchExtRemark_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtRemark_Object = MibTableColumn
hwL2VlanSwitchExtRemark = _HwL2VlanSwitchExtRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 10),
    _HwL2VlanSwitchExtRemark_Type()
)
hwL2VlanSwitchExtRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtRemark.setStatus("current")


class _HwL2VlanSwitchExtRemarkReverse_Type(Integer32):
    """Custom type hwL2VlanSwitchExtRemarkReverse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2VlanSwitchExtRemarkReverse_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtRemarkReverse_Object = MibTableColumn
hwL2VlanSwitchExtRemarkReverse = _HwL2VlanSwitchExtRemarkReverse_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 11),
    _HwL2VlanSwitchExtRemarkReverse_Type()
)
hwL2VlanSwitchExtRemarkReverse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtRemarkReverse.setStatus("current")


class _HwL2VlanSwitchExtLinkStatus_Type(Integer32):
    """Custom type hwL2VlanSwitchExtLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwL2VlanSwitchExtLinkStatus_Type.__name__ = "Integer32"
_HwL2VlanSwitchExtLinkStatus_Object = MibTableColumn
hwL2VlanSwitchExtLinkStatus = _HwL2VlanSwitchExtLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 12),
    _HwL2VlanSwitchExtLinkStatus_Type()
)
hwL2VlanSwitchExtLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtLinkStatus.setStatus("current")
_HwL2VlanSwitchExtRowStatus_Type = RowStatus
_HwL2VlanSwitchExtRowStatus_Object = MibTableColumn
hwL2VlanSwitchExtRowStatus = _HwL2VlanSwitchExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 33, 1, 51),
    _HwL2VlanSwitchExtRowStatus_Type()
)
hwL2VlanSwitchExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtRowStatus.setStatus("current")


class _HwL2VlanPrecedence_Type(Integer32):
    """Custom type hwL2VlanPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipsubnetvlan", 2),
          ("macvlan", 1))
    )


_HwL2VlanPrecedence_Type.__name__ = "Integer32"
_HwL2VlanPrecedence_Object = MibScalar
hwL2VlanPrecedence = _HwL2VlanPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 34),
    _HwL2VlanPrecedence_Type()
)
hwL2VlanPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanPrecedence.setStatus("current")
_HwL2VlanXlateTable_Object = MibTable
hwL2VlanXlateTable = _HwL2VlanXlateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35)
)
if mibBuilder.loadTexts:
    hwL2VlanXlateTable.setStatus("current")
_HwL2VlanXlateEntry_Object = MibTableRow
hwL2VlanXlateEntry = _HwL2VlanXlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1)
)
hwL2VlanXlateEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanXlateInterfaceIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanXlateVlanIdBegin"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanXlateOuterVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanXlateVlan8021p"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanXlateDirection"),
)
if mibBuilder.loadTexts:
    hwL2VlanXlateEntry.setStatus("current")
_HwL2VlanXlateInterfaceIndex_Type = InterfaceIndex
_HwL2VlanXlateInterfaceIndex_Object = MibTableColumn
hwL2VlanXlateInterfaceIndex = _HwL2VlanXlateInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 1),
    _HwL2VlanXlateInterfaceIndex_Type()
)
hwL2VlanXlateInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanXlateInterfaceIndex.setStatus("current")
_HwL2VlanXlateVlanIdBegin_Type = VlanId
_HwL2VlanXlateVlanIdBegin_Object = MibTableColumn
hwL2VlanXlateVlanIdBegin = _HwL2VlanXlateVlanIdBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 2),
    _HwL2VlanXlateVlanIdBegin_Type()
)
hwL2VlanXlateVlanIdBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanXlateVlanIdBegin.setStatus("current")
_HwL2VlanXlateVlanIdEnd_Type = VlanIdOrNone
_HwL2VlanXlateVlanIdEnd_Object = MibTableColumn
hwL2VlanXlateVlanIdEnd = _HwL2VlanXlateVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 3),
    _HwL2VlanXlateVlanIdEnd_Type()
)
hwL2VlanXlateVlanIdEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateVlanIdEnd.setStatus("current")
_HwL2VlanXlateOuterVlanId_Type = VlanIdOrNone
_HwL2VlanXlateOuterVlanId_Object = MibTableColumn
hwL2VlanXlateOuterVlanId = _HwL2VlanXlateOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 4),
    _HwL2VlanXlateOuterVlanId_Type()
)
hwL2VlanXlateOuterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanXlateOuterVlanId.setStatus("current")


class _HwL2VlanXlateVlan8021p_Type(Integer32):
    """Custom type hwL2VlanXlateVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
        ValueRangeConstraint(65535, 65535),
    )


_HwL2VlanXlateVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanXlateVlan8021p_Object = MibTableColumn
hwL2VlanXlateVlan8021p = _HwL2VlanXlateVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 5),
    _HwL2VlanXlateVlan8021p_Type()
)
hwL2VlanXlateVlan8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanXlateVlan8021p.setStatus("current")


class _HwL2VlanXlateDirection_Type(Integer32):
    """Custom type hwL2VlanXlateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_HwL2VlanXlateDirection_Type.__name__ = "Integer32"
_HwL2VlanXlateDirection_Object = MibTableColumn
hwL2VlanXlateDirection = _HwL2VlanXlateDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 6),
    _HwL2VlanXlateDirection_Type()
)
hwL2VlanXlateDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanXlateDirection.setStatus("current")


class _HwL2VlanXlateAction_Type(Integer32):
    """Custom type hwL2VlanXlateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("pop", 3),
          ("stack", 2))
    )


_HwL2VlanXlateAction_Type.__name__ = "Integer32"
_HwL2VlanXlateAction_Object = MibTableColumn
hwL2VlanXlateAction = _HwL2VlanXlateAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 7),
    _HwL2VlanXlateAction_Type()
)
hwL2VlanXlateAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateAction.setStatus("current")
_HwL2VlanXlateToVlanId_Type = VlanIdOrNone
_HwL2VlanXlateToVlanId_Object = MibTableColumn
hwL2VlanXlateToVlanId = _HwL2VlanXlateToVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 8),
    _HwL2VlanXlateToVlanId_Type()
)
hwL2VlanXlateToVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateToVlanId.setStatus("current")
_HwL2VlanXlateToinnerVlanId_Type = VlanIdOrNone
_HwL2VlanXlateToinnerVlanId_Object = MibTableColumn
hwL2VlanXlateToinnerVlanId = _HwL2VlanXlateToinnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 9),
    _HwL2VlanXlateToinnerVlanId_Type()
)
hwL2VlanXlateToinnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateToinnerVlanId.setStatus("current")
_HwL2VlanXlateremark_Type = Integer32
_HwL2VlanXlateremark_Object = MibTableColumn
hwL2VlanXlateremark = _HwL2VlanXlateremark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 10),
    _HwL2VlanXlateremark_Type()
)
hwL2VlanXlateremark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateremark.setStatus("current")
_HwL2VlanXlateRowStatus_Type = RowStatus
_HwL2VlanXlateRowStatus_Object = MibTableColumn
hwL2VlanXlateRowStatus = _HwL2VlanXlateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 35, 1, 51),
    _HwL2VlanXlateRowStatus_Type()
)
hwL2VlanXlateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2VlanXlateRowStatus.setStatus("current")
_HwL2QinQVlanTable_Object = MibTable
hwL2QinQVlanTable = _HwL2QinQVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36)
)
if mibBuilder.loadTexts:
    hwL2QinQVlanTable.setStatus("current")
_HwL2QinQVlanEntry_Object = MibTableRow
hwL2QinQVlanEntry = _HwL2QinQVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1)
)
hwL2QinQVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanIfIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanIdBegin"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanIdEnd"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanInnerVlanIdBegin"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanInnerVlanIdEnd"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlan8021pBegin"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlan8021pEnd"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2QinQVlanEtherType"),
)
if mibBuilder.loadTexts:
    hwL2QinQVlanEntry.setStatus("current")
_HwL2QinQVlanIfIndex_Type = InterfaceIndex
_HwL2QinQVlanIfIndex_Object = MibTableColumn
hwL2QinQVlanIfIndex = _HwL2QinQVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 1),
    _HwL2QinQVlanIfIndex_Type()
)
hwL2QinQVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanIfIndex.setStatus("current")
_HwL2QinQVlanIdBegin_Type = VlanId
_HwL2QinQVlanIdBegin_Object = MibTableColumn
hwL2QinQVlanIdBegin = _HwL2QinQVlanIdBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 2),
    _HwL2QinQVlanIdBegin_Type()
)
hwL2QinQVlanIdBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanIdBegin.setStatus("current")
_HwL2QinQVlanIdEnd_Type = VlanId
_HwL2QinQVlanIdEnd_Object = MibTableColumn
hwL2QinQVlanIdEnd = _HwL2QinQVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 3),
    _HwL2QinQVlanIdEnd_Type()
)
hwL2QinQVlanIdEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanIdEnd.setStatus("current")
_HwL2QinQVlanInnerVlanIdBegin_Type = VlanIdOrNone
_HwL2QinQVlanInnerVlanIdBegin_Object = MibTableColumn
hwL2QinQVlanInnerVlanIdBegin = _HwL2QinQVlanInnerVlanIdBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 4),
    _HwL2QinQVlanInnerVlanIdBegin_Type()
)
hwL2QinQVlanInnerVlanIdBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanInnerVlanIdBegin.setStatus("current")
_HwL2QinQVlanInnerVlanIdEnd_Type = VlanIdOrNone
_HwL2QinQVlanInnerVlanIdEnd_Object = MibTableColumn
hwL2QinQVlanInnerVlanIdEnd = _HwL2QinQVlanInnerVlanIdEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 5),
    _HwL2QinQVlanInnerVlanIdEnd_Type()
)
hwL2QinQVlanInnerVlanIdEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanInnerVlanIdEnd.setStatus("current")


class _HwL2QinQVlan8021pBegin_Type(Integer32):
    """Custom type hwL2QinQVlan8021pBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2QinQVlan8021pBegin_Type.__name__ = "Integer32"
_HwL2QinQVlan8021pBegin_Object = MibTableColumn
hwL2QinQVlan8021pBegin = _HwL2QinQVlan8021pBegin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 6),
    _HwL2QinQVlan8021pBegin_Type()
)
hwL2QinQVlan8021pBegin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlan8021pBegin.setStatus("current")


class _HwL2QinQVlan8021pEnd_Type(Integer32):
    """Custom type hwL2QinQVlan8021pEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2QinQVlan8021pEnd_Type.__name__ = "Integer32"
_HwL2QinQVlan8021pEnd_Object = MibTableColumn
hwL2QinQVlan8021pEnd = _HwL2QinQVlan8021pEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 7),
    _HwL2QinQVlan8021pEnd_Type()
)
hwL2QinQVlan8021pEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlan8021pEnd.setStatus("current")


class _HwL2QinQVlanEtherType_Type(Integer32):
    """Custom type hwL2QinQVlanEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwL2QinQVlanEtherType_Type.__name__ = "Integer32"
_HwL2QinQVlanEtherType_Object = MibTableColumn
hwL2QinQVlanEtherType = _HwL2QinQVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 8),
    _HwL2QinQVlanEtherType_Type()
)
hwL2QinQVlanEtherType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2QinQVlanEtherType.setStatus("current")


class _HwL2QinQVlanMode_Type(Integer32):
    """Custom type hwL2QinQVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cosmapping", 4),
          ("cosstacking", 3),
          ("mapping", 2),
          ("mapping2to1", 5),
          ("mapping2to2", 6),
          ("stacking", 1))
    )


_HwL2QinQVlanMode_Type.__name__ = "Integer32"
_HwL2QinQVlanMode_Object = MibTableColumn
hwL2QinQVlanMode = _HwL2QinQVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 9),
    _HwL2QinQVlanMode_Type()
)
hwL2QinQVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanMode.setStatus("current")
_HwL2QinQVlanChangedVlanId_Type = VlanId
_HwL2QinQVlanChangedVlanId_Object = MibTableColumn
hwL2QinQVlanChangedVlanId = _HwL2QinQVlanChangedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 10),
    _HwL2QinQVlanChangedVlanId_Type()
)
hwL2QinQVlanChangedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanChangedVlanId.setStatus("current")
_HwL2QinQVlanChangedInnerVlanId_Type = VlanIdOrNone
_HwL2QinQVlanChangedInnerVlanId_Object = MibTableColumn
hwL2QinQVlanChangedInnerVlanId = _HwL2QinQVlanChangedInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 11),
    _HwL2QinQVlanChangedInnerVlanId_Type()
)
hwL2QinQVlanChangedInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanChangedInnerVlanId.setStatus("current")


class _HwL2QinQVlanRemark_Type(Integer32):
    """Custom type hwL2QinQVlanRemark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwL2QinQVlanRemark_Type.__name__ = "Integer32"
_HwL2QinQVlanRemark_Object = MibTableColumn
hwL2QinQVlanRemark = _HwL2QinQVlanRemark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 12),
    _HwL2QinQVlanRemark_Type()
)
hwL2QinQVlanRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanRemark.setStatus("current")
_HwL2QinQVlanMapStackVlanId_Type = VlanIdOrNone
_HwL2QinQVlanMapStackVlanId_Object = MibTableColumn
hwL2QinQVlanMapStackVlanId = _HwL2QinQVlanMapStackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 13),
    _HwL2QinQVlanMapStackVlanId_Type()
)
hwL2QinQVlanMapStackVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanMapStackVlanId.setStatus("current")
_HwL2QinQVlanRowStatus_Type = RowStatus
_HwL2QinQVlanRowStatus_Object = MibTableColumn
hwL2QinQVlanRowStatus = _HwL2QinQVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 36, 1, 14),
    _HwL2QinQVlanRowStatus_Type()
)
hwL2QinQVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2QinQVlanRowStatus.setStatus("current")
_HwL2UntagAddDTagTable_Object = MibTable
hwL2UntagAddDTagTable = _HwL2UntagAddDTagTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37)
)
if mibBuilder.loadTexts:
    hwL2UntagAddDTagTable.setStatus("current")
_HwL2UntagAddDTagEntry_Object = MibTableRow
hwL2UntagAddDTagEntry = _HwL2UntagAddDTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37, 1)
)
hwL2UntagAddDTagEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2UntagAddDTagPortIndex"),
)
if mibBuilder.loadTexts:
    hwL2UntagAddDTagEntry.setStatus("current")
_HwL2UntagAddDTagPortIndex_Type = Integer32
_HwL2UntagAddDTagPortIndex_Object = MibTableColumn
hwL2UntagAddDTagPortIndex = _HwL2UntagAddDTagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37, 1, 1),
    _HwL2UntagAddDTagPortIndex_Type()
)
hwL2UntagAddDTagPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2UntagAddDTagPortIndex.setStatus("current")
_HwL2UntagAddDTagOuterVlanId_Type = VlanId
_HwL2UntagAddDTagOuterVlanId_Object = MibTableColumn
hwL2UntagAddDTagOuterVlanId = _HwL2UntagAddDTagOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37, 1, 2),
    _HwL2UntagAddDTagOuterVlanId_Type()
)
hwL2UntagAddDTagOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2UntagAddDTagOuterVlanId.setStatus("current")
_HwL2UntagAddDTagInnerVlanId_Type = VlanId
_HwL2UntagAddDTagInnerVlanId_Object = MibTableColumn
hwL2UntagAddDTagInnerVlanId = _HwL2UntagAddDTagInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37, 1, 3),
    _HwL2UntagAddDTagInnerVlanId_Type()
)
hwL2UntagAddDTagInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2UntagAddDTagInnerVlanId.setStatus("current")
_HwL2UntagAddDTagRowStatus_Type = RowStatus
_HwL2UntagAddDTagRowStatus_Object = MibTableColumn
hwL2UntagAddDTagRowStatus = _HwL2UntagAddDTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 37, 1, 4),
    _HwL2UntagAddDTagRowStatus_Type()
)
hwL2UntagAddDTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2UntagAddDTagRowStatus.setStatus("current")


class _HwL2VlanVoiceVlan8021p_Type(Integer32):
    """Custom type hwL2VlanVoiceVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2VlanVoiceVlan8021p_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlan8021p_Object = MibScalar
hwL2VlanVoiceVlan8021p = _HwL2VlanVoiceVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 38),
    _HwL2VlanVoiceVlan8021p_Type()
)
hwL2VlanVoiceVlan8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlan8021p.setStatus("current")


class _HwL2VlanVoiceVlanDscp_Type(Integer32):
    """Custom type hwL2VlanVoiceVlanDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwL2VlanVoiceVlanDscp_Type.__name__ = "Integer32"
_HwL2VlanVoiceVlanDscp_Object = MibScalar
hwL2VlanVoiceVlanDscp = _HwL2VlanVoiceVlanDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 2, 39),
    _HwL2VlanVoiceVlanDscp_Type()
)
hwL2VlanVoiceVlanDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanDscp.setStatus("current")
_HwL2VlanStatistics_ObjectIdentity = ObjectIdentity
hwL2VlanStatistics = _HwL2VlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3)
)
_HwL2IfStatVlanCfgTable_Object = MibTable
hwL2IfStatVlanCfgTable = _HwL2IfStatVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgTable.setStatus("current")
_HwL2IfStatVlanCfgEntry_Object = MibTableRow
hwL2IfStatVlanCfgEntry = _HwL2IfStatVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1, 1)
)
hwL2IfStatVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanCfgPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanCfgVlanId"),
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgEntry.setStatus("current")


class _HwL2IfStatVlanCfgPortIndex_Type(Integer32):
    """Custom type hwL2IfStatVlanCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStatVlanCfgPortIndex_Type.__name__ = "Integer32"
_HwL2IfStatVlanCfgPortIndex_Object = MibTableColumn
hwL2IfStatVlanCfgPortIndex = _HwL2IfStatVlanCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1, 1, 1),
    _HwL2IfStatVlanCfgPortIndex_Type()
)
hwL2IfStatVlanCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgPortIndex.setStatus("current")
_HwL2IfStatVlanCfgVlanId_Type = VlanId
_HwL2IfStatVlanCfgVlanId_Object = MibTableColumn
hwL2IfStatVlanCfgVlanId = _HwL2IfStatVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1, 1, 2),
    _HwL2IfStatVlanCfgVlanId_Type()
)
hwL2IfStatVlanCfgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgVlanId.setStatus("current")
_HwL2IfStatVlanCfgEnableFlag_Type = EnabledStatus
_HwL2IfStatVlanCfgEnableFlag_Object = MibTableColumn
hwL2IfStatVlanCfgEnableFlag = _HwL2IfStatVlanCfgEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1, 1, 11),
    _HwL2IfStatVlanCfgEnableFlag_Type()
)
hwL2IfStatVlanCfgEnableFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgEnableFlag.setStatus("current")
_HwL2IfStatVlanCfgRowStatus_Type = RowStatus
_HwL2IfStatVlanCfgRowStatus_Object = MibTableColumn
hwL2IfStatVlanCfgRowStatus = _HwL2IfStatVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 1, 1, 12),
    _HwL2IfStatVlanCfgRowStatus_Type()
)
hwL2IfStatVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgRowStatus.setStatus("current")
_HwL2IfStat8021pCfgTable_Object = MibTable
hwL2IfStat8021pCfgTable = _HwL2IfStat8021pCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgTable.setStatus("current")
_HwL2IfStat8021pCfgEntry_Object = MibTableRow
hwL2IfStat8021pCfgEntry = _HwL2IfStat8021pCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2, 1)
)
hwL2IfStat8021pCfgEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pCfgPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pCfg8021p"),
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgEntry.setStatus("current")


class _HwL2IfStat8021pCfgPortIndex_Type(Integer32):
    """Custom type hwL2IfStat8021pCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStat8021pCfgPortIndex_Type.__name__ = "Integer32"
_HwL2IfStat8021pCfgPortIndex_Object = MibTableColumn
hwL2IfStat8021pCfgPortIndex = _HwL2IfStat8021pCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2, 1, 1),
    _HwL2IfStat8021pCfgPortIndex_Type()
)
hwL2IfStat8021pCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgPortIndex.setStatus("current")


class _HwL2IfStat8021pCfg8021p_Type(Integer32):
    """Custom type hwL2IfStat8021pCfg8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2IfStat8021pCfg8021p_Type.__name__ = "Integer32"
_HwL2IfStat8021pCfg8021p_Object = MibTableColumn
hwL2IfStat8021pCfg8021p = _HwL2IfStat8021pCfg8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2, 1, 2),
    _HwL2IfStat8021pCfg8021p_Type()
)
hwL2IfStat8021pCfg8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfg8021p.setStatus("current")
_HwL2IfStat8021pCfgEnableFlag_Type = EnabledStatus
_HwL2IfStat8021pCfgEnableFlag_Object = MibTableColumn
hwL2IfStat8021pCfgEnableFlag = _HwL2IfStat8021pCfgEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2, 1, 11),
    _HwL2IfStat8021pCfgEnableFlag_Type()
)
hwL2IfStat8021pCfgEnableFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgEnableFlag.setStatus("current")
_HwL2IfStat8021pCfgRowStatus_Type = RowStatus
_HwL2IfStat8021pCfgRowStatus_Object = MibTableColumn
hwL2IfStat8021pCfgRowStatus = _HwL2IfStat8021pCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 2, 1, 12),
    _HwL2IfStat8021pCfgRowStatus_Type()
)
hwL2IfStat8021pCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgRowStatus.setStatus("current")
_HwL2IfStat8021pAndVlanCfgTable_Object = MibTable
hwL2IfStat8021pAndVlanCfgTable = _HwL2IfStat8021pAndVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgTable.setStatus("current")
_HwL2IfStat8021pAndVlanCfgEntry_Object = MibTableRow
hwL2IfStat8021pAndVlanCfgEntry = _HwL2IfStat8021pAndVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1)
)
hwL2IfStat8021pAndVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanCfgPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanCfgVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanCfg8021p"),
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgEntry.setStatus("current")


class _HwL2IfStat8021pAndVlanCfgPortIndex_Type(Integer32):
    """Custom type hwL2IfStat8021pAndVlanCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStat8021pAndVlanCfgPortIndex_Type.__name__ = "Integer32"
_HwL2IfStat8021pAndVlanCfgPortIndex_Object = MibTableColumn
hwL2IfStat8021pAndVlanCfgPortIndex = _HwL2IfStat8021pAndVlanCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1, 1),
    _HwL2IfStat8021pAndVlanCfgPortIndex_Type()
)
hwL2IfStat8021pAndVlanCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgPortIndex.setStatus("current")
_HwL2IfStat8021pAndVlanCfgVlanId_Type = VlanId
_HwL2IfStat8021pAndVlanCfgVlanId_Object = MibTableColumn
hwL2IfStat8021pAndVlanCfgVlanId = _HwL2IfStat8021pAndVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1, 2),
    _HwL2IfStat8021pAndVlanCfgVlanId_Type()
)
hwL2IfStat8021pAndVlanCfgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgVlanId.setStatus("current")


class _HwL2IfStat8021pAndVlanCfg8021p_Type(Integer32):
    """Custom type hwL2IfStat8021pAndVlanCfg8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2IfStat8021pAndVlanCfg8021p_Type.__name__ = "Integer32"
_HwL2IfStat8021pAndVlanCfg8021p_Object = MibTableColumn
hwL2IfStat8021pAndVlanCfg8021p = _HwL2IfStat8021pAndVlanCfg8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1, 3),
    _HwL2IfStat8021pAndVlanCfg8021p_Type()
)
hwL2IfStat8021pAndVlanCfg8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfg8021p.setStatus("current")
_HwL2IfStat8021pAndVlanCfgEnableFlag_Type = EnabledStatus
_HwL2IfStat8021pAndVlanCfgEnableFlag_Object = MibTableColumn
hwL2IfStat8021pAndVlanCfgEnableFlag = _HwL2IfStat8021pAndVlanCfgEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1, 11),
    _HwL2IfStat8021pAndVlanCfgEnableFlag_Type()
)
hwL2IfStat8021pAndVlanCfgEnableFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgEnableFlag.setStatus("current")
_HwL2IfStat8021pAndVlanCfgRowStatus_Type = RowStatus
_HwL2IfStat8021pAndVlanCfgRowStatus_Object = MibTableColumn
hwL2IfStat8021pAndVlanCfgRowStatus = _HwL2IfStat8021pAndVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 3, 1, 12),
    _HwL2IfStat8021pAndVlanCfgRowStatus_Type()
)
hwL2IfStat8021pAndVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgRowStatus.setStatus("current")
_HwL2VlanStatTable_Object = MibTable
hwL2VlanStatTable = _HwL2VlanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwL2VlanStatTable.setStatus("current")
_HwL2VlanStatEntry_Object = MibTableRow
hwL2VlanStatEntry = _HwL2VlanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1)
)
hwL2VlanStatEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanStatVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanStatEntry.setStatus("current")
_HwL2VlanStatVlanId_Type = VlanId
_HwL2VlanStatVlanId_Object = MibTableColumn
hwL2VlanStatVlanId = _HwL2VlanStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 1),
    _HwL2VlanStatVlanId_Type()
)
hwL2VlanStatVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanStatVlanId.setStatus("current")
_HwL2VlanStatInTotalPkts_Type = Counter64
_HwL2VlanStatInTotalPkts_Object = MibTableColumn
hwL2VlanStatInTotalPkts = _HwL2VlanStatInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 2),
    _HwL2VlanStatInTotalPkts_Type()
)
hwL2VlanStatInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInTotalPkts.setStatus("current")
_HwL2VlanStatInTotalBytes_Type = Counter64
_HwL2VlanStatInTotalBytes_Object = MibTableColumn
hwL2VlanStatInTotalBytes = _HwL2VlanStatInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 3),
    _HwL2VlanStatInTotalBytes_Type()
)
hwL2VlanStatInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInTotalBytes.setStatus("current")
_HwL2VlanStatOutTotalPkts_Type = Counter64
_HwL2VlanStatOutTotalPkts_Object = MibTableColumn
hwL2VlanStatOutTotalPkts = _HwL2VlanStatOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 4),
    _HwL2VlanStatOutTotalPkts_Type()
)
hwL2VlanStatOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutTotalPkts.setStatus("current")
_HwL2VlanStatOutTotalBytes_Type = Counter64
_HwL2VlanStatOutTotalBytes_Object = MibTableColumn
hwL2VlanStatOutTotalBytes = _HwL2VlanStatOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 5),
    _HwL2VlanStatOutTotalBytes_Type()
)
hwL2VlanStatOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutTotalBytes.setStatus("current")
_HwL2VlanStatUnknownUcastDiscardPkts_Type = Counter64
_HwL2VlanStatUnknownUcastDiscardPkts_Object = MibTableColumn
hwL2VlanStatUnknownUcastDiscardPkts = _HwL2VlanStatUnknownUcastDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 6),
    _HwL2VlanStatUnknownUcastDiscardPkts_Type()
)
hwL2VlanStatUnknownUcastDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatUnknownUcastDiscardPkts.setStatus("current")
_HwL2VlanStatUnknownMcastDiscardPkts_Type = Counter64
_HwL2VlanStatUnknownMcastDiscardPkts_Object = MibTableColumn
hwL2VlanStatUnknownMcastDiscardPkts = _HwL2VlanStatUnknownMcastDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 7),
    _HwL2VlanStatUnknownMcastDiscardPkts_Type()
)
hwL2VlanStatUnknownMcastDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatUnknownMcastDiscardPkts.setStatus("current")
_HwL2VlanStatBcastDiscardPkts_Type = Counter64
_HwL2VlanStatBcastDiscardPkts_Object = MibTableColumn
hwL2VlanStatBcastDiscardPkts = _HwL2VlanStatBcastDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 8),
    _HwL2VlanStatBcastDiscardPkts_Type()
)
hwL2VlanStatBcastDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatBcastDiscardPkts.setStatus("current")
_HwL2VlanStatInUcastPkts_Type = Counter64
_HwL2VlanStatInUcastPkts_Object = MibTableColumn
hwL2VlanStatInUcastPkts = _HwL2VlanStatInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 9),
    _HwL2VlanStatInUcastPkts_Type()
)
hwL2VlanStatInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInUcastPkts.setStatus("current")
_HwL2VlanStatInUcastBytes_Type = Counter64
_HwL2VlanStatInUcastBytes_Object = MibTableColumn
hwL2VlanStatInUcastBytes = _HwL2VlanStatInUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 10),
    _HwL2VlanStatInUcastBytes_Type()
)
hwL2VlanStatInUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInUcastBytes.setStatus("current")
_HwL2VlanStatOutUcastPkts_Type = Counter64
_HwL2VlanStatOutUcastPkts_Object = MibTableColumn
hwL2VlanStatOutUcastPkts = _HwL2VlanStatOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 11),
    _HwL2VlanStatOutUcastPkts_Type()
)
hwL2VlanStatOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutUcastPkts.setStatus("current")
_HwL2VlanStatOutUcastBytes_Type = Counter64
_HwL2VlanStatOutUcastBytes_Object = MibTableColumn
hwL2VlanStatOutUcastBytes = _HwL2VlanStatOutUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 12),
    _HwL2VlanStatOutUcastBytes_Type()
)
hwL2VlanStatOutUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutUcastBytes.setStatus("current")
_HwL2VlanStatInMcastPkts_Type = Counter64
_HwL2VlanStatInMcastPkts_Object = MibTableColumn
hwL2VlanStatInMcastPkts = _HwL2VlanStatInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 13),
    _HwL2VlanStatInMcastPkts_Type()
)
hwL2VlanStatInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInMcastPkts.setStatus("current")
_HwL2VlanStatInMcastBytes_Type = Counter64
_HwL2VlanStatInMcastBytes_Object = MibTableColumn
hwL2VlanStatInMcastBytes = _HwL2VlanStatInMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 14),
    _HwL2VlanStatInMcastBytes_Type()
)
hwL2VlanStatInMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInMcastBytes.setStatus("current")
_HwL2VlanStatOutMcastPkts_Type = Counter64
_HwL2VlanStatOutMcastPkts_Object = MibTableColumn
hwL2VlanStatOutMcastPkts = _HwL2VlanStatOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 15),
    _HwL2VlanStatOutMcastPkts_Type()
)
hwL2VlanStatOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutMcastPkts.setStatus("current")
_HwL2VlanStatOutMcastBytes_Type = Counter64
_HwL2VlanStatOutMcastBytes_Object = MibTableColumn
hwL2VlanStatOutMcastBytes = _HwL2VlanStatOutMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 16),
    _HwL2VlanStatOutMcastBytes_Type()
)
hwL2VlanStatOutMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutMcastBytes.setStatus("current")
_HwL2VlanStatInBcastPkts_Type = Counter64
_HwL2VlanStatInBcastPkts_Object = MibTableColumn
hwL2VlanStatInBcastPkts = _HwL2VlanStatInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 17),
    _HwL2VlanStatInBcastPkts_Type()
)
hwL2VlanStatInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInBcastPkts.setStatus("current")
_HwL2VlanStatInBcastBytes_Type = Counter64
_HwL2VlanStatInBcastBytes_Object = MibTableColumn
hwL2VlanStatInBcastBytes = _HwL2VlanStatInBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 18),
    _HwL2VlanStatInBcastBytes_Type()
)
hwL2VlanStatInBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatInBcastBytes.setStatus("current")
_HwL2VlanStatOutBcastPkts_Type = Counter64
_HwL2VlanStatOutBcastPkts_Object = MibTableColumn
hwL2VlanStatOutBcastPkts = _HwL2VlanStatOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 19),
    _HwL2VlanStatOutBcastPkts_Type()
)
hwL2VlanStatOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutBcastPkts.setStatus("current")
_HwL2VlanStatOutBcastBytes_Type = Counter64
_HwL2VlanStatOutBcastBytes_Object = MibTableColumn
hwL2VlanStatOutBcastBytes = _HwL2VlanStatOutBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 20),
    _HwL2VlanStatOutBcastBytes_Type()
)
hwL2VlanStatOutBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanStatOutBcastBytes.setStatus("current")
_HwL2VlanStatResetFlag_Type = EnabledStatus
_HwL2VlanStatResetFlag_Object = MibTableColumn
hwL2VlanStatResetFlag = _HwL2VlanStatResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 4, 1, 21),
    _HwL2VlanStatResetFlag_Type()
)
hwL2VlanStatResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanStatResetFlag.setStatus("current")
_HwL2IfStatVlanTable_Object = MibTable
hwL2IfStatVlanTable = _HwL2IfStatVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5)
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanTable.setStatus("current")
_HwL2IfStatVlanEntry_Object = MibTableRow
hwL2IfStatVlanEntry = _HwL2IfStatVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1)
)
hwL2IfStatVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanId"),
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanEntry.setStatus("current")


class _HwL2IfStatVlanPortIndex_Type(Integer32):
    """Custom type hwL2IfStatVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStatVlanPortIndex_Type.__name__ = "Integer32"
_HwL2IfStatVlanPortIndex_Object = MibTableColumn
hwL2IfStatVlanPortIndex = _HwL2IfStatVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 1),
    _HwL2IfStatVlanPortIndex_Type()
)
hwL2IfStatVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStatVlanPortIndex.setStatus("current")
_HwL2IfStatVlanId_Type = VlanId
_HwL2IfStatVlanId_Object = MibTableColumn
hwL2IfStatVlanId = _HwL2IfStatVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 2),
    _HwL2IfStatVlanId_Type()
)
hwL2IfStatVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStatVlanId.setStatus("current")
_HwL2IfStatVlanInTotalPkts_Type = Counter64
_HwL2IfStatVlanInTotalPkts_Object = MibTableColumn
hwL2IfStatVlanInTotalPkts = _HwL2IfStatVlanInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 3),
    _HwL2IfStatVlanInTotalPkts_Type()
)
hwL2IfStatVlanInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInTotalPkts.setStatus("current")
_HwL2IfStatVlanInTotalBytes_Type = Counter64
_HwL2IfStatVlanInTotalBytes_Object = MibTableColumn
hwL2IfStatVlanInTotalBytes = _HwL2IfStatVlanInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 4),
    _HwL2IfStatVlanInTotalBytes_Type()
)
hwL2IfStatVlanInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInTotalBytes.setStatus("current")
_HwL2IfStatVlanOutTotalPkts_Type = Counter64
_HwL2IfStatVlanOutTotalPkts_Object = MibTableColumn
hwL2IfStatVlanOutTotalPkts = _HwL2IfStatVlanOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 5),
    _HwL2IfStatVlanOutTotalPkts_Type()
)
hwL2IfStatVlanOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutTotalPkts.setStatus("current")
_HwL2IfStatVlanOutTotalBytes_Type = Counter64
_HwL2IfStatVlanOutTotalBytes_Object = MibTableColumn
hwL2IfStatVlanOutTotalBytes = _HwL2IfStatVlanOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 6),
    _HwL2IfStatVlanOutTotalBytes_Type()
)
hwL2IfStatVlanOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutTotalBytes.setStatus("current")
_HwL2IfStatVlanInPktsRate_Type = Gauge32
_HwL2IfStatVlanInPktsRate_Object = MibTableColumn
hwL2IfStatVlanInPktsRate = _HwL2IfStatVlanInPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 7),
    _HwL2IfStatVlanInPktsRate_Type()
)
hwL2IfStatVlanInPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInPktsRate.setStatus("current")
_HwL2IfStatVlanInBytesRate_Type = Gauge32
_HwL2IfStatVlanInBytesRate_Object = MibTableColumn
hwL2IfStatVlanInBytesRate = _HwL2IfStatVlanInBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 8),
    _HwL2IfStatVlanInBytesRate_Type()
)
hwL2IfStatVlanInBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInBytesRate.setStatus("current")
_HwL2IfStatVlanOutPktsRate_Type = Gauge32
_HwL2IfStatVlanOutPktsRate_Object = MibTableColumn
hwL2IfStatVlanOutPktsRate = _HwL2IfStatVlanOutPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 9),
    _HwL2IfStatVlanOutPktsRate_Type()
)
hwL2IfStatVlanOutPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutPktsRate.setStatus("current")
_HwL2IfStatVlanOutBytesRate_Type = Gauge32
_HwL2IfStatVlanOutBytesRate_Object = MibTableColumn
hwL2IfStatVlanOutBytesRate = _HwL2IfStatVlanOutBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 10),
    _HwL2IfStatVlanOutBytesRate_Type()
)
hwL2IfStatVlanOutBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutBytesRate.setStatus("current")
_HwL2IfStatVlanInUcastPkts_Type = Counter64
_HwL2IfStatVlanInUcastPkts_Object = MibTableColumn
hwL2IfStatVlanInUcastPkts = _HwL2IfStatVlanInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 11),
    _HwL2IfStatVlanInUcastPkts_Type()
)
hwL2IfStatVlanInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInUcastPkts.setStatus("current")
_HwL2IfStatVlanInUcastBytes_Type = Counter64
_HwL2IfStatVlanInUcastBytes_Object = MibTableColumn
hwL2IfStatVlanInUcastBytes = _HwL2IfStatVlanInUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 12),
    _HwL2IfStatVlanInUcastBytes_Type()
)
hwL2IfStatVlanInUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInUcastBytes.setStatus("current")
_HwL2IfStatVlanOutUcastPkts_Type = Counter64
_HwL2IfStatVlanOutUcastPkts_Object = MibTableColumn
hwL2IfStatVlanOutUcastPkts = _HwL2IfStatVlanOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 13),
    _HwL2IfStatVlanOutUcastPkts_Type()
)
hwL2IfStatVlanOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutUcastPkts.setStatus("current")
_HwL2IfStatVlanOutUcastBytes_Type = Counter64
_HwL2IfStatVlanOutUcastBytes_Object = MibTableColumn
hwL2IfStatVlanOutUcastBytes = _HwL2IfStatVlanOutUcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 14),
    _HwL2IfStatVlanOutUcastBytes_Type()
)
hwL2IfStatVlanOutUcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutUcastBytes.setStatus("current")
_HwL2IfStatVlanInMcastPkts_Type = Counter64
_HwL2IfStatVlanInMcastPkts_Object = MibTableColumn
hwL2IfStatVlanInMcastPkts = _HwL2IfStatVlanInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 15),
    _HwL2IfStatVlanInMcastPkts_Type()
)
hwL2IfStatVlanInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInMcastPkts.setStatus("current")
_HwL2IfStatVlanInMcastBytes_Type = Counter64
_HwL2IfStatVlanInMcastBytes_Object = MibTableColumn
hwL2IfStatVlanInMcastBytes = _HwL2IfStatVlanInMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 16),
    _HwL2IfStatVlanInMcastBytes_Type()
)
hwL2IfStatVlanInMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInMcastBytes.setStatus("current")
_HwL2IfStatVlanOutMcastPkts_Type = Counter64
_HwL2IfStatVlanOutMcastPkts_Object = MibTableColumn
hwL2IfStatVlanOutMcastPkts = _HwL2IfStatVlanOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 17),
    _HwL2IfStatVlanOutMcastPkts_Type()
)
hwL2IfStatVlanOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutMcastPkts.setStatus("current")
_HwL2IfStatVlanOutMcastBytes_Type = Counter64
_HwL2IfStatVlanOutMcastBytes_Object = MibTableColumn
hwL2IfStatVlanOutMcastBytes = _HwL2IfStatVlanOutMcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 18),
    _HwL2IfStatVlanOutMcastBytes_Type()
)
hwL2IfStatVlanOutMcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutMcastBytes.setStatus("current")
_HwL2IfStatVlanInBcastPkts_Type = Counter64
_HwL2IfStatVlanInBcastPkts_Object = MibTableColumn
hwL2IfStatVlanInBcastPkts = _HwL2IfStatVlanInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 19),
    _HwL2IfStatVlanInBcastPkts_Type()
)
hwL2IfStatVlanInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInBcastPkts.setStatus("current")
_HwL2IfStatVlanInBcastBytes_Type = Counter64
_HwL2IfStatVlanInBcastBytes_Object = MibTableColumn
hwL2IfStatVlanInBcastBytes = _HwL2IfStatVlanInBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 20),
    _HwL2IfStatVlanInBcastBytes_Type()
)
hwL2IfStatVlanInBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanInBcastBytes.setStatus("current")
_HwL2IfStatVlanOutBcastPkts_Type = Counter64
_HwL2IfStatVlanOutBcastPkts_Object = MibTableColumn
hwL2IfStatVlanOutBcastPkts = _HwL2IfStatVlanOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 21),
    _HwL2IfStatVlanOutBcastPkts_Type()
)
hwL2IfStatVlanOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutBcastPkts.setStatus("current")
_HwL2IfStatVlanOutBcastBytes_Type = Counter64
_HwL2IfStatVlanOutBcastBytes_Object = MibTableColumn
hwL2IfStatVlanOutBcastBytes = _HwL2IfStatVlanOutBcastBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 22),
    _HwL2IfStatVlanOutBcastBytes_Type()
)
hwL2IfStatVlanOutBcastBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStatVlanOutBcastBytes.setStatus("current")
_HwL2IfStatVlanResetFlag_Type = EnabledStatus
_HwL2IfStatVlanResetFlag_Object = MibTableColumn
hwL2IfStatVlanResetFlag = _HwL2IfStatVlanResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 5, 1, 23),
    _HwL2IfStatVlanResetFlag_Type()
)
hwL2IfStatVlanResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfStatVlanResetFlag.setStatus("current")
_HwL2IfStat8021pTable_Object = MibTable
hwL2IfStat8021pTable = _HwL2IfStat8021pTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6)
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pTable.setStatus("current")
_HwL2IfStat8021pEntry_Object = MibTableRow
hwL2IfStat8021pEntry = _HwL2IfStat8021pEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1)
)
hwL2IfStat8021pEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021p"),
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pEntry.setStatus("current")


class _HwL2IfStat8021pPortIndex_Type(Integer32):
    """Custom type hwL2IfStat8021pPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStat8021pPortIndex_Type.__name__ = "Integer32"
_HwL2IfStat8021pPortIndex_Object = MibTableColumn
hwL2IfStat8021pPortIndex = _HwL2IfStat8021pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 1),
    _HwL2IfStat8021pPortIndex_Type()
)
hwL2IfStat8021pPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pPortIndex.setStatus("current")


class _HwL2IfStat8021p_Type(Integer32):
    """Custom type hwL2IfStat8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2IfStat8021p_Type.__name__ = "Integer32"
_HwL2IfStat8021p_Object = MibTableColumn
hwL2IfStat8021p = _HwL2IfStat8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 2),
    _HwL2IfStat8021p_Type()
)
hwL2IfStat8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021p.setStatus("current")
_HwL2IfStat8021pInTotalPkts_Type = Counter64
_HwL2IfStat8021pInTotalPkts_Object = MibTableColumn
hwL2IfStat8021pInTotalPkts = _HwL2IfStat8021pInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 3),
    _HwL2IfStat8021pInTotalPkts_Type()
)
hwL2IfStat8021pInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pInTotalPkts.setStatus("current")
_HwL2IfStat8021pInTotalBytes_Type = Counter64
_HwL2IfStat8021pInTotalBytes_Object = MibTableColumn
hwL2IfStat8021pInTotalBytes = _HwL2IfStat8021pInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 4),
    _HwL2IfStat8021pInTotalBytes_Type()
)
hwL2IfStat8021pInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pInTotalBytes.setStatus("current")
_HwL2IfStat8021pOutTotalPkts_Type = Counter64
_HwL2IfStat8021pOutTotalPkts_Object = MibTableColumn
hwL2IfStat8021pOutTotalPkts = _HwL2IfStat8021pOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 5),
    _HwL2IfStat8021pOutTotalPkts_Type()
)
hwL2IfStat8021pOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pOutTotalPkts.setStatus("current")
_HwL2IfStat8021pOutTotalBytes_Type = Counter64
_HwL2IfStat8021pOutTotalBytes_Object = MibTableColumn
hwL2IfStat8021pOutTotalBytes = _HwL2IfStat8021pOutTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 6),
    _HwL2IfStat8021pOutTotalBytes_Type()
)
hwL2IfStat8021pOutTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pOutTotalBytes.setStatus("current")
_HwL2IfStat8021pInPktsRate_Type = Gauge32
_HwL2IfStat8021pInPktsRate_Object = MibTableColumn
hwL2IfStat8021pInPktsRate = _HwL2IfStat8021pInPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 7),
    _HwL2IfStat8021pInPktsRate_Type()
)
hwL2IfStat8021pInPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pInPktsRate.setStatus("current")
_HwL2IfStat8021pInBytsRate_Type = Gauge32
_HwL2IfStat8021pInBytsRate_Object = MibTableColumn
hwL2IfStat8021pInBytsRate = _HwL2IfStat8021pInBytsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 8),
    _HwL2IfStat8021pInBytsRate_Type()
)
hwL2IfStat8021pInBytsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pInBytsRate.setStatus("current")
_HwL2IfStat8021pOutPktsRate_Type = Gauge32
_HwL2IfStat8021pOutPktsRate_Object = MibTableColumn
hwL2IfStat8021pOutPktsRate = _HwL2IfStat8021pOutPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 9),
    _HwL2IfStat8021pOutPktsRate_Type()
)
hwL2IfStat8021pOutPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pOutPktsRate.setStatus("current")
_HwL2IfStat8021pOutBytesRate_Type = Gauge32
_HwL2IfStat8021pOutBytesRate_Object = MibTableColumn
hwL2IfStat8021pOutBytesRate = _HwL2IfStat8021pOutBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 10),
    _HwL2IfStat8021pOutBytesRate_Type()
)
hwL2IfStat8021pOutBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pOutBytesRate.setStatus("current")
_HwL2IfStat8021pResetFlag_Type = EnabledStatus
_HwL2IfStat8021pResetFlag_Object = MibTableColumn
hwL2IfStat8021pResetFlag = _HwL2IfStat8021pResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 6, 1, 11),
    _HwL2IfStat8021pResetFlag_Type()
)
hwL2IfStat8021pResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfStat8021pResetFlag.setStatus("current")
_HwL2IfStat8021pAndVlanTable_Object = MibTable
hwL2IfStat8021pAndVlanTable = _HwL2IfStat8021pAndVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7)
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanTable.setStatus("current")
_HwL2IfStat8021pAndVlanEntry_Object = MibTableRow
hwL2IfStat8021pAndVlanEntry = _HwL2IfStat8021pAndVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1)
)
hwL2IfStat8021pAndVlanEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanPortIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlan8021p"),
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanEntry.setStatus("current")


class _HwL2IfStat8021pAndVlanPortIndex_Type(Integer32):
    """Custom type hwL2IfStat8021pAndVlanPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwL2IfStat8021pAndVlanPortIndex_Type.__name__ = "Integer32"
_HwL2IfStat8021pAndVlanPortIndex_Object = MibTableColumn
hwL2IfStat8021pAndVlanPortIndex = _HwL2IfStat8021pAndVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 1),
    _HwL2IfStat8021pAndVlanPortIndex_Type()
)
hwL2IfStat8021pAndVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanPortIndex.setStatus("current")
_HwL2IfStat8021pAndVlanVlanId_Type = VlanId
_HwL2IfStat8021pAndVlanVlanId_Object = MibTableColumn
hwL2IfStat8021pAndVlanVlanId = _HwL2IfStat8021pAndVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 2),
    _HwL2IfStat8021pAndVlanVlanId_Type()
)
hwL2IfStat8021pAndVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanVlanId.setStatus("current")


class _HwL2IfStat8021pAndVlan8021p_Type(Integer32):
    """Custom type hwL2IfStat8021pAndVlan8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2IfStat8021pAndVlan8021p_Type.__name__ = "Integer32"
_HwL2IfStat8021pAndVlan8021p_Object = MibTableColumn
hwL2IfStat8021pAndVlan8021p = _HwL2IfStat8021pAndVlan8021p_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 3),
    _HwL2IfStat8021pAndVlan8021p_Type()
)
hwL2IfStat8021pAndVlan8021p.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlan8021p.setStatus("current")
_HwL2IfStat8021pAndVlanInTotalPkts_Type = Counter64
_HwL2IfStat8021pAndVlanInTotalPkts_Object = MibTableColumn
hwL2IfStat8021pAndVlanInTotalPkts = _HwL2IfStat8021pAndVlanInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 4),
    _HwL2IfStat8021pAndVlanInTotalPkts_Type()
)
hwL2IfStat8021pAndVlanInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanInTotalPkts.setStatus("current")
_HwL2IfStat8021pAndVlanInTotalBytes_Type = Counter64
_HwL2IfStat8021pAndVlanInTotalBytes_Object = MibTableColumn
hwL2IfStat8021pAndVlanInTotalBytes = _HwL2IfStat8021pAndVlanInTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 5),
    _HwL2IfStat8021pAndVlanInTotalBytes_Type()
)
hwL2IfStat8021pAndVlanInTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanInTotalBytes.setStatus("current")
_HwL2IfStat8021pAndVlanInPktsRate_Type = Gauge32
_HwL2IfStat8021pAndVlanInPktsRate_Object = MibTableColumn
hwL2IfStat8021pAndVlanInPktsRate = _HwL2IfStat8021pAndVlanInPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 6),
    _HwL2IfStat8021pAndVlanInPktsRate_Type()
)
hwL2IfStat8021pAndVlanInPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanInPktsRate.setStatus("current")
_HwL2IfStat8021pAndVlanInBytsRate_Type = Gauge32
_HwL2IfStat8021pAndVlanInBytsRate_Object = MibTableColumn
hwL2IfStat8021pAndVlanInBytsRate = _HwL2IfStat8021pAndVlanInBytsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 7),
    _HwL2IfStat8021pAndVlanInBytsRate_Type()
)
hwL2IfStat8021pAndVlanInBytsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanInBytsRate.setStatus("current")
_HwL2IfStat8021pAndVlanResetFlag_Type = EnabledStatus
_HwL2IfStat8021pAndVlanResetFlag_Object = MibTableColumn
hwL2IfStat8021pAndVlanResetFlag = _HwL2IfStat8021pAndVlanResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 7, 1, 8),
    _HwL2IfStat8021pAndVlanResetFlag_Type()
)
hwL2IfStat8021pAndVlanResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanResetFlag.setStatus("current")
_HwL2VlanSwitchPSTable_Object = MibTable
hwL2VlanSwitchPSTable = _HwL2VlanSwitchPSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8)
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSTable.setStatus("current")
_HwL2VlanSwitchPSEntry_Object = MibTableRow
hwL2VlanSwitchPSEntry = _HwL2VlanSwitchPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1)
)
hwL2VlanSwitchPSEntry.setIndexNames(
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSIfIndex"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSSVlanId"),
    (0, "HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSCVlanId"),
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSEntry.setStatus("current")
_HwL2VlanSwitchPSIfIndex_Type = InterfaceIndex
_HwL2VlanSwitchPSIfIndex_Object = MibTableColumn
hwL2VlanSwitchPSIfIndex = _HwL2VlanSwitchPSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 1),
    _HwL2VlanSwitchPSIfIndex_Type()
)
hwL2VlanSwitchPSIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSIfIndex.setStatus("current")


class _HwL2VlanSwitchPSSVlanId_Type(Integer32):
    """Custom type hwL2VlanSwitchPSSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwL2VlanSwitchPSSVlanId_Type.__name__ = "Integer32"
_HwL2VlanSwitchPSSVlanId_Object = MibTableColumn
hwL2VlanSwitchPSSVlanId = _HwL2VlanSwitchPSSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 2),
    _HwL2VlanSwitchPSSVlanId_Type()
)
hwL2VlanSwitchPSSVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSSVlanId.setStatus("current")


class _HwL2VlanSwitchPSCVlanId_Type(Integer32):
    """Custom type hwL2VlanSwitchPSCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwL2VlanSwitchPSCVlanId_Type.__name__ = "Integer32"
_HwL2VlanSwitchPSCVlanId_Object = MibTableColumn
hwL2VlanSwitchPSCVlanId = _HwL2VlanSwitchPSCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 3),
    _HwL2VlanSwitchPSCVlanId_Type()
)
hwL2VlanSwitchPSCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSCVlanId.setStatus("current")
_HwL2VlanSwitchPSInputPkts_Type = Counter64
_HwL2VlanSwitchPSInputPkts_Object = MibTableColumn
hwL2VlanSwitchPSInputPkts = _HwL2VlanSwitchPSInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 4),
    _HwL2VlanSwitchPSInputPkts_Type()
)
hwL2VlanSwitchPSInputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSInputPkts.setStatus("current")
_HwL2VlanSwitchPSInputBytes_Type = Counter64
_HwL2VlanSwitchPSInputBytes_Object = MibTableColumn
hwL2VlanSwitchPSInputBytes = _HwL2VlanSwitchPSInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 5),
    _HwL2VlanSwitchPSInputBytes_Type()
)
hwL2VlanSwitchPSInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSInputBytes.setStatus("current")
_HwL2VlanSwitchPSOutputPkts_Type = Counter64
_HwL2VlanSwitchPSOutputPkts_Object = MibTableColumn
hwL2VlanSwitchPSOutputPkts = _HwL2VlanSwitchPSOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 6),
    _HwL2VlanSwitchPSOutputPkts_Type()
)
hwL2VlanSwitchPSOutputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSOutputPkts.setStatus("current")
_HwL2VlanSwitchPSOutputBytes_Type = Counter64
_HwL2VlanSwitchPSOutputBytes_Object = MibTableColumn
hwL2VlanSwitchPSOutputBytes = _HwL2VlanSwitchPSOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 7),
    _HwL2VlanSwitchPSOutputBytes_Type()
)
hwL2VlanSwitchPSOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSOutputBytes.setStatus("current")
_HwL2VlanSwitchPSResetFlag_Type = EnabledStatus
_HwL2VlanSwitchPSResetFlag_Object = MibTableColumn
hwL2VlanSwitchPSResetFlag = _HwL2VlanSwitchPSResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 8),
    _HwL2VlanSwitchPSResetFlag_Type()
)
hwL2VlanSwitchPSResetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSResetFlag.setStatus("current")
_HwL2VlanSwitchPSEnableFlag_Type = EnabledStatus
_HwL2VlanSwitchPSEnableFlag_Object = MibTableColumn
hwL2VlanSwitchPSEnableFlag = _HwL2VlanSwitchPSEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 3, 8, 1, 9),
    _HwL2VlanSwitchPSEnableFlag_Type()
)
hwL2VlanSwitchPSEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSEnableFlag.setStatus("current")
_HwL2VlanTraps_ObjectIdentity = ObjectIdentity
hwL2VlanTraps = _HwL2VlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 4)
)
_HwL2vlanConformance_ObjectIdentity = ObjectIdentity
hwL2vlanConformance = _HwL2vlanConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2)
)
_HwL2vlanGroups_ObjectIdentity = ObjectIdentity
hwL2vlanGroups = _HwL2vlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1)
)
_HwL2vlanCompliances_ObjectIdentity = ObjectIdentity
hwL2vlanCompliances = _HwL2vlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 2)
)
_HwL2VlanTrapsGroups_ObjectIdentity = ObjectIdentity
hwL2VlanTrapsGroups = _HwL2VlanTrapsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 3)
)

# Managed Objects groups

hwL2VlanMIBTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 1)
)
hwL2VlanMIBTableGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPortList"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanType"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanUnknownUnicastProcessing"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanIfIndex"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacLearn"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanCreateStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMulticast"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanAdminStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatisStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanRowStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanBcast"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanUnknownMulticastProcessing"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProperty"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanAgingTime"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanName"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSmartMacLearn"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanServiceName"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanManagementVlan"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanDynamicVlan"))
)
if mibBuilder.loadTexts:
    hwL2VlanMIBTableGroup.setStatus("current")

hwL2vlanStackingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 2)
)
hwL2vlanStackingGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingOutsideVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingOutsideVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2vlanStackingGroup.setStatus("current")

hwL2vlanMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 3)
)
hwL2vlanMappingGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingOutsideVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingOutsideVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2vlanMappingGroup.setStatus("current")

hwSupervlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 4)
)
hwSupervlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwSubVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwSubVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwSupervlanGroup.setStatus("current")

hwL2InterfIsolateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 5)
)
hwL2InterfIsolateGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2InterfIsolateInterflistLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2InterfIsolateInterflistHigh"))
)
if mibBuilder.loadTexts:
    hwL2InterfIsolateGroup.setStatus("current")

hwL2IsolatemappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 6)
)
hwL2IsolatemappingGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IsolateInterflistLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IsolateInterflistHigh"))
)
if mibBuilder.loadTexts:
    hwL2IsolatemappingGroup.setStatus("current")

hwL2VlanStackingExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 7)
)
hwL2VlanStackingExtGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtPriorityMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtVlan8021p"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingExtRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanStackingExtGroup.setStatus("current")

hwL2vlanQinQGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 8)
)
hwL2vlanQinQGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanQinQOutSideVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSysQinQRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2vlanQinQGroup.setStatus("current")

hwL2vlanQinQInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 9)
)
hwL2vlanQinQInterfaceGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanQinQSVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanQinQAction"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanQinQNewCVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanInterfaceQinQRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2vlanQinQInterfaceGroup.setStatus("current")

hwL2DVlanMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 10)
)
hwL2DVlanMappingGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingMapExternalVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingMapInternalVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingAction"),
        ("HUAWEI-L2VLAN-MIB", "hwL2DVlanMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2DVlanMappingGroup.setStatus("current")

hwL2VlanStackingAdvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 11)
)
hwL2VlanStackingAdvGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvOutsideVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvOutsideVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingAdvRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanStackingAdvGroup.setStatus("current")

hwL2VlanMappingAdvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 12)
)
hwL2VlanMappingAdvGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvOutsideVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvOutsideVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingAdvRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanMappingAdvGroup.setStatus("current")

hwL2VlanSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 13)
)
hwL2VlanSwitchGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchOuterSwitchVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchInnerSwitchVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitch8021pRemark"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchOutIfIndex"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMtu"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMtuDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMtuDiscardBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMtuResetFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchMtuEnableFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchGroup.setStatus("current")

hwL2IfStatVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 14)
)
hwL2IfStatVlanCfgGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanCfgEnableFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanCfgGroup.setStatus("current")

hwL2IfStat8021pCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 15)
)
hwL2IfStat8021pCfgGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pCfgEnableFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pCfgGroup.setStatus("current")

hwL2IfStat8021pAndVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 16)
)
hwL2IfStat8021pAndVlanCfgGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanCfgEnableFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanCfgGroup.setStatus("current")

hwL2VlanStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 17)
)
hwL2VlanStatGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatUnknownUcastDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatUnknownMcastDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatBcastDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInUcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInUcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutUcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutUcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInMcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInMcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutMcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutMcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInBcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatInBcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutBcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatOutBcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatResetFlag"))
)
if mibBuilder.loadTexts:
    hwL2VlanStatGroup.setStatus("current")

hwL2IfStatVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 18)
)
hwL2IfStatVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInPktsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInBytesRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutPktsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutBytesRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInUcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInUcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutUcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutUcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInMcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInMcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutMcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutMcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInBcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanInBcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutBcastPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanOutBcastBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStatVlanResetFlag"))
)
if mibBuilder.loadTexts:
    hwL2IfStatVlanGroup.setStatus("current")

hwL2IfStat8021pGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 19)
)
hwL2IfStat8021pGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pInTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pInTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pOutTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pOutTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pInPktsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pInBytsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pOutPktsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pOutBytesRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pResetFlag"))
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pGroup.setStatus("current")

hwL2IfStat8021pAndVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 20)
)
hwL2IfStat8021pAndVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanInTotalPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanInTotalBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanInPktsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanInBytsRate"),
        ("HUAWEI-L2VLAN-MIB", "hwL2IfStat8021pAndVlanResetFlag"))
)
if mibBuilder.loadTexts:
    hwL2IfStat8021pAndVlanGroup.setStatus("current")

hwL2VlanMappingExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 21)
)
hwL2VlanMappingExtGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtRowStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtPriorityMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingExtVlan8021p"))
)
if mibBuilder.loadTexts:
    hwL2VlanMappingExtGroup.setStatus("current")

hwL2VlanQinqVlanTransEnaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 22)
)
hwL2VlanQinqVlanTransEnaGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransEna"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransEnaRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransEnaGroup.setStatus("current")

hwL2VlanQinqVlanTransMissDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 23)
)
hwL2VlanQinqVlanTransMissDropGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransMissDrop"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanQinqVlanTransMissDropRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanQinqVlanTransMissDropGroup.setStatus("current")

hwL2VlanViewMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 24)
)
hwL2VlanViewMappingGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingMapVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingPriorityMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingVlan8021p"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanViewMappingRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanViewMappingGroup.setStatus("current")

hwL2VlanStackingMaskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 25)
)
hwL2VlanStackingMaskGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStackingMaskRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanStackingMaskGroup.setStatus("current")

hwL2VlanIpSubnetVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 26)
)
hwL2VlanIpSubnetVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanIpAddress"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanIpSubnetMask"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanIpSubnetVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanIpSubnetVlanGroup.setStatus("current")

hwL2VlanMacVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 27)
)
hwL2VlanMacVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanMac"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanVlanPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanMacRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanGroup.setStatus("current")

hwL2VlanProtocolVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 28)
)
hwL2VlanProtocolVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanProtocolType"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanEncapType"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanGroup.setStatus("current")

hwL2VlanPolicyVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 29)
)
hwL2VlanPolicyVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanVlanPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanMac"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanIp"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanPort"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanGroup.setStatus("current")

hwL2VlanVoiceVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 30)
)
hwL2VlanVoiceVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanEnabledVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanAgingTime"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanSecurityMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanPortEnable"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanPortMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanPortLegacy"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanPortSecurityMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanOuiDescription"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanOuiRowStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlan8021p"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanVoiceVlanDscp"))
)
if mibBuilder.loadTexts:
    hwL2VlanVoiceVlanGroup.setStatus("current")

hwL2VlanMappingMultiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 31)
)
hwL2VlanMappingMultiGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiVlanListHigh"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMappingMultiRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanMappingMultiGroup.setStatus("current")

hwL2VlanSwitchPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 32)
)
hwL2VlanSwitchPSGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSInputPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSInputBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSOutputPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSOutputBytes"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSResetFlag"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchPSEnableFlag"))
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchPSGroup.setStatus("current")

hwL2VlanMacVlanNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 33)
)
hwL2VlanMacVlanNewGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanNewVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanNewVlanPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMacVlanNewMacRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanMacVlanNewGroup.setStatus("current")

hwL2VlanProtocolVlanNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 34)
)
hwL2VlanProtocolVlanNewGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanNewProtocolType"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanNewProtocolTypeValue"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanNewRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanNewGroup.setStatus("current")

hwL2VlanPolicyVlanNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 35)
)
hwL2VlanPolicyVlanNewGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewVlanPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanPolicyVlanNewRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanPolicyVlanNewGroup.setStatus("current")

hwL2VlanProtocolVlanPortNewGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 36)
)
hwL2VlanProtocolVlanPortNewGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanPortNewPriority"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanProtocolVlanPortNewRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanProtocolVlanPortNewGroup.setStatus("current")

hwL2VlanMultiVoiceVlanPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 37)
)
hwL2VlanMultiVoiceVlanPortGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanMultiVoiceVlanPortVLanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanMultiVoiceVlanPortRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanMultiVoiceVlanPortGroup.setStatus("current")

hwL2VlanPrecedenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 38)
)
hwL2VlanPrecedenceGroup.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanPrecedence")
)
if mibBuilder.loadTexts:
    hwL2VlanPrecedenceGroup.setStatus("current")

hwL2VlanXlateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 39)
)
hwL2VlanXlateGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateVlanIdEnd"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateAction"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateToVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateToinnerVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateremark"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanXlateRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2VlanXlateGroup.setStatus("current")

hwL2VlanSwitchExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 40)
)
hwL2VlanSwitchExtGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtSrcIfIndex"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtDstIfIndex"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtDstInnerVlan"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtRowStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtLinkStatus"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtVlanXlateAction"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtDstVlan"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtRemark"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtRemarkReverse"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtOuterVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtVlanListLow"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanSwitchExtVlanListHigh"))
)
if mibBuilder.loadTexts:
    hwL2VlanSwitchExtGroup.setStatus("current")

hwL2QinQVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 41)
)
hwL2QinQVlanGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanMode"),
        ("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanChangedVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanChangedInnerVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanRemark"),
        ("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanMapStackVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2QinQVlanRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2QinQVlanGroup.setStatus("current")

hwL2UntagAddDTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 1, 42)
)
hwL2UntagAddDTagGroup.setObjects(
      *(("HUAWEI-L2VLAN-MIB", "hwL2UntagAddDTagOuterVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2UntagAddDTagInnerVlanId"),
        ("HUAWEI-L2VLAN-MIB", "hwL2UntagAddDTagRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2UntagAddDTagGroup.setStatus("current")


# Notification objects

hwL2VlanUnkownPacketAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 1, 4, 1)
)
hwL2VlanUnkownPacketAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatUnknownUcastDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatUnknownMcastDiscardPkts"),
        ("HUAWEI-L2VLAN-MIB", "hwL2VlanStatBcastDiscardPkts"))
)
if mibBuilder.loadTexts:
    hwL2VlanUnkownPacketAlarm.setStatus(
        "current"
    )


# Notifications groups

hwL2VlanTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 3, 1)
)
hwL2VlanTrapsGroup.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanUnkownPacketAlarm")
)
if mibBuilder.loadTexts:
    hwL2VlanTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2vlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwL2vlanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2VLAN-MIB",
    **{"hwL2Mgmt": hwL2Mgmt,
       "hwL2Vlan": hwL2Vlan,
       "hwL2VlanMngObjects": hwL2VlanMngObjects,
       "hwL2VlanBase": hwL2VlanBase,
       "hwL2VlanMIBTable": hwL2VlanMIBTable,
       "hwL2VlanMIBEntry": hwL2VlanMIBEntry,
       "hwL2VlanIndex": hwL2VlanIndex,
       "hwL2VlanDescr": hwL2VlanDescr,
       "hwL2VlanPortList": hwL2VlanPortList,
       "hwL2VlanType": hwL2VlanType,
       "hwL2VlanUnknownUnicastProcessing": hwL2VlanUnknownUnicastProcessing,
       "hwL2VlanIfIndex": hwL2VlanIfIndex,
       "hwL2VlanMacLearn": hwL2VlanMacLearn,
       "hwL2VlanMulticast": hwL2VlanMulticast,
       "hwL2VlanAdminStatus": hwL2VlanAdminStatus,
       "hwL2VlanStatisStatus": hwL2VlanStatisStatus,
       "hwL2VlanCreateStatus": hwL2VlanCreateStatus,
       "hwL2VlanRowStatus": hwL2VlanRowStatus,
       "hwL2VlanBcast": hwL2VlanBcast,
       "hwL2VlanUnknownMulticastProcessing": hwL2VlanUnknownMulticastProcessing,
       "hwL2VlanProperty": hwL2VlanProperty,
       "hwL2VlanAgingTime": hwL2VlanAgingTime,
       "hwL2VlanName": hwL2VlanName,
       "hwL2VlanSmartMacLearn": hwL2VlanSmartMacLearn,
       "hwL2VlanServiceName": hwL2VlanServiceName,
       "hwL2VlanManagementVlan": hwL2VlanManagementVlan,
       "hwL2VlanDynamicVlan": hwL2VlanDynamicVlan,
       "hwL2VlanApply": hwL2VlanApply,
       "hwL2VlanStackingTable": hwL2VlanStackingTable,
       "hwL2VlanStackingEntry": hwL2VlanStackingEntry,
       "hwL2VlanStackingPortIndex": hwL2VlanStackingPortIndex,
       "hwL2VlanStackingInsideVlanId": hwL2VlanStackingInsideVlanId,
       "hwL2VlanStackingOutsideVlanListLow": hwL2VlanStackingOutsideVlanListLow,
       "hwL2VlanStackingOutsideVlanListHigh": hwL2VlanStackingOutsideVlanListHigh,
       "hwL2VlanStackingRowStatus": hwL2VlanStackingRowStatus,
       "hwL2VlanMappingTable": hwL2VlanMappingTable,
       "hwL2VlanMappingEntry": hwL2VlanMappingEntry,
       "hwL2VlanMappingPortIndex": hwL2VlanMappingPortIndex,
       "hwL2VlanMappingInsideVlanId": hwL2VlanMappingInsideVlanId,
       "hwL2VlanMappingOutsideVlanListLow": hwL2VlanMappingOutsideVlanListLow,
       "hwL2VlanMappingOutsideVlanListHigh": hwL2VlanMappingOutsideVlanListHigh,
       "hwL2VlanMappingRowStatus": hwL2VlanMappingRowStatus,
       "hwSuperVlanTable": hwSuperVlanTable,
       "hwSuperVlanEntry": hwSuperVlanEntry,
       "hwSuperVlanId": hwSuperVlanId,
       "hwSubVlanListLow": hwSubVlanListLow,
       "hwSubVlanListHigh": hwSubVlanListHigh,
       "hwL2InterfIsolateTable": hwL2InterfIsolateTable,
       "hwL2InterfIsolateEntry": hwL2InterfIsolateEntry,
       "hwL2InterfIsolateVlanId": hwL2InterfIsolateVlanId,
       "hwL2InterfIsolateInterflistLow": hwL2InterfIsolateInterflistLow,
       "hwL2InterfIsolateInterflistHigh": hwL2InterfIsolateInterflistHigh,
       "hwL2IsolatemappingTable": hwL2IsolatemappingTable,
       "hwL2IsolatemappingEntry": hwL2IsolatemappingEntry,
       "hwL2IsolatemappingPortNum": hwL2IsolatemappingPortNum,
       "hwL2IsolateInterflistLow": hwL2IsolateInterflistLow,
       "hwL2IsolateInterflistHigh": hwL2IsolateInterflistHigh,
       "hwL2VlanStackingExtTable": hwL2VlanStackingExtTable,
       "hwL2VlanStackingExtEntry": hwL2VlanStackingExtEntry,
       "hwL2VlanStackingExtPortIndex": hwL2VlanStackingExtPortIndex,
       "hwL2VlanStackingExtVlanId": hwL2VlanStackingExtVlanId,
       "hwL2VlanStackingExtAction": hwL2VlanStackingExtAction,
       "hwL2VlanStackingExtDirection": hwL2VlanStackingExtDirection,
       "hwL2VlanStackingExtVlanListLow": hwL2VlanStackingExtVlanListLow,
       "hwL2VlanStackingExtVlanListHigh": hwL2VlanStackingExtVlanListHigh,
       "hwL2VlanStackingExtRowStatus": hwL2VlanStackingExtRowStatus,
       "hwL2VlanStackingExtPriorityMode": hwL2VlanStackingExtPriorityMode,
       "hwL2VlanStackingExtVlan8021p": hwL2VlanStackingExtVlan8021p,
       "hwL2VlanQinQTable": hwL2VlanQinQTable,
       "hwL2VlanQinQEntry": hwL2VlanQinQEntry,
       "hwL2VlanQinQIndex": hwL2VlanQinQIndex,
       "hwL2VlanQinQDirection": hwL2VlanQinQDirection,
       "hwL2VlanQinQOutSideVlanId": hwL2VlanQinQOutSideVlanId,
       "hwL2VlanSysQinQRowStatus": hwL2VlanSysQinQRowStatus,
       "hwL2VlanInterfaceQinQTable": hwL2VlanInterfaceQinQTable,
       "hwL2VlanInterfaceQinQEntry": hwL2VlanInterfaceQinQEntry,
       "hwL2VlanQinQInterfaceIndex": hwL2VlanQinQInterfaceIndex,
       "hwL2VlanQinQCVlanId": hwL2VlanQinQCVlanId,
       "hwL2VlanQinQSVlanId": hwL2VlanQinQSVlanId,
       "hwL2VlanQinQAction": hwL2VlanQinQAction,
       "hwL2VlanQinQNewCVlanId": hwL2VlanQinQNewCVlanId,
       "hwL2VlanInterfaceQinQRowStatus": hwL2VlanInterfaceQinQRowStatus,
       "hwL2DVlanMappingTable": hwL2DVlanMappingTable,
       "hwL2DVlanMappingEntry": hwL2DVlanMappingEntry,
       "hwL2DVlanMappingInterfaceIndex": hwL2DVlanMappingInterfaceIndex,
       "hwL2DVlanMappingExternalVlanId": hwL2DVlanMappingExternalVlanId,
       "hwL2DVlanMappingInternalVlanId": hwL2DVlanMappingInternalVlanId,
       "hwL2DVlanMappingDirection": hwL2DVlanMappingDirection,
       "hwL2DVlanMappingMapExternalVlanId": hwL2DVlanMappingMapExternalVlanId,
       "hwL2DVlanMappingMapInternalVlanId": hwL2DVlanMappingMapInternalVlanId,
       "hwL2DVlanMappingAction": hwL2DVlanMappingAction,
       "hwL2DVlanMappingRowStatus": hwL2DVlanMappingRowStatus,
       "hwL2VlanMappingExtTable": hwL2VlanMappingExtTable,
       "hwL2VlanMappingExtEntry": hwL2VlanMappingExtEntry,
       "hwL2VlanMappingExtPortIndex": hwL2VlanMappingExtPortIndex,
       "hwL2VlanMappingExtDirection": hwL2VlanMappingExtDirection,
       "hwL2VlanMappingExtVlanId": hwL2VlanMappingExtVlanId,
       "hwL2VlanMappingExtVlanListLow": hwL2VlanMappingExtVlanListLow,
       "hwL2VlanMappingExtVlanListHigh": hwL2VlanMappingExtVlanListHigh,
       "hwL2VlanMappingExtRowStatus": hwL2VlanMappingExtRowStatus,
       "hwL2VlanMappingExtPriorityMode": hwL2VlanMappingExtPriorityMode,
       "hwL2VlanMappingExtVlan8021p": hwL2VlanMappingExtVlan8021p,
       "hwL2VlanStackingAdvTable": hwL2VlanStackingAdvTable,
       "hwL2VlanStackingAdvEntry": hwL2VlanStackingAdvEntry,
       "hwL2VlanStackingAdvPortIndex": hwL2VlanStackingAdvPortIndex,
       "hwL2VlanStackingAdvOutside8021p": hwL2VlanStackingAdvOutside8021p,
       "hwL2VlanStackingAdvStackVlanId": hwL2VlanStackingAdvStackVlanId,
       "hwL2VlanStackingAdvStack8021p": hwL2VlanStackingAdvStack8021p,
       "hwL2VlanStackingAdvMapVlanId": hwL2VlanStackingAdvMapVlanId,
       "hwL2VlanStackingAdvOutsideVlanListLow": hwL2VlanStackingAdvOutsideVlanListLow,
       "hwL2VlanStackingAdvOutsideVlanListHigh": hwL2VlanStackingAdvOutsideVlanListHigh,
       "hwL2VlanStackingAdvRowStatus": hwL2VlanStackingAdvRowStatus,
       "hwL2VlanMappingAdvTable": hwL2VlanMappingAdvTable,
       "hwL2VlanMappingAdvEntry": hwL2VlanMappingAdvEntry,
       "hwL2VlanMappingAdvPortIndex": hwL2VlanMappingAdvPortIndex,
       "hwL2VlanMappingAdvOutsideVlan8021p": hwL2VlanMappingAdvOutsideVlan8021p,
       "hwL2VlanMappingAdvMapVlanId": hwL2VlanMappingAdvMapVlanId,
       "hwL2VlanMappingAdvMapVlan8021p": hwL2VlanMappingAdvMapVlan8021p,
       "hwL2VlanMappingAdvOutsideVlanListLow": hwL2VlanMappingAdvOutsideVlanListLow,
       "hwL2VlanMappingAdvOutsideVlanListHigh": hwL2VlanMappingAdvOutsideVlanListHigh,
       "hwL2VlanMappingAdvRowStatus": hwL2VlanMappingAdvRowStatus,
       "hwL2VlanSwitchTable": hwL2VlanSwitchTable,
       "hwL2VlanSwitchEntry": hwL2VlanSwitchEntry,
       "hwL2VlanSwitchIfIndex": hwL2VlanSwitchIfIndex,
       "hwL2VlanSwitchOuterVlanId": hwL2VlanSwitchOuterVlanId,
       "hwL2VlanSwitchInnerVlanId": hwL2VlanSwitchInnerVlanId,
       "hwL2VlanSwitchMode": hwL2VlanSwitchMode,
       "hwL2VlanSwitchOuterSwitchVlanId": hwL2VlanSwitchOuterSwitchVlanId,
       "hwL2VlanSwitchInnerSwitchVlanId": hwL2VlanSwitchInnerSwitchVlanId,
       "hwL2VlanSwitch8021pRemark": hwL2VlanSwitch8021pRemark,
       "hwL2VlanSwitchOutIfIndex": hwL2VlanSwitchOutIfIndex,
       "hwL2VlanSwitchMtu": hwL2VlanSwitchMtu,
       "hwL2VlanSwitchMtuDiscardPkts": hwL2VlanSwitchMtuDiscardPkts,
       "hwL2VlanSwitchMtuDiscardBytes": hwL2VlanSwitchMtuDiscardBytes,
       "hwL2VlanSwitchMtuResetFlag": hwL2VlanSwitchMtuResetFlag,
       "hwL2VlanSwitchMtuEnableFlag": hwL2VlanSwitchMtuEnableFlag,
       "hwL2VlanSwitchRowStatus": hwL2VlanSwitchRowStatus,
       "hwL2VlanQinqVlanTransEnaTable": hwL2VlanQinqVlanTransEnaTable,
       "hwL2VlanQinqVlanTransEnaEntry": hwL2VlanQinqVlanTransEnaEntry,
       "hwL2VlanQinqVlanTransEnaPortIndex": hwL2VlanQinqVlanTransEnaPortIndex,
       "hwL2VlanQinqVlanTransEna": hwL2VlanQinqVlanTransEna,
       "hwL2VlanQinqVlanTransEnaRowStatus": hwL2VlanQinqVlanTransEnaRowStatus,
       "hwL2VlanQinqVlanTransMissDropTable": hwL2VlanQinqVlanTransMissDropTable,
       "hwL2VlanQinqVlanTransMissDropEntry": hwL2VlanQinqVlanTransMissDropEntry,
       "hwL2VlanQinqVlanTransMissDropPortIndex": hwL2VlanQinqVlanTransMissDropPortIndex,
       "hwL2VlanQinqVlanTransMissDrop": hwL2VlanQinqVlanTransMissDrop,
       "hwL2VlanQinqVlanTransMissDropRowStatus": hwL2VlanQinqVlanTransMissDropRowStatus,
       "hwL2VlanViewMappingTable": hwL2VlanViewMappingTable,
       "hwL2VlanViewMappingEntry": hwL2VlanViewMappingEntry,
       "hwL2VlanViewMappingVlanId": hwL2VlanViewMappingVlanId,
       "hwL2VlanViewMappingDirection": hwL2VlanViewMappingDirection,
       "hwL2VlanViewMappingMapVlanId": hwL2VlanViewMappingMapVlanId,
       "hwL2VlanViewMappingPriorityMode": hwL2VlanViewMappingPriorityMode,
       "hwL2VlanViewMappingVlan8021p": hwL2VlanViewMappingVlan8021p,
       "hwL2VlanViewMappingRowStatus": hwL2VlanViewMappingRowStatus,
       "hwL2VlanStackingMaskTable": hwL2VlanStackingMaskTable,
       "hwL2VlanStackingMaskEntry": hwL2VlanStackingMaskEntry,
       "hwL2VlanStackingMaskPortIndex": hwL2VlanStackingMaskPortIndex,
       "hwL2VlanStackingMaskStackVlanId": hwL2VlanStackingMaskStackVlanId,
       "hwL2VlanStackingMaskStack8021p": hwL2VlanStackingMaskStack8021p,
       "hwL2VlanStackingMaskAction": hwL2VlanStackingMaskAction,
       "hwL2VlanStackingMaskDirection": hwL2VlanStackingMaskDirection,
       "hwL2VlanStackingMaskVlanListLow": hwL2VlanStackingMaskVlanListLow,
       "hwL2VlanStackingMaskVlanListHigh": hwL2VlanStackingMaskVlanListHigh,
       "hwL2VlanStackingMaskRowStatus": hwL2VlanStackingMaskRowStatus,
       "hwL2VlanIpSubnetVlanTable": hwL2VlanIpSubnetVlanTable,
       "hwL2VlanIpSubnetVlanEntry": hwL2VlanIpSubnetVlanEntry,
       "hwL2VlanIpSubnetVlanVlanId": hwL2VlanIpSubnetVlanVlanId,
       "hwL2VlanIpSubnetVlanIpSubnetIndex": hwL2VlanIpSubnetVlanIpSubnetIndex,
       "hwL2VlanIpSubnetVlanIpAddress": hwL2VlanIpSubnetVlanIpAddress,
       "hwL2VlanIpSubnetVlanIpSubnetMask": hwL2VlanIpSubnetVlanIpSubnetMask,
       "hwL2VlanIpSubnetVlanPriority": hwL2VlanIpSubnetVlanPriority,
       "hwL2VlanIpSubnetVlanRowStatus": hwL2VlanIpSubnetVlanRowStatus,
       "hwL2VlanMacVlanTable": hwL2VlanMacVlanTable,
       "hwL2VlanMacVlanEntry": hwL2VlanMacVlanEntry,
       "hwL2VlanMacVlanVlanId": hwL2VlanMacVlanVlanId,
       "hwL2VlanMacVlanMac": hwL2VlanMacVlanMac,
       "hwL2VlanMacVlanVlanPriority": hwL2VlanMacVlanVlanPriority,
       "hwL2VlanMacVlanMacRowStatus": hwL2VlanMacVlanMacRowStatus,
       "hwL2VlanProtocolVlanTable": hwL2VlanProtocolVlanTable,
       "hwL2VlanProtocolVlanEntry": hwL2VlanProtocolVlanEntry,
       "hwL2VlanProtocolVlanVlanId": hwL2VlanProtocolVlanVlanId,
       "hwL2VlanProtocolVlanProtocolIndex": hwL2VlanProtocolVlanProtocolIndex,
       "hwL2VlanProtocolVlanProtocolType": hwL2VlanProtocolVlanProtocolType,
       "hwL2VlanProtocolVlanEncapType": hwL2VlanProtocolVlanEncapType,
       "hwL2VlanProtocolVlanRowStatus": hwL2VlanProtocolVlanRowStatus,
       "hwL2VlanPolicyVlanTable": hwL2VlanPolicyVlanTable,
       "hwL2VlanPolicyVlanEntry": hwL2VlanPolicyVlanEntry,
       "hwL2VlanPolicyVlanMac": hwL2VlanPolicyVlanMac,
       "hwL2VlanPolicyVlanIp": hwL2VlanPolicyVlanIp,
       "hwL2VlanPolicyVlanPort": hwL2VlanPolicyVlanPort,
       "hwL2VlanPolicyVlanVlanId": hwL2VlanPolicyVlanVlanId,
       "hwL2VlanPolicyVlanVlanPriority": hwL2VlanPolicyVlanVlanPriority,
       "hwL2VlanPolicyVlanRowStatus": hwL2VlanPolicyVlanRowStatus,
       "hwL2VlanVoiceVlanEnabledVlanId": hwL2VlanVoiceVlanEnabledVlanId,
       "hwL2VlanVoiceVlanAgingTime": hwL2VlanVoiceVlanAgingTime,
       "hwL2VlanVoiceVlanSecurityMode": hwL2VlanVoiceVlanSecurityMode,
       "hwL2VlanVoiceVlanPortTable": hwL2VlanVoiceVlanPortTable,
       "hwL2VlanVoiceVlanPortEntry": hwL2VlanVoiceVlanPortEntry,
       "hwL2VlanVoiceVlanPortIndex": hwL2VlanVoiceVlanPortIndex,
       "hwL2VlanVoiceVlanPortEnable": hwL2VlanVoiceVlanPortEnable,
       "hwL2VlanVoiceVlanPortMode": hwL2VlanVoiceVlanPortMode,
       "hwL2VlanVoiceVlanPortLegacy": hwL2VlanVoiceVlanPortLegacy,
       "hwL2VlanVoiceVlanPortSecurityMode": hwL2VlanVoiceVlanPortSecurityMode,
       "hwL2VlanVoiceVlanOuiTable": hwL2VlanVoiceVlanOuiTable,
       "hwL2VlanVoiceVlanOuiEntry": hwL2VlanVoiceVlanOuiEntry,
       "hwL2VlanVoiceVlanOuiAddress": hwL2VlanVoiceVlanOuiAddress,
       "hwL2VlanVoiceVlanOuiMask": hwL2VlanVoiceVlanOuiMask,
       "hwL2VlanVoiceVlanOuiDescription": hwL2VlanVoiceVlanOuiDescription,
       "hwL2VlanVoiceVlanOuiRowStatus": hwL2VlanVoiceVlanOuiRowStatus,
       "hwL2VlanMappingMultiTable": hwL2VlanMappingMultiTable,
       "hwL2VlanMappingMultiEntry": hwL2VlanMappingMultiEntry,
       "hwL2VlanMappingMultiPortIndex": hwL2VlanMappingMultiPortIndex,
       "hwL2VlanMappingMultiDirection": hwL2VlanMappingMultiDirection,
       "hwL2VlanMappingMultiVlanId": hwL2VlanMappingMultiVlanId,
       "hwL2VlanMappingMultiVlan8021p": hwL2VlanMappingMultiVlan8021p,
       "hwL2VlanMappingMultiVlanListLow": hwL2VlanMappingMultiVlanListLow,
       "hwL2VlanMappingMultiVlanListHigh": hwL2VlanMappingMultiVlanListHigh,
       "hwL2VlanMappingMultiRowStatus": hwL2VlanMappingMultiRowStatus,
       "hwL2VlanMacVlanNewTable": hwL2VlanMacVlanNewTable,
       "hwL2VlanMacVlanNewEntry": hwL2VlanMacVlanNewEntry,
       "hwL2VlanMacVlanNewMac": hwL2VlanMacVlanNewMac,
       "hwL2VlanMacVlanNewVlanId": hwL2VlanMacVlanNewVlanId,
       "hwL2VlanMacVlanNewVlanPriority": hwL2VlanMacVlanNewVlanPriority,
       "hwL2VlanMacVlanNewMacRowStatus": hwL2VlanMacVlanNewMacRowStatus,
       "hwL2VlanProtocolVlanNewTable": hwL2VlanProtocolVlanNewTable,
       "hwL2VlanProtocolVlanNewEntry": hwL2VlanProtocolVlanNewEntry,
       "hwL2VlanProtocolVlanNewVlanId": hwL2VlanProtocolVlanNewVlanId,
       "hwL2VlanProtocolVlanNewProtocolIndex": hwL2VlanProtocolVlanNewProtocolIndex,
       "hwL2VlanProtocolVlanNewProtocolType": hwL2VlanProtocolVlanNewProtocolType,
       "hwL2VlanProtocolVlanNewProtocolTypeValue": hwL2VlanProtocolVlanNewProtocolTypeValue,
       "hwL2VlanProtocolVlanNewRowStatus": hwL2VlanProtocolVlanNewRowStatus,
       "hwL2VlanPolicyVlanNewTable": hwL2VlanPolicyVlanNewTable,
       "hwL2VlanPolicyVlanNewEntry": hwL2VlanPolicyVlanNewEntry,
       "hwL2VlanPolicyVlanNewMac": hwL2VlanPolicyVlanNewMac,
       "hwL2VlanPolicyVlanNewIp": hwL2VlanPolicyVlanNewIp,
       "hwL2VlanPolicyVlanNewPort": hwL2VlanPolicyVlanNewPort,
       "hwL2VlanPolicyVlanNewVlanId": hwL2VlanPolicyVlanNewVlanId,
       "hwL2VlanPolicyVlanNewVlanPriority": hwL2VlanPolicyVlanNewVlanPriority,
       "hwL2VlanPolicyVlanNewRowStatus": hwL2VlanPolicyVlanNewRowStatus,
       "hwL2VlanProtocolVlanPortNewTable": hwL2VlanProtocolVlanPortNewTable,
       "hwL2VlanProtocolVlanPortNewEntry": hwL2VlanProtocolVlanPortNewEntry,
       "hwL2VlanProtocolVlanPortNewIndex": hwL2VlanProtocolVlanPortNewIndex,
       "hwL2VlanProtocolVlanPortNewVlanId": hwL2VlanProtocolVlanPortNewVlanId,
       "hwL2VlanProtocolVlanPortNewProtocolIndex": hwL2VlanProtocolVlanPortNewProtocolIndex,
       "hwL2VlanProtocolVlanPortNewPriority": hwL2VlanProtocolVlanPortNewPriority,
       "hwL2VlanProtocolVlanPortNewRowStatus": hwL2VlanProtocolVlanPortNewRowStatus,
       "hwL2VlanMultiVoiceVlanPortTable": hwL2VlanMultiVoiceVlanPortTable,
       "hwL2VlanMultiVoiceVlanPortEntry": hwL2VlanMultiVoiceVlanPortEntry,
       "hwL2VlanMultiVoiceVlanIfIndex": hwL2VlanMultiVoiceVlanIfIndex,
       "hwL2VlanMultiVoiceVlanPortVLanId": hwL2VlanMultiVoiceVlanPortVLanId,
       "hwL2VlanMultiVoiceVlanPortRowStatus": hwL2VlanMultiVoiceVlanPortRowStatus,
       "hwL2VlanSwitchExtTable": hwL2VlanSwitchExtTable,
       "hwL2VlanSwitchExtEntry": hwL2VlanSwitchExtEntry,
       "hwL2VlanSwitchExtName": hwL2VlanSwitchExtName,
       "hwL2VlanSwitchExtSrcIfIndex": hwL2VlanSwitchExtSrcIfIndex,
       "hwL2VlanSwitchExtOuterVlanId": hwL2VlanSwitchExtOuterVlanId,
       "hwL2VlanSwitchExtVlanListLow": hwL2VlanSwitchExtVlanListLow,
       "hwL2VlanSwitchExtVlanListHigh": hwL2VlanSwitchExtVlanListHigh,
       "hwL2VlanSwitchExtDstIfIndex": hwL2VlanSwitchExtDstIfIndex,
       "hwL2VlanSwitchExtVlanXlateAction": hwL2VlanSwitchExtVlanXlateAction,
       "hwL2VlanSwitchExtDstVlan": hwL2VlanSwitchExtDstVlan,
       "hwL2VlanSwitchExtDstInnerVlan": hwL2VlanSwitchExtDstInnerVlan,
       "hwL2VlanSwitchExtRemark": hwL2VlanSwitchExtRemark,
       "hwL2VlanSwitchExtRemarkReverse": hwL2VlanSwitchExtRemarkReverse,
       "hwL2VlanSwitchExtLinkStatus": hwL2VlanSwitchExtLinkStatus,
       "hwL2VlanSwitchExtRowStatus": hwL2VlanSwitchExtRowStatus,
       "hwL2VlanPrecedence": hwL2VlanPrecedence,
       "hwL2VlanXlateTable": hwL2VlanXlateTable,
       "hwL2VlanXlateEntry": hwL2VlanXlateEntry,
       "hwL2VlanXlateInterfaceIndex": hwL2VlanXlateInterfaceIndex,
       "hwL2VlanXlateVlanIdBegin": hwL2VlanXlateVlanIdBegin,
       "hwL2VlanXlateVlanIdEnd": hwL2VlanXlateVlanIdEnd,
       "hwL2VlanXlateOuterVlanId": hwL2VlanXlateOuterVlanId,
       "hwL2VlanXlateVlan8021p": hwL2VlanXlateVlan8021p,
       "hwL2VlanXlateDirection": hwL2VlanXlateDirection,
       "hwL2VlanXlateAction": hwL2VlanXlateAction,
       "hwL2VlanXlateToVlanId": hwL2VlanXlateToVlanId,
       "hwL2VlanXlateToinnerVlanId": hwL2VlanXlateToinnerVlanId,
       "hwL2VlanXlateremark": hwL2VlanXlateremark,
       "hwL2VlanXlateRowStatus": hwL2VlanXlateRowStatus,
       "hwL2QinQVlanTable": hwL2QinQVlanTable,
       "hwL2QinQVlanEntry": hwL2QinQVlanEntry,
       "hwL2QinQVlanIfIndex": hwL2QinQVlanIfIndex,
       "hwL2QinQVlanIdBegin": hwL2QinQVlanIdBegin,
       "hwL2QinQVlanIdEnd": hwL2QinQVlanIdEnd,
       "hwL2QinQVlanInnerVlanIdBegin": hwL2QinQVlanInnerVlanIdBegin,
       "hwL2QinQVlanInnerVlanIdEnd": hwL2QinQVlanInnerVlanIdEnd,
       "hwL2QinQVlan8021pBegin": hwL2QinQVlan8021pBegin,
       "hwL2QinQVlan8021pEnd": hwL2QinQVlan8021pEnd,
       "hwL2QinQVlanEtherType": hwL2QinQVlanEtherType,
       "hwL2QinQVlanMode": hwL2QinQVlanMode,
       "hwL2QinQVlanChangedVlanId": hwL2QinQVlanChangedVlanId,
       "hwL2QinQVlanChangedInnerVlanId": hwL2QinQVlanChangedInnerVlanId,
       "hwL2QinQVlanRemark": hwL2QinQVlanRemark,
       "hwL2QinQVlanMapStackVlanId": hwL2QinQVlanMapStackVlanId,
       "hwL2QinQVlanRowStatus": hwL2QinQVlanRowStatus,
       "hwL2UntagAddDTagTable": hwL2UntagAddDTagTable,
       "hwL2UntagAddDTagEntry": hwL2UntagAddDTagEntry,
       "hwL2UntagAddDTagPortIndex": hwL2UntagAddDTagPortIndex,
       "hwL2UntagAddDTagOuterVlanId": hwL2UntagAddDTagOuterVlanId,
       "hwL2UntagAddDTagInnerVlanId": hwL2UntagAddDTagInnerVlanId,
       "hwL2UntagAddDTagRowStatus": hwL2UntagAddDTagRowStatus,
       "hwL2VlanVoiceVlan8021p": hwL2VlanVoiceVlan8021p,
       "hwL2VlanVoiceVlanDscp": hwL2VlanVoiceVlanDscp,
       "hwL2VlanStatistics": hwL2VlanStatistics,
       "hwL2IfStatVlanCfgTable": hwL2IfStatVlanCfgTable,
       "hwL2IfStatVlanCfgEntry": hwL2IfStatVlanCfgEntry,
       "hwL2IfStatVlanCfgPortIndex": hwL2IfStatVlanCfgPortIndex,
       "hwL2IfStatVlanCfgVlanId": hwL2IfStatVlanCfgVlanId,
       "hwL2IfStatVlanCfgEnableFlag": hwL2IfStatVlanCfgEnableFlag,
       "hwL2IfStatVlanCfgRowStatus": hwL2IfStatVlanCfgRowStatus,
       "hwL2IfStat8021pCfgTable": hwL2IfStat8021pCfgTable,
       "hwL2IfStat8021pCfgEntry": hwL2IfStat8021pCfgEntry,
       "hwL2IfStat8021pCfgPortIndex": hwL2IfStat8021pCfgPortIndex,
       "hwL2IfStat8021pCfg8021p": hwL2IfStat8021pCfg8021p,
       "hwL2IfStat8021pCfgEnableFlag": hwL2IfStat8021pCfgEnableFlag,
       "hwL2IfStat8021pCfgRowStatus": hwL2IfStat8021pCfgRowStatus,
       "hwL2IfStat8021pAndVlanCfgTable": hwL2IfStat8021pAndVlanCfgTable,
       "hwL2IfStat8021pAndVlanCfgEntry": hwL2IfStat8021pAndVlanCfgEntry,
       "hwL2IfStat8021pAndVlanCfgPortIndex": hwL2IfStat8021pAndVlanCfgPortIndex,
       "hwL2IfStat8021pAndVlanCfgVlanId": hwL2IfStat8021pAndVlanCfgVlanId,
       "hwL2IfStat8021pAndVlanCfg8021p": hwL2IfStat8021pAndVlanCfg8021p,
       "hwL2IfStat8021pAndVlanCfgEnableFlag": hwL2IfStat8021pAndVlanCfgEnableFlag,
       "hwL2IfStat8021pAndVlanCfgRowStatus": hwL2IfStat8021pAndVlanCfgRowStatus,
       "hwL2VlanStatTable": hwL2VlanStatTable,
       "hwL2VlanStatEntry": hwL2VlanStatEntry,
       "hwL2VlanStatVlanId": hwL2VlanStatVlanId,
       "hwL2VlanStatInTotalPkts": hwL2VlanStatInTotalPkts,
       "hwL2VlanStatInTotalBytes": hwL2VlanStatInTotalBytes,
       "hwL2VlanStatOutTotalPkts": hwL2VlanStatOutTotalPkts,
       "hwL2VlanStatOutTotalBytes": hwL2VlanStatOutTotalBytes,
       "hwL2VlanStatUnknownUcastDiscardPkts": hwL2VlanStatUnknownUcastDiscardPkts,
       "hwL2VlanStatUnknownMcastDiscardPkts": hwL2VlanStatUnknownMcastDiscardPkts,
       "hwL2VlanStatBcastDiscardPkts": hwL2VlanStatBcastDiscardPkts,
       "hwL2VlanStatInUcastPkts": hwL2VlanStatInUcastPkts,
       "hwL2VlanStatInUcastBytes": hwL2VlanStatInUcastBytes,
       "hwL2VlanStatOutUcastPkts": hwL2VlanStatOutUcastPkts,
       "hwL2VlanStatOutUcastBytes": hwL2VlanStatOutUcastBytes,
       "hwL2VlanStatInMcastPkts": hwL2VlanStatInMcastPkts,
       "hwL2VlanStatInMcastBytes": hwL2VlanStatInMcastBytes,
       "hwL2VlanStatOutMcastPkts": hwL2VlanStatOutMcastPkts,
       "hwL2VlanStatOutMcastBytes": hwL2VlanStatOutMcastBytes,
       "hwL2VlanStatInBcastPkts": hwL2VlanStatInBcastPkts,
       "hwL2VlanStatInBcastBytes": hwL2VlanStatInBcastBytes,
       "hwL2VlanStatOutBcastPkts": hwL2VlanStatOutBcastPkts,
       "hwL2VlanStatOutBcastBytes": hwL2VlanStatOutBcastBytes,
       "hwL2VlanStatResetFlag": hwL2VlanStatResetFlag,
       "hwL2IfStatVlanTable": hwL2IfStatVlanTable,
       "hwL2IfStatVlanEntry": hwL2IfStatVlanEntry,
       "hwL2IfStatVlanPortIndex": hwL2IfStatVlanPortIndex,
       "hwL2IfStatVlanId": hwL2IfStatVlanId,
       "hwL2IfStatVlanInTotalPkts": hwL2IfStatVlanInTotalPkts,
       "hwL2IfStatVlanInTotalBytes": hwL2IfStatVlanInTotalBytes,
       "hwL2IfStatVlanOutTotalPkts": hwL2IfStatVlanOutTotalPkts,
       "hwL2IfStatVlanOutTotalBytes": hwL2IfStatVlanOutTotalBytes,
       "hwL2IfStatVlanInPktsRate": hwL2IfStatVlanInPktsRate,
       "hwL2IfStatVlanInBytesRate": hwL2IfStatVlanInBytesRate,
       "hwL2IfStatVlanOutPktsRate": hwL2IfStatVlanOutPktsRate,
       "hwL2IfStatVlanOutBytesRate": hwL2IfStatVlanOutBytesRate,
       "hwL2IfStatVlanInUcastPkts": hwL2IfStatVlanInUcastPkts,
       "hwL2IfStatVlanInUcastBytes": hwL2IfStatVlanInUcastBytes,
       "hwL2IfStatVlanOutUcastPkts": hwL2IfStatVlanOutUcastPkts,
       "hwL2IfStatVlanOutUcastBytes": hwL2IfStatVlanOutUcastBytes,
       "hwL2IfStatVlanInMcastPkts": hwL2IfStatVlanInMcastPkts,
       "hwL2IfStatVlanInMcastBytes": hwL2IfStatVlanInMcastBytes,
       "hwL2IfStatVlanOutMcastPkts": hwL2IfStatVlanOutMcastPkts,
       "hwL2IfStatVlanOutMcastBytes": hwL2IfStatVlanOutMcastBytes,
       "hwL2IfStatVlanInBcastPkts": hwL2IfStatVlanInBcastPkts,
       "hwL2IfStatVlanInBcastBytes": hwL2IfStatVlanInBcastBytes,
       "hwL2IfStatVlanOutBcastPkts": hwL2IfStatVlanOutBcastPkts,
       "hwL2IfStatVlanOutBcastBytes": hwL2IfStatVlanOutBcastBytes,
       "hwL2IfStatVlanResetFlag": hwL2IfStatVlanResetFlag,
       "hwL2IfStat8021pTable": hwL2IfStat8021pTable,
       "hwL2IfStat8021pEntry": hwL2IfStat8021pEntry,
       "hwL2IfStat8021pPortIndex": hwL2IfStat8021pPortIndex,
       "hwL2IfStat8021p": hwL2IfStat8021p,
       "hwL2IfStat8021pInTotalPkts": hwL2IfStat8021pInTotalPkts,
       "hwL2IfStat8021pInTotalBytes": hwL2IfStat8021pInTotalBytes,
       "hwL2IfStat8021pOutTotalPkts": hwL2IfStat8021pOutTotalPkts,
       "hwL2IfStat8021pOutTotalBytes": hwL2IfStat8021pOutTotalBytes,
       "hwL2IfStat8021pInPktsRate": hwL2IfStat8021pInPktsRate,
       "hwL2IfStat8021pInBytsRate": hwL2IfStat8021pInBytsRate,
       "hwL2IfStat8021pOutPktsRate": hwL2IfStat8021pOutPktsRate,
       "hwL2IfStat8021pOutBytesRate": hwL2IfStat8021pOutBytesRate,
       "hwL2IfStat8021pResetFlag": hwL2IfStat8021pResetFlag,
       "hwL2IfStat8021pAndVlanTable": hwL2IfStat8021pAndVlanTable,
       "hwL2IfStat8021pAndVlanEntry": hwL2IfStat8021pAndVlanEntry,
       "hwL2IfStat8021pAndVlanPortIndex": hwL2IfStat8021pAndVlanPortIndex,
       "hwL2IfStat8021pAndVlanVlanId": hwL2IfStat8021pAndVlanVlanId,
       "hwL2IfStat8021pAndVlan8021p": hwL2IfStat8021pAndVlan8021p,
       "hwL2IfStat8021pAndVlanInTotalPkts": hwL2IfStat8021pAndVlanInTotalPkts,
       "hwL2IfStat8021pAndVlanInTotalBytes": hwL2IfStat8021pAndVlanInTotalBytes,
       "hwL2IfStat8021pAndVlanInPktsRate": hwL2IfStat8021pAndVlanInPktsRate,
       "hwL2IfStat8021pAndVlanInBytsRate": hwL2IfStat8021pAndVlanInBytsRate,
       "hwL2IfStat8021pAndVlanResetFlag": hwL2IfStat8021pAndVlanResetFlag,
       "hwL2VlanSwitchPSTable": hwL2VlanSwitchPSTable,
       "hwL2VlanSwitchPSEntry": hwL2VlanSwitchPSEntry,
       "hwL2VlanSwitchPSIfIndex": hwL2VlanSwitchPSIfIndex,
       "hwL2VlanSwitchPSSVlanId": hwL2VlanSwitchPSSVlanId,
       "hwL2VlanSwitchPSCVlanId": hwL2VlanSwitchPSCVlanId,
       "hwL2VlanSwitchPSInputPkts": hwL2VlanSwitchPSInputPkts,
       "hwL2VlanSwitchPSInputBytes": hwL2VlanSwitchPSInputBytes,
       "hwL2VlanSwitchPSOutputPkts": hwL2VlanSwitchPSOutputPkts,
       "hwL2VlanSwitchPSOutputBytes": hwL2VlanSwitchPSOutputBytes,
       "hwL2VlanSwitchPSResetFlag": hwL2VlanSwitchPSResetFlag,
       "hwL2VlanSwitchPSEnableFlag": hwL2VlanSwitchPSEnableFlag,
       "hwL2VlanTraps": hwL2VlanTraps,
       "hwL2VlanUnkownPacketAlarm": hwL2VlanUnkownPacketAlarm,
       "hwL2vlanConformance": hwL2vlanConformance,
       "hwL2vlanGroups": hwL2vlanGroups,
       "hwL2VlanMIBTableGroup": hwL2VlanMIBTableGroup,
       "hwL2vlanStackingGroup": hwL2vlanStackingGroup,
       "hwL2vlanMappingGroup": hwL2vlanMappingGroup,
       "hwSupervlanGroup": hwSupervlanGroup,
       "hwL2InterfIsolateGroup": hwL2InterfIsolateGroup,
       "hwL2IsolatemappingGroup": hwL2IsolatemappingGroup,
       "hwL2VlanStackingExtGroup": hwL2VlanStackingExtGroup,
       "hwL2vlanQinQGroup": hwL2vlanQinQGroup,
       "hwL2vlanQinQInterfaceGroup": hwL2vlanQinQInterfaceGroup,
       "hwL2DVlanMappingGroup": hwL2DVlanMappingGroup,
       "hwL2VlanStackingAdvGroup": hwL2VlanStackingAdvGroup,
       "hwL2VlanMappingAdvGroup": hwL2VlanMappingAdvGroup,
       "hwL2VlanSwitchGroup": hwL2VlanSwitchGroup,
       "hwL2IfStatVlanCfgGroup": hwL2IfStatVlanCfgGroup,
       "hwL2IfStat8021pCfgGroup": hwL2IfStat8021pCfgGroup,
       "hwL2IfStat8021pAndVlanCfgGroup": hwL2IfStat8021pAndVlanCfgGroup,
       "hwL2VlanStatGroup": hwL2VlanStatGroup,
       "hwL2IfStatVlanGroup": hwL2IfStatVlanGroup,
       "hwL2IfStat8021pGroup": hwL2IfStat8021pGroup,
       "hwL2IfStat8021pAndVlanGroup": hwL2IfStat8021pAndVlanGroup,
       "hwL2VlanMappingExtGroup": hwL2VlanMappingExtGroup,
       "hwL2VlanQinqVlanTransEnaGroup": hwL2VlanQinqVlanTransEnaGroup,
       "hwL2VlanQinqVlanTransMissDropGroup": hwL2VlanQinqVlanTransMissDropGroup,
       "hwL2VlanViewMappingGroup": hwL2VlanViewMappingGroup,
       "hwL2VlanStackingMaskGroup": hwL2VlanStackingMaskGroup,
       "hwL2VlanIpSubnetVlanGroup": hwL2VlanIpSubnetVlanGroup,
       "hwL2VlanMacVlanGroup": hwL2VlanMacVlanGroup,
       "hwL2VlanProtocolVlanGroup": hwL2VlanProtocolVlanGroup,
       "hwL2VlanPolicyVlanGroup": hwL2VlanPolicyVlanGroup,
       "hwL2VlanVoiceVlanGroup": hwL2VlanVoiceVlanGroup,
       "hwL2VlanMappingMultiGroup": hwL2VlanMappingMultiGroup,
       "hwL2VlanSwitchPSGroup": hwL2VlanSwitchPSGroup,
       "hwL2VlanMacVlanNewGroup": hwL2VlanMacVlanNewGroup,
       "hwL2VlanProtocolVlanNewGroup": hwL2VlanProtocolVlanNewGroup,
       "hwL2VlanPolicyVlanNewGroup": hwL2VlanPolicyVlanNewGroup,
       "hwL2VlanProtocolVlanPortNewGroup": hwL2VlanProtocolVlanPortNewGroup,
       "hwL2VlanMultiVoiceVlanPortGroup": hwL2VlanMultiVoiceVlanPortGroup,
       "hwL2VlanPrecedenceGroup": hwL2VlanPrecedenceGroup,
       "hwL2VlanXlateGroup": hwL2VlanXlateGroup,
       "hwL2VlanSwitchExtGroup": hwL2VlanSwitchExtGroup,
       "hwL2QinQVlanGroup": hwL2QinQVlanGroup,
       "hwL2UntagAddDTagGroup": hwL2UntagAddDTagGroup,
       "hwL2vlanCompliances": hwL2vlanCompliances,
       "hwL2vlanCompliance": hwL2vlanCompliance,
       "hwL2VlanTrapsGroups": hwL2VlanTrapsGroups,
       "hwL2VlanTrapsGroup": hwL2VlanTrapsGroup}
)
