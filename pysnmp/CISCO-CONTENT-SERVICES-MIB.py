# SNMP MIB module (CISCO-CONTENT-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CONTENT-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:46 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(MplsVpnId,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnId")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoContentServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597)
)
ciscoContentServicesMIB.setRevisions(
        ("2012-11-09 00:00",
         "2012-04-27 00:00",
         "2012-02-13 00:00",
         "2011-02-05 00:00",
         "2010-01-28 00:00",
         "2009-08-12 00:00",
         "2009-01-28 00:00",
         "2008-09-26 00:00",
         "2008-04-21 00:00",
         "2007-03-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcsServerPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoContentServicesMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoContentServicesMIBNotifs = _CiscoContentServicesMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0)
)
_CiscoContentServicesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoContentServicesMIBObjects = _CiscoContentServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1)
)
_CcsConfig_ObjectIdentity = ObjectIdentity
ccsConfig = _CcsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1)
)
_CcsGlobalCfgTable_Object = MibTable
ccsGlobalCfgTable = _CcsGlobalCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccsGlobalCfgTable.setStatus("current")
_CcsGlobalCfgTableEntry_Object = MibTableRow
ccsGlobalCfgTableEntry = _CcsGlobalCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1)
)
ccsGlobalCfgTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsGlobalCfgTableEntry.setStatus("current")


class _CcsgcBMALostRecordTimer_Type(TimeInterval):
    """Custom type ccsgcBMALostRecordTimer based on TimeInterval"""
    defaultValue = 60


_CcsgcBMALostRecordTimer_Object = MibTableColumn
ccsgcBMALostRecordTimer = _CcsgcBMALostRecordTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 2),
    _CcsgcBMALostRecordTimer_Type()
)
ccsgcBMALostRecordTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgcBMALostRecordTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccsgcBMALostRecordTimer.setUnits("seconds")


class _CcsgcQuotaMgrLostRecordTimer_Type(TimeInterval):
    """Custom type ccsgcQuotaMgrLostRecordTimer based on TimeInterval"""
    defaultValue = 60


_CcsgcQuotaMgrLostRecordTimer_Object = MibTableColumn
ccsgcQuotaMgrLostRecordTimer = _CcsgcQuotaMgrLostRecordTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 3),
    _CcsgcQuotaMgrLostRecordTimer_Type()
)
ccsgcQuotaMgrLostRecordTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgcQuotaMgrLostRecordTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccsgcQuotaMgrLostRecordTimer.setUnits("seconds")
_CcsgsUserThreshold_Type = Unsigned32
_CcsgsUserThreshold_Object = MibTableColumn
ccsgsUserThreshold = _CcsgsUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 4),
    _CcsgsUserThreshold_Type()
)
ccsgsUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsUserThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsUserThreshold.setUnits("users")


class _CcsAdControlAlarmUpdateTimer_Type(TimeInterval):
    """Custom type ccsAdControlAlarmUpdateTimer based on TimeInterval"""
    defaultValue = 300

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcsAdControlAlarmUpdateTimer_Type.__name__ = "TimeInterval"
_CcsAdControlAlarmUpdateTimer_Object = MibTableColumn
ccsAdControlAlarmUpdateTimer = _CcsAdControlAlarmUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 5),
    _CcsAdControlAlarmUpdateTimer_Type()
)
ccsAdControlAlarmUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsAdControlAlarmUpdateTimer.setStatus("current")
if mibBuilder.loadTexts:
    ccsAdControlAlarmUpdateTimer.setUnits("seconds")


class _CcsNetServerResponseFailAlarmThreshold_Type(Unsigned32):
    """Custom type ccsNetServerResponseFailAlarmThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_CcsNetServerResponseFailAlarmThreshold_Type.__name__ = "Unsigned32"
_CcsNetServerResponseFailAlarmThreshold_Object = MibTableColumn
ccsNetServerResponseFailAlarmThreshold = _CcsNetServerResponseFailAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 6),
    _CcsNetServerResponseFailAlarmThreshold_Type()
)
ccsNetServerResponseFailAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsNetServerResponseFailAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsNetServerResponseFailAlarmThreshold.setUnits("errors")


class _CcsNetServerResponseFailClearThreshold_Type(Unsigned32):
    """Custom type ccsNetServerResponseFailClearThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_CcsNetServerResponseFailClearThreshold_Type.__name__ = "Unsigned32"
_CcsNetServerResponseFailClearThreshold_Object = MibTableColumn
ccsNetServerResponseFailClearThreshold = _CcsNetServerResponseFailClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 7),
    _CcsNetServerResponseFailClearThreshold_Type()
)
ccsNetServerResponseFailClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsNetServerResponseFailClearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsNetServerResponseFailClearThreshold.setUnits("errors")


class _CcsNetServerFirstPayloadResponseTime_Type(TimeInterval):
    """Custom type ccsNetServerFirstPayloadResponseTime based on TimeInterval"""
    defaultValue = 5

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcsNetServerFirstPayloadResponseTime_Type.__name__ = "TimeInterval"
_CcsNetServerFirstPayloadResponseTime_Object = MibTableColumn
ccsNetServerFirstPayloadResponseTime = _CcsNetServerFirstPayloadResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 8),
    _CcsNetServerFirstPayloadResponseTime_Type()
)
ccsNetServerFirstPayloadResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsNetServerFirstPayloadResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    ccsNetServerFirstPayloadResponseTime.setUnits("seconds")


class _CcsNetServerResponseTimeFailAlarmThreshold_Type(Unsigned32):
    """Custom type ccsNetServerResponseTimeFailAlarmThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_CcsNetServerResponseTimeFailAlarmThreshold_Type.__name__ = "Unsigned32"
_CcsNetServerResponseTimeFailAlarmThreshold_Object = MibTableColumn
ccsNetServerResponseTimeFailAlarmThreshold = _CcsNetServerResponseTimeFailAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 9),
    _CcsNetServerResponseTimeFailAlarmThreshold_Type()
)
ccsNetServerResponseTimeFailAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsNetServerResponseTimeFailAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsNetServerResponseTimeFailAlarmThreshold.setUnits("errors")


class _CcsNetServerResponseTimeFailClearThreshold_Type(Unsigned32):
    """Custom type ccsNetServerResponseTimeFailClearThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_CcsNetServerResponseTimeFailClearThreshold_Type.__name__ = "Unsigned32"
_CcsNetServerResponseTimeFailClearThreshold_Object = MibTableColumn
ccsNetServerResponseTimeFailClearThreshold = _CcsNetServerResponseTimeFailClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 10),
    _CcsNetServerResponseTimeFailClearThreshold_Type()
)
ccsNetServerResponseTimeFailClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsNetServerResponseTimeFailClearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsNetServerResponseTimeFailClearThreshold.setUnits("errors")


class _CcsProtocolParseFailAlarmThreshold_Type(Unsigned32):
    """Custom type ccsProtocolParseFailAlarmThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_CcsProtocolParseFailAlarmThreshold_Type.__name__ = "Unsigned32"
_CcsProtocolParseFailAlarmThreshold_Object = MibTableColumn
ccsProtocolParseFailAlarmThreshold = _CcsProtocolParseFailAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 11),
    _CcsProtocolParseFailAlarmThreshold_Type()
)
ccsProtocolParseFailAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsProtocolParseFailAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsProtocolParseFailAlarmThreshold.setUnits("errors")


class _CcsProtocolParseFailClearThreshold_Type(Unsigned32):
    """Custom type ccsProtocolParseFailClearThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967293),
    )


_CcsProtocolParseFailClearThreshold_Type.__name__ = "Unsigned32"
_CcsProtocolParseFailClearThreshold_Object = MibTableColumn
ccsProtocolParseFailClearThreshold = _CcsProtocolParseFailClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 12),
    _CcsProtocolParseFailClearThreshold_Type()
)
ccsProtocolParseFailClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsProtocolParseFailClearThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ccsProtocolParseFailClearThreshold.setUnits("errors")


class _CcsgsUserEntriesThreshold_Type(Unsigned32):
    """Custom type ccsgsUserEntriesThreshold based on Unsigned32"""
    defaultValue = 300000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_CcsgsUserEntriesThreshold_Type.__name__ = "Unsigned32"
_CcsgsUserEntriesThreshold_Object = MibTableColumn
ccsgsUserEntriesThreshold = _CcsgsUserEntriesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 13),
    _CcsgsUserEntriesThreshold_Type()
)
ccsgsUserEntriesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsUserEntriesThreshold.setStatus("current")


class _CcsgsSessionThreshold_Type(Unsigned32):
    """Custom type ccsgsSessionThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_CcsgsSessionThreshold_Type.__name__ = "Unsigned32"
_CcsgsSessionThreshold_Object = MibTableColumn
ccsgsSessionThreshold = _CcsgsSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 1, 1, 1, 14),
    _CcsgsSessionThreshold_Type()
)
ccsgsSessionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsSessionThreshold.setStatus("current")
_CcsStats_ObjectIdentity = ObjectIdentity
ccsStats = _CcsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2)
)
_CcsGlobalStatsTable_Object = MibTable
ccsGlobalStatsTable = _CcsGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccsGlobalStatsTable.setStatus("current")
_CcsGlobalStatsTableEntry_Object = MibTableRow
ccsGlobalStatsTableEntry = _CcsGlobalStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1)
)
ccsGlobalStatsTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsGlobalStatsTableEntry.setStatus("current")
_CcsgsUserCurrent_Type = Gauge32
_CcsgsUserCurrent_Object = MibTableColumn
ccsgsUserCurrent = _CcsgsUserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 1),
    _CcsgsUserCurrent_Type()
)
ccsgsUserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsUserCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsUserCurrent.setUnits("users")
_CcsgsUserHighWater_Type = Gauge32
_CcsgsUserHighWater_Object = MibTableColumn
ccsgsUserHighWater = _CcsgsUserHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 2),
    _CcsgsUserHighWater_Type()
)
ccsgsUserHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsUserHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsUserHighWater.setUnits("users")
_CcsgsUserHighWaterResetTime_Type = TimeStamp
_CcsgsUserHighWaterResetTime_Object = MibTableColumn
ccsgsUserHighWaterResetTime = _CcsgsUserHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 3),
    _CcsgsUserHighWaterResetTime_Type()
)
ccsgsUserHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsUserHighWaterResetTime.setStatus("current")
_CcsgsSessionCurrent_Type = Gauge32
_CcsgsSessionCurrent_Object = MibTableColumn
ccsgsSessionCurrent = _CcsgsSessionCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 4),
    _CcsgsSessionCurrent_Type()
)
ccsgsSessionCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsSessionCurrent.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsSessionCurrent.setUnits("sessions")
_CcsgsSessionHighWater_Type = Gauge32
_CcsgsSessionHighWater_Object = MibTableColumn
ccsgsSessionHighWater = _CcsgsSessionHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 5),
    _CcsgsSessionHighWater_Type()
)
ccsgsSessionHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsSessionHighWater.setStatus("current")
_CcsgsSessionHighWaterResetTime_Type = TimeStamp
_CcsgsSessionHighWaterResetTime_Object = MibTableColumn
ccsgsSessionHighWaterResetTime = _CcsgsSessionHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 6),
    _CcsgsSessionHighWaterResetTime_Type()
)
ccsgsSessionHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsSessionHighWaterResetTime.setStatus("current")
_CcsgsGTPBMARejected_Type = Counter32
_CcsgsGTPBMARejected_Object = MibTableColumn
ccsgsGTPBMARejected = _CcsgsGTPBMARejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 7),
    _CcsgsGTPBMARejected_Type()
)
ccsgsGTPBMARejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPBMARejected.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPBMARejected.setUnits("messages")
_CcsgsHCGTPBMARejected_Type = Counter64
_CcsgsHCGTPBMARejected_Object = MibTableColumn
ccsgsHCGTPBMARejected = _CcsgsHCGTPBMARejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 8),
    _CcsgsHCGTPBMARejected_Type()
)
ccsgsHCGTPBMARejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMARejected.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMARejected.setUnits("messages")
_CcsgsGTPBMADropped_Type = Counter32
_CcsgsGTPBMADropped_Object = MibTableColumn
ccsgsGTPBMADropped = _CcsgsGTPBMADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 9),
    _CcsgsGTPBMADropped_Type()
)
ccsgsGTPBMADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPBMADropped.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPBMADropped.setUnits("messages")
_CcsgsHCGTPBMADropped_Type = Counter64
_CcsgsHCGTPBMADropped_Object = MibTableColumn
ccsgsHCGTPBMADropped = _CcsgsHCGTPBMADropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 10),
    _CcsgsHCGTPBMADropped_Type()
)
ccsgsHCGTPBMADropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMADropped.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMADropped.setUnits("messages")
_CcsgsGTPBMARetransmit_Type = Counter32
_CcsgsGTPBMARetransmit_Object = MibTableColumn
ccsgsGTPBMARetransmit = _CcsgsGTPBMARetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 11),
    _CcsgsGTPBMARetransmit_Type()
)
ccsgsGTPBMARetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPBMARetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPBMARetransmit.setUnits("messages")
_CcsgsHCGTPBMARetransmit_Type = Counter64
_CcsgsHCGTPBMARetransmit_Object = MibTableColumn
ccsgsHCGTPBMARetransmit = _CcsgsHCGTPBMARetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 12),
    _CcsgsHCGTPBMARetransmit_Type()
)
ccsgsHCGTPBMARetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMARetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPBMARetransmit.setUnits("messages")
_CcsgsGTPQuotaMgrRejected_Type = Counter32
_CcsgsGTPQuotaMgrRejected_Object = MibTableColumn
ccsgsGTPQuotaMgrRejected = _CcsgsGTPQuotaMgrRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 13),
    _CcsgsGTPQuotaMgrRejected_Type()
)
ccsgsGTPQuotaMgrRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRejected.setUnits("messages")
_CcsgsHCGTPQuotaMgrRejected_Type = Counter64
_CcsgsHCGTPQuotaMgrRejected_Object = MibTableColumn
ccsgsHCGTPQuotaMgrRejected = _CcsgsHCGTPQuotaMgrRejected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 14),
    _CcsgsHCGTPQuotaMgrRejected_Type()
)
ccsgsHCGTPQuotaMgrRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrRejected.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrRejected.setUnits("messages")
_CcsgsGTPQuotaMgrDropped_Type = Counter32
_CcsgsGTPQuotaMgrDropped_Object = MibTableColumn
ccsgsGTPQuotaMgrDropped = _CcsgsGTPQuotaMgrDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 15),
    _CcsgsGTPQuotaMgrDropped_Type()
)
ccsgsGTPQuotaMgrDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrDropped.setUnits("messages")
_CcsgsHCGTPQuotaMgrDropped_Type = Counter64
_CcsgsHCGTPQuotaMgrDropped_Object = MibTableColumn
ccsgsHCGTPQuotaMgrDropped = _CcsgsHCGTPQuotaMgrDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 16),
    _CcsgsHCGTPQuotaMgrDropped_Type()
)
ccsgsHCGTPQuotaMgrDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrDropped.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrDropped.setUnits("messages")
_CcsgsGTPQuotaMgrRetransmit_Type = Counter32
_CcsgsGTPQuotaMgrRetransmit_Object = MibTableColumn
ccsgsGTPQuotaMgrRetransmit = _CcsgsGTPQuotaMgrRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 17),
    _CcsgsGTPQuotaMgrRetransmit_Type()
)
ccsgsGTPQuotaMgrRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRetransmit.setUnits("messages")
_CcsgsHCGTPQuotaMgrRetransmit_Type = Counter64
_CcsgsHCGTPQuotaMgrRetransmit_Object = MibTableColumn
ccsgsHCGTPQuotaMgrRetransmit = _CcsgsHCGTPQuotaMgrRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 18),
    _CcsgsHCGTPQuotaMgrRetransmit_Type()
)
ccsgsHCGTPQuotaMgrRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHCGTPQuotaMgrRetransmit.setUnits("messages")


class _CcsgsGTPBMARateInterval_Type(TimeInterval):
    """Custom type ccsgsGTPBMARateInterval based on TimeInterval"""
    defaultValue = 2


_CcsgsGTPBMARateInterval_Object = MibTableColumn
ccsgsGTPBMARateInterval = _CcsgsGTPBMARateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 19),
    _CcsgsGTPBMARateInterval_Type()
)
ccsgsGTPBMARateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsGTPBMARateInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPBMARateInterval.setUnits("seconds")


class _CcsgsGTPQuotaMgrRateInterval_Type(TimeInterval):
    """Custom type ccsgsGTPQuotaMgrRateInterval based on TimeInterval"""
    defaultValue = 2


_CcsgsGTPQuotaMgrRateInterval_Object = MibTableColumn
ccsgsGTPQuotaMgrRateInterval = _CcsgsGTPQuotaMgrRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 20),
    _CcsgsGTPQuotaMgrRateInterval_Type()
)
ccsgsGTPQuotaMgrRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGTPQuotaMgrRateInterval.setUnits("seconds")
_CcsgsGxRuleActivationFail_Type = Counter32
_CcsgsGxRuleActivationFail_Object = MibTableColumn
ccsgsGxRuleActivationFail = _CcsgsGxRuleActivationFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 21),
    _CcsgsGxRuleActivationFail_Type()
)
ccsgsGxRuleActivationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGxRuleActivationFail.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGxRuleActivationFail.setUnits("Gx Rule")
_CcsgsGxRuleDeactivationFail_Type = Counter32
_CcsgsGxRuleDeactivationFail_Object = MibTableColumn
ccsgsGxRuleDeactivationFail = _CcsgsGxRuleDeactivationFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 22),
    _CcsgsGxRuleDeactivationFail_Type()
)
ccsgsGxRuleDeactivationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGxRuleDeactivationFail.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGxRuleDeactivationFail.setUnits("Gx Rule")
_CcsgsGxRevalidationSuccess_Type = Counter32
_CcsgsGxRevalidationSuccess_Object = MibTableColumn
ccsgsGxRevalidationSuccess = _CcsgsGxRevalidationSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 23),
    _CcsgsGxRevalidationSuccess_Type()
)
ccsgsGxRevalidationSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGxRevalidationSuccess.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGxRevalidationSuccess.setUnits("messages")
_CcsgsGxRevalidationFail_Type = Counter32
_CcsgsGxRevalidationFail_Object = MibTableColumn
ccsgsGxRevalidationFail = _CcsgsGxRevalidationFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 24),
    _CcsgsGxRevalidationFail_Type()
)
ccsgsGxRevalidationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsGxRevalidationFail.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsGxRevalidationFail.setUnits("messages")
_CcsgsHTTPHdrObscure_Type = Counter64
_CcsgsHTTPHdrObscure_Object = MibTableColumn
ccsgsHTTPHdrObscure = _CcsgsHTTPHdrObscure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 25),
    _CcsgsHTTPHdrObscure_Type()
)
ccsgsHTTPHdrObscure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHTTPHdrObscure.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHTTPHdrObscure.setUnits("messages")
_CcsgsHTTPHdrBlock_Type = Counter64
_CcsgsHTTPHdrBlock_Object = MibTableColumn
ccsgsHTTPHdrBlock = _CcsgsHTTPHdrBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 1, 1, 26),
    _CcsgsHTTPHdrBlock_Type()
)
ccsgsHTTPHdrBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsgsHTTPHdrBlock.setStatus("current")
if mibBuilder.loadTexts:
    ccsgsHTTPHdrBlock.setUnits("messages")
_CcsUserDbTable_Object = MibTable
ccsUserDbTable = _CcsUserDbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccsUserDbTable.setStatus("current")
_CcsUserDbTableEntry_Object = MibTableRow
ccsUserDbTableEntry = _CcsUserDbTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1)
)
ccsUserDbTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsUserDbVrfName"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsUserDbIpAddrType"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsUserDbIpAddr"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsUserDbPort"),
)
if mibBuilder.loadTexts:
    ccsUserDbTableEntry.setStatus("current")
_CcsUserDbVrfName_Type = MplsVpnId
_CcsUserDbVrfName_Object = MibTableColumn
ccsUserDbVrfName = _CcsUserDbVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 1),
    _CcsUserDbVrfName_Type()
)
ccsUserDbVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsUserDbVrfName.setStatus("current")
_CcsUserDbIpAddrType_Type = InetAddressType
_CcsUserDbIpAddrType_Object = MibTableColumn
ccsUserDbIpAddrType = _CcsUserDbIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 2),
    _CcsUserDbIpAddrType_Type()
)
ccsUserDbIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsUserDbIpAddrType.setStatus("current")
_CcsUserDbIpAddr_Type = InetAddress
_CcsUserDbIpAddr_Object = MibTableColumn
ccsUserDbIpAddr = _CcsUserDbIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 3),
    _CcsUserDbIpAddr_Type()
)
ccsUserDbIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsUserDbIpAddr.setStatus("current")
_CcsUserDbPort_Type = InetPortNumber
_CcsUserDbPort_Object = MibTableColumn
ccsUserDbPort = _CcsUserDbPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 4),
    _CcsUserDbPort_Type()
)
ccsUserDbPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsUserDbPort.setStatus("current")


class _CcsUserDbState_Type(Integer32):
    """Custom type ccsUserDbState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failed", 3),
          ("reset", 1))
    )


_CcsUserDbState_Type.__name__ = "Integer32"
_CcsUserDbState_Object = MibTableColumn
ccsUserDbState = _CcsUserDbState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 5),
    _CcsUserDbState_Type()
)
ccsUserDbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbState.setStatus("current")
_CcsUserDbRequests_Type = Counter32
_CcsUserDbRequests_Object = MibTableColumn
ccsUserDbRequests = _CcsUserDbRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 6),
    _CcsUserDbRequests_Type()
)
ccsUserDbRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbRequests.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbRequests.setUnits("requests")
_CcsUserDbHCRequests_Type = Counter64
_CcsUserDbHCRequests_Object = MibTableColumn
ccsUserDbHCRequests = _CcsUserDbHCRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 7),
    _CcsUserDbHCRequests_Type()
)
ccsUserDbHCRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbHCRequests.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbHCRequests.setUnits("requests")
_CcsUserDbUidsReturned_Type = Counter32
_CcsUserDbUidsReturned_Object = MibTableColumn
ccsUserDbUidsReturned = _CcsUserDbUidsReturned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 8),
    _CcsUserDbUidsReturned_Type()
)
ccsUserDbUidsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbUidsReturned.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbUidsReturned.setUnits("returned identifiers")
_CcsUserDbHCUidsReturned_Type = Counter64
_CcsUserDbHCUidsReturned_Object = MibTableColumn
ccsUserDbHCUidsReturned = _CcsUserDbHCUidsReturned_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 9),
    _CcsUserDbHCUidsReturned_Type()
)
ccsUserDbHCUidsReturned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbHCUidsReturned.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbHCUidsReturned.setUnits("returned identifiers")
_CcsUserDbReqResent_Type = Counter32
_CcsUserDbReqResent_Object = MibTableColumn
ccsUserDbReqResent = _CcsUserDbReqResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 10),
    _CcsUserDbReqResent_Type()
)
ccsUserDbReqResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbReqResent.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbReqResent.setUnits("requests")
_CcsUserDbHCReqResent_Type = Counter64
_CcsUserDbHCReqResent_Object = MibTableColumn
ccsUserDbHCReqResent = _CcsUserDbHCReqResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 11),
    _CcsUserDbHCReqResent_Type()
)
ccsUserDbHCReqResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbHCReqResent.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbHCReqResent.setUnits("requests")
_CcsUserDbReqTimeouts_Type = Counter32
_CcsUserDbReqTimeouts_Object = MibTableColumn
ccsUserDbReqTimeouts = _CcsUserDbReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 12),
    _CcsUserDbReqTimeouts_Type()
)
ccsUserDbReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbReqTimeouts.setUnits("timeouts")
_CcsUserDbHCReqTimeouts_Type = Counter64
_CcsUserDbHCReqTimeouts_Object = MibTableColumn
ccsUserDbHCReqTimeouts = _CcsUserDbHCReqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 13),
    _CcsUserDbHCReqTimeouts_Type()
)
ccsUserDbHCReqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbHCReqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbHCReqTimeouts.setUnits("timeouts")
_CcsUserDbReqErrors_Type = Counter32
_CcsUserDbReqErrors_Object = MibTableColumn
ccsUserDbReqErrors = _CcsUserDbReqErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 14),
    _CcsUserDbReqErrors_Type()
)
ccsUserDbReqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbReqErrors.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbReqErrors.setUnits("errors")
_CcsUserDbHCReqErrors_Type = Counter64
_CcsUserDbHCReqErrors_Object = MibTableColumn
ccsUserDbHCReqErrors = _CcsUserDbHCReqErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 15),
    _CcsUserDbHCReqErrors_Type()
)
ccsUserDbHCReqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUserDbHCReqErrors.setStatus("current")
if mibBuilder.loadTexts:
    ccsUserDbHCReqErrors.setUnits("errors")
_CcsUserDbRowStatus_Type = RowStatus
_CcsUserDbRowStatus_Object = MibTableColumn
ccsUserDbRowStatus = _CcsUserDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 2, 1, 16),
    _CcsUserDbRowStatus_Type()
)
ccsUserDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsUserDbRowStatus.setStatus("current")
_CcsBMATable_Object = MibTable
ccsBMATable = _CcsBMATable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccsBMATable.setStatus("current")
_CcsBMATableEntry_Object = MibTableRow
ccsBMATableEntry = _CcsBMATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1)
)
ccsBMATableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsBMAVrfName"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsBMAIpAddrType"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsBMAIpAddr"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsBMAPort"),
)
if mibBuilder.loadTexts:
    ccsBMATableEntry.setStatus("current")
_CcsBMAVrfName_Type = MplsVpnId
_CcsBMAVrfName_Object = MibTableColumn
ccsBMAVrfName = _CcsBMAVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 1),
    _CcsBMAVrfName_Type()
)
ccsBMAVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsBMAVrfName.setStatus("current")
_CcsBMAIpAddrType_Type = InetAddressType
_CcsBMAIpAddrType_Object = MibTableColumn
ccsBMAIpAddrType = _CcsBMAIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 2),
    _CcsBMAIpAddrType_Type()
)
ccsBMAIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsBMAIpAddrType.setStatus("current")
_CcsBMAIpAddr_Type = InetAddress
_CcsBMAIpAddr_Object = MibTableColumn
ccsBMAIpAddr = _CcsBMAIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 3),
    _CcsBMAIpAddr_Type()
)
ccsBMAIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsBMAIpAddr.setStatus("current")
_CcsBMAPort_Type = InetPortNumber
_CcsBMAPort_Object = MibTableColumn
ccsBMAPort = _CcsBMAPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 4),
    _CcsBMAPort_Type()
)
ccsBMAPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsBMAPort.setStatus("current")
_CcsBMAPriority_Type = CcsServerPriority
_CcsBMAPriority_Object = MibTableColumn
ccsBMAPriority = _CcsBMAPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 5),
    _CcsBMAPriority_Type()
)
ccsBMAPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsBMAPriority.setStatus("current")


class _CcsBMAState_Type(Integer32):
    """Custom type ccsBMAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("echowait", 4),
          ("failed", 2),
          ("nawait", 5),
          ("standby", 1),
          ("suspended", 6))
    )


_CcsBMAState_Type.__name__ = "Integer32"
_CcsBMAState_Object = MibTableColumn
ccsBMAState = _CcsBMAState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 6),
    _CcsBMAState_Type()
)
ccsBMAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAState.setStatus("current")
_CcsBMALostRecords_Type = Counter32
_CcsBMALostRecords_Object = MibTableColumn
ccsBMALostRecords = _CcsBMALostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 7),
    _CcsBMALostRecords_Type()
)
ccsBMALostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMALostRecords.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMALostRecords.setUnits("records")
_CcsBMAHCLostRecords_Type = Counter64
_CcsBMAHCLostRecords_Object = MibTableColumn
ccsBMAHCLostRecords = _CcsBMAHCLostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 8),
    _CcsBMAHCLostRecords_Type()
)
ccsBMAHCLostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHCLostRecords.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHCLostRecords.setUnits("records")
_CcsBMATotalSent_Type = Counter32
_CcsBMATotalSent_Object = MibTableColumn
ccsBMATotalSent = _CcsBMATotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 9),
    _CcsBMATotalSent_Type()
)
ccsBMATotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMATotalSent.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMATotalSent.setUnits("records")
_CcsBMAHCTotalSent_Type = Counter64
_CcsBMAHCTotalSent_Object = MibTableColumn
ccsBMAHCTotalSent = _CcsBMAHCTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 10),
    _CcsBMAHCTotalSent_Type()
)
ccsBMAHCTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHCTotalSent.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHCTotalSent.setUnits("records")
_CcsBMAFailAck_Type = Counter32
_CcsBMAFailAck_Object = MibTableColumn
ccsBMAFailAck = _CcsBMAFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 11),
    _CcsBMAFailAck_Type()
)
ccsBMAFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAFailAck.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAFailAck.setUnits("acknowledgements")
_CcsBMAHCFailAck_Type = Counter64
_CcsBMAHCFailAck_Object = MibTableColumn
ccsBMAHCFailAck = _CcsBMAHCFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 12),
    _CcsBMAHCFailAck_Type()
)
ccsBMAHCFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHCFailAck.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHCFailAck.setUnits("acknowledgements")
_CcsBMAOutstanding_Type = Gauge32
_CcsBMAOutstanding_Object = MibTableColumn
ccsBMAOutstanding = _CcsBMAOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 13),
    _CcsBMAOutstanding_Type()
)
ccsBMAOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAOutstanding.setUnits("messages")
_CcsBMAHighWater_Type = Gauge32
_CcsBMAHighWater_Object = MibTableColumn
ccsBMAHighWater = _CcsBMAHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 14),
    _CcsBMAHighWater_Type()
)
ccsBMAHighWater.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsBMAHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHighWater.setUnits("messages")
_CcsBMAHighWaterResetTime_Type = TimeStamp
_CcsBMAHighWaterResetTime_Object = MibTableColumn
ccsBMAHighWaterResetTime = _CcsBMAHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 15),
    _CcsBMAHighWaterResetTime_Type()
)
ccsBMAHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHighWaterResetTime.setStatus("current")
_CcsBMABadRecord_Type = Counter32
_CcsBMABadRecord_Object = MibTableColumn
ccsBMABadRecord = _CcsBMABadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 16),
    _CcsBMABadRecord_Type()
)
ccsBMABadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMABadRecord.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMABadRecord.setUnits("records")
_CcsBMAHCBadRecord_Type = Counter64
_CcsBMAHCBadRecord_Object = MibTableColumn
ccsBMAHCBadRecord = _CcsBMAHCBadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 17),
    _CcsBMAHCBadRecord_Type()
)
ccsBMAHCBadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHCBadRecord.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHCBadRecord.setUnits("records")
_CcsBMARetransmit_Type = Counter32
_CcsBMARetransmit_Object = MibTableColumn
ccsBMARetransmit = _CcsBMARetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 18),
    _CcsBMARetransmit_Type()
)
ccsBMARetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMARetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMARetransmit.setUnits("messages")
_CcsBMAHCRetransmit_Type = Counter64
_CcsBMAHCRetransmit_Object = MibTableColumn
ccsBMAHCRetransmit = _CcsBMAHCRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 19),
    _CcsBMAHCRetransmit_Type()
)
ccsBMAHCRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAHCRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAHCRetransmit.setUnits("messages")
_CcsBMARowStatus_Type = RowStatus
_CcsBMARowStatus_Object = MibTableColumn
ccsBMARowStatus = _CcsBMARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 20),
    _CcsBMARowStatus_Type()
)
ccsBMARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsBMARowStatus.setStatus("current")
_CcsBMAPacketRate_Type = Gauge32
_CcsBMAPacketRate_Object = MibTableColumn
ccsBMAPacketRate = _CcsBMAPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 21),
    _CcsBMAPacketRate_Type()
)
ccsBMAPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAPacketRate.setUnits("packets")
_CcsBMAAckRate_Type = Gauge32
_CcsBMAAckRate_Object = MibTableColumn
ccsBMAAckRate = _CcsBMAAckRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 3, 1, 22),
    _CcsBMAAckRate_Type()
)
ccsBMAAckRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsBMAAckRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsBMAAckRate.setUnits("acknowledgments")
_CcsQuotaMgrTable_Object = MibTable
ccsQuotaMgrTable = _CcsQuotaMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ccsQuotaMgrTable.setStatus("current")
_CcsQuotaMgrTableEntry_Object = MibTableRow
ccsQuotaMgrTableEntry = _CcsQuotaMgrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1)
)
ccsQuotaMgrTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrVrfName"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrIpAddrType"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrIpAddr"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrPort"),
)
if mibBuilder.loadTexts:
    ccsQuotaMgrTableEntry.setStatus("current")
_CcsQuotaMgrVrfName_Type = MplsVpnId
_CcsQuotaMgrVrfName_Object = MibTableColumn
ccsQuotaMgrVrfName = _CcsQuotaMgrVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 1),
    _CcsQuotaMgrVrfName_Type()
)
ccsQuotaMgrVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsQuotaMgrVrfName.setStatus("current")
_CcsQuotaMgrIpAddrType_Type = InetAddressType
_CcsQuotaMgrIpAddrType_Object = MibTableColumn
ccsQuotaMgrIpAddrType = _CcsQuotaMgrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 2),
    _CcsQuotaMgrIpAddrType_Type()
)
ccsQuotaMgrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsQuotaMgrIpAddrType.setStatus("current")
_CcsQuotaMgrIpAddr_Type = InetAddress
_CcsQuotaMgrIpAddr_Object = MibTableColumn
ccsQuotaMgrIpAddr = _CcsQuotaMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 3),
    _CcsQuotaMgrIpAddr_Type()
)
ccsQuotaMgrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsQuotaMgrIpAddr.setStatus("current")
_CcsQuotaMgrPort_Type = InetPortNumber
_CcsQuotaMgrPort_Object = MibTableColumn
ccsQuotaMgrPort = _CcsQuotaMgrPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 4),
    _CcsQuotaMgrPort_Type()
)
ccsQuotaMgrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsQuotaMgrPort.setStatus("current")
_CcsQuotaMgrPriority_Type = CcsServerPriority
_CcsQuotaMgrPriority_Object = MibTableColumn
ccsQuotaMgrPriority = _CcsQuotaMgrPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 5),
    _CcsQuotaMgrPriority_Type()
)
ccsQuotaMgrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsQuotaMgrPriority.setStatus("current")


class _CcsQuotaMgrState_Type(Integer32):
    """Custom type ccsQuotaMgrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("echowait", 4),
          ("failed", 2),
          ("nawait", 5),
          ("standby", 1),
          ("suspended", 6))
    )


_CcsQuotaMgrState_Type.__name__ = "Integer32"
_CcsQuotaMgrState_Object = MibTableColumn
ccsQuotaMgrState = _CcsQuotaMgrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 6),
    _CcsQuotaMgrState_Type()
)
ccsQuotaMgrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrState.setStatus("current")
_CcsQuotaMgrLostRecords_Type = Counter32
_CcsQuotaMgrLostRecords_Object = MibTableColumn
ccsQuotaMgrLostRecords = _CcsQuotaMgrLostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 7),
    _CcsQuotaMgrLostRecords_Type()
)
ccsQuotaMgrLostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrLostRecords.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrLostRecords.setUnits("records")
_CcsQuotaMgrHCLostRecords_Type = Counter64
_CcsQuotaMgrHCLostRecords_Object = MibTableColumn
ccsQuotaMgrHCLostRecords = _CcsQuotaMgrHCLostRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 8),
    _CcsQuotaMgrHCLostRecords_Type()
)
ccsQuotaMgrHCLostRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCLostRecords.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCLostRecords.setUnits("records")
_CcsQuotaMgrTotalSent_Type = Counter32
_CcsQuotaMgrTotalSent_Object = MibTableColumn
ccsQuotaMgrTotalSent = _CcsQuotaMgrTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 9),
    _CcsQuotaMgrTotalSent_Type()
)
ccsQuotaMgrTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrTotalSent.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrTotalSent.setUnits("records")
_CcsQuotaMgrHCTotalSent_Type = Counter64
_CcsQuotaMgrHCTotalSent_Object = MibTableColumn
ccsQuotaMgrHCTotalSent = _CcsQuotaMgrHCTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 10),
    _CcsQuotaMgrHCTotalSent_Type()
)
ccsQuotaMgrHCTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCTotalSent.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCTotalSent.setUnits("records")
_CcsQuotaMgrFailAck_Type = Counter32
_CcsQuotaMgrFailAck_Object = MibTableColumn
ccsQuotaMgrFailAck = _CcsQuotaMgrFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 11),
    _CcsQuotaMgrFailAck_Type()
)
ccsQuotaMgrFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrFailAck.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrFailAck.setUnits("acknowledgements")
_CcsQuotaMgrHCFailAck_Type = Counter64
_CcsQuotaMgrHCFailAck_Object = MibTableColumn
ccsQuotaMgrHCFailAck = _CcsQuotaMgrHCFailAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 12),
    _CcsQuotaMgrHCFailAck_Type()
)
ccsQuotaMgrHCFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCFailAck.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCFailAck.setUnits("acknowledgements")
_CcsQuotaMgrOutstanding_Type = Gauge32
_CcsQuotaMgrOutstanding_Object = MibTableColumn
ccsQuotaMgrOutstanding = _CcsQuotaMgrOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 13),
    _CcsQuotaMgrOutstanding_Type()
)
ccsQuotaMgrOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrOutstanding.setUnits("messages")
_CcsQuotaMgrHighWater_Type = Gauge32
_CcsQuotaMgrHighWater_Object = MibTableColumn
ccsQuotaMgrHighWater = _CcsQuotaMgrHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 14),
    _CcsQuotaMgrHighWater_Type()
)
ccsQuotaMgrHighWater.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsQuotaMgrHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHighWater.setUnits("messages")
_CcsQuotaMgrHighWaterResetTime_Type = TimeStamp
_CcsQuotaMgrHighWaterResetTime_Object = MibTableColumn
ccsQuotaMgrHighWaterResetTime = _CcsQuotaMgrHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 15),
    _CcsQuotaMgrHighWaterResetTime_Type()
)
ccsQuotaMgrHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHighWaterResetTime.setStatus("current")
_CcsQuotaMgrBadRecord_Type = Counter32
_CcsQuotaMgrBadRecord_Object = MibTableColumn
ccsQuotaMgrBadRecord = _CcsQuotaMgrBadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 16),
    _CcsQuotaMgrBadRecord_Type()
)
ccsQuotaMgrBadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrBadRecord.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrBadRecord.setUnits("records")
_CcsQuotaMgrHCBadRecord_Type = Counter64
_CcsQuotaMgrHCBadRecord_Object = MibTableColumn
ccsQuotaMgrHCBadRecord = _CcsQuotaMgrHCBadRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 17),
    _CcsQuotaMgrHCBadRecord_Type()
)
ccsQuotaMgrHCBadRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCBadRecord.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCBadRecord.setUnits("records")
_CcsQuotaMgrRetransmit_Type = Counter32
_CcsQuotaMgrRetransmit_Object = MibTableColumn
ccsQuotaMgrRetransmit = _CcsQuotaMgrRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 18),
    _CcsQuotaMgrRetransmit_Type()
)
ccsQuotaMgrRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrRetransmit.setUnits("messages")
_CcsQuotaMgrHCRetransmit_Type = Counter64
_CcsQuotaMgrHCRetransmit_Object = MibTableColumn
ccsQuotaMgrHCRetransmit = _CcsQuotaMgrHCRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 19),
    _CcsQuotaMgrHCRetransmit_Type()
)
ccsQuotaMgrHCRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCRetransmit.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrHCRetransmit.setUnits("messages")
_CcsQuotaMgrRowStatus_Type = RowStatus
_CcsQuotaMgrRowStatus_Object = MibTableColumn
ccsQuotaMgrRowStatus = _CcsQuotaMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 20),
    _CcsQuotaMgrRowStatus_Type()
)
ccsQuotaMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsQuotaMgrRowStatus.setStatus("current")
_CcsQuotaMgrPacketRate_Type = Gauge32
_CcsQuotaMgrPacketRate_Object = MibTableColumn
ccsQuotaMgrPacketRate = _CcsQuotaMgrPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 21),
    _CcsQuotaMgrPacketRate_Type()
)
ccsQuotaMgrPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrPacketRate.setUnits("packets")
_CcsQuotaMgrAckRate_Type = Gauge32
_CcsQuotaMgrAckRate_Object = MibTableColumn
ccsQuotaMgrAckRate = _CcsQuotaMgrAckRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 4, 1, 22),
    _CcsQuotaMgrAckRate_Type()
)
ccsQuotaMgrAckRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsQuotaMgrAckRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsQuotaMgrAckRate.setUnits("acknowledgments")
_CcsLoadStatistics_ObjectIdentity = ObjectIdentity
ccsLoadStatistics = _CcsLoadStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5)
)
_CcsLoadStatRadiusTable_Object = MibTable
ccsLoadStatRadiusTable = _CcsLoadStatRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ccsLoadStatRadiusTable.setStatus("current")
_CcsLoadStatRadiusEntry_Object = MibTableRow
ccsLoadStatRadiusEntry = _CcsLoadStatRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1)
)
ccsLoadStatRadiusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatRadiusEntry.setStatus("current")
_CcsLoadStatRadiusStartAllowed_Type = Counter32
_CcsLoadStatRadiusStartAllowed_Object = MibTableColumn
ccsLoadStatRadiusStartAllowed = _CcsLoadStatRadiusStartAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 1),
    _CcsLoadStatRadiusStartAllowed_Type()
)
ccsLoadStatRadiusStartAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowed.setUnits("requests")
_CcsLoadStatHCRadiusStartAllowed_Type = Counter64
_CcsLoadStatHCRadiusStartAllowed_Object = MibTableColumn
ccsLoadStatHCRadiusStartAllowed = _CcsLoadStatHCRadiusStartAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 2),
    _CcsLoadStatHCRadiusStartAllowed_Type()
)
ccsLoadStatHCRadiusStartAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowed.setUnits("requests")
_CcsLoadStatRadiusStartAllowedRate_Type = Gauge32
_CcsLoadStatRadiusStartAllowedRate_Object = MibTableColumn
ccsLoadStatRadiusStartAllowedRate = _CcsLoadStatRadiusStartAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 3),
    _CcsLoadStatRadiusStartAllowedRate_Type()
)
ccsLoadStatRadiusStartAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowedRate.setUnits("requests")
_CcsLoadStatRadiusStartAllowedRateHighWater_Type = Gauge32
_CcsLoadStatRadiusStartAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatRadiusStartAllowedRateHighWater = _CcsLoadStatRadiusStartAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 4),
    _CcsLoadStatRadiusStartAllowedRateHighWater_Type()
)
ccsLoadStatRadiusStartAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartAllowedRateHighWater.setUnits("requests")
_CcsLoadStatHCRadiusStartAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCRadiusStartAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCRadiusStartAllowedRateHighWater = _CcsLoadStatHCRadiusStartAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 5),
    _CcsLoadStatHCRadiusStartAllowedRateHighWater_Type()
)
ccsLoadStatHCRadiusStartAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowedRateHighWater.setUnits("requests")
_CcsLoadStatRadiusStartIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatRadiusStartIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatRadiusStartIPCQueueDepthTolerance = _CcsLoadStatRadiusStartIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 6),
    _CcsLoadStatRadiusStartIPCQueueDepthTolerance_Type()
)
ccsLoadStatRadiusStartIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatRadiusStartDenied_Type = Counter32
_CcsLoadStatRadiusStartDenied_Object = MibTableColumn
ccsLoadStatRadiusStartDenied = _CcsLoadStatRadiusStartDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 7),
    _CcsLoadStatRadiusStartDenied_Type()
)
ccsLoadStatRadiusStartDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenied.setUnits("requests")
_CcsLoadStatHCRadiusStartDenied_Type = Counter64
_CcsLoadStatHCRadiusStartDenied_Object = MibTableColumn
ccsLoadStatHCRadiusStartDenied = _CcsLoadStatHCRadiusStartDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 8),
    _CcsLoadStatHCRadiusStartDenied_Type()
)
ccsLoadStatHCRadiusStartDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenied.setUnits("requests")
_CcsLoadStatRadiusStartDenialRate_Type = Gauge32
_CcsLoadStatRadiusStartDenialRate_Object = MibTableColumn
ccsLoadStatRadiusStartDenialRate = _CcsLoadStatRadiusStartDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 9),
    _CcsLoadStatRadiusStartDenialRate_Type()
)
ccsLoadStatRadiusStartDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenialRate.setUnits("requests")
_CcsLoadStatRadiusStartDenialRateHighWater_Type = Gauge32
_CcsLoadStatRadiusStartDenialRateHighWater_Object = MibTableColumn
ccsLoadStatRadiusStartDenialRateHighWater = _CcsLoadStatRadiusStartDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 10),
    _CcsLoadStatRadiusStartDenialRateHighWater_Type()
)
ccsLoadStatRadiusStartDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatRadiusStartDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCRadiusStartDenialRateHighWater_Type = Counter64
_CcsLoadStatHCRadiusStartDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCRadiusStartDenialRateHighWater = _CcsLoadStatHCRadiusStartDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 11),
    _CcsLoadStatHCRadiusStartDenialRateHighWater_Type()
)
ccsLoadStatHCRadiusStartDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCRadiusStartAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCRadiusStartAllowedRate_Object = MibTableColumn
ccsLoadStatHCRadiusStartAllowedRate = _CcsLoadStatHCRadiusStartAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 12),
    _CcsLoadStatHCRadiusStartAllowedRate_Type()
)
ccsLoadStatHCRadiusStartAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartAllowedRate.setUnits("requests")
_CcsLoadStatHCRadiusStartDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCRadiusStartDenialRate_Object = MibTableColumn
ccsLoadStatHCRadiusStartDenialRate = _CcsLoadStatHCRadiusStartDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 1, 1, 13),
    _CcsLoadStatHCRadiusStartDenialRate_Type()
)
ccsLoadStatHCRadiusStartDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCRadiusStartDenialRate.setUnits("requests")
_CcsLoadStatUserDBTable_Object = MibTable
ccsLoadStatUserDBTable = _CcsLoadStatUserDBTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    ccsLoadStatUserDBTable.setStatus("current")
_CcsLoadStatUserDBEntry_Object = MibTableRow
ccsLoadStatUserDBEntry = _CcsLoadStatUserDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1)
)
ccsLoadStatUserDBEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatUserDBEntry.setStatus("current")
_CcsLoadStatUserDBReqAllowed_Type = Counter32
_CcsLoadStatUserDBReqAllowed_Object = MibTableColumn
ccsLoadStatUserDBReqAllowed = _CcsLoadStatUserDBReqAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 1),
    _CcsLoadStatUserDBReqAllowed_Type()
)
ccsLoadStatUserDBReqAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowed.setUnits("requests")
_CcsLoadStatHCUserDBReqAllowed_Type = Counter64
_CcsLoadStatHCUserDBReqAllowed_Object = MibTableColumn
ccsLoadStatHCUserDBReqAllowed = _CcsLoadStatHCUserDBReqAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 2),
    _CcsLoadStatHCUserDBReqAllowed_Type()
)
ccsLoadStatHCUserDBReqAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowed.setUnits("requests")
_CcsLoadStatUserDBReqAllowedRate_Type = Gauge32
_CcsLoadStatUserDBReqAllowedRate_Object = MibTableColumn
ccsLoadStatUserDBReqAllowedRate = _CcsLoadStatUserDBReqAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 3),
    _CcsLoadStatUserDBReqAllowedRate_Type()
)
ccsLoadStatUserDBReqAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowedRate.setUnits("requests")
_CcsLoadStatUserDBReqAllowedRateHighWater_Type = Gauge32
_CcsLoadStatUserDBReqAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatUserDBReqAllowedRateHighWater = _CcsLoadStatUserDBReqAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 4),
    _CcsLoadStatUserDBReqAllowedRateHighWater_Type()
)
ccsLoadStatUserDBReqAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqAllowedRateHighWater.setUnits("requests")
_CcsLoadStatHCUserDBReqAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCUserDBReqAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCUserDBReqAllowedRateHighWater = _CcsLoadStatHCUserDBReqAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 5),
    _CcsLoadStatHCUserDBReqAllowedRateHighWater_Type()
)
ccsLoadStatHCUserDBReqAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowedRateHighWater.setUnits("requests")
_CcsLoadStatUserDBReqIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatUserDBReqIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatUserDBReqIPCQueueDepthTolerance = _CcsLoadStatUserDBReqIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 6),
    _CcsLoadStatUserDBReqIPCQueueDepthTolerance_Type()
)
ccsLoadStatUserDBReqIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatUserDBReqDenied_Type = Counter32
_CcsLoadStatUserDBReqDenied_Object = MibTableColumn
ccsLoadStatUserDBReqDenied = _CcsLoadStatUserDBReqDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 7),
    _CcsLoadStatUserDBReqDenied_Type()
)
ccsLoadStatUserDBReqDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenied.setUnits("requests")
_CcsLoadStatHCUserDBReqDenied_Type = Counter64
_CcsLoadStatHCUserDBReqDenied_Object = MibTableColumn
ccsLoadStatHCUserDBReqDenied = _CcsLoadStatHCUserDBReqDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 8),
    _CcsLoadStatHCUserDBReqDenied_Type()
)
ccsLoadStatHCUserDBReqDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenied.setUnits("requests")
_CcsLoadStatUserDBReqDenialRate_Type = Gauge32
_CcsLoadStatUserDBReqDenialRate_Object = MibTableColumn
ccsLoadStatUserDBReqDenialRate = _CcsLoadStatUserDBReqDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 9),
    _CcsLoadStatUserDBReqDenialRate_Type()
)
ccsLoadStatUserDBReqDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenialRate.setUnits("requests")
_CcsLoadStatUserDBReqDenialRateHighWater_Type = Gauge32
_CcsLoadStatUserDBReqDenialRateHighWater_Object = MibTableColumn
ccsLoadStatUserDBReqDenialRateHighWater = _CcsLoadStatUserDBReqDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 10),
    _CcsLoadStatUserDBReqDenialRateHighWater_Type()
)
ccsLoadStatUserDBReqDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatUserDBReqDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCUserDBReqDenialRateHighWater_Type = Counter64
_CcsLoadStatHCUserDBReqDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCUserDBReqDenialRateHighWater = _CcsLoadStatHCUserDBReqDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 11),
    _CcsLoadStatHCUserDBReqDenialRateHighWater_Type()
)
ccsLoadStatHCUserDBReqDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCUserDBReqAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCUserDBReqAllowedRate_Object = MibTableColumn
ccsLoadStatHCUserDBReqAllowedRate = _CcsLoadStatHCUserDBReqAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 12),
    _CcsLoadStatHCUserDBReqAllowedRate_Type()
)
ccsLoadStatHCUserDBReqAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqAllowedRate.setUnits("requests")
_CcsLoadStatHCUserDBReqDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCUserDBReqDenialRate_Object = MibTableColumn
ccsLoadStatHCUserDBReqDenialRate = _CcsLoadStatHCUserDBReqDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 2, 1, 13),
    _CcsLoadStatHCUserDBReqDenialRate_Type()
)
ccsLoadStatHCUserDBReqDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCUserDBReqDenialRate.setUnits("requests")
_CcsLoadStatSessionTable_Object = MibTable
ccsLoadStatSessionTable = _CcsLoadStatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    ccsLoadStatSessionTable.setStatus("current")
_CcsLoadStatSessionEntry_Object = MibTableRow
ccsLoadStatSessionEntry = _CcsLoadStatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1)
)
ccsLoadStatSessionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatSessionEntry.setStatus("current")
_CcsLoadStatSessionCreateAllowed_Type = Counter32
_CcsLoadStatSessionCreateAllowed_Object = MibTableColumn
ccsLoadStatSessionCreateAllowed = _CcsLoadStatSessionCreateAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 1),
    _CcsLoadStatSessionCreateAllowed_Type()
)
ccsLoadStatSessionCreateAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowed.setUnits("requests")
_CcsLoadStatHCSessionCreateAllowed_Type = Counter64
_CcsLoadStatHCSessionCreateAllowed_Object = MibTableColumn
ccsLoadStatHCSessionCreateAllowed = _CcsLoadStatHCSessionCreateAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 2),
    _CcsLoadStatHCSessionCreateAllowed_Type()
)
ccsLoadStatHCSessionCreateAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowed.setUnits("requests")
_CcsLoadStatSessionCreateAllowedRate_Type = Gauge32
_CcsLoadStatSessionCreateAllowedRate_Object = MibTableColumn
ccsLoadStatSessionCreateAllowedRate = _CcsLoadStatSessionCreateAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 3),
    _CcsLoadStatSessionCreateAllowedRate_Type()
)
ccsLoadStatSessionCreateAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowedRate.setUnits("requests")
_CcsLoadStatSessionCreateAllowedRateHighWater_Type = Gauge32
_CcsLoadStatSessionCreateAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatSessionCreateAllowedRateHighWater = _CcsLoadStatSessionCreateAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 4),
    _CcsLoadStatSessionCreateAllowedRateHighWater_Type()
)
ccsLoadStatSessionCreateAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateAllowedRateHighWater.setUnits("requests")
_CcsLoadStatHCSessionCreateAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCSessionCreateAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCSessionCreateAllowedRateHighWater = _CcsLoadStatHCSessionCreateAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 5),
    _CcsLoadStatHCSessionCreateAllowedRateHighWater_Type()
)
ccsLoadStatHCSessionCreateAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowedRateHighWater.setUnits("requests")
_CcsLoadStatSessionCreateIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatSessionCreateIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatSessionCreateIPCQueueDepthTolerance = _CcsLoadStatSessionCreateIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 6),
    _CcsLoadStatSessionCreateIPCQueueDepthTolerance_Type()
)
ccsLoadStatSessionCreateIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatSessionCreateDenied_Type = Counter32
_CcsLoadStatSessionCreateDenied_Object = MibTableColumn
ccsLoadStatSessionCreateDenied = _CcsLoadStatSessionCreateDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 7),
    _CcsLoadStatSessionCreateDenied_Type()
)
ccsLoadStatSessionCreateDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenied.setUnits("requests")
_CcsLoadStatHCSessionCreateDenied_Type = Counter64
_CcsLoadStatHCSessionCreateDenied_Object = MibTableColumn
ccsLoadStatHCSessionCreateDenied = _CcsLoadStatHCSessionCreateDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 8),
    _CcsLoadStatHCSessionCreateDenied_Type()
)
ccsLoadStatHCSessionCreateDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenied.setUnits("requests")
_CcsLoadStatSessionCreateDenialRate_Type = Gauge32
_CcsLoadStatSessionCreateDenialRate_Object = MibTableColumn
ccsLoadStatSessionCreateDenialRate = _CcsLoadStatSessionCreateDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 9),
    _CcsLoadStatSessionCreateDenialRate_Type()
)
ccsLoadStatSessionCreateDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenialRate.setUnits("requests")
_CcsLoadStatSessionCreateDenialRateHighWater_Type = Gauge32
_CcsLoadStatSessionCreateDenialRateHighWater_Object = MibTableColumn
ccsLoadStatSessionCreateDenialRateHighWater = _CcsLoadStatSessionCreateDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 10),
    _CcsLoadStatSessionCreateDenialRateHighWater_Type()
)
ccsLoadStatSessionCreateDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatSessionCreateDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCSessionCreateDenialRateHighWater_Type = Counter64
_CcsLoadStatHCSessionCreateDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCSessionCreateDenialRateHighWater = _CcsLoadStatHCSessionCreateDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 11),
    _CcsLoadStatHCSessionCreateDenialRateHighWater_Type()
)
ccsLoadStatHCSessionCreateDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenialRateHighWater.setUnits("requests")
_CcsLoadStatHCSessionCreateAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCSessionCreateAllowedRate_Object = MibTableColumn
ccsLoadStatHCSessionCreateAllowedRate = _CcsLoadStatHCSessionCreateAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 12),
    _CcsLoadStatHCSessionCreateAllowedRate_Type()
)
ccsLoadStatHCSessionCreateAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateAllowedRate.setUnits("requests")
_CcsLoadStatHCSessionCreateDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCSessionCreateDenialRate_Object = MibTableColumn
ccsLoadStatHCSessionCreateDenialRate = _CcsLoadStatHCSessionCreateDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 3, 1, 13),
    _CcsLoadStatHCSessionCreateDenialRate_Type()
)
ccsLoadStatHCSessionCreateDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCSessionCreateDenialRate.setUnits("requests")
_CcsLoadStatBMATable_Object = MibTable
ccsLoadStatBMATable = _CcsLoadStatBMATable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    ccsLoadStatBMATable.setStatus("current")
_CcsLoadStatBMAEntry_Object = MibTableRow
ccsLoadStatBMAEntry = _CcsLoadStatBMAEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1)
)
ccsLoadStatBMAEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatBMAEntry.setStatus("current")
_CcsLoadStatBMAMsgsAllowed_Type = Counter32
_CcsLoadStatBMAMsgsAllowed_Object = MibTableColumn
ccsLoadStatBMAMsgsAllowed = _CcsLoadStatBMAMsgsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 1),
    _CcsLoadStatBMAMsgsAllowed_Type()
)
ccsLoadStatBMAMsgsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowed.setUnits("messages")
_CcsLoadStatHCBMAMsgsAllowed_Type = Counter64
_CcsLoadStatHCBMAMsgsAllowed_Object = MibTableColumn
ccsLoadStatHCBMAMsgsAllowed = _CcsLoadStatHCBMAMsgsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 2),
    _CcsLoadStatHCBMAMsgsAllowed_Type()
)
ccsLoadStatHCBMAMsgsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowed.setUnits("messages")
_CcsLoadStatBMAMsgsAllowedRate_Type = Gauge32
_CcsLoadStatBMAMsgsAllowedRate_Object = MibTableColumn
ccsLoadStatBMAMsgsAllowedRate = _CcsLoadStatBMAMsgsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 3),
    _CcsLoadStatBMAMsgsAllowedRate_Type()
)
ccsLoadStatBMAMsgsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowedRate.setUnits("messages")
_CcsLoadStatBMAMsgsAllowedRateHighWater_Type = Gauge32
_CcsLoadStatBMAMsgsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatBMAMsgsAllowedRateHighWater = _CcsLoadStatBMAMsgsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 4),
    _CcsLoadStatBMAMsgsAllowedRateHighWater_Type()
)
ccsLoadStatBMAMsgsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsAllowedRateHighWater.setUnits("messages")
_CcsLoadStatHCBMAMsgsAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCBMAMsgsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCBMAMsgsAllowedRateHighWater = _CcsLoadStatHCBMAMsgsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 5),
    _CcsLoadStatHCBMAMsgsAllowedRateHighWater_Type()
)
ccsLoadStatHCBMAMsgsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowedRateHighWater.setUnits("messages")
_CcsLoadStatBMAMsgsIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatBMAMsgsIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatBMAMsgsIPCQueueDepthTolerance = _CcsLoadStatBMAMsgsIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 6),
    _CcsLoadStatBMAMsgsIPCQueueDepthTolerance_Type()
)
ccsLoadStatBMAMsgsIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatBMAMsgsDenied_Type = Counter32
_CcsLoadStatBMAMsgsDenied_Object = MibTableColumn
ccsLoadStatBMAMsgsDenied = _CcsLoadStatBMAMsgsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 7),
    _CcsLoadStatBMAMsgsDenied_Type()
)
ccsLoadStatBMAMsgsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenied.setUnits("messages")
_CcsLoadStatHCBMAMsgsDenied_Type = Counter64
_CcsLoadStatHCBMAMsgsDenied_Object = MibTableColumn
ccsLoadStatHCBMAMsgsDenied = _CcsLoadStatHCBMAMsgsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 8),
    _CcsLoadStatHCBMAMsgsDenied_Type()
)
ccsLoadStatHCBMAMsgsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenied.setUnits("messages")
_CcsLoadStatBMAMsgsDenialRate_Type = Gauge32
_CcsLoadStatBMAMsgsDenialRate_Object = MibTableColumn
ccsLoadStatBMAMsgsDenialRate = _CcsLoadStatBMAMsgsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 9),
    _CcsLoadStatBMAMsgsDenialRate_Type()
)
ccsLoadStatBMAMsgsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenialRate.setUnits("messages")
_CcsLoadStatBMAMsgsDenialRateHighWater_Type = Gauge32
_CcsLoadStatBMAMsgsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatBMAMsgsDenialRateHighWater = _CcsLoadStatBMAMsgsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 10),
    _CcsLoadStatBMAMsgsDenialRateHighWater_Type()
)
ccsLoadStatBMAMsgsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatBMAMsgsDenialRateHighWater.setUnits("messages")
_CcsLoadStatHCBMAMsgsDenialRateHighWater_Type = Counter64
_CcsLoadStatHCBMAMsgsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCBMAMsgsDenialRateHighWater = _CcsLoadStatHCBMAMsgsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 11),
    _CcsLoadStatHCBMAMsgsDenialRateHighWater_Type()
)
ccsLoadStatHCBMAMsgsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenialRateHighWater.setUnits("messages")
_CcsLoadStatHCBMAMsgsAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCBMAMsgsAllowedRate_Object = MibTableColumn
ccsLoadStatHCBMAMsgsAllowedRate = _CcsLoadStatHCBMAMsgsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 12),
    _CcsLoadStatHCBMAMsgsAllowedRate_Type()
)
ccsLoadStatHCBMAMsgsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsAllowedRate.setUnits("messages")
_CcsLoadStatHCBMAMsgsDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCBMAMsgsDenialRate_Object = MibTableColumn
ccsLoadStatHCBMAMsgsDenialRate = _CcsLoadStatHCBMAMsgsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 4, 1, 13),
    _CcsLoadStatHCBMAMsgsDenialRate_Type()
)
ccsLoadStatHCBMAMsgsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCBMAMsgsDenialRate.setUnits("messages")
_CcsLoadStatQuotaMgrTable_Object = MibTable
ccsLoadStatQuotaMgrTable = _CcsLoadStatQuotaMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrTable.setStatus("current")
_CcsLoadStatQuotaMgrEntry_Object = MibTableRow
ccsLoadStatQuotaMgrEntry = _CcsLoadStatQuotaMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1)
)
ccsLoadStatQuotaMgrEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrEntry.setStatus("current")
_CcsLoadStatQuotaMgrMsgsAllowed_Type = Counter32
_CcsLoadStatQuotaMgrMsgsAllowed_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsAllowed = _CcsLoadStatQuotaMgrMsgsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 1),
    _CcsLoadStatQuotaMgrMsgsAllowed_Type()
)
ccsLoadStatQuotaMgrMsgsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowed.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsAllowed_Type = Counter64
_CcsLoadStatHCQuotaMgrMsgsAllowed_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsAllowed = _CcsLoadStatHCQuotaMgrMsgsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 2),
    _CcsLoadStatHCQuotaMgrMsgsAllowed_Type()
)
ccsLoadStatHCQuotaMgrMsgsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowed.setUnits("messages")
_CcsLoadStatQuotaMgrMsgsAllowedRate_Type = Gauge32
_CcsLoadStatQuotaMgrMsgsAllowedRate_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsAllowedRate = _CcsLoadStatQuotaMgrMsgsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 3),
    _CcsLoadStatQuotaMgrMsgsAllowedRate_Type()
)
ccsLoadStatQuotaMgrMsgsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowedRate.setUnits("messages")
_CcsLoadStatQuotaMgrMsgsAllowedRateHighWater_Type = Gauge32
_CcsLoadStatQuotaMgrMsgsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsAllowedRateHighWater = _CcsLoadStatQuotaMgrMsgsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 4),
    _CcsLoadStatQuotaMgrMsgsAllowedRateHighWater_Type()
)
ccsLoadStatQuotaMgrMsgsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsAllowedRateHighWater.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCQuotaMgrMsgsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater = _CcsLoadStatHCQuotaMgrMsgsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 5),
    _CcsLoadStatHCQuotaMgrMsgsAllowedRateHighWater_Type()
)
ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater.setUnits("messages")
_CcsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance = _CcsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 6),
    _CcsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance_Type()
)
ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatQuotaMgrMsgsDenied_Type = Counter32
_CcsLoadStatQuotaMgrMsgsDenied_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsDenied = _CcsLoadStatQuotaMgrMsgsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 7),
    _CcsLoadStatQuotaMgrMsgsDenied_Type()
)
ccsLoadStatQuotaMgrMsgsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenied.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsDenied_Type = Counter64
_CcsLoadStatHCQuotaMgrMsgsDenied_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsDenied = _CcsLoadStatHCQuotaMgrMsgsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 8),
    _CcsLoadStatHCQuotaMgrMsgsDenied_Type()
)
ccsLoadStatHCQuotaMgrMsgsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenied.setUnits("messages")
_CcsLoadStatQuotaMgrMsgsDenialRate_Type = Gauge32
_CcsLoadStatQuotaMgrMsgsDenialRate_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsDenialRate = _CcsLoadStatQuotaMgrMsgsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 9),
    _CcsLoadStatQuotaMgrMsgsDenialRate_Type()
)
ccsLoadStatQuotaMgrMsgsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenialRate.setUnits("messages")
_CcsLoadStatQuotaMgrMsgsDenialRateHighWater_Type = Gauge32
_CcsLoadStatQuotaMgrMsgsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatQuotaMgrMsgsDenialRateHighWater = _CcsLoadStatQuotaMgrMsgsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 10),
    _CcsLoadStatQuotaMgrMsgsDenialRateHighWater_Type()
)
ccsLoadStatQuotaMgrMsgsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatQuotaMgrMsgsDenialRateHighWater.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsDenialRateHighWater_Type = Counter64
_CcsLoadStatHCQuotaMgrMsgsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater = _CcsLoadStatHCQuotaMgrMsgsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 11),
    _CcsLoadStatHCQuotaMgrMsgsDenialRateHighWater_Type()
)
ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCQuotaMgrMsgsAllowedRate_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsAllowedRate = _CcsLoadStatHCQuotaMgrMsgsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 12),
    _CcsLoadStatHCQuotaMgrMsgsAllowedRate_Type()
)
ccsLoadStatHCQuotaMgrMsgsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsAllowedRate.setUnits("messages")
_CcsLoadStatHCQuotaMgrMsgsDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCQuotaMgrMsgsDenialRate_Object = MibTableColumn
ccsLoadStatHCQuotaMgrMsgsDenialRate = _CcsLoadStatHCQuotaMgrMsgsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 5, 1, 13),
    _CcsLoadStatHCQuotaMgrMsgsDenialRate_Type()
)
ccsLoadStatHCQuotaMgrMsgsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCQuotaMgrMsgsDenialRate.setUnits("messages")
_CcsLoadStatGxEventTable_Object = MibTable
ccsLoadStatGxEventTable = _CcsLoadStatGxEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    ccsLoadStatGxEventTable.setStatus("current")
_CcsLoadStatGxEventEntry_Object = MibTableRow
ccsLoadStatGxEventEntry = _CcsLoadStatGxEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1)
)
ccsLoadStatGxEventEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsLoadStatGxEventEntry.setStatus("current")
_CcsLoadStatGxEventsAllowed_Type = Counter32
_CcsLoadStatGxEventsAllowed_Object = MibTableColumn
ccsLoadStatGxEventsAllowed = _CcsLoadStatGxEventsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 1),
    _CcsLoadStatGxEventsAllowed_Type()
)
ccsLoadStatGxEventsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowed.setUnits("notifications")
_CcsLoadStatHCGxEventsAllowed_Type = Counter64
_CcsLoadStatHCGxEventsAllowed_Object = MibTableColumn
ccsLoadStatHCGxEventsAllowed = _CcsLoadStatHCGxEventsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 2),
    _CcsLoadStatHCGxEventsAllowed_Type()
)
ccsLoadStatHCGxEventsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowed.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowed.setUnits("notifications")
_CcsLoadStatGxEventsAllowedRate_Type = Gauge32
_CcsLoadStatGxEventsAllowedRate_Object = MibTableColumn
ccsLoadStatGxEventsAllowedRate = _CcsLoadStatGxEventsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 3),
    _CcsLoadStatGxEventsAllowedRate_Type()
)
ccsLoadStatGxEventsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowedRate.setUnits("notifications per second")
_CcsLoadStatGxEventsAllowedRateHighWater_Type = Gauge32
_CcsLoadStatGxEventsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatGxEventsAllowedRateHighWater = _CcsLoadStatGxEventsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 4),
    _CcsLoadStatGxEventsAllowedRateHighWater_Type()
)
ccsLoadStatGxEventsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsAllowedRateHighWater.setUnits("notifications per second")
_CcsLoadStatHCGxEventsAllowedRateHighWater_Type = Counter64
_CcsLoadStatHCGxEventsAllowedRateHighWater_Object = MibTableColumn
ccsLoadStatHCGxEventsAllowedRateHighWater = _CcsLoadStatHCGxEventsAllowedRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 5),
    _CcsLoadStatHCGxEventsAllowedRateHighWater_Type()
)
ccsLoadStatHCGxEventsAllowedRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowedRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowedRateHighWater.setUnits("notifications per second")
_CcsLoadStatGxEventsIPCQueueDepthTolerance_Type = Integer32
_CcsLoadStatGxEventsIPCQueueDepthTolerance_Object = MibTableColumn
ccsLoadStatGxEventsIPCQueueDepthTolerance = _CcsLoadStatGxEventsIPCQueueDepthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 6),
    _CcsLoadStatGxEventsIPCQueueDepthTolerance_Type()
)
ccsLoadStatGxEventsIPCQueueDepthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsIPCQueueDepthTolerance.setStatus("current")
_CcsLoadStatGxEventsDenied_Type = Counter32
_CcsLoadStatGxEventsDenied_Object = MibTableColumn
ccsLoadStatGxEventsDenied = _CcsLoadStatGxEventsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 7),
    _CcsLoadStatGxEventsDenied_Type()
)
ccsLoadStatGxEventsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenied.setUnits("notifications")
_CcsLoadStatHCGxEventsDenied_Type = Counter64
_CcsLoadStatHCGxEventsDenied_Object = MibTableColumn
ccsLoadStatHCGxEventsDenied = _CcsLoadStatHCGxEventsDenied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 8),
    _CcsLoadStatHCGxEventsDenied_Type()
)
ccsLoadStatHCGxEventsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenied.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenied.setUnits("notifications")
_CcsLoadStatGxEventsDenialRate_Type = Gauge32
_CcsLoadStatGxEventsDenialRate_Object = MibTableColumn
ccsLoadStatGxEventsDenialRate = _CcsLoadStatGxEventsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 9),
    _CcsLoadStatGxEventsDenialRate_Type()
)
ccsLoadStatGxEventsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenialRate.setUnits("notifications per second")
_CcsLoadStatGxEventsDenialRateHighWater_Type = Gauge32
_CcsLoadStatGxEventsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatGxEventsDenialRateHighWater = _CcsLoadStatGxEventsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 10),
    _CcsLoadStatGxEventsDenialRateHighWater_Type()
)
ccsLoadStatGxEventsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatGxEventsDenialRateHighWater.setUnits("notifications per second")
_CcsLoadStatHCGxEventsDenialRateHighWater_Type = Counter64
_CcsLoadStatHCGxEventsDenialRateHighWater_Object = MibTableColumn
ccsLoadStatHCGxEventsDenialRateHighWater = _CcsLoadStatHCGxEventsDenialRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 11),
    _CcsLoadStatHCGxEventsDenialRateHighWater_Type()
)
ccsLoadStatHCGxEventsDenialRateHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenialRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenialRateHighWater.setUnits("notifications per second")
_CcsLoadStatHCGxEventsAllowedRate_Type = CounterBasedGauge64
_CcsLoadStatHCGxEventsAllowedRate_Object = MibTableColumn
ccsLoadStatHCGxEventsAllowedRate = _CcsLoadStatHCGxEventsAllowedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 12),
    _CcsLoadStatHCGxEventsAllowedRate_Type()
)
ccsLoadStatHCGxEventsAllowedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowedRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsAllowedRate.setUnits("notifications per second")
_CcsLoadStatHCGxEventsDenialRate_Type = CounterBasedGauge64
_CcsLoadStatHCGxEventsDenialRate_Object = MibTableColumn
ccsLoadStatHCGxEventsDenialRate = _CcsLoadStatHCGxEventsDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 5, 6, 1, 13),
    _CcsLoadStatHCGxEventsDenialRate_Type()
)
ccsLoadStatHCGxEventsDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    ccsLoadStatHCGxEventsDenialRate.setUnits("notifications per second")
_CcsProtocolStatsTable_Object = MibTable
ccsProtocolStatsTable = _CcsProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ccsProtocolStatsTable.setStatus("current")
_CcsProtocolStatsEntry_Object = MibTableRow
ccsProtocolStatsEntry = _CcsProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1)
)
ccsProtocolStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccspsInspectionMethod"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccspsProtocolName"),
)
if mibBuilder.loadTexts:
    ccsProtocolStatsEntry.setStatus("current")


class _CcspsInspectionMethod_Type(Integer32):
    """Custom type ccspsInspectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nbar", 2),
          ("system", 1))
    )


_CcspsInspectionMethod_Type.__name__ = "Integer32"
_CcspsInspectionMethod_Object = MibTableColumn
ccspsInspectionMethod = _CcspsInspectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 1),
    _CcspsInspectionMethod_Type()
)
ccspsInspectionMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccspsInspectionMethod.setStatus("current")


class _CcspsProtocolName_Type(SnmpAdminString):
    """Custom type ccspsProtocolName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcspsProtocolName_Type.__name__ = "SnmpAdminString"
_CcspsProtocolName_Object = MibTableColumn
ccspsProtocolName = _CcspsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 2),
    _CcspsProtocolName_Type()
)
ccspsProtocolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccspsProtocolName.setStatus("current")
_CcspsTransaction_Type = Counter32
_CcspsTransaction_Object = MibTableColumn
ccspsTransaction = _CcspsTransaction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 3),
    _CcspsTransaction_Type()
)
ccspsTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsTransaction.setStatus("current")
if mibBuilder.loadTexts:
    ccspsTransaction.setUnits("transactions")
_CcspsHCTransaction_Type = Counter64
_CcspsHCTransaction_Object = MibTableColumn
ccspsHCTransaction = _CcspsHCTransaction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 4),
    _CcspsHCTransaction_Type()
)
ccspsHCTransaction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsHCTransaction.setStatus("current")
if mibBuilder.loadTexts:
    ccspsHCTransaction.setUnits("transactions")
_CcspsTransactionRate_Type = Gauge32
_CcspsTransactionRate_Object = MibTableColumn
ccspsTransactionRate = _CcspsTransactionRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 5),
    _CcspsTransactionRate_Type()
)
ccspsTransactionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsTransactionRate.setStatus("current")
if mibBuilder.loadTexts:
    ccspsTransactionRate.setUnits("transactions per second")
_CcspsTransactionRateHighWater_Type = Gauge32
_CcspsTransactionRateHighWater_Object = MibTableColumn
ccspsTransactionRateHighWater = _CcspsTransactionRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 6),
    _CcspsTransactionRateHighWater_Type()
)
ccspsTransactionRateHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccspsTransactionRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccspsTransactionRateHighWater.setUnits("transactions per second")
_CcspsTransactionRateHighWaterResetTime_Type = TimeStamp
_CcspsTransactionRateHighWaterResetTime_Object = MibTableColumn
ccspsTransactionRateHighWaterResetTime = _CcspsTransactionRateHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 7),
    _CcspsTransactionRateHighWaterResetTime_Type()
)
ccspsTransactionRateHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsTransactionRateHighWaterResetTime.setStatus("current")
_CcspsTransactionRateHighWaterTime_Type = TimeStamp
_CcspsTransactionRateHighWaterTime_Object = MibTableColumn
ccspsTransactionRateHighWaterTime = _CcspsTransactionRateHighWaterTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 8),
    _CcspsTransactionRateHighWaterTime_Type()
)
ccspsTransactionRateHighWaterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsTransactionRateHighWaterTime.setStatus("current")
_CcspsSubOutPackets_Type = Counter32
_CcspsSubOutPackets_Object = MibTableColumn
ccspsSubOutPackets = _CcspsSubOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 9),
    _CcspsSubOutPackets_Type()
)
ccspsSubOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutPackets.setUnits("packets")
_CcspsHCSubOutPackets_Type = Counter64
_CcspsHCSubOutPackets_Object = MibTableColumn
ccspsHCSubOutPackets = _CcspsHCSubOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 10),
    _CcspsHCSubOutPackets_Type()
)
ccspsHCSubOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsHCSubOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccspsHCSubOutPackets.setUnits("packets")
_CcspsSubOutPacketRate_Type = Gauge32
_CcspsSubOutPacketRate_Object = MibTableColumn
ccspsSubOutPacketRate = _CcspsSubOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 11),
    _CcspsSubOutPacketRate_Type()
)
ccspsSubOutPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRate.setUnits("packets per second")
_CcspsSubOutPacketRateHighWater_Type = Gauge32
_CcspsSubOutPacketRateHighWater_Object = MibTableColumn
ccspsSubOutPacketRateHighWater = _CcspsSubOutPacketRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 12),
    _CcspsSubOutPacketRateHighWater_Type()
)
ccspsSubOutPacketRateHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRateHighWater.setUnits("packets per second")
_CcspsSubOutPacketRateHighWaterResetTime_Type = TimeStamp
_CcspsSubOutPacketRateHighWaterResetTime_Object = MibTableColumn
ccspsSubOutPacketRateHighWaterResetTime = _CcspsSubOutPacketRateHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 13),
    _CcspsSubOutPacketRateHighWaterResetTime_Type()
)
ccspsSubOutPacketRateHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRateHighWaterResetTime.setStatus("current")
_CcspsSubOutPacketRateHighWaterTime_Type = TimeStamp
_CcspsSubOutPacketRateHighWaterTime_Object = MibTableColumn
ccspsSubOutPacketRateHighWaterTime = _CcspsSubOutPacketRateHighWaterTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 14),
    _CcspsSubOutPacketRateHighWaterTime_Type()
)
ccspsSubOutPacketRateHighWaterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutPacketRateHighWaterTime.setStatus("current")
_CcspsNetOutPackets_Type = Counter32
_CcspsNetOutPackets_Object = MibTableColumn
ccspsNetOutPackets = _CcspsNetOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 15),
    _CcspsNetOutPackets_Type()
)
ccspsNetOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutPackets.setUnits("packets")
_CcspsHCNetOutPackets_Type = Counter64
_CcspsHCNetOutPackets_Object = MibTableColumn
ccspsHCNetOutPackets = _CcspsHCNetOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 16),
    _CcspsHCNetOutPackets_Type()
)
ccspsHCNetOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsHCNetOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    ccspsHCNetOutPackets.setUnits("packets")
_CcspsNetOutPacketRate_Type = Gauge32
_CcspsNetOutPacketRate_Object = MibTableColumn
ccspsNetOutPacketRate = _CcspsNetOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 17),
    _CcspsNetOutPacketRate_Type()
)
ccspsNetOutPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRate.setUnits("packets per second")
_CcspsNetOutPacketRateHighWater_Type = Gauge32
_CcspsNetOutPacketRateHighWater_Object = MibTableColumn
ccspsNetOutPacketRateHighWater = _CcspsNetOutPacketRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 18),
    _CcspsNetOutPacketRateHighWater_Type()
)
ccspsNetOutPacketRateHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRateHighWater.setUnits("packets per second")
_CcspsNetOutPacketRateHighWaterResetTime_Type = TimeStamp
_CcspsNetOutPacketRateHighWaterResetTime_Object = MibTableColumn
ccspsNetOutPacketRateHighWaterResetTime = _CcspsNetOutPacketRateHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 19),
    _CcspsNetOutPacketRateHighWaterResetTime_Type()
)
ccspsNetOutPacketRateHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRateHighWaterResetTime.setStatus("current")
_CcspsNetOutPacketRateHighWaterTime_Type = TimeStamp
_CcspsNetOutPacketRateHighWaterTime_Object = MibTableColumn
ccspsNetOutPacketRateHighWaterTime = _CcspsNetOutPacketRateHighWaterTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 20),
    _CcspsNetOutPacketRateHighWaterTime_Type()
)
ccspsNetOutPacketRateHighWaterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutPacketRateHighWaterTime.setStatus("current")
_CcspsSubOutBytes_Type = Counter32
_CcspsSubOutBytes_Object = MibTableColumn
ccspsSubOutBytes = _CcspsSubOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 21),
    _CcspsSubOutBytes_Type()
)
ccspsSubOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutBytes.setUnits("bytes")
_CcspsHCSubOutBytes_Type = Counter64
_CcspsHCSubOutBytes_Object = MibTableColumn
ccspsHCSubOutBytes = _CcspsHCSubOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 22),
    _CcspsHCSubOutBytes_Type()
)
ccspsHCSubOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsHCSubOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccspsHCSubOutBytes.setUnits("bytes")
_CcspsSubOutBitRate_Type = Gauge32
_CcspsSubOutBitRate_Object = MibTableColumn
ccspsSubOutBitRate = _CcspsSubOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 23),
    _CcspsSubOutBitRate_Type()
)
ccspsSubOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutBitRate.setUnits("bits per second")
_CcspsSubOutBitRateHighWater_Type = Gauge32
_CcspsSubOutBitRateHighWater_Object = MibTableColumn
ccspsSubOutBitRateHighWater = _CcspsSubOutBitRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 24),
    _CcspsSubOutBitRateHighWater_Type()
)
ccspsSubOutBitRateHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccspsSubOutBitRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccspsSubOutBitRateHighWater.setUnits("bits per second")
_CcspsSubOutBitRateHighWaterResetTime_Type = TimeStamp
_CcspsSubOutBitRateHighWaterResetTime_Object = MibTableColumn
ccspsSubOutBitRateHighWaterResetTime = _CcspsSubOutBitRateHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 25),
    _CcspsSubOutBitRateHighWaterResetTime_Type()
)
ccspsSubOutBitRateHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutBitRateHighWaterResetTime.setStatus("current")
_CcspsSubOutBitRateHighWaterTime_Type = TimeStamp
_CcspsSubOutBitRateHighWaterTime_Object = MibTableColumn
ccspsSubOutBitRateHighWaterTime = _CcspsSubOutBitRateHighWaterTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 26),
    _CcspsSubOutBitRateHighWaterTime_Type()
)
ccspsSubOutBitRateHighWaterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsSubOutBitRateHighWaterTime.setStatus("current")
_CcspsNetOutBytes_Type = Counter32
_CcspsNetOutBytes_Object = MibTableColumn
ccspsNetOutBytes = _CcspsNetOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 27),
    _CcspsNetOutBytes_Type()
)
ccspsNetOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutBytes.setUnits("bytes")
_CcspsHCNetOutBytes_Type = Counter64
_CcspsHCNetOutBytes_Object = MibTableColumn
ccspsHCNetOutBytes = _CcspsHCNetOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 28),
    _CcspsHCNetOutBytes_Type()
)
ccspsHCNetOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsHCNetOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    ccspsHCNetOutBytes.setUnits("bytes")
_CcspsNetOutBitRate_Type = Gauge32
_CcspsNetOutBitRate_Object = MibTableColumn
ccspsNetOutBitRate = _CcspsNetOutBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 29),
    _CcspsNetOutBitRate_Type()
)
ccspsNetOutBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutBitRate.setUnits("bits per second")
_CcspsNetOutBitRateHighWater_Type = Gauge32
_CcspsNetOutBitRateHighWater_Object = MibTableColumn
ccspsNetOutBitRateHighWater = _CcspsNetOutBitRateHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 30),
    _CcspsNetOutBitRateHighWater_Type()
)
ccspsNetOutBitRateHighWater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccspsNetOutBitRateHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccspsNetOutBitRateHighWater.setUnits("bits per second")
_CcspsNetOutBitRateHighWaterResetTime_Type = TimeStamp
_CcspsNetOutBitRateHighWaterResetTime_Object = MibTableColumn
ccspsNetOutBitRateHighWaterResetTime = _CcspsNetOutBitRateHighWaterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 31),
    _CcspsNetOutBitRateHighWaterResetTime_Type()
)
ccspsNetOutBitRateHighWaterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutBitRateHighWaterResetTime.setStatus("current")
_CcspsNetOutBitRateHighWaterTime_Type = TimeStamp
_CcspsNetOutBitRateHighWaterTime_Object = MibTableColumn
ccspsNetOutBitRateHighWaterTime = _CcspsNetOutBitRateHighWaterTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 6, 1, 32),
    _CcspsNetOutBitRateHighWaterTime_Type()
)
ccspsNetOutBitRateHighWaterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccspsNetOutBitRateHighWaterTime.setStatus("current")
_CcsBillingPlanStatsTable_Object = MibTable
ccsBillingPlanStatsTable = _CcsBillingPlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ccsBillingPlanStatsTable.setStatus("current")
_CcsBillingPlanStatsEntry_Object = MibTableRow
ccsBillingPlanStatsEntry = _CcsBillingPlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1)
)
ccsBillingPlanStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CONTENT-SERVICES-MIB", "ccsbpsBillingPlanName"),
)
if mibBuilder.loadTexts:
    ccsBillingPlanStatsEntry.setStatus("current")


class _CcsbpsBillingPlanName_Type(SnmpAdminString):
    """Custom type ccsbpsBillingPlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CcsbpsBillingPlanName_Type.__name__ = "SnmpAdminString"
_CcsbpsBillingPlanName_Object = MibTableColumn
ccsbpsBillingPlanName = _CcsbpsBillingPlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1, 1),
    _CcsbpsBillingPlanName_Type()
)
ccsbpsBillingPlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsbpsBillingPlanName.setStatus("current")
_CcsbpsSubscribers_Type = Gauge32
_CcsbpsSubscribers_Object = MibTableColumn
ccsbpsSubscribers = _CcsbpsSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1, 2),
    _CcsbpsSubscribers_Type()
)
ccsbpsSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsbpsSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    ccsbpsSubscribers.setUnits("subscribers")
_CcsbpsHCSubscribers_Type = CounterBasedGauge64
_CcsbpsHCSubscribers_Object = MibTableColumn
ccsbpsHCSubscribers = _CcsbpsHCSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1, 3),
    _CcsbpsHCSubscribers_Type()
)
ccsbpsHCSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsbpsHCSubscribers.setStatus("current")
if mibBuilder.loadTexts:
    ccsbpsHCSubscribers.setUnits("subscribers")
_CcsbpsSubscribersHighWater_Type = Gauge32
_CcsbpsSubscribersHighWater_Object = MibTableColumn
ccsbpsSubscribersHighWater = _CcsbpsSubscribersHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1, 4),
    _CcsbpsSubscribersHighWater_Type()
)
ccsbpsSubscribersHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsbpsSubscribersHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsbpsSubscribersHighWater.setUnits("subscribers")
_CcsbpsHCSubscribersHighWater_Type = CounterBasedGauge64
_CcsbpsHCSubscribersHighWater_Object = MibTableColumn
ccsbpsHCSubscribersHighWater = _CcsbpsHCSubscribersHighWater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 2, 7, 1, 5),
    _CcsbpsHCSubscribersHighWater_Type()
)
ccsbpsHCSubscribersHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsbpsHCSubscribersHighWater.setStatus("current")
if mibBuilder.loadTexts:
    ccsbpsHCSubscribersHighWater.setUnits("subscribers")
_CcsNotifConfig_ObjectIdentity = ObjectIdentity
ccsNotifConfig = _CcsNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3)
)
_CcsNotifCfgTable_Object = MibTable
ccsNotifCfgTable = _CcsNotifCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccsNotifCfgTable.setStatus("current")
_CcsNotifCfgTableEntry_Object = MibTableRow
ccsNotifCfgTableEntry = _CcsNotifCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1)
)
ccsNotifCfgTableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ccsNotifCfgTableEntry.setStatus("current")


class _CcsBMAStateChangeNotifEnabled_Type(TruthValue):
    """Custom type ccsBMAStateChangeNotifEnabled based on TruthValue"""


_CcsBMAStateChangeNotifEnabled_Object = MibTableColumn
ccsBMAStateChangeNotifEnabled = _CcsBMAStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 1),
    _CcsBMAStateChangeNotifEnabled_Type()
)
ccsBMAStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsBMAStateChangeNotifEnabled.setStatus("current")


class _CcsQuotaMgrStateChangeNotifEnabled_Type(TruthValue):
    """Custom type ccsQuotaMgrStateChangeNotifEnabled based on TruthValue"""


_CcsQuotaMgrStateChangeNotifEnabled_Object = MibTableColumn
ccsQuotaMgrStateChangeNotifEnabled = _CcsQuotaMgrStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 2),
    _CcsQuotaMgrStateChangeNotifEnabled_Type()
)
ccsQuotaMgrStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsQuotaMgrStateChangeNotifEnabled.setStatus("current")


class _CcsUserDbStateChangeNotifEnabled_Type(TruthValue):
    """Custom type ccsUserDbStateChangeNotifEnabled based on TruthValue"""


_CcsUserDbStateChangeNotifEnabled_Object = MibTableColumn
ccsUserDbStateChangeNotifEnabled = _CcsUserDbStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 3),
    _CcsUserDbStateChangeNotifEnabled_Type()
)
ccsUserDbStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUserDbStateChangeNotifEnabled.setStatus("current")


class _CcsBMALostRecordEventNotifEnabled_Type(TruthValue):
    """Custom type ccsBMALostRecordEventNotifEnabled based on TruthValue"""


_CcsBMALostRecordEventNotifEnabled_Object = MibTableColumn
ccsBMALostRecordEventNotifEnabled = _CcsBMALostRecordEventNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 4),
    _CcsBMALostRecordEventNotifEnabled_Type()
)
ccsBMALostRecordEventNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsBMALostRecordEventNotifEnabled.setStatus("current")


class _CcsQuotaMgrLostRecordEventNotifEnabled_Type(TruthValue):
    """Custom type ccsQuotaMgrLostRecordEventNotifEnabled based on TruthValue"""


_CcsQuotaMgrLostRecordEventNotifEnabled_Object = MibTableColumn
ccsQuotaMgrLostRecordEventNotifEnabled = _CcsQuotaMgrLostRecordEventNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 5),
    _CcsQuotaMgrLostRecordEventNotifEnabled_Type()
)
ccsQuotaMgrLostRecordEventNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsQuotaMgrLostRecordEventNotifEnabled.setStatus("current")


class _CcsUserThresholdExceededNotifEnabled_Type(TruthValue):
    """Custom type ccsUserThresholdExceededNotifEnabled based on TruthValue"""


_CcsUserThresholdExceededNotifEnabled_Object = MibTableColumn
ccsUserThresholdExceededNotifEnabled = _CcsUserThresholdExceededNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 6),
    _CcsUserThresholdExceededNotifEnabled_Type()
)
ccsUserThresholdExceededNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUserThresholdExceededNotifEnabled.setStatus("current")


class _CcsAdControlNotifEnabled_Type(TruthValue):
    """Custom type ccsAdControlNotifEnabled based on TruthValue"""


_CcsAdControlNotifEnabled_Object = MibTableColumn
ccsAdControlNotifEnabled = _CcsAdControlNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 7),
    _CcsAdControlNotifEnabled_Type()
)
ccsAdControlNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsAdControlNotifEnabled.setStatus("current")


class _CcsUserEntriesThresholdNotifEnabled_Type(TruthValue):
    """Custom type ccsUserEntriesThresholdNotifEnabled based on TruthValue"""


_CcsUserEntriesThresholdNotifEnabled_Object = MibTableColumn
ccsUserEntriesThresholdNotifEnabled = _CcsUserEntriesThresholdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 8),
    _CcsUserEntriesThresholdNotifEnabled_Type()
)
ccsUserEntriesThresholdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUserEntriesThresholdNotifEnabled.setStatus("current")


class _CcsSessionThresholdNotifEnabled_Type(TruthValue):
    """Custom type ccsSessionThresholdNotifEnabled based on TruthValue"""


_CcsSessionThresholdNotifEnabled_Object = MibTableColumn
ccsSessionThresholdNotifEnabled = _CcsSessionThresholdNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 3, 1, 1, 9),
    _CcsSessionThresholdNotifEnabled_Type()
)
ccsSessionThresholdNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsSessionThresholdNotifEnabled.setStatus("current")
_CcsNotifInfo_ObjectIdentity = ObjectIdentity
ccsNotifInfo = _CcsNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4)
)
_CcsTPIndexNotifInfo_Type = Unsigned32
_CcsTPIndexNotifInfo_Object = MibScalar
ccsTPIndexNotifInfo = _CcsTPIndexNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 1),
    _CcsTPIndexNotifInfo_Type()
)
ccsTPIndexNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsTPIndexNotifInfo.setStatus("current")


class _CcsServiceNameNotifInfo_Type(OctetString):
    """Custom type ccsServiceNameNotifInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcsServiceNameNotifInfo_Type.__name__ = "OctetString"
_CcsServiceNameNotifInfo_Object = MibScalar
ccsServiceNameNotifInfo = _CcsServiceNameNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 2),
    _CcsServiceNameNotifInfo_Type()
)
ccsServiceNameNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsServiceNameNotifInfo.setStatus("current")


class _CcsContentNameNotifInfo_Type(OctetString):
    """Custom type ccsContentNameNotifInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_CcsContentNameNotifInfo_Type.__name__ = "OctetString"
_CcsContentNameNotifInfo_Object = MibScalar
ccsContentNameNotifInfo = _CcsContentNameNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 3),
    _CcsContentNameNotifInfo_Type()
)
ccsContentNameNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsContentNameNotifInfo.setStatus("current")


class _CcsPolicyNameNotifInfo_Type(OctetString):
    """Custom type ccsPolicyNameNotifInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcsPolicyNameNotifInfo_Type.__name__ = "OctetString"
_CcsPolicyNameNotifInfo_Object = MibScalar
ccsPolicyNameNotifInfo = _CcsPolicyNameNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 4),
    _CcsPolicyNameNotifInfo_Type()
)
ccsPolicyNameNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsPolicyNameNotifInfo.setStatus("current")
_CcsNetServerIpAddrTypeNotifInfo_Type = InetAddressType
_CcsNetServerIpAddrTypeNotifInfo_Object = MibScalar
ccsNetServerIpAddrTypeNotifInfo = _CcsNetServerIpAddrTypeNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 5),
    _CcsNetServerIpAddrTypeNotifInfo_Type()
)
ccsNetServerIpAddrTypeNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsNetServerIpAddrTypeNotifInfo.setStatus("current")
_CcsNetServerIpAddrNotifInfo_Type = InetAddress
_CcsNetServerIpAddrNotifInfo_Object = MibScalar
ccsNetServerIpAddrNotifInfo = _CcsNetServerIpAddrNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 6),
    _CcsNetServerIpAddrNotifInfo_Type()
)
ccsNetServerIpAddrNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsNetServerIpAddrNotifInfo.setStatus("current")
_CcsNetServerPortNotifInfo_Type = InetPortNumber
_CcsNetServerPortNotifInfo_Object = MibScalar
ccsNetServerPortNotifInfo = _CcsNetServerPortNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 7),
    _CcsNetServerPortNotifInfo_Type()
)
ccsNetServerPortNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsNetServerPortNotifInfo.setStatus("current")
_CcsSubscriberIpAddrTypeNotifInfo_Type = InetAddressType
_CcsSubscriberIpAddrTypeNotifInfo_Object = MibScalar
ccsSubscriberIpAddrTypeNotifInfo = _CcsSubscriberIpAddrTypeNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 8),
    _CcsSubscriberIpAddrTypeNotifInfo_Type()
)
ccsSubscriberIpAddrTypeNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsSubscriberIpAddrTypeNotifInfo.setStatus("current")
_CcsSubscriberIpAddrNotifInfo_Type = InetAddress
_CcsSubscriberIpAddrNotifInfo_Object = MibScalar
ccsSubscriberIpAddrNotifInfo = _CcsSubscriberIpAddrNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 9),
    _CcsSubscriberIpAddrNotifInfo_Type()
)
ccsSubscriberIpAddrNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsSubscriberIpAddrNotifInfo.setStatus("current")
_CcsSubscriberPortNotifInfo_Type = InetPortNumber
_CcsSubscriberPortNotifInfo_Object = MibScalar
ccsSubscriberPortNotifInfo = _CcsSubscriberPortNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 10),
    _CcsSubscriberPortNotifInfo_Type()
)
ccsSubscriberPortNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsSubscriberPortNotifInfo.setStatus("current")
_CcsNetServerResponseFailCountNotifInfo_Type = Unsigned32
_CcsNetServerResponseFailCountNotifInfo_Object = MibScalar
ccsNetServerResponseFailCountNotifInfo = _CcsNetServerResponseFailCountNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 11),
    _CcsNetServerResponseFailCountNotifInfo_Type()
)
ccsNetServerResponseFailCountNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsNetServerResponseFailCountNotifInfo.setStatus("current")
_CcsNetServerResponseTimeFailCountNotifInfo_Type = Unsigned32
_CcsNetServerResponseTimeFailCountNotifInfo_Object = MibScalar
ccsNetServerResponseTimeFailCountNotifInfo = _CcsNetServerResponseTimeFailCountNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 12),
    _CcsNetServerResponseTimeFailCountNotifInfo_Type()
)
ccsNetServerResponseTimeFailCountNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsNetServerResponseTimeFailCountNotifInfo.setStatus("current")
_CcsProtocolParseFailCountNotifInfo_Type = Unsigned32
_CcsProtocolParseFailCountNotifInfo_Object = MibScalar
ccsProtocolParseFailCountNotifInfo = _CcsProtocolParseFailCountNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 13),
    _CcsProtocolParseFailCountNotifInfo_Type()
)
ccsProtocolParseFailCountNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsProtocolParseFailCountNotifInfo.setStatus("current")


class _CcsgUserSessionSeverityNotifInfo_Type(Integer32):
    """Custom type ccsgUserSessionSeverityNotifInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("normal", 1),
          ("warning", 2))
    )


_CcsgUserSessionSeverityNotifInfo_Type.__name__ = "Integer32"
_CcsgUserSessionSeverityNotifInfo_Object = MibScalar
ccsgUserSessionSeverityNotifInfo = _CcsgUserSessionSeverityNotifInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 1, 4, 14),
    _CcsgUserSessionSeverityNotifInfo_Type()
)
ccsgUserSessionSeverityNotifInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ccsgUserSessionSeverityNotifInfo.setStatus("current")
_CiscoContentServicesMIBConform_ObjectIdentity = ObjectIdentity
ciscoContentServicesMIBConform = _CiscoContentServicesMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2)
)
_CiscoContentServicesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoContentServicesMIBCompliances = _CiscoContentServicesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1)
)
_CiscoContentServicesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoContentServicesMIBGroups = _CiscoContentServicesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2)
)

# Managed Objects groups

ciscoContentServicesGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 1)
)
ciscoContentServicesGlobalCfgGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgcBMALostRecordTimer"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgcQuotaMgrLostRecordTimer"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalCfgGroup.setStatus("current")

ciscoContentServicesGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 2)
)
ciscoContentServicesGlobalStatsGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserCurrent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionCurrent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionHighWaterResetTime"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalStatsGroup.setStatus("current")

ciscoContentServicesUserDbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 3)
)
ciscoContentServicesUserDbGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbRequests"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbHCRequests"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbUidsReturned"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbHCUidsReturned"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqResent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbHCReqResent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqTimeouts"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbHCReqTimeouts"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqErrors"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbHCReqErrors"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesUserDbGroup.setStatus("current")

ciscoContentServicesBMAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 4)
)
ciscoContentServicesBMAGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsBMAPriority"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMALostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHCLostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMATotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHCTotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHCFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMABadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHCBadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMARetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHCRetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMARowStatus"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesBMAGroup.setStatus("current")

ciscoContentServicesQuotaMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 5)
)
ciscoContentServicesQuotaMgrGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrPriority"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrLostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHCLostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrTotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHCTotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHCFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrBadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHCBadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrRetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHCRetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesQuotaMgrGroup.setStatus("current")

ciscoContentServicesNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 7)
)
ciscoContentServicesNotifEnableGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsBMAStateChangeNotifEnabled"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrStateChangeNotifEnabled"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbStateChangeNotifEnabled"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMALostRecordEventNotifEnabled"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrLostRecordEventNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifEnableGroup.setStatus("current")

ciscoContentServicesLoadStatRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 9)
)
ciscoContentServicesLoadStatRadiusGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatRadiusGroup.setStatus("deprecated")

ciscoContentServicesLoadStatUserDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 10)
)
ciscoContentServicesLoadStatUserDBGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatUserDBGroup.setStatus("deprecated")

ciscoContentServicesLoadStatSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 11)
)
ciscoContentServicesLoadStatSessionGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatSessionGroup.setStatus("deprecated")

ciscoContentServicesLoadStatBMAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 12)
)
ciscoContentServicesLoadStatBMAGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatBMAGroup.setStatus("deprecated")

ciscoContentServicesLoadStatQuotaMgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 13)
)
ciscoContentServicesLoadStatQuotaMgrGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatQuotaMgrGroup.setStatus("deprecated")

ciscoContentServicesGlobalStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 14)
)
ciscoContentServicesGlobalStatsGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPBMARejected"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPBMARejected"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPBMADropped"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPBMADropped"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPBMARetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPBMARetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPQuotaMgrRejected"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPQuotaMgrRejected"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPQuotaMgrDropped"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPQuotaMgrDropped"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPQuotaMgrRetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHCGTPQuotaMgrRetransmit"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPBMARateInterval"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGTPQuotaMgrRateInterval"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalStatsGroupSup1.setStatus("current")

ciscoContentServicesBMAGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 15)
)
ciscoContentServicesBMAGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsBMAPacketRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAAckRate"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesBMAGroupSup1.setStatus("current")

ciscoContentServicesQuotaMgrGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 16)
)
ciscoContentServicesQuotaMgrGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrPacketRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrAckRate"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesQuotaMgrGroupSup1.setStatus("current")

ciscoContentServicesGlobalCfgGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 17)
)
ciscoContentServicesGlobalCfgGroupSup1.setObjects(
    ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserThreshold")
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalCfgGroupSup1.setStatus("current")

ciscoContentServicesNotifEnableGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 18)
)
ciscoContentServicesNotifEnableGroupSup1.setObjects(
    ("CISCO-CONTENT-SERVICES-MIB", "ccsUserThresholdExceededNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifEnableGroupSup1.setStatus("current")

ciscoContentServicesGlobalCfgGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 20)
)
ciscoContentServicesGlobalCfgGroupSup2.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsAdControlAlarmUpdateTimer"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailClearThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerFirstPayloadResponseTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailClearThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalCfgGroupSup2.setStatus("current")

ciscoContentServicesNotifEnableGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 21)
)
ciscoContentServicesNotifEnableGroupSup2.setObjects(
    ("CISCO-CONTENT-SERVICES-MIB", "ccsAdControlNotifEnabled")
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifEnableGroupSup2.setStatus("current")

ciscoContentServicesNotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 23)
)
ciscoContentServicesNotifInfoGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailCountNotifInfo"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifInfoGroup.setStatus("current")

ciscoContentServiceProtocolStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 24)
)
ciscoContentServiceProtocolStatsGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccspsTransaction"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsHCTransaction"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsTransactionRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsTransactionRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsTransactionRateHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsTransactionRateHighWaterTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutPackets"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsHCSubOutPackets"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutPacketRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutPacketRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutPacketRateHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutPacketRateHighWaterTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutPackets"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsHCNetOutPackets"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutPacketRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutPacketRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutPacketRateHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutPacketRateHighWaterTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutBytes"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsHCSubOutBytes"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutBitRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutBitRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutBitRateHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsSubOutBitRateHighWaterTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutBytes"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsHCNetOutBytes"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutBitRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutBitRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutBitRateHighWaterResetTime"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccspsNetOutBitRateHighWaterTime"))
)
if mibBuilder.loadTexts:
    ciscoContentServiceProtocolStatsGroup.setStatus("current")

ciscoContentServicesLoadStatGxEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 25)
)
ciscoContentServicesLoadStatGxEventGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatGxEventGroup.setStatus("deprecated")

ciscoContentServicesBillingPlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 26)
)
ciscoContentServicesBillingPlanStatsGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsbpsSubscribers"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsbpsHCSubscribers"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsbpsSubscribersHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsbpsHCSubscribersHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesBillingPlanStatsGroup.setStatus("current")

ciscoContentServicesLoadStatRadiusGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 27)
)
ciscoContentServicesLoadStatRadiusGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatRadiusStartDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCRadiusStartDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatRadiusGroupSup1.setStatus("current")

ciscoContentServicesLoadStatUserDBGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 28)
)
ciscoContentServicesLoadStatUserDBGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatUserDBReqDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCUserDBReqDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatUserDBGroupSup1.setStatus("current")

ciscoContentServicesLoadStatSessionGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 29)
)
ciscoContentServicesLoadStatSessionGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatSessionCreateDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCSessionCreateDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatSessionGroupSup1.setStatus("current")

ciscoContentServicesLoadStatBMAGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 30)
)
ciscoContentServicesLoadStatBMAGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatBMAMsgsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCBMAMsgsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatBMAGroupSup1.setStatus("current")

ciscoContentServicesLoadStatQuotaMgrGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 31)
)
ciscoContentServicesLoadStatQuotaMgrGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatQuotaMgrMsgsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatQuotaMgrGroupSup1.setStatus("current")

ciscoContentServicesLoadStatGxEventGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 32)
)
ciscoContentServicesLoadStatGxEventGroupSup1.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsAllowed"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsAllowedRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsAllowedRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsIPCQueueDepthTolerance"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsDenied"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsDenialRate"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatGxEventsDenialRateHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsLoadStatHCGxEventsDenialRateHighWater"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesLoadStatGxEventGroupSup1.setStatus("current")

ciscoContentServicesGlobalStatsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 33)
)
ciscoContentServicesGlobalStatsGroupSup2.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsGxRuleActivationFail"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGxRuleDeactivationFail"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGxRevalidationSuccess"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsGxRevalidationFail"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalStatsGroupSup2.setStatus("current")

ciscoContentServicesGlobalHTTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 34)
)
ciscoContentServicesGlobalHTTPGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsHTTPHdrObscure"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsHTTPHdrBlock"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalHTTPGroup.setStatus("current")

ciscoContentServicesGlobalCfgGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 35)
)
ciscoContentServicesGlobalCfgGroupSup3.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserEntriesThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesGlobalCfgGroupSup3.setStatus("current")

ciscoContentServicesNotifEnableGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 36)
)
ciscoContentServicesNotifEnableGroupSup3.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsUserEntriesThresholdNotifEnabled"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSessionThresholdNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifEnableGroupSup3.setStatus("current")

ciscoContentServicesNotifInfoGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 38)
)
ciscoContentServicesNotifInfoGroupSup1.setObjects(
    ("CISCO-CONTENT-SERVICES-MIB", "ccsgUserSessionSeverityNotifInfo")
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifInfoGroupSup1.setStatus("current")


# Notification objects

ciscoContentServicesBMAStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 1)
)
ciscoContentServicesBMAStateChange.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsBMAState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMALostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMATotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMABadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMARetransmit"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesBMAStateChange.setStatus(
        "current"
    )

ciscoContentServicesQuotaMgrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 2)
)
ciscoContentServicesQuotaMgrStateChange.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrLostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrTotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrBadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesQuotaMgrStateChange.setStatus(
        "current"
    )

ciscoContentServicesUserDbStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 3)
)
ciscoContentServicesUserDbStateChange.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbRequests"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbUidsReturned"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqResent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqTimeouts"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsUserDbReqErrors"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesUserDbStateChange.setStatus(
        "current"
    )

ciscoContentServicesBMALostRecordEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 4)
)
ciscoContentServicesBMALostRecordEvent.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsBMAState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMALostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMATotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMAHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMABadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsBMARetransmit"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesBMALostRecordEvent.setStatus(
        "current"
    )

ciscoContentServicesQuotaMgrLostRecordEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 5)
)
ciscoContentServicesQuotaMgrLostRecordEvent.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrState"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrLostRecords"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrTotalSent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrFailAck"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrOutstanding"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrBadRecord"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsQuotaMgrRetransmit"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesQuotaMgrLostRecordEvent.setStatus(
        "current"
    )

ciscoContentServicesUserThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 6)
)
ciscoContentServicesUserThresholdExceeded.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserCurrent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserHighWater"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesUserThresholdExceeded.setStatus(
        "current"
    )

ciscoContentServicesNetServerResponseFailExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 7)
)
ciscoContentServicesNetServerResponseFailExceeded.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNetServerResponseFailExceeded.setStatus(
        "current"
    )

ciscoContentServicesNetServerResponseTimeExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 8)
)
ciscoContentServicesNetServerResponseTimeExceeded.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNetServerResponseTimeExceeded.setStatus(
        "current"
    )

ciscoContentServicesProtocolParseFailExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 9)
)
ciscoContentServicesProtocolParseFailExceeded.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesProtocolParseFailExceeded.setStatus(
        "current"
    )

ciscoContentServicesNetServerResponseFailAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 10)
)
ciscoContentServicesNetServerResponseFailAlarmCleared.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNetServerResponseFailAlarmCleared.setStatus(
        "current"
    )

ciscoContentServicesNetServerResponseTimeAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 11)
)
ciscoContentServicesNetServerResponseTimeAlarmCleared.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerResponseTimeFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNetServerResponseTimeAlarmCleared.setStatus(
        "current"
    )

ciscoContentServicesProtocolParseFailAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 12)
)
ciscoContentServicesProtocolParseFailAlarmCleared.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsServiceNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsContentNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsPolicyNameNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsNetServerPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrTypeNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberIpAddrNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsSubscriberPortNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailCountNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailAlarmThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsProtocolParseFailClearThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesProtocolParseFailAlarmCleared.setStatus(
        "current"
    )

ciscoContentServicesUserEntriesThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 13)
)
ciscoContentServicesUserEntriesThreshold.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserCurrent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsUserEntriesThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgUserSessionSeverityNotifInfo"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesUserEntriesThreshold.setStatus(
        "current"
    )

ciscoContentServicesSessionThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 0, 14)
)
ciscoContentServicesSessionThreshold.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionCurrent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgsSessionThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsgUserSessionSeverityNotifInfo"),
        ("CISCO-CONTENT-SERVICES-MIB", "ccsTPIndexNotifInfo"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesSessionThreshold.setStatus(
        "current"
    )


# Notifications groups

ciscoContentServicesNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 8)
)
ciscoContentServicesNotifGroup.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesBMAStateChange"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesQuotaMgrStateChange"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesUserDbStateChange"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesBMALostRecordEvent"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesQuotaMgrLostRecordEvent"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifGroup.setStatus(
        "current"
    )

ciscoContentServicesNotifGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 19)
)
ciscoContentServicesNotifGroupSup1.setObjects(
    ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesUserThresholdExceeded")
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifGroupSup1.setStatus(
        "current"
    )

ciscoContentServicesNotifGroupSup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 22)
)
ciscoContentServicesNotifGroupSup2.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesNetServerResponseFailExceeded"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesNetServerResponseTimeExceeded"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesProtocolParseFailExceeded"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesNetServerResponseFailAlarmCleared"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesNetServerResponseTimeAlarmCleared"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesProtocolParseFailAlarmCleared"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifGroupSup2.setStatus(
        "current"
    )

ciscoContentServicesNotifGroupSup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 2, 37)
)
ciscoContentServicesNotifGroupSup3.setObjects(
      *(("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesUserEntriesThreshold"),
        ("CISCO-CONTENT-SERVICES-MIB", "ciscoContentServicesSessionThreshold"))
)
if mibBuilder.loadTexts:
    ciscoContentServicesNotifGroupSup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoContentServicesMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBCompliance.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev8.setStatus(
        "deprecated"
    )

ciscoContentServicesMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 597, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ciscoContentServicesMIBComplianceRev9.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CONTENT-SERVICES-MIB",
    **{"CcsServerPriority": CcsServerPriority,
       "ciscoContentServicesMIB": ciscoContentServicesMIB,
       "ciscoContentServicesMIBNotifs": ciscoContentServicesMIBNotifs,
       "ciscoContentServicesBMAStateChange": ciscoContentServicesBMAStateChange,
       "ciscoContentServicesQuotaMgrStateChange": ciscoContentServicesQuotaMgrStateChange,
       "ciscoContentServicesUserDbStateChange": ciscoContentServicesUserDbStateChange,
       "ciscoContentServicesBMALostRecordEvent": ciscoContentServicesBMALostRecordEvent,
       "ciscoContentServicesQuotaMgrLostRecordEvent": ciscoContentServicesQuotaMgrLostRecordEvent,
       "ciscoContentServicesUserThresholdExceeded": ciscoContentServicesUserThresholdExceeded,
       "ciscoContentServicesNetServerResponseFailExceeded": ciscoContentServicesNetServerResponseFailExceeded,
       "ciscoContentServicesNetServerResponseTimeExceeded": ciscoContentServicesNetServerResponseTimeExceeded,
       "ciscoContentServicesProtocolParseFailExceeded": ciscoContentServicesProtocolParseFailExceeded,
       "ciscoContentServicesNetServerResponseFailAlarmCleared": ciscoContentServicesNetServerResponseFailAlarmCleared,
       "ciscoContentServicesNetServerResponseTimeAlarmCleared": ciscoContentServicesNetServerResponseTimeAlarmCleared,
       "ciscoContentServicesProtocolParseFailAlarmCleared": ciscoContentServicesProtocolParseFailAlarmCleared,
       "ciscoContentServicesUserEntriesThreshold": ciscoContentServicesUserEntriesThreshold,
       "ciscoContentServicesSessionThreshold": ciscoContentServicesSessionThreshold,
       "ciscoContentServicesMIBObjects": ciscoContentServicesMIBObjects,
       "ccsConfig": ccsConfig,
       "ccsGlobalCfgTable": ccsGlobalCfgTable,
       "ccsGlobalCfgTableEntry": ccsGlobalCfgTableEntry,
       "ccsgcBMALostRecordTimer": ccsgcBMALostRecordTimer,
       "ccsgcQuotaMgrLostRecordTimer": ccsgcQuotaMgrLostRecordTimer,
       "ccsgsUserThreshold": ccsgsUserThreshold,
       "ccsAdControlAlarmUpdateTimer": ccsAdControlAlarmUpdateTimer,
       "ccsNetServerResponseFailAlarmThreshold": ccsNetServerResponseFailAlarmThreshold,
       "ccsNetServerResponseFailClearThreshold": ccsNetServerResponseFailClearThreshold,
       "ccsNetServerFirstPayloadResponseTime": ccsNetServerFirstPayloadResponseTime,
       "ccsNetServerResponseTimeFailAlarmThreshold": ccsNetServerResponseTimeFailAlarmThreshold,
       "ccsNetServerResponseTimeFailClearThreshold": ccsNetServerResponseTimeFailClearThreshold,
       "ccsProtocolParseFailAlarmThreshold": ccsProtocolParseFailAlarmThreshold,
       "ccsProtocolParseFailClearThreshold": ccsProtocolParseFailClearThreshold,
       "ccsgsUserEntriesThreshold": ccsgsUserEntriesThreshold,
       "ccsgsSessionThreshold": ccsgsSessionThreshold,
       "ccsStats": ccsStats,
       "ccsGlobalStatsTable": ccsGlobalStatsTable,
       "ccsGlobalStatsTableEntry": ccsGlobalStatsTableEntry,
       "ccsgsUserCurrent": ccsgsUserCurrent,
       "ccsgsUserHighWater": ccsgsUserHighWater,
       "ccsgsUserHighWaterResetTime": ccsgsUserHighWaterResetTime,
       "ccsgsSessionCurrent": ccsgsSessionCurrent,
       "ccsgsSessionHighWater": ccsgsSessionHighWater,
       "ccsgsSessionHighWaterResetTime": ccsgsSessionHighWaterResetTime,
       "ccsgsGTPBMARejected": ccsgsGTPBMARejected,
       "ccsgsHCGTPBMARejected": ccsgsHCGTPBMARejected,
       "ccsgsGTPBMADropped": ccsgsGTPBMADropped,
       "ccsgsHCGTPBMADropped": ccsgsHCGTPBMADropped,
       "ccsgsGTPBMARetransmit": ccsgsGTPBMARetransmit,
       "ccsgsHCGTPBMARetransmit": ccsgsHCGTPBMARetransmit,
       "ccsgsGTPQuotaMgrRejected": ccsgsGTPQuotaMgrRejected,
       "ccsgsHCGTPQuotaMgrRejected": ccsgsHCGTPQuotaMgrRejected,
       "ccsgsGTPQuotaMgrDropped": ccsgsGTPQuotaMgrDropped,
       "ccsgsHCGTPQuotaMgrDropped": ccsgsHCGTPQuotaMgrDropped,
       "ccsgsGTPQuotaMgrRetransmit": ccsgsGTPQuotaMgrRetransmit,
       "ccsgsHCGTPQuotaMgrRetransmit": ccsgsHCGTPQuotaMgrRetransmit,
       "ccsgsGTPBMARateInterval": ccsgsGTPBMARateInterval,
       "ccsgsGTPQuotaMgrRateInterval": ccsgsGTPQuotaMgrRateInterval,
       "ccsgsGxRuleActivationFail": ccsgsGxRuleActivationFail,
       "ccsgsGxRuleDeactivationFail": ccsgsGxRuleDeactivationFail,
       "ccsgsGxRevalidationSuccess": ccsgsGxRevalidationSuccess,
       "ccsgsGxRevalidationFail": ccsgsGxRevalidationFail,
       "ccsgsHTTPHdrObscure": ccsgsHTTPHdrObscure,
       "ccsgsHTTPHdrBlock": ccsgsHTTPHdrBlock,
       "ccsUserDbTable": ccsUserDbTable,
       "ccsUserDbTableEntry": ccsUserDbTableEntry,
       "ccsUserDbVrfName": ccsUserDbVrfName,
       "ccsUserDbIpAddrType": ccsUserDbIpAddrType,
       "ccsUserDbIpAddr": ccsUserDbIpAddr,
       "ccsUserDbPort": ccsUserDbPort,
       "ccsUserDbState": ccsUserDbState,
       "ccsUserDbRequests": ccsUserDbRequests,
       "ccsUserDbHCRequests": ccsUserDbHCRequests,
       "ccsUserDbUidsReturned": ccsUserDbUidsReturned,
       "ccsUserDbHCUidsReturned": ccsUserDbHCUidsReturned,
       "ccsUserDbReqResent": ccsUserDbReqResent,
       "ccsUserDbHCReqResent": ccsUserDbHCReqResent,
       "ccsUserDbReqTimeouts": ccsUserDbReqTimeouts,
       "ccsUserDbHCReqTimeouts": ccsUserDbHCReqTimeouts,
       "ccsUserDbReqErrors": ccsUserDbReqErrors,
       "ccsUserDbHCReqErrors": ccsUserDbHCReqErrors,
       "ccsUserDbRowStatus": ccsUserDbRowStatus,
       "ccsBMATable": ccsBMATable,
       "ccsBMATableEntry": ccsBMATableEntry,
       "ccsBMAVrfName": ccsBMAVrfName,
       "ccsBMAIpAddrType": ccsBMAIpAddrType,
       "ccsBMAIpAddr": ccsBMAIpAddr,
       "ccsBMAPort": ccsBMAPort,
       "ccsBMAPriority": ccsBMAPriority,
       "ccsBMAState": ccsBMAState,
       "ccsBMALostRecords": ccsBMALostRecords,
       "ccsBMAHCLostRecords": ccsBMAHCLostRecords,
       "ccsBMATotalSent": ccsBMATotalSent,
       "ccsBMAHCTotalSent": ccsBMAHCTotalSent,
       "ccsBMAFailAck": ccsBMAFailAck,
       "ccsBMAHCFailAck": ccsBMAHCFailAck,
       "ccsBMAOutstanding": ccsBMAOutstanding,
       "ccsBMAHighWater": ccsBMAHighWater,
       "ccsBMAHighWaterResetTime": ccsBMAHighWaterResetTime,
       "ccsBMABadRecord": ccsBMABadRecord,
       "ccsBMAHCBadRecord": ccsBMAHCBadRecord,
       "ccsBMARetransmit": ccsBMARetransmit,
       "ccsBMAHCRetransmit": ccsBMAHCRetransmit,
       "ccsBMARowStatus": ccsBMARowStatus,
       "ccsBMAPacketRate": ccsBMAPacketRate,
       "ccsBMAAckRate": ccsBMAAckRate,
       "ccsQuotaMgrTable": ccsQuotaMgrTable,
       "ccsQuotaMgrTableEntry": ccsQuotaMgrTableEntry,
       "ccsQuotaMgrVrfName": ccsQuotaMgrVrfName,
       "ccsQuotaMgrIpAddrType": ccsQuotaMgrIpAddrType,
       "ccsQuotaMgrIpAddr": ccsQuotaMgrIpAddr,
       "ccsQuotaMgrPort": ccsQuotaMgrPort,
       "ccsQuotaMgrPriority": ccsQuotaMgrPriority,
       "ccsQuotaMgrState": ccsQuotaMgrState,
       "ccsQuotaMgrLostRecords": ccsQuotaMgrLostRecords,
       "ccsQuotaMgrHCLostRecords": ccsQuotaMgrHCLostRecords,
       "ccsQuotaMgrTotalSent": ccsQuotaMgrTotalSent,
       "ccsQuotaMgrHCTotalSent": ccsQuotaMgrHCTotalSent,
       "ccsQuotaMgrFailAck": ccsQuotaMgrFailAck,
       "ccsQuotaMgrHCFailAck": ccsQuotaMgrHCFailAck,
       "ccsQuotaMgrOutstanding": ccsQuotaMgrOutstanding,
       "ccsQuotaMgrHighWater": ccsQuotaMgrHighWater,
       "ccsQuotaMgrHighWaterResetTime": ccsQuotaMgrHighWaterResetTime,
       "ccsQuotaMgrBadRecord": ccsQuotaMgrBadRecord,
       "ccsQuotaMgrHCBadRecord": ccsQuotaMgrHCBadRecord,
       "ccsQuotaMgrRetransmit": ccsQuotaMgrRetransmit,
       "ccsQuotaMgrHCRetransmit": ccsQuotaMgrHCRetransmit,
       "ccsQuotaMgrRowStatus": ccsQuotaMgrRowStatus,
       "ccsQuotaMgrPacketRate": ccsQuotaMgrPacketRate,
       "ccsQuotaMgrAckRate": ccsQuotaMgrAckRate,
       "ccsLoadStatistics": ccsLoadStatistics,
       "ccsLoadStatRadiusTable": ccsLoadStatRadiusTable,
       "ccsLoadStatRadiusEntry": ccsLoadStatRadiusEntry,
       "ccsLoadStatRadiusStartAllowed": ccsLoadStatRadiusStartAllowed,
       "ccsLoadStatHCRadiusStartAllowed": ccsLoadStatHCRadiusStartAllowed,
       "ccsLoadStatRadiusStartAllowedRate": ccsLoadStatRadiusStartAllowedRate,
       "ccsLoadStatRadiusStartAllowedRateHighWater": ccsLoadStatRadiusStartAllowedRateHighWater,
       "ccsLoadStatHCRadiusStartAllowedRateHighWater": ccsLoadStatHCRadiusStartAllowedRateHighWater,
       "ccsLoadStatRadiusStartIPCQueueDepthTolerance": ccsLoadStatRadiusStartIPCQueueDepthTolerance,
       "ccsLoadStatRadiusStartDenied": ccsLoadStatRadiusStartDenied,
       "ccsLoadStatHCRadiusStartDenied": ccsLoadStatHCRadiusStartDenied,
       "ccsLoadStatRadiusStartDenialRate": ccsLoadStatRadiusStartDenialRate,
       "ccsLoadStatRadiusStartDenialRateHighWater": ccsLoadStatRadiusStartDenialRateHighWater,
       "ccsLoadStatHCRadiusStartDenialRateHighWater": ccsLoadStatHCRadiusStartDenialRateHighWater,
       "ccsLoadStatHCRadiusStartAllowedRate": ccsLoadStatHCRadiusStartAllowedRate,
       "ccsLoadStatHCRadiusStartDenialRate": ccsLoadStatHCRadiusStartDenialRate,
       "ccsLoadStatUserDBTable": ccsLoadStatUserDBTable,
       "ccsLoadStatUserDBEntry": ccsLoadStatUserDBEntry,
       "ccsLoadStatUserDBReqAllowed": ccsLoadStatUserDBReqAllowed,
       "ccsLoadStatHCUserDBReqAllowed": ccsLoadStatHCUserDBReqAllowed,
       "ccsLoadStatUserDBReqAllowedRate": ccsLoadStatUserDBReqAllowedRate,
       "ccsLoadStatUserDBReqAllowedRateHighWater": ccsLoadStatUserDBReqAllowedRateHighWater,
       "ccsLoadStatHCUserDBReqAllowedRateHighWater": ccsLoadStatHCUserDBReqAllowedRateHighWater,
       "ccsLoadStatUserDBReqIPCQueueDepthTolerance": ccsLoadStatUserDBReqIPCQueueDepthTolerance,
       "ccsLoadStatUserDBReqDenied": ccsLoadStatUserDBReqDenied,
       "ccsLoadStatHCUserDBReqDenied": ccsLoadStatHCUserDBReqDenied,
       "ccsLoadStatUserDBReqDenialRate": ccsLoadStatUserDBReqDenialRate,
       "ccsLoadStatUserDBReqDenialRateHighWater": ccsLoadStatUserDBReqDenialRateHighWater,
       "ccsLoadStatHCUserDBReqDenialRateHighWater": ccsLoadStatHCUserDBReqDenialRateHighWater,
       "ccsLoadStatHCUserDBReqAllowedRate": ccsLoadStatHCUserDBReqAllowedRate,
       "ccsLoadStatHCUserDBReqDenialRate": ccsLoadStatHCUserDBReqDenialRate,
       "ccsLoadStatSessionTable": ccsLoadStatSessionTable,
       "ccsLoadStatSessionEntry": ccsLoadStatSessionEntry,
       "ccsLoadStatSessionCreateAllowed": ccsLoadStatSessionCreateAllowed,
       "ccsLoadStatHCSessionCreateAllowed": ccsLoadStatHCSessionCreateAllowed,
       "ccsLoadStatSessionCreateAllowedRate": ccsLoadStatSessionCreateAllowedRate,
       "ccsLoadStatSessionCreateAllowedRateHighWater": ccsLoadStatSessionCreateAllowedRateHighWater,
       "ccsLoadStatHCSessionCreateAllowedRateHighWater": ccsLoadStatHCSessionCreateAllowedRateHighWater,
       "ccsLoadStatSessionCreateIPCQueueDepthTolerance": ccsLoadStatSessionCreateIPCQueueDepthTolerance,
       "ccsLoadStatSessionCreateDenied": ccsLoadStatSessionCreateDenied,
       "ccsLoadStatHCSessionCreateDenied": ccsLoadStatHCSessionCreateDenied,
       "ccsLoadStatSessionCreateDenialRate": ccsLoadStatSessionCreateDenialRate,
       "ccsLoadStatSessionCreateDenialRateHighWater": ccsLoadStatSessionCreateDenialRateHighWater,
       "ccsLoadStatHCSessionCreateDenialRateHighWater": ccsLoadStatHCSessionCreateDenialRateHighWater,
       "ccsLoadStatHCSessionCreateAllowedRate": ccsLoadStatHCSessionCreateAllowedRate,
       "ccsLoadStatHCSessionCreateDenialRate": ccsLoadStatHCSessionCreateDenialRate,
       "ccsLoadStatBMATable": ccsLoadStatBMATable,
       "ccsLoadStatBMAEntry": ccsLoadStatBMAEntry,
       "ccsLoadStatBMAMsgsAllowed": ccsLoadStatBMAMsgsAllowed,
       "ccsLoadStatHCBMAMsgsAllowed": ccsLoadStatHCBMAMsgsAllowed,
       "ccsLoadStatBMAMsgsAllowedRate": ccsLoadStatBMAMsgsAllowedRate,
       "ccsLoadStatBMAMsgsAllowedRateHighWater": ccsLoadStatBMAMsgsAllowedRateHighWater,
       "ccsLoadStatHCBMAMsgsAllowedRateHighWater": ccsLoadStatHCBMAMsgsAllowedRateHighWater,
       "ccsLoadStatBMAMsgsIPCQueueDepthTolerance": ccsLoadStatBMAMsgsIPCQueueDepthTolerance,
       "ccsLoadStatBMAMsgsDenied": ccsLoadStatBMAMsgsDenied,
       "ccsLoadStatHCBMAMsgsDenied": ccsLoadStatHCBMAMsgsDenied,
       "ccsLoadStatBMAMsgsDenialRate": ccsLoadStatBMAMsgsDenialRate,
       "ccsLoadStatBMAMsgsDenialRateHighWater": ccsLoadStatBMAMsgsDenialRateHighWater,
       "ccsLoadStatHCBMAMsgsDenialRateHighWater": ccsLoadStatHCBMAMsgsDenialRateHighWater,
       "ccsLoadStatHCBMAMsgsAllowedRate": ccsLoadStatHCBMAMsgsAllowedRate,
       "ccsLoadStatHCBMAMsgsDenialRate": ccsLoadStatHCBMAMsgsDenialRate,
       "ccsLoadStatQuotaMgrTable": ccsLoadStatQuotaMgrTable,
       "ccsLoadStatQuotaMgrEntry": ccsLoadStatQuotaMgrEntry,
       "ccsLoadStatQuotaMgrMsgsAllowed": ccsLoadStatQuotaMgrMsgsAllowed,
       "ccsLoadStatHCQuotaMgrMsgsAllowed": ccsLoadStatHCQuotaMgrMsgsAllowed,
       "ccsLoadStatQuotaMgrMsgsAllowedRate": ccsLoadStatQuotaMgrMsgsAllowedRate,
       "ccsLoadStatQuotaMgrMsgsAllowedRateHighWater": ccsLoadStatQuotaMgrMsgsAllowedRateHighWater,
       "ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater": ccsLoadStatHCQuotaMgrMsgsAllowedRateHighWater,
       "ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance": ccsLoadStatQuotaMgrMsgsIPCQueueDepthTolerance,
       "ccsLoadStatQuotaMgrMsgsDenied": ccsLoadStatQuotaMgrMsgsDenied,
       "ccsLoadStatHCQuotaMgrMsgsDenied": ccsLoadStatHCQuotaMgrMsgsDenied,
       "ccsLoadStatQuotaMgrMsgsDenialRate": ccsLoadStatQuotaMgrMsgsDenialRate,
       "ccsLoadStatQuotaMgrMsgsDenialRateHighWater": ccsLoadStatQuotaMgrMsgsDenialRateHighWater,
       "ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater": ccsLoadStatHCQuotaMgrMsgsDenialRateHighWater,
       "ccsLoadStatHCQuotaMgrMsgsAllowedRate": ccsLoadStatHCQuotaMgrMsgsAllowedRate,
       "ccsLoadStatHCQuotaMgrMsgsDenialRate": ccsLoadStatHCQuotaMgrMsgsDenialRate,
       "ccsLoadStatGxEventTable": ccsLoadStatGxEventTable,
       "ccsLoadStatGxEventEntry": ccsLoadStatGxEventEntry,
       "ccsLoadStatGxEventsAllowed": ccsLoadStatGxEventsAllowed,
       "ccsLoadStatHCGxEventsAllowed": ccsLoadStatHCGxEventsAllowed,
       "ccsLoadStatGxEventsAllowedRate": ccsLoadStatGxEventsAllowedRate,
       "ccsLoadStatGxEventsAllowedRateHighWater": ccsLoadStatGxEventsAllowedRateHighWater,
       "ccsLoadStatHCGxEventsAllowedRateHighWater": ccsLoadStatHCGxEventsAllowedRateHighWater,
       "ccsLoadStatGxEventsIPCQueueDepthTolerance": ccsLoadStatGxEventsIPCQueueDepthTolerance,
       "ccsLoadStatGxEventsDenied": ccsLoadStatGxEventsDenied,
       "ccsLoadStatHCGxEventsDenied": ccsLoadStatHCGxEventsDenied,
       "ccsLoadStatGxEventsDenialRate": ccsLoadStatGxEventsDenialRate,
       "ccsLoadStatGxEventsDenialRateHighWater": ccsLoadStatGxEventsDenialRateHighWater,
       "ccsLoadStatHCGxEventsDenialRateHighWater": ccsLoadStatHCGxEventsDenialRateHighWater,
       "ccsLoadStatHCGxEventsAllowedRate": ccsLoadStatHCGxEventsAllowedRate,
       "ccsLoadStatHCGxEventsDenialRate": ccsLoadStatHCGxEventsDenialRate,
       "ccsProtocolStatsTable": ccsProtocolStatsTable,
       "ccsProtocolStatsEntry": ccsProtocolStatsEntry,
       "ccspsInspectionMethod": ccspsInspectionMethod,
       "ccspsProtocolName": ccspsProtocolName,
       "ccspsTransaction": ccspsTransaction,
       "ccspsHCTransaction": ccspsHCTransaction,
       "ccspsTransactionRate": ccspsTransactionRate,
       "ccspsTransactionRateHighWater": ccspsTransactionRateHighWater,
       "ccspsTransactionRateHighWaterResetTime": ccspsTransactionRateHighWaterResetTime,
       "ccspsTransactionRateHighWaterTime": ccspsTransactionRateHighWaterTime,
       "ccspsSubOutPackets": ccspsSubOutPackets,
       "ccspsHCSubOutPackets": ccspsHCSubOutPackets,
       "ccspsSubOutPacketRate": ccspsSubOutPacketRate,
       "ccspsSubOutPacketRateHighWater": ccspsSubOutPacketRateHighWater,
       "ccspsSubOutPacketRateHighWaterResetTime": ccspsSubOutPacketRateHighWaterResetTime,
       "ccspsSubOutPacketRateHighWaterTime": ccspsSubOutPacketRateHighWaterTime,
       "ccspsNetOutPackets": ccspsNetOutPackets,
       "ccspsHCNetOutPackets": ccspsHCNetOutPackets,
       "ccspsNetOutPacketRate": ccspsNetOutPacketRate,
       "ccspsNetOutPacketRateHighWater": ccspsNetOutPacketRateHighWater,
       "ccspsNetOutPacketRateHighWaterResetTime": ccspsNetOutPacketRateHighWaterResetTime,
       "ccspsNetOutPacketRateHighWaterTime": ccspsNetOutPacketRateHighWaterTime,
       "ccspsSubOutBytes": ccspsSubOutBytes,
       "ccspsHCSubOutBytes": ccspsHCSubOutBytes,
       "ccspsSubOutBitRate": ccspsSubOutBitRate,
       "ccspsSubOutBitRateHighWater": ccspsSubOutBitRateHighWater,
       "ccspsSubOutBitRateHighWaterResetTime": ccspsSubOutBitRateHighWaterResetTime,
       "ccspsSubOutBitRateHighWaterTime": ccspsSubOutBitRateHighWaterTime,
       "ccspsNetOutBytes": ccspsNetOutBytes,
       "ccspsHCNetOutBytes": ccspsHCNetOutBytes,
       "ccspsNetOutBitRate": ccspsNetOutBitRate,
       "ccspsNetOutBitRateHighWater": ccspsNetOutBitRateHighWater,
       "ccspsNetOutBitRateHighWaterResetTime": ccspsNetOutBitRateHighWaterResetTime,
       "ccspsNetOutBitRateHighWaterTime": ccspsNetOutBitRateHighWaterTime,
       "ccsBillingPlanStatsTable": ccsBillingPlanStatsTable,
       "ccsBillingPlanStatsEntry": ccsBillingPlanStatsEntry,
       "ccsbpsBillingPlanName": ccsbpsBillingPlanName,
       "ccsbpsSubscribers": ccsbpsSubscribers,
       "ccsbpsHCSubscribers": ccsbpsHCSubscribers,
       "ccsbpsSubscribersHighWater": ccsbpsSubscribersHighWater,
       "ccsbpsHCSubscribersHighWater": ccsbpsHCSubscribersHighWater,
       "ccsNotifConfig": ccsNotifConfig,
       "ccsNotifCfgTable": ccsNotifCfgTable,
       "ccsNotifCfgTableEntry": ccsNotifCfgTableEntry,
       "ccsBMAStateChangeNotifEnabled": ccsBMAStateChangeNotifEnabled,
       "ccsQuotaMgrStateChangeNotifEnabled": ccsQuotaMgrStateChangeNotifEnabled,
       "ccsUserDbStateChangeNotifEnabled": ccsUserDbStateChangeNotifEnabled,
       "ccsBMALostRecordEventNotifEnabled": ccsBMALostRecordEventNotifEnabled,
       "ccsQuotaMgrLostRecordEventNotifEnabled": ccsQuotaMgrLostRecordEventNotifEnabled,
       "ccsUserThresholdExceededNotifEnabled": ccsUserThresholdExceededNotifEnabled,
       "ccsAdControlNotifEnabled": ccsAdControlNotifEnabled,
       "ccsUserEntriesThresholdNotifEnabled": ccsUserEntriesThresholdNotifEnabled,
       "ccsSessionThresholdNotifEnabled": ccsSessionThresholdNotifEnabled,
       "ccsNotifInfo": ccsNotifInfo,
       "ccsTPIndexNotifInfo": ccsTPIndexNotifInfo,
       "ccsServiceNameNotifInfo": ccsServiceNameNotifInfo,
       "ccsContentNameNotifInfo": ccsContentNameNotifInfo,
       "ccsPolicyNameNotifInfo": ccsPolicyNameNotifInfo,
       "ccsNetServerIpAddrTypeNotifInfo": ccsNetServerIpAddrTypeNotifInfo,
       "ccsNetServerIpAddrNotifInfo": ccsNetServerIpAddrNotifInfo,
       "ccsNetServerPortNotifInfo": ccsNetServerPortNotifInfo,
       "ccsSubscriberIpAddrTypeNotifInfo": ccsSubscriberIpAddrTypeNotifInfo,
       "ccsSubscriberIpAddrNotifInfo": ccsSubscriberIpAddrNotifInfo,
       "ccsSubscriberPortNotifInfo": ccsSubscriberPortNotifInfo,
       "ccsNetServerResponseFailCountNotifInfo": ccsNetServerResponseFailCountNotifInfo,
       "ccsNetServerResponseTimeFailCountNotifInfo": ccsNetServerResponseTimeFailCountNotifInfo,
       "ccsProtocolParseFailCountNotifInfo": ccsProtocolParseFailCountNotifInfo,
       "ccsgUserSessionSeverityNotifInfo": ccsgUserSessionSeverityNotifInfo,
       "ciscoContentServicesMIBConform": ciscoContentServicesMIBConform,
       "ciscoContentServicesMIBCompliances": ciscoContentServicesMIBCompliances,
       "ciscoContentServicesMIBCompliance": ciscoContentServicesMIBCompliance,
       "ciscoContentServicesMIBComplianceRev1": ciscoContentServicesMIBComplianceRev1,
       "ciscoContentServicesMIBComplianceRev2": ciscoContentServicesMIBComplianceRev2,
       "ciscoContentServicesMIBComplianceRev3": ciscoContentServicesMIBComplianceRev3,
       "ciscoContentServicesMIBComplianceRev4": ciscoContentServicesMIBComplianceRev4,
       "ciscoContentServicesMIBComplianceRev5": ciscoContentServicesMIBComplianceRev5,
       "ciscoContentServicesMIBComplianceRev6": ciscoContentServicesMIBComplianceRev6,
       "ciscoContentServicesMIBComplianceRev7": ciscoContentServicesMIBComplianceRev7,
       "ciscoContentServicesMIBComplianceRev8": ciscoContentServicesMIBComplianceRev8,
       "ciscoContentServicesMIBComplianceRev9": ciscoContentServicesMIBComplianceRev9,
       "ciscoContentServicesMIBGroups": ciscoContentServicesMIBGroups,
       "ciscoContentServicesGlobalCfgGroup": ciscoContentServicesGlobalCfgGroup,
       "ciscoContentServicesGlobalStatsGroup": ciscoContentServicesGlobalStatsGroup,
       "ciscoContentServicesUserDbGroup": ciscoContentServicesUserDbGroup,
       "ciscoContentServicesBMAGroup": ciscoContentServicesBMAGroup,
       "ciscoContentServicesQuotaMgrGroup": ciscoContentServicesQuotaMgrGroup,
       "ciscoContentServicesNotifEnableGroup": ciscoContentServicesNotifEnableGroup,
       "ciscoContentServicesNotifGroup": ciscoContentServicesNotifGroup,
       "ciscoContentServicesLoadStatRadiusGroup": ciscoContentServicesLoadStatRadiusGroup,
       "ciscoContentServicesLoadStatUserDBGroup": ciscoContentServicesLoadStatUserDBGroup,
       "ciscoContentServicesLoadStatSessionGroup": ciscoContentServicesLoadStatSessionGroup,
       "ciscoContentServicesLoadStatBMAGroup": ciscoContentServicesLoadStatBMAGroup,
       "ciscoContentServicesLoadStatQuotaMgrGroup": ciscoContentServicesLoadStatQuotaMgrGroup,
       "ciscoContentServicesGlobalStatsGroupSup1": ciscoContentServicesGlobalStatsGroupSup1,
       "ciscoContentServicesBMAGroupSup1": ciscoContentServicesBMAGroupSup1,
       "ciscoContentServicesQuotaMgrGroupSup1": ciscoContentServicesQuotaMgrGroupSup1,
       "ciscoContentServicesGlobalCfgGroupSup1": ciscoContentServicesGlobalCfgGroupSup1,
       "ciscoContentServicesNotifEnableGroupSup1": ciscoContentServicesNotifEnableGroupSup1,
       "ciscoContentServicesNotifGroupSup1": ciscoContentServicesNotifGroupSup1,
       "ciscoContentServicesGlobalCfgGroupSup2": ciscoContentServicesGlobalCfgGroupSup2,
       "ciscoContentServicesNotifEnableGroupSup2": ciscoContentServicesNotifEnableGroupSup2,
       "ciscoContentServicesNotifGroupSup2": ciscoContentServicesNotifGroupSup2,
       "ciscoContentServicesNotifInfoGroup": ciscoContentServicesNotifInfoGroup,
       "ciscoContentServiceProtocolStatsGroup": ciscoContentServiceProtocolStatsGroup,
       "ciscoContentServicesLoadStatGxEventGroup": ciscoContentServicesLoadStatGxEventGroup,
       "ciscoContentServicesBillingPlanStatsGroup": ciscoContentServicesBillingPlanStatsGroup,
       "ciscoContentServicesLoadStatRadiusGroupSup1": ciscoContentServicesLoadStatRadiusGroupSup1,
       "ciscoContentServicesLoadStatUserDBGroupSup1": ciscoContentServicesLoadStatUserDBGroupSup1,
       "ciscoContentServicesLoadStatSessionGroupSup1": ciscoContentServicesLoadStatSessionGroupSup1,
       "ciscoContentServicesLoadStatBMAGroupSup1": ciscoContentServicesLoadStatBMAGroupSup1,
       "ciscoContentServicesLoadStatQuotaMgrGroupSup1": ciscoContentServicesLoadStatQuotaMgrGroupSup1,
       "ciscoContentServicesLoadStatGxEventGroupSup1": ciscoContentServicesLoadStatGxEventGroupSup1,
       "ciscoContentServicesGlobalStatsGroupSup2": ciscoContentServicesGlobalStatsGroupSup2,
       "ciscoContentServicesGlobalHTTPGroup": ciscoContentServicesGlobalHTTPGroup,
       "ciscoContentServicesGlobalCfgGroupSup3": ciscoContentServicesGlobalCfgGroupSup3,
       "ciscoContentServicesNotifEnableGroupSup3": ciscoContentServicesNotifEnableGroupSup3,
       "ciscoContentServicesNotifGroupSup3": ciscoContentServicesNotifGroupSup3,
       "ciscoContentServicesNotifInfoGroupSup1": ciscoContentServicesNotifInfoGroupSup1}
)
