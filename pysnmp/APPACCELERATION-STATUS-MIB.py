# SNMP MIB module (APPACCELERATION-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPACCELERATION-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:28 2024
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

(appAccelerationMgmt,
 appAccelerationNotifications) = mibBuilder.importSymbols(
    "APPACCELERATION-SMI",
    "appAccelerationMgmt",
    "appAccelerationNotifications")

(AppAccelerationAlarmSeverity,
 AppAccelerationDescription,
 AppAccelerationSeqNum,
 AppAccelerationYesNo) = mibBuilder.importSymbols(
    "APPACCELERATION-TC",
    "AppAccelerationAlarmSeverity",
    "AppAccelerationDescription",
    "AppAccelerationSeqNum",
    "AppAccelerationYesNo")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

appAccelerationStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsStatusMIBObjects_ObjectIdentity = ObjectIdentity
wsStatusMIBObjects = _WsStatusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1)
)
_WsStatusMIBScalars_ObjectIdentity = ObjectIdentity
wsStatusMIBScalars = _WsStatusMIBScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1)
)


class _WsOperStatus_Type(Integer32):
    """Custom type wsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100,
              101,
              102,
              103)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 100),
          ("bypassTraffic", 103),
          ("down", 101),
          ("licenseExpired", 102))
    )


_WsOperStatus_Type.__name__ = "Integer32"
_WsOperStatus_Object = MibScalar
wsOperStatus = _WsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 1),
    _WsOperStatus_Type()
)
wsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsOperStatus.setStatus("current")
_WsLoad1Min_Type = Integer32
_WsLoad1Min_Object = MibScalar
wsLoad1Min = _WsLoad1Min_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 2),
    _WsLoad1Min_Type()
)
wsLoad1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLoad1Min.setStatus("deprecated")
_WsLoad5Min_Type = Integer32
_WsLoad5Min_Object = MibScalar
wsLoad5Min = _WsLoad5Min_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 3),
    _WsLoad5Min_Type()
)
wsLoad5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLoad5Min.setStatus("deprecated")
_WsLoad15Min_Type = Integer32
_WsLoad15Min_Object = MibScalar
wsLoad15Min = _WsLoad15Min_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 4),
    _WsLoad15Min_Type()
)
wsLoad15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLoad15Min.setStatus("deprecated")


class _WsBypass_Type(Integer32):
    """Custom type wsBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 2),
          ("normal", 1))
    )


_WsBypass_Type.__name__ = "Integer32"
_WsBypass_Object = MibScalar
wsBypass = _WsBypass_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 5),
    _WsBypass_Type()
)
wsBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsBypass.setStatus("current")
_WsLastAlarmSeqNum_Type = AppAccelerationSeqNum
_WsLastAlarmSeqNum_Object = MibScalar
wsLastAlarmSeqNum = _WsLastAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 6),
    _WsLastAlarmSeqNum_Type()
)
wsLastAlarmSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLastAlarmSeqNum.setStatus("current")


class _WsBoostStatus_Type(Integer32):
    """Custom type wsBoostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hardboost", 1),
          ("softboost", 2))
    )


_WsBoostStatus_Type.__name__ = "Integer32"
_WsBoostStatus_Object = MibScalar
wsBoostStatus = _WsBoostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 7),
    _WsBoostStatus_Type()
)
wsBoostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsBoostStatus.setStatus("deprecated")


class _WsBandwidthMode_Type(Integer32):
    """Custom type wsBandwidthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("partial", 2))
    )


_WsBandwidthMode_Type.__name__ = "Integer32"
_WsBandwidthMode_Object = MibScalar
wsBandwidthMode = _WsBandwidthMode_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 8),
    _WsBandwidthMode_Type()
)
wsBandwidthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsBandwidthMode.setStatus("current")
_WsBandwidthLimit_Type = Integer32
_WsBandwidthLimit_Object = MibScalar
wsBandwidthLimit = _WsBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 9),
    _WsBandwidthLimit_Type()
)
wsBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsBandwidthLimit.setStatus("current")
if mibBuilder.loadTexts:
    wsBandwidthLimit.setUnits("K-Bits/sec")
_WsWanOutOctets_Type = Counter64
_WsWanOutOctets_Object = MibScalar
wsWanOutOctets = _WsWanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 10),
    _WsWanOutOctets_Type()
)
wsWanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWanOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsWanOutOctets.setUnits("Octets")
_WsWanInOctets_Type = Counter64
_WsWanInOctets_Object = MibScalar
wsWanInOctets = _WsWanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 11),
    _WsWanInOctets_Type()
)
wsWanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWanInOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsWanInOctets.setUnits("Octets")
_WsLanOutOctets_Type = Counter64
_WsLanOutOctets_Object = MibScalar
wsLanOutOctets = _WsLanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 12),
    _WsLanOutOctets_Type()
)
wsLanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLanOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsLanOutOctets.setUnits("Octets")
_WsLanInOctets_Type = Counter64
_WsLanInOctets_Object = MibScalar
wsLanInOctets = _WsLanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 13),
    _WsLanInOctets_Type()
)
wsLanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLanInOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsLanInOctets.setUnits("Octets")
_WsCompressionEffectiveBandwidth_Type = Integer32
_WsCompressionEffectiveBandwidth_Object = MibScalar
wsCompressionEffectiveBandwidth = _WsCompressionEffectiveBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 14),
    _WsCompressionEffectiveBandwidth_Type()
)
wsCompressionEffectiveBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCompressionEffectiveBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    wsCompressionEffectiveBandwidth.setUnits("K-Bits/sec")
_WsSendCompressionRatio_Type = Integer32
_WsSendCompressionRatio_Object = MibScalar
wsSendCompressionRatio = _WsSendCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 15),
    _WsSendCompressionRatio_Type()
)
wsSendCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSendCompressionRatio.setStatus("current")
_WsReceiveCompressionRatio_Type = Integer32
_WsReceiveCompressionRatio_Object = MibScalar
wsReceiveCompressionRatio = _WsReceiveCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 16),
    _WsReceiveCompressionRatio_Type()
)
wsReceiveCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsReceiveCompressionRatio.setStatus("current")
_WsCompressionStatsCollectionTime_Type = TimeTicks
_WsCompressionStatsCollectionTime_Object = MibScalar
wsCompressionStatsCollectionTime = _WsCompressionStatsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 17),
    _WsCompressionStatsCollectionTime_Type()
)
wsCompressionStatsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCompressionStatsCollectionTime.setStatus("current")
_WsAcceleratedConnections_Type = Integer32
_WsAcceleratedConnections_Object = MibScalar
wsAcceleratedConnections = _WsAcceleratedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 18),
    _WsAcceleratedConnections_Type()
)
wsAcceleratedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAcceleratedConnections.setStatus("current")
_WsNonAcceleratedConnections_Type = Integer32
_WsNonAcceleratedConnections_Object = MibScalar
wsNonAcceleratedConnections = _WsNonAcceleratedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 19),
    _WsNonAcceleratedConnections_Type()
)
wsNonAcceleratedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNonAcceleratedConnections.setStatus("current")


class _WsHaState_Type(Integer32):
    """Custom type wsHaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 5),
          ("primary", 1),
          ("restarting", 3),
          ("secondary", 2),
          ("standalone", 0),
          ("starting", 4))
    )


_WsHaState_Type.__name__ = "Integer32"
_WsHaState_Object = MibScalar
wsHaState = _WsHaState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 20),
    _WsHaState_Type()
)
wsHaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsHaState.setStatus("current")
_WsHaVmIp_Type = IpAddress
_WsHaVmIp_Object = MibScalar
wsHaVmIp = _WsHaVmIp_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 21),
    _WsHaVmIp_Type()
)
wsHaVmIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsHaVmIp.setStatus("current")
_WsHaSecondaryIp_Type = IpAddress
_WsHaSecondaryIp_Object = MibScalar
wsHaSecondaryIp = _WsHaSecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 22),
    _WsHaSecondaryIp_Type()
)
wsHaSecondaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsHaSecondaryIp.setStatus("current")
_WsPrimaryIp_Type = IpAddress
_WsPrimaryIp_Object = MibScalar
wsPrimaryIp = _WsPrimaryIp_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 23),
    _WsPrimaryIp_Type()
)
wsPrimaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsPrimaryIp.setStatus("current")
_WsCpuUsage_Type = Integer32
_WsCpuUsage_Object = MibScalar
wsCpuUsage = _WsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 24),
    _WsCpuUsage_Type()
)
wsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsCpuUsage.setStatus("current")
if mibBuilder.loadTexts:
    wsCpuUsage.setUnits("%")
_WsConnectedPlugIns_Type = Counter32
_WsConnectedPlugIns_Object = MibScalar
wsConnectedPlugIns = _WsConnectedPlugIns_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 25),
    _WsConnectedPlugIns_Type()
)
wsConnectedPlugIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsConnectedPlugIns.setStatus("current")
_WsMaxPlugIns_Type = Integer32
_WsMaxPlugIns_Object = MibScalar
wsMaxPlugIns = _WsMaxPlugIns_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 26),
    _WsMaxPlugIns_Type()
)
wsMaxPlugIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMaxPlugIns.setStatus("current")
_WsQosStatsCollectionTime_Type = TimeTicks
_WsQosStatsCollectionTime_Object = MibScalar
wsQosStatsCollectionTime = _WsQosStatsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 27),
    _WsQosStatsCollectionTime_Type()
)
wsQosStatsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosStatsCollectionTime.setStatus("current")
_WsUpTime_Type = TimeTicks
_WsUpTime_Object = MibScalar
wsUpTime = _WsUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 28),
    _WsUpTime_Type()
)
wsUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsUpTime.setStatus("current")
_WsSerialNumber_Type = DisplayString
_WsSerialNumber_Object = MibScalar
wsSerialNumber = _WsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 29),
    _WsSerialNumber_Type()
)
wsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSerialNumber.setStatus("current")
_WsNonAcceleratedVolume_Type = Counter64
_WsNonAcceleratedVolume_Object = MibScalar
wsNonAcceleratedVolume = _WsNonAcceleratedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 30),
    _WsNonAcceleratedVolume_Type()
)
wsNonAcceleratedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNonAcceleratedVolume.setStatus("current")
if mibBuilder.loadTexts:
    wsNonAcceleratedVolume.setUnits("1000-Octets")
_WsActiveConnections_Type = Integer32
_WsActiveConnections_Object = MibScalar
wsActiveConnections = _WsActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 31),
    _WsActiveConnections_Type()
)
wsActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveConnections.setStatus("current")


class _WsAccelerationStatus_Type(Integer32):
    """Custom type wsAccelerationStatus based on Integer32"""
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


_WsAccelerationStatus_Type.__name__ = "Integer32"
_WsAccelerationStatus_Object = MibScalar
wsAccelerationStatus = _WsAccelerationStatus_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 32),
    _WsAccelerationStatus_Type()
)
wsAccelerationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAccelerationStatus.setStatus("current")


class _WsTrafficShapingStatus_Type(Integer32):
    """Custom type wsTrafficShapingStatus based on Integer32"""
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


_WsTrafficShapingStatus_Type.__name__ = "Integer32"
_WsTrafficShapingStatus_Object = MibScalar
wsTrafficShapingStatus = _WsTrafficShapingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 33),
    _WsTrafficShapingStatus_Type()
)
wsTrafficShapingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsTrafficShapingStatus.setStatus("current")
_WsSystemLoad_Type = Integer32
_WsSystemLoad_Object = MibScalar
wsSystemLoad = _WsSystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 34),
    _WsSystemLoad_Type()
)
wsSystemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsSystemLoad.setStatus("current")
if mibBuilder.loadTexts:
    wsSystemLoad.setUnits("%")
_WsWanSendRate_Type = Integer32
_WsWanSendRate_Object = MibScalar
wsWanSendRate = _WsWanSendRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 35),
    _WsWanSendRate_Type()
)
wsWanSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWanSendRate.setStatus("current")
if mibBuilder.loadTexts:
    wsWanSendRate.setUnits("bps")
_WsWanReceiveRate_Type = Integer32
_WsWanReceiveRate_Object = MibScalar
wsWanReceiveRate = _WsWanReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 36),
    _WsWanReceiveRate_Type()
)
wsWanReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWanReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    wsWanReceiveRate.setUnits("bps")
_WsLanSendRate_Type = Integer32
_WsLanSendRate_Object = MibScalar
wsLanSendRate = _WsLanSendRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 37),
    _WsLanSendRate_Type()
)
wsLanSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLanSendRate.setStatus("current")
if mibBuilder.loadTexts:
    wsLanSendRate.setUnits("bps")
_WsLanReceiveRate_Type = Integer32
_WsLanReceiveRate_Object = MibScalar
wsLanReceiveRate = _WsLanReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 38),
    _WsLanReceiveRate_Type()
)
wsLanReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsLanReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    wsLanReceiveRate.setUnits("bps")
_WsNonAcceleratedRate_Type = Integer32
_WsNonAcceleratedRate_Object = MibScalar
wsNonAcceleratedRate = _WsNonAcceleratedRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 39),
    _WsNonAcceleratedRate_Type()
)
wsNonAcceleratedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsNonAcceleratedRate.setStatus("current")
if mibBuilder.loadTexts:
    wsNonAcceleratedRate.setUnits("bps")
_WsModelNumber_Type = DisplayString
_WsModelNumber_Object = MibScalar
wsModelNumber = _WsModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 40),
    _WsModelNumber_Type()
)
wsModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsModelNumber.setStatus("current")


class _WsWccpStatus_Type(Integer32):
    """Custom type wsWccpStatus based on Integer32"""
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


_WsWccpStatus_Type.__name__ = "Integer32"
_WsWccpStatus_Object = MibScalar
wsWccpStatus = _WsWccpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 1, 41),
    _WsWccpStatus_Type()
)
wsWccpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsWccpStatus.setStatus("current")
_WsStatusMIBTables_ObjectIdentity = ObjectIdentity
wsStatusMIBTables = _WsStatusMIBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2)
)
_WsActiveAlarmTable_Object = MibTable
wsActiveAlarmTable = _WsActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wsActiveAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "wsActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _WsActiveAlarmIndex_Type(Integer32):
    """Custom type wsActiveAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsActiveAlarmIndex_Type.__name__ = "Integer32"
_WsActiveAlarmIndex_Object = MibTableColumn
wsActiveAlarmIndex = _WsActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 1),
    _WsActiveAlarmIndex_Type()
)
wsActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmIndex.setStatus("current")
_WsActiveAlarmSeqNum_Type = AppAccelerationSeqNum
_WsActiveAlarmSeqNum_Object = MibTableColumn
wsActiveAlarmSeqNum = _WsActiveAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 2),
    _WsActiveAlarmSeqNum_Type()
)
wsActiveAlarmSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmSeqNum.setStatus("current")
_WsActiveAlarmID_Type = ObjectIdentifier
_WsActiveAlarmID_Object = MibTableColumn
wsActiveAlarmID = _WsActiveAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 3),
    _WsActiveAlarmID_Type()
)
wsActiveAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmID.setStatus("current")
_WsActiveAlarmSeverity_Type = AppAccelerationAlarmSeverity
_WsActiveAlarmSeverity_Object = MibTableColumn
wsActiveAlarmSeverity = _WsActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 4),
    _WsActiveAlarmSeverity_Type()
)
wsActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmSeverity.setStatus("current")
_WsActiveAlarmLogTime_Type = TimeTicks
_WsActiveAlarmLogTime_Object = MibTableColumn
wsActiveAlarmLogTime = _WsActiveAlarmLogTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 5),
    _WsActiveAlarmLogTime_Type()
)
wsActiveAlarmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmLogTime.setStatus("current")
_WsActiveAlarmDesc_Type = AppAccelerationDescription
_WsActiveAlarmDesc_Object = MibTableColumn
wsActiveAlarmDesc = _WsActiveAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 6),
    _WsActiveAlarmDesc_Type()
)
wsActiveAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmDesc.setStatus("current")
_WsActiveAlarmAcked_Type = AppAccelerationYesNo
_WsActiveAlarmAcked_Object = MibTableColumn
wsActiveAlarmAcked = _WsActiveAlarmAcked_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 7),
    _WsActiveAlarmAcked_Type()
)
wsActiveAlarmAcked.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsActiveAlarmAcked.setStatus("current")
_WsActiveAlarmServiceAffect_Type = AppAccelerationYesNo
_WsActiveAlarmServiceAffect_Object = MibTableColumn
wsActiveAlarmServiceAffect = _WsActiveAlarmServiceAffect_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 1, 1, 8),
    _WsActiveAlarmServiceAffect_Type()
)
wsActiveAlarmServiceAffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsActiveAlarmServiceAffect.setStatus("current")
_WsServiceClassStatsTable_Object = MibTable
wsServiceClassStatsTable = _WsServiceClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wsServiceClassStatsTable.setStatus("current")
_WsServiceClassStatsEntry_Object = MibTableRow
wsServiceClassStatsEntry = _WsServiceClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1)
)
wsServiceClassStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "wsServiceClassIndex"),
)
if mibBuilder.loadTexts:
    wsServiceClassStatsEntry.setStatus("current")


class _WsServiceClassIndex_Type(Integer32):
    """Custom type wsServiceClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WsServiceClassIndex_Type.__name__ = "Integer32"
_WsServiceClassIndex_Object = MibTableColumn
wsServiceClassIndex = _WsServiceClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 1),
    _WsServiceClassIndex_Type()
)
wsServiceClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsServiceClassIndex.setStatus("current")
_WsServiceClassName_Type = DisplayString
_WsServiceClassName_Object = MibTableColumn
wsServiceClassName = _WsServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 2),
    _WsServiceClassName_Type()
)
wsServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsServiceClassName.setStatus("current")
_WsScsCurrentAcceleratedConnections_Type = Integer32
_WsScsCurrentAcceleratedConnections_Object = MibTableColumn
wsScsCurrentAcceleratedConnections = _WsScsCurrentAcceleratedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 3),
    _WsScsCurrentAcceleratedConnections_Type()
)
wsScsCurrentAcceleratedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsCurrentAcceleratedConnections.setStatus("current")
_WsScsTotalAcceleratedConnections_Type = Counter64
_WsScsTotalAcceleratedConnections_Object = MibTableColumn
wsScsTotalAcceleratedConnections = _WsScsTotalAcceleratedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 4),
    _WsScsTotalAcceleratedConnections_Type()
)
wsScsTotalAcceleratedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsTotalAcceleratedConnections.setStatus("current")
_WsScsTotalAcceleratedOctets_Type = Counter64
_WsScsTotalAcceleratedOctets_Object = MibTableColumn
wsScsTotalAcceleratedOctets = _WsScsTotalAcceleratedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 5),
    _WsScsTotalAcceleratedOctets_Type()
)
wsScsTotalAcceleratedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsTotalAcceleratedOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsTotalAcceleratedOctets.setUnits("Octets")
_WsScsTotalNonAcceleratedConnections_Type = Counter64
_WsScsTotalNonAcceleratedConnections_Object = MibTableColumn
wsScsTotalNonAcceleratedConnections = _WsScsTotalNonAcceleratedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 6),
    _WsScsTotalNonAcceleratedConnections_Type()
)
wsScsTotalNonAcceleratedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsTotalNonAcceleratedConnections.setStatus("current")
_WsScsTotalNonAcceleratedOctets_Type = Counter64
_WsScsTotalNonAcceleratedOctets_Object = MibTableColumn
wsScsTotalNonAcceleratedOctets = _WsScsTotalNonAcceleratedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 7),
    _WsScsTotalNonAcceleratedOctets_Type()
)
wsScsTotalNonAcceleratedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsTotalNonAcceleratedOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsTotalNonAcceleratedOctets.setUnits("Octets")
_WsScsTotalPreCompressionOctets_Type = Counter64
_WsScsTotalPreCompressionOctets_Object = MibTableColumn
wsScsTotalPreCompressionOctets = _WsScsTotalPreCompressionOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 8),
    _WsScsTotalPreCompressionOctets_Type()
)
wsScsTotalPreCompressionOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsTotalPreCompressionOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsTotalPreCompressionOctets.setUnits("Octets")
_WsScsCompressSentOctets_Type = Counter64
_WsScsCompressSentOctets_Object = MibTableColumn
wsScsCompressSentOctets = _WsScsCompressSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 9),
    _WsScsCompressSentOctets_Type()
)
wsScsCompressSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsCompressSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsCompressSentOctets.setUnits("Octets")
_WsScsCompressReceivedOctets_Type = Counter64
_WsScsCompressReceivedOctets_Object = MibTableColumn
wsScsCompressReceivedOctets = _WsScsCompressReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 10),
    _WsScsCompressReceivedOctets_Type()
)
wsScsCompressReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsCompressReceivedOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsCompressReceivedOctets.setUnits("Octets")
_WsScsPreCompressSentOctets_Type = Counter64
_WsScsPreCompressSentOctets_Object = MibTableColumn
wsScsPreCompressSentOctets = _WsScsPreCompressSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 11),
    _WsScsPreCompressSentOctets_Type()
)
wsScsPreCompressSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsPreCompressSentOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsPreCompressSentOctets.setUnits("Octets")
_WsScsPreCompressReceivedOctets_Type = Counter64
_WsScsPreCompressReceivedOctets_Object = MibTableColumn
wsScsPreCompressReceivedOctets = _WsScsPreCompressReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 12),
    _WsScsPreCompressReceivedOctets_Type()
)
wsScsPreCompressReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsPreCompressReceivedOctets.setStatus("current")
if mibBuilder.loadTexts:
    wsScsPreCompressReceivedOctets.setUnits("Octets")
_WsScsSendBWSavings_Type = Integer32
_WsScsSendBWSavings_Object = MibTableColumn
wsScsSendBWSavings = _WsScsSendBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 13),
    _WsScsSendBWSavings_Type()
)
wsScsSendBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsSendBWSavings.setStatus("current")
if mibBuilder.loadTexts:
    wsScsSendBWSavings.setUnits("%")
_WsScsRecvBWSavings_Type = Integer32
_WsScsRecvBWSavings_Object = MibTableColumn
wsScsRecvBWSavings = _WsScsRecvBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 14),
    _WsScsRecvBWSavings_Type()
)
wsScsRecvBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsRecvBWSavings.setStatus("current")
if mibBuilder.loadTexts:
    wsScsRecvBWSavings.setUnits("%")
_WsScsSendRecvBWSavings_Type = Integer32
_WsScsSendRecvBWSavings_Object = MibTableColumn
wsScsSendRecvBWSavings = _WsScsSendRecvBWSavings_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 15),
    _WsScsSendRecvBWSavings_Type()
)
wsScsSendRecvBWSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsSendRecvBWSavings.setStatus("current")
if mibBuilder.loadTexts:
    wsScsSendRecvBWSavings.setUnits("%")
_WsScsSendCompressionRatio_Type = Integer32
_WsScsSendCompressionRatio_Object = MibTableColumn
wsScsSendCompressionRatio = _WsScsSendCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 16),
    _WsScsSendCompressionRatio_Type()
)
wsScsSendCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsSendCompressionRatio.setStatus("current")
_WsScsRecvCompressionRatio_Type = Integer32
_WsScsRecvCompressionRatio_Object = MibTableColumn
wsScsRecvCompressionRatio = _WsScsRecvCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 17),
    _WsScsRecvCompressionRatio_Type()
)
wsScsRecvCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsRecvCompressionRatio.setStatus("current")
_WsScsSendRecvCompressionRatio_Type = Integer32
_WsScsSendRecvCompressionRatio_Object = MibTableColumn
wsScsSendRecvCompressionRatio = _WsScsSendRecvCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 2, 1, 18),
    _WsScsSendRecvCompressionRatio_Type()
)
wsScsSendRecvCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsScsSendRecvCompressionRatio.setStatus("current")
_WsQosTrafficClassStatsTable_Object = MibTable
wsQosTrafficClassStatsTable = _WsQosTrafficClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wsQosTrafficClassStatsTable.setStatus("deprecated")
_WsQosTcStatsEntry_Object = MibTableRow
wsQosTcStatsEntry = _WsQosTcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1)
)
wsQosTcStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "wsQosIndex"),
)
if mibBuilder.loadTexts:
    wsQosTcStatsEntry.setStatus("deprecated")


class _WsQosIndex_Type(Integer32):
    """Custom type wsQosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WsQosIndex_Type.__name__ = "Integer32"
_WsQosIndex_Object = MibTableColumn
wsQosIndex = _WsQosIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1, 1),
    _WsQosIndex_Type()
)
wsQosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosIndex.setStatus("deprecated")
_WsQosName_Type = DisplayString
_WsQosName_Object = MibTableColumn
wsQosName = _WsQosName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1, 2),
    _WsQosName_Type()
)
wsQosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosName.setStatus("deprecated")
_WsQosConfiguredSendRatio_Type = Integer32
_WsQosConfiguredSendRatio_Object = MibTableColumn
wsQosConfiguredSendRatio = _WsQosConfiguredSendRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1, 3),
    _WsQosConfiguredSendRatio_Type()
)
wsQosConfiguredSendRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosConfiguredSendRatio.setStatus("deprecated")
if mibBuilder.loadTexts:
    wsQosConfiguredSendRatio.setUnits("%")
_WsQosSentVolume_Type = Counter64
_WsQosSentVolume_Object = MibTableColumn
wsQosSentVolume = _WsQosSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1, 4),
    _WsQosSentVolume_Type()
)
wsQosSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosSentVolume.setStatus("deprecated")
if mibBuilder.loadTexts:
    wsQosSentVolume.setUnits("K-octets")
_WsQosActualSendRatio_Type = Integer32
_WsQosActualSendRatio_Object = MibTableColumn
wsQosActualSendRatio = _WsQosActualSendRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 3, 1, 5),
    _WsQosActualSendRatio_Type()
)
wsQosActualSendRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsQosActualSendRatio.setStatus("deprecated")
if mibBuilder.loadTexts:
    wsQosActualSendRatio.setUnits("%")
_WsIcaStatsTable_Object = MibTable
wsIcaStatsTable = _WsIcaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wsIcaStatsTable.setStatus("current")
_WsIcaStatsEntry_Object = MibTableRow
wsIcaStatsEntry = _WsIcaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1)
)
wsIcaStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "wsIcaIndex"),
)
if mibBuilder.loadTexts:
    wsIcaStatsEntry.setStatus("current")


class _WsIcaIndex_Type(Integer32):
    """Custom type wsIcaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WsIcaIndex_Type.__name__ = "Integer32"
_WsIcaIndex_Object = MibTableColumn
wsIcaIndex = _WsIcaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 1),
    _WsIcaIndex_Type()
)
wsIcaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaIndex.setStatus("current")
_WsIcaServiceName_Type = DisplayString
_WsIcaServiceName_Object = MibTableColumn
wsIcaServiceName = _WsIcaServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 2),
    _WsIcaServiceName_Type()
)
wsIcaServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaServiceName.setStatus("current")


class _WsIcaPriority_Type(Integer32):
    """Custom type wsIcaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("background", 3),
          ("high", 0),
          ("low", 2),
          ("medium", 1),
          ("notApplicable", 9999))
    )


_WsIcaPriority_Type.__name__ = "Integer32"
_WsIcaPriority_Object = MibTableColumn
wsIcaPriority = _WsIcaPriority_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 3),
    _WsIcaPriority_Type()
)
wsIcaPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaPriority.setStatus("deprecated")
_WsIcaSentVolume_Type = Counter64
_WsIcaSentVolume_Object = MibTableColumn
wsIcaSentVolume = _WsIcaSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 4),
    _WsIcaSentVolume_Type()
)
wsIcaSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaSentVolume.setUnits("K-octets")
_WsIcaSentRatio_Type = Integer32
_WsIcaSentRatio_Object = MibTableColumn
wsIcaSentRatio = _WsIcaSentRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 5),
    _WsIcaSentRatio_Type()
)
wsIcaSentRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaSentRatio.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaSentRatio.setUnits("%")
_WsIcaReceivedVolume_Type = Counter64
_WsIcaReceivedVolume_Object = MibTableColumn
wsIcaReceivedVolume = _WsIcaReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 6),
    _WsIcaReceivedVolume_Type()
)
wsIcaReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaReceivedVolume.setUnits("K-octets")
_WsIcaReceivedRatio_Type = Integer32
_WsIcaReceivedRatio_Object = MibTableColumn
wsIcaReceivedRatio = _WsIcaReceivedRatio_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 7),
    _WsIcaReceivedRatio_Type()
)
wsIcaReceivedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaReceivedRatio.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaReceivedRatio.setUnits("%")
_WsIcaSendRate_Type = Integer32
_WsIcaSendRate_Object = MibTableColumn
wsIcaSendRate = _WsIcaSendRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 8),
    _WsIcaSendRate_Type()
)
wsIcaSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaSendRate.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaSendRate.setUnits("bps")
_WsIcaReceiveRate_Type = Integer32
_WsIcaReceiveRate_Object = MibTableColumn
wsIcaReceiveRate = _WsIcaReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 4, 1, 9),
    _WsIcaReceiveRate_Type()
)
wsIcaReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsIcaReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    wsIcaReceiveRate.setUnits("bps")
_WsAdapterTable_Object = MibTable
wsAdapterTable = _WsAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wsAdapterTable.setStatus("current")
_WsAdapterEntry_Object = MibTableRow
wsAdapterEntry = _WsAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1)
)
wsAdapterEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "wsAdapterIndex"),
)
if mibBuilder.loadTexts:
    wsAdapterEntry.setStatus("current")


class _WsAdapterIndex_Type(Integer32):
    """Custom type wsAdapterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WsAdapterIndex_Type.__name__ = "Integer32"
_WsAdapterIndex_Object = MibTableColumn
wsAdapterIndex = _WsAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 1),
    _WsAdapterIndex_Type()
)
wsAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterIndex.setStatus("current")
_WsAdapterName_Type = DisplayString
_WsAdapterName_Object = MibTableColumn
wsAdapterName = _WsAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 2),
    _WsAdapterName_Type()
)
wsAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterName.setStatus("current")


class _WsAdapterEnabled_Type(Integer32):
    """Custom type wsAdapterEnabled based on Integer32"""
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


_WsAdapterEnabled_Type.__name__ = "Integer32"
_WsAdapterEnabled_Object = MibTableColumn
wsAdapterEnabled = _WsAdapterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 3),
    _WsAdapterEnabled_Type()
)
wsAdapterEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterEnabled.setStatus("current")
_WsAdapterIp_Type = IpAddress
_WsAdapterIp_Object = MibTableColumn
wsAdapterIp = _WsAdapterIp_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 4),
    _WsAdapterIp_Type()
)
wsAdapterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterIp.setStatus("current")
_WsAdapterNetmask_Type = IpAddress
_WsAdapterNetmask_Object = MibTableColumn
wsAdapterNetmask = _WsAdapterNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 5),
    _WsAdapterNetmask_Type()
)
wsAdapterNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterNetmask.setStatus("current")
_WsAdapterGateway_Type = IpAddress
_WsAdapterGateway_Object = MibTableColumn
wsAdapterGateway = _WsAdapterGateway_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 6),
    _WsAdapterGateway_Type()
)
wsAdapterGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterGateway.setStatus("current")
_WsAdapterVirtualIp_Type = IpAddress
_WsAdapterVirtualIp_Object = MibTableColumn
wsAdapterVirtualIp = _WsAdapterVirtualIp_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 7),
    _WsAdapterVirtualIp_Type()
)
wsAdapterVirtualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterVirtualIp.setStatus("current")


class _WsAdapterVLanEnabled_Type(Integer32):
    """Custom type wsAdapterVLanEnabled based on Integer32"""
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


_WsAdapterVLanEnabled_Type.__name__ = "Integer32"
_WsAdapterVLanEnabled_Object = MibTableColumn
wsAdapterVLanEnabled = _WsAdapterVLanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 8),
    _WsAdapterVLanEnabled_Type()
)
wsAdapterVLanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterVLanEnabled.setStatus("current")
_WsAdapterVLanGroup_Type = Integer32
_WsAdapterVLanGroup_Object = MibTableColumn
wsAdapterVLanGroup = _WsAdapterVLanGroup_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 5, 1, 9),
    _WsAdapterVLanGroup_Type()
)
wsAdapterVLanGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAdapterVLanGroup.setStatus("current")
_WsLinkStatsTable_Object = MibTable
wsLinkStatsTable = _WsLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    wsLinkStatsTable.setStatus("current")
_LinkStatsEntry_Object = MibTableRow
linkStatsEntry = _LinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1)
)
linkStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "linkIndex"),
)
if mibBuilder.loadTexts:
    linkStatsEntry.setStatus("current")


class _LinkIndex_Type(Integer32):
    """Custom type linkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LinkIndex_Type.__name__ = "Integer32"
_LinkIndex_Object = MibTableColumn
linkIndex = _LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 1),
    _LinkIndex_Type()
)
linkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIndex.setStatus("current")
_LinkName_Type = DisplayString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 2),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("current")
_LinkSentVolume_Type = Counter64
_LinkSentVolume_Object = MibTableColumn
linkSentVolume = _LinkSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 3),
    _LinkSentVolume_Type()
)
linkSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkSentVolume.setUnits("K-octets")
_LinkReceivedVolume_Type = Counter64
_LinkReceivedVolume_Object = MibTableColumn
linkReceivedVolume = _LinkReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 4),
    _LinkReceivedVolume_Type()
)
linkReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkReceivedVolume.setUnits("K-octets")
_LinkSentPackets_Type = Counter64
_LinkSentPackets_Object = MibTableColumn
linkSentPackets = _LinkSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 5),
    _LinkSentPackets_Type()
)
linkSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkSentPackets.setUnits("Packets")
_LinkReceivedPackets_Type = Counter64
_LinkReceivedPackets_Object = MibTableColumn
linkReceivedPackets = _LinkReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 6),
    _LinkReceivedPackets_Type()
)
linkReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkReceivedPackets.setUnits("Packets")
_LinkDroppedSentVolume_Type = Counter64
_LinkDroppedSentVolume_Object = MibTableColumn
linkDroppedSentVolume = _LinkDroppedSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 7),
    _LinkDroppedSentVolume_Type()
)
linkDroppedSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDroppedSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkDroppedSentVolume.setUnits("K-octets")
_LinkDroppedReceivedVolume_Type = Counter64
_LinkDroppedReceivedVolume_Object = MibTableColumn
linkDroppedReceivedVolume = _LinkDroppedReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 8),
    _LinkDroppedReceivedVolume_Type()
)
linkDroppedReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDroppedReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    linkDroppedReceivedVolume.setUnits("K-octets")
_LinkDroppedSentPackets_Type = Counter64
_LinkDroppedSentPackets_Object = MibTableColumn
linkDroppedSentPackets = _LinkDroppedSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 9),
    _LinkDroppedSentPackets_Type()
)
linkDroppedSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDroppedSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkDroppedSentPackets.setUnits("Packets")
_LinkDroppedReceivedPackets_Type = Counter64
_LinkDroppedReceivedPackets_Object = MibTableColumn
linkDroppedReceivedPackets = _LinkDroppedReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 6, 1, 10),
    _LinkDroppedReceivedPackets_Type()
)
linkDroppedReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDroppedReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    linkDroppedReceivedPackets.setUnits("Packets")
_WsAppStatsTable_Object = MibTable
wsAppStatsTable = _WsAppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    wsAppStatsTable.setStatus("current")
_AppStatsEntry_Object = MibTableRow
appStatsEntry = _AppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1)
)
appStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "appIndex"),
)
if mibBuilder.loadTexts:
    appStatsEntry.setStatus("current")


class _AppIndex_Type(Integer32):
    """Custom type appIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AppIndex_Type.__name__ = "Integer32"
_AppIndex_Object = MibTableColumn
appIndex = _AppIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 1),
    _AppIndex_Type()
)
appIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appIndex.setStatus("current")
_AppName_Type = DisplayString
_AppName_Object = MibTableColumn
appName = _AppName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 2),
    _AppName_Type()
)
appName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appName.setStatus("current")
_AppId_Type = Integer32
_AppId_Object = MibTableColumn
appId = _AppId_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 3),
    _AppId_Type()
)
appId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appId.setStatus("current")
_AppParentId_Type = Integer32
_AppParentId_Object = MibTableColumn
appParentId = _AppParentId_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 4),
    _AppParentId_Type()
)
appParentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appParentId.setStatus("current")
_AppGroupId_Type = Integer32
_AppGroupId_Object = MibTableColumn
appGroupId = _AppGroupId_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 5),
    _AppGroupId_Type()
)
appGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appGroupId.setStatus("current")
_AppSentVolume_Type = Counter64
_AppSentVolume_Object = MibTableColumn
appSentVolume = _AppSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 6),
    _AppSentVolume_Type()
)
appSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    appSentVolume.setUnits("K-octets")
_AppReceivedVolume_Type = Counter64
_AppReceivedVolume_Object = MibTableColumn
appReceivedVolume = _AppReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 7),
    _AppReceivedVolume_Type()
)
appReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    appReceivedVolume.setUnits("K-octets")
_AppSentPackets_Type = Counter64
_AppSentPackets_Object = MibTableColumn
appSentPackets = _AppSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 8),
    _AppSentPackets_Type()
)
appSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    appSentPackets.setUnits("Packets")
_AppReceivedPackets_Type = Counter64
_AppReceivedPackets_Object = MibTableColumn
appReceivedPackets = _AppReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 9),
    _AppReceivedPackets_Type()
)
appReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    appReceivedPackets.setUnits("Packets")
_AppDroppedSentVolume_Type = Counter64
_AppDroppedSentVolume_Object = MibTableColumn
appDroppedSentVolume = _AppDroppedSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 10),
    _AppDroppedSentVolume_Type()
)
appDroppedSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDroppedSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    appDroppedSentVolume.setUnits("K-octets")
_AppDroppedReceiveVolume_Type = Counter64
_AppDroppedReceiveVolume_Object = MibTableColumn
appDroppedReceiveVolume = _AppDroppedReceiveVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 11),
    _AppDroppedReceiveVolume_Type()
)
appDroppedReceiveVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDroppedReceiveVolume.setStatus("current")
if mibBuilder.loadTexts:
    appDroppedReceiveVolume.setUnits("K-octets")
_AppDroppedSentPackets_Type = Counter64
_AppDroppedSentPackets_Object = MibTableColumn
appDroppedSentPackets = _AppDroppedSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 12),
    _AppDroppedSentPackets_Type()
)
appDroppedSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDroppedSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    appDroppedSentPackets.setUnits("Packets")
_AppDroppedReceivedPackets_Type = Counter64
_AppDroppedReceivedPackets_Object = MibTableColumn
appDroppedReceivedPackets = _AppDroppedReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 13),
    _AppDroppedReceivedPackets_Type()
)
appDroppedReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appDroppedReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    appDroppedReceivedPackets.setUnits("Packets")
_AppSendRate_Type = Integer32
_AppSendRate_Object = MibTableColumn
appSendRate = _AppSendRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 14),
    _AppSendRate_Type()
)
appSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appSendRate.setStatus("current")
if mibBuilder.loadTexts:
    appSendRate.setUnits("bps")
_AppReceiveRate_Type = Integer32
_AppReceiveRate_Object = MibTableColumn
appReceiveRate = _AppReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 7, 1, 15),
    _AppReceiveRate_Type()
)
appReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    appReceiveRate.setUnits("bps")
_WsQosStatsTable_Object = MibTable
wsQosStatsTable = _WsQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    wsQosStatsTable.setStatus("current")
_QosStatsEntry_Object = MibTableRow
qosStatsEntry = _QosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1)
)
qosStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "qosIndex"),
)
if mibBuilder.loadTexts:
    qosStatsEntry.setStatus("current")


class _QosIndex_Type(Integer32):
    """Custom type qosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QosIndex_Type.__name__ = "Integer32"
_QosIndex_Object = MibTableColumn
qosIndex = _QosIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 1),
    _QosIndex_Type()
)
qosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosIndex.setStatus("current")
_QosPolicyName_Type = DisplayString
_QosPolicyName_Object = MibTableColumn
qosPolicyName = _QosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 2),
    _QosPolicyName_Type()
)
qosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPolicyName.setStatus("current")
_QosLink_Type = DisplayString
_QosLink_Object = MibTableColumn
qosLink = _QosLink_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 3),
    _QosLink_Type()
)
qosLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLink.setStatus("current")
_QosSentVolume_Type = Counter64
_QosSentVolume_Object = MibTableColumn
qosSentVolume = _QosSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 4),
    _QosSentVolume_Type()
)
qosSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    qosSentVolume.setUnits("K-octets")
_QosReceiveVolume_Type = Counter64
_QosReceiveVolume_Object = MibTableColumn
qosReceiveVolume = _QosReceiveVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 5),
    _QosReceiveVolume_Type()
)
qosReceiveVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosReceiveVolume.setStatus("current")
if mibBuilder.loadTexts:
    qosReceiveVolume.setUnits("K-octets")
_QosSentPackets_Type = Counter64
_QosSentPackets_Object = MibTableColumn
qosSentPackets = _QosSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 6),
    _QosSentPackets_Type()
)
qosSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    qosSentPackets.setUnits("Packets")
_QosReceivedPackets_Type = Counter64
_QosReceivedPackets_Object = MibTableColumn
qosReceivedPackets = _QosReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 7),
    _QosReceivedPackets_Type()
)
qosReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    qosReceivedPackets.setUnits("Packets")
_QosDroppedSentVolume_Type = Counter64
_QosDroppedSentVolume_Object = MibTableColumn
qosDroppedSentVolume = _QosDroppedSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 8),
    _QosDroppedSentVolume_Type()
)
qosDroppedSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDroppedSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    qosDroppedSentVolume.setUnits("K-octets")
_QosDroppedReceiveVolume_Type = Counter64
_QosDroppedReceiveVolume_Object = MibTableColumn
qosDroppedReceiveVolume = _QosDroppedReceiveVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 9),
    _QosDroppedReceiveVolume_Type()
)
qosDroppedReceiveVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDroppedReceiveVolume.setStatus("current")
if mibBuilder.loadTexts:
    qosDroppedReceiveVolume.setUnits("K-octets")
_QosDroppedSentPackets_Type = Counter64
_QosDroppedSentPackets_Object = MibTableColumn
qosDroppedSentPackets = _QosDroppedSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 10),
    _QosDroppedSentPackets_Type()
)
qosDroppedSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDroppedSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    qosDroppedSentPackets.setUnits("Packets")
_QosDroppedReceivedPackets_Type = Counter64
_QosDroppedReceivedPackets_Object = MibTableColumn
qosDroppedReceivedPackets = _QosDroppedReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 8, 1, 11),
    _QosDroppedReceivedPackets_Type()
)
qosDroppedReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosDroppedReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    qosDroppedReceivedPackets.setUnits("Packets")
_WsLscStatsTable_Object = MibTable
wsLscStatsTable = _WsLscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    wsLscStatsTable.setStatus("current")
_LscStatsEntry_Object = MibTableRow
lscStatsEntry = _LscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1)
)
lscStatsEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "lscIndex"),
)
if mibBuilder.loadTexts:
    lscStatsEntry.setStatus("current")


class _LscIndex_Type(Integer32):
    """Custom type lscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LscIndex_Type.__name__ = "Integer32"
_LscIndex_Object = MibTableColumn
lscIndex = _LscIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 1),
    _LscIndex_Type()
)
lscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscIndex.setStatus("current")
_LscServiceClassName_Type = DisplayString
_LscServiceClassName_Object = MibTableColumn
lscServiceClassName = _LscServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 2),
    _LscServiceClassName_Type()
)
lscServiceClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscServiceClassName.setStatus("current")
_LscLink_Type = DisplayString
_LscLink_Object = MibTableColumn
lscLink = _LscLink_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 3),
    _LscLink_Type()
)
lscLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscLink.setStatus("current")
_LscSentVolume_Type = Counter64
_LscSentVolume_Object = MibTableColumn
lscSentVolume = _LscSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 4),
    _LscSentVolume_Type()
)
lscSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    lscSentVolume.setUnits("K-octets")
_LscReceivedVolume_Type = Counter64
_LscReceivedVolume_Object = MibTableColumn
lscReceivedVolume = _LscReceivedVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 5),
    _LscReceivedVolume_Type()
)
lscReceivedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscReceivedVolume.setStatus("current")
if mibBuilder.loadTexts:
    lscReceivedVolume.setUnits("K-octets")
_LscSentPackets_Type = Counter64
_LscSentPackets_Object = MibTableColumn
lscSentPackets = _LscSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 6),
    _LscSentPackets_Type()
)
lscSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    lscSentPackets.setUnits("Packets")
_LscReceivedPackets_Type = Counter64
_LscReceivedPackets_Object = MibTableColumn
lscReceivedPackets = _LscReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 7),
    _LscReceivedPackets_Type()
)
lscReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    lscReceivedPackets.setUnits("Packets")
_LscDroppedSentVolume_Type = Counter64
_LscDroppedSentVolume_Object = MibTableColumn
lscDroppedSentVolume = _LscDroppedSentVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 8),
    _LscDroppedSentVolume_Type()
)
lscDroppedSentVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscDroppedSentVolume.setStatus("current")
if mibBuilder.loadTexts:
    lscDroppedSentVolume.setUnits("K-octets")
_LscDroppedReceiveVolume_Type = Counter64
_LscDroppedReceiveVolume_Object = MibTableColumn
lscDroppedReceiveVolume = _LscDroppedReceiveVolume_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 9),
    _LscDroppedReceiveVolume_Type()
)
lscDroppedReceiveVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscDroppedReceiveVolume.setStatus("current")
if mibBuilder.loadTexts:
    lscDroppedReceiveVolume.setUnits("K-octets")
_LscDroppedSentPackets_Type = Counter64
_LscDroppedSentPackets_Object = MibTableColumn
lscDroppedSentPackets = _LscDroppedSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 10),
    _LscDroppedSentPackets_Type()
)
lscDroppedSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscDroppedSentPackets.setStatus("current")
if mibBuilder.loadTexts:
    lscDroppedSentPackets.setUnits("Packets")
_LscDroppedReceivedPackets_Type = Counter64
_LscDroppedReceivedPackets_Object = MibTableColumn
lscDroppedReceivedPackets = _LscDroppedReceivedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 9, 1, 11),
    _LscDroppedReceivedPackets_Type()
)
lscDroppedReceivedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lscDroppedReceivedPackets.setStatus("current")
if mibBuilder.loadTexts:
    lscDroppedReceivedPackets.setUnits("Packets")
_WsPartnerTable_Object = MibTable
wsPartnerTable = _WsPartnerTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    wsPartnerTable.setStatus("current")
_PartnerEntry_Object = MibTableRow
partnerEntry = _PartnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1)
)
partnerEntry.setIndexNames(
    (0, "APPACCELERATION-STATUS-MIB", "partnerAddrType"),
    (0, "APPACCELERATION-STATUS-MIB", "partnerAddr"),
)
if mibBuilder.loadTexts:
    partnerEntry.setStatus("current")
_PartnerAddrType_Type = InetAddressType
_PartnerAddrType_Object = MibTableColumn
partnerAddrType = _PartnerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 1),
    _PartnerAddrType_Type()
)
partnerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerAddrType.setStatus("current")
_PartnerAddr_Type = InetAddress
_PartnerAddr_Object = MibTableColumn
partnerAddr = _PartnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 2),
    _PartnerAddr_Type()
)
partnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerAddr.setStatus("current")
_PartnerConnections_Type = Integer32
_PartnerConnections_Object = MibTableColumn
partnerConnections = _PartnerConnections_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 3),
    _PartnerConnections_Type()
)
partnerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerConnections.setStatus("current")
_PartnerSendRate_Type = Integer32
_PartnerSendRate_Object = MibTableColumn
partnerSendRate = _PartnerSendRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 4),
    _PartnerSendRate_Type()
)
partnerSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerSendRate.setStatus("current")
if mibBuilder.loadTexts:
    partnerSendRate.setUnits("bps")
_PartnerReceiveRate_Type = Integer32
_PartnerReceiveRate_Object = MibTableColumn
partnerReceiveRate = _PartnerReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 5),
    _PartnerReceiveRate_Type()
)
partnerReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerReceiveRate.setStatus("current")
if mibBuilder.loadTexts:
    partnerReceiveRate.setUnits("bps")
_PartnerIdleTime_Type = TimeTicks
_PartnerIdleTime_Object = MibTableColumn
partnerIdleTime = _PartnerIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 2, 10, 1, 6),
    _PartnerIdleTime_Type()
)
partnerIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnerIdleTime.setStatus("current")
_WsHAMasterIpAddr_Type = IpAddress
_WsHAMasterIpAddr_Object = MibScalar
wsHAMasterIpAddr = _WsHAMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 3),
    _WsHAMasterIpAddr_Type()
)
wsHAMasterIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsHAMasterIpAddr.setStatus("current")
_WsStatusMIBAlertTables_ObjectIdentity = ObjectIdentity
wsStatusMIBAlertTables = _WsStatusMIBAlertTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 4)
)


class _WsAlertAction_Type(Integer32):
    """Custom type wsAlertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expired", 3),
          ("oneShot", 0),
          ("reset", 2),
          ("set", 1))
    )


_WsAlertAction_Type.__name__ = "Integer32"
_WsAlertAction_Object = MibScalar
wsAlertAction = _WsAlertAction_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 4, 1),
    _WsAlertAction_Type()
)
wsAlertAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlertAction.setStatus("current")


class _WsAlertClass_Type(Integer32):
    """Custom type wsAlertClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75)
        )
    )
    namedValues = NamedValues(
        *(("applianceInTheMiddle", 40),
          ("arpTimeout", 6),
          ("asymmetric", 9),
          ("badHardware", 75),
          ("badLicense", 7),
          ("badPackets", 10),
          ("bwTypeMismatch", 22),
          ("compressionError", 21),
          ("connectionInvalid", 4),
          ("connectionStalled", 2),
          ("connectionTimeout", 3),
          ("cpuPegged", 23),
          ("diskDriveDegraded", 30),
          ("diskDriveFailed", 31),
          ("diskDriveFailing", 29),
          ("diskFragmented", 35),
          ("dnsLookup", 38),
          ("driverHung", 48),
          ("ethernetCrcError", 72),
          ("excessiveIpFragments", 65),
          ("fastLossRate", 1),
          ("groupModeError", 32),
          ("haConfigurationChanged", 16),
          ("haDispositionError", 53),
          ("haMisMatchVmip", 34),
          ("haNoSecondary", 17),
          ("haNotCapable", 19),
          ("haPairCommError", 18),
          ("haPeerKeyStoreLocked", 58),
          ("haPeerVersion", 20),
          ("haVIPNotSet", 54),
          ("internal", 13),
          ("internalCritical", 41),
          ("internalMajor", 42),
          ("internalMinor", 43),
          ("internalWarning", 44),
          ("invalidBridgeConfig", 68),
          ("invalidGateway", 57),
          ("invalidHttpCachingConfigFile", 69),
          ("limitExceeded", 8),
          ("lowOnCpu", 11),
          ("lowOnMemory", 12),
          ("lowOnVm", 24),
          ("mapiNtlmError", 71),
          ("maxUnacceleratedConnectionsExceeded", 74),
          ("nicBypassEvent", 33),
          ("nicHalfDuplex", 5),
          ("numBootoutsExceeded", 27),
          ("numFastRtosExceeded", 26),
          ("numRewindsExceeded", 28),
          ("numSlowRtosExceeded", 25),
          ("plugInNearLimit", 51),
          ("qosEngineError", 70),
          ("qosLinkConfigError", 73),
          ("redirectorModeFailure", 39),
          ("redirectorModeSyn", 36),
          ("restartRequired", 14),
          ("scpsError", 50),
          ("signalingChannelError", 49),
          ("slowLossRate", 0),
          ("smb2AccelerationFailure", 67),
          ("sslError", 52),
          ("sslProxyMajor", 59),
          ("sslProxyMinor", 60),
          ("sslProxyWarning", 61),
          ("sslTunnelMajor", 62),
          ("sslTunnelMinor", 63),
          ("sslTunnelWarning", 64),
          ("tooManyBadTcpChecksum", 56),
          ("unreachable", 37),
          ("userAccountLocked", 66),
          ("vlanNotSupported", 55),
          ("vridNotSet", 15),
          ("wccpMajor", 45),
          ("wccpMinor", 46),
          ("wccpWarning", 47))
    )


_WsAlertClass_Type.__name__ = "Integer32"
_WsAlertClass_Object = MibScalar
wsAlertClass = _WsAlertClass_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 4, 2),
    _WsAlertClass_Type()
)
wsAlertClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlertClass.setStatus("current")
_WsAlertMsg_Type = AppAccelerationDescription
_WsAlertMsg_Object = MibScalar
wsAlertMsg = _WsAlertMsg_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 4, 3),
    _WsAlertMsg_Type()
)
wsAlertMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsAlertMsg.setStatus("current")
_WsSourceIpAddr_Type = IpAddress
_WsSourceIpAddr_Object = MibScalar
wsSourceIpAddr = _WsSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 1, 5),
    _WsSourceIpAddr_Type()
)
wsSourceIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wsSourceIpAddr.setStatus("current")
_WsStatusMIBConformance_ObjectIdentity = ObjectIdentity
wsStatusMIBConformance = _WsStatusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2)
)
_WsStatusMIBCompliances_ObjectIdentity = ObjectIdentity
wsStatusMIBCompliances = _WsStatusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 1)
)
_WsStatusMIBGroups_ObjectIdentity = ObjectIdentity
wsStatusMIBGroups = _WsStatusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 2)
)
_WsStatusMIBNotifications_ObjectIdentity = ObjectIdentity
wsStatusMIBNotifications = _WsStatusMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1)
)

# Managed Objects groups

wsStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 2, 1)
)
wsStatusGroup.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsOperStatus"),
        ("APPACCELERATION-STATUS-MIB", "wsLoad1Min"),
        ("APPACCELERATION-STATUS-MIB", "wsLoad5Min"),
        ("APPACCELERATION-STATUS-MIB", "wsLoad15Min"),
        ("APPACCELERATION-STATUS-MIB", "wsBypass"),
        ("APPACCELERATION-STATUS-MIB", "wsLastAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsBoostStatus"),
        ("APPACCELERATION-STATUS-MIB", "wsBandwidthMode"),
        ("APPACCELERATION-STATUS-MIB", "wsBandwidthLimit"),
        ("APPACCELERATION-STATUS-MIB", "wsWanOutOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsWanInOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsLanOutOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsLanInOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsCompressionEffectiveBandwidth"),
        ("APPACCELERATION-STATUS-MIB", "wsSendCompressionRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsReceiveCompressionRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsCompressionStatsCollectionTime"),
        ("APPACCELERATION-STATUS-MIB", "wsAcceleratedConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsNonAcceleratedConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsHaState"),
        ("APPACCELERATION-STATUS-MIB", "wsHaVmIp"),
        ("APPACCELERATION-STATUS-MIB", "wsHaSecondaryIp"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"),
        ("APPACCELERATION-STATUS-MIB", "wsCpuUsage"),
        ("APPACCELERATION-STATUS-MIB", "wsConnectedPlugIns"),
        ("APPACCELERATION-STATUS-MIB", "wsMaxPlugIns"),
        ("APPACCELERATION-STATUS-MIB", "wsQosStatsCollectionTime"),
        ("APPACCELERATION-STATUS-MIB", "wsUpTime"),
        ("APPACCELERATION-STATUS-MIB", "wsSerialNumber"),
        ("APPACCELERATION-STATUS-MIB", "wsNonAcceleratedVolume"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsAccelerationStatus"),
        ("APPACCELERATION-STATUS-MIB", "wsTrafficShapingStatus"),
        ("APPACCELERATION-STATUS-MIB", "wsSystemLoad"),
        ("APPACCELERATION-STATUS-MIB", "wsWanSendRate"),
        ("APPACCELERATION-STATUS-MIB", "wsWanReceiveRate"),
        ("APPACCELERATION-STATUS-MIB", "wsLanSendRate"),
        ("APPACCELERATION-STATUS-MIB", "wsLanReceiveRate"),
        ("APPACCELERATION-STATUS-MIB", "wsNonAcceleratedRate"),
        ("APPACCELERATION-STATUS-MIB", "wsModelNumber"),
        ("APPACCELERATION-STATUS-MIB", "wsWccpStatus"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmIndex"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmID"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmLogTime"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmAcked"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsServiceClassIndex"),
        ("APPACCELERATION-STATUS-MIB", "wsServiceClassName"),
        ("APPACCELERATION-STATUS-MIB", "wsScsCurrentAcceleratedConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsScsTotalAcceleratedConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsScsTotalAcceleratedOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsTotalNonAcceleratedConnections"),
        ("APPACCELERATION-STATUS-MIB", "wsScsTotalNonAcceleratedOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsTotalPreCompressionOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsCompressSentOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsCompressReceivedOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsPreCompressSentOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsPreCompressReceivedOctets"),
        ("APPACCELERATION-STATUS-MIB", "wsScsSendBWSavings"),
        ("APPACCELERATION-STATUS-MIB", "wsScsRecvBWSavings"),
        ("APPACCELERATION-STATUS-MIB", "wsScsSendRecvBWSavings"),
        ("APPACCELERATION-STATUS-MIB", "wsScsSendCompressionRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsScsRecvCompressionRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsScsSendRecvCompressionRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsQosIndex"),
        ("APPACCELERATION-STATUS-MIB", "wsQosName"),
        ("APPACCELERATION-STATUS-MIB", "wsQosConfiguredSendRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsQosSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "wsQosActualSendRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaIndex"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaServiceName"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaPriority"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaSentRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaReceivedVolume"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaReceivedRatio"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaSendRate"),
        ("APPACCELERATION-STATUS-MIB", "wsIcaReceiveRate"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterIndex"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterName"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterEnabled"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterIp"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterNetmask"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterGateway"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterVirtualIp"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterVLanEnabled"),
        ("APPACCELERATION-STATUS-MIB", "wsAdapterVLanGroup"),
        ("APPACCELERATION-STATUS-MIB", "linkIndex"),
        ("APPACCELERATION-STATUS-MIB", "linkName"),
        ("APPACCELERATION-STATUS-MIB", "linkSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "linkReceivedVolume"),
        ("APPACCELERATION-STATUS-MIB", "linkSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "linkReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "linkDroppedSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "linkDroppedReceivedVolume"),
        ("APPACCELERATION-STATUS-MIB", "linkDroppedSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "linkDroppedReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "appIndex"),
        ("APPACCELERATION-STATUS-MIB", "appName"),
        ("APPACCELERATION-STATUS-MIB", "appId"),
        ("APPACCELERATION-STATUS-MIB", "appParentId"),
        ("APPACCELERATION-STATUS-MIB", "appGroupId"),
        ("APPACCELERATION-STATUS-MIB", "appSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "appReceivedVolume"),
        ("APPACCELERATION-STATUS-MIB", "appSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "appReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "appDroppedSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "appDroppedReceiveVolume"),
        ("APPACCELERATION-STATUS-MIB", "appDroppedSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "appDroppedReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "appSendRate"),
        ("APPACCELERATION-STATUS-MIB", "appReceiveRate"),
        ("APPACCELERATION-STATUS-MIB", "qosIndex"),
        ("APPACCELERATION-STATUS-MIB", "qosPolicyName"),
        ("APPACCELERATION-STATUS-MIB", "qosLink"),
        ("APPACCELERATION-STATUS-MIB", "qosSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "qosReceiveVolume"),
        ("APPACCELERATION-STATUS-MIB", "qosSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "qosReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "qosDroppedSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "qosDroppedReceiveVolume"),
        ("APPACCELERATION-STATUS-MIB", "qosDroppedSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "qosDroppedReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "lscIndex"),
        ("APPACCELERATION-STATUS-MIB", "lscServiceClassName"),
        ("APPACCELERATION-STATUS-MIB", "lscLink"),
        ("APPACCELERATION-STATUS-MIB", "lscSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "lscReceivedVolume"),
        ("APPACCELERATION-STATUS-MIB", "lscSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "lscReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "lscDroppedSentVolume"),
        ("APPACCELERATION-STATUS-MIB", "lscDroppedReceiveVolume"),
        ("APPACCELERATION-STATUS-MIB", "lscDroppedSentPackets"),
        ("APPACCELERATION-STATUS-MIB", "lscDroppedReceivedPackets"),
        ("APPACCELERATION-STATUS-MIB", "partnerAddrType"),
        ("APPACCELERATION-STATUS-MIB", "partnerAddr"),
        ("APPACCELERATION-STATUS-MIB", "partnerConnections"),
        ("APPACCELERATION-STATUS-MIB", "partnerSendRate"),
        ("APPACCELERATION-STATUS-MIB", "partnerReceiveRate"),
        ("APPACCELERATION-STATUS-MIB", "partnerIdleTime"))
)
if mibBuilder.loadTexts:
    wsStatusGroup.setStatus("current")

wsStatusTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 2, 2)
)
wsStatusTrapGroup.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsHAMasterIpAddr"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertAction"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertClass"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertMsg"))
)
if mibBuilder.loadTexts:
    wsStatusTrapGroup.setStatus("current")

wsStatusNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 2, 3)
)
wsStatusNotifyGroup.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsNotifyStart"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyShutdown"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyRestart"),
        ("APPACCELERATION-STATUS-MIB", "wsHANotifyNewMaster"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyAvailBWChange"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyUnexpectedRestart"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyPersistentError"),
        ("APPACCELERATION-STATUS-MIB", "wsNotifyAlert"))
)
if mibBuilder.loadTexts:
    wsStatusNotifyGroup.setStatus("current")


# Notification objects

wsNotifyStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 1)
)
wsNotifyStart.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyStart.setStatus(
        "current"
    )

wsNotifyShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 2)
)
wsNotifyShutdown.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyShutdown.setStatus(
        "current"
    )

wsNotifyRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 3)
)
wsNotifyRestart.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"))
)
if mibBuilder.loadTexts:
    wsNotifyRestart.setStatus(
        "deprecated"
    )

wsHANotifyNewMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 4)
)
wsHANotifyNewMaster.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsHAMasterIpAddr"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsHANotifyNewMaster.setStatus(
        "current"
    )

wsNotifyAvailBWChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 5)
)
wsNotifyAvailBWChange.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"))
)
if mibBuilder.loadTexts:
    wsNotifyAvailBWChange.setStatus(
        "deprecated"
    )

wsNotifyUnexpectedRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 6)
)
wsNotifyUnexpectedRestart.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyUnexpectedRestart.setStatus(
        "current"
    )

wsNotifyPersistentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 7)
)
wsNotifyPersistentError.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyPersistentError.setStatus(
        "current"
    )

wsNotifyAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 8)
)
wsNotifyAlert.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertAction"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertClass"),
        ("APPACCELERATION-STATUS-MIB", "wsAlertMsg"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyAlert.setStatus(
        "current"
    )

wsNotifyConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 30, 5, 1, 9)
)
wsNotifyConfigurationChanged.setObjects(
      *(("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeverity"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmSeqNum"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmDesc"),
        ("APPACCELERATION-STATUS-MIB", "wsActiveAlarmServiceAffect"),
        ("APPACCELERATION-STATUS-MIB", "wsPrimaryIp"))
)
if mibBuilder.loadTexts:
    wsNotifyConfigurationChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

wsStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3845, 30, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wsStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPACCELERATION-STATUS-MIB",
    **{"appAccelerationStatusMIB": appAccelerationStatusMIB,
       "wsStatusMIBObjects": wsStatusMIBObjects,
       "wsStatusMIBScalars": wsStatusMIBScalars,
       "wsOperStatus": wsOperStatus,
       "wsLoad1Min": wsLoad1Min,
       "wsLoad5Min": wsLoad5Min,
       "wsLoad15Min": wsLoad15Min,
       "wsBypass": wsBypass,
       "wsLastAlarmSeqNum": wsLastAlarmSeqNum,
       "wsBoostStatus": wsBoostStatus,
       "wsBandwidthMode": wsBandwidthMode,
       "wsBandwidthLimit": wsBandwidthLimit,
       "wsWanOutOctets": wsWanOutOctets,
       "wsWanInOctets": wsWanInOctets,
       "wsLanOutOctets": wsLanOutOctets,
       "wsLanInOctets": wsLanInOctets,
       "wsCompressionEffectiveBandwidth": wsCompressionEffectiveBandwidth,
       "wsSendCompressionRatio": wsSendCompressionRatio,
       "wsReceiveCompressionRatio": wsReceiveCompressionRatio,
       "wsCompressionStatsCollectionTime": wsCompressionStatsCollectionTime,
       "wsAcceleratedConnections": wsAcceleratedConnections,
       "wsNonAcceleratedConnections": wsNonAcceleratedConnections,
       "wsHaState": wsHaState,
       "wsHaVmIp": wsHaVmIp,
       "wsHaSecondaryIp": wsHaSecondaryIp,
       "wsPrimaryIp": wsPrimaryIp,
       "wsCpuUsage": wsCpuUsage,
       "wsConnectedPlugIns": wsConnectedPlugIns,
       "wsMaxPlugIns": wsMaxPlugIns,
       "wsQosStatsCollectionTime": wsQosStatsCollectionTime,
       "wsUpTime": wsUpTime,
       "wsSerialNumber": wsSerialNumber,
       "wsNonAcceleratedVolume": wsNonAcceleratedVolume,
       "wsActiveConnections": wsActiveConnections,
       "wsAccelerationStatus": wsAccelerationStatus,
       "wsTrafficShapingStatus": wsTrafficShapingStatus,
       "wsSystemLoad": wsSystemLoad,
       "wsWanSendRate": wsWanSendRate,
       "wsWanReceiveRate": wsWanReceiveRate,
       "wsLanSendRate": wsLanSendRate,
       "wsLanReceiveRate": wsLanReceiveRate,
       "wsNonAcceleratedRate": wsNonAcceleratedRate,
       "wsModelNumber": wsModelNumber,
       "wsWccpStatus": wsWccpStatus,
       "wsStatusMIBTables": wsStatusMIBTables,
       "wsActiveAlarmTable": wsActiveAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "wsActiveAlarmIndex": wsActiveAlarmIndex,
       "wsActiveAlarmSeqNum": wsActiveAlarmSeqNum,
       "wsActiveAlarmID": wsActiveAlarmID,
       "wsActiveAlarmSeverity": wsActiveAlarmSeverity,
       "wsActiveAlarmLogTime": wsActiveAlarmLogTime,
       "wsActiveAlarmDesc": wsActiveAlarmDesc,
       "wsActiveAlarmAcked": wsActiveAlarmAcked,
       "wsActiveAlarmServiceAffect": wsActiveAlarmServiceAffect,
       "wsServiceClassStatsTable": wsServiceClassStatsTable,
       "wsServiceClassStatsEntry": wsServiceClassStatsEntry,
       "wsServiceClassIndex": wsServiceClassIndex,
       "wsServiceClassName": wsServiceClassName,
       "wsScsCurrentAcceleratedConnections": wsScsCurrentAcceleratedConnections,
       "wsScsTotalAcceleratedConnections": wsScsTotalAcceleratedConnections,
       "wsScsTotalAcceleratedOctets": wsScsTotalAcceleratedOctets,
       "wsScsTotalNonAcceleratedConnections": wsScsTotalNonAcceleratedConnections,
       "wsScsTotalNonAcceleratedOctets": wsScsTotalNonAcceleratedOctets,
       "wsScsTotalPreCompressionOctets": wsScsTotalPreCompressionOctets,
       "wsScsCompressSentOctets": wsScsCompressSentOctets,
       "wsScsCompressReceivedOctets": wsScsCompressReceivedOctets,
       "wsScsPreCompressSentOctets": wsScsPreCompressSentOctets,
       "wsScsPreCompressReceivedOctets": wsScsPreCompressReceivedOctets,
       "wsScsSendBWSavings": wsScsSendBWSavings,
       "wsScsRecvBWSavings": wsScsRecvBWSavings,
       "wsScsSendRecvBWSavings": wsScsSendRecvBWSavings,
       "wsScsSendCompressionRatio": wsScsSendCompressionRatio,
       "wsScsRecvCompressionRatio": wsScsRecvCompressionRatio,
       "wsScsSendRecvCompressionRatio": wsScsSendRecvCompressionRatio,
       "wsQosTrafficClassStatsTable": wsQosTrafficClassStatsTable,
       "wsQosTcStatsEntry": wsQosTcStatsEntry,
       "wsQosIndex": wsQosIndex,
       "wsQosName": wsQosName,
       "wsQosConfiguredSendRatio": wsQosConfiguredSendRatio,
       "wsQosSentVolume": wsQosSentVolume,
       "wsQosActualSendRatio": wsQosActualSendRatio,
       "wsIcaStatsTable": wsIcaStatsTable,
       "wsIcaStatsEntry": wsIcaStatsEntry,
       "wsIcaIndex": wsIcaIndex,
       "wsIcaServiceName": wsIcaServiceName,
       "wsIcaPriority": wsIcaPriority,
       "wsIcaSentVolume": wsIcaSentVolume,
       "wsIcaSentRatio": wsIcaSentRatio,
       "wsIcaReceivedVolume": wsIcaReceivedVolume,
       "wsIcaReceivedRatio": wsIcaReceivedRatio,
       "wsIcaSendRate": wsIcaSendRate,
       "wsIcaReceiveRate": wsIcaReceiveRate,
       "wsAdapterTable": wsAdapterTable,
       "wsAdapterEntry": wsAdapterEntry,
       "wsAdapterIndex": wsAdapterIndex,
       "wsAdapterName": wsAdapterName,
       "wsAdapterEnabled": wsAdapterEnabled,
       "wsAdapterIp": wsAdapterIp,
       "wsAdapterNetmask": wsAdapterNetmask,
       "wsAdapterGateway": wsAdapterGateway,
       "wsAdapterVirtualIp": wsAdapterVirtualIp,
       "wsAdapterVLanEnabled": wsAdapterVLanEnabled,
       "wsAdapterVLanGroup": wsAdapterVLanGroup,
       "wsLinkStatsTable": wsLinkStatsTable,
       "linkStatsEntry": linkStatsEntry,
       "linkIndex": linkIndex,
       "linkName": linkName,
       "linkSentVolume": linkSentVolume,
       "linkReceivedVolume": linkReceivedVolume,
       "linkSentPackets": linkSentPackets,
       "linkReceivedPackets": linkReceivedPackets,
       "linkDroppedSentVolume": linkDroppedSentVolume,
       "linkDroppedReceivedVolume": linkDroppedReceivedVolume,
       "linkDroppedSentPackets": linkDroppedSentPackets,
       "linkDroppedReceivedPackets": linkDroppedReceivedPackets,
       "wsAppStatsTable": wsAppStatsTable,
       "appStatsEntry": appStatsEntry,
       "appIndex": appIndex,
       "appName": appName,
       "appId": appId,
       "appParentId": appParentId,
       "appGroupId": appGroupId,
       "appSentVolume": appSentVolume,
       "appReceivedVolume": appReceivedVolume,
       "appSentPackets": appSentPackets,
       "appReceivedPackets": appReceivedPackets,
       "appDroppedSentVolume": appDroppedSentVolume,
       "appDroppedReceiveVolume": appDroppedReceiveVolume,
       "appDroppedSentPackets": appDroppedSentPackets,
       "appDroppedReceivedPackets": appDroppedReceivedPackets,
       "appSendRate": appSendRate,
       "appReceiveRate": appReceiveRate,
       "wsQosStatsTable": wsQosStatsTable,
       "qosStatsEntry": qosStatsEntry,
       "qosIndex": qosIndex,
       "qosPolicyName": qosPolicyName,
       "qosLink": qosLink,
       "qosSentVolume": qosSentVolume,
       "qosReceiveVolume": qosReceiveVolume,
       "qosSentPackets": qosSentPackets,
       "qosReceivedPackets": qosReceivedPackets,
       "qosDroppedSentVolume": qosDroppedSentVolume,
       "qosDroppedReceiveVolume": qosDroppedReceiveVolume,
       "qosDroppedSentPackets": qosDroppedSentPackets,
       "qosDroppedReceivedPackets": qosDroppedReceivedPackets,
       "wsLscStatsTable": wsLscStatsTable,
       "lscStatsEntry": lscStatsEntry,
       "lscIndex": lscIndex,
       "lscServiceClassName": lscServiceClassName,
       "lscLink": lscLink,
       "lscSentVolume": lscSentVolume,
       "lscReceivedVolume": lscReceivedVolume,
       "lscSentPackets": lscSentPackets,
       "lscReceivedPackets": lscReceivedPackets,
       "lscDroppedSentVolume": lscDroppedSentVolume,
       "lscDroppedReceiveVolume": lscDroppedReceiveVolume,
       "lscDroppedSentPackets": lscDroppedSentPackets,
       "lscDroppedReceivedPackets": lscDroppedReceivedPackets,
       "wsPartnerTable": wsPartnerTable,
       "partnerEntry": partnerEntry,
       "partnerAddrType": partnerAddrType,
       "partnerAddr": partnerAddr,
       "partnerConnections": partnerConnections,
       "partnerSendRate": partnerSendRate,
       "partnerReceiveRate": partnerReceiveRate,
       "partnerIdleTime": partnerIdleTime,
       "wsHAMasterIpAddr": wsHAMasterIpAddr,
       "wsStatusMIBAlertTables": wsStatusMIBAlertTables,
       "wsAlertAction": wsAlertAction,
       "wsAlertClass": wsAlertClass,
       "wsAlertMsg": wsAlertMsg,
       "wsSourceIpAddr": wsSourceIpAddr,
       "wsStatusMIBConformance": wsStatusMIBConformance,
       "wsStatusMIBCompliances": wsStatusMIBCompliances,
       "wsStatusCompliance": wsStatusCompliance,
       "wsStatusMIBGroups": wsStatusMIBGroups,
       "wsStatusGroup": wsStatusGroup,
       "wsStatusTrapGroup": wsStatusTrapGroup,
       "wsStatusNotifyGroup": wsStatusNotifyGroup,
       "wsStatusMIBNotifications": wsStatusMIBNotifications,
       "wsNotifyStart": wsNotifyStart,
       "wsNotifyShutdown": wsNotifyShutdown,
       "wsNotifyRestart": wsNotifyRestart,
       "wsHANotifyNewMaster": wsHANotifyNewMaster,
       "wsNotifyAvailBWChange": wsNotifyAvailBWChange,
       "wsNotifyUnexpectedRestart": wsNotifyUnexpectedRestart,
       "wsNotifyPersistentError": wsNotifyPersistentError,
       "wsNotifyAlert": wsNotifyAlert,
       "wsNotifyConfigurationChanged": wsNotifyConfigurationChanged}
)
