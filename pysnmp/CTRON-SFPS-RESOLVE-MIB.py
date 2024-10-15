# SNMP MIB module (CTRON-SFPS-RESOLVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-RESOLVE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:30 2024
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

(sfpsBlockResolve,
 sfpsBlockResolveAPI,
 sfpsBlockResolveStats,
 sfpsISPResolve,
 sfpsMobilityStats,
 sfpsRelayAgentResolve,
 sfpsRelayAgentResolveStats,
 sfpsResolveStats,
 sfpsSubnetResolve,
 sfpsSubnetResolveAPI,
 sfpsSubnetResolveNvram,
 sfpsSubnetResolveStats,
 sfpsSwitchResolve,
 sfpsTableResolve,
 sfpsTableResolveAPI,
 sfpsUnresolve,
 sfpsUnresolveTableAPI,
 sfpsUnresolveTableStats) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsBlockResolve",
    "sfpsBlockResolveAPI",
    "sfpsBlockResolveStats",
    "sfpsISPResolve",
    "sfpsMobilityStats",
    "sfpsRelayAgentResolve",
    "sfpsRelayAgentResolveStats",
    "sfpsResolveStats",
    "sfpsSubnetResolve",
    "sfpsSubnetResolveAPI",
    "sfpsSubnetResolveNvram",
    "sfpsSubnetResolveStats",
    "sfpsSwitchResolve",
    "sfpsTableResolve",
    "sfpsTableResolveAPI",
    "sfpsUnresolve",
    "sfpsUnresolveTableAPI",
    "sfpsUnresolveTableStats")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsServiceCenterResolveTable_Object = MibTable
sfpsServiceCenterResolveTable = _SfpsServiceCenterResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveTable.setStatus("mandatory")
_SfpsServiceCenterResolveEntry_Object = MibTableRow
sfpsServiceCenterResolveEntry = _SfpsServiceCenterResolveEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1)
)
sfpsServiceCenterResolveEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsServiceCenterResolveHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveEntry.setStatus("mandatory")
_SfpsServiceCenterResolveHashLeaf_Type = HexInteger
_SfpsServiceCenterResolveHashLeaf_Object = MibTableColumn
sfpsServiceCenterResolveHashLeaf = _SfpsServiceCenterResolveHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 1),
    _SfpsServiceCenterResolveHashLeaf_Type()
)
sfpsServiceCenterResolveHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveHashLeaf.setStatus("mandatory")
_SfpsServiceCenterResolveMetric_Type = Integer32
_SfpsServiceCenterResolveMetric_Object = MibTableColumn
sfpsServiceCenterResolveMetric = _SfpsServiceCenterResolveMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 2),
    _SfpsServiceCenterResolveMetric_Type()
)
sfpsServiceCenterResolveMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveMetric.setStatus("mandatory")
_SfpsServiceCenterResolveName_Type = DisplayString
_SfpsServiceCenterResolveName_Object = MibTableColumn
sfpsServiceCenterResolveName = _SfpsServiceCenterResolveName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 3),
    _SfpsServiceCenterResolveName_Type()
)
sfpsServiceCenterResolveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveName.setStatus("mandatory")


class _SfpsServiceCenterResolveOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterResolveOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsServiceCenterResolveOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterResolveOperStatus_Object = MibTableColumn
sfpsServiceCenterResolveOperStatus = _SfpsServiceCenterResolveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 4),
    _SfpsServiceCenterResolveOperStatus_Type()
)
sfpsServiceCenterResolveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveOperStatus.setStatus("mandatory")


class _SfpsServiceCenterResolveAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterResolveAdminStatus based on Integer32"""
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


_SfpsServiceCenterResolveAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterResolveAdminStatus_Object = MibTableColumn
sfpsServiceCenterResolveAdminStatus = _SfpsServiceCenterResolveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 5),
    _SfpsServiceCenterResolveAdminStatus_Type()
)
sfpsServiceCenterResolveAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveAdminStatus.setStatus("mandatory")
_SfpsServiceCenterResolveStatusTime_Type = TimeTicks
_SfpsServiceCenterResolveStatusTime_Object = MibTableColumn
sfpsServiceCenterResolveStatusTime = _SfpsServiceCenterResolveStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 6),
    _SfpsServiceCenterResolveStatusTime_Type()
)
sfpsServiceCenterResolveStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveStatusTime.setStatus("mandatory")
_SfpsServiceCenterResolveRequests_Type = Integer32
_SfpsServiceCenterResolveRequests_Object = MibTableColumn
sfpsServiceCenterResolveRequests = _SfpsServiceCenterResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 7),
    _SfpsServiceCenterResolveRequests_Type()
)
sfpsServiceCenterResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveRequests.setStatus("mandatory")
_SfpsServiceCenterResolveResponses_Type = Integer32
_SfpsServiceCenterResolveResponses_Object = MibTableColumn
sfpsServiceCenterResolveResponses = _SfpsServiceCenterResolveResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 1, 1, 8),
    _SfpsServiceCenterResolveResponses_Type()
)
sfpsServiceCenterResolveResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterResolveResponses.setStatus("mandatory")
_SfpsSwitchResolveTable_Object = MibTable
sfpsSwitchResolveTable = _SfpsSwitchResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsSwitchResolveTable.setStatus("mandatory")
_SfpsSwitchResolveEntry_Object = MibTableRow
sfpsSwitchResolveEntry = _SfpsSwitchResolveEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1)
)
sfpsSwitchResolveEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsSwitchResolveSwitch"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsSwitchResolveCallTag"),
)
if mibBuilder.loadTexts:
    sfpsSwitchResolveEntry.setStatus("mandatory")
_SfpsSwitchResolveSwitch_Type = OctetString
_SfpsSwitchResolveSwitch_Object = MibTableColumn
sfpsSwitchResolveSwitch = _SfpsSwitchResolveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 1),
    _SfpsSwitchResolveSwitch_Type()
)
sfpsSwitchResolveSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveSwitch.setStatus("mandatory")
_SfpsSwitchResolveCallTag_Type = Integer32
_SfpsSwitchResolveCallTag_Object = MibTableColumn
sfpsSwitchResolveCallTag = _SfpsSwitchResolveCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 2),
    _SfpsSwitchResolveCallTag_Type()
)
sfpsSwitchResolveCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveCallTag.setStatus("mandatory")
_SfpsSwitchResolvePortNum_Type = Integer32
_SfpsSwitchResolvePortNum_Object = MibTableColumn
sfpsSwitchResolvePortNum = _SfpsSwitchResolvePortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 3),
    _SfpsSwitchResolvePortNum_Type()
)
sfpsSwitchResolvePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolvePortNum.setStatus("mandatory")
_SfpsSwitchResolveNeighborSw_Type = OctetString
_SfpsSwitchResolveNeighborSw_Object = MibTableColumn
sfpsSwitchResolveNeighborSw = _SfpsSwitchResolveNeighborSw_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 4),
    _SfpsSwitchResolveNeighborSw_Type()
)
sfpsSwitchResolveNeighborSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveNeighborSw.setStatus("mandatory")
_SfpsSwitchResolveRequestCount_Type = Integer32
_SfpsSwitchResolveRequestCount_Object = MibTableColumn
sfpsSwitchResolveRequestCount = _SfpsSwitchResolveRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 5),
    _SfpsSwitchResolveRequestCount_Type()
)
sfpsSwitchResolveRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveRequestCount.setStatus("mandatory")
_SfpsSwitchResolveResponseCount_Type = Integer32
_SfpsSwitchResolveResponseCount_Object = MibTableColumn
sfpsSwitchResolveResponseCount = _SfpsSwitchResolveResponseCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 6),
    _SfpsSwitchResolveResponseCount_Type()
)
sfpsSwitchResolveResponseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveResponseCount.setStatus("mandatory")
_SfpsSwitchResolveMobilityRetry_Type = Integer32
_SfpsSwitchResolveMobilityRetry_Object = MibTableColumn
sfpsSwitchResolveMobilityRetry = _SfpsSwitchResolveMobilityRetry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 7),
    _SfpsSwitchResolveMobilityRetry_Type()
)
sfpsSwitchResolveMobilityRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveMobilityRetry.setStatus("mandatory")
_SfpsSwitchResolveEventId_Type = Integer32
_SfpsSwitchResolveEventId_Object = MibTableColumn
sfpsSwitchResolveEventId = _SfpsSwitchResolveEventId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 2, 1, 1, 8),
    _SfpsSwitchResolveEventId_Type()
)
sfpsSwitchResolveEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSwitchResolveEventId.setStatus("mandatory")
_SfpsResolveStatsRequests_Type = Integer32
_SfpsResolveStatsRequests_Object = MibScalar
sfpsResolveStatsRequests = _SfpsResolveStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 1),
    _SfpsResolveStatsRequests_Type()
)
sfpsResolveStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsRequests.setStatus("mandatory")
_SfpsResolveStatsResponses_Type = Integer32
_SfpsResolveStatsResponses_Object = MibScalar
sfpsResolveStatsResponses = _SfpsResolveStatsResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 2),
    _SfpsResolveStatsResponses_Type()
)
sfpsResolveStatsResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsResponses.setStatus("mandatory")
_SfpsResolveStatsAcks_Type = Integer32
_SfpsResolveStatsAcks_Object = MibScalar
sfpsResolveStatsAcks = _SfpsResolveStatsAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 3),
    _SfpsResolveStatsAcks_Type()
)
sfpsResolveStatsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsAcks.setStatus("mandatory")
_SfpsResolveStatsNaks_Type = Integer32
_SfpsResolveStatsNaks_Object = MibScalar
sfpsResolveStatsNaks = _SfpsResolveStatsNaks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 4),
    _SfpsResolveStatsNaks_Type()
)
sfpsResolveStatsNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsNaks.setStatus("mandatory")
_SfpsResolveStatsUnknowns_Type = Integer32
_SfpsResolveStatsUnknowns_Object = MibScalar
sfpsResolveStatsUnknowns = _SfpsResolveStatsUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 5),
    _SfpsResolveStatsUnknowns_Type()
)
sfpsResolveStatsUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsUnknowns.setStatus("mandatory")
_SfpsResolveStatsNoAnswer_Type = Integer32
_SfpsResolveStatsNoAnswer_Object = MibScalar
sfpsResolveStatsNoAnswer = _SfpsResolveStatsNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 6),
    _SfpsResolveStatsNoAnswer_Type()
)
sfpsResolveStatsNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsNoAnswer.setStatus("mandatory")
_SfpsResolveStatsTimeout_Type = Integer32
_SfpsResolveStatsTimeout_Object = MibScalar
sfpsResolveStatsTimeout = _SfpsResolveStatsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 7),
    _SfpsResolveStatsTimeout_Type()
)
sfpsResolveStatsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsTimeout.setStatus("mandatory")
_SfpsResolveStatsAvgResponseTime_Type = Integer32
_SfpsResolveStatsAvgResponseTime_Object = MibScalar
sfpsResolveStatsAvgResponseTime = _SfpsResolveStatsAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 8),
    _SfpsResolveStatsAvgResponseTime_Type()
)
sfpsResolveStatsAvgResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsAvgResponseTime.setStatus("mandatory")
_SfpsResolveStatsTableSize_Type = Integer32
_SfpsResolveStatsTableSize_Object = MibScalar
sfpsResolveStatsTableSize = _SfpsResolveStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 9),
    _SfpsResolveStatsTableSize_Type()
)
sfpsResolveStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsTableSize.setStatus("mandatory")
_SfpsResolveStatsTableHigh_Type = Integer32
_SfpsResolveStatsTableHigh_Object = MibScalar
sfpsResolveStatsTableHigh = _SfpsResolveStatsTableHigh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 10),
    _SfpsResolveStatsTableHigh_Type()
)
sfpsResolveStatsTableHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsTableHigh.setStatus("mandatory")
_SfpsResolveStatsErrorCount_Type = Integer32
_SfpsResolveStatsErrorCount_Object = MibScalar
sfpsResolveStatsErrorCount = _SfpsResolveStatsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 11),
    _SfpsResolveStatsErrorCount_Type()
)
sfpsResolveStatsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsErrorCount.setStatus("mandatory")
_SfpsResolveStatsStaleCount_Type = Integer32
_SfpsResolveStatsStaleCount_Object = MibScalar
sfpsResolveStatsStaleCount = _SfpsResolveStatsStaleCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 12),
    _SfpsResolveStatsStaleCount_Type()
)
sfpsResolveStatsStaleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsStaleCount.setStatus("mandatory")
_SfpsResolveStatsDupMsgCount_Type = Integer32
_SfpsResolveStatsDupMsgCount_Object = MibScalar
sfpsResolveStatsDupMsgCount = _SfpsResolveStatsDupMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 13),
    _SfpsResolveStatsDupMsgCount_Type()
)
sfpsResolveStatsDupMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsDupMsgCount.setStatus("mandatory")
_SfpsResolveStatsReqRcvd_Type = Integer32
_SfpsResolveStatsReqRcvd_Object = MibScalar
sfpsResolveStatsReqRcvd = _SfpsResolveStatsReqRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 14),
    _SfpsResolveStatsReqRcvd_Type()
)
sfpsResolveStatsReqRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsReqRcvd.setStatus("mandatory")
_SfpsResolveStatsRespAcksSent_Type = Integer32
_SfpsResolveStatsRespAcksSent_Object = MibScalar
sfpsResolveStatsRespAcksSent = _SfpsResolveStatsRespAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 15),
    _SfpsResolveStatsRespAcksSent_Type()
)
sfpsResolveStatsRespAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsRespAcksSent.setStatus("mandatory")
_SfpsResolveStatsRespNaksSent_Type = Integer32
_SfpsResolveStatsRespNaksSent_Object = MibScalar
sfpsResolveStatsRespNaksSent = _SfpsResolveStatsRespNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 16),
    _SfpsResolveStatsRespNaksSent_Type()
)
sfpsResolveStatsRespNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsRespNaksSent.setStatus("mandatory")
_SfpsResolveStatsRespUnknownsSent_Type = Integer32
_SfpsResolveStatsRespUnknownsSent_Object = MibScalar
sfpsResolveStatsRespUnknownsSent = _SfpsResolveStatsRespUnknownsSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 17),
    _SfpsResolveStatsRespUnknownsSent_Type()
)
sfpsResolveStatsRespUnknownsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsRespUnknownsSent.setStatus("mandatory")
_SfpsResolveStatsRespRecvd_Type = Integer32
_SfpsResolveStatsRespRecvd_Object = MibScalar
sfpsResolveStatsRespRecvd = _SfpsResolveStatsRespRecvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 18),
    _SfpsResolveStatsRespRecvd_Type()
)
sfpsResolveStatsRespRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsRespRecvd.setStatus("mandatory")
_SfpsResolveStatsResolveMask_Type = OctetString
_SfpsResolveStatsResolveMask_Object = MibScalar
sfpsResolveStatsResolveMask = _SfpsResolveStatsResolveMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 19),
    _SfpsResolveStatsResolveMask_Type()
)
sfpsResolveStatsResolveMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsResolveMask.setStatus("mandatory")
_SfpsResolveStatsINBMask_Type = OctetString
_SfpsResolveStatsINBMask_Object = MibScalar
sfpsResolveStatsINBMask = _SfpsResolveStatsINBMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 20),
    _SfpsResolveStatsINBMask_Type()
)
sfpsResolveStatsINBMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsINBMask.setStatus("mandatory")
_SfpsResolveStatsFloodMask_Type = OctetString
_SfpsResolveStatsFloodMask_Object = MibScalar
sfpsResolveStatsFloodMask = _SfpsResolveStatsFloodMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 21),
    _SfpsResolveStatsFloodMask_Type()
)
sfpsResolveStatsFloodMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsFloodMask.setStatus("mandatory")
_SfpsResolveStatsChangeCount_Type = Integer32
_SfpsResolveStatsChangeCount_Object = MibScalar
sfpsResolveStatsChangeCount = _SfpsResolveStatsChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 22),
    _SfpsResolveStatsChangeCount_Type()
)
sfpsResolveStatsChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsChangeCount.setStatus("mandatory")
_SfpsResolveStatsChangeTime_Type = TimeTicks
_SfpsResolveStatsChangeTime_Object = MibScalar
sfpsResolveStatsChangeTime = _SfpsResolveStatsChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 23),
    _SfpsResolveStatsChangeTime_Type()
)
sfpsResolveStatsChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsChangeTime.setStatus("mandatory")
_SfpsResolveStatsResetStats_Type = Integer32
_SfpsResolveStatsResetStats_Object = MibScalar
sfpsResolveStatsResetStats = _SfpsResolveStatsResetStats_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 24),
    _SfpsResolveStatsResetStats_Type()
)
sfpsResolveStatsResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsResetStats.setStatus("mandatory")
_SfpsResolveStatsAnswerUnknown_Type = Integer32
_SfpsResolveStatsAnswerUnknown_Object = MibScalar
sfpsResolveStatsAnswerUnknown = _SfpsResolveStatsAnswerUnknown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 25),
    _SfpsResolveStatsAnswerUnknown_Type()
)
sfpsResolveStatsAnswerUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsAnswerUnknown.setStatus("mandatory")
_SfpsResolveStatsDisableProxy_Type = Integer32
_SfpsResolveStatsDisableProxy_Object = MibScalar
sfpsResolveStatsDisableProxy = _SfpsResolveStatsDisableProxy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 26),
    _SfpsResolveStatsDisableProxy_Type()
)
sfpsResolveStatsDisableProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsDisableProxy.setStatus("mandatory")
_SfpsResolveStatsDisableLayer3_Type = Integer32
_SfpsResolveStatsDisableLayer3_Object = MibScalar
sfpsResolveStatsDisableLayer3 = _SfpsResolveStatsDisableLayer3_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 27),
    _SfpsResolveStatsDisableLayer3_Type()
)
sfpsResolveStatsDisableLayer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsDisableLayer3.setStatus("mandatory")
_SfpsResolveStatsCSPDaveMalPkts_Type = Integer32
_SfpsResolveStatsCSPDaveMalPkts_Object = MibScalar
sfpsResolveStatsCSPDaveMalPkts = _SfpsResolveStatsCSPDaveMalPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 28),
    _SfpsResolveStatsCSPDaveMalPkts_Type()
)
sfpsResolveStatsCSPDaveMalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsCSPDaveMalPkts.setStatus("mandatory")
_SfpsResolveStatsStaleTimeOut_Type = Integer32
_SfpsResolveStatsStaleTimeOut_Object = MibScalar
sfpsResolveStatsStaleTimeOut = _SfpsResolveStatsStaleTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 29),
    _SfpsResolveStatsStaleTimeOut_Type()
)
sfpsResolveStatsStaleTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsStaleTimeOut.setStatus("mandatory")
_SfpsResolveStatsMaxResponseTime_Type = Integer32
_SfpsResolveStatsMaxResponseTime_Object = MibScalar
sfpsResolveStatsMaxResponseTime = _SfpsResolveStatsMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 30),
    _SfpsResolveStatsMaxResponseTime_Type()
)
sfpsResolveStatsMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResolveStatsMaxResponseTime.setStatus("mandatory")
_SfpsResolveStatsStaleEntryLost_Type = Integer32
_SfpsResolveStatsStaleEntryLost_Object = MibScalar
sfpsResolveStatsStaleEntryLost = _SfpsResolveStatsStaleEntryLost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 31),
    _SfpsResolveStatsStaleEntryLost_Type()
)
sfpsResolveStatsStaleEntryLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsStaleEntryLost.setStatus("mandatory")
_SfpsResolveStatsDaveEntryLost_Type = Integer32
_SfpsResolveStatsDaveEntryLost_Object = MibScalar
sfpsResolveStatsDaveEntryLost = _SfpsResolveStatsDaveEntryLost_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 3, 32),
    _SfpsResolveStatsDaveEntryLost_Type()
)
sfpsResolveStatsDaveEntryLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResolveStatsDaveEntryLost.setStatus("mandatory")
_SfpsBlockResolveTable_Object = MibTable
sfpsBlockResolveTable = _SfpsBlockResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsBlockResolveTable.setStatus("mandatory")
_SfpsBlockResolveTableEntry_Object = MibTableRow
sfpsBlockResolveTableEntry = _SfpsBlockResolveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1)
)
sfpsBlockResolveTableEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsBlockResolveTableHash"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsBlockResolveTableHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsBlockResolveTableEntry.setStatus("mandatory")
_SfpsBlockResolveTableHash_Type = Integer32
_SfpsBlockResolveTableHash_Object = MibTableColumn
sfpsBlockResolveTableHash = _SfpsBlockResolveTableHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 1),
    _SfpsBlockResolveTableHash_Type()
)
sfpsBlockResolveTableHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableHash.setStatus("mandatory")
_SfpsBlockResolveTableHashIndex_Type = Integer32
_SfpsBlockResolveTableHashIndex_Object = MibTableColumn
sfpsBlockResolveTableHashIndex = _SfpsBlockResolveTableHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 2),
    _SfpsBlockResolveTableHashIndex_Type()
)
sfpsBlockResolveTableHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableHashIndex.setStatus("mandatory")


class _SfpsBlockResolveTableAOType_Type(Integer32):
    """Custom type sfpsBlockResolveTableAOType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("aoAtDDP", 11),
          ("aoEmpty", 12),
          ("aoHostName", 14),
          ("aoInetIP", 7),
          ("aoInetIPMask", 16),
          ("aoInetRIP", 9),
          ("aoInetRPC", 8),
          ("aoInetUDP", 5),
          ("aoInetYP", 4),
          ("aoIpxIpx", 6),
          ("aoIpxRIP", 3),
          ("aoIpxSap", 2),
          ("aoMacDX", 1),
          ("aoMacDXMcast", 10),
          ("aoNetBiosName", 15),
          ("aoVlan", 13))
    )


_SfpsBlockResolveTableAOType_Type.__name__ = "Integer32"
_SfpsBlockResolveTableAOType_Object = MibTableColumn
sfpsBlockResolveTableAOType = _SfpsBlockResolveTableAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 3),
    _SfpsBlockResolveTableAOType_Type()
)
sfpsBlockResolveTableAOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableAOType.setStatus("mandatory")
_SfpsBlockResolveTableAOValue_Type = DisplayString
_SfpsBlockResolveTableAOValue_Object = MibTableColumn
sfpsBlockResolveTableAOValue = _SfpsBlockResolveTableAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 4),
    _SfpsBlockResolveTableAOValue_Type()
)
sfpsBlockResolveTableAOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableAOValue.setStatus("mandatory")
_SfpsBlockResolveTableStartTime_Type = TimeTicks
_SfpsBlockResolveTableStartTime_Object = MibTableColumn
sfpsBlockResolveTableStartTime = _SfpsBlockResolveTableStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 5),
    _SfpsBlockResolveTableStartTime_Type()
)
sfpsBlockResolveTableStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableStartTime.setStatus("mandatory")
_SfpsBlockResolveTableNumBlocked_Type = Counter32
_SfpsBlockResolveTableNumBlocked_Object = MibTableColumn
sfpsBlockResolveTableNumBlocked = _SfpsBlockResolveTableNumBlocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 6),
    _SfpsBlockResolveTableNumBlocked_Type()
)
sfpsBlockResolveTableNumBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableNumBlocked.setStatus("mandatory")
_SfpsBlockResolveTableNumSent_Type = Counter32
_SfpsBlockResolveTableNumSent_Object = MibTableColumn
sfpsBlockResolveTableNumSent = _SfpsBlockResolveTableNumSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 7),
    _SfpsBlockResolveTableNumSent_Type()
)
sfpsBlockResolveTableNumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableNumSent.setStatus("mandatory")
_SfpsBlockResolveTableLastSeen_Type = TimeTicks
_SfpsBlockResolveTableLastSeen_Object = MibTableColumn
sfpsBlockResolveTableLastSeen = _SfpsBlockResolveTableLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 8),
    _SfpsBlockResolveTableLastSeen_Type()
)
sfpsBlockResolveTableLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableLastSeen.setStatus("mandatory")
_SfpsBlockResolveTableAvgPeriod_Type = Integer32
_SfpsBlockResolveTableAvgPeriod_Object = MibTableColumn
sfpsBlockResolveTableAvgPeriod = _SfpsBlockResolveTableAvgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 1, 1, 9),
    _SfpsBlockResolveTableAvgPeriod_Type()
)
sfpsBlockResolveTableAvgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveTableAvgPeriod.setStatus("mandatory")


class _SfpsBlockResolveAPIVerb_Type(Integer32):
    """Custom type sfpsBlockResolveAPIVerb based on Integer32"""
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
        *(("add-entry", 2),
          ("del-entry", 3),
          ("other", 1),
          ("reset", 5),
          ("set-parameter", 4))
    )


_SfpsBlockResolveAPIVerb_Type.__name__ = "Integer32"
_SfpsBlockResolveAPIVerb_Object = MibScalar
sfpsBlockResolveAPIVerb = _SfpsBlockResolveAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 1),
    _SfpsBlockResolveAPIVerb_Type()
)
sfpsBlockResolveAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPIVerb.setStatus("mandatory")
_SfpsBlockResolveAPIAOType_Type = DisplayString
_SfpsBlockResolveAPIAOType_Object = MibScalar
sfpsBlockResolveAPIAOType = _SfpsBlockResolveAPIAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 2),
    _SfpsBlockResolveAPIAOType_Type()
)
sfpsBlockResolveAPIAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPIAOType.setStatus("mandatory")
_SfpsBlockResolveAPIAOValue_Type = DisplayString
_SfpsBlockResolveAPIAOValue_Object = MibScalar
sfpsBlockResolveAPIAOValue = _SfpsBlockResolveAPIAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 3),
    _SfpsBlockResolveAPIAOValue_Type()
)
sfpsBlockResolveAPIAOValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPIAOValue.setStatus("mandatory")
_SfpsBlockResolveAPITestCount_Type = Integer32
_SfpsBlockResolveAPITestCount_Object = MibScalar
sfpsBlockResolveAPITestCount = _SfpsBlockResolveAPITestCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 4),
    _SfpsBlockResolveAPITestCount_Type()
)
sfpsBlockResolveAPITestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPITestCount.setStatus("mandatory")
_SfpsBlockResolveAPIThreshold_Type = Integer32
_SfpsBlockResolveAPIThreshold_Object = MibScalar
sfpsBlockResolveAPIThreshold = _SfpsBlockResolveAPIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 5),
    _SfpsBlockResolveAPIThreshold_Type()
)
sfpsBlockResolveAPIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPIThreshold.setStatus("mandatory")
_SfpsBlockResolveAPISendPeriod_Type = Integer32
_SfpsBlockResolveAPISendPeriod_Object = MibScalar
sfpsBlockResolveAPISendPeriod = _SfpsBlockResolveAPISendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 2, 6),
    _SfpsBlockResolveAPISendPeriod_Type()
)
sfpsBlockResolveAPISendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsBlockResolveAPISendPeriod.setStatus("mandatory")
_SfpsBlockResolveStatsNumEntries_Type = Integer32
_SfpsBlockResolveStatsNumEntries_Object = MibScalar
sfpsBlockResolveStatsNumEntries = _SfpsBlockResolveStatsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 1),
    _SfpsBlockResolveStatsNumEntries_Type()
)
sfpsBlockResolveStatsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsNumEntries.setStatus("mandatory")
_SfpsBlockResolveStatsTableSize_Type = Integer32
_SfpsBlockResolveStatsTableSize_Object = MibScalar
sfpsBlockResolveStatsTableSize = _SfpsBlockResolveStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 2),
    _SfpsBlockResolveStatsTableSize_Type()
)
sfpsBlockResolveStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsTableSize.setStatus("mandatory")
_SfpsBlockResolveStatsTotalReqSeen_Type = Integer32
_SfpsBlockResolveStatsTotalReqSeen_Object = MibScalar
sfpsBlockResolveStatsTotalReqSeen = _SfpsBlockResolveStatsTotalReqSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 3),
    _SfpsBlockResolveStatsTotalReqSeen_Type()
)
sfpsBlockResolveStatsTotalReqSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsTotalReqSeen.setStatus("mandatory")
_SfpsBlockResolveStatsTotalBlocked_Type = Integer32
_SfpsBlockResolveStatsTotalBlocked_Object = MibScalar
sfpsBlockResolveStatsTotalBlocked = _SfpsBlockResolveStatsTotalBlocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 4),
    _SfpsBlockResolveStatsTotalBlocked_Type()
)
sfpsBlockResolveStatsTotalBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsTotalBlocked.setStatus("mandatory")
_SfpsBlockResolveStatsTotalSent_Type = Integer32
_SfpsBlockResolveStatsTotalSent_Object = MibScalar
sfpsBlockResolveStatsTotalSent = _SfpsBlockResolveStatsTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 5),
    _SfpsBlockResolveStatsTotalSent_Type()
)
sfpsBlockResolveStatsTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsTotalSent.setStatus("mandatory")
_SfpsBlockResolveStatsAvgReqTime_Type = Integer32
_SfpsBlockResolveStatsAvgReqTime_Object = MibScalar
sfpsBlockResolveStatsAvgReqTime = _SfpsBlockResolveStatsAvgReqTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 4, 3, 6),
    _SfpsBlockResolveStatsAvgReqTime_Type()
)
sfpsBlockResolveStatsAvgReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsBlockResolveStatsAvgReqTime.setStatus("mandatory")
_SfpsUnresolveTable_Object = MibTable
sfpsUnresolveTable = _SfpsUnresolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsUnresolveTable.setStatus("mandatory")
_SfpsUnresolveTableEntry_Object = MibTableRow
sfpsUnresolveTableEntry = _SfpsUnresolveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1)
)
sfpsUnresolveTableEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsUnresolveTableHash"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsUnresolveTableHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsUnresolveTableEntry.setStatus("mandatory")
_SfpsUnresolveTableHash_Type = Integer32
_SfpsUnresolveTableHash_Object = MibTableColumn
sfpsUnresolveTableHash = _SfpsUnresolveTableHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 1),
    _SfpsUnresolveTableHash_Type()
)
sfpsUnresolveTableHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableHash.setStatus("mandatory")
_SfpsUnresolveTableHashIndex_Type = Integer32
_SfpsUnresolveTableHashIndex_Object = MibTableColumn
sfpsUnresolveTableHashIndex = _SfpsUnresolveTableHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 2),
    _SfpsUnresolveTableHashIndex_Type()
)
sfpsUnresolveTableHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableHashIndex.setStatus("mandatory")


class _SfpsUnresolveTableAOType_Type(Integer32):
    """Custom type sfpsUnresolveTableAOType based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("aoAtDDP", 11),
          ("aoDHCPXID", 21),
          ("aoEmpty", 12),
          ("aoHostName", 14),
          ("aoInetIP", 7),
          ("aoInetIPMask", 17),
          ("aoInetRIP", 9),
          ("aoInetRPC", 8),
          ("aoInetUDP", 5),
          ("aoInetYP", 4),
          ("aoIpxIpx", 6),
          ("aoIpxRIP", 3),
          ("aoIpxSap", 2),
          ("aoIpxSap8022", 18),
          ("aoIpxSapEnet", 20),
          ("aoIpxSapSnap", 19),
          ("aoMacDX", 1),
          ("aoMacDXMcast", 10),
          ("aoNBT", 16),
          ("aoNetBiosName", 15),
          ("aoVlan", 13),
          ("aoipxRip8022", 22),
          ("aoipxRipEnet", 24),
          ("aoipxRipSnap", 23))
    )


_SfpsUnresolveTableAOType_Type.__name__ = "Integer32"
_SfpsUnresolveTableAOType_Object = MibTableColumn
sfpsUnresolveTableAOType = _SfpsUnresolveTableAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 3),
    _SfpsUnresolveTableAOType_Type()
)
sfpsUnresolveTableAOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAOType.setStatus("mandatory")
_SfpsUnresolveTableAOValue_Type = DisplayString
_SfpsUnresolveTableAOValue_Object = MibTableColumn
sfpsUnresolveTableAOValue = _SfpsUnresolveTableAOValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 4),
    _SfpsUnresolveTableAOValue_Type()
)
sfpsUnresolveTableAOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAOValue.setStatus("mandatory")
_SfpsUnresolveTableNumMisses_Type = Integer32
_SfpsUnresolveTableNumMisses_Object = MibTableColumn
sfpsUnresolveTableNumMisses = _SfpsUnresolveTableNumMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 5),
    _SfpsUnresolveTableNumMisses_Type()
)
sfpsUnresolveTableNumMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableNumMisses.setStatus("mandatory")
_SfpsUnresolveTableLastMissTime_Type = TimeTicks
_SfpsUnresolveTableLastMissTime_Object = MibTableColumn
sfpsUnresolveTableLastMissTime = _SfpsUnresolveTableLastMissTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 6),
    _SfpsUnresolveTableLastMissTime_Type()
)
sfpsUnresolveTableLastMissTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableLastMissTime.setStatus("mandatory")
_SfpsUnresolveTableLastCallProc_Type = Integer32
_SfpsUnresolveTableLastCallProc_Object = MibTableColumn
sfpsUnresolveTableLastCallProc = _SfpsUnresolveTableLastCallProc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 7),
    _SfpsUnresolveTableLastCallProc_Type()
)
sfpsUnresolveTableLastCallProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableLastCallProc.setStatus("mandatory")
_SfpsUnresolveTableSrcMAC_Type = SfpsAddress
_SfpsUnresolveTableSrcMAC_Object = MibTableColumn
sfpsUnresolveTableSrcMAC = _SfpsUnresolveTableSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 8),
    _SfpsUnresolveTableSrcMAC_Type()
)
sfpsUnresolveTableSrcMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableSrcMAC.setStatus("mandatory")
_SfpsUnresolveTableAvgPeriod_Type = Integer32
_SfpsUnresolveTableAvgPeriod_Object = MibTableColumn
sfpsUnresolveTableAvgPeriod = _SfpsUnresolveTableAvgPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 9),
    _SfpsUnresolveTableAvgPeriod_Type()
)
sfpsUnresolveTableAvgPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAvgPeriod.setStatus("mandatory")


class _SfpsUnresolveTableBlockFlag_Type(Integer32):
    """Custom type sfpsUnresolveTableBlockFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_SfpsUnresolveTableBlockFlag_Type.__name__ = "Integer32"
_SfpsUnresolveTableBlockFlag_Object = MibTableColumn
sfpsUnresolveTableBlockFlag = _SfpsUnresolveTableBlockFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 1, 1, 10),
    _SfpsUnresolveTableBlockFlag_Type()
)
sfpsUnresolveTableBlockFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableBlockFlag.setStatus("mandatory")


class _SfpsUnresolveTableAPIVerb_Type(Integer32):
    """Custom type sfpsUnresolveTableAPIVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("reset", 2),
          ("set-parameter", 1))
    )


_SfpsUnresolveTableAPIVerb_Type.__name__ = "Integer32"
_SfpsUnresolveTableAPIVerb_Object = MibScalar
sfpsUnresolveTableAPIVerb = _SfpsUnresolveTableAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 2, 1),
    _SfpsUnresolveTableAPIVerb_Type()
)
sfpsUnresolveTableAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAPIVerb.setStatus("mandatory")
_SfpsUnresolveTableAPIAgeOutTime_Type = Integer32
_SfpsUnresolveTableAPIAgeOutTime_Object = MibScalar
sfpsUnresolveTableAPIAgeOutTime = _SfpsUnresolveTableAPIAgeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 2, 2),
    _SfpsUnresolveTableAPIAgeOutTime_Type()
)
sfpsUnresolveTableAPIAgeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAPIAgeOutTime.setStatus("mandatory")


class _SfpsUnresolveTableAPIBlockHoldDown_Type(Integer32):
    """Custom type sfpsUnresolveTableAPIBlockHoldDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3))
    )


_SfpsUnresolveTableAPIBlockHoldDown_Type.__name__ = "Integer32"
_SfpsUnresolveTableAPIBlockHoldDown_Object = MibScalar
sfpsUnresolveTableAPIBlockHoldDown = _SfpsUnresolveTableAPIBlockHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 2, 3),
    _SfpsUnresolveTableAPIBlockHoldDown_Type()
)
sfpsUnresolveTableAPIBlockHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsUnresolveTableAPIBlockHoldDown.setStatus("mandatory")
_SfpsUnresolveTableStatsNumEntries_Type = Integer32
_SfpsUnresolveTableStatsNumEntries_Object = MibScalar
sfpsUnresolveTableStatsNumEntries = _SfpsUnresolveTableStatsNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3, 1),
    _SfpsUnresolveTableStatsNumEntries_Type()
)
sfpsUnresolveTableStatsNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableStatsNumEntries.setStatus("mandatory")
_SfpsUnresolveTableStatsTableSize_Type = Integer32
_SfpsUnresolveTableStatsTableSize_Object = MibScalar
sfpsUnresolveTableStatsTableSize = _SfpsUnresolveTableStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3, 2),
    _SfpsUnresolveTableStatsTableSize_Type()
)
sfpsUnresolveTableStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableStatsTableSize.setStatus("mandatory")
_SfpsUnresolveTableStatsTableFullCount_Type = Integer32
_SfpsUnresolveTableStatsTableFullCount_Object = MibScalar
sfpsUnresolveTableStatsTableFullCount = _SfpsUnresolveTableStatsTableFullCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3, 3),
    _SfpsUnresolveTableStatsTableFullCount_Type()
)
sfpsUnresolveTableStatsTableFullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableStatsTableFullCount.setStatus("mandatory")
_SfpsUnresolveTableStatsTotalReqSeen_Type = Integer32
_SfpsUnresolveTableStatsTotalReqSeen_Object = MibScalar
sfpsUnresolveTableStatsTotalReqSeen = _SfpsUnresolveTableStatsTotalReqSeen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3, 4),
    _SfpsUnresolveTableStatsTotalReqSeen_Type()
)
sfpsUnresolveTableStatsTotalReqSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableStatsTotalReqSeen.setStatus("mandatory")
_SfpsUnresolveTableStatsAvgReqTime_Type = Integer32
_SfpsUnresolveTableStatsAvgReqTime_Object = MibScalar
sfpsUnresolveTableStatsAvgReqTime = _SfpsUnresolveTableStatsAvgReqTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 5, 3, 5),
    _SfpsUnresolveTableStatsAvgReqTime_Type()
)
sfpsUnresolveTableStatsAvgReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsUnresolveTableStatsAvgReqTime.setStatus("mandatory")
_SfpsTableResolveTable_Object = MibTable
sfpsTableResolveTable = _SfpsTableResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sfpsTableResolveTable.setStatus("mandatory")
_SfpsTableResolveTableEntry_Object = MibTableRow
sfpsTableResolveTableEntry = _SfpsTableResolveTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1)
)
sfpsTableResolveTableEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsTableResolveTag"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsTableResolveHash"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsTableResolveHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsTableResolveTableEntry.setStatus("mandatory")
_SfpsTableResolveTag_Type = Integer32
_SfpsTableResolveTag_Object = MibTableColumn
sfpsTableResolveTag = _SfpsTableResolveTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 1),
    _SfpsTableResolveTag_Type()
)
sfpsTableResolveTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveTag.setStatus("mandatory")
_SfpsTableResolveHash_Type = Integer32
_SfpsTableResolveHash_Object = MibTableColumn
sfpsTableResolveHash = _SfpsTableResolveHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 2),
    _SfpsTableResolveHash_Type()
)
sfpsTableResolveHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveHash.setStatus("mandatory")
_SfpsTableResolveHashIndex_Type = Integer32
_SfpsTableResolveHashIndex_Object = MibTableColumn
sfpsTableResolveHashIndex = _SfpsTableResolveHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 3),
    _SfpsTableResolveHashIndex_Type()
)
sfpsTableResolveHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveHashIndex.setStatus("mandatory")
_SfpsTableResolveSrcType_Type = DisplayString
_SfpsTableResolveSrcType_Object = MibTableColumn
sfpsTableResolveSrcType = _SfpsTableResolveSrcType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 4),
    _SfpsTableResolveSrcType_Type()
)
sfpsTableResolveSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveSrcType.setStatus("mandatory")
_SfpsTableResolveSrcLoad_Type = DisplayString
_SfpsTableResolveSrcLoad_Object = MibTableColumn
sfpsTableResolveSrcLoad = _SfpsTableResolveSrcLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 5),
    _SfpsTableResolveSrcLoad_Type()
)
sfpsTableResolveSrcLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveSrcLoad.setStatus("mandatory")
_SfpsTableResolveTrgType_Type = DisplayString
_SfpsTableResolveTrgType_Object = MibTableColumn
sfpsTableResolveTrgType = _SfpsTableResolveTrgType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 6),
    _SfpsTableResolveTrgType_Type()
)
sfpsTableResolveTrgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveTrgType.setStatus("mandatory")
_SfpsTableResolveTrgLoad_Type = DisplayString
_SfpsTableResolveTrgLoad_Object = MibTableColumn
sfpsTableResolveTrgLoad = _SfpsTableResolveTrgLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 1, 1, 7),
    _SfpsTableResolveTrgLoad_Type()
)
sfpsTableResolveTrgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTableResolveTrgLoad.setStatus("mandatory")


class _SfpsTableResolveAPIVerb_Type(Integer32):
    """Custom type sfpsTableResolveAPIVerb based on Integer32"""
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
        *(("add", 2),
          ("clearTable", 5),
          ("delete", 3),
          ("modify", 4),
          ("other", 1))
    )


_SfpsTableResolveAPIVerb_Type.__name__ = "Integer32"
_SfpsTableResolveAPIVerb_Object = MibScalar
sfpsTableResolveAPIVerb = _SfpsTableResolveAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 1),
    _SfpsTableResolveAPIVerb_Type()
)
sfpsTableResolveAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIVerb.setStatus("mandatory")
_SfpsTableResolveAPISrcAOType_Type = DisplayString
_SfpsTableResolveAPISrcAOType_Object = MibScalar
sfpsTableResolveAPISrcAOType = _SfpsTableResolveAPISrcAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 2),
    _SfpsTableResolveAPISrcAOType_Type()
)
sfpsTableResolveAPISrcAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPISrcAOType.setStatus("mandatory")
_SfpsTableResolveAPISrcAOLoad_Type = DisplayString
_SfpsTableResolveAPISrcAOLoad_Object = MibScalar
sfpsTableResolveAPISrcAOLoad = _SfpsTableResolveAPISrcAOLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 3),
    _SfpsTableResolveAPISrcAOLoad_Type()
)
sfpsTableResolveAPISrcAOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPISrcAOLoad.setStatus("mandatory")
_SfpsTableResolveAPITrgAOType_Type = DisplayString
_SfpsTableResolveAPITrgAOType_Object = MibScalar
sfpsTableResolveAPITrgAOType = _SfpsTableResolveAPITrgAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 4),
    _SfpsTableResolveAPITrgAOType_Type()
)
sfpsTableResolveAPITrgAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPITrgAOType.setStatus("mandatory")
_SfpsTableResolveAPITrgAOLoad_Type = DisplayString
_SfpsTableResolveAPITrgAOLoad_Object = MibScalar
sfpsTableResolveAPITrgAOLoad = _SfpsTableResolveAPITrgAOLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 5),
    _SfpsTableResolveAPITrgAOLoad_Type()
)
sfpsTableResolveAPITrgAOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPITrgAOLoad.setStatus("mandatory")
_SfpsTableResolveAPIVlanAOLoad_Type = DisplayString
_SfpsTableResolveAPIVlanAOLoad_Object = MibScalar
sfpsTableResolveAPIVlanAOLoad = _SfpsTableResolveAPIVlanAOLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 6),
    _SfpsTableResolveAPIVlanAOLoad_Type()
)
sfpsTableResolveAPIVlanAOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIVlanAOLoad.setStatus("mandatory")
_SfpsTableResolveAPIDestSwMac_Type = DisplayString
_SfpsTableResolveAPIDestSwMac_Object = MibScalar
sfpsTableResolveAPIDestSwMac = _SfpsTableResolveAPIDestSwMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 7),
    _SfpsTableResolveAPIDestSwMac_Type()
)
sfpsTableResolveAPIDestSwMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIDestSwMac.setStatus("mandatory")


class _SfpsTableResolveAPIScopeToVlan_Type(Integer32):
    """Custom type sfpsTableResolveAPIScopeToVlan based on Integer32"""
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


_SfpsTableResolveAPIScopeToVlan_Type.__name__ = "Integer32"
_SfpsTableResolveAPIScopeToVlan_Object = MibScalar
sfpsTableResolveAPIScopeToVlan = _SfpsTableResolveAPIScopeToVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 8),
    _SfpsTableResolveAPIScopeToVlan_Type()
)
sfpsTableResolveAPIScopeToVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIScopeToVlan.setStatus("mandatory")


class _SfpsTableResolveAPINVRAMEntry_Type(Integer32):
    """Custom type sfpsTableResolveAPINVRAMEntry based on Integer32"""
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


_SfpsTableResolveAPINVRAMEntry_Type.__name__ = "Integer32"
_SfpsTableResolveAPINVRAMEntry_Object = MibScalar
sfpsTableResolveAPINVRAMEntry = _SfpsTableResolveAPINVRAMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 9),
    _SfpsTableResolveAPINVRAMEntry_Type()
)
sfpsTableResolveAPINVRAMEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPINVRAMEntry.setStatus("mandatory")
_SfpsTableResolveAPIMask_Type = HexInteger
_SfpsTableResolveAPIMask_Object = MibScalar
sfpsTableResolveAPIMask = _SfpsTableResolveAPIMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 10),
    _SfpsTableResolveAPIMask_Type()
)
sfpsTableResolveAPIMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIMask.setStatus("mandatory")


class _SfpsTableResolveAPIResolveOption_Type(Integer32):
    """Custom type sfpsTableResolveAPIResolveOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ack", 1),
          ("nak", 2))
    )


_SfpsTableResolveAPIResolveOption_Type.__name__ = "Integer32"
_SfpsTableResolveAPIResolveOption_Object = MibScalar
sfpsTableResolveAPIResolveOption = _SfpsTableResolveAPIResolveOption_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 11),
    _SfpsTableResolveAPIResolveOption_Type()
)
sfpsTableResolveAPIResolveOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIResolveOption.setStatus("mandatory")


class _SfpsTableResolveAPIAdminStatus_Type(Integer32):
    """Custom type sfpsTableResolveAPIAdminStatus based on Integer32"""
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


_SfpsTableResolveAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsTableResolveAPIAdminStatus_Object = MibScalar
sfpsTableResolveAPIAdminStatus = _SfpsTableResolveAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 6, 2, 12),
    _SfpsTableResolveAPIAdminStatus_Type()
)
sfpsTableResolveAPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsTableResolveAPIAdminStatus.setStatus("mandatory")
_SfpsSubnetResolveStatsRequests_Type = Integer32
_SfpsSubnetResolveStatsRequests_Object = MibScalar
sfpsSubnetResolveStatsRequests = _SfpsSubnetResolveStatsRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 1),
    _SfpsSubnetResolveStatsRequests_Type()
)
sfpsSubnetResolveStatsRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsRequests.setStatus("mandatory")
_SfpsSubnetResolveStatsAcks_Type = Integer32
_SfpsSubnetResolveStatsAcks_Object = MibScalar
sfpsSubnetResolveStatsAcks = _SfpsSubnetResolveStatsAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 2),
    _SfpsSubnetResolveStatsAcks_Type()
)
sfpsSubnetResolveStatsAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsAcks.setStatus("mandatory")
_SfpsSubnetResolveStatsUnknowns_Type = Integer32
_SfpsSubnetResolveStatsUnknowns_Object = MibScalar
sfpsSubnetResolveStatsUnknowns = _SfpsSubnetResolveStatsUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 3),
    _SfpsSubnetResolveStatsUnknowns_Type()
)
sfpsSubnetResolveStatsUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsUnknowns.setStatus("mandatory")
_SfpsSubnetResolveStatsInternalUnknowns_Type = Integer32
_SfpsSubnetResolveStatsInternalUnknowns_Object = MibScalar
sfpsSubnetResolveStatsInternalUnknowns = _SfpsSubnetResolveStatsInternalUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 4),
    _SfpsSubnetResolveStatsInternalUnknowns_Type()
)
sfpsSubnetResolveStatsInternalUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsInternalUnknowns.setStatus("mandatory")
_SfpsSubnetResolveStatsGatewayAcks_Type = Integer32
_SfpsSubnetResolveStatsGatewayAcks_Object = MibScalar
sfpsSubnetResolveStatsGatewayAcks = _SfpsSubnetResolveStatsGatewayAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 5),
    _SfpsSubnetResolveStatsGatewayAcks_Type()
)
sfpsSubnetResolveStatsGatewayAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsGatewayAcks.setStatus("mandatory")
_SfpsSubnetResolveStatsErrors_Type = Integer32
_SfpsSubnetResolveStatsErrors_Object = MibScalar
sfpsSubnetResolveStatsErrors = _SfpsSubnetResolveStatsErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 6),
    _SfpsSubnetResolveStatsErrors_Type()
)
sfpsSubnetResolveStatsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsErrors.setStatus("mandatory")
_SfpsSubnetResolveStatsMaxTblSize_Type = Integer32
_SfpsSubnetResolveStatsMaxTblSize_Object = MibScalar
sfpsSubnetResolveStatsMaxTblSize = _SfpsSubnetResolveStatsMaxTblSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 7),
    _SfpsSubnetResolveStatsMaxTblSize_Type()
)
sfpsSubnetResolveStatsMaxTblSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsMaxTblSize.setStatus("mandatory")
_SfpsSubnetResolveStatsTableSize_Type = Integer32
_SfpsSubnetResolveStatsTableSize_Object = MibScalar
sfpsSubnetResolveStatsTableSize = _SfpsSubnetResolveStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 1, 8),
    _SfpsSubnetResolveStatsTableSize_Type()
)
sfpsSubnetResolveStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveStatsTableSize.setStatus("mandatory")


class _SfpsSubnetResolveAPIVerb_Type(Integer32):
    """Custom type sfpsSubnetResolveAPIVerb based on Integer32"""
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
        *(("add", 2),
          ("clearDefGateway", 6),
          ("clearTable", 7),
          ("delete", 3),
          ("other", 1),
          ("setDefGateway", 5),
          ("updateMask", 4))
    )


_SfpsSubnetResolveAPIVerb_Type.__name__ = "Integer32"
_SfpsSubnetResolveAPIVerb_Object = MibScalar
sfpsSubnetResolveAPIVerb = _SfpsSubnetResolveAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 1),
    _SfpsSubnetResolveAPIVerb_Type()
)
sfpsSubnetResolveAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPIVerb.setStatus("mandatory")
_SfpsSubnetResolveAPISrcAOType_Type = DisplayString
_SfpsSubnetResolveAPISrcAOType_Object = MibScalar
sfpsSubnetResolveAPISrcAOType = _SfpsSubnetResolveAPISrcAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 2),
    _SfpsSubnetResolveAPISrcAOType_Type()
)
sfpsSubnetResolveAPISrcAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPISrcAOType.setStatus("mandatory")
_SfpsSubnetResolveAPISrcAPLoad_Type = DisplayString
_SfpsSubnetResolveAPISrcAPLoad_Object = MibScalar
sfpsSubnetResolveAPISrcAPLoad = _SfpsSubnetResolveAPISrcAPLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 3),
    _SfpsSubnetResolveAPISrcAPLoad_Type()
)
sfpsSubnetResolveAPISrcAPLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPISrcAPLoad.setStatus("mandatory")
_SfpsSubnetResolveAPITrgAOType_Type = DisplayString
_SfpsSubnetResolveAPITrgAOType_Object = MibScalar
sfpsSubnetResolveAPITrgAOType = _SfpsSubnetResolveAPITrgAOType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 4),
    _SfpsSubnetResolveAPITrgAOType_Type()
)
sfpsSubnetResolveAPITrgAOType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPITrgAOType.setStatus("mandatory")
_SfpsSubnetResolveAPITrgAOLoad_Type = DisplayString
_SfpsSubnetResolveAPITrgAOLoad_Object = MibScalar
sfpsSubnetResolveAPITrgAOLoad = _SfpsSubnetResolveAPITrgAOLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 5),
    _SfpsSubnetResolveAPITrgAOLoad_Type()
)
sfpsSubnetResolveAPITrgAOLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPITrgAOLoad.setStatus("mandatory")


class _SfpsSubnetResolveAPIRouteType_Type(Integer32):
    """Custom type sfpsSubnetResolveAPIRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("invalid", 3))
    )


_SfpsSubnetResolveAPIRouteType_Type.__name__ = "Integer32"
_SfpsSubnetResolveAPIRouteType_Object = MibScalar
sfpsSubnetResolveAPIRouteType = _SfpsSubnetResolveAPIRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 6),
    _SfpsSubnetResolveAPIRouteType_Type()
)
sfpsSubnetResolveAPIRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPIRouteType.setStatus("mandatory")


class _SfpsSubnetResolveAPINVRAMEntry_Type(Integer32):
    """Custom type sfpsSubnetResolveAPINVRAMEntry based on Integer32"""
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


_SfpsSubnetResolveAPINVRAMEntry_Type.__name__ = "Integer32"
_SfpsSubnetResolveAPINVRAMEntry_Object = MibScalar
sfpsSubnetResolveAPINVRAMEntry = _SfpsSubnetResolveAPINVRAMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 7),
    _SfpsSubnetResolveAPINVRAMEntry_Type()
)
sfpsSubnetResolveAPINVRAMEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPINVRAMEntry.setStatus("mandatory")


class _SfpsSubnetResolveAPIAdminStatus_Type(Integer32):
    """Custom type sfpsSubnetResolveAPIAdminStatus based on Integer32"""
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


_SfpsSubnetResolveAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsSubnetResolveAPIAdminStatus_Object = MibScalar
sfpsSubnetResolveAPIAdminStatus = _SfpsSubnetResolveAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 8),
    _SfpsSubnetResolveAPIAdminStatus_Type()
)
sfpsSubnetResolveAPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPIAdminStatus.setStatus("mandatory")
_SfpsSubnetResolveAPIDefGateway_Type = DisplayString
_SfpsSubnetResolveAPIDefGateway_Object = MibScalar
sfpsSubnetResolveAPIDefGateway = _SfpsSubnetResolveAPIDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 9),
    _SfpsSubnetResolveAPIDefGateway_Type()
)
sfpsSubnetResolveAPIDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPIDefGateway.setStatus("mandatory")
_SfpsSubnetResolveAPISubnetMask_Type = HexInteger
_SfpsSubnetResolveAPISubnetMask_Object = MibScalar
sfpsSubnetResolveAPISubnetMask = _SfpsSubnetResolveAPISubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 2, 10),
    _SfpsSubnetResolveAPISubnetMask_Type()
)
sfpsSubnetResolveAPISubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAPISubnetMask.setStatus("mandatory")
_SfpsSubnetResolveTable_Object = MibTable
sfpsSubnetResolveTable = _SfpsSubnetResolveTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3)
)
if mibBuilder.loadTexts:
    sfpsSubnetResolveTable.setStatus("mandatory")
_SfpsSubnetResolveEntry_Object = MibTableRow
sfpsSubnetResolveEntry = _SfpsSubnetResolveEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1)
)
sfpsSubnetResolveEntry.setIndexNames(
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsSubnetResolveTargetTag"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsSubnetResolveSourceHash"),
    (0, "CTRON-SFPS-RESOLVE-MIB", "sfpsSubnetResolveHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsSubnetResolveEntry.setStatus("mandatory")
_SfpsSubnetResolveTargetTag_Type = Integer32
_SfpsSubnetResolveTargetTag_Object = MibTableColumn
sfpsSubnetResolveTargetTag = _SfpsSubnetResolveTargetTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 1),
    _SfpsSubnetResolveTargetTag_Type()
)
sfpsSubnetResolveTargetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveTargetTag.setStatus("mandatory")
_SfpsSubnetResolveSourceHash_Type = Integer32
_SfpsSubnetResolveSourceHash_Object = MibTableColumn
sfpsSubnetResolveSourceHash = _SfpsSubnetResolveSourceHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 2),
    _SfpsSubnetResolveSourceHash_Type()
)
sfpsSubnetResolveSourceHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveSourceHash.setStatus("mandatory")
_SfpsSubnetResolveHashIndex_Type = Integer32
_SfpsSubnetResolveHashIndex_Object = MibTableColumn
sfpsSubnetResolveHashIndex = _SfpsSubnetResolveHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 3),
    _SfpsSubnetResolveHashIndex_Type()
)
sfpsSubnetResolveHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveHashIndex.setStatus("mandatory")
_SfpsSubnetResolveSrcType_Type = DisplayString
_SfpsSubnetResolveSrcType_Object = MibTableColumn
sfpsSubnetResolveSrcType = _SfpsSubnetResolveSrcType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 4),
    _SfpsSubnetResolveSrcType_Type()
)
sfpsSubnetResolveSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveSrcType.setStatus("mandatory")
_SfpsSubnetResolveSrcLoad_Type = DisplayString
_SfpsSubnetResolveSrcLoad_Object = MibTableColumn
sfpsSubnetResolveSrcLoad = _SfpsSubnetResolveSrcLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 5),
    _SfpsSubnetResolveSrcLoad_Type()
)
sfpsSubnetResolveSrcLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveSrcLoad.setStatus("mandatory")
_SfpsSubnetResolveTrgType_Type = DisplayString
_SfpsSubnetResolveTrgType_Object = MibTableColumn
sfpsSubnetResolveTrgType = _SfpsSubnetResolveTrgType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 6),
    _SfpsSubnetResolveTrgType_Type()
)
sfpsSubnetResolveTrgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveTrgType.setStatus("mandatory")
_SfpsSubnetResolveTrgLoad_Type = DisplayString
_SfpsSubnetResolveTrgLoad_Object = MibTableColumn
sfpsSubnetResolveTrgLoad = _SfpsSubnetResolveTrgLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 7),
    _SfpsSubnetResolveTrgLoad_Type()
)
sfpsSubnetResolveTrgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveTrgLoad.setStatus("mandatory")


class _SfpsSubnetResolveRouteType_Type(Integer32):
    """Custom type sfpsSubnetResolveRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("invalid", 3))
    )


_SfpsSubnetResolveRouteType_Type.__name__ = "Integer32"
_SfpsSubnetResolveRouteType_Object = MibTableColumn
sfpsSubnetResolveRouteType = _SfpsSubnetResolveRouteType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 8),
    _SfpsSubnetResolveRouteType_Type()
)
sfpsSubnetResolveRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveRouteType.setStatus("mandatory")
_SfpsSubnetResolveRelativeCnt_Type = Integer32
_SfpsSubnetResolveRelativeCnt_Object = MibTableColumn
sfpsSubnetResolveRelativeCnt = _SfpsSubnetResolveRelativeCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 9),
    _SfpsSubnetResolveRelativeCnt_Type()
)
sfpsSubnetResolveRelativeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveRelativeCnt.setStatus("mandatory")
_SfpsSubnetResolveAbsoluteCnt_Type = Integer32
_SfpsSubnetResolveAbsoluteCnt_Object = MibTableColumn
sfpsSubnetResolveAbsoluteCnt = _SfpsSubnetResolveAbsoluteCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 10),
    _SfpsSubnetResolveAbsoluteCnt_Type()
)
sfpsSubnetResolveAbsoluteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAbsoluteCnt.setStatus("mandatory")


class _SfpsSubnetResolveNVRAMEntry_Type(Integer32):
    """Custom type sfpsSubnetResolveNVRAMEntry based on Integer32"""
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


_SfpsSubnetResolveNVRAMEntry_Type.__name__ = "Integer32"
_SfpsSubnetResolveNVRAMEntry_Object = MibTableColumn
sfpsSubnetResolveNVRAMEntry = _SfpsSubnetResolveNVRAMEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 11),
    _SfpsSubnetResolveNVRAMEntry_Type()
)
sfpsSubnetResolveNVRAMEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveNVRAMEntry.setStatus("mandatory")


class _SfpsSubnetResolveAdminStatus_Type(Integer32):
    """Custom type sfpsSubnetResolveAdminStatus based on Integer32"""
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


_SfpsSubnetResolveAdminStatus_Type.__name__ = "Integer32"
_SfpsSubnetResolveAdminStatus_Object = MibTableColumn
sfpsSubnetResolveAdminStatus = _SfpsSubnetResolveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 12),
    _SfpsSubnetResolveAdminStatus_Type()
)
sfpsSubnetResolveAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveAdminStatus.setStatus("mandatory")


class _SfpsSubnetResolveOperStatus_Type(Integer32):
    """Custom type sfpsSubnetResolveOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halted", 2),
          ("running", 1))
    )


_SfpsSubnetResolveOperStatus_Type.__name__ = "Integer32"
_SfpsSubnetResolveOperStatus_Object = MibTableColumn
sfpsSubnetResolveOperStatus = _SfpsSubnetResolveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 3, 1, 13),
    _SfpsSubnetResolveOperStatus_Type()
)
sfpsSubnetResolveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveOperStatus.setStatus("mandatory")
_SfpsSubnetResolveNvramMaskEntries_Type = Integer32
_SfpsSubnetResolveNvramMaskEntries_Object = MibScalar
sfpsSubnetResolveNvramMaskEntries = _SfpsSubnetResolveNvramMaskEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 4, 2),
    _SfpsSubnetResolveNvramMaskEntries_Type()
)
sfpsSubnetResolveNvramMaskEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveNvramMaskEntries.setStatus("mandatory")
_SfpsSubnetResolveNvramIpEntries_Type = Integer32
_SfpsSubnetResolveNvramIpEntries_Object = MibScalar
sfpsSubnetResolveNvramIpEntries = _SfpsSubnetResolveNvramIpEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 7, 4, 4),
    _SfpsSubnetResolveNvramIpEntries_Type()
)
sfpsSubnetResolveNvramIpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSubnetResolveNvramIpEntries.setStatus("mandatory")
_SfpsRelayAgentResolveVlanName_Type = OctetString
_SfpsRelayAgentResolveVlanName_Object = MibScalar
sfpsRelayAgentResolveVlanName = _SfpsRelayAgentResolveVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10, 4, 2),
    _SfpsRelayAgentResolveVlanName_Type()
)
sfpsRelayAgentResolveVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRelayAgentResolveVlanName.setStatus("mandatory")
_SfpsRelayAgentResolveStatsTableSize_Type = Integer32
_SfpsRelayAgentResolveStatsTableSize_Object = MibScalar
sfpsRelayAgentResolveStatsTableSize = _SfpsRelayAgentResolveStatsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10, 5, 2),
    _SfpsRelayAgentResolveStatsTableSize_Type()
)
sfpsRelayAgentResolveStatsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRelayAgentResolveStatsTableSize.setStatus("mandatory")
_SfpsRelayAgentResolveStatsHighWater_Type = Integer32
_SfpsRelayAgentResolveStatsHighWater_Object = MibScalar
sfpsRelayAgentResolveStatsHighWater = _SfpsRelayAgentResolveStatsHighWater_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 1, 10, 5, 3),
    _SfpsRelayAgentResolveStatsHighWater_Type()
)
sfpsRelayAgentResolveStatsHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsRelayAgentResolveStatsHighWater.setStatus("mandatory")
_SfpsMobilityStatsOrigSendCount_Type = Integer32
_SfpsMobilityStatsOrigSendCount_Object = MibScalar
sfpsMobilityStatsOrigSendCount = _SfpsMobilityStatsOrigSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 1),
    _SfpsMobilityStatsOrigSendCount_Type()
)
sfpsMobilityStatsOrigSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigSendCount.setStatus("mandatory")
_SfpsMobilityStatsOrigReceiveCount_Type = Integer32
_SfpsMobilityStatsOrigReceiveCount_Object = MibScalar
sfpsMobilityStatsOrigReceiveCount = _SfpsMobilityStatsOrigReceiveCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 2),
    _SfpsMobilityStatsOrigReceiveCount_Type()
)
sfpsMobilityStatsOrigReceiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigReceiveCount.setStatus("mandatory")
_SfpsMobilityStatsOrigNUSendCount_Type = Integer32
_SfpsMobilityStatsOrigNUSendCount_Object = MibScalar
sfpsMobilityStatsOrigNUSendCount = _SfpsMobilityStatsOrigNUSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 3),
    _SfpsMobilityStatsOrigNUSendCount_Type()
)
sfpsMobilityStatsOrigNUSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigNUSendCount.setStatus("mandatory")
_SfpsMobilityStatsOrigNASendCount_Type = Integer32
_SfpsMobilityStatsOrigNASendCount_Object = MibScalar
sfpsMobilityStatsOrigNASendCount = _SfpsMobilityStatsOrigNASendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 4),
    _SfpsMobilityStatsOrigNASendCount_Type()
)
sfpsMobilityStatsOrigNASendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigNASendCount.setStatus("mandatory")
_SfpsMobilityStatsOrigNUASendReqCount_Type = Integer32
_SfpsMobilityStatsOrigNUASendReqCount_Object = MibScalar
sfpsMobilityStatsOrigNUASendReqCount = _SfpsMobilityStatsOrigNUASendReqCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 5),
    _SfpsMobilityStatsOrigNUASendReqCount_Type()
)
sfpsMobilityStatsOrigNUASendReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigNUASendReqCount.setStatus("mandatory")
_SfpsMobilityStatsOrigRetrySendCount_Type = Integer32
_SfpsMobilityStatsOrigRetrySendCount_Object = MibScalar
sfpsMobilityStatsOrigRetrySendCount = _SfpsMobilityStatsOrigRetrySendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 6),
    _SfpsMobilityStatsOrigRetrySendCount_Type()
)
sfpsMobilityStatsOrigRetrySendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigRetrySendCount.setStatus("mandatory")
_SfpsMobilityStatsOrigLocalMoveCount_Type = Integer32
_SfpsMobilityStatsOrigLocalMoveCount_Object = MibScalar
sfpsMobilityStatsOrigLocalMoveCount = _SfpsMobilityStatsOrigLocalMoveCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 7),
    _SfpsMobilityStatsOrigLocalMoveCount_Type()
)
sfpsMobilityStatsOrigLocalMoveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigLocalMoveCount.setStatus("mandatory")
_SfpsMobilityStatsOrigUnknownCount_Type = Integer32
_SfpsMobilityStatsOrigUnknownCount_Object = MibScalar
sfpsMobilityStatsOrigUnknownCount = _SfpsMobilityStatsOrigUnknownCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 8),
    _SfpsMobilityStatsOrigUnknownCount_Type()
)
sfpsMobilityStatsOrigUnknownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigUnknownCount.setStatus("mandatory")
_SfpsMobilityStatsOrigAckCount_Type = Integer32
_SfpsMobilityStatsOrigAckCount_Object = MibScalar
sfpsMobilityStatsOrigAckCount = _SfpsMobilityStatsOrigAckCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 9),
    _SfpsMobilityStatsOrigAckCount_Type()
)
sfpsMobilityStatsOrigAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigAckCount.setStatus("mandatory")
_SfpsMobilityStatsOrigNakNodeCount_Type = Integer32
_SfpsMobilityStatsOrigNakNodeCount_Object = MibScalar
sfpsMobilityStatsOrigNakNodeCount = _SfpsMobilityStatsOrigNakNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 10),
    _SfpsMobilityStatsOrigNakNodeCount_Type()
)
sfpsMobilityStatsOrigNakNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigNakNodeCount.setStatus("mandatory")
_SfpsMobilityStatsOrigNakAliasCount_Type = Integer32
_SfpsMobilityStatsOrigNakAliasCount_Object = MibScalar
sfpsMobilityStatsOrigNakAliasCount = _SfpsMobilityStatsOrigNakAliasCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 11),
    _SfpsMobilityStatsOrigNakAliasCount_Type()
)
sfpsMobilityStatsOrigNakAliasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsOrigNakAliasCount.setStatus("mandatory")
_SfpsMobilityStatsErrorCount_Type = Integer32
_SfpsMobilityStatsErrorCount_Object = MibScalar
sfpsMobilityStatsErrorCount = _SfpsMobilityStatsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 12),
    _SfpsMobilityStatsErrorCount_Type()
)
sfpsMobilityStatsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsErrorCount.setStatus("mandatory")
_SfpsMobilityStatsGenRecCount_Type = Integer32
_SfpsMobilityStatsGenRecCount_Object = MibScalar
sfpsMobilityStatsGenRecCount = _SfpsMobilityStatsGenRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 13),
    _SfpsMobilityStatsGenRecCount_Type()
)
sfpsMobilityStatsGenRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenRecCount.setStatus("mandatory")
_SfpsMobilityStatsGenSendCount_Type = Integer32
_SfpsMobilityStatsGenSendCount_Object = MibScalar
sfpsMobilityStatsGenSendCount = _SfpsMobilityStatsGenSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 14),
    _SfpsMobilityStatsGenSendCount_Type()
)
sfpsMobilityStatsGenSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenSendCount.setStatus("mandatory")
_SfpsMobilityStatsGenReqRecCount_Type = Integer32
_SfpsMobilityStatsGenReqRecCount_Object = MibScalar
sfpsMobilityStatsGenReqRecCount = _SfpsMobilityStatsGenReqRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 15),
    _SfpsMobilityStatsGenReqRecCount_Type()
)
sfpsMobilityStatsGenReqRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenReqRecCount.setStatus("mandatory")
_SfpsMobilityStatsGenReqRetryCount_Type = Integer32
_SfpsMobilityStatsGenReqRetryCount_Object = MibScalar
sfpsMobilityStatsGenReqRetryCount = _SfpsMobilityStatsGenReqRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 16),
    _SfpsMobilityStatsGenReqRetryCount_Type()
)
sfpsMobilityStatsGenReqRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenReqRetryCount.setStatus("mandatory")
_SfpsMobilityStatsGenReqForwardCount_Type = Integer32
_SfpsMobilityStatsGenReqForwardCount_Object = MibScalar
sfpsMobilityStatsGenReqForwardCount = _SfpsMobilityStatsGenReqForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 17),
    _SfpsMobilityStatsGenReqForwardCount_Type()
)
sfpsMobilityStatsGenReqForwardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenReqForwardCount.setStatus("mandatory")
_SfpsMobilityStatsGenRespRecCount_Type = Integer32
_SfpsMobilityStatsGenRespRecCount_Object = MibScalar
sfpsMobilityStatsGenRespRecCount = _SfpsMobilityStatsGenRespRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 18),
    _SfpsMobilityStatsGenRespRecCount_Type()
)
sfpsMobilityStatsGenRespRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenRespRecCount.setStatus("mandatory")
_SfpsMobilityStatsGenRespSendCount_Type = Integer32
_SfpsMobilityStatsGenRespSendCount_Object = MibScalar
sfpsMobilityStatsGenRespSendCount = _SfpsMobilityStatsGenRespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 19),
    _SfpsMobilityStatsGenRespSendCount_Type()
)
sfpsMobilityStatsGenRespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsGenRespSendCount.setStatus("mandatory")
_SfpsMobilityStatsNUReqRecCount_Type = Integer32
_SfpsMobilityStatsNUReqRecCount_Object = MibScalar
sfpsMobilityStatsNUReqRecCount = _SfpsMobilityStatsNUReqRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 20),
    _SfpsMobilityStatsNUReqRecCount_Type()
)
sfpsMobilityStatsNUReqRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNUReqRecCount.setStatus("mandatory")
_SfpsMobilityStatsNURespSendCount_Type = Integer32
_SfpsMobilityStatsNURespSendCount_Object = MibScalar
sfpsMobilityStatsNURespSendCount = _SfpsMobilityStatsNURespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 21),
    _SfpsMobilityStatsNURespSendCount_Type()
)
sfpsMobilityStatsNURespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespSendCount.setStatus("mandatory")
_SfpsMobilityStatsNAReqRecCount_Type = Integer32
_SfpsMobilityStatsNAReqRecCount_Object = MibScalar
sfpsMobilityStatsNAReqRecCount = _SfpsMobilityStatsNAReqRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 22),
    _SfpsMobilityStatsNAReqRecCount_Type()
)
sfpsMobilityStatsNAReqRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNAReqRecCount.setStatus("mandatory")
_SfpsMobilityStatsNARespSendCount_Type = Integer32
_SfpsMobilityStatsNARespSendCount_Object = MibScalar
sfpsMobilityStatsNARespSendCount = _SfpsMobilityStatsNARespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 23),
    _SfpsMobilityStatsNARespSendCount_Type()
)
sfpsMobilityStatsNARespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNARespSendCount.setStatus("mandatory")
_SfpsMobilityStatsNUARespRecUnknownCount_Type = Integer32
_SfpsMobilityStatsNUARespRecUnknownCount_Object = MibScalar
sfpsMobilityStatsNUARespRecUnknownCount = _SfpsMobilityStatsNUARespRecUnknownCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 24),
    _SfpsMobilityStatsNUARespRecUnknownCount_Type()
)
sfpsMobilityStatsNUARespRecUnknownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNUARespRecUnknownCount.setStatus("mandatory")
_SfpsMobilityStatsNURespRecAckCount_Type = Integer32
_SfpsMobilityStatsNURespRecAckCount_Object = MibScalar
sfpsMobilityStatsNURespRecAckCount = _SfpsMobilityStatsNURespRecAckCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 25),
    _SfpsMobilityStatsNURespRecAckCount_Type()
)
sfpsMobilityStatsNURespRecAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespRecAckCount.setStatus("mandatory")
_SfpsMobilityStatsNUARespRecAliasNakCount_Type = Integer32
_SfpsMobilityStatsNUARespRecAliasNakCount_Object = MibScalar
sfpsMobilityStatsNUARespRecAliasNakCount = _SfpsMobilityStatsNUARespRecAliasNakCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 26),
    _SfpsMobilityStatsNUARespRecAliasNakCount_Type()
)
sfpsMobilityStatsNUARespRecAliasNakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNUARespRecAliasNakCount.setStatus("mandatory")
_SfpsMobilityStatsNUARespRecNodeNakCount_Type = Integer32
_SfpsMobilityStatsNUARespRecNodeNakCount_Object = MibScalar
sfpsMobilityStatsNUARespRecNodeNakCount = _SfpsMobilityStatsNUARespRecNodeNakCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 27),
    _SfpsMobilityStatsNUARespRecNodeNakCount_Type()
)
sfpsMobilityStatsNUARespRecNodeNakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNUARespRecNodeNakCount.setStatus("mandatory")
_SfpsMobilityStatsNURespAliasNakSendCount_Type = Integer32
_SfpsMobilityStatsNURespAliasNakSendCount_Object = MibScalar
sfpsMobilityStatsNURespAliasNakSendCount = _SfpsMobilityStatsNURespAliasNakSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 28),
    _SfpsMobilityStatsNURespAliasNakSendCount_Type()
)
sfpsMobilityStatsNURespAliasNakSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespAliasNakSendCount.setStatus("mandatory")
_SfpsMobilityStatsNURespNodeNakSendCount_Type = Integer32
_SfpsMobilityStatsNURespNodeNakSendCount_Object = MibScalar
sfpsMobilityStatsNURespNodeNakSendCount = _SfpsMobilityStatsNURespNodeNakSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 29),
    _SfpsMobilityStatsNURespNodeNakSendCount_Type()
)
sfpsMobilityStatsNURespNodeNakSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespNodeNakSendCount.setStatus("mandatory")
_SfpsMobilityStatsNURespAckSendCount_Type = Integer32
_SfpsMobilityStatsNURespAckSendCount_Object = MibScalar
sfpsMobilityStatsNURespAckSendCount = _SfpsMobilityStatsNURespAckSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 30),
    _SfpsMobilityStatsNURespAckSendCount_Type()
)
sfpsMobilityStatsNURespAckSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespAckSendCount.setStatus("mandatory")
_SfpsMobilityStatsNURespUnknownSendCount_Type = Integer32
_SfpsMobilityStatsNURespUnknownSendCount_Object = MibScalar
sfpsMobilityStatsNURespUnknownSendCount = _SfpsMobilityStatsNURespUnknownSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 31),
    _SfpsMobilityStatsNURespUnknownSendCount_Type()
)
sfpsMobilityStatsNURespUnknownSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNURespUnknownSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterNUARespRecCount_Type = Integer32
_SfpsMobilityStatsInterNUARespRecCount_Object = MibScalar
sfpsMobilityStatsInterNUARespRecCount = _SfpsMobilityStatsInterNUARespRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 32),
    _SfpsMobilityStatsInterNUARespRecCount_Type()
)
sfpsMobilityStatsInterNUARespRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNUARespRecCount.setStatus("mandatory")
_SfpsMobilityStatsInterNUARespSendCount_Type = Integer32
_SfpsMobilityStatsInterNUARespSendCount_Object = MibScalar
sfpsMobilityStatsInterNUARespSendCount = _SfpsMobilityStatsInterNUARespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 33),
    _SfpsMobilityStatsInterNUARespSendCount_Type()
)
sfpsMobilityStatsInterNUARespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNUARespSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterNewUserRespRecCount_Type = Integer32
_SfpsMobilityStatsInterNewUserRespRecCount_Object = MibScalar
sfpsMobilityStatsInterNewUserRespRecCount = _SfpsMobilityStatsInterNewUserRespRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 34),
    _SfpsMobilityStatsInterNewUserRespRecCount_Type()
)
sfpsMobilityStatsInterNewUserRespRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNewUserRespRecCount.setStatus("mandatory")
_SfpsMobilityStatsInterNewAliasRespRecCount_Type = Integer32
_SfpsMobilityStatsInterNewAliasRespRecCount_Object = MibScalar
sfpsMobilityStatsInterNewAliasRespRecCount = _SfpsMobilityStatsInterNewAliasRespRecCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 35),
    _SfpsMobilityStatsInterNewAliasRespRecCount_Type()
)
sfpsMobilityStatsInterNewAliasRespRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNewAliasRespRecCount.setStatus("mandatory")
_SfpsMobilityStatsInterNewUserRespSendCount_Type = Integer32
_SfpsMobilityStatsInterNewUserRespSendCount_Object = MibScalar
sfpsMobilityStatsInterNewUserRespSendCount = _SfpsMobilityStatsInterNewUserRespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 36),
    _SfpsMobilityStatsInterNewUserRespSendCount_Type()
)
sfpsMobilityStatsInterNewUserRespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNewUserRespSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterNewAliasRespSendCount_Type = Integer32
_SfpsMobilityStatsInterNewAliasRespSendCount_Object = MibScalar
sfpsMobilityStatsInterNewAliasRespSendCount = _SfpsMobilityStatsInterNewAliasRespSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 37),
    _SfpsMobilityStatsInterNewAliasRespSendCount_Type()
)
sfpsMobilityStatsInterNewAliasRespSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterNewAliasRespSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterRespNakNodeSendCount_Type = Integer32
_SfpsMobilityStatsInterRespNakNodeSendCount_Object = MibScalar
sfpsMobilityStatsInterRespNakNodeSendCount = _SfpsMobilityStatsInterRespNakNodeSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 38),
    _SfpsMobilityStatsInterRespNakNodeSendCount_Type()
)
sfpsMobilityStatsInterRespNakNodeSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterRespNakNodeSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterRespNakAliasSendCount_Type = Integer32
_SfpsMobilityStatsInterRespNakAliasSendCount_Object = MibScalar
sfpsMobilityStatsInterRespNakAliasSendCount = _SfpsMobilityStatsInterRespNakAliasSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 39),
    _SfpsMobilityStatsInterRespNakAliasSendCount_Type()
)
sfpsMobilityStatsInterRespNakAliasSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterRespNakAliasSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterRespUnknownSendCount_Type = Integer32
_SfpsMobilityStatsInterRespUnknownSendCount_Object = MibScalar
sfpsMobilityStatsInterRespUnknownSendCount = _SfpsMobilityStatsInterRespUnknownSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 40),
    _SfpsMobilityStatsInterRespUnknownSendCount_Type()
)
sfpsMobilityStatsInterRespUnknownSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterRespUnknownSendCount.setStatus("mandatory")
_SfpsMobilityStatsInterRespAckSendCount_Type = Integer32
_SfpsMobilityStatsInterRespAckSendCount_Object = MibScalar
sfpsMobilityStatsInterRespAckSendCount = _SfpsMobilityStatsInterRespAckSendCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 41),
    _SfpsMobilityStatsInterRespAckSendCount_Type()
)
sfpsMobilityStatsInterRespAckSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsInterRespAckSendCount.setStatus("mandatory")
_SfpsMobilityStatsAliasOnOfSwitch_Type = Integer32
_SfpsMobilityStatsAliasOnOfSwitch_Object = MibScalar
sfpsMobilityStatsAliasOnOfSwitch = _SfpsMobilityStatsAliasOnOfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 42),
    _SfpsMobilityStatsAliasOnOfSwitch_Type()
)
sfpsMobilityStatsAliasOnOfSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMobilityStatsAliasOnOfSwitch.setStatus("mandatory")
_SfpsMobilityStatsResetCounters_Type = Integer32
_SfpsMobilityStatsResetCounters_Object = MibScalar
sfpsMobilityStatsResetCounters = _SfpsMobilityStatsResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 43),
    _SfpsMobilityStatsResetCounters_Type()
)
sfpsMobilityStatsResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsResetCounters.setStatus("mandatory")
_SfpsMobilityStatsRetryCount_Type = Integer32
_SfpsMobilityStatsRetryCount_Object = MibScalar
sfpsMobilityStatsRetryCount = _SfpsMobilityStatsRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 44),
    _SfpsMobilityStatsRetryCount_Type()
)
sfpsMobilityStatsRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsRetryCount.setStatus("mandatory")
_SfpsMobilityStatsRetryDrops_Type = Integer32
_SfpsMobilityStatsRetryDrops_Object = MibScalar
sfpsMobilityStatsRetryDrops = _SfpsMobilityStatsRetryDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 45),
    _SfpsMobilityStatsRetryDrops_Type()
)
sfpsMobilityStatsRetryDrops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsRetryDrops.setStatus("mandatory")
_SfpsMobilityStatsMaxRetryReached_Type = Integer32
_SfpsMobilityStatsMaxRetryReached_Object = MibScalar
sfpsMobilityStatsMaxRetryReached = _SfpsMobilityStatsMaxRetryReached_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 46),
    _SfpsMobilityStatsMaxRetryReached_Type()
)
sfpsMobilityStatsMaxRetryReached.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsMaxRetryReached.setStatus("mandatory")
_SfpsMobilityStatsNewUserRetryTime_Type = Integer32
_SfpsMobilityStatsNewUserRetryTime_Object = MibScalar
sfpsMobilityStatsNewUserRetryTime = _SfpsMobilityStatsNewUserRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 47),
    _SfpsMobilityStatsNewUserRetryTime_Type()
)
sfpsMobilityStatsNewUserRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNewUserRetryTime.setStatus("mandatory")
_SfpsMobilityStatsMaxNewUserRetries_Type = Integer32
_SfpsMobilityStatsMaxNewUserRetries_Object = MibScalar
sfpsMobilityStatsMaxNewUserRetries = _SfpsMobilityStatsMaxNewUserRetries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 48),
    _SfpsMobilityStatsMaxNewUserRetries_Type()
)
sfpsMobilityStatsMaxNewUserRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsMaxNewUserRetries.setStatus("mandatory")
_SfpsMobilityStatsNewUserStaleTimeout_Type = Integer32
_SfpsMobilityStatsNewUserStaleTimeout_Object = MibScalar
sfpsMobilityStatsNewUserStaleTimeout = _SfpsMobilityStatsNewUserStaleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 49),
    _SfpsMobilityStatsNewUserStaleTimeout_Type()
)
sfpsMobilityStatsNewUserStaleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsNewUserStaleTimeout.setStatus("mandatory")
_SfpsMobilityStatsAvgResponseTime_Type = Integer32
_SfpsMobilityStatsAvgResponseTime_Object = MibScalar
sfpsMobilityStatsAvgResponseTime = _SfpsMobilityStatsAvgResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 50),
    _SfpsMobilityStatsAvgResponseTime_Type()
)
sfpsMobilityStatsAvgResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsAvgResponseTime.setStatus("mandatory")
_SfpsMobilityStatsMaxResponeTime_Type = Integer32
_SfpsMobilityStatsMaxResponeTime_Object = MibScalar
sfpsMobilityStatsMaxResponeTime = _SfpsMobilityStatsMaxResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 9, 2, 3, 51),
    _SfpsMobilityStatsMaxResponeTime_Type()
)
sfpsMobilityStatsMaxResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsMobilityStatsMaxResponeTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-RESOLVE-MIB",
    **{"HexInteger": HexInteger,
       "SfpsAddress": SfpsAddress,
       "sfpsServiceCenterResolveTable": sfpsServiceCenterResolveTable,
       "sfpsServiceCenterResolveEntry": sfpsServiceCenterResolveEntry,
       "sfpsServiceCenterResolveHashLeaf": sfpsServiceCenterResolveHashLeaf,
       "sfpsServiceCenterResolveMetric": sfpsServiceCenterResolveMetric,
       "sfpsServiceCenterResolveName": sfpsServiceCenterResolveName,
       "sfpsServiceCenterResolveOperStatus": sfpsServiceCenterResolveOperStatus,
       "sfpsServiceCenterResolveAdminStatus": sfpsServiceCenterResolveAdminStatus,
       "sfpsServiceCenterResolveStatusTime": sfpsServiceCenterResolveStatusTime,
       "sfpsServiceCenterResolveRequests": sfpsServiceCenterResolveRequests,
       "sfpsServiceCenterResolveResponses": sfpsServiceCenterResolveResponses,
       "sfpsSwitchResolveTable": sfpsSwitchResolveTable,
       "sfpsSwitchResolveEntry": sfpsSwitchResolveEntry,
       "sfpsSwitchResolveSwitch": sfpsSwitchResolveSwitch,
       "sfpsSwitchResolveCallTag": sfpsSwitchResolveCallTag,
       "sfpsSwitchResolvePortNum": sfpsSwitchResolvePortNum,
       "sfpsSwitchResolveNeighborSw": sfpsSwitchResolveNeighborSw,
       "sfpsSwitchResolveRequestCount": sfpsSwitchResolveRequestCount,
       "sfpsSwitchResolveResponseCount": sfpsSwitchResolveResponseCount,
       "sfpsSwitchResolveMobilityRetry": sfpsSwitchResolveMobilityRetry,
       "sfpsSwitchResolveEventId": sfpsSwitchResolveEventId,
       "sfpsResolveStatsRequests": sfpsResolveStatsRequests,
       "sfpsResolveStatsResponses": sfpsResolveStatsResponses,
       "sfpsResolveStatsAcks": sfpsResolveStatsAcks,
       "sfpsResolveStatsNaks": sfpsResolveStatsNaks,
       "sfpsResolveStatsUnknowns": sfpsResolveStatsUnknowns,
       "sfpsResolveStatsNoAnswer": sfpsResolveStatsNoAnswer,
       "sfpsResolveStatsTimeout": sfpsResolveStatsTimeout,
       "sfpsResolveStatsAvgResponseTime": sfpsResolveStatsAvgResponseTime,
       "sfpsResolveStatsTableSize": sfpsResolveStatsTableSize,
       "sfpsResolveStatsTableHigh": sfpsResolveStatsTableHigh,
       "sfpsResolveStatsErrorCount": sfpsResolveStatsErrorCount,
       "sfpsResolveStatsStaleCount": sfpsResolveStatsStaleCount,
       "sfpsResolveStatsDupMsgCount": sfpsResolveStatsDupMsgCount,
       "sfpsResolveStatsReqRcvd": sfpsResolveStatsReqRcvd,
       "sfpsResolveStatsRespAcksSent": sfpsResolveStatsRespAcksSent,
       "sfpsResolveStatsRespNaksSent": sfpsResolveStatsRespNaksSent,
       "sfpsResolveStatsRespUnknownsSent": sfpsResolveStatsRespUnknownsSent,
       "sfpsResolveStatsRespRecvd": sfpsResolveStatsRespRecvd,
       "sfpsResolveStatsResolveMask": sfpsResolveStatsResolveMask,
       "sfpsResolveStatsINBMask": sfpsResolveStatsINBMask,
       "sfpsResolveStatsFloodMask": sfpsResolveStatsFloodMask,
       "sfpsResolveStatsChangeCount": sfpsResolveStatsChangeCount,
       "sfpsResolveStatsChangeTime": sfpsResolveStatsChangeTime,
       "sfpsResolveStatsResetStats": sfpsResolveStatsResetStats,
       "sfpsResolveStatsAnswerUnknown": sfpsResolveStatsAnswerUnknown,
       "sfpsResolveStatsDisableProxy": sfpsResolveStatsDisableProxy,
       "sfpsResolveStatsDisableLayer3": sfpsResolveStatsDisableLayer3,
       "sfpsResolveStatsCSPDaveMalPkts": sfpsResolveStatsCSPDaveMalPkts,
       "sfpsResolveStatsStaleTimeOut": sfpsResolveStatsStaleTimeOut,
       "sfpsResolveStatsMaxResponseTime": sfpsResolveStatsMaxResponseTime,
       "sfpsResolveStatsStaleEntryLost": sfpsResolveStatsStaleEntryLost,
       "sfpsResolveStatsDaveEntryLost": sfpsResolveStatsDaveEntryLost,
       "sfpsBlockResolveTable": sfpsBlockResolveTable,
       "sfpsBlockResolveTableEntry": sfpsBlockResolveTableEntry,
       "sfpsBlockResolveTableHash": sfpsBlockResolveTableHash,
       "sfpsBlockResolveTableHashIndex": sfpsBlockResolveTableHashIndex,
       "sfpsBlockResolveTableAOType": sfpsBlockResolveTableAOType,
       "sfpsBlockResolveTableAOValue": sfpsBlockResolveTableAOValue,
       "sfpsBlockResolveTableStartTime": sfpsBlockResolveTableStartTime,
       "sfpsBlockResolveTableNumBlocked": sfpsBlockResolveTableNumBlocked,
       "sfpsBlockResolveTableNumSent": sfpsBlockResolveTableNumSent,
       "sfpsBlockResolveTableLastSeen": sfpsBlockResolveTableLastSeen,
       "sfpsBlockResolveTableAvgPeriod": sfpsBlockResolveTableAvgPeriod,
       "sfpsBlockResolveAPIVerb": sfpsBlockResolveAPIVerb,
       "sfpsBlockResolveAPIAOType": sfpsBlockResolveAPIAOType,
       "sfpsBlockResolveAPIAOValue": sfpsBlockResolveAPIAOValue,
       "sfpsBlockResolveAPITestCount": sfpsBlockResolveAPITestCount,
       "sfpsBlockResolveAPIThreshold": sfpsBlockResolveAPIThreshold,
       "sfpsBlockResolveAPISendPeriod": sfpsBlockResolveAPISendPeriod,
       "sfpsBlockResolveStatsNumEntries": sfpsBlockResolveStatsNumEntries,
       "sfpsBlockResolveStatsTableSize": sfpsBlockResolveStatsTableSize,
       "sfpsBlockResolveStatsTotalReqSeen": sfpsBlockResolveStatsTotalReqSeen,
       "sfpsBlockResolveStatsTotalBlocked": sfpsBlockResolveStatsTotalBlocked,
       "sfpsBlockResolveStatsTotalSent": sfpsBlockResolveStatsTotalSent,
       "sfpsBlockResolveStatsAvgReqTime": sfpsBlockResolveStatsAvgReqTime,
       "sfpsUnresolveTable": sfpsUnresolveTable,
       "sfpsUnresolveTableEntry": sfpsUnresolveTableEntry,
       "sfpsUnresolveTableHash": sfpsUnresolveTableHash,
       "sfpsUnresolveTableHashIndex": sfpsUnresolveTableHashIndex,
       "sfpsUnresolveTableAOType": sfpsUnresolveTableAOType,
       "sfpsUnresolveTableAOValue": sfpsUnresolveTableAOValue,
       "sfpsUnresolveTableNumMisses": sfpsUnresolveTableNumMisses,
       "sfpsUnresolveTableLastMissTime": sfpsUnresolveTableLastMissTime,
       "sfpsUnresolveTableLastCallProc": sfpsUnresolveTableLastCallProc,
       "sfpsUnresolveTableSrcMAC": sfpsUnresolveTableSrcMAC,
       "sfpsUnresolveTableAvgPeriod": sfpsUnresolveTableAvgPeriod,
       "sfpsUnresolveTableBlockFlag": sfpsUnresolveTableBlockFlag,
       "sfpsUnresolveTableAPIVerb": sfpsUnresolveTableAPIVerb,
       "sfpsUnresolveTableAPIAgeOutTime": sfpsUnresolveTableAPIAgeOutTime,
       "sfpsUnresolveTableAPIBlockHoldDown": sfpsUnresolveTableAPIBlockHoldDown,
       "sfpsUnresolveTableStatsNumEntries": sfpsUnresolveTableStatsNumEntries,
       "sfpsUnresolveTableStatsTableSize": sfpsUnresolveTableStatsTableSize,
       "sfpsUnresolveTableStatsTableFullCount": sfpsUnresolveTableStatsTableFullCount,
       "sfpsUnresolveTableStatsTotalReqSeen": sfpsUnresolveTableStatsTotalReqSeen,
       "sfpsUnresolveTableStatsAvgReqTime": sfpsUnresolveTableStatsAvgReqTime,
       "sfpsTableResolveTable": sfpsTableResolveTable,
       "sfpsTableResolveTableEntry": sfpsTableResolveTableEntry,
       "sfpsTableResolveTag": sfpsTableResolveTag,
       "sfpsTableResolveHash": sfpsTableResolveHash,
       "sfpsTableResolveHashIndex": sfpsTableResolveHashIndex,
       "sfpsTableResolveSrcType": sfpsTableResolveSrcType,
       "sfpsTableResolveSrcLoad": sfpsTableResolveSrcLoad,
       "sfpsTableResolveTrgType": sfpsTableResolveTrgType,
       "sfpsTableResolveTrgLoad": sfpsTableResolveTrgLoad,
       "sfpsTableResolveAPIVerb": sfpsTableResolveAPIVerb,
       "sfpsTableResolveAPISrcAOType": sfpsTableResolveAPISrcAOType,
       "sfpsTableResolveAPISrcAOLoad": sfpsTableResolveAPISrcAOLoad,
       "sfpsTableResolveAPITrgAOType": sfpsTableResolveAPITrgAOType,
       "sfpsTableResolveAPITrgAOLoad": sfpsTableResolveAPITrgAOLoad,
       "sfpsTableResolveAPIVlanAOLoad": sfpsTableResolveAPIVlanAOLoad,
       "sfpsTableResolveAPIDestSwMac": sfpsTableResolveAPIDestSwMac,
       "sfpsTableResolveAPIScopeToVlan": sfpsTableResolveAPIScopeToVlan,
       "sfpsTableResolveAPINVRAMEntry": sfpsTableResolveAPINVRAMEntry,
       "sfpsTableResolveAPIMask": sfpsTableResolveAPIMask,
       "sfpsTableResolveAPIResolveOption": sfpsTableResolveAPIResolveOption,
       "sfpsTableResolveAPIAdminStatus": sfpsTableResolveAPIAdminStatus,
       "sfpsSubnetResolveStatsRequests": sfpsSubnetResolveStatsRequests,
       "sfpsSubnetResolveStatsAcks": sfpsSubnetResolveStatsAcks,
       "sfpsSubnetResolveStatsUnknowns": sfpsSubnetResolveStatsUnknowns,
       "sfpsSubnetResolveStatsInternalUnknowns": sfpsSubnetResolveStatsInternalUnknowns,
       "sfpsSubnetResolveStatsGatewayAcks": sfpsSubnetResolveStatsGatewayAcks,
       "sfpsSubnetResolveStatsErrors": sfpsSubnetResolveStatsErrors,
       "sfpsSubnetResolveStatsMaxTblSize": sfpsSubnetResolveStatsMaxTblSize,
       "sfpsSubnetResolveStatsTableSize": sfpsSubnetResolveStatsTableSize,
       "sfpsSubnetResolveAPIVerb": sfpsSubnetResolveAPIVerb,
       "sfpsSubnetResolveAPISrcAOType": sfpsSubnetResolveAPISrcAOType,
       "sfpsSubnetResolveAPISrcAPLoad": sfpsSubnetResolveAPISrcAPLoad,
       "sfpsSubnetResolveAPITrgAOType": sfpsSubnetResolveAPITrgAOType,
       "sfpsSubnetResolveAPITrgAOLoad": sfpsSubnetResolveAPITrgAOLoad,
       "sfpsSubnetResolveAPIRouteType": sfpsSubnetResolveAPIRouteType,
       "sfpsSubnetResolveAPINVRAMEntry": sfpsSubnetResolveAPINVRAMEntry,
       "sfpsSubnetResolveAPIAdminStatus": sfpsSubnetResolveAPIAdminStatus,
       "sfpsSubnetResolveAPIDefGateway": sfpsSubnetResolveAPIDefGateway,
       "sfpsSubnetResolveAPISubnetMask": sfpsSubnetResolveAPISubnetMask,
       "sfpsSubnetResolveTable": sfpsSubnetResolveTable,
       "sfpsSubnetResolveEntry": sfpsSubnetResolveEntry,
       "sfpsSubnetResolveTargetTag": sfpsSubnetResolveTargetTag,
       "sfpsSubnetResolveSourceHash": sfpsSubnetResolveSourceHash,
       "sfpsSubnetResolveHashIndex": sfpsSubnetResolveHashIndex,
       "sfpsSubnetResolveSrcType": sfpsSubnetResolveSrcType,
       "sfpsSubnetResolveSrcLoad": sfpsSubnetResolveSrcLoad,
       "sfpsSubnetResolveTrgType": sfpsSubnetResolveTrgType,
       "sfpsSubnetResolveTrgLoad": sfpsSubnetResolveTrgLoad,
       "sfpsSubnetResolveRouteType": sfpsSubnetResolveRouteType,
       "sfpsSubnetResolveRelativeCnt": sfpsSubnetResolveRelativeCnt,
       "sfpsSubnetResolveAbsoluteCnt": sfpsSubnetResolveAbsoluteCnt,
       "sfpsSubnetResolveNVRAMEntry": sfpsSubnetResolveNVRAMEntry,
       "sfpsSubnetResolveAdminStatus": sfpsSubnetResolveAdminStatus,
       "sfpsSubnetResolveOperStatus": sfpsSubnetResolveOperStatus,
       "sfpsSubnetResolveNvramMaskEntries": sfpsSubnetResolveNvramMaskEntries,
       "sfpsSubnetResolveNvramIpEntries": sfpsSubnetResolveNvramIpEntries,
       "sfpsRelayAgentResolveVlanName": sfpsRelayAgentResolveVlanName,
       "sfpsRelayAgentResolveStatsTableSize": sfpsRelayAgentResolveStatsTableSize,
       "sfpsRelayAgentResolveStatsHighWater": sfpsRelayAgentResolveStatsHighWater,
       "sfpsMobilityStatsOrigSendCount": sfpsMobilityStatsOrigSendCount,
       "sfpsMobilityStatsOrigReceiveCount": sfpsMobilityStatsOrigReceiveCount,
       "sfpsMobilityStatsOrigNUSendCount": sfpsMobilityStatsOrigNUSendCount,
       "sfpsMobilityStatsOrigNASendCount": sfpsMobilityStatsOrigNASendCount,
       "sfpsMobilityStatsOrigNUASendReqCount": sfpsMobilityStatsOrigNUASendReqCount,
       "sfpsMobilityStatsOrigRetrySendCount": sfpsMobilityStatsOrigRetrySendCount,
       "sfpsMobilityStatsOrigLocalMoveCount": sfpsMobilityStatsOrigLocalMoveCount,
       "sfpsMobilityStatsOrigUnknownCount": sfpsMobilityStatsOrigUnknownCount,
       "sfpsMobilityStatsOrigAckCount": sfpsMobilityStatsOrigAckCount,
       "sfpsMobilityStatsOrigNakNodeCount": sfpsMobilityStatsOrigNakNodeCount,
       "sfpsMobilityStatsOrigNakAliasCount": sfpsMobilityStatsOrigNakAliasCount,
       "sfpsMobilityStatsErrorCount": sfpsMobilityStatsErrorCount,
       "sfpsMobilityStatsGenRecCount": sfpsMobilityStatsGenRecCount,
       "sfpsMobilityStatsGenSendCount": sfpsMobilityStatsGenSendCount,
       "sfpsMobilityStatsGenReqRecCount": sfpsMobilityStatsGenReqRecCount,
       "sfpsMobilityStatsGenReqRetryCount": sfpsMobilityStatsGenReqRetryCount,
       "sfpsMobilityStatsGenReqForwardCount": sfpsMobilityStatsGenReqForwardCount,
       "sfpsMobilityStatsGenRespRecCount": sfpsMobilityStatsGenRespRecCount,
       "sfpsMobilityStatsGenRespSendCount": sfpsMobilityStatsGenRespSendCount,
       "sfpsMobilityStatsNUReqRecCount": sfpsMobilityStatsNUReqRecCount,
       "sfpsMobilityStatsNURespSendCount": sfpsMobilityStatsNURespSendCount,
       "sfpsMobilityStatsNAReqRecCount": sfpsMobilityStatsNAReqRecCount,
       "sfpsMobilityStatsNARespSendCount": sfpsMobilityStatsNARespSendCount,
       "sfpsMobilityStatsNUARespRecUnknownCount": sfpsMobilityStatsNUARespRecUnknownCount,
       "sfpsMobilityStatsNURespRecAckCount": sfpsMobilityStatsNURespRecAckCount,
       "sfpsMobilityStatsNUARespRecAliasNakCount": sfpsMobilityStatsNUARespRecAliasNakCount,
       "sfpsMobilityStatsNUARespRecNodeNakCount": sfpsMobilityStatsNUARespRecNodeNakCount,
       "sfpsMobilityStatsNURespAliasNakSendCount": sfpsMobilityStatsNURespAliasNakSendCount,
       "sfpsMobilityStatsNURespNodeNakSendCount": sfpsMobilityStatsNURespNodeNakSendCount,
       "sfpsMobilityStatsNURespAckSendCount": sfpsMobilityStatsNURespAckSendCount,
       "sfpsMobilityStatsNURespUnknownSendCount": sfpsMobilityStatsNURespUnknownSendCount,
       "sfpsMobilityStatsInterNUARespRecCount": sfpsMobilityStatsInterNUARespRecCount,
       "sfpsMobilityStatsInterNUARespSendCount": sfpsMobilityStatsInterNUARespSendCount,
       "sfpsMobilityStatsInterNewUserRespRecCount": sfpsMobilityStatsInterNewUserRespRecCount,
       "sfpsMobilityStatsInterNewAliasRespRecCount": sfpsMobilityStatsInterNewAliasRespRecCount,
       "sfpsMobilityStatsInterNewUserRespSendCount": sfpsMobilityStatsInterNewUserRespSendCount,
       "sfpsMobilityStatsInterNewAliasRespSendCount": sfpsMobilityStatsInterNewAliasRespSendCount,
       "sfpsMobilityStatsInterRespNakNodeSendCount": sfpsMobilityStatsInterRespNakNodeSendCount,
       "sfpsMobilityStatsInterRespNakAliasSendCount": sfpsMobilityStatsInterRespNakAliasSendCount,
       "sfpsMobilityStatsInterRespUnknownSendCount": sfpsMobilityStatsInterRespUnknownSendCount,
       "sfpsMobilityStatsInterRespAckSendCount": sfpsMobilityStatsInterRespAckSendCount,
       "sfpsMobilityStatsAliasOnOfSwitch": sfpsMobilityStatsAliasOnOfSwitch,
       "sfpsMobilityStatsResetCounters": sfpsMobilityStatsResetCounters,
       "sfpsMobilityStatsRetryCount": sfpsMobilityStatsRetryCount,
       "sfpsMobilityStatsRetryDrops": sfpsMobilityStatsRetryDrops,
       "sfpsMobilityStatsMaxRetryReached": sfpsMobilityStatsMaxRetryReached,
       "sfpsMobilityStatsNewUserRetryTime": sfpsMobilityStatsNewUserRetryTime,
       "sfpsMobilityStatsMaxNewUserRetries": sfpsMobilityStatsMaxNewUserRetries,
       "sfpsMobilityStatsNewUserStaleTimeout": sfpsMobilityStatsNewUserStaleTimeout,
       "sfpsMobilityStatsAvgResponseTime": sfpsMobilityStatsAvgResponseTime,
       "sfpsMobilityStatsMaxResponeTime": sfpsMobilityStatsMaxResponeTime}
)
