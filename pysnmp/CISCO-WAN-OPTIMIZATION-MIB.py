# SNMP MIB module (CISCO-WAN-OPTIMIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-OPTIMIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:12 2024
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

(cpmCPUTotalMonIntervalValue,) = mibBuilder.importSymbols(
    "CISCO-PROCESS-MIB",
    "cpmCPUTotalMonIntervalValue")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoMilliSeconds,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds",
    "TimeIntervalSec",
    "Unsigned64")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanOptimizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762)
)
ciscoWanOptimizationMIB.setRevisions(
        ("2016-05-22 00:00",
         "2016-05-18 00:00",
         "2015-11-30 00:00",
         "2013-05-23 00:00",
         "2012-12-13 00:00",
         "2012-03-05 00:00",
         "2011-04-19 00:00",
         "2010-10-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CwoHttpAKCPrepStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("disabled", 3),
          ("error", 5),
          ("scheduled", 2),
          ("success", 4),
          ("unknown", 1))
    )



class CwoDreCacheStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 5),
          ("initializing", 2),
          ("notUsable", 1),
          ("temporarilyFailed", 4),
          ("usable", 3))
    )



class CwoAoName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 96),
    )



class CwoAoOperationalState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleaningup", 6),
          ("error", 7),
          ("initializing", 2),
          ("licenseExpired", 5),
          ("normalDisabled", 4),
          ("normalRunning", 3),
          ("shutdown", 1))
    )



class CwoLoadStates(Integer32, TextualConvention):
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
        *(("green", 2),
          ("red", 4),
          ("unknown", 1),
          ("yellow", 3))
    )



class CwoTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("appnav", 2),
          ("waas", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWanOptimizationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanOptimizationMIBNotifs = _CiscoWanOptimizationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0)
)
_CiscoWanOptimizationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanOptimizationMIBObjects = _CiscoWanOptimizationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1)
)
_CwoGeneral_ObjectIdentity = ObjectIdentity
cwoGeneral = _CwoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1)
)
_CwoGeneralActivePeers_Type = Gauge32
_CwoGeneralActivePeers_Object = MibScalar
cwoGeneralActivePeers = _CwoGeneralActivePeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1, 1),
    _CwoGeneralActivePeers_Type()
)
cwoGeneralActivePeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoGeneralActivePeers.setStatus("current")
if mibBuilder.loadTexts:
    cwoGeneralActivePeers.setUnits("number of peers")
_CwoGeneralMaxActivePeers_Type = Unsigned32
_CwoGeneralMaxActivePeers_Object = MibScalar
cwoGeneralMaxActivePeers = _CwoGeneralMaxActivePeers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1, 2),
    _CwoGeneralMaxActivePeers_Type()
)
cwoGeneralMaxActivePeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoGeneralMaxActivePeers.setStatus("current")


class _CwoGeneralCpuThrottleHigh_Type(Unsigned32):
    """Custom type cwoGeneralCpuThrottleHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwoGeneralCpuThrottleHigh_Type.__name__ = "Unsigned32"
_CwoGeneralCpuThrottleHigh_Object = MibScalar
cwoGeneralCpuThrottleHigh = _CwoGeneralCpuThrottleHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1, 3),
    _CwoGeneralCpuThrottleHigh_Type()
)
cwoGeneralCpuThrottleHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwoGeneralCpuThrottleHigh.setStatus("current")
if mibBuilder.loadTexts:
    cwoGeneralCpuThrottleHigh.setUnits("percent")


class _CwoGeneralCpuThrottleLow_Type(Unsigned32):
    """Custom type cwoGeneralCpuThrottleLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwoGeneralCpuThrottleLow_Type.__name__ = "Unsigned32"
_CwoGeneralCpuThrottleLow_Object = MibScalar
cwoGeneralCpuThrottleLow = _CwoGeneralCpuThrottleLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1, 4),
    _CwoGeneralCpuThrottleLow_Type()
)
cwoGeneralCpuThrottleLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwoGeneralCpuThrottleLow.setStatus("current")
if mibBuilder.loadTexts:
    cwoGeneralCpuThrottleLow.setUnits("percent")
_CwoGeneralCpuThrottlPeriod_Type = TimeInterval
_CwoGeneralCpuThrottlPeriod_Object = MibScalar
cwoGeneralCpuThrottlPeriod = _CwoGeneralCpuThrottlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 1, 5),
    _CwoGeneralCpuThrottlPeriod_Type()
)
cwoGeneralCpuThrottlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwoGeneralCpuThrottlPeriod.setStatus("current")
_CwoTfo_ObjectIdentity = ObjectIdentity
cwoTfo = _CwoTfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2)
)
_CwoTfoStats_ObjectIdentity = ObjectIdentity
cwoTfoStats = _CwoTfoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1)
)
_CwoTfoStatsTotalOptConn_Type = Counter64
_CwoTfoStatsTotalOptConn_Object = MibScalar
cwoTfoStatsTotalOptConn = _CwoTfoStatsTotalOptConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 1),
    _CwoTfoStatsTotalOptConn_Type()
)
cwoTfoStatsTotalOptConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsTotalOptConn.setStatus("current")
_CwoTfoStatsActiveOptConn_Type = CounterBasedGauge64
_CwoTfoStatsActiveOptConn_Object = MibScalar
cwoTfoStatsActiveOptConn = _CwoTfoStatsActiveOptConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 2),
    _CwoTfoStatsActiveOptConn_Type()
)
cwoTfoStatsActiveOptConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActiveOptConn.setStatus("current")
_CwoTfoStatsMaxActiveConn_Type = Unsigned64
_CwoTfoStatsMaxActiveConn_Object = MibScalar
cwoTfoStatsMaxActiveConn = _CwoTfoStatsMaxActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 3),
    _CwoTfoStatsMaxActiveConn_Type()
)
cwoTfoStatsMaxActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsMaxActiveConn.setStatus("current")
_CwoTfoStatsActiveOptTCPPlusConn_Type = CounterBasedGauge64
_CwoTfoStatsActiveOptTCPPlusConn_Object = MibScalar
cwoTfoStatsActiveOptTCPPlusConn = _CwoTfoStatsActiveOptTCPPlusConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 4),
    _CwoTfoStatsActiveOptTCPPlusConn_Type()
)
cwoTfoStatsActiveOptTCPPlusConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActiveOptTCPPlusConn.setStatus("current")
_CwoTfoStatsActiveOptTCPOnlyConn_Type = CounterBasedGauge64
_CwoTfoStatsActiveOptTCPOnlyConn_Object = MibScalar
cwoTfoStatsActiveOptTCPOnlyConn = _CwoTfoStatsActiveOptTCPOnlyConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 5),
    _CwoTfoStatsActiveOptTCPOnlyConn_Type()
)
cwoTfoStatsActiveOptTCPOnlyConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActiveOptTCPOnlyConn.setStatus("current")
_CwoTfoStatsActiveOptTCPPrepConn_Type = CounterBasedGauge64
_CwoTfoStatsActiveOptTCPPrepConn_Object = MibScalar
cwoTfoStatsActiveOptTCPPrepConn = _CwoTfoStatsActiveOptTCPPrepConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 6),
    _CwoTfoStatsActiveOptTCPPrepConn_Type()
)
cwoTfoStatsActiveOptTCPPrepConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActiveOptTCPPrepConn.setStatus("current")
_CwoTfoStatsActiveADConn_Type = CounterBasedGauge64
_CwoTfoStatsActiveADConn_Object = MibScalar
cwoTfoStatsActiveADConn = _CwoTfoStatsActiveADConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 7),
    _CwoTfoStatsActiveADConn_Type()
)
cwoTfoStatsActiveADConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActiveADConn.setStatus("current")
_CwoTfoStatsReservedConn_Type = Unsigned64
_CwoTfoStatsReservedConn_Object = MibScalar
cwoTfoStatsReservedConn = _CwoTfoStatsReservedConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 8),
    _CwoTfoStatsReservedConn_Type()
)
cwoTfoStatsReservedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsReservedConn.setStatus("current")
_CwoTfoStatsPendingConn_Type = CounterBasedGauge64
_CwoTfoStatsPendingConn_Object = MibScalar
cwoTfoStatsPendingConn = _CwoTfoStatsPendingConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 9),
    _CwoTfoStatsPendingConn_Type()
)
cwoTfoStatsPendingConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsPendingConn.setStatus("current")
_CwoTfoStatsActivePTConn_Type = CounterBasedGauge64
_CwoTfoStatsActivePTConn_Object = MibScalar
cwoTfoStatsActivePTConn = _CwoTfoStatsActivePTConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 10),
    _CwoTfoStatsActivePTConn_Type()
)
cwoTfoStatsActivePTConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsActivePTConn.setStatus("current")
_CwoTfoStatsTotalNormalClosedConn_Type = Counter64
_CwoTfoStatsTotalNormalClosedConn_Object = MibScalar
cwoTfoStatsTotalNormalClosedConn = _CwoTfoStatsTotalNormalClosedConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 11),
    _CwoTfoStatsTotalNormalClosedConn_Type()
)
cwoTfoStatsTotalNormalClosedConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsTotalNormalClosedConn.setStatus("current")
_CwoTfoStatsResetConn_Type = Counter64
_CwoTfoStatsResetConn_Object = MibScalar
cwoTfoStatsResetConn = _CwoTfoStatsResetConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 12),
    _CwoTfoStatsResetConn_Type()
)
cwoTfoStatsResetConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsResetConn.setStatus("current")
_CwoTfoStatsLoadStatus_Type = CwoLoadStates
_CwoTfoStatsLoadStatus_Object = MibScalar
cwoTfoStatsLoadStatus = _CwoTfoStatsLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 2, 1, 13),
    _CwoTfoStatsLoadStatus_Type()
)
cwoTfoStatsLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoTfoStatsLoadStatus.setStatus("current")
_CwoAo_ObjectIdentity = ObjectIdentity
cwoAo = _CwoAo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3)
)
_CwoAoStatsTable_Object = MibTable
cwoAoStatsTable = _CwoAoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cwoAoStatsTable.setStatus("current")
_CwoAoStatsEntry_Object = MibTableRow
cwoAoStatsEntry = _CwoAoStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1)
)
cwoAoStatsEntry.setIndexNames(
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsName"),
)
if mibBuilder.loadTexts:
    cwoAoStatsEntry.setStatus("current")
_CwoAoStatsName_Type = CwoAoName
_CwoAoStatsName_Object = MibTableColumn
cwoAoStatsName = _CwoAoStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 1),
    _CwoAoStatsName_Type()
)
cwoAoStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoAoStatsName.setStatus("current")
_CwoAoStatsIsConfigured_Type = TruthValue
_CwoAoStatsIsConfigured_Object = MibTableColumn
cwoAoStatsIsConfigured = _CwoAoStatsIsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 2),
    _CwoAoStatsIsConfigured_Type()
)
cwoAoStatsIsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsIsConfigured.setStatus("current")
_CwoAoStatsIsLicensed_Type = TruthValue
_CwoAoStatsIsLicensed_Object = MibTableColumn
cwoAoStatsIsLicensed = _CwoAoStatsIsLicensed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 3),
    _CwoAoStatsIsLicensed_Type()
)
cwoAoStatsIsLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsIsLicensed.setStatus("current")
_CwoAoStatsOperationalState_Type = CwoAoOperationalState
_CwoAoStatsOperationalState_Object = MibTableColumn
cwoAoStatsOperationalState = _CwoAoStatsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 4),
    _CwoAoStatsOperationalState_Type()
)
cwoAoStatsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsOperationalState.setStatus("current")
_CwoAoStatsStartUpTime_Type = DateAndTime
_CwoAoStatsStartUpTime_Object = MibTableColumn
cwoAoStatsStartUpTime = _CwoAoStatsStartUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 5),
    _CwoAoStatsStartUpTime_Type()
)
cwoAoStatsStartUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsStartUpTime.setStatus("current")
_CwoAoStatsLastResetTime_Type = DateAndTime
_CwoAoStatsLastResetTime_Object = MibTableColumn
cwoAoStatsLastResetTime = _CwoAoStatsLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 6),
    _CwoAoStatsLastResetTime_Type()
)
cwoAoStatsLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsLastResetTime.setStatus("current")
_CwoAoStatsTotalHandledConns_Type = Counter32
_CwoAoStatsTotalHandledConns_Object = MibTableColumn
cwoAoStatsTotalHandledConns = _CwoAoStatsTotalHandledConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 7),
    _CwoAoStatsTotalHandledConns_Type()
)
cwoAoStatsTotalHandledConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsTotalHandledConns.setStatus("current")
_CwoAoStatsTotalOptConns_Type = Counter32
_CwoAoStatsTotalOptConns_Object = MibTableColumn
cwoAoStatsTotalOptConns = _CwoAoStatsTotalOptConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 8),
    _CwoAoStatsTotalOptConns_Type()
)
cwoAoStatsTotalOptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsTotalOptConns.setStatus("current")
_CwoAoStatsTotalHandedOffConns_Type = Counter32
_CwoAoStatsTotalHandedOffConns_Object = MibTableColumn
cwoAoStatsTotalHandedOffConns = _CwoAoStatsTotalHandedOffConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 9),
    _CwoAoStatsTotalHandedOffConns_Type()
)
cwoAoStatsTotalHandedOffConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsTotalHandedOffConns.setStatus("current")
_CwoAoStatsTotalDroppedConns_Type = Counter32
_CwoAoStatsTotalDroppedConns_Object = MibTableColumn
cwoAoStatsTotalDroppedConns = _CwoAoStatsTotalDroppedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 10),
    _CwoAoStatsTotalDroppedConns_Type()
)
cwoAoStatsTotalDroppedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsTotalDroppedConns.setStatus("current")
_CwoAoStatsActiveOptConns_Type = Gauge32
_CwoAoStatsActiveOptConns_Object = MibTableColumn
cwoAoStatsActiveOptConns = _CwoAoStatsActiveOptConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 11),
    _CwoAoStatsActiveOptConns_Type()
)
cwoAoStatsActiveOptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsActiveOptConns.setStatus("current")
_CwoAoStatsPendingConns_Type = Gauge32
_CwoAoStatsPendingConns_Object = MibTableColumn
cwoAoStatsPendingConns = _CwoAoStatsPendingConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 12),
    _CwoAoStatsPendingConns_Type()
)
cwoAoStatsPendingConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsPendingConns.setStatus("current")
_CwoAoStatsMaxActiveOptConns_Type = Unsigned32
_CwoAoStatsMaxActiveOptConns_Object = MibTableColumn
cwoAoStatsMaxActiveOptConns = _CwoAoStatsMaxActiveOptConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 13),
    _CwoAoStatsMaxActiveOptConns_Type()
)
cwoAoStatsMaxActiveOptConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsMaxActiveOptConns.setStatus("current")
_CwoAoStatsLoadStatus_Type = CwoLoadStates
_CwoAoStatsLoadStatus_Object = MibTableColumn
cwoAoStatsLoadStatus = _CwoAoStatsLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 14),
    _CwoAoStatsLoadStatus_Type()
)
cwoAoStatsLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsLoadStatus.setStatus("current")


class _CwoAoStatsBwOpt_Type(Gauge32):
    """Custom type cwoAoStatsBwOpt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoStatsBwOpt_Type.__name__ = "Gauge32"
_CwoAoStatsBwOpt_Object = MibTableColumn
cwoAoStatsBwOpt = _CwoAoStatsBwOpt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 1, 1, 15),
    _CwoAoStatsBwOpt_Type()
)
cwoAoStatsBwOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoStatsBwOpt.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoStatsBwOpt.setUnits("percent")
_CwoAoSmbxStats_ObjectIdentity = ObjectIdentity
cwoAoSmbxStats = _CwoAoSmbxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2)
)
_CwoAoSmbxStatsBytesReadCache_Type = Counter64
_CwoAoSmbxStatsBytesReadCache_Object = MibScalar
cwoAoSmbxStatsBytesReadCache = _CwoAoSmbxStatsBytesReadCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 1),
    _CwoAoSmbxStatsBytesReadCache_Type()
)
cwoAoSmbxStatsBytesReadCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadCache.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadCache.setUnits("bytes")
_CwoAoSmbxStatsBytesWriteCache_Type = Counter64
_CwoAoSmbxStatsBytesWriteCache_Object = MibScalar
cwoAoSmbxStatsBytesWriteCache = _CwoAoSmbxStatsBytesWriteCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 2),
    _CwoAoSmbxStatsBytesWriteCache_Type()
)
cwoAoSmbxStatsBytesWriteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteCache.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteCache.setUnits("bytes")
_CwoAoSmbxStatsBytesReadServer_Type = Counter64
_CwoAoSmbxStatsBytesReadServer_Object = MibScalar
cwoAoSmbxStatsBytesReadServer = _CwoAoSmbxStatsBytesReadServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 3),
    _CwoAoSmbxStatsBytesReadServer_Type()
)
cwoAoSmbxStatsBytesReadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadServer.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadServer.setUnits("bytes")
_CwoAoSmbxStatsBytesWriteServer_Type = Counter64
_CwoAoSmbxStatsBytesWriteServer_Object = MibScalar
cwoAoSmbxStatsBytesWriteServer = _CwoAoSmbxStatsBytesWriteServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 4),
    _CwoAoSmbxStatsBytesWriteServer_Type()
)
cwoAoSmbxStatsBytesWriteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteServer.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteServer.setUnits("bytes")
_CwoAoSmbxStatsBytesReadClient_Type = Counter64
_CwoAoSmbxStatsBytesReadClient_Object = MibScalar
cwoAoSmbxStatsBytesReadClient = _CwoAoSmbxStatsBytesReadClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 5),
    _CwoAoSmbxStatsBytesReadClient_Type()
)
cwoAoSmbxStatsBytesReadClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadClient.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesReadClient.setUnits("bytes")
_CwoAoSmbxStatsBytesWriteClient_Type = Counter64
_CwoAoSmbxStatsBytesWriteClient_Object = MibScalar
cwoAoSmbxStatsBytesWriteClient = _CwoAoSmbxStatsBytesWriteClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 6),
    _CwoAoSmbxStatsBytesWriteClient_Type()
)
cwoAoSmbxStatsBytesWriteClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteClient.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsBytesWriteClient.setUnits("bytes")
_CwoAoSmbxStatsProcessedReqs_Type = Counter64
_CwoAoSmbxStatsProcessedReqs_Object = MibScalar
cwoAoSmbxStatsProcessedReqs = _CwoAoSmbxStatsProcessedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 7),
    _CwoAoSmbxStatsProcessedReqs_Type()
)
cwoAoSmbxStatsProcessedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsProcessedReqs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsProcessedReqs.setUnits("requests")
_CwoAoSmbxStatsActiveReqs_Type = CounterBasedGauge64
_CwoAoSmbxStatsActiveReqs_Object = MibScalar
cwoAoSmbxStatsActiveReqs = _CwoAoSmbxStatsActiveReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 8),
    _CwoAoSmbxStatsActiveReqs_Type()
)
cwoAoSmbxStatsActiveReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsActiveReqs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsActiveReqs.setUnits("requests")
_CwoAoSmbxStatsTotalTimedOutReqs_Type = Unsigned64
_CwoAoSmbxStatsTotalTimedOutReqs_Object = MibScalar
cwoAoSmbxStatsTotalTimedOutReqs = _CwoAoSmbxStatsTotalTimedOutReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 9),
    _CwoAoSmbxStatsTotalTimedOutReqs_Type()
)
cwoAoSmbxStatsTotalTimedOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalTimedOutReqs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalTimedOutReqs.setUnits("requests")
_CwoAoSmbxStatsTotalRemoteReqs_Type = Counter64
_CwoAoSmbxStatsTotalRemoteReqs_Object = MibScalar
cwoAoSmbxStatsTotalRemoteReqs = _CwoAoSmbxStatsTotalRemoteReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 10),
    _CwoAoSmbxStatsTotalRemoteReqs_Type()
)
cwoAoSmbxStatsTotalRemoteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalRemoteReqs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalRemoteReqs.setUnits("requests")
_CwoAoSmbxStatsTotalLocalReqs_Type = Counter64
_CwoAoSmbxStatsTotalLocalReqs_Object = MibScalar
cwoAoSmbxStatsTotalLocalReqs = _CwoAoSmbxStatsTotalLocalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 11),
    _CwoAoSmbxStatsTotalLocalReqs_Type()
)
cwoAoSmbxStatsTotalLocalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalLocalReqs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalLocalReqs.setUnits("requests")
_CwoAoSmbxStatsRemoteAvgTime_Type = CiscoMilliSeconds
_CwoAoSmbxStatsRemoteAvgTime_Object = MibScalar
cwoAoSmbxStatsRemoteAvgTime = _CwoAoSmbxStatsRemoteAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 12),
    _CwoAoSmbxStatsRemoteAvgTime_Type()
)
cwoAoSmbxStatsRemoteAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRemoteAvgTime.setStatus("current")
_CwoAoSmbxStatsLocalAvgTime_Type = CiscoMilliSeconds
_CwoAoSmbxStatsLocalAvgTime_Object = MibScalar
cwoAoSmbxStatsLocalAvgTime = _CwoAoSmbxStatsLocalAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 13),
    _CwoAoSmbxStatsLocalAvgTime_Type()
)
cwoAoSmbxStatsLocalAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsLocalAvgTime.setStatus("current")
_CwoAoSmbxStatsRACacheHitCount_Type = Counter64
_CwoAoSmbxStatsRACacheHitCount_Object = MibScalar
cwoAoSmbxStatsRACacheHitCount = _CwoAoSmbxStatsRACacheHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 14),
    _CwoAoSmbxStatsRACacheHitCount_Type()
)
cwoAoSmbxStatsRACacheHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRACacheHitCount.setStatus("current")
_CwoAoSmbxStatsMDCacheHitCount_Type = Counter64
_CwoAoSmbxStatsMDCacheHitCount_Object = MibScalar
cwoAoSmbxStatsMDCacheHitCount = _CwoAoSmbxStatsMDCacheHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 15),
    _CwoAoSmbxStatsMDCacheHitCount_Type()
)
cwoAoSmbxStatsMDCacheHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMDCacheHitCount.setStatus("current")


class _CwoAoSmbxStatsRACacheHitRate_Type(Gauge32):
    """Custom type cwoAoSmbxStatsRACacheHitRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoSmbxStatsRACacheHitRate_Type.__name__ = "Gauge32"
_CwoAoSmbxStatsRACacheHitRate_Object = MibScalar
cwoAoSmbxStatsRACacheHitRate = _CwoAoSmbxStatsRACacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 16),
    _CwoAoSmbxStatsRACacheHitRate_Type()
)
cwoAoSmbxStatsRACacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRACacheHitRate.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRACacheHitRate.setUnits("percent")


class _CwoAoSmbxStatsMDCacheHitRate_Type(Gauge32):
    """Custom type cwoAoSmbxStatsMDCacheHitRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoSmbxStatsMDCacheHitRate_Type.__name__ = "Gauge32"
_CwoAoSmbxStatsMDCacheHitRate_Object = MibScalar
cwoAoSmbxStatsMDCacheHitRate = _CwoAoSmbxStatsMDCacheHitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 17),
    _CwoAoSmbxStatsMDCacheHitRate_Type()
)
cwoAoSmbxStatsMDCacheHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMDCacheHitRate.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMDCacheHitRate.setUnits("percent")
_CwoAoSmbxStatsMaxRACacheSize_Type = Unsigned64
_CwoAoSmbxStatsMaxRACacheSize_Object = MibScalar
cwoAoSmbxStatsMaxRACacheSize = _CwoAoSmbxStatsMaxRACacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 18),
    _CwoAoSmbxStatsMaxRACacheSize_Type()
)
cwoAoSmbxStatsMaxRACacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMaxRACacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMaxRACacheSize.setUnits("bytes")
_CwoAoSmbxStatsMaxMDCacheSize_Type = Unsigned64
_CwoAoSmbxStatsMaxMDCacheSize_Object = MibScalar
cwoAoSmbxStatsMaxMDCacheSize = _CwoAoSmbxStatsMaxMDCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 19),
    _CwoAoSmbxStatsMaxMDCacheSize_Type()
)
cwoAoSmbxStatsMaxMDCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMaxMDCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMaxMDCacheSize.setUnits("bytes")
_CwoAoSmbxStatsMDCacheSize_Type = CounterBasedGauge64
_CwoAoSmbxStatsMDCacheSize_Object = MibScalar
cwoAoSmbxStatsMDCacheSize = _CwoAoSmbxStatsMDCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 20),
    _CwoAoSmbxStatsMDCacheSize_Type()
)
cwoAoSmbxStatsMDCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMDCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsMDCacheSize.setUnits("bytes")
_CwoAoSmbxStatsRAEvictedAge_Type = CiscoMilliSeconds
_CwoAoSmbxStatsRAEvictedAge_Object = MibScalar
cwoAoSmbxStatsRAEvictedAge = _CwoAoSmbxStatsRAEvictedAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 21),
    _CwoAoSmbxStatsRAEvictedAge_Type()
)
cwoAoSmbxStatsRAEvictedAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRAEvictedAge.setStatus("current")
_CwoAoSmbxStatsRTT_Type = TimeIntervalSec
_CwoAoSmbxStatsRTT_Object = MibScalar
cwoAoSmbxStatsRTT = _CwoAoSmbxStatsRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 22),
    _CwoAoSmbxStatsRTT_Type()
)
cwoAoSmbxStatsRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRTT.setStatus("current")
_CwoAoSmbxStatsTotalRespTimeSaving_Type = TimeIntervalSec
_CwoAoSmbxStatsTotalRespTimeSaving_Object = MibScalar
cwoAoSmbxStatsTotalRespTimeSaving = _CwoAoSmbxStatsTotalRespTimeSaving_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 23),
    _CwoAoSmbxStatsTotalRespTimeSaving_Type()
)
cwoAoSmbxStatsTotalRespTimeSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalRespTimeSaving.setStatus("current")
_CwoAoSmbxStatsOpenFiles_Type = Gauge32
_CwoAoSmbxStatsOpenFiles_Object = MibScalar
cwoAoSmbxStatsOpenFiles = _CwoAoSmbxStatsOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 24),
    _CwoAoSmbxStatsOpenFiles_Type()
)
cwoAoSmbxStatsOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsOpenFiles.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsOpenFiles.setUnits("files")
_CwoAoSmbxStatsTotalFilesInRACache_Type = Gauge32
_CwoAoSmbxStatsTotalFilesInRACache_Object = MibScalar
cwoAoSmbxStatsTotalFilesInRACache = _CwoAoSmbxStatsTotalFilesInRACache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 25),
    _CwoAoSmbxStatsTotalFilesInRACache_Type()
)
cwoAoSmbxStatsTotalFilesInRACache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalFilesInRACache.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsTotalFilesInRACache.setUnits("files")
_CwoAoSmbxStatsRdL4SignWANBytes_Type = Counter64
_CwoAoSmbxStatsRdL4SignWANBytes_Object = MibScalar
cwoAoSmbxStatsRdL4SignWANBytes = _CwoAoSmbxStatsRdL4SignWANBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 26),
    _CwoAoSmbxStatsRdL4SignWANBytes_Type()
)
cwoAoSmbxStatsRdL4SignWANBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRdL4SignWANBytes.setStatus("current")
_CwoAoSmbxStatsWrL4SignWANBytes_Type = Counter64
_CwoAoSmbxStatsWrL4SignWANBytes_Object = MibScalar
cwoAoSmbxStatsWrL4SignWANBytes = _CwoAoSmbxStatsWrL4SignWANBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 27),
    _CwoAoSmbxStatsWrL4SignWANBytes_Type()
)
cwoAoSmbxStatsWrL4SignWANBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsWrL4SignWANBytes.setStatus("current")
_CwoAoSmbxStatsRdSignLANBytes_Type = Counter64
_CwoAoSmbxStatsRdSignLANBytes_Object = MibScalar
cwoAoSmbxStatsRdSignLANBytes = _CwoAoSmbxStatsRdSignLANBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 28),
    _CwoAoSmbxStatsRdSignLANBytes_Type()
)
cwoAoSmbxStatsRdSignLANBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsRdSignLANBytes.setStatus("current")
_CwoAoSmbxStatsWrSignLANBytes_Type = Counter64
_CwoAoSmbxStatsWrSignLANBytes_Object = MibScalar
cwoAoSmbxStatsWrSignLANBytes = _CwoAoSmbxStatsWrSignLANBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 2, 29),
    _CwoAoSmbxStatsWrSignLANBytes_Type()
)
cwoAoSmbxStatsWrSignLANBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoSmbxStatsWrSignLANBytes.setStatus("current")
_CwoAoHttpxStats_ObjectIdentity = ObjectIdentity
cwoAoHttpxStats = _CwoAoHttpxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3)
)
_CwoAoHttpxStatsTotalSavedTime_Type = CiscoMilliSeconds
_CwoAoHttpxStatsTotalSavedTime_Object = MibScalar
cwoAoHttpxStatsTotalSavedTime = _CwoAoHttpxStatsTotalSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 1),
    _CwoAoHttpxStatsTotalSavedTime_Type()
)
cwoAoHttpxStatsTotalSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSavedTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSavedTime.setUnits("milliseconds")
_CwoAoHttpxStatsTotalRTT_Type = CiscoMilliSeconds
_CwoAoHttpxStatsTotalRTT_Object = MibScalar
cwoAoHttpxStatsTotalRTT = _CwoAoHttpxStatsTotalRTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 2),
    _CwoAoHttpxStatsTotalRTT_Type()
)
cwoAoHttpxStatsTotalRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalRTT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalRTT.setUnits("milliseconds")
_CwoAoHttpxStatsTotalMDCMTime_Type = CiscoMilliSeconds
_CwoAoHttpxStatsTotalMDCMTime_Object = MibScalar
cwoAoHttpxStatsTotalMDCMTime = _CwoAoHttpxStatsTotalMDCMTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 3),
    _CwoAoHttpxStatsTotalMDCMTime_Type()
)
cwoAoHttpxStatsTotalMDCMTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalMDCMTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalMDCMTime.setUnits("milliseconds")


class _CwoAoHttpxStatsEstSavedTime_Type(Gauge32):
    """Custom type cwoAoHttpxStatsEstSavedTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsEstSavedTime_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsEstSavedTime_Object = MibScalar
cwoAoHttpxStatsEstSavedTime = _CwoAoHttpxStatsEstSavedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 4),
    _CwoAoHttpxStatsEstSavedTime_Type()
)
cwoAoHttpxStatsEstSavedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsEstSavedTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsEstSavedTime.setUnits("percent")
_CwoAoHttpxStatsTotalSPSessions_Type = Counter64
_CwoAoHttpxStatsTotalSPSessions_Object = MibScalar
cwoAoHttpxStatsTotalSPSessions = _CwoAoHttpxStatsTotalSPSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 5),
    _CwoAoHttpxStatsTotalSPSessions_Type()
)
cwoAoHttpxStatsTotalSPSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPSessions.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPSessions.setUnits("sessions")
_CwoAoHttpxStatsTotalSPPFSessions_Type = Counter64
_CwoAoHttpxStatsTotalSPPFSessions_Object = MibScalar
cwoAoHttpxStatsTotalSPPFSessions = _CwoAoHttpxStatsTotalSPPFSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 6),
    _CwoAoHttpxStatsTotalSPPFSessions_Type()
)
cwoAoHttpxStatsTotalSPPFSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFSessions.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFSessions.setUnits("sessions")
_CwoAoHttpxStatsTotalSPPFObjects_Type = Counter64
_CwoAoHttpxStatsTotalSPPFObjects_Object = MibScalar
cwoAoHttpxStatsTotalSPPFObjects = _CwoAoHttpxStatsTotalSPPFObjects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 7),
    _CwoAoHttpxStatsTotalSPPFObjects_Type()
)
cwoAoHttpxStatsTotalSPPFObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFObjects.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFObjects.setUnits("requests")
_CwoAoHttpxStatsTotalSPRTTSaved_Type = Counter64
_CwoAoHttpxStatsTotalSPRTTSaved_Object = MibScalar
cwoAoHttpxStatsTotalSPRTTSaved = _CwoAoHttpxStatsTotalSPRTTSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 8),
    _CwoAoHttpxStatsTotalSPRTTSaved_Type()
)
cwoAoHttpxStatsTotalSPRTTSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPRTTSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPRTTSaved.setUnits("milliseconds")
_CwoAoHttpxStatsTotalSPPFMissTime_Type = Counter64
_CwoAoHttpxStatsTotalSPPFMissTime_Object = MibScalar
cwoAoHttpxStatsTotalSPPFMissTime = _CwoAoHttpxStatsTotalSPPFMissTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 9),
    _CwoAoHttpxStatsTotalSPPFMissTime_Type()
)
cwoAoHttpxStatsTotalSPPFMissTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFMissTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsTotalSPPFMissTime.setUnits("milliseconds")
_CwoAoHttpxStatsAKC_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKC = _CwoAoHttpxStatsAKC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10)
)
_CwoAoHttpxStatsAKCBypassEntry_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKCBypassEntry = _CwoAoHttpxStatsAKCBypassEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1)
)
_CwoAoHttpxStatsAKCBypassCacheTrans_Type = Counter64
_CwoAoHttpxStatsAKCBypassCacheTrans_Object = MibScalar
cwoAoHttpxStatsAKCBypassCacheTrans = _CwoAoHttpxStatsAKCBypassCacheTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 1),
    _CwoAoHttpxStatsAKCBypassCacheTrans_Type()
)
cwoAoHttpxStatsAKCBypassCacheTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheTrans.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheTrans.setUnits("requests")
_CwoAoHttpxStatsAKCBypassRespBytes_Type = Counter64
_CwoAoHttpxStatsAKCBypassRespBytes_Object = MibScalar
cwoAoHttpxStatsAKCBypassRespBytes = _CwoAoHttpxStatsAKCBypassRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 2),
    _CwoAoHttpxStatsAKCBypassRespBytes_Type()
)
cwoAoHttpxStatsAKCBypassRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespBytes.setUnits("bytes")


class _CwoAoHttpxStatsAKCBypassCacheTransPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBypassCacheTransPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBypassCacheTransPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBypassCacheTransPercent_Object = MibScalar
cwoAoHttpxStatsAKCBypassCacheTransPercent = _CwoAoHttpxStatsAKCBypassCacheTransPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 3),
    _CwoAoHttpxStatsAKCBypassCacheTransPercent_Type()
)
cwoAoHttpxStatsAKCBypassCacheTransPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheTransPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheTransPercent.setUnits("percent")


class _CwoAoHttpxStatsAKCBypassRespBytesPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBypassRespBytesPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBypassRespBytesPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBypassRespBytesPercent_Object = MibScalar
cwoAoHttpxStatsAKCBypassRespBytesPercent = _CwoAoHttpxStatsAKCBypassRespBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 4),
    _CwoAoHttpxStatsAKCBypassRespBytesPercent_Type()
)
cwoAoHttpxStatsAKCBypassRespBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespBytesPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespBytesPercent.setUnits("percent")
_CwoAoHttpxStatsAKCBypassCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCBypassCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCBypassCacheRespTimeSaved = _CwoAoHttpxStatsAKCBypassCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 5),
    _CwoAoHttpxStatsAKCBypassCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCBypassCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassCacheRespTimeSaved.setUnits("milliseconds")
_CwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved = _CwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 6),
    _CwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved.setUnits("milliseconds")


class _CwoAoHttpxStatsAKCBypassRespTimeSavedPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBypassRespTimeSavedPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBypassRespTimeSavedPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBypassRespTimeSavedPercent_Object = MibScalar
cwoAoHttpxStatsAKCBypassRespTimeSavedPercent = _CwoAoHttpxStatsAKCBypassRespTimeSavedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 1, 7),
    _CwoAoHttpxStatsAKCBypassRespTimeSavedPercent_Type()
)
cwoAoHttpxStatsAKCBypassRespTimeSavedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespTimeSavedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBypassRespTimeSavedPercent.setUnits("percent")
_CwoAoHttpxStatsAKCStdEntry_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKCStdEntry = _CwoAoHttpxStatsAKCStdEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2)
)
_CwoAoHttpxStatsAKCStdCacheTrans_Type = Counter64
_CwoAoHttpxStatsAKCStdCacheTrans_Object = MibScalar
cwoAoHttpxStatsAKCStdCacheTrans = _CwoAoHttpxStatsAKCStdCacheTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 1),
    _CwoAoHttpxStatsAKCStdCacheTrans_Type()
)
cwoAoHttpxStatsAKCStdCacheTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheTrans.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheTrans.setUnits("requests")
_CwoAoHttpxStatsAKCStdRespBytes_Type = Counter64
_CwoAoHttpxStatsAKCStdRespBytes_Object = MibScalar
cwoAoHttpxStatsAKCStdRespBytes = _CwoAoHttpxStatsAKCStdRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 2),
    _CwoAoHttpxStatsAKCStdRespBytes_Type()
)
cwoAoHttpxStatsAKCStdRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespBytes.setUnits("bytes")


class _CwoAoHttpxStatsAKCStdCacheTransPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCStdCacheTransPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCStdCacheTransPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCStdCacheTransPercent_Object = MibScalar
cwoAoHttpxStatsAKCStdCacheTransPercent = _CwoAoHttpxStatsAKCStdCacheTransPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 3),
    _CwoAoHttpxStatsAKCStdCacheTransPercent_Type()
)
cwoAoHttpxStatsAKCStdCacheTransPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheTransPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheTransPercent.setUnits("percent")


class _CwoAoHttpxStatsAKCStdRespBytesPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCStdRespBytesPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCStdRespBytesPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCStdRespBytesPercent_Object = MibScalar
cwoAoHttpxStatsAKCStdRespBytesPercent = _CwoAoHttpxStatsAKCStdRespBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 4),
    _CwoAoHttpxStatsAKCStdRespBytesPercent_Type()
)
cwoAoHttpxStatsAKCStdRespBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespBytesPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespBytesPercent.setUnits("percent")
_CwoAoHttpxStatsAKCStdCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCStdCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCStdCacheRespTimeSaved = _CwoAoHttpxStatsAKCStdCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 5),
    _CwoAoHttpxStatsAKCStdCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCStdCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdCacheRespTimeSaved.setUnits("milliseconds")
_CwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved = _CwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 6),
    _CwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved.setUnits("milliseconds")


class _CwoAoHttpxStatsAKCStdRespTimeSavedPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCStdRespTimeSavedPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCStdRespTimeSavedPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCStdRespTimeSavedPercent_Object = MibScalar
cwoAoHttpxStatsAKCStdRespTimeSavedPercent = _CwoAoHttpxStatsAKCStdRespTimeSavedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 2, 7),
    _CwoAoHttpxStatsAKCStdRespTimeSavedPercent_Type()
)
cwoAoHttpxStatsAKCStdRespTimeSavedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespTimeSavedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCStdRespTimeSavedPercent.setUnits("percent")
_CwoAoHttpxStatsAKCBasicEntry_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKCBasicEntry = _CwoAoHttpxStatsAKCBasicEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3)
)
_CwoAoHttpxStatsAKCBasicCacheTrans_Type = Counter64
_CwoAoHttpxStatsAKCBasicCacheTrans_Object = MibScalar
cwoAoHttpxStatsAKCBasicCacheTrans = _CwoAoHttpxStatsAKCBasicCacheTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 1),
    _CwoAoHttpxStatsAKCBasicCacheTrans_Type()
)
cwoAoHttpxStatsAKCBasicCacheTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheTrans.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheTrans.setUnits("requests")
_CwoAoHttpxStatsAKCBasicRespBytes_Type = Counter64
_CwoAoHttpxStatsAKCBasicRespBytes_Object = MibScalar
cwoAoHttpxStatsAKCBasicRespBytes = _CwoAoHttpxStatsAKCBasicRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 2),
    _CwoAoHttpxStatsAKCBasicRespBytes_Type()
)
cwoAoHttpxStatsAKCBasicRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespBytes.setUnits("bytes")


class _CwoAoHttpxStatsAKCBasicCacheTransPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBasicCacheTransPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBasicCacheTransPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBasicCacheTransPercent_Object = MibScalar
cwoAoHttpxStatsAKCBasicCacheTransPercent = _CwoAoHttpxStatsAKCBasicCacheTransPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 3),
    _CwoAoHttpxStatsAKCBasicCacheTransPercent_Type()
)
cwoAoHttpxStatsAKCBasicCacheTransPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheTransPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheTransPercent.setUnits("percent")


class _CwoAoHttpxStatsAKCBasicRespBytesPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBasicRespBytesPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBasicRespBytesPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBasicRespBytesPercent_Object = MibScalar
cwoAoHttpxStatsAKCBasicRespBytesPercent = _CwoAoHttpxStatsAKCBasicRespBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 4),
    _CwoAoHttpxStatsAKCBasicRespBytesPercent_Type()
)
cwoAoHttpxStatsAKCBasicRespBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespBytesPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespBytesPercent.setUnits("percent")
_CwoAoHttpxStatsAKCBasicCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCBasicCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCBasicCacheRespTimeSaved = _CwoAoHttpxStatsAKCBasicCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 5),
    _CwoAoHttpxStatsAKCBasicCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCBasicCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicCacheRespTimeSaved.setUnits("milliseconds")
_CwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved = _CwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 6),
    _CwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved.setUnits("milliseconds")


class _CwoAoHttpxStatsAKCBasicRespTimeSavedPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCBasicRespTimeSavedPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCBasicRespTimeSavedPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCBasicRespTimeSavedPercent_Object = MibScalar
cwoAoHttpxStatsAKCBasicRespTimeSavedPercent = _CwoAoHttpxStatsAKCBasicRespTimeSavedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 3, 7),
    _CwoAoHttpxStatsAKCBasicRespTimeSavedPercent_Type()
)
cwoAoHttpxStatsAKCBasicRespTimeSavedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespTimeSavedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCBasicRespTimeSavedPercent.setUnits("percent")
_CwoAoHttpxStatsAKCAdvEntry_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKCAdvEntry = _CwoAoHttpxStatsAKCAdvEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4)
)
_CwoAoHttpxStatsAKCAdvCacheTrans_Type = Counter64
_CwoAoHttpxStatsAKCAdvCacheTrans_Object = MibScalar
cwoAoHttpxStatsAKCAdvCacheTrans = _CwoAoHttpxStatsAKCAdvCacheTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 1),
    _CwoAoHttpxStatsAKCAdvCacheTrans_Type()
)
cwoAoHttpxStatsAKCAdvCacheTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheTrans.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheTrans.setUnits("requests")
_CwoAoHttpxStatsAKCAdvRespBytes_Type = Counter64
_CwoAoHttpxStatsAKCAdvRespBytes_Object = MibScalar
cwoAoHttpxStatsAKCAdvRespBytes = _CwoAoHttpxStatsAKCAdvRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 2),
    _CwoAoHttpxStatsAKCAdvRespBytes_Type()
)
cwoAoHttpxStatsAKCAdvRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespBytes.setUnits("bytes")


class _CwoAoHttpxStatsAKCAdvCacheTransPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCAdvCacheTransPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCAdvCacheTransPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCAdvCacheTransPercent_Object = MibScalar
cwoAoHttpxStatsAKCAdvCacheTransPercent = _CwoAoHttpxStatsAKCAdvCacheTransPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 3),
    _CwoAoHttpxStatsAKCAdvCacheTransPercent_Type()
)
cwoAoHttpxStatsAKCAdvCacheTransPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheTransPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheTransPercent.setUnits("percent")


class _CwoAoHttpxStatsAKCAdvRespBytesPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCAdvRespBytesPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCAdvRespBytesPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCAdvRespBytesPercent_Object = MibScalar
cwoAoHttpxStatsAKCAdvRespBytesPercent = _CwoAoHttpxStatsAKCAdvRespBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 4),
    _CwoAoHttpxStatsAKCAdvRespBytesPercent_Type()
)
cwoAoHttpxStatsAKCAdvRespBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespBytesPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespBytesPercent.setUnits("percent")
_CwoAoHttpxStatsAKCAdvCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCAdvCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCAdvCacheRespTimeSaved = _CwoAoHttpxStatsAKCAdvCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 5),
    _CwoAoHttpxStatsAKCAdvCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCAdvCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvCacheRespTimeSaved.setUnits("milliseconds")
_CwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved = _CwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 6),
    _CwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved.setUnits("milliseconds")


class _CwoAoHttpxStatsAKCAdvRespTimeSavedPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCAdvRespTimeSavedPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCAdvRespTimeSavedPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCAdvRespTimeSavedPercent_Object = MibScalar
cwoAoHttpxStatsAKCAdvRespTimeSavedPercent = _CwoAoHttpxStatsAKCAdvRespTimeSavedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 4, 7),
    _CwoAoHttpxStatsAKCAdvRespTimeSavedPercent_Type()
)
cwoAoHttpxStatsAKCAdvRespTimeSavedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespTimeSavedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCAdvRespTimeSavedPercent.setUnits("percent")
_CwoAoHttpxStatsAKCTotalEntry_ObjectIdentity = ObjectIdentity
cwoAoHttpxStatsAKCTotalEntry = _CwoAoHttpxStatsAKCTotalEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5)
)
_CwoAoHttpxStatsAKCTotalCacheTrans_Type = Counter64
_CwoAoHttpxStatsAKCTotalCacheTrans_Object = MibScalar
cwoAoHttpxStatsAKCTotalCacheTrans = _CwoAoHttpxStatsAKCTotalCacheTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 1),
    _CwoAoHttpxStatsAKCTotalCacheTrans_Type()
)
cwoAoHttpxStatsAKCTotalCacheTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheTrans.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheTrans.setUnits("requests")
_CwoAoHttpxStatsAKCTotalRespBytes_Type = Counter64
_CwoAoHttpxStatsAKCTotalRespBytes_Object = MibScalar
cwoAoHttpxStatsAKCTotalRespBytes = _CwoAoHttpxStatsAKCTotalRespBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 2),
    _CwoAoHttpxStatsAKCTotalRespBytes_Type()
)
cwoAoHttpxStatsAKCTotalRespBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespBytes.setUnits("bytes")


class _CwoAoHttpxStatsAKCTotalCacheTransPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCTotalCacheTransPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCTotalCacheTransPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCTotalCacheTransPercent_Object = MibScalar
cwoAoHttpxStatsAKCTotalCacheTransPercent = _CwoAoHttpxStatsAKCTotalCacheTransPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 3),
    _CwoAoHttpxStatsAKCTotalCacheTransPercent_Type()
)
cwoAoHttpxStatsAKCTotalCacheTransPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheTransPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheTransPercent.setUnits("percent")


class _CwoAoHttpxStatsAKCTotalRespBytesPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCTotalRespBytesPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCTotalRespBytesPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCTotalRespBytesPercent_Object = MibScalar
cwoAoHttpxStatsAKCTotalRespBytesPercent = _CwoAoHttpxStatsAKCTotalRespBytesPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 4),
    _CwoAoHttpxStatsAKCTotalRespBytesPercent_Type()
)
cwoAoHttpxStatsAKCTotalRespBytesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespBytesPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespBytesPercent.setUnits("percent")
_CwoAoHttpxStatsAKCTotalCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCTotalCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCTotalCacheRespTimeSaved = _CwoAoHttpxStatsAKCTotalCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 5),
    _CwoAoHttpxStatsAKCTotalCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCTotalCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalCacheRespTimeSaved.setUnits("milliseconds")
_CwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved_Type = CiscoMilliSeconds
_CwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved_Object = MibScalar
cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved = _CwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 6),
    _CwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved_Type()
)
cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved.setUnits("milliseconds")


class _CwoAoHttpxStatsAKCTotalRespTimeSavedPercent_Type(Gauge32):
    """Custom type cwoAoHttpxStatsAKCTotalRespTimeSavedPercent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoHttpxStatsAKCTotalRespTimeSavedPercent_Type.__name__ = "Gauge32"
_CwoAoHttpxStatsAKCTotalRespTimeSavedPercent_Object = MibScalar
cwoAoHttpxStatsAKCTotalRespTimeSavedPercent = _CwoAoHttpxStatsAKCTotalRespTimeSavedPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 5, 7),
    _CwoAoHttpxStatsAKCTotalRespTimeSavedPercent_Type()
)
cwoAoHttpxStatsAKCTotalRespTimeSavedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespTimeSavedPercent.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCTotalRespTimeSavedPercent.setUnits("percent")
_CwoAoHttpxStatsAKCPrepTable_Object = MibTable
cwoAoHttpxStatsAKCPrepTable = _CwoAoHttpxStatsAKCPrepTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6)
)
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepTable.setStatus("current")
_CwoAoHttpxStatsAKCPrepEntry_Object = MibTableRow
cwoAoHttpxStatsAKCPrepEntry = _CwoAoHttpxStatsAKCPrepEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6, 1)
)
cwoAoHttpxStatsAKCPrepEntry.setIndexNames(
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCPrepTaskName"),
)
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepEntry.setStatus("current")


class _CwoAoHttpxStatsAKCPrepTaskName_Type(OctetString):
    """Custom type cwoAoHttpxStatsAKCPrepTaskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CwoAoHttpxStatsAKCPrepTaskName_Type.__name__ = "OctetString"
_CwoAoHttpxStatsAKCPrepTaskName_Object = MibTableColumn
cwoAoHttpxStatsAKCPrepTaskName = _CwoAoHttpxStatsAKCPrepTaskName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6, 1, 1),
    _CwoAoHttpxStatsAKCPrepTaskName_Type()
)
cwoAoHttpxStatsAKCPrepTaskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepTaskName.setStatus("current")
_CwoAoHttpxStatsAKCPrepStatus_Type = CwoHttpAKCPrepStatus
_CwoAoHttpxStatsAKCPrepStatus_Object = MibTableColumn
cwoAoHttpxStatsAKCPrepStatus = _CwoAoHttpxStatsAKCPrepStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6, 1, 2),
    _CwoAoHttpxStatsAKCPrepStatus_Type()
)
cwoAoHttpxStatsAKCPrepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepStatus.setStatus("current")
_CwoAoHttpxStatsAKCPrepCacheStoreBytes_Type = Gauge32
_CwoAoHttpxStatsAKCPrepCacheStoreBytes_Object = MibTableColumn
cwoAoHttpxStatsAKCPrepCacheStoreBytes = _CwoAoHttpxStatsAKCPrepCacheStoreBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6, 1, 3),
    _CwoAoHttpxStatsAKCPrepCacheStoreBytes_Type()
)
cwoAoHttpxStatsAKCPrepCacheStoreBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepCacheStoreBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepCacheStoreBytes.setUnits("bytes")
_CwoAoHttpxStatsAKCPrepUncacheStoreBytes_Type = Gauge32
_CwoAoHttpxStatsAKCPrepUncacheStoreBytes_Object = MibTableColumn
cwoAoHttpxStatsAKCPrepUncacheStoreBytes = _CwoAoHttpxStatsAKCPrepUncacheStoreBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 3, 10, 6, 1, 4),
    _CwoAoHttpxStatsAKCPrepUncacheStoreBytes_Type()
)
cwoAoHttpxStatsAKCPrepUncacheStoreBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepUncacheStoreBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoHttpxStatsAKCPrepUncacheStoreBytes.setUnits("bytes")
_CwoAoMapixStats_ObjectIdentity = ObjectIdentity
cwoAoMapixStats = _CwoAoMapixStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4)
)
_CwoAoMapixStatsUnEncrALRT_Type = CiscoMilliSeconds
_CwoAoMapixStatsUnEncrALRT_Object = MibScalar
cwoAoMapixStatsUnEncrALRT = _CwoAoMapixStatsUnEncrALRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 1),
    _CwoAoMapixStatsUnEncrALRT_Type()
)
cwoAoMapixStatsUnEncrALRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrALRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrALRT.setUnits("milliseconds")
_CwoAoMapixStatsEncrALRT_Type = CiscoMilliSeconds
_CwoAoMapixStatsEncrALRT_Object = MibScalar
cwoAoMapixStatsEncrALRT = _CwoAoMapixStatsEncrALRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 2),
    _CwoAoMapixStatsEncrALRT_Type()
)
cwoAoMapixStatsEncrALRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrALRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrALRT.setUnits("milliseconds")
_CwoAoMapixStatsUnEncrARRT_Type = CiscoMilliSeconds
_CwoAoMapixStatsUnEncrARRT_Object = MibScalar
cwoAoMapixStatsUnEncrARRT = _CwoAoMapixStatsUnEncrARRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 3),
    _CwoAoMapixStatsUnEncrARRT_Type()
)
cwoAoMapixStatsUnEncrARRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrARRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrARRT.setUnits("milliseconds")
_CwoAoMapixStatsEncrARRT_Type = CiscoMilliSeconds
_CwoAoMapixStatsEncrARRT_Object = MibScalar
cwoAoMapixStatsEncrARRT = _CwoAoMapixStatsEncrARRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 4),
    _CwoAoMapixStatsEncrARRT_Type()
)
cwoAoMapixStatsEncrARRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrARRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrARRT.setUnits("milliseconds")
_CwoAoMapixStatsTotalUnEncrLRs_Type = Counter64
_CwoAoMapixStatsTotalUnEncrLRs_Object = MibScalar
cwoAoMapixStatsTotalUnEncrLRs = _CwoAoMapixStatsTotalUnEncrLRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 5),
    _CwoAoMapixStatsTotalUnEncrLRs_Type()
)
cwoAoMapixStatsTotalUnEncrLRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalUnEncrLRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalUnEncrLRs.setUnits("requests")
_CwoAoMapixStatsTotalEncrLRs_Type = Counter64
_CwoAoMapixStatsTotalEncrLRs_Object = MibScalar
cwoAoMapixStatsTotalEncrLRs = _CwoAoMapixStatsTotalEncrLRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 6),
    _CwoAoMapixStatsTotalEncrLRs_Type()
)
cwoAoMapixStatsTotalEncrLRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalEncrLRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalEncrLRs.setUnits("requests")
_CwoAoMapixStatsTotalUnEncrRRs_Type = Counter64
_CwoAoMapixStatsTotalUnEncrRRs_Object = MibScalar
cwoAoMapixStatsTotalUnEncrRRs = _CwoAoMapixStatsTotalUnEncrRRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 7),
    _CwoAoMapixStatsTotalUnEncrRRs_Type()
)
cwoAoMapixStatsTotalUnEncrRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalUnEncrRRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalUnEncrRRs.setUnits("requests")
_CwoAoMapixStatsTotalEncrRRs_Type = Counter64
_CwoAoMapixStatsTotalEncrRRs_Object = MibScalar
cwoAoMapixStatsTotalEncrRRs = _CwoAoMapixStatsTotalEncrRRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 8),
    _CwoAoMapixStatsTotalEncrRRs_Type()
)
cwoAoMapixStatsTotalEncrRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalEncrRRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsTotalEncrRRs.setUnits("requests")
_CwoAoMapixStatsUnEncrAvgRedTime_Type = CiscoMilliSeconds
_CwoAoMapixStatsUnEncrAvgRedTime_Object = MibScalar
cwoAoMapixStatsUnEncrAvgRedTime = _CwoAoMapixStatsUnEncrAvgRedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 9),
    _CwoAoMapixStatsUnEncrAvgRedTime_Type()
)
cwoAoMapixStatsUnEncrAvgRedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrAvgRedTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsUnEncrAvgRedTime.setUnits("milliseconds")
_CwoAoMapixStatsEncrAvgRedTime_Type = CiscoMilliSeconds
_CwoAoMapixStatsEncrAvgRedTime_Object = MibScalar
cwoAoMapixStatsEncrAvgRedTime = _CwoAoMapixStatsEncrAvgRedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 4, 10),
    _CwoAoMapixStatsEncrAvgRedTime_Type()
)
cwoAoMapixStatsEncrAvgRedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrAvgRedTime.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoMapixStatsEncrAvgRedTime.setUnits("milliseconds")
_CwoAoNfsxStats_ObjectIdentity = ObjectIdentity
cwoAoNfsxStats = _CwoAoNfsxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5)
)
_CwoAoNfsxStatsALRT_Type = CiscoMilliSeconds
_CwoAoNfsxStatsALRT_Object = MibScalar
cwoAoNfsxStatsALRT = _CwoAoNfsxStatsALRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5, 1),
    _CwoAoNfsxStatsALRT_Type()
)
cwoAoNfsxStatsALRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsALRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsALRT.setUnits("milliseconds")
_CwoAoNfsxStatsARRT_Type = CiscoMilliSeconds
_CwoAoNfsxStatsARRT_Object = MibScalar
cwoAoNfsxStatsARRT = _CwoAoNfsxStatsARRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5, 2),
    _CwoAoNfsxStatsARRT_Type()
)
cwoAoNfsxStatsARRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsARRT.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsARRT.setUnits("milliseconds")
_CwoAoNfsxStatsTotalLRs_Type = Counter64
_CwoAoNfsxStatsTotalLRs_Object = MibScalar
cwoAoNfsxStatsTotalLRs = _CwoAoNfsxStatsTotalLRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5, 3),
    _CwoAoNfsxStatsTotalLRs_Type()
)
cwoAoNfsxStatsTotalLRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsTotalLRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsTotalLRs.setUnits("requests")
_CwoAoNfsxStatsTotalRRs_Type = Counter64
_CwoAoNfsxStatsTotalRRs_Object = MibScalar
cwoAoNfsxStatsTotalRRs = _CwoAoNfsxStatsTotalRRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5, 4),
    _CwoAoNfsxStatsTotalRRs_Type()
)
cwoAoNfsxStatsTotalRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsTotalRRs.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsTotalRRs.setUnits("requests")


class _CwoAoNfsxStatsEstTimeSaved_Type(Gauge32):
    """Custom type cwoAoNfsxStatsEstTimeSaved based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoNfsxStatsEstTimeSaved_Type.__name__ = "Gauge32"
_CwoAoNfsxStatsEstTimeSaved_Object = MibScalar
cwoAoNfsxStatsEstTimeSaved = _CwoAoNfsxStatsEstTimeSaved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 5, 5),
    _CwoAoNfsxStatsEstTimeSaved_Type()
)
cwoAoNfsxStatsEstTimeSaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsEstTimeSaved.setStatus("current")
if mibBuilder.loadTexts:
    cwoAoNfsxStatsEstTimeSaved.setUnits("percent")
_CwoAoVideoxStats_ObjectIdentity = ObjectIdentity
cwoAoVideoxStats = _CwoAoVideoxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 6)
)
_CwoAoVideoxStatsTotalInBytes_Type = Counter64
_CwoAoVideoxStatsTotalInBytes_Object = MibScalar
cwoAoVideoxStatsTotalInBytes = _CwoAoVideoxStatsTotalInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 6, 1),
    _CwoAoVideoxStatsTotalInBytes_Type()
)
cwoAoVideoxStatsTotalInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoVideoxStatsTotalInBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoVideoxStatsTotalInBytes.setUnits("bytes")
_CwoAoVideoxStatsTotalOutBytes_Type = Counter64
_CwoAoVideoxStatsTotalOutBytes_Object = MibScalar
cwoAoVideoxStatsTotalOutBytes = _CwoAoVideoxStatsTotalOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 6, 2),
    _CwoAoVideoxStatsTotalOutBytes_Type()
)
cwoAoVideoxStatsTotalOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoVideoxStatsTotalOutBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoVideoxStatsTotalOutBytes.setUnits("bytes")
_CwoAoCifsxStats_ObjectIdentity = ObjectIdentity
cwoAoCifsxStats = _CwoAoCifsxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7)
)
_CwoAoCifsxStatsTotalReadBytes_Type = Counter32
_CwoAoCifsxStatsTotalReadBytes_Object = MibScalar
cwoAoCifsxStatsTotalReadBytes = _CwoAoCifsxStatsTotalReadBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 1),
    _CwoAoCifsxStatsTotalReadBytes_Type()
)
cwoAoCifsxStatsTotalReadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalReadBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalReadBytes.setUnits("kilo-bytes")
_CwoAoCifsxStatsTotalWrittenBytes_Type = Counter32
_CwoAoCifsxStatsTotalWrittenBytes_Object = MibScalar
cwoAoCifsxStatsTotalWrittenBytes = _CwoAoCifsxStatsTotalWrittenBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 2),
    _CwoAoCifsxStatsTotalWrittenBytes_Type()
)
cwoAoCifsxStatsTotalWrittenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalWrittenBytes.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalWrittenBytes.setUnits("kilo-bytes")
_CwoAoCifsxStatsTotalRemoteReqs_Type = Counter32
_CwoAoCifsxStatsTotalRemoteReqs_Object = MibScalar
cwoAoCifsxStatsTotalRemoteReqs = _CwoAoCifsxStatsTotalRemoteReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 3),
    _CwoAoCifsxStatsTotalRemoteReqs_Type()
)
cwoAoCifsxStatsTotalRemoteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalRemoteReqs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalRemoteReqs.setUnits("requests")
_CwoAoCifsxStatsTotalLocalReqs_Type = Counter32
_CwoAoCifsxStatsTotalLocalReqs_Object = MibScalar
cwoAoCifsxStatsTotalLocalReqs = _CwoAoCifsxStatsTotalLocalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 4),
    _CwoAoCifsxStatsTotalLocalReqs_Type()
)
cwoAoCifsxStatsTotalLocalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalLocalReqs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalLocalReqs.setUnits("requests")
_CwoAoCifsxStatsTotalRemoteTime_Type = CiscoMilliSeconds
_CwoAoCifsxStatsTotalRemoteTime_Object = MibScalar
cwoAoCifsxStatsTotalRemoteTime = _CwoAoCifsxStatsTotalRemoteTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 5),
    _CwoAoCifsxStatsTotalRemoteTime_Type()
)
cwoAoCifsxStatsTotalRemoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalRemoteTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalRemoteTime.setUnits("milliseconds")
_CwoAoCifsxStatsTotalLocalTime_Type = CiscoMilliSeconds
_CwoAoCifsxStatsTotalLocalTime_Object = MibScalar
cwoAoCifsxStatsTotalLocalTime = _CwoAoCifsxStatsTotalLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 6),
    _CwoAoCifsxStatsTotalLocalTime_Type()
)
cwoAoCifsxStatsTotalLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalLocalTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsTotalLocalTime.setUnits("milliseconds")
_CwoAoCifsxStatsConnectedSessions_Type = Gauge32
_CwoAoCifsxStatsConnectedSessions_Object = MibScalar
cwoAoCifsxStatsConnectedSessions = _CwoAoCifsxStatsConnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 7),
    _CwoAoCifsxStatsConnectedSessions_Type()
)
cwoAoCifsxStatsConnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsConnectedSessions.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsConnectedSessions.setUnits("sessions")
_CwoAoCifsxStatsOpenFiles_Type = Gauge32
_CwoAoCifsxStatsOpenFiles_Object = MibScalar
cwoAoCifsxStatsOpenFiles = _CwoAoCifsxStatsOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 8),
    _CwoAoCifsxStatsOpenFiles_Type()
)
cwoAoCifsxStatsOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsOpenFiles.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsOpenFiles.setUnits("files")
_CwoAoCifsxStatsMaxCacheSize_Type = Gauge32
_CwoAoCifsxStatsMaxCacheSize_Object = MibScalar
cwoAoCifsxStatsMaxCacheSize = _CwoAoCifsxStatsMaxCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 9),
    _CwoAoCifsxStatsMaxCacheSize_Type()
)
cwoAoCifsxStatsMaxCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsMaxCacheSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsMaxCacheSize.setUnits("kilo-bytes")
_CwoAoCifsxStatsCurrentCacheSize_Type = Gauge32
_CwoAoCifsxStatsCurrentCacheSize_Object = MibScalar
cwoAoCifsxStatsCurrentCacheSize = _CwoAoCifsxStatsCurrentCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 10),
    _CwoAoCifsxStatsCurrentCacheSize_Type()
)
cwoAoCifsxStatsCurrentCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsCurrentCacheSize.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsCurrentCacheSize.setUnits("kilo-bytes")
_CwoAoCifsxStatsMaxCacheResources_Type = Gauge32
_CwoAoCifsxStatsMaxCacheResources_Object = MibScalar
cwoAoCifsxStatsMaxCacheResources = _CwoAoCifsxStatsMaxCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 11),
    _CwoAoCifsxStatsMaxCacheResources_Type()
)
cwoAoCifsxStatsMaxCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsMaxCacheResources.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsMaxCacheResources.setUnits("files")
_CwoAoCifsxStatsCacheResources_Type = Gauge32
_CwoAoCifsxStatsCacheResources_Object = MibScalar
cwoAoCifsxStatsCacheResources = _CwoAoCifsxStatsCacheResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 12),
    _CwoAoCifsxStatsCacheResources_Type()
)
cwoAoCifsxStatsCacheResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsCacheResources.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsCacheResources.setUnits("files")
_CwoAoCifsxStatsEvictedResources_Type = Counter32
_CwoAoCifsxStatsEvictedResources_Object = MibScalar
cwoAoCifsxStatsEvictedResources = _CwoAoCifsxStatsEvictedResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 13),
    _CwoAoCifsxStatsEvictedResources_Type()
)
cwoAoCifsxStatsEvictedResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsEvictedResources.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsEvictedResources.setUnits("files")
_CwoAoCifsxStatsLastEvictedTime_Type = TimeStamp
_CwoAoCifsxStatsLastEvictedTime_Object = MibScalar
cwoAoCifsxStatsLastEvictedTime = _CwoAoCifsxStatsLastEvictedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 14),
    _CwoAoCifsxStatsLastEvictedTime_Type()
)
cwoAoCifsxStatsLastEvictedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsLastEvictedTime.setStatus("deprecated")


class _CwoAoCifsxStatsVolHiWatermark_Type(Gauge32):
    """Custom type cwoAoCifsxStatsVolHiWatermark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoCifsxStatsVolHiWatermark_Type.__name__ = "Gauge32"
_CwoAoCifsxStatsVolHiWatermark_Object = MibScalar
cwoAoCifsxStatsVolHiWatermark = _CwoAoCifsxStatsVolHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 15),
    _CwoAoCifsxStatsVolHiWatermark_Type()
)
cwoAoCifsxStatsVolHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsVolHiWatermark.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsVolHiWatermark.setUnits("percent")


class _CwoAoCifsxStatsVolLoWatermark_Type(Gauge32):
    """Custom type cwoAoCifsxStatsVolLoWatermark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoCifsxStatsVolLoWatermark_Type.__name__ = "Gauge32"
_CwoAoCifsxStatsVolLoWatermark_Object = MibScalar
cwoAoCifsxStatsVolLoWatermark = _CwoAoCifsxStatsVolLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 16),
    _CwoAoCifsxStatsVolLoWatermark_Type()
)
cwoAoCifsxStatsVolLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsVolLoWatermark.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsVolLoWatermark.setUnits("percent")


class _CwoAoCifsxStatsAmntHiWatermark_Type(Gauge32):
    """Custom type cwoAoCifsxStatsAmntHiWatermark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoCifsxStatsAmntHiWatermark_Type.__name__ = "Gauge32"
_CwoAoCifsxStatsAmntHiWatermark_Object = MibScalar
cwoAoCifsxStatsAmntHiWatermark = _CwoAoCifsxStatsAmntHiWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 17),
    _CwoAoCifsxStatsAmntHiWatermark_Type()
)
cwoAoCifsxStatsAmntHiWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsAmntHiWatermark.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsAmntHiWatermark.setUnits("percent")


class _CwoAoCifsxStatsAmntLoWatermark_Type(Gauge32):
    """Custom type cwoAoCifsxStatsAmntLoWatermark based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwoAoCifsxStatsAmntLoWatermark_Type.__name__ = "Gauge32"
_CwoAoCifsxStatsAmntLoWatermark_Object = MibScalar
cwoAoCifsxStatsAmntLoWatermark = _CwoAoCifsxStatsAmntLoWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 18),
    _CwoAoCifsxStatsAmntLoWatermark_Type()
)
cwoAoCifsxStatsAmntLoWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsAmntLoWatermark.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsAmntLoWatermark.setUnits("percent")
_CwoAoCifsxStatsEvictedAge_Type = TimeInterval
_CwoAoCifsxStatsEvictedAge_Object = MibScalar
cwoAoCifsxStatsEvictedAge = _CwoAoCifsxStatsEvictedAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 19),
    _CwoAoCifsxStatsEvictedAge_Type()
)
cwoAoCifsxStatsEvictedAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsEvictedAge.setStatus("deprecated")
_CwoAoCifsxStatsEvictedLastAccess_Type = TimeStamp
_CwoAoCifsxStatsEvictedLastAccess_Object = MibScalar
cwoAoCifsxStatsEvictedLastAccess = _CwoAoCifsxStatsEvictedLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 20),
    _CwoAoCifsxStatsEvictedLastAccess_Type()
)
cwoAoCifsxStatsEvictedLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsEvictedLastAccess.setStatus("deprecated")
_CwoAoCifsxStatsFFTotalReqs_Type = Counter64
_CwoAoCifsxStatsFFTotalReqs_Object = MibScalar
cwoAoCifsxStatsFFTotalReqs = _CwoAoCifsxStatsFFTotalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 21),
    _CwoAoCifsxStatsFFTotalReqs_Type()
)
cwoAoCifsxStatsFFTotalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFTotalReqs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFTotalReqs.setUnits("requests")
_CwoAoCifsxStatsFFRemoteReqs_Type = Counter64
_CwoAoCifsxStatsFFRemoteReqs_Object = MibScalar
cwoAoCifsxStatsFFRemoteReqs = _CwoAoCifsxStatsFFRemoteReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 22),
    _CwoAoCifsxStatsFFRemoteReqs_Type()
)
cwoAoCifsxStatsFFRemoteReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFRemoteReqs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFRemoteReqs.setUnits("requests")
_CwoAoCifsxStatsFFLocalRespTime_Type = CiscoMilliSeconds
_CwoAoCifsxStatsFFLocalRespTime_Object = MibScalar
cwoAoCifsxStatsFFLocalRespTime = _CwoAoCifsxStatsFFLocalRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 23),
    _CwoAoCifsxStatsFFLocalRespTime_Type()
)
cwoAoCifsxStatsFFLocalRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFLocalRespTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFLocalRespTime.setUnits("milliseconds")
_CwoAoCifsxStatsFFRemoteRespTime_Type = CiscoMilliSeconds
_CwoAoCifsxStatsFFRemoteRespTime_Object = MibScalar
cwoAoCifsxStatsFFRemoteRespTime = _CwoAoCifsxStatsFFRemoteRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 24),
    _CwoAoCifsxStatsFFRemoteRespTime_Type()
)
cwoAoCifsxStatsFFRemoteRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFRemoteRespTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsFFRemoteRespTime.setUnits("milliseconds")
_CwoAoCifsxStatsDirResources_Type = Gauge32
_CwoAoCifsxStatsDirResources_Object = MibScalar
cwoAoCifsxStatsDirResources = _CwoAoCifsxStatsDirResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 3, 7, 25),
    _CwoAoCifsxStatsDirResources_Type()
)
cwoAoCifsxStatsDirResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsDirResources.setStatus("deprecated")
if mibBuilder.loadTexts:
    cwoAoCifsxStatsDirResources.setUnits("files")
_CwoApp_ObjectIdentity = ObjectIdentity
cwoApp = _CwoApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4)
)
_CwoAppStatsTable_Object = MibTable
cwoAppStatsTable = _CwoAppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cwoAppStatsTable.setStatus("current")
_CwoAppStatsEntry_Object = MibTableRow
cwoAppStatsEntry = _CwoAppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1, 1)
)
cwoAppStatsEntry.setIndexNames(
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoAppStatsAppName"),
)
if mibBuilder.loadTexts:
    cwoAppStatsEntry.setStatus("current")
_CwoAppStatsAppName_Type = SnmpAdminString
_CwoAppStatsAppName_Object = MibTableColumn
cwoAppStatsAppName = _CwoAppStatsAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1, 1, 1),
    _CwoAppStatsAppName_Type()
)
cwoAppStatsAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoAppStatsAppName.setStatus("current")
_CwoAppStatsOriginalBytes_Type = Counter64
_CwoAppStatsOriginalBytes_Object = MibTableColumn
cwoAppStatsOriginalBytes = _CwoAppStatsOriginalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1, 1, 2),
    _CwoAppStatsOriginalBytes_Type()
)
cwoAppStatsOriginalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAppStatsOriginalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAppStatsOriginalBytes.setUnits("bytes")
_CwoAppStatsOptimizedBytes_Type = Counter64
_CwoAppStatsOptimizedBytes_Object = MibTableColumn
cwoAppStatsOptimizedBytes = _CwoAppStatsOptimizedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1, 1, 3),
    _CwoAppStatsOptimizedBytes_Type()
)
cwoAppStatsOptimizedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAppStatsOptimizedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAppStatsOptimizedBytes.setUnits("bytes")
_CwoAppStatsPTBytes_Type = Counter64
_CwoAppStatsPTBytes_Object = MibTableColumn
cwoAppStatsPTBytes = _CwoAppStatsPTBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 4, 1, 1, 4),
    _CwoAppStatsPTBytes_Type()
)
cwoAppStatsPTBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoAppStatsPTBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoAppStatsPTBytes.setUnits("bytes")
_CwoPmap_ObjectIdentity = ObjectIdentity
cwoPmap = _CwoPmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5)
)
_CwoPmapStatsTable_Object = MibTable
cwoPmapStatsTable = _CwoPmapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cwoPmapStatsTable.setStatus("current")
_CwoPmapStatsEntry_Object = MibTableRow
cwoPmapStatsEntry = _CwoPmapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1)
)
cwoPmapStatsEntry.setIndexNames(
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsType"),
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsName"),
)
if mibBuilder.loadTexts:
    cwoPmapStatsEntry.setStatus("current")
_CwoPmapStatsType_Type = CwoTypes
_CwoPmapStatsType_Object = MibTableColumn
cwoPmapStatsType = _CwoPmapStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 1),
    _CwoPmapStatsType_Type()
)
cwoPmapStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoPmapStatsType.setStatus("current")
_CwoPmapStatsName_Type = SnmpAdminString
_CwoPmapStatsName_Object = MibTableColumn
cwoPmapStatsName = _CwoPmapStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 2),
    _CwoPmapStatsName_Type()
)
cwoPmapStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoPmapStatsName.setStatus("current")
_CwoPmapStatsDescr_Type = SnmpAdminString
_CwoPmapStatsDescr_Object = MibTableColumn
cwoPmapStatsDescr = _CwoPmapStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 3),
    _CwoPmapStatsDescr_Type()
)
cwoPmapStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoPmapStatsDescr.setStatus("current")
_CwoPmapStatsTotalConns_Type = Counter64
_CwoPmapStatsTotalConns_Object = MibTableColumn
cwoPmapStatsTotalConns = _CwoPmapStatsTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 4),
    _CwoPmapStatsTotalConns_Type()
)
cwoPmapStatsTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalConns.setStatus("current")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalConns.setUnits("connections")
_CwoPmapStatsTotalBytes_Type = Counter64
_CwoPmapStatsTotalBytes_Object = MibTableColumn
cwoPmapStatsTotalBytes = _CwoPmapStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 5),
    _CwoPmapStatsTotalBytes_Type()
)
cwoPmapStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalBytes.setUnits("kilo-bytes")
_CwoPmapStatsTotalPTConns_Type = Counter64
_CwoPmapStatsTotalPTConns_Object = MibTableColumn
cwoPmapStatsTotalPTConns = _CwoPmapStatsTotalPTConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 6),
    _CwoPmapStatsTotalPTConns_Type()
)
cwoPmapStatsTotalPTConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalPTConns.setStatus("current")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalPTConns.setUnits("connections")
_CwoPmapStatsTotalPTBytes_Type = Counter64
_CwoPmapStatsTotalPTBytes_Object = MibTableColumn
cwoPmapStatsTotalPTBytes = _CwoPmapStatsTotalPTBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 5, 1, 1, 7),
    _CwoPmapStatsTotalPTBytes_Type()
)
cwoPmapStatsTotalPTBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalPTBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoPmapStatsTotalPTBytes.setUnits("kilo-bytes")
_CwoCmap_ObjectIdentity = ObjectIdentity
cwoCmap = _CwoCmap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6)
)
_CwoCmapStatsTable_Object = MibTable
cwoCmapStatsTable = _CwoCmapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cwoCmapStatsTable.setStatus("current")
_CwoCmapStatsEntry_Object = MibTableRow
cwoCmapStatsEntry = _CwoCmapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1)
)
cwoCmapStatsEntry.setIndexNames(
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsType"),
    (0, "CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsName"),
)
if mibBuilder.loadTexts:
    cwoCmapStatsEntry.setStatus("current")
_CwoCmapStatsType_Type = CwoTypes
_CwoCmapStatsType_Object = MibTableColumn
cwoCmapStatsType = _CwoCmapStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 1),
    _CwoCmapStatsType_Type()
)
cwoCmapStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoCmapStatsType.setStatus("current")
_CwoCmapStatsName_Type = SnmpAdminString
_CwoCmapStatsName_Object = MibTableColumn
cwoCmapStatsName = _CwoCmapStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 2),
    _CwoCmapStatsName_Type()
)
cwoCmapStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwoCmapStatsName.setStatus("current")
_CwoCmapStatsDescr_Type = SnmpAdminString
_CwoCmapStatsDescr_Object = MibTableColumn
cwoCmapStatsDescr = _CwoCmapStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 3),
    _CwoCmapStatsDescr_Type()
)
cwoCmapStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoCmapStatsDescr.setStatus("current")
_CwoCmapStatsTotalConns_Type = Counter64
_CwoCmapStatsTotalConns_Object = MibTableColumn
cwoCmapStatsTotalConns = _CwoCmapStatsTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 4),
    _CwoCmapStatsTotalConns_Type()
)
cwoCmapStatsTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalConns.setStatus("current")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalConns.setUnits("connections")
_CwoCmapStatsTotalBytes_Type = Counter64
_CwoCmapStatsTotalBytes_Object = MibTableColumn
cwoCmapStatsTotalBytes = _CwoCmapStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 5),
    _CwoCmapStatsTotalBytes_Type()
)
cwoCmapStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalBytes.setUnits("bytes")
_CwoCmapStatsTotalPTConns_Type = Counter64
_CwoCmapStatsTotalPTConns_Object = MibTableColumn
cwoCmapStatsTotalPTConns = _CwoCmapStatsTotalPTConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 6),
    _CwoCmapStatsTotalPTConns_Type()
)
cwoCmapStatsTotalPTConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalPTConns.setStatus("current")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalPTConns.setUnits("connections")
_CwoCmapStatsTotalPTBytes_Type = Counter64
_CwoCmapStatsTotalPTBytes_Object = MibTableColumn
cwoCmapStatsTotalPTBytes = _CwoCmapStatsTotalPTBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 6, 1, 1, 7),
    _CwoCmapStatsTotalPTBytes_Type()
)
cwoCmapStatsTotalPTBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalPTBytes.setStatus("current")
if mibBuilder.loadTexts:
    cwoCmapStatsTotalPTBytes.setUnits("bytes")
_CwoDre_ObjectIdentity = ObjectIdentity
cwoDre = _CwoDre_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7)
)
_CwoDreCacheStats_ObjectIdentity = ObjectIdentity
cwoDreCacheStats = _CwoDreCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1)
)
_CwoDreCacheStatsStatus_Type = CwoDreCacheStatus
_CwoDreCacheStatsStatus_Object = MibScalar
cwoDreCacheStatsStatus = _CwoDreCacheStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 1),
    _CwoDreCacheStatsStatus_Type()
)
cwoDreCacheStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsStatus.setStatus("current")
_CwoDreCacheStatsAge_Type = SnmpAdminString
_CwoDreCacheStatsAge_Object = MibScalar
cwoDreCacheStatsAge = _CwoDreCacheStatsAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 2),
    _CwoDreCacheStatsAge_Type()
)
cwoDreCacheStatsAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsAge.setStatus("current")
_CwoDreCacheStatsTotal_Type = Unsigned32
_CwoDreCacheStatsTotal_Object = MibScalar
cwoDreCacheStatsTotal = _CwoDreCacheStatsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 3),
    _CwoDreCacheStatsTotal_Type()
)
cwoDreCacheStatsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsTotal.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsTotal.setUnits("MB")
_CwoDreCacheStatsUsed_Type = Gauge32
_CwoDreCacheStatsUsed_Object = MibScalar
cwoDreCacheStatsUsed = _CwoDreCacheStatsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 4),
    _CwoDreCacheStatsUsed_Type()
)
cwoDreCacheStatsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsUsed.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsUsed.setUnits("percent")
_CwoDreCacheStatsDataUnitUsage_Type = Unsigned32
_CwoDreCacheStatsDataUnitUsage_Object = MibScalar
cwoDreCacheStatsDataUnitUsage = _CwoDreCacheStatsDataUnitUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 5),
    _CwoDreCacheStatsDataUnitUsage_Type()
)
cwoDreCacheStatsDataUnitUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsDataUnitUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsDataUnitUsage.setUnits("MB")
_CwoDreCacheStatsReplacedOneHrDataUnit_Type = Unsigned32
_CwoDreCacheStatsReplacedOneHrDataUnit_Object = MibScalar
cwoDreCacheStatsReplacedOneHrDataUnit = _CwoDreCacheStatsReplacedOneHrDataUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 6),
    _CwoDreCacheStatsReplacedOneHrDataUnit_Type()
)
cwoDreCacheStatsReplacedOneHrDataUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsReplacedOneHrDataUnit.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsReplacedOneHrDataUnit.setUnits("MB")
_CwoDreCacheStatsDataUnitAge_Type = SnmpAdminString
_CwoDreCacheStatsDataUnitAge_Object = MibScalar
cwoDreCacheStatsDataUnitAge = _CwoDreCacheStatsDataUnitAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 7),
    _CwoDreCacheStatsDataUnitAge_Type()
)
cwoDreCacheStatsDataUnitAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsDataUnitAge.setStatus("current")
_CwoDreCacheStatsSigblockUsage_Type = Unsigned32
_CwoDreCacheStatsSigblockUsage_Object = MibScalar
cwoDreCacheStatsSigblockUsage = _CwoDreCacheStatsSigblockUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 8),
    _CwoDreCacheStatsSigblockUsage_Type()
)
cwoDreCacheStatsSigblockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsSigblockUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsSigblockUsage.setUnits("MB")
_CwoDreCacheStatsReplacedOneHrSigblock_Type = Unsigned32
_CwoDreCacheStatsReplacedOneHrSigblock_Object = MibScalar
cwoDreCacheStatsReplacedOneHrSigblock = _CwoDreCacheStatsReplacedOneHrSigblock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 9),
    _CwoDreCacheStatsReplacedOneHrSigblock_Type()
)
cwoDreCacheStatsReplacedOneHrSigblock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsReplacedOneHrSigblock.setStatus("current")
if mibBuilder.loadTexts:
    cwoDreCacheStatsReplacedOneHrSigblock.setUnits("MB")
_CwoDreCacheStatsSigblockAge_Type = SnmpAdminString
_CwoDreCacheStatsSigblockAge_Object = MibScalar
cwoDreCacheStatsSigblockAge = _CwoDreCacheStatsSigblockAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 1, 10),
    _CwoDreCacheStatsSigblockAge_Type()
)
cwoDreCacheStatsSigblockAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDreCacheStatsSigblockAge.setStatus("current")
_CwoDrePerfStats_ObjectIdentity = ObjectIdentity
cwoDrePerfStats = _CwoDrePerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2)
)


class _CwoDrePerfStatsEncodeCompressionRatio_Type(Gauge32):
    """Custom type cwoDrePerfStatsEncodeCompressionRatio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwoDrePerfStatsEncodeCompressionRatio_Type.__name__ = "Gauge32"
_CwoDrePerfStatsEncodeCompressionRatio_Object = MibScalar
cwoDrePerfStatsEncodeCompressionRatio = _CwoDrePerfStatsEncodeCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 1),
    _CwoDrePerfStatsEncodeCompressionRatio_Type()
)
cwoDrePerfStatsEncodeCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeCompressionRatio.setUnits("percent")
_CwoDrePerfStatsEncodeCompressionLatency_Type = Unsigned32
_CwoDrePerfStatsEncodeCompressionLatency_Object = MibScalar
cwoDrePerfStatsEncodeCompressionLatency = _CwoDrePerfStatsEncodeCompressionLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 2),
    _CwoDrePerfStatsEncodeCompressionLatency_Type()
)
cwoDrePerfStatsEncodeCompressionLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeCompressionLatency.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeCompressionLatency.setUnits("ms")
_CwoDrePerfStatsEncodeAvgMsgSize_Type = Unsigned32
_CwoDrePerfStatsEncodeAvgMsgSize_Object = MibScalar
cwoDrePerfStatsEncodeAvgMsgSize = _CwoDrePerfStatsEncodeAvgMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 3),
    _CwoDrePerfStatsEncodeAvgMsgSize_Type()
)
cwoDrePerfStatsEncodeAvgMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeAvgMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsEncodeAvgMsgSize.setUnits("bytes")


class _CwoDrePerfStatsDecodeCompressionRatio_Type(Gauge32):
    """Custom type cwoDrePerfStatsDecodeCompressionRatio based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CwoDrePerfStatsDecodeCompressionRatio_Type.__name__ = "Gauge32"
_CwoDrePerfStatsDecodeCompressionRatio_Object = MibScalar
cwoDrePerfStatsDecodeCompressionRatio = _CwoDrePerfStatsDecodeCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 4),
    _CwoDrePerfStatsDecodeCompressionRatio_Type()
)
cwoDrePerfStatsDecodeCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeCompressionRatio.setUnits("percent")
_CwoDrePerfStatsDecodeCompressionLatency_Type = Unsigned32
_CwoDrePerfStatsDecodeCompressionLatency_Object = MibScalar
cwoDrePerfStatsDecodeCompressionLatency = _CwoDrePerfStatsDecodeCompressionLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 5),
    _CwoDrePerfStatsDecodeCompressionLatency_Type()
)
cwoDrePerfStatsDecodeCompressionLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeCompressionLatency.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeCompressionLatency.setUnits("ms")
_CwoDrePerfStatsDecodeAvgMsgSize_Type = Unsigned32
_CwoDrePerfStatsDecodeAvgMsgSize_Object = MibScalar
cwoDrePerfStatsDecodeAvgMsgSize = _CwoDrePerfStatsDecodeAvgMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 1, 7, 2, 6),
    _CwoDrePerfStatsDecodeAvgMsgSize_Type()
)
cwoDrePerfStatsDecodeAvgMsgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeAvgMsgSize.setStatus("current")
if mibBuilder.loadTexts:
    cwoDrePerfStatsDecodeAvgMsgSize.setUnits("bytes")
_CiscoWanOptimizationMIBConform_ObjectIdentity = ObjectIdentity
ciscoWanOptimizationMIBConform = _CiscoWanOptimizationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3)
)
_CiscoWanOptimizationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanOptimizationMIBCompliances = _CiscoWanOptimizationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1)
)
_CiscoWanOptimizationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanOptimizationMIBGroups = _CiscoWanOptimizationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2)
)

# Managed Objects groups

cwoGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 1)
)
cwoGeneralGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralActivePeers"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralMaxActivePeers"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottleHigh"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottleLow"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottlPeriod"))
)
if mibBuilder.loadTexts:
    cwoGeneralGroup.setStatus("current")

cwoTfoBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 2)
)
cwoTfoBaseGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsTotalOptConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActiveOptConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsMaxActiveConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsTotalNormalClosedConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsResetConn"))
)
if mibBuilder.loadTexts:
    cwoTfoBaseGroup.setStatus("current")

cwoTfoExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 3)
)
cwoTfoExtGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActiveOptTCPPlusConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActiveOptTCPOnlyConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActiveOptTCPPrepConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActiveADConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsReservedConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsPendingConn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsActivePTConn"))
)
if mibBuilder.loadTexts:
    cwoTfoExtGroup.setStatus("current")

cwoAoStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 4)
)
cwoAoStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsIsConfigured"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsIsLicensed"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsOperationalState"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsStartUpTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsTotalHandledConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsTotalOptConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsTotalHandedOffConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsTotalDroppedConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsActiveOptConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsPendingConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsMaxActiveOptConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsLastResetTime"))
)
if mibBuilder.loadTexts:
    cwoAoStatsGroup.setStatus("current")

cwoAoSmbExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 7)
)
cwoAoSmbExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesReadCache"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesWriteCache"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesReadServer"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesWriteServer"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesReadClient"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsBytesWriteClient"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsProcessedReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsActiveReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsTotalTimedOutReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsTotalRemoteReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsTotalLocalReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRemoteAvgTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsLocalAvgTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRACacheHitCount"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsMDCacheHitCount"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRACacheHitRate"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsMDCacheHitRate"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsMaxRACacheSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsMaxMDCacheSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsMDCacheSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRAEvictedAge"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRTT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsTotalRespTimeSaving"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsOpenFiles"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsTotalFilesInRACache"))
)
if mibBuilder.loadTexts:
    cwoAoSmbExtendedStatsGroup.setStatus("current")

cwoAoHttpExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 9)
)
cwoAoHttpExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSavedTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalRTT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalMDCMTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsEstSavedTime"))
)
if mibBuilder.loadTexts:
    cwoAoHttpExtendedStatsGroup.setStatus("current")

cwoAoMapiExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 10)
)
cwoAoMapiExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsUnEncrALRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsUnEncrARRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsTotalUnEncrLRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsTotalUnEncrRRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsUnEncrAvgRedTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsEncrALRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsEncrARRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsTotalEncrLRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsTotalEncrRRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoMapixStatsEncrAvgRedTime"))
)
if mibBuilder.loadTexts:
    cwoAoMapiExtendedStatsGroup.setStatus("current")

cwoAoNfsExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 11)
)
cwoAoNfsExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoNfsxStatsALRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoNfsxStatsARRT"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoNfsxStatsTotalLRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoNfsxStatsTotalRRs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoNfsxStatsEstTimeSaved"))
)
if mibBuilder.loadTexts:
    cwoAoNfsExtendedStatsGroup.setStatus("current")

cwoAoVideoExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 12)
)
cwoAoVideoExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoVideoxStatsTotalInBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoVideoxStatsTotalOutBytes"))
)
if mibBuilder.loadTexts:
    cwoAoVideoExtendedStatsGroup.setStatus("deprecated")

cwoAoCifsExtendedStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 13)
)
cwoAoCifsExtendedStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalReadBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalWrittenBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalRemoteReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalLocalReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalRemoteTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsTotalLocalTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsConnectedSessions"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsOpenFiles"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsMaxCacheSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsCurrentCacheSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsMaxCacheResources"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsCacheResources"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsEvictedResources"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsLastEvictedTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsVolHiWatermark"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsVolLoWatermark"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsAmntHiWatermark"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsAmntLoWatermark"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsEvictedAge"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsEvictedLastAccess"))
)
if mibBuilder.loadTexts:
    cwoAoCifsExtendedStatsGroup.setStatus("deprecated")

cwoAoApplicationStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 14)
)
cwoAoApplicationStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAppStatsOriginalBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAppStatsOptimizedBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAppStatsPTBytes"))
)
if mibBuilder.loadTexts:
    cwoAoApplicationStatsGroup.setStatus("current")

cwoAoPolicyMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 15)
)
cwoAoPolicyMapStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsDescr"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsTotalConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsTotalBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsTotalPTConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoPmapStatsTotalPTBytes"))
)
if mibBuilder.loadTexts:
    cwoAoPolicyMapStatsGroup.setStatus("current")

cwoAoClassMapStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 16)
)
cwoAoClassMapStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsDescr"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsTotalConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsTotalBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsTotalPTConns"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoCmapStatsTotalPTBytes"))
)
if mibBuilder.loadTexts:
    cwoAoClassMapStatsGroup.setStatus("current")

cwoAoStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 17)
)
cwoAoStatsGroupRev1.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsLoadStatus"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoStatsBwOpt"))
)
if mibBuilder.loadTexts:
    cwoAoStatsGroupRev1.setStatus("current")

cwoAoTfoExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 18)
)
cwoAoTfoExtGroupRev1.setObjects(
    ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsLoadStatus")
)
if mibBuilder.loadTexts:
    cwoAoTfoExtGroupRev1.setStatus("current")

cwoAoHttpExtendedStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 19)
)
cwoAoHttpExtendedStatsGroupRev1.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSPSessions"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSPPFSessions"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSPPFObjects"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSPRTTSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsTotalSPPFMissTime"))
)
if mibBuilder.loadTexts:
    cwoAoHttpExtendedStatsGroupRev1.setStatus("current")

cwoAoCifsExtendedStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 20)
)
cwoAoCifsExtendedStatsGroupRev1.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsFFTotalReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsFFRemoteReqs"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsFFLocalRespTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsFFRemoteRespTime"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoCifsxStatsDirResources"))
)
if mibBuilder.loadTexts:
    cwoAoCifsExtendedStatsGroupRev1.setStatus("deprecated")

cwoAoSmbExtendedStatsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 21)
)
cwoAoSmbExtendedStatsGroupRev1.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRdL4SignWANBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsWrL4SignWANBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsRdSignLANBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoSmbxStatsWrSignLANBytes"))
)
if mibBuilder.loadTexts:
    cwoAoSmbExtendedStatsGroupRev1.setStatus("current")

cwoAoHttpExtendedStatsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 22)
)
cwoAoHttpExtendedStatsGroupRev2.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassCacheTrans"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassRespBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassCacheTransPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassRespBytesPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBypassRespTimeSavedPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdCacheTrans"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdRespBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdCacheTransPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdRespBytesPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCStdRespTimeSavedPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicCacheTrans"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicRespBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicCacheTransPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicRespBytesPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCBasicRespTimeSavedPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvCacheTrans"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvRespBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvCacheTransPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvRespBytesPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCAdvRespTimeSavedPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalCacheTrans"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalRespBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalCacheTransPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalRespBytesPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCTotalRespTimeSavedPercent"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCPrepStatus"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCPrepCacheStoreBytes"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoAoHttpxStatsAKCPrepUncacheStoreBytes"))
)
if mibBuilder.loadTexts:
    cwoAoHttpExtendedStatsGroupRev2.setStatus("current")

cwoDreCacheStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 23)
)
cwoDreCacheStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsStatus"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsAge"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsTotal"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsUsed"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsDataUnitUsage"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsReplacedOneHrDataUnit"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsDataUnitAge"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsSigblockUsage"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsReplacedOneHrSigblock"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDreCacheStatsSigblockAge"))
)
if mibBuilder.loadTexts:
    cwoDreCacheStatsGroup.setStatus("current")

cwoDrePerfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 24)
)
cwoDrePerfStatsGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsEncodeCompressionRatio"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsEncodeCompressionLatency"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsEncodeAvgMsgSize"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsDecodeCompressionRatio"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsDecodeCompressionLatency"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoDrePerfStatsDecodeAvgMsgSize"))
)
if mibBuilder.loadTexts:
    cwoDrePerfStatsGroup.setStatus("current")


# Notification objects

cwoTfoConnectionOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 1)
)
cwoTfoConnectionOverload.setObjects(
    ("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoStatsMaxActiveConn")
)
if mibBuilder.loadTexts:
    cwoTfoConnectionOverload.setStatus(
        "current"
    )

cwoPeerOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 2)
)
cwoPeerOverload.setObjects(
    ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralMaxActivePeers")
)
if mibBuilder.loadTexts:
    cwoPeerOverload.setStatus(
        "current"
    )

cwoCpuThrottlingOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 3)
)
cwoCpuThrottlingOn.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottleHigh"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottlPeriod"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotalMonIntervalValue"))
)
if mibBuilder.loadTexts:
    cwoCpuThrottlingOn.setStatus(
        "current"
    )

cwoCpuThrottlingOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 4)
)
cwoCpuThrottlingOff.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottleLow"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoGeneralCpuThrottlPeriod"),
        ("CISCO-PROCESS-MIB", "cpmCPUTotalMonIntervalValue"))
)
if mibBuilder.loadTexts:
    cwoCpuThrottlingOff.setStatus(
        "current"
    )

cwoLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 5)
)
if mibBuilder.loadTexts:
    cwoLicenseExpired.setStatus(
        "current"
    )

cwoLicenseRevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 6)
)
if mibBuilder.loadTexts:
    cwoLicenseRevoked.setStatus(
        "current"
    )

cwoLicenseDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 0, 7)
)
if mibBuilder.loadTexts:
    cwoLicenseDeleted.setStatus(
        "current"
    )


# Notifications groups

cwoOverloadNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 5)
)
cwoOverloadNotificationGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoTfoConnectionOverload"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoPeerOverload"))
)
if mibBuilder.loadTexts:
    cwoOverloadNotificationGroup.setStatus(
        "current"
    )

cwoCpuNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 6)
)
cwoCpuNotificationGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoCpuThrottlingOn"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoCpuThrottlingOff"))
)
if mibBuilder.loadTexts:
    cwoCpuNotificationGroup.setStatus(
        "current"
    )

cwoLicenseNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 2, 8)
)
cwoLicenseNotificationGroup.setObjects(
      *(("CISCO-WAN-OPTIMIZATION-MIB", "cwoLicenseExpired"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoLicenseRevoked"),
        ("CISCO-WAN-OPTIMIZATION-MIB", "cwoLicenseDeleted"))
)
if mibBuilder.loadTexts:
    cwoLicenseNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWanOptimizationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWanOptimizationMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoWanOptimizationMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoWanOptimizationMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoWanOptimizationMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoWanOptimizationMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 762, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoWanOptimizationMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-OPTIMIZATION-MIB",
    **{"CwoHttpAKCPrepStatus": CwoHttpAKCPrepStatus,
       "CwoDreCacheStatus": CwoDreCacheStatus,
       "CwoAoName": CwoAoName,
       "CwoAoOperationalState": CwoAoOperationalState,
       "CwoLoadStates": CwoLoadStates,
       "CwoTypes": CwoTypes,
       "ciscoWanOptimizationMIB": ciscoWanOptimizationMIB,
       "ciscoWanOptimizationMIBNotifs": ciscoWanOptimizationMIBNotifs,
       "cwoTfoConnectionOverload": cwoTfoConnectionOverload,
       "cwoPeerOverload": cwoPeerOverload,
       "cwoCpuThrottlingOn": cwoCpuThrottlingOn,
       "cwoCpuThrottlingOff": cwoCpuThrottlingOff,
       "cwoLicenseExpired": cwoLicenseExpired,
       "cwoLicenseRevoked": cwoLicenseRevoked,
       "cwoLicenseDeleted": cwoLicenseDeleted,
       "ciscoWanOptimizationMIBObjects": ciscoWanOptimizationMIBObjects,
       "cwoGeneral": cwoGeneral,
       "cwoGeneralActivePeers": cwoGeneralActivePeers,
       "cwoGeneralMaxActivePeers": cwoGeneralMaxActivePeers,
       "cwoGeneralCpuThrottleHigh": cwoGeneralCpuThrottleHigh,
       "cwoGeneralCpuThrottleLow": cwoGeneralCpuThrottleLow,
       "cwoGeneralCpuThrottlPeriod": cwoGeneralCpuThrottlPeriod,
       "cwoTfo": cwoTfo,
       "cwoTfoStats": cwoTfoStats,
       "cwoTfoStatsTotalOptConn": cwoTfoStatsTotalOptConn,
       "cwoTfoStatsActiveOptConn": cwoTfoStatsActiveOptConn,
       "cwoTfoStatsMaxActiveConn": cwoTfoStatsMaxActiveConn,
       "cwoTfoStatsActiveOptTCPPlusConn": cwoTfoStatsActiveOptTCPPlusConn,
       "cwoTfoStatsActiveOptTCPOnlyConn": cwoTfoStatsActiveOptTCPOnlyConn,
       "cwoTfoStatsActiveOptTCPPrepConn": cwoTfoStatsActiveOptTCPPrepConn,
       "cwoTfoStatsActiveADConn": cwoTfoStatsActiveADConn,
       "cwoTfoStatsReservedConn": cwoTfoStatsReservedConn,
       "cwoTfoStatsPendingConn": cwoTfoStatsPendingConn,
       "cwoTfoStatsActivePTConn": cwoTfoStatsActivePTConn,
       "cwoTfoStatsTotalNormalClosedConn": cwoTfoStatsTotalNormalClosedConn,
       "cwoTfoStatsResetConn": cwoTfoStatsResetConn,
       "cwoTfoStatsLoadStatus": cwoTfoStatsLoadStatus,
       "cwoAo": cwoAo,
       "cwoAoStatsTable": cwoAoStatsTable,
       "cwoAoStatsEntry": cwoAoStatsEntry,
       "cwoAoStatsName": cwoAoStatsName,
       "cwoAoStatsIsConfigured": cwoAoStatsIsConfigured,
       "cwoAoStatsIsLicensed": cwoAoStatsIsLicensed,
       "cwoAoStatsOperationalState": cwoAoStatsOperationalState,
       "cwoAoStatsStartUpTime": cwoAoStatsStartUpTime,
       "cwoAoStatsLastResetTime": cwoAoStatsLastResetTime,
       "cwoAoStatsTotalHandledConns": cwoAoStatsTotalHandledConns,
       "cwoAoStatsTotalOptConns": cwoAoStatsTotalOptConns,
       "cwoAoStatsTotalHandedOffConns": cwoAoStatsTotalHandedOffConns,
       "cwoAoStatsTotalDroppedConns": cwoAoStatsTotalDroppedConns,
       "cwoAoStatsActiveOptConns": cwoAoStatsActiveOptConns,
       "cwoAoStatsPendingConns": cwoAoStatsPendingConns,
       "cwoAoStatsMaxActiveOptConns": cwoAoStatsMaxActiveOptConns,
       "cwoAoStatsLoadStatus": cwoAoStatsLoadStatus,
       "cwoAoStatsBwOpt": cwoAoStatsBwOpt,
       "cwoAoSmbxStats": cwoAoSmbxStats,
       "cwoAoSmbxStatsBytesReadCache": cwoAoSmbxStatsBytesReadCache,
       "cwoAoSmbxStatsBytesWriteCache": cwoAoSmbxStatsBytesWriteCache,
       "cwoAoSmbxStatsBytesReadServer": cwoAoSmbxStatsBytesReadServer,
       "cwoAoSmbxStatsBytesWriteServer": cwoAoSmbxStatsBytesWriteServer,
       "cwoAoSmbxStatsBytesReadClient": cwoAoSmbxStatsBytesReadClient,
       "cwoAoSmbxStatsBytesWriteClient": cwoAoSmbxStatsBytesWriteClient,
       "cwoAoSmbxStatsProcessedReqs": cwoAoSmbxStatsProcessedReqs,
       "cwoAoSmbxStatsActiveReqs": cwoAoSmbxStatsActiveReqs,
       "cwoAoSmbxStatsTotalTimedOutReqs": cwoAoSmbxStatsTotalTimedOutReqs,
       "cwoAoSmbxStatsTotalRemoteReqs": cwoAoSmbxStatsTotalRemoteReqs,
       "cwoAoSmbxStatsTotalLocalReqs": cwoAoSmbxStatsTotalLocalReqs,
       "cwoAoSmbxStatsRemoteAvgTime": cwoAoSmbxStatsRemoteAvgTime,
       "cwoAoSmbxStatsLocalAvgTime": cwoAoSmbxStatsLocalAvgTime,
       "cwoAoSmbxStatsRACacheHitCount": cwoAoSmbxStatsRACacheHitCount,
       "cwoAoSmbxStatsMDCacheHitCount": cwoAoSmbxStatsMDCacheHitCount,
       "cwoAoSmbxStatsRACacheHitRate": cwoAoSmbxStatsRACacheHitRate,
       "cwoAoSmbxStatsMDCacheHitRate": cwoAoSmbxStatsMDCacheHitRate,
       "cwoAoSmbxStatsMaxRACacheSize": cwoAoSmbxStatsMaxRACacheSize,
       "cwoAoSmbxStatsMaxMDCacheSize": cwoAoSmbxStatsMaxMDCacheSize,
       "cwoAoSmbxStatsMDCacheSize": cwoAoSmbxStatsMDCacheSize,
       "cwoAoSmbxStatsRAEvictedAge": cwoAoSmbxStatsRAEvictedAge,
       "cwoAoSmbxStatsRTT": cwoAoSmbxStatsRTT,
       "cwoAoSmbxStatsTotalRespTimeSaving": cwoAoSmbxStatsTotalRespTimeSaving,
       "cwoAoSmbxStatsOpenFiles": cwoAoSmbxStatsOpenFiles,
       "cwoAoSmbxStatsTotalFilesInRACache": cwoAoSmbxStatsTotalFilesInRACache,
       "cwoAoSmbxStatsRdL4SignWANBytes": cwoAoSmbxStatsRdL4SignWANBytes,
       "cwoAoSmbxStatsWrL4SignWANBytes": cwoAoSmbxStatsWrL4SignWANBytes,
       "cwoAoSmbxStatsRdSignLANBytes": cwoAoSmbxStatsRdSignLANBytes,
       "cwoAoSmbxStatsWrSignLANBytes": cwoAoSmbxStatsWrSignLANBytes,
       "cwoAoHttpxStats": cwoAoHttpxStats,
       "cwoAoHttpxStatsTotalSavedTime": cwoAoHttpxStatsTotalSavedTime,
       "cwoAoHttpxStatsTotalRTT": cwoAoHttpxStatsTotalRTT,
       "cwoAoHttpxStatsTotalMDCMTime": cwoAoHttpxStatsTotalMDCMTime,
       "cwoAoHttpxStatsEstSavedTime": cwoAoHttpxStatsEstSavedTime,
       "cwoAoHttpxStatsTotalSPSessions": cwoAoHttpxStatsTotalSPSessions,
       "cwoAoHttpxStatsTotalSPPFSessions": cwoAoHttpxStatsTotalSPPFSessions,
       "cwoAoHttpxStatsTotalSPPFObjects": cwoAoHttpxStatsTotalSPPFObjects,
       "cwoAoHttpxStatsTotalSPRTTSaved": cwoAoHttpxStatsTotalSPRTTSaved,
       "cwoAoHttpxStatsTotalSPPFMissTime": cwoAoHttpxStatsTotalSPPFMissTime,
       "cwoAoHttpxStatsAKC": cwoAoHttpxStatsAKC,
       "cwoAoHttpxStatsAKCBypassEntry": cwoAoHttpxStatsAKCBypassEntry,
       "cwoAoHttpxStatsAKCBypassCacheTrans": cwoAoHttpxStatsAKCBypassCacheTrans,
       "cwoAoHttpxStatsAKCBypassRespBytes": cwoAoHttpxStatsAKCBypassRespBytes,
       "cwoAoHttpxStatsAKCBypassCacheTransPercent": cwoAoHttpxStatsAKCBypassCacheTransPercent,
       "cwoAoHttpxStatsAKCBypassRespBytesPercent": cwoAoHttpxStatsAKCBypassRespBytesPercent,
       "cwoAoHttpxStatsAKCBypassCacheRespTimeSaved": cwoAoHttpxStatsAKCBypassCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved": cwoAoHttpxStatsAKCBypassAvgCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCBypassRespTimeSavedPercent": cwoAoHttpxStatsAKCBypassRespTimeSavedPercent,
       "cwoAoHttpxStatsAKCStdEntry": cwoAoHttpxStatsAKCStdEntry,
       "cwoAoHttpxStatsAKCStdCacheTrans": cwoAoHttpxStatsAKCStdCacheTrans,
       "cwoAoHttpxStatsAKCStdRespBytes": cwoAoHttpxStatsAKCStdRespBytes,
       "cwoAoHttpxStatsAKCStdCacheTransPercent": cwoAoHttpxStatsAKCStdCacheTransPercent,
       "cwoAoHttpxStatsAKCStdRespBytesPercent": cwoAoHttpxStatsAKCStdRespBytesPercent,
       "cwoAoHttpxStatsAKCStdCacheRespTimeSaved": cwoAoHttpxStatsAKCStdCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved": cwoAoHttpxStatsAKCStdAvgCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCStdRespTimeSavedPercent": cwoAoHttpxStatsAKCStdRespTimeSavedPercent,
       "cwoAoHttpxStatsAKCBasicEntry": cwoAoHttpxStatsAKCBasicEntry,
       "cwoAoHttpxStatsAKCBasicCacheTrans": cwoAoHttpxStatsAKCBasicCacheTrans,
       "cwoAoHttpxStatsAKCBasicRespBytes": cwoAoHttpxStatsAKCBasicRespBytes,
       "cwoAoHttpxStatsAKCBasicCacheTransPercent": cwoAoHttpxStatsAKCBasicCacheTransPercent,
       "cwoAoHttpxStatsAKCBasicRespBytesPercent": cwoAoHttpxStatsAKCBasicRespBytesPercent,
       "cwoAoHttpxStatsAKCBasicCacheRespTimeSaved": cwoAoHttpxStatsAKCBasicCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved": cwoAoHttpxStatsAKCBasicAvgCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCBasicRespTimeSavedPercent": cwoAoHttpxStatsAKCBasicRespTimeSavedPercent,
       "cwoAoHttpxStatsAKCAdvEntry": cwoAoHttpxStatsAKCAdvEntry,
       "cwoAoHttpxStatsAKCAdvCacheTrans": cwoAoHttpxStatsAKCAdvCacheTrans,
       "cwoAoHttpxStatsAKCAdvRespBytes": cwoAoHttpxStatsAKCAdvRespBytes,
       "cwoAoHttpxStatsAKCAdvCacheTransPercent": cwoAoHttpxStatsAKCAdvCacheTransPercent,
       "cwoAoHttpxStatsAKCAdvRespBytesPercent": cwoAoHttpxStatsAKCAdvRespBytesPercent,
       "cwoAoHttpxStatsAKCAdvCacheRespTimeSaved": cwoAoHttpxStatsAKCAdvCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved": cwoAoHttpxStatsAKCAdvAvgCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCAdvRespTimeSavedPercent": cwoAoHttpxStatsAKCAdvRespTimeSavedPercent,
       "cwoAoHttpxStatsAKCTotalEntry": cwoAoHttpxStatsAKCTotalEntry,
       "cwoAoHttpxStatsAKCTotalCacheTrans": cwoAoHttpxStatsAKCTotalCacheTrans,
       "cwoAoHttpxStatsAKCTotalRespBytes": cwoAoHttpxStatsAKCTotalRespBytes,
       "cwoAoHttpxStatsAKCTotalCacheTransPercent": cwoAoHttpxStatsAKCTotalCacheTransPercent,
       "cwoAoHttpxStatsAKCTotalRespBytesPercent": cwoAoHttpxStatsAKCTotalRespBytesPercent,
       "cwoAoHttpxStatsAKCTotalCacheRespTimeSaved": cwoAoHttpxStatsAKCTotalCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved": cwoAoHttpxStatsAKCTotalAvgCacheRespTimeSaved,
       "cwoAoHttpxStatsAKCTotalRespTimeSavedPercent": cwoAoHttpxStatsAKCTotalRespTimeSavedPercent,
       "cwoAoHttpxStatsAKCPrepTable": cwoAoHttpxStatsAKCPrepTable,
       "cwoAoHttpxStatsAKCPrepEntry": cwoAoHttpxStatsAKCPrepEntry,
       "cwoAoHttpxStatsAKCPrepTaskName": cwoAoHttpxStatsAKCPrepTaskName,
       "cwoAoHttpxStatsAKCPrepStatus": cwoAoHttpxStatsAKCPrepStatus,
       "cwoAoHttpxStatsAKCPrepCacheStoreBytes": cwoAoHttpxStatsAKCPrepCacheStoreBytes,
       "cwoAoHttpxStatsAKCPrepUncacheStoreBytes": cwoAoHttpxStatsAKCPrepUncacheStoreBytes,
       "cwoAoMapixStats": cwoAoMapixStats,
       "cwoAoMapixStatsUnEncrALRT": cwoAoMapixStatsUnEncrALRT,
       "cwoAoMapixStatsEncrALRT": cwoAoMapixStatsEncrALRT,
       "cwoAoMapixStatsUnEncrARRT": cwoAoMapixStatsUnEncrARRT,
       "cwoAoMapixStatsEncrARRT": cwoAoMapixStatsEncrARRT,
       "cwoAoMapixStatsTotalUnEncrLRs": cwoAoMapixStatsTotalUnEncrLRs,
       "cwoAoMapixStatsTotalEncrLRs": cwoAoMapixStatsTotalEncrLRs,
       "cwoAoMapixStatsTotalUnEncrRRs": cwoAoMapixStatsTotalUnEncrRRs,
       "cwoAoMapixStatsTotalEncrRRs": cwoAoMapixStatsTotalEncrRRs,
       "cwoAoMapixStatsUnEncrAvgRedTime": cwoAoMapixStatsUnEncrAvgRedTime,
       "cwoAoMapixStatsEncrAvgRedTime": cwoAoMapixStatsEncrAvgRedTime,
       "cwoAoNfsxStats": cwoAoNfsxStats,
       "cwoAoNfsxStatsALRT": cwoAoNfsxStatsALRT,
       "cwoAoNfsxStatsARRT": cwoAoNfsxStatsARRT,
       "cwoAoNfsxStatsTotalLRs": cwoAoNfsxStatsTotalLRs,
       "cwoAoNfsxStatsTotalRRs": cwoAoNfsxStatsTotalRRs,
       "cwoAoNfsxStatsEstTimeSaved": cwoAoNfsxStatsEstTimeSaved,
       "cwoAoVideoxStats": cwoAoVideoxStats,
       "cwoAoVideoxStatsTotalInBytes": cwoAoVideoxStatsTotalInBytes,
       "cwoAoVideoxStatsTotalOutBytes": cwoAoVideoxStatsTotalOutBytes,
       "cwoAoCifsxStats": cwoAoCifsxStats,
       "cwoAoCifsxStatsTotalReadBytes": cwoAoCifsxStatsTotalReadBytes,
       "cwoAoCifsxStatsTotalWrittenBytes": cwoAoCifsxStatsTotalWrittenBytes,
       "cwoAoCifsxStatsTotalRemoteReqs": cwoAoCifsxStatsTotalRemoteReqs,
       "cwoAoCifsxStatsTotalLocalReqs": cwoAoCifsxStatsTotalLocalReqs,
       "cwoAoCifsxStatsTotalRemoteTime": cwoAoCifsxStatsTotalRemoteTime,
       "cwoAoCifsxStatsTotalLocalTime": cwoAoCifsxStatsTotalLocalTime,
       "cwoAoCifsxStatsConnectedSessions": cwoAoCifsxStatsConnectedSessions,
       "cwoAoCifsxStatsOpenFiles": cwoAoCifsxStatsOpenFiles,
       "cwoAoCifsxStatsMaxCacheSize": cwoAoCifsxStatsMaxCacheSize,
       "cwoAoCifsxStatsCurrentCacheSize": cwoAoCifsxStatsCurrentCacheSize,
       "cwoAoCifsxStatsMaxCacheResources": cwoAoCifsxStatsMaxCacheResources,
       "cwoAoCifsxStatsCacheResources": cwoAoCifsxStatsCacheResources,
       "cwoAoCifsxStatsEvictedResources": cwoAoCifsxStatsEvictedResources,
       "cwoAoCifsxStatsLastEvictedTime": cwoAoCifsxStatsLastEvictedTime,
       "cwoAoCifsxStatsVolHiWatermark": cwoAoCifsxStatsVolHiWatermark,
       "cwoAoCifsxStatsVolLoWatermark": cwoAoCifsxStatsVolLoWatermark,
       "cwoAoCifsxStatsAmntHiWatermark": cwoAoCifsxStatsAmntHiWatermark,
       "cwoAoCifsxStatsAmntLoWatermark": cwoAoCifsxStatsAmntLoWatermark,
       "cwoAoCifsxStatsEvictedAge": cwoAoCifsxStatsEvictedAge,
       "cwoAoCifsxStatsEvictedLastAccess": cwoAoCifsxStatsEvictedLastAccess,
       "cwoAoCifsxStatsFFTotalReqs": cwoAoCifsxStatsFFTotalReqs,
       "cwoAoCifsxStatsFFRemoteReqs": cwoAoCifsxStatsFFRemoteReqs,
       "cwoAoCifsxStatsFFLocalRespTime": cwoAoCifsxStatsFFLocalRespTime,
       "cwoAoCifsxStatsFFRemoteRespTime": cwoAoCifsxStatsFFRemoteRespTime,
       "cwoAoCifsxStatsDirResources": cwoAoCifsxStatsDirResources,
       "cwoApp": cwoApp,
       "cwoAppStatsTable": cwoAppStatsTable,
       "cwoAppStatsEntry": cwoAppStatsEntry,
       "cwoAppStatsAppName": cwoAppStatsAppName,
       "cwoAppStatsOriginalBytes": cwoAppStatsOriginalBytes,
       "cwoAppStatsOptimizedBytes": cwoAppStatsOptimizedBytes,
       "cwoAppStatsPTBytes": cwoAppStatsPTBytes,
       "cwoPmap": cwoPmap,
       "cwoPmapStatsTable": cwoPmapStatsTable,
       "cwoPmapStatsEntry": cwoPmapStatsEntry,
       "cwoPmapStatsType": cwoPmapStatsType,
       "cwoPmapStatsName": cwoPmapStatsName,
       "cwoPmapStatsDescr": cwoPmapStatsDescr,
       "cwoPmapStatsTotalConns": cwoPmapStatsTotalConns,
       "cwoPmapStatsTotalBytes": cwoPmapStatsTotalBytes,
       "cwoPmapStatsTotalPTConns": cwoPmapStatsTotalPTConns,
       "cwoPmapStatsTotalPTBytes": cwoPmapStatsTotalPTBytes,
       "cwoCmap": cwoCmap,
       "cwoCmapStatsTable": cwoCmapStatsTable,
       "cwoCmapStatsEntry": cwoCmapStatsEntry,
       "cwoCmapStatsType": cwoCmapStatsType,
       "cwoCmapStatsName": cwoCmapStatsName,
       "cwoCmapStatsDescr": cwoCmapStatsDescr,
       "cwoCmapStatsTotalConns": cwoCmapStatsTotalConns,
       "cwoCmapStatsTotalBytes": cwoCmapStatsTotalBytes,
       "cwoCmapStatsTotalPTConns": cwoCmapStatsTotalPTConns,
       "cwoCmapStatsTotalPTBytes": cwoCmapStatsTotalPTBytes,
       "cwoDre": cwoDre,
       "cwoDreCacheStats": cwoDreCacheStats,
       "cwoDreCacheStatsStatus": cwoDreCacheStatsStatus,
       "cwoDreCacheStatsAge": cwoDreCacheStatsAge,
       "cwoDreCacheStatsTotal": cwoDreCacheStatsTotal,
       "cwoDreCacheStatsUsed": cwoDreCacheStatsUsed,
       "cwoDreCacheStatsDataUnitUsage": cwoDreCacheStatsDataUnitUsage,
       "cwoDreCacheStatsReplacedOneHrDataUnit": cwoDreCacheStatsReplacedOneHrDataUnit,
       "cwoDreCacheStatsDataUnitAge": cwoDreCacheStatsDataUnitAge,
       "cwoDreCacheStatsSigblockUsage": cwoDreCacheStatsSigblockUsage,
       "cwoDreCacheStatsReplacedOneHrSigblock": cwoDreCacheStatsReplacedOneHrSigblock,
       "cwoDreCacheStatsSigblockAge": cwoDreCacheStatsSigblockAge,
       "cwoDrePerfStats": cwoDrePerfStats,
       "cwoDrePerfStatsEncodeCompressionRatio": cwoDrePerfStatsEncodeCompressionRatio,
       "cwoDrePerfStatsEncodeCompressionLatency": cwoDrePerfStatsEncodeCompressionLatency,
       "cwoDrePerfStatsEncodeAvgMsgSize": cwoDrePerfStatsEncodeAvgMsgSize,
       "cwoDrePerfStatsDecodeCompressionRatio": cwoDrePerfStatsDecodeCompressionRatio,
       "cwoDrePerfStatsDecodeCompressionLatency": cwoDrePerfStatsDecodeCompressionLatency,
       "cwoDrePerfStatsDecodeAvgMsgSize": cwoDrePerfStatsDecodeAvgMsgSize,
       "ciscoWanOptimizationMIBConform": ciscoWanOptimizationMIBConform,
       "ciscoWanOptimizationMIBCompliances": ciscoWanOptimizationMIBCompliances,
       "ciscoWanOptimizationMIBCompliance": ciscoWanOptimizationMIBCompliance,
       "ciscoWanOptimizationMIBCompliance1": ciscoWanOptimizationMIBCompliance1,
       "ciscoWanOptimizationMIBComplianceRev2": ciscoWanOptimizationMIBComplianceRev2,
       "ciscoWanOptimizationMIBComplianceRev3": ciscoWanOptimizationMIBComplianceRev3,
       "ciscoWanOptimizationMIBComplianceRev4": ciscoWanOptimizationMIBComplianceRev4,
       "ciscoWanOptimizationMIBComplianceRev5": ciscoWanOptimizationMIBComplianceRev5,
       "ciscoWanOptimizationMIBGroups": ciscoWanOptimizationMIBGroups,
       "cwoGeneralGroup": cwoGeneralGroup,
       "cwoTfoBaseGroup": cwoTfoBaseGroup,
       "cwoTfoExtGroup": cwoTfoExtGroup,
       "cwoAoStatsGroup": cwoAoStatsGroup,
       "cwoOverloadNotificationGroup": cwoOverloadNotificationGroup,
       "cwoCpuNotificationGroup": cwoCpuNotificationGroup,
       "cwoAoSmbExtendedStatsGroup": cwoAoSmbExtendedStatsGroup,
       "cwoLicenseNotificationGroup": cwoLicenseNotificationGroup,
       "cwoAoHttpExtendedStatsGroup": cwoAoHttpExtendedStatsGroup,
       "cwoAoMapiExtendedStatsGroup": cwoAoMapiExtendedStatsGroup,
       "cwoAoNfsExtendedStatsGroup": cwoAoNfsExtendedStatsGroup,
       "cwoAoVideoExtendedStatsGroup": cwoAoVideoExtendedStatsGroup,
       "cwoAoCifsExtendedStatsGroup": cwoAoCifsExtendedStatsGroup,
       "cwoAoApplicationStatsGroup": cwoAoApplicationStatsGroup,
       "cwoAoPolicyMapStatsGroup": cwoAoPolicyMapStatsGroup,
       "cwoAoClassMapStatsGroup": cwoAoClassMapStatsGroup,
       "cwoAoStatsGroupRev1": cwoAoStatsGroupRev1,
       "cwoAoTfoExtGroupRev1": cwoAoTfoExtGroupRev1,
       "cwoAoHttpExtendedStatsGroupRev1": cwoAoHttpExtendedStatsGroupRev1,
       "cwoAoCifsExtendedStatsGroupRev1": cwoAoCifsExtendedStatsGroupRev1,
       "cwoAoSmbExtendedStatsGroupRev1": cwoAoSmbExtendedStatsGroupRev1,
       "cwoAoHttpExtendedStatsGroupRev2": cwoAoHttpExtendedStatsGroupRev2,
       "cwoDreCacheStatsGroup": cwoDreCacheStatsGroup,
       "cwoDrePerfStatsGroup": cwoDrePerfStatsGroup}
)
