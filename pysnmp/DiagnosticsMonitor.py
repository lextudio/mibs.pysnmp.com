# SNMP MIB module (DiagnosticsMonitor) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DiagnosticsMonitor
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:47 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Concord_ObjectIdentity = ObjectIdentity
concord = _Concord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149)
)
_NetHealth_ObjectIdentity = ObjectIdentity
netHealth = _NetHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2)
)
_NetHealthMib_ObjectIdentity = ObjectIdentity
netHealthMib = _NetHealthMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 1)
)
_NhdTraps_ObjectIdentity = ObjectIdentity
nhdTraps = _NhdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1)
)
_NhdServer_ObjectIdentity = ObjectIdentity
nhdServer = _NhdServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 1)
)
_NhdServerIp_Type = IpAddress
_NhdServerIp_Object = MibScalar
nhdServerIp = _NhdServerIp_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 1, 1),
    _NhdServerIp_Type()
)
nhdServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdServerIp.setStatus("mandatory")
_NhdServerName_Type = OctetString
_NhdServerName_Object = MibScalar
nhdServerName = _NhdServerName_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 1, 2),
    _NhdServerName_Type()
)
nhdServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdServerName.setStatus("mandatory")
_NhdError_ObjectIdentity = ObjectIdentity
nhdError = _NhdError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 2)
)
_NhdErrorDate_Type = OctetString
_NhdErrorDate_Object = MibScalar
nhdErrorDate = _NhdErrorDate_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 2, 1),
    _NhdErrorDate_Type()
)
nhdErrorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdErrorDate.setStatus("mandatory")
_NhdErrorTime_Type = OctetString
_NhdErrorTime_Object = MibScalar
nhdErrorTime = _NhdErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 2, 2),
    _NhdErrorTime_Type()
)
nhdErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdErrorTime.setStatus("mandatory")
_NhdErrorCode_Type = OctetString
_NhdErrorCode_Object = MibScalar
nhdErrorCode = _NhdErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 2, 3),
    _NhdErrorCode_Type()
)
nhdErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdErrorCode.setStatus("mandatory")
_NhdErrorMessage_Type = OctetString
_NhdErrorMessage_Object = MibScalar
nhdErrorMessage = _NhdErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 1, 1, 2, 5),
    _NhdErrorMessage_Type()
)
nhdErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhdErrorMessage.setStatus("mandatory")
_NhSysInfo_ObjectIdentity = ObjectIdentity
nhSysInfo = _NhSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 2)
)
_NhServerIp_Type = IpAddress
_NhServerIp_Object = MibScalar
nhServerIp = _NhServerIp_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 2, 1),
    _NhServerIp_Type()
)
nhServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhServerIp.setStatus("mandatory")
_NhServerName_Type = DisplayString
_NhServerName_Object = MibScalar
nhServerName = _NhServerName_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 2, 2),
    _NhServerName_Type()
)
nhServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhServerName.setStatus("mandatory")
_NhServerPort_Type = Integer32
_NhServerPort_Object = MibScalar
nhServerPort = _NhServerPort_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 2, 3),
    _NhServerPort_Type()
)
nhServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhServerPort.setStatus("mandatory")
_NhArgs_ObjectIdentity = ObjectIdentity
nhArgs = _NhArgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 149, 2, 3)
)
_NhElementIp_Type = IpAddress
_NhElementIp_Object = MibScalar
nhElementIp = _NhElementIp_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 1),
    _NhElementIp_Type()
)
nhElementIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhElementIp.setStatus("mandatory")
_NhElementName_Type = DisplayString
_NhElementName_Object = MibScalar
nhElementName = _NhElementName_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 2),
    _NhElementName_Type()
)
nhElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhElementName.setStatus("mandatory")
_NhElementId_Type = Integer32
_NhElementId_Object = MibScalar
nhElementId = _NhElementId_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 3),
    _NhElementId_Type()
)
nhElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhElementId.setStatus("mandatory")
_NhStartTime_Type = Integer32
_NhStartTime_Object = MibScalar
nhStartTime = _NhStartTime_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 4),
    _NhStartTime_Type()
)
nhStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhStartTime.setStatus("mandatory")
_NhExceptionType_Type = DisplayString
_NhExceptionType_Object = MibScalar
nhExceptionType = _NhExceptionType_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 5),
    _NhExceptionType_Type()
)
nhExceptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhExceptionType.setStatus("mandatory")
_NhVariable_Type = DisplayString
_NhVariable_Object = MibScalar
nhVariable = _NhVariable_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 6),
    _NhVariable_Type()
)
nhVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhVariable.setStatus("mandatory")


class _NhSeverity_Type(Integer32):
    """Custom type nhSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("major", 4),
          ("minor", 3),
          ("normal", 1),
          ("warning", 2))
    )


_NhSeverity_Type.__name__ = "Integer32"
_NhSeverity_Object = MibScalar
nhSeverity = _NhSeverity_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 7),
    _NhSeverity_Type()
)
nhSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhSeverity.setStatus("mandatory")
_NhGroup_Type = DisplayString
_NhGroup_Object = MibScalar
nhGroup = _NhGroup_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 8),
    _NhGroup_Type()
)
nhGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhGroup.setStatus("mandatory")
_NhGroupList_Type = DisplayString
_NhGroupList_Object = MibScalar
nhGroupList = _NhGroupList_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 9),
    _NhGroupList_Type()
)
nhGroupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhGroupList.setStatus("mandatory")
_NhDisplayStr_Type = DisplayString
_NhDisplayStr_Object = MibScalar
nhDisplayStr = _NhDisplayStr_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 10),
    _NhDisplayStr_Type()
)
nhDisplayStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhDisplayStr.setStatus("mandatory")
_NhExceptionId_Type = Integer32
_NhExceptionId_Object = MibScalar
nhExceptionId = _NhExceptionId_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 11),
    _NhExceptionId_Type()
)
nhExceptionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhExceptionId.setStatus("mandatory")
_NhTechType_Type = DisplayString
_NhTechType_Object = MibScalar
nhTechType = _NhTechType_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 12),
    _NhTechType_Type()
)
nhTechType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhTechType.setStatus("mandatory")
_NhResetTime_Type = Integer32
_NhResetTime_Object = MibScalar
nhResetTime = _NhResetTime_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 13),
    _NhResetTime_Type()
)
nhResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhResetTime.setStatus("mandatory")
_NhProfile_Type = DisplayString
_NhProfile_Object = MibScalar
nhProfile = _NhProfile_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 14),
    _NhProfile_Type()
)
nhProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhProfile.setStatus("mandatory")
_NhProblemStartTime_Type = Integer32
_NhProblemStartTime_Object = MibScalar
nhProblemStartTime = _NhProblemStartTime_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 15),
    _NhProblemStartTime_Type()
)
nhProblemStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhProblemStartTime.setStatus("mandatory")
_NhProblemDuration_Type = Integer32
_NhProblemDuration_Object = MibScalar
nhProblemDuration = _NhProblemDuration_Object(
    (1, 3, 6, 1, 4, 1, 149, 2, 3, 16),
    _NhProblemDuration_Type()
)
nhProblemDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nhProblemDuration.setStatus("mandatory")

# Managed Objects groups


# Notification objects

netHealthInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 15)
)
netHealthInfo.setObjects(
      *(("DiagnosticsMonitor", "nhdErrorDate"),
        ("DiagnosticsMonitor", "nhdErrorTime"),
        ("DiagnosticsMonitor", "nhdErrorCode"),
        ("DiagnosticsMonitor", "nhdErrorMessage"),
        ("DiagnosticsMonitor", "nhdServerIp"),
        ("DiagnosticsMonitor", "nhdServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementId"))
)
if mibBuilder.loadTexts:
    netHealthInfo.setStatus(
        ""
    )

netHealthWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 16)
)
netHealthWarning.setObjects(
      *(("DiagnosticsMonitor", "nhdErrorDate"),
        ("DiagnosticsMonitor", "nhdErrorTime"),
        ("DiagnosticsMonitor", "nhdErrorCode"),
        ("DiagnosticsMonitor", "nhdErrorMessage"),
        ("DiagnosticsMonitor", "nhdServerIp"),
        ("DiagnosticsMonitor", "nhdServerName"))
)
if mibBuilder.loadTexts:
    netHealthWarning.setStatus(
        ""
    )

netHealthReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 17)
)
netHealthReset.setObjects(
      *(("DiagnosticsMonitor", "nhdErrorDate"),
        ("DiagnosticsMonitor", "nhdErrorTime"),
        ("DiagnosticsMonitor", "nhdErrorCode"),
        ("DiagnosticsMonitor", "nhdErrorMessage"),
        ("DiagnosticsMonitor", "nhdServerIp"),
        ("DiagnosticsMonitor", "nhdServerName"))
)
if mibBuilder.loadTexts:
    netHealthReset.setStatus(
        ""
    )

netHealthUrgent = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 18)
)
netHealthUrgent.setObjects(
      *(("DiagnosticsMonitor", "nhdErrorDate"),
        ("DiagnosticsMonitor", "nhdErrorTime"),
        ("DiagnosticsMonitor", "nhdErrorCode"),
        ("DiagnosticsMonitor", "nhdErrorMessage"),
        ("DiagnosticsMonitor", "nhdServerIp"),
        ("DiagnosticsMonitor", "nhdServerName"))
)
if mibBuilder.loadTexts:
    netHealthUrgent.setStatus(
        ""
    )

netHealthException = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 19)
)
netHealthException.setObjects(
      *(("DiagnosticsMonitor", "nhdErrorDate"),
        ("DiagnosticsMonitor", "nhdErrorTime"),
        ("DiagnosticsMonitor", "nhdErrorCode"),
        ("DiagnosticsMonitor", "nhdErrorMessage"),
        ("DiagnosticsMonitor", "nhdServerIp"),
        ("DiagnosticsMonitor", "nhdServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhServerIp"))
)
if mibBuilder.loadTexts:
    netHealthException.setStatus(
        ""
    )

nhLiveException = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 20)
)
nhLiveException.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementIp"),
        ("DiagnosticsMonitor", "nhElementName"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhStartTime"),
        ("DiagnosticsMonitor", "nhDisplayStr"),
        ("DiagnosticsMonitor", "nhGroup"),
        ("DiagnosticsMonitor", "nhGroupList"),
        ("DiagnosticsMonitor", "nhSeverity"),
        ("DiagnosticsMonitor", "nhProfile"),
        ("DiagnosticsMonitor", "nhExceptionId"),
        ("DiagnosticsMonitor", "nhTechType"))
)
if mibBuilder.loadTexts:
    nhLiveException.setStatus(
        ""
    )

nhLiveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 21)
)
nhLiveAlarm.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementIp"),
        ("DiagnosticsMonitor", "nhElementName"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhStartTime"),
        ("DiagnosticsMonitor", "nhDisplayStr"),
        ("DiagnosticsMonitor", "nhGroup"),
        ("DiagnosticsMonitor", "nhGroupList"),
        ("DiagnosticsMonitor", "nhExceptionType"),
        ("DiagnosticsMonitor", "nhVariable"),
        ("DiagnosticsMonitor", "nhSeverity"),
        ("DiagnosticsMonitor", "nhProfile"),
        ("DiagnosticsMonitor", "nhExceptionId"),
        ("DiagnosticsMonitor", "nhTechType"))
)
if mibBuilder.loadTexts:
    nhLiveAlarm.setStatus(
        ""
    )

nhLiveClearException = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 22)
)
nhLiveClearException.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementIp"),
        ("DiagnosticsMonitor", "nhElementName"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhStartTime"),
        ("DiagnosticsMonitor", "nhDisplayStr"),
        ("DiagnosticsMonitor", "nhGroup"),
        ("DiagnosticsMonitor", "nhGroupList"),
        ("DiagnosticsMonitor", "nhSeverity"),
        ("DiagnosticsMonitor", "nhProfile"),
        ("DiagnosticsMonitor", "nhExceptionId"),
        ("DiagnosticsMonitor", "nhTechType"),
        ("DiagnosticsMonitor", "nhProblemStartTime"),
        ("DiagnosticsMonitor", "nhProblemDuration"))
)
if mibBuilder.loadTexts:
    nhLiveClearException.setStatus(
        ""
    )

nhLiveClearAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 23)
)
nhLiveClearAlarm.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementIp"),
        ("DiagnosticsMonitor", "nhElementName"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhStartTime"),
        ("DiagnosticsMonitor", "nhDisplayStr"),
        ("DiagnosticsMonitor", "nhGroup"),
        ("DiagnosticsMonitor", "nhGroupList"),
        ("DiagnosticsMonitor", "nhExceptionType"),
        ("DiagnosticsMonitor", "nhVariable"),
        ("DiagnosticsMonitor", "nhSeverity"),
        ("DiagnosticsMonitor", "nhProfile"),
        ("DiagnosticsMonitor", "nhExceptionId"),
        ("DiagnosticsMonitor", "nhTechType"),
        ("DiagnosticsMonitor", "nhProblemStartTime"),
        ("DiagnosticsMonitor", "nhProblemDuration"))
)
if mibBuilder.loadTexts:
    nhLiveClearAlarm.setStatus(
        ""
    )

nhLiveUpdateException = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 24)
)
nhLiveUpdateException.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhElementIp"),
        ("DiagnosticsMonitor", "nhElementName"),
        ("DiagnosticsMonitor", "nhElementId"),
        ("DiagnosticsMonitor", "nhStartTime"),
        ("DiagnosticsMonitor", "nhDisplayStr"),
        ("DiagnosticsMonitor", "nhGroup"),
        ("DiagnosticsMonitor", "nhGroupList"),
        ("DiagnosticsMonitor", "nhSeverity"),
        ("DiagnosticsMonitor", "nhProfile"),
        ("DiagnosticsMonitor", "nhExceptionId"),
        ("DiagnosticsMonitor", "nhTechType"))
)
if mibBuilder.loadTexts:
    nhLiveUpdateException.setStatus(
        ""
    )

nhLiveResetExceptions = NotificationType(
    (1, 3, 6, 1, 4, 1, 149, 0, 25)
)
nhLiveResetExceptions.setObjects(
      *(("DiagnosticsMonitor", "nhServerIp"),
        ("DiagnosticsMonitor", "nhServerName"),
        ("DiagnosticsMonitor", "nhServerPort"),
        ("DiagnosticsMonitor", "nhResetTime"))
)
if mibBuilder.loadTexts:
    nhLiveResetExceptions.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DiagnosticsMonitor",
    **{"concord": concord,
       "netHealthInfo": netHealthInfo,
       "netHealthWarning": netHealthWarning,
       "netHealthReset": netHealthReset,
       "netHealthUrgent": netHealthUrgent,
       "netHealthException": netHealthException,
       "nhLiveException": nhLiveException,
       "nhLiveAlarm": nhLiveAlarm,
       "nhLiveClearException": nhLiveClearException,
       "nhLiveClearAlarm": nhLiveClearAlarm,
       "nhLiveUpdateException": nhLiveUpdateException,
       "nhLiveResetExceptions": nhLiveResetExceptions,
       "netHealth": netHealth,
       "netHealthMib": netHealthMib,
       "nhdTraps": nhdTraps,
       "nhdServer": nhdServer,
       "nhdServerIp": nhdServerIp,
       "nhdServerName": nhdServerName,
       "nhdError": nhdError,
       "nhdErrorDate": nhdErrorDate,
       "nhdErrorTime": nhdErrorTime,
       "nhdErrorCode": nhdErrorCode,
       "nhdErrorMessage": nhdErrorMessage,
       "nhSysInfo": nhSysInfo,
       "nhServerIp": nhServerIp,
       "nhServerName": nhServerName,
       "nhServerPort": nhServerPort,
       "nhArgs": nhArgs,
       "nhElementIp": nhElementIp,
       "nhElementName": nhElementName,
       "nhElementId": nhElementId,
       "nhStartTime": nhStartTime,
       "nhExceptionType": nhExceptionType,
       "nhVariable": nhVariable,
       "nhSeverity": nhSeverity,
       "nhGroup": nhGroup,
       "nhGroupList": nhGroupList,
       "nhDisplayStr": nhDisplayStr,
       "nhExceptionId": nhExceptionId,
       "nhTechType": nhTechType,
       "nhResetTime": nhResetTime,
       "nhProfile": nhProfile,
       "nhProblemStartTime": nhProblemStartTime,
       "nhProblemDuration": nhProblemDuration}
)
