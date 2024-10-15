# SNMP MIB module (CISCO-TN3270SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TN3270SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:43 2024
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoTn3270ServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54)
)
ciscoTn3270ServerMIB.setRevisions(
        ("1997-01-22 00:00",
         "1996-09-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Tn3270sUnsigned32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class Tn3270sTCPPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class Tn3270sPUIndex(Tn3270sUnsigned32, TextualConvention):
    status = "current"


class Tn3270sLUIndex(Tn3270sUnsigned32, TextualConvention):
    status = "current"


class Tn3270sCpuCard(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 16),
    )



# MIB Managed Objects in the order of their OIDs

_Tn3270sObjects_ObjectIdentity = ObjectIdentity
tn3270sObjects = _Tn3270sObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1)
)
_Tn3270sGlobal_ObjectIdentity = ObjectIdentity
tn3270sGlobal = _Tn3270sGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1)
)
_Tn3270sGlobalTable_Object = MibTable
tn3270sGlobalTable = _Tn3270sGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tn3270sGlobalTable.setStatus("current")
_Tn3270sGlobalEntry_Object = MibTableRow
tn3270sGlobalEntry = _Tn3270sGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1)
)
tn3270sGlobalEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
)
if mibBuilder.loadTexts:
    tn3270sGlobalEntry.setStatus("current")
_Tn3270sIndex_Type = Tn3270sUnsigned32
_Tn3270sIndex_Object = MibTableColumn
tn3270sIndex = _Tn3270sIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 1),
    _Tn3270sIndex_Type()
)
tn3270sIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sIndex.setStatus("current")
_Tn3270sCpuCard_Type = Tn3270sCpuCard
_Tn3270sCpuCard_Object = MibTableColumn
tn3270sCpuCard = _Tn3270sCpuCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 2),
    _Tn3270sCpuCard_Type()
)
tn3270sCpuCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sCpuCard.setStatus("current")


class _Tn3270sMaxLus_Type(Tn3270sUnsigned32):
    """Custom type tn3270sMaxLus based on Tn3270sUnsigned32"""
    subtypeSpec = Tn3270sUnsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Tn3270sMaxLus_Type.__name__ = "Tn3270sUnsigned32"
_Tn3270sMaxLus_Object = MibTableColumn
tn3270sMaxLus = _Tn3270sMaxLus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 3),
    _Tn3270sMaxLus_Type()
)
tn3270sMaxLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sMaxLus.setStatus("current")


class _Tn3270sLusInUse_Type(Gauge32):
    """Custom type tn3270sLusInUse based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270sLusInUse_Type.__name__ = "Gauge32"
_Tn3270sLusInUse_Object = MibTableColumn
tn3270sLusInUse = _Tn3270sLusInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 4),
    _Tn3270sLusInUse_Type()
)
tn3270sLusInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLusInUse.setStatus("current")
_Tn3270sStartupTime_Type = TimeStamp
_Tn3270sStartupTime_Object = MibTableColumn
tn3270sStartupTime = _Tn3270sStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 5),
    _Tn3270sStartupTime_Type()
)
tn3270sStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStartupTime.setStatus("current")
_Tn3270sGlobalTcpPort_Type = Tn3270sTCPPort
_Tn3270sGlobalTcpPort_Object = MibTableColumn
tn3270sGlobalTcpPort = _Tn3270sGlobalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 6),
    _Tn3270sGlobalTcpPort_Type()
)
tn3270sGlobalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sGlobalTcpPort.setStatus("current")


class _Tn3270sGlobalIdleTimeout_Type(Integer32):
    """Custom type tn3270sGlobalIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Tn3270sGlobalIdleTimeout_Type.__name__ = "Integer32"
_Tn3270sGlobalIdleTimeout_Object = MibTableColumn
tn3270sGlobalIdleTimeout = _Tn3270sGlobalIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 7),
    _Tn3270sGlobalIdleTimeout_Type()
)
tn3270sGlobalIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sGlobalIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sGlobalIdleTimeout.setUnits("seconds")


class _Tn3270sGlobalKeepAlive_Type(Integer32):
    """Custom type tn3270sGlobalKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Tn3270sGlobalKeepAlive_Type.__name__ = "Integer32"
_Tn3270sGlobalKeepAlive_Object = MibTableColumn
tn3270sGlobalKeepAlive = _Tn3270sGlobalKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 8),
    _Tn3270sGlobalKeepAlive_Type()
)
tn3270sGlobalKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sGlobalKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sGlobalKeepAlive.setUnits("seconds")


class _Tn3270sGlobalUnbindAction_Type(Integer32):
    """Custom type tn3270sGlobalUnbindAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("keep", 1))
    )


_Tn3270sGlobalUnbindAction_Type.__name__ = "Integer32"
_Tn3270sGlobalUnbindAction_Object = MibTableColumn
tn3270sGlobalUnbindAction = _Tn3270sGlobalUnbindAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 9),
    _Tn3270sGlobalUnbindAction_Type()
)
tn3270sGlobalUnbindAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sGlobalUnbindAction.setStatus("current")


class _Tn3270sGlobalGenericPool_Type(Integer32):
    """Custom type tn3270sGlobalGenericPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_Tn3270sGlobalGenericPool_Type.__name__ = "Integer32"
_Tn3270sGlobalGenericPool_Object = MibTableColumn
tn3270sGlobalGenericPool = _Tn3270sGlobalGenericPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 10),
    _Tn3270sGlobalGenericPool_Type()
)
tn3270sGlobalGenericPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sGlobalGenericPool.setStatus("current")
_Tn3270sTimingMarkSupported_Type = TruthValue
_Tn3270sTimingMarkSupported_Object = MibTableColumn
tn3270sTimingMarkSupported = _Tn3270sTimingMarkSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 11),
    _Tn3270sTimingMarkSupported_Type()
)
tn3270sTimingMarkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sTimingMarkSupported.setStatus("current")
_Tn3270sRunningTime_Type = Tn3270sUnsigned32
_Tn3270sRunningTime_Object = MibTableColumn
tn3270sRunningTime = _Tn3270sRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 1, 1, 1, 12),
    _Tn3270sRunningTime_Type()
)
tn3270sRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sRunningTime.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sRunningTime.setUnits("seconds")
_Tn3270sStats_ObjectIdentity = ObjectIdentity
tn3270sStats = _Tn3270sStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2)
)
_Tn3270sStatsTable_Object = MibTable
tn3270sStatsTable = _Tn3270sStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tn3270sStatsTable.setStatus("current")
_Tn3270sStatsEntry_Object = MibTableRow
tn3270sStatsEntry = _Tn3270sStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1)
)
tn3270sStatsEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sStatsServerAddr"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sStatsServerTcpPort"),
)
if mibBuilder.loadTexts:
    tn3270sStatsEntry.setStatus("current")
_Tn3270sStatsServerAddr_Type = IpAddress
_Tn3270sStatsServerAddr_Object = MibTableColumn
tn3270sStatsServerAddr = _Tn3270sStatsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 1),
    _Tn3270sStatsServerAddr_Type()
)
tn3270sStatsServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sStatsServerAddr.setStatus("current")
_Tn3270sStatsServerTcpPort_Type = Tn3270sTCPPort
_Tn3270sStatsServerTcpPort_Object = MibTableColumn
tn3270sStatsServerTcpPort = _Tn3270sStatsServerTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 2),
    _Tn3270sStatsServerTcpPort_Type()
)
tn3270sStatsServerTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sStatsServerTcpPort.setStatus("current")
_Tn3270sStatsMaxSess_Type = Gauge32
_Tn3270sStatsMaxSess_Object = MibTableColumn
tn3270sStatsMaxSess = _Tn3270sStatsMaxSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 3),
    _Tn3270sStatsMaxSess_Type()
)
tn3270sStatsMaxSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsMaxSess.setStatus("current")
_Tn3270sStatsSpareSess_Type = Gauge32
_Tn3270sStatsSpareSess_Object = MibTableColumn
tn3270sStatsSpareSess = _Tn3270sStatsSpareSess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 4),
    _Tn3270sStatsSpareSess_Type()
)
tn3270sStatsSpareSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsSpareSess.setStatus("current")
_Tn3270sStatsConnectsIn_Type = Counter32
_Tn3270sStatsConnectsIn_Object = MibTableColumn
tn3270sStatsConnectsIn = _Tn3270sStatsConnectsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 5),
    _Tn3270sStatsConnectsIn_Type()
)
tn3270sStatsConnectsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsConnectsIn.setStatus("current")
_Tn3270sStatsDisconnects_Type = Counter32
_Tn3270sStatsDisconnects_Object = MibTableColumn
tn3270sStatsDisconnects = _Tn3270sStatsDisconnects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 6),
    _Tn3270sStatsDisconnects_Type()
)
tn3270sStatsDisconnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsDisconnects.setStatus("current")
_Tn3270sStatsTN3270ConnectsFailed_Type = Counter32
_Tn3270sStatsTN3270ConnectsFailed_Object = MibTableColumn
tn3270sStatsTN3270ConnectsFailed = _Tn3270sStatsTN3270ConnectsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 7),
    _Tn3270sStatsTN3270ConnectsFailed_Type()
)
tn3270sStatsTN3270ConnectsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsTN3270ConnectsFailed.setStatus("current")
_Tn3270sStatsInboundChains_Type = Counter32
_Tn3270sStatsInboundChains_Object = MibTableColumn
tn3270sStatsInboundChains = _Tn3270sStatsInboundChains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 8),
    _Tn3270sStatsInboundChains_Type()
)
tn3270sStatsInboundChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsInboundChains.setStatus("current")
_Tn3270sStatsOutboundChains_Type = Counter32
_Tn3270sStatsOutboundChains_Object = MibTableColumn
tn3270sStatsOutboundChains = _Tn3270sStatsOutboundChains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 9),
    _Tn3270sStatsOutboundChains_Type()
)
tn3270sStatsOutboundChains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsOutboundChains.setStatus("current")
_Tn3270sStatsSampledHostResponses_Type = Counter32
_Tn3270sStatsSampledHostResponses_Object = MibTableColumn
tn3270sStatsSampledHostResponses = _Tn3270sStatsSampledHostResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 10),
    _Tn3270sStatsSampledHostResponses_Type()
)
tn3270sStatsSampledHostResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsSampledHostResponses.setStatus("current")
_Tn3270sStatsNetSampledHostResponseTime_Type = Tn3270sUnsigned32
_Tn3270sStatsNetSampledHostResponseTime_Object = MibTableColumn
tn3270sStatsNetSampledHostResponseTime = _Tn3270sStatsNetSampledHostResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 11),
    _Tn3270sStatsNetSampledHostResponseTime_Type()
)
tn3270sStatsNetSampledHostResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsNetSampledHostResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sStatsNetSampledHostResponseTime.setUnits("10milliseconds")
_Tn3270sStatsSampledClientResponses_Type = Counter32
_Tn3270sStatsSampledClientResponses_Object = MibTableColumn
tn3270sStatsSampledClientResponses = _Tn3270sStatsSampledClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 12),
    _Tn3270sStatsSampledClientResponses_Type()
)
tn3270sStatsSampledClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsSampledClientResponses.setStatus("current")
_Tn3270sStatsNetSampledClientResponseTime_Type = Tn3270sUnsigned32
_Tn3270sStatsNetSampledClientResponseTime_Object = MibTableColumn
tn3270sStatsNetSampledClientResponseTime = _Tn3270sStatsNetSampledClientResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 2, 1, 1, 13),
    _Tn3270sStatsNetSampledClientResponseTime_Type()
)
tn3270sStatsNetSampledClientResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sStatsNetSampledClientResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sStatsNetSampledClientResponseTime.setUnits("10milliseconds")
_Tn3270sPu_ObjectIdentity = ObjectIdentity
tn3270sPu = _Tn3270sPu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3)
)
_Tn3270sPuTable_Object = MibTable
tn3270sPuTable = _Tn3270sPuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tn3270sPuTable.setStatus("current")
_Tn3270sPuEntry_Object = MibTableRow
tn3270sPuEntry = _Tn3270sPuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1)
)
tn3270sPuEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sPuIndex"),
)
if mibBuilder.loadTexts:
    tn3270sPuEntry.setStatus("current")
_Tn3270sPuIndex_Type = Tn3270sPUIndex
_Tn3270sPuIndex_Object = MibTableColumn
tn3270sPuIndex = _Tn3270sPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 1),
    _Tn3270sPuIndex_Type()
)
tn3270sPuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sPuIndex.setStatus("current")
_Tn3270sPuIpAddr_Type = IpAddress
_Tn3270sPuIpAddr_Object = MibTableColumn
tn3270sPuIpAddr = _Tn3270sPuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 2),
    _Tn3270sPuIpAddr_Type()
)
tn3270sPuIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIpAddr.setStatus("current")
_Tn3270sPuTcpPort_Type = Tn3270sTCPPort
_Tn3270sPuTcpPort_Object = MibTableColumn
tn3270sPuTcpPort = _Tn3270sPuTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 3),
    _Tn3270sPuTcpPort_Type()
)
tn3270sPuTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuTcpPort.setStatus("current")


class _Tn3270sPuIdleTimeout_Type(Integer32):
    """Custom type tn3270sPuIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270sPuIdleTimeout_Type.__name__ = "Integer32"
_Tn3270sPuIdleTimeout_Object = MibTableColumn
tn3270sPuIdleTimeout = _Tn3270sPuIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 4),
    _Tn3270sPuIdleTimeout_Type()
)
tn3270sPuIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIdleTimeout.setStatus("current")


class _Tn3270sPuKeepAlive_Type(Integer32):
    """Custom type tn3270sPuKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270sPuKeepAlive_Type.__name__ = "Integer32"
_Tn3270sPuKeepAlive_Object = MibTableColumn
tn3270sPuKeepAlive = _Tn3270sPuKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 5),
    _Tn3270sPuKeepAlive_Type()
)
tn3270sPuKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuKeepAlive.setStatus("current")


class _Tn3270sPuUnbindAction_Type(Integer32):
    """Custom type tn3270sPuUnbindAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("inherit", 3),
          ("keep", 1))
    )


_Tn3270sPuUnbindAction_Type.__name__ = "Integer32"
_Tn3270sPuUnbindAction_Object = MibTableColumn
tn3270sPuUnbindAction = _Tn3270sPuUnbindAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 6),
    _Tn3270sPuUnbindAction_Type()
)
tn3270sPuUnbindAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuUnbindAction.setStatus("current")


class _Tn3270sPuGenericPool_Type(Integer32):
    """Custom type tn3270sPuGenericPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("inherit", 3),
          ("permit", 1))
    )


_Tn3270sPuGenericPool_Type.__name__ = "Integer32"
_Tn3270sPuGenericPool_Object = MibTableColumn
tn3270sPuGenericPool = _Tn3270sPuGenericPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 7),
    _Tn3270sPuGenericPool_Type()
)
tn3270sPuGenericPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuGenericPool.setStatus("current")


class _Tn3270sPuState_Type(Integer32):
    """Custom type tn3270sPuState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("actBusy", 8),
          ("active", 7),
          ("inactive", 3),
          ("pActpu", 6),
          ("reset", 2),
          ("shut", 1),
          ("test", 4),
          ("xid", 5))
    )


_Tn3270sPuState_Type.__name__ = "Integer32"
_Tn3270sPuState_Object = MibTableColumn
tn3270sPuState = _Tn3270sPuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 8),
    _Tn3270sPuState_Type()
)
tn3270sPuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuState.setStatus("current")


class _Tn3270sPuType_Type(Integer32):
    """Custom type tn3270sPuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("dlur", 1))
    )


_Tn3270sPuType_Type.__name__ = "Integer32"
_Tn3270sPuType_Object = MibTableColumn
tn3270sPuType = _Tn3270sPuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 9),
    _Tn3270sPuType_Type()
)
tn3270sPuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuType.setStatus("current")


class _Tn3270sPuLuSeed_Type(DisplayString):
    """Custom type tn3270sPuLuSeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_Tn3270sPuLuSeed_Type.__name__ = "DisplayString"
_Tn3270sPuLuSeed_Object = MibTableColumn
tn3270sPuLuSeed = _Tn3270sPuLuSeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 10),
    _Tn3270sPuLuSeed_Type()
)
tn3270sPuLuSeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuLuSeed.setStatus("current")


class _Tn3270sLocalSapAddress_Type(Integer32):
    """Custom type tn3270sLocalSapAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Tn3270sLocalSapAddress_Type.__name__ = "Integer32"
_Tn3270sLocalSapAddress_Object = MibTableColumn
tn3270sLocalSapAddress = _Tn3270sLocalSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 11),
    _Tn3270sLocalSapAddress_Type()
)
tn3270sLocalSapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLocalSapAddress.setStatus("current")


class _Tn3270sRemoteSapAddress_Type(Integer32):
    """Custom type tn3270sRemoteSapAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Tn3270sRemoteSapAddress_Type.__name__ = "Integer32"
_Tn3270sRemoteSapAddress_Object = MibTableColumn
tn3270sRemoteSapAddress = _Tn3270sRemoteSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 12),
    _Tn3270sRemoteSapAddress_Type()
)
tn3270sRemoteSapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sRemoteSapAddress.setStatus("current")
_Tn3270sRemoteMacAddress_Type = MacAddress
_Tn3270sRemoteMacAddress_Object = MibTableColumn
tn3270sRemoteMacAddress = _Tn3270sRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 13),
    _Tn3270sRemoteMacAddress_Type()
)
tn3270sRemoteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sRemoteMacAddress.setStatus("current")


class _Tn3270sPuIpPrecedenceScreen_Type(Integer32):
    """Custom type tn3270sPuIpPrecedenceScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tn3270sPuIpPrecedenceScreen_Type.__name__ = "Integer32"
_Tn3270sPuIpPrecedenceScreen_Object = MibTableColumn
tn3270sPuIpPrecedenceScreen = _Tn3270sPuIpPrecedenceScreen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 14),
    _Tn3270sPuIpPrecedenceScreen_Type()
)
tn3270sPuIpPrecedenceScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIpPrecedenceScreen.setStatus("current")


class _Tn3270sPuIpPrecedencePrinter_Type(Integer32):
    """Custom type tn3270sPuIpPrecedencePrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tn3270sPuIpPrecedencePrinter_Type.__name__ = "Integer32"
_Tn3270sPuIpPrecedencePrinter_Object = MibTableColumn
tn3270sPuIpPrecedencePrinter = _Tn3270sPuIpPrecedencePrinter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 15),
    _Tn3270sPuIpPrecedencePrinter_Type()
)
tn3270sPuIpPrecedencePrinter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIpPrecedencePrinter.setStatus("current")


class _Tn3270sPuIpTosScreen_Type(Integer32):
    """Custom type tn3270sPuIpTosScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Tn3270sPuIpTosScreen_Type.__name__ = "Integer32"
_Tn3270sPuIpTosScreen_Object = MibTableColumn
tn3270sPuIpTosScreen = _Tn3270sPuIpTosScreen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 16),
    _Tn3270sPuIpTosScreen_Type()
)
tn3270sPuIpTosScreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIpTosScreen.setStatus("current")


class _Tn3270sPuIpTosPrinter_Type(Integer32):
    """Custom type tn3270sPuIpTosPrinter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Tn3270sPuIpTosPrinter_Type.__name__ = "Integer32"
_Tn3270sPuIpTosPrinter_Object = MibTableColumn
tn3270sPuIpTosPrinter = _Tn3270sPuIpTosPrinter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 3, 1, 1, 17),
    _Tn3270sPuIpTosPrinter_Type()
)
tn3270sPuIpTosPrinter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuIpTosPrinter.setStatus("current")
_Tn3270sIp_ObjectIdentity = ObjectIdentity
tn3270sIp = _Tn3270sIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4)
)
_Tn3270sIpTable_Object = MibTable
tn3270sIpTable = _Tn3270sIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tn3270sIpTable.setStatus("current")
_Tn3270sIpEntry_Object = MibTableRow
tn3270sIpEntry = _Tn3270sIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1, 1)
)
tn3270sIpEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIpClientAddr"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIpClientTcpPort"),
)
if mibBuilder.loadTexts:
    tn3270sIpEntry.setStatus("current")
_Tn3270sIpClientAddr_Type = IpAddress
_Tn3270sIpClientAddr_Object = MibTableColumn
tn3270sIpClientAddr = _Tn3270sIpClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1, 1, 1),
    _Tn3270sIpClientAddr_Type()
)
tn3270sIpClientAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sIpClientAddr.setStatus("current")
_Tn3270sIpClientTcpPort_Type = Tn3270sTCPPort
_Tn3270sIpClientTcpPort_Object = MibTableColumn
tn3270sIpClientTcpPort = _Tn3270sIpClientTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1, 1, 2),
    _Tn3270sIpClientTcpPort_Type()
)
tn3270sIpClientTcpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sIpClientTcpPort.setStatus("current")
_Tn3270sIpPuIndex_Type = Tn3270sPUIndex
_Tn3270sIpPuIndex_Object = MibTableColumn
tn3270sIpPuIndex = _Tn3270sIpPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1, 1, 3),
    _Tn3270sIpPuIndex_Type()
)
tn3270sIpPuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpPuIndex.setStatus("current")
_Tn3270sIpLuIndex_Type = Tn3270sLUIndex
_Tn3270sIpLuIndex_Object = MibTableColumn
tn3270sIpLuIndex = _Tn3270sIpLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 4, 1, 1, 4),
    _Tn3270sIpLuIndex_Type()
)
tn3270sIpLuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpLuIndex.setStatus("current")
_Tn3270sLu_ObjectIdentity = ObjectIdentity
tn3270sLu = _Tn3270sLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5)
)
_Tn3270sLuTable_Object = MibTable
tn3270sLuTable = _Tn3270sLuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tn3270sLuTable.setStatus("current")
_Tn3270sLuEntry_Object = MibTableRow
tn3270sLuEntry = _Tn3270sLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1)
)
tn3270sLuEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sLuPuIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sLuIndex"),
)
if mibBuilder.loadTexts:
    tn3270sLuEntry.setStatus("current")
_Tn3270sLuPuIndex_Type = Tn3270sPUIndex
_Tn3270sLuPuIndex_Object = MibTableColumn
tn3270sLuPuIndex = _Tn3270sLuPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 1),
    _Tn3270sLuPuIndex_Type()
)
tn3270sLuPuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sLuPuIndex.setStatus("current")
_Tn3270sLuIndex_Type = Tn3270sLUIndex
_Tn3270sLuIndex_Object = MibTableColumn
tn3270sLuIndex = _Tn3270sLuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 2),
    _Tn3270sLuIndex_Type()
)
tn3270sLuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270sLuIndex.setStatus("current")
_Tn3270sLuClientAddr_Type = IpAddress
_Tn3270sLuClientAddr_Object = MibTableColumn
tn3270sLuClientAddr = _Tn3270sLuClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 3),
    _Tn3270sLuClientAddr_Type()
)
tn3270sLuClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuClientAddr.setStatus("current")
_Tn3270sLuClientTcpPort_Type = Tn3270sTCPPort
_Tn3270sLuClientTcpPort_Object = MibTableColumn
tn3270sLuClientTcpPort = _Tn3270sLuClientTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 4),
    _Tn3270sLuClientTcpPort_Type()
)
tn3270sLuClientTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuClientTcpPort.setStatus("current")


class _Tn3270sLuTelnetType_Type(Integer32):
    """Custom type tn3270sLuTelnetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("neverConnect", 3),
          ("tn3270", 1),
          ("tn3270e", 2))
    )


_Tn3270sLuTelnetType_Type.__name__ = "Integer32"
_Tn3270sLuTelnetType_Object = MibTableColumn
tn3270sLuTelnetType = _Tn3270sLuTelnetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 5),
    _Tn3270sLuTelnetType_Type()
)
tn3270sLuTelnetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuTelnetType.setStatus("current")


class _Tn3270sLuTermModel_Type(DisplayString):
    """Custom type tn3270sLuTermModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_Tn3270sLuTermModel_Type.__name__ = "DisplayString"
_Tn3270sLuTermModel_Object = MibTableColumn
tn3270sLuTermModel = _Tn3270sLuTermModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 6),
    _Tn3270sLuTermModel_Type()
)
tn3270sLuTermModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuTermModel.setStatus("current")


class _Tn3270sLuState_Type(Integer32):
    """Custom type tn3270sLuState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("actSession", 4),
          ("active", 2),
          ("inactive", 1),
          ("pActlu", 5),
          ("pBind", 10),
          ("pNotifyAv", 6),
          ("pNotifyUa", 7),
          ("pPsid", 9),
          ("pReset", 8),
          ("pSdt", 3),
          ("pUnbind", 11),
          ("sdtWt", 13),
          ("unbindWt", 12))
    )


_Tn3270sLuState_Type.__name__ = "Integer32"
_Tn3270sLuState_Object = MibTableColumn
tn3270sLuState = _Tn3270sLuState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 7),
    _Tn3270sLuState_Type()
)
tn3270sLuState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuState.setStatus("current")


class _Tn3270sLuCurInbPacing_Type(Integer32):
    """Custom type tn3270sLuCurInbPacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Tn3270sLuCurInbPacing_Type.__name__ = "Integer32"
_Tn3270sLuCurInbPacing_Object = MibTableColumn
tn3270sLuCurInbPacing = _Tn3270sLuCurInbPacing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 8),
    _Tn3270sLuCurInbPacing_Type()
)
tn3270sLuCurInbPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuCurInbPacing.setStatus("current")


class _Tn3270sLuCurInbQsize_Type(Integer32):
    """Custom type tn3270sLuCurInbQsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Tn3270sLuCurInbQsize_Type.__name__ = "Integer32"
_Tn3270sLuCurInbQsize_Object = MibTableColumn
tn3270sLuCurInbQsize = _Tn3270sLuCurInbQsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 9),
    _Tn3270sLuCurInbQsize_Type()
)
tn3270sLuCurInbQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuCurInbQsize.setStatus("current")


class _Tn3270sLuCurOutQsize_Type(Integer32):
    """Custom type tn3270sLuCurOutQsize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Tn3270sLuCurOutQsize_Type.__name__ = "Integer32"
_Tn3270sLuCurOutQsize_Object = MibTableColumn
tn3270sLuCurOutQsize = _Tn3270sLuCurOutQsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 10),
    _Tn3270sLuCurOutQsize_Type()
)
tn3270sLuCurOutQsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuCurOutQsize.setStatus("current")


class _Tn3270sLuIdleTime_Type(Integer32):
    """Custom type tn3270sLuIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270sLuIdleTime_Type.__name__ = "Integer32"
_Tn3270sLuIdleTime_Object = MibTableColumn
tn3270sLuIdleTime = _Tn3270sLuIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 11),
    _Tn3270sLuIdleTime_Type()
)
tn3270sLuIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    tn3270sLuIdleTime.setUnits("seconds")


class _Tn3270sLuType_Type(Integer32):
    """Custom type tn3270sLuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_Tn3270sLuType_Type.__name__ = "Integer32"
_Tn3270sLuType_Object = MibTableColumn
tn3270sLuType = _Tn3270sLuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 12),
    _Tn3270sLuType_Type()
)
tn3270sLuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuType.setStatus("current")


class _Tn3270sLuAppnLinkIndex_Type(DisplayString):
    """Custom type tn3270sLuAppnLinkIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270sLuAppnLinkIndex_Type.__name__ = "DisplayString"
_Tn3270sLuAppnLinkIndex_Object = MibTableColumn
tn3270sLuAppnLinkIndex = _Tn3270sLuAppnLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 13),
    _Tn3270sLuAppnLinkIndex_Type()
)
tn3270sLuAppnLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuAppnLinkIndex.setStatus("current")


class _Tn3270sLuLfsid_Type(Integer32):
    """Custom type tn3270sLuLfsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270sLuLfsid_Type.__name__ = "Integer32"
_Tn3270sLuLfsid_Object = MibTableColumn
tn3270sLuLfsid = _Tn3270sLuLfsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 14),
    _Tn3270sLuLfsid_Type()
)
tn3270sLuLfsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuLfsid.setStatus("current")
_Tn3270sLuLastEvent_Type = TimeStamp
_Tn3270sLuLastEvent_Object = MibTableColumn
tn3270sLuLastEvent = _Tn3270sLuLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 15),
    _Tn3270sLuLastEvent_Type()
)
tn3270sLuLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuLastEvent.setStatus("obsolete")


class _Tn3270sLuEvents_Type(OctetString):
    """Custom type tn3270sLuEvents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tn3270sLuEvents_Type.__name__ = "OctetString"
_Tn3270sLuEvents_Object = MibTableColumn
tn3270sLuEvents = _Tn3270sLuEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 16),
    _Tn3270sLuEvents_Type()
)
tn3270sLuEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuEvents.setStatus("current")
_Tn3270sLuNail_Type = TruthValue
_Tn3270sLuNail_Object = MibTableColumn
tn3270sLuNail = _Tn3270sLuNail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 5, 1, 1, 17),
    _Tn3270sLuNail_Type()
)
tn3270sLuNail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sLuNail.setStatus("current")
_Tn3270sPuNail_ObjectIdentity = ObjectIdentity
tn3270sPuNail = _Tn3270sPuNail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6)
)
_Tn3270sPuNailTable_Object = MibTable
tn3270sPuNailTable = _Tn3270sPuNailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tn3270sPuNailTable.setStatus("current")
_Tn3270sPuNailEntry_Object = MibTableRow
tn3270sPuNailEntry = _Tn3270sPuNailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1)
)
tn3270sPuNailEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sPuIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sPuNailClientIpAddr"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sPuNailLuFirst"),
)
if mibBuilder.loadTexts:
    tn3270sPuNailEntry.setStatus("current")
_Tn3270sPuNailClientIpAddr_Type = IpAddress
_Tn3270sPuNailClientIpAddr_Object = MibTableColumn
tn3270sPuNailClientIpAddr = _Tn3270sPuNailClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1, 1),
    _Tn3270sPuNailClientIpAddr_Type()
)
tn3270sPuNailClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuNailClientIpAddr.setStatus("current")
_Tn3270sPuNailClientIpMask_Type = IpAddress
_Tn3270sPuNailClientIpMask_Object = MibTableColumn
tn3270sPuNailClientIpMask = _Tn3270sPuNailClientIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1, 2),
    _Tn3270sPuNailClientIpMask_Type()
)
tn3270sPuNailClientIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuNailClientIpMask.setStatus("current")


class _Tn3270sPuNailType_Type(Integer32):
    """Custom type tn3270sPuNailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("printer", 2),
          ("screen", 1))
    )


_Tn3270sPuNailType_Type.__name__ = "Integer32"
_Tn3270sPuNailType_Object = MibTableColumn
tn3270sPuNailType = _Tn3270sPuNailType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1, 3),
    _Tn3270sPuNailType_Type()
)
tn3270sPuNailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuNailType.setStatus("current")


class _Tn3270sPuNailLuFirst_Type(Integer32):
    """Custom type tn3270sPuNailLuFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tn3270sPuNailLuFirst_Type.__name__ = "Integer32"
_Tn3270sPuNailLuFirst_Object = MibTableColumn
tn3270sPuNailLuFirst = _Tn3270sPuNailLuFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1, 4),
    _Tn3270sPuNailLuFirst_Type()
)
tn3270sPuNailLuFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuNailLuFirst.setStatus("current")


class _Tn3270sPuNailLuLast_Type(Integer32):
    """Custom type tn3270sPuNailLuLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tn3270sPuNailLuLast_Type.__name__ = "Integer32"
_Tn3270sPuNailLuLast_Object = MibTableColumn
tn3270sPuNailLuLast = _Tn3270sPuNailLuLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 6, 1, 1, 5),
    _Tn3270sPuNailLuLast_Type()
)
tn3270sPuNailLuLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sPuNailLuLast.setStatus("current")
_Tn3270sIpNail_ObjectIdentity = ObjectIdentity
tn3270sIpNail = _Tn3270sIpNail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7)
)
_Tn3270sIpNailTable_Object = MibTable
tn3270sIpNailTable = _Tn3270sIpNailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tn3270sIpNailTable.setStatus("current")
_Tn3270sIpNailEntry_Object = MibTableRow
tn3270sIpNailEntry = _Tn3270sIpNailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1)
)
tn3270sIpNailEntry.setIndexNames(
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIpNailClientIpAddr"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sPuIndex"),
    (0, "CISCO-TN3270SERVER-MIB", "tn3270sIpNailLuFirst"),
)
if mibBuilder.loadTexts:
    tn3270sIpNailEntry.setStatus("current")
_Tn3270sIpNailClientIpAddr_Type = IpAddress
_Tn3270sIpNailClientIpAddr_Object = MibTableColumn
tn3270sIpNailClientIpAddr = _Tn3270sIpNailClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1, 1),
    _Tn3270sIpNailClientIpAddr_Type()
)
tn3270sIpNailClientIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpNailClientIpAddr.setStatus("current")
_Tn3270sIpNailClientIpMask_Type = IpAddress
_Tn3270sIpNailClientIpMask_Object = MibTableColumn
tn3270sIpNailClientIpMask = _Tn3270sIpNailClientIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1, 2),
    _Tn3270sIpNailClientIpMask_Type()
)
tn3270sIpNailClientIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpNailClientIpMask.setStatus("current")


class _Tn3270sIpNailType_Type(Integer32):
    """Custom type tn3270sIpNailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("printer", 2),
          ("screen", 1))
    )


_Tn3270sIpNailType_Type.__name__ = "Integer32"
_Tn3270sIpNailType_Object = MibTableColumn
tn3270sIpNailType = _Tn3270sIpNailType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1, 3),
    _Tn3270sIpNailType_Type()
)
tn3270sIpNailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpNailType.setStatus("current")


class _Tn3270sIpNailLuFirst_Type(Integer32):
    """Custom type tn3270sIpNailLuFirst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tn3270sIpNailLuFirst_Type.__name__ = "Integer32"
_Tn3270sIpNailLuFirst_Object = MibTableColumn
tn3270sIpNailLuFirst = _Tn3270sIpNailLuFirst_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1, 4),
    _Tn3270sIpNailLuFirst_Type()
)
tn3270sIpNailLuFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpNailLuFirst.setStatus("current")


class _Tn3270sIpNailLuLast_Type(Integer32):
    """Custom type tn3270sIpNailLuLast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Tn3270sIpNailLuLast_Type.__name__ = "Integer32"
_Tn3270sIpNailLuLast_Object = MibTableColumn
tn3270sIpNailLuLast = _Tn3270sIpNailLuLast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 1, 7, 1, 1, 5),
    _Tn3270sIpNailLuLast_Type()
)
tn3270sIpNailLuLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270sIpNailLuLast.setStatus("current")
_CiscoTn3270ServerMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoTn3270ServerMIBNotificationPrefix = _CiscoTn3270ServerMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 2)
)
_CiscoTn3270ServerMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTn3270ServerMIBConformance = _CiscoTn3270ServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3)
)
_CiscoTn3270ServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTn3270ServerMIBCompliances = _CiscoTn3270ServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 1)
)
_CiscoTn3270ServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTn3270ServerMIBGroups = _CiscoTn3270ServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 2)
)

# Managed Objects groups

ciscoTn3270ServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 2, 1)
)
ciscoTn3270ServerMIBGroup.setObjects(
      *(("CISCO-TN3270SERVER-MIB", "tn3270sCpuCard"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sMaxLus"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLusInUse"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStartupTime"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sGlobalTcpPort"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sGlobalIdleTimeout"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sGlobalKeepAlive"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sGlobalUnbindAction"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sGlobalGenericPool"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sTimingMarkSupported"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sRunningTime"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsMaxSess"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsSpareSess"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsConnectsIn"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsDisconnects"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsTN3270ConnectsFailed"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsInboundChains"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsOutboundChains"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsSampledHostResponses"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsNetSampledHostResponseTime"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsSampledClientResponses"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sStatsNetSampledClientResponseTime"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuIpAddr"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuTcpPort"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuIdleTimeout"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuKeepAlive"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuUnbindAction"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuGenericPool"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuState"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuType"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuLuSeed"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLocalSapAddress"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sRemoteSapAddress"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sRemoteMacAddress"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpPuIndex"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpLuIndex"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuClientAddr"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuClientTcpPort"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuTelnetType"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuTermModel"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuState"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuCurInbPacing"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuCurInbQsize"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuCurOutQsize"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuIdleTime"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuType"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuAppnLinkIndex"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuLfsid"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuEvents"))
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBGroup.setStatus("current")

ciscoTn3270ServerMIBGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 2, 2)
)
ciscoTn3270ServerMIBGroupObsolete.setObjects(
    ("CISCO-TN3270SERVER-MIB", "tn3270sLuLastEvent")
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBGroupObsolete.setStatus("obsolete")

ciscoTn3270ServerMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 2, 3)
)
ciscoTn3270ServerMIBGroupRev1.setObjects(
      *(("CISCO-TN3270SERVER-MIB", "tn3270sPuIpPrecedenceScreen"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuIpPrecedencePrinter"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuIpTosScreen"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuIpTosPrinter"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sLuNail"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuNailClientIpAddr"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuNailClientIpMask"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuNailType"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuNailLuFirst"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sPuNailLuLast"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpNailClientIpAddr"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpNailClientIpMask"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpNailType"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpNailLuFirst"),
        ("CISCO-TN3270SERVER-MIB", "tn3270sIpNailLuLast"))
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTn3270ServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBCompliance.setStatus(
        "current"
    )

ciscoTn3270ServerMIBComplianceObsolete = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBComplianceObsolete.setStatus(
        "obsolete"
    )

ciscoTn3270ServerMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 54, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTn3270ServerMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TN3270SERVER-MIB",
    **{"Tn3270sUnsigned32": Tn3270sUnsigned32,
       "Tn3270sTCPPort": Tn3270sTCPPort,
       "Tn3270sPUIndex": Tn3270sPUIndex,
       "Tn3270sLUIndex": Tn3270sLUIndex,
       "Tn3270sCpuCard": Tn3270sCpuCard,
       "ciscoTn3270ServerMIB": ciscoTn3270ServerMIB,
       "tn3270sObjects": tn3270sObjects,
       "tn3270sGlobal": tn3270sGlobal,
       "tn3270sGlobalTable": tn3270sGlobalTable,
       "tn3270sGlobalEntry": tn3270sGlobalEntry,
       "tn3270sIndex": tn3270sIndex,
       "tn3270sCpuCard": tn3270sCpuCard,
       "tn3270sMaxLus": tn3270sMaxLus,
       "tn3270sLusInUse": tn3270sLusInUse,
       "tn3270sStartupTime": tn3270sStartupTime,
       "tn3270sGlobalTcpPort": tn3270sGlobalTcpPort,
       "tn3270sGlobalIdleTimeout": tn3270sGlobalIdleTimeout,
       "tn3270sGlobalKeepAlive": tn3270sGlobalKeepAlive,
       "tn3270sGlobalUnbindAction": tn3270sGlobalUnbindAction,
       "tn3270sGlobalGenericPool": tn3270sGlobalGenericPool,
       "tn3270sTimingMarkSupported": tn3270sTimingMarkSupported,
       "tn3270sRunningTime": tn3270sRunningTime,
       "tn3270sStats": tn3270sStats,
       "tn3270sStatsTable": tn3270sStatsTable,
       "tn3270sStatsEntry": tn3270sStatsEntry,
       "tn3270sStatsServerAddr": tn3270sStatsServerAddr,
       "tn3270sStatsServerTcpPort": tn3270sStatsServerTcpPort,
       "tn3270sStatsMaxSess": tn3270sStatsMaxSess,
       "tn3270sStatsSpareSess": tn3270sStatsSpareSess,
       "tn3270sStatsConnectsIn": tn3270sStatsConnectsIn,
       "tn3270sStatsDisconnects": tn3270sStatsDisconnects,
       "tn3270sStatsTN3270ConnectsFailed": tn3270sStatsTN3270ConnectsFailed,
       "tn3270sStatsInboundChains": tn3270sStatsInboundChains,
       "tn3270sStatsOutboundChains": tn3270sStatsOutboundChains,
       "tn3270sStatsSampledHostResponses": tn3270sStatsSampledHostResponses,
       "tn3270sStatsNetSampledHostResponseTime": tn3270sStatsNetSampledHostResponseTime,
       "tn3270sStatsSampledClientResponses": tn3270sStatsSampledClientResponses,
       "tn3270sStatsNetSampledClientResponseTime": tn3270sStatsNetSampledClientResponseTime,
       "tn3270sPu": tn3270sPu,
       "tn3270sPuTable": tn3270sPuTable,
       "tn3270sPuEntry": tn3270sPuEntry,
       "tn3270sPuIndex": tn3270sPuIndex,
       "tn3270sPuIpAddr": tn3270sPuIpAddr,
       "tn3270sPuTcpPort": tn3270sPuTcpPort,
       "tn3270sPuIdleTimeout": tn3270sPuIdleTimeout,
       "tn3270sPuKeepAlive": tn3270sPuKeepAlive,
       "tn3270sPuUnbindAction": tn3270sPuUnbindAction,
       "tn3270sPuGenericPool": tn3270sPuGenericPool,
       "tn3270sPuState": tn3270sPuState,
       "tn3270sPuType": tn3270sPuType,
       "tn3270sPuLuSeed": tn3270sPuLuSeed,
       "tn3270sLocalSapAddress": tn3270sLocalSapAddress,
       "tn3270sRemoteSapAddress": tn3270sRemoteSapAddress,
       "tn3270sRemoteMacAddress": tn3270sRemoteMacAddress,
       "tn3270sPuIpPrecedenceScreen": tn3270sPuIpPrecedenceScreen,
       "tn3270sPuIpPrecedencePrinter": tn3270sPuIpPrecedencePrinter,
       "tn3270sPuIpTosScreen": tn3270sPuIpTosScreen,
       "tn3270sPuIpTosPrinter": tn3270sPuIpTosPrinter,
       "tn3270sIp": tn3270sIp,
       "tn3270sIpTable": tn3270sIpTable,
       "tn3270sIpEntry": tn3270sIpEntry,
       "tn3270sIpClientAddr": tn3270sIpClientAddr,
       "tn3270sIpClientTcpPort": tn3270sIpClientTcpPort,
       "tn3270sIpPuIndex": tn3270sIpPuIndex,
       "tn3270sIpLuIndex": tn3270sIpLuIndex,
       "tn3270sLu": tn3270sLu,
       "tn3270sLuTable": tn3270sLuTable,
       "tn3270sLuEntry": tn3270sLuEntry,
       "tn3270sLuPuIndex": tn3270sLuPuIndex,
       "tn3270sLuIndex": tn3270sLuIndex,
       "tn3270sLuClientAddr": tn3270sLuClientAddr,
       "tn3270sLuClientTcpPort": tn3270sLuClientTcpPort,
       "tn3270sLuTelnetType": tn3270sLuTelnetType,
       "tn3270sLuTermModel": tn3270sLuTermModel,
       "tn3270sLuState": tn3270sLuState,
       "tn3270sLuCurInbPacing": tn3270sLuCurInbPacing,
       "tn3270sLuCurInbQsize": tn3270sLuCurInbQsize,
       "tn3270sLuCurOutQsize": tn3270sLuCurOutQsize,
       "tn3270sLuIdleTime": tn3270sLuIdleTime,
       "tn3270sLuType": tn3270sLuType,
       "tn3270sLuAppnLinkIndex": tn3270sLuAppnLinkIndex,
       "tn3270sLuLfsid": tn3270sLuLfsid,
       "tn3270sLuLastEvent": tn3270sLuLastEvent,
       "tn3270sLuEvents": tn3270sLuEvents,
       "tn3270sLuNail": tn3270sLuNail,
       "tn3270sPuNail": tn3270sPuNail,
       "tn3270sPuNailTable": tn3270sPuNailTable,
       "tn3270sPuNailEntry": tn3270sPuNailEntry,
       "tn3270sPuNailClientIpAddr": tn3270sPuNailClientIpAddr,
       "tn3270sPuNailClientIpMask": tn3270sPuNailClientIpMask,
       "tn3270sPuNailType": tn3270sPuNailType,
       "tn3270sPuNailLuFirst": tn3270sPuNailLuFirst,
       "tn3270sPuNailLuLast": tn3270sPuNailLuLast,
       "tn3270sIpNail": tn3270sIpNail,
       "tn3270sIpNailTable": tn3270sIpNailTable,
       "tn3270sIpNailEntry": tn3270sIpNailEntry,
       "tn3270sIpNailClientIpAddr": tn3270sIpNailClientIpAddr,
       "tn3270sIpNailClientIpMask": tn3270sIpNailClientIpMask,
       "tn3270sIpNailType": tn3270sIpNailType,
       "tn3270sIpNailLuFirst": tn3270sIpNailLuFirst,
       "tn3270sIpNailLuLast": tn3270sIpNailLuLast,
       "ciscoTn3270ServerMIBNotificationPrefix": ciscoTn3270ServerMIBNotificationPrefix,
       "ciscoTn3270ServerMIBConformance": ciscoTn3270ServerMIBConformance,
       "ciscoTn3270ServerMIBCompliances": ciscoTn3270ServerMIBCompliances,
       "ciscoTn3270ServerMIBCompliance": ciscoTn3270ServerMIBCompliance,
       "ciscoTn3270ServerMIBComplianceObsolete": ciscoTn3270ServerMIBComplianceObsolete,
       "ciscoTn3270ServerMIBComplianceRev1": ciscoTn3270ServerMIBComplianceRev1,
       "ciscoTn3270ServerMIBGroups": ciscoTn3270ServerMIBGroups,
       "ciscoTn3270ServerMIBGroup": ciscoTn3270ServerMIBGroup,
       "ciscoTn3270ServerMIBGroupObsolete": ciscoTn3270ServerMIBGroupObsolete,
       "ciscoTn3270ServerMIBGroupRev1": ciscoTn3270ServerMIBGroupRev1}
)
