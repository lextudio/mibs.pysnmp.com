# SNMP MIB module (CISCO-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VSAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:04 2024
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

(FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "VsanIndex")

(CiscoMilliSeconds,
 ListIndex,
 ListIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds",
    "ListIndex",
    "ListIndexOrZero")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVsanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282)
)
ciscoVsanMIB.setRevisions(
        ("2006-02-06 00:00",
         "2005-12-07 00:00",
         "2005-10-07 00:00",
         "2005-06-07 00:00",
         "2004-02-18 00:00",
         "2003-12-02 00:00",
         "2003-05-07 00:00",
         "2003-04-23 00:00",
         "2002-12-18 00:00",
         "2002-11-04 00:00",
         "2002-09-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VsanMediaType(Integer32, TextualConvention):
    status = "current"
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
        *(("ethernet", 2),
          ("fibreChannel", 1),
          ("infiniband", 3),
          ("other", 4))
    )



class VsanAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspended", 2))
    )



class VsanOperationalState(Integer32, TextualConvention):
    status = "current"
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



class VsanLoadBalancingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srcIdDestId", 1),
          ("srcIdDestIdOxId", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVsanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVsanMIBObjects = _CiscoVsanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1)
)
_VsanConfiguration_ObjectIdentity = ObjectIdentity
vsanConfiguration = _VsanConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1)
)


class _VsanNumber_Type(Integer32):
    """Custom type vsanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VsanNumber_Type.__name__ = "Integer32"
_VsanNumber_Object = MibScalar
vsanNumber = _VsanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 1),
    _VsanNumber_Type()
)
vsanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanNumber.setStatus("current")
_VsanLastChange_Type = TimeStamp
_VsanLastChange_Object = MibScalar
vsanLastChange = _VsanLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 2),
    _VsanLastChange_Type()
)
vsanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanLastChange.setStatus("current")
_VsanTable_Object = MibTable
vsanTable = _VsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vsanTable.setStatus("current")
_VsanEntry_Object = MibTableRow
vsanEntry = _VsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1)
)
vsanEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    vsanEntry.setStatus("current")
_VsanIndex_Type = VsanIndex
_VsanIndex_Object = MibTableColumn
vsanIndex = _VsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 1),
    _VsanIndex_Type()
)
vsanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsanIndex.setStatus("current")


class _VsanName_Type(SnmpAdminString):
    """Custom type vsanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VsanName_Type.__name__ = "SnmpAdminString"
_VsanName_Object = MibTableColumn
vsanName = _VsanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 2),
    _VsanName_Type()
)
vsanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanName.setStatus("current")


class _VsanMediaType_Type(VsanMediaType):
    """Custom type vsanMediaType based on VsanMediaType"""


_VsanMediaType_Object = MibTableColumn
vsanMediaType = _VsanMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 3),
    _VsanMediaType_Type()
)
vsanMediaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanMediaType.setStatus("current")


class _VsanAdminState_Type(VsanAdminState):
    """Custom type vsanAdminState based on VsanAdminState"""


_VsanAdminState_Object = MibTableColumn
vsanAdminState = _VsanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 4),
    _VsanAdminState_Type()
)
vsanAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanAdminState.setStatus("current")


class _VsanMtu_Type(Unsigned32):
    """Custom type vsanMtu based on Unsigned32"""
    defaultValue = 2112

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VsanMtu_Type.__name__ = "Unsigned32"
_VsanMtu_Object = MibTableColumn
vsanMtu = _VsanMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 5),
    _VsanMtu_Type()
)
vsanMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanMtu.setStatus("current")


class _VsanLoadBalancingType_Type(VsanLoadBalancingType):
    """Custom type vsanLoadBalancingType based on VsanLoadBalancingType"""


_VsanLoadBalancingType_Object = MibTableColumn
vsanLoadBalancingType = _VsanLoadBalancingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 6),
    _VsanLoadBalancingType_Type()
)
vsanLoadBalancingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanLoadBalancingType.setStatus("current")


class _VsanInterOperMode_Type(TruthValue):
    """Custom type vsanInterOperMode based on TruthValue"""


_VsanInterOperMode_Object = MibTableColumn
vsanInterOperMode = _VsanInterOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 7),
    _VsanInterOperMode_Type()
)
vsanInterOperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanInterOperMode.setStatus("deprecated")
_VsanOperState_Type = VsanOperationalState
_VsanOperState_Object = MibTableColumn
vsanOperState = _VsanOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 8),
    _VsanOperState_Type()
)
vsanOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanOperState.setStatus("current")
_VsanRowStatus_Type = RowStatus
_VsanRowStatus_Object = MibTableColumn
vsanRowStatus = _VsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 9),
    _VsanRowStatus_Type()
)
vsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanRowStatus.setStatus("current")


class _VsanInterOperValue_Type(Integer32):
    """Custom type vsanInterOperValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VsanInterOperValue_Type.__name__ = "Integer32"
_VsanInterOperValue_Object = MibTableColumn
vsanInterOperValue = _VsanInterOperValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 10),
    _VsanInterOperValue_Type()
)
vsanInterOperValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanInterOperValue.setStatus("current")


class _VsanInorderDelivery_Type(TruthValue):
    """Custom type vsanInorderDelivery based on TruthValue"""


_VsanInorderDelivery_Object = MibTableColumn
vsanInorderDelivery = _VsanInorderDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 11),
    _VsanInorderDelivery_Type()
)
vsanInorderDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanInorderDelivery.setStatus("current")


class _VsanNetworkDropLatency_Type(CiscoMilliSeconds):
    """Custom type vsanNetworkDropLatency based on CiscoMilliSeconds"""
    defaultValue = 2000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_VsanNetworkDropLatency_Type.__name__ = "CiscoMilliSeconds"
_VsanNetworkDropLatency_Object = MibTableColumn
vsanNetworkDropLatency = _VsanNetworkDropLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 3, 1, 12),
    _VsanNetworkDropLatency_Type()
)
vsanNetworkDropLatency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanNetworkDropLatency.setStatus("current")
if mibBuilder.loadTexts:
    vsanNetworkDropLatency.setUnits("msec")
_NotifyVsanIndex_Type = VsanIndex
_NotifyVsanIndex_Object = MibScalar
notifyVsanIndex = _NotifyVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 1, 4),
    _NotifyVsanIndex_Type()
)
notifyVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    notifyVsanIndex.setStatus("current")
_VsanMembership_ObjectIdentity = ObjectIdentity
vsanMembership = _VsanMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2)
)


class _VsanDenyUnknownWwn_Type(TruthValue):
    """Custom type vsanDenyUnknownWwn based on TruthValue"""


_VsanDenyUnknownWwn_Object = MibScalar
vsanDenyUnknownWwn = _VsanDenyUnknownWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 1),
    _VsanDenyUnknownWwn_Type()
)
vsanDenyUnknownWwn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsanDenyUnknownWwn.setStatus("current")


class _VsanWwnListNumber_Type(Integer32):
    """Custom type vsanWwnListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsanWwnListNumber_Type.__name__ = "Integer32"
_VsanWwnListNumber_Object = MibScalar
vsanWwnListNumber = _VsanWwnListNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 2),
    _VsanWwnListNumber_Type()
)
vsanWwnListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanWwnListNumber.setStatus("current")
_VsanWwnListTable_Object = MibTable
vsanWwnListTable = _VsanWwnListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3)
)
if mibBuilder.loadTexts:
    vsanWwnListTable.setStatus("current")
_VsanWwnListEntry_Object = MibTableRow
vsanWwnListEntry = _VsanWwnListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1)
)
vsanWwnListEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanWwnListIndex"),
    (0, "CISCO-VSAN-MIB", "vsanWwnListWwnIndex"),
)
if mibBuilder.loadTexts:
    vsanWwnListEntry.setStatus("current")


class _VsanWwnListIndex_Type(ListIndex):
    """Custom type vsanWwnListIndex based on ListIndex"""
    subtypeSpec = ListIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsanWwnListIndex_Type.__name__ = "ListIndex"
_VsanWwnListIndex_Object = MibTableColumn
vsanWwnListIndex = _VsanWwnListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 1),
    _VsanWwnListIndex_Type()
)
vsanWwnListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsanWwnListIndex.setStatus("current")


class _VsanWwnListWwnIndex_Type(Unsigned32):
    """Custom type vsanWwnListWwnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VsanWwnListWwnIndex_Type.__name__ = "Unsigned32"
_VsanWwnListWwnIndex_Object = MibTableColumn
vsanWwnListWwnIndex = _VsanWwnListWwnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 2),
    _VsanWwnListWwnIndex_Type()
)
vsanWwnListWwnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vsanWwnListWwnIndex.setStatus("current")
_VsanWwnListWwn_Type = FcNameId
_VsanWwnListWwn_Object = MibTableColumn
vsanWwnListWwn = _VsanWwnListWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 3),
    _VsanWwnListWwn_Type()
)
vsanWwnListWwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanWwnListWwn.setStatus("current")
_VsanWwnListRowStatus_Type = RowStatus
_VsanWwnListRowStatus_Object = MibTableColumn
vsanWwnListRowStatus = _VsanWwnListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 3, 1, 4),
    _VsanWwnListRowStatus_Type()
)
vsanWwnListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanWwnListRowStatus.setStatus("current")


class _VsanIfNumber_Type(Integer32):
    """Custom type vsanIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsanIfNumber_Type.__name__ = "Integer32"
_VsanIfNumber_Object = MibScalar
vsanIfNumber = _VsanIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 4),
    _VsanIfNumber_Type()
)
vsanIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanIfNumber.setStatus("current")
_VsanIfTable_Object = MibTable
vsanIfTable = _VsanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5)
)
if mibBuilder.loadTexts:
    vsanIfTable.setStatus("current")
_VsanIfEntry_Object = MibTableRow
vsanIfEntry = _VsanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1)
)
vsanIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vsanIfEntry.setStatus("current")


class _VsanIfVsan_Type(VsanIndex):
    """Custom type vsanIfVsan based on VsanIndex"""
    defaultValue = 1


_VsanIfVsan_Object = MibTableColumn
vsanIfVsan = _VsanIfVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 1),
    _VsanIfVsan_Type()
)
vsanIfVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsanIfVsan.setStatus("current")


class _VsanIfDenyList_Type(ListIndexOrZero):
    """Custom type vsanIfDenyList based on ListIndexOrZero"""
    defaultValue = 0


_VsanIfDenyList_Object = MibTableColumn
vsanIfDenyList = _VsanIfDenyList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 5, 1, 2),
    _VsanIfDenyList_Type()
)
vsanIfDenyList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsanIfDenyList.setStatus("current")


class _VsanDynamicListNumber_Type(Integer32):
    """Custom type vsanDynamicListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VsanDynamicListNumber_Type.__name__ = "Integer32"
_VsanDynamicListNumber_Object = MibScalar
vsanDynamicListNumber = _VsanDynamicListNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 6),
    _VsanDynamicListNumber_Type()
)
vsanDynamicListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanDynamicListNumber.setStatus("current")
_VsanDynamicTable_Object = MibTable
vsanDynamicTable = _VsanDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7)
)
if mibBuilder.loadTexts:
    vsanDynamicTable.setStatus("current")
_VsanDynamicEntry_Object = MibTableRow
vsanDynamicEntry = _VsanDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1)
)
vsanDynamicEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanWwnListIndex"),
)
if mibBuilder.loadTexts:
    vsanDynamicEntry.setStatus("current")


class _VsanDynamicVsan_Type(VsanIndex):
    """Custom type vsanDynamicVsan based on VsanIndex"""
    defaultValue = 1


_VsanDynamicVsan_Object = MibTableColumn
vsanDynamicVsan = _VsanDynamicVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 1),
    _VsanDynamicVsan_Type()
)
vsanDynamicVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanDynamicVsan.setStatus("current")
_VsanDynamicRowStatus_Type = RowStatus
_VsanDynamicRowStatus_Object = MibTableColumn
vsanDynamicRowStatus = _VsanDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 7, 1, 2),
    _VsanDynamicRowStatus_Type()
)
vsanDynamicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanDynamicRowStatus.setStatus("current")
_VsanMembershipSummaryTable_Object = MibTable
vsanMembershipSummaryTable = _VsanMembershipSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8)
)
if mibBuilder.loadTexts:
    vsanMembershipSummaryTable.setStatus("current")
_VsanMembershipSummaryEntry_Object = MibTableRow
vsanMembershipSummaryEntry = _VsanMembershipSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1)
)
vsanMembershipSummaryEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-VSAN-MIB", "vsanMembershipSummaryInterface"),
)
if mibBuilder.loadTexts:
    vsanMembershipSummaryEntry.setStatus("current")
_VsanMembershipSummaryInterface_Type = InterfaceIndex
_VsanMembershipSummaryInterface_Object = MibTableColumn
vsanMembershipSummaryInterface = _VsanMembershipSummaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 1),
    _VsanMembershipSummaryInterface_Type()
)
vsanMembershipSummaryInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanMembershipSummaryInterface.setStatus("current")


class _VsanMembershipSummaryIntfType_Type(Integer32):
    """Custom type vsanMembershipSummaryIntfType based on Integer32"""
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
          ("static", 2),
          ("unknown", 1))
    )


_VsanMembershipSummaryIntfType_Type.__name__ = "Integer32"
_VsanMembershipSummaryIntfType_Object = MibTableColumn
vsanMembershipSummaryIntfType = _VsanMembershipSummaryIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 2, 8, 1, 2),
    _VsanMembershipSummaryIntfType_Type()
)
vsanMembershipSummaryIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanMembershipSummaryIntfType.setStatus("current")
_VsanNotification_ObjectIdentity = ObjectIdentity
vsanNotification = _VsanNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3)
)
_VsanNotifications_ObjectIdentity = ObjectIdentity
vsanNotifications = _VsanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0)
)
_VsanFcConfiguration_ObjectIdentity = ObjectIdentity
vsanFcConfiguration = _VsanFcConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4)
)


class _FcTimerRatov_Type(CiscoMilliSeconds):
    """Custom type fcTimerRatov based on CiscoMilliSeconds"""
    defaultValue = 10000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 100000),
    )


_FcTimerRatov_Type.__name__ = "CiscoMilliSeconds"
_FcTimerRatov_Object = MibScalar
fcTimerRatov = _FcTimerRatov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 1),
    _FcTimerRatov_Type()
)
fcTimerRatov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcTimerRatov.setStatus("current")
if mibBuilder.loadTexts:
    fcTimerRatov.setUnits("msec")


class _FcTimerEdtov_Type(CiscoMilliSeconds):
    """Custom type fcTimerEdtov based on CiscoMilliSeconds"""
    defaultValue = 2000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 100000),
    )


_FcTimerEdtov_Type.__name__ = "CiscoMilliSeconds"
_FcTimerEdtov_Object = MibScalar
fcTimerEdtov = _FcTimerEdtov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 2),
    _FcTimerEdtov_Type()
)
fcTimerEdtov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcTimerEdtov.setStatus("current")
if mibBuilder.loadTexts:
    fcTimerEdtov.setUnits("msec")
_FcTimerFstov_Type = CiscoMilliSeconds
_FcTimerFstov_Object = MibScalar
fcTimerFstov = _FcTimerFstov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 3),
    _FcTimerFstov_Type()
)
fcTimerFstov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTimerFstov.setStatus("current")
if mibBuilder.loadTexts:
    fcTimerFstov.setUnits("msec")


class _FcTimerDstov_Type(CiscoMilliSeconds):
    """Custom type fcTimerDstov based on CiscoMilliSeconds"""
    defaultValue = 5000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 100000),
    )


_FcTimerDstov_Type.__name__ = "CiscoMilliSeconds"
_FcTimerDstov_Object = MibScalar
fcTimerDstov = _FcTimerDstov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 4),
    _FcTimerDstov_Type()
)
fcTimerDstov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcTimerDstov.setStatus("current")
if mibBuilder.loadTexts:
    fcTimerDstov.setUnits("msec")


class _FcNetworkDropLatency_Type(CiscoMilliSeconds):
    """Custom type fcNetworkDropLatency based on CiscoMilliSeconds"""
    defaultValue = 2000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 60000),
    )


_FcNetworkDropLatency_Type.__name__ = "CiscoMilliSeconds"
_FcNetworkDropLatency_Object = MibScalar
fcNetworkDropLatency = _FcNetworkDropLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 5),
    _FcNetworkDropLatency_Type()
)
fcNetworkDropLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcNetworkDropLatency.setStatus("current")
if mibBuilder.loadTexts:
    fcNetworkDropLatency.setUnits("msec")


class _FcSwitchDropLatency_Type(CiscoMilliSeconds):
    """Custom type fcSwitchDropLatency based on CiscoMilliSeconds"""
    defaultValue = 500

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_FcSwitchDropLatency_Type.__name__ = "CiscoMilliSeconds"
_FcSwitchDropLatency_Object = MibScalar
fcSwitchDropLatency = _FcSwitchDropLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 6),
    _FcSwitchDropLatency_Type()
)
fcSwitchDropLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcSwitchDropLatency.setStatus("current")
if mibBuilder.loadTexts:
    fcSwitchDropLatency.setUnits("msec")


class _FcInorderDelivery_Type(TruthValue):
    """Custom type fcInorderDelivery based on TruthValue"""


_FcInorderDelivery_Object = MibScalar
fcInorderDelivery = _FcInorderDelivery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 7),
    _FcInorderDelivery_Type()
)
fcInorderDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcInorderDelivery.setStatus("current")
_VsanFcTimerTable_Object = MibTable
vsanFcTimerTable = _VsanFcTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8)
)
if mibBuilder.loadTexts:
    vsanFcTimerTable.setStatus("current")
_VsanFcTimerEntry_Object = MibTableRow
vsanFcTimerEntry = _VsanFcTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    vsanFcTimerEntry.setStatus("current")


class _VsanFcTimerForceFlag_Type(Bits):
    """Custom type vsanFcTimerForceFlag based on Bits"""
    namedValues = NamedValues(
        *(("dstov", 2),
          ("edtov", 1),
          ("ratov", 0))
    )

_VsanFcTimerForceFlag_Type.__name__ = "Bits"
_VsanFcTimerForceFlag_Object = MibTableColumn
vsanFcTimerForceFlag = _VsanFcTimerForceFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 1),
    _VsanFcTimerForceFlag_Type()
)
vsanFcTimerForceFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanFcTimerForceFlag.setStatus("current")


class _VsanFcTimerRatov_Type(CiscoMilliSeconds):
    """Custom type vsanFcTimerRatov based on CiscoMilliSeconds"""
    defaultValue = 10000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 100000),
    )


_VsanFcTimerRatov_Type.__name__ = "CiscoMilliSeconds"
_VsanFcTimerRatov_Object = MibTableColumn
vsanFcTimerRatov = _VsanFcTimerRatov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 2),
    _VsanFcTimerRatov_Type()
)
vsanFcTimerRatov.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanFcTimerRatov.setStatus("current")
if mibBuilder.loadTexts:
    vsanFcTimerRatov.setUnits("msec")


class _VsanFcTimerEdtov_Type(CiscoMilliSeconds):
    """Custom type vsanFcTimerEdtov based on CiscoMilliSeconds"""
    defaultValue = 2000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 100000),
    )


_VsanFcTimerEdtov_Type.__name__ = "CiscoMilliSeconds"
_VsanFcTimerEdtov_Object = MibTableColumn
vsanFcTimerEdtov = _VsanFcTimerEdtov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 3),
    _VsanFcTimerEdtov_Type()
)
vsanFcTimerEdtov.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanFcTimerEdtov.setStatus("current")
if mibBuilder.loadTexts:
    vsanFcTimerEdtov.setUnits("msec")


class _VsanFcTimerDstov_Type(CiscoMilliSeconds):
    """Custom type vsanFcTimerDstov based on CiscoMilliSeconds"""
    defaultValue = 5000

    subtypeSpec = CiscoMilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 100000),
    )


_VsanFcTimerDstov_Type.__name__ = "CiscoMilliSeconds"
_VsanFcTimerDstov_Object = MibTableColumn
vsanFcTimerDstov = _VsanFcTimerDstov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 4),
    _VsanFcTimerDstov_Type()
)
vsanFcTimerDstov.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vsanFcTimerDstov.setStatus("current")
if mibBuilder.loadTexts:
    vsanFcTimerDstov.setUnits("msec")
_VsanFcTimerFstov_Type = CiscoMilliSeconds
_VsanFcTimerFstov_Object = MibTableColumn
vsanFcTimerFstov = _VsanFcTimerFstov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 4, 8, 1, 5),
    _VsanFcTimerFstov_Type()
)
vsanFcTimerFstov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vsanFcTimerFstov.setStatus("current")
if mibBuilder.loadTexts:
    vsanFcTimerFstov.setUnits("msec")
_VsanStats_ObjectIdentity = ObjectIdentity
vsanStats = _VsanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5)
)
_VsanFcFeElementName_Type = FcNameId
_VsanFcFeElementName_Object = MibScalar
vsanFcFeElementName = _VsanFcFeElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 5, 1),
    _VsanFcFeElementName_Type()
)
vsanFcFeElementName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vsanFcFeElementName.setStatus("current")
_VsanMIBConformance_ObjectIdentity = ObjectIdentity
vsanMIBConformance = _VsanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3)
)
_VsanMIBCompliances_ObjectIdentity = ObjectIdentity
vsanMIBCompliances = _VsanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1)
)
_VsanMIBGroups_ObjectIdentity = ObjectIdentity
vsanMIBGroups = _VsanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2)
)
vsanEntry.registerAugmentions(
    ("CISCO-VSAN-MIB",
     "vsanFcTimerEntry")
)
vsanFcTimerEntry.setIndexNames(*vsanEntry.getIndexNames())

# Managed Objects groups

vsanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 1)
)
vsanGroup.setObjects(
      *(("CISCO-VSAN-MIB", "vsanNumber"),
        ("CISCO-VSAN-MIB", "vsanLastChange"),
        ("CISCO-VSAN-MIB", "vsanName"),
        ("CISCO-VSAN-MIB", "vsanMediaType"),
        ("CISCO-VSAN-MIB", "vsanMtu"),
        ("CISCO-VSAN-MIB", "vsanAdminState"),
        ("CISCO-VSAN-MIB", "vsanLoadBalancingType"),
        ("CISCO-VSAN-MIB", "vsanInterOperMode"),
        ("CISCO-VSAN-MIB", "vsanOperState"),
        ("CISCO-VSAN-MIB", "vsanRowStatus"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-VSAN-MIB", "fcInorderDelivery"))
)
if mibBuilder.loadTexts:
    vsanGroup.setStatus("deprecated")

vsanMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 3)
)
vsanMembershipGroup.setObjects(
    ("CISCO-VSAN-MIB", "vsanDenyUnknownWwn")
)
if mibBuilder.loadTexts:
    vsanMembershipGroup.setStatus("current")

vsanStaticMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 4)
)
vsanStaticMembershipGroup.setObjects(
      *(("CISCO-VSAN-MIB", "vsanIfNumber"),
        ("CISCO-VSAN-MIB", "vsanIfVsan"),
        ("CISCO-VSAN-MIB", "vsanIfDenyList"))
)
if mibBuilder.loadTexts:
    vsanStaticMembershipGroup.setStatus("current")

vsanWWNListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 5)
)
vsanWWNListGroup.setObjects(
      *(("CISCO-VSAN-MIB", "vsanWwnListNumber"),
        ("CISCO-VSAN-MIB", "vsanWwnListWwn"),
        ("CISCO-VSAN-MIB", "vsanWwnListRowStatus"))
)
if mibBuilder.loadTexts:
    vsanWWNListGroup.setStatus("current")

vsanDynamicMembershipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 6)
)
vsanDynamicMembershipGroup.setObjects(
      *(("CISCO-VSAN-MIB", "vsanDynamicListNumber"),
        ("CISCO-VSAN-MIB", "vsanDynamicVsan"),
        ("CISCO-VSAN-MIB", "vsanDynamicRowStatus"))
)
if mibBuilder.loadTexts:
    vsanDynamicMembershipGroup.setStatus("current")

vsanFcTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 8)
)
vsanFcTimerGroup.setObjects(
      *(("CISCO-VSAN-MIB", "fcTimerRatov"),
        ("CISCO-VSAN-MIB", "fcTimerEdtov"),
        ("CISCO-VSAN-MIB", "fcTimerFstov"),
        ("CISCO-VSAN-MIB", "fcTimerDstov"))
)
if mibBuilder.loadTexts:
    vsanFcTimerGroup.setStatus("deprecated")

vsanFcLatencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 9)
)
vsanFcLatencyGroup.setObjects(
      *(("CISCO-VSAN-MIB", "fcNetworkDropLatency"),
        ("CISCO-VSAN-MIB", "fcSwitchDropLatency"))
)
if mibBuilder.loadTexts:
    vsanFcLatencyGroup.setStatus("current")

vsanVsanMembershipSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 10)
)
vsanVsanMembershipSummaryGroup.setObjects(
    ("CISCO-VSAN-MIB", "vsanMembershipSummaryInterface")
)
if mibBuilder.loadTexts:
    vsanVsanMembershipSummaryGroup.setStatus("current")

vsanGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 11)
)
vsanGroupRev1.setObjects(
      *(("CISCO-VSAN-MIB", "vsanNumber"),
        ("CISCO-VSAN-MIB", "vsanLastChange"),
        ("CISCO-VSAN-MIB", "vsanName"),
        ("CISCO-VSAN-MIB", "vsanMediaType"),
        ("CISCO-VSAN-MIB", "vsanMtu"),
        ("CISCO-VSAN-MIB", "vsanAdminState"),
        ("CISCO-VSAN-MIB", "vsanLoadBalancingType"),
        ("CISCO-VSAN-MIB", "vsanOperState"),
        ("CISCO-VSAN-MIB", "vsanRowStatus"),
        ("CISCO-VSAN-MIB", "vsanInterOperValue"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-VSAN-MIB", "fcInorderDelivery"))
)
if mibBuilder.loadTexts:
    vsanGroupRev1.setStatus("deprecated")

vsanFcTimerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 12)
)
vsanFcTimerGroupRev1.setObjects(
      *(("CISCO-VSAN-MIB", "fcTimerRatov"),
        ("CISCO-VSAN-MIB", "fcTimerEdtov"),
        ("CISCO-VSAN-MIB", "fcTimerDstov"),
        ("CISCO-VSAN-MIB", "fcTimerFstov"),
        ("CISCO-VSAN-MIB", "vsanFcTimerForceFlag"),
        ("CISCO-VSAN-MIB", "vsanFcTimerRatov"),
        ("CISCO-VSAN-MIB", "vsanFcTimerEdtov"),
        ("CISCO-VSAN-MIB", "vsanFcTimerDstov"),
        ("CISCO-VSAN-MIB", "vsanFcTimerFstov"))
)
if mibBuilder.loadTexts:
    vsanFcTimerGroupRev1.setStatus("current")

vsanGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 13)
)
vsanGroupRev2.setObjects(
      *(("CISCO-VSAN-MIB", "vsanNumber"),
        ("CISCO-VSAN-MIB", "vsanLastChange"),
        ("CISCO-VSAN-MIB", "vsanName"),
        ("CISCO-VSAN-MIB", "vsanMediaType"),
        ("CISCO-VSAN-MIB", "vsanMtu"),
        ("CISCO-VSAN-MIB", "vsanAdminState"),
        ("CISCO-VSAN-MIB", "vsanLoadBalancingType"),
        ("CISCO-VSAN-MIB", "vsanOperState"),
        ("CISCO-VSAN-MIB", "vsanRowStatus"),
        ("CISCO-VSAN-MIB", "vsanInterOperValue"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-VSAN-MIB", "fcInorderDelivery"),
        ("CISCO-VSAN-MIB", "vsanInorderDelivery"),
        ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"))
)
if mibBuilder.loadTexts:
    vsanGroupRev2.setStatus("deprecated")

vsanMembershipSummaryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 14)
)
vsanMembershipSummaryGroupRev1.setObjects(
    ("CISCO-VSAN-MIB", "vsanMembershipSummaryIntfType")
)
if mibBuilder.loadTexts:
    vsanMembershipSummaryGroupRev1.setStatus("current")

vsanGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 16)
)
vsanGroupRev3.setObjects(
      *(("CISCO-VSAN-MIB", "vsanNumber"),
        ("CISCO-VSAN-MIB", "vsanLastChange"),
        ("CISCO-VSAN-MIB", "vsanName"),
        ("CISCO-VSAN-MIB", "vsanMediaType"),
        ("CISCO-VSAN-MIB", "vsanMtu"),
        ("CISCO-VSAN-MIB", "vsanAdminState"),
        ("CISCO-VSAN-MIB", "vsanLoadBalancingType"),
        ("CISCO-VSAN-MIB", "vsanOperState"),
        ("CISCO-VSAN-MIB", "vsanRowStatus"),
        ("CISCO-VSAN-MIB", "vsanInterOperValue"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-VSAN-MIB", "fcInorderDelivery"),
        ("CISCO-VSAN-MIB", "vsanInorderDelivery"),
        ("CISCO-VSAN-MIB", "vsanNetworkDropLatency"),
        ("CISCO-VSAN-MIB", "vsanFcFeElementName"))
)
if mibBuilder.loadTexts:
    vsanGroupRev3.setStatus("current")


# Notification objects

vsanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 1)
)
vsanStatusChange.setObjects(
      *(("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-VSAN-MIB", "vsanAdminState"),
        ("CISCO-VSAN-MIB", "vsanOperState"))
)
if mibBuilder.loadTexts:
    vsanStatusChange.setStatus(
        "current"
    )

vsanPortMembershipChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 1, 3, 0, 2)
)
vsanPortMembershipChange.setObjects(
      *(("CISCO-VSAN-MIB", "vsanFcFeElementName"),
        ("IF-MIB", "ifIndex"),
        ("CISCO-VSAN-MIB", "notifyVsanIndex"))
)
if mibBuilder.loadTexts:
    vsanPortMembershipChange.setStatus(
        "current"
    )


# Notifications groups

vsanNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 7)
)
vsanNotificationGroup.setObjects(
    ("CISCO-VSAN-MIB", "vsanStatusChange")
)
if mibBuilder.loadTexts:
    vsanNotificationGroup.setStatus(
        "deprecated"
    )

vsanNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 2, 15)
)
vsanNotificationGroupRev1.setObjects(
      *(("CISCO-VSAN-MIB", "vsanStatusChange"),
        ("CISCO-VSAN-MIB", "vsanPortMembershipChange"))
)
if mibBuilder.loadTexts:
    vsanNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vsanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance.setStatus(
        "deprecated"
    )

vsanMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance1.setStatus(
        "deprecated"
    )

vsanMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance2.setStatus(
        "deprecated"
    )

vsanMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 4)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance3.setStatus(
        "deprecated"
    )

vsanMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 5)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance4.setStatus(
        "deprecated"
    )

vsanMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 6)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance5.setStatus(
        "deprecated"
    )

vsanMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 7)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance6.setStatus(
        "deprecated"
    )

vsanMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 282, 3, 1, 8)
)
if mibBuilder.loadTexts:
    vsanMIBCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VSAN-MIB",
    **{"VsanMediaType": VsanMediaType,
       "VsanAdminState": VsanAdminState,
       "VsanOperationalState": VsanOperationalState,
       "VsanLoadBalancingType": VsanLoadBalancingType,
       "ciscoVsanMIB": ciscoVsanMIB,
       "ciscoVsanMIBObjects": ciscoVsanMIBObjects,
       "vsanConfiguration": vsanConfiguration,
       "vsanNumber": vsanNumber,
       "vsanLastChange": vsanLastChange,
       "vsanTable": vsanTable,
       "vsanEntry": vsanEntry,
       "vsanIndex": vsanIndex,
       "vsanName": vsanName,
       "vsanMediaType": vsanMediaType,
       "vsanAdminState": vsanAdminState,
       "vsanMtu": vsanMtu,
       "vsanLoadBalancingType": vsanLoadBalancingType,
       "vsanInterOperMode": vsanInterOperMode,
       "vsanOperState": vsanOperState,
       "vsanRowStatus": vsanRowStatus,
       "vsanInterOperValue": vsanInterOperValue,
       "vsanInorderDelivery": vsanInorderDelivery,
       "vsanNetworkDropLatency": vsanNetworkDropLatency,
       "notifyVsanIndex": notifyVsanIndex,
       "vsanMembership": vsanMembership,
       "vsanDenyUnknownWwn": vsanDenyUnknownWwn,
       "vsanWwnListNumber": vsanWwnListNumber,
       "vsanWwnListTable": vsanWwnListTable,
       "vsanWwnListEntry": vsanWwnListEntry,
       "vsanWwnListIndex": vsanWwnListIndex,
       "vsanWwnListWwnIndex": vsanWwnListWwnIndex,
       "vsanWwnListWwn": vsanWwnListWwn,
       "vsanWwnListRowStatus": vsanWwnListRowStatus,
       "vsanIfNumber": vsanIfNumber,
       "vsanIfTable": vsanIfTable,
       "vsanIfEntry": vsanIfEntry,
       "vsanIfVsan": vsanIfVsan,
       "vsanIfDenyList": vsanIfDenyList,
       "vsanDynamicListNumber": vsanDynamicListNumber,
       "vsanDynamicTable": vsanDynamicTable,
       "vsanDynamicEntry": vsanDynamicEntry,
       "vsanDynamicVsan": vsanDynamicVsan,
       "vsanDynamicRowStatus": vsanDynamicRowStatus,
       "vsanMembershipSummaryTable": vsanMembershipSummaryTable,
       "vsanMembershipSummaryEntry": vsanMembershipSummaryEntry,
       "vsanMembershipSummaryInterface": vsanMembershipSummaryInterface,
       "vsanMembershipSummaryIntfType": vsanMembershipSummaryIntfType,
       "vsanNotification": vsanNotification,
       "vsanNotifications": vsanNotifications,
       "vsanStatusChange": vsanStatusChange,
       "vsanPortMembershipChange": vsanPortMembershipChange,
       "vsanFcConfiguration": vsanFcConfiguration,
       "fcTimerRatov": fcTimerRatov,
       "fcTimerEdtov": fcTimerEdtov,
       "fcTimerFstov": fcTimerFstov,
       "fcTimerDstov": fcTimerDstov,
       "fcNetworkDropLatency": fcNetworkDropLatency,
       "fcSwitchDropLatency": fcSwitchDropLatency,
       "fcInorderDelivery": fcInorderDelivery,
       "vsanFcTimerTable": vsanFcTimerTable,
       "vsanFcTimerEntry": vsanFcTimerEntry,
       "vsanFcTimerForceFlag": vsanFcTimerForceFlag,
       "vsanFcTimerRatov": vsanFcTimerRatov,
       "vsanFcTimerEdtov": vsanFcTimerEdtov,
       "vsanFcTimerDstov": vsanFcTimerDstov,
       "vsanFcTimerFstov": vsanFcTimerFstov,
       "vsanStats": vsanStats,
       "vsanFcFeElementName": vsanFcFeElementName,
       "vsanMIBConformance": vsanMIBConformance,
       "vsanMIBCompliances": vsanMIBCompliances,
       "vsanMIBCompliance": vsanMIBCompliance,
       "vsanMIBCompliance1": vsanMIBCompliance1,
       "vsanMIBCompliance2": vsanMIBCompliance2,
       "vsanMIBCompliance3": vsanMIBCompliance3,
       "vsanMIBCompliance4": vsanMIBCompliance4,
       "vsanMIBCompliance5": vsanMIBCompliance5,
       "vsanMIBCompliance6": vsanMIBCompliance6,
       "vsanMIBCompliance7": vsanMIBCompliance7,
       "vsanMIBGroups": vsanMIBGroups,
       "vsanGroup": vsanGroup,
       "vsanMembershipGroup": vsanMembershipGroup,
       "vsanStaticMembershipGroup": vsanStaticMembershipGroup,
       "vsanWWNListGroup": vsanWWNListGroup,
       "vsanDynamicMembershipGroup": vsanDynamicMembershipGroup,
       "vsanNotificationGroup": vsanNotificationGroup,
       "vsanFcTimerGroup": vsanFcTimerGroup,
       "vsanFcLatencyGroup": vsanFcLatencyGroup,
       "vsanVsanMembershipSummaryGroup": vsanVsanMembershipSummaryGroup,
       "vsanGroupRev1": vsanGroupRev1,
       "vsanFcTimerGroupRev1": vsanFcTimerGroupRev1,
       "vsanGroupRev2": vsanGroupRev2,
       "vsanMembershipSummaryGroupRev1": vsanMembershipSummaryGroupRev1,
       "vsanNotificationGroupRev1": vsanNotificationGroupRev1,
       "vsanGroupRev3": vsanGroupRev3}
)
