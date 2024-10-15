# SNMP MIB module (HPN-ICF-LswVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:44 2024
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

(PortList,
 hpnicfifVLANTrunkStatusEntry) = mibBuilder.importSymbols(
    "HPN-ICF-LswINF-MIB",
    "PortList",
    "hpnicfifVLANTrunkStatusEntry")

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfVlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfLswVlanMngObject_ObjectIdentity = ObjectIdentity
hpnicfLswVlanMngObject = _HpnicfLswVlanMngObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfLswVlanMngObject.setStatus("current")
_Hpnicfdot1qVlanMIBTable_Object = MibTable
hpnicfdot1qVlanMIBTable = _Hpnicfdot1qVlanMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMIBTable.setStatus("current")
_Hpnicfdot1qVlanMIBEntry_Object = MibTableRow
hpnicfdot1qVlanMIBEntry = _Hpnicfdot1qVlanMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1)
)
hpnicfdot1qVlanMIBEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMIBEntry.setStatus("current")
_Hpnicfdot1qVlanIndex_Type = HpnicfVlanIndex
_Hpnicfdot1qVlanIndex_Object = MibTableColumn
hpnicfdot1qVlanIndex = _Hpnicfdot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 1),
    _Hpnicfdot1qVlanIndex_Type()
)
hpnicfdot1qVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanIndex.setStatus("current")


class _Hpnicfdot1qVlanName_Type(SnmpAdminString):
    """Custom type hpnicfdot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hpnicfdot1qVlanName_Type.__name__ = "SnmpAdminString"
_Hpnicfdot1qVlanName_Object = MibTableColumn
hpnicfdot1qVlanName = _Hpnicfdot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 2),
    _Hpnicfdot1qVlanName_Type()
)
hpnicfdot1qVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanName.setStatus("current")
_Hpnicfdot1qVlanPorts_Type = PortList
_Hpnicfdot1qVlanPorts_Object = MibTableColumn
hpnicfdot1qVlanPorts = _Hpnicfdot1qVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 3),
    _Hpnicfdot1qVlanPorts_Type()
)
hpnicfdot1qVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanPorts.setStatus("current")


class _Hpnicfdot1qVlanType_Type(Integer32):
    """Custom type hpnicfdot1qVlanType based on Integer32"""
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
        *(("common-vlan", 2),
          ("isolate-user-vlan", 4),
          ("primaryVlan", 6),
          ("secondary-vlan", 5),
          ("sub-vlan", 3),
          ("superVlan", 1))
    )


_Hpnicfdot1qVlanType_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanType_Object = MibTableColumn
hpnicfdot1qVlanType = _Hpnicfdot1qVlanType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 4),
    _Hpnicfdot1qVlanType_Type()
)
hpnicfdot1qVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanType.setStatus("current")
_Hpnicfdot1qVlanMacFilter_Type = TruthValue
_Hpnicfdot1qVlanMacFilter_Object = MibTableColumn
hpnicfdot1qVlanMacFilter = _Hpnicfdot1qVlanMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 5),
    _Hpnicfdot1qVlanMacFilter_Type()
)
hpnicfdot1qVlanMacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMacFilter.setStatus("current")
_Hpnicfdot1qVlanMcastUnknownProtos_Type = TruthValue
_Hpnicfdot1qVlanMcastUnknownProtos_Object = MibTableColumn
hpnicfdot1qVlanMcastUnknownProtos = _Hpnicfdot1qVlanMcastUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 6),
    _Hpnicfdot1qVlanMcastUnknownProtos_Type()
)
hpnicfdot1qVlanMcastUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMcastUnknownProtos.setStatus("current")
_HpnicfExistInterface_Type = TruthValue
_HpnicfExistInterface_Object = MibTableColumn
hpnicfExistInterface = _HpnicfExistInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 7),
    _HpnicfExistInterface_Type()
)
hpnicfExistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfExistInterface.setStatus("current")
_HpnicfVlanInterfaceIndex_Type = Integer32
_HpnicfVlanInterfaceIndex_Object = MibTableColumn
hpnicfVlanInterfaceIndex = _HpnicfVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 8),
    _HpnicfVlanInterfaceIndex_Type()
)
hpnicfVlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIndex.setStatus("current")
_Hpnicfdot1qVlanMacLearn_Type = TruthValue
_Hpnicfdot1qVlanMacLearn_Object = MibTableColumn
hpnicfdot1qVlanMacLearn = _Hpnicfdot1qVlanMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 9),
    _Hpnicfdot1qVlanMacLearn_Type()
)
hpnicfdot1qVlanMacLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMacLearn.setStatus("current")


class _Hpnicfdot1qVlanStatus_Type(Integer32):
    """Custom type hpnicfdot1qVlanStatus based on Integer32"""
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


_Hpnicfdot1qVlanStatus_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanStatus_Object = MibTableColumn
hpnicfdot1qVlanStatus = _Hpnicfdot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 10),
    _Hpnicfdot1qVlanStatus_Type()
)
hpnicfdot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanStatus.setStatus("current")
_Hpnicfdot1qVlanCreationTime_Type = TimeTicks
_Hpnicfdot1qVlanCreationTime_Object = MibTableColumn
hpnicfdot1qVlanCreationTime = _Hpnicfdot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 11),
    _Hpnicfdot1qVlanCreationTime_Type()
)
hpnicfdot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanCreationTime.setStatus("current")


class _Hpnicfdot1qVlanPriority_Type(Integer32):
    """Custom type hpnicfdot1qVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hpnicfdot1qVlanPriority_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanPriority_Object = MibTableColumn
hpnicfdot1qVlanPriority = _Hpnicfdot1qVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 12),
    _Hpnicfdot1qVlanPriority_Type()
)
hpnicfdot1qVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanPriority.setStatus("current")
_Hpnicfdot1qVlanRowStatus_Type = RowStatus
_Hpnicfdot1qVlanRowStatus_Object = MibTableColumn
hpnicfdot1qVlanRowStatus = _Hpnicfdot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 13),
    _Hpnicfdot1qVlanRowStatus_Type()
)
hpnicfdot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanRowStatus.setStatus("current")


class _Hpnicfdot1qVlanBroadcastSuppression_Type(Integer32):
    """Custom type hpnicfdot1qVlanBroadcastSuppression based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hpnicfdot1qVlanBroadcastSuppression_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanBroadcastSuppression_Object = MibTableColumn
hpnicfdot1qVlanBroadcastSuppression = _Hpnicfdot1qVlanBroadcastSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 14),
    _Hpnicfdot1qVlanBroadcastSuppression_Type()
)
hpnicfdot1qVlanBroadcastSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBroadcastSuppression.setStatus("current")


class _Hpnicfdot1qVlanBcastSuppressionPPS_Type(Integer32):
    """Custom type hpnicfdot1qVlanBcastSuppressionPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 148800),
    )


_Hpnicfdot1qVlanBcastSuppressionPPS_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanBcastSuppressionPPS_Object = MibTableColumn
hpnicfdot1qVlanBcastSuppressionPPS = _Hpnicfdot1qVlanBcastSuppressionPPS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 15),
    _Hpnicfdot1qVlanBcastSuppressionPPS_Type()
)
hpnicfdot1qVlanBcastSuppressionPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBcastSuppressionPPS.setStatus("current")


class _Hpnicfdot1qVlanMulticast_Type(Integer32):
    """Custom type hpnicfdot1qVlanMulticast based on Integer32"""
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


_Hpnicfdot1qVlanMulticast_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanMulticast_Object = MibTableColumn
hpnicfdot1qVlanMulticast = _Hpnicfdot1qVlanMulticast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 16),
    _Hpnicfdot1qVlanMulticast_Type()
)
hpnicfdot1qVlanMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanMulticast.setStatus("current")
_Hpnicfdot1qVlanTaggedPorts_Type = PortList
_Hpnicfdot1qVlanTaggedPorts_Object = MibTableColumn
hpnicfdot1qVlanTaggedPorts = _Hpnicfdot1qVlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 17),
    _Hpnicfdot1qVlanTaggedPorts_Type()
)
hpnicfdot1qVlanTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanTaggedPorts.setStatus("current")
_Hpnicfdot1qVlanUntaggedPorts_Type = PortList
_Hpnicfdot1qVlanUntaggedPorts_Object = MibTableColumn
hpnicfdot1qVlanUntaggedPorts = _Hpnicfdot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 18),
    _Hpnicfdot1qVlanUntaggedPorts_Type()
)
hpnicfdot1qVlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanUntaggedPorts.setStatus("current")
_Hpnicfdot1qVlanPortIndexs_Type = OctetString
_Hpnicfdot1qVlanPortIndexs_Object = MibTableColumn
hpnicfdot1qVlanPortIndexs = _Hpnicfdot1qVlanPortIndexs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 1, 1, 19),
    _Hpnicfdot1qVlanPortIndexs_Type()
)
hpnicfdot1qVlanPortIndexs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanPortIndexs.setStatus("current")
_HpnicfVlanInterfaceTable_Object = MibTable
hpnicfVlanInterfaceTable = _HpnicfVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceTable.setStatus("current")
_HpnicfVlanInterfaceEntry_Object = MibTableRow
hpnicfVlanInterfaceEntry = _HpnicfVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1)
)
hpnicfVlanInterfaceEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfVlanInterfaceID"),
)
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceEntry.setStatus("current")
_HpnicfVlanInterfaceID_Type = Integer32
_HpnicfVlanInterfaceID_Object = MibTableColumn
hpnicfVlanInterfaceID = _HpnicfVlanInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 1),
    _HpnicfVlanInterfaceID_Type()
)
hpnicfVlanInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceID.setStatus("current")
_Hpnicfdot1qVlanID_Type = HpnicfVlanIndex
_Hpnicfdot1qVlanID_Object = MibTableColumn
hpnicfdot1qVlanID = _Hpnicfdot1qVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 2),
    _Hpnicfdot1qVlanID_Type()
)
hpnicfdot1qVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanID.setStatus("current")
_Hpnicfdot1qVlanIpAddress_Type = IpAddress
_Hpnicfdot1qVlanIpAddress_Object = MibTableColumn
hpnicfdot1qVlanIpAddress = _Hpnicfdot1qVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 3),
    _Hpnicfdot1qVlanIpAddress_Type()
)
hpnicfdot1qVlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanIpAddress.setStatus("current")
_Hpnicfdot1qVlanIpAddressMask_Type = IpAddress
_Hpnicfdot1qVlanIpAddressMask_Object = MibTableColumn
hpnicfdot1qVlanIpAddressMask = _Hpnicfdot1qVlanIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 4),
    _Hpnicfdot1qVlanIpAddressMask_Type()
)
hpnicfdot1qVlanIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanIpAddressMask.setStatus("current")


class _HpnicfVlanInterfaceAdminStatus_Type(Integer32):
    """Custom type hpnicfVlanInterfaceAdminStatus based on Integer32"""
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


_HpnicfVlanInterfaceAdminStatus_Type.__name__ = "Integer32"
_HpnicfVlanInterfaceAdminStatus_Object = MibTableColumn
hpnicfVlanInterfaceAdminStatus = _HpnicfVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 5),
    _HpnicfVlanInterfaceAdminStatus_Type()
)
hpnicfVlanInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceAdminStatus.setStatus("current")


class _HpnicfVlanInterfaceFrameType_Type(Integer32):
    """Custom type hpnicfVlanInterfaceFrameType based on Integer32"""
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


_HpnicfVlanInterfaceFrameType_Type.__name__ = "Integer32"
_HpnicfVlanInterfaceFrameType_Object = MibTableColumn
hpnicfVlanInterfaceFrameType = _HpnicfVlanInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 6),
    _HpnicfVlanInterfaceFrameType_Type()
)
hpnicfVlanInterfaceFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceFrameType.setStatus("current")
_HpnicfInterfaceRowStatus_Type = RowStatus
_HpnicfInterfaceRowStatus_Object = MibTableColumn
hpnicfInterfaceRowStatus = _HpnicfInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 7),
    _HpnicfInterfaceRowStatus_Type()
)
hpnicfInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfInterfaceRowStatus.setStatus("current")


class _HpnicfVlanInterfaceIpMethod_Type(Integer32):
    """Custom type hpnicfVlanInterfaceIpMethod based on Integer32"""
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


_HpnicfVlanInterfaceIpMethod_Type.__name__ = "Integer32"
_HpnicfVlanInterfaceIpMethod_Object = MibTableColumn
hpnicfVlanInterfaceIpMethod = _HpnicfVlanInterfaceIpMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 8),
    _HpnicfVlanInterfaceIpMethod_Type()
)
hpnicfVlanInterfaceIpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpMethod.setStatus("current")
_HpnicfVlanInterfaceIfIndex_Type = Integer32
_HpnicfVlanInterfaceIfIndex_Object = MibTableColumn
hpnicfVlanInterfaceIfIndex = _HpnicfVlanInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 2, 1, 9),
    _HpnicfVlanInterfaceIfIndex_Type()
)
hpnicfVlanInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIfIndex.setStatus("current")
_HpnicfifIsolateMappingTable_Object = MibTable
hpnicfifIsolateMappingTable = _HpnicfifIsolateMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfifIsolateMappingTable.setStatus("current")
_HpnicfifIsolateMappingEntry_Object = MibTableRow
hpnicfifIsolateMappingEntry = _HpnicfifIsolateMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 4, 1)
)
hpnicfifIsolateMappingEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfifIsolatePrimaryVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfifIsolateMappingEntry.setStatus("current")
_HpnicfifIsolatePrimaryVlanID_Type = HpnicfVlanIndex
_HpnicfifIsolatePrimaryVlanID_Object = MibTableColumn
hpnicfifIsolatePrimaryVlanID = _HpnicfifIsolatePrimaryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 4, 1, 1),
    _HpnicfifIsolatePrimaryVlanID_Type()
)
hpnicfifIsolatePrimaryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIsolatePrimaryVlanID.setStatus("current")


class _HpnicfifIsolateSecondaryVlanlistLow_Type(OctetString):
    """Custom type hpnicfifIsolateSecondaryVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifIsolateSecondaryVlanlistLow_Type.__name__ = "OctetString"
_HpnicfifIsolateSecondaryVlanlistLow_Object = MibTableColumn
hpnicfifIsolateSecondaryVlanlistLow = _HpnicfifIsolateSecondaryVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 4, 1, 2),
    _HpnicfifIsolateSecondaryVlanlistLow_Type()
)
hpnicfifIsolateSecondaryVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifIsolateSecondaryVlanlistLow.setStatus("current")


class _HpnicfifIsolateSecondaryVlanlistHigh_Type(OctetString):
    """Custom type hpnicfifIsolateSecondaryVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifIsolateSecondaryVlanlistHigh_Type.__name__ = "OctetString"
_HpnicfifIsolateSecondaryVlanlistHigh_Object = MibTableColumn
hpnicfifIsolateSecondaryVlanlistHigh = _HpnicfifIsolateSecondaryVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 4, 1, 3),
    _HpnicfifIsolateSecondaryVlanlistHigh_Type()
)
hpnicfifIsolateSecondaryVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifIsolateSecondaryVlanlistHigh.setStatus("current")
_HpnicfVlanInterfaceAddrTable_Object = MibTable
hpnicfVlanInterfaceAddrTable = _HpnicfVlanInterfaceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceAddrTable.setStatus("current")
_HpnicfVlanInterfaceAddrEntry_Object = MibTableRow
hpnicfVlanInterfaceAddrEntry = _HpnicfVlanInterfaceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1)
)
hpnicfVlanInterfaceAddrEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfVlanInterfaceIpIfIndex"),
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfVlanInterfaceIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceAddrEntry.setStatus("current")
_HpnicfVlanInterfaceIpIfIndex_Type = Integer32
_HpnicfVlanInterfaceIpIfIndex_Object = MibTableColumn
hpnicfVlanInterfaceIpIfIndex = _HpnicfVlanInterfaceIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1, 1),
    _HpnicfVlanInterfaceIpIfIndex_Type()
)
hpnicfVlanInterfaceIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpIfIndex.setStatus("current")
_HpnicfVlanInterfaceIpAddr_Type = IpAddress
_HpnicfVlanInterfaceIpAddr_Object = MibTableColumn
hpnicfVlanInterfaceIpAddr = _HpnicfVlanInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1, 2),
    _HpnicfVlanInterfaceIpAddr_Type()
)
hpnicfVlanInterfaceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpAddr.setStatus("current")
_HpnicfVlanInterfaceIpMask_Type = IpAddress
_HpnicfVlanInterfaceIpMask_Object = MibTableColumn
hpnicfVlanInterfaceIpMask = _HpnicfVlanInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1, 3),
    _HpnicfVlanInterfaceIpMask_Type()
)
hpnicfVlanInterfaceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpMask.setStatus("current")


class _HpnicfVlanInterfaceIpType_Type(Integer32):
    """Custom type hpnicfVlanInterfaceIpType based on Integer32"""
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


_HpnicfVlanInterfaceIpType_Type.__name__ = "Integer32"
_HpnicfVlanInterfaceIpType_Object = MibTableColumn
hpnicfVlanInterfaceIpType = _HpnicfVlanInterfaceIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1, 4),
    _HpnicfVlanInterfaceIpType_Type()
)
hpnicfVlanInterfaceIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpType.setStatus("current")
_HpnicfVlanInterfaceIpRowStatus_Type = RowStatus
_HpnicfVlanInterfaceIpRowStatus_Object = MibTableColumn
hpnicfVlanInterfaceIpRowStatus = _HpnicfVlanInterfaceIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 5, 1, 5),
    _HpnicfVlanInterfaceIpRowStatus_Type()
)
hpnicfVlanInterfaceIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVlanInterfaceIpRowStatus.setStatus("current")
_HpnicfDot1qVlanBatchMIBTable_Object = MibTable
hpnicfDot1qVlanBatchMIBTable = _HpnicfDot1qVlanBatchMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfDot1qVlanBatchMIBTable.setStatus("current")
_HpnicfDot1qVlanBatchMIBEntry_Object = MibTableRow
hpnicfDot1qVlanBatchMIBEntry = _HpnicfDot1qVlanBatchMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1)
)
hpnicfDot1qVlanBatchMIBEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfdot1qVlanBatchOperIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDot1qVlanBatchMIBEntry.setStatus("current")
_Hpnicfdot1qVlanBatchOperIndex_Type = Integer32
_Hpnicfdot1qVlanBatchOperIndex_Object = MibTableColumn
hpnicfdot1qVlanBatchOperIndex = _Hpnicfdot1qVlanBatchOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 1),
    _Hpnicfdot1qVlanBatchOperIndex_Type()
)
hpnicfdot1qVlanBatchOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchOperIndex.setStatus("current")
_Hpnicfdot1qVlanBatchStartIndex_Type = HpnicfVlanIndex
_Hpnicfdot1qVlanBatchStartIndex_Object = MibTableColumn
hpnicfdot1qVlanBatchStartIndex = _Hpnicfdot1qVlanBatchStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 2),
    _Hpnicfdot1qVlanBatchStartIndex_Type()
)
hpnicfdot1qVlanBatchStartIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchStartIndex.setStatus("current")
_Hpnicfdot1qVlanBatchEndIndex_Type = HpnicfVlanIndex
_Hpnicfdot1qVlanBatchEndIndex_Object = MibTableColumn
hpnicfdot1qVlanBatchEndIndex = _Hpnicfdot1qVlanBatchEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 3),
    _Hpnicfdot1qVlanBatchEndIndex_Type()
)
hpnicfdot1qVlanBatchEndIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchEndIndex.setStatus("current")


class _Hpnicfdot1qVlanBatchOperStatus_Type(Integer32):
    """Custom type hpnicfdot1qVlanBatchOperStatus based on Integer32"""
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


_Hpnicfdot1qVlanBatchOperStatus_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanBatchOperStatus_Object = MibTableColumn
hpnicfdot1qVlanBatchOperStatus = _Hpnicfdot1qVlanBatchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 4),
    _Hpnicfdot1qVlanBatchOperStatus_Type()
)
hpnicfdot1qVlanBatchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchOperStatus.setStatus("current")
_Hpnicfdot1qVlanBatchRowStatus_Type = RowStatus
_Hpnicfdot1qVlanBatchRowStatus_Object = MibTableColumn
hpnicfdot1qVlanBatchRowStatus = _Hpnicfdot1qVlanBatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 5),
    _Hpnicfdot1qVlanBatchRowStatus_Type()
)
hpnicfdot1qVlanBatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchRowStatus.setStatus("current")


class _Hpnicfdot1qVlanBatchSetOperate_Type(Integer32):
    """Custom type hpnicfdot1qVlanBatchSetOperate based on Integer32"""
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


_Hpnicfdot1qVlanBatchSetOperate_Type.__name__ = "Integer32"
_Hpnicfdot1qVlanBatchSetOperate_Object = MibTableColumn
hpnicfdot1qVlanBatchSetOperate = _Hpnicfdot1qVlanBatchSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 6, 1, 6),
    _Hpnicfdot1qVlanBatchSetOperate_Type()
)
hpnicfdot1qVlanBatchSetOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfdot1qVlanBatchSetOperate.setStatus("current")
_HpnicfifSuperVlanMappingTable_Object = MibTable
hpnicfifSuperVlanMappingTable = _HpnicfifSuperVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfifSuperVlanMappingTable.setStatus("current")
_HpnicfifSuperVlanMappingEntry_Object = MibTableRow
hpnicfifSuperVlanMappingEntry = _HpnicfifSuperVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 7, 1)
)
hpnicfifSuperVlanMappingEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfifSuperVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfifSuperVlanMappingEntry.setStatus("current")
_HpnicfifSuperVlanID_Type = HpnicfVlanIndex
_HpnicfifSuperVlanID_Object = MibTableColumn
hpnicfifSuperVlanID = _HpnicfifSuperVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 7, 1, 1),
    _HpnicfifSuperVlanID_Type()
)
hpnicfifSuperVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifSuperVlanID.setStatus("current")


class _HpnicfifSubVlanlistLow_Type(OctetString):
    """Custom type hpnicfifSubVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifSubVlanlistLow_Type.__name__ = "OctetString"
_HpnicfifSubVlanlistLow_Object = MibTableColumn
hpnicfifSubVlanlistLow = _HpnicfifSubVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 7, 1, 2),
    _HpnicfifSubVlanlistLow_Type()
)
hpnicfifSubVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifSubVlanlistLow.setStatus("current")


class _HpnicfifSubVlanlistHigh_Type(OctetString):
    """Custom type hpnicfifSubVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifSubVlanlistHigh_Type.__name__ = "OctetString"
_HpnicfifSubVlanlistHigh_Object = MibTableColumn
hpnicfifSubVlanlistHigh = _HpnicfifSubVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 7, 1, 3),
    _HpnicfifSubVlanlistHigh_Type()
)
hpnicfifSubVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifSubVlanlistHigh.setStatus("current")
_HpnicfPrivateVlanMappingTable_Object = MibTable
hpnicfPrivateVlanMappingTable = _HpnicfPrivateVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfPrivateVlanMappingTable.setStatus("current")
_HpnicfPrivateVlanMappingEntry_Object = MibTableRow
hpnicfPrivateVlanMappingEntry = _HpnicfPrivateVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 8, 1)
)
hpnicfPrivateVlanMappingEntry.setIndexNames(
    (0, "HPN-ICF-LswVLAN-MIB", "hpnicfPrimaryVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfPrivateVlanMappingEntry.setStatus("current")
_HpnicfPrimaryVlanID_Type = HpnicfVlanIndex
_HpnicfPrimaryVlanID_Object = MibTableColumn
hpnicfPrimaryVlanID = _HpnicfPrimaryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 8, 1, 1),
    _HpnicfPrimaryVlanID_Type()
)
hpnicfPrimaryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPrimaryVlanID.setStatus("current")


class _HpnicfSecondaryVlanlistLow_Type(OctetString):
    """Custom type hpnicfSecondaryVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfSecondaryVlanlistLow_Type.__name__ = "OctetString"
_HpnicfSecondaryVlanlistLow_Object = MibTableColumn
hpnicfSecondaryVlanlistLow = _HpnicfSecondaryVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 8, 1, 2),
    _HpnicfSecondaryVlanlistLow_Type()
)
hpnicfSecondaryVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecondaryVlanlistLow.setStatus("current")


class _HpnicfSecondaryVlanlistHigh_Type(OctetString):
    """Custom type hpnicfSecondaryVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfSecondaryVlanlistHigh_Type.__name__ = "OctetString"
_HpnicfSecondaryVlanlistHigh_Object = MibTableColumn
hpnicfSecondaryVlanlistHigh = _HpnicfSecondaryVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 1, 8, 1, 3),
    _HpnicfSecondaryVlanlistHigh_Type()
)
hpnicfSecondaryVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecondaryVlanlistHigh.setStatus("current")
_HpnicfLswVlanProtoObject_ObjectIdentity = ObjectIdentity
hpnicfLswVlanProtoObject = _HpnicfLswVlanProtoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfLswVlanProtoObject.setStatus("current")


class _HpnicfVLANMibGarpLeaveAllTime_Type(TimeInterval):
    """Custom type hpnicfVLANMibGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_HpnicfVLANMibGarpLeaveAllTime_Object = MibScalar
hpnicfVLANMibGarpLeaveAllTime = _HpnicfVLANMibGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 14),
    _HpnicfVLANMibGarpLeaveAllTime_Type()
)
hpnicfVLANMibGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVLANMibGarpLeaveAllTime.setStatus("current")
_HpnicfvLANMibSwitchCountTable_Object = MibTable
hpnicfvLANMibSwitchCountTable = _HpnicfvLANMibSwitchCountTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfvLANMibSwitchCountTable.setStatus("current")
_HpnicfvLANMibSwitchCountEntry_Object = MibTableRow
hpnicfvLANMibSwitchCountEntry = _HpnicfvLANMibSwitchCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    hpnicfvLANMibSwitchCountEntry.setStatus("current")
_HpnicfVLANMibSwitchGMRPRXPkt_Type = Counter32
_HpnicfVLANMibSwitchGMRPRXPkt_Object = MibTableColumn
hpnicfVLANMibSwitchGMRPRXPkt = _HpnicfVLANMibSwitchGMRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 1),
    _HpnicfVLANMibSwitchGMRPRXPkt_Type()
)
hpnicfVLANMibSwitchGMRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchGMRPRXPkt.setStatus("current")
_HpnicfVLANMibSwitchGVRPRXPkt_Type = Counter32
_HpnicfVLANMibSwitchGVRPRXPkt_Object = MibTableColumn
hpnicfVLANMibSwitchGVRPRXPkt = _HpnicfVLANMibSwitchGVRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 2),
    _HpnicfVLANMibSwitchGVRPRXPkt_Type()
)
hpnicfVLANMibSwitchGVRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchGVRPRXPkt.setStatus("current")
_HpnicfVLANMibSwitchGMRPTXPkt_Type = Counter32
_HpnicfVLANMibSwitchGMRPTXPkt_Object = MibTableColumn
hpnicfVLANMibSwitchGMRPTXPkt = _HpnicfVLANMibSwitchGMRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 3),
    _HpnicfVLANMibSwitchGMRPTXPkt_Type()
)
hpnicfVLANMibSwitchGMRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchGMRPTXPkt.setStatus("current")
_HpnicfVLANMibSwitchGVRPTXPkt_Type = Counter32
_HpnicfVLANMibSwitchGVRPTXPkt_Object = MibTableColumn
hpnicfVLANMibSwitchGVRPTXPkt = _HpnicfVLANMibSwitchGVRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 4),
    _HpnicfVLANMibSwitchGVRPTXPkt_Type()
)
hpnicfVLANMibSwitchGVRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchGVRPTXPkt.setStatus("current")
_HpnicfVLANMibSwitchDiscardedPkt_Type = Counter32
_HpnicfVLANMibSwitchDiscardedPkt_Object = MibTableColumn
hpnicfVLANMibSwitchDiscardedPkt = _HpnicfVLANMibSwitchDiscardedPkt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 5),
    _HpnicfVLANMibSwitchDiscardedPkt_Type()
)
hpnicfVLANMibSwitchDiscardedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchDiscardedPkt.setStatus("current")


class _HpnicfVLANMibSwitchGarpStatClear_Type(Integer32):
    """Custom type hpnicfVLANMibSwitchGarpStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HpnicfVLANMibSwitchGarpStatClear_Type.__name__ = "Integer32"
_HpnicfVLANMibSwitchGarpStatClear_Object = MibTableColumn
hpnicfVLANMibSwitchGarpStatClear = _HpnicfVLANMibSwitchGarpStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 15, 1, 6),
    _HpnicfVLANMibSwitchGarpStatClear_Type()
)
hpnicfVLANMibSwitchGarpStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVLANMibSwitchGarpStatClear.setStatus("current")
_HpnicfvLANMibHoldTimeTable_Object = MibTable
hpnicfvLANMibHoldTimeTable = _HpnicfvLANMibHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfvLANMibHoldTimeTable.setStatus("current")
_HpnicfvLANMibHoldTimeEntry_Object = MibTableRow
hpnicfvLANMibHoldTimeEntry = _HpnicfvLANMibHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    hpnicfvLANMibHoldTimeEntry.setStatus("current")


class _HpnicfVLANMibHoldTime_Type(Integer32):
    """Custom type hpnicfVLANMibHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32765),
    )


_HpnicfVLANMibHoldTime_Type.__name__ = "Integer32"
_HpnicfVLANMibHoldTime_Object = MibTableColumn
hpnicfVLANMibHoldTime = _HpnicfVLANMibHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 2, 2, 16, 1, 1),
    _HpnicfVLANMibHoldTime_Type()
)
hpnicfVLANMibHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVLANMibHoldTime.setStatus("current")
hpnicfifVLANTrunkStatusEntry.registerAugmentions(
    ("HPN-ICF-LswVLAN-MIB",
     "hpnicfvLANMibSwitchCountEntry")
)
hpnicfvLANMibSwitchCountEntry.setIndexNames(*hpnicfifVLANTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("HPN-ICF-LswVLAN-MIB",
     "hpnicfvLANMibHoldTimeEntry")
)
hpnicfvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswVLAN-MIB",
    **{"HpnicfVlanIndex": HpnicfVlanIndex,
       "hpnicfLswVlan": hpnicfLswVlan,
       "hpnicfLswVlanMngObject": hpnicfLswVlanMngObject,
       "hpnicfdot1qVlanMIBTable": hpnicfdot1qVlanMIBTable,
       "hpnicfdot1qVlanMIBEntry": hpnicfdot1qVlanMIBEntry,
       "hpnicfdot1qVlanIndex": hpnicfdot1qVlanIndex,
       "hpnicfdot1qVlanName": hpnicfdot1qVlanName,
       "hpnicfdot1qVlanPorts": hpnicfdot1qVlanPorts,
       "hpnicfdot1qVlanType": hpnicfdot1qVlanType,
       "hpnicfdot1qVlanMacFilter": hpnicfdot1qVlanMacFilter,
       "hpnicfdot1qVlanMcastUnknownProtos": hpnicfdot1qVlanMcastUnknownProtos,
       "hpnicfExistInterface": hpnicfExistInterface,
       "hpnicfVlanInterfaceIndex": hpnicfVlanInterfaceIndex,
       "hpnicfdot1qVlanMacLearn": hpnicfdot1qVlanMacLearn,
       "hpnicfdot1qVlanStatus": hpnicfdot1qVlanStatus,
       "hpnicfdot1qVlanCreationTime": hpnicfdot1qVlanCreationTime,
       "hpnicfdot1qVlanPriority": hpnicfdot1qVlanPriority,
       "hpnicfdot1qVlanRowStatus": hpnicfdot1qVlanRowStatus,
       "hpnicfdot1qVlanBroadcastSuppression": hpnicfdot1qVlanBroadcastSuppression,
       "hpnicfdot1qVlanBcastSuppressionPPS": hpnicfdot1qVlanBcastSuppressionPPS,
       "hpnicfdot1qVlanMulticast": hpnicfdot1qVlanMulticast,
       "hpnicfdot1qVlanTaggedPorts": hpnicfdot1qVlanTaggedPorts,
       "hpnicfdot1qVlanUntaggedPorts": hpnicfdot1qVlanUntaggedPorts,
       "hpnicfdot1qVlanPortIndexs": hpnicfdot1qVlanPortIndexs,
       "hpnicfVlanInterfaceTable": hpnicfVlanInterfaceTable,
       "hpnicfVlanInterfaceEntry": hpnicfVlanInterfaceEntry,
       "hpnicfVlanInterfaceID": hpnicfVlanInterfaceID,
       "hpnicfdot1qVlanID": hpnicfdot1qVlanID,
       "hpnicfdot1qVlanIpAddress": hpnicfdot1qVlanIpAddress,
       "hpnicfdot1qVlanIpAddressMask": hpnicfdot1qVlanIpAddressMask,
       "hpnicfVlanInterfaceAdminStatus": hpnicfVlanInterfaceAdminStatus,
       "hpnicfVlanInterfaceFrameType": hpnicfVlanInterfaceFrameType,
       "hpnicfInterfaceRowStatus": hpnicfInterfaceRowStatus,
       "hpnicfVlanInterfaceIpMethod": hpnicfVlanInterfaceIpMethod,
       "hpnicfVlanInterfaceIfIndex": hpnicfVlanInterfaceIfIndex,
       "hpnicfifIsolateMappingTable": hpnicfifIsolateMappingTable,
       "hpnicfifIsolateMappingEntry": hpnicfifIsolateMappingEntry,
       "hpnicfifIsolatePrimaryVlanID": hpnicfifIsolatePrimaryVlanID,
       "hpnicfifIsolateSecondaryVlanlistLow": hpnicfifIsolateSecondaryVlanlistLow,
       "hpnicfifIsolateSecondaryVlanlistHigh": hpnicfifIsolateSecondaryVlanlistHigh,
       "hpnicfVlanInterfaceAddrTable": hpnicfVlanInterfaceAddrTable,
       "hpnicfVlanInterfaceAddrEntry": hpnicfVlanInterfaceAddrEntry,
       "hpnicfVlanInterfaceIpIfIndex": hpnicfVlanInterfaceIpIfIndex,
       "hpnicfVlanInterfaceIpAddr": hpnicfVlanInterfaceIpAddr,
       "hpnicfVlanInterfaceIpMask": hpnicfVlanInterfaceIpMask,
       "hpnicfVlanInterfaceIpType": hpnicfVlanInterfaceIpType,
       "hpnicfVlanInterfaceIpRowStatus": hpnicfVlanInterfaceIpRowStatus,
       "hpnicfDot1qVlanBatchMIBTable": hpnicfDot1qVlanBatchMIBTable,
       "hpnicfDot1qVlanBatchMIBEntry": hpnicfDot1qVlanBatchMIBEntry,
       "hpnicfdot1qVlanBatchOperIndex": hpnicfdot1qVlanBatchOperIndex,
       "hpnicfdot1qVlanBatchStartIndex": hpnicfdot1qVlanBatchStartIndex,
       "hpnicfdot1qVlanBatchEndIndex": hpnicfdot1qVlanBatchEndIndex,
       "hpnicfdot1qVlanBatchOperStatus": hpnicfdot1qVlanBatchOperStatus,
       "hpnicfdot1qVlanBatchRowStatus": hpnicfdot1qVlanBatchRowStatus,
       "hpnicfdot1qVlanBatchSetOperate": hpnicfdot1qVlanBatchSetOperate,
       "hpnicfifSuperVlanMappingTable": hpnicfifSuperVlanMappingTable,
       "hpnicfifSuperVlanMappingEntry": hpnicfifSuperVlanMappingEntry,
       "hpnicfifSuperVlanID": hpnicfifSuperVlanID,
       "hpnicfifSubVlanlistLow": hpnicfifSubVlanlistLow,
       "hpnicfifSubVlanlistHigh": hpnicfifSubVlanlistHigh,
       "hpnicfPrivateVlanMappingTable": hpnicfPrivateVlanMappingTable,
       "hpnicfPrivateVlanMappingEntry": hpnicfPrivateVlanMappingEntry,
       "hpnicfPrimaryVlanID": hpnicfPrimaryVlanID,
       "hpnicfSecondaryVlanlistLow": hpnicfSecondaryVlanlistLow,
       "hpnicfSecondaryVlanlistHigh": hpnicfSecondaryVlanlistHigh,
       "hpnicfLswVlanProtoObject": hpnicfLswVlanProtoObject,
       "hpnicfVLANMibGarpLeaveAllTime": hpnicfVLANMibGarpLeaveAllTime,
       "hpnicfvLANMibSwitchCountTable": hpnicfvLANMibSwitchCountTable,
       "hpnicfvLANMibSwitchCountEntry": hpnicfvLANMibSwitchCountEntry,
       "hpnicfVLANMibSwitchGMRPRXPkt": hpnicfVLANMibSwitchGMRPRXPkt,
       "hpnicfVLANMibSwitchGVRPRXPkt": hpnicfVLANMibSwitchGVRPRXPkt,
       "hpnicfVLANMibSwitchGMRPTXPkt": hpnicfVLANMibSwitchGMRPTXPkt,
       "hpnicfVLANMibSwitchGVRPTXPkt": hpnicfVLANMibSwitchGVRPTXPkt,
       "hpnicfVLANMibSwitchDiscardedPkt": hpnicfVLANMibSwitchDiscardedPkt,
       "hpnicfVLANMibSwitchGarpStatClear": hpnicfVLANMibSwitchGarpStatClear,
       "hpnicfvLANMibHoldTimeTable": hpnicfvLANMibHoldTimeTable,
       "hpnicfvLANMibHoldTimeEntry": hpnicfvLANMibHoldTimeEntry,
       "hpnicfVLANMibHoldTime": hpnicfVLANMibHoldTime}
)
