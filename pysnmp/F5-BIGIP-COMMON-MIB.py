# SNMP MIB module (F5-BIGIP-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-BIGIP-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:34 2024
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

f5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LongDisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_BigipTrafficMgmt_ObjectIdentity = ObjectIdentity
bigipTrafficMgmt = _BigipTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2)
)
_BigipNotification_ObjectIdentity = ObjectIdentity
bigipNotification = _BigipNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4)
)
_BigipNotifications_ObjectIdentity = ObjectIdentity
bigipNotifications = _BigipNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0)
)
_BigipNotifyObjects_ObjectIdentity = ObjectIdentity
bigipNotifyObjects = _BigipNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 1)
)
_BigipNotifyObjMsg_Type = DisplayString
_BigipNotifyObjMsg_Object = MibScalar
bigipNotifyObjMsg = _BigipNotifyObjMsg_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 1, 1),
    _BigipNotifyObjMsg_Type()
)
bigipNotifyObjMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bigipNotifyObjMsg.setStatus("current")
_BigipNotifyObjNode_Type = DisplayString
_BigipNotifyObjNode_Object = MibScalar
bigipNotifyObjNode = _BigipNotifyObjNode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 1, 2),
    _BigipNotifyObjNode_Type()
)
bigipNotifyObjNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bigipNotifyObjNode.setStatus("current")
_BigipNotifyObjPort_Type = DisplayString
_BigipNotifyObjPort_Object = MibScalar
bigipNotifyObjPort = _BigipNotifyObjPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 1, 3),
    _BigipNotifyObjPort_Type()
)
bigipNotifyObjPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bigipNotifyObjPort.setStatus("current")
_BigipCompliance_ObjectIdentity = ObjectIdentity
bigipCompliance = _BigipCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5)
)
_BigipCompliances_ObjectIdentity = ObjectIdentity
bigipCompliances = _BigipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 1)
)
_BigipGroups_ObjectIdentity = ObjectIdentity
bigipGroups = _BigipGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2)
)
_BigipNotificationGroups_ObjectIdentity = ObjectIdentity
bigipNotificationGroups = _BigipNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 4)
)

# Managed Objects groups

bigipNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 4, 1)
)
bigipNotifyObjectsGroup.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjNode"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjPort"))
)
if mibBuilder.loadTexts:
    bigipNotifyObjectsGroup.setStatus("current")


# Notification objects

bigipAgentStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 1)
)
if mibBuilder.loadTexts:
    bigipAgentStart.setStatus(
        "current"
    )

bigipAgentShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 2)
)
if mibBuilder.loadTexts:
    bigipAgentShutdown.setStatus(
        "current"
    )

bigipAgentRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 3)
)
if mibBuilder.loadTexts:
    bigipAgentRestart.setStatus(
        "current"
    )

bigipCpuTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 4)
)
bigipCpuTempHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipCpuTempHigh.setStatus(
        "current"
    )

bigipCpuFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 5)
)
bigipCpuFanSpeedLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipCpuFanSpeedLow.setStatus(
        "current"
    )

bigipCpuFanSpeedBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 6)
)
bigipCpuFanSpeedBad.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipCpuFanSpeedBad.setStatus(
        "current"
    )

bigipChassisTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 7)
)
bigipChassisTempHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipChassisTempHigh.setStatus(
        "current"
    )

bigipChassisFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 8)
)
bigipChassisFanBad.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipChassisFanBad.setStatus(
        "current"
    )

bigipChassisPowerSupplyBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 9)
)
bigipChassisPowerSupplyBad.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipChassisPowerSupplyBad.setStatus(
        "current"
    )

bigipServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 10)
)
bigipServiceDown.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjNode"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjPort"))
)
if mibBuilder.loadTexts:
    bigipServiceDown.setStatus(
        "current"
    )

bigipServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 11)
)
bigipServiceUp.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjNode"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjPort"))
)
if mibBuilder.loadTexts:
    bigipServiceUp.setStatus(
        "current"
    )

bigipNodeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 12)
)
bigipNodeDown.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjNode"))
)
if mibBuilder.loadTexts:
    bigipNodeDown.setStatus(
        "current"
    )

bigipNodeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 13)
)
bigipNodeUp.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg"),
        ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjNode"))
)
if mibBuilder.loadTexts:
    bigipNodeUp.setStatus(
        "current"
    )

bigipStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 14)
)
bigipStandby.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipStandby.setStatus(
        "current"
    )

bigipActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 15)
)
bigipActive.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipActive.setStatus(
        "current"
    )

bigipActiveActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 16)
)
bigipActiveActive.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipActiveActive.setStatus(
        "current"
    )

bigipFeatureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 17)
)
bigipFeatureFailed.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipFeatureFailed.setStatus(
        "current"
    )

bigipFeatureOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 18)
)
bigipFeatureOnline.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipFeatureOnline.setStatus(
        "current"
    )

bigipLicenseFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 19)
)
bigipLicenseFailed.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLicenseFailed.setStatus(
        "current"
    )

bigipLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 20)
)
bigipLicenseExpired.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLicenseExpired.setStatus(
        "current"
    )

bigipTamdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 21)
)
bigipTamdAlert.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTamdAlert.setStatus(
        "current"
    )

bigipAggrReaperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 22)
)
bigipAggrReaperStateChange.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAggrReaperStateChange.setStatus(
        "current"
    )

bigipARPConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 23)
)
bigipARPConflict.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipARPConflict.setStatus(
        "current"
    )

bigipNetLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 24)
)
bigipNetLinkDown.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipNetLinkDown.setStatus(
        "current"
    )

bigipDiskPartitionWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 25)
)
bigipDiskPartitionWarn.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipDiskPartitionWarn.setStatus(
        "current"
    )

bigipDiskPartitionGrowth = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 26)
)
bigipDiskPartitionGrowth.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipDiskPartitionGrowth.setStatus(
        "current"
    )

bigipAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 27)
)
bigipAuthFailed.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAuthFailed.setStatus(
        "current"
    )

bigipConfigLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 28)
)
bigipConfigLoaded.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipConfigLoaded.setStatus(
        "deprecated"
    )

bigipLogEmerg = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 29)
)
bigipLogEmerg.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLogEmerg.setStatus(
        "current"
    )

bigipLogAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 30)
)
bigipLogAlert.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLogAlert.setStatus(
        "current"
    )

bigipLogCrit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 31)
)
bigipLogCrit.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLogCrit.setStatus(
        "current"
    )

bigipLogErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 32)
)
bigipLogErr.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLogErr.setStatus(
        "current"
    )

bigipLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 33)
)
bigipLogWarning.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLogWarning.setStatus(
        "current"
    )

bigipPacketRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 34)
)
bigipPacketRejected.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipPacketRejected.setStatus(
        "current"
    )

bigipCompLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 35)
)
bigipCompLimitExceeded.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipCompLimitExceeded.setStatus(
        "current"
    )

bigipSslLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 36)
)
bigipSslLimitExceeded.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSslLimitExceeded.setStatus(
        "current"
    )

bigipExternalLinkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 37)
)
bigipExternalLinkChange.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipExternalLinkChange.setStatus(
        "current"
    )

bigipAsmRequestBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 38)
)
bigipAsmRequestBlocked.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmRequestBlocked.setStatus(
        "current"
    )

bigipAsmRequestViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 39)
)
bigipAsmRequestViolation.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmRequestViolation.setStatus(
        "current"
    )

bigipGtmPoolAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 40)
)
bigipGtmPoolAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolAvail.setStatus(
        "current"
    )

bigipGtmPoolNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 41)
)
bigipGtmPoolNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolNotAvail.setStatus(
        "current"
    )

bigipGtmPoolDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 42)
)
bigipGtmPoolDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolDisabled.setStatus(
        "current"
    )

bigipGtmPoolEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 43)
)
bigipGtmPoolEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolEnabled.setStatus(
        "current"
    )

bigipGtmLinkAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 44)
)
bigipGtmLinkAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmLinkAvail.setStatus(
        "current"
    )

bigipGtmLinkNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 45)
)
bigipGtmLinkNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmLinkNotAvail.setStatus(
        "current"
    )

bigipGtmLinkDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 46)
)
bigipGtmLinkDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmLinkDisabled.setStatus(
        "current"
    )

bigipGtmLinkEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 47)
)
bigipGtmLinkEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmLinkEnabled.setStatus(
        "current"
    )

bigipGtmWideIpAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 48)
)
bigipGtmWideIpAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmWideIpAvail.setStatus(
        "current"
    )

bigipGtmWideIpNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 49)
)
bigipGtmWideIpNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmWideIpNotAvail.setStatus(
        "current"
    )

bigipGtmWideIpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 50)
)
bigipGtmWideIpDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmWideIpDisabled.setStatus(
        "current"
    )

bigipGtmWideIpEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 51)
)
bigipGtmWideIpEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmWideIpEnabled.setStatus(
        "current"
    )

bigipGtmPoolMbrAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 52)
)
bigipGtmPoolMbrAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolMbrAvail.setStatus(
        "current"
    )

bigipGtmPoolMbrNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 53)
)
bigipGtmPoolMbrNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolMbrNotAvail.setStatus(
        "current"
    )

bigipGtmPoolMbrDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 54)
)
bigipGtmPoolMbrDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolMbrDisabled.setStatus(
        "current"
    )

bigipGtmPoolMbrEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 55)
)
bigipGtmPoolMbrEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmPoolMbrEnabled.setStatus(
        "current"
    )

bigipGtmServerAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 56)
)
bigipGtmServerAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmServerAvail.setStatus(
        "current"
    )

bigipGtmServerNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 57)
)
bigipGtmServerNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmServerNotAvail.setStatus(
        "current"
    )

bigipGtmServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 58)
)
bigipGtmServerDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmServerDisabled.setStatus(
        "current"
    )

bigipGtmServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 59)
)
bigipGtmServerEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmServerEnabled.setStatus(
        "current"
    )

bigipGtmVsAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 60)
)
bigipGtmVsAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmVsAvail.setStatus(
        "current"
    )

bigipGtmVsNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 61)
)
bigipGtmVsNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmVsNotAvail.setStatus(
        "current"
    )

bigipGtmVsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 62)
)
bigipGtmVsDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmVsDisabled.setStatus(
        "current"
    )

bigipGtmVsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 63)
)
bigipGtmVsEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmVsEnabled.setStatus(
        "current"
    )

bigipGtmDcAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 64)
)
bigipGtmDcAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmDcAvail.setStatus(
        "current"
    )

bigipGtmDcNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 65)
)
bigipGtmDcNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmDcNotAvail.setStatus(
        "current"
    )

bigipGtmDcDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 66)
)
bigipGtmDcDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmDcDisabled.setStatus(
        "current"
    )

bigipGtmDcEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 67)
)
bigipGtmDcEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmDcEnabled.setStatus(
        "current"
    )

bigipHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 68)
)
bigipHardDiskFailure.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipHardDiskFailure.setStatus(
        "deprecated"
    )

bigipGtmAppObjAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 69)
)
bigipGtmAppObjAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmAppObjAvail.setStatus(
        "current"
    )

bigipGtmAppObjNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 70)
)
bigipGtmAppObjNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmAppObjNotAvail.setStatus(
        "current"
    )

bigipGtmAppAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 71)
)
bigipGtmAppAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmAppAvail.setStatus(
        "current"
    )

bigipGtmAppNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 72)
)
bigipGtmAppNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmAppNotAvail.setStatus(
        "current"
    )

bigipGtmJoinedGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 73)
)
bigipGtmJoinedGroup.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmJoinedGroup.setStatus(
        "current"
    )

bigipGtmLeftGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 74)
)
bigipGtmLeftGroup.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmLeftGroup.setStatus(
        "current"
    )

bigipStandByFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 75)
)
bigipStandByFail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipStandByFail.setStatus(
        "current"
    )

bigipInetPortExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 76)
)
bigipInetPortExhaustion.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipInetPortExhaustion.setStatus(
        "current"
    )

bigipGtmBoxAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 77)
)
bigipGtmBoxAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmBoxAvail.setStatus(
        "current"
    )

bigipGtmBoxNotAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 78)
)
bigipGtmBoxNotAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmBoxNotAvail.setStatus(
        "current"
    )

bigipAsmFtpRequestBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 79)
)
bigipAsmFtpRequestBlocked.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmFtpRequestBlocked.setStatus(
        "current"
    )

bigipAsmFtpRequestViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 80)
)
bigipAsmFtpRequestViolation.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmFtpRequestViolation.setStatus(
        "current"
    )

bigipGtmBig3dSslCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 81)
)
bigipGtmBig3dSslCertExpired.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmBig3dSslCertExpired.setStatus(
        "current"
    )

bigipGtmBig3dSslCertWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 82)
)
bigipGtmBig3dSslCertWillExpire.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmBig3dSslCertWillExpire.setStatus(
        "current"
    )

bigipGtmSslCertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 83)
)
bigipGtmSslCertExpired.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmSslCertExpired.setStatus(
        "current"
    )

bigipGtmSslCertWillExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 84)
)
bigipGtmSslCertWillExpire.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmSslCertWillExpire.setStatus(
        "current"
    )

bigipAsmSmtpRequestBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 85)
)
bigipAsmSmtpRequestBlocked.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmSmtpRequestBlocked.setStatus(
        "current"
    )

bigipAsmSmtpRequestViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 86)
)
bigipAsmSmtpRequestViolation.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmSmtpRequestViolation.setStatus(
        "current"
    )

bigipBladeTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 87)
)
bigipBladeTempHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipBladeTempHigh.setStatus(
        "current"
    )

bigipBladeNoPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 88)
)
bigipBladeNoPower.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipBladeNoPower.setStatus(
        "current"
    )

bigipClusterdNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 89)
)
bigipClusterdNoResponse.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipClusterdNoResponse.setStatus(
        "current"
    )

bigipBladeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 90)
)
bigipBladeOffline.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipBladeOffline.setStatus(
        "current"
    )

bigipAsmDosAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 91)
)
bigipAsmDosAttackDetected.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmDosAttackDetected.setStatus(
        "current"
    )

bigipAsmBruteForceAttackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 92)
)
bigipAsmBruteForceAttackDetected.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAsmBruteForceAttackDetected.setStatus(
        "current"
    )

bigipAomCpuTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 93)
)
bigipAomCpuTempTooHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAomCpuTempTooHigh.setStatus(
        "current"
    )

bigipGtmKeyGenerationRollover = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 94)
)
bigipGtmKeyGenerationRollover.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmKeyGenerationRollover.setStatus(
        "current"
    )

bigipGtmKeyGenerationExpiration = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 95)
)
bigipGtmKeyGenerationExpiration.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmKeyGenerationExpiration.setStatus(
        "current"
    )

bigipRaidDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 96)
)
bigipRaidDiskFailure.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipRaidDiskFailure.setStatus(
        "current"
    )

bigipGtmProberPoolStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 97)
)
bigipGtmProberPoolStatusChange.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolStatusChange.setStatus(
        "current"
    )

bigipGtmProberPoolStatusChangeReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 98)
)
bigipGtmProberPoolStatusChangeReason.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolStatusChangeReason.setStatus(
        "current"
    )

bigipGtmProberPoolDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 99)
)
bigipGtmProberPoolDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolDisabled.setStatus(
        "current"
    )

bigipGtmProberPoolEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 100)
)
bigipGtmProberPoolEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolEnabled.setStatus(
        "current"
    )

bigipGtmProberPoolMbrStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 101)
)
bigipGtmProberPoolMbrStatusChange.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolMbrStatusChange.setStatus(
        "current"
    )

bigipGtmProberPoolMbrStatusChangeReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 102)
)
bigipGtmProberPoolMbrStatusChangeReason.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolMbrStatusChangeReason.setStatus(
        "current"
    )

bigipGtmProberPoolMbrDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 103)
)
bigipGtmProberPoolMbrDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolMbrDisabled.setStatus(
        "current"
    )

bigipGtmProberPoolMbrEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 104)
)
bigipGtmProberPoolMbrEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmProberPoolMbrEnabled.setStatus(
        "current"
    )

bigipAvrAlertsMetricSnmp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 105)
)
bigipAvrAlertsMetricSnmp.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAvrAlertsMetricSnmp.setStatus(
        "current"
    )

bigipAvrAlertsMetricSmtp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 106)
)
bigipAvrAlertsMetricSmtp.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipAvrAlertsMetricSmtp.setStatus(
        "deprecated"
    )

bigipVcmpAlertsVcmpPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 107)
)
bigipVcmpAlertsVcmpPowerOn.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipVcmpAlertsVcmpPowerOn.setStatus(
        "current"
    )

bigipVcmpAlertsVcmpPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 108)
)
bigipVcmpAlertsVcmpPowerOff.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipVcmpAlertsVcmpPowerOff.setStatus(
        "current"
    )

bigipVcmpAlertsVcmpHBLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 109)
)
bigipVcmpAlertsVcmpHBLost.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipVcmpAlertsVcmpHBLost.setStatus(
        "current"
    )

bigipVcmpAlertsVcmpHBDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 110)
)
bigipVcmpAlertsVcmpHBDetected.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipVcmpAlertsVcmpHBDetected.setStatus(
        "current"
    )

bigipSsdMwiNearThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 111)
)
bigipSsdMwiNearThreshold.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSsdMwiNearThreshold.setStatus(
        "current"
    )

bigipSsdMwiReachedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 112)
)
bigipSsdMwiReachedThreshold.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSsdMwiReachedThreshold.setStatus(
        "current"
    )

bigipSystemCheckAlertTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 113)
)
bigipSystemCheckAlertTempHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertTempHigh.setStatus(
        "current"
    )

bigipSystemCheckAlertVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 114)
)
bigipSystemCheckAlertVoltageHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertVoltageHigh.setStatus(
        "current"
    )

bigipSystemCheckAlertFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 115)
)
bigipSystemCheckAlertFanSpeedLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertFanSpeedLow.setStatus(
        "current"
    )

bigipLibhalSsdPhysicalDiskRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 116)
)
bigipLibhalSsdPhysicalDiskRemoved.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLibhalSsdPhysicalDiskRemoved.setStatus(
        "current"
    )

bigipLibhalSsdLogicalDiskRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 117)
)
bigipLibhalSsdLogicalDiskRemoved.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLibhalSsdLogicalDiskRemoved.setStatus(
        "current"
    )

bigipLibhalDiskBayRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 118)
)
bigipLibhalDiskBayRemoved.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLibhalDiskBayRemoved.setStatus(
        "current"
    )

bigipLibhalBladePoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 119)
)
bigipLibhalBladePoweredOff.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLibhalBladePoweredOff.setStatus(
        "current"
    )

bigipLibhalSensorAlarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 120)
)
bigipLibhalSensorAlarmCritical.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLibhalSensorAlarmCritical.setStatus(
        "current"
    )

bigipChmandAlertFanTrayBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 121)
)
bigipChmandAlertFanTrayBad.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipChmandAlertFanTrayBad.setStatus(
        "current"
    )

bigipUnsolicitedRepliesExceededThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 122)
)
bigipUnsolicitedRepliesExceededThreshold.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipUnsolicitedRepliesExceededThreshold.setStatus(
        "current"
    )

bigipSystemCheckAlertVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 123)
)
bigipSystemCheckAlertVoltageLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertVoltageLow.setStatus(
        "current"
    )

bigipSystemCheckAlertMilliVoltageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 124)
)
bigipSystemCheckAlertMilliVoltageHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertMilliVoltageHigh.setStatus(
        "current"
    )

bigipSystemCheckAlertCurrentHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 125)
)
bigipSystemCheckAlertCurrentHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertCurrentHigh.setStatus(
        "current"
    )

bigipSystemCheckAlertPowerHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 126)
)
bigipSystemCheckAlertPowerHigh.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertPowerHigh.setStatus(
        "current"
    )

bigipSystemCheckAlertMilliVoltageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 127)
)
bigipSystemCheckAlertMilliVoltageLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertMilliVoltageLow.setStatus(
        "current"
    )

bigipSystemCheckAlertCurrentLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 128)
)
bigipSystemCheckAlertCurrentLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertCurrentLow.setStatus(
        "current"
    )

bigipSystemCheckAlertPowerLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 129)
)
bigipSystemCheckAlertPowerLow.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemCheckAlertPowerLow.setStatus(
        "current"
    )

bigipNodeRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 130)
)
bigipNodeRate.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipNodeRate.setStatus(
        "current"
    )

bigipMemberRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 131)
)
bigipMemberRate.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipMemberRate.setStatus(
        "current"
    )

bigipVirtualRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 132)
)
bigipVirtualRate.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipVirtualRate.setStatus(
        "current"
    )

bigipDosAttackStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 133)
)
bigipDosAttackStart.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipDosAttackStart.setStatus(
        "current"
    )

bigipDosAttackStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 134)
)
bigipDosAttackStop.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipDosAttackStop.setStatus(
        "current"
    )

bigipLtmVsAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 135)
)
bigipLtmVsAvail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLtmVsAvail.setStatus(
        "current"
    )

bigipLtmVsUnavail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 136)
)
bigipLtmVsUnavail.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLtmVsUnavail.setStatus(
        "current"
    )

bigipLtmVsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 137)
)
bigipLtmVsEnabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLtmVsEnabled.setStatus(
        "current"
    )

bigipLtmVsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 138)
)
bigipLtmVsDisabled.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipLtmVsDisabled.setStatus(
        "current"
    )

bigipDnsRequestRateLimiterEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 139)
)
bigipDnsRequestRateLimiterEngaged.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipDnsRequestRateLimiterEngaged.setStatus(
        "current"
    )

bigipGtmRequestRateLimiterEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 140)
)
bigipGtmRequestRateLimiterEngaged.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipGtmRequestRateLimiterEngaged.setStatus(
        "current"
    )

bigipTrafficGroupStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 141)
)
bigipTrafficGroupStandby.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupStandby.setStatus(
        "current"
    )

bigipTrafficGroupActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 142)
)
bigipTrafficGroupActive.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupActive.setStatus(
        "current"
    )

bigipTrafficGroupOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 143)
)
bigipTrafficGroupOffline.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupOffline.setStatus(
        "current"
    )

bigipTrafficGroupForcedOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 144)
)
bigipTrafficGroupForcedOffline.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupForcedOffline.setStatus(
        "current"
    )

bigipTrafficGroupDeactivate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 145)
)
bigipTrafficGroupDeactivate.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupDeactivate.setStatus(
        "current"
    )

bigipTrafficGroupActivate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 146)
)
bigipTrafficGroupActivate.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipTrafficGroupActivate.setStatus(
        "current"
    )

bigipPsPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 147)
)
bigipPsPowerOn.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipPsPowerOn.setStatus(
        "current"
    )

bigipPsPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 148)
)
bigipPsPowerOff.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipPsPowerOff.setStatus(
        "current"
    )

bigipPsAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 149)
)
bigipPsAbsent.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipPsAbsent.setStatus(
        "current"
    )

bigipClusterPrimaryChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 150)
)
bigipClusterPrimaryChanged.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipClusterPrimaryChanged.setStatus(
        "current"
    )

bigipSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 151)
)
bigipSystemShutdown.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipSystemShutdown.setStatus(
        "current"
    )

bigipFipsDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 152)
)
bigipFipsDeviceError.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipFipsDeviceError.setStatus(
        "current"
    )

bigipUpdatePriority = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 153)
)
bigipUpdatePriority.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipUpdatePriority.setStatus(
        "current"
    )

bigipUpdateServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 154)
)
bigipUpdateServer.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipUpdateServer.setStatus(
        "current"
    )

bigipUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 155)
)
bigipUpdateError.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipUpdateError.setStatus(
        "current"
    )

bigipFipsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 2, 4, 0, 156)
)
bigipFipsFault.setObjects(
    ("F5-BIGIP-COMMON-MIB", "bigipNotifyObjMsg")
)
if mibBuilder.loadTexts:
    bigipFipsFault.setStatus(
        "current"
    )


# Notifications groups

bigipAgentNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 4, 2)
)
bigipAgentNotifyGroup.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipAgentStart"),
        ("F5-BIGIP-COMMON-MIB", "bigipAgentShutdown"),
        ("F5-BIGIP-COMMON-MIB", "bigipAgentRestart"))
)
if mibBuilder.loadTexts:
    bigipAgentNotifyGroup.setStatus(
        "current"
    )

bigipSystemNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 4, 3)
)
bigipSystemNotifyGroup.setObjects(
      *(("F5-BIGIP-COMMON-MIB", "bigipCpuTempHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipCpuFanSpeedLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipCpuFanSpeedBad"),
        ("F5-BIGIP-COMMON-MIB", "bigipChassisTempHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipChassisFanBad"),
        ("F5-BIGIP-COMMON-MIB", "bigipChassisPowerSupplyBad"),
        ("F5-BIGIP-COMMON-MIB", "bigipServiceDown"),
        ("F5-BIGIP-COMMON-MIB", "bigipServiceUp"),
        ("F5-BIGIP-COMMON-MIB", "bigipNodeDown"),
        ("F5-BIGIP-COMMON-MIB", "bigipNodeUp"),
        ("F5-BIGIP-COMMON-MIB", "bigipStandby"),
        ("F5-BIGIP-COMMON-MIB", "bigipActive"),
        ("F5-BIGIP-COMMON-MIB", "bigipActiveActive"),
        ("F5-BIGIP-COMMON-MIB", "bigipFeatureFailed"),
        ("F5-BIGIP-COMMON-MIB", "bigipFeatureOnline"),
        ("F5-BIGIP-COMMON-MIB", "bigipLicenseFailed"),
        ("F5-BIGIP-COMMON-MIB", "bigipLicenseExpired"),
        ("F5-BIGIP-COMMON-MIB", "bigipTamdAlert"),
        ("F5-BIGIP-COMMON-MIB", "bigipAggrReaperStateChange"),
        ("F5-BIGIP-COMMON-MIB", "bigipARPConflict"),
        ("F5-BIGIP-COMMON-MIB", "bigipNetLinkDown"),
        ("F5-BIGIP-COMMON-MIB", "bigipDiskPartitionWarn"),
        ("F5-BIGIP-COMMON-MIB", "bigipDiskPartitionGrowth"),
        ("F5-BIGIP-COMMON-MIB", "bigipAuthFailed"),
        ("F5-BIGIP-COMMON-MIB", "bigipConfigLoaded"),
        ("F5-BIGIP-COMMON-MIB", "bigipLogEmerg"),
        ("F5-BIGIP-COMMON-MIB", "bigipLogAlert"),
        ("F5-BIGIP-COMMON-MIB", "bigipLogCrit"),
        ("F5-BIGIP-COMMON-MIB", "bigipLogErr"),
        ("F5-BIGIP-COMMON-MIB", "bigipLogWarning"),
        ("F5-BIGIP-COMMON-MIB", "bigipPacketRejected"),
        ("F5-BIGIP-COMMON-MIB", "bigipCompLimitExceeded"),
        ("F5-BIGIP-COMMON-MIB", "bigipSslLimitExceeded"),
        ("F5-BIGIP-COMMON-MIB", "bigipExternalLinkChange"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmRequestBlocked"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmRequestViolation"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmLinkAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmLinkNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmLinkDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmLinkEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmWideIpAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmWideIpNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmWideIpDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmWideIpEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolMbrAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolMbrNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolMbrDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmPoolMbrEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmServerAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmServerNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmServerDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmServerEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmVsAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmVsNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmVsDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmVsEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmDcAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmDcNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmDcDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmDcEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipHardDiskFailure"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmAppObjAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmAppObjNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmAppAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmAppNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmJoinedGroup"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmLeftGroup"),
        ("F5-BIGIP-COMMON-MIB", "bigipStandByFail"),
        ("F5-BIGIP-COMMON-MIB", "bigipInetPortExhaustion"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmBoxAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmBoxNotAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmFtpRequestBlocked"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmFtpRequestViolation"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmBig3dSslCertExpired"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmBig3dSslCertWillExpire"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmSslCertExpired"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmSslCertWillExpire"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmSmtpRequestBlocked"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmSmtpRequestViolation"),
        ("F5-BIGIP-COMMON-MIB", "bigipBladeTempHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipBladeNoPower"),
        ("F5-BIGIP-COMMON-MIB", "bigipClusterdNoResponse"),
        ("F5-BIGIP-COMMON-MIB", "bigipBladeOffline"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmDosAttackDetected"),
        ("F5-BIGIP-COMMON-MIB", "bigipAsmBruteForceAttackDetected"),
        ("F5-BIGIP-COMMON-MIB", "bigipAomCpuTempTooHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmKeyGenerationRollover"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmKeyGenerationExpiration"),
        ("F5-BIGIP-COMMON-MIB", "bigipRaidDiskFailure"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolStatusChange"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolStatusChangeReason"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolMbrStatusChange"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolMbrStatusChangeReason"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolMbrDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmProberPoolMbrEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipAvrAlertsMetricSnmp"),
        ("F5-BIGIP-COMMON-MIB", "bigipAvrAlertsMetricSmtp"),
        ("F5-BIGIP-COMMON-MIB", "bigipVcmpAlertsVcmpPowerOn"),
        ("F5-BIGIP-COMMON-MIB", "bigipVcmpAlertsVcmpPowerOff"),
        ("F5-BIGIP-COMMON-MIB", "bigipVcmpAlertsVcmpHBLost"),
        ("F5-BIGIP-COMMON-MIB", "bigipVcmpAlertsVcmpHBDetected"),
        ("F5-BIGIP-COMMON-MIB", "bigipSsdMwiNearThreshold"),
        ("F5-BIGIP-COMMON-MIB", "bigipSsdMwiReachedThreshold"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertTempHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertVoltageHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertFanSpeedLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipLibhalSsdPhysicalDiskRemoved"),
        ("F5-BIGIP-COMMON-MIB", "bigipLibhalSsdLogicalDiskRemoved"),
        ("F5-BIGIP-COMMON-MIB", "bigipLibhalDiskBayRemoved"),
        ("F5-BIGIP-COMMON-MIB", "bigipLibhalBladePoweredOff"),
        ("F5-BIGIP-COMMON-MIB", "bigipLibhalSensorAlarmCritical"),
        ("F5-BIGIP-COMMON-MIB", "bigipChmandAlertFanTrayBad"),
        ("F5-BIGIP-COMMON-MIB", "bigipUnsolicitedRepliesExceededThreshold"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertVoltageLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertMilliVoltageHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertCurrentHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertPowerHigh"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertMilliVoltageLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertCurrentLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemCheckAlertPowerLow"),
        ("F5-BIGIP-COMMON-MIB", "bigipNodeRate"),
        ("F5-BIGIP-COMMON-MIB", "bigipMemberRate"),
        ("F5-BIGIP-COMMON-MIB", "bigipVirtualRate"),
        ("F5-BIGIP-COMMON-MIB", "bigipDosAttackStart"),
        ("F5-BIGIP-COMMON-MIB", "bigipDosAttackStop"),
        ("F5-BIGIP-COMMON-MIB", "bigipLtmVsAvail"),
        ("F5-BIGIP-COMMON-MIB", "bigipLtmVsUnavail"),
        ("F5-BIGIP-COMMON-MIB", "bigipLtmVsEnabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipLtmVsDisabled"),
        ("F5-BIGIP-COMMON-MIB", "bigipDnsRequestRateLimiterEngaged"),
        ("F5-BIGIP-COMMON-MIB", "bigipGtmRequestRateLimiterEngaged"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupStandby"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupActive"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupOffline"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupForcedOffline"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupDeactivate"),
        ("F5-BIGIP-COMMON-MIB", "bigipTrafficGroupActivate"),
        ("F5-BIGIP-COMMON-MIB", "bigipPsPowerOn"),
        ("F5-BIGIP-COMMON-MIB", "bigipPsPowerOff"),
        ("F5-BIGIP-COMMON-MIB", "bigipPsAbsent"),
        ("F5-BIGIP-COMMON-MIB", "bigipClusterPrimaryChanged"),
        ("F5-BIGIP-COMMON-MIB", "bigipSystemShutdown"),
        ("F5-BIGIP-COMMON-MIB", "bigipFipsDeviceError"),
        ("F5-BIGIP-COMMON-MIB", "bigipUpdatePriority"),
        ("F5-BIGIP-COMMON-MIB", "bigipUpdateServer"),
        ("F5-BIGIP-COMMON-MIB", "bigipUpdateError"),
        ("F5-BIGIP-COMMON-MIB", "bigipFipsFault"))
)
if mibBuilder.loadTexts:
    bigipSystemNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bigipNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    bigipNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-BIGIP-COMMON-MIB",
    **{"LongDisplayString": LongDisplayString,
       "f5": f5,
       "bigipTrafficMgmt": bigipTrafficMgmt,
       "bigipNotification": bigipNotification,
       "bigipNotifications": bigipNotifications,
       "bigipAgentStart": bigipAgentStart,
       "bigipAgentShutdown": bigipAgentShutdown,
       "bigipAgentRestart": bigipAgentRestart,
       "bigipCpuTempHigh": bigipCpuTempHigh,
       "bigipCpuFanSpeedLow": bigipCpuFanSpeedLow,
       "bigipCpuFanSpeedBad": bigipCpuFanSpeedBad,
       "bigipChassisTempHigh": bigipChassisTempHigh,
       "bigipChassisFanBad": bigipChassisFanBad,
       "bigipChassisPowerSupplyBad": bigipChassisPowerSupplyBad,
       "bigipServiceDown": bigipServiceDown,
       "bigipServiceUp": bigipServiceUp,
       "bigipNodeDown": bigipNodeDown,
       "bigipNodeUp": bigipNodeUp,
       "bigipStandby": bigipStandby,
       "bigipActive": bigipActive,
       "bigipActiveActive": bigipActiveActive,
       "bigipFeatureFailed": bigipFeatureFailed,
       "bigipFeatureOnline": bigipFeatureOnline,
       "bigipLicenseFailed": bigipLicenseFailed,
       "bigipLicenseExpired": bigipLicenseExpired,
       "bigipTamdAlert": bigipTamdAlert,
       "bigipAggrReaperStateChange": bigipAggrReaperStateChange,
       "bigipARPConflict": bigipARPConflict,
       "bigipNetLinkDown": bigipNetLinkDown,
       "bigipDiskPartitionWarn": bigipDiskPartitionWarn,
       "bigipDiskPartitionGrowth": bigipDiskPartitionGrowth,
       "bigipAuthFailed": bigipAuthFailed,
       "bigipConfigLoaded": bigipConfigLoaded,
       "bigipLogEmerg": bigipLogEmerg,
       "bigipLogAlert": bigipLogAlert,
       "bigipLogCrit": bigipLogCrit,
       "bigipLogErr": bigipLogErr,
       "bigipLogWarning": bigipLogWarning,
       "bigipPacketRejected": bigipPacketRejected,
       "bigipCompLimitExceeded": bigipCompLimitExceeded,
       "bigipSslLimitExceeded": bigipSslLimitExceeded,
       "bigipExternalLinkChange": bigipExternalLinkChange,
       "bigipAsmRequestBlocked": bigipAsmRequestBlocked,
       "bigipAsmRequestViolation": bigipAsmRequestViolation,
       "bigipGtmPoolAvail": bigipGtmPoolAvail,
       "bigipGtmPoolNotAvail": bigipGtmPoolNotAvail,
       "bigipGtmPoolDisabled": bigipGtmPoolDisabled,
       "bigipGtmPoolEnabled": bigipGtmPoolEnabled,
       "bigipGtmLinkAvail": bigipGtmLinkAvail,
       "bigipGtmLinkNotAvail": bigipGtmLinkNotAvail,
       "bigipGtmLinkDisabled": bigipGtmLinkDisabled,
       "bigipGtmLinkEnabled": bigipGtmLinkEnabled,
       "bigipGtmWideIpAvail": bigipGtmWideIpAvail,
       "bigipGtmWideIpNotAvail": bigipGtmWideIpNotAvail,
       "bigipGtmWideIpDisabled": bigipGtmWideIpDisabled,
       "bigipGtmWideIpEnabled": bigipGtmWideIpEnabled,
       "bigipGtmPoolMbrAvail": bigipGtmPoolMbrAvail,
       "bigipGtmPoolMbrNotAvail": bigipGtmPoolMbrNotAvail,
       "bigipGtmPoolMbrDisabled": bigipGtmPoolMbrDisabled,
       "bigipGtmPoolMbrEnabled": bigipGtmPoolMbrEnabled,
       "bigipGtmServerAvail": bigipGtmServerAvail,
       "bigipGtmServerNotAvail": bigipGtmServerNotAvail,
       "bigipGtmServerDisabled": bigipGtmServerDisabled,
       "bigipGtmServerEnabled": bigipGtmServerEnabled,
       "bigipGtmVsAvail": bigipGtmVsAvail,
       "bigipGtmVsNotAvail": bigipGtmVsNotAvail,
       "bigipGtmVsDisabled": bigipGtmVsDisabled,
       "bigipGtmVsEnabled": bigipGtmVsEnabled,
       "bigipGtmDcAvail": bigipGtmDcAvail,
       "bigipGtmDcNotAvail": bigipGtmDcNotAvail,
       "bigipGtmDcDisabled": bigipGtmDcDisabled,
       "bigipGtmDcEnabled": bigipGtmDcEnabled,
       "bigipHardDiskFailure": bigipHardDiskFailure,
       "bigipGtmAppObjAvail": bigipGtmAppObjAvail,
       "bigipGtmAppObjNotAvail": bigipGtmAppObjNotAvail,
       "bigipGtmAppAvail": bigipGtmAppAvail,
       "bigipGtmAppNotAvail": bigipGtmAppNotAvail,
       "bigipGtmJoinedGroup": bigipGtmJoinedGroup,
       "bigipGtmLeftGroup": bigipGtmLeftGroup,
       "bigipStandByFail": bigipStandByFail,
       "bigipInetPortExhaustion": bigipInetPortExhaustion,
       "bigipGtmBoxAvail": bigipGtmBoxAvail,
       "bigipGtmBoxNotAvail": bigipGtmBoxNotAvail,
       "bigipAsmFtpRequestBlocked": bigipAsmFtpRequestBlocked,
       "bigipAsmFtpRequestViolation": bigipAsmFtpRequestViolation,
       "bigipGtmBig3dSslCertExpired": bigipGtmBig3dSslCertExpired,
       "bigipGtmBig3dSslCertWillExpire": bigipGtmBig3dSslCertWillExpire,
       "bigipGtmSslCertExpired": bigipGtmSslCertExpired,
       "bigipGtmSslCertWillExpire": bigipGtmSslCertWillExpire,
       "bigipAsmSmtpRequestBlocked": bigipAsmSmtpRequestBlocked,
       "bigipAsmSmtpRequestViolation": bigipAsmSmtpRequestViolation,
       "bigipBladeTempHigh": bigipBladeTempHigh,
       "bigipBladeNoPower": bigipBladeNoPower,
       "bigipClusterdNoResponse": bigipClusterdNoResponse,
       "bigipBladeOffline": bigipBladeOffline,
       "bigipAsmDosAttackDetected": bigipAsmDosAttackDetected,
       "bigipAsmBruteForceAttackDetected": bigipAsmBruteForceAttackDetected,
       "bigipAomCpuTempTooHigh": bigipAomCpuTempTooHigh,
       "bigipGtmKeyGenerationRollover": bigipGtmKeyGenerationRollover,
       "bigipGtmKeyGenerationExpiration": bigipGtmKeyGenerationExpiration,
       "bigipRaidDiskFailure": bigipRaidDiskFailure,
       "bigipGtmProberPoolStatusChange": bigipGtmProberPoolStatusChange,
       "bigipGtmProberPoolStatusChangeReason": bigipGtmProberPoolStatusChangeReason,
       "bigipGtmProberPoolDisabled": bigipGtmProberPoolDisabled,
       "bigipGtmProberPoolEnabled": bigipGtmProberPoolEnabled,
       "bigipGtmProberPoolMbrStatusChange": bigipGtmProberPoolMbrStatusChange,
       "bigipGtmProberPoolMbrStatusChangeReason": bigipGtmProberPoolMbrStatusChangeReason,
       "bigipGtmProberPoolMbrDisabled": bigipGtmProberPoolMbrDisabled,
       "bigipGtmProberPoolMbrEnabled": bigipGtmProberPoolMbrEnabled,
       "bigipAvrAlertsMetricSnmp": bigipAvrAlertsMetricSnmp,
       "bigipAvrAlertsMetricSmtp": bigipAvrAlertsMetricSmtp,
       "bigipVcmpAlertsVcmpPowerOn": bigipVcmpAlertsVcmpPowerOn,
       "bigipVcmpAlertsVcmpPowerOff": bigipVcmpAlertsVcmpPowerOff,
       "bigipVcmpAlertsVcmpHBLost": bigipVcmpAlertsVcmpHBLost,
       "bigipVcmpAlertsVcmpHBDetected": bigipVcmpAlertsVcmpHBDetected,
       "bigipSsdMwiNearThreshold": bigipSsdMwiNearThreshold,
       "bigipSsdMwiReachedThreshold": bigipSsdMwiReachedThreshold,
       "bigipSystemCheckAlertTempHigh": bigipSystemCheckAlertTempHigh,
       "bigipSystemCheckAlertVoltageHigh": bigipSystemCheckAlertVoltageHigh,
       "bigipSystemCheckAlertFanSpeedLow": bigipSystemCheckAlertFanSpeedLow,
       "bigipLibhalSsdPhysicalDiskRemoved": bigipLibhalSsdPhysicalDiskRemoved,
       "bigipLibhalSsdLogicalDiskRemoved": bigipLibhalSsdLogicalDiskRemoved,
       "bigipLibhalDiskBayRemoved": bigipLibhalDiskBayRemoved,
       "bigipLibhalBladePoweredOff": bigipLibhalBladePoweredOff,
       "bigipLibhalSensorAlarmCritical": bigipLibhalSensorAlarmCritical,
       "bigipChmandAlertFanTrayBad": bigipChmandAlertFanTrayBad,
       "bigipUnsolicitedRepliesExceededThreshold": bigipUnsolicitedRepliesExceededThreshold,
       "bigipSystemCheckAlertVoltageLow": bigipSystemCheckAlertVoltageLow,
       "bigipSystemCheckAlertMilliVoltageHigh": bigipSystemCheckAlertMilliVoltageHigh,
       "bigipSystemCheckAlertCurrentHigh": bigipSystemCheckAlertCurrentHigh,
       "bigipSystemCheckAlertPowerHigh": bigipSystemCheckAlertPowerHigh,
       "bigipSystemCheckAlertMilliVoltageLow": bigipSystemCheckAlertMilliVoltageLow,
       "bigipSystemCheckAlertCurrentLow": bigipSystemCheckAlertCurrentLow,
       "bigipSystemCheckAlertPowerLow": bigipSystemCheckAlertPowerLow,
       "bigipNodeRate": bigipNodeRate,
       "bigipMemberRate": bigipMemberRate,
       "bigipVirtualRate": bigipVirtualRate,
       "bigipDosAttackStart": bigipDosAttackStart,
       "bigipDosAttackStop": bigipDosAttackStop,
       "bigipLtmVsAvail": bigipLtmVsAvail,
       "bigipLtmVsUnavail": bigipLtmVsUnavail,
       "bigipLtmVsEnabled": bigipLtmVsEnabled,
       "bigipLtmVsDisabled": bigipLtmVsDisabled,
       "bigipDnsRequestRateLimiterEngaged": bigipDnsRequestRateLimiterEngaged,
       "bigipGtmRequestRateLimiterEngaged": bigipGtmRequestRateLimiterEngaged,
       "bigipTrafficGroupStandby": bigipTrafficGroupStandby,
       "bigipTrafficGroupActive": bigipTrafficGroupActive,
       "bigipTrafficGroupOffline": bigipTrafficGroupOffline,
       "bigipTrafficGroupForcedOffline": bigipTrafficGroupForcedOffline,
       "bigipTrafficGroupDeactivate": bigipTrafficGroupDeactivate,
       "bigipTrafficGroupActivate": bigipTrafficGroupActivate,
       "bigipPsPowerOn": bigipPsPowerOn,
       "bigipPsPowerOff": bigipPsPowerOff,
       "bigipPsAbsent": bigipPsAbsent,
       "bigipClusterPrimaryChanged": bigipClusterPrimaryChanged,
       "bigipSystemShutdown": bigipSystemShutdown,
       "bigipFipsDeviceError": bigipFipsDeviceError,
       "bigipUpdatePriority": bigipUpdatePriority,
       "bigipUpdateServer": bigipUpdateServer,
       "bigipUpdateError": bigipUpdateError,
       "bigipFipsFault": bigipFipsFault,
       "bigipNotifyObjects": bigipNotifyObjects,
       "bigipNotifyObjMsg": bigipNotifyObjMsg,
       "bigipNotifyObjNode": bigipNotifyObjNode,
       "bigipNotifyObjPort": bigipNotifyObjPort,
       "bigipCompliance": bigipCompliance,
       "bigipCompliances": bigipCompliances,
       "bigipNotificationCompliance": bigipNotificationCompliance,
       "bigipGroups": bigipGroups,
       "bigipNotificationGroups": bigipNotificationGroups,
       "bigipNotifyObjectsGroup": bigipNotifyObjectsGroup,
       "bigipAgentNotifyGroup": bigipAgentNotifyGroup,
       "bigipSystemNotifyGroup": bigipSystemNotifyGroup}
)
