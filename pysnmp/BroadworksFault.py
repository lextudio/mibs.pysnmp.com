# SNMP MIB module (BroadworksFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BroadworksFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:59 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
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
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1)
)
_SystemFaults_ObjectIdentity = ObjectIdentity
systemFaults = _SystemFaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1)
)
_BroadsoftNotifications_ObjectIdentity = ObjectIdentity
broadsoftNotifications = _BroadsoftNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 0)
)
_FaultFields_ObjectIdentity = ObjectIdentity
faultFields = _FaultFields_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1)
)
_Identifier_Type = Counter32
_Identifier_Object = MibScalar
identifier = _Identifier_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 1),
    _Identifier_Type()
)
identifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    identifier.setStatus("current")
_TimeStamp_Type = DateAndTime
_TimeStamp_Object = MibScalar
timeStamp = _TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 2),
    _TimeStamp_Type()
)
timeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    timeStamp.setStatus("current")
_AlarmName_Type = DisplayString
_AlarmName_Object = MibScalar
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 3),
    _AlarmName_Type()
)
alarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")
_SystemName_Type = DisplayString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 4),
    _SystemName_Type()
)
systemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("high", 3),
          ("informational", 0),
          ("low", 1),
          ("medium", 2))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 5),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 6),
    _AlarmState_Type()
)
alarmState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")


class _Component_Type(Integer32):
    """Custom type component based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("applicationserver", 0),
          ("calldetailserver", 7),
          ("clientmanagementaccessserver", 9),
          ("clientmanagementprofileserver", 8),
          ("elementmanagementsystem", 5),
          ("mediaserver", 1),
          ("networkserver", 2),
          ("profileserver", 11),
          ("relayserver", 3),
          ("servicecontrolproxy", 4),
          ("webserver", 6),
          ("xtendedservicesplatform", 10))
    )


_Component_Type.__name__ = "Integer32"
_Component_Object = MibScalar
component = _Component_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 7),
    _Component_Type()
)
component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component.setStatus("current")


class _Subcomponent_Type(Integer32):
    """Custom type subcomponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 26),
          ("bcct", 41),
          ("callLogs", 39),
          ("callp", 15),
          ("cap", 36),
          ("ccp", 5),
          ("cms", 43),
          ("conferencing", 11),
          ("cpeDeviceManagement", 31),
          ("database", 3),
          ("diameterFrontNode", 51),
          ("diameterServer", 42),
          ("dns", 50),
          ("emergency", 19),
          ("externalAuthentication", 33),
          ("filesystem", 14),
          ("ims", 23),
          ("ivr", 13),
          ("ldap", 28),
          ("licensing", 27),
          ("liveAudio", 34),
          ("logging", 46),
          ("loggingserver", 21),
          ("mcp", 7),
          ("mgcp", 6),
          ("mm", 49),
          ("mss", 17),
          ("networkDeviceManagement", 32),
          ("nrs", 24),
          ("nslocation", 22),
          ("nssynch", 16),
          ("ociReporting", 40),
          ("openClientServer", 37),
          ("oss", 25),
          ("pmReporting", 29),
          ("pop3", 9),
          ("processmonitor", 1),
          ("rtcp", 10),
          ("rtp", 12),
          ("servicePackMigration", 35),
          ("sh", 52),
          ("sip", 4),
          ("smap", 20),
          ("smdi", 30),
          ("smpp", 48),
          ("smtp", 8),
          ("snmpAgent", 53),
          ("soap", 47),
          ("subscriberCache", 56),
          ("surveillance", 55),
          ("taskMonitor", 44),
          ("tcp", 45),
          ("transevent", 18),
          ("trunking", 57),
          ("unspecified", 0),
          ("voicePortal", 38),
          ("webserver", 2),
          ("xsp", 54))
    )


_Subcomponent_Type.__name__ = "Integer32"
_Subcomponent_Object = MibScalar
subcomponent = _Subcomponent_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 8),
    _Subcomponent_Type()
)
subcomponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subcomponent.setStatus("current")
_ProblemText_Type = DisplayString
_ProblemText_Object = MibScalar
problemText = _ProblemText_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 9),
    _ProblemText_Type()
)
problemText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    problemText.setStatus("current")
_RecommendedActionsText_Type = DisplayString
_RecommendedActionsText_Object = MibScalar
recommendedActionsText = _RecommendedActionsText_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1, 10),
    _RecommendedActionsText_Type()
)
recommendedActionsText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    recommendedActionsText.setStatus("current")

# Managed Objects groups


# Notification objects

notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2)
)
notification.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    notification.setStatus(
        "current"
    )

statefulAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3)
)
statefulAlarm.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    statefulAlarm.setStatus(
        "current"
    )

softwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 4)
)
softwareError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    softwareError.setStatus(
        "current"
    )

bwGeneralSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 5)
)
bwGeneralSoftwareError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwGeneralSoftwareError.setStatus(
        "current"
    )

bwPMtomcatLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 6)
)
bwPMtomcatLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMtomcatLaunched.setStatus(
        "current"
    )

bwPMtomcatShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 7)
)
bwPMtomcatShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMtomcatShutDown.setStatus(
        "current"
    )

bwPMtomcatRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 8)
)
bwPMtomcatRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMtomcatRestarted.setStatus(
        "current"
    )

bwPMtomcatDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 9)
)
bwPMtomcatDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMtomcatDeath.setStatus(
        "current"
    )

bwSystemHealthReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 10)
)
bwSystemHealthReport.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSystemHealthReport.setStatus(
        "current"
    )

bwDatabaseSyncReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 11)
)
bwDatabaseSyncReport.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwDatabaseSyncReport.setStatus(
        "current"
    )

bwServerStateTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 12)
)
bwServerStateTransition.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwServerStateTransition.setStatus(
        "current"
    )

bwCounterThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 13)
)
bwCounterThreshold.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCounterThreshold.setStatus(
        "current"
    )

bwGaugeLowLimitThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 14)
)
bwGaugeLowLimitThreshold.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwGaugeLowLimitThreshold.setStatus(
        "current"
    )

bwGaugeHighLimitThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 15)
)
bwGaugeHighLimitThreshold.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwGaugeHighLimitThreshold.setStatus(
        "current"
    )

bwPMReportingFTPConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 16)
)
bwPMReportingFTPConnectionError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMReportingFTPConnectionError.setStatus(
        "current"
    )

bwCPUIdleTimeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 17)
)
bwCPUIdleTimeLimitReached.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCPUIdleTimeLimitReached.setStatus(
        "current"
    )

bwMemoryLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 18)
)
bwMemoryLimitReached.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwMemoryLimitReached.setStatus(
        "current"
    )

bwNetworkDeviceIsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 19)
)
bwNetworkDeviceIsFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNetworkDeviceIsFailed.setStatus(
        "current"
    )

bwNetworkDeviceIsOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 20)
)
bwNetworkDeviceIsOnline.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNetworkDeviceIsOnline.setStatus(
        "current"
    )

bwPMremotexlaLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 21)
)
bwPMremotexlaLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMremotexlaLaunched.setStatus(
        "current"
    )

bwPMremotexlaShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 22)
)
bwPMremotexlaShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMremotexlaShutDown.setStatus(
        "current"
    )

bwPMremotexlaRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 23)
)
bwPMremotexlaRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMremotexlaRestarted.setStatus(
        "current"
    )

bwPMremotexlaDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 24)
)
bwPMremotexlaDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMremotexlaDeath.setStatus(
        "current"
    )

bwLicenseFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 25)
)
bwLicenseFileNotFound.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseFileNotFound.setStatus(
        "current"
    )

bwSMAPConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 26)
)
bwSMAPConnectionFailure.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSMAPConnectionFailure.setStatus(
        "current"
    )

bwMaximumFailedLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 27)
)
bwMaximumFailedLoginAttempts.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwMaximumFailedLoginAttempts.setStatus(
        "current"
    )

bwCommProtocolInitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 28)
)
bwCommProtocolInitError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCommProtocolInitError.setStatus(
        "current"
    )

bwCommProtocolHostNotAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 29)
)
bwCommProtocolHostNotAllowed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCommProtocolHostNotAllowed.setStatus(
        "current"
    )

bwCommProtocolInterfaceNotAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 30)
)
bwCommProtocolInterfaceNotAllowed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCommProtocolInterfaceNotAllowed.setStatus(
        "current"
    )

bwSipTcpExceededMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 31)
)
bwSipTcpExceededMax.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSipTcpExceededMax.setStatus(
        "current"
    )

bwSipTcpExceededMaxPerPeer = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 32)
)
bwSipTcpExceededMaxPerPeer.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSipTcpExceededMaxPerPeer.setStatus(
        "current"
    )

bwSipTcpSocketError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 33)
)
bwSipTcpSocketError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSipTcpSocketError.setStatus(
        "current"
    )

bwTaskMonitorWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 34)
)
bwTaskMonitorWarning.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwTaskMonitorWarning.setStatus(
        "current"
    )

bwTaskMonitorHungTask = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 35)
)
bwTaskMonitorHungTask.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwTaskMonitorHungTask.setStatus(
        "current"
    )

bwTcpSubsystemFatalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 36)
)
bwTcpSubsystemFatalError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwTcpSubsystemFatalError.setStatus(
        "current"
    )

bwFileServerClusterUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 37)
)
bwFileServerClusterUnreachable.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwFileServerClusterUnreachable.setStatus(
        "current"
    )

bwFileServerNodeUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 38)
)
bwFileServerNodeUnreachable.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwFileServerNodeUnreachable.setStatus(
        "current"
    )

bwFileServerClusterUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 39)
)
bwFileServerClusterUnreachableClear.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwFileServerClusterUnreachableClear.setStatus(
        "current"
    )

bwFileServerNodeUnreachableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 40)
)
bwFileServerNodeUnreachableClear.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwFileServerNodeUnreachableClear.setStatus(
        "current"
    )

bwAlarmsDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 41)
)
bwAlarmsDiscarded.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwAlarmsDiscarded.setStatus(
        "current"
    )

bwLogQueueSizeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 42)
)
bwLogQueueSizeLimitReached.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLogQueueSizeLimitReached.setStatus(
        "current"
    )

bwLogQueueSizeLimitReachedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 43)
)
bwLogQueueSizeLimitReachedClear.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLogQueueSizeLimitReachedClear.setStatus(
        "current"
    )

bwLicenseFileExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 44)
)
bwLicenseFileExpiring.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseFileExpiring.setStatus(
        "current"
    )

bwLicenseFileExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 45)
)
bwLicenseFileExpired.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseFileExpired.setStatus(
        "current"
    )

bwCongestionManagementNeighborsInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 46)
)
bwCongestionManagementNeighborsInhibited.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCongestionManagementNeighborsInhibited.setStatus(
        "current"
    )

bwPMhttpdLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 48)
)
bwPMhttpdLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMhttpdLaunched.setStatus(
        "current"
    )

bwPMhttpdShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 49)
)
bwPMhttpdShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMhttpdShutDown.setStatus(
        "current"
    )

bwPMhttpdRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 50)
)
bwPMhttpdRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMhttpdRestarted.setStatus(
        "current"
    )

bwPMhttpdDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 51)
)
bwPMhttpdDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMhttpdDeath.setStatus(
        "current"
    )

bwLicenseHWViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3543)
)
bwLicenseHWViolation.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseHWViolation.setStatus(
        "current"
    )

bwCallOverloadZoneTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3618)
)
bwCallOverloadZoneTransition.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCallOverloadZoneTransition.setStatus(
        "current"
    )

bwNonCallOverloadZoneTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3619)
)
bwNonCallOverloadZoneTransition.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNonCallOverloadZoneTransition.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BroadworksFault",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "common": common,
       "systemFaults": systemFaults,
       "broadsoftNotifications": broadsoftNotifications,
       "faultFields": faultFields,
       "identifier": identifier,
       "timeStamp": timeStamp,
       "alarmName": alarmName,
       "systemName": systemName,
       "severity": severity,
       "alarmState": alarmState,
       "component": component,
       "subcomponent": subcomponent,
       "problemText": problemText,
       "recommendedActionsText": recommendedActionsText,
       "notification": notification,
       "statefulAlarm": statefulAlarm,
       "softwareError": softwareError,
       "bwGeneralSoftwareError": bwGeneralSoftwareError,
       "bwPMtomcatLaunched": bwPMtomcatLaunched,
       "bwPMtomcatShutDown": bwPMtomcatShutDown,
       "bwPMtomcatRestarted": bwPMtomcatRestarted,
       "bwPMtomcatDeath": bwPMtomcatDeath,
       "bwSystemHealthReport": bwSystemHealthReport,
       "bwDatabaseSyncReport": bwDatabaseSyncReport,
       "bwServerStateTransition": bwServerStateTransition,
       "bwCounterThreshold": bwCounterThreshold,
       "bwGaugeLowLimitThreshold": bwGaugeLowLimitThreshold,
       "bwGaugeHighLimitThreshold": bwGaugeHighLimitThreshold,
       "bwPMReportingFTPConnectionError": bwPMReportingFTPConnectionError,
       "bwCPUIdleTimeLimitReached": bwCPUIdleTimeLimitReached,
       "bwMemoryLimitReached": bwMemoryLimitReached,
       "bwNetworkDeviceIsFailed": bwNetworkDeviceIsFailed,
       "bwNetworkDeviceIsOnline": bwNetworkDeviceIsOnline,
       "bwPMremotexlaLaunched": bwPMremotexlaLaunched,
       "bwPMremotexlaShutDown": bwPMremotexlaShutDown,
       "bwPMremotexlaRestarted": bwPMremotexlaRestarted,
       "bwPMremotexlaDeath": bwPMremotexlaDeath,
       "bwLicenseFileNotFound": bwLicenseFileNotFound,
       "bwSMAPConnectionFailure": bwSMAPConnectionFailure,
       "bwMaximumFailedLoginAttempts": bwMaximumFailedLoginAttempts,
       "bwCommProtocolInitError": bwCommProtocolInitError,
       "bwCommProtocolHostNotAllowed": bwCommProtocolHostNotAllowed,
       "bwCommProtocolInterfaceNotAllowed": bwCommProtocolInterfaceNotAllowed,
       "bwSipTcpExceededMax": bwSipTcpExceededMax,
       "bwSipTcpExceededMaxPerPeer": bwSipTcpExceededMaxPerPeer,
       "bwSipTcpSocketError": bwSipTcpSocketError,
       "bwTaskMonitorWarning": bwTaskMonitorWarning,
       "bwTaskMonitorHungTask": bwTaskMonitorHungTask,
       "bwTcpSubsystemFatalError": bwTcpSubsystemFatalError,
       "bwFileServerClusterUnreachable": bwFileServerClusterUnreachable,
       "bwFileServerNodeUnreachable": bwFileServerNodeUnreachable,
       "bwFileServerClusterUnreachableClear": bwFileServerClusterUnreachableClear,
       "bwFileServerNodeUnreachableClear": bwFileServerNodeUnreachableClear,
       "bwAlarmsDiscarded": bwAlarmsDiscarded,
       "bwLogQueueSizeLimitReached": bwLogQueueSizeLimitReached,
       "bwLogQueueSizeLimitReachedClear": bwLogQueueSizeLimitReachedClear,
       "bwLicenseFileExpiring": bwLicenseFileExpiring,
       "bwLicenseFileExpired": bwLicenseFileExpired,
       "bwCongestionManagementNeighborsInhibited": bwCongestionManagementNeighborsInhibited,
       "bwPMhttpdLaunched": bwPMhttpdLaunched,
       "bwPMhttpdShutDown": bwPMhttpdShutDown,
       "bwPMhttpdRestarted": bwPMhttpdRestarted,
       "bwPMhttpdDeath": bwPMhttpdDeath,
       "bwLicenseHWViolation": bwLicenseHWViolation,
       "bwCallOverloadZoneTransition": bwCallOverloadZoneTransition,
       "bwNonCallOverloadZoneTransition": bwNonCallOverloadZoneTransition}
)
