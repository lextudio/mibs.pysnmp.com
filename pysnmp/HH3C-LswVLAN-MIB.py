# SNMP MIB module (HH3C-LswVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:44 2024
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
 hh3cifVLANTrunkStatusEntry) = mibBuilder.importSymbols(
    "HH3C-LswINF-MIB",
    "PortList",
    "hh3cifVLANTrunkStatusEntry")

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cVlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cLswVlanMngObject_ObjectIdentity = ObjectIdentity
hh3cLswVlanMngObject = _Hh3cLswVlanMngObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cLswVlanMngObject.setStatus("current")
_Hh3cdot1qVlanMIBTable_Object = MibTable
hh3cdot1qVlanMIBTable = _Hh3cdot1qVlanMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cdot1qVlanMIBTable.setStatus("current")
_Hh3cdot1qVlanMIBEntry_Object = MibTableRow
hh3cdot1qVlanMIBEntry = _Hh3cdot1qVlanMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1)
)
hh3cdot1qVlanMIBEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cdot1qVlanMIBEntry.setStatus("current")
_Hh3cdot1qVlanIndex_Type = Hh3cVlanIndex
_Hh3cdot1qVlanIndex_Object = MibTableColumn
hh3cdot1qVlanIndex = _Hh3cdot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 1),
    _Hh3cdot1qVlanIndex_Type()
)
hh3cdot1qVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanIndex.setStatus("current")


class _Hh3cdot1qVlanName_Type(SnmpAdminString):
    """Custom type hh3cdot1qVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cdot1qVlanName_Type.__name__ = "SnmpAdminString"
_Hh3cdot1qVlanName_Object = MibTableColumn
hh3cdot1qVlanName = _Hh3cdot1qVlanName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 2),
    _Hh3cdot1qVlanName_Type()
)
hh3cdot1qVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanName.setStatus("current")
_Hh3cdot1qVlanPorts_Type = PortList
_Hh3cdot1qVlanPorts_Object = MibTableColumn
hh3cdot1qVlanPorts = _Hh3cdot1qVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 3),
    _Hh3cdot1qVlanPorts_Type()
)
hh3cdot1qVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanPorts.setStatus("current")


class _Hh3cdot1qVlanType_Type(Integer32):
    """Custom type hh3cdot1qVlanType based on Integer32"""
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


_Hh3cdot1qVlanType_Type.__name__ = "Integer32"
_Hh3cdot1qVlanType_Object = MibTableColumn
hh3cdot1qVlanType = _Hh3cdot1qVlanType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 4),
    _Hh3cdot1qVlanType_Type()
)
hh3cdot1qVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanType.setStatus("current")
_Hh3cdot1qVlanMacFilter_Type = TruthValue
_Hh3cdot1qVlanMacFilter_Object = MibTableColumn
hh3cdot1qVlanMacFilter = _Hh3cdot1qVlanMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 5),
    _Hh3cdot1qVlanMacFilter_Type()
)
hh3cdot1qVlanMacFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanMacFilter.setStatus("current")
_Hh3cdot1qVlanMcastUnknownProtos_Type = TruthValue
_Hh3cdot1qVlanMcastUnknownProtos_Object = MibTableColumn
hh3cdot1qVlanMcastUnknownProtos = _Hh3cdot1qVlanMcastUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 6),
    _Hh3cdot1qVlanMcastUnknownProtos_Type()
)
hh3cdot1qVlanMcastUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanMcastUnknownProtos.setStatus("current")
_Hh3cExistInterface_Type = TruthValue
_Hh3cExistInterface_Object = MibTableColumn
hh3cExistInterface = _Hh3cExistInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 7),
    _Hh3cExistInterface_Type()
)
hh3cExistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cExistInterface.setStatus("current")
_Hh3cVlanInterfaceIndex_Type = Integer32
_Hh3cVlanInterfaceIndex_Object = MibTableColumn
hh3cVlanInterfaceIndex = _Hh3cVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 8),
    _Hh3cVlanInterfaceIndex_Type()
)
hh3cVlanInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIndex.setStatus("current")
_Hh3cdot1qVlanMacLearn_Type = TruthValue
_Hh3cdot1qVlanMacLearn_Object = MibTableColumn
hh3cdot1qVlanMacLearn = _Hh3cdot1qVlanMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 9),
    _Hh3cdot1qVlanMacLearn_Type()
)
hh3cdot1qVlanMacLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanMacLearn.setStatus("current")


class _Hh3cdot1qVlanStatus_Type(Integer32):
    """Custom type hh3cdot1qVlanStatus based on Integer32"""
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


_Hh3cdot1qVlanStatus_Type.__name__ = "Integer32"
_Hh3cdot1qVlanStatus_Object = MibTableColumn
hh3cdot1qVlanStatus = _Hh3cdot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 10),
    _Hh3cdot1qVlanStatus_Type()
)
hh3cdot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanStatus.setStatus("current")
_Hh3cdot1qVlanCreationTime_Type = TimeTicks
_Hh3cdot1qVlanCreationTime_Object = MibTableColumn
hh3cdot1qVlanCreationTime = _Hh3cdot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 11),
    _Hh3cdot1qVlanCreationTime_Type()
)
hh3cdot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanCreationTime.setStatus("current")


class _Hh3cdot1qVlanPriority_Type(Integer32):
    """Custom type hh3cdot1qVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cdot1qVlanPriority_Type.__name__ = "Integer32"
_Hh3cdot1qVlanPriority_Object = MibTableColumn
hh3cdot1qVlanPriority = _Hh3cdot1qVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 12),
    _Hh3cdot1qVlanPriority_Type()
)
hh3cdot1qVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanPriority.setStatus("current")
_Hh3cdot1qVlanRowStatus_Type = RowStatus
_Hh3cdot1qVlanRowStatus_Object = MibTableColumn
hh3cdot1qVlanRowStatus = _Hh3cdot1qVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 13),
    _Hh3cdot1qVlanRowStatus_Type()
)
hh3cdot1qVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdot1qVlanRowStatus.setStatus("current")


class _Hh3cdot1qVlanBroadcastSuppression_Type(Integer32):
    """Custom type hh3cdot1qVlanBroadcastSuppression based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cdot1qVlanBroadcastSuppression_Type.__name__ = "Integer32"
_Hh3cdot1qVlanBroadcastSuppression_Object = MibTableColumn
hh3cdot1qVlanBroadcastSuppression = _Hh3cdot1qVlanBroadcastSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 14),
    _Hh3cdot1qVlanBroadcastSuppression_Type()
)
hh3cdot1qVlanBroadcastSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBroadcastSuppression.setStatus("current")


class _Hh3cdot1qVlanBcastSuppressionPPS_Type(Integer32):
    """Custom type hh3cdot1qVlanBcastSuppressionPPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 148800),
    )


_Hh3cdot1qVlanBcastSuppressionPPS_Type.__name__ = "Integer32"
_Hh3cdot1qVlanBcastSuppressionPPS_Object = MibTableColumn
hh3cdot1qVlanBcastSuppressionPPS = _Hh3cdot1qVlanBcastSuppressionPPS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 15),
    _Hh3cdot1qVlanBcastSuppressionPPS_Type()
)
hh3cdot1qVlanBcastSuppressionPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBcastSuppressionPPS.setStatus("current")


class _Hh3cdot1qVlanMulticast_Type(Integer32):
    """Custom type hh3cdot1qVlanMulticast based on Integer32"""
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


_Hh3cdot1qVlanMulticast_Type.__name__ = "Integer32"
_Hh3cdot1qVlanMulticast_Object = MibTableColumn
hh3cdot1qVlanMulticast = _Hh3cdot1qVlanMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 16),
    _Hh3cdot1qVlanMulticast_Type()
)
hh3cdot1qVlanMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanMulticast.setStatus("current")
_Hh3cdot1qVlanTaggedPorts_Type = PortList
_Hh3cdot1qVlanTaggedPorts_Object = MibTableColumn
hh3cdot1qVlanTaggedPorts = _Hh3cdot1qVlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 17),
    _Hh3cdot1qVlanTaggedPorts_Type()
)
hh3cdot1qVlanTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanTaggedPorts.setStatus("current")
_Hh3cdot1qVlanUntaggedPorts_Type = PortList
_Hh3cdot1qVlanUntaggedPorts_Object = MibTableColumn
hh3cdot1qVlanUntaggedPorts = _Hh3cdot1qVlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 18),
    _Hh3cdot1qVlanUntaggedPorts_Type()
)
hh3cdot1qVlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanUntaggedPorts.setStatus("current")
_Hh3cdot1qVlanPortIndexs_Type = OctetString
_Hh3cdot1qVlanPortIndexs_Object = MibTableColumn
hh3cdot1qVlanPortIndexs = _Hh3cdot1qVlanPortIndexs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 1, 1, 19),
    _Hh3cdot1qVlanPortIndexs_Type()
)
hh3cdot1qVlanPortIndexs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanPortIndexs.setStatus("current")
_Hh3cVlanInterfaceTable_Object = MibTable
hh3cVlanInterfaceTable = _Hh3cVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVlanInterfaceTable.setStatus("current")
_Hh3cVlanInterfaceEntry_Object = MibTableRow
hh3cVlanInterfaceEntry = _Hh3cVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1)
)
hh3cVlanInterfaceEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceID"),
)
if mibBuilder.loadTexts:
    hh3cVlanInterfaceEntry.setStatus("current")
_Hh3cVlanInterfaceID_Type = Integer32
_Hh3cVlanInterfaceID_Object = MibTableColumn
hh3cVlanInterfaceID = _Hh3cVlanInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 1),
    _Hh3cVlanInterfaceID_Type()
)
hh3cVlanInterfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceID.setStatus("current")
_Hh3cdot1qVlanID_Type = Hh3cVlanIndex
_Hh3cdot1qVlanID_Object = MibTableColumn
hh3cdot1qVlanID = _Hh3cdot1qVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 2),
    _Hh3cdot1qVlanID_Type()
)
hh3cdot1qVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanID.setStatus("current")
_Hh3cdot1qVlanIpAddress_Type = IpAddress
_Hh3cdot1qVlanIpAddress_Object = MibTableColumn
hh3cdot1qVlanIpAddress = _Hh3cdot1qVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 3),
    _Hh3cdot1qVlanIpAddress_Type()
)
hh3cdot1qVlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanIpAddress.setStatus("current")
_Hh3cdot1qVlanIpAddressMask_Type = IpAddress
_Hh3cdot1qVlanIpAddressMask_Object = MibTableColumn
hh3cdot1qVlanIpAddressMask = _Hh3cdot1qVlanIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 4),
    _Hh3cdot1qVlanIpAddressMask_Type()
)
hh3cdot1qVlanIpAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanIpAddressMask.setStatus("current")


class _Hh3cVlanInterfaceAdminStatus_Type(Integer32):
    """Custom type hh3cVlanInterfaceAdminStatus based on Integer32"""
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


_Hh3cVlanInterfaceAdminStatus_Type.__name__ = "Integer32"
_Hh3cVlanInterfaceAdminStatus_Object = MibTableColumn
hh3cVlanInterfaceAdminStatus = _Hh3cVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 5),
    _Hh3cVlanInterfaceAdminStatus_Type()
)
hh3cVlanInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceAdminStatus.setStatus("current")


class _Hh3cVlanInterfaceFrameType_Type(Integer32):
    """Custom type hh3cVlanInterfaceFrameType based on Integer32"""
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


_Hh3cVlanInterfaceFrameType_Type.__name__ = "Integer32"
_Hh3cVlanInterfaceFrameType_Object = MibTableColumn
hh3cVlanInterfaceFrameType = _Hh3cVlanInterfaceFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 6),
    _Hh3cVlanInterfaceFrameType_Type()
)
hh3cVlanInterfaceFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceFrameType.setStatus("current")
_Hh3cInterfaceRowStatus_Type = RowStatus
_Hh3cInterfaceRowStatus_Object = MibTableColumn
hh3cInterfaceRowStatus = _Hh3cInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 7),
    _Hh3cInterfaceRowStatus_Type()
)
hh3cInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cInterfaceRowStatus.setStatus("current")


class _Hh3cVlanInterfaceIpMethod_Type(Integer32):
    """Custom type hh3cVlanInterfaceIpMethod based on Integer32"""
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


_Hh3cVlanInterfaceIpMethod_Type.__name__ = "Integer32"
_Hh3cVlanInterfaceIpMethod_Object = MibTableColumn
hh3cVlanInterfaceIpMethod = _Hh3cVlanInterfaceIpMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 8),
    _Hh3cVlanInterfaceIpMethod_Type()
)
hh3cVlanInterfaceIpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpMethod.setStatus("current")
_Hh3cVlanInterfaceIfIndex_Type = Integer32
_Hh3cVlanInterfaceIfIndex_Object = MibTableColumn
hh3cVlanInterfaceIfIndex = _Hh3cVlanInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 2, 1, 9),
    _Hh3cVlanInterfaceIfIndex_Type()
)
hh3cVlanInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIfIndex.setStatus("current")
_Hh3cifIsolateMappingTable_Object = MibTable
hh3cifIsolateMappingTable = _Hh3cifIsolateMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cifIsolateMappingTable.setStatus("current")
_Hh3cifIsolateMappingEntry_Object = MibTableRow
hh3cifIsolateMappingEntry = _Hh3cifIsolateMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1)
)
hh3cifIsolateMappingEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cifIsolatePrimaryVlanID"),
)
if mibBuilder.loadTexts:
    hh3cifIsolateMappingEntry.setStatus("current")
_Hh3cifIsolatePrimaryVlanID_Type = Hh3cVlanIndex
_Hh3cifIsolatePrimaryVlanID_Object = MibTableColumn
hh3cifIsolatePrimaryVlanID = _Hh3cifIsolatePrimaryVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 1),
    _Hh3cifIsolatePrimaryVlanID_Type()
)
hh3cifIsolatePrimaryVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifIsolatePrimaryVlanID.setStatus("current")


class _Hh3cifIsolateSecondaryVlanlistLow_Type(OctetString):
    """Custom type hh3cifIsolateSecondaryVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifIsolateSecondaryVlanlistLow_Type.__name__ = "OctetString"
_Hh3cifIsolateSecondaryVlanlistLow_Object = MibTableColumn
hh3cifIsolateSecondaryVlanlistLow = _Hh3cifIsolateSecondaryVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 2),
    _Hh3cifIsolateSecondaryVlanlistLow_Type()
)
hh3cifIsolateSecondaryVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifIsolateSecondaryVlanlistLow.setStatus("current")


class _Hh3cifIsolateSecondaryVlanlistHigh_Type(OctetString):
    """Custom type hh3cifIsolateSecondaryVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifIsolateSecondaryVlanlistHigh_Type.__name__ = "OctetString"
_Hh3cifIsolateSecondaryVlanlistHigh_Object = MibTableColumn
hh3cifIsolateSecondaryVlanlistHigh = _Hh3cifIsolateSecondaryVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 4, 1, 3),
    _Hh3cifIsolateSecondaryVlanlistHigh_Type()
)
hh3cifIsolateSecondaryVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifIsolateSecondaryVlanlistHigh.setStatus("current")
_Hh3cVlanInterfaceAddrTable_Object = MibTable
hh3cVlanInterfaceAddrTable = _Hh3cVlanInterfaceAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cVlanInterfaceAddrTable.setStatus("current")
_Hh3cVlanInterfaceAddrEntry_Object = MibTableRow
hh3cVlanInterfaceAddrEntry = _Hh3cVlanInterfaceAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1)
)
hh3cVlanInterfaceAddrEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceIpIfIndex"),
    (0, "HH3C-LswVLAN-MIB", "hh3cVlanInterfaceIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cVlanInterfaceAddrEntry.setStatus("current")
_Hh3cVlanInterfaceIpIfIndex_Type = Integer32
_Hh3cVlanInterfaceIpIfIndex_Object = MibTableColumn
hh3cVlanInterfaceIpIfIndex = _Hh3cVlanInterfaceIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 1),
    _Hh3cVlanInterfaceIpIfIndex_Type()
)
hh3cVlanInterfaceIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpIfIndex.setStatus("current")
_Hh3cVlanInterfaceIpAddr_Type = IpAddress
_Hh3cVlanInterfaceIpAddr_Object = MibTableColumn
hh3cVlanInterfaceIpAddr = _Hh3cVlanInterfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 2),
    _Hh3cVlanInterfaceIpAddr_Type()
)
hh3cVlanInterfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpAddr.setStatus("current")
_Hh3cVlanInterfaceIpMask_Type = IpAddress
_Hh3cVlanInterfaceIpMask_Object = MibTableColumn
hh3cVlanInterfaceIpMask = _Hh3cVlanInterfaceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 3),
    _Hh3cVlanInterfaceIpMask_Type()
)
hh3cVlanInterfaceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpMask.setStatus("current")


class _Hh3cVlanInterfaceIpType_Type(Integer32):
    """Custom type hh3cVlanInterfaceIpType based on Integer32"""
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


_Hh3cVlanInterfaceIpType_Type.__name__ = "Integer32"
_Hh3cVlanInterfaceIpType_Object = MibTableColumn
hh3cVlanInterfaceIpType = _Hh3cVlanInterfaceIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 4),
    _Hh3cVlanInterfaceIpType_Type()
)
hh3cVlanInterfaceIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpType.setStatus("current")
_Hh3cVlanInterfaceIpRowStatus_Type = RowStatus
_Hh3cVlanInterfaceIpRowStatus_Object = MibTableColumn
hh3cVlanInterfaceIpRowStatus = _Hh3cVlanInterfaceIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 5, 1, 5),
    _Hh3cVlanInterfaceIpRowStatus_Type()
)
hh3cVlanInterfaceIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVlanInterfaceIpRowStatus.setStatus("current")
_Hh3cDot1qVlanBatchMIBTable_Object = MibTable
hh3cDot1qVlanBatchMIBTable = _Hh3cDot1qVlanBatchMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot1qVlanBatchMIBTable.setStatus("current")
_Hh3cDot1qVlanBatchMIBEntry_Object = MibTableRow
hh3cDot1qVlanBatchMIBEntry = _Hh3cDot1qVlanBatchMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1)
)
hh3cDot1qVlanBatchMIBEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cdot1qVlanBatchOperIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot1qVlanBatchMIBEntry.setStatus("current")
_Hh3cdot1qVlanBatchOperIndex_Type = Integer32
_Hh3cdot1qVlanBatchOperIndex_Object = MibTableColumn
hh3cdot1qVlanBatchOperIndex = _Hh3cdot1qVlanBatchOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 1),
    _Hh3cdot1qVlanBatchOperIndex_Type()
)
hh3cdot1qVlanBatchOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchOperIndex.setStatus("current")
_Hh3cdot1qVlanBatchStartIndex_Type = Hh3cVlanIndex
_Hh3cdot1qVlanBatchStartIndex_Object = MibTableColumn
hh3cdot1qVlanBatchStartIndex = _Hh3cdot1qVlanBatchStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 2),
    _Hh3cdot1qVlanBatchStartIndex_Type()
)
hh3cdot1qVlanBatchStartIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchStartIndex.setStatus("current")
_Hh3cdot1qVlanBatchEndIndex_Type = Hh3cVlanIndex
_Hh3cdot1qVlanBatchEndIndex_Object = MibTableColumn
hh3cdot1qVlanBatchEndIndex = _Hh3cdot1qVlanBatchEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 3),
    _Hh3cdot1qVlanBatchEndIndex_Type()
)
hh3cdot1qVlanBatchEndIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchEndIndex.setStatus("current")


class _Hh3cdot1qVlanBatchOperStatus_Type(Integer32):
    """Custom type hh3cdot1qVlanBatchOperStatus based on Integer32"""
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


_Hh3cdot1qVlanBatchOperStatus_Type.__name__ = "Integer32"
_Hh3cdot1qVlanBatchOperStatus_Object = MibTableColumn
hh3cdot1qVlanBatchOperStatus = _Hh3cdot1qVlanBatchOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 4),
    _Hh3cdot1qVlanBatchOperStatus_Type()
)
hh3cdot1qVlanBatchOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchOperStatus.setStatus("current")
_Hh3cdot1qVlanBatchRowStatus_Type = RowStatus
_Hh3cdot1qVlanBatchRowStatus_Object = MibTableColumn
hh3cdot1qVlanBatchRowStatus = _Hh3cdot1qVlanBatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 5),
    _Hh3cdot1qVlanBatchRowStatus_Type()
)
hh3cdot1qVlanBatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchRowStatus.setStatus("current")


class _Hh3cdot1qVlanBatchSetOperate_Type(Integer32):
    """Custom type hh3cdot1qVlanBatchSetOperate based on Integer32"""
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


_Hh3cdot1qVlanBatchSetOperate_Type.__name__ = "Integer32"
_Hh3cdot1qVlanBatchSetOperate_Object = MibTableColumn
hh3cdot1qVlanBatchSetOperate = _Hh3cdot1qVlanBatchSetOperate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 6, 1, 6),
    _Hh3cdot1qVlanBatchSetOperate_Type()
)
hh3cdot1qVlanBatchSetOperate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cdot1qVlanBatchSetOperate.setStatus("current")
_Hh3cifSuperVlanMappingTable_Object = MibTable
hh3cifSuperVlanMappingTable = _Hh3cifSuperVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cifSuperVlanMappingTable.setStatus("current")
_Hh3cifSuperVlanMappingEntry_Object = MibTableRow
hh3cifSuperVlanMappingEntry = _Hh3cifSuperVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1)
)
hh3cifSuperVlanMappingEntry.setIndexNames(
    (0, "HH3C-LswVLAN-MIB", "hh3cifSuperVlanID"),
)
if mibBuilder.loadTexts:
    hh3cifSuperVlanMappingEntry.setStatus("current")
_Hh3cifSuperVlanID_Type = Hh3cVlanIndex
_Hh3cifSuperVlanID_Object = MibTableColumn
hh3cifSuperVlanID = _Hh3cifSuperVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 1),
    _Hh3cifSuperVlanID_Type()
)
hh3cifSuperVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifSuperVlanID.setStatus("current")


class _Hh3cifSubVlanlistLow_Type(OctetString):
    """Custom type hh3cifSubVlanlistLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifSubVlanlistLow_Type.__name__ = "OctetString"
_Hh3cifSubVlanlistLow_Object = MibTableColumn
hh3cifSubVlanlistLow = _Hh3cifSubVlanlistLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 2),
    _Hh3cifSubVlanlistLow_Type()
)
hh3cifSubVlanlistLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifSubVlanlistLow.setStatus("current")


class _Hh3cifSubVlanlistHigh_Type(OctetString):
    """Custom type hh3cifSubVlanlistHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifSubVlanlistHigh_Type.__name__ = "OctetString"
_Hh3cifSubVlanlistHigh_Object = MibTableColumn
hh3cifSubVlanlistHigh = _Hh3cifSubVlanlistHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 1, 7, 1, 3),
    _Hh3cifSubVlanlistHigh_Type()
)
hh3cifSubVlanlistHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifSubVlanlistHigh.setStatus("current")
_Hh3cLswVlanProtoObject_ObjectIdentity = ObjectIdentity
hh3cLswVlanProtoObject = _Hh3cLswVlanProtoObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cLswVlanProtoObject.setStatus("current")


class _Hh3cVLANMibGarpLeaveAllTime_Type(TimeInterval):
    """Custom type hh3cVLANMibGarpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_Hh3cVLANMibGarpLeaveAllTime_Object = MibScalar
hh3cVLANMibGarpLeaveAllTime = _Hh3cVLANMibGarpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 14),
    _Hh3cVLANMibGarpLeaveAllTime_Type()
)
hh3cVLANMibGarpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVLANMibGarpLeaveAllTime.setStatus("current")
_Hh3cvLANMibSwitchCountTable_Object = MibTable
hh3cvLANMibSwitchCountTable = _Hh3cvLANMibSwitchCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cvLANMibSwitchCountTable.setStatus("current")
_Hh3cvLANMibSwitchCountEntry_Object = MibTableRow
hh3cvLANMibSwitchCountEntry = _Hh3cvLANMibSwitchCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    hh3cvLANMibSwitchCountEntry.setStatus("current")
_Hh3cVLANMibSwitchGMRPRXPkt_Type = Counter32
_Hh3cVLANMibSwitchGMRPRXPkt_Object = MibTableColumn
hh3cVLANMibSwitchGMRPRXPkt = _Hh3cVLANMibSwitchGMRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 1),
    _Hh3cVLANMibSwitchGMRPRXPkt_Type()
)
hh3cVLANMibSwitchGMRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchGMRPRXPkt.setStatus("current")
_Hh3cVLANMibSwitchGVRPRXPkt_Type = Counter32
_Hh3cVLANMibSwitchGVRPRXPkt_Object = MibTableColumn
hh3cVLANMibSwitchGVRPRXPkt = _Hh3cVLANMibSwitchGVRPRXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 2),
    _Hh3cVLANMibSwitchGVRPRXPkt_Type()
)
hh3cVLANMibSwitchGVRPRXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchGVRPRXPkt.setStatus("current")
_Hh3cVLANMibSwitchGMRPTXPkt_Type = Counter32
_Hh3cVLANMibSwitchGMRPTXPkt_Object = MibTableColumn
hh3cVLANMibSwitchGMRPTXPkt = _Hh3cVLANMibSwitchGMRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 3),
    _Hh3cVLANMibSwitchGMRPTXPkt_Type()
)
hh3cVLANMibSwitchGMRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchGMRPTXPkt.setStatus("current")
_Hh3cVLANMibSwitchGVRPTXPkt_Type = Counter32
_Hh3cVLANMibSwitchGVRPTXPkt_Object = MibTableColumn
hh3cVLANMibSwitchGVRPTXPkt = _Hh3cVLANMibSwitchGVRPTXPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 4),
    _Hh3cVLANMibSwitchGVRPTXPkt_Type()
)
hh3cVLANMibSwitchGVRPTXPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchGVRPTXPkt.setStatus("current")
_Hh3cVLANMibSwitchDiscardedPkt_Type = Counter32
_Hh3cVLANMibSwitchDiscardedPkt_Object = MibTableColumn
hh3cVLANMibSwitchDiscardedPkt = _Hh3cVLANMibSwitchDiscardedPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 5),
    _Hh3cVLANMibSwitchDiscardedPkt_Type()
)
hh3cVLANMibSwitchDiscardedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchDiscardedPkt.setStatus("current")


class _Hh3cVLANMibSwitchGarpStatClear_Type(Integer32):
    """Custom type hh3cVLANMibSwitchGarpStatClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hh3cVLANMibSwitchGarpStatClear_Type.__name__ = "Integer32"
_Hh3cVLANMibSwitchGarpStatClear_Object = MibTableColumn
hh3cVLANMibSwitchGarpStatClear = _Hh3cVLANMibSwitchGarpStatClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 15, 1, 6),
    _Hh3cVLANMibSwitchGarpStatClear_Type()
)
hh3cVLANMibSwitchGarpStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVLANMibSwitchGarpStatClear.setStatus("current")
_Hh3cvLANMibHoldTimeTable_Object = MibTable
hh3cvLANMibHoldTimeTable = _Hh3cvLANMibHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cvLANMibHoldTimeTable.setStatus("current")
_Hh3cvLANMibHoldTimeEntry_Object = MibTableRow
hh3cvLANMibHoldTimeEntry = _Hh3cvLANMibHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    hh3cvLANMibHoldTimeEntry.setStatus("current")


class _Hh3cVLANMibHoldTime_Type(Integer32):
    """Custom type hh3cVLANMibHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32765),
    )


_Hh3cVLANMibHoldTime_Type.__name__ = "Integer32"
_Hh3cVLANMibHoldTime_Object = MibTableColumn
hh3cVLANMibHoldTime = _Hh3cVLANMibHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 2, 2, 16, 1, 1),
    _Hh3cVLANMibHoldTime_Type()
)
hh3cVLANMibHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVLANMibHoldTime.setStatus("current")
hh3cifVLANTrunkStatusEntry.registerAugmentions(
    ("HH3C-LswVLAN-MIB",
     "hh3cvLANMibSwitchCountEntry")
)
hh3cvLANMibSwitchCountEntry.setIndexNames(*hh3cifVLANTrunkStatusEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("HH3C-LswVLAN-MIB",
     "hh3cvLANMibHoldTimeEntry")
)
hh3cvLANMibHoldTimeEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswVLAN-MIB",
    **{"Hh3cVlanIndex": Hh3cVlanIndex,
       "hh3cLswVlan": hh3cLswVlan,
       "hh3cLswVlanMngObject": hh3cLswVlanMngObject,
       "hh3cdot1qVlanMIBTable": hh3cdot1qVlanMIBTable,
       "hh3cdot1qVlanMIBEntry": hh3cdot1qVlanMIBEntry,
       "hh3cdot1qVlanIndex": hh3cdot1qVlanIndex,
       "hh3cdot1qVlanName": hh3cdot1qVlanName,
       "hh3cdot1qVlanPorts": hh3cdot1qVlanPorts,
       "hh3cdot1qVlanType": hh3cdot1qVlanType,
       "hh3cdot1qVlanMacFilter": hh3cdot1qVlanMacFilter,
       "hh3cdot1qVlanMcastUnknownProtos": hh3cdot1qVlanMcastUnknownProtos,
       "hh3cExistInterface": hh3cExistInterface,
       "hh3cVlanInterfaceIndex": hh3cVlanInterfaceIndex,
       "hh3cdot1qVlanMacLearn": hh3cdot1qVlanMacLearn,
       "hh3cdot1qVlanStatus": hh3cdot1qVlanStatus,
       "hh3cdot1qVlanCreationTime": hh3cdot1qVlanCreationTime,
       "hh3cdot1qVlanPriority": hh3cdot1qVlanPriority,
       "hh3cdot1qVlanRowStatus": hh3cdot1qVlanRowStatus,
       "hh3cdot1qVlanBroadcastSuppression": hh3cdot1qVlanBroadcastSuppression,
       "hh3cdot1qVlanBcastSuppressionPPS": hh3cdot1qVlanBcastSuppressionPPS,
       "hh3cdot1qVlanMulticast": hh3cdot1qVlanMulticast,
       "hh3cdot1qVlanTaggedPorts": hh3cdot1qVlanTaggedPorts,
       "hh3cdot1qVlanUntaggedPorts": hh3cdot1qVlanUntaggedPorts,
       "hh3cdot1qVlanPortIndexs": hh3cdot1qVlanPortIndexs,
       "hh3cVlanInterfaceTable": hh3cVlanInterfaceTable,
       "hh3cVlanInterfaceEntry": hh3cVlanInterfaceEntry,
       "hh3cVlanInterfaceID": hh3cVlanInterfaceID,
       "hh3cdot1qVlanID": hh3cdot1qVlanID,
       "hh3cdot1qVlanIpAddress": hh3cdot1qVlanIpAddress,
       "hh3cdot1qVlanIpAddressMask": hh3cdot1qVlanIpAddressMask,
       "hh3cVlanInterfaceAdminStatus": hh3cVlanInterfaceAdminStatus,
       "hh3cVlanInterfaceFrameType": hh3cVlanInterfaceFrameType,
       "hh3cInterfaceRowStatus": hh3cInterfaceRowStatus,
       "hh3cVlanInterfaceIpMethod": hh3cVlanInterfaceIpMethod,
       "hh3cVlanInterfaceIfIndex": hh3cVlanInterfaceIfIndex,
       "hh3cifIsolateMappingTable": hh3cifIsolateMappingTable,
       "hh3cifIsolateMappingEntry": hh3cifIsolateMappingEntry,
       "hh3cifIsolatePrimaryVlanID": hh3cifIsolatePrimaryVlanID,
       "hh3cifIsolateSecondaryVlanlistLow": hh3cifIsolateSecondaryVlanlistLow,
       "hh3cifIsolateSecondaryVlanlistHigh": hh3cifIsolateSecondaryVlanlistHigh,
       "hh3cVlanInterfaceAddrTable": hh3cVlanInterfaceAddrTable,
       "hh3cVlanInterfaceAddrEntry": hh3cVlanInterfaceAddrEntry,
       "hh3cVlanInterfaceIpIfIndex": hh3cVlanInterfaceIpIfIndex,
       "hh3cVlanInterfaceIpAddr": hh3cVlanInterfaceIpAddr,
       "hh3cVlanInterfaceIpMask": hh3cVlanInterfaceIpMask,
       "hh3cVlanInterfaceIpType": hh3cVlanInterfaceIpType,
       "hh3cVlanInterfaceIpRowStatus": hh3cVlanInterfaceIpRowStatus,
       "hh3cDot1qVlanBatchMIBTable": hh3cDot1qVlanBatchMIBTable,
       "hh3cDot1qVlanBatchMIBEntry": hh3cDot1qVlanBatchMIBEntry,
       "hh3cdot1qVlanBatchOperIndex": hh3cdot1qVlanBatchOperIndex,
       "hh3cdot1qVlanBatchStartIndex": hh3cdot1qVlanBatchStartIndex,
       "hh3cdot1qVlanBatchEndIndex": hh3cdot1qVlanBatchEndIndex,
       "hh3cdot1qVlanBatchOperStatus": hh3cdot1qVlanBatchOperStatus,
       "hh3cdot1qVlanBatchRowStatus": hh3cdot1qVlanBatchRowStatus,
       "hh3cdot1qVlanBatchSetOperate": hh3cdot1qVlanBatchSetOperate,
       "hh3cifSuperVlanMappingTable": hh3cifSuperVlanMappingTable,
       "hh3cifSuperVlanMappingEntry": hh3cifSuperVlanMappingEntry,
       "hh3cifSuperVlanID": hh3cifSuperVlanID,
       "hh3cifSubVlanlistLow": hh3cifSubVlanlistLow,
       "hh3cifSubVlanlistHigh": hh3cifSubVlanlistHigh,
       "hh3cLswVlanProtoObject": hh3cLswVlanProtoObject,
       "hh3cVLANMibGarpLeaveAllTime": hh3cVLANMibGarpLeaveAllTime,
       "hh3cvLANMibSwitchCountTable": hh3cvLANMibSwitchCountTable,
       "hh3cvLANMibSwitchCountEntry": hh3cvLANMibSwitchCountEntry,
       "hh3cVLANMibSwitchGMRPRXPkt": hh3cVLANMibSwitchGMRPRXPkt,
       "hh3cVLANMibSwitchGVRPRXPkt": hh3cVLANMibSwitchGVRPRXPkt,
       "hh3cVLANMibSwitchGMRPTXPkt": hh3cVLANMibSwitchGMRPTXPkt,
       "hh3cVLANMibSwitchGVRPTXPkt": hh3cVLANMibSwitchGVRPTXPkt,
       "hh3cVLANMibSwitchDiscardedPkt": hh3cVLANMibSwitchDiscardedPkt,
       "hh3cVLANMibSwitchGarpStatClear": hh3cVLANMibSwitchGarpStatClear,
       "hh3cvLANMibHoldTimeTable": hh3cvLANMibHoldTimeTable,
       "hh3cvLANMibHoldTimeEntry": hh3cvLANMibHoldTimeEntry,
       "hh3cVLANMibHoldTime": hh3cVLANMibHoldTime}
)
