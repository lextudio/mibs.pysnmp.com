# SNMP MIB module (HUAWEI-LswVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:04 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

(PortList,
 hwifVLANTrunkStatusEntry) = mibBuilder.importSymbols(
    "HUAWEI-LswINF-MIB",
    "PortList",
    "hwifVLANTrunkStatusEntry")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

hwLswVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwVlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_HwLswVlanMngObject_ObjectIdentity = ObjectIdentity
hwLswVlanMngObject = _HwLswVlanMngObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwLswVlanMngObject.setStatus("current")
_Hwdot1qVlanMIBTable_Object = MibTable
hwdot1qVlanMIBTable = _Hwdot1qVlanMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwdot1qVlanMIBTable.setStatus("current")
_Hwdot1qVlanMIBEntry_Object = MibTableRow
hwdot1qVlanMIBEntry = _Hwdot1qVlanMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1)
)
hwdot1qVlanMIBEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hwdot1qVlanMIBEntry.setStatus("current")
_Hwdot1qVlanIndex_Type = HwVlanIndex
_Hwdot1qVlanIndex_Object = MibTableColumn
hwdot1qVlanIndex = _Hwdot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 1),
    _Hwdot1qVlanIndex_Type()
)
hwdot1qVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanIndex.setStatus("current")


class _Hwdot1qVlanName_Type(SnmpAdminString):
    """Custom type hwdot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hwdot1qVlanName_Type.__name__ = "SnmpAdminString"
_Hwdot1qVlanName_Object = MibTableColumn
hwdot1qVlanName = _Hwdot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 2),
    _Hwdot1qVlanName_Type()
)
hwdot1qVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanName.setStatus("current")
_Hwdot1qVlanPorts_Type = PortList
_Hwdot1qVlanPorts_Object = MibTableColumn
hwdot1qVlanPorts = _Hwdot1qVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 3),
    _Hwdot1qVlanPorts_Type()
)
hwdot1qVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanPorts.setStatus("current")


class _Hwdot1qVlanType_Type(Integer32):
    """Custom type hwdot1qVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("common-vlan", 2),
          ("isolate-user-vlan", 4),
          ("secondary-vlan", 5),
          ("sub-vlan", 3),
          ("superVlan", 1))
    )


_Hwdot1qVlanType_Type.__name__ = "Integer32"
_Hwdot1qVlanType_Object = MibTableColumn
hwdot1qVlanType = _Hwdot1qVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 4),
    _Hwdot1qVlanType_Type()
)
hwdot1qVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanType.setStatus("current")
_Hwdot1qVlanMacFilter_Type = TruthValue
_Hwdot1qVlanMacFilter_Object = MibTableColumn
hwdot1qVlanMacFilter = _Hwdot1qVlanMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 5),
    _Hwdot1qVlanMacFilter_Type()
)
hwdot1qVlanMacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanMacFilter.setStatus("current")
_Hwdot1qVlanMcastUnknownProtos_Type = TruthValue
_Hwdot1qVlanMcastUnknownProtos_Object = MibTableColumn
hwdot1qVlanMcastUnknownProtos = _Hwdot1qVlanMcastUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 6),
    _Hwdot1qVlanMcastUnknownProtos_Type()
)
hwdot1qVlanMcastUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanMcastUnknownProtos.setStatus("current")
_HwExistInterface_Type = TruthValue
_HwExistInterface_Object = MibTableColumn
hwExistInterface = _HwExistInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 7),
    _HwExistInterface_Type()
)
hwExistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExistInterface.setStatus("current")
_HwVlanInterfaceIndex_Type = Integer32
_HwVlanInterfaceIndex_Object = MibTableColumn
hwVlanInterfaceIndex = _HwVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 8),
    _HwVlanInterfaceIndex_Type()
)
hwVlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceIndex.setStatus("current")
_Hwdot1qVlanMacLearn_Type = TruthValue
_Hwdot1qVlanMacLearn_Object = MibTableColumn
hwdot1qVlanMacLearn = _Hwdot1qVlanMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 9),
    _Hwdot1qVlanMacLearn_Type()
)
hwdot1qVlanMacLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanMacLearn.setStatus("current")


class _Hwdot1qVlanStatus_Type(Integer32):
    """Custom type hwdot1qVlanStatus based on Integer32"""
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


_Hwdot1qVlanStatus_Type.__name__ = "Integer32"
_Hwdot1qVlanStatus_Object = MibTableColumn
hwdot1qVlanStatus = _Hwdot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 10),
    _Hwdot1qVlanStatus_Type()
)
hwdot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanStatus.setStatus("current")
_Hwdot1qVlanCreationTime_Type = TimeTicks
_Hwdot1qVlanCreationTime_Object = MibTableColumn
hwdot1qVlanCreationTime = _Hwdot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 11),
    _Hwdot1qVlanCreationTime_Type()
)
hwdot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanCreationTime.setStatus("current")


class _Hwdot1qVlanPriority_Type(Integer32):
    """Custom type hwdot1qVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hwdot1qVlanPriority_Type.__name__ = "Integer32"
_Hwdot1qVlanPriority_Object = MibTableColumn
hwdot1qVlanPriority = _Hwdot1qVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 12),
    _Hwdot1qVlanPriority_Type()
)
hwdot1qVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanPriority.setStatus("current")
_Hwdot1qVlanRowStatus_Type = RowStatus
_Hwdot1qVlanRowStatus_Object = MibTableColumn
hwdot1qVlanRowStatus = _Hwdot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 13),
    _Hwdot1qVlanRowStatus_Type()
)
hwdot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwdot1qVlanRowStatus.setStatus("current")


class _Hwdot1qVlanBroadcastSuppression_Type(Integer32):
    """Custom type hwdot1qVlanBroadcastSuppression based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hwdot1qVlanBroadcastSuppression_Type.__name__ = "Integer32"
_Hwdot1qVlanBroadcastSuppression_Object = MibTableColumn
hwdot1qVlanBroadcastSuppression = _Hwdot1qVlanBroadcastSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 14),
    _Hwdot1qVlanBroadcastSuppression_Type()
)
hwdot1qVlanBroadcastSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanBroadcastSuppression.setStatus("current")


class _Hwdot1qVlanBcastSuppressionPPS_Type(Integer32):
    """Custom type hwdot1qVlanBcastSuppressionPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 148800),
    )


_Hwdot1qVlanBcastSuppressionPPS_Type.__name__ = "Integer32"
_Hwdot1qVlanBcastSuppressionPPS_Object = MibTableColumn
hwdot1qVlanBcastSuppressionPPS = _Hwdot1qVlanBcastSuppressionPPS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 15),
    _Hwdot1qVlanBcastSuppressionPPS_Type()
)
hwdot1qVlanBcastSuppressionPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanBcastSuppressionPPS.setStatus("current")


class _Hwdot1qVlanMulticast_Type(Integer32):
    """Custom type hwdot1qVlanMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Hwdot1qVlanMulticast_Type.__name__ = "Integer32"
_Hwdot1qVlanMulticast_Object = MibTableColumn
hwdot1qVlanMulticast = _Hwdot1qVlanMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 16),
    _Hwdot1qVlanMulticast_Type()
)
hwdot1qVlanMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanMulticast.setStatus("current")
_Hwdot1qVlanTaggedPorts_Type = PortList
_Hwdot1qVlanTaggedPorts_Object = MibTableColumn
hwdot1qVlanTaggedPorts = _Hwdot1qVlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 17),
    _Hwdot1qVlanTaggedPorts_Type()
)
hwdot1qVlanTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanTaggedPorts.setStatus("current")
_Hwdot1qVlanUntaggedPorts_Type = PortList
_Hwdot1qVlanUntaggedPorts_Object = MibTableColumn
hwdot1qVlanUntaggedPorts = _Hwdot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 18),
    _Hwdot1qVlanUntaggedPorts_Type()
)
hwdot1qVlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanUntaggedPorts.setStatus("current")
_Hwdot1qVlanPortIndexs_Type = OctetString
_Hwdot1qVlanPortIndexs_Object = MibTableColumn
hwdot1qVlanPortIndexs = _Hwdot1qVlanPortIndexs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 1, 1, 19),
    _Hwdot1qVlanPortIndexs_Type()
)
hwdot1qVlanPortIndexs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanPortIndexs.setStatus("current")
_HwVlanInterfaceTable_Object = MibTable
hwVlanInterfaceTable = _HwVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwVlanInterfaceTable.setStatus("current")
_HwVlanInterfaceEntry_Object = MibTableRow
hwVlanInterfaceEntry = _HwVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1)
)
hwVlanInterfaceEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceID"),
)
if mibBuilder.loadTexts:
    hwVlanInterfaceEntry.setStatus("current")
_HwVlanInterfaceID_Type = Integer32
_HwVlanInterfaceID_Object = MibTableColumn
hwVlanInterfaceID = _HwVlanInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 1),
    _HwVlanInterfaceID_Type()
)
hwVlanInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceID.setStatus("current")
_Hwdot1qVlanID_Type = HwVlanIndex
_Hwdot1qVlanID_Object = MibTableColumn
hwdot1qVlanID = _Hwdot1qVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 2),
    _Hwdot1qVlanID_Type()
)
hwdot1qVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanID.setStatus("current")
_Hwdot1qVlanIpAddress_Type = IpAddress
_Hwdot1qVlanIpAddress_Object = MibTableColumn
hwdot1qVlanIpAddress = _Hwdot1qVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 3),
    _Hwdot1qVlanIpAddress_Type()
)
hwdot1qVlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanIpAddress.setStatus("current")
_Hwdot1qVlanIpAddressMask_Type = IpAddress
_Hwdot1qVlanIpAddressMask_Object = MibTableColumn
hwdot1qVlanIpAddressMask = _Hwdot1qVlanIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 4),
    _Hwdot1qVlanIpAddressMask_Type()
)
hwdot1qVlanIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanIpAddressMask.setStatus("current")


class _HwVlanInterfaceAdminStatus_Type(Integer32):
    """Custom type hwVlanInterfaceAdminStatus based on Integer32"""
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


_HwVlanInterfaceAdminStatus_Type.__name__ = "Integer32"
_HwVlanInterfaceAdminStatus_Object = MibTableColumn
hwVlanInterfaceAdminStatus = _HwVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 5),
    _HwVlanInterfaceAdminStatus_Type()
)
hwVlanInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceAdminStatus.setStatus("current")


class _HwVlanInterfaceFrameType_Type(Integer32):
    """Custom type hwVlanInterfaceFrameType based on Integer32"""
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
        *(("ethernet-8022", 3),
          ("ethernet-8023", 4),
          ("ethernet-ii", 1),
          ("ethernet-snap", 2))
    )


_HwVlanInterfaceFrameType_Type.__name__ = "Integer32"
_HwVlanInterfaceFrameType_Object = MibTableColumn
hwVlanInterfaceFrameType = _HwVlanInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 6),
    _HwVlanInterfaceFrameType_Type()
)
hwVlanInterfaceFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceFrameType.setStatus("current")
_HwInterfaceRowStatus_Type = RowStatus
_HwInterfaceRowStatus_Object = MibTableColumn
hwInterfaceRowStatus = _HwInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 7),
    _HwInterfaceRowStatus_Type()
)
hwInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwInterfaceRowStatus.setStatus("current")


class _HwVlanInterfaceIpMethod_Type(Integer32):
    """Custom type hwVlanInterfaceIpMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("assigned-ip", 1),
          ("bootp-ip", 3),
          ("dhcp-ip", 2))
    )


_HwVlanInterfaceIpMethod_Type.__name__ = "Integer32"
_HwVlanInterfaceIpMethod_Object = MibTableColumn
hwVlanInterfaceIpMethod = _HwVlanInterfaceIpMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 8),
    _HwVlanInterfaceIpMethod_Type()
)
hwVlanInterfaceIpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpMethod.setStatus("current")
_HwVlanInterfaceIfIndex_Type = Integer32
_HwVlanInterfaceIfIndex_Object = MibTableColumn
hwVlanInterfaceIfIndex = _HwVlanInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 2, 1, 9),
    _HwVlanInterfaceIfIndex_Type()
)
hwVlanInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceIfIndex.setStatus("current")
_HwifIsolateMappingTable_Object = MibTable
hwifIsolateMappingTable = _HwifIsolateMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwifIsolateMappingTable.setStatus("current")
_HwifIsolateMappingEntry_Object = MibTableRow
hwifIsolateMappingEntry = _HwifIsolateMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1)
)
hwifIsolateMappingEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwifIsolatePrimaryVlanID"),
)
if mibBuilder.loadTexts:
    hwifIsolateMappingEntry.setStatus("current")
_HwifIsolatePrimaryVlanID_Type = HwVlanIndex
_HwifIsolatePrimaryVlanID_Object = MibTableColumn
hwifIsolatePrimaryVlanID = _HwifIsolatePrimaryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 1),
    _HwifIsolatePrimaryVlanID_Type()
)
hwifIsolatePrimaryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifIsolatePrimaryVlanID.setStatus("current")


class _HwifIsolateSecondaryVlanlistLow_Type(OctetString):
    """Custom type hwifIsolateSecondaryVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifIsolateSecondaryVlanlistLow_Type.__name__ = "OctetString"
_HwifIsolateSecondaryVlanlistLow_Object = MibTableColumn
hwifIsolateSecondaryVlanlistLow = _HwifIsolateSecondaryVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 2),
    _HwifIsolateSecondaryVlanlistLow_Type()
)
hwifIsolateSecondaryVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifIsolateSecondaryVlanlistLow.setStatus("current")


class _HwifIsolateSecondaryVlanlistHigh_Type(OctetString):
    """Custom type hwifIsolateSecondaryVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifIsolateSecondaryVlanlistHigh_Type.__name__ = "OctetString"
_HwifIsolateSecondaryVlanlistHigh_Object = MibTableColumn
hwifIsolateSecondaryVlanlistHigh = _HwifIsolateSecondaryVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 4, 1, 3),
    _HwifIsolateSecondaryVlanlistHigh_Type()
)
hwifIsolateSecondaryVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifIsolateSecondaryVlanlistHigh.setStatus("current")
_HwVlanInterfaceAddrTable_Object = MibTable
hwVlanInterfaceAddrTable = _HwVlanInterfaceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwVlanInterfaceAddrTable.setStatus("current")
_HwVlanInterfaceAddrEntry_Object = MibTableRow
hwVlanInterfaceAddrEntry = _HwVlanInterfaceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1)
)
hwVlanInterfaceAddrEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceIpIfIndex"),
    (0, "HUAWEI-LswVLAN-MIB", "hwVlanInterfaceIpAddr"),
)
if mibBuilder.loadTexts:
    hwVlanInterfaceAddrEntry.setStatus("current")
_HwVlanInterfaceIpIfIndex_Type = Integer32
_HwVlanInterfaceIpIfIndex_Object = MibTableColumn
hwVlanInterfaceIpIfIndex = _HwVlanInterfaceIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 1),
    _HwVlanInterfaceIpIfIndex_Type()
)
hwVlanInterfaceIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpIfIndex.setStatus("current")
_HwVlanInterfaceIpAddr_Type = IpAddress
_HwVlanInterfaceIpAddr_Object = MibTableColumn
hwVlanInterfaceIpAddr = _HwVlanInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 2),
    _HwVlanInterfaceIpAddr_Type()
)
hwVlanInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpAddr.setStatus("current")
_HwVlanInterfaceIpMask_Type = IpAddress
_HwVlanInterfaceIpMask_Object = MibTableColumn
hwVlanInterfaceIpMask = _HwVlanInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 3),
    _HwVlanInterfaceIpMask_Type()
)
hwVlanInterfaceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpMask.setStatus("current")


class _HwVlanInterfaceIpType_Type(Integer32):
    """Custom type hwVlanInterfaceIpType based on Integer32"""
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
        *(("cluster", 3),
          ("primary", 1),
          ("sub", 2),
          ("vrrp", 4))
    )


_HwVlanInterfaceIpType_Type.__name__ = "Integer32"
_HwVlanInterfaceIpType_Object = MibTableColumn
hwVlanInterfaceIpType = _HwVlanInterfaceIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 4),
    _HwVlanInterfaceIpType_Type()
)
hwVlanInterfaceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpType.setStatus("current")
_HwVlanInterfaceIpRowStatus_Type = RowStatus
_HwVlanInterfaceIpRowStatus_Object = MibTableColumn
hwVlanInterfaceIpRowStatus = _HwVlanInterfaceIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 5, 1, 5),
    _HwVlanInterfaceIpRowStatus_Type()
)
hwVlanInterfaceIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanInterfaceIpRowStatus.setStatus("current")
_Hwdot1qVlanBatchMIBTable_Object = MibTable
hwdot1qVlanBatchMIBTable = _Hwdot1qVlanBatchMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwdot1qVlanBatchMIBTable.setStatus("current")
_HwDot1qVlanBatchMIBEntry_Object = MibTableRow
hwDot1qVlanBatchMIBEntry = _HwDot1qVlanBatchMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1)
)
hwDot1qVlanBatchMIBEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwdot1qVlanBatchOperIndex"),
)
if mibBuilder.loadTexts:
    hwDot1qVlanBatchMIBEntry.setStatus("current")
_Hwdot1qVlanBatchOperIndex_Type = Integer32
_Hwdot1qVlanBatchOperIndex_Object = MibTableColumn
hwdot1qVlanBatchOperIndex = _Hwdot1qVlanBatchOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 1),
    _Hwdot1qVlanBatchOperIndex_Type()
)
hwdot1qVlanBatchOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchOperIndex.setStatus("current")
_Hwdot1qVlanBatchStartIndex_Type = HwVlanIndex
_Hwdot1qVlanBatchStartIndex_Object = MibTableColumn
hwdot1qVlanBatchStartIndex = _Hwdot1qVlanBatchStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 2),
    _Hwdot1qVlanBatchStartIndex_Type()
)
hwdot1qVlanBatchStartIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchStartIndex.setStatus("current")
_Hwdot1qVlanBatchEndIndex_Type = HwVlanIndex
_Hwdot1qVlanBatchEndIndex_Object = MibTableColumn
hwdot1qVlanBatchEndIndex = _Hwdot1qVlanBatchEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 3),
    _Hwdot1qVlanBatchEndIndex_Type()
)
hwdot1qVlanBatchEndIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchEndIndex.setStatus("current")


class _Hwdot1qVlanBatchOperStatus_Type(Integer32):
    """Custom type hwdot1qVlanBatchOperStatus based on Integer32"""
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
        *(("opInprogress", 1),
          ("opfailure", 2),
          ("opsuccess", 3),
          ("opsuccesspartial", 4))
    )


_Hwdot1qVlanBatchOperStatus_Type.__name__ = "Integer32"
_Hwdot1qVlanBatchOperStatus_Object = MibTableColumn
hwdot1qVlanBatchOperStatus = _Hwdot1qVlanBatchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 4),
    _Hwdot1qVlanBatchOperStatus_Type()
)
hwdot1qVlanBatchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchOperStatus.setStatus("current")
_Hwdot1qVlanBatchRowStatus_Type = RowStatus
_Hwdot1qVlanBatchRowStatus_Object = MibTableColumn
hwdot1qVlanBatchRowStatus = _Hwdot1qVlanBatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 5),
    _Hwdot1qVlanBatchRowStatus_Type()
)
hwdot1qVlanBatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchRowStatus.setStatus("current")


class _Hwdot1qVlanBatchSetOperate_Type(Integer32):
    """Custom type hwdot1qVlanBatchSetOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_Hwdot1qVlanBatchSetOperate_Type.__name__ = "Integer32"
_Hwdot1qVlanBatchSetOperate_Object = MibTableColumn
hwdot1qVlanBatchSetOperate = _Hwdot1qVlanBatchSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 6, 1, 6),
    _Hwdot1qVlanBatchSetOperate_Type()
)
hwdot1qVlanBatchSetOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwdot1qVlanBatchSetOperate.setStatus("current")
_HwifSuperVlanMappingTable_Object = MibTable
hwifSuperVlanMappingTable = _HwifSuperVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwifSuperVlanMappingTable.setStatus("current")
_HwifSuperVlanMappingEntry_Object = MibTableRow
hwifSuperVlanMappingEntry = _HwifSuperVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1)
)
hwifSuperVlanMappingEntry.setIndexNames(
    (0, "HUAWEI-LswVLAN-MIB", "hwifSuperVlanID"),
)
if mibBuilder.loadTexts:
    hwifSuperVlanMappingEntry.setStatus("current")
_HwifSuperVlanID_Type = HwVlanIndex
_HwifSuperVlanID_Object = MibTableColumn
hwifSuperVlanID = _HwifSuperVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 1),
    _HwifSuperVlanID_Type()
)
hwifSuperVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwifSuperVlanID.setStatus("current")


class _HwifSubVlanlistLow_Type(OctetString):
    """Custom type hwifSubVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifSubVlanlistLow_Type.__name__ = "OctetString"
_HwifSubVlanlistLow_Object = MibTableColumn
hwifSubVlanlistLow = _HwifSubVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 2),
    _HwifSubVlanlistLow_Type()
)
hwifSubVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifSubVlanlistLow.setStatus("current")


class _HwifSubVlanlistHigh_Type(OctetString):
    """Custom type hwifSubVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwifSubVlanlistHigh_Type.__name__ = "OctetString"
_HwifSubVlanlistHigh_Object = MibTableColumn
hwifSubVlanlistHigh = _HwifSubVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 1, 7, 1, 3),
    _HwifSubVlanlistHigh_Type()
)
hwifSubVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwifSubVlanlistHigh.setStatus("current")
_HwLswVlanProtoObject_ObjectIdentity = ObjectIdentity
hwLswVlanProtoObject = _HwLswVlanProtoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwLswVlanProtoObject.setStatus("current")


class _HwVLANMibGarpLeaveAllTime_Type(TimeInterval):
    """Custom type hwVLANMibGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_HwVLANMibGarpLeaveAllTime_Object = MibScalar
hwVLANMibGarpLeaveAllTime = _HwVLANMibGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 14),
    _HwVLANMibGarpLeaveAllTime_Type()
)
hwVLANMibGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVLANMibGarpLeaveAllTime.setStatus("current")
_HwvLANMibSwitchCountTable_Object = MibTable
hwvLANMibSwitchCountTable = _HwvLANMibSwitchCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hwvLANMibSwitchCountTable.setStatus("current")
_HwvLANMibSwitchCountEntry_Object = MibTableRow
hwvLANMibSwitchCountEntry = _HwvLANMibSwitchCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    hwvLANMibSwitchCountEntry.setStatus("current")
_HwVLANMibSwitchGMRPRXPkt_Type = Counter32
_HwVLANMibSwitchGMRPRXPkt_Object = MibTableColumn
hwVLANMibSwitchGMRPRXPkt = _HwVLANMibSwitchGMRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 1),
    _HwVLANMibSwitchGMRPRXPkt_Type()
)
hwVLANMibSwitchGMRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibSwitchGMRPRXPkt.setStatus("current")
_HwVLANMibSwitchGVRPRXPkt_Type = Counter32
_HwVLANMibSwitchGVRPRXPkt_Object = MibTableColumn
hwVLANMibSwitchGVRPRXPkt = _HwVLANMibSwitchGVRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 2),
    _HwVLANMibSwitchGVRPRXPkt_Type()
)
hwVLANMibSwitchGVRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibSwitchGVRPRXPkt.setStatus("current")
_HwVLANMibSwitchGMRPTXPkt_Type = Counter32
_HwVLANMibSwitchGMRPTXPkt_Object = MibTableColumn
hwVLANMibSwitchGMRPTXPkt = _HwVLANMibSwitchGMRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 3),
    _HwVLANMibSwitchGMRPTXPkt_Type()
)
hwVLANMibSwitchGMRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibSwitchGMRPTXPkt.setStatus("current")
_HwVLANMibSwitchGVRPTXPkt_Type = Counter32
_HwVLANMibSwitchGVRPTXPkt_Object = MibTableColumn
hwVLANMibSwitchGVRPTXPkt = _HwVLANMibSwitchGVRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 4),
    _HwVLANMibSwitchGVRPTXPkt_Type()
)
hwVLANMibSwitchGVRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibSwitchGVRPTXPkt.setStatus("current")
_HwVLANMibSwitchDiscardedPkt_Type = Counter32
_HwVLANMibSwitchDiscardedPkt_Object = MibTableColumn
hwVLANMibSwitchDiscardedPkt = _HwVLANMibSwitchDiscardedPkt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 5),
    _HwVLANMibSwitchDiscardedPkt_Type()
)
hwVLANMibSwitchDiscardedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVLANMibSwitchDiscardedPkt.setStatus("current")


class _HwVLANMibSwitchGarpStatClear_Type(Integer32):
    """Custom type hwVLANMibSwitchGarpStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HwVLANMibSwitchGarpStatClear_Type.__name__ = "Integer32"
_HwVLANMibSwitchGarpStatClear_Object = MibTableColumn
hwVLANMibSwitchGarpStatClear = _HwVLANMibSwitchGarpStatClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 15, 1, 6),
    _HwVLANMibSwitchGarpStatClear_Type()
)
hwVLANMibSwitchGarpStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVLANMibSwitchGarpStatClear.setStatus("current")
_HwvLANMibHoldTimeTable_Object = MibTable
hwvLANMibHoldTimeTable = _HwvLANMibHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hwvLANMibHoldTimeTable.setStatus("current")
_HwvLANMibHoldTimeEntry_Object = MibTableRow
hwvLANMibHoldTimeEntry = _HwvLANMibHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    hwvLANMibHoldTimeEntry.setStatus("current")


class _HwVLANMibHoldTime_Type(Integer32):
    """Custom type hwVLANMibHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32765),
    )


_HwVLANMibHoldTime_Type.__name__ = "Integer32"
_HwVLANMibHoldTime_Object = MibTableColumn
hwVLANMibHoldTime = _HwVLANMibHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 2, 2, 16, 1, 1),
    _HwVLANMibHoldTime_Type()
)
hwVLANMibHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVLANMibHoldTime.setStatus("current")
hwifVLANTrunkStatusEntry.registerAugmentions(
    ("HUAWEI-LswVLAN-MIB",
     "hwvLANMibSwitchCountEntry")
)
hwvLANMibSwitchCountEntry.setIndexNames(*hwifVLANTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("HUAWEI-LswVLAN-MIB",
     "hwvLANMibHoldTimeEntry")
)
hwvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswVLAN-MIB",
    **{"HwVlanIndex": HwVlanIndex,
       "hwLswVlan": hwLswVlan,
       "hwLswVlanMngObject": hwLswVlanMngObject,
       "hwdot1qVlanMIBTable": hwdot1qVlanMIBTable,
       "hwdot1qVlanMIBEntry": hwdot1qVlanMIBEntry,
       "hwdot1qVlanIndex": hwdot1qVlanIndex,
       "hwdot1qVlanName": hwdot1qVlanName,
       "hwdot1qVlanPorts": hwdot1qVlanPorts,
       "hwdot1qVlanType": hwdot1qVlanType,
       "hwdot1qVlanMacFilter": hwdot1qVlanMacFilter,
       "hwdot1qVlanMcastUnknownProtos": hwdot1qVlanMcastUnknownProtos,
       "hwExistInterface": hwExistInterface,
       "hwVlanInterfaceIndex": hwVlanInterfaceIndex,
       "hwdot1qVlanMacLearn": hwdot1qVlanMacLearn,
       "hwdot1qVlanStatus": hwdot1qVlanStatus,
       "hwdot1qVlanCreationTime": hwdot1qVlanCreationTime,
       "hwdot1qVlanPriority": hwdot1qVlanPriority,
       "hwdot1qVlanRowStatus": hwdot1qVlanRowStatus,
       "hwdot1qVlanBroadcastSuppression": hwdot1qVlanBroadcastSuppression,
       "hwdot1qVlanBcastSuppressionPPS": hwdot1qVlanBcastSuppressionPPS,
       "hwdot1qVlanMulticast": hwdot1qVlanMulticast,
       "hwdot1qVlanTaggedPorts": hwdot1qVlanTaggedPorts,
       "hwdot1qVlanUntaggedPorts": hwdot1qVlanUntaggedPorts,
       "hwdot1qVlanPortIndexs": hwdot1qVlanPortIndexs,
       "hwVlanInterfaceTable": hwVlanInterfaceTable,
       "hwVlanInterfaceEntry": hwVlanInterfaceEntry,
       "hwVlanInterfaceID": hwVlanInterfaceID,
       "hwdot1qVlanID": hwdot1qVlanID,
       "hwdot1qVlanIpAddress": hwdot1qVlanIpAddress,
       "hwdot1qVlanIpAddressMask": hwdot1qVlanIpAddressMask,
       "hwVlanInterfaceAdminStatus": hwVlanInterfaceAdminStatus,
       "hwVlanInterfaceFrameType": hwVlanInterfaceFrameType,
       "hwInterfaceRowStatus": hwInterfaceRowStatus,
       "hwVlanInterfaceIpMethod": hwVlanInterfaceIpMethod,
       "hwVlanInterfaceIfIndex": hwVlanInterfaceIfIndex,
       "hwifIsolateMappingTable": hwifIsolateMappingTable,
       "hwifIsolateMappingEntry": hwifIsolateMappingEntry,
       "hwifIsolatePrimaryVlanID": hwifIsolatePrimaryVlanID,
       "hwifIsolateSecondaryVlanlistLow": hwifIsolateSecondaryVlanlistLow,
       "hwifIsolateSecondaryVlanlistHigh": hwifIsolateSecondaryVlanlistHigh,
       "hwVlanInterfaceAddrTable": hwVlanInterfaceAddrTable,
       "hwVlanInterfaceAddrEntry": hwVlanInterfaceAddrEntry,
       "hwVlanInterfaceIpIfIndex": hwVlanInterfaceIpIfIndex,
       "hwVlanInterfaceIpAddr": hwVlanInterfaceIpAddr,
       "hwVlanInterfaceIpMask": hwVlanInterfaceIpMask,
       "hwVlanInterfaceIpType": hwVlanInterfaceIpType,
       "hwVlanInterfaceIpRowStatus": hwVlanInterfaceIpRowStatus,
       "hwdot1qVlanBatchMIBTable": hwdot1qVlanBatchMIBTable,
       "hwDot1qVlanBatchMIBEntry": hwDot1qVlanBatchMIBEntry,
       "hwdot1qVlanBatchOperIndex": hwdot1qVlanBatchOperIndex,
       "hwdot1qVlanBatchStartIndex": hwdot1qVlanBatchStartIndex,
       "hwdot1qVlanBatchEndIndex": hwdot1qVlanBatchEndIndex,
       "hwdot1qVlanBatchOperStatus": hwdot1qVlanBatchOperStatus,
       "hwdot1qVlanBatchRowStatus": hwdot1qVlanBatchRowStatus,
       "hwdot1qVlanBatchSetOperate": hwdot1qVlanBatchSetOperate,
       "hwifSuperVlanMappingTable": hwifSuperVlanMappingTable,
       "hwifSuperVlanMappingEntry": hwifSuperVlanMappingEntry,
       "hwifSuperVlanID": hwifSuperVlanID,
       "hwifSubVlanlistLow": hwifSubVlanlistLow,
       "hwifSubVlanlistHigh": hwifSubVlanlistHigh,
       "hwLswVlanProtoObject": hwLswVlanProtoObject,
       "hwVLANMibGarpLeaveAllTime": hwVLANMibGarpLeaveAllTime,
       "hwvLANMibSwitchCountTable": hwvLANMibSwitchCountTable,
       "hwvLANMibSwitchCountEntry": hwvLANMibSwitchCountEntry,
       "hwVLANMibSwitchGMRPRXPkt": hwVLANMibSwitchGMRPRXPkt,
       "hwVLANMibSwitchGVRPRXPkt": hwVLANMibSwitchGVRPRXPkt,
       "hwVLANMibSwitchGMRPTXPkt": hwVLANMibSwitchGMRPTXPkt,
       "hwVLANMibSwitchGVRPTXPkt": hwVLANMibSwitchGVRPTXPkt,
       "hwVLANMibSwitchDiscardedPkt": hwVLANMibSwitchDiscardedPkt,
       "hwVLANMibSwitchGarpStatClear": hwVLANMibSwitchGarpStatClear,
       "hwvLANMibHoldTimeTable": hwvLANMibHoldTimeTable,
       "hwvLANMibHoldTimeEntry": hwvLANMibHoldTimeEntry,
       "hwVLANMibHoldTime": hwVLANMibHoldTime}
)
