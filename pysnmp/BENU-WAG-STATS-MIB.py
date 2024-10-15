# SNMP MIB module (BENU-WAG-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-WAG-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:04 2024
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

benuWagStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3)
)
benuWagStatsMIB.setRevisions(
        ("1970-01-01 00:00",
         "2017-01-31 00:00",
         "2017-01-20 00:00",
         "2016-07-05 00:00",
         "2016-07-05 00:00",
         "2016-05-30 00:00",
         "2016-05-27 00:00",
         "2016-03-03 00:00",
         "2015-10-05 00:00",
         "2015-09-30 00:00",
         "2015-09-29 00:00",
         "2015-09-26 00:00",
         "2015-09-24 00:00",
         "2015-09-24 00:01",
         "2015-09-22 00:01",
         "2015-09-22 00:00",
         "2015-09-21 00:00",
         "2015-09-15 00:00",
         "2015-09-08 00:00",
         "2015-08-06 00:00",
         "2015-07-15 00:00",
         "2015-06-26 00:00",
         "2015-06-24 00:00",
         "2015-06-12 00:00",
         "2015-05-21 00:00",
         "2015-05-20 00:00",
         "2015-05-12 00:00",
         "2015-04-15 00:00",
         "2015-04-13 00:00",
         "2015-04-12 00:00",
         "2015-03-27 00:00",
         "2015-02-27 00:00",
         "2015-02-25 00:00",
         "2015-02-20 00:00",
         "2015-02-18 00:00",
         "2015-02-17 00:00",
         "2015-02-16 00:00",
         "2015-01-28 00:00",
         "2015-01-12 00:00",
         "2015-01-08 00:00",
         "2015-01-05 00:00",
         "2015-01-02 00:00",
         "2014-09-09 00:00",
         "2014-04-28 00:00",
         "2014-03-05 00:00",
         "2014-02-25 00:00",
         "2014-02-19 00:00",
         "2014-02-14 00:00",
         "2014-01-17 00:00",
         "2014-01-16 00:00",
         "2014-01-09 00:00",
         "2013-12-31 00:00",
         "2013-12-23 00:01",
         "2013-12-17 00:01",
         "2013-12-10 00:01",
         "2013-12-10 00:00",
         "2013-11-29 00:00",
         "2013-11-23 00:00",
         "2013-11-21 00:00",
         "2013-11-13 00:00",
         "2013-09-13 00:00",
         "2016-07-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BWagStatsNotifications_ObjectIdentity = ObjectIdentity
bWagStatsNotifications = _BWagStatsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0)
)
if mibBuilder.loadTexts:
    bWagStatsNotifications.setStatus("current")
_BWagRadiusMIBObjects_ObjectIdentity = ObjectIdentity
bWagRadiusMIBObjects = _BWagRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bWagRadiusMIBObjects.setStatus("current")
_BWagRadiusTable_Object = MibTable
bWagRadiusTable = _BWagRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bWagRadiusTable.setStatus("current")
_BWagRadiusEntry_Object = MibTableRow
bWagRadiusEntry = _BWagRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1)
)
bWagRadiusEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagRadiusStatsInterval"),
)
if mibBuilder.loadTexts:
    bWagRadiusEntry.setStatus("current")
_BWagRadiusStatsInterval_Type = Integer32
_BWagRadiusStatsInterval_Object = MibTableColumn
bWagRadiusStatsInterval = _BWagRadiusStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 1),
    _BWagRadiusStatsInterval_Type()
)
bWagRadiusStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagRadiusStatsInterval.setStatus("current")
_BWagRadiusIntervalDuration_Type = Integer32
_BWagRadiusIntervalDuration_Object = MibTableColumn
bWagRadiusIntervalDuration = _BWagRadiusIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 2),
    _BWagRadiusIntervalDuration_Type()
)
bWagRadiusIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusIntervalDuration.setStatus("current")
_BWagRadiusAuthLatencyMin_Type = Unsigned32
_BWagRadiusAuthLatencyMin_Object = MibTableColumn
bWagRadiusAuthLatencyMin = _BWagRadiusAuthLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 3),
    _BWagRadiusAuthLatencyMin_Type()
)
bWagRadiusAuthLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAuthLatencyMin.setStatus("current")
_BWagRadiusAuthLatencyMax_Type = Unsigned32
_BWagRadiusAuthLatencyMax_Object = MibTableColumn
bWagRadiusAuthLatencyMax = _BWagRadiusAuthLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 4),
    _BWagRadiusAuthLatencyMax_Type()
)
bWagRadiusAuthLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAuthLatencyMax.setStatus("current")
_BWagRadiusAuthLatencyAvg_Type = Unsigned32
_BWagRadiusAuthLatencyAvg_Object = MibTableColumn
bWagRadiusAuthLatencyAvg = _BWagRadiusAuthLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 5),
    _BWagRadiusAuthLatencyAvg_Type()
)
bWagRadiusAuthLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAuthLatencyAvg.setStatus("current")
_BWagRadiusAuthLatencyLast_Type = Unsigned32
_BWagRadiusAuthLatencyLast_Object = MibTableColumn
bWagRadiusAuthLatencyLast = _BWagRadiusAuthLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 6),
    _BWagRadiusAuthLatencyLast_Type()
)
bWagRadiusAuthLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAuthLatencyLast.setStatus("current")
_BWagRadiusAcctLatencyMin_Type = Unsigned32
_BWagRadiusAcctLatencyMin_Object = MibTableColumn
bWagRadiusAcctLatencyMin = _BWagRadiusAcctLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 7),
    _BWagRadiusAcctLatencyMin_Type()
)
bWagRadiusAcctLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctLatencyMin.setStatus("current")
_BWagRadiusAcctLatencyMax_Type = Unsigned32
_BWagRadiusAcctLatencyMax_Object = MibTableColumn
bWagRadiusAcctLatencyMax = _BWagRadiusAcctLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 8),
    _BWagRadiusAcctLatencyMax_Type()
)
bWagRadiusAcctLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctLatencyMax.setStatus("current")
_BWagRadiusAcctLatencyAvg_Type = Unsigned32
_BWagRadiusAcctLatencyAvg_Object = MibTableColumn
bWagRadiusAcctLatencyAvg = _BWagRadiusAcctLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 9),
    _BWagRadiusAcctLatencyAvg_Type()
)
bWagRadiusAcctLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctLatencyAvg.setStatus("current")
_BWagRadiusAcctLatencyLast_Type = Unsigned32
_BWagRadiusAcctLatencyLast_Object = MibTableColumn
bWagRadiusAcctLatencyLast = _BWagRadiusAcctLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 10),
    _BWagRadiusAcctLatencyLast_Type()
)
bWagRadiusAcctLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctLatencyLast.setStatus("current")
_BWagRadiusAccessRequestSent_Type = Unsigned32
_BWagRadiusAccessRequestSent_Object = MibTableColumn
bWagRadiusAccessRequestSent = _BWagRadiusAccessRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 11),
    _BWagRadiusAccessRequestSent_Type()
)
bWagRadiusAccessRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAccessRequestSent.setStatus("current")
_BWagRadiusAccessAcceptReceived_Type = Unsigned32
_BWagRadiusAccessAcceptReceived_Object = MibTableColumn
bWagRadiusAccessAcceptReceived = _BWagRadiusAccessAcceptReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 12),
    _BWagRadiusAccessAcceptReceived_Type()
)
bWagRadiusAccessAcceptReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAccessAcceptReceived.setStatus("current")
_BWagRadiusAccessRejectReceived_Type = Unsigned32
_BWagRadiusAccessRejectReceived_Object = MibTableColumn
bWagRadiusAccessRejectReceived = _BWagRadiusAccessRejectReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 13),
    _BWagRadiusAccessRejectReceived_Type()
)
bWagRadiusAccessRejectReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAccessRejectReceived.setStatus("current")
_BWagRadiusAcctRequestSent_Type = Unsigned32
_BWagRadiusAcctRequestSent_Object = MibTableColumn
bWagRadiusAcctRequestSent = _BWagRadiusAcctRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 14),
    _BWagRadiusAcctRequestSent_Type()
)
bWagRadiusAcctRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctRequestSent.setStatus("current")
_BWagRadiusAcctResponseReceived_Type = Unsigned32
_BWagRadiusAcctResponseReceived_Object = MibTableColumn
bWagRadiusAcctResponseReceived = _BWagRadiusAcctResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 15),
    _BWagRadiusAcctResponseReceived_Type()
)
bWagRadiusAcctResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusAcctResponseReceived.setStatus("current")
_BWagRadiusCoAAckSent_Type = Unsigned32
_BWagRadiusCoAAckSent_Object = MibTableColumn
bWagRadiusCoAAckSent = _BWagRadiusCoAAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 16),
    _BWagRadiusCoAAckSent_Type()
)
bWagRadiusCoAAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoAAckSent.setStatus("current")
_BWagRadiusCoANackSent_Type = Unsigned32
_BWagRadiusCoANackSent_Object = MibTableColumn
bWagRadiusCoANackSent = _BWagRadiusCoANackSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 17),
    _BWagRadiusCoANackSent_Type()
)
bWagRadiusCoANackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoANackSent.setStatus("current")
_BWagRadiusCoARequestReceived_Type = Unsigned32
_BWagRadiusCoARequestReceived_Object = MibTableColumn
bWagRadiusCoARequestReceived = _BWagRadiusCoARequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 18),
    _BWagRadiusCoARequestReceived_Type()
)
bWagRadiusCoARequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoARequestReceived.setStatus("current")
_BWagRadiusCoALatencyMin_Type = Unsigned32
_BWagRadiusCoALatencyMin_Object = MibTableColumn
bWagRadiusCoALatencyMin = _BWagRadiusCoALatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 19),
    _BWagRadiusCoALatencyMin_Type()
)
bWagRadiusCoALatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoALatencyMin.setStatus("current")
_BWagRadiusCoALatencyMax_Type = Unsigned32
_BWagRadiusCoALatencyMax_Object = MibTableColumn
bWagRadiusCoALatencyMax = _BWagRadiusCoALatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 20),
    _BWagRadiusCoALatencyMax_Type()
)
bWagRadiusCoALatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoALatencyMax.setStatus("current")
_BWagRadiusCoALatencyAvg_Type = Unsigned32
_BWagRadiusCoALatencyAvg_Object = MibTableColumn
bWagRadiusCoALatencyAvg = _BWagRadiusCoALatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 21),
    _BWagRadiusCoALatencyAvg_Type()
)
bWagRadiusCoALatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoALatencyAvg.setStatus("current")
_BWagRadiusCoALatencyLast_Type = Unsigned32
_BWagRadiusCoALatencyLast_Object = MibTableColumn
bWagRadiusCoALatencyLast = _BWagRadiusCoALatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 22),
    _BWagRadiusCoALatencyLast_Type()
)
bWagRadiusCoALatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusCoALatencyLast.setStatus("current")
_BWagRadiusDMLatencyMin_Type = Unsigned32
_BWagRadiusDMLatencyMin_Object = MibTableColumn
bWagRadiusDMLatencyMin = _BWagRadiusDMLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 23),
    _BWagRadiusDMLatencyMin_Type()
)
bWagRadiusDMLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMLatencyMin.setStatus("current")
_BWagRadiusDMLatencyMax_Type = Unsigned32
_BWagRadiusDMLatencyMax_Object = MibTableColumn
bWagRadiusDMLatencyMax = _BWagRadiusDMLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 24),
    _BWagRadiusDMLatencyMax_Type()
)
bWagRadiusDMLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMLatencyMax.setStatus("current")
_BWagRadiusDMLatencyAvg_Type = Unsigned32
_BWagRadiusDMLatencyAvg_Object = MibTableColumn
bWagRadiusDMLatencyAvg = _BWagRadiusDMLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 25),
    _BWagRadiusDMLatencyAvg_Type()
)
bWagRadiusDMLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMLatencyAvg.setStatus("current")
_BWagRadiusDMLatencyLast_Type = Unsigned32
_BWagRadiusDMLatencyLast_Object = MibTableColumn
bWagRadiusDMLatencyLast = _BWagRadiusDMLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 26),
    _BWagRadiusDMLatencyLast_Type()
)
bWagRadiusDMLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMLatencyLast.setStatus("current")
_BWagRadiusDMAckSent_Type = Unsigned32
_BWagRadiusDMAckSent_Object = MibTableColumn
bWagRadiusDMAckSent = _BWagRadiusDMAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 27),
    _BWagRadiusDMAckSent_Type()
)
bWagRadiusDMAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMAckSent.setStatus("current")
_BWagRadiusDMNackSent_Type = Unsigned32
_BWagRadiusDMNackSent_Object = MibTableColumn
bWagRadiusDMNackSent = _BWagRadiusDMNackSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 28),
    _BWagRadiusDMNackSent_Type()
)
bWagRadiusDMNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMNackSent.setStatus("current")
_BWagRadiusDMRequestReceived_Type = Unsigned32
_BWagRadiusDMRequestReceived_Object = MibTableColumn
bWagRadiusDMRequestReceived = _BWagRadiusDMRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 1, 1, 1, 29),
    _BWagRadiusDMRequestReceived_Type()
)
bWagRadiusDMRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagRadiusDMRequestReceived.setStatus("current")
_BWagRadiusNotifObjects_ObjectIdentity = ObjectIdentity
bWagRadiusNotifObjects = _BWagRadiusNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bWagRadiusNotifObjects.setStatus("current")
_BWagDhcpMIBObjects_ObjectIdentity = ObjectIdentity
bWagDhcpMIBObjects = _BWagDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    bWagDhcpMIBObjects.setStatus("current")
_BWagDhcpTable_Object = MibTable
bWagDhcpTable = _BWagDhcpTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    bWagDhcpTable.setStatus("current")
_BWagDhcpEntry_Object = MibTableRow
bWagDhcpEntry = _BWagDhcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1)
)
bWagDhcpEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagDhcpStatsInterval"),
)
if mibBuilder.loadTexts:
    bWagDhcpEntry.setStatus("current")
_BWagDhcpStatsInterval_Type = Integer32
_BWagDhcpStatsInterval_Object = MibTableColumn
bWagDhcpStatsInterval = _BWagDhcpStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 1),
    _BWagDhcpStatsInterval_Type()
)
bWagDhcpStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagDhcpStatsInterval.setStatus("current")
_BWagDhcpIntervalDuration_Type = Integer32
_BWagDhcpIntervalDuration_Object = MibTableColumn
bWagDhcpIntervalDuration = _BWagDhcpIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 2),
    _BWagDhcpIntervalDuration_Type()
)
bWagDhcpIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpIntervalDuration.setStatus("current")
_BWagDhcpDiscoverAckIntervalMin_Type = Unsigned32
_BWagDhcpDiscoverAckIntervalMin_Object = MibTableColumn
bWagDhcpDiscoverAckIntervalMin = _BWagDhcpDiscoverAckIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 3),
    _BWagDhcpDiscoverAckIntervalMin_Type()
)
bWagDhcpDiscoverAckIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverAckIntervalMin.setStatus("current")
_BWagDhcpDiscoverAckIntervalMax_Type = Unsigned32
_BWagDhcpDiscoverAckIntervalMax_Object = MibTableColumn
bWagDhcpDiscoverAckIntervalMax = _BWagDhcpDiscoverAckIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 4),
    _BWagDhcpDiscoverAckIntervalMax_Type()
)
bWagDhcpDiscoverAckIntervalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverAckIntervalMax.setStatus("current")
_BWagDhcpDiscoverAckIntervalAvg_Type = Unsigned32
_BWagDhcpDiscoverAckIntervalAvg_Object = MibTableColumn
bWagDhcpDiscoverAckIntervalAvg = _BWagDhcpDiscoverAckIntervalAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 5),
    _BWagDhcpDiscoverAckIntervalAvg_Type()
)
bWagDhcpDiscoverAckIntervalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverAckIntervalAvg.setStatus("current")
_BWagDhcpDiscoverAckIntervalLast_Type = Unsigned32
_BWagDhcpDiscoverAckIntervalLast_Object = MibTableColumn
bWagDhcpDiscoverAckIntervalLast = _BWagDhcpDiscoverAckIntervalLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 6),
    _BWagDhcpDiscoverAckIntervalLast_Type()
)
bWagDhcpDiscoverAckIntervalLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverAckIntervalLast.setStatus("current")
_BWagDhcpRequestAckLatencyMin_Type = Unsigned32
_BWagDhcpRequestAckLatencyMin_Object = MibTableColumn
bWagDhcpRequestAckLatencyMin = _BWagDhcpRequestAckLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 7),
    _BWagDhcpRequestAckLatencyMin_Type()
)
bWagDhcpRequestAckLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpRequestAckLatencyMin.setStatus("current")
_BWagDhcpRequestAckLatencyMax_Type = Unsigned32
_BWagDhcpRequestAckLatencyMax_Object = MibTableColumn
bWagDhcpRequestAckLatencyMax = _BWagDhcpRequestAckLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 8),
    _BWagDhcpRequestAckLatencyMax_Type()
)
bWagDhcpRequestAckLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpRequestAckLatencyMax.setStatus("current")
_BWagDhcpRequestAckLatencyAvg_Type = Unsigned32
_BWagDhcpRequestAckLatencyAvg_Object = MibTableColumn
bWagDhcpRequestAckLatencyAvg = _BWagDhcpRequestAckLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 9),
    _BWagDhcpRequestAckLatencyAvg_Type()
)
bWagDhcpRequestAckLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpRequestAckLatencyAvg.setStatus("current")
_BWagDhcpRequestAckLatencyLast_Type = Unsigned32
_BWagDhcpRequestAckLatencyLast_Object = MibTableColumn
bWagDhcpRequestAckLatencyLast = _BWagDhcpRequestAckLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 10),
    _BWagDhcpRequestAckLatencyLast_Type()
)
bWagDhcpRequestAckLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpRequestAckLatencyLast.setStatus("current")
_BWagDhcpDiscoverOfferLatencyMin_Type = Unsigned32
_BWagDhcpDiscoverOfferLatencyMin_Object = MibTableColumn
bWagDhcpDiscoverOfferLatencyMin = _BWagDhcpDiscoverOfferLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 11),
    _BWagDhcpDiscoverOfferLatencyMin_Type()
)
bWagDhcpDiscoverOfferLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverOfferLatencyMin.setStatus("current")
_BWagDhcpDiscoverOfferLatencyMax_Type = Unsigned32
_BWagDhcpDiscoverOfferLatencyMax_Object = MibTableColumn
bWagDhcpDiscoverOfferLatencyMax = _BWagDhcpDiscoverOfferLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 12),
    _BWagDhcpDiscoverOfferLatencyMax_Type()
)
bWagDhcpDiscoverOfferLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverOfferLatencyMax.setStatus("current")
_BWagDhcpDiscoverOfferLatencyAvg_Type = Unsigned32
_BWagDhcpDiscoverOfferLatencyAvg_Object = MibTableColumn
bWagDhcpDiscoverOfferLatencyAvg = _BWagDhcpDiscoverOfferLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 13),
    _BWagDhcpDiscoverOfferLatencyAvg_Type()
)
bWagDhcpDiscoverOfferLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverOfferLatencyAvg.setStatus("current")
_BWagDhcpDiscoverOfferLatencyLast_Type = Unsigned32
_BWagDhcpDiscoverOfferLatencyLast_Object = MibTableColumn
bWagDhcpDiscoverOfferLatencyLast = _BWagDhcpDiscoverOfferLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 14),
    _BWagDhcpDiscoverOfferLatencyLast_Type()
)
bWagDhcpDiscoverOfferLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverOfferLatencyLast.setStatus("current")
_BWagDhcpDiscoverReceived_Type = Unsigned32
_BWagDhcpDiscoverReceived_Object = MibTableColumn
bWagDhcpDiscoverReceived = _BWagDhcpDiscoverReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 15),
    _BWagDhcpDiscoverReceived_Type()
)
bWagDhcpDiscoverReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpDiscoverReceived.setStatus("current")
_BWagDhcpOfferSent_Type = Unsigned32
_BWagDhcpOfferSent_Object = MibTableColumn
bWagDhcpOfferSent = _BWagDhcpOfferSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 16),
    _BWagDhcpOfferSent_Type()
)
bWagDhcpOfferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpOfferSent.setStatus("current")
_BWagDhcpRequestReceived_Type = Unsigned32
_BWagDhcpRequestReceived_Object = MibTableColumn
bWagDhcpRequestReceived = _BWagDhcpRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 17),
    _BWagDhcpRequestReceived_Type()
)
bWagDhcpRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpRequestReceived.setStatus("current")
_BWagDhcpAckSent_Type = Unsigned32
_BWagDhcpAckSent_Object = MibTableColumn
bWagDhcpAckSent = _BWagDhcpAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 18),
    _BWagDhcpAckSent_Type()
)
bWagDhcpAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpAckSent.setStatus("current")
_BWagDhcpNackSent_Type = Unsigned32
_BWagDhcpNackSent_Object = MibTableColumn
bWagDhcpNackSent = _BWagDhcpNackSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 19),
    _BWagDhcpNackSent_Type()
)
bWagDhcpNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpNackSent.setStatus("current")
_BWagDhcpOfferRequestIntervalMin_Type = Unsigned32
_BWagDhcpOfferRequestIntervalMin_Object = MibTableColumn
bWagDhcpOfferRequestIntervalMin = _BWagDhcpOfferRequestIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 20),
    _BWagDhcpOfferRequestIntervalMin_Type()
)
bWagDhcpOfferRequestIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpOfferRequestIntervalMin.setStatus("current")
_BWagDhcpOfferRequestIntervalMax_Type = Unsigned32
_BWagDhcpOfferRequestIntervalMax_Object = MibTableColumn
bWagDhcpOfferRequestIntervalMax = _BWagDhcpOfferRequestIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 21),
    _BWagDhcpOfferRequestIntervalMax_Type()
)
bWagDhcpOfferRequestIntervalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpOfferRequestIntervalMax.setStatus("current")
_BWagDhcpOfferRequestIntervalAvg_Type = Unsigned32
_BWagDhcpOfferRequestIntervalAvg_Object = MibTableColumn
bWagDhcpOfferRequestIntervalAvg = _BWagDhcpOfferRequestIntervalAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 22),
    _BWagDhcpOfferRequestIntervalAvg_Type()
)
bWagDhcpOfferRequestIntervalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpOfferRequestIntervalAvg.setStatus("current")
_BWagDhcpOfferRequestIntervalLast_Type = Unsigned32
_BWagDhcpOfferRequestIntervalLast_Object = MibTableColumn
bWagDhcpOfferRequestIntervalLast = _BWagDhcpOfferRequestIntervalLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 1, 1, 23),
    _BWagDhcpOfferRequestIntervalLast_Type()
)
bWagDhcpOfferRequestIntervalLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpOfferRequestIntervalLast.setStatus("current")
_BWagDhcpTPSTable_Object = MibTable
bWagDhcpTPSTable = _BWagDhcpTPSTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    bWagDhcpTPSTable.setStatus("current")
_BWagDhcpTPSEntry_Object = MibTableRow
bWagDhcpTPSEntry = _BWagDhcpTPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1)
)
bWagDhcpTPSEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagDhcpTPSInterval"),
)
if mibBuilder.loadTexts:
    bWagDhcpTPSEntry.setStatus("current")
_BWagDhcpTPSInterval_Type = Integer32
_BWagDhcpTPSInterval_Object = MibTableColumn
bWagDhcpTPSInterval = _BWagDhcpTPSInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1, 1),
    _BWagDhcpTPSInterval_Type()
)
bWagDhcpTPSInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagDhcpTPSInterval.setStatus("current")
_BWagDhcpTPSIntervalDuration_Type = Unsigned32
_BWagDhcpTPSIntervalDuration_Object = MibTableColumn
bWagDhcpTPSIntervalDuration = _BWagDhcpTPSIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1, 2),
    _BWagDhcpTPSIntervalDuration_Type()
)
bWagDhcpTPSIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpTPSIntervalDuration.setStatus("current")
_BWagDhcpTPSLow_Type = Unsigned32
_BWagDhcpTPSLow_Object = MibTableColumn
bWagDhcpTPSLow = _BWagDhcpTPSLow_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1, 3),
    _BWagDhcpTPSLow_Type()
)
bWagDhcpTPSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpTPSLow.setStatus("current")
_BWagDhcpTPSHigh_Type = Unsigned32
_BWagDhcpTPSHigh_Object = MibTableColumn
bWagDhcpTPSHigh = _BWagDhcpTPSHigh_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1, 4),
    _BWagDhcpTPSHigh_Type()
)
bWagDhcpTPSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpTPSHigh.setStatus("current")
_BWagDhcpTPS_Type = Unsigned32
_BWagDhcpTPS_Object = MibTableColumn
bWagDhcpTPS = _BWagDhcpTPS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 3, 2, 1, 5),
    _BWagDhcpTPS_Type()
)
bWagDhcpTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDhcpTPS.setStatus("current")
_BWagDhcpNotifObjects_ObjectIdentity = ObjectIdentity
bWagDhcpNotifObjects = _BWagDhcpNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    bWagDhcpNotifObjects.setStatus("current")
_BWagSubscriberMIBObjects_ObjectIdentity = ObjectIdentity
bWagSubscriberMIBObjects = _BWagSubscriberMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    bWagSubscriberMIBObjects.setStatus("current")
_BWagSubscriberTable_Object = MibTable
bWagSubscriberTable = _BWagSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    bWagSubscriberTable.setStatus("current")
_BWagSubscriberEntry_Object = MibTableRow
bWagSubscriberEntry = _BWagSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1)
)
bWagSubscriberEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagSubscriberStatsInterval"),
)
if mibBuilder.loadTexts:
    bWagSubscriberEntry.setStatus("current")
_BWagSubscriberStatsInterval_Type = Integer32
_BWagSubscriberStatsInterval_Object = MibTableColumn
bWagSubscriberStatsInterval = _BWagSubscriberStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 1),
    _BWagSubscriberStatsInterval_Type()
)
bWagSubscriberStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagSubscriberStatsInterval.setStatus("current")
_BWagSubscriberIntervalDuration_Type = Integer32
_BWagSubscriberIntervalDuration_Object = MibTableColumn
bWagSubscriberIntervalDuration = _BWagSubscriberIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 2),
    _BWagSubscriberIntervalDuration_Type()
)
bWagSubscriberIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberIntervalDuration.setStatus("current")
_BWagSubscriberActivationsCount_Type = Unsigned32
_BWagSubscriberActivationsCount_Object = MibTableColumn
bWagSubscriberActivationsCount = _BWagSubscriberActivationsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 3),
    _BWagSubscriberActivationsCount_Type()
)
bWagSubscriberActivationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberActivationsCount.setStatus("current")
_BWagSubscriberDeletionsCount_Type = Unsigned32
_BWagSubscriberDeletionsCount_Object = MibTableColumn
bWagSubscriberDeletionsCount = _BWagSubscriberDeletionsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 4),
    _BWagSubscriberDeletionsCount_Type()
)
bWagSubscriberDeletionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberDeletionsCount.setStatus("current")
_BWagSubscriberAuthenticationsCount_Type = Unsigned32
_BWagSubscriberAuthenticationsCount_Object = MibTableColumn
bWagSubscriberAuthenticationsCount = _BWagSubscriberAuthenticationsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 5),
    _BWagSubscriberAuthenticationsCount_Type()
)
bWagSubscriberAuthenticationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAuthenticationsCount.setStatus("current")
_BWagSubscriberRedirectionsCount_Type = Unsigned32
_BWagSubscriberRedirectionsCount_Object = MibTableColumn
bWagSubscriberRedirectionsCount = _BWagSubscriberRedirectionsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 6),
    _BWagSubscriberRedirectionsCount_Type()
)
bWagSubscriberRedirectionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberRedirectionsCount.setStatus("current")
_BWagSubscriberRedirectionsByAcl_Type = Unsigned32
_BWagSubscriberRedirectionsByAcl_Object = MibTableColumn
bWagSubscriberRedirectionsByAcl = _BWagSubscriberRedirectionsByAcl_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 7),
    _BWagSubscriberRedirectionsByAcl_Type()
)
bWagSubscriberRedirectionsByAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberRedirectionsByAcl.setStatus("obsolete")
_BWagSubscriberAPMobilityOccurencesCount_Type = Unsigned32
_BWagSubscriberAPMobilityOccurencesCount_Object = MibTableColumn
bWagSubscriberAPMobilityOccurencesCount = _BWagSubscriberAPMobilityOccurencesCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 8),
    _BWagSubscriberAPMobilityOccurencesCount_Type()
)
bWagSubscriberAPMobilityOccurencesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAPMobilityOccurencesCount.setStatus("current")
_BWagSubscriberDeletionsByDMCount_Type = Unsigned32
_BWagSubscriberDeletionsByDMCount_Object = MibTableColumn
bWagSubscriberDeletionsByDMCount = _BWagSubscriberDeletionsByDMCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 9),
    _BWagSubscriberDeletionsByDMCount_Type()
)
bWagSubscriberDeletionsByDMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberDeletionsByDMCount.setStatus("current")
_BWagSubscriberIdleTimeoutCount_Type = Unsigned32
_BWagSubscriberIdleTimeoutCount_Object = MibTableColumn
bWagSubscriberIdleTimeoutCount = _BWagSubscriberIdleTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 10),
    _BWagSubscriberIdleTimeoutCount_Type()
)
bWagSubscriberIdleTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberIdleTimeoutCount.setStatus("current")
_BWagSubscriberSessionTimeoutPreauthCount_Type = Unsigned32
_BWagSubscriberSessionTimeoutPreauthCount_Object = MibTableColumn
bWagSubscriberSessionTimeoutPreauthCount = _BWagSubscriberSessionTimeoutPreauthCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 11),
    _BWagSubscriberSessionTimeoutPreauthCount_Type()
)
bWagSubscriberSessionTimeoutPreauthCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberSessionTimeoutPreauthCount.setStatus("current")
_BWagSubscriberSessionTimeoutAuthviaportalCount_Type = Unsigned32
_BWagSubscriberSessionTimeoutAuthviaportalCount_Object = MibTableColumn
bWagSubscriberSessionTimeoutAuthviaportalCount = _BWagSubscriberSessionTimeoutAuthviaportalCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 12),
    _BWagSubscriberSessionTimeoutAuthviaportalCount_Type()
)
bWagSubscriberSessionTimeoutAuthviaportalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberSessionTimeoutAuthviaportalCount.setStatus("current")
_BWagSubscriberDroppedByLicenseManagerCount_Type = Unsigned32
_BWagSubscriberDroppedByLicenseManagerCount_Object = MibTableColumn
bWagSubscriberDroppedByLicenseManagerCount = _BWagSubscriberDroppedByLicenseManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 13),
    _BWagSubscriberDroppedByLicenseManagerCount_Type()
)
bWagSubscriberDroppedByLicenseManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberDroppedByLicenseManagerCount.setStatus("current")
_BWagSubscriberThrottlingOccurrencesCount_Type = Unsigned32
_BWagSubscriberThrottlingOccurrencesCount_Object = MibTableColumn
bWagSubscriberThrottlingOccurrencesCount = _BWagSubscriberThrottlingOccurrencesCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 14),
    _BWagSubscriberThrottlingOccurrencesCount_Type()
)
bWagSubscriberThrottlingOccurrencesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberThrottlingOccurrencesCount.setStatus("obsolete")
_BWagSubscriberThrottledCount_Type = Unsigned32
_BWagSubscriberThrottledCount_Object = MibTableColumn
bWagSubscriberThrottledCount = _BWagSubscriberThrottledCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 15),
    _BWagSubscriberThrottledCount_Type()
)
bWagSubscriberThrottledCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberThrottledCount.setStatus("obsolete")
_BWagSubscriberAbsoluteTimeoutCount_Type = Unsigned32
_BWagSubscriberAbsoluteTimeoutCount_Object = MibTableColumn
bWagSubscriberAbsoluteTimeoutCount = _BWagSubscriberAbsoluteTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 16),
    _BWagSubscriberAbsoluteTimeoutCount_Type()
)
bWagSubscriberAbsoluteTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAbsoluteTimeoutCount.setStatus("current")
_BWagSubscriberAuthsViaPortalCount_Type = Unsigned32
_BWagSubscriberAuthsViaPortalCount_Object = MibTableColumn
bWagSubscriberAuthsViaPortalCount = _BWagSubscriberAuthsViaPortalCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 17),
    _BWagSubscriberAuthsViaPortalCount_Type()
)
bWagSubscriberAuthsViaPortalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAuthsViaPortalCount.setStatus("current")
_BWagSubscriberAuthenticationsCountVia8021x_Type = Unsigned32
_BWagSubscriberAuthenticationsCountVia8021x_Object = MibTableColumn
bWagSubscriberAuthenticationsCountVia8021x = _BWagSubscriberAuthenticationsCountVia8021x_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 18),
    _BWagSubscriberAuthenticationsCountVia8021x_Type()
)
bWagSubscriberAuthenticationsCountVia8021x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAuthenticationsCountVia8021x.setStatus("current")
_BWagSubscriberAuthenticationsCountViaSingleStatic_Type = Unsigned32
_BWagSubscriberAuthenticationsCountViaSingleStatic_Object = MibTableColumn
bWagSubscriberAuthenticationsCountViaSingleStatic = _BWagSubscriberAuthenticationsCountViaSingleStatic_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 19),
    _BWagSubscriberAuthenticationsCountViaSingleStatic_Type()
)
bWagSubscriberAuthenticationsCountViaSingleStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAuthenticationsCountViaSingleStatic.setStatus("current")
_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Type = Unsigned32
_BWagSubscriberAuthenticationsCountViaRoutedSubnet_Object = MibTableColumn
bWagSubscriberAuthenticationsCountViaRoutedSubnet = _BWagSubscriberAuthenticationsCountViaRoutedSubnet_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 20),
    _BWagSubscriberAuthenticationsCountViaRoutedSubnet_Type()
)
bWagSubscriberAuthenticationsCountViaRoutedSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberAuthenticationsCountViaRoutedSubnet.setStatus("current")
_BWagSubscriberSessionTimeoutAuthVia8021x_Type = Unsigned32
_BWagSubscriberSessionTimeoutAuthVia8021x_Object = MibTableColumn
bWagSubscriberSessionTimeoutAuthVia8021x = _BWagSubscriberSessionTimeoutAuthVia8021x_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 21),
    _BWagSubscriberSessionTimeoutAuthVia8021x_Type()
)
bWagSubscriberSessionTimeoutAuthVia8021x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberSessionTimeoutAuthVia8021x.setStatus("current")
_BWagSubscriberHomeTotalSubsDeleted_Type = Unsigned32
_BWagSubscriberHomeTotalSubsDeleted_Object = MibTableColumn
bWagSubscriberHomeTotalSubsDeleted = _BWagSubscriberHomeTotalSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 22),
    _BWagSubscriberHomeTotalSubsDeleted_Type()
)
bWagSubscriberHomeTotalSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeTotalSubsDeleted.setStatus("current")
_BWagSubscriberHomeTransientSubsDeleted_Type = Unsigned32
_BWagSubscriberHomeTransientSubsDeleted_Object = MibTableColumn
bWagSubscriberHomeTransientSubsDeleted = _BWagSubscriberHomeTransientSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 23),
    _BWagSubscriberHomeTransientSubsDeleted_Type()
)
bWagSubscriberHomeTransientSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeTransientSubsDeleted.setStatus("current")
_BWagSubscriberHomeUserStaticSubsDeleted_Type = Unsigned32
_BWagSubscriberHomeUserStaticSubsDeleted_Object = MibTableColumn
bWagSubscriberHomeUserStaticSubsDeleted = _BWagSubscriberHomeUserStaticSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 24),
    _BWagSubscriberHomeUserStaticSubsDeleted_Type()
)
bWagSubscriberHomeUserStaticSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeUserStaticSubsDeleted.setStatus("current")
_BWagSubscriberHomeDhcpStaticSubsDeleted_Type = Unsigned32
_BWagSubscriberHomeDhcpStaticSubsDeleted_Object = MibTableColumn
bWagSubscriberHomeDhcpStaticSubsDeleted = _BWagSubscriberHomeDhcpStaticSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 25),
    _BWagSubscriberHomeDhcpStaticSubsDeleted_Type()
)
bWagSubscriberHomeDhcpStaticSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeDhcpStaticSubsDeleted.setStatus("current")
_BWagSubscriberHomeDhcpDynSubsDeleted_Type = Unsigned32
_BWagSubscriberHomeDhcpDynSubsDeleted_Object = MibTableColumn
bWagSubscriberHomeDhcpDynSubsDeleted = _BWagSubscriberHomeDhcpDynSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 26),
    _BWagSubscriberHomeDhcpDynSubsDeleted_Type()
)
bWagSubscriberHomeDhcpDynSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeDhcpDynSubsDeleted.setStatus("current")
_BWagSubscriberHomePubStaticSubsDeleted_Type = Unsigned32
_BWagSubscriberHomePubStaticSubsDeleted_Object = MibTableColumn
bWagSubscriberHomePubStaticSubsDeleted = _BWagSubscriberHomePubStaticSubsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 27),
    _BWagSubscriberHomePubStaticSubsDeleted_Type()
)
bWagSubscriberHomePubStaticSubsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomePubStaticSubsDeleted.setStatus("current")
_BWagSubscriberSpWifiActivationsCount_Type = Unsigned32
_BWagSubscriberSpWifiActivationsCount_Object = MibTableColumn
bWagSubscriberSpWifiActivationsCount = _BWagSubscriberSpWifiActivationsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 28),
    _BWagSubscriberSpWifiActivationsCount_Type()
)
bWagSubscriberSpWifiActivationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberSpWifiActivationsCount.setStatus("current")
_BWagSubscriberHomeActivationsCount_Type = Unsigned32
_BWagSubscriberHomeActivationsCount_Object = MibTableColumn
bWagSubscriberHomeActivationsCount = _BWagSubscriberHomeActivationsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 29),
    _BWagSubscriberHomeActivationsCount_Type()
)
bWagSubscriberHomeActivationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberHomeActivationsCount.setStatus("current")
_BWagSubscriberDsLiteActivationsCount_Type = Unsigned32
_BWagSubscriberDsLiteActivationsCount_Object = MibTableColumn
bWagSubscriberDsLiteActivationsCount = _BWagSubscriberDsLiteActivationsCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 1, 1, 30),
    _BWagSubscriberDsLiteActivationsCount_Type()
)
bWagSubscriberDsLiteActivationsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagSubscriberDsLiteActivationsCount.setStatus("current")
_BWagNumCurrentSubscribers_Type = Unsigned32
_BWagNumCurrentSubscribers_Object = MibScalar
bWagNumCurrentSubscribers = _BWagNumCurrentSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 2),
    _BWagNumCurrentSubscribers_Type()
)
bWagNumCurrentSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentSubscribers.setStatus("current")
_BWagNumAuthenticatedSubscribers_Type = Unsigned32
_BWagNumAuthenticatedSubscribers_Object = MibScalar
bWagNumAuthenticatedSubscribers = _BWagNumAuthenticatedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 3),
    _BWagNumAuthenticatedSubscribers_Type()
)
bWagNumAuthenticatedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumAuthenticatedSubscribers.setStatus("current")
_BWagNumUnauthenticatedSubscribers_Type = Unsigned32
_BWagNumUnauthenticatedSubscribers_Object = MibScalar
bWagNumUnauthenticatedSubscribers = _BWagNumUnauthenticatedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 4),
    _BWagNumUnauthenticatedSubscribers_Type()
)
bWagNumUnauthenticatedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumUnauthenticatedSubscribers.setStatus("current")
_BWagNumSubsWithPrivateIPAddress_Type = Unsigned32
_BWagNumSubsWithPrivateIPAddress_Object = MibScalar
bWagNumSubsWithPrivateIPAddress = _BWagNumSubsWithPrivateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 5),
    _BWagNumSubsWithPrivateIPAddress_Type()
)
bWagNumSubsWithPrivateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumSubsWithPrivateIPAddress.setStatus("current")
_BWagNumAuthSubsWithPublicIPAddress_Type = Unsigned32
_BWagNumAuthSubsWithPublicIPAddress_Object = MibScalar
bWagNumAuthSubsWithPublicIPAddress = _BWagNumAuthSubsWithPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 6),
    _BWagNumAuthSubsWithPublicIPAddress_Type()
)
bWagNumAuthSubsWithPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumAuthSubsWithPublicIPAddress.setStatus("current")
_BWagNumUnAuthSubsWithPublicIPAddress_Type = Unsigned32
_BWagNumUnAuthSubsWithPublicIPAddress_Object = MibScalar
bWagNumUnAuthSubsWithPublicIPAddress = _BWagNumUnAuthSubsWithPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 7),
    _BWagNumUnAuthSubsWithPublicIPAddress_Type()
)
bWagNumUnAuthSubsWithPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumUnAuthSubsWithPublicIPAddress.setStatus("current")
_BWagNumMigrantSubscribersCount_Type = Unsigned32
_BWagNumMigrantSubscribersCount_Object = MibScalar
bWagNumMigrantSubscribersCount = _BWagNumMigrantSubscribersCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 8),
    _BWagNumMigrantSubscribersCount_Type()
)
bWagNumMigrantSubscribersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumMigrantSubscribersCount.setStatus("current")
_BWagNumRedirectedSubscribersCount_Type = Unsigned32
_BWagNumRedirectedSubscribersCount_Object = MibScalar
bWagNumRedirectedSubscribersCount = _BWagNumRedirectedSubscribersCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 9),
    _BWagNumRedirectedSubscribersCount_Type()
)
bWagNumRedirectedSubscribersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumRedirectedSubscribersCount.setStatus("current")
_BWagPolicyTable_Object = MibTable
bWagPolicyTable = _BWagPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10)
)
if mibBuilder.loadTexts:
    bWagPolicyTable.setStatus("current")
_BWagPolicyEntry_Object = MibTableRow
bWagPolicyEntry = _BWagPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1)
)
bWagPolicyEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagPolicyType"),
    (0, "BENU-WAG-STATS-MIB", "bWagPolicyIndex"),
)
if mibBuilder.loadTexts:
    bWagPolicyEntry.setStatus("current")


class _BWagPolicyType_Type(Integer32):
    """Custom type bWagPolicyType based on Integer32"""
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
        *(("acl", 3),
          ("li", 2),
          ("none", 0),
          ("qos", 1))
    )


_BWagPolicyType_Type.__name__ = "Integer32"
_BWagPolicyType_Object = MibTableColumn
bWagPolicyType = _BWagPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 1),
    _BWagPolicyType_Type()
)
bWagPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagPolicyType.setStatus("current")
_BWagPolicyIndex_Type = Integer32
_BWagPolicyIndex_Object = MibTableColumn
bWagPolicyIndex = _BWagPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 2),
    _BWagPolicyIndex_Type()
)
bWagPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagPolicyIndex.setStatus("current")
_BWagPolicyName_Type = DisplayString
_BWagPolicyName_Object = MibTableColumn
bWagPolicyName = _BWagPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 3),
    _BWagPolicyName_Type()
)
bWagPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagPolicyName.setStatus("current")
_BWagNumOfSubscribersWithPolicy_Type = Unsigned32
_BWagNumOfSubscribersWithPolicy_Object = MibTableColumn
bWagNumOfSubscribersWithPolicy = _BWagNumOfSubscribersWithPolicy_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 4),
    _BWagNumOfSubscribersWithPolicy_Type()
)
bWagNumOfSubscribersWithPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumOfSubscribersWithPolicy.setStatus("current")
_BWagNumOfAuthSubscribersWithPolicy_Type = Unsigned32
_BWagNumOfAuthSubscribersWithPolicy_Object = MibTableColumn
bWagNumOfAuthSubscribersWithPolicy = _BWagNumOfAuthSubscribersWithPolicy_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 5),
    _BWagNumOfAuthSubscribersWithPolicy_Type()
)
bWagNumOfAuthSubscribersWithPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumOfAuthSubscribersWithPolicy.setStatus("current")
_BWagNumOfUnAuthSubscribersWithPolicy_Type = Unsigned32
_BWagNumOfUnAuthSubscribersWithPolicy_Object = MibTableColumn
bWagNumOfUnAuthSubscribersWithPolicy = _BWagNumOfUnAuthSubscribersWithPolicy_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 10, 1, 6),
    _BWagNumOfUnAuthSubscribersWithPolicy_Type()
)
bWagNumOfUnAuthSubscribersWithPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumOfUnAuthSubscribersWithPolicy.setStatus("current")
_BWagNumSubsAuthenticatedWithIPv6Prefix_Type = Unsigned32
_BWagNumSubsAuthenticatedWithIPv6Prefix_Object = MibScalar
bWagNumSubsAuthenticatedWithIPv6Prefix = _BWagNumSubsAuthenticatedWithIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 11),
    _BWagNumSubsAuthenticatedWithIPv6Prefix_Type()
)
bWagNumSubsAuthenticatedWithIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumSubsAuthenticatedWithIPv6Prefix.setStatus("current")
_BWagNumCurrent8021xSubscribers_Type = Unsigned32
_BWagNumCurrent8021xSubscribers_Object = MibScalar
bWagNumCurrent8021xSubscribers = _BWagNumCurrent8021xSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 12),
    _BWagNumCurrent8021xSubscribers_Type()
)
bWagNumCurrent8021xSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrent8021xSubscribers.setStatus("current")
_BWagNumPreAuthenticatedSubscribers_Type = Unsigned32
_BWagNumPreAuthenticatedSubscribers_Object = MibScalar
bWagNumPreAuthenticatedSubscribers = _BWagNumPreAuthenticatedSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 13),
    _BWagNumPreAuthenticatedSubscribers_Type()
)
bWagNumPreAuthenticatedSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumPreAuthenticatedSubscribers.setStatus("current")
_BWagNumCurrentSingleStaticSubscribers_Type = Unsigned32
_BWagNumCurrentSingleStaticSubscribers_Object = MibScalar
bWagNumCurrentSingleStaticSubscribers = _BWagNumCurrentSingleStaticSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 14),
    _BWagNumCurrentSingleStaticSubscribers_Type()
)
bWagNumCurrentSingleStaticSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentSingleStaticSubscribers.setStatus("current")
_BWagNumCurrentRoutedSubnetSubscribers_Type = Unsigned32
_BWagNumCurrentRoutedSubnetSubscribers_Object = MibScalar
bWagNumCurrentRoutedSubnetSubscribers = _BWagNumCurrentRoutedSubnetSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 15),
    _BWagNumCurrentRoutedSubnetSubscribers_Type()
)
bWagNumCurrentRoutedSubnetSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentRoutedSubnetSubscribers.setStatus("current")
_BWagNumSubsUnauthenticatedWithIPv6Prefix_Type = Unsigned32
_BWagNumSubsUnauthenticatedWithIPv6Prefix_Object = MibScalar
bWagNumSubsUnauthenticatedWithIPv6Prefix = _BWagNumSubsUnauthenticatedWithIPv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 16),
    _BWagNumSubsUnauthenticatedWithIPv6Prefix_Type()
)
bWagNumSubsUnauthenticatedWithIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumSubsUnauthenticatedWithIPv6Prefix.setStatus("current")
_BWagNumSubsViaStaticAuthPolicy_Type = Unsigned32
_BWagNumSubsViaStaticAuthPolicy_Object = MibScalar
bWagNumSubsViaStaticAuthPolicy = _BWagNumSubsViaStaticAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 17),
    _BWagNumSubsViaStaticAuthPolicy_Type()
)
bWagNumSubsViaStaticAuthPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumSubsViaStaticAuthPolicy.setStatus("current")
_BWagNumCurrentHomeSubscribers_Type = Unsigned32
_BWagNumCurrentHomeSubscribers_Object = MibScalar
bWagNumCurrentHomeSubscribers = _BWagNumCurrentHomeSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 18),
    _BWagNumCurrentHomeSubscribers_Type()
)
bWagNumCurrentHomeSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomeSubscribers.setStatus("current")
_BWagNumCurrentSPWiFiSubscribers_Type = Unsigned32
_BWagNumCurrentSPWiFiSubscribers_Object = MibScalar
bWagNumCurrentSPWiFiSubscribers = _BWagNumCurrentSPWiFiSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 19),
    _BWagNumCurrentSPWiFiSubscribers_Type()
)
bWagNumCurrentSPWiFiSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentSPWiFiSubscribers.setStatus("current")
_BWagNumCurrentHomeTransientSubs_Type = Unsigned32
_BWagNumCurrentHomeTransientSubs_Object = MibScalar
bWagNumCurrentHomeTransientSubs = _BWagNumCurrentHomeTransientSubs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 20),
    _BWagNumCurrentHomeTransientSubs_Type()
)
bWagNumCurrentHomeTransientSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomeTransientSubs.setStatus("current")
_BWagNumCurrentHomeUserStatSubs_Type = Unsigned32
_BWagNumCurrentHomeUserStatSubs_Object = MibScalar
bWagNumCurrentHomeUserStatSubs = _BWagNumCurrentHomeUserStatSubs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 21),
    _BWagNumCurrentHomeUserStatSubs_Type()
)
bWagNumCurrentHomeUserStatSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomeUserStatSubs.setStatus("current")
_BWagNumCurrentHomeDhcpStatSubs_Type = Unsigned32
_BWagNumCurrentHomeDhcpStatSubs_Object = MibScalar
bWagNumCurrentHomeDhcpStatSubs = _BWagNumCurrentHomeDhcpStatSubs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 22),
    _BWagNumCurrentHomeDhcpStatSubs_Type()
)
bWagNumCurrentHomeDhcpStatSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomeDhcpStatSubs.setStatus("current")
_BWagNumCurrentHomeDhcpDynSubs_Type = Unsigned32
_BWagNumCurrentHomeDhcpDynSubs_Object = MibScalar
bWagNumCurrentHomeDhcpDynSubs = _BWagNumCurrentHomeDhcpDynSubs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 23),
    _BWagNumCurrentHomeDhcpDynSubs_Type()
)
bWagNumCurrentHomeDhcpDynSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomeDhcpDynSubs.setStatus("current")
_BWagNumCurrentHomePubStatSubs_Type = Unsigned32
_BWagNumCurrentHomePubStatSubs_Object = MibScalar
bWagNumCurrentHomePubStatSubs = _BWagNumCurrentHomePubStatSubs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 24),
    _BWagNumCurrentHomePubStatSubs_Type()
)
bWagNumCurrentHomePubStatSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentHomePubStatSubs.setStatus("current")
_BWagNumPreAuthSpwifiSubscribers_Type = Unsigned32
_BWagNumPreAuthSpwifiSubscribers_Object = MibScalar
bWagNumPreAuthSpwifiSubscribers = _BWagNumPreAuthSpwifiSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 25),
    _BWagNumPreAuthSpwifiSubscribers_Type()
)
bWagNumPreAuthSpwifiSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumPreAuthSpwifiSubscribers.setStatus("current")
_BWagNumPreAuthHomeSubscribers_Type = Unsigned32
_BWagNumPreAuthHomeSubscribers_Object = MibScalar
bWagNumPreAuthHomeSubscribers = _BWagNumPreAuthHomeSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 26),
    _BWagNumPreAuthHomeSubscribers_Type()
)
bWagNumPreAuthHomeSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumPreAuthHomeSubscribers.setStatus("current")
_BWagNumPreAuthenticatedSubscribersS2aPmip6_Type = Unsigned32
_BWagNumPreAuthenticatedSubscribersS2aPmip6_Object = MibScalar
bWagNumPreAuthenticatedSubscribersS2aPmip6 = _BWagNumPreAuthenticatedSubscribersS2aPmip6_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 27),
    _BWagNumPreAuthenticatedSubscribersS2aPmip6_Type()
)
bWagNumPreAuthenticatedSubscribersS2aPmip6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumPreAuthenticatedSubscribersS2aPmip6.setStatus("current")
_BWagNumCurrentSSIDS2aSubscribersPmip6_Type = Unsigned32
_BWagNumCurrentSSIDS2aSubscribersPmip6_Object = MibScalar
bWagNumCurrentSSIDS2aSubscribersPmip6 = _BWagNumCurrentSSIDS2aSubscribersPmip6_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 28),
    _BWagNumCurrentSSIDS2aSubscribersPmip6_Type()
)
bWagNumCurrentSSIDS2aSubscribersPmip6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentSSIDS2aSubscribersPmip6.setStatus("current")
_BWagNumCurrentDSLiteSubscribers_Type = Unsigned32
_BWagNumCurrentDSLiteSubscribers_Object = MibScalar
bWagNumCurrentDSLiteSubscribers = _BWagNumCurrentDSLiteSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 5, 29),
    _BWagNumCurrentDSLiteSubscribers_Type()
)
bWagNumCurrentDSLiteSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentDSLiteSubscribers.setStatus("current")
_BWagSubscriberNotifObjects_ObjectIdentity = ObjectIdentity
bWagSubscriberNotifObjects = _BWagSubscriberNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    bWagSubscriberNotifObjects.setStatus("current")
_BWagTunnelStatsMIBObjects_ObjectIdentity = ObjectIdentity
bWagTunnelStatsMIBObjects = _BWagTunnelStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    bWagTunnelStatsMIBObjects.setStatus("current")
_BWagTunnelTable_Object = MibTable
bWagTunnelTable = _BWagTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1)
)
if mibBuilder.loadTexts:
    bWagTunnelTable.setStatus("current")
_BWagTunnelEntry_Object = MibTableRow
bWagTunnelEntry = _BWagTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1)
)
bWagTunnelEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagTunnelStatsInterval"),
)
if mibBuilder.loadTexts:
    bWagTunnelEntry.setStatus("current")
_BWagTunnelStatsInterval_Type = Integer32
_BWagTunnelStatsInterval_Object = MibTableColumn
bWagTunnelStatsInterval = _BWagTunnelStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 1),
    _BWagTunnelStatsInterval_Type()
)
bWagTunnelStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagTunnelStatsInterval.setStatus("current")
_BWagTunnelIntervalDuration_Type = Integer32
_BWagTunnelIntervalDuration_Object = MibTableColumn
bWagTunnelIntervalDuration = _BWagTunnelIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 2),
    _BWagTunnelIntervalDuration_Type()
)
bWagTunnelIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelIntervalDuration.setStatus("current")
_BWagTunnelPktsRxdGRE_Type = Unsigned32
_BWagTunnelPktsRxdGRE_Object = MibTableColumn
bWagTunnelPktsRxdGRE = _BWagTunnelPktsRxdGRE_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 3),
    _BWagTunnelPktsRxdGRE_Type()
)
bWagTunnelPktsRxdGRE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdGRE.setStatus("current")
_BWagTunnelPktsRxdGREPayloadTEB_Type = Unsigned32
_BWagTunnelPktsRxdGREPayloadTEB_Object = MibTableColumn
bWagTunnelPktsRxdGREPayloadTEB = _BWagTunnelPktsRxdGREPayloadTEB_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 4),
    _BWagTunnelPktsRxdGREPayloadTEB_Type()
)
bWagTunnelPktsRxdGREPayloadTEB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdGREPayloadTEB.setStatus("current")
_BWagTunnelPktsRxdGREPayloadMPLS_Type = Unsigned32
_BWagTunnelPktsRxdGREPayloadMPLS_Object = MibTableColumn
bWagTunnelPktsRxdGREPayloadMPLS = _BWagTunnelPktsRxdGREPayloadMPLS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 5),
    _BWagTunnelPktsRxdGREPayloadMPLS_Type()
)
bWagTunnelPktsRxdGREPayloadMPLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdGREPayloadMPLS.setStatus("current")
_BWagTunnelPktsEncapsulatedGRE_Type = Unsigned32
_BWagTunnelPktsEncapsulatedGRE_Object = MibTableColumn
bWagTunnelPktsEncapsulatedGRE = _BWagTunnelPktsEncapsulatedGRE_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 6),
    _BWagTunnelPktsEncapsulatedGRE_Type()
)
bWagTunnelPktsEncapsulatedGRE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsEncapsulatedGRE.setStatus("current")
_BWagTunnelPktsDecapsulatedGRE_Type = Unsigned32
_BWagTunnelPktsDecapsulatedGRE_Object = MibTableColumn
bWagTunnelPktsDecapsulatedGRE = _BWagTunnelPktsDecapsulatedGRE_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 7),
    _BWagTunnelPktsDecapsulatedGRE_Type()
)
bWagTunnelPktsDecapsulatedGRE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsDecapsulatedGRE.setStatus("current")
_BWagTunnelPktsRxdARP_Type = Unsigned32
_BWagTunnelPktsRxdARP_Object = MibTableColumn
bWagTunnelPktsRxdARP = _BWagTunnelPktsRxdARP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 8),
    _BWagTunnelPktsRxdARP_Type()
)
bWagTunnelPktsRxdARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdARP.setStatus("current")
_BWagTunnelPktsRxdDHCP_Type = Unsigned32
_BWagTunnelPktsRxdDHCP_Object = MibTableColumn
bWagTunnelPktsRxdDHCP = _BWagTunnelPktsRxdDHCP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 9),
    _BWagTunnelPktsRxdDHCP_Type()
)
bWagTunnelPktsRxdDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdDHCP.setStatus("current")
_BWagTunnelPktsRxdDNS_Type = Unsigned32
_BWagTunnelPktsRxdDNS_Object = MibTableColumn
bWagTunnelPktsRxdDNS = _BWagTunnelPktsRxdDNS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 10),
    _BWagTunnelPktsRxdDNS_Type()
)
bWagTunnelPktsRxdDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdDNS.setStatus("obsolete")
_BWagTunnelPktsRxdHTTP_Type = Unsigned32
_BWagTunnelPktsRxdHTTP_Object = MibTableColumn
bWagTunnelPktsRxdHTTP = _BWagTunnelPktsRxdHTTP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 11),
    _BWagTunnelPktsRxdHTTP_Type()
)
bWagTunnelPktsRxdHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdHTTP.setStatus("obsolete")
_BWagTunnelPktsRxdHTTPGetReq_Type = Unsigned32
_BWagTunnelPktsRxdHTTPGetReq_Object = MibTableColumn
bWagTunnelPktsRxdHTTPGetReq = _BWagTunnelPktsRxdHTTPGetReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 12),
    _BWagTunnelPktsRxdHTTPGetReq_Type()
)
bWagTunnelPktsRxdHTTPGetReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdHTTPGetReq.setStatus("obsolete")
_BWagTunnelPktsTxdHTTP_Type = Unsigned32
_BWagTunnelPktsTxdHTTP_Object = MibTableColumn
bWagTunnelPktsTxdHTTP = _BWagTunnelPktsTxdHTTP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 13),
    _BWagTunnelPktsTxdHTTP_Type()
)
bWagTunnelPktsTxdHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsTxdHTTP.setStatus("obsolete")
_BWagTunnelPktsTxdHTTPRedir_Type = Unsigned32
_BWagTunnelPktsTxdHTTPRedir_Object = MibTableColumn
bWagTunnelPktsTxdHTTPRedir = _BWagTunnelPktsTxdHTTPRedir_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 14),
    _BWagTunnelPktsTxdHTTPRedir_Type()
)
bWagTunnelPktsTxdHTTPRedir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsTxdHTTPRedir.setStatus("obsolete")
_BWagTunnelPktsRxdHTTPS_Type = Unsigned32
_BWagTunnelPktsRxdHTTPS_Object = MibTableColumn
bWagTunnelPktsRxdHTTPS = _BWagTunnelPktsRxdHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 15),
    _BWagTunnelPktsRxdHTTPS_Type()
)
bWagTunnelPktsRxdHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdHTTPS.setStatus("obsolete")
_BWagTunnelPktsRxdTCPSyn_Type = Unsigned32
_BWagTunnelPktsRxdTCPSyn_Object = MibTableColumn
bWagTunnelPktsRxdTCPSyn = _BWagTunnelPktsRxdTCPSyn_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 16),
    _BWagTunnelPktsRxdTCPSyn_Type()
)
bWagTunnelPktsRxdTCPSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdTCPSyn.setStatus("obsolete")
_BWagTunnelPktsTxdTCPSynAck_Type = Unsigned32
_BWagTunnelPktsTxdTCPSynAck_Object = MibTableColumn
bWagTunnelPktsTxdTCPSynAck = _BWagTunnelPktsTxdTCPSynAck_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 17),
    _BWagTunnelPktsTxdTCPSynAck_Type()
)
bWagTunnelPktsTxdTCPSynAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsTxdTCPSynAck.setStatus("obsolete")
_BWagTunnelPktsTxdTCPFin_Type = Unsigned32
_BWagTunnelPktsTxdTCPFin_Object = MibTableColumn
bWagTunnelPktsTxdTCPFin = _BWagTunnelPktsTxdTCPFin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 18),
    _BWagTunnelPktsTxdTCPFin_Type()
)
bWagTunnelPktsTxdTCPFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsTxdTCPFin.setStatus("obsolete")
_BWagTunnelPktsRxdTCPFinAck_Type = Unsigned32
_BWagTunnelPktsRxdTCPFinAck_Object = MibTableColumn
bWagTunnelPktsRxdTCPFinAck = _BWagTunnelPktsRxdTCPFinAck_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 19),
    _BWagTunnelPktsRxdTCPFinAck_Type()
)
bWagTunnelPktsRxdTCPFinAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsRxdTCPFinAck.setStatus("obsolete")
_BWagTunnelPktsTxdTCPAck2Fin_Type = Unsigned32
_BWagTunnelPktsTxdTCPAck2Fin_Object = MibTableColumn
bWagTunnelPktsTxdTCPAck2Fin = _BWagTunnelPktsTxdTCPAck2Fin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 20),
    _BWagTunnelPktsTxdTCPAck2Fin_Type()
)
bWagTunnelPktsTxdTCPAck2Fin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelPktsTxdTCPAck2Fin.setStatus("obsolete")
_BWagTunnelCreatedDynamically_Type = Unsigned32
_BWagTunnelCreatedDynamically_Object = MibTableColumn
bWagTunnelCreatedDynamically = _BWagTunnelCreatedDynamically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 21),
    _BWagTunnelCreatedDynamically_Type()
)
bWagTunnelCreatedDynamically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelCreatedDynamically.setStatus("current")
_BWagTunnelCreatedStatically_Type = Unsigned32
_BWagTunnelCreatedStatically_Object = MibTableColumn
bWagTunnelCreatedStatically = _BWagTunnelCreatedStatically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 22),
    _BWagTunnelCreatedStatically_Type()
)
bWagTunnelCreatedStatically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelCreatedStatically.setStatus("current")
_BWagTunnelDeleted_Type = Unsigned32
_BWagTunnelDeleted_Object = MibTableColumn
bWagTunnelDeleted = _BWagTunnelDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 23),
    _BWagTunnelDeleted_Type()
)
bWagTunnelDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeleted.setStatus("current")
_BWagTunnelDeletedDueToInactivity_Type = Unsigned32
_BWagTunnelDeletedDueToInactivity_Object = MibTableColumn
bWagTunnelDeletedDueToInactivity = _BWagTunnelDeletedDueToInactivity_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 24),
    _BWagTunnelDeletedDueToInactivity_Type()
)
bWagTunnelDeletedDueToInactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToInactivity.setStatus("current")
_BWagTunnelDeletedByCommand_Type = Unsigned32
_BWagTunnelDeletedByCommand_Object = MibTableColumn
bWagTunnelDeletedByCommand = _BWagTunnelDeletedByCommand_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 25),
    _BWagTunnelDeletedByCommand_Type()
)
bWagTunnelDeletedByCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedByCommand.setStatus("current")
_BWagTunnelMaxSupported_Type = Unsigned32
_BWagTunnelMaxSupported_Object = MibTableColumn
bWagTunnelMaxSupported = _BWagTunnelMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 26),
    _BWagTunnelMaxSupported_Type()
)
bWagTunnelMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelMaxSupported.setStatus("current")
_BWagTunnelMaxCountReached_Type = Unsigned32
_BWagTunnelMaxCountReached_Object = MibTableColumn
bWagTunnelMaxCountReached = _BWagTunnelMaxCountReached_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 27),
    _BWagTunnelMaxCountReached_Type()
)
bWagTunnelMaxCountReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelMaxCountReached.setStatus("current")
_BWagTunnelTunnelsLookupFound_Type = Unsigned32
_BWagTunnelTunnelsLookupFound_Object = MibTableColumn
bWagTunnelTunnelsLookupFound = _BWagTunnelTunnelsLookupFound_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 28),
    _BWagTunnelTunnelsLookupFound_Type()
)
bWagTunnelTunnelsLookupFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelTunnelsLookupFound.setStatus("current")
_BWagTunnelTunnelsLookupNotFound_Type = Unsigned32
_BWagTunnelTunnelsLookupNotFound_Object = MibTableColumn
bWagTunnelTunnelsLookupNotFound = _BWagTunnelTunnelsLookupNotFound_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 29),
    _BWagTunnelTunnelsLookupNotFound_Type()
)
bWagTunnelTunnelsLookupNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelTunnelsLookupNotFound.setStatus("current")
_BWagTunnelCountHighThreshold_Type = Unsigned32
_BWagTunnelCountHighThreshold_Object = MibTableColumn
bWagTunnelCountHighThreshold = _BWagTunnelCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 30),
    _BWagTunnelCountHighThreshold_Type()
)
bWagTunnelCountHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelCountHighThreshold.setStatus("current")
_BWagTunnelCountLowThreshold_Type = Unsigned32
_BWagTunnelCountLowThreshold_Object = MibTableColumn
bWagTunnelCountLowThreshold = _BWagTunnelCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 31),
    _BWagTunnelCountLowThreshold_Type()
)
bWagTunnelCountLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelCountLowThreshold.setStatus("current")
_BWagTunnelDeletedDueToReject_Type = Unsigned32
_BWagTunnelDeletedDueToReject_Object = MibTableColumn
bWagTunnelDeletedDueToReject = _BWagTunnelDeletedDueToReject_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 32),
    _BWagTunnelDeletedDueToReject_Type()
)
bWagTunnelDeletedDueToReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToReject.setStatus("current")
_BWagTunnelDeletedDueToAbort_Type = Unsigned32
_BWagTunnelDeletedDueToAbort_Object = MibTableColumn
bWagTunnelDeletedDueToAbort = _BWagTunnelDeletedDueToAbort_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 33),
    _BWagTunnelDeletedDueToAbort_Type()
)
bWagTunnelDeletedDueToAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToAbort.setStatus("current")
_BWagTunnelDeletedDueToMacResFail_Type = Unsigned32
_BWagTunnelDeletedDueToMacResFail_Object = MibTableColumn
bWagTunnelDeletedDueToMacResFail = _BWagTunnelDeletedDueToMacResFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 34),
    _BWagTunnelDeletedDueToMacResFail_Type()
)
bWagTunnelDeletedDueToMacResFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToMacResFail.setStatus("current")
_BWagTunnelDeletedDueToLifDown_Type = Unsigned32
_BWagTunnelDeletedDueToLifDown_Object = MibTableColumn
bWagTunnelDeletedDueToLifDown = _BWagTunnelDeletedDueToLifDown_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 35),
    _BWagTunnelDeletedDueToLifDown_Type()
)
bWagTunnelDeletedDueToLifDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToLifDown.setStatus("current")
_BWagTunnelDeletedDueToB2bSubsDelete_Type = Unsigned32
_BWagTunnelDeletedDueToB2bSubsDelete_Object = MibTableColumn
bWagTunnelDeletedDueToB2bSubsDelete = _BWagTunnelDeletedDueToB2bSubsDelete_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 36),
    _BWagTunnelDeletedDueToB2bSubsDelete_Type()
)
bWagTunnelDeletedDueToB2bSubsDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagTunnelDeletedDueToB2bSubsDelete.setStatus("current")
_BWagL2tpv3TunnelPktsRxd_Type = Unsigned32
_BWagL2tpv3TunnelPktsRxd_Object = MibTableColumn
bWagL2tpv3TunnelPktsRxd = _BWagL2tpv3TunnelPktsRxd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 37),
    _BWagL2tpv3TunnelPktsRxd_Type()
)
bWagL2tpv3TunnelPktsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsRxd.setStatus("current")
_BWagL2tpv3TunnelPktsEncapsulated_Type = Unsigned32
_BWagL2tpv3TunnelPktsEncapsulated_Object = MibTableColumn
bWagL2tpv3TunnelPktsEncapsulated = _BWagL2tpv3TunnelPktsEncapsulated_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 38),
    _BWagL2tpv3TunnelPktsEncapsulated_Type()
)
bWagL2tpv3TunnelPktsEncapsulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsEncapsulated.setStatus("current")
_BWagL2tpv3TunnelPktsDecapsulated_Type = Unsigned32
_BWagL2tpv3TunnelPktsDecapsulated_Object = MibTableColumn
bWagL2tpv3TunnelPktsDecapsulated = _BWagL2tpv3TunnelPktsDecapsulated_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 39),
    _BWagL2tpv3TunnelPktsDecapsulated_Type()
)
bWagL2tpv3TunnelPktsDecapsulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsDecapsulated.setStatus("current")
_BWagL2tpv3TunnelPktsRxdARP_Type = Unsigned32
_BWagL2tpv3TunnelPktsRxdARP_Object = MibTableColumn
bWagL2tpv3TunnelPktsRxdARP = _BWagL2tpv3TunnelPktsRxdARP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 40),
    _BWagL2tpv3TunnelPktsRxdARP_Type()
)
bWagL2tpv3TunnelPktsRxdARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsRxdARP.setStatus("current")
_BWagL2tpv3TunnelPktsRxdDHCP_Type = Unsigned32
_BWagL2tpv3TunnelPktsRxdDHCP_Object = MibTableColumn
bWagL2tpv3TunnelPktsRxdDHCP = _BWagL2tpv3TunnelPktsRxdDHCP_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 41),
    _BWagL2tpv3TunnelPktsRxdDHCP_Type()
)
bWagL2tpv3TunnelPktsRxdDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsRxdDHCP.setStatus("current")
_BWagL2tpv3TunnelPktsRxdDNS_Type = Unsigned32
_BWagL2tpv3TunnelPktsRxdDNS_Object = MibTableColumn
bWagL2tpv3TunnelPktsRxdDNS = _BWagL2tpv3TunnelPktsRxdDNS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 42),
    _BWagL2tpv3TunnelPktsRxdDNS_Type()
)
bWagL2tpv3TunnelPktsRxdDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelPktsRxdDNS.setStatus("obsolete")
_BWagL2tpv3TunnelCreatedDynamically_Type = Unsigned32
_BWagL2tpv3TunnelCreatedDynamically_Object = MibTableColumn
bWagL2tpv3TunnelCreatedDynamically = _BWagL2tpv3TunnelCreatedDynamically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 43),
    _BWagL2tpv3TunnelCreatedDynamically_Type()
)
bWagL2tpv3TunnelCreatedDynamically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelCreatedDynamically.setStatus("current")
_BWagL2tpv3TunnelDeleted_Type = Unsigned32
_BWagL2tpv3TunnelDeleted_Object = MibTableColumn
bWagL2tpv3TunnelDeleted = _BWagL2tpv3TunnelDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 44),
    _BWagL2tpv3TunnelDeleted_Type()
)
bWagL2tpv3TunnelDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelDeleted.setStatus("current")
_BWagL2tpv3TunnelDeletedDueToInactivity_Type = Unsigned32
_BWagL2tpv3TunnelDeletedDueToInactivity_Object = MibTableColumn
bWagL2tpv3TunnelDeletedDueToInactivity = _BWagL2tpv3TunnelDeletedDueToInactivity_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 45),
    _BWagL2tpv3TunnelDeletedDueToInactivity_Type()
)
bWagL2tpv3TunnelDeletedDueToInactivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelDeletedDueToInactivity.setStatus("current")
_BWagL2tpv3TunnelDeletedByCommand_Type = Unsigned32
_BWagL2tpv3TunnelDeletedByCommand_Object = MibTableColumn
bWagL2tpv3TunnelDeletedByCommand = _BWagL2tpv3TunnelDeletedByCommand_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 46),
    _BWagL2tpv3TunnelDeletedByCommand_Type()
)
bWagL2tpv3TunnelDeletedByCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelDeletedByCommand.setStatus("current")
_BWagL2tpv3TunnelDeletedDueToLifDown_Type = Unsigned32
_BWagL2tpv3TunnelDeletedDueToLifDown_Object = MibTableColumn
bWagL2tpv3TunnelDeletedDueToLifDown = _BWagL2tpv3TunnelDeletedDueToLifDown_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 1, 1, 47),
    _BWagL2tpv3TunnelDeletedDueToLifDown_Type()
)
bWagL2tpv3TunnelDeletedDueToLifDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagL2tpv3TunnelDeletedDueToLifDown.setStatus("current")
_BWagNumCurrentTunnels_Type = Unsigned32
_BWagNumCurrentTunnels_Object = MibScalar
bWagNumCurrentTunnels = _BWagNumCurrentTunnels_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 2),
    _BWagNumCurrentTunnels_Type()
)
bWagNumCurrentTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnels.setStatus("current")
_BWagNumTunnelsCreatedDynamically_Type = Counter64
_BWagNumTunnelsCreatedDynamically_Object = MibScalar
bWagNumTunnelsCreatedDynamically = _BWagNumTunnelsCreatedDynamically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 3),
    _BWagNumTunnelsCreatedDynamically_Type()
)
bWagNumTunnelsCreatedDynamically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsCreatedDynamically.setStatus("current")
_BWagNumTunnelsCreatedStatically_Type = Counter64
_BWagNumTunnelsCreatedStatically_Object = MibScalar
bWagNumTunnelsCreatedStatically = _BWagNumTunnelsCreatedStatically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 4),
    _BWagNumTunnelsCreatedStatically_Type()
)
bWagNumTunnelsCreatedStatically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsCreatedStatically.setStatus("current")
_BWagNumTunnelsDeleted_Type = Counter64
_BWagNumTunnelsDeleted_Object = MibScalar
bWagNumTunnelsDeleted = _BWagNumTunnelsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 5),
    _BWagNumTunnelsDeleted_Type()
)
bWagNumTunnelsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsDeleted.setStatus("current")
_BWagNumTunnelsInactiveDeleted_Type = Counter64
_BWagNumTunnelsInactiveDeleted_Object = MibScalar
bWagNumTunnelsInactiveDeleted = _BWagNumTunnelsInactiveDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 6),
    _BWagNumTunnelsInactiveDeleted_Type()
)
bWagNumTunnelsInactiveDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsInactiveDeleted.setStatus("current")
_BWagNumTunnelsDeletedByCommand_Type = Counter64
_BWagNumTunnelsDeletedByCommand_Object = MibScalar
bWagNumTunnelsDeletedByCommand = _BWagNumTunnelsDeletedByCommand_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 7),
    _BWagNumTunnelsDeletedByCommand_Type()
)
bWagNumTunnelsDeletedByCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsDeletedByCommand.setStatus("current")
_BWagNumTunnelsSubsAssociated_Type = Unsigned32
_BWagNumTunnelsSubsAssociated_Object = MibScalar
bWagNumTunnelsSubsAssociated = _BWagNumTunnelsSubsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 8),
    _BWagNumTunnelsSubsAssociated_Type()
)
bWagNumTunnelsSubsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsSubsAssociated.setStatus("current")
_BWagNumTunnelsSchedDeletion_Type = Unsigned32
_BWagNumTunnelsSchedDeletion_Object = MibScalar
bWagNumTunnelsSchedDeletion = _BWagNumTunnelsSchedDeletion_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 9),
    _BWagNumTunnelsSchedDeletion_Type()
)
bWagNumTunnelsSchedDeletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsSchedDeletion.setStatus("current")
_BWagNumCurrentTunnelsIPv4_Type = Unsigned32
_BWagNumCurrentTunnelsIPv4_Object = MibScalar
bWagNumCurrentTunnelsIPv4 = _BWagNumCurrentTunnelsIPv4_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 10),
    _BWagNumCurrentTunnelsIPv4_Type()
)
bWagNumCurrentTunnelsIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnelsIPv4.setStatus("current")
_BWagNumCurrentTunnelsIPv6_Type = Unsigned32
_BWagNumCurrentTunnelsIPv6_Object = MibScalar
bWagNumCurrentTunnelsIPv6 = _BWagNumCurrentTunnelsIPv6_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 11),
    _BWagNumCurrentTunnelsIPv6_Type()
)
bWagNumCurrentTunnelsIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnelsIPv6.setStatus("current")
_BWagNumTunnelsDeletedByB2B_Type = Counter64
_BWagNumTunnelsDeletedByB2B_Object = MibScalar
bWagNumTunnelsDeletedByB2B = _BWagNumTunnelsDeletedByB2B_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 12),
    _BWagNumTunnelsDeletedByB2B_Type()
)
bWagNumTunnelsDeletedByB2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsDeletedByB2B.setStatus("current")
_BWagNumTunnelsDeletedDuetoLIFDown_Type = Counter64
_BWagNumTunnelsDeletedDuetoLIFDown_Object = MibScalar
bWagNumTunnelsDeletedDuetoLIFDown = _BWagNumTunnelsDeletedDuetoLIFDown_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 13),
    _BWagNumTunnelsDeletedDuetoLIFDown_Type()
)
bWagNumTunnelsDeletedDuetoLIFDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumTunnelsDeletedDuetoLIFDown.setStatus("current")
_BWagNumCurrentTunnelsSpWiFi_Type = Unsigned32
_BWagNumCurrentTunnelsSpWiFi_Object = MibScalar
bWagNumCurrentTunnelsSpWiFi = _BWagNumCurrentTunnelsSpWiFi_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 14),
    _BWagNumCurrentTunnelsSpWiFi_Type()
)
bWagNumCurrentTunnelsSpWiFi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnelsSpWiFi.setStatus("current")
_BWagNumCurrentTunnelsHome_Type = Unsigned32
_BWagNumCurrentTunnelsHome_Object = MibScalar
bWagNumCurrentTunnelsHome = _BWagNumCurrentTunnelsHome_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 15),
    _BWagNumCurrentTunnelsHome_Type()
)
bWagNumCurrentTunnelsHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnelsHome.setStatus("current")
_BWagNumCurrTunnHomeAndSpWiFi_Type = Unsigned32
_BWagNumCurrTunnHomeAndSpWiFi_Object = MibScalar
bWagNumCurrTunnHomeAndSpWiFi = _BWagNumCurrTunnHomeAndSpWiFi_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 16),
    _BWagNumCurrTunnHomeAndSpWiFi_Type()
)
bWagNumCurrTunnHomeAndSpWiFi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrTunnHomeAndSpWiFi.setStatus("current")
_BWagNumCurrentTunnHomeInactive_Type = Unsigned32
_BWagNumCurrentTunnHomeInactive_Object = MibScalar
bWagNumCurrentTunnHomeInactive = _BWagNumCurrentTunnHomeInactive_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 17),
    _BWagNumCurrentTunnHomeInactive_Type()
)
bWagNumCurrentTunnHomeInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnHomeInactive.setStatus("current")
_BWagNumCurrentTunnHomeAccept_Type = Unsigned32
_BWagNumCurrentTunnHomeAccept_Object = MibScalar
bWagNumCurrentTunnHomeAccept = _BWagNumCurrentTunnHomeAccept_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 18),
    _BWagNumCurrentTunnHomeAccept_Type()
)
bWagNumCurrentTunnHomeAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnHomeAccept.setStatus("current")
_BWagNumL2tpv3TunnelsCreatedDynamically_Type = Counter64
_BWagNumL2tpv3TunnelsCreatedDynamically_Object = MibScalar
bWagNumL2tpv3TunnelsCreatedDynamically = _BWagNumL2tpv3TunnelsCreatedDynamically_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 19),
    _BWagNumL2tpv3TunnelsCreatedDynamically_Type()
)
bWagNumL2tpv3TunnelsCreatedDynamically.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsCreatedDynamically.setStatus("current")
_BWagNumL2tpv3TunnelsDeleted_Type = Counter64
_BWagNumL2tpv3TunnelsDeleted_Object = MibScalar
bWagNumL2tpv3TunnelsDeleted = _BWagNumL2tpv3TunnelsDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 20),
    _BWagNumL2tpv3TunnelsDeleted_Type()
)
bWagNumL2tpv3TunnelsDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsDeleted.setStatus("current")
_BWagNumL2tpv3TunnelsInactiveDeleted_Type = Counter64
_BWagNumL2tpv3TunnelsInactiveDeleted_Object = MibScalar
bWagNumL2tpv3TunnelsInactiveDeleted = _BWagNumL2tpv3TunnelsInactiveDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 21),
    _BWagNumL2tpv3TunnelsInactiveDeleted_Type()
)
bWagNumL2tpv3TunnelsInactiveDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsInactiveDeleted.setStatus("current")
_BWagNumL2tpv3TunnelsDeletedByCommand_Type = Counter64
_BWagNumL2tpv3TunnelsDeletedByCommand_Object = MibScalar
bWagNumL2tpv3TunnelsDeletedByCommand = _BWagNumL2tpv3TunnelsDeletedByCommand_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 22),
    _BWagNumL2tpv3TunnelsDeletedByCommand_Type()
)
bWagNumL2tpv3TunnelsDeletedByCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsDeletedByCommand.setStatus("current")
_BWagNumL2tpv3TunnelsSubsAssociated_Type = Unsigned32
_BWagNumL2tpv3TunnelsSubsAssociated_Object = MibScalar
bWagNumL2tpv3TunnelsSubsAssociated = _BWagNumL2tpv3TunnelsSubsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 23),
    _BWagNumL2tpv3TunnelsSubsAssociated_Type()
)
bWagNumL2tpv3TunnelsSubsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsSubsAssociated.setStatus("current")
_BWagNumCurrentL2tpv3TunnelsIPv4_Type = Unsigned32
_BWagNumCurrentL2tpv3TunnelsIPv4_Object = MibScalar
bWagNumCurrentL2tpv3TunnelsIPv4 = _BWagNumCurrentL2tpv3TunnelsIPv4_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 24),
    _BWagNumCurrentL2tpv3TunnelsIPv4_Type()
)
bWagNumCurrentL2tpv3TunnelsIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentL2tpv3TunnelsIPv4.setStatus("current")
_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Type = Counter64
_BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Object = MibScalar
bWagNumL2tpv3TunnelsDeletedDuetoLIFDown = _BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 25),
    _BWagNumL2tpv3TunnelsDeletedDuetoLIFDown_Type()
)
bWagNumL2tpv3TunnelsDeletedDuetoLIFDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumL2tpv3TunnelsDeletedDuetoLIFDown.setStatus("current")
_BWagNumCurrentL2tpv3TunnelsSpWiFi_Type = Unsigned32
_BWagNumCurrentL2tpv3TunnelsSpWiFi_Object = MibScalar
bWagNumCurrentL2tpv3TunnelsSpWiFi = _BWagNumCurrentL2tpv3TunnelsSpWiFi_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 26),
    _BWagNumCurrentL2tpv3TunnelsSpWiFi_Type()
)
bWagNumCurrentL2tpv3TunnelsSpWiFi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentL2tpv3TunnelsSpWiFi.setStatus("current")
_BWagNumCurrentTunnelsDSLite_Type = Unsigned32
_BWagNumCurrentTunnelsDSLite_Object = MibScalar
bWagNumCurrentTunnelsDSLite = _BWagNumCurrentTunnelsDSLite_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 7, 27),
    _BWagNumCurrentTunnelsDSLite_Type()
)
bWagNumCurrentTunnelsDSLite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagNumCurrentTunnelsDSLite.setStatus("current")
_BWagTunnelNotifObjects_ObjectIdentity = ObjectIdentity
bWagTunnelNotifObjects = _BWagTunnelNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    bWagTunnelNotifObjects.setStatus("current")
_BWagCgnatMIBObjects_ObjectIdentity = ObjectIdentity
bWagCgnatMIBObjects = _BWagCgnatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    bWagCgnatMIBObjects.setStatus("current")
_BWagCgnatProfileStatsTable_Object = MibTable
bWagCgnatProfileStatsTable = _BWagCgnatProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1)
)
if mibBuilder.loadTexts:
    bWagCgnatProfileStatsTable.setStatus("current")
_BWagCgnatProfileStatsEntry_Object = MibTableRow
bWagCgnatProfileStatsEntry = _BWagCgnatProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1)
)
bWagCgnatProfileStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatProfileStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatProfileStatsEntry.setStatus("current")
_BWagCgnatProfileStatsIndex_Type = Integer32
_BWagCgnatProfileStatsIndex_Object = MibTableColumn
bWagCgnatProfileStatsIndex = _BWagCgnatProfileStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 1),
    _BWagCgnatProfileStatsIndex_Type()
)
bWagCgnatProfileStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatProfileStatsIndex.setStatus("current")
_BWagCgnatProfileName_Type = DisplayString
_BWagCgnatProfileName_Object = MibTableColumn
bWagCgnatProfileName = _BWagCgnatProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 2),
    _BWagCgnatProfileName_Type()
)
bWagCgnatProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileName.setStatus("current")
_BWagCgnatProfileType_Type = DisplayString
_BWagCgnatProfileType_Object = MibTableColumn
bWagCgnatProfileType = _BWagCgnatProfileType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 3),
    _BWagCgnatProfileType_Type()
)
bWagCgnatProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileType.setStatus("current")
_BWagCgnatProfileNATIPPoolGroup_Type = DisplayString
_BWagCgnatProfileNATIPPoolGroup_Object = MibTableColumn
bWagCgnatProfileNATIPPoolGroup = _BWagCgnatProfileNATIPPoolGroup_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 4),
    _BWagCgnatProfileNATIPPoolGroup_Type()
)
bWagCgnatProfileNATIPPoolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileNATIPPoolGroup.setStatus("current")
_BWagCgnatProfileSubscribers_Type = Unsigned32
_BWagCgnatProfileSubscribers_Object = MibTableColumn
bWagCgnatProfileSubscribers = _BWagCgnatProfileSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 5),
    _BWagCgnatProfileSubscribers_Type()
)
bWagCgnatProfileSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileSubscribers.setStatus("current")
_BWagCgnatProfileMaxIPAddresses_Type = Unsigned32
_BWagCgnatProfileMaxIPAddresses_Object = MibTableColumn
bWagCgnatProfileMaxIPAddresses = _BWagCgnatProfileMaxIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 6),
    _BWagCgnatProfileMaxIPAddresses_Type()
)
bWagCgnatProfileMaxIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileMaxIPAddresses.setStatus("current")
_BWagCgnatProfileUsedIPAddresses_Type = Unsigned32
_BWagCgnatProfileUsedIPAddresses_Object = MibTableColumn
bWagCgnatProfileUsedIPAddresses = _BWagCgnatProfileUsedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 7),
    _BWagCgnatProfileUsedIPAddresses_Type()
)
bWagCgnatProfileUsedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileUsedIPAddresses.setStatus("current")
_BWagCgnatProfileReservedIPAddresses_Type = Unsigned32
_BWagCgnatProfileReservedIPAddresses_Object = MibTableColumn
bWagCgnatProfileReservedIPAddresses = _BWagCgnatProfileReservedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 8),
    _BWagCgnatProfileReservedIPAddresses_Type()
)
bWagCgnatProfileReservedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileReservedIPAddresses.setStatus("current")
_BWagCgnatProfileTotalPortBlocks_Type = Unsigned32
_BWagCgnatProfileTotalPortBlocks_Object = MibTableColumn
bWagCgnatProfileTotalPortBlocks = _BWagCgnatProfileTotalPortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 9),
    _BWagCgnatProfileTotalPortBlocks_Type()
)
bWagCgnatProfileTotalPortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileTotalPortBlocks.setStatus("current")
_BWagCgnatProfilePortBlocksUsed_Type = Unsigned32
_BWagCgnatProfilePortBlocksUsed_Object = MibTableColumn
bWagCgnatProfilePortBlocksUsed = _BWagCgnatProfilePortBlocksUsed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 10),
    _BWagCgnatProfilePortBlocksUsed_Type()
)
bWagCgnatProfilePortBlocksUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfilePortBlocksUsed.setStatus("obsolete")
_BWagCgnatProfilePortBlocksReused_Type = Unsigned32
_BWagCgnatProfilePortBlocksReused_Object = MibTableColumn
bWagCgnatProfilePortBlocksReused = _BWagCgnatProfilePortBlocksReused_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 11),
    _BWagCgnatProfilePortBlocksReused_Type()
)
bWagCgnatProfilePortBlocksReused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfilePortBlocksReused.setStatus("obsolete")
_BWagCgnatProfileTotalPoolIPAddresses_Type = Unsigned32
_BWagCgnatProfileTotalPoolIPAddresses_Object = MibTableColumn
bWagCgnatProfileTotalPoolIPAddresses = _BWagCgnatProfileTotalPoolIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 1, 1, 12),
    _BWagCgnatProfileTotalPoolIPAddresses_Type()
)
bWagCgnatProfileTotalPoolIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatProfileTotalPoolIPAddresses.setStatus("current")
_BWagCgnatIPStatsTable_Object = MibTable
bWagCgnatIPStatsTable = _BWagCgnatIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    bWagCgnatIPStatsTable.setStatus("current")
_BWagCgnatIPStatsEntry_Object = MibTableRow
bWagCgnatIPStatsEntry = _BWagCgnatIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1)
)
bWagCgnatIPStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatIPStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatIPStatsEntry.setStatus("current")
_BWagCgnatIPStatsIndex_Type = Integer32
_BWagCgnatIPStatsIndex_Object = MibTableColumn
bWagCgnatIPStatsIndex = _BWagCgnatIPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 1),
    _BWagCgnatIPStatsIndex_Type()
)
bWagCgnatIPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatIPStatsIndex.setStatus("current")
_BWagCgnatPublicIPAddressType_Type = InetAddressType
_BWagCgnatPublicIPAddressType_Object = MibTableColumn
bWagCgnatPublicIPAddressType = _BWagCgnatPublicIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 2),
    _BWagCgnatPublicIPAddressType_Type()
)
bWagCgnatPublicIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPublicIPAddressType.setStatus("current")
_BWagCgnatPublicIPAddress_Type = InetAddress
_BWagCgnatPublicIPAddress_Object = MibTableColumn
bWagCgnatPublicIPAddress = _BWagCgnatPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 3),
    _BWagCgnatPublicIPAddress_Type()
)
bWagCgnatPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPublicIPAddress.setStatus("current")
_BWagCgnatIPPortBlocksUsed_Type = Unsigned32
_BWagCgnatIPPortBlocksUsed_Object = MibTableColumn
bWagCgnatIPPortBlocksUsed = _BWagCgnatIPPortBlocksUsed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 4),
    _BWagCgnatIPPortBlocksUsed_Type()
)
bWagCgnatIPPortBlocksUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPPortBlocksUsed.setStatus("obsolete")
_BWagCgnatIPPortBlocksFree_Type = Unsigned32
_BWagCgnatIPPortBlocksFree_Object = MibTableColumn
bWagCgnatIPPortBlocksFree = _BWagCgnatIPPortBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 5),
    _BWagCgnatIPPortBlocksFree_Type()
)
bWagCgnatIPPortBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPPortBlocksFree.setStatus("current")
_BWagCgnatIPPortBlocksReused_Type = Unsigned32
_BWagCgnatIPPortBlocksReused_Object = MibTableColumn
bWagCgnatIPPortBlocksReused = _BWagCgnatIPPortBlocksReused_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 6),
    _BWagCgnatIPPortBlocksReused_Type()
)
bWagCgnatIPPortBlocksReused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPPortBlocksReused.setStatus("obsolete")
_BWagCgnatIPSubActiveCount_Type = Unsigned32
_BWagCgnatIPSubActiveCount_Object = MibTableColumn
bWagCgnatIPSubActiveCount = _BWagCgnatIPSubActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 7),
    _BWagCgnatIPSubActiveCount_Type()
)
bWagCgnatIPSubActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPSubActiveCount.setStatus("current")
_BWagCgnatIPPacketsDropped_Type = Unsigned32
_BWagCgnatIPPacketsDropped_Object = MibTableColumn
bWagCgnatIPPacketsDropped = _BWagCgnatIPPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 2, 1, 8),
    _BWagCgnatIPPacketsDropped_Type()
)
bWagCgnatIPPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPPacketsDropped.setStatus("obsolete")
_BWagCgnatPeriodIpTable_Object = MibTable
bWagCgnatPeriodIpTable = _BWagCgnatPeriodIpTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3)
)
if mibBuilder.loadTexts:
    bWagCgnatPeriodIpTable.setStatus("obsolete")
_BWagCgnatPeriodIpEntry_Object = MibTableRow
bWagCgnatPeriodIpEntry = _BWagCgnatPeriodIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1)
)
bWagCgnatPeriodIpEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatPeriodIpInterval"),
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatPeriodIpIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatPeriodIpEntry.setStatus("obsolete")
_BWagCgnatPeriodIpInterval_Type = Integer32
_BWagCgnatPeriodIpInterval_Object = MibTableColumn
bWagCgnatPeriodIpInterval = _BWagCgnatPeriodIpInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 1),
    _BWagCgnatPeriodIpInterval_Type()
)
bWagCgnatPeriodIpInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatPeriodIpInterval.setStatus("obsolete")
_BWagCgnatPeriodIpIndex_Type = Integer32
_BWagCgnatPeriodIpIndex_Object = MibTableColumn
bWagCgnatPeriodIpIndex = _BWagCgnatPeriodIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 2),
    _BWagCgnatPeriodIpIndex_Type()
)
bWagCgnatPeriodIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatPeriodIpIndex.setStatus("obsolete")
_BWagCgnatIPAddressType_Type = InetAddressType
_BWagCgnatIPAddressType_Object = MibTableColumn
bWagCgnatIPAddressType = _BWagCgnatIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 3),
    _BWagCgnatIPAddressType_Type()
)
bWagCgnatIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPAddressType.setStatus("obsolete")
_BWagCgnatIPAddress_Type = InetAddress
_BWagCgnatIPAddress_Object = MibTableColumn
bWagCgnatIPAddress = _BWagCgnatIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 4),
    _BWagCgnatIPAddress_Type()
)
bWagCgnatIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIPAddress.setStatus("obsolete")
_BWagCgnatPacketsDropped_Type = Unsigned32
_BWagCgnatPacketsDropped_Object = MibTableColumn
bWagCgnatPacketsDropped = _BWagCgnatPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 5),
    _BWagCgnatPacketsDropped_Type()
)
bWagCgnatPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPacketsDropped.setStatus("obsolete")
_BWagCgnatPortBlockMaxUtil_Type = Unsigned32
_BWagCgnatPortBlockMaxUtil_Object = MibTableColumn
bWagCgnatPortBlockMaxUtil = _BWagCgnatPortBlockMaxUtil_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 6),
    _BWagCgnatPortBlockMaxUtil_Type()
)
bWagCgnatPortBlockMaxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPortBlockMaxUtil.setStatus("obsolete")
_BWagCgnatPortBlockMinUtil_Type = Unsigned32
_BWagCgnatPortBlockMinUtil_Object = MibTableColumn
bWagCgnatPortBlockMinUtil = _BWagCgnatPortBlockMinUtil_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 7),
    _BWagCgnatPortBlockMinUtil_Type()
)
bWagCgnatPortBlockMinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPortBlockMinUtil.setStatus("obsolete")
_BWagCgnatIntervalDuration_Type = Unsigned32
_BWagCgnatIntervalDuration_Object = MibTableColumn
bWagCgnatIntervalDuration = _BWagCgnatIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 3, 1, 8),
    _BWagCgnatIntervalDuration_Type()
)
bWagCgnatIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatIntervalDuration.setStatus("obsolete")
_BWagCgnatUnauthIPStatsTable_Object = MibTable
bWagCgnatUnauthIPStatsTable = _BWagCgnatUnauthIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4)
)
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPStatsTable.setStatus("current")
_BWagCgnatUnauthIPStatsEntry_Object = MibTableRow
bWagCgnatUnauthIPStatsEntry = _BWagCgnatUnauthIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1)
)
bWagCgnatUnauthIPStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatUnauthIPStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPStatsEntry.setStatus("current")
_BWagCgnatUnauthIPStatsIndex_Type = Integer32
_BWagCgnatUnauthIPStatsIndex_Object = MibTableColumn
bWagCgnatUnauthIPStatsIndex = _BWagCgnatUnauthIPStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 1),
    _BWagCgnatUnauthIPStatsIndex_Type()
)
bWagCgnatUnauthIPStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPStatsIndex.setStatus("current")
_BWagCgnatUnauthPublicIPAddressType_Type = InetAddressType
_BWagCgnatUnauthPublicIPAddressType_Object = MibTableColumn
bWagCgnatUnauthPublicIPAddressType = _BWagCgnatUnauthPublicIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 2),
    _BWagCgnatUnauthPublicIPAddressType_Type()
)
bWagCgnatUnauthPublicIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPublicIPAddressType.setStatus("current")
_BWagCgnatUnauthPublicIPAddress_Type = InetAddress
_BWagCgnatUnauthPublicIPAddress_Object = MibTableColumn
bWagCgnatUnauthPublicIPAddress = _BWagCgnatUnauthPublicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 3),
    _BWagCgnatUnauthPublicIPAddress_Type()
)
bWagCgnatUnauthPublicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPublicIPAddress.setStatus("current")
_BWagCgnatUnauthIPPortBlocksUsed_Type = Unsigned32
_BWagCgnatUnauthIPPortBlocksUsed_Object = MibTableColumn
bWagCgnatUnauthIPPortBlocksUsed = _BWagCgnatUnauthIPPortBlocksUsed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 4),
    _BWagCgnatUnauthIPPortBlocksUsed_Type()
)
bWagCgnatUnauthIPPortBlocksUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPPortBlocksUsed.setStatus("obsolete")
_BWagCgnatUnauthIPPortBlocksFree_Type = Unsigned32
_BWagCgnatUnauthIPPortBlocksFree_Object = MibTableColumn
bWagCgnatUnauthIPPortBlocksFree = _BWagCgnatUnauthIPPortBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 5),
    _BWagCgnatUnauthIPPortBlocksFree_Type()
)
bWagCgnatUnauthIPPortBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPPortBlocksFree.setStatus("current")
_BWagCgnatUnauthIPPortBlocksReused_Type = Unsigned32
_BWagCgnatUnauthIPPortBlocksReused_Object = MibTableColumn
bWagCgnatUnauthIPPortBlocksReused = _BWagCgnatUnauthIPPortBlocksReused_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 6),
    _BWagCgnatUnauthIPPortBlocksReused_Type()
)
bWagCgnatUnauthIPPortBlocksReused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPPortBlocksReused.setStatus("obsolete")
_BWagCgnatUnauthIPSubActiveCount_Type = Unsigned32
_BWagCgnatUnauthIPSubActiveCount_Object = MibTableColumn
bWagCgnatUnauthIPSubActiveCount = _BWagCgnatUnauthIPSubActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 4, 1, 7),
    _BWagCgnatUnauthIPSubActiveCount_Type()
)
bWagCgnatUnauthIPSubActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPSubActiveCount.setStatus("current")
_BWagCgnatUnauthPeriodIpTable_Object = MibTable
bWagCgnatUnauthPeriodIpTable = _BWagCgnatUnauthPeriodIpTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5)
)
if mibBuilder.loadTexts:
    bWagCgnatUnauthPeriodIpTable.setStatus("obsolete")
_BWagCgnatUnauthPeriodIpEntry_Object = MibTableRow
bWagCgnatUnauthPeriodIpEntry = _BWagCgnatUnauthPeriodIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1)
)
bWagCgnatUnauthPeriodIpEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatUnauthPeriodIpInterval"),
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatUnauthPeriodIpIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatUnauthPeriodIpEntry.setStatus("obsolete")
_BWagCgnatUnauthPeriodIpInterval_Type = Integer32
_BWagCgnatUnauthPeriodIpInterval_Object = MibTableColumn
bWagCgnatUnauthPeriodIpInterval = _BWagCgnatUnauthPeriodIpInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 1),
    _BWagCgnatUnauthPeriodIpInterval_Type()
)
bWagCgnatUnauthPeriodIpInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPeriodIpInterval.setStatus("obsolete")
_BWagCgnatUnauthPeriodIpIndex_Type = Integer32
_BWagCgnatUnauthPeriodIpIndex_Object = MibTableColumn
bWagCgnatUnauthPeriodIpIndex = _BWagCgnatUnauthPeriodIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 2),
    _BWagCgnatUnauthPeriodIpIndex_Type()
)
bWagCgnatUnauthPeriodIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPeriodIpIndex.setStatus("obsolete")
_BWagCgnatUnauthIPAddressType_Type = InetAddressType
_BWagCgnatUnauthIPAddressType_Object = MibTableColumn
bWagCgnatUnauthIPAddressType = _BWagCgnatUnauthIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 3),
    _BWagCgnatUnauthIPAddressType_Type()
)
bWagCgnatUnauthIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPAddressType.setStatus("obsolete")
_BWagCgnatUnauthIPAddress_Type = InetAddress
_BWagCgnatUnauthIPAddress_Object = MibTableColumn
bWagCgnatUnauthIPAddress = _BWagCgnatUnauthIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 4),
    _BWagCgnatUnauthIPAddress_Type()
)
bWagCgnatUnauthIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIPAddress.setStatus("obsolete")
_BWagCgnatUnauthPortBlockMaxUtil_Type = Unsigned32
_BWagCgnatUnauthPortBlockMaxUtil_Object = MibTableColumn
bWagCgnatUnauthPortBlockMaxUtil = _BWagCgnatUnauthPortBlockMaxUtil_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 5),
    _BWagCgnatUnauthPortBlockMaxUtil_Type()
)
bWagCgnatUnauthPortBlockMaxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPortBlockMaxUtil.setStatus("obsolete")
_BWagCgnatUnauthPortBlockMinUtil_Type = Unsigned32
_BWagCgnatUnauthPortBlockMinUtil_Object = MibTableColumn
bWagCgnatUnauthPortBlockMinUtil = _BWagCgnatUnauthPortBlockMinUtil_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 6),
    _BWagCgnatUnauthPortBlockMinUtil_Type()
)
bWagCgnatUnauthPortBlockMinUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthPortBlockMinUtil.setStatus("obsolete")
_BWagCgnatUnauthIntervalDuration_Type = Unsigned32
_BWagCgnatUnauthIntervalDuration_Object = MibTableColumn
bWagCgnatUnauthIntervalDuration = _BWagCgnatUnauthIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 5, 1, 7),
    _BWagCgnatUnauthIntervalDuration_Type()
)
bWagCgnatUnauthIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatUnauthIntervalDuration.setStatus("obsolete")
_BWagCgnatAuthPortUtilTable_Object = MibTable
bWagCgnatAuthPortUtilTable = _BWagCgnatAuthPortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 6)
)
if mibBuilder.loadTexts:
    bWagCgnatAuthPortUtilTable.setStatus("obsolete")
_BWagCgnatAuthPortUtilEntry_Object = MibTableRow
bWagCgnatAuthPortUtilEntry = _BWagCgnatAuthPortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 6, 1)
)
bWagCgnatAuthPortUtilEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatAuthSubscriberMac"),
)
if mibBuilder.loadTexts:
    bWagCgnatAuthPortUtilEntry.setStatus("obsolete")
_BWagCgnatAuthSubscriberMac_Type = MacAddress
_BWagCgnatAuthSubscriberMac_Object = MibTableColumn
bWagCgnatAuthSubscriberMac = _BWagCgnatAuthSubscriberMac_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 6, 1, 1),
    _BWagCgnatAuthSubscriberMac_Type()
)
bWagCgnatAuthSubscriberMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatAuthSubscriberMac.setStatus("obsolete")
_BWagCgnatAuthSubscriberPortsUtil_Type = Unsigned32
_BWagCgnatAuthSubscriberPortsUtil_Object = MibTableColumn
bWagCgnatAuthSubscriberPortsUtil = _BWagCgnatAuthSubscriberPortsUtil_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 6, 1, 2),
    _BWagCgnatAuthSubscriberPortsUtil_Type()
)
bWagCgnatAuthSubscriberPortsUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatAuthSubscriberPortsUtil.setStatus("obsolete")
_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Type = Unsigned32
_BWagCgnatAuthPortRisingThresholdCrossedSubCount_Object = MibScalar
bWagCgnatAuthPortRisingThresholdCrossedSubCount = _BWagCgnatAuthPortRisingThresholdCrossedSubCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 7),
    _BWagCgnatAuthPortRisingThresholdCrossedSubCount_Type()
)
bWagCgnatAuthPortRisingThresholdCrossedSubCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatAuthPortRisingThresholdCrossedSubCount.setStatus("obsolete")
_BWagCgnatPoolGroupStatsTable_Object = MibTable
bWagCgnatPoolGroupStatsTable = _BWagCgnatPoolGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8)
)
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupStatsTable.setStatus("current")
_BWagCgnatPoolGroupStatsEntry_Object = MibTableRow
bWagCgnatPoolGroupStatsEntry = _BWagCgnatPoolGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1)
)
bWagCgnatPoolGroupStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatPoolGroupType"),
    (0, "BENU-WAG-STATS-MIB", "bWagCgnatPoolGroupIndex"),
)
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupStatsEntry.setStatus("current")


class _BWagCgnatPoolGroupType_Type(Integer32):
    """Custom type bWagCgnatPoolGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authNapt", 2),
          ("none", 0),
          ("unAuthNapt", 1))
    )


_BWagCgnatPoolGroupType_Type.__name__ = "Integer32"
_BWagCgnatPoolGroupType_Object = MibTableColumn
bWagCgnatPoolGroupType = _BWagCgnatPoolGroupType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 1),
    _BWagCgnatPoolGroupType_Type()
)
bWagCgnatPoolGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupType.setStatus("current")
_BWagCgnatPoolGroupIndex_Type = Unsigned32
_BWagCgnatPoolGroupIndex_Object = MibTableColumn
bWagCgnatPoolGroupIndex = _BWagCgnatPoolGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 2),
    _BWagCgnatPoolGroupIndex_Type()
)
bWagCgnatPoolGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupIndex.setStatus("current")


class _BWagCgnatPoolGroupName_Type(DisplayString):
    """Custom type bWagCgnatPoolGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BWagCgnatPoolGroupName_Type.__name__ = "DisplayString"
_BWagCgnatPoolGroupName_Object = MibTableColumn
bWagCgnatPoolGroupName = _BWagCgnatPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 3),
    _BWagCgnatPoolGroupName_Type()
)
bWagCgnatPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupName.setStatus("current")
_BWagCgnatPoolGroupSubscribers_Type = Unsigned32
_BWagCgnatPoolGroupSubscribers_Object = MibTableColumn
bWagCgnatPoolGroupSubscribers = _BWagCgnatPoolGroupSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 4),
    _BWagCgnatPoolGroupSubscribers_Type()
)
bWagCgnatPoolGroupSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupSubscribers.setStatus("current")
_BWagCgnatPoolGroupUsedIPAddresses_Type = Unsigned32
_BWagCgnatPoolGroupUsedIPAddresses_Object = MibTableColumn
bWagCgnatPoolGroupUsedIPAddresses = _BWagCgnatPoolGroupUsedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 5),
    _BWagCgnatPoolGroupUsedIPAddresses_Type()
)
bWagCgnatPoolGroupUsedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupUsedIPAddresses.setStatus("current")
_BWagCgnatPoolGroupReservedIPAddresses_Type = Unsigned32
_BWagCgnatPoolGroupReservedIPAddresses_Object = MibTableColumn
bWagCgnatPoolGroupReservedIPAddresses = _BWagCgnatPoolGroupReservedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 6),
    _BWagCgnatPoolGroupReservedIPAddresses_Type()
)
bWagCgnatPoolGroupReservedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupReservedIPAddresses.setStatus("current")
_BWagCgnatPoolGroupTotalIPAddresses_Type = Unsigned32
_BWagCgnatPoolGroupTotalIPAddresses_Object = MibTableColumn
bWagCgnatPoolGroupTotalIPAddresses = _BWagCgnatPoolGroupTotalIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 9, 8, 1, 7),
    _BWagCgnatPoolGroupTotalIPAddresses_Type()
)
bWagCgnatPoolGroupTotalIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagCgnatPoolGroupTotalIPAddresses.setStatus("current")
_BWagCgnatNotifObjects_ObjectIdentity = ObjectIdentity
bWagCgnatNotifObjects = _BWagCgnatNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10)
)
if mibBuilder.loadTexts:
    bWagCgnatNotifObjects.setStatus("current")
_BWagCgnatProfileIPPoolGroup_Type = DisplayString
_BWagCgnatProfileIPPoolGroup_Object = MibScalar
bWagCgnatProfileIPPoolGroup = _BWagCgnatProfileIPPoolGroup_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 1),
    _BWagCgnatProfileIPPoolGroup_Type()
)
bWagCgnatProfileIPPoolGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatProfileIPPoolGroup.setStatus("current")
_BWagCgnatTotalPoolIPAddresses_Type = Unsigned32
_BWagCgnatTotalPoolIPAddresses_Object = MibScalar
bWagCgnatTotalPoolIPAddresses = _BWagCgnatTotalPoolIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 2),
    _BWagCgnatTotalPoolIPAddresses_Type()
)
bWagCgnatTotalPoolIPAddresses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatTotalPoolIPAddresses.setStatus("current")
_BWagCgnatAuthIpAddrUsedHighThreshold_Type = Unsigned32
_BWagCgnatAuthIpAddrUsedHighThreshold_Object = MibScalar
bWagCgnatAuthIpAddrUsedHighThreshold = _BWagCgnatAuthIpAddrUsedHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 3),
    _BWagCgnatAuthIpAddrUsedHighThreshold_Type()
)
bWagCgnatAuthIpAddrUsedHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatAuthIpAddrUsedHighThreshold.setStatus("current")
_BWagCgnatAuthIpAddrUsedLowThreshold_Type = Unsigned32
_BWagCgnatAuthIpAddrUsedLowThreshold_Object = MibScalar
bWagCgnatAuthIpAddrUsedLowThreshold = _BWagCgnatAuthIpAddrUsedLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 4),
    _BWagCgnatAuthIpAddrUsedLowThreshold_Type()
)
bWagCgnatAuthIpAddrUsedLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatAuthIpAddrUsedLowThreshold.setStatus("current")
_BWagCgnatSubscriberMac_Type = MacAddress
_BWagCgnatSubscriberMac_Object = MibScalar
bWagCgnatSubscriberMac = _BWagCgnatSubscriberMac_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 5),
    _BWagCgnatSubscriberMac_Type()
)
bWagCgnatSubscriberMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatSubscriberMac.setStatus("obsolete")
_BWagCgnatTotalPortBlocksPerSubscriber_Type = Unsigned32
_BWagCgnatTotalPortBlocksPerSubscriber_Object = MibScalar
bWagCgnatTotalPortBlocksPerSubscriber = _BWagCgnatTotalPortBlocksPerSubscriber_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 6),
    _BWagCgnatTotalPortBlocksPerSubscriber_Type()
)
bWagCgnatTotalPortBlocksPerSubscriber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatTotalPortBlocksPerSubscriber.setStatus("obsolete")
_BWagCgnatPortBlocksUsedHighThreshold_Type = Unsigned32
_BWagCgnatPortBlocksUsedHighThreshold_Object = MibScalar
bWagCgnatPortBlocksUsedHighThreshold = _BWagCgnatPortBlocksUsedHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 7),
    _BWagCgnatPortBlocksUsedHighThreshold_Type()
)
bWagCgnatPortBlocksUsedHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatPortBlocksUsedHighThreshold.setStatus("obsolete")
_BWagCgnatPortBlocksUsedLowThreshold_Type = Unsigned32
_BWagCgnatPortBlocksUsedLowThreshold_Object = MibScalar
bWagCgnatPortBlocksUsedLowThreshold = _BWagCgnatPortBlocksUsedLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 10, 8),
    _BWagCgnatPortBlocksUsedLowThreshold_Type()
)
bWagCgnatPortBlocksUsedLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagCgnatPortBlocksUsedLowThreshold.setStatus("obsolete")
_BWagProcessingLatencyMIBObjects_ObjectIdentity = ObjectIdentity
bWagProcessingLatencyMIBObjects = _BWagProcessingLatencyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11)
)
if mibBuilder.loadTexts:
    bWagProcessingLatencyMIBObjects.setStatus("current")
_BWagUpstreamProcessingLatencyPktCount_Type = Unsigned32
_BWagUpstreamProcessingLatencyPktCount_Object = MibScalar
bWagUpstreamProcessingLatencyPktCount = _BWagUpstreamProcessingLatencyPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 1),
    _BWagUpstreamProcessingLatencyPktCount_Type()
)
bWagUpstreamProcessingLatencyPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagUpstreamProcessingLatencyPktCount.setStatus("obsolete")
_BWagUpstreamProcessingLatencyMax_Type = Unsigned32
_BWagUpstreamProcessingLatencyMax_Object = MibScalar
bWagUpstreamProcessingLatencyMax = _BWagUpstreamProcessingLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 2),
    _BWagUpstreamProcessingLatencyMax_Type()
)
bWagUpstreamProcessingLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagUpstreamProcessingLatencyMax.setStatus("obsolete")
_BWagUpstreamProcessingLatencyMin_Type = Unsigned32
_BWagUpstreamProcessingLatencyMin_Object = MibScalar
bWagUpstreamProcessingLatencyMin = _BWagUpstreamProcessingLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 3),
    _BWagUpstreamProcessingLatencyMin_Type()
)
bWagUpstreamProcessingLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagUpstreamProcessingLatencyMin.setStatus("obsolete")
_BWagUpstreamProcessingLatencyAvg_Type = Unsigned32
_BWagUpstreamProcessingLatencyAvg_Object = MibScalar
bWagUpstreamProcessingLatencyAvg = _BWagUpstreamProcessingLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 4),
    _BWagUpstreamProcessingLatencyAvg_Type()
)
bWagUpstreamProcessingLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagUpstreamProcessingLatencyAvg.setStatus("obsolete")
_BWagDownstreamProcessingLatencyPktCount_Type = Unsigned32
_BWagDownstreamProcessingLatencyPktCount_Object = MibScalar
bWagDownstreamProcessingLatencyPktCount = _BWagDownstreamProcessingLatencyPktCount_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 5),
    _BWagDownstreamProcessingLatencyPktCount_Type()
)
bWagDownstreamProcessingLatencyPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDownstreamProcessingLatencyPktCount.setStatus("obsolete")
_BWagDownstreamProcessingLatencyMax_Type = Unsigned32
_BWagDownstreamProcessingLatencyMax_Object = MibScalar
bWagDownstreamProcessingLatencyMax = _BWagDownstreamProcessingLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 6),
    _BWagDownstreamProcessingLatencyMax_Type()
)
bWagDownstreamProcessingLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDownstreamProcessingLatencyMax.setStatus("obsolete")
_BWagDownstreamProcessingLatencyMin_Type = Unsigned32
_BWagDownstreamProcessingLatencyMin_Object = MibScalar
bWagDownstreamProcessingLatencyMin = _BWagDownstreamProcessingLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 7),
    _BWagDownstreamProcessingLatencyMin_Type()
)
bWagDownstreamProcessingLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDownstreamProcessingLatencyMin.setStatus("obsolete")
_BWagDownstreamProcessingLatencyAvg_Type = Unsigned32
_BWagDownstreamProcessingLatencyAvg_Object = MibScalar
bWagDownstreamProcessingLatencyAvg = _BWagDownstreamProcessingLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 11, 8),
    _BWagDownstreamProcessingLatencyAvg_Type()
)
bWagDownstreamProcessingLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDownstreamProcessingLatencyAvg.setStatus("obsolete")
_BWagProcessingLatencyNotifObjects_ObjectIdentity = ObjectIdentity
bWagProcessingLatencyNotifObjects = _BWagProcessingLatencyNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 12)
)
if mibBuilder.loadTexts:
    bWagProcessingLatencyNotifObjects.setStatus("current")
_BWagDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
bWagDhcpv6MIBObjects = _BWagDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13)
)
if mibBuilder.loadTexts:
    bWagDhcpv6MIBObjects.setStatus("current")
_BWagDHCPv6Table_Object = MibTable
bWagDHCPv6Table = _BWagDHCPv6Table_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1)
)
if mibBuilder.loadTexts:
    bWagDHCPv6Table.setStatus("current")
_BWagDHCPv6Entry_Object = MibTableRow
bWagDHCPv6Entry = _BWagDHCPv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1)
)
bWagDHCPv6Entry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagDHCPv6StatsInterval"),
)
if mibBuilder.loadTexts:
    bWagDHCPv6Entry.setStatus("current")
_BWagDHCPv6StatsInterval_Type = Integer32
_BWagDHCPv6StatsInterval_Object = MibTableColumn
bWagDHCPv6StatsInterval = _BWagDHCPv6StatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 1),
    _BWagDHCPv6StatsInterval_Type()
)
bWagDHCPv6StatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagDHCPv6StatsInterval.setStatus("current")
_BWagDHCPv6IntervalDuration_Type = Integer32
_BWagDHCPv6IntervalDuration_Object = MibTableColumn
bWagDHCPv6IntervalDuration = _BWagDHCPv6IntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 2),
    _BWagDHCPv6IntervalDuration_Type()
)
bWagDHCPv6IntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6IntervalDuration.setStatus("current")
_BWagDHCPv6SolicitReplyIntervalMin_Type = Unsigned32
_BWagDHCPv6SolicitReplyIntervalMin_Object = MibTableColumn
bWagDHCPv6SolicitReplyIntervalMin = _BWagDHCPv6SolicitReplyIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 3),
    _BWagDHCPv6SolicitReplyIntervalMin_Type()
)
bWagDHCPv6SolicitReplyIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitReplyIntervalMin.setStatus("current")
_BWagDHCPv6SolicitReplyIntervalMax_Type = Unsigned32
_BWagDHCPv6SolicitReplyIntervalMax_Object = MibTableColumn
bWagDHCPv6SolicitReplyIntervalMax = _BWagDHCPv6SolicitReplyIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 4),
    _BWagDHCPv6SolicitReplyIntervalMax_Type()
)
bWagDHCPv6SolicitReplyIntervalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitReplyIntervalMax.setStatus("current")
_BWagDHCPv6SolicitReplyIntervalAvg_Type = Unsigned32
_BWagDHCPv6SolicitReplyIntervalAvg_Object = MibTableColumn
bWagDHCPv6SolicitReplyIntervalAvg = _BWagDHCPv6SolicitReplyIntervalAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 5),
    _BWagDHCPv6SolicitReplyIntervalAvg_Type()
)
bWagDHCPv6SolicitReplyIntervalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitReplyIntervalAvg.setStatus("current")
_BWagDHCPv6SolicitReplyIntervalLast_Type = Unsigned32
_BWagDHCPv6SolicitReplyIntervalLast_Object = MibTableColumn
bWagDHCPv6SolicitReplyIntervalLast = _BWagDHCPv6SolicitReplyIntervalLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 6),
    _BWagDHCPv6SolicitReplyIntervalLast_Type()
)
bWagDHCPv6SolicitReplyIntervalLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitReplyIntervalLast.setStatus("current")
_BWagDHCPv6RequestReplyLatencyMin_Type = Unsigned32
_BWagDHCPv6RequestReplyLatencyMin_Object = MibTableColumn
bWagDHCPv6RequestReplyLatencyMin = _BWagDHCPv6RequestReplyLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 7),
    _BWagDHCPv6RequestReplyLatencyMin_Type()
)
bWagDHCPv6RequestReplyLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6RequestReplyLatencyMin.setStatus("current")
_BWagDHCPv6RequestReplyLatencyMax_Type = Unsigned32
_BWagDHCPv6RequestReplyLatencyMax_Object = MibTableColumn
bWagDHCPv6RequestReplyLatencyMax = _BWagDHCPv6RequestReplyLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 8),
    _BWagDHCPv6RequestReplyLatencyMax_Type()
)
bWagDHCPv6RequestReplyLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6RequestReplyLatencyMax.setStatus("current")
_BWagDHCPv6RequestReplyLatencyAvg_Type = Unsigned32
_BWagDHCPv6RequestReplyLatencyAvg_Object = MibTableColumn
bWagDHCPv6RequestReplyLatencyAvg = _BWagDHCPv6RequestReplyLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 9),
    _BWagDHCPv6RequestReplyLatencyAvg_Type()
)
bWagDHCPv6RequestReplyLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6RequestReplyLatencyAvg.setStatus("current")
_BWagDHCPv6RequestReplyLatencyLast_Type = Unsigned32
_BWagDHCPv6RequestReplyLatencyLast_Object = MibTableColumn
bWagDHCPv6RequestReplyLatencyLast = _BWagDHCPv6RequestReplyLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 10),
    _BWagDHCPv6RequestReplyLatencyLast_Type()
)
bWagDHCPv6RequestReplyLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6RequestReplyLatencyLast.setStatus("current")
_BWagDHCPv6SolicitAdvLatencyMin_Type = Unsigned32
_BWagDHCPv6SolicitAdvLatencyMin_Object = MibTableColumn
bWagDHCPv6SolicitAdvLatencyMin = _BWagDHCPv6SolicitAdvLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 11),
    _BWagDHCPv6SolicitAdvLatencyMin_Type()
)
bWagDHCPv6SolicitAdvLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitAdvLatencyMin.setStatus("current")
_BWagDHCPv6SolicitAdvLatencyMax_Type = Unsigned32
_BWagDHCPv6SolicitAdvLatencyMax_Object = MibTableColumn
bWagDHCPv6SolicitAdvLatencyMax = _BWagDHCPv6SolicitAdvLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 12),
    _BWagDHCPv6SolicitAdvLatencyMax_Type()
)
bWagDHCPv6SolicitAdvLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitAdvLatencyMax.setStatus("current")
_BWagDHCPv6SolicitAdvLatencyAvg_Type = Unsigned32
_BWagDHCPv6SolicitAdvLatencyAvg_Object = MibTableColumn
bWagDHCPv6SolicitAdvLatencyAvg = _BWagDHCPv6SolicitAdvLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 13),
    _BWagDHCPv6SolicitAdvLatencyAvg_Type()
)
bWagDHCPv6SolicitAdvLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitAdvLatencyAvg.setStatus("current")
_BWagDHCPv6SolicitAdvLatencyLast_Type = Unsigned32
_BWagDHCPv6SolicitAdvLatencyLast_Object = MibTableColumn
bWagDHCPv6SolicitAdvLatencyLast = _BWagDHCPv6SolicitAdvLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 14),
    _BWagDHCPv6SolicitAdvLatencyLast_Type()
)
bWagDHCPv6SolicitAdvLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitAdvLatencyLast.setStatus("current")
_BWagDHCPv6AdvRequestIntervalMin_Type = Unsigned32
_BWagDHCPv6AdvRequestIntervalMin_Object = MibTableColumn
bWagDHCPv6AdvRequestIntervalMin = _BWagDHCPv6AdvRequestIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 15),
    _BWagDHCPv6AdvRequestIntervalMin_Type()
)
bWagDHCPv6AdvRequestIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6AdvRequestIntervalMin.setStatus("current")
_BWagDHCPv6AdvRequestIntervalMax_Type = Unsigned32
_BWagDHCPv6AdvRequestIntervalMax_Object = MibTableColumn
bWagDHCPv6AdvRequestIntervalMax = _BWagDHCPv6AdvRequestIntervalMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 16),
    _BWagDHCPv6AdvRequestIntervalMax_Type()
)
bWagDHCPv6AdvRequestIntervalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6AdvRequestIntervalMax.setStatus("current")
_BWagDHCPv6AdvRequestIntervalAvg_Type = Unsigned32
_BWagDHCPv6AdvRequestIntervalAvg_Object = MibTableColumn
bWagDHCPv6AdvRequestIntervalAvg = _BWagDHCPv6AdvRequestIntervalAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 17),
    _BWagDHCPv6AdvRequestIntervalAvg_Type()
)
bWagDHCPv6AdvRequestIntervalAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6AdvRequestIntervalAvg.setStatus("current")
_BWagDHCPv6AdvRequestIntervalLast_Type = Unsigned32
_BWagDHCPv6AdvRequestIntervalLast_Object = MibTableColumn
bWagDHCPv6AdvRequestIntervalLast = _BWagDHCPv6AdvRequestIntervalLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 18),
    _BWagDHCPv6AdvRequestIntervalLast_Type()
)
bWagDHCPv6AdvRequestIntervalLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6AdvRequestIntervalLast.setStatus("current")
_BWagDHCPv6SolicitReceived_Type = Unsigned32
_BWagDHCPv6SolicitReceived_Object = MibTableColumn
bWagDHCPv6SolicitReceived = _BWagDHCPv6SolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 19),
    _BWagDHCPv6SolicitReceived_Type()
)
bWagDHCPv6SolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6SolicitReceived.setStatus("current")
_BWagDHCPv6AdvertisementSent_Type = Unsigned32
_BWagDHCPv6AdvertisementSent_Object = MibTableColumn
bWagDHCPv6AdvertisementSent = _BWagDHCPv6AdvertisementSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 20),
    _BWagDHCPv6AdvertisementSent_Type()
)
bWagDHCPv6AdvertisementSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6AdvertisementSent.setStatus("current")
_BWagDHCPv6RequestReceived_Type = Unsigned32
_BWagDHCPv6RequestReceived_Object = MibTableColumn
bWagDHCPv6RequestReceived = _BWagDHCPv6RequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 21),
    _BWagDHCPv6RequestReceived_Type()
)
bWagDHCPv6RequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6RequestReceived.setStatus("current")
_BWagDHCPv6ReplySent_Type = Unsigned32
_BWagDHCPv6ReplySent_Object = MibTableColumn
bWagDHCPv6ReplySent = _BWagDHCPv6ReplySent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 13, 1, 1, 22),
    _BWagDHCPv6ReplySent_Type()
)
bWagDHCPv6ReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDHCPv6ReplySent.setStatus("current")
_BWagMHNMIBObjects_ObjectIdentity = ObjectIdentity
bWagMHNMIBObjects = _BWagMHNMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14)
)
if mibBuilder.loadTexts:
    bWagMHNMIBObjects.setStatus("current")
_BWagMHNProfileStatsTable_Object = MibTable
bWagMHNProfileStatsTable = _BWagMHNProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1)
)
if mibBuilder.loadTexts:
    bWagMHNProfileStatsTable.setStatus("current")
_BWagMHNProfileStatsEntry_Object = MibTableRow
bWagMHNProfileStatsEntry = _BWagMHNProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1)
)
bWagMHNProfileStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagMHNProfileStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagMHNProfileStatsEntry.setStatus("current")
_BWagMHNProfileStatsIndex_Type = Integer32
_BWagMHNProfileStatsIndex_Object = MibTableColumn
bWagMHNProfileStatsIndex = _BWagMHNProfileStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 1),
    _BWagMHNProfileStatsIndex_Type()
)
bWagMHNProfileStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagMHNProfileStatsIndex.setStatus("current")
_BWagMHNProfileName_Type = DisplayString
_BWagMHNProfileName_Object = MibTableColumn
bWagMHNProfileName = _BWagMHNProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 2),
    _BWagMHNProfileName_Type()
)
bWagMHNProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileName.setStatus("current")
_BWagMHNProfileNATIPPoolGroup_Type = DisplayString
_BWagMHNProfileNATIPPoolGroup_Object = MibTableColumn
bWagMHNProfileNATIPPoolGroup = _BWagMHNProfileNATIPPoolGroup_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 3),
    _BWagMHNProfileNATIPPoolGroup_Type()
)
bWagMHNProfileNATIPPoolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileNATIPPoolGroup.setStatus("current")
_BWagMHNProfileMaxSubscribers_Type = Unsigned32
_BWagMHNProfileMaxSubscribers_Object = MibTableColumn
bWagMHNProfileMaxSubscribers = _BWagMHNProfileMaxSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 4),
    _BWagMHNProfileMaxSubscribers_Type()
)
bWagMHNProfileMaxSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileMaxSubscribers.setStatus("current")
_BWagMHNProfileMaxIPAddresses_Type = Unsigned32
_BWagMHNProfileMaxIPAddresses_Object = MibTableColumn
bWagMHNProfileMaxIPAddresses = _BWagMHNProfileMaxIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 5),
    _BWagMHNProfileMaxIPAddresses_Type()
)
bWagMHNProfileMaxIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileMaxIPAddresses.setStatus("current")
_BWagMHNProfileUsedIPAddresses_Type = Unsigned32
_BWagMHNProfileUsedIPAddresses_Object = MibTableColumn
bWagMHNProfileUsedIPAddresses = _BWagMHNProfileUsedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 6),
    _BWagMHNProfileUsedIPAddresses_Type()
)
bWagMHNProfileUsedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileUsedIPAddresses.setStatus("current")
_BWagMHNProfileTotalPortBlocks_Type = Unsigned32
_BWagMHNProfileTotalPortBlocks_Object = MibTableColumn
bWagMHNProfileTotalPortBlocks = _BWagMHNProfileTotalPortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 7),
    _BWagMHNProfileTotalPortBlocks_Type()
)
bWagMHNProfileTotalPortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileTotalPortBlocks.setStatus("current")
_BWagMHNProfileTotalPoolIPAddresses_Type = Unsigned32
_BWagMHNProfileTotalPoolIPAddresses_Object = MibTableColumn
bWagMHNProfileTotalPoolIPAddresses = _BWagMHNProfileTotalPoolIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 14, 1, 1, 8),
    _BWagMHNProfileTotalPoolIPAddresses_Type()
)
bWagMHNProfileTotalPoolIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagMHNProfileTotalPoolIPAddresses.setStatus("current")
_BWagVrgApiNotifObjects_ObjectIdentity = ObjectIdentity
bWagVrgApiNotifObjects = _BWagVrgApiNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 15)
)
if mibBuilder.loadTexts:
    bWagVrgApiNotifObjects.setStatus("current")
_BWagVrgApiIpAddrUsedHighThreshold_Type = Unsigned32
_BWagVrgApiIpAddrUsedHighThreshold_Object = MibScalar
bWagVrgApiIpAddrUsedHighThreshold = _BWagVrgApiIpAddrUsedHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 15, 1),
    _BWagVrgApiIpAddrUsedHighThreshold_Type()
)
bWagVrgApiIpAddrUsedHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagVrgApiIpAddrUsedHighThreshold.setStatus("current")
_BWagVrgApiIpAddrUsedLowThreshold_Type = Unsigned32
_BWagVrgApiIpAddrUsedLowThreshold_Object = MibScalar
bWagVrgApiIpAddrUsedLowThreshold = _BWagVrgApiIpAddrUsedLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 15, 2),
    _BWagVrgApiIpAddrUsedLowThreshold_Type()
)
bWagVrgApiIpAddrUsedLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagVrgApiIpAddrUsedLowThreshold.setStatus("current")
_BWagrgApiIPPoolGroup_Type = DisplayString
_BWagrgApiIPPoolGroup_Object = MibScalar
bWagrgApiIPPoolGroup = _BWagrgApiIPPoolGroup_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 15, 3),
    _BWagrgApiIPPoolGroup_Type()
)
bWagrgApiIPPoolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagrgApiIPPoolGroup.setStatus("current")
_BWagVRGApiIPoolIPAddresses_Type = Unsigned32
_BWagVRGApiIPoolIPAddresses_Object = MibScalar
bWagVRGApiIPoolIPAddresses = _BWagVRGApiIPoolIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 15, 4),
    _BWagVRGApiIPoolIPAddresses_Type()
)
bWagVRGApiIPoolIPAddresses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bWagVRGApiIPoolIPAddresses.setStatus("current")
_BWagDsLiteMIBObjects_ObjectIdentity = ObjectIdentity
bWagDsLiteMIBObjects = _BWagDsLiteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16)
)
if mibBuilder.loadTexts:
    bWagDsLiteMIBObjects.setStatus("current")
_BWagDsLiteProfileStatsTable_Object = MibTable
bWagDsLiteProfileStatsTable = _BWagDsLiteProfileStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1)
)
if mibBuilder.loadTexts:
    bWagDsLiteProfileStatsTable.setStatus("current")
_BWagDsLiteProfileStatsEntry_Object = MibTableRow
bWagDsLiteProfileStatsEntry = _BWagDsLiteProfileStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1)
)
bWagDsLiteProfileStatsEntry.setIndexNames(
    (0, "BENU-WAG-STATS-MIB", "bWagDsLiteProfileStatsIndex"),
)
if mibBuilder.loadTexts:
    bWagDsLiteProfileStatsEntry.setStatus("current")
_BWagDsLiteProfileStatsIndex_Type = Integer32
_BWagDsLiteProfileStatsIndex_Object = MibTableColumn
bWagDsLiteProfileStatsIndex = _BWagDsLiteProfileStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 1),
    _BWagDsLiteProfileStatsIndex_Type()
)
bWagDsLiteProfileStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bWagDsLiteProfileStatsIndex.setStatus("current")
_BWagDsLiteProfileName_Type = DisplayString
_BWagDsLiteProfileName_Object = MibTableColumn
bWagDsLiteProfileName = _BWagDsLiteProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 2),
    _BWagDsLiteProfileName_Type()
)
bWagDsLiteProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileName.setStatus("current")
_BWagDsLiteProfileType_Type = DisplayString
_BWagDsLiteProfileType_Object = MibTableColumn
bWagDsLiteProfileType = _BWagDsLiteProfileType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 3),
    _BWagDsLiteProfileType_Type()
)
bWagDsLiteProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileType.setStatus("current")
_BWagDsLiteProfileNATIPPoolGroup_Type = DisplayString
_BWagDsLiteProfileNATIPPoolGroup_Object = MibTableColumn
bWagDsLiteProfileNATIPPoolGroup = _BWagDsLiteProfileNATIPPoolGroup_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 4),
    _BWagDsLiteProfileNATIPPoolGroup_Type()
)
bWagDsLiteProfileNATIPPoolGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileNATIPPoolGroup.setStatus("current")
_BWagDsLiteProfileMaxIPAddresses_Type = Unsigned32
_BWagDsLiteProfileMaxIPAddresses_Object = MibTableColumn
bWagDsLiteProfileMaxIPAddresses = _BWagDsLiteProfileMaxIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 5),
    _BWagDsLiteProfileMaxIPAddresses_Type()
)
bWagDsLiteProfileMaxIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileMaxIPAddresses.setStatus("current")
_BWagDsLiteProfileUsedIPAddresses_Type = Unsigned32
_BWagDsLiteProfileUsedIPAddresses_Object = MibTableColumn
bWagDsLiteProfileUsedIPAddresses = _BWagDsLiteProfileUsedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 6),
    _BWagDsLiteProfileUsedIPAddresses_Type()
)
bWagDsLiteProfileUsedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileUsedIPAddresses.setStatus("current")
_BWagDsLiteProfileReservedIPAddresses_Type = Unsigned32
_BWagDsLiteProfileReservedIPAddresses_Object = MibTableColumn
bWagDsLiteProfileReservedIPAddresses = _BWagDsLiteProfileReservedIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 7),
    _BWagDsLiteProfileReservedIPAddresses_Type()
)
bWagDsLiteProfileReservedIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileReservedIPAddresses.setStatus("current")
_BWagDsLiteProfileTotalPoolIPAddresses_Type = Unsigned32
_BWagDsLiteProfileTotalPoolIPAddresses_Object = MibTableColumn
bWagDsLiteProfileTotalPoolIPAddresses = _BWagDsLiteProfileTotalPoolIPAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 8),
    _BWagDsLiteProfileTotalPoolIPAddresses_Type()
)
bWagDsLiteProfileTotalPoolIPAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileTotalPoolIPAddresses.setStatus("current")
_BWagDsLiteProfileMaxSubscribers_Type = Unsigned32
_BWagDsLiteProfileMaxSubscribers_Object = MibTableColumn
bWagDsLiteProfileMaxSubscribers = _BWagDsLiteProfileMaxSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 9),
    _BWagDsLiteProfileMaxSubscribers_Type()
)
bWagDsLiteProfileMaxSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileMaxSubscribers.setStatus("current")
_BWagDsLiteProfileMaxTunnels_Type = Unsigned32
_BWagDsLiteProfileMaxTunnels_Object = MibTableColumn
bWagDsLiteProfileMaxTunnels = _BWagDsLiteProfileMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 1, 1, 10),
    _BWagDsLiteProfileMaxTunnels_Type()
)
bWagDsLiteProfileMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagDsLiteProfileMaxTunnels.setStatus("obsolete")
_BDSLitePortBlocksTotal_Type = Unsigned32
_BDSLitePortBlocksTotal_Object = MibScalar
bDSLitePortBlocksTotal = _BDSLitePortBlocksTotal_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 2),
    _BDSLitePortBlocksTotal_Type()
)
bDSLitePortBlocksTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLitePortBlocksTotal.setStatus("current")
_BDSLitePortBlocksInUse_Type = Unsigned32
_BDSLitePortBlocksInUse_Object = MibScalar
bDSLitePortBlocksInUse = _BDSLitePortBlocksInUse_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 3),
    _BDSLitePortBlocksInUse_Type()
)
bDSLitePortBlocksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLitePortBlocksInUse.setStatus("current")
_BDSLiteTunnelsUsingOnePortBlock_Type = Unsigned32
_BDSLiteTunnelsUsingOnePortBlock_Object = MibScalar
bDSLiteTunnelsUsingOnePortBlock = _BDSLiteTunnelsUsingOnePortBlock_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 4),
    _BDSLiteTunnelsUsingOnePortBlock_Type()
)
bDSLiteTunnelsUsingOnePortBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLiteTunnelsUsingOnePortBlock.setStatus("current")
_BDSLiteTunnelsUsingTwoPortBlocks_Type = Unsigned32
_BDSLiteTunnelsUsingTwoPortBlocks_Object = MibScalar
bDSLiteTunnelsUsingTwoPortBlocks = _BDSLiteTunnelsUsingTwoPortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 5),
    _BDSLiteTunnelsUsingTwoPortBlocks_Type()
)
bDSLiteTunnelsUsingTwoPortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLiteTunnelsUsingTwoPortBlocks.setStatus("current")
_BDSLiteTunnelsUsingThreePortBlocks_Type = Unsigned32
_BDSLiteTunnelsUsingThreePortBlocks_Object = MibScalar
bDSLiteTunnelsUsingThreePortBlocks = _BDSLiteTunnelsUsingThreePortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 6),
    _BDSLiteTunnelsUsingThreePortBlocks_Type()
)
bDSLiteTunnelsUsingThreePortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLiteTunnelsUsingThreePortBlocks.setStatus("current")
_BDSLiteTunnelsUsingFourPortBlocks_Type = Unsigned32
_BDSLiteTunnelsUsingFourPortBlocks_Object = MibScalar
bDSLiteTunnelsUsingFourPortBlocks = _BDSLiteTunnelsUsingFourPortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 7),
    _BDSLiteTunnelsUsingFourPortBlocks_Type()
)
bDSLiteTunnelsUsingFourPortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLiteTunnelsUsingFourPortBlocks.setStatus("current")
_BDSLiteTunnelsUsingFivePortBlocks_Type = Unsigned32
_BDSLiteTunnelsUsingFivePortBlocks_Object = MibScalar
bDSLiteTunnelsUsingFivePortBlocks = _BDSLiteTunnelsUsingFivePortBlocks_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 16, 8),
    _BDSLiteTunnelsUsingFivePortBlocks_Type()
)
bDSLiteTunnelsUsingFivePortBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDSLiteTunnelsUsingFivePortBlocks.setStatus("current")
_BWagDsLiteNotifObjects_ObjectIdentity = ObjectIdentity
bWagDsLiteNotifObjects = _BWagDsLiteNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 17)
)
if mibBuilder.loadTexts:
    bWagDsLiteNotifObjects.setStatus("current")
_BWagIpSystemStatsMIBObjects_ObjectIdentity = ObjectIdentity
bWagIpSystemStatsMIBObjects = _BWagIpSystemStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18)
)
if mibBuilder.loadTexts:
    bWagIpSystemStatsMIBObjects.setStatus("current")
_BWagIpSystemStatsReasmReqds_Type = Counter64
_BWagIpSystemStatsReasmReqds_Object = MibScalar
bWagIpSystemStatsReasmReqds = _BWagIpSystemStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 1),
    _BWagIpSystemStatsReasmReqds_Type()
)
bWagIpSystemStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpSystemStatsReasmReqds.setStatus("current")
_BWagIpIfStatsOutFragOKs_Type = Counter64
_BWagIpIfStatsOutFragOKs_Object = MibScalar
bWagIpIfStatsOutFragOKs = _BWagIpIfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 2),
    _BWagIpIfStatsOutFragOKs_Type()
)
bWagIpIfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpIfStatsOutFragOKs.setStatus("current")
_BWagIpSystemStatsReasmFails_Type = Counter64
_BWagIpSystemStatsReasmFails_Object = MibScalar
bWagIpSystemStatsReasmFails = _BWagIpSystemStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 3),
    _BWagIpSystemStatsReasmFails_Type()
)
bWagIpSystemStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpSystemStatsReasmFails.setStatus("current")
_BWagIpv6IfStatsReasmReqds_Type = Counter64
_BWagIpv6IfStatsReasmReqds_Object = MibScalar
bWagIpv6IfStatsReasmReqds = _BWagIpv6IfStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 4),
    _BWagIpv6IfStatsReasmReqds_Type()
)
bWagIpv6IfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpv6IfStatsReasmReqds.setStatus("current")
_BWagIpv6IfStatsOutFragOKs_Type = Counter64
_BWagIpv6IfStatsOutFragOKs_Object = MibScalar
bWagIpv6IfStatsOutFragOKs = _BWagIpv6IfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 5),
    _BWagIpv6IfStatsOutFragOKs_Type()
)
bWagIpv6IfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpv6IfStatsOutFragOKs.setStatus("current")
_BWagIpv6IfStatsReasmFails_Type = Counter64
_BWagIpv6IfStatsReasmFails_Object = MibScalar
bWagIpv6IfStatsReasmFails = _BWagIpv6IfStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 18, 6),
    _BWagIpv6IfStatsReasmFails_Type()
)
bWagIpv6IfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bWagIpv6IfStatsReasmFails.setStatus("current")

# Managed Objects groups


# Notification objects

bWagCgnatAuthIpAddrHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 1)
)
bWagCgnatAuthIpAddrHighThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagCgnatProfileIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatTotalPoolIPAddresses"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatAuthIpAddrUsedHighThreshold"))
)
if mibBuilder.loadTexts:
    bWagCgnatAuthIpAddrHighThresholdReached.setStatus(
        "current"
    )

bWagCgnatAuthIpAddrLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 2)
)
bWagCgnatAuthIpAddrLowThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagCgnatProfileIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatTotalPoolIPAddresses"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatAuthIpAddrUsedLowThreshold"))
)
if mibBuilder.loadTexts:
    bWagCgnatAuthIpAddrLowThresholdReached.setStatus(
        "current"
    )

bWagCgnatAuthIpAddressesExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 3)
)
bWagCgnatAuthIpAddressesExhausted.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagCgnatProfileIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatTotalPoolIPAddresses"))
)
if mibBuilder.loadTexts:
    bWagCgnatAuthIpAddressesExhausted.setStatus(
        "current"
    )

bWagCgnatPortBlocksUsedHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 4)
)
bWagCgnatPortBlocksUsedHighThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagCgnatSubscriberMac"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatTotalPortBlocksPerSubscriber"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatPortBlocksUsedHighThreshold"))
)
if mibBuilder.loadTexts:
    bWagCgnatPortBlocksUsedHighThresholdReached.setStatus(
        "obsolete"
    )

bWagCgnatPortBlocksUsedLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 5)
)
bWagCgnatPortBlocksUsedLowThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagCgnatSubscriberMac"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatTotalPortBlocksPerSubscriber"),
        ("BENU-WAG-STATS-MIB", "bWagCgnatPortBlocksUsedLowThreshold"))
)
if mibBuilder.loadTexts:
    bWagCgnatPortBlocksUsedLowThresholdReached.setStatus(
        "obsolete"
    )

bWagDhcpTPSHighReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 6)
)
bWagDhcpTPSHighReached.setObjects(
    ("BENU-WAG-STATS-MIB", "bWagDhcpTPS")
)
if mibBuilder.loadTexts:
    bWagDhcpTPSHighReached.setStatus(
        "current"
    )

bWagDhcpTPSLowReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 7)
)
bWagDhcpTPSLowReached.setObjects(
    ("BENU-WAG-STATS-MIB", "bWagDhcpTPS")
)
if mibBuilder.loadTexts:
    bWagDhcpTPSLowReached.setStatus(
        "current"
    )

bWagVrgApiIpAddrUsedHighThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 8)
)
bWagVrgApiIpAddrUsedHighThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagrgApiIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagVRGApiIPoolIPAddresses"),
        ("BENU-WAG-STATS-MIB", "bWagVrgApiIpAddrUsedHighThreshold"))
)
if mibBuilder.loadTexts:
    bWagVrgApiIpAddrUsedHighThresholdReached.setStatus(
        "current"
    )

bWagVrgApiIpAddrUsedLowThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 9)
)
bWagVrgApiIpAddrUsedLowThresholdReached.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagrgApiIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagVRGApiIPoolIPAddresses"),
        ("BENU-WAG-STATS-MIB", "bWagVrgApiIpAddrUsedLowThreshold"))
)
if mibBuilder.loadTexts:
    bWagVrgApiIpAddrUsedLowThresholdReached.setStatus(
        "current"
    )

bWagVrgApiIpAddressesExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 3, 0, 10)
)
bWagVrgApiIpAddressesExhausted.setObjects(
      *(("BENU-WAG-STATS-MIB", "bWagrgApiIPPoolGroup"),
        ("BENU-WAG-STATS-MIB", "bWagVRGApiIPoolIPAddresses"))
)
if mibBuilder.loadTexts:
    bWagVrgApiIpAddressesExhausted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-WAG-STATS-MIB",
    **{"benuWagStatsMIB": benuWagStatsMIB,
       "bWagStatsNotifications": bWagStatsNotifications,
       "bWagCgnatAuthIpAddrHighThresholdReached": bWagCgnatAuthIpAddrHighThresholdReached,
       "bWagCgnatAuthIpAddrLowThresholdReached": bWagCgnatAuthIpAddrLowThresholdReached,
       "bWagCgnatAuthIpAddressesExhausted": bWagCgnatAuthIpAddressesExhausted,
       "bWagCgnatPortBlocksUsedHighThresholdReached": bWagCgnatPortBlocksUsedHighThresholdReached,
       "bWagCgnatPortBlocksUsedLowThresholdReached": bWagCgnatPortBlocksUsedLowThresholdReached,
       "bWagDhcpTPSHighReached": bWagDhcpTPSHighReached,
       "bWagDhcpTPSLowReached": bWagDhcpTPSLowReached,
       "bWagVrgApiIpAddrUsedHighThresholdReached": bWagVrgApiIpAddrUsedHighThresholdReached,
       "bWagVrgApiIpAddrUsedLowThresholdReached": bWagVrgApiIpAddrUsedLowThresholdReached,
       "bWagVrgApiIpAddressesExhausted": bWagVrgApiIpAddressesExhausted,
       "bWagRadiusMIBObjects": bWagRadiusMIBObjects,
       "bWagRadiusTable": bWagRadiusTable,
       "bWagRadiusEntry": bWagRadiusEntry,
       "bWagRadiusStatsInterval": bWagRadiusStatsInterval,
       "bWagRadiusIntervalDuration": bWagRadiusIntervalDuration,
       "bWagRadiusAuthLatencyMin": bWagRadiusAuthLatencyMin,
       "bWagRadiusAuthLatencyMax": bWagRadiusAuthLatencyMax,
       "bWagRadiusAuthLatencyAvg": bWagRadiusAuthLatencyAvg,
       "bWagRadiusAuthLatencyLast": bWagRadiusAuthLatencyLast,
       "bWagRadiusAcctLatencyMin": bWagRadiusAcctLatencyMin,
       "bWagRadiusAcctLatencyMax": bWagRadiusAcctLatencyMax,
       "bWagRadiusAcctLatencyAvg": bWagRadiusAcctLatencyAvg,
       "bWagRadiusAcctLatencyLast": bWagRadiusAcctLatencyLast,
       "bWagRadiusAccessRequestSent": bWagRadiusAccessRequestSent,
       "bWagRadiusAccessAcceptReceived": bWagRadiusAccessAcceptReceived,
       "bWagRadiusAccessRejectReceived": bWagRadiusAccessRejectReceived,
       "bWagRadiusAcctRequestSent": bWagRadiusAcctRequestSent,
       "bWagRadiusAcctResponseReceived": bWagRadiusAcctResponseReceived,
       "bWagRadiusCoAAckSent": bWagRadiusCoAAckSent,
       "bWagRadiusCoANackSent": bWagRadiusCoANackSent,
       "bWagRadiusCoARequestReceived": bWagRadiusCoARequestReceived,
       "bWagRadiusCoALatencyMin": bWagRadiusCoALatencyMin,
       "bWagRadiusCoALatencyMax": bWagRadiusCoALatencyMax,
       "bWagRadiusCoALatencyAvg": bWagRadiusCoALatencyAvg,
       "bWagRadiusCoALatencyLast": bWagRadiusCoALatencyLast,
       "bWagRadiusDMLatencyMin": bWagRadiusDMLatencyMin,
       "bWagRadiusDMLatencyMax": bWagRadiusDMLatencyMax,
       "bWagRadiusDMLatencyAvg": bWagRadiusDMLatencyAvg,
       "bWagRadiusDMLatencyLast": bWagRadiusDMLatencyLast,
       "bWagRadiusDMAckSent": bWagRadiusDMAckSent,
       "bWagRadiusDMNackSent": bWagRadiusDMNackSent,
       "bWagRadiusDMRequestReceived": bWagRadiusDMRequestReceived,
       "bWagRadiusNotifObjects": bWagRadiusNotifObjects,
       "bWagDhcpMIBObjects": bWagDhcpMIBObjects,
       "bWagDhcpTable": bWagDhcpTable,
       "bWagDhcpEntry": bWagDhcpEntry,
       "bWagDhcpStatsInterval": bWagDhcpStatsInterval,
       "bWagDhcpIntervalDuration": bWagDhcpIntervalDuration,
       "bWagDhcpDiscoverAckIntervalMin": bWagDhcpDiscoverAckIntervalMin,
       "bWagDhcpDiscoverAckIntervalMax": bWagDhcpDiscoverAckIntervalMax,
       "bWagDhcpDiscoverAckIntervalAvg": bWagDhcpDiscoverAckIntervalAvg,
       "bWagDhcpDiscoverAckIntervalLast": bWagDhcpDiscoverAckIntervalLast,
       "bWagDhcpRequestAckLatencyMin": bWagDhcpRequestAckLatencyMin,
       "bWagDhcpRequestAckLatencyMax": bWagDhcpRequestAckLatencyMax,
       "bWagDhcpRequestAckLatencyAvg": bWagDhcpRequestAckLatencyAvg,
       "bWagDhcpRequestAckLatencyLast": bWagDhcpRequestAckLatencyLast,
       "bWagDhcpDiscoverOfferLatencyMin": bWagDhcpDiscoverOfferLatencyMin,
       "bWagDhcpDiscoverOfferLatencyMax": bWagDhcpDiscoverOfferLatencyMax,
       "bWagDhcpDiscoverOfferLatencyAvg": bWagDhcpDiscoverOfferLatencyAvg,
       "bWagDhcpDiscoverOfferLatencyLast": bWagDhcpDiscoverOfferLatencyLast,
       "bWagDhcpDiscoverReceived": bWagDhcpDiscoverReceived,
       "bWagDhcpOfferSent": bWagDhcpOfferSent,
       "bWagDhcpRequestReceived": bWagDhcpRequestReceived,
       "bWagDhcpAckSent": bWagDhcpAckSent,
       "bWagDhcpNackSent": bWagDhcpNackSent,
       "bWagDhcpOfferRequestIntervalMin": bWagDhcpOfferRequestIntervalMin,
       "bWagDhcpOfferRequestIntervalMax": bWagDhcpOfferRequestIntervalMax,
       "bWagDhcpOfferRequestIntervalAvg": bWagDhcpOfferRequestIntervalAvg,
       "bWagDhcpOfferRequestIntervalLast": bWagDhcpOfferRequestIntervalLast,
       "bWagDhcpTPSTable": bWagDhcpTPSTable,
       "bWagDhcpTPSEntry": bWagDhcpTPSEntry,
       "bWagDhcpTPSInterval": bWagDhcpTPSInterval,
       "bWagDhcpTPSIntervalDuration": bWagDhcpTPSIntervalDuration,
       "bWagDhcpTPSLow": bWagDhcpTPSLow,
       "bWagDhcpTPSHigh": bWagDhcpTPSHigh,
       "bWagDhcpTPS": bWagDhcpTPS,
       "bWagDhcpNotifObjects": bWagDhcpNotifObjects,
       "bWagSubscriberMIBObjects": bWagSubscriberMIBObjects,
       "bWagSubscriberTable": bWagSubscriberTable,
       "bWagSubscriberEntry": bWagSubscriberEntry,
       "bWagSubscriberStatsInterval": bWagSubscriberStatsInterval,
       "bWagSubscriberIntervalDuration": bWagSubscriberIntervalDuration,
       "bWagSubscriberActivationsCount": bWagSubscriberActivationsCount,
       "bWagSubscriberDeletionsCount": bWagSubscriberDeletionsCount,
       "bWagSubscriberAuthenticationsCount": bWagSubscriberAuthenticationsCount,
       "bWagSubscriberRedirectionsCount": bWagSubscriberRedirectionsCount,
       "bWagSubscriberRedirectionsByAcl": bWagSubscriberRedirectionsByAcl,
       "bWagSubscriberAPMobilityOccurencesCount": bWagSubscriberAPMobilityOccurencesCount,
       "bWagSubscriberDeletionsByDMCount": bWagSubscriberDeletionsByDMCount,
       "bWagSubscriberIdleTimeoutCount": bWagSubscriberIdleTimeoutCount,
       "bWagSubscriberSessionTimeoutPreauthCount": bWagSubscriberSessionTimeoutPreauthCount,
       "bWagSubscriberSessionTimeoutAuthviaportalCount": bWagSubscriberSessionTimeoutAuthviaportalCount,
       "bWagSubscriberDroppedByLicenseManagerCount": bWagSubscriberDroppedByLicenseManagerCount,
       "bWagSubscriberThrottlingOccurrencesCount": bWagSubscriberThrottlingOccurrencesCount,
       "bWagSubscriberThrottledCount": bWagSubscriberThrottledCount,
       "bWagSubscriberAbsoluteTimeoutCount": bWagSubscriberAbsoluteTimeoutCount,
       "bWagSubscriberAuthsViaPortalCount": bWagSubscriberAuthsViaPortalCount,
       "bWagSubscriberAuthenticationsCountVia8021x": bWagSubscriberAuthenticationsCountVia8021x,
       "bWagSubscriberAuthenticationsCountViaSingleStatic": bWagSubscriberAuthenticationsCountViaSingleStatic,
       "bWagSubscriberAuthenticationsCountViaRoutedSubnet": bWagSubscriberAuthenticationsCountViaRoutedSubnet,
       "bWagSubscriberSessionTimeoutAuthVia8021x": bWagSubscriberSessionTimeoutAuthVia8021x,
       "bWagSubscriberHomeTotalSubsDeleted": bWagSubscriberHomeTotalSubsDeleted,
       "bWagSubscriberHomeTransientSubsDeleted": bWagSubscriberHomeTransientSubsDeleted,
       "bWagSubscriberHomeUserStaticSubsDeleted": bWagSubscriberHomeUserStaticSubsDeleted,
       "bWagSubscriberHomeDhcpStaticSubsDeleted": bWagSubscriberHomeDhcpStaticSubsDeleted,
       "bWagSubscriberHomeDhcpDynSubsDeleted": bWagSubscriberHomeDhcpDynSubsDeleted,
       "bWagSubscriberHomePubStaticSubsDeleted": bWagSubscriberHomePubStaticSubsDeleted,
       "bWagSubscriberSpWifiActivationsCount": bWagSubscriberSpWifiActivationsCount,
       "bWagSubscriberHomeActivationsCount": bWagSubscriberHomeActivationsCount,
       "bWagSubscriberDsLiteActivationsCount": bWagSubscriberDsLiteActivationsCount,
       "bWagNumCurrentSubscribers": bWagNumCurrentSubscribers,
       "bWagNumAuthenticatedSubscribers": bWagNumAuthenticatedSubscribers,
       "bWagNumUnauthenticatedSubscribers": bWagNumUnauthenticatedSubscribers,
       "bWagNumSubsWithPrivateIPAddress": bWagNumSubsWithPrivateIPAddress,
       "bWagNumAuthSubsWithPublicIPAddress": bWagNumAuthSubsWithPublicIPAddress,
       "bWagNumUnAuthSubsWithPublicIPAddress": bWagNumUnAuthSubsWithPublicIPAddress,
       "bWagNumMigrantSubscribersCount": bWagNumMigrantSubscribersCount,
       "bWagNumRedirectedSubscribersCount": bWagNumRedirectedSubscribersCount,
       "bWagPolicyTable": bWagPolicyTable,
       "bWagPolicyEntry": bWagPolicyEntry,
       "bWagPolicyType": bWagPolicyType,
       "bWagPolicyIndex": bWagPolicyIndex,
       "bWagPolicyName": bWagPolicyName,
       "bWagNumOfSubscribersWithPolicy": bWagNumOfSubscribersWithPolicy,
       "bWagNumOfAuthSubscribersWithPolicy": bWagNumOfAuthSubscribersWithPolicy,
       "bWagNumOfUnAuthSubscribersWithPolicy": bWagNumOfUnAuthSubscribersWithPolicy,
       "bWagNumSubsAuthenticatedWithIPv6Prefix": bWagNumSubsAuthenticatedWithIPv6Prefix,
       "bWagNumCurrent8021xSubscribers": bWagNumCurrent8021xSubscribers,
       "bWagNumPreAuthenticatedSubscribers": bWagNumPreAuthenticatedSubscribers,
       "bWagNumCurrentSingleStaticSubscribers": bWagNumCurrentSingleStaticSubscribers,
       "bWagNumCurrentRoutedSubnetSubscribers": bWagNumCurrentRoutedSubnetSubscribers,
       "bWagNumSubsUnauthenticatedWithIPv6Prefix": bWagNumSubsUnauthenticatedWithIPv6Prefix,
       "bWagNumSubsViaStaticAuthPolicy": bWagNumSubsViaStaticAuthPolicy,
       "bWagNumCurrentHomeSubscribers": bWagNumCurrentHomeSubscribers,
       "bWagNumCurrentSPWiFiSubscribers": bWagNumCurrentSPWiFiSubscribers,
       "bWagNumCurrentHomeTransientSubs": bWagNumCurrentHomeTransientSubs,
       "bWagNumCurrentHomeUserStatSubs": bWagNumCurrentHomeUserStatSubs,
       "bWagNumCurrentHomeDhcpStatSubs": bWagNumCurrentHomeDhcpStatSubs,
       "bWagNumCurrentHomeDhcpDynSubs": bWagNumCurrentHomeDhcpDynSubs,
       "bWagNumCurrentHomePubStatSubs": bWagNumCurrentHomePubStatSubs,
       "bWagNumPreAuthSpwifiSubscribers": bWagNumPreAuthSpwifiSubscribers,
       "bWagNumPreAuthHomeSubscribers": bWagNumPreAuthHomeSubscribers,
       "bWagNumPreAuthenticatedSubscribersS2aPmip6": bWagNumPreAuthenticatedSubscribersS2aPmip6,
       "bWagNumCurrentSSIDS2aSubscribersPmip6": bWagNumCurrentSSIDS2aSubscribersPmip6,
       "bWagNumCurrentDSLiteSubscribers": bWagNumCurrentDSLiteSubscribers,
       "bWagSubscriberNotifObjects": bWagSubscriberNotifObjects,
       "bWagTunnelStatsMIBObjects": bWagTunnelStatsMIBObjects,
       "bWagTunnelTable": bWagTunnelTable,
       "bWagTunnelEntry": bWagTunnelEntry,
       "bWagTunnelStatsInterval": bWagTunnelStatsInterval,
       "bWagTunnelIntervalDuration": bWagTunnelIntervalDuration,
       "bWagTunnelPktsRxdGRE": bWagTunnelPktsRxdGRE,
       "bWagTunnelPktsRxdGREPayloadTEB": bWagTunnelPktsRxdGREPayloadTEB,
       "bWagTunnelPktsRxdGREPayloadMPLS": bWagTunnelPktsRxdGREPayloadMPLS,
       "bWagTunnelPktsEncapsulatedGRE": bWagTunnelPktsEncapsulatedGRE,
       "bWagTunnelPktsDecapsulatedGRE": bWagTunnelPktsDecapsulatedGRE,
       "bWagTunnelPktsRxdARP": bWagTunnelPktsRxdARP,
       "bWagTunnelPktsRxdDHCP": bWagTunnelPktsRxdDHCP,
       "bWagTunnelPktsRxdDNS": bWagTunnelPktsRxdDNS,
       "bWagTunnelPktsRxdHTTP": bWagTunnelPktsRxdHTTP,
       "bWagTunnelPktsRxdHTTPGetReq": bWagTunnelPktsRxdHTTPGetReq,
       "bWagTunnelPktsTxdHTTP": bWagTunnelPktsTxdHTTP,
       "bWagTunnelPktsTxdHTTPRedir": bWagTunnelPktsTxdHTTPRedir,
       "bWagTunnelPktsRxdHTTPS": bWagTunnelPktsRxdHTTPS,
       "bWagTunnelPktsRxdTCPSyn": bWagTunnelPktsRxdTCPSyn,
       "bWagTunnelPktsTxdTCPSynAck": bWagTunnelPktsTxdTCPSynAck,
       "bWagTunnelPktsTxdTCPFin": bWagTunnelPktsTxdTCPFin,
       "bWagTunnelPktsRxdTCPFinAck": bWagTunnelPktsRxdTCPFinAck,
       "bWagTunnelPktsTxdTCPAck2Fin": bWagTunnelPktsTxdTCPAck2Fin,
       "bWagTunnelCreatedDynamically": bWagTunnelCreatedDynamically,
       "bWagTunnelCreatedStatically": bWagTunnelCreatedStatically,
       "bWagTunnelDeleted": bWagTunnelDeleted,
       "bWagTunnelDeletedDueToInactivity": bWagTunnelDeletedDueToInactivity,
       "bWagTunnelDeletedByCommand": bWagTunnelDeletedByCommand,
       "bWagTunnelMaxSupported": bWagTunnelMaxSupported,
       "bWagTunnelMaxCountReached": bWagTunnelMaxCountReached,
       "bWagTunnelTunnelsLookupFound": bWagTunnelTunnelsLookupFound,
       "bWagTunnelTunnelsLookupNotFound": bWagTunnelTunnelsLookupNotFound,
       "bWagTunnelCountHighThreshold": bWagTunnelCountHighThreshold,
       "bWagTunnelCountLowThreshold": bWagTunnelCountLowThreshold,
       "bWagTunnelDeletedDueToReject": bWagTunnelDeletedDueToReject,
       "bWagTunnelDeletedDueToAbort": bWagTunnelDeletedDueToAbort,
       "bWagTunnelDeletedDueToMacResFail": bWagTunnelDeletedDueToMacResFail,
       "bWagTunnelDeletedDueToLifDown": bWagTunnelDeletedDueToLifDown,
       "bWagTunnelDeletedDueToB2bSubsDelete": bWagTunnelDeletedDueToB2bSubsDelete,
       "bWagL2tpv3TunnelPktsRxd": bWagL2tpv3TunnelPktsRxd,
       "bWagL2tpv3TunnelPktsEncapsulated": bWagL2tpv3TunnelPktsEncapsulated,
       "bWagL2tpv3TunnelPktsDecapsulated": bWagL2tpv3TunnelPktsDecapsulated,
       "bWagL2tpv3TunnelPktsRxdARP": bWagL2tpv3TunnelPktsRxdARP,
       "bWagL2tpv3TunnelPktsRxdDHCP": bWagL2tpv3TunnelPktsRxdDHCP,
       "bWagL2tpv3TunnelPktsRxdDNS": bWagL2tpv3TunnelPktsRxdDNS,
       "bWagL2tpv3TunnelCreatedDynamically": bWagL2tpv3TunnelCreatedDynamically,
       "bWagL2tpv3TunnelDeleted": bWagL2tpv3TunnelDeleted,
       "bWagL2tpv3TunnelDeletedDueToInactivity": bWagL2tpv3TunnelDeletedDueToInactivity,
       "bWagL2tpv3TunnelDeletedByCommand": bWagL2tpv3TunnelDeletedByCommand,
       "bWagL2tpv3TunnelDeletedDueToLifDown": bWagL2tpv3TunnelDeletedDueToLifDown,
       "bWagNumCurrentTunnels": bWagNumCurrentTunnels,
       "bWagNumTunnelsCreatedDynamically": bWagNumTunnelsCreatedDynamically,
       "bWagNumTunnelsCreatedStatically": bWagNumTunnelsCreatedStatically,
       "bWagNumTunnelsDeleted": bWagNumTunnelsDeleted,
       "bWagNumTunnelsInactiveDeleted": bWagNumTunnelsInactiveDeleted,
       "bWagNumTunnelsDeletedByCommand": bWagNumTunnelsDeletedByCommand,
       "bWagNumTunnelsSubsAssociated": bWagNumTunnelsSubsAssociated,
       "bWagNumTunnelsSchedDeletion": bWagNumTunnelsSchedDeletion,
       "bWagNumCurrentTunnelsIPv4": bWagNumCurrentTunnelsIPv4,
       "bWagNumCurrentTunnelsIPv6": bWagNumCurrentTunnelsIPv6,
       "bWagNumTunnelsDeletedByB2B": bWagNumTunnelsDeletedByB2B,
       "bWagNumTunnelsDeletedDuetoLIFDown": bWagNumTunnelsDeletedDuetoLIFDown,
       "bWagNumCurrentTunnelsSpWiFi": bWagNumCurrentTunnelsSpWiFi,
       "bWagNumCurrentTunnelsHome": bWagNumCurrentTunnelsHome,
       "bWagNumCurrTunnHomeAndSpWiFi": bWagNumCurrTunnHomeAndSpWiFi,
       "bWagNumCurrentTunnHomeInactive": bWagNumCurrentTunnHomeInactive,
       "bWagNumCurrentTunnHomeAccept": bWagNumCurrentTunnHomeAccept,
       "bWagNumL2tpv3TunnelsCreatedDynamically": bWagNumL2tpv3TunnelsCreatedDynamically,
       "bWagNumL2tpv3TunnelsDeleted": bWagNumL2tpv3TunnelsDeleted,
       "bWagNumL2tpv3TunnelsInactiveDeleted": bWagNumL2tpv3TunnelsInactiveDeleted,
       "bWagNumL2tpv3TunnelsDeletedByCommand": bWagNumL2tpv3TunnelsDeletedByCommand,
       "bWagNumL2tpv3TunnelsSubsAssociated": bWagNumL2tpv3TunnelsSubsAssociated,
       "bWagNumCurrentL2tpv3TunnelsIPv4": bWagNumCurrentL2tpv3TunnelsIPv4,
       "bWagNumL2tpv3TunnelsDeletedDuetoLIFDown": bWagNumL2tpv3TunnelsDeletedDuetoLIFDown,
       "bWagNumCurrentL2tpv3TunnelsSpWiFi": bWagNumCurrentL2tpv3TunnelsSpWiFi,
       "bWagNumCurrentTunnelsDSLite": bWagNumCurrentTunnelsDSLite,
       "bWagTunnelNotifObjects": bWagTunnelNotifObjects,
       "bWagCgnatMIBObjects": bWagCgnatMIBObjects,
       "bWagCgnatProfileStatsTable": bWagCgnatProfileStatsTable,
       "bWagCgnatProfileStatsEntry": bWagCgnatProfileStatsEntry,
       "bWagCgnatProfileStatsIndex": bWagCgnatProfileStatsIndex,
       "bWagCgnatProfileName": bWagCgnatProfileName,
       "bWagCgnatProfileType": bWagCgnatProfileType,
       "bWagCgnatProfileNATIPPoolGroup": bWagCgnatProfileNATIPPoolGroup,
       "bWagCgnatProfileSubscribers": bWagCgnatProfileSubscribers,
       "bWagCgnatProfileMaxIPAddresses": bWagCgnatProfileMaxIPAddresses,
       "bWagCgnatProfileUsedIPAddresses": bWagCgnatProfileUsedIPAddresses,
       "bWagCgnatProfileReservedIPAddresses": bWagCgnatProfileReservedIPAddresses,
       "bWagCgnatProfileTotalPortBlocks": bWagCgnatProfileTotalPortBlocks,
       "bWagCgnatProfilePortBlocksUsed": bWagCgnatProfilePortBlocksUsed,
       "bWagCgnatProfilePortBlocksReused": bWagCgnatProfilePortBlocksReused,
       "bWagCgnatProfileTotalPoolIPAddresses": bWagCgnatProfileTotalPoolIPAddresses,
       "bWagCgnatIPStatsTable": bWagCgnatIPStatsTable,
       "bWagCgnatIPStatsEntry": bWagCgnatIPStatsEntry,
       "bWagCgnatIPStatsIndex": bWagCgnatIPStatsIndex,
       "bWagCgnatPublicIPAddressType": bWagCgnatPublicIPAddressType,
       "bWagCgnatPublicIPAddress": bWagCgnatPublicIPAddress,
       "bWagCgnatIPPortBlocksUsed": bWagCgnatIPPortBlocksUsed,
       "bWagCgnatIPPortBlocksFree": bWagCgnatIPPortBlocksFree,
       "bWagCgnatIPPortBlocksReused": bWagCgnatIPPortBlocksReused,
       "bWagCgnatIPSubActiveCount": bWagCgnatIPSubActiveCount,
       "bWagCgnatIPPacketsDropped": bWagCgnatIPPacketsDropped,
       "bWagCgnatPeriodIpTable": bWagCgnatPeriodIpTable,
       "bWagCgnatPeriodIpEntry": bWagCgnatPeriodIpEntry,
       "bWagCgnatPeriodIpInterval": bWagCgnatPeriodIpInterval,
       "bWagCgnatPeriodIpIndex": bWagCgnatPeriodIpIndex,
       "bWagCgnatIPAddressType": bWagCgnatIPAddressType,
       "bWagCgnatIPAddress": bWagCgnatIPAddress,
       "bWagCgnatPacketsDropped": bWagCgnatPacketsDropped,
       "bWagCgnatPortBlockMaxUtil": bWagCgnatPortBlockMaxUtil,
       "bWagCgnatPortBlockMinUtil": bWagCgnatPortBlockMinUtil,
       "bWagCgnatIntervalDuration": bWagCgnatIntervalDuration,
       "bWagCgnatUnauthIPStatsTable": bWagCgnatUnauthIPStatsTable,
       "bWagCgnatUnauthIPStatsEntry": bWagCgnatUnauthIPStatsEntry,
       "bWagCgnatUnauthIPStatsIndex": bWagCgnatUnauthIPStatsIndex,
       "bWagCgnatUnauthPublicIPAddressType": bWagCgnatUnauthPublicIPAddressType,
       "bWagCgnatUnauthPublicIPAddress": bWagCgnatUnauthPublicIPAddress,
       "bWagCgnatUnauthIPPortBlocksUsed": bWagCgnatUnauthIPPortBlocksUsed,
       "bWagCgnatUnauthIPPortBlocksFree": bWagCgnatUnauthIPPortBlocksFree,
       "bWagCgnatUnauthIPPortBlocksReused": bWagCgnatUnauthIPPortBlocksReused,
       "bWagCgnatUnauthIPSubActiveCount": bWagCgnatUnauthIPSubActiveCount,
       "bWagCgnatUnauthPeriodIpTable": bWagCgnatUnauthPeriodIpTable,
       "bWagCgnatUnauthPeriodIpEntry": bWagCgnatUnauthPeriodIpEntry,
       "bWagCgnatUnauthPeriodIpInterval": bWagCgnatUnauthPeriodIpInterval,
       "bWagCgnatUnauthPeriodIpIndex": bWagCgnatUnauthPeriodIpIndex,
       "bWagCgnatUnauthIPAddressType": bWagCgnatUnauthIPAddressType,
       "bWagCgnatUnauthIPAddress": bWagCgnatUnauthIPAddress,
       "bWagCgnatUnauthPortBlockMaxUtil": bWagCgnatUnauthPortBlockMaxUtil,
       "bWagCgnatUnauthPortBlockMinUtil": bWagCgnatUnauthPortBlockMinUtil,
       "bWagCgnatUnauthIntervalDuration": bWagCgnatUnauthIntervalDuration,
       "bWagCgnatAuthPortUtilTable": bWagCgnatAuthPortUtilTable,
       "bWagCgnatAuthPortUtilEntry": bWagCgnatAuthPortUtilEntry,
       "bWagCgnatAuthSubscriberMac": bWagCgnatAuthSubscriberMac,
       "bWagCgnatAuthSubscriberPortsUtil": bWagCgnatAuthSubscriberPortsUtil,
       "bWagCgnatAuthPortRisingThresholdCrossedSubCount": bWagCgnatAuthPortRisingThresholdCrossedSubCount,
       "bWagCgnatPoolGroupStatsTable": bWagCgnatPoolGroupStatsTable,
       "bWagCgnatPoolGroupStatsEntry": bWagCgnatPoolGroupStatsEntry,
       "bWagCgnatPoolGroupType": bWagCgnatPoolGroupType,
       "bWagCgnatPoolGroupIndex": bWagCgnatPoolGroupIndex,
       "bWagCgnatPoolGroupName": bWagCgnatPoolGroupName,
       "bWagCgnatPoolGroupSubscribers": bWagCgnatPoolGroupSubscribers,
       "bWagCgnatPoolGroupUsedIPAddresses": bWagCgnatPoolGroupUsedIPAddresses,
       "bWagCgnatPoolGroupReservedIPAddresses": bWagCgnatPoolGroupReservedIPAddresses,
       "bWagCgnatPoolGroupTotalIPAddresses": bWagCgnatPoolGroupTotalIPAddresses,
       "bWagCgnatNotifObjects": bWagCgnatNotifObjects,
       "bWagCgnatProfileIPPoolGroup": bWagCgnatProfileIPPoolGroup,
       "bWagCgnatTotalPoolIPAddresses": bWagCgnatTotalPoolIPAddresses,
       "bWagCgnatAuthIpAddrUsedHighThreshold": bWagCgnatAuthIpAddrUsedHighThreshold,
       "bWagCgnatAuthIpAddrUsedLowThreshold": bWagCgnatAuthIpAddrUsedLowThreshold,
       "bWagCgnatSubscriberMac": bWagCgnatSubscriberMac,
       "bWagCgnatTotalPortBlocksPerSubscriber": bWagCgnatTotalPortBlocksPerSubscriber,
       "bWagCgnatPortBlocksUsedHighThreshold": bWagCgnatPortBlocksUsedHighThreshold,
       "bWagCgnatPortBlocksUsedLowThreshold": bWagCgnatPortBlocksUsedLowThreshold,
       "bWagProcessingLatencyMIBObjects": bWagProcessingLatencyMIBObjects,
       "bWagUpstreamProcessingLatencyPktCount": bWagUpstreamProcessingLatencyPktCount,
       "bWagUpstreamProcessingLatencyMax": bWagUpstreamProcessingLatencyMax,
       "bWagUpstreamProcessingLatencyMin": bWagUpstreamProcessingLatencyMin,
       "bWagUpstreamProcessingLatencyAvg": bWagUpstreamProcessingLatencyAvg,
       "bWagDownstreamProcessingLatencyPktCount": bWagDownstreamProcessingLatencyPktCount,
       "bWagDownstreamProcessingLatencyMax": bWagDownstreamProcessingLatencyMax,
       "bWagDownstreamProcessingLatencyMin": bWagDownstreamProcessingLatencyMin,
       "bWagDownstreamProcessingLatencyAvg": bWagDownstreamProcessingLatencyAvg,
       "bWagProcessingLatencyNotifObjects": bWagProcessingLatencyNotifObjects,
       "bWagDhcpv6MIBObjects": bWagDhcpv6MIBObjects,
       "bWagDHCPv6Table": bWagDHCPv6Table,
       "bWagDHCPv6Entry": bWagDHCPv6Entry,
       "bWagDHCPv6StatsInterval": bWagDHCPv6StatsInterval,
       "bWagDHCPv6IntervalDuration": bWagDHCPv6IntervalDuration,
       "bWagDHCPv6SolicitReplyIntervalMin": bWagDHCPv6SolicitReplyIntervalMin,
       "bWagDHCPv6SolicitReplyIntervalMax": bWagDHCPv6SolicitReplyIntervalMax,
       "bWagDHCPv6SolicitReplyIntervalAvg": bWagDHCPv6SolicitReplyIntervalAvg,
       "bWagDHCPv6SolicitReplyIntervalLast": bWagDHCPv6SolicitReplyIntervalLast,
       "bWagDHCPv6RequestReplyLatencyMin": bWagDHCPv6RequestReplyLatencyMin,
       "bWagDHCPv6RequestReplyLatencyMax": bWagDHCPv6RequestReplyLatencyMax,
       "bWagDHCPv6RequestReplyLatencyAvg": bWagDHCPv6RequestReplyLatencyAvg,
       "bWagDHCPv6RequestReplyLatencyLast": bWagDHCPv6RequestReplyLatencyLast,
       "bWagDHCPv6SolicitAdvLatencyMin": bWagDHCPv6SolicitAdvLatencyMin,
       "bWagDHCPv6SolicitAdvLatencyMax": bWagDHCPv6SolicitAdvLatencyMax,
       "bWagDHCPv6SolicitAdvLatencyAvg": bWagDHCPv6SolicitAdvLatencyAvg,
       "bWagDHCPv6SolicitAdvLatencyLast": bWagDHCPv6SolicitAdvLatencyLast,
       "bWagDHCPv6AdvRequestIntervalMin": bWagDHCPv6AdvRequestIntervalMin,
       "bWagDHCPv6AdvRequestIntervalMax": bWagDHCPv6AdvRequestIntervalMax,
       "bWagDHCPv6AdvRequestIntervalAvg": bWagDHCPv6AdvRequestIntervalAvg,
       "bWagDHCPv6AdvRequestIntervalLast": bWagDHCPv6AdvRequestIntervalLast,
       "bWagDHCPv6SolicitReceived": bWagDHCPv6SolicitReceived,
       "bWagDHCPv6AdvertisementSent": bWagDHCPv6AdvertisementSent,
       "bWagDHCPv6RequestReceived": bWagDHCPv6RequestReceived,
       "bWagDHCPv6ReplySent": bWagDHCPv6ReplySent,
       "bWagMHNMIBObjects": bWagMHNMIBObjects,
       "bWagMHNProfileStatsTable": bWagMHNProfileStatsTable,
       "bWagMHNProfileStatsEntry": bWagMHNProfileStatsEntry,
       "bWagMHNProfileStatsIndex": bWagMHNProfileStatsIndex,
       "bWagMHNProfileName": bWagMHNProfileName,
       "bWagMHNProfileNATIPPoolGroup": bWagMHNProfileNATIPPoolGroup,
       "bWagMHNProfileMaxSubscribers": bWagMHNProfileMaxSubscribers,
       "bWagMHNProfileMaxIPAddresses": bWagMHNProfileMaxIPAddresses,
       "bWagMHNProfileUsedIPAddresses": bWagMHNProfileUsedIPAddresses,
       "bWagMHNProfileTotalPortBlocks": bWagMHNProfileTotalPortBlocks,
       "bWagMHNProfileTotalPoolIPAddresses": bWagMHNProfileTotalPoolIPAddresses,
       "bWagVrgApiNotifObjects": bWagVrgApiNotifObjects,
       "bWagVrgApiIpAddrUsedHighThreshold": bWagVrgApiIpAddrUsedHighThreshold,
       "bWagVrgApiIpAddrUsedLowThreshold": bWagVrgApiIpAddrUsedLowThreshold,
       "bWagrgApiIPPoolGroup": bWagrgApiIPPoolGroup,
       "bWagVRGApiIPoolIPAddresses": bWagVRGApiIPoolIPAddresses,
       "bWagDsLiteMIBObjects": bWagDsLiteMIBObjects,
       "bWagDsLiteProfileStatsTable": bWagDsLiteProfileStatsTable,
       "bWagDsLiteProfileStatsEntry": bWagDsLiteProfileStatsEntry,
       "bWagDsLiteProfileStatsIndex": bWagDsLiteProfileStatsIndex,
       "bWagDsLiteProfileName": bWagDsLiteProfileName,
       "bWagDsLiteProfileType": bWagDsLiteProfileType,
       "bWagDsLiteProfileNATIPPoolGroup": bWagDsLiteProfileNATIPPoolGroup,
       "bWagDsLiteProfileMaxIPAddresses": bWagDsLiteProfileMaxIPAddresses,
       "bWagDsLiteProfileUsedIPAddresses": bWagDsLiteProfileUsedIPAddresses,
       "bWagDsLiteProfileReservedIPAddresses": bWagDsLiteProfileReservedIPAddresses,
       "bWagDsLiteProfileTotalPoolIPAddresses": bWagDsLiteProfileTotalPoolIPAddresses,
       "bWagDsLiteProfileMaxSubscribers": bWagDsLiteProfileMaxSubscribers,
       "bWagDsLiteProfileMaxTunnels": bWagDsLiteProfileMaxTunnels,
       "bDSLitePortBlocksTotal": bDSLitePortBlocksTotal,
       "bDSLitePortBlocksInUse": bDSLitePortBlocksInUse,
       "bDSLiteTunnelsUsingOnePortBlock": bDSLiteTunnelsUsingOnePortBlock,
       "bDSLiteTunnelsUsingTwoPortBlocks": bDSLiteTunnelsUsingTwoPortBlocks,
       "bDSLiteTunnelsUsingThreePortBlocks": bDSLiteTunnelsUsingThreePortBlocks,
       "bDSLiteTunnelsUsingFourPortBlocks": bDSLiteTunnelsUsingFourPortBlocks,
       "bDSLiteTunnelsUsingFivePortBlocks": bDSLiteTunnelsUsingFivePortBlocks,
       "bWagDsLiteNotifObjects": bWagDsLiteNotifObjects,
       "bWagIpSystemStatsMIBObjects": bWagIpSystemStatsMIBObjects,
       "bWagIpSystemStatsReasmReqds": bWagIpSystemStatsReasmReqds,
       "bWagIpIfStatsOutFragOKs": bWagIpIfStatsOutFragOKs,
       "bWagIpSystemStatsReasmFails": bWagIpSystemStatsReasmFails,
       "bWagIpv6IfStatsReasmReqds": bWagIpv6IfStatsReasmReqds,
       "bWagIpv6IfStatsOutFragOKs": bWagIpv6IfStatsOutFragOKs,
       "bWagIpv6IfStatsReasmFails": bWagIpv6IfStatsReasmFails}
)
