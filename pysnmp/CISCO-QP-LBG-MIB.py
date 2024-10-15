# SNMP MIB module (CISCO-QP-LBG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-QP-LBG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:23 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoQpLbgMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824)
)
ciscoQpLbgMIB.setRevisions(
        ("2015-09-21 00:00",
         "2014-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoQpLbgNotifs_ObjectIdentity = ObjectIdentity
ciscoQpLbgNotifs = _CiscoQpLbgNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0)
)
_CiscoQpLbgObjects_ObjectIdentity = ObjectIdentity
ciscoQpLbgObjects = _CiscoQpLbgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1)
)
_CqlqamPartitionTable_Object = MibTable
cqlqamPartitionTable = _CqlqamPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1)
)
if mibBuilder.loadTexts:
    cqlqamPartitionTable.setStatus("current")
_CqlqamPartitionEntry_Object = MibTableRow
cqlqamPartitionEntry = _CqlqamPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1)
)
cqlqamPartitionEntry.setIndexNames(
    (0, "CISCO-QP-LBG-MIB", "cqlqpIndex"),
)
if mibBuilder.loadTexts:
    cqlqamPartitionEntry.setStatus("current")
_CqlqpIndex_Type = Unsigned32
_CqlqpIndex_Object = MibTableColumn
cqlqpIndex = _CqlqpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 1),
    _CqlqpIndex_Type()
)
cqlqpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqlqpIndex.setStatus("current")
_CqlqpId_Type = Unsigned32
_CqlqpId_Object = MibTableColumn
cqlqpId = _CqlqpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 2),
    _CqlqpId_Type()
)
cqlqpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpId.setStatus("current")


class _CqlqpMgmtIpAddrType_Type(InetAddressType):
    """Custom type cqlqpMgmtIpAddrType based on InetAddressType"""


_CqlqpMgmtIpAddrType_Object = MibTableColumn
cqlqpMgmtIpAddrType = _CqlqpMgmtIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 3),
    _CqlqpMgmtIpAddrType_Type()
)
cqlqpMgmtIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpMgmtIpAddrType.setStatus("current")
_CqlqpMgmtIp_Type = InetAddress
_CqlqpMgmtIp_Object = MibTableColumn
cqlqpMgmtIp = _CqlqpMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 4),
    _CqlqpMgmtIp_Type()
)
cqlqpMgmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpMgmtIp.setStatus("current")
_CqlqpServerIpAddrType_Type = InetAddressType
_CqlqpServerIpAddrType_Object = MibTableColumn
cqlqpServerIpAddrType = _CqlqpServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 5),
    _CqlqpServerIpAddrType_Type()
)
cqlqpServerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpServerIpAddrType.setStatus("current")
_CqlqpServerIp_Type = InetAddress
_CqlqpServerIp_Object = MibTableColumn
cqlqpServerIp = _CqlqpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 6),
    _CqlqpServerIp_Type()
)
cqlqpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpServerIp.setStatus("current")


class _CqlqpState_Type(Integer32):
    """Custom type cqlqpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 1),
          ("init", 2))
    )


_CqlqpState_Type.__name__ = "Integer32"
_CqlqpState_Object = MibTableColumn
cqlqpState = _CqlqpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 7),
    _CqlqpState_Type()
)
cqlqpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpState.setStatus("current")


class _CqlqpProtocol_Type(Integer32):
    """Custom type cqlqpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ermi", 2),
          ("gqi", 1))
    )


_CqlqpProtocol_Type.__name__ = "Integer32"
_CqlqpProtocol_Object = MibTableColumn
cqlqpProtocol = _CqlqpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 8),
    _CqlqpProtocol_Type()
)
cqlqpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpProtocol.setStatus("current")
_CqlqpKeepAliveTime_Type = Unsigned32
_CqlqpKeepAliveTime_Object = MibTableColumn
cqlqpKeepAliveTime = _CqlqpKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 9),
    _CqlqpKeepAliveTime_Type()
)
cqlqpKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpKeepAliveTime.setUnits("seconds")


class _CqlqpServerState_Type(Integer32):
    """Custom type cqlqpServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_CqlqpServerState_Type.__name__ = "Integer32"
_CqlqpServerState_Object = MibTableColumn
cqlqpServerState = _CqlqpServerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 10),
    _CqlqpServerState_Type()
)
cqlqpServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpServerState.setStatus("current")
_CqlqpGqiMacAddr_Type = MacAddress
_CqlqpGqiMacAddr_Object = MibTableColumn
cqlqpGqiMacAddr = _CqlqpGqiMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 11),
    _CqlqpGqiMacAddr_Type()
)
cqlqpGqiMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpGqiMacAddr.setStatus("current")
_CqlqpGqiResetInterval_Type = Unsigned32
_CqlqpGqiResetInterval_Object = MibTableColumn
cqlqpGqiResetInterval = _CqlqpGqiResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 12),
    _CqlqpGqiResetInterval_Type()
)
cqlqpGqiResetInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpGqiResetInterval.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpGqiResetInterval.setUnits("seconds")
_CqlqpNumQams_Type = Unsigned32
_CqlqpNumQams_Object = MibTableColumn
cqlqpNumQams = _CqlqpNumQams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 13),
    _CqlqpNumQams_Type()
)
cqlqpNumQams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpNumQams.setStatus("current")
_CqlqpQamCarrrierList_Type = OctetString
_CqlqpQamCarrrierList_Object = MibTableColumn
cqlqpQamCarrrierList = _CqlqpQamCarrrierList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 14),
    _CqlqpQamCarrrierList_Type()
)
cqlqpQamCarrrierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpQamCarrrierList.setStatus("current")
_CqlqpNumRoutes_Type = Unsigned32
_CqlqpNumRoutes_Object = MibTableColumn
cqlqpNumRoutes = _CqlqpNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 15),
    _CqlqpNumRoutes_Type()
)
cqlqpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpNumRoutes.setStatus("current")
_CqlqpRouteDetails_Type = OctetString
_CqlqpRouteDetails_Object = MibTableColumn
cqlqpRouteDetails = _CqlqpRouteDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 16),
    _CqlqpRouteDetails_Type()
)
cqlqpRouteDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpRouteDetails.setStatus("current")
_CqlqpErmiErrpComponentName_Type = OctetString
_CqlqpErmiErrpComponentName_Object = MibTableColumn
cqlqpErmiErrpComponentName = _CqlqpErmiErrpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 17),
    _CqlqpErmiErrpComponentName_Type()
)
cqlqpErmiErrpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiErrpComponentName.setStatus("current")
_CqlqpErmiErrpStreamingZone_Type = OctetString
_CqlqpErmiErrpStreamingZone_Object = MibTableColumn
cqlqpErmiErrpStreamingZone = _CqlqpErmiErrpStreamingZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 18),
    _CqlqpErmiErrpStreamingZone_Type()
)
cqlqpErmiErrpStreamingZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiErrpStreamingZone.setStatus("current")


class _CqlqpErmiErrpHoldTime_Type(Unsigned32):
    """Custom type cqlqpErmiErrpHoldTime based on Unsigned32"""
    defaultValue = 90


_CqlqpErmiErrpHoldTime_Object = MibTableColumn
cqlqpErmiErrpHoldTime = _CqlqpErmiErrpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 19),
    _CqlqpErmiErrpHoldTime_Type()
)
cqlqpErmiErrpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiErrpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiErrpHoldTime.setUnits("seconds")


class _CqlqpErmiErrpConnnectTime_Type(Unsigned32):
    """Custom type cqlqpErmiErrpConnnectTime based on Unsigned32"""
    defaultValue = 10


_CqlqpErmiErrpConnnectTime_Object = MibTableColumn
cqlqpErmiErrpConnnectTime = _CqlqpErmiErrpConnnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 20),
    _CqlqpErmiErrpConnnectTime_Type()
)
cqlqpErmiErrpConnnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiErrpConnnectTime.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiErrpConnnectTime.setUnits("seconds")


class _CqlqpErmiErrpConnectRetry_Type(Unsigned32):
    """Custom type cqlqpErmiErrpConnectRetry based on Unsigned32"""
    defaultValue = 0


_CqlqpErmiErrpConnectRetry_Object = MibTableColumn
cqlqpErmiErrpConnectRetry = _CqlqpErmiErrpConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 21),
    _CqlqpErmiErrpConnectRetry_Type()
)
cqlqpErmiErrpConnectRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiErrpConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiErrpConnectRetry.setUnits("seconds")


class _CqlqpErmiRtspConnectTime_Type(Unsigned32):
    """Custom type cqlqpErmiRtspConnectTime based on Unsigned32"""
    defaultValue = 200


_CqlqpErmiRtspConnectTime_Object = MibTableColumn
cqlqpErmiRtspConnectTime = _CqlqpErmiRtspConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 22),
    _CqlqpErmiRtspConnectTime_Type()
)
cqlqpErmiRtspConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiRtspConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiRtspConnectTime.setUnits("seconds")


class _CqlqpErmiRtspConnectRetry_Type(Unsigned32):
    """Custom type cqlqpErmiRtspConnectRetry based on Unsigned32"""
    defaultValue = 0


_CqlqpErmiRtspConnectRetry_Object = MibTableColumn
cqlqpErmiRtspConnectRetry = _CqlqpErmiRtspConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 23),
    _CqlqpErmiRtspConnectRetry_Type()
)
cqlqpErmiRtspConnectRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiRtspConnectRetry.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiRtspConnectRetry.setUnits("seconds")


class _CqlqpErmiRtspKeepAliveTime_Type(Unsigned32):
    """Custom type cqlqpErmiRtspKeepAliveTime based on Unsigned32"""
    defaultValue = 300


_CqlqpErmiRtspKeepAliveTime_Object = MibTableColumn
cqlqpErmiRtspKeepAliveTime = _CqlqpErmiRtspKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 24),
    _CqlqpErmiRtspKeepAliveTime_Type()
)
cqlqpErmiRtspKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiRtspKeepAliveTime.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiRtspKeepAliveTime.setUnits("seconds")


class _CqlqpErmiRtspSessionTimeout_Type(Unsigned32):
    """Custom type cqlqpErmiRtspSessionTimeout based on Unsigned32"""
    defaultValue = 10800


_CqlqpErmiRtspSessionTimeout_Object = MibTableColumn
cqlqpErmiRtspSessionTimeout = _CqlqpErmiRtspSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 25),
    _CqlqpErmiRtspSessionTimeout_Type()
)
cqlqpErmiRtspSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpErmiRtspSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cqlqpErmiRtspSessionTimeout.setUnits("seconds")


class _CqlqpQamOversubscribedStatus_Type(TruthValue):
    """Custom type cqlqpQamOversubscribedStatus based on TruthValue"""


_CqlqpQamOversubscribedStatus_Object = MibTableColumn
cqlqpQamOversubscribedStatus = _CqlqpQamOversubscribedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 26),
    _CqlqpQamOversubscribedStatus_Type()
)
cqlqpQamOversubscribedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpQamOversubscribedStatus.setStatus("current")
_CqlqpServerIpList_Type = OctetString
_CqlqpServerIpList_Object = MibTableColumn
cqlqpServerIpList = _CqlqpServerIpList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 1, 1, 27),
    _CqlqpServerIpList_Type()
)
cqlqpServerIpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqlqpServerIpList.setStatus("current")
_CqlloadBalanceGroupTable_Object = MibTable
cqlloadBalanceGroupTable = _CqlloadBalanceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2)
)
if mibBuilder.loadTexts:
    cqlloadBalanceGroupTable.setStatus("current")
_CqlloadBalanceGroupEntry_Object = MibTableRow
cqlloadBalanceGroupEntry = _CqlloadBalanceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1)
)
cqlloadBalanceGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-QP-LBG-MIB", "cqllbgIndex"),
)
if mibBuilder.loadTexts:
    cqlloadBalanceGroupEntry.setStatus("current")
_CqllbgIndex_Type = Unsigned32
_CqllbgIndex_Object = MibTableColumn
cqllbgIndex = _CqllbgIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1, 1),
    _CqllbgIndex_Type()
)
cqllbgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqllbgIndex.setStatus("current")
_CqllbgTotalBandwidth_Type = Unsigned32
_CqllbgTotalBandwidth_Object = MibTableColumn
cqllbgTotalBandwidth = _CqllbgTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1, 2),
    _CqllbgTotalBandwidth_Type()
)
cqllbgTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgTotalBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgTotalBandwidth.setUnits("Kbps")
_CqllbgQamRsvBandwidth_Type = Unsigned32
_CqllbgQamRsvBandwidth_Object = MibTableColumn
cqllbgQamRsvBandwidth = _CqllbgQamRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1, 3),
    _CqllbgQamRsvBandwidth_Type()
)
cqllbgQamRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgQamRsvBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgQamRsvBandwidth.setUnits("Kbps")
_CqllbgIpRsvBandwidth_Type = Unsigned32
_CqllbgIpRsvBandwidth_Object = MibTableColumn
cqllbgIpRsvBandwidth = _CqllbgIpRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1, 4),
    _CqllbgIpRsvBandwidth_Type()
)
cqllbgIpRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgIpRsvBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgIpRsvBandwidth.setUnits("Kbps")
_CqllbgAvailableBandwidth_Type = Unsigned32
_CqllbgAvailableBandwidth_Object = MibTableColumn
cqllbgAvailableBandwidth = _CqllbgAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 2, 1, 5),
    _CqllbgAvailableBandwidth_Type()
)
cqllbgAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgAvailableBandwidth.setUnits("Kbps")
_CqllbgrouteTable_Object = MibTable
cqllbgrouteTable = _CqllbgrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3)
)
if mibBuilder.loadTexts:
    cqllbgrouteTable.setStatus("current")
_CqllbgrouteEntry_Object = MibTableRow
cqllbgrouteEntry = _CqllbgrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1)
)
cqllbgrouteEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-QP-LBG-MIB", "cqllbgRouteIndex"),
)
if mibBuilder.loadTexts:
    cqllbgrouteEntry.setStatus("current")
_CqllbgRouteIndex_Type = Unsigned32
_CqllbgRouteIndex_Object = MibTableColumn
cqllbgRouteIndex = _CqllbgRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 1),
    _CqllbgRouteIndex_Type()
)
cqllbgRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cqllbgRouteIndex.setStatus("current")
_CqllbgQpId_Type = Unsigned32
_CqllbgQpId_Object = MibTableColumn
cqllbgQpId = _CqllbgQpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 2),
    _CqllbgQpId_Type()
)
cqllbgQpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgQpId.setStatus("current")


class _CqllbgDstIpAddrType_Type(InetAddressType):
    """Custom type cqllbgDstIpAddrType based on InetAddressType"""


_CqllbgDstIpAddrType_Object = MibTableColumn
cqllbgDstIpAddrType = _CqllbgDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 3),
    _CqllbgDstIpAddrType_Type()
)
cqllbgDstIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgDstIpAddrType.setStatus("current")
_CqllbgDstIpAddr_Type = InetAddress
_CqllbgDstIpAddr_Object = MibTableColumn
cqllbgDstIpAddr = _CqllbgDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 4),
    _CqllbgDstIpAddr_Type()
)
cqllbgDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgDstIpAddr.setStatus("current")
_CqllbgUdpPortRangeMin_Type = Unsigned32
_CqllbgUdpPortRangeMin_Object = MibTableColumn
cqllbgUdpPortRangeMin = _CqllbgUdpPortRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 5),
    _CqllbgUdpPortRangeMin_Type()
)
cqllbgUdpPortRangeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgUdpPortRangeMin.setStatus("current")
_CqllbgUdpPortRangeMax_Type = Unsigned32
_CqllbgUdpPortRangeMax_Object = MibTableColumn
cqllbgUdpPortRangeMax = _CqllbgUdpPortRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 6),
    _CqllbgUdpPortRangeMax_Type()
)
cqllbgUdpPortRangeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgUdpPortRangeMax.setStatus("current")
_CqllbgGqiIngressPort_Type = Unsigned32
_CqllbgGqiIngressPort_Object = MibTableColumn
cqllbgGqiIngressPort = _CqllbgGqiIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 7),
    _CqllbgGqiIngressPort_Type()
)
cqllbgGqiIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgGqiIngressPort.setStatus("current")
_CqllbgRsvBandwidth_Type = Unsigned32
_CqllbgRsvBandwidth_Object = MibTableColumn
cqllbgRsvBandwidth = _CqllbgRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 8),
    _CqllbgRsvBandwidth_Type()
)
cqllbgRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgRsvBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgRsvBandwidth.setUnits("Kbps")
_CqllbgAllocatedBandwidth_Type = Unsigned32
_CqllbgAllocatedBandwidth_Object = MibTableColumn
cqllbgAllocatedBandwidth = _CqllbgAllocatedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 9),
    _CqllbgAllocatedBandwidth_Type()
)
cqllbgAllocatedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgAllocatedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cqllbgAllocatedBandwidth.setUnits("Kbps")
_CqllbgNumFlows_Type = Unsigned32
_CqllbgNumFlows_Object = MibTableColumn
cqllbgNumFlows = _CqllbgNumFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 3, 1, 10),
    _CqllbgNumFlows_Type()
)
cqllbgNumFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cqllbgNumFlows.setStatus("current")


class _CqlQpNotifyEnable_Type(TruthValue):
    """Custom type cqlQpNotifyEnable based on TruthValue"""


_CqlQpNotifyEnable_Object = MibScalar
cqlQpNotifyEnable = _CqlQpNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 4),
    _CqlQpNotifyEnable_Type()
)
cqlQpNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cqlQpNotifyEnable.setStatus("current")


class _CqlQamNotifyEnable_Type(TruthValue):
    """Custom type cqlQamNotifyEnable based on TruthValue"""


_CqlQamNotifyEnable_Object = MibScalar
cqlQamNotifyEnable = _CqlQamNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 5),
    _CqlQamNotifyEnable_Type()
)
cqlQamNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cqlQamNotifyEnable.setStatus("current")


class _CqlRouteNotifyEnable_Type(TruthValue):
    """Custom type cqlRouteNotifyEnable based on TruthValue"""


_CqlRouteNotifyEnable_Object = MibScalar
cqlRouteNotifyEnable = _CqlRouteNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 6),
    _CqlRouteNotifyEnable_Type()
)
cqlRouteNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cqlRouteNotifyEnable.setStatus("current")


class _CqlQamOverSubscribedEnable_Type(TruthValue):
    """Custom type cqlQamOverSubscribedEnable based on TruthValue"""


_CqlQamOverSubscribedEnable_Object = MibScalar
cqlQamOverSubscribedEnable = _CqlQamOverSubscribedEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 1, 7),
    _CqlQamOverSubscribedEnable_Type()
)
cqlQamOverSubscribedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cqlQamOverSubscribedEnable.setStatus("current")
_CiscoQpLbgConform_ObjectIdentity = ObjectIdentity
ciscoQpLbgConform = _CiscoQpLbgConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2)
)
_CiscoQpLbgCompliances_ObjectIdentity = ObjectIdentity
ciscoQpLbgCompliances = _CiscoQpLbgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 1)
)
_CiscoQpLbgGroups_ObjectIdentity = ObjectIdentity
ciscoQpLbgGroups = _CiscoQpLbgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2)
)

# Managed Objects groups

cqlciscoQpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 3)
)
cqlciscoQpObjectGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlqpId"),
        ("CISCO-QP-LBG-MIB", "cqlqpMgmtIp"),
        ("CISCO-QP-LBG-MIB", "cqlqpState"),
        ("CISCO-QP-LBG-MIB", "cqlqpProtocol"),
        ("CISCO-QP-LBG-MIB", "cqlqpKeepAliveTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpGqiResetInterval"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerIp"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerState"),
        ("CISCO-QP-LBG-MIB", "cqlqpGqiMacAddr"),
        ("CISCO-QP-LBG-MIB", "cqlqpNumQams"),
        ("CISCO-QP-LBG-MIB", "cqlqpQamCarrrierList"),
        ("CISCO-QP-LBG-MIB", "cqlqpNumRoutes"),
        ("CISCO-QP-LBG-MIB", "cqlqpRouteDetails"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpComponentName"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpStreamingZone"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpConnectRetry"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpConnnectTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpHoldTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspConnectRetry"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspConnectTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspKeepAliveTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspSessionTimeout"),
        ("CISCO-QP-LBG-MIB", "cqlqpMgmtIpAddrType"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerIpAddrType"))
)
if mibBuilder.loadTexts:
    cqlciscoQpObjectGroup.setStatus("deprecated")

cqlciscoLbgObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 4)
)
cqlciscoLbgObjectGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqllbgTotalBandwidth"),
        ("CISCO-QP-LBG-MIB", "cqllbgQamRsvBandwidth"),
        ("CISCO-QP-LBG-MIB", "cqllbgIpRsvBandwidth"),
        ("CISCO-QP-LBG-MIB", "cqllbgAvailableBandwidth"))
)
if mibBuilder.loadTexts:
    cqlciscoLbgObjectGroup.setStatus("current")

cqlciscoLbgRouteObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 5)
)
cqlciscoLbgRouteObjectGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqllbgQpId"),
        ("CISCO-QP-LBG-MIB", "cqllbgDstIpAddr"),
        ("CISCO-QP-LBG-MIB", "cqllbgUdpPortRangeMin"),
        ("CISCO-QP-LBG-MIB", "cqllbgUdpPortRangeMax"),
        ("CISCO-QP-LBG-MIB", "cqllbgGqiIngressPort"),
        ("CISCO-QP-LBG-MIB", "cqllbgAllocatedBandwidth"),
        ("CISCO-QP-LBG-MIB", "cqllbgRsvBandwidth"),
        ("CISCO-QP-LBG-MIB", "cqllbgNumFlows"),
        ("CISCO-QP-LBG-MIB", "cqllbgDstIpAddrType"))
)
if mibBuilder.loadTexts:
    cqlciscoLbgRouteObjectGroup.setStatus("current")

cqlciscoQpLbgNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 6)
)
cqlciscoQpLbgNotifsControlGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlQpNotifyEnable"),
        ("CISCO-QP-LBG-MIB", "cqlQamNotifyEnable"),
        ("CISCO-QP-LBG-MIB", "cqlRouteNotifyEnable"))
)
if mibBuilder.loadTexts:
    cqlciscoQpLbgNotifsControlGroup.setStatus("deprecated")

cqlciscoQpObjectGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 8)
)
cqlciscoQpObjectGroup1.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlqpId"),
        ("CISCO-QP-LBG-MIB", "cqlqpMgmtIpAddrType"),
        ("CISCO-QP-LBG-MIB", "cqlqpMgmtIp"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerIpAddrType"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerIp"),
        ("CISCO-QP-LBG-MIB", "cqlqpState"),
        ("CISCO-QP-LBG-MIB", "cqlqpProtocol"),
        ("CISCO-QP-LBG-MIB", "cqlqpKeepAliveTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerState"),
        ("CISCO-QP-LBG-MIB", "cqlqpGqiMacAddr"),
        ("CISCO-QP-LBG-MIB", "cqlqpGqiResetInterval"),
        ("CISCO-QP-LBG-MIB", "cqlqpNumQams"),
        ("CISCO-QP-LBG-MIB", "cqlqpQamCarrrierList"),
        ("CISCO-QP-LBG-MIB", "cqlqpNumRoutes"),
        ("CISCO-QP-LBG-MIB", "cqlqpRouteDetails"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpComponentName"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpStreamingZone"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpHoldTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpConnnectTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiErrpConnectRetry"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspConnectTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspConnectRetry"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspKeepAliveTime"),
        ("CISCO-QP-LBG-MIB", "cqlqpErmiRtspSessionTimeout"),
        ("CISCO-QP-LBG-MIB", "cqlqpQamOversubscribedStatus"),
        ("CISCO-QP-LBG-MIB", "cqlqpServerIpList"))
)
if mibBuilder.loadTexts:
    cqlciscoQpObjectGroup1.setStatus("current")

cqlciscoQpLbgNotifsControlGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 9)
)
cqlciscoQpLbgNotifsControlGroup1.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlQpNotifyEnable"),
        ("CISCO-QP-LBG-MIB", "cqlQamNotifyEnable"),
        ("CISCO-QP-LBG-MIB", "cqlRouteNotifyEnable"),
        ("CISCO-QP-LBG-MIB", "cqlQamOverSubscribedEnable"))
)
if mibBuilder.loadTexts:
    cqlciscoQpLbgNotifsControlGroup1.setStatus("current")


# Notification objects

cqlQpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 1)
)
cqlQpStateChange.setObjects(
    ("CISCO-QP-LBG-MIB", "cqlqpState")
)
if mibBuilder.loadTexts:
    cqlQpStateChange.setStatus(
        "current"
    )

cqlQamAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 2)
)
cqlQamAdd.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlqpId"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    cqlQamAdd.setStatus(
        "current"
    )

cqlQamDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 3)
)
cqlQamDelete.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlqpId"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    cqlQamDelete.setStatus(
        "current"
    )

cqlLbgRouteAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 4)
)
cqlLbgRouteAdd.setObjects(
    ("CISCO-QP-LBG-MIB", "cqlqpRouteDetails")
)
if mibBuilder.loadTexts:
    cqlLbgRouteAdd.setStatus(
        "current"
    )

cqlLbgRouteDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 5)
)
cqlLbgRouteDelete.setObjects(
    ("CISCO-QP-LBG-MIB", "cqlqpRouteDetails")
)
if mibBuilder.loadTexts:
    cqlLbgRouteDelete.setStatus(
        "current"
    )

cqlQamOverSubscribedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 0, 6)
)
cqlQamOverSubscribedAlert.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("CISCO-QP-LBG-MIB", "cqlqpQamOversubscribedStatus"))
)
if mibBuilder.loadTexts:
    cqlQamOverSubscribedAlert.setStatus(
        "current"
    )


# Notifications groups

cqlciscoQpNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 1)
)
cqlciscoQpNotifsGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlQpStateChange"),
        ("CISCO-QP-LBG-MIB", "cqlQamAdd"),
        ("CISCO-QP-LBG-MIB", "cqlQamDelete"))
)
if mibBuilder.loadTexts:
    cqlciscoQpNotifsGroup.setStatus(
        "deprecated"
    )

cqlciscoLbgNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 2)
)
cqlciscoLbgNotifsGroup.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlLbgRouteAdd"),
        ("CISCO-QP-LBG-MIB", "cqlLbgRouteDelete"))
)
if mibBuilder.loadTexts:
    cqlciscoLbgNotifsGroup.setStatus(
        "current"
    )

cqlciscoQpNotifsGroup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 2, 7)
)
cqlciscoQpNotifsGroup1.setObjects(
      *(("CISCO-QP-LBG-MIB", "cqlQpStateChange"),
        ("CISCO-QP-LBG-MIB", "cqlQamAdd"),
        ("CISCO-QP-LBG-MIB", "cqlQamDelete"),
        ("CISCO-QP-LBG-MIB", "cqlQamOverSubscribedAlert"))
)
if mibBuilder.loadTexts:
    cqlciscoQpNotifsGroup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cqlciscoQpLbgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cqlciscoQpLbgCompliance.setStatus(
        "deprecated"
    )

cqlciscoQpLbgCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 824, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cqlciscoQpLbgCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-QP-LBG-MIB",
    **{"ciscoQpLbgMIB": ciscoQpLbgMIB,
       "ciscoQpLbgNotifs": ciscoQpLbgNotifs,
       "cqlQpStateChange": cqlQpStateChange,
       "cqlQamAdd": cqlQamAdd,
       "cqlQamDelete": cqlQamDelete,
       "cqlLbgRouteAdd": cqlLbgRouteAdd,
       "cqlLbgRouteDelete": cqlLbgRouteDelete,
       "cqlQamOverSubscribedAlert": cqlQamOverSubscribedAlert,
       "ciscoQpLbgObjects": ciscoQpLbgObjects,
       "cqlqamPartitionTable": cqlqamPartitionTable,
       "cqlqamPartitionEntry": cqlqamPartitionEntry,
       "cqlqpIndex": cqlqpIndex,
       "cqlqpId": cqlqpId,
       "cqlqpMgmtIpAddrType": cqlqpMgmtIpAddrType,
       "cqlqpMgmtIp": cqlqpMgmtIp,
       "cqlqpServerIpAddrType": cqlqpServerIpAddrType,
       "cqlqpServerIp": cqlqpServerIp,
       "cqlqpState": cqlqpState,
       "cqlqpProtocol": cqlqpProtocol,
       "cqlqpKeepAliveTime": cqlqpKeepAliveTime,
       "cqlqpServerState": cqlqpServerState,
       "cqlqpGqiMacAddr": cqlqpGqiMacAddr,
       "cqlqpGqiResetInterval": cqlqpGqiResetInterval,
       "cqlqpNumQams": cqlqpNumQams,
       "cqlqpQamCarrrierList": cqlqpQamCarrrierList,
       "cqlqpNumRoutes": cqlqpNumRoutes,
       "cqlqpRouteDetails": cqlqpRouteDetails,
       "cqlqpErmiErrpComponentName": cqlqpErmiErrpComponentName,
       "cqlqpErmiErrpStreamingZone": cqlqpErmiErrpStreamingZone,
       "cqlqpErmiErrpHoldTime": cqlqpErmiErrpHoldTime,
       "cqlqpErmiErrpConnnectTime": cqlqpErmiErrpConnnectTime,
       "cqlqpErmiErrpConnectRetry": cqlqpErmiErrpConnectRetry,
       "cqlqpErmiRtspConnectTime": cqlqpErmiRtspConnectTime,
       "cqlqpErmiRtspConnectRetry": cqlqpErmiRtspConnectRetry,
       "cqlqpErmiRtspKeepAliveTime": cqlqpErmiRtspKeepAliveTime,
       "cqlqpErmiRtspSessionTimeout": cqlqpErmiRtspSessionTimeout,
       "cqlqpQamOversubscribedStatus": cqlqpQamOversubscribedStatus,
       "cqlqpServerIpList": cqlqpServerIpList,
       "cqlloadBalanceGroupTable": cqlloadBalanceGroupTable,
       "cqlloadBalanceGroupEntry": cqlloadBalanceGroupEntry,
       "cqllbgIndex": cqllbgIndex,
       "cqllbgTotalBandwidth": cqllbgTotalBandwidth,
       "cqllbgQamRsvBandwidth": cqllbgQamRsvBandwidth,
       "cqllbgIpRsvBandwidth": cqllbgIpRsvBandwidth,
       "cqllbgAvailableBandwidth": cqllbgAvailableBandwidth,
       "cqllbgrouteTable": cqllbgrouteTable,
       "cqllbgrouteEntry": cqllbgrouteEntry,
       "cqllbgRouteIndex": cqllbgRouteIndex,
       "cqllbgQpId": cqllbgQpId,
       "cqllbgDstIpAddrType": cqllbgDstIpAddrType,
       "cqllbgDstIpAddr": cqllbgDstIpAddr,
       "cqllbgUdpPortRangeMin": cqllbgUdpPortRangeMin,
       "cqllbgUdpPortRangeMax": cqllbgUdpPortRangeMax,
       "cqllbgGqiIngressPort": cqllbgGqiIngressPort,
       "cqllbgRsvBandwidth": cqllbgRsvBandwidth,
       "cqllbgAllocatedBandwidth": cqllbgAllocatedBandwidth,
       "cqllbgNumFlows": cqllbgNumFlows,
       "cqlQpNotifyEnable": cqlQpNotifyEnable,
       "cqlQamNotifyEnable": cqlQamNotifyEnable,
       "cqlRouteNotifyEnable": cqlRouteNotifyEnable,
       "cqlQamOverSubscribedEnable": cqlQamOverSubscribedEnable,
       "ciscoQpLbgConform": ciscoQpLbgConform,
       "ciscoQpLbgCompliances": ciscoQpLbgCompliances,
       "cqlciscoQpLbgCompliance": cqlciscoQpLbgCompliance,
       "cqlciscoQpLbgCompliance1": cqlciscoQpLbgCompliance1,
       "ciscoQpLbgGroups": ciscoQpLbgGroups,
       "cqlciscoQpNotifsGroup": cqlciscoQpNotifsGroup,
       "cqlciscoLbgNotifsGroup": cqlciscoLbgNotifsGroup,
       "cqlciscoQpObjectGroup": cqlciscoQpObjectGroup,
       "cqlciscoLbgObjectGroup": cqlciscoLbgObjectGroup,
       "cqlciscoLbgRouteObjectGroup": cqlciscoLbgRouteObjectGroup,
       "cqlciscoQpLbgNotifsControlGroup": cqlciscoQpLbgNotifsControlGroup,
       "cqlciscoQpNotifsGroup1": cqlciscoQpNotifsGroup1,
       "cqlciscoQpObjectGroup1": cqlciscoQpObjectGroup1,
       "cqlciscoQpLbgNotifsControlGroup1": cqlciscoQpLbgNotifsControlGroup1}
)
