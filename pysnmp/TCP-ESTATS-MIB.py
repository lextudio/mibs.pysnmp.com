# SNMP MIB module (TCP-ESTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TCP-ESTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:59 2024
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

(ZeroBasedCounter64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "ZeroBasedCounter64")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tcpConnectionEntry,
 tcpListenerEntry) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnectionEntry",
    "tcpListenerEntry")


# MODULE-IDENTITY

tcpEStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 156)
)
tcpEStatsMIB.setRevisions(
        ("2007-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TcpEStatsNegotiated(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("peerDisabled", 3),
          ("selfDisabled", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TcpEStatsNotifications_ObjectIdentity = ObjectIdentity
tcpEStatsNotifications = _TcpEStatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 0)
)
_TcpEStatsMIBObjects_ObjectIdentity = ObjectIdentity
tcpEStatsMIBObjects = _TcpEStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 1)
)
_TcpEStats_ObjectIdentity = ObjectIdentity
tcpEStats = _TcpEStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 1, 1)
)
_TcpEStatsListenerTable_Object = MibTable
tcpEStatsListenerTable = _TcpEStatsListenerTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tcpEStatsListenerTable.setStatus("current")
_TcpEStatsListenerEntry_Object = MibTableRow
tcpEStatsListenerEntry = _TcpEStatsListenerEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tcpEStatsListenerEntry.setStatus("current")
_TcpEStatsListenerStartTime_Type = TimeStamp
_TcpEStatsListenerStartTime_Object = MibTableColumn
tcpEStatsListenerStartTime = _TcpEStatsListenerStartTime_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 1),
    _TcpEStatsListenerStartTime_Type()
)
tcpEStatsListenerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerStartTime.setStatus("current")
_TcpEStatsListenerSynRcvd_Type = ZeroBasedCounter32
_TcpEStatsListenerSynRcvd_Object = MibTableColumn
tcpEStatsListenerSynRcvd = _TcpEStatsListenerSynRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 2),
    _TcpEStatsListenerSynRcvd_Type()
)
tcpEStatsListenerSynRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerSynRcvd.setStatus("current")
_TcpEStatsListenerInitial_Type = ZeroBasedCounter32
_TcpEStatsListenerInitial_Object = MibTableColumn
tcpEStatsListenerInitial = _TcpEStatsListenerInitial_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 3),
    _TcpEStatsListenerInitial_Type()
)
tcpEStatsListenerInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerInitial.setStatus("current")
_TcpEStatsListenerEstablished_Type = ZeroBasedCounter32
_TcpEStatsListenerEstablished_Object = MibTableColumn
tcpEStatsListenerEstablished = _TcpEStatsListenerEstablished_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 4),
    _TcpEStatsListenerEstablished_Type()
)
tcpEStatsListenerEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerEstablished.setStatus("current")
_TcpEStatsListenerAccepted_Type = ZeroBasedCounter32
_TcpEStatsListenerAccepted_Object = MibTableColumn
tcpEStatsListenerAccepted = _TcpEStatsListenerAccepted_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 5),
    _TcpEStatsListenerAccepted_Type()
)
tcpEStatsListenerAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerAccepted.setStatus("current")
_TcpEStatsListenerExceedBacklog_Type = ZeroBasedCounter32
_TcpEStatsListenerExceedBacklog_Object = MibTableColumn
tcpEStatsListenerExceedBacklog = _TcpEStatsListenerExceedBacklog_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 6),
    _TcpEStatsListenerExceedBacklog_Type()
)
tcpEStatsListenerExceedBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerExceedBacklog.setStatus("current")
_TcpEStatsListenerHCSynRcvd_Type = ZeroBasedCounter64
_TcpEStatsListenerHCSynRcvd_Object = MibTableColumn
tcpEStatsListenerHCSynRcvd = _TcpEStatsListenerHCSynRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 7),
    _TcpEStatsListenerHCSynRcvd_Type()
)
tcpEStatsListenerHCSynRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerHCSynRcvd.setStatus("current")
_TcpEStatsListenerHCInitial_Type = ZeroBasedCounter64
_TcpEStatsListenerHCInitial_Object = MibTableColumn
tcpEStatsListenerHCInitial = _TcpEStatsListenerHCInitial_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 8),
    _TcpEStatsListenerHCInitial_Type()
)
tcpEStatsListenerHCInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerHCInitial.setStatus("current")
_TcpEStatsListenerHCEstablished_Type = ZeroBasedCounter64
_TcpEStatsListenerHCEstablished_Object = MibTableColumn
tcpEStatsListenerHCEstablished = _TcpEStatsListenerHCEstablished_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 9),
    _TcpEStatsListenerHCEstablished_Type()
)
tcpEStatsListenerHCEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerHCEstablished.setStatus("current")
_TcpEStatsListenerHCAccepted_Type = ZeroBasedCounter64
_TcpEStatsListenerHCAccepted_Object = MibTableColumn
tcpEStatsListenerHCAccepted = _TcpEStatsListenerHCAccepted_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 10),
    _TcpEStatsListenerHCAccepted_Type()
)
tcpEStatsListenerHCAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerHCAccepted.setStatus("current")
_TcpEStatsListenerHCExceedBacklog_Type = ZeroBasedCounter64
_TcpEStatsListenerHCExceedBacklog_Object = MibTableColumn
tcpEStatsListenerHCExceedBacklog = _TcpEStatsListenerHCExceedBacklog_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 11),
    _TcpEStatsListenerHCExceedBacklog_Type()
)
tcpEStatsListenerHCExceedBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerHCExceedBacklog.setStatus("current")
_TcpEStatsListenerCurConns_Type = Gauge32
_TcpEStatsListenerCurConns_Object = MibTableColumn
tcpEStatsListenerCurConns = _TcpEStatsListenerCurConns_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 12),
    _TcpEStatsListenerCurConns_Type()
)
tcpEStatsListenerCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerCurConns.setStatus("current")
_TcpEStatsListenerMaxBacklog_Type = Unsigned32
_TcpEStatsListenerMaxBacklog_Object = MibTableColumn
tcpEStatsListenerMaxBacklog = _TcpEStatsListenerMaxBacklog_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 13),
    _TcpEStatsListenerMaxBacklog_Type()
)
tcpEStatsListenerMaxBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerMaxBacklog.setStatus("current")
_TcpEStatsListenerCurBacklog_Type = Gauge32
_TcpEStatsListenerCurBacklog_Object = MibTableColumn
tcpEStatsListenerCurBacklog = _TcpEStatsListenerCurBacklog_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 14),
    _TcpEStatsListenerCurBacklog_Type()
)
tcpEStatsListenerCurBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerCurBacklog.setStatus("current")
_TcpEStatsListenerCurEstabBacklog_Type = Gauge32
_TcpEStatsListenerCurEstabBacklog_Object = MibTableColumn
tcpEStatsListenerCurEstabBacklog = _TcpEStatsListenerCurEstabBacklog_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 1, 1, 15),
    _TcpEStatsListenerCurEstabBacklog_Type()
)
tcpEStatsListenerCurEstabBacklog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerCurEstabBacklog.setStatus("current")
_TcpEStatsConnectIdTable_Object = MibTable
tcpEStatsConnectIdTable = _TcpEStatsConnectIdTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tcpEStatsConnectIdTable.setStatus("current")
_TcpEStatsConnectIdEntry_Object = MibTableRow
tcpEStatsConnectIdEntry = _TcpEStatsConnectIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tcpEStatsConnectIdEntry.setStatus("current")


class _TcpEStatsConnectIndex_Type(Unsigned32):
    """Custom type tcpEStatsConnectIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TcpEStatsConnectIndex_Type.__name__ = "Unsigned32"
_TcpEStatsConnectIndex_Object = MibTableColumn
tcpEStatsConnectIndex = _TcpEStatsConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 2, 1, 1),
    _TcpEStatsConnectIndex_Type()
)
tcpEStatsConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsConnectIndex.setStatus("current")
_TcpEStatsPerfTable_Object = MibTable
tcpEStatsPerfTable = _TcpEStatsPerfTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tcpEStatsPerfTable.setStatus("current")
_TcpEStatsPerfEntry_Object = MibTableRow
tcpEStatsPerfEntry = _TcpEStatsPerfEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1)
)
tcpEStatsPerfEntry.setIndexNames(
    (0, "TCP-ESTATS-MIB", "tcpEStatsConnectIndex"),
)
if mibBuilder.loadTexts:
    tcpEStatsPerfEntry.setStatus("current")
_TcpEStatsPerfSegsOut_Type = ZeroBasedCounter32
_TcpEStatsPerfSegsOut_Object = MibTableColumn
tcpEStatsPerfSegsOut = _TcpEStatsPerfSegsOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 1),
    _TcpEStatsPerfSegsOut_Type()
)
tcpEStatsPerfSegsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSegsOut.setStatus("current")
_TcpEStatsPerfDataSegsOut_Type = ZeroBasedCounter32
_TcpEStatsPerfDataSegsOut_Object = MibTableColumn
tcpEStatsPerfDataSegsOut = _TcpEStatsPerfDataSegsOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 2),
    _TcpEStatsPerfDataSegsOut_Type()
)
tcpEStatsPerfDataSegsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataSegsOut.setStatus("current")
_TcpEStatsPerfDataOctetsOut_Type = ZeroBasedCounter32
_TcpEStatsPerfDataOctetsOut_Object = MibTableColumn
tcpEStatsPerfDataOctetsOut = _TcpEStatsPerfDataOctetsOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 3),
    _TcpEStatsPerfDataOctetsOut_Type()
)
tcpEStatsPerfDataOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataOctetsOut.setUnits("octets")
_TcpEStatsPerfHCDataOctetsOut_Type = ZeroBasedCounter64
_TcpEStatsPerfHCDataOctetsOut_Object = MibTableColumn
tcpEStatsPerfHCDataOctetsOut = _TcpEStatsPerfHCDataOctetsOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 4),
    _TcpEStatsPerfHCDataOctetsOut_Type()
)
tcpEStatsPerfHCDataOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfHCDataOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfHCDataOctetsOut.setUnits("octets")
_TcpEStatsPerfSegsRetrans_Type = ZeroBasedCounter32
_TcpEStatsPerfSegsRetrans_Object = MibTableColumn
tcpEStatsPerfSegsRetrans = _TcpEStatsPerfSegsRetrans_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 5),
    _TcpEStatsPerfSegsRetrans_Type()
)
tcpEStatsPerfSegsRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSegsRetrans.setStatus("current")
_TcpEStatsPerfOctetsRetrans_Type = ZeroBasedCounter32
_TcpEStatsPerfOctetsRetrans_Object = MibTableColumn
tcpEStatsPerfOctetsRetrans = _TcpEStatsPerfOctetsRetrans_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 6),
    _TcpEStatsPerfOctetsRetrans_Type()
)
tcpEStatsPerfOctetsRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfOctetsRetrans.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfOctetsRetrans.setUnits("octets")
_TcpEStatsPerfSegsIn_Type = ZeroBasedCounter32
_TcpEStatsPerfSegsIn_Object = MibTableColumn
tcpEStatsPerfSegsIn = _TcpEStatsPerfSegsIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 7),
    _TcpEStatsPerfSegsIn_Type()
)
tcpEStatsPerfSegsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSegsIn.setStatus("current")
_TcpEStatsPerfDataSegsIn_Type = ZeroBasedCounter32
_TcpEStatsPerfDataSegsIn_Object = MibTableColumn
tcpEStatsPerfDataSegsIn = _TcpEStatsPerfDataSegsIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 8),
    _TcpEStatsPerfDataSegsIn_Type()
)
tcpEStatsPerfDataSegsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataSegsIn.setStatus("current")
_TcpEStatsPerfDataOctetsIn_Type = ZeroBasedCounter32
_TcpEStatsPerfDataOctetsIn_Object = MibTableColumn
tcpEStatsPerfDataOctetsIn = _TcpEStatsPerfDataOctetsIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 9),
    _TcpEStatsPerfDataOctetsIn_Type()
)
tcpEStatsPerfDataOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfDataOctetsIn.setUnits("octets")
_TcpEStatsPerfHCDataOctetsIn_Type = ZeroBasedCounter64
_TcpEStatsPerfHCDataOctetsIn_Object = MibTableColumn
tcpEStatsPerfHCDataOctetsIn = _TcpEStatsPerfHCDataOctetsIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 10),
    _TcpEStatsPerfHCDataOctetsIn_Type()
)
tcpEStatsPerfHCDataOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfHCDataOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfHCDataOctetsIn.setUnits("octets")
_TcpEStatsPerfElapsedSecs_Type = ZeroBasedCounter32
_TcpEStatsPerfElapsedSecs_Object = MibTableColumn
tcpEStatsPerfElapsedSecs = _TcpEStatsPerfElapsedSecs_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 11),
    _TcpEStatsPerfElapsedSecs_Type()
)
tcpEStatsPerfElapsedSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfElapsedSecs.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfElapsedSecs.setUnits("seconds")
_TcpEStatsPerfElapsedMicroSecs_Type = ZeroBasedCounter32
_TcpEStatsPerfElapsedMicroSecs_Object = MibTableColumn
tcpEStatsPerfElapsedMicroSecs = _TcpEStatsPerfElapsedMicroSecs_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 12),
    _TcpEStatsPerfElapsedMicroSecs_Type()
)
tcpEStatsPerfElapsedMicroSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfElapsedMicroSecs.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfElapsedMicroSecs.setUnits("microseconds")
_TcpEStatsPerfStartTimeStamp_Type = DateAndTime
_TcpEStatsPerfStartTimeStamp_Object = MibTableColumn
tcpEStatsPerfStartTimeStamp = _TcpEStatsPerfStartTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 13),
    _TcpEStatsPerfStartTimeStamp_Type()
)
tcpEStatsPerfStartTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfStartTimeStamp.setStatus("current")
_TcpEStatsPerfCurMSS_Type = Gauge32
_TcpEStatsPerfCurMSS_Object = MibTableColumn
tcpEStatsPerfCurMSS = _TcpEStatsPerfCurMSS_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 14),
    _TcpEStatsPerfCurMSS_Type()
)
tcpEStatsPerfCurMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurMSS.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurMSS.setUnits("octets")
_TcpEStatsPerfPipeSize_Type = Gauge32
_TcpEStatsPerfPipeSize_Object = MibTableColumn
tcpEStatsPerfPipeSize = _TcpEStatsPerfPipeSize_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 15),
    _TcpEStatsPerfPipeSize_Type()
)
tcpEStatsPerfPipeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfPipeSize.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfPipeSize.setUnits("octets")
_TcpEStatsPerfMaxPipeSize_Type = Gauge32
_TcpEStatsPerfMaxPipeSize_Object = MibTableColumn
tcpEStatsPerfMaxPipeSize = _TcpEStatsPerfMaxPipeSize_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 16),
    _TcpEStatsPerfMaxPipeSize_Type()
)
tcpEStatsPerfMaxPipeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxPipeSize.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxPipeSize.setUnits("octets")
_TcpEStatsPerfSmoothedRTT_Type = Gauge32
_TcpEStatsPerfSmoothedRTT_Object = MibTableColumn
tcpEStatsPerfSmoothedRTT = _TcpEStatsPerfSmoothedRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 17),
    _TcpEStatsPerfSmoothedRTT_Type()
)
tcpEStatsPerfSmoothedRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSmoothedRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfSmoothedRTT.setUnits("milliseconds")
_TcpEStatsPerfCurRTO_Type = Gauge32
_TcpEStatsPerfCurRTO_Object = MibTableColumn
tcpEStatsPerfCurRTO = _TcpEStatsPerfCurRTO_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 18),
    _TcpEStatsPerfCurRTO_Type()
)
tcpEStatsPerfCurRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRTO.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRTO.setUnits("milliseconds")
_TcpEStatsPerfCongSignals_Type = ZeroBasedCounter32
_TcpEStatsPerfCongSignals_Object = MibTableColumn
tcpEStatsPerfCongSignals = _TcpEStatsPerfCongSignals_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 19),
    _TcpEStatsPerfCongSignals_Type()
)
tcpEStatsPerfCongSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCongSignals.setStatus("current")
_TcpEStatsPerfCurCwnd_Type = Gauge32
_TcpEStatsPerfCurCwnd_Object = MibTableColumn
tcpEStatsPerfCurCwnd = _TcpEStatsPerfCurCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 20),
    _TcpEStatsPerfCurCwnd_Type()
)
tcpEStatsPerfCurCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurCwnd.setUnits("octets")
_TcpEStatsPerfCurSsthresh_Type = Gauge32
_TcpEStatsPerfCurSsthresh_Object = MibTableColumn
tcpEStatsPerfCurSsthresh = _TcpEStatsPerfCurSsthresh_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 21),
    _TcpEStatsPerfCurSsthresh_Type()
)
tcpEStatsPerfCurSsthresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurSsthresh.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurSsthresh.setUnits("octets")
_TcpEStatsPerfTimeouts_Type = ZeroBasedCounter32
_TcpEStatsPerfTimeouts_Object = MibTableColumn
tcpEStatsPerfTimeouts = _TcpEStatsPerfTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 22),
    _TcpEStatsPerfTimeouts_Type()
)
tcpEStatsPerfTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfTimeouts.setStatus("current")
_TcpEStatsPerfCurRwinSent_Type = Gauge32
_TcpEStatsPerfCurRwinSent_Object = MibTableColumn
tcpEStatsPerfCurRwinSent = _TcpEStatsPerfCurRwinSent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 23),
    _TcpEStatsPerfCurRwinSent_Type()
)
tcpEStatsPerfCurRwinSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRwinSent.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRwinSent.setUnits("octets")
_TcpEStatsPerfMaxRwinSent_Type = Gauge32
_TcpEStatsPerfMaxRwinSent_Object = MibTableColumn
tcpEStatsPerfMaxRwinSent = _TcpEStatsPerfMaxRwinSent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 24),
    _TcpEStatsPerfMaxRwinSent_Type()
)
tcpEStatsPerfMaxRwinSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxRwinSent.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxRwinSent.setUnits("octets")
_TcpEStatsPerfZeroRwinSent_Type = ZeroBasedCounter32
_TcpEStatsPerfZeroRwinSent_Object = MibTableColumn
tcpEStatsPerfZeroRwinSent = _TcpEStatsPerfZeroRwinSent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 25),
    _TcpEStatsPerfZeroRwinSent_Type()
)
tcpEStatsPerfZeroRwinSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfZeroRwinSent.setStatus("current")
_TcpEStatsPerfCurRwinRcvd_Type = Gauge32
_TcpEStatsPerfCurRwinRcvd_Object = MibTableColumn
tcpEStatsPerfCurRwinRcvd = _TcpEStatsPerfCurRwinRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 26),
    _TcpEStatsPerfCurRwinRcvd_Type()
)
tcpEStatsPerfCurRwinRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRwinRcvd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfCurRwinRcvd.setUnits("octets")
_TcpEStatsPerfMaxRwinRcvd_Type = Gauge32
_TcpEStatsPerfMaxRwinRcvd_Object = MibTableColumn
tcpEStatsPerfMaxRwinRcvd = _TcpEStatsPerfMaxRwinRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 27),
    _TcpEStatsPerfMaxRwinRcvd_Type()
)
tcpEStatsPerfMaxRwinRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxRwinRcvd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfMaxRwinRcvd.setUnits("octets")
_TcpEStatsPerfZeroRwinRcvd_Type = ZeroBasedCounter32
_TcpEStatsPerfZeroRwinRcvd_Object = MibTableColumn
tcpEStatsPerfZeroRwinRcvd = _TcpEStatsPerfZeroRwinRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 28),
    _TcpEStatsPerfZeroRwinRcvd_Type()
)
tcpEStatsPerfZeroRwinRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfZeroRwinRcvd.setStatus("current")
_TcpEStatsPerfSndLimTransRwin_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTransRwin_Object = MibTableColumn
tcpEStatsPerfSndLimTransRwin = _TcpEStatsPerfSndLimTransRwin_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 31),
    _TcpEStatsPerfSndLimTransRwin_Type()
)
tcpEStatsPerfSndLimTransRwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTransRwin.setStatus("current")
_TcpEStatsPerfSndLimTransCwnd_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTransCwnd_Object = MibTableColumn
tcpEStatsPerfSndLimTransCwnd = _TcpEStatsPerfSndLimTransCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 32),
    _TcpEStatsPerfSndLimTransCwnd_Type()
)
tcpEStatsPerfSndLimTransCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTransCwnd.setStatus("current")
_TcpEStatsPerfSndLimTransSnd_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTransSnd_Object = MibTableColumn
tcpEStatsPerfSndLimTransSnd = _TcpEStatsPerfSndLimTransSnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 33),
    _TcpEStatsPerfSndLimTransSnd_Type()
)
tcpEStatsPerfSndLimTransSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTransSnd.setStatus("current")
_TcpEStatsPerfSndLimTimeRwin_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTimeRwin_Object = MibTableColumn
tcpEStatsPerfSndLimTimeRwin = _TcpEStatsPerfSndLimTimeRwin_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 34),
    _TcpEStatsPerfSndLimTimeRwin_Type()
)
tcpEStatsPerfSndLimTimeRwin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeRwin.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeRwin.setUnits("milliseconds")
_TcpEStatsPerfSndLimTimeCwnd_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTimeCwnd_Object = MibTableColumn
tcpEStatsPerfSndLimTimeCwnd = _TcpEStatsPerfSndLimTimeCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 35),
    _TcpEStatsPerfSndLimTimeCwnd_Type()
)
tcpEStatsPerfSndLimTimeCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeCwnd.setUnits("milliseconds")
_TcpEStatsPerfSndLimTimeSnd_Type = ZeroBasedCounter32
_TcpEStatsPerfSndLimTimeSnd_Object = MibTableColumn
tcpEStatsPerfSndLimTimeSnd = _TcpEStatsPerfSndLimTimeSnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 3, 1, 36),
    _TcpEStatsPerfSndLimTimeSnd_Type()
)
tcpEStatsPerfSndLimTimeSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeSnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPerfSndLimTimeSnd.setUnits("milliseconds")
_TcpEStatsPathTable_Object = MibTable
tcpEStatsPathTable = _TcpEStatsPathTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tcpEStatsPathTable.setStatus("current")
_TcpEStatsPathEntry_Object = MibTableRow
tcpEStatsPathEntry = _TcpEStatsPathEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1)
)
tcpEStatsPathEntry.setIndexNames(
    (0, "TCP-ESTATS-MIB", "tcpEStatsConnectIndex"),
)
if mibBuilder.loadTexts:
    tcpEStatsPathEntry.setStatus("current")
_TcpEStatsPathRetranThresh_Type = Gauge32
_TcpEStatsPathRetranThresh_Object = MibTableColumn
tcpEStatsPathRetranThresh = _TcpEStatsPathRetranThresh_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 1),
    _TcpEStatsPathRetranThresh_Type()
)
tcpEStatsPathRetranThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathRetranThresh.setStatus("current")
_TcpEStatsPathNonRecovDAEpisodes_Type = ZeroBasedCounter32
_TcpEStatsPathNonRecovDAEpisodes_Object = MibTableColumn
tcpEStatsPathNonRecovDAEpisodes = _TcpEStatsPathNonRecovDAEpisodes_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 2),
    _TcpEStatsPathNonRecovDAEpisodes_Type()
)
tcpEStatsPathNonRecovDAEpisodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathNonRecovDAEpisodes.setStatus("current")
_TcpEStatsPathSumOctetsReordered_Type = ZeroBasedCounter32
_TcpEStatsPathSumOctetsReordered_Object = MibTableColumn
tcpEStatsPathSumOctetsReordered = _TcpEStatsPathSumOctetsReordered_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 3),
    _TcpEStatsPathSumOctetsReordered_Type()
)
tcpEStatsPathSumOctetsReordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathSumOctetsReordered.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathSumOctetsReordered.setUnits("octets")
_TcpEStatsPathNonRecovDA_Type = ZeroBasedCounter32
_TcpEStatsPathNonRecovDA_Object = MibTableColumn
tcpEStatsPathNonRecovDA = _TcpEStatsPathNonRecovDA_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 4),
    _TcpEStatsPathNonRecovDA_Type()
)
tcpEStatsPathNonRecovDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathNonRecovDA.setStatus("current")
_TcpEStatsPathSampleRTT_Type = Gauge32
_TcpEStatsPathSampleRTT_Object = MibTableColumn
tcpEStatsPathSampleRTT = _TcpEStatsPathSampleRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 11),
    _TcpEStatsPathSampleRTT_Type()
)
tcpEStatsPathSampleRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathSampleRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathSampleRTT.setUnits("milliseconds")
_TcpEStatsPathRTTVar_Type = Gauge32
_TcpEStatsPathRTTVar_Object = MibTableColumn
tcpEStatsPathRTTVar = _TcpEStatsPathRTTVar_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 12),
    _TcpEStatsPathRTTVar_Type()
)
tcpEStatsPathRTTVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathRTTVar.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathRTTVar.setUnits("milliseconds")
_TcpEStatsPathMaxRTT_Type = Gauge32
_TcpEStatsPathMaxRTT_Object = MibTableColumn
tcpEStatsPathMaxRTT = _TcpEStatsPathMaxRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 13),
    _TcpEStatsPathMaxRTT_Type()
)
tcpEStatsPathMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathMaxRTT.setUnits("milliseconds")
_TcpEStatsPathMinRTT_Type = Gauge32
_TcpEStatsPathMinRTT_Object = MibTableColumn
tcpEStatsPathMinRTT = _TcpEStatsPathMinRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 14),
    _TcpEStatsPathMinRTT_Type()
)
tcpEStatsPathMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathMinRTT.setUnits("milliseconds")
_TcpEStatsPathSumRTT_Type = ZeroBasedCounter32
_TcpEStatsPathSumRTT_Object = MibTableColumn
tcpEStatsPathSumRTT = _TcpEStatsPathSumRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 15),
    _TcpEStatsPathSumRTT_Type()
)
tcpEStatsPathSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathSumRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathSumRTT.setUnits("milliseconds")
_TcpEStatsPathHCSumRTT_Type = ZeroBasedCounter64
_TcpEStatsPathHCSumRTT_Object = MibTableColumn
tcpEStatsPathHCSumRTT = _TcpEStatsPathHCSumRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 16),
    _TcpEStatsPathHCSumRTT_Type()
)
tcpEStatsPathHCSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathHCSumRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathHCSumRTT.setUnits("milliseconds")
_TcpEStatsPathCountRTT_Type = ZeroBasedCounter32
_TcpEStatsPathCountRTT_Object = MibTableColumn
tcpEStatsPathCountRTT = _TcpEStatsPathCountRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 17),
    _TcpEStatsPathCountRTT_Type()
)
tcpEStatsPathCountRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathCountRTT.setStatus("current")
_TcpEStatsPathMaxRTO_Type = Gauge32
_TcpEStatsPathMaxRTO_Object = MibTableColumn
tcpEStatsPathMaxRTO = _TcpEStatsPathMaxRTO_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 18),
    _TcpEStatsPathMaxRTO_Type()
)
tcpEStatsPathMaxRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathMaxRTO.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathMaxRTO.setUnits("milliseconds")
_TcpEStatsPathMinRTO_Type = Gauge32
_TcpEStatsPathMinRTO_Object = MibTableColumn
tcpEStatsPathMinRTO = _TcpEStatsPathMinRTO_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 19),
    _TcpEStatsPathMinRTO_Type()
)
tcpEStatsPathMinRTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathMinRTO.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathMinRTO.setUnits("milliseconds")
_TcpEStatsPathIpTtl_Type = Unsigned32
_TcpEStatsPathIpTtl_Object = MibTableColumn
tcpEStatsPathIpTtl = _TcpEStatsPathIpTtl_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 20),
    _TcpEStatsPathIpTtl_Type()
)
tcpEStatsPathIpTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathIpTtl.setStatus("current")


class _TcpEStatsPathIpTosIn_Type(OctetString):
    """Custom type tcpEStatsPathIpTosIn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TcpEStatsPathIpTosIn_Type.__name__ = "OctetString"
_TcpEStatsPathIpTosIn_Object = MibTableColumn
tcpEStatsPathIpTosIn = _TcpEStatsPathIpTosIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 21),
    _TcpEStatsPathIpTosIn_Type()
)
tcpEStatsPathIpTosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathIpTosIn.setStatus("current")


class _TcpEStatsPathIpTosOut_Type(OctetString):
    """Custom type tcpEStatsPathIpTosOut based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_TcpEStatsPathIpTosOut_Type.__name__ = "OctetString"
_TcpEStatsPathIpTosOut_Object = MibTableColumn
tcpEStatsPathIpTosOut = _TcpEStatsPathIpTosOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 22),
    _TcpEStatsPathIpTosOut_Type()
)
tcpEStatsPathIpTosOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathIpTosOut.setStatus("current")
_TcpEStatsPathPreCongSumCwnd_Type = ZeroBasedCounter32
_TcpEStatsPathPreCongSumCwnd_Object = MibTableColumn
tcpEStatsPathPreCongSumCwnd = _TcpEStatsPathPreCongSumCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 23),
    _TcpEStatsPathPreCongSumCwnd_Type()
)
tcpEStatsPathPreCongSumCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathPreCongSumCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathPreCongSumCwnd.setUnits("octets")
_TcpEStatsPathPreCongSumRTT_Type = ZeroBasedCounter32
_TcpEStatsPathPreCongSumRTT_Object = MibTableColumn
tcpEStatsPathPreCongSumRTT = _TcpEStatsPathPreCongSumRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 24),
    _TcpEStatsPathPreCongSumRTT_Type()
)
tcpEStatsPathPreCongSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathPreCongSumRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathPreCongSumRTT.setUnits("milliseconds")
_TcpEStatsPathPostCongSumRTT_Type = ZeroBasedCounter32
_TcpEStatsPathPostCongSumRTT_Object = MibTableColumn
tcpEStatsPathPostCongSumRTT = _TcpEStatsPathPostCongSumRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 25),
    _TcpEStatsPathPostCongSumRTT_Type()
)
tcpEStatsPathPostCongSumRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathPostCongSumRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathPostCongSumRTT.setUnits("octets")
_TcpEStatsPathPostCongCountRTT_Type = ZeroBasedCounter32
_TcpEStatsPathPostCongCountRTT_Object = MibTableColumn
tcpEStatsPathPostCongCountRTT = _TcpEStatsPathPostCongCountRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 26),
    _TcpEStatsPathPostCongCountRTT_Type()
)
tcpEStatsPathPostCongCountRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathPostCongCountRTT.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsPathPostCongCountRTT.setUnits("milliseconds")
_TcpEStatsPathECNsignals_Type = ZeroBasedCounter32
_TcpEStatsPathECNsignals_Object = MibTableColumn
tcpEStatsPathECNsignals = _TcpEStatsPathECNsignals_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 27),
    _TcpEStatsPathECNsignals_Type()
)
tcpEStatsPathECNsignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathECNsignals.setStatus("current")
_TcpEStatsPathDupAckEpisodes_Type = ZeroBasedCounter32
_TcpEStatsPathDupAckEpisodes_Object = MibTableColumn
tcpEStatsPathDupAckEpisodes = _TcpEStatsPathDupAckEpisodes_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 28),
    _TcpEStatsPathDupAckEpisodes_Type()
)
tcpEStatsPathDupAckEpisodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathDupAckEpisodes.setStatus("current")
_TcpEStatsPathRcvRTT_Type = Gauge32
_TcpEStatsPathRcvRTT_Object = MibTableColumn
tcpEStatsPathRcvRTT = _TcpEStatsPathRcvRTT_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 29),
    _TcpEStatsPathRcvRTT_Type()
)
tcpEStatsPathRcvRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathRcvRTT.setStatus("current")
_TcpEStatsPathDupAcksOut_Type = ZeroBasedCounter32
_TcpEStatsPathDupAcksOut_Object = MibTableColumn
tcpEStatsPathDupAcksOut = _TcpEStatsPathDupAcksOut_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 30),
    _TcpEStatsPathDupAcksOut_Type()
)
tcpEStatsPathDupAcksOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathDupAcksOut.setStatus("current")
_TcpEStatsPathCERcvd_Type = ZeroBasedCounter32
_TcpEStatsPathCERcvd_Object = MibTableColumn
tcpEStatsPathCERcvd = _TcpEStatsPathCERcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 31),
    _TcpEStatsPathCERcvd_Type()
)
tcpEStatsPathCERcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathCERcvd.setStatus("current")
_TcpEStatsPathECESent_Type = ZeroBasedCounter32
_TcpEStatsPathECESent_Object = MibTableColumn
tcpEStatsPathECESent = _TcpEStatsPathECESent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 4, 1, 32),
    _TcpEStatsPathECESent_Type()
)
tcpEStatsPathECESent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsPathECESent.setStatus("current")
_TcpEStatsStackTable_Object = MibTable
tcpEStatsStackTable = _TcpEStatsStackTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tcpEStatsStackTable.setStatus("current")
_TcpEStatsStackEntry_Object = MibTableRow
tcpEStatsStackEntry = _TcpEStatsStackEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1)
)
tcpEStatsStackEntry.setIndexNames(
    (0, "TCP-ESTATS-MIB", "tcpEStatsConnectIndex"),
)
if mibBuilder.loadTexts:
    tcpEStatsStackEntry.setStatus("current")
_TcpEStatsStackActiveOpen_Type = TruthValue
_TcpEStatsStackActiveOpen_Object = MibTableColumn
tcpEStatsStackActiveOpen = _TcpEStatsStackActiveOpen_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 1),
    _TcpEStatsStackActiveOpen_Type()
)
tcpEStatsStackActiveOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackActiveOpen.setStatus("current")
_TcpEStatsStackMSSSent_Type = Unsigned32
_TcpEStatsStackMSSSent_Object = MibTableColumn
tcpEStatsStackMSSSent = _TcpEStatsStackMSSSent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 2),
    _TcpEStatsStackMSSSent_Type()
)
tcpEStatsStackMSSSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMSSSent.setStatus("current")
_TcpEStatsStackMSSRcvd_Type = Unsigned32
_TcpEStatsStackMSSRcvd_Object = MibTableColumn
tcpEStatsStackMSSRcvd = _TcpEStatsStackMSSRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 3),
    _TcpEStatsStackMSSRcvd_Type()
)
tcpEStatsStackMSSRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMSSRcvd.setStatus("current")


class _TcpEStatsStackWinScaleSent_Type(Integer32):
    """Custom type tcpEStatsStackWinScaleSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_TcpEStatsStackWinScaleSent_Type.__name__ = "Integer32"
_TcpEStatsStackWinScaleSent_Object = MibTableColumn
tcpEStatsStackWinScaleSent = _TcpEStatsStackWinScaleSent_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 4),
    _TcpEStatsStackWinScaleSent_Type()
)
tcpEStatsStackWinScaleSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackWinScaleSent.setStatus("current")


class _TcpEStatsStackWinScaleRcvd_Type(Integer32):
    """Custom type tcpEStatsStackWinScaleRcvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 14),
    )


_TcpEStatsStackWinScaleRcvd_Type.__name__ = "Integer32"
_TcpEStatsStackWinScaleRcvd_Object = MibTableColumn
tcpEStatsStackWinScaleRcvd = _TcpEStatsStackWinScaleRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 5),
    _TcpEStatsStackWinScaleRcvd_Type()
)
tcpEStatsStackWinScaleRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackWinScaleRcvd.setStatus("current")
_TcpEStatsStackTimeStamps_Type = TcpEStatsNegotiated
_TcpEStatsStackTimeStamps_Object = MibTableColumn
tcpEStatsStackTimeStamps = _TcpEStatsStackTimeStamps_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 6),
    _TcpEStatsStackTimeStamps_Type()
)
tcpEStatsStackTimeStamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackTimeStamps.setStatus("current")
_TcpEStatsStackECN_Type = TcpEStatsNegotiated
_TcpEStatsStackECN_Object = MibTableColumn
tcpEStatsStackECN = _TcpEStatsStackECN_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 7),
    _TcpEStatsStackECN_Type()
)
tcpEStatsStackECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackECN.setStatus("current")
_TcpEStatsStackWillSendSACK_Type = TcpEStatsNegotiated
_TcpEStatsStackWillSendSACK_Object = MibTableColumn
tcpEStatsStackWillSendSACK = _TcpEStatsStackWillSendSACK_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 8),
    _TcpEStatsStackWillSendSACK_Type()
)
tcpEStatsStackWillSendSACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackWillSendSACK.setStatus("current")
_TcpEStatsStackWillUseSACK_Type = TcpEStatsNegotiated
_TcpEStatsStackWillUseSACK_Object = MibTableColumn
tcpEStatsStackWillUseSACK = _TcpEStatsStackWillUseSACK_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 9),
    _TcpEStatsStackWillUseSACK_Type()
)
tcpEStatsStackWillUseSACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackWillUseSACK.setStatus("current")


class _TcpEStatsStackState_Type(Integer32):
    """Custom type tcpEStatsStackState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("tcpESStateCloseWait", 8),
          ("tcpESStateClosed", 1),
          ("tcpESStateClosing", 10),
          ("tcpESStateDeleteTcb", 12),
          ("tcpESStateEstablished", 5),
          ("tcpESStateFinWait1", 6),
          ("tcpESStateFinWait2", 7),
          ("tcpESStateLastAck", 9),
          ("tcpESStateListen", 2),
          ("tcpESStateSynReceived", 4),
          ("tcpESStateSynSent", 3),
          ("tcpESStateTimeWait", 11))
    )


_TcpEStatsStackState_Type.__name__ = "Integer32"
_TcpEStatsStackState_Object = MibTableColumn
tcpEStatsStackState = _TcpEStatsStackState_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 10),
    _TcpEStatsStackState_Type()
)
tcpEStatsStackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackState.setStatus("current")
_TcpEStatsStackNagle_Type = TruthValue
_TcpEStatsStackNagle_Object = MibTableColumn
tcpEStatsStackNagle = _TcpEStatsStackNagle_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 11),
    _TcpEStatsStackNagle_Type()
)
tcpEStatsStackNagle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackNagle.setStatus("current")
_TcpEStatsStackMaxSsCwnd_Type = Gauge32
_TcpEStatsStackMaxSsCwnd_Object = MibTableColumn
tcpEStatsStackMaxSsCwnd = _TcpEStatsStackMaxSsCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 12),
    _TcpEStatsStackMaxSsCwnd_Type()
)
tcpEStatsStackMaxSsCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxSsCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxSsCwnd.setUnits("octets")
_TcpEStatsStackMaxCaCwnd_Type = Gauge32
_TcpEStatsStackMaxCaCwnd_Object = MibTableColumn
tcpEStatsStackMaxCaCwnd = _TcpEStatsStackMaxCaCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 13),
    _TcpEStatsStackMaxCaCwnd_Type()
)
tcpEStatsStackMaxCaCwnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxCaCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxCaCwnd.setUnits("octets")
_TcpEStatsStackMaxSsthresh_Type = Gauge32
_TcpEStatsStackMaxSsthresh_Object = MibTableColumn
tcpEStatsStackMaxSsthresh = _TcpEStatsStackMaxSsthresh_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 14),
    _TcpEStatsStackMaxSsthresh_Type()
)
tcpEStatsStackMaxSsthresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxSsthresh.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxSsthresh.setUnits("octets")
_TcpEStatsStackMinSsthresh_Type = Gauge32
_TcpEStatsStackMinSsthresh_Object = MibTableColumn
tcpEStatsStackMinSsthresh = _TcpEStatsStackMinSsthresh_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 15),
    _TcpEStatsStackMinSsthresh_Type()
)
tcpEStatsStackMinSsthresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMinSsthresh.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMinSsthresh.setUnits("octets")


class _TcpEStatsStackInRecovery_Type(Integer32):
    """Custom type tcpEStatsStackInRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcpESDataContiguous", 1),
          ("tcpESDataRecovery", 3),
          ("tcpESDataUnordered", 2))
    )


_TcpEStatsStackInRecovery_Type.__name__ = "Integer32"
_TcpEStatsStackInRecovery_Object = MibTableColumn
tcpEStatsStackInRecovery = _TcpEStatsStackInRecovery_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 16),
    _TcpEStatsStackInRecovery_Type()
)
tcpEStatsStackInRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackInRecovery.setStatus("current")
_TcpEStatsStackDupAcksIn_Type = ZeroBasedCounter32
_TcpEStatsStackDupAcksIn_Object = MibTableColumn
tcpEStatsStackDupAcksIn = _TcpEStatsStackDupAcksIn_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 17),
    _TcpEStatsStackDupAcksIn_Type()
)
tcpEStatsStackDupAcksIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackDupAcksIn.setStatus("current")
_TcpEStatsStackSpuriousFrDetected_Type = ZeroBasedCounter32
_TcpEStatsStackSpuriousFrDetected_Object = MibTableColumn
tcpEStatsStackSpuriousFrDetected = _TcpEStatsStackSpuriousFrDetected_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 18),
    _TcpEStatsStackSpuriousFrDetected_Type()
)
tcpEStatsStackSpuriousFrDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSpuriousFrDetected.setStatus("current")
_TcpEStatsStackSpuriousRtoDetected_Type = ZeroBasedCounter32
_TcpEStatsStackSpuriousRtoDetected_Object = MibTableColumn
tcpEStatsStackSpuriousRtoDetected = _TcpEStatsStackSpuriousRtoDetected_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 19),
    _TcpEStatsStackSpuriousRtoDetected_Type()
)
tcpEStatsStackSpuriousRtoDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSpuriousRtoDetected.setStatus("current")
_TcpEStatsStackSoftErrors_Type = ZeroBasedCounter32
_TcpEStatsStackSoftErrors_Object = MibTableColumn
tcpEStatsStackSoftErrors = _TcpEStatsStackSoftErrors_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 21),
    _TcpEStatsStackSoftErrors_Type()
)
tcpEStatsStackSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSoftErrors.setStatus("current")


class _TcpEStatsStackSoftErrorReason_Type(Integer32):
    """Custom type tcpEStatsStackSoftErrorReason based on Integer32"""
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
        *(("aboveAckWindow", 4),
          ("aboveDataWindow", 2),
          ("aboveTSWindow", 6),
          ("belowAckWindow", 3),
          ("belowDataWindow", 1),
          ("belowTSWindow", 5),
          ("dataCheckSum", 7),
          ("otherSoftError", 8))
    )


_TcpEStatsStackSoftErrorReason_Type.__name__ = "Integer32"
_TcpEStatsStackSoftErrorReason_Object = MibTableColumn
tcpEStatsStackSoftErrorReason = _TcpEStatsStackSoftErrorReason_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 22),
    _TcpEStatsStackSoftErrorReason_Type()
)
tcpEStatsStackSoftErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSoftErrorReason.setStatus("current")
_TcpEStatsStackSlowStart_Type = ZeroBasedCounter32
_TcpEStatsStackSlowStart_Object = MibTableColumn
tcpEStatsStackSlowStart = _TcpEStatsStackSlowStart_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 23),
    _TcpEStatsStackSlowStart_Type()
)
tcpEStatsStackSlowStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSlowStart.setStatus("current")
_TcpEStatsStackCongAvoid_Type = ZeroBasedCounter32
_TcpEStatsStackCongAvoid_Object = MibTableColumn
tcpEStatsStackCongAvoid = _TcpEStatsStackCongAvoid_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 24),
    _TcpEStatsStackCongAvoid_Type()
)
tcpEStatsStackCongAvoid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackCongAvoid.setStatus("current")
_TcpEStatsStackOtherReductions_Type = ZeroBasedCounter32
_TcpEStatsStackOtherReductions_Object = MibTableColumn
tcpEStatsStackOtherReductions = _TcpEStatsStackOtherReductions_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 25),
    _TcpEStatsStackOtherReductions_Type()
)
tcpEStatsStackOtherReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackOtherReductions.setStatus("current")
_TcpEStatsStackCongOverCount_Type = ZeroBasedCounter32
_TcpEStatsStackCongOverCount_Object = MibTableColumn
tcpEStatsStackCongOverCount = _TcpEStatsStackCongOverCount_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 26),
    _TcpEStatsStackCongOverCount_Type()
)
tcpEStatsStackCongOverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackCongOverCount.setStatus("current")
_TcpEStatsStackFastRetran_Type = ZeroBasedCounter32
_TcpEStatsStackFastRetran_Object = MibTableColumn
tcpEStatsStackFastRetran = _TcpEStatsStackFastRetran_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 27),
    _TcpEStatsStackFastRetran_Type()
)
tcpEStatsStackFastRetran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackFastRetran.setStatus("current")
_TcpEStatsStackSubsequentTimeouts_Type = ZeroBasedCounter32
_TcpEStatsStackSubsequentTimeouts_Object = MibTableColumn
tcpEStatsStackSubsequentTimeouts = _TcpEStatsStackSubsequentTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 28),
    _TcpEStatsStackSubsequentTimeouts_Type()
)
tcpEStatsStackSubsequentTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSubsequentTimeouts.setStatus("current")
_TcpEStatsStackCurTimeoutCount_Type = Gauge32
_TcpEStatsStackCurTimeoutCount_Object = MibTableColumn
tcpEStatsStackCurTimeoutCount = _TcpEStatsStackCurTimeoutCount_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 29),
    _TcpEStatsStackCurTimeoutCount_Type()
)
tcpEStatsStackCurTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackCurTimeoutCount.setStatus("current")
_TcpEStatsStackAbruptTimeouts_Type = ZeroBasedCounter32
_TcpEStatsStackAbruptTimeouts_Object = MibTableColumn
tcpEStatsStackAbruptTimeouts = _TcpEStatsStackAbruptTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 30),
    _TcpEStatsStackAbruptTimeouts_Type()
)
tcpEStatsStackAbruptTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackAbruptTimeouts.setStatus("current")
_TcpEStatsStackSACKsRcvd_Type = ZeroBasedCounter32
_TcpEStatsStackSACKsRcvd_Object = MibTableColumn
tcpEStatsStackSACKsRcvd = _TcpEStatsStackSACKsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 31),
    _TcpEStatsStackSACKsRcvd_Type()
)
tcpEStatsStackSACKsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSACKsRcvd.setStatus("current")
_TcpEStatsStackSACKBlocksRcvd_Type = ZeroBasedCounter32
_TcpEStatsStackSACKBlocksRcvd_Object = MibTableColumn
tcpEStatsStackSACKBlocksRcvd = _TcpEStatsStackSACKBlocksRcvd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 32),
    _TcpEStatsStackSACKBlocksRcvd_Type()
)
tcpEStatsStackSACKBlocksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSACKBlocksRcvd.setStatus("current")
_TcpEStatsStackSendStall_Type = ZeroBasedCounter32
_TcpEStatsStackSendStall_Object = MibTableColumn
tcpEStatsStackSendStall = _TcpEStatsStackSendStall_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 33),
    _TcpEStatsStackSendStall_Type()
)
tcpEStatsStackSendStall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSendStall.setStatus("current")
_TcpEStatsStackDSACKDups_Type = ZeroBasedCounter32
_TcpEStatsStackDSACKDups_Object = MibTableColumn
tcpEStatsStackDSACKDups = _TcpEStatsStackDSACKDups_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 34),
    _TcpEStatsStackDSACKDups_Type()
)
tcpEStatsStackDSACKDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackDSACKDups.setStatus("current")
_TcpEStatsStackMaxMSS_Type = Gauge32
_TcpEStatsStackMaxMSS_Object = MibTableColumn
tcpEStatsStackMaxMSS = _TcpEStatsStackMaxMSS_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 35),
    _TcpEStatsStackMaxMSS_Type()
)
tcpEStatsStackMaxMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxMSS.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxMSS.setUnits("octets")
_TcpEStatsStackMinMSS_Type = Gauge32
_TcpEStatsStackMinMSS_Object = MibTableColumn
tcpEStatsStackMinMSS = _TcpEStatsStackMinMSS_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 36),
    _TcpEStatsStackMinMSS_Type()
)
tcpEStatsStackMinMSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMinMSS.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMinMSS.setUnits("octets")
_TcpEStatsStackSndInitial_Type = Unsigned32
_TcpEStatsStackSndInitial_Object = MibTableColumn
tcpEStatsStackSndInitial = _TcpEStatsStackSndInitial_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 37),
    _TcpEStatsStackSndInitial_Type()
)
tcpEStatsStackSndInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackSndInitial.setStatus("current")
_TcpEStatsStackRecInitial_Type = Unsigned32
_TcpEStatsStackRecInitial_Object = MibTableColumn
tcpEStatsStackRecInitial = _TcpEStatsStackRecInitial_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 38),
    _TcpEStatsStackRecInitial_Type()
)
tcpEStatsStackRecInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackRecInitial.setStatus("current")
_TcpEStatsStackCurRetxQueue_Type = Gauge32
_TcpEStatsStackCurRetxQueue_Object = MibTableColumn
tcpEStatsStackCurRetxQueue = _TcpEStatsStackCurRetxQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 39),
    _TcpEStatsStackCurRetxQueue_Type()
)
tcpEStatsStackCurRetxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackCurRetxQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackCurRetxQueue.setUnits("octets")
_TcpEStatsStackMaxRetxQueue_Type = Gauge32
_TcpEStatsStackMaxRetxQueue_Object = MibTableColumn
tcpEStatsStackMaxRetxQueue = _TcpEStatsStackMaxRetxQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 40),
    _TcpEStatsStackMaxRetxQueue_Type()
)
tcpEStatsStackMaxRetxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxRetxQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxRetxQueue.setUnits("octets")
_TcpEStatsStackCurReasmQueue_Type = Gauge32
_TcpEStatsStackCurReasmQueue_Object = MibTableColumn
tcpEStatsStackCurReasmQueue = _TcpEStatsStackCurReasmQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 41),
    _TcpEStatsStackCurReasmQueue_Type()
)
tcpEStatsStackCurReasmQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackCurReasmQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsStackCurReasmQueue.setUnits("octets")
_TcpEStatsStackMaxReasmQueue_Type = Gauge32
_TcpEStatsStackMaxReasmQueue_Object = MibTableColumn
tcpEStatsStackMaxReasmQueue = _TcpEStatsStackMaxReasmQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 5, 1, 42),
    _TcpEStatsStackMaxReasmQueue_Type()
)
tcpEStatsStackMaxReasmQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsStackMaxReasmQueue.setStatus("current")
_TcpEStatsAppTable_Object = MibTable
tcpEStatsAppTable = _TcpEStatsAppTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tcpEStatsAppTable.setStatus("current")
_TcpEStatsAppEntry_Object = MibTableRow
tcpEStatsAppEntry = _TcpEStatsAppEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1)
)
tcpEStatsAppEntry.setIndexNames(
    (0, "TCP-ESTATS-MIB", "tcpEStatsConnectIndex"),
)
if mibBuilder.loadTexts:
    tcpEStatsAppEntry.setStatus("current")
_TcpEStatsAppSndUna_Type = Counter32
_TcpEStatsAppSndUna_Object = MibTableColumn
tcpEStatsAppSndUna = _TcpEStatsAppSndUna_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 1),
    _TcpEStatsAppSndUna_Type()
)
tcpEStatsAppSndUna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppSndUna.setStatus("current")
_TcpEStatsAppSndNxt_Type = Unsigned32
_TcpEStatsAppSndNxt_Object = MibTableColumn
tcpEStatsAppSndNxt = _TcpEStatsAppSndNxt_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 2),
    _TcpEStatsAppSndNxt_Type()
)
tcpEStatsAppSndNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppSndNxt.setStatus("current")
_TcpEStatsAppSndMax_Type = Counter32
_TcpEStatsAppSndMax_Object = MibTableColumn
tcpEStatsAppSndMax = _TcpEStatsAppSndMax_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 3),
    _TcpEStatsAppSndMax_Type()
)
tcpEStatsAppSndMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppSndMax.setStatus("current")
_TcpEStatsAppThruOctetsAcked_Type = ZeroBasedCounter32
_TcpEStatsAppThruOctetsAcked_Object = MibTableColumn
tcpEStatsAppThruOctetsAcked = _TcpEStatsAppThruOctetsAcked_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 4),
    _TcpEStatsAppThruOctetsAcked_Type()
)
tcpEStatsAppThruOctetsAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppThruOctetsAcked.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppThruOctetsAcked.setUnits("octets")
_TcpEStatsAppHCThruOctetsAcked_Type = ZeroBasedCounter64
_TcpEStatsAppHCThruOctetsAcked_Object = MibTableColumn
tcpEStatsAppHCThruOctetsAcked = _TcpEStatsAppHCThruOctetsAcked_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 5),
    _TcpEStatsAppHCThruOctetsAcked_Type()
)
tcpEStatsAppHCThruOctetsAcked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppHCThruOctetsAcked.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppHCThruOctetsAcked.setUnits("octets")
_TcpEStatsAppRcvNxt_Type = Counter32
_TcpEStatsAppRcvNxt_Object = MibTableColumn
tcpEStatsAppRcvNxt = _TcpEStatsAppRcvNxt_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 6),
    _TcpEStatsAppRcvNxt_Type()
)
tcpEStatsAppRcvNxt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppRcvNxt.setStatus("current")
_TcpEStatsAppThruOctetsReceived_Type = ZeroBasedCounter32
_TcpEStatsAppThruOctetsReceived_Object = MibTableColumn
tcpEStatsAppThruOctetsReceived = _TcpEStatsAppThruOctetsReceived_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 7),
    _TcpEStatsAppThruOctetsReceived_Type()
)
tcpEStatsAppThruOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppThruOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppThruOctetsReceived.setUnits("octets")
_TcpEStatsAppHCThruOctetsReceived_Type = ZeroBasedCounter64
_TcpEStatsAppHCThruOctetsReceived_Object = MibTableColumn
tcpEStatsAppHCThruOctetsReceived = _TcpEStatsAppHCThruOctetsReceived_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 8),
    _TcpEStatsAppHCThruOctetsReceived_Type()
)
tcpEStatsAppHCThruOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppHCThruOctetsReceived.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppHCThruOctetsReceived.setUnits("octets")
_TcpEStatsAppCurAppWQueue_Type = Gauge32
_TcpEStatsAppCurAppWQueue_Object = MibTableColumn
tcpEStatsAppCurAppWQueue = _TcpEStatsAppCurAppWQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 11),
    _TcpEStatsAppCurAppWQueue_Type()
)
tcpEStatsAppCurAppWQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppCurAppWQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppCurAppWQueue.setUnits("octets")
_TcpEStatsAppMaxAppWQueue_Type = Gauge32
_TcpEStatsAppMaxAppWQueue_Object = MibTableColumn
tcpEStatsAppMaxAppWQueue = _TcpEStatsAppMaxAppWQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 12),
    _TcpEStatsAppMaxAppWQueue_Type()
)
tcpEStatsAppMaxAppWQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppMaxAppWQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppMaxAppWQueue.setUnits("octets")
_TcpEStatsAppCurAppRQueue_Type = Gauge32
_TcpEStatsAppCurAppRQueue_Object = MibTableColumn
tcpEStatsAppCurAppRQueue = _TcpEStatsAppCurAppRQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 13),
    _TcpEStatsAppCurAppRQueue_Type()
)
tcpEStatsAppCurAppRQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppCurAppRQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppCurAppRQueue.setUnits("octets")
_TcpEStatsAppMaxAppRQueue_Type = Gauge32
_TcpEStatsAppMaxAppRQueue_Object = MibTableColumn
tcpEStatsAppMaxAppRQueue = _TcpEStatsAppMaxAppRQueue_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 6, 1, 14),
    _TcpEStatsAppMaxAppRQueue_Type()
)
tcpEStatsAppMaxAppRQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsAppMaxAppRQueue.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsAppMaxAppRQueue.setUnits("octets")
_TcpEStatsTuneTable_Object = MibTable
tcpEStatsTuneTable = _TcpEStatsTuneTable_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tcpEStatsTuneTable.setStatus("current")
_TcpEStatsTuneEntry_Object = MibTableRow
tcpEStatsTuneEntry = _TcpEStatsTuneEntry_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7, 1)
)
tcpEStatsTuneEntry.setIndexNames(
    (0, "TCP-ESTATS-MIB", "tcpEStatsConnectIndex"),
)
if mibBuilder.loadTexts:
    tcpEStatsTuneEntry.setStatus("current")
_TcpEStatsTuneLimCwnd_Type = Unsigned32
_TcpEStatsTuneLimCwnd_Object = MibTableColumn
tcpEStatsTuneLimCwnd = _TcpEStatsTuneLimCwnd_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7, 1, 1),
    _TcpEStatsTuneLimCwnd_Type()
)
tcpEStatsTuneLimCwnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimCwnd.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimCwnd.setUnits("octets")
_TcpEStatsTuneLimSsthresh_Type = Unsigned32
_TcpEStatsTuneLimSsthresh_Object = MibTableColumn
tcpEStatsTuneLimSsthresh = _TcpEStatsTuneLimSsthresh_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7, 1, 2),
    _TcpEStatsTuneLimSsthresh_Type()
)
tcpEStatsTuneLimSsthresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimSsthresh.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimSsthresh.setUnits("octets")
_TcpEStatsTuneLimRwin_Type = Unsigned32
_TcpEStatsTuneLimRwin_Object = MibTableColumn
tcpEStatsTuneLimRwin = _TcpEStatsTuneLimRwin_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7, 1, 3),
    _TcpEStatsTuneLimRwin_Type()
)
tcpEStatsTuneLimRwin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimRwin.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimRwin.setUnits("octets")
_TcpEStatsTuneLimMSS_Type = Unsigned32
_TcpEStatsTuneLimMSS_Object = MibTableColumn
tcpEStatsTuneLimMSS = _TcpEStatsTuneLimMSS_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 1, 7, 1, 4),
    _TcpEStatsTuneLimMSS_Type()
)
tcpEStatsTuneLimMSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimMSS.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsTuneLimMSS.setUnits("octets")
_TcpEStatsControl_ObjectIdentity = ObjectIdentity
tcpEStatsControl = _TcpEStatsControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 1, 2)
)


class _TcpEStatsControlPath_Type(TruthValue):
    """Custom type tcpEStatsControlPath based on TruthValue"""


_TcpEStatsControlPath_Object = MibScalar
tcpEStatsControlPath = _TcpEStatsControlPath_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 1),
    _TcpEStatsControlPath_Type()
)
tcpEStatsControlPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsControlPath.setStatus("current")


class _TcpEStatsControlStack_Type(TruthValue):
    """Custom type tcpEStatsControlStack based on TruthValue"""


_TcpEStatsControlStack_Object = MibScalar
tcpEStatsControlStack = _TcpEStatsControlStack_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 2),
    _TcpEStatsControlStack_Type()
)
tcpEStatsControlStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsControlStack.setStatus("current")


class _TcpEStatsControlApp_Type(TruthValue):
    """Custom type tcpEStatsControlApp based on TruthValue"""


_TcpEStatsControlApp_Object = MibScalar
tcpEStatsControlApp = _TcpEStatsControlApp_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 3),
    _TcpEStatsControlApp_Type()
)
tcpEStatsControlApp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsControlApp.setStatus("current")


class _TcpEStatsControlTune_Type(TruthValue):
    """Custom type tcpEStatsControlTune based on TruthValue"""


_TcpEStatsControlTune_Object = MibScalar
tcpEStatsControlTune = _TcpEStatsControlTune_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 4),
    _TcpEStatsControlTune_Type()
)
tcpEStatsControlTune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsControlTune.setStatus("current")


class _TcpEStatsControlNotify_Type(TruthValue):
    """Custom type tcpEStatsControlNotify based on TruthValue"""


_TcpEStatsControlNotify_Object = MibScalar
tcpEStatsControlNotify = _TcpEStatsControlNotify_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 5),
    _TcpEStatsControlNotify_Type()
)
tcpEStatsControlNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsControlNotify.setStatus("current")


class _TcpEStatsConnTableLatency_Type(Unsigned32):
    """Custom type tcpEStatsConnTableLatency based on Unsigned32"""
    defaultValue = 0


_TcpEStatsConnTableLatency_Object = MibScalar
tcpEStatsConnTableLatency = _TcpEStatsConnTableLatency_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 2, 6),
    _TcpEStatsConnTableLatency_Type()
)
tcpEStatsConnTableLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpEStatsConnTableLatency.setStatus("current")
if mibBuilder.loadTexts:
    tcpEStatsConnTableLatency.setUnits("seconds")
_TcpEStatsScalar_ObjectIdentity = ObjectIdentity
tcpEStatsScalar = _TcpEStatsScalar_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 1, 3)
)
_TcpEStatsListenerTableLastChange_Type = TimeStamp
_TcpEStatsListenerTableLastChange_Object = MibScalar
tcpEStatsListenerTableLastChange = _TcpEStatsListenerTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 156, 1, 3, 3),
    _TcpEStatsListenerTableLastChange_Type()
)
tcpEStatsListenerTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEStatsListenerTableLastChange.setStatus("current")
_TcpEStatsConformance_ObjectIdentity = ObjectIdentity
tcpEStatsConformance = _TcpEStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 2)
)
_TcpEStatsCompliances_ObjectIdentity = ObjectIdentity
tcpEStatsCompliances = _TcpEStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 2, 1)
)
_TcpEStatsGroups_ObjectIdentity = ObjectIdentity
tcpEStatsGroups = _TcpEStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 156, 2, 2)
)
tcpListenerEntry.registerAugmentions(
    ("TCP-ESTATS-MIB",
     "tcpEStatsListenerEntry")
)
tcpEStatsListenerEntry.setIndexNames(*tcpListenerEntry.getIndexNames())
tcpConnectionEntry.registerAugmentions(
    ("TCP-ESTATS-MIB",
     "tcpEStatsConnectIdEntry")
)
tcpEStatsConnectIdEntry.setIndexNames(*tcpConnectionEntry.getIndexNames())

# Managed Objects groups

tcpEStatsListenerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 1)
)
tcpEStatsListenerGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsListenerTableLastChange"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerStartTime"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerSynRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerInitial"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerEstablished"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerAccepted"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerExceedBacklog"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerCurConns"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerMaxBacklog"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerCurBacklog"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerCurEstabBacklog"))
)
if mibBuilder.loadTexts:
    tcpEStatsListenerGroup.setStatus("current")

tcpEStatsListenerHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 2)
)
tcpEStatsListenerHCGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsListenerHCSynRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerHCInitial"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerHCEstablished"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerHCAccepted"),
        ("TCP-ESTATS-MIB", "tcpEStatsListenerHCExceedBacklog"))
)
if mibBuilder.loadTexts:
    tcpEStatsListenerHCGroup.setStatus("current")

tcpEStatsConnectIdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 3)
)
tcpEStatsConnectIdGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsConnTableLatency"),
        ("TCP-ESTATS-MIB", "tcpEStatsConnectIndex"))
)
if mibBuilder.loadTexts:
    tcpEStatsConnectIdGroup.setStatus("current")

tcpEStatsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 4)
)
tcpEStatsPerfGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsPerfSegsOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfDataSegsOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfDataOctetsOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSegsRetrans"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfOctetsRetrans"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSegsIn"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfDataSegsIn"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfDataOctetsIn"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfElapsedSecs"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfElapsedMicroSecs"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfStartTimeStamp"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurMSS"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfPipeSize"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfMaxPipeSize"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSmoothedRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurRTO"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCongSignals"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurSsthresh"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfTimeouts"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurRwinSent"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfMaxRwinSent"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfZeroRwinSent"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfCurRwinRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfMaxRwinRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfZeroRwinRcvd"))
)
if mibBuilder.loadTexts:
    tcpEStatsPerfGroup.setStatus("current")

tcpEStatsPerfOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 5)
)
tcpEStatsPerfOptionalGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTransRwin"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTransCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTransSnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTimeRwin"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTimeCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfSndLimTimeSnd"))
)
if mibBuilder.loadTexts:
    tcpEStatsPerfOptionalGroup.setStatus("current")

tcpEStatsPerfHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 6)
)
tcpEStatsPerfHCGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsPerfHCDataOctetsOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPerfHCDataOctetsIn"))
)
if mibBuilder.loadTexts:
    tcpEStatsPerfHCGroup.setStatus("current")

tcpEStatsPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 7)
)
tcpEStatsPathGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsControlPath"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathRetranThresh"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathNonRecovDAEpisodes"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathSumOctetsReordered"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathNonRecovDA"))
)
if mibBuilder.loadTexts:
    tcpEStatsPathGroup.setStatus("current")

tcpEStatsPathOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 8)
)
tcpEStatsPathOptionalGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsPathSampleRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathRTTVar"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathMaxRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathMinRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathSumRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathCountRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathMaxRTO"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathMinRTO"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathIpTtl"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathIpTosIn"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathIpTosOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathPreCongSumCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathPreCongSumRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathPostCongSumRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathPostCongCountRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathECNsignals"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathDupAckEpisodes"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathRcvRTT"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathDupAcksOut"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathCERcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsPathECESent"))
)
if mibBuilder.loadTexts:
    tcpEStatsPathOptionalGroup.setStatus("current")

tcpEStatsPathHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 9)
)
tcpEStatsPathHCGroup.setObjects(
    ("TCP-ESTATS-MIB", "tcpEStatsPathHCSumRTT")
)
if mibBuilder.loadTexts:
    tcpEStatsPathHCGroup.setStatus("current")

tcpEStatsStackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 10)
)
tcpEStatsStackGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsControlStack"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackActiveOpen"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMSSSent"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMSSRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackWinScaleSent"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackWinScaleRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackTimeStamps"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackECN"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackWillSendSACK"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackWillUseSACK"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackState"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackNagle"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxSsCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxCaCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxSsthresh"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMinSsthresh"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackInRecovery"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackDupAcksIn"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSpuriousFrDetected"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSpuriousRtoDetected"))
)
if mibBuilder.loadTexts:
    tcpEStatsStackGroup.setStatus("current")

tcpEStatsStackOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 11)
)
tcpEStatsStackOptionalGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsStackSoftErrors"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSoftErrorReason"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSlowStart"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackCongAvoid"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackOtherReductions"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackCongOverCount"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackFastRetran"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSubsequentTimeouts"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackCurTimeoutCount"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackAbruptTimeouts"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSACKsRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSACKBlocksRcvd"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSendStall"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackDSACKDups"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxMSS"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMinMSS"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackSndInitial"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackRecInitial"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackCurRetxQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxRetxQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackCurReasmQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsStackMaxReasmQueue"))
)
if mibBuilder.loadTexts:
    tcpEStatsStackOptionalGroup.setStatus("current")

tcpEStatsAppGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 12)
)
tcpEStatsAppGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsControlApp"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppSndUna"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppSndNxt"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppSndMax"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppThruOctetsAcked"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppRcvNxt"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppThruOctetsReceived"))
)
if mibBuilder.loadTexts:
    tcpEStatsAppGroup.setStatus("current")

tcpEStatsAppHCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 13)
)
tcpEStatsAppHCGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsAppHCThruOctetsAcked"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppHCThruOctetsReceived"))
)
if mibBuilder.loadTexts:
    tcpEStatsAppHCGroup.setStatus("current")

tcpEStatsAppOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 14)
)
tcpEStatsAppOptionalGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsAppCurAppWQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppMaxAppWQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppCurAppRQueue"),
        ("TCP-ESTATS-MIB", "tcpEStatsAppMaxAppRQueue"))
)
if mibBuilder.loadTexts:
    tcpEStatsAppOptionalGroup.setStatus("current")

tcpEStatsTuneOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 15)
)
tcpEStatsTuneOptionalGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsControlTune"),
        ("TCP-ESTATS-MIB", "tcpEStatsTuneLimCwnd"),
        ("TCP-ESTATS-MIB", "tcpEStatsTuneLimSsthresh"),
        ("TCP-ESTATS-MIB", "tcpEStatsTuneLimRwin"),
        ("TCP-ESTATS-MIB", "tcpEStatsTuneLimMSS"))
)
if mibBuilder.loadTexts:
    tcpEStatsTuneOptionalGroup.setStatus("current")

tcpEStatsNotificationsCtlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 17)
)
tcpEStatsNotificationsCtlGroup.setObjects(
    ("TCP-ESTATS-MIB", "tcpEStatsControlNotify")
)
if mibBuilder.loadTexts:
    tcpEStatsNotificationsCtlGroup.setStatus("current")


# Notification objects

tcpEStatsEstablishNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 156, 0, 1)
)
tcpEStatsEstablishNotification.setObjects(
    ("TCP-ESTATS-MIB", "tcpEStatsConnectIndex")
)
if mibBuilder.loadTexts:
    tcpEStatsEstablishNotification.setStatus(
        "current"
    )

tcpEStatsCloseNotification = NotificationType(
    (1, 3, 6, 1, 2, 1, 156, 0, 2)
)
tcpEStatsCloseNotification.setObjects(
    ("TCP-ESTATS-MIB", "tcpEStatsConnectIndex")
)
if mibBuilder.loadTexts:
    tcpEStatsCloseNotification.setStatus(
        "current"
    )


# Notifications groups

tcpEStatsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 156, 2, 2, 16)
)
tcpEStatsNotificationsGroup.setObjects(
      *(("TCP-ESTATS-MIB", "tcpEStatsEstablishNotification"),
        ("TCP-ESTATS-MIB", "tcpEStatsCloseNotification"))
)
if mibBuilder.loadTexts:
    tcpEStatsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcpEStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 156, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tcpEStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TCP-ESTATS-MIB",
    **{"TcpEStatsNegotiated": TcpEStatsNegotiated,
       "tcpEStatsMIB": tcpEStatsMIB,
       "tcpEStatsNotifications": tcpEStatsNotifications,
       "tcpEStatsEstablishNotification": tcpEStatsEstablishNotification,
       "tcpEStatsCloseNotification": tcpEStatsCloseNotification,
       "tcpEStatsMIBObjects": tcpEStatsMIBObjects,
       "tcpEStats": tcpEStats,
       "tcpEStatsListenerTable": tcpEStatsListenerTable,
       "tcpEStatsListenerEntry": tcpEStatsListenerEntry,
       "tcpEStatsListenerStartTime": tcpEStatsListenerStartTime,
       "tcpEStatsListenerSynRcvd": tcpEStatsListenerSynRcvd,
       "tcpEStatsListenerInitial": tcpEStatsListenerInitial,
       "tcpEStatsListenerEstablished": tcpEStatsListenerEstablished,
       "tcpEStatsListenerAccepted": tcpEStatsListenerAccepted,
       "tcpEStatsListenerExceedBacklog": tcpEStatsListenerExceedBacklog,
       "tcpEStatsListenerHCSynRcvd": tcpEStatsListenerHCSynRcvd,
       "tcpEStatsListenerHCInitial": tcpEStatsListenerHCInitial,
       "tcpEStatsListenerHCEstablished": tcpEStatsListenerHCEstablished,
       "tcpEStatsListenerHCAccepted": tcpEStatsListenerHCAccepted,
       "tcpEStatsListenerHCExceedBacklog": tcpEStatsListenerHCExceedBacklog,
       "tcpEStatsListenerCurConns": tcpEStatsListenerCurConns,
       "tcpEStatsListenerMaxBacklog": tcpEStatsListenerMaxBacklog,
       "tcpEStatsListenerCurBacklog": tcpEStatsListenerCurBacklog,
       "tcpEStatsListenerCurEstabBacklog": tcpEStatsListenerCurEstabBacklog,
       "tcpEStatsConnectIdTable": tcpEStatsConnectIdTable,
       "tcpEStatsConnectIdEntry": tcpEStatsConnectIdEntry,
       "tcpEStatsConnectIndex": tcpEStatsConnectIndex,
       "tcpEStatsPerfTable": tcpEStatsPerfTable,
       "tcpEStatsPerfEntry": tcpEStatsPerfEntry,
       "tcpEStatsPerfSegsOut": tcpEStatsPerfSegsOut,
       "tcpEStatsPerfDataSegsOut": tcpEStatsPerfDataSegsOut,
       "tcpEStatsPerfDataOctetsOut": tcpEStatsPerfDataOctetsOut,
       "tcpEStatsPerfHCDataOctetsOut": tcpEStatsPerfHCDataOctetsOut,
       "tcpEStatsPerfSegsRetrans": tcpEStatsPerfSegsRetrans,
       "tcpEStatsPerfOctetsRetrans": tcpEStatsPerfOctetsRetrans,
       "tcpEStatsPerfSegsIn": tcpEStatsPerfSegsIn,
       "tcpEStatsPerfDataSegsIn": tcpEStatsPerfDataSegsIn,
       "tcpEStatsPerfDataOctetsIn": tcpEStatsPerfDataOctetsIn,
       "tcpEStatsPerfHCDataOctetsIn": tcpEStatsPerfHCDataOctetsIn,
       "tcpEStatsPerfElapsedSecs": tcpEStatsPerfElapsedSecs,
       "tcpEStatsPerfElapsedMicroSecs": tcpEStatsPerfElapsedMicroSecs,
       "tcpEStatsPerfStartTimeStamp": tcpEStatsPerfStartTimeStamp,
       "tcpEStatsPerfCurMSS": tcpEStatsPerfCurMSS,
       "tcpEStatsPerfPipeSize": tcpEStatsPerfPipeSize,
       "tcpEStatsPerfMaxPipeSize": tcpEStatsPerfMaxPipeSize,
       "tcpEStatsPerfSmoothedRTT": tcpEStatsPerfSmoothedRTT,
       "tcpEStatsPerfCurRTO": tcpEStatsPerfCurRTO,
       "tcpEStatsPerfCongSignals": tcpEStatsPerfCongSignals,
       "tcpEStatsPerfCurCwnd": tcpEStatsPerfCurCwnd,
       "tcpEStatsPerfCurSsthresh": tcpEStatsPerfCurSsthresh,
       "tcpEStatsPerfTimeouts": tcpEStatsPerfTimeouts,
       "tcpEStatsPerfCurRwinSent": tcpEStatsPerfCurRwinSent,
       "tcpEStatsPerfMaxRwinSent": tcpEStatsPerfMaxRwinSent,
       "tcpEStatsPerfZeroRwinSent": tcpEStatsPerfZeroRwinSent,
       "tcpEStatsPerfCurRwinRcvd": tcpEStatsPerfCurRwinRcvd,
       "tcpEStatsPerfMaxRwinRcvd": tcpEStatsPerfMaxRwinRcvd,
       "tcpEStatsPerfZeroRwinRcvd": tcpEStatsPerfZeroRwinRcvd,
       "tcpEStatsPerfSndLimTransRwin": tcpEStatsPerfSndLimTransRwin,
       "tcpEStatsPerfSndLimTransCwnd": tcpEStatsPerfSndLimTransCwnd,
       "tcpEStatsPerfSndLimTransSnd": tcpEStatsPerfSndLimTransSnd,
       "tcpEStatsPerfSndLimTimeRwin": tcpEStatsPerfSndLimTimeRwin,
       "tcpEStatsPerfSndLimTimeCwnd": tcpEStatsPerfSndLimTimeCwnd,
       "tcpEStatsPerfSndLimTimeSnd": tcpEStatsPerfSndLimTimeSnd,
       "tcpEStatsPathTable": tcpEStatsPathTable,
       "tcpEStatsPathEntry": tcpEStatsPathEntry,
       "tcpEStatsPathRetranThresh": tcpEStatsPathRetranThresh,
       "tcpEStatsPathNonRecovDAEpisodes": tcpEStatsPathNonRecovDAEpisodes,
       "tcpEStatsPathSumOctetsReordered": tcpEStatsPathSumOctetsReordered,
       "tcpEStatsPathNonRecovDA": tcpEStatsPathNonRecovDA,
       "tcpEStatsPathSampleRTT": tcpEStatsPathSampleRTT,
       "tcpEStatsPathRTTVar": tcpEStatsPathRTTVar,
       "tcpEStatsPathMaxRTT": tcpEStatsPathMaxRTT,
       "tcpEStatsPathMinRTT": tcpEStatsPathMinRTT,
       "tcpEStatsPathSumRTT": tcpEStatsPathSumRTT,
       "tcpEStatsPathHCSumRTT": tcpEStatsPathHCSumRTT,
       "tcpEStatsPathCountRTT": tcpEStatsPathCountRTT,
       "tcpEStatsPathMaxRTO": tcpEStatsPathMaxRTO,
       "tcpEStatsPathMinRTO": tcpEStatsPathMinRTO,
       "tcpEStatsPathIpTtl": tcpEStatsPathIpTtl,
       "tcpEStatsPathIpTosIn": tcpEStatsPathIpTosIn,
       "tcpEStatsPathIpTosOut": tcpEStatsPathIpTosOut,
       "tcpEStatsPathPreCongSumCwnd": tcpEStatsPathPreCongSumCwnd,
       "tcpEStatsPathPreCongSumRTT": tcpEStatsPathPreCongSumRTT,
       "tcpEStatsPathPostCongSumRTT": tcpEStatsPathPostCongSumRTT,
       "tcpEStatsPathPostCongCountRTT": tcpEStatsPathPostCongCountRTT,
       "tcpEStatsPathECNsignals": tcpEStatsPathECNsignals,
       "tcpEStatsPathDupAckEpisodes": tcpEStatsPathDupAckEpisodes,
       "tcpEStatsPathRcvRTT": tcpEStatsPathRcvRTT,
       "tcpEStatsPathDupAcksOut": tcpEStatsPathDupAcksOut,
       "tcpEStatsPathCERcvd": tcpEStatsPathCERcvd,
       "tcpEStatsPathECESent": tcpEStatsPathECESent,
       "tcpEStatsStackTable": tcpEStatsStackTable,
       "tcpEStatsStackEntry": tcpEStatsStackEntry,
       "tcpEStatsStackActiveOpen": tcpEStatsStackActiveOpen,
       "tcpEStatsStackMSSSent": tcpEStatsStackMSSSent,
       "tcpEStatsStackMSSRcvd": tcpEStatsStackMSSRcvd,
       "tcpEStatsStackWinScaleSent": tcpEStatsStackWinScaleSent,
       "tcpEStatsStackWinScaleRcvd": tcpEStatsStackWinScaleRcvd,
       "tcpEStatsStackTimeStamps": tcpEStatsStackTimeStamps,
       "tcpEStatsStackECN": tcpEStatsStackECN,
       "tcpEStatsStackWillSendSACK": tcpEStatsStackWillSendSACK,
       "tcpEStatsStackWillUseSACK": tcpEStatsStackWillUseSACK,
       "tcpEStatsStackState": tcpEStatsStackState,
       "tcpEStatsStackNagle": tcpEStatsStackNagle,
       "tcpEStatsStackMaxSsCwnd": tcpEStatsStackMaxSsCwnd,
       "tcpEStatsStackMaxCaCwnd": tcpEStatsStackMaxCaCwnd,
       "tcpEStatsStackMaxSsthresh": tcpEStatsStackMaxSsthresh,
       "tcpEStatsStackMinSsthresh": tcpEStatsStackMinSsthresh,
       "tcpEStatsStackInRecovery": tcpEStatsStackInRecovery,
       "tcpEStatsStackDupAcksIn": tcpEStatsStackDupAcksIn,
       "tcpEStatsStackSpuriousFrDetected": tcpEStatsStackSpuriousFrDetected,
       "tcpEStatsStackSpuriousRtoDetected": tcpEStatsStackSpuriousRtoDetected,
       "tcpEStatsStackSoftErrors": tcpEStatsStackSoftErrors,
       "tcpEStatsStackSoftErrorReason": tcpEStatsStackSoftErrorReason,
       "tcpEStatsStackSlowStart": tcpEStatsStackSlowStart,
       "tcpEStatsStackCongAvoid": tcpEStatsStackCongAvoid,
       "tcpEStatsStackOtherReductions": tcpEStatsStackOtherReductions,
       "tcpEStatsStackCongOverCount": tcpEStatsStackCongOverCount,
       "tcpEStatsStackFastRetran": tcpEStatsStackFastRetran,
       "tcpEStatsStackSubsequentTimeouts": tcpEStatsStackSubsequentTimeouts,
       "tcpEStatsStackCurTimeoutCount": tcpEStatsStackCurTimeoutCount,
       "tcpEStatsStackAbruptTimeouts": tcpEStatsStackAbruptTimeouts,
       "tcpEStatsStackSACKsRcvd": tcpEStatsStackSACKsRcvd,
       "tcpEStatsStackSACKBlocksRcvd": tcpEStatsStackSACKBlocksRcvd,
       "tcpEStatsStackSendStall": tcpEStatsStackSendStall,
       "tcpEStatsStackDSACKDups": tcpEStatsStackDSACKDups,
       "tcpEStatsStackMaxMSS": tcpEStatsStackMaxMSS,
       "tcpEStatsStackMinMSS": tcpEStatsStackMinMSS,
       "tcpEStatsStackSndInitial": tcpEStatsStackSndInitial,
       "tcpEStatsStackRecInitial": tcpEStatsStackRecInitial,
       "tcpEStatsStackCurRetxQueue": tcpEStatsStackCurRetxQueue,
       "tcpEStatsStackMaxRetxQueue": tcpEStatsStackMaxRetxQueue,
       "tcpEStatsStackCurReasmQueue": tcpEStatsStackCurReasmQueue,
       "tcpEStatsStackMaxReasmQueue": tcpEStatsStackMaxReasmQueue,
       "tcpEStatsAppTable": tcpEStatsAppTable,
       "tcpEStatsAppEntry": tcpEStatsAppEntry,
       "tcpEStatsAppSndUna": tcpEStatsAppSndUna,
       "tcpEStatsAppSndNxt": tcpEStatsAppSndNxt,
       "tcpEStatsAppSndMax": tcpEStatsAppSndMax,
       "tcpEStatsAppThruOctetsAcked": tcpEStatsAppThruOctetsAcked,
       "tcpEStatsAppHCThruOctetsAcked": tcpEStatsAppHCThruOctetsAcked,
       "tcpEStatsAppRcvNxt": tcpEStatsAppRcvNxt,
       "tcpEStatsAppThruOctetsReceived": tcpEStatsAppThruOctetsReceived,
       "tcpEStatsAppHCThruOctetsReceived": tcpEStatsAppHCThruOctetsReceived,
       "tcpEStatsAppCurAppWQueue": tcpEStatsAppCurAppWQueue,
       "tcpEStatsAppMaxAppWQueue": tcpEStatsAppMaxAppWQueue,
       "tcpEStatsAppCurAppRQueue": tcpEStatsAppCurAppRQueue,
       "tcpEStatsAppMaxAppRQueue": tcpEStatsAppMaxAppRQueue,
       "tcpEStatsTuneTable": tcpEStatsTuneTable,
       "tcpEStatsTuneEntry": tcpEStatsTuneEntry,
       "tcpEStatsTuneLimCwnd": tcpEStatsTuneLimCwnd,
       "tcpEStatsTuneLimSsthresh": tcpEStatsTuneLimSsthresh,
       "tcpEStatsTuneLimRwin": tcpEStatsTuneLimRwin,
       "tcpEStatsTuneLimMSS": tcpEStatsTuneLimMSS,
       "tcpEStatsControl": tcpEStatsControl,
       "tcpEStatsControlPath": tcpEStatsControlPath,
       "tcpEStatsControlStack": tcpEStatsControlStack,
       "tcpEStatsControlApp": tcpEStatsControlApp,
       "tcpEStatsControlTune": tcpEStatsControlTune,
       "tcpEStatsControlNotify": tcpEStatsControlNotify,
       "tcpEStatsConnTableLatency": tcpEStatsConnTableLatency,
       "tcpEStatsScalar": tcpEStatsScalar,
       "tcpEStatsListenerTableLastChange": tcpEStatsListenerTableLastChange,
       "tcpEStatsConformance": tcpEStatsConformance,
       "tcpEStatsCompliances": tcpEStatsCompliances,
       "tcpEStatsCompliance": tcpEStatsCompliance,
       "tcpEStatsGroups": tcpEStatsGroups,
       "tcpEStatsListenerGroup": tcpEStatsListenerGroup,
       "tcpEStatsListenerHCGroup": tcpEStatsListenerHCGroup,
       "tcpEStatsConnectIdGroup": tcpEStatsConnectIdGroup,
       "tcpEStatsPerfGroup": tcpEStatsPerfGroup,
       "tcpEStatsPerfOptionalGroup": tcpEStatsPerfOptionalGroup,
       "tcpEStatsPerfHCGroup": tcpEStatsPerfHCGroup,
       "tcpEStatsPathGroup": tcpEStatsPathGroup,
       "tcpEStatsPathOptionalGroup": tcpEStatsPathOptionalGroup,
       "tcpEStatsPathHCGroup": tcpEStatsPathHCGroup,
       "tcpEStatsStackGroup": tcpEStatsStackGroup,
       "tcpEStatsStackOptionalGroup": tcpEStatsStackOptionalGroup,
       "tcpEStatsAppGroup": tcpEStatsAppGroup,
       "tcpEStatsAppHCGroup": tcpEStatsAppHCGroup,
       "tcpEStatsAppOptionalGroup": tcpEStatsAppOptionalGroup,
       "tcpEStatsTuneOptionalGroup": tcpEStatsTuneOptionalGroup,
       "tcpEStatsNotificationsGroup": tcpEStatsNotificationsGroup,
       "tcpEStatsNotificationsCtlGroup": tcpEStatsNotificationsCtlGroup}
)
