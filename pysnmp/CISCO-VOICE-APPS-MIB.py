# SNMP MIB module (CISCO-VOICE-APPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-APPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:16 2024
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

ciscoVoiceAppsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190)
)
ciscoVoiceAppsMIB.setRevisions(
        ("2005-12-22 00:00",
         "2001-02-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceAppsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBObjects = _CiscoVoiceAppsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1)
)
_CvaGeneralInfo_ObjectIdentity = ObjectIdentity
cvaGeneralInfo = _CvaGeneralInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1)
)
_CvaWorkflowInstallTable_Object = MibTable
cvaWorkflowInstallTable = _CvaWorkflowInstallTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvaWorkflowInstallTable.setStatus("current")
_CvaWorkflowInstallEntry_Object = MibTableRow
cvaWorkflowInstallEntry = _CvaWorkflowInstallEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1)
)
cvaWorkflowInstallEntry.setIndexNames(
    (0, "CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallIndex"),
)
if mibBuilder.loadTexts:
    cvaWorkflowInstallEntry.setStatus("current")
_CvaWorkflowInstallIndex_Type = Unsigned32
_CvaWorkflowInstallIndex_Object = MibTableColumn
cvaWorkflowInstallIndex = _CvaWorkflowInstallIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 1),
    _CvaWorkflowInstallIndex_Type()
)
cvaWorkflowInstallIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvaWorkflowInstallIndex.setStatus("current")


class _CvaWorkflowInstallName_Type(SnmpAdminString):
    """Custom type cvaWorkflowInstallName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvaWorkflowInstallName_Type.__name__ = "SnmpAdminString"
_CvaWorkflowInstallName_Object = MibTableColumn
cvaWorkflowInstallName = _CvaWorkflowInstallName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 2),
    _CvaWorkflowInstallName_Type()
)
cvaWorkflowInstallName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaWorkflowInstallName.setStatus("current")


class _CvaWorkflowInstallLocator_Type(OctetString):
    """Custom type cvaWorkflowInstallLocator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvaWorkflowInstallLocator_Type.__name__ = "OctetString"
_CvaWorkflowInstallLocator_Object = MibTableColumn
cvaWorkflowInstallLocator = _CvaWorkflowInstallLocator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 3),
    _CvaWorkflowInstallLocator_Type()
)
cvaWorkflowInstallLocator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaWorkflowInstallLocator.setStatus("current")


class _CvaWorkflowInstallScriptName_Type(SnmpAdminString):
    """Custom type cvaWorkflowInstallScriptName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvaWorkflowInstallScriptName_Type.__name__ = "SnmpAdminString"
_CvaWorkflowInstallScriptName_Object = MibTableColumn
cvaWorkflowInstallScriptName = _CvaWorkflowInstallScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 4),
    _CvaWorkflowInstallScriptName_Type()
)
cvaWorkflowInstallScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaWorkflowInstallScriptName.setStatus("current")
_CvaWorkflowInstallEnable_Type = TruthValue
_CvaWorkflowInstallEnable_Object = MibTableColumn
cvaWorkflowInstallEnable = _CvaWorkflowInstallEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 1, 1, 5),
    _CvaWorkflowInstallEnable_Type()
)
cvaWorkflowInstallEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvaWorkflowInstallEnable.setStatus("current")
_CvaNotificationEnable_Type = TruthValue
_CvaNotificationEnable_Object = MibScalar
cvaNotificationEnable = _CvaNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 1, 3),
    _CvaNotificationEnable_Type()
)
cvaNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvaNotificationEnable.setStatus("current")
_CvaModuleFailureInfo_ObjectIdentity = ObjectIdentity
cvaModuleFailureInfo = _CvaModuleFailureInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2)
)


class _CvaAlarmSeverity_Type(Integer32):
    """Custom type cvaAlarmSeverity based on Integer32"""
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
        *(("alert", 2),
          ("critical", 3),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )


_CvaAlarmSeverity_Type.__name__ = "Integer32"
_CvaAlarmSeverity_Object = MibScalar
cvaAlarmSeverity = _CvaAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 1),
    _CvaAlarmSeverity_Type()
)
cvaAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaAlarmSeverity.setStatus("current")


class _CvaModuleName_Type(DisplayString):
    """Custom type cvaModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvaModuleName_Type.__name__ = "DisplayString"
_CvaModuleName_Object = MibScalar
cvaModuleName = _CvaModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 2),
    _CvaModuleName_Type()
)
cvaModuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaModuleName.setStatus("current")
_CvaProcessId_Type = Unsigned32
_CvaProcessId_Object = MibScalar
cvaProcessId = _CvaProcessId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 3),
    _CvaProcessId_Type()
)
cvaProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaProcessId.setStatus("current")


class _CvaModuleFailureName_Type(DisplayString):
    """Custom type cvaModuleFailureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvaModuleFailureName_Type.__name__ = "DisplayString"
_CvaModuleFailureName_Object = MibScalar
cvaModuleFailureName = _CvaModuleFailureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 4),
    _CvaModuleFailureName_Type()
)
cvaModuleFailureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaModuleFailureName.setStatus("current")


class _CvaModuleFailureCause_Type(Integer32):
    """Custom type cvaModuleFailureCause based on Integer32"""
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
        *(("gracefulShutDown", 2),
          ("heartBeatFailure", 3),
          ("initFailure", 4),
          ("other", 1),
          ("outOfResource", 5),
          ("partialFailure", 6))
    )


_CvaModuleFailureCause_Type.__name__ = "Integer32"
_CvaModuleFailureCause_Object = MibScalar
cvaModuleFailureCause = _CvaModuleFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 5),
    _CvaModuleFailureCause_Type()
)
cvaModuleFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaModuleFailureCause.setStatus("current")


class _CvaModuleFailureMessage_Type(DisplayString):
    """Custom type cvaModuleFailureMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CvaModuleFailureMessage_Type.__name__ = "DisplayString"
_CvaModuleFailureMessage_Object = MibScalar
cvaModuleFailureMessage = _CvaModuleFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 6),
    _CvaModuleFailureMessage_Type()
)
cvaModuleFailureMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaModuleFailureMessage.setStatus("current")


class _CvaModuleRunTimeFailureCause_Type(Integer32):
    """Custom type cvaModuleRunTimeFailureCause based on Integer32"""
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
        *(("callProcessFailure", 10),
          ("connectionFailure", 13),
          ("createFailure", 4),
          ("deRegistrationFailure", 12),
          ("deleteFailure", 5),
          ("disconnectionFailure", 14),
          ("initFailure", 7),
          ("loadFailure", 8),
          ("other", 1),
          ("outOfResource", 9),
          ("readAccessFailure", 2),
          ("registrationFailure", 11),
          ("unReacheableTarget", 16),
          ("unknownTarget", 15),
          ("updateFailure", 6),
          ("writeAccessFailure", 3))
    )


_CvaModuleRunTimeFailureCause_Type.__name__ = "Integer32"
_CvaModuleRunTimeFailureCause_Object = MibScalar
cvaModuleRunTimeFailureCause = _CvaModuleRunTimeFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 1, 2, 7),
    _CvaModuleRunTimeFailureCause_Type()
)
cvaModuleRunTimeFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cvaModuleRunTimeFailureCause.setStatus("current")
_CiscoVoiceAppsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBNotificationPrefix = _CiscoVoiceAppsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2)
)
_CiscoVoiceAppsMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBNotifications = _CiscoVoiceAppsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0)
)
_CiscoVoiceAppsMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBConformance = _CiscoVoiceAppsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3)
)
_CiscoVoiceAppsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBCompliances = _CiscoVoiceAppsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1)
)
_CiscoVoiceAppsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVoiceAppsMIBGroups = _CiscoVoiceAppsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2)
)

# Managed Objects groups

cvaModuleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 1)
)
cvaModuleInfoGroup.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallName"),
        ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallLocator"),
        ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallScriptName"),
        ("CISCO-VOICE-APPS-MIB", "cvaWorkflowInstallEnable"),
        ("CISCO-VOICE-APPS-MIB", "cvaNotificationEnable"))
)
if mibBuilder.loadTexts:
    cvaModuleInfoGroup.setStatus("current")

cvaNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 2)
)
cvaNotificationInfoGroup.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"),
        ("CISCO-VOICE-APPS-MIB", "cvaProcessId"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"))
)
if mibBuilder.loadTexts:
    cvaNotificationInfoGroup.setStatus("current")


# Notification objects

cvaModuleStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 1)
)
cvaModuleStart.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"))
)
if mibBuilder.loadTexts:
    cvaModuleStart.setStatus(
        "current"
    )

cvaModuleStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 2)
)
cvaModuleStop.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureCause"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
)
if mibBuilder.loadTexts:
    cvaModuleStop.setStatus(
        "current"
    )

cvaModuleRunTimeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 3)
)
cvaModuleRunTimeFailure.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailureCause"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureName"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleFailureMessage"))
)
if mibBuilder.loadTexts:
    cvaModuleRunTimeFailure.setStatus(
        "current"
    )

cvaProcessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 4)
)
cvaProcessStart.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"),
        ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
)
if mibBuilder.loadTexts:
    cvaProcessStart.setStatus(
        "current"
    )

cvaProcessStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 2, 0, 5)
)
cvaProcessStop.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaAlarmSeverity"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleName"),
        ("CISCO-VOICE-APPS-MIB", "cvaProcessId"))
)
if mibBuilder.loadTexts:
    cvaProcessStop.setStatus(
        "current"
    )


# Notifications groups

cvaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 2, 3)
)
cvaNotificationGroup.setObjects(
      *(("CISCO-VOICE-APPS-MIB", "cvaModuleStart"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleStop"),
        ("CISCO-VOICE-APPS-MIB", "cvaModuleRunTimeFailure"),
        ("CISCO-VOICE-APPS-MIB", "cvaProcessStart"),
        ("CISCO-VOICE-APPS-MIB", "cvaProcessStop"))
)
if mibBuilder.loadTexts:
    cvaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoVoiceAppsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 190, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVoiceAppsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-APPS-MIB",
    **{"ciscoVoiceAppsMIB": ciscoVoiceAppsMIB,
       "ciscoVoiceAppsMIBObjects": ciscoVoiceAppsMIBObjects,
       "cvaGeneralInfo": cvaGeneralInfo,
       "cvaWorkflowInstallTable": cvaWorkflowInstallTable,
       "cvaWorkflowInstallEntry": cvaWorkflowInstallEntry,
       "cvaWorkflowInstallIndex": cvaWorkflowInstallIndex,
       "cvaWorkflowInstallName": cvaWorkflowInstallName,
       "cvaWorkflowInstallLocator": cvaWorkflowInstallLocator,
       "cvaWorkflowInstallScriptName": cvaWorkflowInstallScriptName,
       "cvaWorkflowInstallEnable": cvaWorkflowInstallEnable,
       "cvaNotificationEnable": cvaNotificationEnable,
       "cvaModuleFailureInfo": cvaModuleFailureInfo,
       "cvaAlarmSeverity": cvaAlarmSeverity,
       "cvaModuleName": cvaModuleName,
       "cvaProcessId": cvaProcessId,
       "cvaModuleFailureName": cvaModuleFailureName,
       "cvaModuleFailureCause": cvaModuleFailureCause,
       "cvaModuleFailureMessage": cvaModuleFailureMessage,
       "cvaModuleRunTimeFailureCause": cvaModuleRunTimeFailureCause,
       "ciscoVoiceAppsMIBNotificationPrefix": ciscoVoiceAppsMIBNotificationPrefix,
       "ciscoVoiceAppsMIBNotifications": ciscoVoiceAppsMIBNotifications,
       "cvaModuleStart": cvaModuleStart,
       "cvaModuleStop": cvaModuleStop,
       "cvaModuleRunTimeFailure": cvaModuleRunTimeFailure,
       "cvaProcessStart": cvaProcessStart,
       "cvaProcessStop": cvaProcessStop,
       "ciscoVoiceAppsMIBConformance": ciscoVoiceAppsMIBConformance,
       "ciscoVoiceAppsMIBCompliances": ciscoVoiceAppsMIBCompliances,
       "ciscoVoiceAppsMIBCompliance": ciscoVoiceAppsMIBCompliance,
       "ciscoVoiceAppsMIBGroups": ciscoVoiceAppsMIBGroups,
       "cvaModuleInfoGroup": cvaModuleInfoGroup,
       "cvaNotificationInfoGroup": cvaNotificationInfoGroup,
       "cvaNotificationGroup": cvaNotificationGroup}
)
