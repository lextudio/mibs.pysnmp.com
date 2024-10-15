# SNMP MIB module (BENU-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:59 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

benuRadiusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4)
)
benuRadiusMIB.setRevisions(
        ("2016-07-28 00:00",
         "2016-03-17 00:00",
         "2015-06-24 00:00",
         "2015-05-21 00:00",
         "2015-05-20 00:00",
         "2015-03-16 00:00",
         "2015-03-02 00:00",
         "2015-02-24 00:00",
         "2015-01-26 00:00",
         "2015-01-02 00:00",
         "2014-12-02 00:00",
         "2014-07-17 00:00",
         "2014-05-19 00:00",
         "2013-04-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BenuRadiusInstance(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("radiusInstance0", 1)
    )



# MIB Managed Objects in the order of their OIDs

_BRadiusNotifications_ObjectIdentity = ObjectIdentity
bRadiusNotifications = _BRadiusNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0)
)
if mibBuilder.loadTexts:
    bRadiusNotifications.setStatus("current")
_BRadiusMIBObjects_ObjectIdentity = ObjectIdentity
bRadiusMIBObjects = _BRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bRadiusMIBObjects.setStatus("current")
_BRadiusServerAuthTable_Object = MibTable
bRadiusServerAuthTable = _BRadiusServerAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    bRadiusServerAuthTable.setStatus("current")
_BRadiusServerAuthEntry_Object = MibTableRow
bRadiusServerAuthEntry = _BRadiusServerAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1)
)
bRadiusServerAuthEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusAuthStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    bRadiusServerAuthEntry.setStatus("current")
_BRadiusAuthStatsInterval_Type = Integer32
_BRadiusAuthStatsInterval_Object = MibTableColumn
bRadiusAuthStatsInterval = _BRadiusAuthStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 1),
    _BRadiusAuthStatsInterval_Type()
)
bRadiusAuthStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAuthStatsInterval.setStatus("current")
_BRadiusAuthServerIndex_Type = Integer32
_BRadiusAuthServerIndex_Object = MibTableColumn
bRadiusAuthServerIndex = _BRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 2),
    _BRadiusAuthServerIndex_Type()
)
bRadiusAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAuthServerIndex.setStatus("current")
_BRadiusAuthServerInetAddressType_Type = InetAddressType
_BRadiusAuthServerInetAddressType_Object = MibTableColumn
bRadiusAuthServerInetAddressType = _BRadiusAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 3),
    _BRadiusAuthServerInetAddressType_Type()
)
bRadiusAuthServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthServerInetAddressType.setStatus("current")
_BRadiusAuthServerInetAddress_Type = InetAddress
_BRadiusAuthServerInetAddress_Object = MibTableColumn
bRadiusAuthServerInetAddress = _BRadiusAuthServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 4),
    _BRadiusAuthServerInetAddress_Type()
)
bRadiusAuthServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthServerInetAddress.setStatus("current")
_BRadiusAuthIntervalDuration_Type = Integer32
_BRadiusAuthIntervalDuration_Object = MibTableColumn
bRadiusAuthIntervalDuration = _BRadiusAuthIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 5),
    _BRadiusAuthIntervalDuration_Type()
)
bRadiusAuthIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthIntervalDuration.setStatus("current")
_BRadiusAccessRequestSent_Type = Unsigned32
_BRadiusAccessRequestSent_Object = MibTableColumn
bRadiusAccessRequestSent = _BRadiusAccessRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 6),
    _BRadiusAccessRequestSent_Type()
)
bRadiusAccessRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRequestSent.setStatus("current")
_BRadiusAccessAcceptReceived_Type = Unsigned32
_BRadiusAccessAcceptReceived_Object = MibTableColumn
bRadiusAccessAcceptReceived = _BRadiusAccessAcceptReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 7),
    _BRadiusAccessAcceptReceived_Type()
)
bRadiusAccessAcceptReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessAcceptReceived.setStatus("current")
_BRadiusAccessRejectReceived_Type = Unsigned32
_BRadiusAccessRejectReceived_Object = MibTableColumn
bRadiusAccessRejectReceived = _BRadiusAccessRejectReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 8),
    _BRadiusAccessRejectReceived_Type()
)
bRadiusAccessRejectReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRejectReceived.setStatus("current")
_BRadiusAccessChallengeReceived_Type = Unsigned32
_BRadiusAccessChallengeReceived_Object = MibTableColumn
bRadiusAccessChallengeReceived = _BRadiusAccessChallengeReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 9),
    _BRadiusAccessChallengeReceived_Type()
)
bRadiusAccessChallengeReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessChallengeReceived.setStatus("current")
_BRadiusAccessRequestResent_Type = Unsigned32
_BRadiusAccessRequestResent_Object = MibTableColumn
bRadiusAccessRequestResent = _BRadiusAccessRequestResent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 10),
    _BRadiusAccessRequestResent_Type()
)
bRadiusAccessRequestResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRequestResent.setStatus("current")
_BRadiusAccessRequestDropped_Type = Unsigned32
_BRadiusAccessRequestDropped_Object = MibTableColumn
bRadiusAccessRequestDropped = _BRadiusAccessRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 11),
    _BRadiusAccessRequestDropped_Type()
)
bRadiusAccessRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRequestDropped.setStatus("current")
_BRadiusAccessRequestTimedOut_Type = Unsigned32
_BRadiusAccessRequestTimedOut_Object = MibTableColumn
bRadiusAccessRequestTimedOut = _BRadiusAccessRequestTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 12),
    _BRadiusAccessRequestTimedOut_Type()
)
bRadiusAccessRequestTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRequestTimedOut.setStatus("current")
_BRadiusAccessRequestSentFail_Type = Unsigned32
_BRadiusAccessRequestSentFail_Object = MibTableColumn
bRadiusAccessRequestSentFail = _BRadiusAccessRequestSentFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 13),
    _BRadiusAccessRequestSentFail_Type()
)
bRadiusAccessRequestSentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessRequestSentFail.setStatus("current")
_BRadiusAccessPeakRequestPending_Type = Unsigned32
_BRadiusAccessPeakRequestPending_Object = MibTableColumn
bRadiusAccessPeakRequestPending = _BRadiusAccessPeakRequestPending_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 14),
    _BRadiusAccessPeakRequestPending_Type()
)
bRadiusAccessPeakRequestPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessPeakRequestPending.setStatus("current")
_BRadiusAccessMalformedRespDropped_Type = Unsigned32
_BRadiusAccessMalformedRespDropped_Object = MibTableColumn
bRadiusAccessMalformedRespDropped = _BRadiusAccessMalformedRespDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 15),
    _BRadiusAccessMalformedRespDropped_Type()
)
bRadiusAccessMalformedRespDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessMalformedRespDropped.setStatus("current")
_BRadiusAccessBadAuthenticatorRcvd_Type = Unsigned32
_BRadiusAccessBadAuthenticatorRcvd_Object = MibTableColumn
bRadiusAccessBadAuthenticatorRcvd = _BRadiusAccessBadAuthenticatorRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 16),
    _BRadiusAccessBadAuthenticatorRcvd_Type()
)
bRadiusAccessBadAuthenticatorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessBadAuthenticatorRcvd.setStatus("current")
_BRadiusAccessServerMarkedDead_Type = Unsigned32
_BRadiusAccessServerMarkedDead_Object = MibTableColumn
bRadiusAccessServerMarkedDead = _BRadiusAccessServerMarkedDead_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 17),
    _BRadiusAccessServerMarkedDead_Type()
)
bRadiusAccessServerMarkedDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAccessServerMarkedDead.setStatus("current")
_BRadiusAuthLatencyMin_Type = Unsigned32
_BRadiusAuthLatencyMin_Object = MibTableColumn
bRadiusAuthLatencyMin = _BRadiusAuthLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 18),
    _BRadiusAuthLatencyMin_Type()
)
bRadiusAuthLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyMin.setStatus("current")
_BRadiusAuthLatencyMax_Type = Unsigned32
_BRadiusAuthLatencyMax_Object = MibTableColumn
bRadiusAuthLatencyMax = _BRadiusAuthLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 19),
    _BRadiusAuthLatencyMax_Type()
)
bRadiusAuthLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyMax.setStatus("current")
_BRadiusAuthLatencyAvg_Type = Unsigned32
_BRadiusAuthLatencyAvg_Object = MibTableColumn
bRadiusAuthLatencyAvg = _BRadiusAuthLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 20),
    _BRadiusAuthLatencyAvg_Type()
)
bRadiusAuthLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyAvg.setStatus("current")
_BRadiusAuthLatencyLast_Type = Unsigned32
_BRadiusAuthLatencyLast_Object = MibTableColumn
bRadiusAuthLatencyLast = _BRadiusAuthLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 21),
    _BRadiusAuthLatencyLast_Type()
)
bRadiusAuthLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyLast.setStatus("current")
_BRadiusAuthAAAGroupName_Type = DisplayString
_BRadiusAuthAAAGroupName_Object = MibTableColumn
bRadiusAuthAAAGroupName = _BRadiusAuthAAAGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 1, 1, 22),
    _BRadiusAuthAAAGroupName_Type()
)
bRadiusAuthAAAGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthAAAGroupName.setStatus("current")
_BRadiusServerAcctTable_Object = MibTable
bRadiusServerAcctTable = _BRadiusServerAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    bRadiusServerAcctTable.setStatus("current")
_BRadiusServerAcctEntry_Object = MibTableRow
bRadiusServerAcctEntry = _BRadiusServerAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1)
)
bRadiusServerAcctEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusAcctStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusAcctServerIndex"),
)
if mibBuilder.loadTexts:
    bRadiusServerAcctEntry.setStatus("current")
_BRadiusAcctStatsInterval_Type = Integer32
_BRadiusAcctStatsInterval_Object = MibTableColumn
bRadiusAcctStatsInterval = _BRadiusAcctStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 1),
    _BRadiusAcctStatsInterval_Type()
)
bRadiusAcctStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAcctStatsInterval.setStatus("current")
_BRadiusAcctServerIndex_Type = Integer32
_BRadiusAcctServerIndex_Object = MibTableColumn
bRadiusAcctServerIndex = _BRadiusAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 2),
    _BRadiusAcctServerIndex_Type()
)
bRadiusAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAcctServerIndex.setStatus("current")
_BRadiusAcctServerInetAddressType_Type = InetAddressType
_BRadiusAcctServerInetAddressType_Object = MibTableColumn
bRadiusAcctServerInetAddressType = _BRadiusAcctServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 3),
    _BRadiusAcctServerInetAddressType_Type()
)
bRadiusAcctServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctServerInetAddressType.setStatus("current")
_BRadiusAcctServerInetAddress_Type = InetAddress
_BRadiusAcctServerInetAddress_Object = MibTableColumn
bRadiusAcctServerInetAddress = _BRadiusAcctServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 4),
    _BRadiusAcctServerInetAddress_Type()
)
bRadiusAcctServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctServerInetAddress.setStatus("current")
_BRadiusAcctIntervalDuration_Type = Integer32
_BRadiusAcctIntervalDuration_Object = MibTableColumn
bRadiusAcctIntervalDuration = _BRadiusAcctIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 5),
    _BRadiusAcctIntervalDuration_Type()
)
bRadiusAcctIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctIntervalDuration.setStatus("current")
_BRadiusAcctRequestSent_Type = Unsigned32
_BRadiusAcctRequestSent_Object = MibTableColumn
bRadiusAcctRequestSent = _BRadiusAcctRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 6),
    _BRadiusAcctRequestSent_Type()
)
bRadiusAcctRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctRequestSent.setStatus("current")
_BRadiusAcctStartRequestSent_Type = Unsigned32
_BRadiusAcctStartRequestSent_Object = MibTableColumn
bRadiusAcctStartRequestSent = _BRadiusAcctStartRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 7),
    _BRadiusAcctStartRequestSent_Type()
)
bRadiusAcctStartRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctStartRequestSent.setStatus("current")
_BRadiusAcctStopRequestSent_Type = Unsigned32
_BRadiusAcctStopRequestSent_Object = MibTableColumn
bRadiusAcctStopRequestSent = _BRadiusAcctStopRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 8),
    _BRadiusAcctStopRequestSent_Type()
)
bRadiusAcctStopRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctStopRequestSent.setStatus("current")
_BRadiusAcctInterimUpdateSent_Type = Unsigned32
_BRadiusAcctInterimUpdateSent_Object = MibTableColumn
bRadiusAcctInterimUpdateSent = _BRadiusAcctInterimUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 9),
    _BRadiusAcctInterimUpdateSent_Type()
)
bRadiusAcctInterimUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctInterimUpdateSent.setStatus("current")
_BRadiusAcctResponseReceived_Type = Unsigned32
_BRadiusAcctResponseReceived_Object = MibTableColumn
bRadiusAcctResponseReceived = _BRadiusAcctResponseReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 10),
    _BRadiusAcctResponseReceived_Type()
)
bRadiusAcctResponseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctResponseReceived.setStatus("current")
_BRadiusAcctRequestResent_Type = Unsigned32
_BRadiusAcctRequestResent_Object = MibTableColumn
bRadiusAcctRequestResent = _BRadiusAcctRequestResent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 11),
    _BRadiusAcctRequestResent_Type()
)
bRadiusAcctRequestResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctRequestResent.setStatus("current")
_BRadiusAcctRequestDropped_Type = Unsigned32
_BRadiusAcctRequestDropped_Object = MibTableColumn
bRadiusAcctRequestDropped = _BRadiusAcctRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 12),
    _BRadiusAcctRequestDropped_Type()
)
bRadiusAcctRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctRequestDropped.setStatus("current")
_BRadiusAcctRequestTimedOut_Type = Unsigned32
_BRadiusAcctRequestTimedOut_Object = MibTableColumn
bRadiusAcctRequestTimedOut = _BRadiusAcctRequestTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 13),
    _BRadiusAcctRequestTimedOut_Type()
)
bRadiusAcctRequestTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctRequestTimedOut.setStatus("current")
_BRadiusAcctRequestSentFail_Type = Unsigned32
_BRadiusAcctRequestSentFail_Object = MibTableColumn
bRadiusAcctRequestSentFail = _BRadiusAcctRequestSentFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 14),
    _BRadiusAcctRequestSentFail_Type()
)
bRadiusAcctRequestSentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctRequestSentFail.setStatus("current")
_BRadiusAcctPeakRequestPending_Type = Unsigned32
_BRadiusAcctPeakRequestPending_Object = MibTableColumn
bRadiusAcctPeakRequestPending = _BRadiusAcctPeakRequestPending_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 15),
    _BRadiusAcctPeakRequestPending_Type()
)
bRadiusAcctPeakRequestPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctPeakRequestPending.setStatus("current")
_BRadiusAcctMalformedRespDropped_Type = Unsigned32
_BRadiusAcctMalformedRespDropped_Object = MibTableColumn
bRadiusAcctMalformedRespDropped = _BRadiusAcctMalformedRespDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 16),
    _BRadiusAcctMalformedRespDropped_Type()
)
bRadiusAcctMalformedRespDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctMalformedRespDropped.setStatus("current")
_BRadiusAcctBadAuthenticatorRcvd_Type = Unsigned32
_BRadiusAcctBadAuthenticatorRcvd_Object = MibTableColumn
bRadiusAcctBadAuthenticatorRcvd = _BRadiusAcctBadAuthenticatorRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 17),
    _BRadiusAcctBadAuthenticatorRcvd_Type()
)
bRadiusAcctBadAuthenticatorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctBadAuthenticatorRcvd.setStatus("current")
_BRadiusAcctServerMarkedDead_Type = Unsigned32
_BRadiusAcctServerMarkedDead_Object = MibTableColumn
bRadiusAcctServerMarkedDead = _BRadiusAcctServerMarkedDead_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 18),
    _BRadiusAcctServerMarkedDead_Type()
)
bRadiusAcctServerMarkedDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctServerMarkedDead.setStatus("current")
_BRadiusAcctLatencyMin_Type = Unsigned32
_BRadiusAcctLatencyMin_Object = MibTableColumn
bRadiusAcctLatencyMin = _BRadiusAcctLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 19),
    _BRadiusAcctLatencyMin_Type()
)
bRadiusAcctLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctLatencyMin.setStatus("current")
_BRadiusAcctLatencyMax_Type = Unsigned32
_BRadiusAcctLatencyMax_Object = MibTableColumn
bRadiusAcctLatencyMax = _BRadiusAcctLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 20),
    _BRadiusAcctLatencyMax_Type()
)
bRadiusAcctLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctLatencyMax.setStatus("current")
_BRadiusAcctLatencyAvg_Type = Unsigned32
_BRadiusAcctLatencyAvg_Object = MibTableColumn
bRadiusAcctLatencyAvg = _BRadiusAcctLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 21),
    _BRadiusAcctLatencyAvg_Type()
)
bRadiusAcctLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctLatencyAvg.setStatus("current")
_BRadiusAcctLatencyLast_Type = Unsigned32
_BRadiusAcctLatencyLast_Object = MibTableColumn
bRadiusAcctLatencyLast = _BRadiusAcctLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 22),
    _BRadiusAcctLatencyLast_Type()
)
bRadiusAcctLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctLatencyLast.setStatus("current")
_BRadiusAcctAAAGroupName_Type = DisplayString
_BRadiusAcctAAAGroupName_Object = MibTableColumn
bRadiusAcctAAAGroupName = _BRadiusAcctAAAGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 2, 1, 23),
    _BRadiusAcctAAAGroupName_Type()
)
bRadiusAcctAAAGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAcctAAAGroupName.setStatus("current")
_BRadiusClientCoATable_Object = MibTable
bRadiusClientCoATable = _BRadiusClientCoATable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    bRadiusClientCoATable.setStatus("current")
_BRadiusClientCoAEntry_Object = MibTableRow
bRadiusClientCoAEntry = _BRadiusClientCoAEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1)
)
bRadiusClientCoAEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusCOAStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusCoAClientIndex"),
)
if mibBuilder.loadTexts:
    bRadiusClientCoAEntry.setStatus("current")
_BRadiusCOAStatsInterval_Type = Integer32
_BRadiusCOAStatsInterval_Object = MibTableColumn
bRadiusCOAStatsInterval = _BRadiusCOAStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 1),
    _BRadiusCOAStatsInterval_Type()
)
bRadiusCOAStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusCOAStatsInterval.setStatus("current")
_BRadiusCoAClientIndex_Type = Integer32
_BRadiusCoAClientIndex_Object = MibTableColumn
bRadiusCoAClientIndex = _BRadiusCoAClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 2),
    _BRadiusCoAClientIndex_Type()
)
bRadiusCoAClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusCoAClientIndex.setStatus("current")
_BRadiusCoAClientInetAddressType_Type = InetAddressType
_BRadiusCoAClientInetAddressType_Object = MibTableColumn
bRadiusCoAClientInetAddressType = _BRadiusCoAClientInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 3),
    _BRadiusCoAClientInetAddressType_Type()
)
bRadiusCoAClientInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAClientInetAddressType.setStatus("current")
_BRadiusCoAClientInetAddress_Type = InetAddress
_BRadiusCoAClientInetAddress_Object = MibTableColumn
bRadiusCoAClientInetAddress = _BRadiusCoAClientInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 4),
    _BRadiusCoAClientInetAddress_Type()
)
bRadiusCoAClientInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAClientInetAddress.setStatus("current")
_BRadiusCoAIntervalDuration_Type = Integer32
_BRadiusCoAIntervalDuration_Object = MibTableColumn
bRadiusCoAIntervalDuration = _BRadiusCoAIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 5),
    _BRadiusCoAIntervalDuration_Type()
)
bRadiusCoAIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAIntervalDuration.setStatus("current")
_BRadiusCoAAckSent_Type = Unsigned32
_BRadiusCoAAckSent_Object = MibTableColumn
bRadiusCoAAckSent = _BRadiusCoAAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 6),
    _BRadiusCoAAckSent_Type()
)
bRadiusCoAAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAAckSent.setStatus("current")
_BRadiusCoANackSent_Type = Unsigned32
_BRadiusCoANackSent_Object = MibTableColumn
bRadiusCoANackSent = _BRadiusCoANackSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 7),
    _BRadiusCoANackSent_Type()
)
bRadiusCoANackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoANackSent.setStatus("current")
_BRadiusCoARequestReceived_Type = Unsigned32
_BRadiusCoARequestReceived_Object = MibTableColumn
bRadiusCoARequestReceived = _BRadiusCoARequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 8),
    _BRadiusCoARequestReceived_Type()
)
bRadiusCoARequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoARequestReceived.setStatus("current")
_BRadiusCoARequestDropped_Type = Unsigned32
_BRadiusCoARequestDropped_Object = MibTableColumn
bRadiusCoARequestDropped = _BRadiusCoARequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 9),
    _BRadiusCoARequestDropped_Type()
)
bRadiusCoARequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoARequestDropped.setStatus("current")
_BRadiusCoAReqDropDueToDupReq_Type = Unsigned32
_BRadiusCoAReqDropDueToDupReq_Object = MibTableColumn
bRadiusCoAReqDropDueToDupReq = _BRadiusCoAReqDropDueToDupReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 10),
    _BRadiusCoAReqDropDueToDupReq_Type()
)
bRadiusCoAReqDropDueToDupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAReqDropDueToDupReq.setStatus("current")
_BRadiusCoAReqDropDueToInvalidTime_Type = Unsigned32
_BRadiusCoAReqDropDueToInvalidTime_Object = MibTableColumn
bRadiusCoAReqDropDueToInvalidTime = _BRadiusCoAReqDropDueToInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 11),
    _BRadiusCoAReqDropDueToInvalidTime_Type()
)
bRadiusCoAReqDropDueToInvalidTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAReqDropDueToInvalidTime.setStatus("current")
_BRadiusCoAReqDropDueToBadAuthenticator_Type = Unsigned32
_BRadiusCoAReqDropDueToBadAuthenticator_Object = MibTableColumn
bRadiusCoAReqDropDueToBadAuthenticator = _BRadiusCoAReqDropDueToBadAuthenticator_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 12),
    _BRadiusCoAReqDropDueToBadAuthenticator_Type()
)
bRadiusCoAReqDropDueToBadAuthenticator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAReqDropDueToBadAuthenticator.setStatus("current")
_BRadiusCoANackDueToInvalidReq_Type = Unsigned32
_BRadiusCoANackDueToInvalidReq_Object = MibTableColumn
bRadiusCoANackDueToInvalidReq = _BRadiusCoANackDueToInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 13),
    _BRadiusCoANackDueToInvalidReq_Type()
)
bRadiusCoANackDueToInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoANackDueToInvalidReq.setStatus("current")
_BRadiusCoANackDueToExceedMaxOutstanding_Type = Unsigned32
_BRadiusCoANackDueToExceedMaxOutstanding_Object = MibTableColumn
bRadiusCoANackDueToExceedMaxOutstanding = _BRadiusCoANackDueToExceedMaxOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 14),
    _BRadiusCoANackDueToExceedMaxOutstanding_Type()
)
bRadiusCoANackDueToExceedMaxOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoANackDueToExceedMaxOutstanding.setStatus("current")
_BRadiusDisconnectRequestReceived_Type = Unsigned32
_BRadiusDisconnectRequestReceived_Object = MibTableColumn
bRadiusDisconnectRequestReceived = _BRadiusDisconnectRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 15),
    _BRadiusDisconnectRequestReceived_Type()
)
bRadiusDisconnectRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectRequestReceived.setStatus("current")
_BRadiusDisconnectAckSent_Type = Unsigned32
_BRadiusDisconnectAckSent_Object = MibTableColumn
bRadiusDisconnectAckSent = _BRadiusDisconnectAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 16),
    _BRadiusDisconnectAckSent_Type()
)
bRadiusDisconnectAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectAckSent.setStatus("current")
_BRadiusDisconnectNackSent_Type = Unsigned32
_BRadiusDisconnectNackSent_Object = MibTableColumn
bRadiusDisconnectNackSent = _BRadiusDisconnectNackSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 17),
    _BRadiusDisconnectNackSent_Type()
)
bRadiusDisconnectNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectNackSent.setStatus("current")
_BRadiusDisconnectRequestDropped_Type = Unsigned32
_BRadiusDisconnectRequestDropped_Object = MibTableColumn
bRadiusDisconnectRequestDropped = _BRadiusDisconnectRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 18),
    _BRadiusDisconnectRequestDropped_Type()
)
bRadiusDisconnectRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectRequestDropped.setStatus("current")
_BRadiusDisconnectReqDropDueToDupReq_Type = Unsigned32
_BRadiusDisconnectReqDropDueToDupReq_Object = MibTableColumn
bRadiusDisconnectReqDropDueToDupReq = _BRadiusDisconnectReqDropDueToDupReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 19),
    _BRadiusDisconnectReqDropDueToDupReq_Type()
)
bRadiusDisconnectReqDropDueToDupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectReqDropDueToDupReq.setStatus("current")
_BRadiusDisconnectReqDropDueToInvalidTime_Type = Unsigned32
_BRadiusDisconnectReqDropDueToInvalidTime_Object = MibTableColumn
bRadiusDisconnectReqDropDueToInvalidTime = _BRadiusDisconnectReqDropDueToInvalidTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 20),
    _BRadiusDisconnectReqDropDueToInvalidTime_Type()
)
bRadiusDisconnectReqDropDueToInvalidTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectReqDropDueToInvalidTime.setStatus("current")
_BRadiusDisconnectReqDropDueToBadAuthenticator_Type = Unsigned32
_BRadiusDisconnectReqDropDueToBadAuthenticator_Object = MibTableColumn
bRadiusDisconnectReqDropDueToBadAuthenticator = _BRadiusDisconnectReqDropDueToBadAuthenticator_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 21),
    _BRadiusDisconnectReqDropDueToBadAuthenticator_Type()
)
bRadiusDisconnectReqDropDueToBadAuthenticator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectReqDropDueToBadAuthenticator.setStatus("current")
_BRadiusDisconnectNackDueToInvalidReq_Type = Unsigned32
_BRadiusDisconnectNackDueToInvalidReq_Object = MibTableColumn
bRadiusDisconnectNackDueToInvalidReq = _BRadiusDisconnectNackDueToInvalidReq_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 22),
    _BRadiusDisconnectNackDueToInvalidReq_Type()
)
bRadiusDisconnectNackDueToInvalidReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectNackDueToInvalidReq.setStatus("current")
_BRadiusDisconnectNackDueToExceedMaxOutstanding_Type = Unsigned32
_BRadiusDisconnectNackDueToExceedMaxOutstanding_Object = MibTableColumn
bRadiusDisconnectNackDueToExceedMaxOutstanding = _BRadiusDisconnectNackDueToExceedMaxOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 23),
    _BRadiusDisconnectNackDueToExceedMaxOutstanding_Type()
)
bRadiusDisconnectNackDueToExceedMaxOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusDisconnectNackDueToExceedMaxOutstanding.setStatus("current")
_BRadiusCoALatencyMin_Type = Unsigned32
_BRadiusCoALatencyMin_Object = MibTableColumn
bRadiusCoALatencyMin = _BRadiusCoALatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 24),
    _BRadiusCoALatencyMin_Type()
)
bRadiusCoALatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoALatencyMin.setStatus("current")
_BRadiusCoALatencyMax_Type = Unsigned32
_BRadiusCoALatencyMax_Object = MibTableColumn
bRadiusCoALatencyMax = _BRadiusCoALatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 25),
    _BRadiusCoALatencyMax_Type()
)
bRadiusCoALatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoALatencyMax.setStatus("current")
_BRadiusCoALatencyAvg_Type = Unsigned32
_BRadiusCoALatencyAvg_Object = MibTableColumn
bRadiusCoALatencyAvg = _BRadiusCoALatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 26),
    _BRadiusCoALatencyAvg_Type()
)
bRadiusCoALatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoALatencyAvg.setStatus("current")
_BRadiusCoALatencyLast_Type = Unsigned32
_BRadiusCoALatencyLast_Object = MibTableColumn
bRadiusCoALatencyLast = _BRadiusCoALatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 27),
    _BRadiusCoALatencyLast_Type()
)
bRadiusCoALatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoALatencyLast.setStatus("current")
_BRadiusCoADMLatencyMin_Type = Unsigned32
_BRadiusCoADMLatencyMin_Object = MibTableColumn
bRadiusCoADMLatencyMin = _BRadiusCoADMLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 28),
    _BRadiusCoADMLatencyMin_Type()
)
bRadiusCoADMLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoADMLatencyMin.setStatus("current")
_BRadiusCoADMLatencyMax_Type = Unsigned32
_BRadiusCoADMLatencyMax_Object = MibTableColumn
bRadiusCoADMLatencyMax = _BRadiusCoADMLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 29),
    _BRadiusCoADMLatencyMax_Type()
)
bRadiusCoADMLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoADMLatencyMax.setStatus("current")
_BRadiusCoADMLatencyAvg_Type = Unsigned32
_BRadiusCoADMLatencyAvg_Object = MibTableColumn
bRadiusCoADMLatencyAvg = _BRadiusCoADMLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 30),
    _BRadiusCoADMLatencyAvg_Type()
)
bRadiusCoADMLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoADMLatencyAvg.setStatus("current")
_BRadiusCoADMLatencyLast_Type = Unsigned32
_BRadiusCoADMLatencyLast_Object = MibTableColumn
bRadiusCoADMLatencyLast = _BRadiusCoADMLatencyLast_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 31),
    _BRadiusCoADMLatencyLast_Type()
)
bRadiusCoADMLatencyLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoADMLatencyLast.setStatus("current")
_BRadiusCoAAAAGroupName_Type = DisplayString
_BRadiusCoAAAAGroupName_Object = MibTableColumn
bRadiusCoAAAAGroupName = _BRadiusCoAAAAGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 3, 1, 32),
    _BRadiusCoAAAAGroupName_Type()
)
bRadiusCoAAAAGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusCoAAAAGroupName.setStatus("current")
_BAAAGroupAuthTable_Object = MibTable
bAAAGroupAuthTable = _BAAAGroupAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    bAAAGroupAuthTable.setStatus("current")
_BAAAGroupAuthEntry_Object = MibTableRow
bAAAGroupAuthEntry = _BAAAGroupAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1)
)
bAAAGroupAuthEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bAAAGroupAuthStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bAAAGroupAuthIndex"),
)
if mibBuilder.loadTexts:
    bAAAGroupAuthEntry.setStatus("current")
_BAAAGroupAuthStatsInterval_Type = Integer32
_BAAAGroupAuthStatsInterval_Object = MibTableColumn
bAAAGroupAuthStatsInterval = _BAAAGroupAuthStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 1),
    _BAAAGroupAuthStatsInterval_Type()
)
bAAAGroupAuthStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupAuthStatsInterval.setStatus("current")
_BAAAGroupAuthIndex_Type = Integer32
_BAAAGroupAuthIndex_Object = MibTableColumn
bAAAGroupAuthIndex = _BAAAGroupAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 2),
    _BAAAGroupAuthIndex_Type()
)
bAAAGroupAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupAuthIndex.setStatus("current")
_BAAAGroupAuthName_Type = DisplayString
_BAAAGroupAuthName_Object = MibTableColumn
bAAAGroupAuthName = _BAAAGroupAuthName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 3),
    _BAAAGroupAuthName_Type()
)
bAAAGroupAuthName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAuthName.setStatus("current")
_BAAAGroupAuthIntervalDuration_Type = Integer32
_BAAAGroupAuthIntervalDuration_Object = MibTableColumn
bAAAGroupAuthIntervalDuration = _BAAAGroupAuthIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 4),
    _BAAAGroupAuthIntervalDuration_Type()
)
bAAAGroupAuthIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAuthIntervalDuration.setStatus("current")
_BAAAGroupMaximumOutstandingAuthReqs_Type = Unsigned32
_BAAAGroupMaximumOutstandingAuthReqs_Object = MibTableColumn
bAAAGroupMaximumOutstandingAuthReqs = _BAAAGroupMaximumOutstandingAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 5),
    _BAAAGroupMaximumOutstandingAuthReqs_Type()
)
bAAAGroupMaximumOutstandingAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupMaximumOutstandingAuthReqs.setStatus("current")
_BAAAGroupPeakOutstandingAuthReqsReached_Type = Unsigned32
_BAAAGroupPeakOutstandingAuthReqsReached_Object = MibTableColumn
bAAAGroupPeakOutstandingAuthReqsReached = _BAAAGroupPeakOutstandingAuthReqsReached_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 6),
    _BAAAGroupPeakOutstandingAuthReqsReached_Type()
)
bAAAGroupPeakOutstandingAuthReqsReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupPeakOutstandingAuthReqsReached.setStatus("current")
_BAAAGroupAuthReqsDropped_Type = Unsigned32
_BAAAGroupAuthReqsDropped_Object = MibTableColumn
bAAAGroupAuthReqsDropped = _BAAAGroupAuthReqsDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 7),
    _BAAAGroupAuthReqsDropped_Type()
)
bAAAGroupAuthReqsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAuthReqsDropped.setStatus("current")
_BAAAGroupOutstandingAuthReqsHighThreshold_Type = Unsigned32
_BAAAGroupOutstandingAuthReqsHighThreshold_Object = MibTableColumn
bAAAGroupOutstandingAuthReqsHighThreshold = _BAAAGroupOutstandingAuthReqsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 8),
    _BAAAGroupOutstandingAuthReqsHighThreshold_Type()
)
bAAAGroupOutstandingAuthReqsHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAuthReqsHighThreshold.setStatus("current")
_BAAAGroupOutstandingAuthReqsLowThreshold_Type = Unsigned32
_BAAAGroupOutstandingAuthReqsLowThreshold_Object = MibTableColumn
bAAAGroupOutstandingAuthReqsLowThreshold = _BAAAGroupOutstandingAuthReqsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 9),
    _BAAAGroupOutstandingAuthReqsLowThreshold_Type()
)
bAAAGroupOutstandingAuthReqsLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAuthReqsLowThreshold.setStatus("current")
_BAAAGroupAuthCurrentOutstanding_Type = Unsigned32
_BAAAGroupAuthCurrentOutstanding_Object = MibTableColumn
bAAAGroupAuthCurrentOutstanding = _BAAAGroupAuthCurrentOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 4, 1, 10),
    _BAAAGroupAuthCurrentOutstanding_Type()
)
bAAAGroupAuthCurrentOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAuthCurrentOutstanding.setStatus("current")
_BAAAGroupAcctTable_Object = MibTable
bAAAGroupAcctTable = _BAAAGroupAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    bAAAGroupAcctTable.setStatus("current")
_BAAAGroupAcctEntry_Object = MibTableRow
bAAAGroupAcctEntry = _BAAAGroupAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1)
)
bAAAGroupAcctEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bAAAGroupAcctStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bAAAGroupAcctIndex"),
)
if mibBuilder.loadTexts:
    bAAAGroupAcctEntry.setStatus("current")
_BAAAGroupAcctStatsInterval_Type = Integer32
_BAAAGroupAcctStatsInterval_Object = MibTableColumn
bAAAGroupAcctStatsInterval = _BAAAGroupAcctStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 1),
    _BAAAGroupAcctStatsInterval_Type()
)
bAAAGroupAcctStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupAcctStatsInterval.setStatus("current")
_BAAAGroupAcctIndex_Type = Integer32
_BAAAGroupAcctIndex_Object = MibTableColumn
bAAAGroupAcctIndex = _BAAAGroupAcctIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 2),
    _BAAAGroupAcctIndex_Type()
)
bAAAGroupAcctIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupAcctIndex.setStatus("current")
_BAAAGroupAcctName_Type = DisplayString
_BAAAGroupAcctName_Object = MibTableColumn
bAAAGroupAcctName = _BAAAGroupAcctName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 3),
    _BAAAGroupAcctName_Type()
)
bAAAGroupAcctName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAcctName.setStatus("current")
_BAAAGroupAcctIntervalDuration_Type = Integer32
_BAAAGroupAcctIntervalDuration_Object = MibTableColumn
bAAAGroupAcctIntervalDuration = _BAAAGroupAcctIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 4),
    _BAAAGroupAcctIntervalDuration_Type()
)
bAAAGroupAcctIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAcctIntervalDuration.setStatus("current")
_BAAAGroupMaximumOutstandingAcctReqs_Type = Unsigned32
_BAAAGroupMaximumOutstandingAcctReqs_Object = MibTableColumn
bAAAGroupMaximumOutstandingAcctReqs = _BAAAGroupMaximumOutstandingAcctReqs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 5),
    _BAAAGroupMaximumOutstandingAcctReqs_Type()
)
bAAAGroupMaximumOutstandingAcctReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupMaximumOutstandingAcctReqs.setStatus("current")
_BAAAGroupPeakOutstandingAcctReqsReached_Type = Unsigned32
_BAAAGroupPeakOutstandingAcctReqsReached_Object = MibTableColumn
bAAAGroupPeakOutstandingAcctReqsReached = _BAAAGroupPeakOutstandingAcctReqsReached_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 6),
    _BAAAGroupPeakOutstandingAcctReqsReached_Type()
)
bAAAGroupPeakOutstandingAcctReqsReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupPeakOutstandingAcctReqsReached.setStatus("current")
_BAAAGroupAcctReqsDropped_Type = Unsigned32
_BAAAGroupAcctReqsDropped_Object = MibTableColumn
bAAAGroupAcctReqsDropped = _BAAAGroupAcctReqsDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 7),
    _BAAAGroupAcctReqsDropped_Type()
)
bAAAGroupAcctReqsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAcctReqsDropped.setStatus("current")
_BAAAGroupOutstandingAcctReqsHighThreshold_Type = Unsigned32
_BAAAGroupOutstandingAcctReqsHighThreshold_Object = MibTableColumn
bAAAGroupOutstandingAcctReqsHighThreshold = _BAAAGroupOutstandingAcctReqsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 8),
    _BAAAGroupOutstandingAcctReqsHighThreshold_Type()
)
bAAAGroupOutstandingAcctReqsHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAcctReqsHighThreshold.setStatus("current")
_BAAAGroupOutstandingAcctReqsLowThreshold_Type = Unsigned32
_BAAAGroupOutstandingAcctReqsLowThreshold_Object = MibTableColumn
bAAAGroupOutstandingAcctReqsLowThreshold = _BAAAGroupOutstandingAcctReqsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 9),
    _BAAAGroupOutstandingAcctReqsLowThreshold_Type()
)
bAAAGroupOutstandingAcctReqsLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAcctReqsLowThreshold.setStatus("current")
_BAAAGroupAcctCurrentOutstanding_Type = Unsigned32
_BAAAGroupAcctCurrentOutstanding_Object = MibTableColumn
bAAAGroupAcctCurrentOutstanding = _BAAAGroupAcctCurrentOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 5, 1, 10),
    _BAAAGroupAcctCurrentOutstanding_Type()
)
bAAAGroupAcctCurrentOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupAcctCurrentOutstanding.setStatus("current")
_BAAAGroupCoATable_Object = MibTable
bAAAGroupCoATable = _BAAAGroupCoATable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    bAAAGroupCoATable.setStatus("current")
_BAAAGroupCoAEntry_Object = MibTableRow
bAAAGroupCoAEntry = _BAAAGroupCoAEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1)
)
bAAAGroupCoAEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bAAAGroupCoAStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bAAAGroupCoAIndex"),
)
if mibBuilder.loadTexts:
    bAAAGroupCoAEntry.setStatus("current")
_BAAAGroupCoAStatsInterval_Type = Integer32
_BAAAGroupCoAStatsInterval_Object = MibTableColumn
bAAAGroupCoAStatsInterval = _BAAAGroupCoAStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 1),
    _BAAAGroupCoAStatsInterval_Type()
)
bAAAGroupCoAStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupCoAStatsInterval.setStatus("current")
_BAAAGroupCoAIndex_Type = Integer32
_BAAAGroupCoAIndex_Object = MibTableColumn
bAAAGroupCoAIndex = _BAAAGroupCoAIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 2),
    _BAAAGroupCoAIndex_Type()
)
bAAAGroupCoAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bAAAGroupCoAIndex.setStatus("current")
_BAAAGroupCoAName_Type = DisplayString
_BAAAGroupCoAName_Object = MibTableColumn
bAAAGroupCoAName = _BAAAGroupCoAName_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 3),
    _BAAAGroupCoAName_Type()
)
bAAAGroupCoAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupCoAName.setStatus("current")
_BAAAGroupCoAIntervalDuration_Type = Integer32
_BAAAGroupCoAIntervalDuration_Object = MibTableColumn
bAAAGroupCoAIntervalDuration = _BAAAGroupCoAIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 4),
    _BAAAGroupCoAIntervalDuration_Type()
)
bAAAGroupCoAIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupCoAIntervalDuration.setStatus("current")
_BAAAGroupCoANumOfClients_Type = Unsigned32
_BAAAGroupCoANumOfClients_Object = MibTableColumn
bAAAGroupCoANumOfClients = _BAAAGroupCoANumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 5),
    _BAAAGroupCoANumOfClients_Type()
)
bAAAGroupCoANumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupCoANumOfClients.setStatus("current")
_BAAAGroupCoAReqsDropDueToInvalidClient_Type = Unsigned32
_BAAAGroupCoAReqsDropDueToInvalidClient_Object = MibTableColumn
bAAAGroupCoAReqsDropDueToInvalidClient = _BAAAGroupCoAReqsDropDueToInvalidClient_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 6),
    _BAAAGroupCoAReqsDropDueToInvalidClient_Type()
)
bAAAGroupCoAReqsDropDueToInvalidClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupCoAReqsDropDueToInvalidClient.setStatus("current")
_BAAAGroupDisconnectReqsDropDueToInvalidClient_Type = Unsigned32
_BAAAGroupDisconnectReqsDropDueToInvalidClient_Object = MibTableColumn
bAAAGroupDisconnectReqsDropDueToInvalidClient = _BAAAGroupDisconnectReqsDropDueToInvalidClient_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 7),
    _BAAAGroupDisconnectReqsDropDueToInvalidClient_Type()
)
bAAAGroupDisconnectReqsDropDueToInvalidClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupDisconnectReqsDropDueToInvalidClient.setStatus("current")
_BAAAGroupMaximumOutstandingCoAReqs_Type = Unsigned32
_BAAAGroupMaximumOutstandingCoAReqs_Object = MibTableColumn
bAAAGroupMaximumOutstandingCoAReqs = _BAAAGroupMaximumOutstandingCoAReqs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 8),
    _BAAAGroupMaximumOutstandingCoAReqs_Type()
)
bAAAGroupMaximumOutstandingCoAReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupMaximumOutstandingCoAReqs.setStatus("current")
_BAAAGroupPeakOutstandingCoAReqs_Type = Unsigned32
_BAAAGroupPeakOutstandingCoAReqs_Object = MibTableColumn
bAAAGroupPeakOutstandingCoAReqs = _BAAAGroupPeakOutstandingCoAReqs_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 9),
    _BAAAGroupPeakOutstandingCoAReqs_Type()
)
bAAAGroupPeakOutstandingCoAReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupPeakOutstandingCoAReqs.setStatus("current")
_BAAAGroupOutstandingCoAReqsHighThreshold_Type = Unsigned32
_BAAAGroupOutstandingCoAReqsHighThreshold_Object = MibTableColumn
bAAAGroupOutstandingCoAReqsHighThreshold = _BAAAGroupOutstandingCoAReqsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 10),
    _BAAAGroupOutstandingCoAReqsHighThreshold_Type()
)
bAAAGroupOutstandingCoAReqsHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingCoAReqsHighThreshold.setStatus("current")
_BAAAGroupOutstandingCoAReqsLowThreshold_Type = Unsigned32
_BAAAGroupOutstandingCoAReqsLowThreshold_Object = MibTableColumn
bAAAGroupOutstandingCoAReqsLowThreshold = _BAAAGroupOutstandingCoAReqsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 11),
    _BAAAGroupOutstandingCoAReqsLowThreshold_Type()
)
bAAAGroupOutstandingCoAReqsLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupOutstandingCoAReqsLowThreshold.setStatus("current")
_BAAAGroupCoaCurrentOutstanding_Type = Unsigned32
_BAAAGroupCoaCurrentOutstanding_Object = MibTableColumn
bAAAGroupCoaCurrentOutstanding = _BAAAGroupCoaCurrentOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 6, 1, 12),
    _BAAAGroupCoaCurrentOutstanding_Type()
)
bAAAGroupCoaCurrentOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAAAGroupCoaCurrentOutstanding.setStatus("current")
_BRadiusLatencyAuthTable_Object = MibTable
bRadiusLatencyAuthTable = _BRadiusLatencyAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7)
)
if mibBuilder.loadTexts:
    bRadiusLatencyAuthTable.setStatus("current")
_BRadiusLatencyAuthEntry_Object = MibTableRow
bRadiusLatencyAuthEntry = _BRadiusLatencyAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1)
)
bRadiusLatencyAuthEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusAuthLatencyStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusAuthInstanceIndex"),
)
if mibBuilder.loadTexts:
    bRadiusLatencyAuthEntry.setStatus("current")
_BRadiusAuthLatencyStatsInterval_Type = Integer32
_BRadiusAuthLatencyStatsInterval_Object = MibTableColumn
bRadiusAuthLatencyStatsInterval = _BRadiusAuthLatencyStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 1),
    _BRadiusAuthLatencyStatsInterval_Type()
)
bRadiusAuthLatencyStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyStatsInterval.setStatus("current")
_BRadiusAuthInstanceIndex_Type = BenuRadiusInstance
_BRadiusAuthInstanceIndex_Object = MibTableColumn
bRadiusAuthInstanceIndex = _BRadiusAuthInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 2),
    _BRadiusAuthInstanceIndex_Type()
)
bRadiusAuthInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusAuthInstanceIndex.setStatus("current")
_BRadiusAuthLatencyIntervalDuration_Type = Integer32
_BRadiusAuthLatencyIntervalDuration_Object = MibTableColumn
bRadiusAuthLatencyIntervalDuration = _BRadiusAuthLatencyIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 3),
    _BRadiusAuthLatencyIntervalDuration_Type()
)
bRadiusAuthLatencyIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthLatencyIntervalDuration.setStatus("current")
_BRadiusAuthRequestTotalPackets_Type = Unsigned32
_BRadiusAuthRequestTotalPackets_Object = MibTableColumn
bRadiusAuthRequestTotalPackets = _BRadiusAuthRequestTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 4),
    _BRadiusAuthRequestTotalPackets_Type()
)
bRadiusAuthRequestTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthRequestTotalPackets.setStatus("current")
_BRadiusAuthRequestMaximumProcessingTime_Type = Unsigned32
_BRadiusAuthRequestMaximumProcessingTime_Object = MibTableColumn
bRadiusAuthRequestMaximumProcessingTime = _BRadiusAuthRequestMaximumProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 5),
    _BRadiusAuthRequestMaximumProcessingTime_Type()
)
bRadiusAuthRequestMaximumProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthRequestMaximumProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthRequestMaximumProcessingTime.setUnits("microseconds")
_BRadiusAuthRequestMinimumProcessingTime_Type = Unsigned32
_BRadiusAuthRequestMinimumProcessingTime_Object = MibTableColumn
bRadiusAuthRequestMinimumProcessingTime = _BRadiusAuthRequestMinimumProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 6),
    _BRadiusAuthRequestMinimumProcessingTime_Type()
)
bRadiusAuthRequestMinimumProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthRequestMinimumProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthRequestMinimumProcessingTime.setUnits("microseconds")
_BRadiusAuthRequestAverageProcessingTime_Type = Unsigned32
_BRadiusAuthRequestAverageProcessingTime_Object = MibTableColumn
bRadiusAuthRequestAverageProcessingTime = _BRadiusAuthRequestAverageProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 7),
    _BRadiusAuthRequestAverageProcessingTime_Type()
)
bRadiusAuthRequestAverageProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthRequestAverageProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthRequestAverageProcessingTime.setUnits("microseconds")
_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Type = Unsigned32
_BRadiusAuthRequestProcessingTimeGreaterthan1MS_Object = MibTableColumn
bRadiusAuthRequestProcessingTimeGreaterthan1MS = _BRadiusAuthRequestProcessingTimeGreaterthan1MS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 8),
    _BRadiusAuthRequestProcessingTimeGreaterthan1MS_Type()
)
bRadiusAuthRequestProcessingTimeGreaterthan1MS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthRequestProcessingTimeGreaterthan1MS.setStatus("current")
_BRadiusAuthResponseTotalPackets_Type = Unsigned32
_BRadiusAuthResponseTotalPackets_Object = MibTableColumn
bRadiusAuthResponseTotalPackets = _BRadiusAuthResponseTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 9),
    _BRadiusAuthResponseTotalPackets_Type()
)
bRadiusAuthResponseTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthResponseTotalPackets.setStatus("current")
_BRadiusAuthResponseMaximumProcessingTime_Type = Unsigned32
_BRadiusAuthResponseMaximumProcessingTime_Object = MibTableColumn
bRadiusAuthResponseMaximumProcessingTime = _BRadiusAuthResponseMaximumProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 10),
    _BRadiusAuthResponseMaximumProcessingTime_Type()
)
bRadiusAuthResponseMaximumProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthResponseMaximumProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthResponseMaximumProcessingTime.setUnits("microseconds")
_BRadiusAuthResponseMinimumProcessingTime_Type = Unsigned32
_BRadiusAuthResponseMinimumProcessingTime_Object = MibTableColumn
bRadiusAuthResponseMinimumProcessingTime = _BRadiusAuthResponseMinimumProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 11),
    _BRadiusAuthResponseMinimumProcessingTime_Type()
)
bRadiusAuthResponseMinimumProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthResponseMinimumProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthResponseMinimumProcessingTime.setUnits("microseconds")
_BRadiusAuthResponseAverageProcessingTime_Type = Unsigned32
_BRadiusAuthResponseAverageProcessingTime_Object = MibTableColumn
bRadiusAuthResponseAverageProcessingTime = _BRadiusAuthResponseAverageProcessingTime_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 12),
    _BRadiusAuthResponseAverageProcessingTime_Type()
)
bRadiusAuthResponseAverageProcessingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthResponseAverageProcessingTime.setStatus("current")
if mibBuilder.loadTexts:
    bRadiusAuthResponseAverageProcessingTime.setUnits("microseconds")
_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Type = Unsigned32
_BRadiusAuthResponseProcessingTimeGreaterthan1MS_Object = MibTableColumn
bRadiusAuthResponseProcessingTimeGreaterthan1MS = _BRadiusAuthResponseProcessingTimeGreaterthan1MS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 1, 7, 1, 13),
    _BRadiusAuthResponseProcessingTimeGreaterthan1MS_Type()
)
bRadiusAuthResponseProcessingTimeGreaterthan1MS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusAuthResponseProcessingTimeGreaterthan1MS.setStatus("current")
_BRadiusNotifObjects_ObjectIdentity = ObjectIdentity
bRadiusNotifObjects = _BRadiusNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bRadiusNotifObjects.setStatus("current")
_BRadiusServerIPAddrType_Type = InetAddressType
_BRadiusServerIPAddrType_Object = MibScalar
bRadiusServerIPAddrType = _BRadiusServerIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 2, 1),
    _BRadiusServerIPAddrType_Type()
)
bRadiusServerIPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bRadiusServerIPAddrType.setStatus("current")
_BRadiusServerIPAddress_Type = InetAddress
_BRadiusServerIPAddress_Object = MibScalar
bRadiusServerIPAddress = _BRadiusServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 2, 2),
    _BRadiusServerIPAddress_Type()
)
bRadiusServerIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bRadiusServerIPAddress.setStatus("current")
_BRadiusProxyMIBObjects_ObjectIdentity = ObjectIdentity
bRadiusProxyMIBObjects = _BRadiusProxyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    bRadiusProxyMIBObjects.setStatus("current")
_BRadiusProxyServerAuthTable_Object = MibTable
bRadiusProxyServerAuthTable = _BRadiusProxyServerAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    bRadiusProxyServerAuthTable.setStatus("current")
_BRadiusProxyServerAuthEntry_Object = MibTableRow
bRadiusProxyServerAuthEntry = _BRadiusProxyServerAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1)
)
bRadiusProxyServerAuthEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusProxyAuthStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusProxyAuthServerIndex"),
)
if mibBuilder.loadTexts:
    bRadiusProxyServerAuthEntry.setStatus("current")
_BRadiusProxyAuthStatsInterval_Type = Integer32
_BRadiusProxyAuthStatsInterval_Object = MibTableColumn
bRadiusProxyAuthStatsInterval = _BRadiusProxyAuthStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 1),
    _BRadiusProxyAuthStatsInterval_Type()
)
bRadiusProxyAuthStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusProxyAuthStatsInterval.setStatus("current")
_BRadiusProxyAuthServerIndex_Type = Integer32
_BRadiusProxyAuthServerIndex_Object = MibTableColumn
bRadiusProxyAuthServerIndex = _BRadiusProxyAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 2),
    _BRadiusProxyAuthServerIndex_Type()
)
bRadiusProxyAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusProxyAuthServerIndex.setStatus("current")
_BRadiusProxyAuthServerInetAddressType_Type = InetAddressType
_BRadiusProxyAuthServerInetAddressType_Object = MibTableColumn
bRadiusProxyAuthServerInetAddressType = _BRadiusProxyAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 3),
    _BRadiusProxyAuthServerInetAddressType_Type()
)
bRadiusProxyAuthServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthServerInetAddressType.setStatus("current")
_BRadiusProxyAuthServerInetAddress_Type = InetAddress
_BRadiusProxyAuthServerInetAddress_Object = MibTableColumn
bRadiusProxyAuthServerInetAddress = _BRadiusProxyAuthServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 4),
    _BRadiusProxyAuthServerInetAddress_Type()
)
bRadiusProxyAuthServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthServerInetAddress.setStatus("current")
_BRadiusProxyAuthIntervalDuration_Type = Integer32
_BRadiusProxyAuthIntervalDuration_Object = MibTableColumn
bRadiusProxyAuthIntervalDuration = _BRadiusProxyAuthIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 5),
    _BRadiusProxyAuthIntervalDuration_Type()
)
bRadiusProxyAuthIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthIntervalDuration.setStatus("current")
_BRadiusProxyAccessRequestRcvd_Type = Unsigned32
_BRadiusProxyAccessRequestRcvd_Object = MibTableColumn
bRadiusProxyAccessRequestRcvd = _BRadiusProxyAccessRequestRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 6),
    _BRadiusProxyAccessRequestRcvd_Type()
)
bRadiusProxyAccessRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessRequestRcvd.setStatus("current")
_BRadiusProxyAccessUnknownTypeRcvd_Type = Unsigned32
_BRadiusProxyAccessUnknownTypeRcvd_Object = MibTableColumn
bRadiusProxyAccessUnknownTypeRcvd = _BRadiusProxyAccessUnknownTypeRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 7),
    _BRadiusProxyAccessUnknownTypeRcvd_Type()
)
bRadiusProxyAccessUnknownTypeRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessUnknownTypeRcvd.setStatus("current")
_BRadiusProxyAccessUnknownClientRcvd_Type = Unsigned32
_BRadiusProxyAccessUnknownClientRcvd_Object = MibTableColumn
bRadiusProxyAccessUnknownClientRcvd = _BRadiusProxyAccessUnknownClientRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 8),
    _BRadiusProxyAccessUnknownClientRcvd_Type()
)
bRadiusProxyAccessUnknownClientRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessUnknownClientRcvd.setStatus("current")
_BRadiusProxyAccessRequestDropped_Type = Unsigned32
_BRadiusProxyAccessRequestDropped_Object = MibTableColumn
bRadiusProxyAccessRequestDropped = _BRadiusProxyAccessRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 9),
    _BRadiusProxyAccessRequestDropped_Type()
)
bRadiusProxyAccessRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessRequestDropped.setStatus("current")
_BRadiusProxyAccessSentFail_Type = Unsigned32
_BRadiusProxyAccessSentFail_Object = MibTableColumn
bRadiusProxyAccessSentFail = _BRadiusProxyAccessSentFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 10),
    _BRadiusProxyAccessSentFail_Type()
)
bRadiusProxyAccessSentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessSentFail.setStatus("current")
_BRadiusProxyAccessBadAuthenticatorRcvd_Type = Unsigned32
_BRadiusProxyAccessBadAuthenticatorRcvd_Object = MibTableColumn
bRadiusProxyAccessBadAuthenticatorRcvd = _BRadiusProxyAccessBadAuthenticatorRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 11),
    _BRadiusProxyAccessBadAuthenticatorRcvd_Type()
)
bRadiusProxyAccessBadAuthenticatorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessBadAuthenticatorRcvd.setStatus("current")
_BRadiusProxyAccessAcceptRcvd_Type = Unsigned32
_BRadiusProxyAccessAcceptRcvd_Object = MibTableColumn
bRadiusProxyAccessAcceptRcvd = _BRadiusProxyAccessAcceptRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 12),
    _BRadiusProxyAccessAcceptRcvd_Type()
)
bRadiusProxyAccessAcceptRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessAcceptRcvd.setStatus("current")
_BRadiusProxyAccessRejectRcvd_Type = Unsigned32
_BRadiusProxyAccessRejectRcvd_Object = MibTableColumn
bRadiusProxyAccessRejectRcvd = _BRadiusProxyAccessRejectRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 13),
    _BRadiusProxyAccessRejectRcvd_Type()
)
bRadiusProxyAccessRejectRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessRejectRcvd.setStatus("current")
_BRadiusProxyAccessChallengeRcvd_Type = Unsigned32
_BRadiusProxyAccessChallengeRcvd_Object = MibTableColumn
bRadiusProxyAccessChallengeRcvd = _BRadiusProxyAccessChallengeRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 14),
    _BRadiusProxyAccessChallengeRcvd_Type()
)
bRadiusProxyAccessChallengeRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAccessChallengeRcvd.setStatus("current")
_BRadiusProxySubscriberBlocked_Type = Unsigned32
_BRadiusProxySubscriberBlocked_Object = MibTableColumn
bRadiusProxySubscriberBlocked = _BRadiusProxySubscriberBlocked_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 15),
    _BRadiusProxySubscriberBlocked_Type()
)
bRadiusProxySubscriberBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxySubscriberBlocked.setStatus("current")
_BRadiusProxySubscriberDeleted_Type = Unsigned32
_BRadiusProxySubscriberDeleted_Object = MibTableColumn
bRadiusProxySubscriberDeleted = _BRadiusProxySubscriberDeleted_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 1, 1, 16),
    _BRadiusProxySubscriberDeleted_Type()
)
bRadiusProxySubscriberDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxySubscriberDeleted.setStatus("current")
_BRadiusProxyServerAcctTable_Object = MibTable
bRadiusProxyServerAcctTable = _BRadiusProxyServerAcctTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    bRadiusProxyServerAcctTable.setStatus("current")
_BRadiusProxyServerAcctEntry_Object = MibTableRow
bRadiusProxyServerAcctEntry = _BRadiusProxyServerAcctEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1)
)
bRadiusProxyServerAcctEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusProxyAcctStatsInterval"),
    (0, "BENU-RADIUS-MIB", "bRadiusProxyAcctServerIndex"),
)
if mibBuilder.loadTexts:
    bRadiusProxyServerAcctEntry.setStatus("current")
_BRadiusProxyAcctStatsInterval_Type = Integer32
_BRadiusProxyAcctStatsInterval_Object = MibTableColumn
bRadiusProxyAcctStatsInterval = _BRadiusProxyAcctStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 1),
    _BRadiusProxyAcctStatsInterval_Type()
)
bRadiusProxyAcctStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusProxyAcctStatsInterval.setStatus("current")
_BRadiusProxyAcctServerIndex_Type = Integer32
_BRadiusProxyAcctServerIndex_Object = MibTableColumn
bRadiusProxyAcctServerIndex = _BRadiusProxyAcctServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 2),
    _BRadiusProxyAcctServerIndex_Type()
)
bRadiusProxyAcctServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusProxyAcctServerIndex.setStatus("current")
_BRadiusProxyAcctServerInetAddressType_Type = InetAddressType
_BRadiusProxyAcctServerInetAddressType_Object = MibTableColumn
bRadiusProxyAcctServerInetAddressType = _BRadiusProxyAcctServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 3),
    _BRadiusProxyAcctServerInetAddressType_Type()
)
bRadiusProxyAcctServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctServerInetAddressType.setStatus("current")
_BRadiusProxyAcctServerInetAddress_Type = InetAddress
_BRadiusProxyAcctServerInetAddress_Object = MibTableColumn
bRadiusProxyAcctServerInetAddress = _BRadiusProxyAcctServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 4),
    _BRadiusProxyAcctServerInetAddress_Type()
)
bRadiusProxyAcctServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctServerInetAddress.setStatus("current")
_BRadiusProxyAcctIntervalDuration_Type = Integer32
_BRadiusProxyAcctIntervalDuration_Object = MibTableColumn
bRadiusProxyAcctIntervalDuration = _BRadiusProxyAcctIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 5),
    _BRadiusProxyAcctIntervalDuration_Type()
)
bRadiusProxyAcctIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctIntervalDuration.setStatus("current")
_BRadiusProxyAcctRequestRcvd_Type = Unsigned32
_BRadiusProxyAcctRequestRcvd_Object = MibTableColumn
bRadiusProxyAcctRequestRcvd = _BRadiusProxyAcctRequestRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 6),
    _BRadiusProxyAcctRequestRcvd_Type()
)
bRadiusProxyAcctRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctRequestRcvd.setStatus("current")
_BRadiusProxyAcctRequestSent_Type = Unsigned32
_BRadiusProxyAcctRequestSent_Object = MibTableColumn
bRadiusProxyAcctRequestSent = _BRadiusProxyAcctRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 7),
    _BRadiusProxyAcctRequestSent_Type()
)
bRadiusProxyAcctRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctRequestSent.setStatus("current")
_BRadiusProxyAcctStartRequestRcvd_Type = Unsigned32
_BRadiusProxyAcctStartRequestRcvd_Object = MibTableColumn
bRadiusProxyAcctStartRequestRcvd = _BRadiusProxyAcctStartRequestRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 8),
    _BRadiusProxyAcctStartRequestRcvd_Type()
)
bRadiusProxyAcctStartRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctStartRequestRcvd.setStatus("current")
_BRadiusProxyAcctStopRequestRcvd_Type = Unsigned32
_BRadiusProxyAcctStopRequestRcvd_Object = MibTableColumn
bRadiusProxyAcctStopRequestRcvd = _BRadiusProxyAcctStopRequestRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 9),
    _BRadiusProxyAcctStopRequestRcvd_Type()
)
bRadiusProxyAcctStopRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctStopRequestRcvd.setStatus("current")
_BRadiusProxyAcctInterimUpdateRcvd_Type = Unsigned32
_BRadiusProxyAcctInterimUpdateRcvd_Object = MibTableColumn
bRadiusProxyAcctInterimUpdateRcvd = _BRadiusProxyAcctInterimUpdateRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 10),
    _BRadiusProxyAcctInterimUpdateRcvd_Type()
)
bRadiusProxyAcctInterimUpdateRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctInterimUpdateRcvd.setStatus("current")
_BRadiusProxyAcctStartRequestSent_Type = Unsigned32
_BRadiusProxyAcctStartRequestSent_Object = MibTableColumn
bRadiusProxyAcctStartRequestSent = _BRadiusProxyAcctStartRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 11),
    _BRadiusProxyAcctStartRequestSent_Type()
)
bRadiusProxyAcctStartRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctStartRequestSent.setStatus("current")
_BRadiusProxyAcctStopRequestSent_Type = Unsigned32
_BRadiusProxyAcctStopRequestSent_Object = MibTableColumn
bRadiusProxyAcctStopRequestSent = _BRadiusProxyAcctStopRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 12),
    _BRadiusProxyAcctStopRequestSent_Type()
)
bRadiusProxyAcctStopRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctStopRequestSent.setStatus("current")
_BRadiusProxyAcctInterimUpdateSent_Type = Unsigned32
_BRadiusProxyAcctInterimUpdateSent_Object = MibTableColumn
bRadiusProxyAcctInterimUpdateSent = _BRadiusProxyAcctInterimUpdateSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 13),
    _BRadiusProxyAcctInterimUpdateSent_Type()
)
bRadiusProxyAcctInterimUpdateSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctInterimUpdateSent.setStatus("current")
_BRadiusProxyAcctResponseRcvd_Type = Unsigned32
_BRadiusProxyAcctResponseRcvd_Object = MibTableColumn
bRadiusProxyAcctResponseRcvd = _BRadiusProxyAcctResponseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 14),
    _BRadiusProxyAcctResponseRcvd_Type()
)
bRadiusProxyAcctResponseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctResponseRcvd.setStatus("current")
_BRadiusProxyAcctResponseSent_Type = Unsigned32
_BRadiusProxyAcctResponseSent_Object = MibTableColumn
bRadiusProxyAcctResponseSent = _BRadiusProxyAcctResponseSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 2, 1, 15),
    _BRadiusProxyAcctResponseSent_Type()
)
bRadiusProxyAcctResponseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAcctResponseSent.setStatus("current")
_BRadiusProxyAuthTPSTable_Object = MibTable
bRadiusProxyAuthTPSTable = _BRadiusProxyAuthTPSTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSTable.setStatus("current")
_BRadiusProxyAuthTPSEntry_Object = MibTableRow
bRadiusProxyAuthTPSEntry = _BRadiusProxyAuthTPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1)
)
bRadiusProxyAuthTPSEntry.setIndexNames(
    (0, "BENU-RADIUS-MIB", "bRadiusProxyAuthTPSInterval"),
)
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSEntry.setStatus("current")
_BRadiusProxyAuthTPSInterval_Type = Integer32
_BRadiusProxyAuthTPSInterval_Object = MibTableColumn
bRadiusProxyAuthTPSInterval = _BRadiusProxyAuthTPSInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1, 1),
    _BRadiusProxyAuthTPSInterval_Type()
)
bRadiusProxyAuthTPSInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSInterval.setStatus("current")
_BRadiusProxyAuthTPSIntervalDuration_Type = Unsigned32
_BRadiusProxyAuthTPSIntervalDuration_Object = MibTableColumn
bRadiusProxyAuthTPSIntervalDuration = _BRadiusProxyAuthTPSIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1, 2),
    _BRadiusProxyAuthTPSIntervalDuration_Type()
)
bRadiusProxyAuthTPSIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSIntervalDuration.setStatus("current")
_BRadiusProxyAuthTPSLow_Type = Unsigned32
_BRadiusProxyAuthTPSLow_Object = MibTableColumn
bRadiusProxyAuthTPSLow = _BRadiusProxyAuthTPSLow_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1, 3),
    _BRadiusProxyAuthTPSLow_Type()
)
bRadiusProxyAuthTPSLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSLow.setStatus("current")
_BRadiusProxyAuthTPSHigh_Type = Unsigned32
_BRadiusProxyAuthTPSHigh_Object = MibTableColumn
bRadiusProxyAuthTPSHigh = _BRadiusProxyAuthTPSHigh_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1, 4),
    _BRadiusProxyAuthTPSHigh_Type()
)
bRadiusProxyAuthTPSHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSHigh.setStatus("current")
_BRadiusProxyAuthTPS_Type = Unsigned32
_BRadiusProxyAuthTPS_Object = MibTableColumn
bRadiusProxyAuthTPS = _BRadiusProxyAuthTPS_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 3, 3, 1, 5),
    _BRadiusProxyAuthTPS_Type()
)
bRadiusProxyAuthTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPS.setStatus("current")
_BRadiusProxyNotifObjects_ObjectIdentity = ObjectIdentity
bRadiusProxyNotifObjects = _BRadiusProxyNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    bRadiusProxyNotifObjects.setStatus("current")

# Managed Objects groups


# Notification objects

bAAAGroupOutstandingAuthReqsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 1)
)
bAAAGroupOutstandingAuthReqsLow.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupAuthName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingAuthReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingAuthReqsLowThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAuthReqsLow.setStatus(
        "current"
    )

bAAAGroupOutstandingAuthReqsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 2)
)
bAAAGroupOutstandingAuthReqsHigh.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupAuthName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingAuthReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingAuthReqsHighThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAuthReqsHigh.setStatus(
        "current"
    )

bAAAGroupOutstandingAcctReqsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 3)
)
bAAAGroupOutstandingAcctReqsLow.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupAcctName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingAcctReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingAcctReqsLowThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAcctReqsLow.setStatus(
        "current"
    )

bAAAGroupOutstandingAcctReqsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 4)
)
bAAAGroupOutstandingAcctReqsHigh.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupAcctName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingAcctReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingAcctReqsHighThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingAcctReqsHigh.setStatus(
        "current"
    )

bAAAGroupOutstandingCoAReqsLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 5)
)
bAAAGroupOutstandingCoAReqsLow.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupCoAName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingCoAReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingCoAReqsLowThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingCoAReqsLow.setStatus(
        "current"
    )

bAAAGroupOutstandingCoAReqsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 6)
)
bAAAGroupOutstandingCoAReqsHigh.setObjects(
      *(("BENU-RADIUS-MIB", "bAAAGroupCoAName"),
        ("BENU-RADIUS-MIB", "bAAAGroupMaximumOutstandingCoAReqs"),
        ("BENU-RADIUS-MIB", "bAAAGroupOutstandingCoAReqsHighThreshold"))
)
if mibBuilder.loadTexts:
    bAAAGroupOutstandingCoAReqsHigh.setStatus(
        "current"
    )

bRadiusAuthServerMarkedDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 7)
)
bRadiusAuthServerMarkedDead.setObjects(
      *(("BENU-RADIUS-MIB", "bRadiusServerIPAddrType"),
        ("BENU-RADIUS-MIB", "bRadiusServerIPAddress"))
)
if mibBuilder.loadTexts:
    bRadiusAuthServerMarkedDead.setStatus(
        "current"
    )

bRadiusAuthServerMarkedAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 8)
)
bRadiusAuthServerMarkedAlive.setObjects(
      *(("BENU-RADIUS-MIB", "bRadiusServerIPAddrType"),
        ("BENU-RADIUS-MIB", "bRadiusServerIPAddress"))
)
if mibBuilder.loadTexts:
    bRadiusAuthServerMarkedAlive.setStatus(
        "current"
    )

bRadiusAccountingServerMarkedDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 9)
)
bRadiusAccountingServerMarkedDead.setObjects(
      *(("BENU-RADIUS-MIB", "bRadiusServerIPAddrType"),
        ("BENU-RADIUS-MIB", "bRadiusServerIPAddress"))
)
if mibBuilder.loadTexts:
    bRadiusAccountingServerMarkedDead.setStatus(
        "current"
    )

bRadiusAccountingServerMarkedAlive = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 10)
)
bRadiusAccountingServerMarkedAlive.setObjects(
      *(("BENU-RADIUS-MIB", "bRadiusServerIPAddrType"),
        ("BENU-RADIUS-MIB", "bRadiusServerIPAddress"))
)
if mibBuilder.loadTexts:
    bRadiusAccountingServerMarkedAlive.setStatus(
        "current"
    )

bRadiusProxyAuthTPSLowReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 11)
)
bRadiusProxyAuthTPSLowReached.setObjects(
    ("BENU-RADIUS-MIB", "bRadiusProxyAuthTPS")
)
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSLowReached.setStatus(
        "current"
    )

bRadiusProxyAuthTPSHighReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 4, 0, 12)
)
bRadiusProxyAuthTPSHighReached.setObjects(
    ("BENU-RADIUS-MIB", "bRadiusProxyAuthTPS")
)
if mibBuilder.loadTexts:
    bRadiusProxyAuthTPSHighReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-RADIUS-MIB",
    **{"BenuRadiusInstance": BenuRadiusInstance,
       "benuRadiusMIB": benuRadiusMIB,
       "bRadiusNotifications": bRadiusNotifications,
       "bAAAGroupOutstandingAuthReqsLow": bAAAGroupOutstandingAuthReqsLow,
       "bAAAGroupOutstandingAuthReqsHigh": bAAAGroupOutstandingAuthReqsHigh,
       "bAAAGroupOutstandingAcctReqsLow": bAAAGroupOutstandingAcctReqsLow,
       "bAAAGroupOutstandingAcctReqsHigh": bAAAGroupOutstandingAcctReqsHigh,
       "bAAAGroupOutstandingCoAReqsLow": bAAAGroupOutstandingCoAReqsLow,
       "bAAAGroupOutstandingCoAReqsHigh": bAAAGroupOutstandingCoAReqsHigh,
       "bRadiusAuthServerMarkedDead": bRadiusAuthServerMarkedDead,
       "bRadiusAuthServerMarkedAlive": bRadiusAuthServerMarkedAlive,
       "bRadiusAccountingServerMarkedDead": bRadiusAccountingServerMarkedDead,
       "bRadiusAccountingServerMarkedAlive": bRadiusAccountingServerMarkedAlive,
       "bRadiusProxyAuthTPSLowReached": bRadiusProxyAuthTPSLowReached,
       "bRadiusProxyAuthTPSHighReached": bRadiusProxyAuthTPSHighReached,
       "bRadiusMIBObjects": bRadiusMIBObjects,
       "bRadiusServerAuthTable": bRadiusServerAuthTable,
       "bRadiusServerAuthEntry": bRadiusServerAuthEntry,
       "bRadiusAuthStatsInterval": bRadiusAuthStatsInterval,
       "bRadiusAuthServerIndex": bRadiusAuthServerIndex,
       "bRadiusAuthServerInetAddressType": bRadiusAuthServerInetAddressType,
       "bRadiusAuthServerInetAddress": bRadiusAuthServerInetAddress,
       "bRadiusAuthIntervalDuration": bRadiusAuthIntervalDuration,
       "bRadiusAccessRequestSent": bRadiusAccessRequestSent,
       "bRadiusAccessAcceptReceived": bRadiusAccessAcceptReceived,
       "bRadiusAccessRejectReceived": bRadiusAccessRejectReceived,
       "bRadiusAccessChallengeReceived": bRadiusAccessChallengeReceived,
       "bRadiusAccessRequestResent": bRadiusAccessRequestResent,
       "bRadiusAccessRequestDropped": bRadiusAccessRequestDropped,
       "bRadiusAccessRequestTimedOut": bRadiusAccessRequestTimedOut,
       "bRadiusAccessRequestSentFail": bRadiusAccessRequestSentFail,
       "bRadiusAccessPeakRequestPending": bRadiusAccessPeakRequestPending,
       "bRadiusAccessMalformedRespDropped": bRadiusAccessMalformedRespDropped,
       "bRadiusAccessBadAuthenticatorRcvd": bRadiusAccessBadAuthenticatorRcvd,
       "bRadiusAccessServerMarkedDead": bRadiusAccessServerMarkedDead,
       "bRadiusAuthLatencyMin": bRadiusAuthLatencyMin,
       "bRadiusAuthLatencyMax": bRadiusAuthLatencyMax,
       "bRadiusAuthLatencyAvg": bRadiusAuthLatencyAvg,
       "bRadiusAuthLatencyLast": bRadiusAuthLatencyLast,
       "bRadiusAuthAAAGroupName": bRadiusAuthAAAGroupName,
       "bRadiusServerAcctTable": bRadiusServerAcctTable,
       "bRadiusServerAcctEntry": bRadiusServerAcctEntry,
       "bRadiusAcctStatsInterval": bRadiusAcctStatsInterval,
       "bRadiusAcctServerIndex": bRadiusAcctServerIndex,
       "bRadiusAcctServerInetAddressType": bRadiusAcctServerInetAddressType,
       "bRadiusAcctServerInetAddress": bRadiusAcctServerInetAddress,
       "bRadiusAcctIntervalDuration": bRadiusAcctIntervalDuration,
       "bRadiusAcctRequestSent": bRadiusAcctRequestSent,
       "bRadiusAcctStartRequestSent": bRadiusAcctStartRequestSent,
       "bRadiusAcctStopRequestSent": bRadiusAcctStopRequestSent,
       "bRadiusAcctInterimUpdateSent": bRadiusAcctInterimUpdateSent,
       "bRadiusAcctResponseReceived": bRadiusAcctResponseReceived,
       "bRadiusAcctRequestResent": bRadiusAcctRequestResent,
       "bRadiusAcctRequestDropped": bRadiusAcctRequestDropped,
       "bRadiusAcctRequestTimedOut": bRadiusAcctRequestTimedOut,
       "bRadiusAcctRequestSentFail": bRadiusAcctRequestSentFail,
       "bRadiusAcctPeakRequestPending": bRadiusAcctPeakRequestPending,
       "bRadiusAcctMalformedRespDropped": bRadiusAcctMalformedRespDropped,
       "bRadiusAcctBadAuthenticatorRcvd": bRadiusAcctBadAuthenticatorRcvd,
       "bRadiusAcctServerMarkedDead": bRadiusAcctServerMarkedDead,
       "bRadiusAcctLatencyMin": bRadiusAcctLatencyMin,
       "bRadiusAcctLatencyMax": bRadiusAcctLatencyMax,
       "bRadiusAcctLatencyAvg": bRadiusAcctLatencyAvg,
       "bRadiusAcctLatencyLast": bRadiusAcctLatencyLast,
       "bRadiusAcctAAAGroupName": bRadiusAcctAAAGroupName,
       "bRadiusClientCoATable": bRadiusClientCoATable,
       "bRadiusClientCoAEntry": bRadiusClientCoAEntry,
       "bRadiusCOAStatsInterval": bRadiusCOAStatsInterval,
       "bRadiusCoAClientIndex": bRadiusCoAClientIndex,
       "bRadiusCoAClientInetAddressType": bRadiusCoAClientInetAddressType,
       "bRadiusCoAClientInetAddress": bRadiusCoAClientInetAddress,
       "bRadiusCoAIntervalDuration": bRadiusCoAIntervalDuration,
       "bRadiusCoAAckSent": bRadiusCoAAckSent,
       "bRadiusCoANackSent": bRadiusCoANackSent,
       "bRadiusCoARequestReceived": bRadiusCoARequestReceived,
       "bRadiusCoARequestDropped": bRadiusCoARequestDropped,
       "bRadiusCoAReqDropDueToDupReq": bRadiusCoAReqDropDueToDupReq,
       "bRadiusCoAReqDropDueToInvalidTime": bRadiusCoAReqDropDueToInvalidTime,
       "bRadiusCoAReqDropDueToBadAuthenticator": bRadiusCoAReqDropDueToBadAuthenticator,
       "bRadiusCoANackDueToInvalidReq": bRadiusCoANackDueToInvalidReq,
       "bRadiusCoANackDueToExceedMaxOutstanding": bRadiusCoANackDueToExceedMaxOutstanding,
       "bRadiusDisconnectRequestReceived": bRadiusDisconnectRequestReceived,
       "bRadiusDisconnectAckSent": bRadiusDisconnectAckSent,
       "bRadiusDisconnectNackSent": bRadiusDisconnectNackSent,
       "bRadiusDisconnectRequestDropped": bRadiusDisconnectRequestDropped,
       "bRadiusDisconnectReqDropDueToDupReq": bRadiusDisconnectReqDropDueToDupReq,
       "bRadiusDisconnectReqDropDueToInvalidTime": bRadiusDisconnectReqDropDueToInvalidTime,
       "bRadiusDisconnectReqDropDueToBadAuthenticator": bRadiusDisconnectReqDropDueToBadAuthenticator,
       "bRadiusDisconnectNackDueToInvalidReq": bRadiusDisconnectNackDueToInvalidReq,
       "bRadiusDisconnectNackDueToExceedMaxOutstanding": bRadiusDisconnectNackDueToExceedMaxOutstanding,
       "bRadiusCoALatencyMin": bRadiusCoALatencyMin,
       "bRadiusCoALatencyMax": bRadiusCoALatencyMax,
       "bRadiusCoALatencyAvg": bRadiusCoALatencyAvg,
       "bRadiusCoALatencyLast": bRadiusCoALatencyLast,
       "bRadiusCoADMLatencyMin": bRadiusCoADMLatencyMin,
       "bRadiusCoADMLatencyMax": bRadiusCoADMLatencyMax,
       "bRadiusCoADMLatencyAvg": bRadiusCoADMLatencyAvg,
       "bRadiusCoADMLatencyLast": bRadiusCoADMLatencyLast,
       "bRadiusCoAAAAGroupName": bRadiusCoAAAAGroupName,
       "bAAAGroupAuthTable": bAAAGroupAuthTable,
       "bAAAGroupAuthEntry": bAAAGroupAuthEntry,
       "bAAAGroupAuthStatsInterval": bAAAGroupAuthStatsInterval,
       "bAAAGroupAuthIndex": bAAAGroupAuthIndex,
       "bAAAGroupAuthName": bAAAGroupAuthName,
       "bAAAGroupAuthIntervalDuration": bAAAGroupAuthIntervalDuration,
       "bAAAGroupMaximumOutstandingAuthReqs": bAAAGroupMaximumOutstandingAuthReqs,
       "bAAAGroupPeakOutstandingAuthReqsReached": bAAAGroupPeakOutstandingAuthReqsReached,
       "bAAAGroupAuthReqsDropped": bAAAGroupAuthReqsDropped,
       "bAAAGroupOutstandingAuthReqsHighThreshold": bAAAGroupOutstandingAuthReqsHighThreshold,
       "bAAAGroupOutstandingAuthReqsLowThreshold": bAAAGroupOutstandingAuthReqsLowThreshold,
       "bAAAGroupAuthCurrentOutstanding": bAAAGroupAuthCurrentOutstanding,
       "bAAAGroupAcctTable": bAAAGroupAcctTable,
       "bAAAGroupAcctEntry": bAAAGroupAcctEntry,
       "bAAAGroupAcctStatsInterval": bAAAGroupAcctStatsInterval,
       "bAAAGroupAcctIndex": bAAAGroupAcctIndex,
       "bAAAGroupAcctName": bAAAGroupAcctName,
       "bAAAGroupAcctIntervalDuration": bAAAGroupAcctIntervalDuration,
       "bAAAGroupMaximumOutstandingAcctReqs": bAAAGroupMaximumOutstandingAcctReqs,
       "bAAAGroupPeakOutstandingAcctReqsReached": bAAAGroupPeakOutstandingAcctReqsReached,
       "bAAAGroupAcctReqsDropped": bAAAGroupAcctReqsDropped,
       "bAAAGroupOutstandingAcctReqsHighThreshold": bAAAGroupOutstandingAcctReqsHighThreshold,
       "bAAAGroupOutstandingAcctReqsLowThreshold": bAAAGroupOutstandingAcctReqsLowThreshold,
       "bAAAGroupAcctCurrentOutstanding": bAAAGroupAcctCurrentOutstanding,
       "bAAAGroupCoATable": bAAAGroupCoATable,
       "bAAAGroupCoAEntry": bAAAGroupCoAEntry,
       "bAAAGroupCoAStatsInterval": bAAAGroupCoAStatsInterval,
       "bAAAGroupCoAIndex": bAAAGroupCoAIndex,
       "bAAAGroupCoAName": bAAAGroupCoAName,
       "bAAAGroupCoAIntervalDuration": bAAAGroupCoAIntervalDuration,
       "bAAAGroupCoANumOfClients": bAAAGroupCoANumOfClients,
       "bAAAGroupCoAReqsDropDueToInvalidClient": bAAAGroupCoAReqsDropDueToInvalidClient,
       "bAAAGroupDisconnectReqsDropDueToInvalidClient": bAAAGroupDisconnectReqsDropDueToInvalidClient,
       "bAAAGroupMaximumOutstandingCoAReqs": bAAAGroupMaximumOutstandingCoAReqs,
       "bAAAGroupPeakOutstandingCoAReqs": bAAAGroupPeakOutstandingCoAReqs,
       "bAAAGroupOutstandingCoAReqsHighThreshold": bAAAGroupOutstandingCoAReqsHighThreshold,
       "bAAAGroupOutstandingCoAReqsLowThreshold": bAAAGroupOutstandingCoAReqsLowThreshold,
       "bAAAGroupCoaCurrentOutstanding": bAAAGroupCoaCurrentOutstanding,
       "bRadiusLatencyAuthTable": bRadiusLatencyAuthTable,
       "bRadiusLatencyAuthEntry": bRadiusLatencyAuthEntry,
       "bRadiusAuthLatencyStatsInterval": bRadiusAuthLatencyStatsInterval,
       "bRadiusAuthInstanceIndex": bRadiusAuthInstanceIndex,
       "bRadiusAuthLatencyIntervalDuration": bRadiusAuthLatencyIntervalDuration,
       "bRadiusAuthRequestTotalPackets": bRadiusAuthRequestTotalPackets,
       "bRadiusAuthRequestMaximumProcessingTime": bRadiusAuthRequestMaximumProcessingTime,
       "bRadiusAuthRequestMinimumProcessingTime": bRadiusAuthRequestMinimumProcessingTime,
       "bRadiusAuthRequestAverageProcessingTime": bRadiusAuthRequestAverageProcessingTime,
       "bRadiusAuthRequestProcessingTimeGreaterthan1MS": bRadiusAuthRequestProcessingTimeGreaterthan1MS,
       "bRadiusAuthResponseTotalPackets": bRadiusAuthResponseTotalPackets,
       "bRadiusAuthResponseMaximumProcessingTime": bRadiusAuthResponseMaximumProcessingTime,
       "bRadiusAuthResponseMinimumProcessingTime": bRadiusAuthResponseMinimumProcessingTime,
       "bRadiusAuthResponseAverageProcessingTime": bRadiusAuthResponseAverageProcessingTime,
       "bRadiusAuthResponseProcessingTimeGreaterthan1MS": bRadiusAuthResponseProcessingTimeGreaterthan1MS,
       "bRadiusNotifObjects": bRadiusNotifObjects,
       "bRadiusServerIPAddrType": bRadiusServerIPAddrType,
       "bRadiusServerIPAddress": bRadiusServerIPAddress,
       "bRadiusProxyMIBObjects": bRadiusProxyMIBObjects,
       "bRadiusProxyServerAuthTable": bRadiusProxyServerAuthTable,
       "bRadiusProxyServerAuthEntry": bRadiusProxyServerAuthEntry,
       "bRadiusProxyAuthStatsInterval": bRadiusProxyAuthStatsInterval,
       "bRadiusProxyAuthServerIndex": bRadiusProxyAuthServerIndex,
       "bRadiusProxyAuthServerInetAddressType": bRadiusProxyAuthServerInetAddressType,
       "bRadiusProxyAuthServerInetAddress": bRadiusProxyAuthServerInetAddress,
       "bRadiusProxyAuthIntervalDuration": bRadiusProxyAuthIntervalDuration,
       "bRadiusProxyAccessRequestRcvd": bRadiusProxyAccessRequestRcvd,
       "bRadiusProxyAccessUnknownTypeRcvd": bRadiusProxyAccessUnknownTypeRcvd,
       "bRadiusProxyAccessUnknownClientRcvd": bRadiusProxyAccessUnknownClientRcvd,
       "bRadiusProxyAccessRequestDropped": bRadiusProxyAccessRequestDropped,
       "bRadiusProxyAccessSentFail": bRadiusProxyAccessSentFail,
       "bRadiusProxyAccessBadAuthenticatorRcvd": bRadiusProxyAccessBadAuthenticatorRcvd,
       "bRadiusProxyAccessAcceptRcvd": bRadiusProxyAccessAcceptRcvd,
       "bRadiusProxyAccessRejectRcvd": bRadiusProxyAccessRejectRcvd,
       "bRadiusProxyAccessChallengeRcvd": bRadiusProxyAccessChallengeRcvd,
       "bRadiusProxySubscriberBlocked": bRadiusProxySubscriberBlocked,
       "bRadiusProxySubscriberDeleted": bRadiusProxySubscriberDeleted,
       "bRadiusProxyServerAcctTable": bRadiusProxyServerAcctTable,
       "bRadiusProxyServerAcctEntry": bRadiusProxyServerAcctEntry,
       "bRadiusProxyAcctStatsInterval": bRadiusProxyAcctStatsInterval,
       "bRadiusProxyAcctServerIndex": bRadiusProxyAcctServerIndex,
       "bRadiusProxyAcctServerInetAddressType": bRadiusProxyAcctServerInetAddressType,
       "bRadiusProxyAcctServerInetAddress": bRadiusProxyAcctServerInetAddress,
       "bRadiusProxyAcctIntervalDuration": bRadiusProxyAcctIntervalDuration,
       "bRadiusProxyAcctRequestRcvd": bRadiusProxyAcctRequestRcvd,
       "bRadiusProxyAcctRequestSent": bRadiusProxyAcctRequestSent,
       "bRadiusProxyAcctStartRequestRcvd": bRadiusProxyAcctStartRequestRcvd,
       "bRadiusProxyAcctStopRequestRcvd": bRadiusProxyAcctStopRequestRcvd,
       "bRadiusProxyAcctInterimUpdateRcvd": bRadiusProxyAcctInterimUpdateRcvd,
       "bRadiusProxyAcctStartRequestSent": bRadiusProxyAcctStartRequestSent,
       "bRadiusProxyAcctStopRequestSent": bRadiusProxyAcctStopRequestSent,
       "bRadiusProxyAcctInterimUpdateSent": bRadiusProxyAcctInterimUpdateSent,
       "bRadiusProxyAcctResponseRcvd": bRadiusProxyAcctResponseRcvd,
       "bRadiusProxyAcctResponseSent": bRadiusProxyAcctResponseSent,
       "bRadiusProxyAuthTPSTable": bRadiusProxyAuthTPSTable,
       "bRadiusProxyAuthTPSEntry": bRadiusProxyAuthTPSEntry,
       "bRadiusProxyAuthTPSInterval": bRadiusProxyAuthTPSInterval,
       "bRadiusProxyAuthTPSIntervalDuration": bRadiusProxyAuthTPSIntervalDuration,
       "bRadiusProxyAuthTPSLow": bRadiusProxyAuthTPSLow,
       "bRadiusProxyAuthTPSHigh": bRadiusProxyAuthTPSHigh,
       "bRadiusProxyAuthTPS": bRadiusProxyAuthTPS,
       "bRadiusProxyNotifObjects": bRadiusProxyNotifObjects}
)
