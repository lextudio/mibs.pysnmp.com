# SNMP MIB module (MLD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MLD-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:33 2024
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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swMldSnpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 34)
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

_SwMldSnpCtrl_ObjectIdentity = ObjectIdentity
swMldSnpCtrl = _SwMldSnpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 1)
)


class _SwMldSnoopingGlobalState_Type(Integer32):
    """Custom type swMldSnoopingGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMldSnoopingGlobalState_Type.__name__ = "Integer32"
_SwMldSnoopingGlobalState_Object = MibScalar
swMldSnoopingGlobalState = _SwMldSnoopingGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 1, 1),
    _SwMldSnoopingGlobalState_Type()
)
swMldSnoopingGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingGlobalState.setStatus("current")


class _SwMldSnoopingMcstRTOnly_Type(Integer32):
    """Custom type swMldSnoopingMcstRTOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMldSnoopingMcstRTOnly_Type.__name__ = "Integer32"
_SwMldSnoopingMcstRTOnly_Object = MibScalar
swMldSnoopingMcstRTOnly = _SwMldSnoopingMcstRTOnly_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 1, 2),
    _SwMldSnoopingMcstRTOnly_Type()
)
swMldSnoopingMcstRTOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingMcstRTOnly.setStatus("current")
_SwMldSnpInfo_ObjectIdentity = ObjectIdentity
swMldSnpInfo = _SwMldSnpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 2)
)
_SwMldSnpMgmt_ObjectIdentity = ObjectIdentity
swMldSnpMgmt = _SwMldSnpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3)
)


class _SwMldSnoopingMaxSupportedVlans_Type(Integer32):
    """Custom type swMldSnoopingMaxSupportedVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnoopingMaxSupportedVlans_Type.__name__ = "Integer32"
_SwMldSnoopingMaxSupportedVlans_Object = MibScalar
swMldSnoopingMaxSupportedVlans = _SwMldSnoopingMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 1),
    _SwMldSnoopingMaxSupportedVlans_Type()
)
swMldSnoopingMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingMaxSupportedVlans.setStatus("current")
_SwMldSnoopingCtrlTable_Object = MibTable
swMldSnoopingCtrlTable = _SwMldSnoopingCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2)
)
if mibBuilder.loadTexts:
    swMldSnoopingCtrlTable.setStatus("current")
_SwMldSnoopingCtrlEntry_Object = MibTableRow
swMldSnoopingCtrlEntry = _SwMldSnoopingCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1)
)
swMldSnoopingCtrlEntry.setIndexNames(
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingCtrlVid"),
)
if mibBuilder.loadTexts:
    swMldSnoopingCtrlEntry.setStatus("current")


class _SwMldSnoopingCtrlVid_Type(Integer32):
    """Custom type swMldSnoopingCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnoopingCtrlVid_Type.__name__ = "Integer32"
_SwMldSnoopingCtrlVid_Object = MibTableColumn
swMldSnoopingCtrlVid = _SwMldSnoopingCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 1),
    _SwMldSnoopingCtrlVid_Type()
)
swMldSnoopingCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingCtrlVid.setStatus("current")


class _SwMldSnoopingQueryInterval_Type(Integer32):
    """Custom type swMldSnoopingQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMldSnoopingQueryInterval_Type.__name__ = "Integer32"
_SwMldSnoopingQueryInterval_Object = MibTableColumn
swMldSnoopingQueryInterval = _SwMldSnoopingQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 2),
    _SwMldSnoopingQueryInterval_Type()
)
swMldSnoopingQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingQueryInterval.setStatus("current")


class _SwMldSnoopingMaxResponseTime_Type(Integer32):
    """Custom type swMldSnoopingMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwMldSnoopingMaxResponseTime_Type.__name__ = "Integer32"
_SwMldSnoopingMaxResponseTime_Object = MibTableColumn
swMldSnoopingMaxResponseTime = _SwMldSnoopingMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 3),
    _SwMldSnoopingMaxResponseTime_Type()
)
swMldSnoopingMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingMaxResponseTime.setStatus("current")


class _SwMldSnoopingRobustness_Type(Integer32):
    """Custom type swMldSnoopingRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwMldSnoopingRobustness_Type.__name__ = "Integer32"
_SwMldSnoopingRobustness_Object = MibTableColumn
swMldSnoopingRobustness = _SwMldSnoopingRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 4),
    _SwMldSnoopingRobustness_Type()
)
swMldSnoopingRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingRobustness.setStatus("current")


class _SwMldSnoopingLastMemberQueryInterval_Type(Integer32):
    """Custom type swMldSnoopingLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwMldSnoopingLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwMldSnoopingLastMemberQueryInterval_Object = MibTableColumn
swMldSnoopingLastMemberQueryInterval = _SwMldSnoopingLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 5),
    _SwMldSnoopingLastMemberQueryInterval_Type()
)
swMldSnoopingLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingLastMemberQueryInterval.setStatus("current")


class _SwMldSnoopingHostTimeout_Type(Integer32):
    """Custom type swMldSnoopingHostTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwMldSnoopingHostTimeout_Type.__name__ = "Integer32"
_SwMldSnoopingHostTimeout_Object = MibTableColumn
swMldSnoopingHostTimeout = _SwMldSnoopingHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 6),
    _SwMldSnoopingHostTimeout_Type()
)
swMldSnoopingHostTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingHostTimeout.setStatus("current")


class _SwMldSnoopingRouteTimeout_Type(Integer32):
    """Custom type swMldSnoopingRouteTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwMldSnoopingRouteTimeout_Type.__name__ = "Integer32"
_SwMldSnoopingRouteTimeout_Object = MibTableColumn
swMldSnoopingRouteTimeout = _SwMldSnoopingRouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 7),
    _SwMldSnoopingRouteTimeout_Type()
)
swMldSnoopingRouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingRouteTimeout.setStatus("current")


class _SwMldSnoopingDoneTimer_Type(Integer32):
    """Custom type swMldSnoopingDoneTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16711450),
    )


_SwMldSnoopingDoneTimer_Type.__name__ = "Integer32"
_SwMldSnoopingDoneTimer_Object = MibTableColumn
swMldSnoopingDoneTimer = _SwMldSnoopingDoneTimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 8),
    _SwMldSnoopingDoneTimer_Type()
)
swMldSnoopingDoneTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingDoneTimer.setStatus("current")


class _SwMldSnoopingQueryState_Type(Integer32):
    """Custom type swMldSnoopingQueryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwMldSnoopingQueryState_Type.__name__ = "Integer32"
_SwMldSnoopingQueryState_Object = MibTableColumn
swMldSnoopingQueryState = _SwMldSnoopingQueryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 9),
    _SwMldSnoopingQueryState_Type()
)
swMldSnoopingQueryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingQueryState.setStatus("current")


class _SwMldSnoopingCurrentState_Type(Integer32):
    """Custom type swMldSnoopingCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-querier", 3),
          ("other", 1),
          ("querier", 2))
    )


_SwMldSnoopingCurrentState_Type.__name__ = "Integer32"
_SwMldSnoopingCurrentState_Object = MibTableColumn
swMldSnoopingCurrentState = _SwMldSnoopingCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 10),
    _SwMldSnoopingCurrentState_Type()
)
swMldSnoopingCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingCurrentState.setStatus("current")


class _SwMldSnoopingCtrlState_Type(Integer32):
    """Custom type swMldSnoopingCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwMldSnoopingCtrlState_Type.__name__ = "Integer32"
_SwMldSnoopingCtrlState_Object = MibTableColumn
swMldSnoopingCtrlState = _SwMldSnoopingCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 11),
    _SwMldSnoopingCtrlState_Type()
)
swMldSnoopingCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingCtrlState.setStatus("current")


class _SwMldSnoopingFastDoneState_Type(Integer32):
    """Custom type swMldSnoopingFastDoneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwMldSnoopingFastDoneState_Type.__name__ = "Integer32"
_SwMldSnoopingFastDoneState_Object = MibTableColumn
swMldSnoopingFastDoneState = _SwMldSnoopingFastDoneState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 12),
    _SwMldSnoopingFastDoneState_Type()
)
swMldSnoopingFastDoneState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingFastDoneState.setStatus("current")


class _SwMldSnoopingVersion_Type(Integer32):
    """Custom type swMldSnoopingVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version-1", 1),
          ("version-2", 2))
    )


_SwMldSnoopingVersion_Type.__name__ = "Integer32"
_SwMldSnoopingVersion_Object = MibTableColumn
swMldSnoopingVersion = _SwMldSnoopingVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 2, 1, 13),
    _SwMldSnoopingVersion_Type()
)
swMldSnoopingVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnoopingVersion.setStatus("current")
_SwMldSnoopingGroupInfoTable_Object = MibTable
swMldSnoopingGroupInfoTable = _SwMldSnoopingGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3)
)
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoTable.setStatus("obsolete")
_SwMldSnoopingGroupInfoEntry_Object = MibTableRow
swMldSnoopingGroupInfoEntry = _SwMldSnoopingGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1)
)
swMldSnoopingGroupInfoEntry.setIndexNames(
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupInfoVid"),
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupInfoIpAddr"),
)
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoEntry.setStatus("obsolete")


class _SwMldSnoopingGroupInfoVid_Type(Integer32):
    """Custom type swMldSnoopingGroupInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnoopingGroupInfoVid_Type.__name__ = "Integer32"
_SwMldSnoopingGroupInfoVid_Object = MibTableColumn
swMldSnoopingGroupInfoVid = _SwMldSnoopingGroupInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 1),
    _SwMldSnoopingGroupInfoVid_Type()
)
swMldSnoopingGroupInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoVid.setStatus("obsolete")
_SwMldSnoopingGroupInfoIpAddr_Type = Ipv6Address
_SwMldSnoopingGroupInfoIpAddr_Object = MibTableColumn
swMldSnoopingGroupInfoIpAddr = _SwMldSnoopingGroupInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 2),
    _SwMldSnoopingGroupInfoIpAddr_Type()
)
swMldSnoopingGroupInfoIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoIpAddr.setStatus("obsolete")
_SwMldSnoopingGroupInfoMacAddr_Type = MacAddress
_SwMldSnoopingGroupInfoMacAddr_Object = MibTableColumn
swMldSnoopingGroupInfoMacAddr = _SwMldSnoopingGroupInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 3),
    _SwMldSnoopingGroupInfoMacAddr_Type()
)
swMldSnoopingGroupInfoMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoMacAddr.setStatus("obsolete")
_SwMldSnoopingGroupInfoPortMap_Type = PortList
_SwMldSnoopingGroupInfoPortMap_Object = MibTableColumn
swMldSnoopingGroupInfoPortMap = _SwMldSnoopingGroupInfoPortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 4),
    _SwMldSnoopingGroupInfoPortMap_Type()
)
swMldSnoopingGroupInfoPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoPortMap.setStatus("obsolete")


class _SwMldSnoopingGroupInfoReportCount_Type(Integer32):
    """Custom type swMldSnoopingGroupInfoReportCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnoopingGroupInfoReportCount_Type.__name__ = "Integer32"
_SwMldSnoopingGroupInfoReportCount_Object = MibTableColumn
swMldSnoopingGroupInfoReportCount = _SwMldSnoopingGroupInfoReportCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 3, 1, 5),
    _SwMldSnoopingGroupInfoReportCount_Type()
)
swMldSnoopingGroupInfoReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupInfoReportCount.setStatus("obsolete")
_SwMldSnpRouterPortsTable_Object = MibTable
swMldSnpRouterPortsTable = _SwMldSnpRouterPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4)
)
if mibBuilder.loadTexts:
    swMldSnpRouterPortsTable.setStatus("current")
_SwMldSnpRouterPortsEntry_Object = MibTableRow
swMldSnpRouterPortsEntry = _SwMldSnpRouterPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1)
)
swMldSnpRouterPortsEntry.setIndexNames(
    (0, "MLD-SNOOPING-MIB", "swMldSnpRouterPortsVid"),
)
if mibBuilder.loadTexts:
    swMldSnpRouterPortsEntry.setStatus("current")


class _SwMldSnpRouterPortsVid_Type(Integer32):
    """Custom type swMldSnpRouterPortsVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnpRouterPortsVid_Type.__name__ = "Integer32"
_SwMldSnpRouterPortsVid_Object = MibTableColumn
swMldSnpRouterPortsVid = _SwMldSnpRouterPortsVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 1),
    _SwMldSnpRouterPortsVid_Type()
)
swMldSnpRouterPortsVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpRouterPortsVid.setStatus("current")
_SwMldSnpRouterStaticPortList_Type = PortList
_SwMldSnpRouterStaticPortList_Object = MibTableColumn
swMldSnpRouterStaticPortList = _SwMldSnpRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 2),
    _SwMldSnpRouterStaticPortList_Type()
)
swMldSnpRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnpRouterStaticPortList.setStatus("current")
_SwMldSnpRouterDynamicPortList_Type = PortList
_SwMldSnpRouterDynamicPortList_Object = MibTableColumn
swMldSnpRouterDynamicPortList = _SwMldSnpRouterDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 3),
    _SwMldSnpRouterDynamicPortList_Type()
)
swMldSnpRouterDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpRouterDynamicPortList.setStatus("current")
_SwMldSnpRouterForbiddenPortList_Type = PortList
_SwMldSnpRouterForbiddenPortList_Object = MibTableColumn
swMldSnpRouterForbiddenPortList = _SwMldSnpRouterForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 4, 1, 4),
    _SwMldSnpRouterForbiddenPortList_Type()
)
swMldSnpRouterForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMldSnpRouterForbiddenPortList.setStatus("current")
_SwMldSnoopingGroupTable_Object = MibTable
swMldSnoopingGroupTable = _SwMldSnoopingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5)
)
if mibBuilder.loadTexts:
    swMldSnoopingGroupTable.setStatus("current")
_SwMldSnoopingGroupEntry_Object = MibTableRow
swMldSnoopingGroupEntry = _SwMldSnoopingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1)
)
swMldSnoopingGroupEntry.setIndexNames(
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupVid"),
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupGroupAddr"),
    (0, "MLD-SNOOPING-MIB", "swMldSnoopingGroupSourceAddr"),
)
if mibBuilder.loadTexts:
    swMldSnoopingGroupEntry.setStatus("current")


class _SwMldSnoopingGroupVid_Type(Integer32):
    """Custom type swMldSnoopingGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnoopingGroupVid_Type.__name__ = "Integer32"
_SwMldSnoopingGroupVid_Object = MibTableColumn
swMldSnoopingGroupVid = _SwMldSnoopingGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 1),
    _SwMldSnoopingGroupVid_Type()
)
swMldSnoopingGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupVid.setStatus("current")
_SwMldSnoopingGroupGroupAddr_Type = Ipv6Address
_SwMldSnoopingGroupGroupAddr_Object = MibTableColumn
swMldSnoopingGroupGroupAddr = _SwMldSnoopingGroupGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 2),
    _SwMldSnoopingGroupGroupAddr_Type()
)
swMldSnoopingGroupGroupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupGroupAddr.setStatus("current")
_SwMldSnoopingGroupSourceAddr_Type = Ipv6Address
_SwMldSnoopingGroupSourceAddr_Object = MibTableColumn
swMldSnoopingGroupSourceAddr = _SwMldSnoopingGroupSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 3),
    _SwMldSnoopingGroupSourceAddr_Type()
)
swMldSnoopingGroupSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupSourceAddr.setStatus("current")
_SwMldSnoopingGroupIncludePortMap_Type = PortList
_SwMldSnoopingGroupIncludePortMap_Object = MibTableColumn
swMldSnoopingGroupIncludePortMap = _SwMldSnoopingGroupIncludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 4),
    _SwMldSnoopingGroupIncludePortMap_Type()
)
swMldSnoopingGroupIncludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupIncludePortMap.setStatus("current")
_SwMldSnoopingGroupExcludePortMap_Type = PortList
_SwMldSnoopingGroupExcludePortMap_Object = MibTableColumn
swMldSnoopingGroupExcludePortMap = _SwMldSnoopingGroupExcludePortMap_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 5, 1, 5),
    _SwMldSnoopingGroupExcludePortMap_Type()
)
swMldSnoopingGroupExcludePortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnoopingGroupExcludePortMap.setStatus("current")
_SwMldSnpForwardingTable_Object = MibTable
swMldSnpForwardingTable = _SwMldSnpForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6)
)
if mibBuilder.loadTexts:
    swMldSnpForwardingTable.setStatus("current")
_SwMldSnpForwardingEntry_Object = MibTableRow
swMldSnpForwardingEntry = _SwMldSnpForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1)
)
swMldSnpForwardingEntry.setIndexNames(
    (0, "MLD-SNOOPING-MIB", "swMldSnpVid"),
    (0, "MLD-SNOOPING-MIB", "swMldSnpSourceIpAddr"),
    (0, "MLD-SNOOPING-MIB", "swMldSnpMutiGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swMldSnpForwardingEntry.setStatus("current")


class _SwMldSnpVid_Type(Integer32):
    """Custom type swMldSnpVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwMldSnpVid_Type.__name__ = "Integer32"
_SwMldSnpVid_Object = MibTableColumn
swMldSnpVid = _SwMldSnpVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 1),
    _SwMldSnpVid_Type()
)
swMldSnpVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpVid.setStatus("current")
_SwMldSnpSourceIpAddr_Type = Ipv6Address
_SwMldSnpSourceIpAddr_Object = MibTableColumn
swMldSnpSourceIpAddr = _SwMldSnpSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 2),
    _SwMldSnpSourceIpAddr_Type()
)
swMldSnpSourceIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpSourceIpAddr.setStatus("current")
_SwMldSnpMutiGroupIpAddr_Type = Ipv6Address
_SwMldSnpMutiGroupIpAddr_Object = MibTableColumn
swMldSnpMutiGroupIpAddr = _SwMldSnpMutiGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 3),
    _SwMldSnpMutiGroupIpAddr_Type()
)
swMldSnpMutiGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpMutiGroupIpAddr.setStatus("current")
_SwMldSnpForwardingListenPort_Type = PortList
_SwMldSnpForwardingListenPort_Object = MibTableColumn
swMldSnpForwardingListenPort = _SwMldSnpForwardingListenPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 34, 3, 6, 1, 4),
    _SwMldSnpForwardingListenPort_Type()
)
swMldSnpForwardingListenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMldSnpForwardingListenPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MLD-SNOOPING-MIB",
    **{"Ipv6Address": Ipv6Address,
       "PortList": PortList,
       "swMldSnpMIB": swMldSnpMIB,
       "swMldSnpCtrl": swMldSnpCtrl,
       "swMldSnoopingGlobalState": swMldSnoopingGlobalState,
       "swMldSnoopingMcstRTOnly": swMldSnoopingMcstRTOnly,
       "swMldSnpInfo": swMldSnpInfo,
       "swMldSnpMgmt": swMldSnpMgmt,
       "swMldSnoopingMaxSupportedVlans": swMldSnoopingMaxSupportedVlans,
       "swMldSnoopingCtrlTable": swMldSnoopingCtrlTable,
       "swMldSnoopingCtrlEntry": swMldSnoopingCtrlEntry,
       "swMldSnoopingCtrlVid": swMldSnoopingCtrlVid,
       "swMldSnoopingQueryInterval": swMldSnoopingQueryInterval,
       "swMldSnoopingMaxResponseTime": swMldSnoopingMaxResponseTime,
       "swMldSnoopingRobustness": swMldSnoopingRobustness,
       "swMldSnoopingLastMemberQueryInterval": swMldSnoopingLastMemberQueryInterval,
       "swMldSnoopingHostTimeout": swMldSnoopingHostTimeout,
       "swMldSnoopingRouteTimeout": swMldSnoopingRouteTimeout,
       "swMldSnoopingDoneTimer": swMldSnoopingDoneTimer,
       "swMldSnoopingQueryState": swMldSnoopingQueryState,
       "swMldSnoopingCurrentState": swMldSnoopingCurrentState,
       "swMldSnoopingCtrlState": swMldSnoopingCtrlState,
       "swMldSnoopingFastDoneState": swMldSnoopingFastDoneState,
       "swMldSnoopingVersion": swMldSnoopingVersion,
       "swMldSnoopingGroupInfoTable": swMldSnoopingGroupInfoTable,
       "swMldSnoopingGroupInfoEntry": swMldSnoopingGroupInfoEntry,
       "swMldSnoopingGroupInfoVid": swMldSnoopingGroupInfoVid,
       "swMldSnoopingGroupInfoIpAddr": swMldSnoopingGroupInfoIpAddr,
       "swMldSnoopingGroupInfoMacAddr": swMldSnoopingGroupInfoMacAddr,
       "swMldSnoopingGroupInfoPortMap": swMldSnoopingGroupInfoPortMap,
       "swMldSnoopingGroupInfoReportCount": swMldSnoopingGroupInfoReportCount,
       "swMldSnpRouterPortsTable": swMldSnpRouterPortsTable,
       "swMldSnpRouterPortsEntry": swMldSnpRouterPortsEntry,
       "swMldSnpRouterPortsVid": swMldSnpRouterPortsVid,
       "swMldSnpRouterStaticPortList": swMldSnpRouterStaticPortList,
       "swMldSnpRouterDynamicPortList": swMldSnpRouterDynamicPortList,
       "swMldSnpRouterForbiddenPortList": swMldSnpRouterForbiddenPortList,
       "swMldSnoopingGroupTable": swMldSnoopingGroupTable,
       "swMldSnoopingGroupEntry": swMldSnoopingGroupEntry,
       "swMldSnoopingGroupVid": swMldSnoopingGroupVid,
       "swMldSnoopingGroupGroupAddr": swMldSnoopingGroupGroupAddr,
       "swMldSnoopingGroupSourceAddr": swMldSnoopingGroupSourceAddr,
       "swMldSnoopingGroupIncludePortMap": swMldSnoopingGroupIncludePortMap,
       "swMldSnoopingGroupExcludePortMap": swMldSnoopingGroupExcludePortMap,
       "swMldSnpForwardingTable": swMldSnpForwardingTable,
       "swMldSnpForwardingEntry": swMldSnpForwardingEntry,
       "swMldSnpVid": swMldSnpVid,
       "swMldSnpSourceIpAddr": swMldSnpSourceIpAddr,
       "swMldSnpMutiGroupIpAddr": swMldSnpMutiGroupIpAddr,
       "swMldSnpForwardingListenPort": swMldSnpForwardingListenPort}
)
