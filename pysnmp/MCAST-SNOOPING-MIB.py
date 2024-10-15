# SNMP MIB module (MCAST-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MCAST-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:40 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swMcastSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwMcastSnoopingCtrl_ObjectIdentity = ObjectIdentity
swMcastSnoopingCtrl = _SwMcastSnoopingCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 1)
)


class _SwIGMPSnoopingGlobalState_Type(Integer32):
    """Custom type swIGMPSnoopingGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwIGMPSnoopingGlobalState_Type.__name__ = "Integer32"
_SwIGMPSnoopingGlobalState_Object = MibScalar
swIGMPSnoopingGlobalState = _SwIGMPSnoopingGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 1, 1),
    _SwIGMPSnoopingGlobalState_Type()
)
swIGMPSnoopingGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnoopingGlobalState.setStatus("current")


class _SwIGMPSnoopingMaxDataDrivenLearningCount_Type(Integer32):
    """Custom type swIGMPSnoopingMaxDataDrivenLearningCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwIGMPSnoopingMaxDataDrivenLearningCount_Type.__name__ = "Integer32"
_SwIGMPSnoopingMaxDataDrivenLearningCount_Object = MibScalar
swIGMPSnoopingMaxDataDrivenLearningCount = _SwIGMPSnoopingMaxDataDrivenLearningCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 1, 3),
    _SwIGMPSnoopingMaxDataDrivenLearningCount_Type()
)
swIGMPSnoopingMaxDataDrivenLearningCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnoopingMaxDataDrivenLearningCount.setStatus("current")
_SwMcastSnoopingInfo_ObjectIdentity = ObjectIdentity
swMcastSnoopingInfo = _SwMcastSnoopingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2)
)
_SwIGMPSnoopingInfo_ObjectIdentity = ObjectIdentity
swIGMPSnoopingInfo = _SwIGMPSnoopingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1)
)
_SwIGMPSnoopingForwardingTable_Object = MibTable
swIGMPSnoopingForwardingTable = _SwIGMPSnoopingForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingForwardingTable.setStatus("current")
_SwIGMPSnoopingForwardingEntry_Object = MibTableRow
swIGMPSnoopingForwardingEntry = _SwIGMPSnoopingForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1)
)
swIGMPSnoopingForwardingEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"),
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnpFwdSrcAddr"),
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnpFwdGrpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingForwardingEntry.setStatus("current")


class _SwIGMPSnoopingVlanID_Type(Integer32):
    """Custom type swIGMPSnoopingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwIGMPSnoopingVlanID_Type.__name__ = "Integer32"
_SwIGMPSnoopingVlanID_Object = MibTableColumn
swIGMPSnoopingVlanID = _SwIGMPSnoopingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 1),
    _SwIGMPSnoopingVlanID_Type()
)
swIGMPSnoopingVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingVlanID.setStatus("current")
_SwIGMPSnpFwdSrcAddr_Type = IpAddress
_SwIGMPSnpFwdSrcAddr_Object = MibTableColumn
swIGMPSnpFwdSrcAddr = _SwIGMPSnpFwdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 2),
    _SwIGMPSnpFwdSrcAddr_Type()
)
swIGMPSnpFwdSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpFwdSrcAddr.setStatus("current")
_SwIGMPSnpFwdGrpAddr_Type = IpAddress
_SwIGMPSnpFwdGrpAddr_Object = MibTableColumn
swIGMPSnpFwdGrpAddr = _SwIGMPSnpFwdGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 3),
    _SwIGMPSnpFwdGrpAddr_Type()
)
swIGMPSnpFwdGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpFwdGrpAddr.setStatus("current")
_SwIGMPSnpFwdMemberPorts_Type = PortList
_SwIGMPSnpFwdMemberPorts_Object = MibTableColumn
swIGMPSnpFwdMemberPorts = _SwIGMPSnpFwdMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 4),
    _SwIGMPSnpFwdMemberPorts_Type()
)
swIGMPSnpFwdMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpFwdMemberPorts.setStatus("current")
_SwIGMPSnoopingGroupTable_Object = MibTable
swIGMPSnoopingGroupTable = _SwIGMPSnoopingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupTable.setStatus("current")
_SwIGMPSnoopingGroupEntry_Object = MibTableRow
swIGMPSnoopingGroupEntry = _SwIGMPSnoopingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1)
)
swIGMPSnoopingGroupEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"),
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnpGrpSrcAddr"),
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnpGrpGrpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingGroupEntry.setStatus("current")
_SwIGMPSnpGrpSrcAddr_Type = IpAddress
_SwIGMPSnpGrpSrcAddr_Object = MibTableColumn
swIGMPSnpGrpSrcAddr = _SwIGMPSnpGrpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 1),
    _SwIGMPSnpGrpSrcAddr_Type()
)
swIGMPSnpGrpSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpSrcAddr.setStatus("current")
_SwIGMPSnpGrpGrpAddr_Type = IpAddress
_SwIGMPSnpGrpGrpAddr_Object = MibTableColumn
swIGMPSnpGrpGrpAddr = _SwIGMPSnpGrpGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 2),
    _SwIGMPSnpGrpGrpAddr_Type()
)
swIGMPSnpGrpGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpGrpAddr.setStatus("current")
_SwIGMPSnpGrpIncludeMemberPorts_Type = PortList
_SwIGMPSnpGrpIncludeMemberPorts_Object = MibTableColumn
swIGMPSnpGrpIncludeMemberPorts = _SwIGMPSnpGrpIncludeMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 3),
    _SwIGMPSnpGrpIncludeMemberPorts_Type()
)
swIGMPSnpGrpIncludeMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpIncludeMemberPorts.setStatus("current")
_SwIGMPSnpGrpExcludeMemberPorts_Type = PortList
_SwIGMPSnpGrpExcludeMemberPorts_Object = MibTableColumn
swIGMPSnpGrpExcludeMemberPorts = _SwIGMPSnpGrpExcludeMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 4),
    _SwIGMPSnpGrpExcludeMemberPorts_Type()
)
swIGMPSnpGrpExcludeMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpExcludeMemberPorts.setStatus("current")
_SwIGMPSnpGrpRouterPorts_Type = PortList
_SwIGMPSnpGrpRouterPorts_Object = MibTableColumn
swIGMPSnpGrpRouterPorts = _SwIGMPSnpGrpRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 5),
    _SwIGMPSnpGrpRouterPorts_Type()
)
swIGMPSnpGrpRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpRouterPorts.setStatus("current")
_SwIGMPSnpGrpUpTime_Type = Integer32
_SwIGMPSnpGrpUpTime_Object = MibTableColumn
swIGMPSnpGrpUpTime = _SwIGMPSnpGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 6),
    _SwIGMPSnpGrpUpTime_Type()
)
swIGMPSnpGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpUpTime.setStatus("current")
_SwIGMPSnpGrpExpiryTime_Type = Integer32
_SwIGMPSnpGrpExpiryTime_Object = MibTableColumn
swIGMPSnpGrpExpiryTime = _SwIGMPSnpGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 7),
    _SwIGMPSnpGrpExpiryTime_Type()
)
swIGMPSnpGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpExpiryTime.setStatus("current")
_SwIGMPSnpGrpReportCount_Type = Integer32
_SwIGMPSnpGrpReportCount_Object = MibTableColumn
swIGMPSnpGrpReportCount = _SwIGMPSnpGrpReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 8),
    _SwIGMPSnpGrpReportCount_Type()
)
swIGMPSnpGrpReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpGrpReportCount.setStatus("current")
_SwMLDSnoopingInfo_ObjectIdentity = ObjectIdentity
swMLDSnoopingInfo = _SwMLDSnoopingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2)
)
_SwMLDSnoopingForwardingTable_Object = MibTable
swMLDSnoopingForwardingTable = _SwMLDSnoopingForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swMLDSnoopingForwardingTable.setStatus("current")
_SwMLDSnoopingForwardingEntry_Object = MibTableRow
swMLDSnoopingForwardingEntry = _SwMLDSnoopingForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1)
)
swMLDSnoopingForwardingEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swMLDSnoopingVlanID"),
    (0, "MCAST-SNOOPING-MIB", "swMLDSnpFwdSrcAddr"),
    (0, "MCAST-SNOOPING-MIB", "swMLDSnpFwdGrpAddr"),
)
if mibBuilder.loadTexts:
    swMLDSnoopingForwardingEntry.setStatus("current")


class _SwMLDSnoopingVlanID_Type(Integer32):
    """Custom type swMLDSnoopingVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwMLDSnoopingVlanID_Type.__name__ = "Integer32"
_SwMLDSnoopingVlanID_Object = MibTableColumn
swMLDSnoopingVlanID = _SwMLDSnoopingVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 1),
    _SwMLDSnoopingVlanID_Type()
)
swMLDSnoopingVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDSnoopingVlanID.setStatus("current")
_SwMLDSnpFwdSrcAddr_Type = Ipv6Address
_SwMLDSnpFwdSrcAddr_Object = MibTableColumn
swMLDSnpFwdSrcAddr = _SwMLDSnpFwdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 2),
    _SwMLDSnpFwdSrcAddr_Type()
)
swMLDSnpFwdSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDSnpFwdSrcAddr.setStatus("current")
_SwMLDSnpFwdGrpAddr_Type = Ipv6Address
_SwMLDSnpFwdGrpAddr_Object = MibTableColumn
swMLDSnpFwdGrpAddr = _SwMLDSnpFwdGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 3),
    _SwMLDSnpFwdGrpAddr_Type()
)
swMLDSnpFwdGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDSnpFwdGrpAddr.setStatus("current")
_SwMLDSnpFwdMemberPorts_Type = PortList
_SwMLDSnpFwdMemberPorts_Object = MibTableColumn
swMLDSnpFwdMemberPorts = _SwMLDSnpFwdMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 4),
    _SwMLDSnpFwdMemberPorts_Type()
)
swMLDSnpFwdMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDSnpFwdMemberPorts.setStatus("current")
_SwMLDSnoopingVlanStatisticCounterTable_Object = MibTable
swMLDSnoopingVlanStatisticCounterTable = _SwMLDSnoopingVlanStatisticCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swMLDSnoopingVlanStatisticCounterTable.setStatus("current")
_SwMLDSnoopingVlanStatisticCounterEntry_Object = MibTableRow
swMLDSnoopingVlanStatisticCounterEntry = _SwMLDSnoopingVlanStatisticCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3, 1)
)
swMLDSnoopingVlanStatisticCounterEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swMLDSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    swMLDSnoopingVlanStatisticCounterEntry.setStatus("current")
_SwMLDSnpVlanCounterTotalRxQuery_Type = Counter32
_SwMLDSnpVlanCounterTotalRxQuery_Object = MibTableColumn
swMLDSnpVlanCounterTotalRxQuery = _SwMLDSnpVlanCounterTotalRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3, 1, 20),
    _SwMLDSnpVlanCounterTotalRxQuery_Type()
)
swMLDSnpVlanCounterTotalRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMLDSnpVlanCounterTotalRxQuery.setStatus("current")
_SwMcastSnoopingMgmt_ObjectIdentity = ObjectIdentity
swMcastSnoopingMgmt = _SwMcastSnoopingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3)
)
_SwIGMPSnoopingMgmt_ObjectIdentity = ObjectIdentity
swIGMPSnoopingMgmt = _SwIGMPSnoopingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1)
)
_SwIGMPSnoopingCtrlTable_Object = MibTable
swIGMPSnoopingCtrlTable = _SwIGMPSnoopingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingCtrlTable.setStatus("current")
_SwIGMPSnoopingCtrlEntry_Object = MibTableRow
swIGMPSnoopingCtrlEntry = _SwIGMPSnoopingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1)
)
swIGMPSnoopingCtrlEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingCtrlEntry.setStatus("current")


class _SwIGMPSnpCtrlQueryInterval_Type(Integer32):
    """Custom type swIGMPSnpCtrlQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwIGMPSnpCtrlQueryInterval_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlQueryInterval_Object = MibTableColumn
swIGMPSnpCtrlQueryInterval = _SwIGMPSnpCtrlQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 5),
    _SwIGMPSnpCtrlQueryInterval_Type()
)
swIGMPSnpCtrlQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlQueryInterval.setStatus("current")


class _SwIGMPSnpCtrlMaxResponseTime_Type(Integer32):
    """Custom type swIGMPSnpCtrlMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwIGMPSnpCtrlMaxResponseTime_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlMaxResponseTime_Object = MibTableColumn
swIGMPSnpCtrlMaxResponseTime = _SwIGMPSnpCtrlMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 10),
    _SwIGMPSnpCtrlMaxResponseTime_Type()
)
swIGMPSnpCtrlMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlMaxResponseTime.setStatus("current")


class _SwIGMPSnpCtrlRobustnessValue_Type(Integer32):
    """Custom type swIGMPSnpCtrlRobustnessValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwIGMPSnpCtrlRobustnessValue_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlRobustnessValue_Object = MibTableColumn
swIGMPSnpCtrlRobustnessValue = _SwIGMPSnpCtrlRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 15),
    _SwIGMPSnpCtrlRobustnessValue_Type()
)
swIGMPSnpCtrlRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlRobustnessValue.setStatus("current")


class _SwIGMPSnpCtrlLastMemberQueryInterval_Type(Integer32):
    """Custom type swIGMPSnpCtrlLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwIGMPSnpCtrlLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlLastMemberQueryInterval_Object = MibTableColumn
swIGMPSnpCtrlLastMemberQueryInterval = _SwIGMPSnpCtrlLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 20),
    _SwIGMPSnpCtrlLastMemberQueryInterval_Type()
)
swIGMPSnpCtrlLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlLastMemberQueryInterval.setStatus("current")


class _SwIGMPSnpCtrlQuerierState_Type(Integer32):
    """Custom type swIGMPSnpCtrlQuerierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwIGMPSnpCtrlQuerierState_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlQuerierState_Object = MibTableColumn
swIGMPSnpCtrlQuerierState = _SwIGMPSnpCtrlQuerierState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 25),
    _SwIGMPSnpCtrlQuerierState_Type()
)
swIGMPSnpCtrlQuerierState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlQuerierState.setStatus("current")


class _SwIGMPSnpCtrlQuerierRole_Type(Integer32):
    """Custom type swIGMPSnpCtrlQuerierRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-querier", 2),
          ("querier", 1))
    )


_SwIGMPSnpCtrlQuerierRole_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlQuerierRole_Object = MibTableColumn
swIGMPSnpCtrlQuerierRole = _SwIGMPSnpCtrlQuerierRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 30),
    _SwIGMPSnpCtrlQuerierRole_Type()
)
swIGMPSnpCtrlQuerierRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlQuerierRole.setStatus("current")
_SwIGMPSnpCtrlQuerierIP_Type = IpAddress
_SwIGMPSnpCtrlQuerierIP_Object = MibTableColumn
swIGMPSnpCtrlQuerierIP = _SwIGMPSnpCtrlQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 35),
    _SwIGMPSnpCtrlQuerierIP_Type()
)
swIGMPSnpCtrlQuerierIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlQuerierIP.setStatus("current")


class _SwIGMPSnpCtrlQuerierExpiryTime_Type(Integer32):
    """Custom type swIGMPSnpCtrlQuerierExpiryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwIGMPSnpCtrlQuerierExpiryTime_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlQuerierExpiryTime_Object = MibTableColumn
swIGMPSnpCtrlQuerierExpiryTime = _SwIGMPSnpCtrlQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 40),
    _SwIGMPSnpCtrlQuerierExpiryTime_Type()
)
swIGMPSnpCtrlQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlQuerierExpiryTime.setStatus("current")


class _SwIGMPSnpCtrlState_Type(Integer32):
    """Custom type swIGMPSnpCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwIGMPSnpCtrlState_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlState_Object = MibTableColumn
swIGMPSnpCtrlState = _SwIGMPSnpCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 45),
    _SwIGMPSnpCtrlState_Type()
)
swIGMPSnpCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlState.setStatus("current")


class _SwIGMPSnpCtrlFastLeaveState_Type(Integer32):
    """Custom type swIGMPSnpCtrlFastLeaveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwIGMPSnpCtrlFastLeaveState_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlFastLeaveState_Object = MibTableColumn
swIGMPSnpCtrlFastLeaveState = _SwIGMPSnpCtrlFastLeaveState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 50),
    _SwIGMPSnpCtrlFastLeaveState_Type()
)
swIGMPSnpCtrlFastLeaveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlFastLeaveState.setStatus("current")


class _SwIGMPSnpCtrlVersion_Type(Integer32):
    """Custom type swIGMPSnpCtrlVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version-1", 1),
          ("version-2", 2),
          ("version-3", 3))
    )


_SwIGMPSnpCtrlVersion_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlVersion_Object = MibTableColumn
swIGMPSnpCtrlVersion = _SwIGMPSnpCtrlVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 60),
    _SwIGMPSnpCtrlVersion_Type()
)
swIGMPSnpCtrlVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlVersion.setStatus("current")


class _SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type(Integer32):
    """Custom type swIGMPSnpCtrlDataDrivenLearningAgedOutState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type.__name__ = "Integer32"
_SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Object = MibTableColumn
swIGMPSnpCtrlDataDrivenLearningAgedOutState = _SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 70),
    _SwIGMPSnpCtrlDataDrivenLearningAgedOutState_Type()
)
swIGMPSnpCtrlDataDrivenLearningAgedOutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpCtrlDataDrivenLearningAgedOutState.setStatus("current")
_SwIGMPSnoopingDataDrivenLearningGroupTable_Object = MibTable
swIGMPSnoopingDataDrivenLearningGroupTable = _SwIGMPSnoopingDataDrivenLearningGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingDataDrivenLearningGroupTable.setStatus("current")
_SwIGMPSnoopingDataDrivenLearningGroupEntry_Object = MibTableRow
swIGMPSnoopingDataDrivenLearningGroupEntry = _SwIGMPSnoopingDataDrivenLearningGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1)
)
swIGMPSnoopingDataDrivenLearningGroupEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"),
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnpDataDrivenLearningGrpGrpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingDataDrivenLearningGroupEntry.setStatus("current")
_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Type = IpAddress
_SwIGMPSnpDataDrivenLearningGrpGrpAddr_Object = MibTableColumn
swIGMPSnpDataDrivenLearningGrpGrpAddr = _SwIGMPSnpDataDrivenLearningGrpGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 1),
    _SwIGMPSnpDataDrivenLearningGrpGrpAddr_Type()
)
swIGMPSnpDataDrivenLearningGrpGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpDataDrivenLearningGrpGrpAddr.setStatus("current")
_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Type = PortList
_SwIGMPSnpDataDrivenLearningGrpRouterPorts_Object = MibTableColumn
swIGMPSnpDataDrivenLearningGrpRouterPorts = _SwIGMPSnpDataDrivenLearningGrpRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 2),
    _SwIGMPSnpDataDrivenLearningGrpRouterPorts_Type()
)
swIGMPSnpDataDrivenLearningGrpRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpDataDrivenLearningGrpRouterPorts.setStatus("current")
_SwIGMPSnpDataDrivenLearningGrpUpTime_Type = Integer32
_SwIGMPSnpDataDrivenLearningGrpUpTime_Object = MibTableColumn
swIGMPSnpDataDrivenLearningGrpUpTime = _SwIGMPSnpDataDrivenLearningGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 3),
    _SwIGMPSnpDataDrivenLearningGrpUpTime_Type()
)
swIGMPSnpDataDrivenLearningGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpDataDrivenLearningGrpUpTime.setStatus("current")
_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Type = Integer32
_SwIGMPSnpDataDrivenLearningGrpExpiryTime_Object = MibTableColumn
swIGMPSnpDataDrivenLearningGrpExpiryTime = _SwIGMPSnpDataDrivenLearningGrpExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 4),
    _SwIGMPSnpDataDrivenLearningGrpExpiryTime_Type()
)
swIGMPSnpDataDrivenLearningGrpExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpDataDrivenLearningGrpExpiryTime.setStatus("current")


class _SwIGMPSnpDataDrivenLearningGrpClearGrp_Type(Integer32):
    """Custom type swIGMPSnpDataDrivenLearningGrpClearGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("other", 1))
    )


_SwIGMPSnpDataDrivenLearningGrpClearGrp_Type.__name__ = "Integer32"
_SwIGMPSnpDataDrivenLearningGrpClearGrp_Object = MibTableColumn
swIGMPSnpDataDrivenLearningGrpClearGrp = _SwIGMPSnpDataDrivenLearningGrpClearGrp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 100),
    _SwIGMPSnpDataDrivenLearningGrpClearGrp_Type()
)
swIGMPSnpDataDrivenLearningGrpClearGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpDataDrivenLearningGrpClearGrp.setStatus("current")
_SwIGMPSnoopingRouterPortTable_Object = MibTable
swIGMPSnoopingRouterPortTable = _SwIGMPSnoopingRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingRouterPortTable.setStatus("current")
_SwIGMPSnoopingRouterPortEntry_Object = MibTableRow
swIGMPSnoopingRouterPortEntry = _SwIGMPSnoopingRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1)
)
swIGMPSnoopingRouterPortEntry.setIndexNames(
    (0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingRouterPortEntry.setStatus("current")
_SwIGMPSnpStaticRouterPorts_Type = PortList
_SwIGMPSnpStaticRouterPorts_Object = MibTableColumn
swIGMPSnpStaticRouterPorts = _SwIGMPSnpStaticRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 5),
    _SwIGMPSnpStaticRouterPorts_Type()
)
swIGMPSnpStaticRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpStaticRouterPorts.setStatus("current")
_SwIGMPSnpDynamicRouterPorts_Type = PortList
_SwIGMPSnpDynamicRouterPorts_Object = MibTableColumn
swIGMPSnpDynamicRouterPorts = _SwIGMPSnpDynamicRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 10),
    _SwIGMPSnpDynamicRouterPorts_Type()
)
swIGMPSnpDynamicRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnpDynamicRouterPorts.setStatus("current")
_SwIGMPSnpForbiddenRouterPorts_Type = PortList
_SwIGMPSnpForbiddenRouterPorts_Object = MibTableColumn
swIGMPSnpForbiddenRouterPorts = _SwIGMPSnpForbiddenRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 15),
    _SwIGMPSnpForbiddenRouterPorts_Type()
)
swIGMPSnpForbiddenRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPSnpForbiddenRouterPorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAST-SNOOPING-MIB",
    **{"Ipv6Address": Ipv6Address,
       "PortList": PortList,
       "swMcastSnoopingMIB": swMcastSnoopingMIB,
       "swMcastSnoopingCtrl": swMcastSnoopingCtrl,
       "swIGMPSnoopingGlobalState": swIGMPSnoopingGlobalState,
       "swIGMPSnoopingMaxDataDrivenLearningCount": swIGMPSnoopingMaxDataDrivenLearningCount,
       "swMcastSnoopingInfo": swMcastSnoopingInfo,
       "swIGMPSnoopingInfo": swIGMPSnoopingInfo,
       "swIGMPSnoopingForwardingTable": swIGMPSnoopingForwardingTable,
       "swIGMPSnoopingForwardingEntry": swIGMPSnoopingForwardingEntry,
       "swIGMPSnoopingVlanID": swIGMPSnoopingVlanID,
       "swIGMPSnpFwdSrcAddr": swIGMPSnpFwdSrcAddr,
       "swIGMPSnpFwdGrpAddr": swIGMPSnpFwdGrpAddr,
       "swIGMPSnpFwdMemberPorts": swIGMPSnpFwdMemberPorts,
       "swIGMPSnoopingGroupTable": swIGMPSnoopingGroupTable,
       "swIGMPSnoopingGroupEntry": swIGMPSnoopingGroupEntry,
       "swIGMPSnpGrpSrcAddr": swIGMPSnpGrpSrcAddr,
       "swIGMPSnpGrpGrpAddr": swIGMPSnpGrpGrpAddr,
       "swIGMPSnpGrpIncludeMemberPorts": swIGMPSnpGrpIncludeMemberPorts,
       "swIGMPSnpGrpExcludeMemberPorts": swIGMPSnpGrpExcludeMemberPorts,
       "swIGMPSnpGrpRouterPorts": swIGMPSnpGrpRouterPorts,
       "swIGMPSnpGrpUpTime": swIGMPSnpGrpUpTime,
       "swIGMPSnpGrpExpiryTime": swIGMPSnpGrpExpiryTime,
       "swIGMPSnpGrpReportCount": swIGMPSnpGrpReportCount,
       "swMLDSnoopingInfo": swMLDSnoopingInfo,
       "swMLDSnoopingForwardingTable": swMLDSnoopingForwardingTable,
       "swMLDSnoopingForwardingEntry": swMLDSnoopingForwardingEntry,
       "swMLDSnoopingVlanID": swMLDSnoopingVlanID,
       "swMLDSnpFwdSrcAddr": swMLDSnpFwdSrcAddr,
       "swMLDSnpFwdGrpAddr": swMLDSnpFwdGrpAddr,
       "swMLDSnpFwdMemberPorts": swMLDSnpFwdMemberPorts,
       "swMLDSnoopingVlanStatisticCounterTable": swMLDSnoopingVlanStatisticCounterTable,
       "swMLDSnoopingVlanStatisticCounterEntry": swMLDSnoopingVlanStatisticCounterEntry,
       "swMLDSnpVlanCounterTotalRxQuery": swMLDSnpVlanCounterTotalRxQuery,
       "swMcastSnoopingMgmt": swMcastSnoopingMgmt,
       "swIGMPSnoopingMgmt": swIGMPSnoopingMgmt,
       "swIGMPSnoopingCtrlTable": swIGMPSnoopingCtrlTable,
       "swIGMPSnoopingCtrlEntry": swIGMPSnoopingCtrlEntry,
       "swIGMPSnpCtrlQueryInterval": swIGMPSnpCtrlQueryInterval,
       "swIGMPSnpCtrlMaxResponseTime": swIGMPSnpCtrlMaxResponseTime,
       "swIGMPSnpCtrlRobustnessValue": swIGMPSnpCtrlRobustnessValue,
       "swIGMPSnpCtrlLastMemberQueryInterval": swIGMPSnpCtrlLastMemberQueryInterval,
       "swIGMPSnpCtrlQuerierState": swIGMPSnpCtrlQuerierState,
       "swIGMPSnpCtrlQuerierRole": swIGMPSnpCtrlQuerierRole,
       "swIGMPSnpCtrlQuerierIP": swIGMPSnpCtrlQuerierIP,
       "swIGMPSnpCtrlQuerierExpiryTime": swIGMPSnpCtrlQuerierExpiryTime,
       "swIGMPSnpCtrlState": swIGMPSnpCtrlState,
       "swIGMPSnpCtrlFastLeaveState": swIGMPSnpCtrlFastLeaveState,
       "swIGMPSnpCtrlVersion": swIGMPSnpCtrlVersion,
       "swIGMPSnpCtrlDataDrivenLearningAgedOutState": swIGMPSnpCtrlDataDrivenLearningAgedOutState,
       "swIGMPSnoopingDataDrivenLearningGroupTable": swIGMPSnoopingDataDrivenLearningGroupTable,
       "swIGMPSnoopingDataDrivenLearningGroupEntry": swIGMPSnoopingDataDrivenLearningGroupEntry,
       "swIGMPSnpDataDrivenLearningGrpGrpAddr": swIGMPSnpDataDrivenLearningGrpGrpAddr,
       "swIGMPSnpDataDrivenLearningGrpRouterPorts": swIGMPSnpDataDrivenLearningGrpRouterPorts,
       "swIGMPSnpDataDrivenLearningGrpUpTime": swIGMPSnpDataDrivenLearningGrpUpTime,
       "swIGMPSnpDataDrivenLearningGrpExpiryTime": swIGMPSnpDataDrivenLearningGrpExpiryTime,
       "swIGMPSnpDataDrivenLearningGrpClearGrp": swIGMPSnpDataDrivenLearningGrpClearGrp,
       "swIGMPSnoopingRouterPortTable": swIGMPSnoopingRouterPortTable,
       "swIGMPSnoopingRouterPortEntry": swIGMPSnoopingRouterPortEntry,
       "swIGMPSnpStaticRouterPorts": swIGMPSnpStaticRouterPorts,
       "swIGMPSnpDynamicRouterPorts": swIGMPSnpDynamicRouterPorts,
       "swIGMPSnpForbiddenRouterPorts": swIGMPSnpForbiddenRouterPorts}
)
