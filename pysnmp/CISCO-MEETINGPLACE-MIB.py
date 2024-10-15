# SNMP MIB module (CISCO-MEETINGPLACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MEETINGPLACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:23 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMeetingPlaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733)
)
ciscoMeetingPlaceMIB.setRevisions(
        ("2010-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoMeetingPlaceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMeetingPlaceMIBNotifs = _CiscoMeetingPlaceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0)
)
_CiscoMeetingPlaceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMeetingPlaceMIBObjects = _CiscoMeetingPlaceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1)
)
_CmpAlarmObjects_ObjectIdentity = ObjectIdentity
cmpAlarmObjects = _CmpAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1)
)
_CmpExceptionCode_Type = Unsigned32
_CmpExceptionCode_Object = MibScalar
cmpExceptionCode = _CmpExceptionCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 1),
    _CmpExceptionCode_Type()
)
cmpExceptionCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpExceptionCode.setStatus("current")
_CmpSysUnit_Type = Unsigned32
_CmpSysUnit_Object = MibScalar
cmpSysUnit = _CmpSysUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 2),
    _CmpSysUnit_Type()
)
cmpSysUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpSysUnit.setStatus("current")


class _CmpHwDev_Type(Integer32):
    """Custom type cmpHwDev based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("mpAnalogBlade", 13),
          ("mpDSPMSC", 10),
          ("mpDSPPRC", 11),
          ("mpDisketteDrive", 6),
          ("mpE1Blade", 17),
          ("mpE1Network", 18),
          ("mpEthernet", 7),
          ("mpHardDrive", 5),
          ("mpMainMemory", 16),
          ("mpModem", 8),
          ("mpPowerSupply", 2),
          ("mpSerialPort", 3),
          ("mpSystemIntegrityCard", 15),
          ("mpSystemMisc", 9),
          ("mpT1Blade", 12),
          ("mpT1Network", 14),
          ("mpTapeDrive", 4),
          ("mpTemperature", 1),
          ("mpVoIPBlade", 19))
    )


_CmpHwDev_Type.__name__ = "Integer32"
_CmpHwDev_Object = MibScalar
cmpHwDev = _CmpHwDev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 3),
    _CmpHwDev_Type()
)
cmpHwDev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpHwDev.setStatus("current")
_CmpHwUnit_Type = Unsigned32
_CmpHwUnit_Object = MibScalar
cmpHwUnit = _CmpHwUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 4),
    _CmpHwUnit_Type()
)
cmpHwUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpHwUnit.setStatus("current")
_CmpHwSlot_Type = Unsigned32
_CmpHwSlot_Object = MibScalar
cmpHwSlot = _CmpHwSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 5),
    _CmpHwSlot_Type()
)
cmpHwSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpHwSlot.setStatus("current")
_CmpHwPort_Type = Unsigned32
_CmpHwPort_Object = MibScalar
cmpHwPort = _CmpHwPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 6),
    _CmpHwPort_Type()
)
cmpHwPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpHwPort.setStatus("current")
_CmpAlarmDesc_Type = SnmpAdminString
_CmpAlarmDesc_Object = MibScalar
cmpAlarmDesc = _CmpAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 1, 7),
    _CmpAlarmDesc_Type()
)
cmpAlarmDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmpAlarmDesc.setStatus("current")
_CmpConferenceInfo_ObjectIdentity = ObjectIdentity
cmpConferenceInfo = _CmpConferenceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2)
)
_CmpPeakMeeting_Type = Unsigned32
_CmpPeakMeeting_Object = MibScalar
cmpPeakMeeting = _CmpPeakMeeting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 1),
    _CmpPeakMeeting_Type()
)
cmpPeakMeeting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpPeakMeeting.setStatus("current")
_CmpPeakHour_Type = Unsigned32
_CmpPeakHour_Object = MibScalar
cmpPeakHour = _CmpPeakHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 2),
    _CmpPeakHour_Type()
)
cmpPeakHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpPeakHour.setStatus("current")
_CmpMeetingCurrent_Type = Unsigned32
_CmpMeetingCurrent_Object = MibScalar
cmpMeetingCurrent = _CmpMeetingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 2, 3),
    _CmpMeetingCurrent_Type()
)
cmpMeetingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMeetingCurrent.setStatus("current")
_CmpLicenseInfo_ObjectIdentity = ObjectIdentity
cmpLicenseInfo = _CmpLicenseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3)
)
_CmpAudioLicense_Type = Unsigned32
_CmpAudioLicense_Object = MibScalar
cmpAudioLicense = _CmpAudioLicense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 1),
    _CmpAudioLicense_Type()
)
cmpAudioLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpAudioLicense.setStatus("current")
_CmpMaxAudioLicense_Type = Unsigned32
_CmpMaxAudioLicense_Object = MibScalar
cmpMaxAudioLicense = _CmpMaxAudioLicense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 2),
    _CmpMaxAudioLicense_Type()
)
cmpMaxAudioLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxAudioLicense.setStatus("current")
_CmpVideoLicense_Type = Unsigned32
_CmpVideoLicense_Object = MibScalar
cmpVideoLicense = _CmpVideoLicense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 3),
    _CmpVideoLicense_Type()
)
cmpVideoLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpVideoLicense.setStatus("current")
_CmpMaxVideoLicense_Type = Unsigned32
_CmpMaxVideoLicense_Object = MibScalar
cmpMaxVideoLicense = _CmpMaxVideoLicense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 3, 4),
    _CmpMaxVideoLicense_Type()
)
cmpMaxVideoLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxVideoLicense.setStatus("current")
_CmpUsageInfo_ObjectIdentity = ObjectIdentity
cmpUsageInfo = _CmpUsageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4)
)
_CmpVideoPortsUsage_Type = Unsigned32
_CmpVideoPortsUsage_Object = MibScalar
cmpVideoPortsUsage = _CmpVideoPortsUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 1),
    _CmpVideoPortsUsage_Type()
)
cmpVideoPortsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpVideoPortsUsage.setStatus("current")
_CmpMaxVideoPortsAvailable_Type = Unsigned32
_CmpMaxVideoPortsAvailable_Object = MibScalar
cmpMaxVideoPortsAvailable = _CmpMaxVideoPortsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 2),
    _CmpMaxVideoPortsAvailable_Type()
)
cmpMaxVideoPortsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxVideoPortsAvailable.setStatus("current")
_CmpAudioPortsUsage_Type = Unsigned32
_CmpAudioPortsUsage_Object = MibScalar
cmpAudioPortsUsage = _CmpAudioPortsUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 3),
    _CmpAudioPortsUsage_Type()
)
cmpAudioPortsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpAudioPortsUsage.setStatus("current")
_CmpMaxAudioPortsAvailable_Type = Unsigned32
_CmpMaxAudioPortsAvailable_Object = MibScalar
cmpMaxAudioPortsAvailable = _CmpMaxAudioPortsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 4),
    _CmpMaxAudioPortsAvailable_Type()
)
cmpMaxAudioPortsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxAudioPortsAvailable.setStatus("current")
_CmpMaxAudioPortsUsage24Hours_Type = Unsigned32
_CmpMaxAudioPortsUsage24Hours_Object = MibScalar
cmpMaxAudioPortsUsage24Hours = _CmpMaxAudioPortsUsage24Hours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 5),
    _CmpMaxAudioPortsUsage24Hours_Type()
)
cmpMaxAudioPortsUsage24Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxAudioPortsUsage24Hours.setStatus("current")
_CmpMaxVideoPortsUsage24Hours_Type = Unsigned32
_CmpMaxVideoPortsUsage24Hours_Object = MibScalar
cmpMaxVideoPortsUsage24Hours = _CmpMaxVideoPortsUsage24Hours_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 4, 6),
    _CmpMaxVideoPortsUsage24Hours_Type()
)
cmpMaxVideoPortsUsage24Hours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpMaxVideoPortsUsage24Hours.setStatus("current")
_CmpNodeInfo_ObjectIdentity = ObjectIdentity
cmpNodeInfo = _CmpNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5)
)
_CmpNodeDeployType_Type = OctetString
_CmpNodeDeployType_Object = MibScalar
cmpNodeDeployType = _CmpNodeDeployType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 1),
    _CmpNodeDeployType_Type()
)
cmpNodeDeployType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpNodeDeployType.setStatus("current")
_CmpNodeRole_Type = OctetString
_CmpNodeRole_Object = MibScalar
cmpNodeRole = _CmpNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 2),
    _CmpNodeRole_Type()
)
cmpNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpNodeRole.setStatus("current")
_CmpRegionInfo_Type = OctetString
_CmpRegionInfo_Object = MibScalar
cmpRegionInfo = _CmpRegionInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 3),
    _CmpRegionInfo_Type()
)
cmpRegionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpRegionInfo.setStatus("current")
_CmpSiteInfo_Type = OctetString
_CmpSiteInfo_Object = MibScalar
cmpSiteInfo = _CmpSiteInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 5, 4),
    _CmpSiteInfo_Type()
)
cmpSiteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpSiteInfo.setStatus("current")
_CmpNotificationStatus_Type = TruthValue
_CmpNotificationStatus_Object = MibScalar
cmpNotificationStatus = _CmpNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 1, 6),
    _CmpNotificationStatus_Type()
)
cmpNotificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmpNotificationStatus.setStatus("current")
_CiscoMeetingPlaceMIBConform_ObjectIdentity = ObjectIdentity
ciscoMeetingPlaceMIBConform = _CiscoMeetingPlaceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2)
)
_CmpMIBCompliances_ObjectIdentity = ObjectIdentity
cmpMIBCompliances = _CmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 1)
)
_CmpMIBGroups_ObjectIdentity = ObjectIdentity
cmpMIBGroups = _CmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2)
)

# Managed Objects groups

cmpAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 1)
)
cmpAlarmGroup.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"),
        ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"),
        ("CISCO-MEETINGPLACE-MIB", "cmpNotificationStatus"))
)
if mibBuilder.loadTexts:
    cmpAlarmGroup.setStatus("current")

cmpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 3)
)
cmpInfoGroup.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpPeakMeeting"),
        ("CISCO-MEETINGPLACE-MIB", "cmpPeakHour"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioPortsUsage24Hours"),
        ("CISCO-MEETINGPLACE-MIB", "cmpAudioLicense"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioLicense"),
        ("CISCO-MEETINGPLACE-MIB", "cmpVideoLicense"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoLicense"),
        ("CISCO-MEETINGPLACE-MIB", "cmpVideoPortsUsage"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoPortsAvailable"),
        ("CISCO-MEETINGPLACE-MIB", "cmpAudioPortsUsage"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxAudioPortsAvailable"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMeetingCurrent"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMaxVideoPortsUsage24Hours"),
        ("CISCO-MEETINGPLACE-MIB", "cmpNodeDeployType"),
        ("CISCO-MEETINGPLACE-MIB", "cmpNodeRole"),
        ("CISCO-MEETINGPLACE-MIB", "cmpRegionInfo"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSiteInfo"))
)
if mibBuilder.loadTexts:
    cmpInfoGroup.setStatus("current")


# Notification objects

cmpT1Down = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 1)
)
if mibBuilder.loadTexts:
    cmpT1Down.setStatus(
        "current"
    )

cmpGWSimAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 2)
)
if mibBuilder.loadTexts:
    cmpGWSimAlarm.setStatus(
        "current"
    )

cmpMajHwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 3)
)
cmpMajHwAlarm.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"))
)
if mibBuilder.loadTexts:
    cmpMajHwAlarm.setStatus(
        "current"
    )

cmpMinHwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 4)
)
cmpMinHwAlarm.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwDev"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwSlot"),
        ("CISCO-MEETINGPLACE-MIB", "cmpHwPort"))
)
if mibBuilder.loadTexts:
    cmpMinHwAlarm.setStatus(
        "current"
    )

cmpMajSwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 5)
)
cmpMajSwAlarm.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"))
)
if mibBuilder.loadTexts:
    cmpMajSwAlarm.setStatus(
        "current"
    )

cmpMinSwAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 0, 6)
)
cmpMinSwAlarm.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpExceptionCode"),
        ("CISCO-MEETINGPLACE-MIB", "cmpSysUnit"),
        ("CISCO-MEETINGPLACE-MIB", "cmpAlarmDesc"))
)
if mibBuilder.loadTexts:
    cmpMinSwAlarm.setStatus(
        "current"
    )


# Notifications groups

cmpNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 2, 2)
)
cmpNotifsGroup.setObjects(
      *(("CISCO-MEETINGPLACE-MIB", "cmpT1Down"),
        ("CISCO-MEETINGPLACE-MIB", "cmpGWSimAlarm"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMajHwAlarm"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMinHwAlarm"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMajSwAlarm"),
        ("CISCO-MEETINGPLACE-MIB", "cmpMinSwAlarm"))
)
if mibBuilder.loadTexts:
    cmpNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 733, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MEETINGPLACE-MIB",
    **{"ciscoMeetingPlaceMIB": ciscoMeetingPlaceMIB,
       "ciscoMeetingPlaceMIBNotifs": ciscoMeetingPlaceMIBNotifs,
       "cmpT1Down": cmpT1Down,
       "cmpGWSimAlarm": cmpGWSimAlarm,
       "cmpMajHwAlarm": cmpMajHwAlarm,
       "cmpMinHwAlarm": cmpMinHwAlarm,
       "cmpMajSwAlarm": cmpMajSwAlarm,
       "cmpMinSwAlarm": cmpMinSwAlarm,
       "ciscoMeetingPlaceMIBObjects": ciscoMeetingPlaceMIBObjects,
       "cmpAlarmObjects": cmpAlarmObjects,
       "cmpExceptionCode": cmpExceptionCode,
       "cmpSysUnit": cmpSysUnit,
       "cmpHwDev": cmpHwDev,
       "cmpHwUnit": cmpHwUnit,
       "cmpHwSlot": cmpHwSlot,
       "cmpHwPort": cmpHwPort,
       "cmpAlarmDesc": cmpAlarmDesc,
       "cmpConferenceInfo": cmpConferenceInfo,
       "cmpPeakMeeting": cmpPeakMeeting,
       "cmpPeakHour": cmpPeakHour,
       "cmpMeetingCurrent": cmpMeetingCurrent,
       "cmpLicenseInfo": cmpLicenseInfo,
       "cmpAudioLicense": cmpAudioLicense,
       "cmpMaxAudioLicense": cmpMaxAudioLicense,
       "cmpVideoLicense": cmpVideoLicense,
       "cmpMaxVideoLicense": cmpMaxVideoLicense,
       "cmpUsageInfo": cmpUsageInfo,
       "cmpVideoPortsUsage": cmpVideoPortsUsage,
       "cmpMaxVideoPortsAvailable": cmpMaxVideoPortsAvailable,
       "cmpAudioPortsUsage": cmpAudioPortsUsage,
       "cmpMaxAudioPortsAvailable": cmpMaxAudioPortsAvailable,
       "cmpMaxAudioPortsUsage24Hours": cmpMaxAudioPortsUsage24Hours,
       "cmpMaxVideoPortsUsage24Hours": cmpMaxVideoPortsUsage24Hours,
       "cmpNodeInfo": cmpNodeInfo,
       "cmpNodeDeployType": cmpNodeDeployType,
       "cmpNodeRole": cmpNodeRole,
       "cmpRegionInfo": cmpRegionInfo,
       "cmpSiteInfo": cmpSiteInfo,
       "cmpNotificationStatus": cmpNotificationStatus,
       "ciscoMeetingPlaceMIBConform": ciscoMeetingPlaceMIBConform,
       "cmpMIBCompliances": cmpMIBCompliances,
       "cmpMIBCompliance": cmpMIBCompliance,
       "cmpMIBGroups": cmpMIBGroups,
       "cmpAlarmGroup": cmpAlarmGroup,
       "cmpNotifsGroup": cmpNotifsGroup,
       "cmpInfoGroup": cmpInfoGroup}
)
