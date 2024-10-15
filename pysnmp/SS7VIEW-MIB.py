# SNMP MIB module (SS7VIEW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SS7VIEW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:41 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class AlarmRaiseType(Integer32):
    """Custom type AlarmRaiseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("raise", 1),
          ("state", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nortel_ObjectIdentity = ObjectIdentity
nortel = _Nortel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562)
)
_Dialaccess_ObjectIdentity = ObjectIdentity
dialaccess = _Dialaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14)
)
_Ss7view_ObjectIdentity = ObjectIdentity
ss7view = _Ss7view_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1)
)
_Ss7viewTrapVars_ObjectIdentity = ObjectIdentity
ss7viewTrapVars = _Ss7viewTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1)
)
_PartitionName_Type = DisplayString
_PartitionName_Object = MibScalar
partitionName = _PartitionName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 1),
    _PartitionName_Type()
)
partitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    partitionName.setStatus("mandatory")
_DiskCapacity_Type = DisplayString
_DiskCapacity_Object = MibScalar
diskCapacity = _DiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 2),
    _DiskCapacity_Type()
)
diskCapacity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskCapacity.setStatus("mandatory")
_DiskThreshold_Type = DisplayString
_DiskThreshold_Object = MibScalar
diskThreshold = _DiskThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 3),
    _DiskThreshold_Type()
)
diskThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskThreshold.setStatus("mandatory")
_TrapSource_Type = DisplayString
_TrapSource_Object = MibScalar
trapSource = _TrapSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 4),
    _TrapSource_Type()
)
trapSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSource.setStatus("mandatory")
_PollSS7ViewHost_Type = DisplayString
_PollSS7ViewHost_Object = MibScalar
pollSS7ViewHost = _PollSS7ViewHost_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 30),
    _PollSS7ViewHost_Type()
)
pollSS7ViewHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollSS7ViewHost.setStatus("mandatory")
_PollSS7ViewIP_Type = IpAddress
_PollSS7ViewIP_Object = MibScalar
pollSS7ViewIP = _PollSS7ViewIP_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 31),
    _PollSS7ViewIP_Type()
)
pollSS7ViewIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollSS7ViewIP.setStatus("mandatory")
_PollServerName_Type = DisplayString
_PollServerName_Object = MibScalar
pollServerName = _PollServerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 32),
    _PollServerName_Type()
)
pollServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollServerName.setStatus("mandatory")
_PollServerCLLI_Type = DisplayString
_PollServerCLLI_Object = MibScalar
pollServerCLLI = _PollServerCLLI_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 33),
    _PollServerCLLI_Type()
)
pollServerCLLI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollServerCLLI.setStatus("mandatory")
_PollServerIpAddress_Type = IpAddress
_PollServerIpAddress_Object = MibScalar
pollServerIpAddress = _PollServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 34),
    _PollServerIpAddress_Type()
)
pollServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollServerIpAddress.setStatus("mandatory")
_PollFailReason_Type = DisplayString
_PollFailReason_Object = MibScalar
pollFailReason = _PollFailReason_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 35),
    _PollFailReason_Type()
)
pollFailReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollFailReason.setStatus("mandatory")
_PollSeverity_Type = DisplayString
_PollSeverity_Object = MibScalar
pollSeverity = _PollSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 36),
    _PollSeverity_Type()
)
pollSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pollSeverity.setStatus("mandatory")
_StateChangeServerName_Type = DisplayString
_StateChangeServerName_Object = MibScalar
stateChangeServerName = _StateChangeServerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 50),
    _StateChangeServerName_Type()
)
stateChangeServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChangeServerName.setStatus("mandatory")
_StateChangeServerCLLI_Type = DisplayString
_StateChangeServerCLLI_Object = MibScalar
stateChangeServerCLLI = _StateChangeServerCLLI_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 51),
    _StateChangeServerCLLI_Type()
)
stateChangeServerCLLI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChangeServerCLLI.setStatus("mandatory")
_StateChangeServerOpState_Type = DisplayString
_StateChangeServerOpState_Object = MibScalar
stateChangeServerOpState = _StateChangeServerOpState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 52),
    _StateChangeServerOpState_Type()
)
stateChangeServerOpState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChangeServerOpState.setStatus("mandatory")
_StateChangeServerStandbyState_Type = DisplayString
_StateChangeServerStandbyState_Object = MibScalar
stateChangeServerStandbyState = _StateChangeServerStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 53),
    _StateChangeServerStandbyState_Type()
)
stateChangeServerStandbyState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChangeServerStandbyState.setStatus("mandatory")
_StateChangeServerAvailState_Type = DisplayString
_StateChangeServerAvailState_Object = MibScalar
stateChangeServerAvailState = _StateChangeServerAvailState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 54),
    _StateChangeServerAvailState_Type()
)
stateChangeServerAvailState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stateChangeServerAvailState.setStatus("mandatory")
_LogArchiveName_Type = DisplayString
_LogArchiveName_Object = MibScalar
logArchiveName = _LogArchiveName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 80),
    _LogArchiveName_Type()
)
logArchiveName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logArchiveName.setStatus("mandatory")
_Ss7viewTraps_ObjectIdentity = ObjectIdentity
ss7viewTraps = _Ss7viewTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 2)
)
_PrivateTrapVars_Type = ObjectIdentifier
_PrivateTrapVars_Object = MibScalar
privateTrapVars = _PrivateTrapVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 3),
    _PrivateTrapVars_Type()
)
privateTrapVars.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateTrapVars.setStatus("mandatory")
_AlarmRaise_Type = AlarmRaiseType
_AlarmRaise_Object = MibScalar
alarmRaise = _AlarmRaise_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 3, 1),
    _AlarmRaise_Type()
)
alarmRaise.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmRaise.setStatus("mandatory")
_IncSelectionName_Type = DisplayString
_IncSelectionName_Object = MibScalar
incSelectionName = _IncSelectionName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 3, 2),
    _IncSelectionName_Type()
)
incSelectionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incSelectionName.setStatus("mandatory")
_Ss7viewWebUITrapVars_ObjectIdentity = ObjectIdentity
ss7viewWebUITrapVars = _Ss7viewWebUITrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4)
)
_PrivateTraps_Type = ObjectIdentifier
_PrivateTraps_Object = MibScalar
privateTraps = _PrivateTraps_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4),
    _PrivateTraps_Type()
)
privateTraps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateTraps.setStatus("mandatory")
_Ss7viewINCTrapVars_ObjectIdentity = ObjectIdentity
ss7viewINCTrapVars = _Ss7viewINCTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5)
)
_IncComplexAlarmVars_Type = ObjectIdentifier
_IncComplexAlarmVars_Object = MibScalar
incComplexAlarmVars = _IncComplexAlarmVars_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1),
    _IncComplexAlarmVars_Type()
)
incComplexAlarmVars.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexAlarmVars.setStatus("mandatory")
_IncComplexName_Type = DisplayString
_IncComplexName_Object = MibScalar
incComplexName = _IncComplexName_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 1),
    _IncComplexName_Type()
)
incComplexName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexName.setStatus("mandatory")
_IncComplexIpAddress_Type = IpAddress
_IncComplexIpAddress_Object = MibScalar
incComplexIpAddress = _IncComplexIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 2),
    _IncComplexIpAddress_Type()
)
incComplexIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexIpAddress.setStatus("mandatory")
_IncComplexState_Type = DisplayString
_IncComplexState_Object = MibScalar
incComplexState = _IncComplexState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 3),
    _IncComplexState_Type()
)
incComplexState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexState.setStatus("mandatory")
_IncComplexOpState_Type = DisplayString
_IncComplexOpState_Object = MibScalar
incComplexOpState = _IncComplexOpState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 4),
    _IncComplexOpState_Type()
)
incComplexOpState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexOpState.setStatus("mandatory")
_IncComplexStandbyState_Type = DisplayString
_IncComplexStandbyState_Object = MibScalar
incComplexStandbyState = _IncComplexStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 5),
    _IncComplexStandbyState_Type()
)
incComplexStandbyState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexStandbyState.setStatus("mandatory")
_IncComplexAvailState_Type = DisplayString
_IncComplexAvailState_Object = MibScalar
incComplexAvailState = _IncComplexAvailState_Object(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 5, 1, 6),
    _IncComplexAvailState_Type()
)
incComplexAvailState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    incComplexAvailState.setStatus("mandatory")
_Ss7viewINCTraps_ObjectIdentity = ObjectIdentity
ss7viewINCTraps = _Ss7viewINCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6)
)

# Managed Objects groups


# Notification objects

csgStatusPollClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1031)
)
csgStatusPollClear.setObjects(
      *(("SS7VIEW-MIB", "pollSS7ViewHost"),
        ("SS7VIEW-MIB", "pollSS7ViewIP"),
        ("SS7VIEW-MIB", "pollServerName"),
        ("SS7VIEW-MIB", "pollServerCLLI"),
        ("SS7VIEW-MIB", "pollServerIpAddress"))
)
if mibBuilder.loadTexts:
    csgStatusPollClear.setStatus(
        ""
    )

csgStatusPollFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1033)
)
csgStatusPollFailed.setObjects(
      *(("SS7VIEW-MIB", "pollSS7ViewHost"),
        ("SS7VIEW-MIB", "pollSS7ViewIP"),
        ("SS7VIEW-MIB", "pollServerName"),
        ("SS7VIEW-MIB", "pollServerCLLI"),
        ("SS7VIEW-MIB", "pollServerIpAddress"),
        ("SS7VIEW-MIB", "pollFailReason"),
        ("SS7VIEW-MIB", "pollSeverity"))
)
if mibBuilder.loadTexts:
    csgStatusPollFailed.setStatus(
        ""
    )

csgStateChangeNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1051)
)
csgStateChangeNormal.setObjects(
      *(("SS7VIEW-MIB", "stateChangeServerName"),
        ("SS7VIEW-MIB", "stateChangeServerCLLI"),
        ("SS7VIEW-MIB", "stateChangeServerOpState"),
        ("SS7VIEW-MIB", "stateChangeServerStandbyState"),
        ("SS7VIEW-MIB", "stateChangeServerAvailState"))
)
if mibBuilder.loadTexts:
    csgStateChangeNormal.setStatus(
        ""
    )

csgStateChangeWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1052)
)
csgStateChangeWarning.setObjects(
      *(("SS7VIEW-MIB", "stateChangeServerName"),
        ("SS7VIEW-MIB", "stateChangeServerCLLI"),
        ("SS7VIEW-MIB", "stateChangeServerOpState"),
        ("SS7VIEW-MIB", "stateChangeServerStandbyState"),
        ("SS7VIEW-MIB", "stateChangeServerAvailState"))
)
if mibBuilder.loadTexts:
    csgStateChangeWarning.setStatus(
        ""
    )

csgStateChangeMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1053)
)
csgStateChangeMinor.setObjects(
      *(("SS7VIEW-MIB", "stateChangeServerName"),
        ("SS7VIEW-MIB", "stateChangeServerCLLI"),
        ("SS7VIEW-MIB", "stateChangeServerOpState"),
        ("SS7VIEW-MIB", "stateChangeServerStandbyState"),
        ("SS7VIEW-MIB", "stateChangeServerAvailState"))
)
if mibBuilder.loadTexts:
    csgStateChangeMinor.setStatus(
        ""
    )

csgStateChangeMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1054)
)
csgStateChangeMajor.setObjects(
      *(("SS7VIEW-MIB", "stateChangeServerName"),
        ("SS7VIEW-MIB", "stateChangeServerCLLI"),
        ("SS7VIEW-MIB", "stateChangeServerOpState"),
        ("SS7VIEW-MIB", "stateChangeServerStandbyState"),
        ("SS7VIEW-MIB", "stateChangeServerAvailState"))
)
if mibBuilder.loadTexts:
    csgStateChangeMajor.setStatus(
        ""
    )

csgStateChangeCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1055)
)
csgStateChangeCritical.setObjects(
      *(("SS7VIEW-MIB", "stateChangeServerName"),
        ("SS7VIEW-MIB", "stateChangeServerCLLI"),
        ("SS7VIEW-MIB", "stateChangeServerOpState"),
        ("SS7VIEW-MIB", "stateChangeServerStandbyState"),
        ("SS7VIEW-MIB", "stateChangeServerAvailState"))
)
if mibBuilder.loadTexts:
    csgStateChangeCritical.setStatus(
        ""
    )

ss7viewLogArchive = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 1, 0, 1081)
)
ss7viewLogArchive.setObjects(
      *(("SS7VIEW-MIB", "pollSS7ViewHost"),
        ("SS7VIEW-MIB", "pollSS7ViewIP"),
        ("SS7VIEW-MIB", "logArchiveName"))
)
if mibBuilder.loadTexts:
    ss7viewLogArchive.setStatus(
        ""
    )

ss7viewApplyConfigFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 2, 0, 1000)
)
ss7viewApplyConfigFile.setObjects(
    ("SS7VIEW-MIB", "trapSource")
)
if mibBuilder.loadTexts:
    ss7viewApplyConfigFile.setStatus(
        ""
    )

ss7viewRefreshReadOnlyMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 2, 0, 1001)
)
if mibBuilder.loadTexts:
    ss7viewRefreshReadOnlyMap.setStatus(
        ""
    )

ss7viewDiskFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 2, 0, 1002)
)
ss7viewDiskFullClear.setObjects(
      *(("SS7VIEW-MIB", "partitionName"),
        ("SS7VIEW-MIB", "diskCapacity"),
        ("SS7VIEW-MIB", "diskThreshold"))
)
if mibBuilder.loadTexts:
    ss7viewDiskFullClear.setStatus(
        ""
    )

ss7viewDiskFullRaise = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 2, 0, 2002)
)
ss7viewDiskFullRaise.setObjects(
      *(("SS7VIEW-MIB", "partitionName"),
        ("SS7VIEW-MIB", "diskCapacity"),
        ("SS7VIEW-MIB", "diskThreshold"))
)
if mibBuilder.loadTexts:
    ss7viewDiskFullRaise.setStatus(
        ""
    )

privateRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4, 0, 3000)
)
if mibBuilder.loadTexts:
    privateRestarted.setStatus(
        ""
    )

telnetServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4, 0, 4000)
)
if mibBuilder.loadTexts:
    telnetServerRestarted.setStatus(
        ""
    )

webServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4, 0, 4010)
)
if mibBuilder.loadTexts:
    webServerRestarted.setStatus(
        ""
    )

privateNotifyMap = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 4, 0, 58916871)
)
privateNotifyMap.setObjects(
      *(("SS7VIEW-MIB", "incSelectionName"),
        ("SS7VIEW-MIB", "alarmRaise"))
)
if mibBuilder.loadTexts:
    privateNotifyMap.setStatus(
        ""
    )

incCompStateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6, 0, 1001)
)
incCompStateNormal.setObjects(
      *(("SS7VIEW-MIB", "incComplexName"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"))
)
if mibBuilder.loadTexts:
    incCompStateNormal.setStatus(
        ""
    )

incCompStateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6, 0, 1002)
)
incCompStateWarning.setObjects(
      *(("SS7VIEW-MIB", "incComplexName"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"))
)
if mibBuilder.loadTexts:
    incCompStateWarning.setStatus(
        ""
    )

incCompStateMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6, 0, 1003)
)
incCompStateMinor.setObjects(
      *(("SS7VIEW-MIB", "incComplexName"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"))
)
if mibBuilder.loadTexts:
    incCompStateMinor.setStatus(
        ""
    )

incCompStateMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6, 0, 1004)
)
incCompStateMajor.setObjects(
      *(("SS7VIEW-MIB", "incComplexName"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"))
)
if mibBuilder.loadTexts:
    incCompStateMajor.setStatus(
        ""
    )

incCompStateCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 14, 1, 6, 0, 1005)
)
incCompStateCritical.setObjects(
      *(("SS7VIEW-MIB", "incComplexName"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"),
        ("SS7VIEW-MIB", "incComplexIpAddress"),
        ("SS7VIEW-MIB", "incComplexState"))
)
if mibBuilder.loadTexts:
    incCompStateCritical.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SS7VIEW-MIB",
    **{"AlarmRaiseType": AlarmRaiseType,
       "nortel": nortel,
       "dialaccess": dialaccess,
       "ss7view": ss7view,
       "ss7viewTrapVars": ss7viewTrapVars,
       "csgStatusPollClear": csgStatusPollClear,
       "csgStatusPollFailed": csgStatusPollFailed,
       "csgStateChangeNormal": csgStateChangeNormal,
       "csgStateChangeWarning": csgStateChangeWarning,
       "csgStateChangeMinor": csgStateChangeMinor,
       "csgStateChangeMajor": csgStateChangeMajor,
       "csgStateChangeCritical": csgStateChangeCritical,
       "ss7viewLogArchive": ss7viewLogArchive,
       "partitionName": partitionName,
       "diskCapacity": diskCapacity,
       "diskThreshold": diskThreshold,
       "trapSource": trapSource,
       "pollSS7ViewHost": pollSS7ViewHost,
       "pollSS7ViewIP": pollSS7ViewIP,
       "pollServerName": pollServerName,
       "pollServerCLLI": pollServerCLLI,
       "pollServerIpAddress": pollServerIpAddress,
       "pollFailReason": pollFailReason,
       "pollSeverity": pollSeverity,
       "stateChangeServerName": stateChangeServerName,
       "stateChangeServerCLLI": stateChangeServerCLLI,
       "stateChangeServerOpState": stateChangeServerOpState,
       "stateChangeServerStandbyState": stateChangeServerStandbyState,
       "stateChangeServerAvailState": stateChangeServerAvailState,
       "logArchiveName": logArchiveName,
       "ss7viewTraps": ss7viewTraps,
       "ss7viewApplyConfigFile": ss7viewApplyConfigFile,
       "ss7viewRefreshReadOnlyMap": ss7viewRefreshReadOnlyMap,
       "ss7viewDiskFullClear": ss7viewDiskFullClear,
       "ss7viewDiskFullRaise": ss7viewDiskFullRaise,
       "privateTrapVars": privateTrapVars,
       "alarmRaise": alarmRaise,
       "incSelectionName": incSelectionName,
       "ss7viewWebUITrapVars": ss7viewWebUITrapVars,
       "privateTraps": privateTraps,
       "privateRestarted": privateRestarted,
       "telnetServerRestarted": telnetServerRestarted,
       "webServerRestarted": webServerRestarted,
       "privateNotifyMap": privateNotifyMap,
       "ss7viewINCTrapVars": ss7viewINCTrapVars,
       "incComplexAlarmVars": incComplexAlarmVars,
       "incComplexName": incComplexName,
       "incComplexIpAddress": incComplexIpAddress,
       "incComplexState": incComplexState,
       "incComplexOpState": incComplexOpState,
       "incComplexStandbyState": incComplexStandbyState,
       "incComplexAvailState": incComplexAvailState,
       "ss7viewINCTraps": ss7viewINCTraps,
       "incCompStateNormal": incCompStateNormal,
       "incCompStateWarning": incCompStateWarning,
       "incCompStateMinor": incCompStateMinor,
       "incCompStateMajor": incCompStateMajor,
       "incCompStateCritical": incCompStateCritical}
)
