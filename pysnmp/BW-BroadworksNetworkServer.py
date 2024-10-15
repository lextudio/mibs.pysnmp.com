# SNMP MIB module (BW-BroadworksNetworkServer) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-BroadworksNetworkServer
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:04 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2000-09-19 14:31",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_NsExecutionServer_ObjectIdentity = ObjectIdentity
nsExecutionServer = _NsExecutionServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1)
)
_Licensing_ObjectIdentity = ObjectIdentity
licensing = _Licensing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11)
)
_BwNbTimePeriodWithLicenseViolations_Type = Counter32
_BwNbTimePeriodWithLicenseViolations_Object = MibScalar
bwNbTimePeriodWithLicenseViolations = _BwNbTimePeriodWithLicenseViolations_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 1),
    _BwNbTimePeriodWithLicenseViolations_Type()
)
bwNbTimePeriodWithLicenseViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbTimePeriodWithLicenseViolations.setStatus("current")
_BwNbTransactionInViolation_Type = Counter32
_BwNbTransactionInViolation_Object = MibScalar
bwNbTransactionInViolation = _BwNbTransactionInViolation_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 2),
    _BwNbTransactionInViolation_Type()
)
bwNbTransactionInViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbTransactionInViolation.setStatus("current")
_BwNbThresholdAlarmSent_Type = Counter32
_BwNbThresholdAlarmSent_Object = MibScalar
bwNbThresholdAlarmSent = _BwNbThresholdAlarmSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 3),
    _BwNbThresholdAlarmSent_Type()
)
bwNbThresholdAlarmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbThresholdAlarmSent.setStatus("current")
_BwNbNonInviteTimePeriodWithLicenseViolations_Type = Counter32
_BwNbNonInviteTimePeriodWithLicenseViolations_Object = MibScalar
bwNbNonInviteTimePeriodWithLicenseViolations = _BwNbNonInviteTimePeriodWithLicenseViolations_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 4),
    _BwNbNonInviteTimePeriodWithLicenseViolations_Type()
)
bwNbNonInviteTimePeriodWithLicenseViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbNonInviteTimePeriodWithLicenseViolations.setStatus("current")
_BwNbNonInviteTransactionInViolation_Type = Counter32
_BwNbNonInviteTransactionInViolation_Object = MibScalar
bwNbNonInviteTransactionInViolation = _BwNbNonInviteTransactionInViolation_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 5),
    _BwNbNonInviteTransactionInViolation_Type()
)
bwNbNonInviteTransactionInViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbNonInviteTransactionInViolation.setStatus("current")
_BwNbNonInviteThresholdAlarmSent_Type = Counter32
_BwNbNonInviteThresholdAlarmSent_Object = MibScalar
bwNbNonInviteThresholdAlarmSent = _BwNbNonInviteThresholdAlarmSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 11, 6),
    _BwNbNonInviteThresholdAlarmSent_Type()
)
bwNbNonInviteThresholdAlarmSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNbNonInviteThresholdAlarmSent.setStatus("current")
_InternalStats_ObjectIdentity = ObjectIdentity
internalStats = _InternalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12)
)
_BwNSSystemInternalQueueResets_Type = Counter32
_BwNSSystemInternalQueueResets_Object = MibScalar
bwNSSystemInternalQueueResets = _BwNSSystemInternalQueueResets_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 1),
    _BwNSSystemInternalQueueResets_Type()
)
bwNSSystemInternalQueueResets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueResets.setStatus("current")
_BwNSSystemInternalQueueTable_Object = MibTable
bwNSSystemInternalQueueTable = _BwNSSystemInternalQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2)
)
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTable.setStatus("current")
_BwNSSystemInternalQueueEntry_Object = MibTableRow
bwNSSystemInternalQueueEntry = _BwNSSystemInternalQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1)
)
bwNSSystemInternalQueueEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSystemInternalQueueIndex"),
)
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueEntry.setStatus("current")
_BwNSSystemInternalQueueIndex_Type = Unsigned32
_BwNSSystemInternalQueueIndex_Object = MibTableColumn
bwNSSystemInternalQueueIndex = _BwNSSystemInternalQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 1),
    _BwNSSystemInternalQueueIndex_Type()
)
bwNSSystemInternalQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueIndex.setStatus("current")
_BwNSSystemInternalQueueName_Type = DisplayString
_BwNSSystemInternalQueueName_Object = MibTableColumn
bwNSSystemInternalQueueName = _BwNSSystemInternalQueueName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 2),
    _BwNSSystemInternalQueueName_Type()
)
bwNSSystemInternalQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueName.setStatus("current")
_BwNSSystemInternalQueueSize_Type = Counter32
_BwNSSystemInternalQueueSize_Object = MibTableColumn
bwNSSystemInternalQueueSize = _BwNSSystemInternalQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 3),
    _BwNSSystemInternalQueueSize_Type()
)
bwNSSystemInternalQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueSize.setStatus("current")
_BwNSSystemInternalQueueTimeAvg_Type = Gauge32
_BwNSSystemInternalQueueTimeAvg_Object = MibTableColumn
bwNSSystemInternalQueueTimeAvg = _BwNSSystemInternalQueueTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 4),
    _BwNSSystemInternalQueueTimeAvg_Type()
)
bwNSSystemInternalQueueTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeAvg.setStatus("current")
_BwNSSystemInternalQueueTimeMin_Type = Gauge32
_BwNSSystemInternalQueueTimeMin_Object = MibTableColumn
bwNSSystemInternalQueueTimeMin = _BwNSSystemInternalQueueTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 5),
    _BwNSSystemInternalQueueTimeMin_Type()
)
bwNSSystemInternalQueueTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeMin.setStatus("current")
_BwNSSystemInternalQueueTimeMax_Type = Gauge32
_BwNSSystemInternalQueueTimeMax_Object = MibTableColumn
bwNSSystemInternalQueueTimeMax = _BwNSSystemInternalQueueTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 6),
    _BwNSSystemInternalQueueTimeMax_Type()
)
bwNSSystemInternalQueueTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeMax.setStatus("current")
_BwNSSystemInternalQueueTimeMaxTimestamp_Type = Gauge32
_BwNSSystemInternalQueueTimeMaxTimestamp_Object = MibScalar
bwNSSystemInternalQueueTimeMaxTimestamp = _BwNSSystemInternalQueueTimeMaxTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 7),
    _BwNSSystemInternalQueueTimeMaxTimestamp_Type()
)
bwNSSystemInternalQueueTimeMaxTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeMaxTimestamp.setStatus("obsolete")
_BwNSSystemInternalQueueLengthCurrent_Type = Gauge32
_BwNSSystemInternalQueueLengthCurrent_Object = MibTableColumn
bwNSSystemInternalQueueLengthCurrent = _BwNSSystemInternalQueueLengthCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 8),
    _BwNSSystemInternalQueueLengthCurrent_Type()
)
bwNSSystemInternalQueueLengthCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthCurrent.setStatus("current")
_BwNSSystemInternalQueueLengthAvg_Type = Gauge32
_BwNSSystemInternalQueueLengthAvg_Object = MibTableColumn
bwNSSystemInternalQueueLengthAvg = _BwNSSystemInternalQueueLengthAvg_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 9),
    _BwNSSystemInternalQueueLengthAvg_Type()
)
bwNSSystemInternalQueueLengthAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthAvg.setStatus("current")
_BwNSSystemInternalQueueLengthMax_Type = Gauge32
_BwNSSystemInternalQueueLengthMax_Object = MibTableColumn
bwNSSystemInternalQueueLengthMax = _BwNSSystemInternalQueueLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 10),
    _BwNSSystemInternalQueueLengthMax_Type()
)
bwNSSystemInternalQueueLengthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthMax.setStatus("current")
_BwNSSystemInternalQueueLengthMaxTimestamp_Type = Gauge32
_BwNSSystemInternalQueueLengthMaxTimestamp_Object = MibScalar
bwNSSystemInternalQueueLengthMaxTimestamp = _BwNSSystemInternalQueueLengthMaxTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 11),
    _BwNSSystemInternalQueueLengthMaxTimestamp_Type()
)
bwNSSystemInternalQueueLengthMaxTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthMaxTimestamp.setStatus("obsolete")
_BwNSSystemInternalQueueTimeMaxTimestampMSB_Type = Gauge32
_BwNSSystemInternalQueueTimeMaxTimestampMSB_Object = MibTableColumn
bwNSSystemInternalQueueTimeMaxTimestampMSB = _BwNSSystemInternalQueueTimeMaxTimestampMSB_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 12),
    _BwNSSystemInternalQueueTimeMaxTimestampMSB_Type()
)
bwNSSystemInternalQueueTimeMaxTimestampMSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeMaxTimestampMSB.setStatus("current")
_BwNSSystemInternalQueueLengthMaxTimestampMSB_Type = Gauge32
_BwNSSystemInternalQueueLengthMaxTimestampMSB_Object = MibTableColumn
bwNSSystemInternalQueueLengthMaxTimestampMSB = _BwNSSystemInternalQueueLengthMaxTimestampMSB_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 13),
    _BwNSSystemInternalQueueLengthMaxTimestampMSB_Type()
)
bwNSSystemInternalQueueLengthMaxTimestampMSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthMaxTimestampMSB.setStatus("current")
_BwNSSystemInternalQueueLengthMaxTimestampLSB_Type = Gauge32
_BwNSSystemInternalQueueLengthMaxTimestampLSB_Object = MibTableColumn
bwNSSystemInternalQueueLengthMaxTimestampLSB = _BwNSSystemInternalQueueLengthMaxTimestampLSB_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 14),
    _BwNSSystemInternalQueueLengthMaxTimestampLSB_Type()
)
bwNSSystemInternalQueueLengthMaxTimestampLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueLengthMaxTimestampLSB.setStatus("current")
_BwNSSystemInternalQueueTimeMaxTimestampLSB_Type = Gauge32
_BwNSSystemInternalQueueTimeMaxTimestampLSB_Object = MibTableColumn
bwNSSystemInternalQueueTimeMaxTimestampLSB = _BwNSSystemInternalQueueTimeMaxTimestampLSB_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 12, 2, 1, 15),
    _BwNSSystemInternalQueueTimeMaxTimestampLSB_Type()
)
bwNSSystemInternalQueueTimeMaxTimestampLSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSystemInternalQueueTimeMaxTimestampLSB.setStatus("current")
_OverloadStats_ObjectIdentity = ObjectIdentity
overloadStats = _OverloadStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13)
)
_BwNSCurrentCallOverloadZone_Type = DisplayString
_BwNSCurrentCallOverloadZone_Object = MibScalar
bwNSCurrentCallOverloadZone = _BwNSCurrentCallOverloadZone_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 1),
    _BwNSCurrentCallOverloadZone_Type()
)
bwNSCurrentCallOverloadZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCurrentCallOverloadZone.setStatus("current")
_BwNSNumCallYellowZoneOverloadTrans_Type = Counter32
_BwNSNumCallYellowZoneOverloadTrans_Object = MibScalar
bwNSNumCallYellowZoneOverloadTrans = _BwNSNumCallYellowZoneOverloadTrans_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 2),
    _BwNSNumCallYellowZoneOverloadTrans_Type()
)
bwNSNumCallYellowZoneOverloadTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNumCallYellowZoneOverloadTrans.setStatus("current")
_BwNSNumCallRedZoneOverloadTrans_Type = Counter32
_BwNSNumCallRedZoneOverloadTrans_Object = MibScalar
bwNSNumCallRedZoneOverloadTrans = _BwNSNumCallRedZoneOverloadTrans_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 3),
    _BwNSNumCallRedZoneOverloadTrans_Type()
)
bwNSNumCallRedZoneOverloadTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNumCallRedZoneOverloadTrans.setStatus("current")
_BwNSCurrentNonCallOverloadZone_Type = DisplayString
_BwNSCurrentNonCallOverloadZone_Object = MibScalar
bwNSCurrentNonCallOverloadZone = _BwNSCurrentNonCallOverloadZone_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 4),
    _BwNSCurrentNonCallOverloadZone_Type()
)
bwNSCurrentNonCallOverloadZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCurrentNonCallOverloadZone.setStatus("current")
_BwNSNumNonCallYellowZoneOverloadTrans_Type = Counter32
_BwNSNumNonCallYellowZoneOverloadTrans_Object = MibScalar
bwNSNumNonCallYellowZoneOverloadTrans = _BwNSNumNonCallYellowZoneOverloadTrans_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 5),
    _BwNSNumNonCallYellowZoneOverloadTrans_Type()
)
bwNSNumNonCallYellowZoneOverloadTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNumNonCallYellowZoneOverloadTrans.setStatus("current")
_BwNSNumNonCallRedZoneOverloadTrans_Type = Counter32
_BwNSNumNonCallRedZoneOverloadTrans_Object = MibScalar
bwNSNumNonCallRedZoneOverloadTrans = _BwNSNumNonCallRedZoneOverloadTrans_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 6),
    _BwNSNumNonCallRedZoneOverloadTrans_Type()
)
bwNSNumNonCallRedZoneOverloadTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNumNonCallRedZoneOverloadTrans.setStatus("current")
_BwNSNumDiscardedMessage_Type = Counter32
_BwNSNumDiscardedMessage_Object = MibScalar
bwNSNumDiscardedMessage = _BwNSNumDiscardedMessage_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 7),
    _BwNSNumDiscardedMessage_Type()
)
bwNSNumDiscardedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNumDiscardedMessage.setStatus("current")
_BwNSTimeLastDiscardedMessage_Type = DisplayString
_BwNSTimeLastDiscardedMessage_Object = MibScalar
bwNSTimeLastDiscardedMessage = _BwNSTimeLastDiscardedMessage_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 1, 13, 8),
    _BwNSTimeLastDiscardedMessage_Type()
)
bwNSTimeLastDiscardedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSTimeLastDiscardedMessage.setStatus("current")
_Processing_ObjectIdentity = ObjectIdentity
processing = _Processing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2)
)
_Policies_ObjectIdentity = ObjectIdentity
policies = _Policies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3)
)
_PublicPolicyStatTable_Object = MibTable
publicPolicyStatTable = _PublicPolicyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1)
)
if mibBuilder.loadTexts:
    publicPolicyStatTable.setStatus("current")
_PublicPolicyStatEntry_Object = MibTableRow
publicPolicyStatEntry = _PublicPolicyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1)
)
publicPolicyStatEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "pubPolStatID"),
)
if mibBuilder.loadTexts:
    publicPolicyStatEntry.setStatus("current")
_PubPolStatID_Type = Unsigned32
_PubPolStatID_Object = MibTableColumn
pubPolStatID = _PubPolStatID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 1),
    _PubPolStatID_Type()
)
pubPolStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pubPolStatID.setStatus("current")
_PubPolStatPolicyName_Type = DisplayString
_PubPolStatPolicyName_Object = MibTableColumn
pubPolStatPolicyName = _PubPolStatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 2),
    _PubPolStatPolicyName_Type()
)
pubPolStatPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pubPolStatPolicyName.setStatus("current")
_PubPolStatNbInstances_Type = Gauge32
_PubPolStatNbInstances_Object = MibTableColumn
pubPolStatNbInstances = _PubPolStatNbInstances_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 3),
    _PubPolStatNbInstances_Type()
)
pubPolStatNbInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pubPolStatNbInstances.setStatus("current")
_PubPolStatNbRequests_Type = Counter32
_PubPolStatNbRequests_Object = MibTableColumn
pubPolStatNbRequests = _PubPolStatNbRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 4),
    _PubPolStatNbRequests_Type()
)
pubPolStatNbRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pubPolStatNbRequests.setStatus("current")
_PubPolStatNbRequestsFailures_Type = Counter32
_PubPolStatNbRequestsFailures_Object = MibTableColumn
pubPolStatNbRequestsFailures = _PubPolStatNbRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 5),
    _PubPolStatNbRequestsFailures_Type()
)
pubPolStatNbRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pubPolStatNbRequestsFailures.setStatus("current")
_PubPolStatNbRequestsResults_Type = Counter32
_PubPolStatNbRequestsResults_Object = MibTableColumn
pubPolStatNbRequestsResults = _PubPolStatNbRequestsResults_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 1, 1, 6),
    _PubPolStatNbRequestsResults_Type()
)
pubPolStatNbRequestsResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pubPolStatNbRequestsResults.setStatus("current")
_PrivatePolicyStatTable_Object = MibTable
privatePolicyStatTable = _PrivatePolicyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    privatePolicyStatTable.setStatus("current")
_PrivatePolicyStatEntry_Object = MibTableRow
privatePolicyStatEntry = _PrivatePolicyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1)
)
privatePolicyStatEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "privPolStatID"),
)
if mibBuilder.loadTexts:
    privatePolicyStatEntry.setStatus("current")
_PrivPolStatID_Type = Unsigned32
_PrivPolStatID_Object = MibTableColumn
privPolStatID = _PrivPolStatID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 1),
    _PrivPolStatID_Type()
)
privPolStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privPolStatID.setStatus("current")
_PrivPolStatEnterpriseName_Type = DisplayString
_PrivPolStatEnterpriseName_Object = MibTableColumn
privPolStatEnterpriseName = _PrivPolStatEnterpriseName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 2),
    _PrivPolStatEnterpriseName_Type()
)
privPolStatEnterpriseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privPolStatEnterpriseName.setStatus("current")
_PrivPolStatPolicyName_Type = DisplayString
_PrivPolStatPolicyName_Object = MibTableColumn
privPolStatPolicyName = _PrivPolStatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 3),
    _PrivPolStatPolicyName_Type()
)
privPolStatPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privPolStatPolicyName.setStatus("current")
_PrivPolStatNbRequests_Type = Counter32
_PrivPolStatNbRequests_Object = MibTableColumn
privPolStatNbRequests = _PrivPolStatNbRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 4),
    _PrivPolStatNbRequests_Type()
)
privPolStatNbRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privPolStatNbRequests.setStatus("current")
_PrivPolStatNbRequestsFailures_Type = Counter32
_PrivPolStatNbRequestsFailures_Object = MibTableColumn
privPolStatNbRequestsFailures = _PrivPolStatNbRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 5),
    _PrivPolStatNbRequestsFailures_Type()
)
privPolStatNbRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privPolStatNbRequestsFailures.setStatus("current")
_PrivPolStatNbRequestsResults_Type = Counter32
_PrivPolStatNbRequestsResults_Object = MibTableColumn
privPolStatNbRequestsResults = _PrivPolStatNbRequestsResults_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 2, 1, 6),
    _PrivPolStatNbRequestsResults_Type()
)
privPolStatNbRequestsResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privPolStatNbRequestsResults.setStatus("current")
_PolicyInfoTable_Object = MibTable
policyInfoTable = _PolicyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    policyInfoTable.setStatus("current")
_PolicyInfoEntry_Object = MibTableRow
policyInfoEntry = _PolicyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1)
)
policyInfoEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "polInfoID"),
)
if mibBuilder.loadTexts:
    policyInfoEntry.setStatus("current")
_PolInfoID_Type = Unsigned32
_PolInfoID_Object = MibTableColumn
polInfoID = _PolInfoID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1, 1),
    _PolInfoID_Type()
)
polInfoID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    polInfoID.setStatus("current")
_PolInfoEnterpriseName_Type = DisplayString
_PolInfoEnterpriseName_Object = MibTableColumn
polInfoEnterpriseName = _PolInfoEnterpriseName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1, 2),
    _PolInfoEnterpriseName_Type()
)
polInfoEnterpriseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polInfoEnterpriseName.setStatus("current")
_PolInfoPolicyName_Type = DisplayString
_PolInfoPolicyName_Object = MibTableColumn
polInfoPolicyName = _PolInfoPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1, 3),
    _PolInfoPolicyName_Type()
)
polInfoPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polInfoPolicyName.setStatus("current")
_PolInfoInfoName_Type = DisplayString
_PolInfoInfoName_Object = MibTableColumn
polInfoInfoName = _PolInfoInfoName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1, 4),
    _PolInfoInfoName_Type()
)
polInfoInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polInfoInfoName.setStatus("current")
_PolInfoNbOccurences_Type = Counter32
_PolInfoNbOccurences_Object = MibTableColumn
polInfoNbOccurences = _PolInfoNbOccurences_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 3, 1, 5),
    _PolInfoNbOccurences_Type()
)
polInfoNbOccurences.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    polInfoNbOccurences.setStatus("current")
_BwNbPolicyRequests_Type = Counter32
_BwNbPolicyRequests_Object = MibScalar
bwNbPolicyRequests = _BwNbPolicyRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 4),
    _BwNbPolicyRequests_Type()
)
bwNbPolicyRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNbPolicyRequests.setStatus("current")
_BwNbPolicyRequestFailures_Type = Counter32
_BwNbPolicyRequestFailures_Object = MibScalar
bwNbPolicyRequestFailures = _BwNbPolicyRequestFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 3, 5),
    _BwNbPolicyRequestFailures_Type()
)
bwNbPolicyRequestFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNbPolicyRequestFailures.setStatus("current")
_NeStatTable_Object = MibTable
neStatTable = _NeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    neStatTable.setStatus("current")
_NeStatEntry_Object = MibTableRow
neStatEntry = _NeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1)
)
neStatEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "neStatID"),
)
if mibBuilder.loadTexts:
    neStatEntry.setStatus("current")
_NeStatID_Type = Unsigned32
_NeStatID_Object = MibTableColumn
neStatID = _NeStatID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 1),
    _NeStatID_Type()
)
neStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neStatID.setStatus("current")
_NeStatName_Type = DisplayString
_NeStatName_Object = MibTableColumn
neStatName = _NeStatName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 2),
    _NeStatName_Type()
)
neStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatName.setStatus("current")
_NeStatNbSIPRequests_Type = Counter32
_NeStatNbSIPRequests_Object = MibTableColumn
neStatNbSIPRequests = _NeStatNbSIPRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 3),
    _NeStatNbSIPRequests_Type()
)
neStatNbSIPRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neStatNbSIPRequests.setStatus("current")
_NeStatNbSIPRequestsFailures_Type = Counter32
_NeStatNbSIPRequestsFailures_Object = MibTableColumn
neStatNbSIPRequestsFailures = _NeStatNbSIPRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 4),
    _NeStatNbSIPRequestsFailures_Type()
)
neStatNbSIPRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neStatNbSIPRequestsFailures.setStatus("current")
_NeStatNbMSSRequests_Type = Counter32
_NeStatNbMSSRequests_Object = MibTableColumn
neStatNbMSSRequests = _NeStatNbMSSRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 5),
    _NeStatNbMSSRequests_Type()
)
neStatNbMSSRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neStatNbMSSRequests.setStatus("current")
_NeStatNbMSSRequestsFailures_Type = Counter32
_NeStatNbMSSRequestsFailures_Object = MibTableColumn
neStatNbMSSRequestsFailures = _NeStatNbMSSRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 4, 1, 6),
    _NeStatNbMSSRequestsFailures_Type()
)
neStatNbMSSRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neStatNbMSSRequestsFailures.setStatus("current")
_ErrorStatTable_Object = MibTable
errorStatTable = _ErrorStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    errorStatTable.setStatus("current")
_ErrorStatEntry_Object = MibTableRow
errorStatEntry = _ErrorStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 5, 1)
)
errorStatEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "errStatID"),
)
if mibBuilder.loadTexts:
    errorStatEntry.setStatus("current")
_ErrStatID_Type = Unsigned32
_ErrStatID_Object = MibTableColumn
errStatID = _ErrStatID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 5, 1, 1),
    _ErrStatID_Type()
)
errStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errStatID.setStatus("current")
_ErrStatName_Type = DisplayString
_ErrStatName_Object = MibTableColumn
errStatName = _ErrStatName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 5, 1, 2),
    _ErrStatName_Type()
)
errStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errStatName.setStatus("current")
_ErrStatNbOccurences_Type = Counter32
_ErrStatNbOccurences_Object = MibTableColumn
errStatNbOccurences = _ErrStatNbOccurences_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 5, 1, 3),
    _ErrStatNbOccurences_Type()
)
errStatNbOccurences.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errStatNbOccurences.setStatus("current")
_BwNSCallpCallsPerSecond_Type = Gauge32
_BwNSCallpCallsPerSecond_Object = MibScalar
bwNSCallpCallsPerSecond = _BwNSCallpCallsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 6),
    _BwNSCallpCallsPerSecond_Type()
)
bwNSCallpCallsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCallpCallsPerSecond.setStatus("current")
_CarrierStatTable_Object = MibTable
carrierStatTable = _CarrierStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    carrierStatTable.setStatus("current")
_CarrierStatEntry_Object = MibTableRow
carrierStatEntry = _CarrierStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1)
)
carrierStatEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwCarrierStatID"),
)
if mibBuilder.loadTexts:
    carrierStatEntry.setStatus("current")
_BwCarrierStatID_Type = Unsigned32
_BwCarrierStatID_Object = MibTableColumn
bwCarrierStatID = _BwCarrierStatID_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 1),
    _BwCarrierStatID_Type()
)
bwCarrierStatID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwCarrierStatID.setStatus("current")
_BwCarrierName_Type = DisplayString
_BwCarrierName_Object = MibTableColumn
bwCarrierName = _BwCarrierName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 2),
    _BwCarrierName_Type()
)
bwCarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCarrierName.setStatus("current")
_BwCarrierCic_Type = DisplayString
_BwCarrierCic_Object = MibTableColumn
bwCarrierCic = _BwCarrierCic_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 3),
    _BwCarrierCic_Type()
)
bwCarrierCic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCarrierCic.setStatus("current")
_BwCarrierNbIntraLataCalls_Type = Counter32
_BwCarrierNbIntraLataCalls_Object = MibTableColumn
bwCarrierNbIntraLataCalls = _BwCarrierNbIntraLataCalls_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 4),
    _BwCarrierNbIntraLataCalls_Type()
)
bwCarrierNbIntraLataCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCarrierNbIntraLataCalls.setStatus("current")
_BwCarrierNbInterLataCalls_Type = Counter32
_BwCarrierNbInterLataCalls_Object = MibTableColumn
bwCarrierNbInterLataCalls = _BwCarrierNbInterLataCalls_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 5),
    _BwCarrierNbInterLataCalls_Type()
)
bwCarrierNbInterLataCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCarrierNbInterLataCalls.setStatus("current")
_BwCarrierNbInternationalCalls_Type = Counter32
_BwCarrierNbInternationalCalls_Object = MibTableColumn
bwCarrierNbInternationalCalls = _BwCarrierNbInternationalCalls_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 2, 7, 1, 6),
    _BwCarrierNbInternationalCalls_Type()
)
bwCarrierNbInternationalCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCarrierNbInternationalCalls.setStatus("current")
_Protocol_ObjectIdentity = ObjectIdentity
protocol = _Protocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3)
)
_Sip_ObjectIdentity = ObjectIdentity
sip = _Sip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1)
)
_BwNSSipStatsInviteIns_Type = Counter32
_BwNSSipStatsInviteIns_Object = MibScalar
bwNSSipStatsInviteIns = _BwNSSipStatsInviteIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 1),
    _BwNSSipStatsInviteIns_Type()
)
bwNSSipStatsInviteIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsInviteIns.setStatus("current")
_BwNSSipStatsAckIns_Type = Counter32
_BwNSSipStatsAckIns_Object = MibScalar
bwNSSipStatsAckIns = _BwNSSipStatsAckIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 2),
    _BwNSSipStatsAckIns_Type()
)
bwNSSipStatsAckIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsAckIns.setStatus("current")
_BwNSSipStatsInviteResponsesTable_Object = MibTable
bwNSSipStatsInviteResponsesTable = _BwNSSipStatsInviteResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 3)
)
if mibBuilder.loadTexts:
    bwNSSipStatsInviteResponsesTable.setStatus("current")
_BwNSSipStatsInviteResponsesEntry_Object = MibTableRow
bwNSSipStatsInviteResponsesEntry = _BwNSSipStatsInviteResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 3, 1)
)
bwNSSipStatsInviteResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsInviteResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsInviteResponsesEntry.setStatus("current")


class _BwNSSipStatsInviteResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsInviteResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsInviteResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsInviteResponseCodeValue_Object = MibTableColumn
bwNSSipStatsInviteResponseCodeValue = _BwNSSipStatsInviteResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 3, 1, 1),
    _BwNSSipStatsInviteResponseCodeValue_Type()
)
bwNSSipStatsInviteResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsInviteResponseCodeValue.setStatus("current")
_BwNSSipStatsInviteResponseOuts_Type = Counter32
_BwNSSipStatsInviteResponseOuts_Object = MibTableColumn
bwNSSipStatsInviteResponseOuts = _BwNSSipStatsInviteResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 3, 1, 3),
    _BwNSSipStatsInviteResponseOuts_Type()
)
bwNSSipStatsInviteResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsInviteResponseOuts.setStatus("current")
_BwNSSipStatsCancelIns_Type = Counter32
_BwNSSipStatsCancelIns_Object = MibScalar
bwNSSipStatsCancelIns = _BwNSSipStatsCancelIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 4),
    _BwNSSipStatsCancelIns_Type()
)
bwNSSipStatsCancelIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsCancelIns.setStatus("current")
_BwNSSipStatsRegisterIns_Type = Counter32
_BwNSSipStatsRegisterIns_Object = MibScalar
bwNSSipStatsRegisterIns = _BwNSSipStatsRegisterIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 5),
    _BwNSSipStatsRegisterIns_Type()
)
bwNSSipStatsRegisterIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterIns.setStatus("current")
_BwNSSipStatsNotifyIns_Type = Counter32
_BwNSSipStatsNotifyIns_Object = MibScalar
bwNSSipStatsNotifyIns = _BwNSSipStatsNotifyIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 6),
    _BwNSSipStatsNotifyIns_Type()
)
bwNSSipStatsNotifyIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyIns.setStatus("current")
_BwNSSipStatsSubscribeIns_Type = Counter32
_BwNSSipStatsSubscribeIns_Object = MibScalar
bwNSSipStatsSubscribeIns = _BwNSSipStatsSubscribeIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 7),
    _BwNSSipStatsSubscribeIns_Type()
)
bwNSSipStatsSubscribeIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeIns.setStatus("current")
_BwNSSipStatsMessageIns_Type = Counter32
_BwNSSipStatsMessageIns_Object = MibScalar
bwNSSipStatsMessageIns = _BwNSSipStatsMessageIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 8),
    _BwNSSipStatsMessageIns_Type()
)
bwNSSipStatsMessageIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsMessageIns.setStatus("current")
_BwNSSipStatsInfoIns_Type = Counter32
_BwNSSipStatsInfoIns_Object = MibScalar
bwNSSipStatsInfoIns = _BwNSSipStatsInfoIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 9),
    _BwNSSipStatsInfoIns_Type()
)
bwNSSipStatsInfoIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsInfoIns.setStatus("current")
_BwNSSipStatsOptionsIns_Type = Counter32
_BwNSSipStatsOptionsIns_Object = MibScalar
bwNSSipStatsOptionsIns = _BwNSSipStatsOptionsIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 10),
    _BwNSSipStatsOptionsIns_Type()
)
bwNSSipStatsOptionsIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsIns.setStatus("current")
_BwNSSipStatsOptionsResponsesTable_Object = MibTable
bwNSSipStatsOptionsResponsesTable = _BwNSSipStatsOptionsResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 11)
)
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsResponsesTable.setStatus("current")
_BwNSSipStatsOptionsResponsesEntry_Object = MibTableRow
bwNSSipStatsOptionsResponsesEntry = _BwNSSipStatsOptionsResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 11, 1)
)
bwNSSipStatsOptionsResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsOptionsResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsResponsesEntry.setStatus("current")


class _BwNSSipStatsOptionsResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsOptionsResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsOptionsResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsOptionsResponseCodeValue_Object = MibTableColumn
bwNSSipStatsOptionsResponseCodeValue = _BwNSSipStatsOptionsResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 11, 1, 1),
    _BwNSSipStatsOptionsResponseCodeValue_Type()
)
bwNSSipStatsOptionsResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsResponseCodeValue.setStatus("current")
_BwNSSipStatsOptionsResponseIns_Type = Counter32
_BwNSSipStatsOptionsResponseIns_Object = MibTableColumn
bwNSSipStatsOptionsResponseIns = _BwNSSipStatsOptionsResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 11, 1, 2),
    _BwNSSipStatsOptionsResponseIns_Type()
)
bwNSSipStatsOptionsResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsResponseIns.setStatus("current")
_BwNSSipStatsOptionsResponseOuts_Type = Counter32
_BwNSSipStatsOptionsResponseOuts_Object = MibTableColumn
bwNSSipStatsOptionsResponseOuts = _BwNSSipStatsOptionsResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 11, 1, 3),
    _BwNSSipStatsOptionsResponseOuts_Type()
)
bwNSSipStatsOptionsResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsOptionsResponseOuts.setStatus("current")
_BwNSSipStatsRegisterResponsesTable_Object = MibTable
bwNSSipStatsRegisterResponsesTable = _BwNSSipStatsRegisterResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 12)
)
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterResponsesTable.setStatus("current")
_BwNSSipStatsRegisterResponsesEntry_Object = MibTableRow
bwNSSipStatsRegisterResponsesEntry = _BwNSSipStatsRegisterResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 12, 1)
)
bwNSSipStatsRegisterResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsRegisterResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterResponsesEntry.setStatus("current")


class _BwNSSipStatsRegisterResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsRegisterResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsRegisterResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsRegisterResponseCodeValue_Object = MibTableColumn
bwNSSipStatsRegisterResponseCodeValue = _BwNSSipStatsRegisterResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 12, 1, 1),
    _BwNSSipStatsRegisterResponseCodeValue_Type()
)
bwNSSipStatsRegisterResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterResponseCodeValue.setStatus("current")
_BwNSSipStatsRegisterResponseIns_Type = Counter32
_BwNSSipStatsRegisterResponseIns_Object = MibTableColumn
bwNSSipStatsRegisterResponseIns = _BwNSSipStatsRegisterResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 12, 1, 2),
    _BwNSSipStatsRegisterResponseIns_Type()
)
bwNSSipStatsRegisterResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterResponseIns.setStatus("current")
_BwNSSipStatsRegisterResponseOuts_Type = Counter32
_BwNSSipStatsRegisterResponseOuts_Object = MibTableColumn
bwNSSipStatsRegisterResponseOuts = _BwNSSipStatsRegisterResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 12, 1, 3),
    _BwNSSipStatsRegisterResponseOuts_Type()
)
bwNSSipStatsRegisterResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsRegisterResponseOuts.setStatus("current")
_BwNSSipStatsInfoResponsesTable_Object = MibTable
bwNSSipStatsInfoResponsesTable = _BwNSSipStatsInfoResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 13)
)
if mibBuilder.loadTexts:
    bwNSSipStatsInfoResponsesTable.setStatus("current")
_BwNSSipStatsInfoResponsesEntry_Object = MibTableRow
bwNSSipStatsInfoResponsesEntry = _BwNSSipStatsInfoResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 13, 1)
)
bwNSSipStatsInfoResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsInfoResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsInfoResponsesEntry.setStatus("current")


class _BwNSSipStatsInfoResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsInfoResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsInfoResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsInfoResponseCodeValue_Object = MibTableColumn
bwNSSipStatsInfoResponseCodeValue = _BwNSSipStatsInfoResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 13, 1, 1),
    _BwNSSipStatsInfoResponseCodeValue_Type()
)
bwNSSipStatsInfoResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsInfoResponseCodeValue.setStatus("current")
_BwNSSipStatsInfoResponseIns_Type = Counter32
_BwNSSipStatsInfoResponseIns_Object = MibTableColumn
bwNSSipStatsInfoResponseIns = _BwNSSipStatsInfoResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 13, 1, 2),
    _BwNSSipStatsInfoResponseIns_Type()
)
bwNSSipStatsInfoResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsInfoResponseIns.setStatus("current")
_BwNSSipStatsInfoResponseOuts_Type = Counter32
_BwNSSipStatsInfoResponseOuts_Object = MibTableColumn
bwNSSipStatsInfoResponseOuts = _BwNSSipStatsInfoResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 13, 1, 3),
    _BwNSSipStatsInfoResponseOuts_Type()
)
bwNSSipStatsInfoResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsInfoResponseOuts.setStatus("current")
_BwNSSipStatsNotifyResponsesTable_Object = MibTable
bwNSSipStatsNotifyResponsesTable = _BwNSSipStatsNotifyResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 14)
)
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyResponsesTable.setStatus("current")
_BwNSSipStatsNotifyResponsesEntry_Object = MibTableRow
bwNSSipStatsNotifyResponsesEntry = _BwNSSipStatsNotifyResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 14, 1)
)
bwNSSipStatsNotifyResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsNotifyResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyResponsesEntry.setStatus("current")


class _BwNSSipStatsNotifyResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsNotifyResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsNotifyResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsNotifyResponseCodeValue_Object = MibTableColumn
bwNSSipStatsNotifyResponseCodeValue = _BwNSSipStatsNotifyResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 14, 1, 1),
    _BwNSSipStatsNotifyResponseCodeValue_Type()
)
bwNSSipStatsNotifyResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyResponseCodeValue.setStatus("current")
_BwNSSipStatsNotifyResponseIns_Type = Counter32
_BwNSSipStatsNotifyResponseIns_Object = MibTableColumn
bwNSSipStatsNotifyResponseIns = _BwNSSipStatsNotifyResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 14, 1, 2),
    _BwNSSipStatsNotifyResponseIns_Type()
)
bwNSSipStatsNotifyResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyResponseIns.setStatus("current")
_BwNSSipStatsNotifyResponseOuts_Type = Counter32
_BwNSSipStatsNotifyResponseOuts_Object = MibTableColumn
bwNSSipStatsNotifyResponseOuts = _BwNSSipStatsNotifyResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 14, 1, 3),
    _BwNSSipStatsNotifyResponseOuts_Type()
)
bwNSSipStatsNotifyResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsNotifyResponseOuts.setStatus("current")
_BwNSSipStatsSubscribeResponsesTable_Object = MibTable
bwNSSipStatsSubscribeResponsesTable = _BwNSSipStatsSubscribeResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 15)
)
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeResponsesTable.setStatus("current")
_BwNSSipStatsSubscribeResponsesEntry_Object = MibTableRow
bwNSSipStatsSubscribeResponsesEntry = _BwNSSipStatsSubscribeResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 15, 1)
)
bwNSSipStatsSubscribeResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeResponsesEntry.setStatus("current")


class _BwNSSipStatsSubscribeResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsSubscribeResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsSubscribeResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsSubscribeResponseCodeValue_Object = MibTableColumn
bwNSSipStatsSubscribeResponseCodeValue = _BwNSSipStatsSubscribeResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 15, 1, 1),
    _BwNSSipStatsSubscribeResponseCodeValue_Type()
)
bwNSSipStatsSubscribeResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeResponseCodeValue.setStatus("current")
_BwNSSipStatsSubscribeResponseIns_Type = Counter32
_BwNSSipStatsSubscribeResponseIns_Object = MibTableColumn
bwNSSipStatsSubscribeResponseIns = _BwNSSipStatsSubscribeResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 15, 1, 2),
    _BwNSSipStatsSubscribeResponseIns_Type()
)
bwNSSipStatsSubscribeResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeResponseIns.setStatus("current")
_BwNSSipStatsSubscribeResponseOuts_Type = Counter32
_BwNSSipStatsSubscribeResponseOuts_Object = MibTableColumn
bwNSSipStatsSubscribeResponseOuts = _BwNSSipStatsSubscribeResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 15, 1, 3),
    _BwNSSipStatsSubscribeResponseOuts_Type()
)
bwNSSipStatsSubscribeResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsSubscribeResponseOuts.setStatus("current")
_BwNSSipStatsMessageResponsesTable_Object = MibTable
bwNSSipStatsMessageResponsesTable = _BwNSSipStatsMessageResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 16)
)
if mibBuilder.loadTexts:
    bwNSSipStatsMessageResponsesTable.setStatus("current")
_BwNSSipStatsMessageResponsesEntry_Object = MibTableRow
bwNSSipStatsMessageResponsesEntry = _BwNSSipStatsMessageResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 16, 1)
)
bwNSSipStatsMessageResponsesEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSSipStatsMessageResponseCodeValue"),
)
if mibBuilder.loadTexts:
    bwNSSipStatsMessageResponsesEntry.setStatus("current")


class _BwNSSipStatsMessageResponseCodeValue_Type(Integer32):
    """Custom type bwNSSipStatsMessageResponseCodeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999),
    )


_BwNSSipStatsMessageResponseCodeValue_Type.__name__ = "Integer32"
_BwNSSipStatsMessageResponseCodeValue_Object = MibTableColumn
bwNSSipStatsMessageResponseCodeValue = _BwNSSipStatsMessageResponseCodeValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 16, 1, 1),
    _BwNSSipStatsMessageResponseCodeValue_Type()
)
bwNSSipStatsMessageResponseCodeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSSipStatsMessageResponseCodeValue.setStatus("current")
_BwNSSipStatsMessageResponseIns_Type = Counter32
_BwNSSipStatsMessageResponseIns_Object = MibTableColumn
bwNSSipStatsMessageResponseIns = _BwNSSipStatsMessageResponseIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 16, 1, 2),
    _BwNSSipStatsMessageResponseIns_Type()
)
bwNSSipStatsMessageResponseIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsMessageResponseIns.setStatus("current")
_BwNSSipStatsMessageResponseOuts_Type = Counter32
_BwNSSipStatsMessageResponseOuts_Object = MibTableColumn
bwNSSipStatsMessageResponseOuts = _BwNSSipStatsMessageResponseOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 16, 1, 3),
    _BwNSSipStatsMessageResponseOuts_Type()
)
bwNSSipStatsMessageResponseOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsMessageResponseOuts.setStatus("current")
_BwNSSipStatsFailures_Type = Counter32
_BwNSSipStatsFailures_Object = MibScalar
bwNSSipStatsFailures = _BwNSSipStatsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 17),
    _BwNSSipStatsFailures_Type()
)
bwNSSipStatsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsFailures.setStatus("current")
_BwNSSipStatsActiveTcpConnections_Type = Gauge32
_BwNSSipStatsActiveTcpConnections_Object = MibScalar
bwNSSipStatsActiveTcpConnections = _BwNSSipStatsActiveTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 18),
    _BwNSSipStatsActiveTcpConnections_Type()
)
bwNSSipStatsActiveTcpConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSSipStatsActiveTcpConnections.setStatus("current")
_BwNSSipStatsTcpIns_Type = Counter32
_BwNSSipStatsTcpIns_Object = MibScalar
bwNSSipStatsTcpIns = _BwNSSipStatsTcpIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 19),
    _BwNSSipStatsTcpIns_Type()
)
bwNSSipStatsTcpIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsTcpIns.setStatus("current")
_BwNSSipStatsTcpOuts_Type = Counter32
_BwNSSipStatsTcpOuts_Object = MibScalar
bwNSSipStatsTcpOuts = _BwNSSipStatsTcpOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 20),
    _BwNSSipStatsTcpOuts_Type()
)
bwNSSipStatsTcpOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsTcpOuts.setStatus("current")
_BwNSSipStatsTcpFailures_Type = Counter32
_BwNSSipStatsTcpFailures_Object = MibScalar
bwNSSipStatsTcpFailures = _BwNSSipStatsTcpFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 21),
    _BwNSSipStatsTcpFailures_Type()
)
bwNSSipStatsTcpFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsTcpFailures.setStatus("current")
_BwNSSipStatsUdpIns_Type = Counter32
_BwNSSipStatsUdpIns_Object = MibScalar
bwNSSipStatsUdpIns = _BwNSSipStatsUdpIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 22),
    _BwNSSipStatsUdpIns_Type()
)
bwNSSipStatsUdpIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsUdpIns.setStatus("current")
_BwNSSipStatsUdpOuts_Type = Counter32
_BwNSSipStatsUdpOuts_Object = MibScalar
bwNSSipStatsUdpOuts = _BwNSSipStatsUdpOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 23),
    _BwNSSipStatsUdpOuts_Type()
)
bwNSSipStatsUdpOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSipStatsUdpOuts.setStatus("current")
_BwNSSIPReclaimedStaleTcpConnections_Type = Counter32
_BwNSSIPReclaimedStaleTcpConnections_Object = MibScalar
bwNSSIPReclaimedStaleTcpConnections = _BwNSSIPReclaimedStaleTcpConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 24),
    _BwNSSIPReclaimedStaleTcpConnections_Type()
)
bwNSSIPReclaimedStaleTcpConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSSIPReclaimedStaleTcpConnections.setStatus("current")
_CongestionManagement_ObjectIdentity = ObjectIdentity
congestionManagement = _CongestionManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25)
)
_BwNSCongestionManagementNeighborTable_Object = MibTable
bwNSCongestionManagementNeighborTable = _BwNSCongestionManagementNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1)
)
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborTable.setStatus("current")
_BwNSCongestionManagementNeighborEntry_Object = MibTableRow
bwNSCongestionManagementNeighborEntry = _BwNSCongestionManagementNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1)
)
bwNSCongestionManagementNeighborEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborIndex"),
)
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborEntry.setStatus("current")
_BwNSCongestionManagementNeighborIndex_Type = Unsigned32
_BwNSCongestionManagementNeighborIndex_Object = MibTableColumn
bwNSCongestionManagementNeighborIndex = _BwNSCongestionManagementNeighborIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 1),
    _BwNSCongestionManagementNeighborIndex_Type()
)
bwNSCongestionManagementNeighborIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborIndex.setStatus("current")
_BwNSCongestionManagementNeighborIpAddress_Type = DisplayString
_BwNSCongestionManagementNeighborIpAddress_Object = MibTableColumn
bwNSCongestionManagementNeighborIpAddress = _BwNSCongestionManagementNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 2),
    _BwNSCongestionManagementNeighborIpAddress_Type()
)
bwNSCongestionManagementNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborIpAddress.setStatus("current")
_BwNSCongestionManagementNeighborInviteIn_Type = Counter32
_BwNSCongestionManagementNeighborInviteIn_Object = MibTableColumn
bwNSCongestionManagementNeighborInviteIn = _BwNSCongestionManagementNeighborInviteIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 3),
    _BwNSCongestionManagementNeighborInviteIn_Type()
)
bwNSCongestionManagementNeighborInviteIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborInviteIn.setStatus("current")
_BwNSCongestionManagementNeighborRegisterIn_Type = Counter32
_BwNSCongestionManagementNeighborRegisterIn_Object = MibTableColumn
bwNSCongestionManagementNeighborRegisterIn = _BwNSCongestionManagementNeighborRegisterIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 4),
    _BwNSCongestionManagementNeighborRegisterIn_Type()
)
bwNSCongestionManagementNeighborRegisterIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborRegisterIn.setStatus("current")
_BwNSCongestionManagementNeighborOptionsIn_Type = Counter32
_BwNSCongestionManagementNeighborOptionsIn_Object = MibTableColumn
bwNSCongestionManagementNeighborOptionsIn = _BwNSCongestionManagementNeighborOptionsIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 5),
    _BwNSCongestionManagementNeighborOptionsIn_Type()
)
bwNSCongestionManagementNeighborOptionsIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborOptionsIn.setStatus("current")
_BwNSCongestionManagementNeighborOptionsOut_Type = Counter32
_BwNSCongestionManagementNeighborOptionsOut_Object = MibTableColumn
bwNSCongestionManagementNeighborOptionsOut = _BwNSCongestionManagementNeighborOptionsOut_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 6),
    _BwNSCongestionManagementNeighborOptionsOut_Type()
)
bwNSCongestionManagementNeighborOptionsOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborOptionsOut.setStatus("current")
_BwNSCongestionManagementNeighborSubscribeNotifyIn_Type = Counter32
_BwNSCongestionManagementNeighborSubscribeNotifyIn_Object = MibTableColumn
bwNSCongestionManagementNeighborSubscribeNotifyIn = _BwNSCongestionManagementNeighborSubscribeNotifyIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 7),
    _BwNSCongestionManagementNeighborSubscribeNotifyIn_Type()
)
bwNSCongestionManagementNeighborSubscribeNotifyIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborSubscribeNotifyIn.setStatus("current")
_BwNSCongestionManagementNeighbor5xxIn_Type = Counter32
_BwNSCongestionManagementNeighbor5xxIn_Object = MibTableColumn
bwNSCongestionManagementNeighbor5xxIn = _BwNSCongestionManagementNeighbor5xxIn_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 8),
    _BwNSCongestionManagementNeighbor5xxIn_Type()
)
bwNSCongestionManagementNeighbor5xxIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighbor5xxIn.setStatus("current")
_BwNSCongestionManagementNeighborCallpRequestInRate_Type = Gauge32
_BwNSCongestionManagementNeighborCallpRequestInRate_Object = MibTableColumn
bwNSCongestionManagementNeighborCallpRequestInRate = _BwNSCongestionManagementNeighborCallpRequestInRate_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 9),
    _BwNSCongestionManagementNeighborCallpRequestInRate_Type()
)
bwNSCongestionManagementNeighborCallpRequestInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborCallpRequestInRate.setStatus("current")
_BwNSCongestionManagementNeighborNonCallpRequestInRate_Type = Gauge32
_BwNSCongestionManagementNeighborNonCallpRequestInRate_Object = MibTableColumn
bwNSCongestionManagementNeighborNonCallpRequestInRate = _BwNSCongestionManagementNeighborNonCallpRequestInRate_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 10),
    _BwNSCongestionManagementNeighborNonCallpRequestInRate_Type()
)
bwNSCongestionManagementNeighborNonCallpRequestInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborNonCallpRequestInRate.setStatus("current")
_BwNSCongestionManagementNeighborState_Type = DisplayString
_BwNSCongestionManagementNeighborState_Object = MibTableColumn
bwNSCongestionManagementNeighborState = _BwNSCongestionManagementNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 11),
    _BwNSCongestionManagementNeighborState_Type()
)
bwNSCongestionManagementNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborState.setStatus("current")
_BwNSCongestionManagementNeighborCapability_Type = DisplayString
_BwNSCongestionManagementNeighborCapability_Object = MibTableColumn
bwNSCongestionManagementNeighborCapability = _BwNSCongestionManagementNeighborCapability_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 1, 25, 1, 1, 12),
    _BwNSCongestionManagementNeighborCapability_Type()
)
bwNSCongestionManagementNeighborCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCongestionManagementNeighborCapability.setStatus("current")
_Nrs_ObjectIdentity = ObjectIdentity
nrs = _Nrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2)
)
_BwNSNbInvalidMessagesReceived_Type = Counter32
_BwNSNbInvalidMessagesReceived_Object = MibScalar
bwNSNbInvalidMessagesReceived = _BwNSNbInvalidMessagesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 6),
    _BwNSNbInvalidMessagesReceived_Type()
)
bwNSNbInvalidMessagesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbInvalidMessagesReceived.setStatus("current")
_BwNSNbRequestsReceived_Type = Counter32
_BwNSNbRequestsReceived_Object = MibScalar
bwNSNbRequestsReceived = _BwNSNbRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 7),
    _BwNSNbRequestsReceived_Type()
)
bwNSNbRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbRequestsReceived.setStatus("current")
_BwNSNbResponsesReceived_Type = Counter32
_BwNSNbResponsesReceived_Object = MibScalar
bwNSNbResponsesReceived = _BwNSNbResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 8),
    _BwNSNbResponsesReceived_Type()
)
bwNSNbResponsesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbResponsesReceived.setStatus("current")
_BwNSNbErrorsReceived_Type = Counter32
_BwNSNbErrorsReceived_Object = MibScalar
bwNSNbErrorsReceived = _BwNSNbErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 9),
    _BwNSNbErrorsReceived_Type()
)
bwNSNbErrorsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbErrorsReceived.setStatus("current")
_BwNSNbRequestsSent_Type = Counter32
_BwNSNbRequestsSent_Object = MibScalar
bwNSNbRequestsSent = _BwNSNbRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 10),
    _BwNSNbRequestsSent_Type()
)
bwNSNbRequestsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbRequestsSent.setStatus("current")
_BwNSNbResponsesSent_Type = Counter32
_BwNSNbResponsesSent_Object = MibScalar
bwNSNbResponsesSent = _BwNSNbResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 11),
    _BwNSNbResponsesSent_Type()
)
bwNSNbResponsesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbResponsesSent.setStatus("current")
_BwNSNbErrorsSent_Type = Counter32
_BwNSNbErrorsSent_Object = MibScalar
bwNSNbErrorsSent = _BwNSNbErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 12),
    _BwNSNbErrorsSent_Type()
)
bwNSNbErrorsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbErrorsSent.setStatus("current")
_BwNSNbRequestsResent_Type = Counter32
_BwNSNbRequestsResent_Object = MibScalar
bwNSNbRequestsResent = _BwNSNbRequestsResent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 13),
    _BwNSNbRequestsResent_Type()
)
bwNSNbRequestsResent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbRequestsResent.setStatus("current")
_BwNSNbResponsesResent_Type = Counter32
_BwNSNbResponsesResent_Object = MibScalar
bwNSNbResponsesResent = _BwNSNbResponsesResent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 14),
    _BwNSNbResponsesResent_Type()
)
bwNSNbResponsesResent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbResponsesResent.setStatus("current")
_BwNSNbRequestsUnanswered_Type = Counter32
_BwNSNbRequestsUnanswered_Object = MibScalar
bwNSNbRequestsUnanswered = _BwNSNbRequestsUnanswered_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 15),
    _BwNSNbRequestsUnanswered_Type()
)
bwNSNbRequestsUnanswered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNbRequestsUnanswered.setStatus("current")
_BwNSNRSStatsTable_Object = MibTable
bwNSNRSStatsTable = _BwNSNRSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16)
)
if mibBuilder.loadTexts:
    bwNSNRSStatsTable.setStatus("current")
_BwNSNRSStatsEntry_Object = MibTableRow
bwNSNRSStatsEntry = _BwNSNRSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1)
)
bwNSNRSStatsEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSNRSStatsTableIndex"),
)
if mibBuilder.loadTexts:
    bwNSNRSStatsEntry.setStatus("current")
_BwNSNRSStatsTableIndex_Type = Unsigned32
_BwNSNRSStatsTableIndex_Object = MibTableColumn
bwNSNRSStatsTableIndex = _BwNSNRSStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 1),
    _BwNSNRSStatsTableIndex_Type()
)
bwNSNRSStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableIndex.setStatus("current")
_BwNSNRSStatsTableProtocolName_Type = DisplayString
_BwNSNRSStatsTableProtocolName_Object = MibTableColumn
bwNSNRSStatsTableProtocolName = _BwNSNRSStatsTableProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 2),
    _BwNSNRSStatsTableProtocolName_Type()
)
bwNSNRSStatsTableProtocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableProtocolName.setStatus("current")
_BwNSNRSStatsTableNbRequestsReceived_Type = Counter32
_BwNSNRSStatsTableNbRequestsReceived_Object = MibTableColumn
bwNSNRSStatsTableNbRequestsReceived = _BwNSNRSStatsTableNbRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 3),
    _BwNSNRSStatsTableNbRequestsReceived_Type()
)
bwNSNRSStatsTableNbRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbRequestsReceived.setStatus("current")
_BwNSNRSStatsTableNbResponsesReceived_Type = Counter32
_BwNSNRSStatsTableNbResponsesReceived_Object = MibTableColumn
bwNSNRSStatsTableNbResponsesReceived = _BwNSNRSStatsTableNbResponsesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 4),
    _BwNSNRSStatsTableNbResponsesReceived_Type()
)
bwNSNRSStatsTableNbResponsesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbResponsesReceived.setStatus("current")
_BwNSNRSStatsTableNbErrorsReceived_Type = Counter32
_BwNSNRSStatsTableNbErrorsReceived_Object = MibTableColumn
bwNSNRSStatsTableNbErrorsReceived = _BwNSNRSStatsTableNbErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 5),
    _BwNSNRSStatsTableNbErrorsReceived_Type()
)
bwNSNRSStatsTableNbErrorsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbErrorsReceived.setStatus("current")
_BwNSNRSStatsTableNbRequestsSent_Type = Counter32
_BwNSNRSStatsTableNbRequestsSent_Object = MibTableColumn
bwNSNRSStatsTableNbRequestsSent = _BwNSNRSStatsTableNbRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 6),
    _BwNSNRSStatsTableNbRequestsSent_Type()
)
bwNSNRSStatsTableNbRequestsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbRequestsSent.setStatus("current")
_BwNSNRSStatsTableNbResponsesSent_Type = Counter32
_BwNSNRSStatsTableNbResponsesSent_Object = MibTableColumn
bwNSNRSStatsTableNbResponsesSent = _BwNSNRSStatsTableNbResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 7),
    _BwNSNRSStatsTableNbResponsesSent_Type()
)
bwNSNRSStatsTableNbResponsesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbResponsesSent.setStatus("current")
_BwNSNRSStatsTableNbErrorsSent_Type = Counter32
_BwNSNRSStatsTableNbErrorsSent_Object = MibTableColumn
bwNSNRSStatsTableNbErrorsSent = _BwNSNRSStatsTableNbErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 8),
    _BwNSNRSStatsTableNbErrorsSent_Type()
)
bwNSNRSStatsTableNbErrorsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbErrorsSent.setStatus("current")
_BwNSNRSStatsTableNbRequestsResent_Type = Counter32
_BwNSNRSStatsTableNbRequestsResent_Object = MibTableColumn
bwNSNRSStatsTableNbRequestsResent = _BwNSNRSStatsTableNbRequestsResent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 9),
    _BwNSNRSStatsTableNbRequestsResent_Type()
)
bwNSNRSStatsTableNbRequestsResent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbRequestsResent.setStatus("current")
_BwNSNRSStatsTableNbResponsesResent_Type = Counter32
_BwNSNRSStatsTableNbResponsesResent_Object = MibTableColumn
bwNSNRSStatsTableNbResponsesResent = _BwNSNRSStatsTableNbResponsesResent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 10),
    _BwNSNRSStatsTableNbResponsesResent_Type()
)
bwNSNRSStatsTableNbResponsesResent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbResponsesResent.setStatus("current")
_BwNSNRSStatsTableNbRequestsUnanswered_Type = Counter32
_BwNSNRSStatsTableNbRequestsUnanswered_Object = MibTableColumn
bwNSNRSStatsTableNbRequestsUnanswered = _BwNSNRSStatsTableNbRequestsUnanswered_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 2, 16, 1, 11),
    _BwNSNRSStatsTableNbRequestsUnanswered_Type()
)
bwNSNRSStatsTableNbRequestsUnanswered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSNRSStatsTableNbRequestsUnanswered.setStatus("current")
_CallLog_ObjectIdentity = ObjectIdentity
callLog = _CallLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 6)
)
_CalllogNbEnterprises_Type = Gauge32
_CalllogNbEnterprises_Object = MibScalar
calllogNbEnterprises = _CalllogNbEnterprises_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 6, 1),
    _CalllogNbEnterprises_Type()
)
calllogNbEnterprises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calllogNbEnterprises.setStatus("current")
_CalllogNbClients_Type = Gauge32
_CalllogNbClients_Object = MibScalar
calllogNbClients = _CalllogNbClients_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 6, 2),
    _CalllogNbClients_Type()
)
calllogNbClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calllogNbClients.setStatus("current")
_NsXSCommonCommStats_ObjectIdentity = ObjectIdentity
nsXSCommonCommStats = _NsXSCommonCommStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7)
)
_BwNSCommonCommXSStatsTable_Object = MibTable
bwNSCommonCommXSStatsTable = _BwNSCommonCommXSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1)
)
if mibBuilder.loadTexts:
    bwNSCommonCommXSStatsTable.setStatus("current")
_BwNSCommonCommXSStatsEntry_Object = MibTableRow
bwNSCommonCommXSStatsEntry = _BwNSCommonCommXSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1)
)
bwNSCommonCommXSStatsEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSCommonCommXSStatsIndex"),
)
if mibBuilder.loadTexts:
    bwNSCommonCommXSStatsEntry.setStatus("current")
_BwNSCommonCommXSStatsIndex_Type = Unsigned32
_BwNSCommonCommXSStatsIndex_Object = MibTableColumn
bwNSCommonCommXSStatsIndex = _BwNSCommonCommXSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 1),
    _BwNSCommonCommXSStatsIndex_Type()
)
bwNSCommonCommXSStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommXSStatsIndex.setStatus("current")
_BwNSCommonCommXSHost_Type = DisplayString
_BwNSCommonCommXSHost_Object = MibTableColumn
bwNSCommonCommXSHost = _BwNSCommonCommXSHost_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 2),
    _BwNSCommonCommXSHost_Type()
)
bwNSCommonCommXSHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommXSHost.setStatus("current")
_BwNSCommonCommXSInterface_Type = DisplayString
_BwNSCommonCommXSInterface_Object = MibTableColumn
bwNSCommonCommXSInterface = _BwNSCommonCommXSInterface_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 3),
    _BwNSCommonCommXSInterface_Type()
)
bwNSCommonCommXSInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommXSInterface.setStatus("current")
_BwNSCommonCommXSProtocol_Type = DisplayString
_BwNSCommonCommXSProtocol_Object = MibTableColumn
bwNSCommonCommXSProtocol = _BwNSCommonCommXSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 4),
    _BwNSCommonCommXSProtocol_Type()
)
bwNSCommonCommXSProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommXSProtocol.setStatus("current")
_BwNSCommonCommXSAcceptedOutboundConnections_Type = Counter32
_BwNSCommonCommXSAcceptedOutboundConnections_Object = MibTableColumn
bwNSCommonCommXSAcceptedOutboundConnections = _BwNSCommonCommXSAcceptedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 5),
    _BwNSCommonCommXSAcceptedOutboundConnections_Type()
)
bwNSCommonCommXSAcceptedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSAcceptedOutboundConnections.setStatus("current")
_BwNSCommonCommXSAcceptedInboundConnections_Type = Counter32
_BwNSCommonCommXSAcceptedInboundConnections_Object = MibTableColumn
bwNSCommonCommXSAcceptedInboundConnections = _BwNSCommonCommXSAcceptedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 6),
    _BwNSCommonCommXSAcceptedInboundConnections_Type()
)
bwNSCommonCommXSAcceptedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSAcceptedInboundConnections.setStatus("current")
_BwNSCommonCommXSRejectedOutboundConnections_Type = Counter32
_BwNSCommonCommXSRejectedOutboundConnections_Object = MibTableColumn
bwNSCommonCommXSRejectedOutboundConnections = _BwNSCommonCommXSRejectedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 7),
    _BwNSCommonCommXSRejectedOutboundConnections_Type()
)
bwNSCommonCommXSRejectedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSRejectedOutboundConnections.setStatus("current")
_BwNSCommonCommXSRejectedInboundConnections_Type = Counter32
_BwNSCommonCommXSRejectedInboundConnections_Object = MibTableColumn
bwNSCommonCommXSRejectedInboundConnections = _BwNSCommonCommXSRejectedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 8),
    _BwNSCommonCommXSRejectedInboundConnections_Type()
)
bwNSCommonCommXSRejectedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSRejectedInboundConnections.setStatus("current")
_BwNSCommonCommXSOutputMessagesProcessed_Type = Counter32
_BwNSCommonCommXSOutputMessagesProcessed_Object = MibTableColumn
bwNSCommonCommXSOutputMessagesProcessed = _BwNSCommonCommXSOutputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 9),
    _BwNSCommonCommXSOutputMessagesProcessed_Type()
)
bwNSCommonCommXSOutputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSOutputMessagesProcessed.setStatus("current")
_BwNSCommonCommXSInputMessagesProcessed_Type = Counter32
_BwNSCommonCommXSInputMessagesProcessed_Object = MibTableColumn
bwNSCommonCommXSInputMessagesProcessed = _BwNSCommonCommXSInputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 10),
    _BwNSCommonCommXSInputMessagesProcessed_Type()
)
bwNSCommonCommXSInputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSInputMessagesProcessed.setStatus("current")
_BwNSCommonCommXSOutputCommunicationErrors_Type = Counter32
_BwNSCommonCommXSOutputCommunicationErrors_Object = MibTableColumn
bwNSCommonCommXSOutputCommunicationErrors = _BwNSCommonCommXSOutputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 11),
    _BwNSCommonCommXSOutputCommunicationErrors_Type()
)
bwNSCommonCommXSOutputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSOutputCommunicationErrors.setStatus("current")
_BwNSCommonCommXSInputCommunicationErrors_Type = Counter32
_BwNSCommonCommXSInputCommunicationErrors_Object = MibTableColumn
bwNSCommonCommXSInputCommunicationErrors = _BwNSCommonCommXSInputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 7, 1, 1, 12),
    _BwNSCommonCommXSInputCommunicationErrors_Type()
)
bwNSCommonCommXSInputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommXSInputCommunicationErrors.setStatus("current")
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8)
)
_BwNSXSTcpServersStatsTable_Object = MibTable
bwNSXSTcpServersStatsTable = _BwNSXSTcpServersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1)
)
if mibBuilder.loadTexts:
    bwNSXSTcpServersStatsTable.setStatus("current")
_BwNSXSTcpServersStatsEntry_Object = MibTableRow
bwNSXSTcpServersStatsEntry = _BwNSXSTcpServersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1)
)
bwNSXSTcpServersStatsEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSXSTcpServersStatsIndex"),
)
if mibBuilder.loadTexts:
    bwNSXSTcpServersStatsEntry.setStatus("current")
_BwNSXSTcpServersStatsIndex_Type = Unsigned32
_BwNSXSTcpServersStatsIndex_Object = MibTableColumn
bwNSXSTcpServersStatsIndex = _BwNSXSTcpServersStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 1),
    _BwNSXSTcpServersStatsIndex_Type()
)
bwNSXSTcpServersStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTcpServersStatsIndex.setStatus("current")
_BwNSXSTcpServersName_Type = DisplayString
_BwNSXSTcpServersName_Object = MibTableColumn
bwNSXSTcpServersName = _BwNSXSTcpServersName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 2),
    _BwNSXSTcpServersName_Type()
)
bwNSXSTcpServersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTcpServersName.setStatus("current")
_BwNSXSTcpServersNbConnectionsAccepted_Type = Counter32
_BwNSXSTcpServersNbConnectionsAccepted_Object = MibTableColumn
bwNSXSTcpServersNbConnectionsAccepted = _BwNSXSTcpServersNbConnectionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 3),
    _BwNSXSTcpServersNbConnectionsAccepted_Type()
)
bwNSXSTcpServersNbConnectionsAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbConnectionsAccepted.setStatus("current")
_BwNSXSTcpServersNbConnectionsRefused_Type = Counter32
_BwNSXSTcpServersNbConnectionsRefused_Object = MibTableColumn
bwNSXSTcpServersNbConnectionsRefused = _BwNSXSTcpServersNbConnectionsRefused_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 4),
    _BwNSXSTcpServersNbConnectionsRefused_Type()
)
bwNSXSTcpServersNbConnectionsRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbConnectionsRefused.setStatus("current")
_BwNSXSTcpServersNbConnectionsInitiated_Type = Counter32
_BwNSXSTcpServersNbConnectionsInitiated_Object = MibTableColumn
bwNSXSTcpServersNbConnectionsInitiated = _BwNSXSTcpServersNbConnectionsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 5),
    _BwNSXSTcpServersNbConnectionsInitiated_Type()
)
bwNSXSTcpServersNbConnectionsInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbConnectionsInitiated.setStatus("current")
_BwNSXSTcpServersNbConnectionsClosed_Type = Counter32
_BwNSXSTcpServersNbConnectionsClosed_Object = MibTableColumn
bwNSXSTcpServersNbConnectionsClosed = _BwNSXSTcpServersNbConnectionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 6),
    _BwNSXSTcpServersNbConnectionsClosed_Type()
)
bwNSXSTcpServersNbConnectionsClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbConnectionsClosed.setStatus("current")
_BwNSXSTcpServersNbBytesSent_Type = Gauge32
_BwNSXSTcpServersNbBytesSent_Object = MibTableColumn
bwNSXSTcpServersNbBytesSent = _BwNSXSTcpServersNbBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 7),
    _BwNSXSTcpServersNbBytesSent_Type()
)
bwNSXSTcpServersNbBytesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbBytesSent.setStatus("current")
_BwNSXSTcpServersNbBytesReceived_Type = Gauge32
_BwNSXSTcpServersNbBytesReceived_Object = MibTableColumn
bwNSXSTcpServersNbBytesReceived = _BwNSXSTcpServersNbBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 8),
    _BwNSXSTcpServersNbBytesReceived_Type()
)
bwNSXSTcpServersNbBytesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbBytesReceived.setStatus("current")
_BwNSXSTcpServersOutgoingQueueSize_Type = Gauge32
_BwNSXSTcpServersOutgoingQueueSize_Object = MibTableColumn
bwNSXSTcpServersOutgoingQueueSize = _BwNSXSTcpServersOutgoingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 9),
    _BwNSXSTcpServersOutgoingQueueSize_Type()
)
bwNSXSTcpServersOutgoingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTcpServersOutgoingQueueSize.setStatus("current")
_BwNSXSTcpServersIncomingQueueSize_Type = Gauge32
_BwNSXSTcpServersIncomingQueueSize_Object = MibTableColumn
bwNSXSTcpServersIncomingQueueSize = _BwNSXSTcpServersIncomingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 10),
    _BwNSXSTcpServersIncomingQueueSize_Type()
)
bwNSXSTcpServersIncomingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTcpServersIncomingQueueSize.setStatus("current")
_BwNSXSTcpServersNbBytesSentSecure_Type = Gauge32
_BwNSXSTcpServersNbBytesSentSecure_Object = MibTableColumn
bwNSXSTcpServersNbBytesSentSecure = _BwNSXSTcpServersNbBytesSentSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 11),
    _BwNSXSTcpServersNbBytesSentSecure_Type()
)
bwNSXSTcpServersNbBytesSentSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbBytesSentSecure.setStatus("current")
_BwNSXSTcpServersNbBytesReceivedSecure_Type = Gauge32
_BwNSXSTcpServersNbBytesReceivedSecure_Object = MibTableColumn
bwNSXSTcpServersNbBytesReceivedSecure = _BwNSXSTcpServersNbBytesReceivedSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 3, 8, 1, 1, 12),
    _BwNSXSTcpServersNbBytesReceivedSecure_Type()
)
bwNSXSTcpServersNbBytesReceivedSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTcpServersNbBytesReceivedSecure.setStatus("current")
_Persistency_ObjectIdentity = ObjectIdentity
persistency = _Persistency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4)
)
_TimesTen_ObjectIdentity = ObjectIdentity
timesTen = _TimesTen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1)
)
_TtNSNbConnectionsCreated_Type = Counter32
_TtNSNbConnectionsCreated_Object = MibScalar
ttNSNbConnectionsCreated = _TtNSNbConnectionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 1),
    _TtNSNbConnectionsCreated_Type()
)
ttNSNbConnectionsCreated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ttNSNbConnectionsCreated.setStatus("current")
_TtNSConnectionPoolSize_Type = Gauge32
_TtNSConnectionPoolSize_Object = MibScalar
ttNSConnectionPoolSize = _TtNSConnectionPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 2),
    _TtNSConnectionPoolSize_Type()
)
ttNSConnectionPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttNSConnectionPoolSize.setStatus("current")
_TtNSNbBackdoorUpdates_Type = Counter32
_TtNSNbBackdoorUpdates_Object = MibScalar
ttNSNbBackdoorUpdates = _TtNSNbBackdoorUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 3),
    _TtNSNbBackdoorUpdates_Type()
)
ttNSNbBackdoorUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ttNSNbBackdoorUpdates.setStatus("obsolete")
_TtNSNbFailedCheckpoints_Type = Counter32
_TtNSNbFailedCheckpoints_Object = MibScalar
ttNSNbFailedCheckpoints = _TtNSNbFailedCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 4),
    _TtNSNbFailedCheckpoints_Type()
)
ttNSNbFailedCheckpoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ttNSNbFailedCheckpoints.setStatus("obsolete")
_XsRemoteXla_ObjectIdentity = ObjectIdentity
xsRemoteXla = _XsRemoteXla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 5)
)
_XsNSRemoteXlaNbTimesConnected_Type = Counter32
_XsNSRemoteXlaNbTimesConnected_Object = MibScalar
xsNSRemoteXlaNbTimesConnected = _XsNSRemoteXlaNbTimesConnected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 5, 1),
    _XsNSRemoteXlaNbTimesConnected_Type()
)
xsNSRemoteXlaNbTimesConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsNSRemoteXlaNbTimesConnected.setStatus("current")
_XsNSRemoteXlaNbTimesDisconnected_Type = Counter32
_XsNSRemoteXlaNbTimesDisconnected_Object = MibScalar
xsNSRemoteXlaNbTimesDisconnected = _XsNSRemoteXlaNbTimesDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 5, 2),
    _XsNSRemoteXlaNbTimesDisconnected_Type()
)
xsNSRemoteXlaNbTimesDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsNSRemoteXlaNbTimesDisconnected.setStatus("current")
_XsNSRemoteXlaUpdatesProcessed_Type = Counter32
_XsNSRemoteXlaUpdatesProcessed_Object = MibScalar
xsNSRemoteXlaUpdatesProcessed = _XsNSRemoteXlaUpdatesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 5, 3),
    _XsNSRemoteXlaUpdatesProcessed_Type()
)
xsNSRemoteXlaUpdatesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsNSRemoteXlaUpdatesProcessed.setStatus("current")
_XsNSRemoteXlaUpdatesPending_Type = Gauge32
_XsNSRemoteXlaUpdatesPending_Object = MibScalar
xsNSRemoteXlaUpdatesPending = _XsNSRemoteXlaUpdatesPending_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 5, 4),
    _XsNSRemoteXlaUpdatesPending_Type()
)
xsNSRemoteXlaUpdatesPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xsNSRemoteXlaUpdatesPending.setStatus("current")
_BwNSXSAvgUpdateTime_Type = Gauge32
_BwNSXSAvgUpdateTime_Object = MibScalar
bwNSXSAvgUpdateTime = _BwNSXSAvgUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 6),
    _BwNSXSAvgUpdateTime_Type()
)
bwNSXSAvgUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSAvgUpdateTime.setStatus("current")
_BwNSXSAvgRowsUpdated_Type = Gauge32
_BwNSXSAvgRowsUpdated_Object = MibScalar
bwNSXSAvgRowsUpdated = _BwNSXSAvgRowsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 7),
    _BwNSXSAvgRowsUpdated_Type()
)
bwNSXSAvgRowsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSAvgRowsUpdated.setStatus("current")
_BwNSXSAvgQueryTime_Type = Gauge32
_BwNSXSAvgQueryTime_Object = MibScalar
bwNSXSAvgQueryTime = _BwNSXSAvgQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 8),
    _BwNSXSAvgQueryTime_Type()
)
bwNSXSAvgQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSAvgQueryTime.setStatus("current")
_BwNSXSAvgRowsQueried_Type = Gauge32
_BwNSXSAvgRowsQueried_Object = MibScalar
bwNSXSAvgRowsQueried = _BwNSXSAvgRowsQueried_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 9),
    _BwNSXSAvgRowsQueried_Type()
)
bwNSXSAvgRowsQueried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSAvgRowsQueried.setStatus("current")
_BwNSXSUpdateCount_Type = Counter32
_BwNSXSUpdateCount_Object = MibScalar
bwNSXSUpdateCount = _BwNSXSUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 10),
    _BwNSXSUpdateCount_Type()
)
bwNSXSUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSUpdateCount.setStatus("current")
_BwNSXSQueryCount_Type = Counter32
_BwNSXSQueryCount_Object = MibScalar
bwNSXSQueryCount = _BwNSXSQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 11),
    _BwNSXSQueryCount_Type()
)
bwNSXSQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSQueryCount.setStatus("current")
_BwNSXSTTHWMTable_Object = MibTable
bwNSXSTTHWMTable = _BwNSXSTTHWMTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12)
)
if mibBuilder.loadTexts:
    bwNSXSTTHWMTable.setStatus("current")
_BwNSXSTTHWMEntry_Object = MibTableRow
bwNSXSTTHWMEntry = _BwNSXSTTHWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1)
)
bwNSXSTTHWMEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSXSTTHWMIndex"),
)
if mibBuilder.loadTexts:
    bwNSXSTTHWMEntry.setStatus("current")
_BwNSXSTTHWMIndex_Type = Unsigned32
_BwNSXSTTHWMIndex_Object = MibScalar
bwNSXSTTHWMIndex = _BwNSXSTTHWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1, 1),
    _BwNSXSTTHWMIndex_Type()
)
bwNSXSTTHWMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTTHWMIndex.setStatus("current")
_BwNSXSTTHWMName_Type = DisplayString
_BwNSXSTTHWMName_Object = MibTableColumn
bwNSXSTTHWMName = _BwNSXSTTHWMName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1, 2),
    _BwNSXSTTHWMName_Type()
)
bwNSXSTTHWMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSTTHWMName.setStatus("current")
_BwNSXSTTHWMValue_Type = Gauge32
_BwNSXSTTHWMValue_Object = MibTableColumn
bwNSXSTTHWMValue = _BwNSXSTTHWMValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1, 3),
    _BwNSXSTTHWMValue_Type()
)
bwNSXSTTHWMValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTTHWMValue.setStatus("current")
_BwNSXSTTHWMTimestamp_Type = DisplayString
_BwNSXSTTHWMTimestamp_Object = MibTableColumn
bwNSXSTTHWMTimestamp = _BwNSXSTTHWMTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1, 4),
    _BwNSXSTTHWMTimestamp_Type()
)
bwNSXSTTHWMTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTTHWMTimestamp.setStatus("current")
_BwNSXSTTHWMStackTrace_Type = DisplayString
_BwNSXSTTHWMStackTrace_Object = MibTableColumn
bwNSXSTTHWMStackTrace = _BwNSXSTTHWMStackTrace_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 1, 12, 1, 5),
    _BwNSXSTTHWMStackTrace_Type()
)
bwNSXSTTHWMStackTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSTTHWMStackTrace.setStatus("current")
_PerNSNbOpenedTransactions_Type = Counter32
_PerNSNbOpenedTransactions_Object = MibScalar
perNSNbOpenedTransactions = _PerNSNbOpenedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 2),
    _PerNSNbOpenedTransactions_Type()
)
perNSNbOpenedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perNSNbOpenedTransactions.setStatus("current")
_PerNSNbCommittedTransactions_Type = Counter32
_PerNSNbCommittedTransactions_Object = MibScalar
perNSNbCommittedTransactions = _PerNSNbCommittedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 3),
    _PerNSNbCommittedTransactions_Type()
)
perNSNbCommittedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perNSNbCommittedTransactions.setStatus("current")
_PerNSNbFailedTransactions_Type = Counter32
_PerNSNbFailedTransactions_Object = MibScalar
perNSNbFailedTransactions = _PerNSNbFailedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 4),
    _PerNSNbFailedTransactions_Type()
)
perNSNbFailedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perNSNbFailedTransactions.setStatus("current")
_PerNSNbCriticalErrors_Type = Counter32
_PerNSNbCriticalErrors_Object = MibScalar
perNSNbCriticalErrors = _PerNSNbCriticalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 4, 5),
    _PerNSNbCriticalErrors_Type()
)
perNSNbCriticalErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perNSNbCriticalErrors.setStatus("current")
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 5)
)
_ResetAllNSCounters_Type = Counter32
_ResetAllNSCounters_Object = MibScalar
resetAllNSCounters = _ResetAllNSCounters_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 5, 1),
    _ResetAllNSCounters_Type()
)
resetAllNSCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetAllNSCounters.setStatus("current")
_ServiceControlProxy_ObjectIdentity = ObjectIdentity
serviceControlProxy = _ServiceControlProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6)
)
_ScpSystemModule_ObjectIdentity = ObjectIdentity
scpSystemModule = _ScpSystemModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 1)
)
_BwSCProxyStatsACLViolationCount_Type = Counter32
_BwSCProxyStatsACLViolationCount_Object = MibScalar
bwSCProxyStatsACLViolationCount = _BwSCProxyStatsACLViolationCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 1, 1),
    _BwSCProxyStatsACLViolationCount_Type()
)
bwSCProxyStatsACLViolationCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsACLViolationCount.setStatus("current")
_BwSCProxyStatsSCPMessageIns_Type = Counter32
_BwSCProxyStatsSCPMessageIns_Object = MibScalar
bwSCProxyStatsSCPMessageIns = _BwSCProxyStatsSCPMessageIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 1, 2),
    _BwSCProxyStatsSCPMessageIns_Type()
)
bwSCProxyStatsSCPMessageIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsSCPMessageIns.setStatus("current")
_BwSCProxyStatsSCPMessageOuts_Type = Counter32
_BwSCProxyStatsSCPMessageOuts_Object = MibScalar
bwSCProxyStatsSCPMessageOuts = _BwSCProxyStatsSCPMessageOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 1, 3),
    _BwSCProxyStatsSCPMessageOuts_Type()
)
bwSCProxyStatsSCPMessageOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsSCPMessageOuts.setStatus("current")
_BwSCProxyStatsSCPMessageErrors_Type = Counter32
_BwSCProxyStatsSCPMessageErrors_Object = MibScalar
bwSCProxyStatsSCPMessageErrors = _BwSCProxyStatsSCPMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 1, 4),
    _BwSCProxyStatsSCPMessageErrors_Type()
)
bwSCProxyStatsSCPMessageErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsSCPMessageErrors.setStatus("current")
_ScpCapModule_ObjectIdentity = ObjectIdentity
scpCapModule = _ScpCapModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2)
)
_BwSCProxyStatsASTable_Object = MibTable
bwSCProxyStatsASTable = _BwSCProxyStatsASTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    bwSCProxyStatsASTable.setStatus("current")
_BwSCProxyStatsASEntry_Object = MibTableRow
bwSCProxyStatsASEntry = _BwSCProxyStatsASEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1)
)
bwSCProxyStatsASEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwSCProxyStatsASIndex"),
)
if mibBuilder.loadTexts:
    bwSCProxyStatsASEntry.setStatus("current")
_BwSCProxyStatsASIndex_Type = Unsigned32
_BwSCProxyStatsASIndex_Object = MibTableColumn
bwSCProxyStatsASIndex = _BwSCProxyStatsASIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1, 1),
    _BwSCProxyStatsASIndex_Type()
)
bwSCProxyStatsASIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwSCProxyStatsASIndex.setStatus("current")
_BwSCProxyStatsASAddr_Type = DisplayString
_BwSCProxyStatsASAddr_Object = MibTableColumn
bwSCProxyStatsASAddr = _BwSCProxyStatsASAddr_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1, 2),
    _BwSCProxyStatsASAddr_Type()
)
bwSCProxyStatsASAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSCProxyStatsASAddr.setStatus("current")
_BwSCProxyStatsASMessageIns_Type = Counter32
_BwSCProxyStatsASMessageIns_Object = MibTableColumn
bwSCProxyStatsASMessageIns = _BwSCProxyStatsASMessageIns_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1, 3),
    _BwSCProxyStatsASMessageIns_Type()
)
bwSCProxyStatsASMessageIns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsASMessageIns.setStatus("current")
_BwSCProxyStatsASMessageOuts_Type = Counter32
_BwSCProxyStatsASMessageOuts_Object = MibTableColumn
bwSCProxyStatsASMessageOuts = _BwSCProxyStatsASMessageOuts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1, 4),
    _BwSCProxyStatsASMessageOuts_Type()
)
bwSCProxyStatsASMessageOuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsASMessageOuts.setStatus("current")
_BwSCProxyStatsASMessageErrors_Type = Counter32
_BwSCProxyStatsASMessageErrors_Object = MibTableColumn
bwSCProxyStatsASMessageErrors = _BwSCProxyStatsASMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 6, 2, 1, 1, 5),
    _BwSCProxyStatsASMessageErrors_Type()
)
bwSCProxyStatsASMessageErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSCProxyStatsASMessageErrors.setStatus("current")
_Concurrent_ObjectIdentity = ObjectIdentity
concurrent = _Concurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7)
)
_BwNSXSMonitoringExecutorTable_Object = MibTable
bwNSXSMonitoringExecutorTable = _BwNSXSMonitoringExecutorTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1)
)
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorTable.setStatus("current")
_BwNSXSMonitoringExecutorEntry_Object = MibTableRow
bwNSXSMonitoringExecutorEntry = _BwNSXSMonitoringExecutorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1)
)
bwNSXSMonitoringExecutorEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorIndex"),
)
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorEntry.setStatus("current")
_BwNSXSMonitoringExecutorIndex_Type = Unsigned32
_BwNSXSMonitoringExecutorIndex_Object = MibTableColumn
bwNSXSMonitoringExecutorIndex = _BwNSXSMonitoringExecutorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 1),
    _BwNSXSMonitoringExecutorIndex_Type()
)
bwNSXSMonitoringExecutorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorIndex.setStatus("current")
_BwNSXSMonitoringExecutorName_Type = DisplayString
_BwNSXSMonitoringExecutorName_Object = MibTableColumn
bwNSXSMonitoringExecutorName = _BwNSXSMonitoringExecutorName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 2),
    _BwNSXSMonitoringExecutorName_Type()
)
bwNSXSMonitoringExecutorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorName.setStatus("current")
_BwNSXSMonitoringExecutorCurrentPoolSize_Type = Gauge32
_BwNSXSMonitoringExecutorCurrentPoolSize_Object = MibTableColumn
bwNSXSMonitoringExecutorCurrentPoolSize = _BwNSXSMonitoringExecutorCurrentPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 3),
    _BwNSXSMonitoringExecutorCurrentPoolSize_Type()
)
bwNSXSMonitoringExecutorCurrentPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorCurrentPoolSize.setStatus("current")
_BwNSXSMonitoringExecutorMaxPoolSize_Type = Gauge32
_BwNSXSMonitoringExecutorMaxPoolSize_Object = MibTableColumn
bwNSXSMonitoringExecutorMaxPoolSize = _BwNSXSMonitoringExecutorMaxPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 4),
    _BwNSXSMonitoringExecutorMaxPoolSize_Type()
)
bwNSXSMonitoringExecutorMaxPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorMaxPoolSize.setStatus("current")
_BwNSXSMonitoringExecutorAvgActiveThreads_Type = Gauge32
_BwNSXSMonitoringExecutorAvgActiveThreads_Object = MibTableColumn
bwNSXSMonitoringExecutorAvgActiveThreads = _BwNSXSMonitoringExecutorAvgActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 5),
    _BwNSXSMonitoringExecutorAvgActiveThreads_Type()
)
bwNSXSMonitoringExecutorAvgActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorAvgActiveThreads.setStatus("current")
_BwNSXSMonitoringExecutorTaskQueueSize_Type = Gauge32
_BwNSXSMonitoringExecutorTaskQueueSize_Object = MibTableColumn
bwNSXSMonitoringExecutorTaskQueueSize = _BwNSXSMonitoringExecutorTaskQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 6),
    _BwNSXSMonitoringExecutorTaskQueueSize_Type()
)
bwNSXSMonitoringExecutorTaskQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorTaskQueueSize.setStatus("current")
_BwNSXSMonitoringExecutorNbTasksRun_Type = Counter32
_BwNSXSMonitoringExecutorNbTasksRun_Object = MibTableColumn
bwNSXSMonitoringExecutorNbTasksRun = _BwNSXSMonitoringExecutorNbTasksRun_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 7),
    _BwNSXSMonitoringExecutorNbTasksRun_Type()
)
bwNSXSMonitoringExecutorNbTasksRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorNbTasksRun.setStatus("current")
_BwNSXSMonitoringExecutorNbWarnings_Type = Counter32
_BwNSXSMonitoringExecutorNbWarnings_Object = MibTableColumn
bwNSXSMonitoringExecutorNbWarnings = _BwNSXSMonitoringExecutorNbWarnings_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 8),
    _BwNSXSMonitoringExecutorNbWarnings_Type()
)
bwNSXSMonitoringExecutorNbWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorNbWarnings.setStatus("current")
_BwNSXSMonitoringExecutorNbErrors_Type = Counter32
_BwNSXSMonitoringExecutorNbErrors_Object = MibTableColumn
bwNSXSMonitoringExecutorNbErrors = _BwNSXSMonitoringExecutorNbErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 9),
    _BwNSXSMonitoringExecutorNbErrors_Type()
)
bwNSXSMonitoringExecutorNbErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorNbErrors.setStatus("current")
_BwNSXSMonitoringExecutorLongestTaskMs_Type = Gauge32
_BwNSXSMonitoringExecutorLongestTaskMs_Object = MibTableColumn
bwNSXSMonitoringExecutorLongestTaskMs = _BwNSXSMonitoringExecutorLongestTaskMs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 10),
    _BwNSXSMonitoringExecutorLongestTaskMs_Type()
)
bwNSXSMonitoringExecutorLongestTaskMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorLongestTaskMs.setStatus("current")
_BwNSXSMonitoringExecutorLongestTaskName_Type = DisplayString
_BwNSXSMonitoringExecutorLongestTaskName_Object = MibTableColumn
bwNSXSMonitoringExecutorLongestTaskName = _BwNSXSMonitoringExecutorLongestTaskName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 7, 1, 1, 11),
    _BwNSXSMonitoringExecutorLongestTaskName_Type()
)
bwNSXSMonitoringExecutorLongestTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSXSMonitoringExecutorLongestTaskName.setStatus("current")
_BwNSMibConformance_ObjectIdentity = ObjectIdentity
bwNSMibConformance = _BwNSMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100)
)
_BwNSMibGroups_ObjectIdentity = ObjectIdentity
bwNSMibGroups = _BwNSMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1)
)
_BwNSMibCompliancy_ObjectIdentity = ObjectIdentity
bwNSMibCompliancy = _BwNSMibCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 2)
)
_NsProvisioningServer_ObjectIdentity = ObjectIdentity
nsProvisioningServer = _NsProvisioningServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9)
)
_PsSystem_ObjectIdentity = ObjectIdentity
psSystem = _PsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1)
)
_SystemNbGrps_Type = Gauge32
_SystemNbGrps_Object = MibScalar
systemNbGrps = _SystemNbGrps_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 1),
    _SystemNbGrps_Type()
)
systemNbGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbGrps.setStatus("current")
_SystemNbDNs_Type = Gauge32
_SystemNbDNs_Object = MibScalar
systemNbDNs = _SystemNbDNs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 2),
    _SystemNbDNs_Type()
)
systemNbDNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbDNs.setStatus("current")
_SystemNbURLs_Type = Gauge32
_SystemNbURLs_Object = MibScalar
systemNbURLs = _SystemNbURLs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 3),
    _SystemNbURLs_Type()
)
systemNbURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbURLs.setStatus("current")
_SystemNbProfiles_Type = Gauge32
_SystemNbProfiles_Object = MibScalar
systemNbProfiles = _SystemNbProfiles_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 4),
    _SystemNbProfiles_Type()
)
systemNbProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbProfiles.setStatus("current")
_SystemNbRoutingNEs_Type = Gauge32
_SystemNbRoutingNEs_Object = MibScalar
systemNbRoutingNEs = _SystemNbRoutingNEs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 5),
    _SystemNbRoutingNEs_Type()
)
systemNbRoutingNEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbRoutingNEs.setStatus("current")
_SystemNbResourceNEs_Type = Gauge32
_SystemNbResourceNEs_Object = MibScalar
systemNbResourceNEs = _SystemNbResourceNEs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 6),
    _SystemNbResourceNEs_Type()
)
systemNbResourceNEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbResourceNEs.setStatus("current")
_SystemNbEnterprises_Type = Gauge32
_SystemNbEnterprises_Object = MibScalar
systemNbEnterprises = _SystemNbEnterprises_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 7),
    _SystemNbEnterprises_Type()
)
systemNbEnterprises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbEnterprises.setStatus("current")
_SystemNbUnassignedDNs_Type = Gauge32
_SystemNbUnassignedDNs_Object = MibScalar
systemNbUnassignedDNs = _SystemNbUnassignedDNs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 8),
    _SystemNbUnassignedDNs_Type()
)
systemNbUnassignedDNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbUnassignedDNs.setStatus("current")
_SystemNbExts_Type = Gauge32
_SystemNbExts_Object = MibScalar
systemNbExts = _SystemNbExts_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 9),
    _SystemNbExts_Type()
)
systemNbExts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbExts.setStatus("current")
_SystemNbSites_Type = Gauge32
_SystemNbSites_Object = MibScalar
systemNbSites = _SystemNbSites_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 10),
    _SystemNbSites_Type()
)
systemNbSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbSites.setStatus("current")
_SystemNbHostingNes_Type = Gauge32
_SystemNbHostingNes_Object = MibScalar
systemNbHostingNes = _SystemNbHostingNes_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 1, 11),
    _SystemNbHostingNes_Type()
)
systemNbHostingNes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemNbHostingNes.setStatus("current")
_PsProtocol_ObjectIdentity = ObjectIdentity
psProtocol = _PsProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3)
)
_SynchAPI_ObjectIdentity = ObjectIdentity
synchAPI = _SynchAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3)
)
_SyncNbUpdatesRequests_Type = Counter32
_SyncNbUpdatesRequests_Object = MibScalar
syncNbUpdatesRequests = _SyncNbUpdatesRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3, 1),
    _SyncNbUpdatesRequests_Type()
)
syncNbUpdatesRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncNbUpdatesRequests.setStatus("current")
_SyncNbUpdatesRequestsFailures_Type = Counter32
_SyncNbUpdatesRequestsFailures_Object = MibScalar
syncNbUpdatesRequestsFailures = _SyncNbUpdatesRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3, 2),
    _SyncNbUpdatesRequestsFailures_Type()
)
syncNbUpdatesRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncNbUpdatesRequestsFailures.setStatus("current")
_SyncNbOpenedSessions_Type = Counter32
_SyncNbOpenedSessions_Object = MibScalar
syncNbOpenedSessions = _SyncNbOpenedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3, 3),
    _SyncNbOpenedSessions_Type()
)
syncNbOpenedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncNbOpenedSessions.setStatus("current")
_SyncNbAuthorizationFailures_Type = Counter32
_SyncNbAuthorizationFailures_Object = MibScalar
syncNbAuthorizationFailures = _SyncNbAuthorizationFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3, 4),
    _SyncNbAuthorizationFailures_Type()
)
syncNbAuthorizationFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncNbAuthorizationFailures.setStatus("current")
_SyncNbActiveSessions_Type = Gauge32
_SyncNbActiveSessions_Object = MibScalar
syncNbActiveSessions = _SyncNbActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 3, 5),
    _SyncNbActiveSessions_Type()
)
syncNbActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncNbActiveSessions.setStatus("current")
_Oamp_ObjectIdentity = ObjectIdentity
oamp = _Oamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 4)
)
_OampNbActiveSessions_Type = Gauge32
_OampNbActiveSessions_Object = MibScalar
oampNbActiveSessions = _OampNbActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 4, 1),
    _OampNbActiveSessions_Type()
)
oampNbActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oampNbActiveSessions.setStatus("current")
_Oss_ObjectIdentity = ObjectIdentity
oss = _Oss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5)
)
_OssNbUpdatesRequests_Type = Counter32
_OssNbUpdatesRequests_Object = MibScalar
ossNbUpdatesRequests = _OssNbUpdatesRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 1),
    _OssNbUpdatesRequests_Type()
)
ossNbUpdatesRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbUpdatesRequests.setStatus("current")
_OssNbUpdatesRequestsFailures_Type = Counter32
_OssNbUpdatesRequestsFailures_Object = MibScalar
ossNbUpdatesRequestsFailures = _OssNbUpdatesRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 2),
    _OssNbUpdatesRequestsFailures_Type()
)
ossNbUpdatesRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbUpdatesRequestsFailures.setStatus("current")
_OssNbQueriesRequests_Type = Counter32
_OssNbQueriesRequests_Object = MibScalar
ossNbQueriesRequests = _OssNbQueriesRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 3),
    _OssNbQueriesRequests_Type()
)
ossNbQueriesRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbQueriesRequests.setStatus("current")
_OssNbQueriesRequestsFailures_Type = Counter32
_OssNbQueriesRequestsFailures_Object = MibScalar
ossNbQueriesRequestsFailures = _OssNbQueriesRequestsFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 4),
    _OssNbQueriesRequestsFailures_Type()
)
ossNbQueriesRequestsFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbQueriesRequestsFailures.setStatus("current")
_OssNbOpenedSessions_Type = Counter32
_OssNbOpenedSessions_Object = MibScalar
ossNbOpenedSessions = _OssNbOpenedSessions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 5),
    _OssNbOpenedSessions_Type()
)
ossNbOpenedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbOpenedSessions.setStatus("current")
_OssNbAuthorizationFailures_Type = Counter32
_OssNbAuthorizationFailures_Object = MibScalar
ossNbAuthorizationFailures = _OssNbAuthorizationFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 6),
    _OssNbAuthorizationFailures_Type()
)
ossNbAuthorizationFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ossNbAuthorizationFailures.setStatus("current")
_OssNbActiveSessions_Type = Gauge32
_OssNbActiveSessions_Object = MibScalar
ossNbActiveSessions = _OssNbActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 5, 7),
    _OssNbActiveSessions_Type()
)
ossNbActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ossNbActiveSessions.setStatus("current")
_NsPSCommonCommStats_ObjectIdentity = ObjectIdentity
nsPSCommonCommStats = _NsPSCommonCommStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6)
)
_BwNSCommonCommPSStatsTable_Object = MibTable
bwNSCommonCommPSStatsTable = _BwNSCommonCommPSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1)
)
if mibBuilder.loadTexts:
    bwNSCommonCommPSStatsTable.setStatus("current")
_BwNSCommonCommPSStatsEntry_Object = MibTableRow
bwNSCommonCommPSStatsEntry = _BwNSCommonCommPSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1)
)
bwNSCommonCommPSStatsEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSCommonCommPSStatsIndex"),
)
if mibBuilder.loadTexts:
    bwNSCommonCommPSStatsEntry.setStatus("current")
_BwNSCommonCommPSStatsIndex_Type = Unsigned32
_BwNSCommonCommPSStatsIndex_Object = MibTableColumn
bwNSCommonCommPSStatsIndex = _BwNSCommonCommPSStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 1),
    _BwNSCommonCommPSStatsIndex_Type()
)
bwNSCommonCommPSStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommPSStatsIndex.setStatus("current")
_BwNSCommonCommPSHost_Type = DisplayString
_BwNSCommonCommPSHost_Object = MibTableColumn
bwNSCommonCommPSHost = _BwNSCommonCommPSHost_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 2),
    _BwNSCommonCommPSHost_Type()
)
bwNSCommonCommPSHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommPSHost.setStatus("current")
_BwNSCommonCommPSInterface_Type = DisplayString
_BwNSCommonCommPSInterface_Object = MibTableColumn
bwNSCommonCommPSInterface = _BwNSCommonCommPSInterface_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 3),
    _BwNSCommonCommPSInterface_Type()
)
bwNSCommonCommPSInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommPSInterface.setStatus("current")
_BwNSCommonCommPSProtocol_Type = DisplayString
_BwNSCommonCommPSProtocol_Object = MibTableColumn
bwNSCommonCommPSProtocol = _BwNSCommonCommPSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 4),
    _BwNSCommonCommPSProtocol_Type()
)
bwNSCommonCommPSProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSCommonCommPSProtocol.setStatus("current")
_BwNSCommonCommPSAcceptedOutboundConnections_Type = Counter32
_BwNSCommonCommPSAcceptedOutboundConnections_Object = MibTableColumn
bwNSCommonCommPSAcceptedOutboundConnections = _BwNSCommonCommPSAcceptedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 5),
    _BwNSCommonCommPSAcceptedOutboundConnections_Type()
)
bwNSCommonCommPSAcceptedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSAcceptedOutboundConnections.setStatus("current")
_BwNSCommonCommPSAcceptedInboundConnections_Type = Counter32
_BwNSCommonCommPSAcceptedInboundConnections_Object = MibTableColumn
bwNSCommonCommPSAcceptedInboundConnections = _BwNSCommonCommPSAcceptedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 6),
    _BwNSCommonCommPSAcceptedInboundConnections_Type()
)
bwNSCommonCommPSAcceptedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSAcceptedInboundConnections.setStatus("current")
_BwNSCommonCommPSRejectedOutboundConnections_Type = Counter32
_BwNSCommonCommPSRejectedOutboundConnections_Object = MibTableColumn
bwNSCommonCommPSRejectedOutboundConnections = _BwNSCommonCommPSRejectedOutboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 7),
    _BwNSCommonCommPSRejectedOutboundConnections_Type()
)
bwNSCommonCommPSRejectedOutboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSRejectedOutboundConnections.setStatus("current")
_BwNSCommonCommPSRejectedInboundConnections_Type = Counter32
_BwNSCommonCommPSRejectedInboundConnections_Object = MibTableColumn
bwNSCommonCommPSRejectedInboundConnections = _BwNSCommonCommPSRejectedInboundConnections_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 8),
    _BwNSCommonCommPSRejectedInboundConnections_Type()
)
bwNSCommonCommPSRejectedInboundConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSRejectedInboundConnections.setStatus("current")
_BwNSCommonCommPSOutputMessagesProcessed_Type = Counter32
_BwNSCommonCommPSOutputMessagesProcessed_Object = MibTableColumn
bwNSCommonCommPSOutputMessagesProcessed = _BwNSCommonCommPSOutputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 9),
    _BwNSCommonCommPSOutputMessagesProcessed_Type()
)
bwNSCommonCommPSOutputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSOutputMessagesProcessed.setStatus("current")
_BwNSCommonCommPSInputMessagesProcessed_Type = Counter32
_BwNSCommonCommPSInputMessagesProcessed_Object = MibTableColumn
bwNSCommonCommPSInputMessagesProcessed = _BwNSCommonCommPSInputMessagesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 10),
    _BwNSCommonCommPSInputMessagesProcessed_Type()
)
bwNSCommonCommPSInputMessagesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSInputMessagesProcessed.setStatus("current")
_BwNSCommonCommPSOutputCommunicationErrors_Type = Counter32
_BwNSCommonCommPSOutputCommunicationErrors_Object = MibTableColumn
bwNSCommonCommPSOutputCommunicationErrors = _BwNSCommonCommPSOutputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 11),
    _BwNSCommonCommPSOutputCommunicationErrors_Type()
)
bwNSCommonCommPSOutputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSOutputCommunicationErrors.setStatus("current")
_BwNSCommonCommPSInputCommunicationErrors_Type = Counter32
_BwNSCommonCommPSInputCommunicationErrors_Object = MibTableColumn
bwNSCommonCommPSInputCommunicationErrors = _BwNSCommonCommPSInputCommunicationErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 6, 1, 1, 12),
    _BwNSCommonCommPSInputCommunicationErrors_Type()
)
bwNSCommonCommPSInputCommunicationErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSCommonCommPSInputCommunicationErrors.setStatus("current")
_NsTcp_ObjectIdentity = ObjectIdentity
nsTcp = _NsTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7)
)
_BwNSPSTcpServersStatsTable_Object = MibTable
bwNSPSTcpServersStatsTable = _BwNSPSTcpServersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1)
)
if mibBuilder.loadTexts:
    bwNSPSTcpServersStatsTable.setStatus("current")
_BwNSPSTcpServersStatsEntry_Object = MibTableRow
bwNSPSTcpServersStatsEntry = _BwNSPSTcpServersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1)
)
bwNSPSTcpServersStatsEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSPSTcpServersStatsIndex"),
)
if mibBuilder.loadTexts:
    bwNSPSTcpServersStatsEntry.setStatus("current")
_BwNSPSTcpServersStatsIndex_Type = Unsigned32
_BwNSPSTcpServersStatsIndex_Object = MibTableColumn
bwNSPSTcpServersStatsIndex = _BwNSPSTcpServersStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 1),
    _BwNSPSTcpServersStatsIndex_Type()
)
bwNSPSTcpServersStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTcpServersStatsIndex.setStatus("current")
_BwNSPSTcpServersName_Type = DisplayString
_BwNSPSTcpServersName_Object = MibTableColumn
bwNSPSTcpServersName = _BwNSPSTcpServersName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 2),
    _BwNSPSTcpServersName_Type()
)
bwNSPSTcpServersName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTcpServersName.setStatus("current")
_BwNSPSTcpServersNbConnectionsAccepted_Type = Counter32
_BwNSPSTcpServersNbConnectionsAccepted_Object = MibTableColumn
bwNSPSTcpServersNbConnectionsAccepted = _BwNSPSTcpServersNbConnectionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 3),
    _BwNSPSTcpServersNbConnectionsAccepted_Type()
)
bwNSPSTcpServersNbConnectionsAccepted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbConnectionsAccepted.setStatus("current")
_BwNSPSTcpServersNbConnectionsRefused_Type = Counter32
_BwNSPSTcpServersNbConnectionsRefused_Object = MibTableColumn
bwNSPSTcpServersNbConnectionsRefused = _BwNSPSTcpServersNbConnectionsRefused_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 4),
    _BwNSPSTcpServersNbConnectionsRefused_Type()
)
bwNSPSTcpServersNbConnectionsRefused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbConnectionsRefused.setStatus("current")
_BwNSPSTcpServersNbConnectionsInitiated_Type = Counter32
_BwNSPSTcpServersNbConnectionsInitiated_Object = MibTableColumn
bwNSPSTcpServersNbConnectionsInitiated = _BwNSPSTcpServersNbConnectionsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 5),
    _BwNSPSTcpServersNbConnectionsInitiated_Type()
)
bwNSPSTcpServersNbConnectionsInitiated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbConnectionsInitiated.setStatus("current")
_BwNSPSTcpServersNbConnectionsClosed_Type = Counter32
_BwNSPSTcpServersNbConnectionsClosed_Object = MibTableColumn
bwNSPSTcpServersNbConnectionsClosed = _BwNSPSTcpServersNbConnectionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 6),
    _BwNSPSTcpServersNbConnectionsClosed_Type()
)
bwNSPSTcpServersNbConnectionsClosed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbConnectionsClosed.setStatus("current")
_BwNSPSTcpServersNbBytesSent_Type = Gauge32
_BwNSPSTcpServersNbBytesSent_Object = MibTableColumn
bwNSPSTcpServersNbBytesSent = _BwNSPSTcpServersNbBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 7),
    _BwNSPSTcpServersNbBytesSent_Type()
)
bwNSPSTcpServersNbBytesSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbBytesSent.setStatus("current")
_BwNSPSTcpServersNbBytesReceived_Type = Gauge32
_BwNSPSTcpServersNbBytesReceived_Object = MibTableColumn
bwNSPSTcpServersNbBytesReceived = _BwNSPSTcpServersNbBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 8),
    _BwNSPSTcpServersNbBytesReceived_Type()
)
bwNSPSTcpServersNbBytesReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbBytesReceived.setStatus("current")
_BwNSPSTcpServersOutgoingQueueSize_Type = Gauge32
_BwNSPSTcpServersOutgoingQueueSize_Object = MibTableColumn
bwNSPSTcpServersOutgoingQueueSize = _BwNSPSTcpServersOutgoingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 9),
    _BwNSPSTcpServersOutgoingQueueSize_Type()
)
bwNSPSTcpServersOutgoingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTcpServersOutgoingQueueSize.setStatus("current")
_BwNSPSTcpServersIncomingQueueSize_Type = Gauge32
_BwNSPSTcpServersIncomingQueueSize_Object = MibTableColumn
bwNSPSTcpServersIncomingQueueSize = _BwNSPSTcpServersIncomingQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 10),
    _BwNSPSTcpServersIncomingQueueSize_Type()
)
bwNSPSTcpServersIncomingQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTcpServersIncomingQueueSize.setStatus("current")
_BwNSPSTcpServersNbBytesSentSecure_Type = Gauge32
_BwNSPSTcpServersNbBytesSentSecure_Object = MibTableColumn
bwNSPSTcpServersNbBytesSentSecure = _BwNSPSTcpServersNbBytesSentSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 11),
    _BwNSPSTcpServersNbBytesSentSecure_Type()
)
bwNSPSTcpServersNbBytesSentSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbBytesSentSecure.setStatus("current")
_BwNSPSTcpServersNbBytesReceivedSecure_Type = Gauge32
_BwNSPSTcpServersNbBytesReceivedSecure_Object = MibTableColumn
bwNSPSTcpServersNbBytesReceivedSecure = _BwNSPSTcpServersNbBytesReceivedSecure_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 3, 7, 1, 1, 12),
    _BwNSPSTcpServersNbBytesReceivedSecure_Type()
)
bwNSPSTcpServersNbBytesReceivedSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTcpServersNbBytesReceivedSecure.setStatus("current")
_PsPersistency_ObjectIdentity = ObjectIdentity
psPersistency = _PsPersistency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4)
)
_PsTimesTen_ObjectIdentity = ObjectIdentity
psTimesTen = _PsTimesTen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1)
)
_PsNSTtNbConnectionsCreated_Type = Counter32
_PsNSTtNbConnectionsCreated_Object = MibScalar
psNSTtNbConnectionsCreated = _PsNSTtNbConnectionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 1),
    _PsNSTtNbConnectionsCreated_Type()
)
psNSTtNbConnectionsCreated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSTtNbConnectionsCreated.setStatus("current")
_PsNSTtConnectionPoolSize_Type = Gauge32
_PsNSTtConnectionPoolSize_Object = MibScalar
psNSTtConnectionPoolSize = _PsNSTtConnectionPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 2),
    _PsNSTtConnectionPoolSize_Type()
)
psNSTtConnectionPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psNSTtConnectionPoolSize.setStatus("current")
_PsNSTtNbBackdoorUpdates_Type = Counter32
_PsNSTtNbBackdoorUpdates_Object = MibScalar
psNSTtNbBackdoorUpdates = _PsNSTtNbBackdoorUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 3),
    _PsNSTtNbBackdoorUpdates_Type()
)
psNSTtNbBackdoorUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSTtNbBackdoorUpdates.setStatus("obsolete")
_PsNSTtNbFailedCheckpoints_Type = Counter32
_PsNSTtNbFailedCheckpoints_Object = MibScalar
psNSTtNbFailedCheckpoints = _PsNSTtNbFailedCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 4),
    _PsNSTtNbFailedCheckpoints_Type()
)
psNSTtNbFailedCheckpoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSTtNbFailedCheckpoints.setStatus("obsolete")
_PsRemoteXla_ObjectIdentity = ObjectIdentity
psRemoteXla = _PsRemoteXla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 5)
)
_PsNSRemoteXlaNbTimesConnected_Type = Counter32
_PsNSRemoteXlaNbTimesConnected_Object = MibScalar
psNSRemoteXlaNbTimesConnected = _PsNSRemoteXlaNbTimesConnected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 5, 1),
    _PsNSRemoteXlaNbTimesConnected_Type()
)
psNSRemoteXlaNbTimesConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSRemoteXlaNbTimesConnected.setStatus("current")
_PsNSRemoteXlaNbTimesDisconnected_Type = Counter32
_PsNSRemoteXlaNbTimesDisconnected_Object = MibScalar
psNSRemoteXlaNbTimesDisconnected = _PsNSRemoteXlaNbTimesDisconnected_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 5, 2),
    _PsNSRemoteXlaNbTimesDisconnected_Type()
)
psNSRemoteXlaNbTimesDisconnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSRemoteXlaNbTimesDisconnected.setStatus("current")
_PsNSRemoteXlaUpdatesProcessed_Type = Counter32
_PsNSRemoteXlaUpdatesProcessed_Object = MibScalar
psNSRemoteXlaUpdatesProcessed = _PsNSRemoteXlaUpdatesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 5, 3),
    _PsNSRemoteXlaUpdatesProcessed_Type()
)
psNSRemoteXlaUpdatesProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSRemoteXlaUpdatesProcessed.setStatus("current")
_PsNSRemoteXlaUpdatesPending_Type = Gauge32
_PsNSRemoteXlaUpdatesPending_Object = MibScalar
psNSRemoteXlaUpdatesPending = _PsNSRemoteXlaUpdatesPending_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 5, 4),
    _PsNSRemoteXlaUpdatesPending_Type()
)
psNSRemoteXlaUpdatesPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSRemoteXlaUpdatesPending.setStatus("current")
_BwNSPSAvgUpdateTime_Type = Gauge32
_BwNSPSAvgUpdateTime_Object = MibScalar
bwNSPSAvgUpdateTime = _BwNSPSAvgUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 6),
    _BwNSPSAvgUpdateTime_Type()
)
bwNSPSAvgUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSAvgUpdateTime.setStatus("current")
_BwNSPSAvgRowsUpdated_Type = Gauge32
_BwNSPSAvgRowsUpdated_Object = MibScalar
bwNSPSAvgRowsUpdated = _BwNSPSAvgRowsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 7),
    _BwNSPSAvgRowsUpdated_Type()
)
bwNSPSAvgRowsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSAvgRowsUpdated.setStatus("current")
_BwNSPSAvgQueryTime_Type = Gauge32
_BwNSPSAvgQueryTime_Object = MibScalar
bwNSPSAvgQueryTime = _BwNSPSAvgQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 8),
    _BwNSPSAvgQueryTime_Type()
)
bwNSPSAvgQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSAvgQueryTime.setStatus("current")
_BwNSPSAvgRowsQueried_Type = Gauge32
_BwNSPSAvgRowsQueried_Object = MibScalar
bwNSPSAvgRowsQueried = _BwNSPSAvgRowsQueried_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 9),
    _BwNSPSAvgRowsQueried_Type()
)
bwNSPSAvgRowsQueried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSAvgRowsQueried.setStatus("current")
_BwNSPSUpdateCount_Type = Counter32
_BwNSPSUpdateCount_Object = MibScalar
bwNSPSUpdateCount = _BwNSPSUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 10),
    _BwNSPSUpdateCount_Type()
)
bwNSPSUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSUpdateCount.setStatus("current")
_BwNSPSQueryCount_Type = Counter32
_BwNSPSQueryCount_Object = MibScalar
bwNSPSQueryCount = _BwNSPSQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 11),
    _BwNSPSQueryCount_Type()
)
bwNSPSQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSQueryCount.setStatus("current")
_BwNSPSTTHWMTable_Object = MibTable
bwNSPSTTHWMTable = _BwNSPSTTHWMTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12)
)
if mibBuilder.loadTexts:
    bwNSPSTTHWMTable.setStatus("current")
_BwNSPSTTHWMEntry_Object = MibTableRow
bwNSPSTTHWMEntry = _BwNSPSTTHWMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1)
)
bwNSPSTTHWMEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSPSTTHWMIndex"),
)
if mibBuilder.loadTexts:
    bwNSPSTTHWMEntry.setStatus("current")
_BwNSPSTTHWMIndex_Type = Unsigned32
_BwNSPSTTHWMIndex_Object = MibTableColumn
bwNSPSTTHWMIndex = _BwNSPSTTHWMIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1, 1),
    _BwNSPSTTHWMIndex_Type()
)
bwNSPSTTHWMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTTHWMIndex.setStatus("current")
_BwNSPSTTHWMName_Type = DisplayString
_BwNSPSTTHWMName_Object = MibTableColumn
bwNSPSTTHWMName = _BwNSPSTTHWMName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1, 2),
    _BwNSPSTTHWMName_Type()
)
bwNSPSTTHWMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSTTHWMName.setStatus("current")
_BwNSPSTTHWMValue_Type = Gauge32
_BwNSPSTTHWMValue_Object = MibTableColumn
bwNSPSTTHWMValue = _BwNSPSTTHWMValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1, 3),
    _BwNSPSTTHWMValue_Type()
)
bwNSPSTTHWMValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTTHWMValue.setStatus("current")
_BwNSPSTTHWMTimestamp_Type = DisplayString
_BwNSPSTTHWMTimestamp_Object = MibTableColumn
bwNSPSTTHWMTimestamp = _BwNSPSTTHWMTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1, 4),
    _BwNSPSTTHWMTimestamp_Type()
)
bwNSPSTTHWMTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTTHWMTimestamp.setStatus("current")
_BwNSPSTTHWMStackTrace_Type = DisplayString
_BwNSPSTTHWMStackTrace_Object = MibTableColumn
bwNSPSTTHWMStackTrace = _BwNSPSTTHWMStackTrace_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 1, 12, 1, 5),
    _BwNSPSTTHWMStackTrace_Type()
)
bwNSPSTTHWMStackTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSTTHWMStackTrace.setStatus("current")
_PsNSPerNbOpenedTransactions_Type = Counter32
_PsNSPerNbOpenedTransactions_Object = MibScalar
psNSPerNbOpenedTransactions = _PsNSPerNbOpenedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 2),
    _PsNSPerNbOpenedTransactions_Type()
)
psNSPerNbOpenedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSPerNbOpenedTransactions.setStatus("current")
_PsNSPerNbCommittedTransactions_Type = Counter32
_PsNSPerNbCommittedTransactions_Object = MibScalar
psNSPerNbCommittedTransactions = _PsNSPerNbCommittedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 3),
    _PsNSPerNbCommittedTransactions_Type()
)
psNSPerNbCommittedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSPerNbCommittedTransactions.setStatus("current")
_PsNSPerNbFailedTransactions_Type = Counter32
_PsNSPerNbFailedTransactions_Object = MibScalar
psNSPerNbFailedTransactions = _PsNSPerNbFailedTransactions_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 4),
    _PsNSPerNbFailedTransactions_Type()
)
psNSPerNbFailedTransactions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSPerNbFailedTransactions.setStatus("current")
_PsNSPerNbCriticalErrors_Type = Counter32
_PsNSPerNbCriticalErrors_Object = MibScalar
psNSPerNbCriticalErrors = _PsNSPerNbCriticalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 4, 5),
    _PsNSPerNbCriticalErrors_Type()
)
psNSPerNbCriticalErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psNSPerNbCriticalErrors.setStatus("current")
_PsConcurrent_ObjectIdentity = ObjectIdentity
psConcurrent = _PsConcurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5)
)
_BwNSPSMonitoringExecutorTable_Object = MibTable
bwNSPSMonitoringExecutorTable = _BwNSPSMonitoringExecutorTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1)
)
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorTable.setStatus("current")
_BwNSPSMonitoringExecutorEntry_Object = MibTableRow
bwNSPSMonitoringExecutorEntry = _BwNSPSMonitoringExecutorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1)
)
bwNSPSMonitoringExecutorEntry.setIndexNames(
    (0, "BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorIndex"),
)
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorEntry.setStatus("current")
_BwNSPSMonitoringExecutorIndex_Type = Unsigned32
_BwNSPSMonitoringExecutorIndex_Object = MibTableColumn
bwNSPSMonitoringExecutorIndex = _BwNSPSMonitoringExecutorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 1),
    _BwNSPSMonitoringExecutorIndex_Type()
)
bwNSPSMonitoringExecutorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorIndex.setStatus("current")
_BwNSPSMonitoringExecutorName_Type = DisplayString
_BwNSPSMonitoringExecutorName_Object = MibTableColumn
bwNSPSMonitoringExecutorName = _BwNSPSMonitoringExecutorName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 2),
    _BwNSPSMonitoringExecutorName_Type()
)
bwNSPSMonitoringExecutorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorName.setStatus("current")
_BwNSPSMonitoringExecutorCurrentPoolSize_Type = Gauge32
_BwNSPSMonitoringExecutorCurrentPoolSize_Object = MibTableColumn
bwNSPSMonitoringExecutorCurrentPoolSize = _BwNSPSMonitoringExecutorCurrentPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 3),
    _BwNSPSMonitoringExecutorCurrentPoolSize_Type()
)
bwNSPSMonitoringExecutorCurrentPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorCurrentPoolSize.setStatus("current")
_BwNSPSMonitoringExecutorMaxPoolSize_Type = Gauge32
_BwNSPSMonitoringExecutorMaxPoolSize_Object = MibTableColumn
bwNSPSMonitoringExecutorMaxPoolSize = _BwNSPSMonitoringExecutorMaxPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 4),
    _BwNSPSMonitoringExecutorMaxPoolSize_Type()
)
bwNSPSMonitoringExecutorMaxPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorMaxPoolSize.setStatus("current")
_BwNSPSMonitoringExecutorAvgActiveThreads_Type = Gauge32
_BwNSPSMonitoringExecutorAvgActiveThreads_Object = MibTableColumn
bwNSPSMonitoringExecutorAvgActiveThreads = _BwNSPSMonitoringExecutorAvgActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 5),
    _BwNSPSMonitoringExecutorAvgActiveThreads_Type()
)
bwNSPSMonitoringExecutorAvgActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorAvgActiveThreads.setStatus("current")
_BwNSPSMonitoringExecutorTaskQueueSize_Type = Gauge32
_BwNSPSMonitoringExecutorTaskQueueSize_Object = MibTableColumn
bwNSPSMonitoringExecutorTaskQueueSize = _BwNSPSMonitoringExecutorTaskQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 6),
    _BwNSPSMonitoringExecutorTaskQueueSize_Type()
)
bwNSPSMonitoringExecutorTaskQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorTaskQueueSize.setStatus("current")
_BwNSPSMonitoringExecutorNbTasksRun_Type = Counter32
_BwNSPSMonitoringExecutorNbTasksRun_Object = MibTableColumn
bwNSPSMonitoringExecutorNbTasksRun = _BwNSPSMonitoringExecutorNbTasksRun_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 7),
    _BwNSPSMonitoringExecutorNbTasksRun_Type()
)
bwNSPSMonitoringExecutorNbTasksRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorNbTasksRun.setStatus("current")
_BwNSPSMonitoringExecutorNbWarnings_Type = Counter32
_BwNSPSMonitoringExecutorNbWarnings_Object = MibTableColumn
bwNSPSMonitoringExecutorNbWarnings = _BwNSPSMonitoringExecutorNbWarnings_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 8),
    _BwNSPSMonitoringExecutorNbWarnings_Type()
)
bwNSPSMonitoringExecutorNbWarnings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorNbWarnings.setStatus("current")
_BwNSPSMonitoringExecutorNbErrors_Type = Counter32
_BwNSPSMonitoringExecutorNbErrors_Object = MibTableColumn
bwNSPSMonitoringExecutorNbErrors = _BwNSPSMonitoringExecutorNbErrors_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 9),
    _BwNSPSMonitoringExecutorNbErrors_Type()
)
bwNSPSMonitoringExecutorNbErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorNbErrors.setStatus("current")
_BwNSPSMonitoringExecutorLongestTaskMs_Type = Gauge32
_BwNSPSMonitoringExecutorLongestTaskMs_Object = MibTableColumn
bwNSPSMonitoringExecutorLongestTaskMs = _BwNSPSMonitoringExecutorLongestTaskMs_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 10),
    _BwNSPSMonitoringExecutorLongestTaskMs_Type()
)
bwNSPSMonitoringExecutorLongestTaskMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorLongestTaskMs.setStatus("current")
_BwNSPSMonitoringExecutorLongestTaskName_Type = DisplayString
_BwNSPSMonitoringExecutorLongestTaskName_Object = MibTableColumn
bwNSPSMonitoringExecutorLongestTaskName = _BwNSPSMonitoringExecutorLongestTaskName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 9, 5, 1, 1, 11),
    _BwNSPSMonitoringExecutorLongestTaskName_Type()
)
bwNSPSMonitoringExecutorLongestTaskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwNSPSMonitoringExecutorLongestTaskName.setStatus("current")
_NetworkServer_ObjectIdentity = ObjectIdentity
networkServer = _NetworkServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11)
)
_NsProtocol_ObjectIdentity = ObjectIdentity
nsProtocol = _NsProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1)
)
_LocationApi_ObjectIdentity = ObjectIdentity
locationApi = _LocationApi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1, 1)
)
_BwUserLocationRequests_Type = Counter32
_BwUserLocationRequests_Object = MibScalar
bwUserLocationRequests = _BwUserLocationRequests_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1, 1, 1),
    _BwUserLocationRequests_Type()
)
bwUserLocationRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwUserLocationRequests.setStatus("current")
_BwUserLocationRequestSuccess_Type = Counter32
_BwUserLocationRequestSuccess_Object = MibScalar
bwUserLocationRequestSuccess = _BwUserLocationRequestSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1, 1, 2),
    _BwUserLocationRequestSuccess_Type()
)
bwUserLocationRequestSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwUserLocationRequestSuccess.setStatus("current")
_BwUserLocationRequestUnknownUser_Type = Counter32
_BwUserLocationRequestUnknownUser_Object = MibScalar
bwUserLocationRequestUnknownUser = _BwUserLocationRequestUnknownUser_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1, 1, 3),
    _BwUserLocationRequestUnknownUser_Type()
)
bwUserLocationRequestUnknownUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwUserLocationRequestUnknownUser.setStatus("current")
_BwUserLocationRequestFailures_Type = Counter32
_BwUserLocationRequestFailures_Object = MibScalar
bwUserLocationRequestFailures = _BwUserLocationRequestFailures_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 11, 1, 1, 4),
    _BwUserLocationRequestFailures_Type()
)
bwUserLocationRequestFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwUserLocationRequestFailures.setStatus("current")

# Managed Objects groups

bwNsLicensingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 1)
)
bwNsLicensingGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNbTimePeriodWithLicenseViolations"),
        ("BW-BroadworksNetworkServer", "bwNbTransactionInViolation"),
        ("BW-BroadworksNetworkServer", "bwNbThresholdAlarmSent"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueResets"))
)
if mibBuilder.loadTexts:
    bwNsLicensingGroup.setStatus("current")

bwNsSystemQueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 2)
)
bwNsSystemQueueStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueResets"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTable"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueIndex"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueName"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTimeAvg"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTimeMin"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTimeMax"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTimeMaxTimestampMSB"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueLengthCurrent"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueLengthAvg"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueLengthMax"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueLengthMaxTimestampMSB"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueLengthMaxTimestampLSB"),
        ("BW-BroadworksNetworkServer", "bwNSSystemInternalQueueTimeMaxTimestampLSB"))
)
if mibBuilder.loadTexts:
    bwNsSystemQueueStatsGroup.setStatus("current")

bwNsGenericPolicyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 3)
)
bwNsGenericPolicyStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "publicPolicyStatTable"),
        ("BW-BroadworksNetworkServer", "pubPolStatID"),
        ("BW-BroadworksNetworkServer", "pubPolStatPolicyName"),
        ("BW-BroadworksNetworkServer", "pubPolStatNbInstances"),
        ("BW-BroadworksNetworkServer", "pubPolStatNbRequests"),
        ("BW-BroadworksNetworkServer", "pubPolStatNbRequestsFailures"),
        ("BW-BroadworksNetworkServer", "pubPolStatNbRequestsResults"),
        ("BW-BroadworksNetworkServer", "privatePolicyStatTable"),
        ("BW-BroadworksNetworkServer", "privPolStatID"),
        ("BW-BroadworksNetworkServer", "privPolStatEnterpriseName"),
        ("BW-BroadworksNetworkServer", "privPolStatPolicyName"),
        ("BW-BroadworksNetworkServer", "privPolStatNbRequests"),
        ("BW-BroadworksNetworkServer", "privPolStatNbRequestsFailures"),
        ("BW-BroadworksNetworkServer", "privPolStatNbRequestsResults"),
        ("BW-BroadworksNetworkServer", "policyInfoTable"),
        ("BW-BroadworksNetworkServer", "polInfoID"),
        ("BW-BroadworksNetworkServer", "polInfoEnterpriseName"),
        ("BW-BroadworksNetworkServer", "polInfoPolicyName"),
        ("BW-BroadworksNetworkServer", "polInfoInfoName"),
        ("BW-BroadworksNetworkServer", "polInfoNbOccurences"),
        ("BW-BroadworksNetworkServer", "bwNbPolicyRequests"),
        ("BW-BroadworksNetworkServer", "bwNbPolicyRequestFailures"))
)
if mibBuilder.loadTexts:
    bwNsGenericPolicyStatsGroup.setStatus("current")

bwNsNeStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 4)
)
bwNsNeStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "neStatTable"),
        ("BW-BroadworksNetworkServer", "neStatID"),
        ("BW-BroadworksNetworkServer", "neStatName"),
        ("BW-BroadworksNetworkServer", "neStatNbSIPRequests"),
        ("BW-BroadworksNetworkServer", "neStatNbSIPRequestsFailures"),
        ("BW-BroadworksNetworkServer", "neStatNbMSSRequests"),
        ("BW-BroadworksNetworkServer", "neStatNbMSSRequestsFailures"))
)
if mibBuilder.loadTexts:
    bwNsNeStatsGroup.setStatus("current")

bwNsErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 5)
)
bwNsErrorStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "errorStatTable"),
        ("BW-BroadworksNetworkServer", "errorStatEntry"),
        ("BW-BroadworksNetworkServer", "errStatID"),
        ("BW-BroadworksNetworkServer", "errStatName"),
        ("BW-BroadworksNetworkServer", "errStatNbOccurences"))
)
if mibBuilder.loadTexts:
    bwNsErrorStatsGroup.setStatus("current")

bwNsCallPStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 6)
)
bwNsCallPStatsGroup.setObjects(
    ("BW-BroadworksNetworkServer", "bwNSCallpCallsPerSecond")
)
if mibBuilder.loadTexts:
    bwNsCallPStatsGroup.setStatus("current")

bwNsCarrierStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 7)
)
bwNsCarrierStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "carrierStatTable"),
        ("BW-BroadworksNetworkServer", "carrierStatEntry"),
        ("BW-BroadworksNetworkServer", "bwCarrierStatID"),
        ("BW-BroadworksNetworkServer", "bwCarrierName"),
        ("BW-BroadworksNetworkServer", "bwCarrierCic"),
        ("BW-BroadworksNetworkServer", "bwCarrierNbIntraLataCalls"),
        ("BW-BroadworksNetworkServer", "bwCarrierNbInterLataCalls"),
        ("BW-BroadworksNetworkServer", "bwCarrierNbInternationalCalls"))
)
if mibBuilder.loadTexts:
    bwNsCarrierStatsGroup.setStatus("current")

bwNsSipStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 8)
)
bwNsSipStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSSipStatsInviteIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsAckIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInviteResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsCancelIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsRegisterIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsNotifyIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsMessageIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInfoIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsOptionsIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsOptionsResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsRegisterResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInfoResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsNotifyResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsMessageResponsesTable"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsFailures"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsActiveTcpConnections"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsTcpIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsTcpOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsTcpFailures"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsUdpIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsUdpOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInviteResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInviteResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsOptionsResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsOptionsResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsOptionsResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsRegisterResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsRegisterResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsRegisterResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInfoResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInfoResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsInfoResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsNotifyResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsNotifyResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsNotifyResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsSubscribeResponseOuts"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsMessageResponseCodeValue"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsMessageResponseIns"),
        ("BW-BroadworksNetworkServer", "bwNSSipStatsMessageResponseOuts"))
)
if mibBuilder.loadTexts:
    bwNsSipStatsGroup.setStatus("current")

bwNsNrsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 9)
)
bwNsNrsStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSNbInvalidMessagesReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNbRequestsReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNbResponsesReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNbErrorsReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNbRequestsSent"),
        ("BW-BroadworksNetworkServer", "bwNSNbResponsesSent"),
        ("BW-BroadworksNetworkServer", "bwNSNbErrorsSent"),
        ("BW-BroadworksNetworkServer", "bwNSNbRequestsResent"),
        ("BW-BroadworksNetworkServer", "bwNSNbResponsesResent"),
        ("BW-BroadworksNetworkServer", "bwNSNbRequestsUnanswered"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTable"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableIndex"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableProtocolName"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbRequestsReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbResponsesReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbErrorsReceived"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbRequestsSent"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbResponsesSent"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbErrorsSent"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbRequestsResent"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbResponsesResent"),
        ("BW-BroadworksNetworkServer", "bwNSNRSStatsTableNbRequestsUnanswered"))
)
if mibBuilder.loadTexts:
    bwNsNrsStatsGroup.setStatus("current")

bwNsCallLogsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 10)
)
bwNsCallLogsStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "calllogNbEnterprises"),
        ("BW-BroadworksNetworkServer", "calllogNbClients"))
)
if mibBuilder.loadTexts:
    bwNsCallLogsStatsGroup.setStatus("current")

bwNsXSPersistencyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 11)
)
bwNsXSPersistencyStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "perNSNbOpenedTransactions"),
        ("BW-BroadworksNetworkServer", "perNSNbCommittedTransactions"),
        ("BW-BroadworksNetworkServer", "perNSNbFailedTransactions"),
        ("BW-BroadworksNetworkServer", "perNSNbCriticalErrors"),
        ("BW-BroadworksNetworkServer", "ttNSNbConnectionsCreated"),
        ("BW-BroadworksNetworkServer", "ttNSConnectionPoolSize"),
        ("BW-BroadworksNetworkServer", "ttNSNbBackdoorUpdates"),
        ("BW-BroadworksNetworkServer", "ttNSNbFailedCheckpoints"),
        ("BW-BroadworksNetworkServer", "xsNSRemoteXlaNbTimesConnected"),
        ("BW-BroadworksNetworkServer", "xsNSRemoteXlaNbTimesDisconnected"),
        ("BW-BroadworksNetworkServer", "xsNSRemoteXlaUpdatesProcessed"),
        ("BW-BroadworksNetworkServer", "xsNSRemoteXlaUpdatesPending"))
)
if mibBuilder.loadTexts:
    bwNsXSPersistencyStatsGroup.setStatus("current")

bwNsMoCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 12)
)
bwNsMoCountersGroup.setObjects(
    ("BW-BroadworksNetworkServer", "resetAllNSCounters")
)
if mibBuilder.loadTexts:
    bwNsMoCountersGroup.setStatus("current")

bwNsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 13)
)
bwNsSystemGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "systemNbGrps"),
        ("BW-BroadworksNetworkServer", "systemNbDNs"),
        ("BW-BroadworksNetworkServer", "systemNbURLs"),
        ("BW-BroadworksNetworkServer", "systemNbProfiles"),
        ("BW-BroadworksNetworkServer", "systemNbRoutingNEs"),
        ("BW-BroadworksNetworkServer", "systemNbResourceNEs"),
        ("BW-BroadworksNetworkServer", "systemNbEnterprises"),
        ("BW-BroadworksNetworkServer", "systemNbUnassignedDNs"),
        ("BW-BroadworksNetworkServer", "systemNbExts"),
        ("BW-BroadworksNetworkServer", "systemNbSites"),
        ("BW-BroadworksNetworkServer", "systemNbHostingNes"))
)
if mibBuilder.loadTexts:
    bwNsSystemGroup.setStatus("current")

bwNsSyncAPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 14)
)
bwNsSyncAPIGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "syncNbUpdatesRequests"),
        ("BW-BroadworksNetworkServer", "syncNbUpdatesRequestsFailures"),
        ("BW-BroadworksNetworkServer", "syncNbOpenedSessions"),
        ("BW-BroadworksNetworkServer", "syncNbAuthorizationFailures"),
        ("BW-BroadworksNetworkServer", "syncNbActiveSessions"))
)
if mibBuilder.loadTexts:
    bwNsSyncAPIGroup.setStatus("current")

bwNsOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 15)
)
bwNsOamGroup.setObjects(
    ("BW-BroadworksNetworkServer", "oampNbActiveSessions")
)
if mibBuilder.loadTexts:
    bwNsOamGroup.setStatus("current")

bwNsOssGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 16)
)
bwNsOssGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "ossNbUpdatesRequests"),
        ("BW-BroadworksNetworkServer", "ossNbUpdatesRequestsFailures"),
        ("BW-BroadworksNetworkServer", "ossNbQueriesRequests"),
        ("BW-BroadworksNetworkServer", "ossNbQueriesRequestsFailures"),
        ("BW-BroadworksNetworkServer", "ossNbOpenedSessions"),
        ("BW-BroadworksNetworkServer", "ossNbAuthorizationFailures"),
        ("BW-BroadworksNetworkServer", "ossNbActiveSessions"))
)
if mibBuilder.loadTexts:
    bwNsOssGroup.setStatus("current")

bwNsPSPersistencyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 17)
)
bwNsPSPersistencyStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "psNSPerNbOpenedTransactions"),
        ("BW-BroadworksNetworkServer", "psNSPerNbCommittedTransactions"),
        ("BW-BroadworksNetworkServer", "psNSPerNbFailedTransactions"),
        ("BW-BroadworksNetworkServer", "psNSPerNbCriticalErrors"),
        ("BW-BroadworksNetworkServer", "psNSTtNbConnectionsCreated"),
        ("BW-BroadworksNetworkServer", "psNSTtConnectionPoolSize"),
        ("BW-BroadworksNetworkServer", "psNSTtNbBackdoorUpdates"),
        ("BW-BroadworksNetworkServer", "psNSTtNbFailedCheckpoints"),
        ("BW-BroadworksNetworkServer", "psNSRemoteXlaNbTimesConnected"),
        ("BW-BroadworksNetworkServer", "psNSRemoteXlaNbTimesDisconnected"),
        ("BW-BroadworksNetworkServer", "psNSRemoteXlaUpdatesProcessed"),
        ("BW-BroadworksNetworkServer", "psNSRemoteXlaUpdatesPending"))
)
if mibBuilder.loadTexts:
    bwNsPSPersistencyStatsGroup.setStatus("current")

bwNsScpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 18)
)
bwNsScpStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwSCProxyStatsACLViolationCount"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsSCPMessageIns"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsSCPMessageOuts"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsSCPMessageErrors"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASTable"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASIndex"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASAddr"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASMessageIns"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASMessageOuts"),
        ("BW-BroadworksNetworkServer", "bwSCProxyStatsASMessageErrors"))
)
if mibBuilder.loadTexts:
    bwNsScpStatsGroup.setStatus("current")

bwNsXsBcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 19)
)
bwNsXsBcctGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSCommonCommXSStatsTable"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSStatsIndex"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSHost"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSInterface"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSProtocol"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSAcceptedOutboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSAcceptedInboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSRejectedOutboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSRejectedInboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSOutputMessagesProcessed"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSInputMessagesProcessed"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSOutputCommunicationErrors"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommXSInputCommunicationErrors"))
)
if mibBuilder.loadTexts:
    bwNsXsBcctGroup.setStatus("current")

bwNsPsBcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 20)
)
bwNsPsBcctGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSCommonCommPSStatsTable"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSStatsIndex"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSHost"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSInterface"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSProtocol"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSAcceptedOutboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSAcceptedInboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSRejectedOutboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSRejectedInboundConnections"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSOutputMessagesProcessed"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSInputMessagesProcessed"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSOutputCommunicationErrors"),
        ("BW-BroadworksNetworkServer", "bwNSCommonCommPSInputCommunicationErrors"))
)
if mibBuilder.loadTexts:
    bwNsPsBcctGroup.setStatus("current")

bwNSXSTcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 21)
)
bwNSXSTcpStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSXSTcpServersStatsTable"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersStatsIndex"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersName"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersNbConnectionsAccepted"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersNbConnectionsClosed"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersOutgoingQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersIncomingQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersNbBytesSentSecure"),
        ("BW-BroadworksNetworkServer", "bwNSXSTcpServersNbBytesReceivedSecure"))
)
if mibBuilder.loadTexts:
    bwNSXSTcpStatsGroup.setStatus("current")

bwNSPSTcpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 22)
)
bwNSPSTcpStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSPSTcpServersStatsTable"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersStatsIndex"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersName"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersNbConnectionsAccepted"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersNbConnectionsClosed"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersOutgoingQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersIncomingQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersNbBytesSentSecure"),
        ("BW-BroadworksNetworkServer", "bwNSPSTcpServersNbBytesReceivedSecure"))
)
if mibBuilder.loadTexts:
    bwNSPSTcpStatsGroup.setStatus("current")

bwNSXSConcurrentFrameworkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 23)
)
bwNSXSConcurrentFrameworkStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorTable"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorIndex"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorName"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorCurrentPoolSize"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorMaxPoolSize"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorAvgActiveThreads"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorTaskQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorNbTasksRun"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorNbWarnings"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorNbErrors"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorLongestTaskMs"),
        ("BW-BroadworksNetworkServer", "bwNSXSMonitoringExecutorLongestTaskName"))
)
if mibBuilder.loadTexts:
    bwNSXSConcurrentFrameworkStatsGroup.setStatus("current")

bwNSPSConcurrentFrameworkStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 24)
)
bwNSPSConcurrentFrameworkStatsGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorTable"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorIndex"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorName"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorCurrentPoolSize"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorMaxPoolSize"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorAvgActiveThreads"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorTaskQueueSize"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorNbTasksRun"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorNbWarnings"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorNbErrors"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorLongestTaskMs"),
        ("BW-BroadworksNetworkServer", "bwNSPSMonitoringExecutorLongestTaskName"))
)
if mibBuilder.loadTexts:
    bwNSPSConcurrentFrameworkStatsGroup.setStatus("current")

bwNSXSCongestionManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 25)
)
bwNSXSCongestionManagementGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSCurrentCallOverloadZone"),
        ("BW-BroadworksNetworkServer", "bwNSNumCallYellowZoneOverloadTrans"),
        ("BW-BroadworksNetworkServer", "bwNSNumCallRedZoneOverloadTrans"),
        ("BW-BroadworksNetworkServer", "bwNSCurrentNonCallOverloadZone"),
        ("BW-BroadworksNetworkServer", "bwNSNumNonCallYellowZoneOverloadTrans"),
        ("BW-BroadworksNetworkServer", "bwNSNumNonCallRedZoneOverloadTrans"),
        ("BW-BroadworksNetworkServer", "bwNSNumDiscardedMessage"),
        ("BW-BroadworksNetworkServer", "bwNSTimeLastDiscardedMessage"))
)
if mibBuilder.loadTexts:
    bwNSXSCongestionManagementGroup.setStatus("current")

bwSIPCongestionManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 1, 26)
)
bwSIPCongestionManagementGroup.setObjects(
      *(("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborTable"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborIndex"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborIpAddress"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborInviteIn"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborRegisterIn"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborOptionsIn"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborOptionsOut"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborSubscribeNotifyIn"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighbor5xxIn"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborCallpRequestInRate"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborNonCallpRequestInRate"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborState"),
        ("BW-BroadworksNetworkServer", "bwNSCongestionManagementNeighborCapability"))
)
if mibBuilder.loadTexts:
    bwSIPCongestionManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwNsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 5, 100, 2, 1)
)
if mibBuilder.loadTexts:
    bwNsBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-BroadworksNetworkServer",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "nsExecutionServer": nsExecutionServer,
       "system": system,
       "licensing": licensing,
       "bwNbTimePeriodWithLicenseViolations": bwNbTimePeriodWithLicenseViolations,
       "bwNbTransactionInViolation": bwNbTransactionInViolation,
       "bwNbThresholdAlarmSent": bwNbThresholdAlarmSent,
       "bwNbNonInviteTimePeriodWithLicenseViolations": bwNbNonInviteTimePeriodWithLicenseViolations,
       "bwNbNonInviteTransactionInViolation": bwNbNonInviteTransactionInViolation,
       "bwNbNonInviteThresholdAlarmSent": bwNbNonInviteThresholdAlarmSent,
       "internalStats": internalStats,
       "bwNSSystemInternalQueueResets": bwNSSystemInternalQueueResets,
       "bwNSSystemInternalQueueTable": bwNSSystemInternalQueueTable,
       "bwNSSystemInternalQueueEntry": bwNSSystemInternalQueueEntry,
       "bwNSSystemInternalQueueIndex": bwNSSystemInternalQueueIndex,
       "bwNSSystemInternalQueueName": bwNSSystemInternalQueueName,
       "bwNSSystemInternalQueueSize": bwNSSystemInternalQueueSize,
       "bwNSSystemInternalQueueTimeAvg": bwNSSystemInternalQueueTimeAvg,
       "bwNSSystemInternalQueueTimeMin": bwNSSystemInternalQueueTimeMin,
       "bwNSSystemInternalQueueTimeMax": bwNSSystemInternalQueueTimeMax,
       "bwNSSystemInternalQueueTimeMaxTimestamp": bwNSSystemInternalQueueTimeMaxTimestamp,
       "bwNSSystemInternalQueueLengthCurrent": bwNSSystemInternalQueueLengthCurrent,
       "bwNSSystemInternalQueueLengthAvg": bwNSSystemInternalQueueLengthAvg,
       "bwNSSystemInternalQueueLengthMax": bwNSSystemInternalQueueLengthMax,
       "bwNSSystemInternalQueueLengthMaxTimestamp": bwNSSystemInternalQueueLengthMaxTimestamp,
       "bwNSSystemInternalQueueTimeMaxTimestampMSB": bwNSSystemInternalQueueTimeMaxTimestampMSB,
       "bwNSSystemInternalQueueLengthMaxTimestampMSB": bwNSSystemInternalQueueLengthMaxTimestampMSB,
       "bwNSSystemInternalQueueLengthMaxTimestampLSB": bwNSSystemInternalQueueLengthMaxTimestampLSB,
       "bwNSSystemInternalQueueTimeMaxTimestampLSB": bwNSSystemInternalQueueTimeMaxTimestampLSB,
       "overloadStats": overloadStats,
       "bwNSCurrentCallOverloadZone": bwNSCurrentCallOverloadZone,
       "bwNSNumCallYellowZoneOverloadTrans": bwNSNumCallYellowZoneOverloadTrans,
       "bwNSNumCallRedZoneOverloadTrans": bwNSNumCallRedZoneOverloadTrans,
       "bwNSCurrentNonCallOverloadZone": bwNSCurrentNonCallOverloadZone,
       "bwNSNumNonCallYellowZoneOverloadTrans": bwNSNumNonCallYellowZoneOverloadTrans,
       "bwNSNumNonCallRedZoneOverloadTrans": bwNSNumNonCallRedZoneOverloadTrans,
       "bwNSNumDiscardedMessage": bwNSNumDiscardedMessage,
       "bwNSTimeLastDiscardedMessage": bwNSTimeLastDiscardedMessage,
       "processing": processing,
       "policies": policies,
       "publicPolicyStatTable": publicPolicyStatTable,
       "publicPolicyStatEntry": publicPolicyStatEntry,
       "pubPolStatID": pubPolStatID,
       "pubPolStatPolicyName": pubPolStatPolicyName,
       "pubPolStatNbInstances": pubPolStatNbInstances,
       "pubPolStatNbRequests": pubPolStatNbRequests,
       "pubPolStatNbRequestsFailures": pubPolStatNbRequestsFailures,
       "pubPolStatNbRequestsResults": pubPolStatNbRequestsResults,
       "privatePolicyStatTable": privatePolicyStatTable,
       "privatePolicyStatEntry": privatePolicyStatEntry,
       "privPolStatID": privPolStatID,
       "privPolStatEnterpriseName": privPolStatEnterpriseName,
       "privPolStatPolicyName": privPolStatPolicyName,
       "privPolStatNbRequests": privPolStatNbRequests,
       "privPolStatNbRequestsFailures": privPolStatNbRequestsFailures,
       "privPolStatNbRequestsResults": privPolStatNbRequestsResults,
       "policyInfoTable": policyInfoTable,
       "policyInfoEntry": policyInfoEntry,
       "polInfoID": polInfoID,
       "polInfoEnterpriseName": polInfoEnterpriseName,
       "polInfoPolicyName": polInfoPolicyName,
       "polInfoInfoName": polInfoInfoName,
       "polInfoNbOccurences": polInfoNbOccurences,
       "bwNbPolicyRequests": bwNbPolicyRequests,
       "bwNbPolicyRequestFailures": bwNbPolicyRequestFailures,
       "neStatTable": neStatTable,
       "neStatEntry": neStatEntry,
       "neStatID": neStatID,
       "neStatName": neStatName,
       "neStatNbSIPRequests": neStatNbSIPRequests,
       "neStatNbSIPRequestsFailures": neStatNbSIPRequestsFailures,
       "neStatNbMSSRequests": neStatNbMSSRequests,
       "neStatNbMSSRequestsFailures": neStatNbMSSRequestsFailures,
       "errorStatTable": errorStatTable,
       "errorStatEntry": errorStatEntry,
       "errStatID": errStatID,
       "errStatName": errStatName,
       "errStatNbOccurences": errStatNbOccurences,
       "bwNSCallpCallsPerSecond": bwNSCallpCallsPerSecond,
       "carrierStatTable": carrierStatTable,
       "carrierStatEntry": carrierStatEntry,
       "bwCarrierStatID": bwCarrierStatID,
       "bwCarrierName": bwCarrierName,
       "bwCarrierCic": bwCarrierCic,
       "bwCarrierNbIntraLataCalls": bwCarrierNbIntraLataCalls,
       "bwCarrierNbInterLataCalls": bwCarrierNbInterLataCalls,
       "bwCarrierNbInternationalCalls": bwCarrierNbInternationalCalls,
       "protocol": protocol,
       "sip": sip,
       "bwNSSipStatsInviteIns": bwNSSipStatsInviteIns,
       "bwNSSipStatsAckIns": bwNSSipStatsAckIns,
       "bwNSSipStatsInviteResponsesTable": bwNSSipStatsInviteResponsesTable,
       "bwNSSipStatsInviteResponsesEntry": bwNSSipStatsInviteResponsesEntry,
       "bwNSSipStatsInviteResponseCodeValue": bwNSSipStatsInviteResponseCodeValue,
       "bwNSSipStatsInviteResponseOuts": bwNSSipStatsInviteResponseOuts,
       "bwNSSipStatsCancelIns": bwNSSipStatsCancelIns,
       "bwNSSipStatsRegisterIns": bwNSSipStatsRegisterIns,
       "bwNSSipStatsNotifyIns": bwNSSipStatsNotifyIns,
       "bwNSSipStatsSubscribeIns": bwNSSipStatsSubscribeIns,
       "bwNSSipStatsMessageIns": bwNSSipStatsMessageIns,
       "bwNSSipStatsInfoIns": bwNSSipStatsInfoIns,
       "bwNSSipStatsOptionsIns": bwNSSipStatsOptionsIns,
       "bwNSSipStatsOptionsResponsesTable": bwNSSipStatsOptionsResponsesTable,
       "bwNSSipStatsOptionsResponsesEntry": bwNSSipStatsOptionsResponsesEntry,
       "bwNSSipStatsOptionsResponseCodeValue": bwNSSipStatsOptionsResponseCodeValue,
       "bwNSSipStatsOptionsResponseIns": bwNSSipStatsOptionsResponseIns,
       "bwNSSipStatsOptionsResponseOuts": bwNSSipStatsOptionsResponseOuts,
       "bwNSSipStatsRegisterResponsesTable": bwNSSipStatsRegisterResponsesTable,
       "bwNSSipStatsRegisterResponsesEntry": bwNSSipStatsRegisterResponsesEntry,
       "bwNSSipStatsRegisterResponseCodeValue": bwNSSipStatsRegisterResponseCodeValue,
       "bwNSSipStatsRegisterResponseIns": bwNSSipStatsRegisterResponseIns,
       "bwNSSipStatsRegisterResponseOuts": bwNSSipStatsRegisterResponseOuts,
       "bwNSSipStatsInfoResponsesTable": bwNSSipStatsInfoResponsesTable,
       "bwNSSipStatsInfoResponsesEntry": bwNSSipStatsInfoResponsesEntry,
       "bwNSSipStatsInfoResponseCodeValue": bwNSSipStatsInfoResponseCodeValue,
       "bwNSSipStatsInfoResponseIns": bwNSSipStatsInfoResponseIns,
       "bwNSSipStatsInfoResponseOuts": bwNSSipStatsInfoResponseOuts,
       "bwNSSipStatsNotifyResponsesTable": bwNSSipStatsNotifyResponsesTable,
       "bwNSSipStatsNotifyResponsesEntry": bwNSSipStatsNotifyResponsesEntry,
       "bwNSSipStatsNotifyResponseCodeValue": bwNSSipStatsNotifyResponseCodeValue,
       "bwNSSipStatsNotifyResponseIns": bwNSSipStatsNotifyResponseIns,
       "bwNSSipStatsNotifyResponseOuts": bwNSSipStatsNotifyResponseOuts,
       "bwNSSipStatsSubscribeResponsesTable": bwNSSipStatsSubscribeResponsesTable,
       "bwNSSipStatsSubscribeResponsesEntry": bwNSSipStatsSubscribeResponsesEntry,
       "bwNSSipStatsSubscribeResponseCodeValue": bwNSSipStatsSubscribeResponseCodeValue,
       "bwNSSipStatsSubscribeResponseIns": bwNSSipStatsSubscribeResponseIns,
       "bwNSSipStatsSubscribeResponseOuts": bwNSSipStatsSubscribeResponseOuts,
       "bwNSSipStatsMessageResponsesTable": bwNSSipStatsMessageResponsesTable,
       "bwNSSipStatsMessageResponsesEntry": bwNSSipStatsMessageResponsesEntry,
       "bwNSSipStatsMessageResponseCodeValue": bwNSSipStatsMessageResponseCodeValue,
       "bwNSSipStatsMessageResponseIns": bwNSSipStatsMessageResponseIns,
       "bwNSSipStatsMessageResponseOuts": bwNSSipStatsMessageResponseOuts,
       "bwNSSipStatsFailures": bwNSSipStatsFailures,
       "bwNSSipStatsActiveTcpConnections": bwNSSipStatsActiveTcpConnections,
       "bwNSSipStatsTcpIns": bwNSSipStatsTcpIns,
       "bwNSSipStatsTcpOuts": bwNSSipStatsTcpOuts,
       "bwNSSipStatsTcpFailures": bwNSSipStatsTcpFailures,
       "bwNSSipStatsUdpIns": bwNSSipStatsUdpIns,
       "bwNSSipStatsUdpOuts": bwNSSipStatsUdpOuts,
       "bwNSSIPReclaimedStaleTcpConnections": bwNSSIPReclaimedStaleTcpConnections,
       "congestionManagement": congestionManagement,
       "bwNSCongestionManagementNeighborTable": bwNSCongestionManagementNeighborTable,
       "bwNSCongestionManagementNeighborEntry": bwNSCongestionManagementNeighborEntry,
       "bwNSCongestionManagementNeighborIndex": bwNSCongestionManagementNeighborIndex,
       "bwNSCongestionManagementNeighborIpAddress": bwNSCongestionManagementNeighborIpAddress,
       "bwNSCongestionManagementNeighborInviteIn": bwNSCongestionManagementNeighborInviteIn,
       "bwNSCongestionManagementNeighborRegisterIn": bwNSCongestionManagementNeighborRegisterIn,
       "bwNSCongestionManagementNeighborOptionsIn": bwNSCongestionManagementNeighborOptionsIn,
       "bwNSCongestionManagementNeighborOptionsOut": bwNSCongestionManagementNeighborOptionsOut,
       "bwNSCongestionManagementNeighborSubscribeNotifyIn": bwNSCongestionManagementNeighborSubscribeNotifyIn,
       "bwNSCongestionManagementNeighbor5xxIn": bwNSCongestionManagementNeighbor5xxIn,
       "bwNSCongestionManagementNeighborCallpRequestInRate": bwNSCongestionManagementNeighborCallpRequestInRate,
       "bwNSCongestionManagementNeighborNonCallpRequestInRate": bwNSCongestionManagementNeighborNonCallpRequestInRate,
       "bwNSCongestionManagementNeighborState": bwNSCongestionManagementNeighborState,
       "bwNSCongestionManagementNeighborCapability": bwNSCongestionManagementNeighborCapability,
       "nrs": nrs,
       "bwNSNbInvalidMessagesReceived": bwNSNbInvalidMessagesReceived,
       "bwNSNbRequestsReceived": bwNSNbRequestsReceived,
       "bwNSNbResponsesReceived": bwNSNbResponsesReceived,
       "bwNSNbErrorsReceived": bwNSNbErrorsReceived,
       "bwNSNbRequestsSent": bwNSNbRequestsSent,
       "bwNSNbResponsesSent": bwNSNbResponsesSent,
       "bwNSNbErrorsSent": bwNSNbErrorsSent,
       "bwNSNbRequestsResent": bwNSNbRequestsResent,
       "bwNSNbResponsesResent": bwNSNbResponsesResent,
       "bwNSNbRequestsUnanswered": bwNSNbRequestsUnanswered,
       "bwNSNRSStatsTable": bwNSNRSStatsTable,
       "bwNSNRSStatsEntry": bwNSNRSStatsEntry,
       "bwNSNRSStatsTableIndex": bwNSNRSStatsTableIndex,
       "bwNSNRSStatsTableProtocolName": bwNSNRSStatsTableProtocolName,
       "bwNSNRSStatsTableNbRequestsReceived": bwNSNRSStatsTableNbRequestsReceived,
       "bwNSNRSStatsTableNbResponsesReceived": bwNSNRSStatsTableNbResponsesReceived,
       "bwNSNRSStatsTableNbErrorsReceived": bwNSNRSStatsTableNbErrorsReceived,
       "bwNSNRSStatsTableNbRequestsSent": bwNSNRSStatsTableNbRequestsSent,
       "bwNSNRSStatsTableNbResponsesSent": bwNSNRSStatsTableNbResponsesSent,
       "bwNSNRSStatsTableNbErrorsSent": bwNSNRSStatsTableNbErrorsSent,
       "bwNSNRSStatsTableNbRequestsResent": bwNSNRSStatsTableNbRequestsResent,
       "bwNSNRSStatsTableNbResponsesResent": bwNSNRSStatsTableNbResponsesResent,
       "bwNSNRSStatsTableNbRequestsUnanswered": bwNSNRSStatsTableNbRequestsUnanswered,
       "callLog": callLog,
       "calllogNbEnterprises": calllogNbEnterprises,
       "calllogNbClients": calllogNbClients,
       "nsXSCommonCommStats": nsXSCommonCommStats,
       "bwNSCommonCommXSStatsTable": bwNSCommonCommXSStatsTable,
       "bwNSCommonCommXSStatsEntry": bwNSCommonCommXSStatsEntry,
       "bwNSCommonCommXSStatsIndex": bwNSCommonCommXSStatsIndex,
       "bwNSCommonCommXSHost": bwNSCommonCommXSHost,
       "bwNSCommonCommXSInterface": bwNSCommonCommXSInterface,
       "bwNSCommonCommXSProtocol": bwNSCommonCommXSProtocol,
       "bwNSCommonCommXSAcceptedOutboundConnections": bwNSCommonCommXSAcceptedOutboundConnections,
       "bwNSCommonCommXSAcceptedInboundConnections": bwNSCommonCommXSAcceptedInboundConnections,
       "bwNSCommonCommXSRejectedOutboundConnections": bwNSCommonCommXSRejectedOutboundConnections,
       "bwNSCommonCommXSRejectedInboundConnections": bwNSCommonCommXSRejectedInboundConnections,
       "bwNSCommonCommXSOutputMessagesProcessed": bwNSCommonCommXSOutputMessagesProcessed,
       "bwNSCommonCommXSInputMessagesProcessed": bwNSCommonCommXSInputMessagesProcessed,
       "bwNSCommonCommXSOutputCommunicationErrors": bwNSCommonCommXSOutputCommunicationErrors,
       "bwNSCommonCommXSInputCommunicationErrors": bwNSCommonCommXSInputCommunicationErrors,
       "tcp": tcp,
       "bwNSXSTcpServersStatsTable": bwNSXSTcpServersStatsTable,
       "bwNSXSTcpServersStatsEntry": bwNSXSTcpServersStatsEntry,
       "bwNSXSTcpServersStatsIndex": bwNSXSTcpServersStatsIndex,
       "bwNSXSTcpServersName": bwNSXSTcpServersName,
       "bwNSXSTcpServersNbConnectionsAccepted": bwNSXSTcpServersNbConnectionsAccepted,
       "bwNSXSTcpServersNbConnectionsRefused": bwNSXSTcpServersNbConnectionsRefused,
       "bwNSXSTcpServersNbConnectionsInitiated": bwNSXSTcpServersNbConnectionsInitiated,
       "bwNSXSTcpServersNbConnectionsClosed": bwNSXSTcpServersNbConnectionsClosed,
       "bwNSXSTcpServersNbBytesSent": bwNSXSTcpServersNbBytesSent,
       "bwNSXSTcpServersNbBytesReceived": bwNSXSTcpServersNbBytesReceived,
       "bwNSXSTcpServersOutgoingQueueSize": bwNSXSTcpServersOutgoingQueueSize,
       "bwNSXSTcpServersIncomingQueueSize": bwNSXSTcpServersIncomingQueueSize,
       "bwNSXSTcpServersNbBytesSentSecure": bwNSXSTcpServersNbBytesSentSecure,
       "bwNSXSTcpServersNbBytesReceivedSecure": bwNSXSTcpServersNbBytesReceivedSecure,
       "persistency": persistency,
       "timesTen": timesTen,
       "ttNSNbConnectionsCreated": ttNSNbConnectionsCreated,
       "ttNSConnectionPoolSize": ttNSConnectionPoolSize,
       "ttNSNbBackdoorUpdates": ttNSNbBackdoorUpdates,
       "ttNSNbFailedCheckpoints": ttNSNbFailedCheckpoints,
       "xsRemoteXla": xsRemoteXla,
       "xsNSRemoteXlaNbTimesConnected": xsNSRemoteXlaNbTimesConnected,
       "xsNSRemoteXlaNbTimesDisconnected": xsNSRemoteXlaNbTimesDisconnected,
       "xsNSRemoteXlaUpdatesProcessed": xsNSRemoteXlaUpdatesProcessed,
       "xsNSRemoteXlaUpdatesPending": xsNSRemoteXlaUpdatesPending,
       "bwNSXSAvgUpdateTime": bwNSXSAvgUpdateTime,
       "bwNSXSAvgRowsUpdated": bwNSXSAvgRowsUpdated,
       "bwNSXSAvgQueryTime": bwNSXSAvgQueryTime,
       "bwNSXSAvgRowsQueried": bwNSXSAvgRowsQueried,
       "bwNSXSUpdateCount": bwNSXSUpdateCount,
       "bwNSXSQueryCount": bwNSXSQueryCount,
       "bwNSXSTTHWMTable": bwNSXSTTHWMTable,
       "bwNSXSTTHWMEntry": bwNSXSTTHWMEntry,
       "bwNSXSTTHWMIndex": bwNSXSTTHWMIndex,
       "bwNSXSTTHWMName": bwNSXSTTHWMName,
       "bwNSXSTTHWMValue": bwNSXSTTHWMValue,
       "bwNSXSTTHWMTimestamp": bwNSXSTTHWMTimestamp,
       "bwNSXSTTHWMStackTrace": bwNSXSTTHWMStackTrace,
       "perNSNbOpenedTransactions": perNSNbOpenedTransactions,
       "perNSNbCommittedTransactions": perNSNbCommittedTransactions,
       "perNSNbFailedTransactions": perNSNbFailedTransactions,
       "perNSNbCriticalErrors": perNSNbCriticalErrors,
       "management": management,
       "resetAllNSCounters": resetAllNSCounters,
       "serviceControlProxy": serviceControlProxy,
       "scpSystemModule": scpSystemModule,
       "bwSCProxyStatsACLViolationCount": bwSCProxyStatsACLViolationCount,
       "bwSCProxyStatsSCPMessageIns": bwSCProxyStatsSCPMessageIns,
       "bwSCProxyStatsSCPMessageOuts": bwSCProxyStatsSCPMessageOuts,
       "bwSCProxyStatsSCPMessageErrors": bwSCProxyStatsSCPMessageErrors,
       "scpCapModule": scpCapModule,
       "bwSCProxyStatsASTable": bwSCProxyStatsASTable,
       "bwSCProxyStatsASEntry": bwSCProxyStatsASEntry,
       "bwSCProxyStatsASIndex": bwSCProxyStatsASIndex,
       "bwSCProxyStatsASAddr": bwSCProxyStatsASAddr,
       "bwSCProxyStatsASMessageIns": bwSCProxyStatsASMessageIns,
       "bwSCProxyStatsASMessageOuts": bwSCProxyStatsASMessageOuts,
       "bwSCProxyStatsASMessageErrors": bwSCProxyStatsASMessageErrors,
       "concurrent": concurrent,
       "bwNSXSMonitoringExecutorTable": bwNSXSMonitoringExecutorTable,
       "bwNSXSMonitoringExecutorEntry": bwNSXSMonitoringExecutorEntry,
       "bwNSXSMonitoringExecutorIndex": bwNSXSMonitoringExecutorIndex,
       "bwNSXSMonitoringExecutorName": bwNSXSMonitoringExecutorName,
       "bwNSXSMonitoringExecutorCurrentPoolSize": bwNSXSMonitoringExecutorCurrentPoolSize,
       "bwNSXSMonitoringExecutorMaxPoolSize": bwNSXSMonitoringExecutorMaxPoolSize,
       "bwNSXSMonitoringExecutorAvgActiveThreads": bwNSXSMonitoringExecutorAvgActiveThreads,
       "bwNSXSMonitoringExecutorTaskQueueSize": bwNSXSMonitoringExecutorTaskQueueSize,
       "bwNSXSMonitoringExecutorNbTasksRun": bwNSXSMonitoringExecutorNbTasksRun,
       "bwNSXSMonitoringExecutorNbWarnings": bwNSXSMonitoringExecutorNbWarnings,
       "bwNSXSMonitoringExecutorNbErrors": bwNSXSMonitoringExecutorNbErrors,
       "bwNSXSMonitoringExecutorLongestTaskMs": bwNSXSMonitoringExecutorLongestTaskMs,
       "bwNSXSMonitoringExecutorLongestTaskName": bwNSXSMonitoringExecutorLongestTaskName,
       "bwNSMibConformance": bwNSMibConformance,
       "bwNSMibGroups": bwNSMibGroups,
       "bwNsLicensingGroup": bwNsLicensingGroup,
       "bwNsSystemQueueStatsGroup": bwNsSystemQueueStatsGroup,
       "bwNsGenericPolicyStatsGroup": bwNsGenericPolicyStatsGroup,
       "bwNsNeStatsGroup": bwNsNeStatsGroup,
       "bwNsErrorStatsGroup": bwNsErrorStatsGroup,
       "bwNsCallPStatsGroup": bwNsCallPStatsGroup,
       "bwNsCarrierStatsGroup": bwNsCarrierStatsGroup,
       "bwNsSipStatsGroup": bwNsSipStatsGroup,
       "bwNsNrsStatsGroup": bwNsNrsStatsGroup,
       "bwNsCallLogsStatsGroup": bwNsCallLogsStatsGroup,
       "bwNsXSPersistencyStatsGroup": bwNsXSPersistencyStatsGroup,
       "bwNsMoCountersGroup": bwNsMoCountersGroup,
       "bwNsSystemGroup": bwNsSystemGroup,
       "bwNsSyncAPIGroup": bwNsSyncAPIGroup,
       "bwNsOamGroup": bwNsOamGroup,
       "bwNsOssGroup": bwNsOssGroup,
       "bwNsPSPersistencyStatsGroup": bwNsPSPersistencyStatsGroup,
       "bwNsScpStatsGroup": bwNsScpStatsGroup,
       "bwNsXsBcctGroup": bwNsXsBcctGroup,
       "bwNsPsBcctGroup": bwNsPsBcctGroup,
       "bwNSXSTcpStatsGroup": bwNSXSTcpStatsGroup,
       "bwNSPSTcpStatsGroup": bwNSPSTcpStatsGroup,
       "bwNSXSConcurrentFrameworkStatsGroup": bwNSXSConcurrentFrameworkStatsGroup,
       "bwNSPSConcurrentFrameworkStatsGroup": bwNSPSConcurrentFrameworkStatsGroup,
       "bwNSXSCongestionManagementGroup": bwNSXSCongestionManagementGroup,
       "bwSIPCongestionManagementGroup": bwSIPCongestionManagementGroup,
       "bwNSMibCompliancy": bwNSMibCompliancy,
       "bwNsBasicCompliance": bwNsBasicCompliance,
       "nsProvisioningServer": nsProvisioningServer,
       "psSystem": psSystem,
       "systemNbGrps": systemNbGrps,
       "systemNbDNs": systemNbDNs,
       "systemNbURLs": systemNbURLs,
       "systemNbProfiles": systemNbProfiles,
       "systemNbRoutingNEs": systemNbRoutingNEs,
       "systemNbResourceNEs": systemNbResourceNEs,
       "systemNbEnterprises": systemNbEnterprises,
       "systemNbUnassignedDNs": systemNbUnassignedDNs,
       "systemNbExts": systemNbExts,
       "systemNbSites": systemNbSites,
       "systemNbHostingNes": systemNbHostingNes,
       "psProtocol": psProtocol,
       "synchAPI": synchAPI,
       "syncNbUpdatesRequests": syncNbUpdatesRequests,
       "syncNbUpdatesRequestsFailures": syncNbUpdatesRequestsFailures,
       "syncNbOpenedSessions": syncNbOpenedSessions,
       "syncNbAuthorizationFailures": syncNbAuthorizationFailures,
       "syncNbActiveSessions": syncNbActiveSessions,
       "oamp": oamp,
       "oampNbActiveSessions": oampNbActiveSessions,
       "oss": oss,
       "ossNbUpdatesRequests": ossNbUpdatesRequests,
       "ossNbUpdatesRequestsFailures": ossNbUpdatesRequestsFailures,
       "ossNbQueriesRequests": ossNbQueriesRequests,
       "ossNbQueriesRequestsFailures": ossNbQueriesRequestsFailures,
       "ossNbOpenedSessions": ossNbOpenedSessions,
       "ossNbAuthorizationFailures": ossNbAuthorizationFailures,
       "ossNbActiveSessions": ossNbActiveSessions,
       "nsPSCommonCommStats": nsPSCommonCommStats,
       "bwNSCommonCommPSStatsTable": bwNSCommonCommPSStatsTable,
       "bwNSCommonCommPSStatsEntry": bwNSCommonCommPSStatsEntry,
       "bwNSCommonCommPSStatsIndex": bwNSCommonCommPSStatsIndex,
       "bwNSCommonCommPSHost": bwNSCommonCommPSHost,
       "bwNSCommonCommPSInterface": bwNSCommonCommPSInterface,
       "bwNSCommonCommPSProtocol": bwNSCommonCommPSProtocol,
       "bwNSCommonCommPSAcceptedOutboundConnections": bwNSCommonCommPSAcceptedOutboundConnections,
       "bwNSCommonCommPSAcceptedInboundConnections": bwNSCommonCommPSAcceptedInboundConnections,
       "bwNSCommonCommPSRejectedOutboundConnections": bwNSCommonCommPSRejectedOutboundConnections,
       "bwNSCommonCommPSRejectedInboundConnections": bwNSCommonCommPSRejectedInboundConnections,
       "bwNSCommonCommPSOutputMessagesProcessed": bwNSCommonCommPSOutputMessagesProcessed,
       "bwNSCommonCommPSInputMessagesProcessed": bwNSCommonCommPSInputMessagesProcessed,
       "bwNSCommonCommPSOutputCommunicationErrors": bwNSCommonCommPSOutputCommunicationErrors,
       "bwNSCommonCommPSInputCommunicationErrors": bwNSCommonCommPSInputCommunicationErrors,
       "nsTcp": nsTcp,
       "bwNSPSTcpServersStatsTable": bwNSPSTcpServersStatsTable,
       "bwNSPSTcpServersStatsEntry": bwNSPSTcpServersStatsEntry,
       "bwNSPSTcpServersStatsIndex": bwNSPSTcpServersStatsIndex,
       "bwNSPSTcpServersName": bwNSPSTcpServersName,
       "bwNSPSTcpServersNbConnectionsAccepted": bwNSPSTcpServersNbConnectionsAccepted,
       "bwNSPSTcpServersNbConnectionsRefused": bwNSPSTcpServersNbConnectionsRefused,
       "bwNSPSTcpServersNbConnectionsInitiated": bwNSPSTcpServersNbConnectionsInitiated,
       "bwNSPSTcpServersNbConnectionsClosed": bwNSPSTcpServersNbConnectionsClosed,
       "bwNSPSTcpServersNbBytesSent": bwNSPSTcpServersNbBytesSent,
       "bwNSPSTcpServersNbBytesReceived": bwNSPSTcpServersNbBytesReceived,
       "bwNSPSTcpServersOutgoingQueueSize": bwNSPSTcpServersOutgoingQueueSize,
       "bwNSPSTcpServersIncomingQueueSize": bwNSPSTcpServersIncomingQueueSize,
       "bwNSPSTcpServersNbBytesSentSecure": bwNSPSTcpServersNbBytesSentSecure,
       "bwNSPSTcpServersNbBytesReceivedSecure": bwNSPSTcpServersNbBytesReceivedSecure,
       "psPersistency": psPersistency,
       "psTimesTen": psTimesTen,
       "psNSTtNbConnectionsCreated": psNSTtNbConnectionsCreated,
       "psNSTtConnectionPoolSize": psNSTtConnectionPoolSize,
       "psNSTtNbBackdoorUpdates": psNSTtNbBackdoorUpdates,
       "psNSTtNbFailedCheckpoints": psNSTtNbFailedCheckpoints,
       "psRemoteXla": psRemoteXla,
       "psNSRemoteXlaNbTimesConnected": psNSRemoteXlaNbTimesConnected,
       "psNSRemoteXlaNbTimesDisconnected": psNSRemoteXlaNbTimesDisconnected,
       "psNSRemoteXlaUpdatesProcessed": psNSRemoteXlaUpdatesProcessed,
       "psNSRemoteXlaUpdatesPending": psNSRemoteXlaUpdatesPending,
       "bwNSPSAvgUpdateTime": bwNSPSAvgUpdateTime,
       "bwNSPSAvgRowsUpdated": bwNSPSAvgRowsUpdated,
       "bwNSPSAvgQueryTime": bwNSPSAvgQueryTime,
       "bwNSPSAvgRowsQueried": bwNSPSAvgRowsQueried,
       "bwNSPSUpdateCount": bwNSPSUpdateCount,
       "bwNSPSQueryCount": bwNSPSQueryCount,
       "bwNSPSTTHWMTable": bwNSPSTTHWMTable,
       "bwNSPSTTHWMEntry": bwNSPSTTHWMEntry,
       "bwNSPSTTHWMIndex": bwNSPSTTHWMIndex,
       "bwNSPSTTHWMName": bwNSPSTTHWMName,
       "bwNSPSTTHWMValue": bwNSPSTTHWMValue,
       "bwNSPSTTHWMTimestamp": bwNSPSTTHWMTimestamp,
       "bwNSPSTTHWMStackTrace": bwNSPSTTHWMStackTrace,
       "psNSPerNbOpenedTransactions": psNSPerNbOpenedTransactions,
       "psNSPerNbCommittedTransactions": psNSPerNbCommittedTransactions,
       "psNSPerNbFailedTransactions": psNSPerNbFailedTransactions,
       "psNSPerNbCriticalErrors": psNSPerNbCriticalErrors,
       "psConcurrent": psConcurrent,
       "bwNSPSMonitoringExecutorTable": bwNSPSMonitoringExecutorTable,
       "bwNSPSMonitoringExecutorEntry": bwNSPSMonitoringExecutorEntry,
       "bwNSPSMonitoringExecutorIndex": bwNSPSMonitoringExecutorIndex,
       "bwNSPSMonitoringExecutorName": bwNSPSMonitoringExecutorName,
       "bwNSPSMonitoringExecutorCurrentPoolSize": bwNSPSMonitoringExecutorCurrentPoolSize,
       "bwNSPSMonitoringExecutorMaxPoolSize": bwNSPSMonitoringExecutorMaxPoolSize,
       "bwNSPSMonitoringExecutorAvgActiveThreads": bwNSPSMonitoringExecutorAvgActiveThreads,
       "bwNSPSMonitoringExecutorTaskQueueSize": bwNSPSMonitoringExecutorTaskQueueSize,
       "bwNSPSMonitoringExecutorNbTasksRun": bwNSPSMonitoringExecutorNbTasksRun,
       "bwNSPSMonitoringExecutorNbWarnings": bwNSPSMonitoringExecutorNbWarnings,
       "bwNSPSMonitoringExecutorNbErrors": bwNSPSMonitoringExecutorNbErrors,
       "bwNSPSMonitoringExecutorLongestTaskMs": bwNSPSMonitoringExecutorLongestTaskMs,
       "bwNSPSMonitoringExecutorLongestTaskName": bwNSPSMonitoringExecutorLongestTaskName,
       "networkServer": networkServer,
       "nsProtocol": nsProtocol,
       "locationApi": locationApi,
       "bwUserLocationRequests": bwUserLocationRequests,
       "bwUserLocationRequestSuccess": bwUserLocationRequestSuccess,
       "bwUserLocationRequestUnknownUser": bwUserLocationRequestUnknownUser,
       "bwUserLocationRequestFailures": bwUserLocationRequestFailures}
)
