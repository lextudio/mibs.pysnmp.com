# SNMP MIB module (POLYCOM-RMX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLYCOM-RMX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:13 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

polycom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13885)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RmxStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("major", 3),
          ("minor", 2),
          ("normal", 0),
          ("startup", 1))
    )



# MIB Managed Objects in the order of their OIDs

_NsdProducts_ObjectIdentity = ObjectIdentity
nsdProducts = _NsdProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9)
)
_Rmx_ObjectIdentity = ObjectIdentity
rmx = _Rmx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1)
)
_RmxMib1_ObjectIdentity = ObjectIdentity
rmxMib1 = _RmxMib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1)
)
_RmxMib1General_ObjectIdentity = ObjectIdentity
rmxMib1General = _RmxMib1General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 1)
)
_RmxCurrentStatus_Type = RmxStatus
_RmxCurrentStatus_Object = MibScalar
rmxCurrentStatus = _RmxCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 1, 1),
    _RmxCurrentStatus_Type()
)
rmxCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmxCurrentStatus.setStatus("current")
_RmxMib1Events_ObjectIdentity = ObjectIdentity
rmxMib1Events = _RmxMib1Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2)
)
_RmxMib1EventsParams_ObjectIdentity = ObjectIdentity
rmxMib1EventsParams = _RmxMib1EventsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1)
)


class _RmxAlarmDescription_Type(OctetString):
    """Custom type rmxAlarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmxAlarmDescription_Type.__name__ = "OctetString"
_RmxAlarmDescription_Object = MibScalar
rmxAlarmDescription = _RmxAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1, 1),
    _RmxAlarmDescription_Type()
)
rmxAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rmxAlarmDescription.setStatus("current")
_RmxActiveAlarmDateAndTime_Type = DateAndTime
_RmxActiveAlarmDateAndTime_Object = MibScalar
rmxActiveAlarmDateAndTime = _RmxActiveAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1, 2),
    _RmxActiveAlarmDateAndTime_Type()
)
rmxActiveAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rmxActiveAlarmDateAndTime.setStatus("current")
_RmxActiveAlarmIndex_Type = Unsigned32
_RmxActiveAlarmIndex_Object = MibScalar
rmxActiveAlarmIndex = _RmxActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1, 3),
    _RmxActiveAlarmIndex_Type()
)
rmxActiveAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rmxActiveAlarmIndex.setStatus("current")


class _RmxActiveAlarmListName_Type(OctetString):
    """Custom type rmxActiveAlarmListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmxActiveAlarmListName_Type.__name__ = "OctetString"
_RmxActiveAlarmListName_Object = MibScalar
rmxActiveAlarmListName = _RmxActiveAlarmListName_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1, 4),
    _RmxActiveAlarmListName_Type()
)
rmxActiveAlarmListName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rmxActiveAlarmListName.setStatus("current")
_RmxActiveAlarmRmxStatus_Type = RmxStatus
_RmxActiveAlarmRmxStatus_Object = MibScalar
rmxActiveAlarmRmxStatus = _RmxActiveAlarmRmxStatus_Object(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 1, 5),
    _RmxActiveAlarmRmxStatus_Type()
)
rmxActiveAlarmRmxStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rmxActiveAlarmRmxStatus.setStatus("current")
_RmxNotify_ObjectIdentity = ObjectIdentity
rmxNotify = _RmxNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2)
)
_RmxTraps_ObjectIdentity = ObjectIdentity
rmxTraps = _RmxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0)
)
_RmxProducts_ObjectIdentity = ObjectIdentity
rmxProducts = _RmxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 10)
)
_Rmx2000_ObjectIdentity = ObjectIdentity
rmx2000 = _Rmx2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 10, 1)
)
_Rmx4000_ObjectIdentity = ObjectIdentity
rmx4000 = _Rmx4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 10, 2)
)

# Managed Objects groups


# Notification objects

rmxNoLicensingAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5001)
)
rmxNoLicensingAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoLicensingAlarmFault.setStatus(
        "current"
    )

rmxNoMeetingRoomAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5002)
)
rmxNoMeetingRoomAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoMeetingRoomAlarmFault.setStatus(
        "current"
    )

rmxNoIpServiceParamsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5003)
)
rmxNoIpServiceParamsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIpServiceParamsAlarmFault.setStatus(
        "current"
    )

rmxTaskTerminatedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5004)
)
rmxTaskTerminatedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTaskTerminatedAlarmFault.setStatus(
        "current"
    )

rmxCfgChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5005)
)
rmxCfgChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCfgChangedAlarmFault.setStatus(
        "current"
    )

rmxCfgInvalidAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5006)
)
rmxCfgInvalidAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCfgInvalidAlarmFault.setStatus(
        "current"
    )

rmxDebugModeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5007)
)
rmxDebugModeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDebugModeAlarmFault.setStatus(
        "current"
    )

rmxLowProcessMemoryAlertAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5008)
)
rmxLowProcessMemoryAlertAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxLowProcessMemoryAlertAlarmFault.setStatus(
        "current"
    )

rmxLowSystemMemoryAlertAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5009)
)
rmxLowSystemMemoryAlertAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxLowSystemMemoryAlertAlarmFault.setStatus(
        "current"
    )

rmxSystemCpuUsageAlertAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5010)
)
rmxSystemCpuUsageAlertAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemCpuUsageAlertAlarmFault.setStatus(
        "current"
    )

rmxTestErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5011)
)
rmxTestErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTestErrorAlarmFault.setStatus(
        "current"
    )

rmxSipSecuredCommunicationFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5012)
)
rmxSipSecuredCommunicationFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSipSecuredCommunicationFailedAlarmFault.setStatus(
        "current"
    )

rmxBadFileAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5013)
)
rmxBadFileAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadFileAlarmFault.setStatus(
        "current"
    )

rmxHighCpuUsageProcessAlertAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5014)
)
rmxHighCpuUsageProcessAlertAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHighCpuUsageProcessAlertAlarmFault.setStatus(
        "current"
    )

rmxIdleDeadlineReachedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5016)
)
rmxIdleDeadlineReachedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIdleDeadlineReachedAlarmFault.setStatus(
        "current"
    )

rmxStartupConditionConfigurationAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5017)
)
rmxStartupConditionConfigurationAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxStartupConditionConfigurationAlarmFault.setStatus(
        "current"
    )

rmxRestoringDefaultFactoryAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5018)
)
rmxRestoringDefaultFactoryAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoringDefaultFactoryAlarmFault.setStatus(
        "current"
    )

rmxIpVersionChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5019)
)
rmxIpVersionChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpVersionChangedAlarmFault.setStatus(
        "current"
    )

rmxNoServiceFoundInDbAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5050)
)
rmxNoServiceFoundInDbAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoServiceFoundInDbAlarmFault.setStatus(
        "current"
    )

rmxNoConnectionWithCsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5052)
)
rmxNoConnectionWithCsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithCsAlarmFault.setStatus(
        "current"
    )

rmxCsComponentFatalAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5053)
)
rmxCsComponentFatalAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsComponentFatalAlarmFault.setStatus(
        "current"
    )

rmxCsNotConfiguredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5054)
)
rmxCsNotConfiguredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsNotConfiguredAlarmFault.setStatus(
        "current"
    )

rmxCsServiceStateFailAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5055)
)
rmxCsServiceStateFailAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsServiceStateFailAlarmFault.setStatus(
        "current"
    )

rmxCsStartupFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5056)
)
rmxCsStartupFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsStartupFailedAlarmFault.setStatus(
        "current"
    )

rmxDuplicateIpCsMngmntAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5058)
)
rmxDuplicateIpCsMngmntAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDuplicateIpCsMngmntAlarmFault.setStatus(
        "current"
    )

rmxIpServiceDeletedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5059)
)
rmxIpServiceDeletedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpServiceDeletedAlarmFault.setStatus(
        "current"
    )

rmxIpServiceChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5060)
)
rmxIpServiceChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpServiceChangedAlarmFault.setStatus(
        "current"
    )

rmxCsRecoveryStatusAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5061)
)
rmxCsRecoveryStatusAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsRecoveryStatusAlarmFault.setStatus(
        "current"
    )

rmxExternalAlertCsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5062)
)
rmxExternalAlertCsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalAlertCsAlarmFault.setStatus(
        "current"
    )

rmxProductActivationFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5100)
)
rmxProductActivationFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProductActivationFailureAlarmFault.setStatus(
        "current"
    )

rmxNoManagementIpInterfaceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5101)
)
rmxNoManagementIpInterfaceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoManagementIpInterfaceAlarmFault.setStatus(
        "current"
    )

rmxNoTimeConfigurationAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5102)
)
rmxNoTimeConfigurationAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoTimeConfigurationAlarmFault.setStatus(
        "current"
    )

rmxMplStartupFailureAuthenticationNotReceivedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5103)
)
rmxMplStartupFailureAuthenticationNotReceivedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMplStartupFailureAuthenticationNotReceivedAlarmFault.setStatus(
        "current"
    )

rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5104)
)
rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmFault.setStatus(
        "current"
    )

rmxNoDnsConfigurationAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5105)
)
rmxNoDnsConfigurationAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoDnsConfigurationAlarmFault.setStatus(
        "current"
    )

rmxDnsRegistraionFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5106)
)
rmxDnsRegistraionFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDnsRegistraionFailedAlarmFault.setStatus(
        "current"
    )

rmxFailedToOpenApacheConfigurationFileAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5107)
)
rmxFailedToOpenApacheConfigurationFileAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToOpenApacheConfigurationFileAlarmFault.setStatus(
        "current"
    )

rmxFailedToSaveApacheConfigurationFileAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5108)
)
rmxFailedToSaveApacheConfigurationFileAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToSaveApacheConfigurationFileAlarmFault.setStatus(
        "current"
    )

rmxPatchedVersionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5109)
)
rmxPatchedVersionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPatchedVersionAlarmFault.setStatus(
        "current"
    )

rmxPrivateVersionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5110)
)
rmxPrivateVersionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPrivateVersionAlarmFault.setStatus(
        "current"
    )

rmxNtpSyncFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5111)
)
rmxNtpSyncFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNtpSyncFailureAlarmFault.setStatus(
        "current"
    )

rmxIllegalTimeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5112)
)
rmxIllegalTimeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIllegalTimeAlarmFault.setStatus(
        "current"
    )

rmxExternalNtpServersFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5113)
)
rmxExternalNtpServersFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalNtpServersFailureAlarmFault.setStatus(
        "current"
    )

rmxRunningVersionMismatchesCurrentVersionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5114)
)
rmxRunningVersionMismatchesCurrentVersionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRunningVersionMismatchesCurrentVersionAlarmFault.setStatus(
        "current"
    )

rmxIdeNotInDmaModeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5115)
)
rmxIdeNotInDmaModeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIdeNotInDmaModeAlarmFault.setStatus(
        "current"
    )

rmxBadEthernetSettingsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5116)
)
rmxBadEthernetSettingsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadEthernetSettingsAlarmFault.setStatus(
        "current"
    )

rmxSmartReportErrorsOnHdAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5117)
)
rmxSmartReportErrorsOnHdAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSmartReportErrorsOnHdAlarmFault.setStatus(
        "current"
    )

rmxIllegalMcuVersionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5118)
)
rmxIllegalMcuVersionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIllegalMcuVersionAlarmFault.setStatus(
        "current"
    )

rmxDebugCfgExistAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5119)
)
rmxDebugCfgExistAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDebugCfgExistAlarmFault.setStatus(
        "current"
    )

rmxInstallingNewVersionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5120)
)
rmxInstallingNewVersionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInstallingNewVersionAlarmFault.setStatus(
        "current"
    )

rmxSshEnabledAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5121)
)
rmxSshEnabledAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSshEnabledAlarmFault.setStatus(
        "current"
    )

rmxFailedToValidateCertificateAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5122)
)
rmxFailedToValidateCertificateAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToValidateCertificateAlarmFault.setStatus(
        "current"
    )

rmxCertificateExpiredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5123)
)
rmxCertificateExpiredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateExpiredAlarmFault.setStatus(
        "current"
    )

rmxCertificateCommonNameErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5124)
)
rmxCertificateCommonNameErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateCommonNameErrorAlarmFault.setStatus(
        "current"
    )

rmxCertificateNotValidYetAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5125)
)
rmxCertificateNotValidYetAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateNotValidYetAlarmFault.setStatus(
        "current"
    )

rmxCertificateGoingToBeExpiredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5126)
)
rmxCertificateGoingToBeExpiredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateGoingToBeExpiredAlarmFault.setStatus(
        "current"
    )

rmxProductTypeMismatchAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5127)
)
rmxProductTypeMismatchAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProductTypeMismatchAlarmFault.setStatus(
        "current"
    )

rmxUnknownCpuSlotIdAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5128)
)
rmxUnknownCpuSlotIdAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUnknownCpuSlotIdAlarmFault.setStatus(
        "current"
    )

rmxNoFipsTestResultFromEncryptionkeyserverAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5129)
)
rmxNoFipsTestResultFromEncryptionkeyserverAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoFipsTestResultFromEncryptionkeyserverAlarmFault.setStatus(
        "current"
    )

rmxFipsFailureWithinEncryptionkeyserverAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5130)
)
rmxFipsFailureWithinEncryptionkeyserverAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFipsFailureWithinEncryptionkeyserverAlarmFault.setStatus(
        "current"
    )

rmxHttpsDisabledInJitcAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5131)
)
rmxHttpsDisabledInJitcAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHttpsDisabledInJitcAlarmFault.setStatus(
        "current"
    )

rmxBackupOfCdrFilesIsRequiredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5140)
)
rmxBackupOfCdrFilesIsRequiredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfCdrFilesIsRequiredAlarmFault.setStatus(
        "current"
    )

rmxNoMusicSourceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5150)
)
rmxNoMusicSourceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoMusicSourceAlarmFault.setStatus(
        "current"
    )

rmxSwitchNotLoadedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5151)
)
rmxSwitchNotLoadedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSwitchNotLoadedAlarmFault.setStatus(
        "current"
    )

rmxNoIsdnServiceParamsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5152)
)
rmxNoIsdnServiceParamsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIsdnServiceParamsAlarmFault.setStatus(
        "current"
    )

rmxModuleDoesNotExistAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5153)
)
rmxModuleDoesNotExistAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxModuleDoesNotExistAlarmFault.setStatus(
        "current"
    )

rmxNoDefaultIsdnServiceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5154)
)
rmxNoDefaultIsdnServiceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoDefaultIsdnServiceAlarmFault.setStatus(
        "current"
    )

rmxExternalAlertEmbAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5155)
)
rmxExternalAlertEmbAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalAlertEmbAlarmFault.setStatus(
        "current"
    )

rmxVersionInstallProgressAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5156)
)
rmxVersionInstallProgressAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVersionInstallProgressAlarmFault.setStatus(
        "current"
    )

rmxVersionIpmcInstallProgressAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5157)
)
rmxVersionIpmcInstallProgressAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVersionIpmcInstallProgressAlarmFault.setStatus(
        "current"
    )

rmxVoltageProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5200)
)
rmxVoltageProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVoltageProblemAlarmFault.setStatus(
        "current"
    )

rmxTemperatureMajorProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5201)
)
rmxTemperatureMajorProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTemperatureMajorProblemAlarmFault.setStatus(
        "current"
    )

rmxTemperatureCriticalProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5202)
)
rmxTemperatureCriticalProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTemperatureCriticalProblemAlarmFault.setStatus(
        "current"
    )

rmxFailureProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5203)
)
rmxFailureProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailureProblemAlarmFault.setStatus(
        "current"
    )

rmxPowerOffProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5204)
)
rmxPowerOffProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPowerOffProblemAlarmFault.setStatus(
        "current"
    )

rmxOtherProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5205)
)
rmxOtherProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxOtherProblemAlarmFault.setStatus(
        "current"
    )

rmxNoConnectionWithCardAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5206)
)
rmxNoConnectionWithCardAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithCardAlarmFault.setStatus(
        "current"
    )

rmxUnitNotRespondingAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5207)
)
rmxUnitNotRespondingAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUnitNotRespondingAlarmFault.setStatus(
        "current"
    )

rmxMediaIpConfigurationFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5208)
)
rmxMediaIpConfigurationFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMediaIpConfigurationFailureAlarmFault.setStatus(
        "current"
    )

rmxCardFolderMountingFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5209)
)
rmxCardFolderMountingFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardFolderMountingFailedAlarmFault.setStatus(
        "current"
    )

rmxCardStartupFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5211)
)
rmxCardStartupFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardStartupFailureAlarmFault.setStatus(
        "current"
    )

rmxRtmIsdnStartupFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5212)
)
rmxRtmIsdnStartupFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmIsdnStartupFailureAlarmFault.setStatus(
        "current"
    )

rmxRtmIsdnStartupProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5213)
)
rmxRtmIsdnStartupProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmIsdnStartupProblemAlarmFault.setStatus(
        "current"
    )

rmxNoConnectionWithRtmIsdnAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5214)
)
rmxNoConnectionWithRtmIsdnAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithRtmIsdnAlarmFault.setStatus(
        "current"
    )

rmxRedAlarmAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5215)
)
rmxRedAlarmAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRedAlarmAlarmFault.setStatus(
        "current"
    )

rmxYellowAlarmAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5216)
)
rmxYellowAlarmAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxYellowAlarmAlarmFault.setStatus(
        "current"
    )

rmxDChannelNotEstablishedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5217)
)
rmxDChannelNotEstablishedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDChannelNotEstablishedAlarmFault.setStatus(
        "current"
    )

rmxCardsConfigEventAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5218)
)
rmxCardsConfigEventAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsConfigEventAlarmFault.setStatus(
        "current"
    )

rmxCardsWrongFileModeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5219)
)
rmxCardsWrongFileModeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsWrongFileModeAlarmFault.setStatus(
        "current"
    )

rmxCardsFlashAccessProblemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5220)
)
rmxCardsFlashAccessProblemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsFlashAccessProblemAlarmFault.setStatus(
        "current"
    )

rmxRtmLanOrIsdnMissingAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5221)
)
rmxRtmLanOrIsdnMissingAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmLanOrIsdnMissingAlarmFault.setStatus(
        "current"
    )

rmxNoLanConnectionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5222)
)
rmxNoLanConnectionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoLanConnectionAlarmFault.setStatus(
        "current"
    )

rmxCanNotEstablishConnectionWithSipRegistrarAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5300)
)
rmxCanNotEstablishConnectionWithSipRegistrarAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotEstablishConnectionWithSipRegistrarAlarmFault.setStatus(
        "current"
    )

rmxSipRegistrationLimitReachedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5301)
)
rmxSipRegistrationLimitReachedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSipRegistrationLimitReachedAlarmFault.setStatus(
        "current"
    )

rmxFailedToAccessDnsServerAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5350)
)
rmxFailedToAccessDnsServerAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToAccessDnsServerAlarmFault.setStatus(
        "current"
    )

rmxNoIndDnsSuccessAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5351)
)
rmxNoIndDnsSuccessAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIndDnsSuccessAlarmFault.setStatus(
        "current"
    )

rmxFailedToInitFileSystemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5400)
)
rmxFailedToInitFileSystemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToInitFileSystemAlarmFault.setStatus(
        "current"
    )

rmxBadFileSystemAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5401)
)
rmxBadFileSystemAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadFileSystemAlarmFault.setStatus(
        "current"
    )

rmxBadHardDiskAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5402)
)
rmxBadHardDiskAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadHardDiskAlarmFault.setStatus(
        "current"
    )

rmxBackupOfLogFilesIsRequiredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5403)
)
rmxBackupOfLogFilesIsRequiredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfLogFilesIsRequiredAlarmFault.setStatus(
        "current"
    )

rmxBackupOfAuditFilesIsRequiredAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5430)
)
rmxBackupOfAuditFilesIsRequiredAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfAuditFilesIsRequiredAlarmFault.setStatus(
        "current"
    )

rmxFailedToFillActionRedirectionAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5450)
)
rmxFailedToFillActionRedirectionAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToFillActionRedirectionAlarmFault.setStatus(
        "current"
    )

rmxFailedConfigUserListInLinuxAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5500)
)
rmxFailedConfigUserListInLinuxAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedConfigUserListInLinuxAlarmFault.setStatus(
        "current"
    )

rmxInsufficientResourcesAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5550)
)
rmxInsufficientResourcesAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInsufficientResourcesAlarmFault.setStatus(
        "current"
    )

rmxPortConfigurationChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5551)
)
rmxPortConfigurationChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPortConfigurationChangedAlarmFault.setStatus(
        "current"
    )

rmxNoUtilizableUnitForAudioControllerAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5552)
)
rmxNoUtilizableUnitForAudioControllerAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoUtilizableUnitForAudioControllerAlarmFault.setStatus(
        "current"
    )

rmxAllocationModeChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5553)
)
rmxAllocationModeChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxAllocationModeChangedAlarmFault.setStatus(
        "current"
    )

rmxProcessTerminatedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5601)
)
rmxProcessTerminatedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProcessTerminatedAlarmFault.setStatus(
        "current"
    )

rmxResetMcuByTerminalAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5602)
)
rmxResetMcuByTerminalAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuByTerminalAlarmFault.setStatus(
        "current"
    )

rmxResetMcuByOperatorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5603)
)
rmxResetMcuByOperatorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuByOperatorAlarmFault.setStatus(
        "current"
    )

rmxResetMcuInternalAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5604)
)
rmxResetMcuInternalAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuInternalAlarmFault.setStatus(
        "current"
    )

rmxResetMcuAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5605)
)
rmxResetMcuAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuAlarmFault.setStatus(
        "current"
    )

rmxResetMcuDiagnosticsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5606)
)
rmxResetMcuDiagnosticsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuDiagnosticsAlarmFault.setStatus(
        "current"
    )

rmxProcessStartupFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5607)
)
rmxProcessStartupFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProcessStartupFailedAlarmFault.setStatus(
        "current"
    )

rmxSystemInSafeModeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5608)
)
rmxSystemInSafeModeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemInSafeModeAlarmFault.setStatus(
        "current"
    )

rmxGuiSystemConfigIsIllegalAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5609)
)
rmxGuiSystemConfigIsIllegalAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGuiSystemConfigIsIllegalAlarmFault.setStatus(
        "current"
    )

rmxFileSystemFailedToScanAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5650)
)
rmxFileSystemFailedToScanAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFileSystemFailedToScanAlarmFault.setStatus(
        "current"
    )

rmxFileSystemOverflowAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5651)
)
rmxFileSystemOverflowAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFileSystemOverflowAlarmFault.setStatus(
        "current"
    )

rmxHardDiskFailureAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5652)
)
rmxHardDiskFailureAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHardDiskFailureAlarmFault.setStatus(
        "current"
    )

rmxCpuIpcmSoftwareIsNotUpdatedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5690)
)
rmxCpuIpcmSoftwareIsNotUpdatedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCpuIpcmSoftwareIsNotUpdatedAlarmFault.setStatus(
        "current"
    )

rmxNewVersionInstalledAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5700)
)
rmxNewVersionInstalledAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNewVersionInstalledAlarmFault.setStatus(
        "current"
    )

rmxNewActivationKeyLoadedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5701)
)
rmxNewActivationKeyLoadedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNewActivationKeyLoadedAlarmFault.setStatus(
        "current"
    )

rmxInsufficientUdpPortsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5751)
)
rmxInsufficientUdpPortsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInsufficientUdpPortsAlarmFault.setStatus(
        "current"
    )

rmxUsersListCorruptedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5800)
)
rmxUsersListCorruptedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUsersListCorruptedAlarmFault.setStatus(
        "current"
    )

rmxDefaultUserExistsAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5801)
)
rmxDefaultUserExistsAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDefaultUserExistsAlarmFault.setStatus(
        "current"
    )

rmxSupportOperatorIllegalInFederalModeAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5802)
)
rmxSupportOperatorIllegalInFederalModeAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSupportOperatorIllegalInFederalModeAlarmFault.setStatus(
        "current"
    )

rmxIsdnServicesConfigurationChangedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5900)
)
rmxIsdnServicesConfigurationChangedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIsdnServicesConfigurationChangedAlarmFault.setStatus(
        "current"
    )

rmxNoIsdnPstnLicensingAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5901)
)
rmxNoIsdnPstnLicensingAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIsdnPstnLicensingAlarmFault.setStatus(
        "current"
    )

rmxNoRtmIsdnCardAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5902)
)
rmxNoRtmIsdnCardAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoRtmIsdnCardAlarmFault.setStatus(
        "current"
    )

rmxNoClockSourceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5903)
)
rmxNoClockSourceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoClockSourceAlarmFault.setStatus(
        "current"
    )

rmxSingleClockSourceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5904)
)
rmxSingleClockSourceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSingleClockSourceAlarmFault.setStatus(
        "current"
    )

rmxGkmngrAvfWrongMcuConfigAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5950)
)
rmxGkmngrAvfWrongMcuConfigAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGkmngrAvfWrongMcuConfigAlarmFault.setStatus(
        "current"
    )

rmxGateKeeperErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 5951)
)
rmxGateKeeperErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGateKeeperErrorAlarmFault.setStatus(
        "current"
    )

rmxCanNotEstablishConnectionWithApplicationServerAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6000)
)
rmxCanNotEstablishConnectionWithApplicationServerAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotEstablishConnectionWithApplicationServerAlarmFault.setStatus(
        "current"
    )

rmxSystemConfigurationAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6001)
)
rmxSystemConfigurationAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemConfigurationAlarmFault.setStatus(
        "current"
    )

rmxExternalDbCertificateErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6002)
)
rmxExternalDbCertificateErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalDbCertificateErrorAlarmFault.setStatus(
        "current"
    )

rmxIvrServiceListMissingDefaultServiceAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6050)
)
rmxIvrServiceListMissingDefaultServiceAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIvrServiceListMissingDefaultServiceAlarmFault.setStatus(
        "current"
    )

rmxCanNotCreateDefaultProfileAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6051)
)
rmxCanNotCreateDefaultProfileAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotCreateDefaultProfileAlarmFault.setStatus(
        "current"
    )

rmxNoReadMrDbReqRecievedFromRsrcAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6052)
)
rmxNoReadMrDbReqRecievedFromRsrcAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoReadMrDbReqRecievedFromRsrcAlarmFault.setStatus(
        "current"
    )

rmxFailedToConnectRecordingLinkAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6053)
)
rmxFailedToConnectRecordingLinkAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToConnectRecordingLinkAlarmFault.setStatus(
        "current"
    )

rmxRecordingLinkDisconnecedUnexpectedlyAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6054)
)
rmxRecordingLinkDisconnecedUnexpectedlyAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRecordingLinkDisconnecedUnexpectedlyAlarmFault.setStatus(
        "current"
    )

rmxSystemBasedModeNotIntializedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6055)
)
rmxSystemBasedModeNotIntializedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemBasedModeNotIntializedAlarmFault.setStatus(
        "current"
    )

rmxConfEncryptionErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6056)
)
rmxConfEncryptionErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxConfEncryptionErrorAlarmFault.setStatus(
        "current"
    )

rmxSnmpAgentInitFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6100)
)
rmxSnmpAgentInitFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSnmpAgentInitFailedAlarmFault.setStatus(
        "current"
    )

rmxRestoreSucceededAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6200)
)
rmxRestoreSucceededAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoreSucceededAlarmFault.setStatus(
        "current"
    )

rmxRestoreFailedAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 6201)
)
rmxRestoreFailedAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoreFailedAlarmFault.setStatus(
        "current"
    )

rmxEncryptionServerErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 7010)
)
rmxEncryptionServerErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxEncryptionServerErrorAlarmFault.setStatus(
        "current"
    )

rmxExchangeServerConnectionErrorAlarmFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 7050)
)
rmxExchangeServerConnectionErrorAlarmFault.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExchangeServerConnectionErrorAlarmFault.setStatus(
        "current"
    )

rmxNoLicensingAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15001)
)
rmxNoLicensingAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoLicensingAlarmClear.setStatus(
        "current"
    )

rmxNoMeetingRoomAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15002)
)
rmxNoMeetingRoomAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoMeetingRoomAlarmClear.setStatus(
        "current"
    )

rmxNoIpServiceParamsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15003)
)
rmxNoIpServiceParamsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIpServiceParamsAlarmClear.setStatus(
        "current"
    )

rmxTaskTerminatedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15004)
)
rmxTaskTerminatedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTaskTerminatedAlarmClear.setStatus(
        "current"
    )

rmxCfgChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15005)
)
rmxCfgChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCfgChangedAlarmClear.setStatus(
        "current"
    )

rmxCfgInvalidAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15006)
)
rmxCfgInvalidAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCfgInvalidAlarmClear.setStatus(
        "current"
    )

rmxDebugModeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15007)
)
rmxDebugModeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDebugModeAlarmClear.setStatus(
        "current"
    )

rmxLowProcessMemoryAlertAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15008)
)
rmxLowProcessMemoryAlertAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxLowProcessMemoryAlertAlarmClear.setStatus(
        "current"
    )

rmxLowSystemMemoryAlertAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15009)
)
rmxLowSystemMemoryAlertAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxLowSystemMemoryAlertAlarmClear.setStatus(
        "current"
    )

rmxSystemCpuUsageAlertAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15010)
)
rmxSystemCpuUsageAlertAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemCpuUsageAlertAlarmClear.setStatus(
        "current"
    )

rmxTestErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15011)
)
rmxTestErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTestErrorAlarmClear.setStatus(
        "current"
    )

rmxSipSecuredCommunicationFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15012)
)
rmxSipSecuredCommunicationFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSipSecuredCommunicationFailedAlarmClear.setStatus(
        "current"
    )

rmxBadFileAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15013)
)
rmxBadFileAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadFileAlarmClear.setStatus(
        "current"
    )

rmxHighCpuUsageProcessAlertAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15014)
)
rmxHighCpuUsageProcessAlertAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHighCpuUsageProcessAlertAlarmClear.setStatus(
        "current"
    )

rmxIdleDeadlineReachedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15016)
)
rmxIdleDeadlineReachedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIdleDeadlineReachedAlarmClear.setStatus(
        "current"
    )

rmxStartupConditionConfigurationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15017)
)
rmxStartupConditionConfigurationAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxStartupConditionConfigurationAlarmClear.setStatus(
        "current"
    )

rmxRestoringDefaultFactoryAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15018)
)
rmxRestoringDefaultFactoryAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoringDefaultFactoryAlarmClear.setStatus(
        "current"
    )

rmxIpVersionChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15019)
)
rmxIpVersionChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpVersionChangedAlarmClear.setStatus(
        "current"
    )

rmxNoServiceFoundInDbAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15050)
)
rmxNoServiceFoundInDbAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoServiceFoundInDbAlarmClear.setStatus(
        "current"
    )

rmxNoConnectionWithCsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15052)
)
rmxNoConnectionWithCsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithCsAlarmClear.setStatus(
        "current"
    )

rmxCsComponentFatalAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15053)
)
rmxCsComponentFatalAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsComponentFatalAlarmClear.setStatus(
        "current"
    )

rmxCsNotConfiguredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15054)
)
rmxCsNotConfiguredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsNotConfiguredAlarmClear.setStatus(
        "current"
    )

rmxCsServiceStateFailAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15055)
)
rmxCsServiceStateFailAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsServiceStateFailAlarmClear.setStatus(
        "current"
    )

rmxCsStartupFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15056)
)
rmxCsStartupFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsStartupFailedAlarmClear.setStatus(
        "current"
    )

rmxDuplicateIpCsMngmntAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15058)
)
rmxDuplicateIpCsMngmntAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDuplicateIpCsMngmntAlarmClear.setStatus(
        "current"
    )

rmxIpServiceDeletedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15059)
)
rmxIpServiceDeletedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpServiceDeletedAlarmClear.setStatus(
        "current"
    )

rmxIpServiceChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15060)
)
rmxIpServiceChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIpServiceChangedAlarmClear.setStatus(
        "current"
    )

rmxCsRecoveryStatusAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15061)
)
rmxCsRecoveryStatusAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCsRecoveryStatusAlarmClear.setStatus(
        "current"
    )

rmxExternalAlertCsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15062)
)
rmxExternalAlertCsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalAlertCsAlarmClear.setStatus(
        "current"
    )

rmxProductActivationFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15100)
)
rmxProductActivationFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProductActivationFailureAlarmClear.setStatus(
        "current"
    )

rmxNoManagementIpInterfaceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15101)
)
rmxNoManagementIpInterfaceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoManagementIpInterfaceAlarmClear.setStatus(
        "current"
    )

rmxNoTimeConfigurationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15102)
)
rmxNoTimeConfigurationAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoTimeConfigurationAlarmClear.setStatus(
        "current"
    )

rmxMplStartupFailureAuthenticationNotReceivedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15103)
)
rmxMplStartupFailureAuthenticationNotReceivedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMplStartupFailureAuthenticationNotReceivedAlarmClear.setStatus(
        "current"
    )

rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15104)
)
rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmClear.setStatus(
        "current"
    )

rmxNoDnsConfigurationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15105)
)
rmxNoDnsConfigurationAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoDnsConfigurationAlarmClear.setStatus(
        "current"
    )

rmxDnsRegistraionFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15106)
)
rmxDnsRegistraionFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDnsRegistraionFailedAlarmClear.setStatus(
        "current"
    )

rmxFailedToOpenApacheConfigurationFileAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15107)
)
rmxFailedToOpenApacheConfigurationFileAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToOpenApacheConfigurationFileAlarmClear.setStatus(
        "current"
    )

rmxFailedToSaveApacheConfigurationFileAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15108)
)
rmxFailedToSaveApacheConfigurationFileAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToSaveApacheConfigurationFileAlarmClear.setStatus(
        "current"
    )

rmxPatchedVersionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15109)
)
rmxPatchedVersionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPatchedVersionAlarmClear.setStatus(
        "current"
    )

rmxPrivateVersionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15110)
)
rmxPrivateVersionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPrivateVersionAlarmClear.setStatus(
        "current"
    )

rmxNtpSyncFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15111)
)
rmxNtpSyncFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNtpSyncFailureAlarmClear.setStatus(
        "current"
    )

rmxIllegalTimeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15112)
)
rmxIllegalTimeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIllegalTimeAlarmClear.setStatus(
        "current"
    )

rmxExternalNtpServersFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15113)
)
rmxExternalNtpServersFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalNtpServersFailureAlarmClear.setStatus(
        "current"
    )

rmxRunningVersionMismatchesCurrentVersionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15114)
)
rmxRunningVersionMismatchesCurrentVersionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRunningVersionMismatchesCurrentVersionAlarmClear.setStatus(
        "current"
    )

rmxIdeNotInDmaModeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15115)
)
rmxIdeNotInDmaModeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIdeNotInDmaModeAlarmClear.setStatus(
        "current"
    )

rmxBadEthernetSettingsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15116)
)
rmxBadEthernetSettingsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadEthernetSettingsAlarmClear.setStatus(
        "current"
    )

rmxSmartReportErrorsOnHdAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15117)
)
rmxSmartReportErrorsOnHdAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSmartReportErrorsOnHdAlarmClear.setStatus(
        "current"
    )

rmxIllegalMcuVersionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15118)
)
rmxIllegalMcuVersionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIllegalMcuVersionAlarmClear.setStatus(
        "current"
    )

rmxDebugCfgExistAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15119)
)
rmxDebugCfgExistAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDebugCfgExistAlarmClear.setStatus(
        "current"
    )

rmxInstallingNewVersionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15120)
)
rmxInstallingNewVersionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInstallingNewVersionAlarmClear.setStatus(
        "current"
    )

rmxSshEnabledAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15121)
)
rmxSshEnabledAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSshEnabledAlarmClear.setStatus(
        "current"
    )

rmxFailedToValidateCertificateAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15122)
)
rmxFailedToValidateCertificateAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToValidateCertificateAlarmClear.setStatus(
        "current"
    )

rmxCertificateExpiredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15123)
)
rmxCertificateExpiredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateExpiredAlarmClear.setStatus(
        "current"
    )

rmxCertificateCommonNameErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15124)
)
rmxCertificateCommonNameErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateCommonNameErrorAlarmClear.setStatus(
        "current"
    )

rmxCertificateNotValidYetAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15125)
)
rmxCertificateNotValidYetAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateNotValidYetAlarmClear.setStatus(
        "current"
    )

rmxCertificateGoingToBeExpiredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15126)
)
rmxCertificateGoingToBeExpiredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCertificateGoingToBeExpiredAlarmClear.setStatus(
        "current"
    )

rmxProductTypeMismatchAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15127)
)
rmxProductTypeMismatchAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProductTypeMismatchAlarmClear.setStatus(
        "current"
    )

rmxUnknownCpuSlotIdAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15128)
)
rmxUnknownCpuSlotIdAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUnknownCpuSlotIdAlarmClear.setStatus(
        "current"
    )

rmxNoFipsTestResultFromEncryptionkeyserverAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15129)
)
rmxNoFipsTestResultFromEncryptionkeyserverAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoFipsTestResultFromEncryptionkeyserverAlarmClear.setStatus(
        "current"
    )

rmxFipsFailureWithinEncryptionkeyserverAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15130)
)
rmxFipsFailureWithinEncryptionkeyserverAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFipsFailureWithinEncryptionkeyserverAlarmClear.setStatus(
        "current"
    )

rmxHttpsDisabledInJitcAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15131)
)
rmxHttpsDisabledInJitcAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHttpsDisabledInJitcAlarmClear.setStatus(
        "current"
    )

rmxBackupOfCdrFilesIsRequiredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15140)
)
rmxBackupOfCdrFilesIsRequiredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfCdrFilesIsRequiredAlarmClear.setStatus(
        "current"
    )

rmxNoMusicSourceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15150)
)
rmxNoMusicSourceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoMusicSourceAlarmClear.setStatus(
        "current"
    )

rmxSwitchNotLoadedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15151)
)
rmxSwitchNotLoadedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSwitchNotLoadedAlarmClear.setStatus(
        "current"
    )

rmxNoIsdnServiceParamsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15152)
)
rmxNoIsdnServiceParamsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIsdnServiceParamsAlarmClear.setStatus(
        "current"
    )

rmxModuleDoesNotExistAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15153)
)
rmxModuleDoesNotExistAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxModuleDoesNotExistAlarmClear.setStatus(
        "current"
    )

rmxNoDefaultIsdnServiceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15154)
)
rmxNoDefaultIsdnServiceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoDefaultIsdnServiceAlarmClear.setStatus(
        "current"
    )

rmxExternalAlertEmbAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15155)
)
rmxExternalAlertEmbAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalAlertEmbAlarmClear.setStatus(
        "current"
    )

rmxVersionInstallProgressAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15156)
)
rmxVersionInstallProgressAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVersionInstallProgressAlarmClear.setStatus(
        "current"
    )

rmxVersionIpmcInstallProgressAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15157)
)
rmxVersionIpmcInstallProgressAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVersionIpmcInstallProgressAlarmClear.setStatus(
        "current"
    )

rmxVoltageProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15200)
)
rmxVoltageProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxVoltageProblemAlarmClear.setStatus(
        "current"
    )

rmxTemperatureMajorProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15201)
)
rmxTemperatureMajorProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTemperatureMajorProblemAlarmClear.setStatus(
        "current"
    )

rmxTemperatureCriticalProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15202)
)
rmxTemperatureCriticalProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxTemperatureCriticalProblemAlarmClear.setStatus(
        "current"
    )

rmxFailureProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15203)
)
rmxFailureProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailureProblemAlarmClear.setStatus(
        "current"
    )

rmxPowerOffProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15204)
)
rmxPowerOffProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPowerOffProblemAlarmClear.setStatus(
        "current"
    )

rmxOtherProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15205)
)
rmxOtherProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxOtherProblemAlarmClear.setStatus(
        "current"
    )

rmxNoConnectionWithCardAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15206)
)
rmxNoConnectionWithCardAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithCardAlarmClear.setStatus(
        "current"
    )

rmxUnitNotRespondingAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15207)
)
rmxUnitNotRespondingAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUnitNotRespondingAlarmClear.setStatus(
        "current"
    )

rmxMediaIpConfigurationFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15208)
)
rmxMediaIpConfigurationFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxMediaIpConfigurationFailureAlarmClear.setStatus(
        "current"
    )

rmxCardFolderMountingFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15209)
)
rmxCardFolderMountingFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardFolderMountingFailedAlarmClear.setStatus(
        "current"
    )

rmxCardStartupFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15211)
)
rmxCardStartupFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardStartupFailureAlarmClear.setStatus(
        "current"
    )

rmxRtmIsdnStartupFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15212)
)
rmxRtmIsdnStartupFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmIsdnStartupFailureAlarmClear.setStatus(
        "current"
    )

rmxRtmIsdnStartupProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15213)
)
rmxRtmIsdnStartupProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmIsdnStartupProblemAlarmClear.setStatus(
        "current"
    )

rmxNoConnectionWithRtmIsdnAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15214)
)
rmxNoConnectionWithRtmIsdnAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoConnectionWithRtmIsdnAlarmClear.setStatus(
        "current"
    )

rmxRedAlarmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15215)
)
rmxRedAlarmAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRedAlarmAlarmClear.setStatus(
        "current"
    )

rmxYellowAlarmAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15216)
)
rmxYellowAlarmAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxYellowAlarmAlarmClear.setStatus(
        "current"
    )

rmxDChannelNotEstablishedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15217)
)
rmxDChannelNotEstablishedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDChannelNotEstablishedAlarmClear.setStatus(
        "current"
    )

rmxCardsConfigEventAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15218)
)
rmxCardsConfigEventAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsConfigEventAlarmClear.setStatus(
        "current"
    )

rmxCardsWrongFileModeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15219)
)
rmxCardsWrongFileModeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsWrongFileModeAlarmClear.setStatus(
        "current"
    )

rmxCardsFlashAccessProblemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15220)
)
rmxCardsFlashAccessProblemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCardsFlashAccessProblemAlarmClear.setStatus(
        "current"
    )

rmxRtmLanOrIsdnMissingAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15221)
)
rmxRtmLanOrIsdnMissingAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRtmLanOrIsdnMissingAlarmClear.setStatus(
        "current"
    )

rmxNoLanConnectionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15222)
)
rmxNoLanConnectionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoLanConnectionAlarmClear.setStatus(
        "current"
    )

rmxCanNotEstablishConnectionWithSipRegistrarAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15300)
)
rmxCanNotEstablishConnectionWithSipRegistrarAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotEstablishConnectionWithSipRegistrarAlarmClear.setStatus(
        "current"
    )

rmxSipRegistrationLimitReachedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15301)
)
rmxSipRegistrationLimitReachedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSipRegistrationLimitReachedAlarmClear.setStatus(
        "current"
    )

rmxFailedToAccessDnsServerAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15350)
)
rmxFailedToAccessDnsServerAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToAccessDnsServerAlarmClear.setStatus(
        "current"
    )

rmxNoIndDnsSuccessAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15351)
)
rmxNoIndDnsSuccessAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIndDnsSuccessAlarmClear.setStatus(
        "current"
    )

rmxFailedToInitFileSystemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15400)
)
rmxFailedToInitFileSystemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToInitFileSystemAlarmClear.setStatus(
        "current"
    )

rmxBadFileSystemAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15401)
)
rmxBadFileSystemAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadFileSystemAlarmClear.setStatus(
        "current"
    )

rmxBadHardDiskAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15402)
)
rmxBadHardDiskAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBadHardDiskAlarmClear.setStatus(
        "current"
    )

rmxBackupOfLogFilesIsRequiredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15403)
)
rmxBackupOfLogFilesIsRequiredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfLogFilesIsRequiredAlarmClear.setStatus(
        "current"
    )

rmxBackupOfAuditFilesIsRequiredAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15430)
)
rmxBackupOfAuditFilesIsRequiredAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxBackupOfAuditFilesIsRequiredAlarmClear.setStatus(
        "current"
    )

rmxFailedToFillActionRedirectionAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15450)
)
rmxFailedToFillActionRedirectionAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToFillActionRedirectionAlarmClear.setStatus(
        "current"
    )

rmxFailedConfigUserListInLinuxAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15500)
)
rmxFailedConfigUserListInLinuxAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedConfigUserListInLinuxAlarmClear.setStatus(
        "current"
    )

rmxInsufficientResourcesAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15550)
)
rmxInsufficientResourcesAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInsufficientResourcesAlarmClear.setStatus(
        "current"
    )

rmxPortConfigurationChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15551)
)
rmxPortConfigurationChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxPortConfigurationChangedAlarmClear.setStatus(
        "current"
    )

rmxNoUtilizableUnitForAudioControllerAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15552)
)
rmxNoUtilizableUnitForAudioControllerAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoUtilizableUnitForAudioControllerAlarmClear.setStatus(
        "current"
    )

rmxAllocationModeChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15553)
)
rmxAllocationModeChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxAllocationModeChangedAlarmClear.setStatus(
        "current"
    )

rmxProcessTerminatedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15601)
)
rmxProcessTerminatedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProcessTerminatedAlarmClear.setStatus(
        "current"
    )

rmxResetMcuByTerminalAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15602)
)
rmxResetMcuByTerminalAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuByTerminalAlarmClear.setStatus(
        "current"
    )

rmxResetMcuByOperatorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15603)
)
rmxResetMcuByOperatorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuByOperatorAlarmClear.setStatus(
        "current"
    )

rmxResetMcuInternalAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15604)
)
rmxResetMcuInternalAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuInternalAlarmClear.setStatus(
        "current"
    )

rmxResetMcuAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15605)
)
rmxResetMcuAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuAlarmClear.setStatus(
        "current"
    )

rmxResetMcuDiagnosticsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15606)
)
rmxResetMcuDiagnosticsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxResetMcuDiagnosticsAlarmClear.setStatus(
        "current"
    )

rmxProcessStartupFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15607)
)
rmxProcessStartupFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxProcessStartupFailedAlarmClear.setStatus(
        "current"
    )

rmxSystemInSafeModeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15608)
)
rmxSystemInSafeModeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemInSafeModeAlarmClear.setStatus(
        "current"
    )

rmxGuiSystemConfigIsIllegalAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15609)
)
rmxGuiSystemConfigIsIllegalAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGuiSystemConfigIsIllegalAlarmClear.setStatus(
        "current"
    )

rmxFileSystemFailedToScanAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15650)
)
rmxFileSystemFailedToScanAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFileSystemFailedToScanAlarmClear.setStatus(
        "current"
    )

rmxFileSystemOverflowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15651)
)
rmxFileSystemOverflowAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFileSystemOverflowAlarmClear.setStatus(
        "current"
    )

rmxHardDiskFailureAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15652)
)
rmxHardDiskFailureAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxHardDiskFailureAlarmClear.setStatus(
        "current"
    )

rmxCpuIpcmSoftwareIsNotUpdatedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15690)
)
rmxCpuIpcmSoftwareIsNotUpdatedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCpuIpcmSoftwareIsNotUpdatedAlarmClear.setStatus(
        "current"
    )

rmxNewVersionInstalledAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15700)
)
rmxNewVersionInstalledAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNewVersionInstalledAlarmClear.setStatus(
        "current"
    )

rmxNewActivationKeyLoadedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15701)
)
rmxNewActivationKeyLoadedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNewActivationKeyLoadedAlarmClear.setStatus(
        "current"
    )

rmxInsufficientUdpPortsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15751)
)
rmxInsufficientUdpPortsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxInsufficientUdpPortsAlarmClear.setStatus(
        "current"
    )

rmxUsersListCorruptedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15800)
)
rmxUsersListCorruptedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxUsersListCorruptedAlarmClear.setStatus(
        "current"
    )

rmxDefaultUserExistsAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15801)
)
rmxDefaultUserExistsAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxDefaultUserExistsAlarmClear.setStatus(
        "current"
    )

rmxSupportOperatorIllegalInFederalModeAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15802)
)
rmxSupportOperatorIllegalInFederalModeAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSupportOperatorIllegalInFederalModeAlarmClear.setStatus(
        "current"
    )

rmxIsdnServicesConfigurationChangedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15900)
)
rmxIsdnServicesConfigurationChangedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIsdnServicesConfigurationChangedAlarmClear.setStatus(
        "current"
    )

rmxNoIsdnPstnLicensingAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15901)
)
rmxNoIsdnPstnLicensingAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoIsdnPstnLicensingAlarmClear.setStatus(
        "current"
    )

rmxNoRtmIsdnCardAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15902)
)
rmxNoRtmIsdnCardAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoRtmIsdnCardAlarmClear.setStatus(
        "current"
    )

rmxNoClockSourceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15903)
)
rmxNoClockSourceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoClockSourceAlarmClear.setStatus(
        "current"
    )

rmxSingleClockSourceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15904)
)
rmxSingleClockSourceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSingleClockSourceAlarmClear.setStatus(
        "current"
    )

rmxGkmngrAvfWrongMcuConfigAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15950)
)
rmxGkmngrAvfWrongMcuConfigAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGkmngrAvfWrongMcuConfigAlarmClear.setStatus(
        "current"
    )

rmxGateKeeperErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 15951)
)
rmxGateKeeperErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxGateKeeperErrorAlarmClear.setStatus(
        "current"
    )

rmxCanNotEstablishConnectionWithApplicationServerAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16000)
)
rmxCanNotEstablishConnectionWithApplicationServerAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotEstablishConnectionWithApplicationServerAlarmClear.setStatus(
        "current"
    )

rmxSystemConfigurationAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16001)
)
rmxSystemConfigurationAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemConfigurationAlarmClear.setStatus(
        "current"
    )

rmxExternalDbCertificateErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16002)
)
rmxExternalDbCertificateErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExternalDbCertificateErrorAlarmClear.setStatus(
        "current"
    )

rmxIvrServiceListMissingDefaultServiceAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16050)
)
rmxIvrServiceListMissingDefaultServiceAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxIvrServiceListMissingDefaultServiceAlarmClear.setStatus(
        "current"
    )

rmxCanNotCreateDefaultProfileAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16051)
)
rmxCanNotCreateDefaultProfileAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxCanNotCreateDefaultProfileAlarmClear.setStatus(
        "current"
    )

rmxNoReadMrDbReqRecievedFromRsrcAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16052)
)
rmxNoReadMrDbReqRecievedFromRsrcAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxNoReadMrDbReqRecievedFromRsrcAlarmClear.setStatus(
        "current"
    )

rmxFailedToConnectRecordingLinkAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16053)
)
rmxFailedToConnectRecordingLinkAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxFailedToConnectRecordingLinkAlarmClear.setStatus(
        "current"
    )

rmxRecordingLinkDisconnecedUnexpectedlyAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16054)
)
rmxRecordingLinkDisconnecedUnexpectedlyAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRecordingLinkDisconnecedUnexpectedlyAlarmClear.setStatus(
        "current"
    )

rmxSystemBasedModeNotIntializedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16055)
)
rmxSystemBasedModeNotIntializedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSystemBasedModeNotIntializedAlarmClear.setStatus(
        "current"
    )

rmxConfEncryptionErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16056)
)
rmxConfEncryptionErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxConfEncryptionErrorAlarmClear.setStatus(
        "current"
    )

rmxSnmpAgentInitFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16100)
)
rmxSnmpAgentInitFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxSnmpAgentInitFailedAlarmClear.setStatus(
        "current"
    )

rmxRestoreSucceededAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16200)
)
rmxRestoreSucceededAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoreSucceededAlarmClear.setStatus(
        "current"
    )

rmxRestoreFailedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 16201)
)
rmxRestoreFailedAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxRestoreFailedAlarmClear.setStatus(
        "current"
    )

rmxEncryptionServerErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 17010)
)
rmxEncryptionServerErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxEncryptionServerErrorAlarmClear.setStatus(
        "current"
    )

rmxExchangeServerConnectionErrorAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 13885, 9, 1, 1, 2, 2, 0, 17050)
)
rmxExchangeServerConnectionErrorAlarmClear.setObjects(
      *(("POLYCOM-RMX-MIB", "rmxAlarmDescription"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmDateAndTime"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmIndex"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmListName"),
        ("POLYCOM-RMX-MIB", "rmxActiveAlarmRmxStatus"))
)
if mibBuilder.loadTexts:
    rmxExchangeServerConnectionErrorAlarmClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLYCOM-RMX-MIB",
    **{"RmxStatus": RmxStatus,
       "polycom": polycom,
       "nsdProducts": nsdProducts,
       "rmx": rmx,
       "rmxMib1": rmxMib1,
       "rmxMib1General": rmxMib1General,
       "rmxCurrentStatus": rmxCurrentStatus,
       "rmxMib1Events": rmxMib1Events,
       "rmxMib1EventsParams": rmxMib1EventsParams,
       "rmxAlarmDescription": rmxAlarmDescription,
       "rmxActiveAlarmDateAndTime": rmxActiveAlarmDateAndTime,
       "rmxActiveAlarmIndex": rmxActiveAlarmIndex,
       "rmxActiveAlarmListName": rmxActiveAlarmListName,
       "rmxActiveAlarmRmxStatus": rmxActiveAlarmRmxStatus,
       "rmxNotify": rmxNotify,
       "rmxTraps": rmxTraps,
       "rmxNoLicensingAlarmFault": rmxNoLicensingAlarmFault,
       "rmxNoMeetingRoomAlarmFault": rmxNoMeetingRoomAlarmFault,
       "rmxNoIpServiceParamsAlarmFault": rmxNoIpServiceParamsAlarmFault,
       "rmxTaskTerminatedAlarmFault": rmxTaskTerminatedAlarmFault,
       "rmxCfgChangedAlarmFault": rmxCfgChangedAlarmFault,
       "rmxCfgInvalidAlarmFault": rmxCfgInvalidAlarmFault,
       "rmxDebugModeAlarmFault": rmxDebugModeAlarmFault,
       "rmxLowProcessMemoryAlertAlarmFault": rmxLowProcessMemoryAlertAlarmFault,
       "rmxLowSystemMemoryAlertAlarmFault": rmxLowSystemMemoryAlertAlarmFault,
       "rmxSystemCpuUsageAlertAlarmFault": rmxSystemCpuUsageAlertAlarmFault,
       "rmxTestErrorAlarmFault": rmxTestErrorAlarmFault,
       "rmxSipSecuredCommunicationFailedAlarmFault": rmxSipSecuredCommunicationFailedAlarmFault,
       "rmxBadFileAlarmFault": rmxBadFileAlarmFault,
       "rmxHighCpuUsageProcessAlertAlarmFault": rmxHighCpuUsageProcessAlertAlarmFault,
       "rmxIdleDeadlineReachedAlarmFault": rmxIdleDeadlineReachedAlarmFault,
       "rmxStartupConditionConfigurationAlarmFault": rmxStartupConditionConfigurationAlarmFault,
       "rmxRestoringDefaultFactoryAlarmFault": rmxRestoringDefaultFactoryAlarmFault,
       "rmxIpVersionChangedAlarmFault": rmxIpVersionChangedAlarmFault,
       "rmxNoServiceFoundInDbAlarmFault": rmxNoServiceFoundInDbAlarmFault,
       "rmxNoConnectionWithCsAlarmFault": rmxNoConnectionWithCsAlarmFault,
       "rmxCsComponentFatalAlarmFault": rmxCsComponentFatalAlarmFault,
       "rmxCsNotConfiguredAlarmFault": rmxCsNotConfiguredAlarmFault,
       "rmxCsServiceStateFailAlarmFault": rmxCsServiceStateFailAlarmFault,
       "rmxCsStartupFailedAlarmFault": rmxCsStartupFailedAlarmFault,
       "rmxDuplicateIpCsMngmntAlarmFault": rmxDuplicateIpCsMngmntAlarmFault,
       "rmxIpServiceDeletedAlarmFault": rmxIpServiceDeletedAlarmFault,
       "rmxIpServiceChangedAlarmFault": rmxIpServiceChangedAlarmFault,
       "rmxCsRecoveryStatusAlarmFault": rmxCsRecoveryStatusAlarmFault,
       "rmxExternalAlertCsAlarmFault": rmxExternalAlertCsAlarmFault,
       "rmxProductActivationFailureAlarmFault": rmxProductActivationFailureAlarmFault,
       "rmxNoManagementIpInterfaceAlarmFault": rmxNoManagementIpInterfaceAlarmFault,
       "rmxNoTimeConfigurationAlarmFault": rmxNoTimeConfigurationAlarmFault,
       "rmxMplStartupFailureAuthenticationNotReceivedAlarmFault": rmxMplStartupFailureAuthenticationNotReceivedAlarmFault,
       "rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmFault": rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmFault,
       "rmxNoDnsConfigurationAlarmFault": rmxNoDnsConfigurationAlarmFault,
       "rmxDnsRegistraionFailedAlarmFault": rmxDnsRegistraionFailedAlarmFault,
       "rmxFailedToOpenApacheConfigurationFileAlarmFault": rmxFailedToOpenApacheConfigurationFileAlarmFault,
       "rmxFailedToSaveApacheConfigurationFileAlarmFault": rmxFailedToSaveApacheConfigurationFileAlarmFault,
       "rmxPatchedVersionAlarmFault": rmxPatchedVersionAlarmFault,
       "rmxPrivateVersionAlarmFault": rmxPrivateVersionAlarmFault,
       "rmxNtpSyncFailureAlarmFault": rmxNtpSyncFailureAlarmFault,
       "rmxIllegalTimeAlarmFault": rmxIllegalTimeAlarmFault,
       "rmxExternalNtpServersFailureAlarmFault": rmxExternalNtpServersFailureAlarmFault,
       "rmxRunningVersionMismatchesCurrentVersionAlarmFault": rmxRunningVersionMismatchesCurrentVersionAlarmFault,
       "rmxIdeNotInDmaModeAlarmFault": rmxIdeNotInDmaModeAlarmFault,
       "rmxBadEthernetSettingsAlarmFault": rmxBadEthernetSettingsAlarmFault,
       "rmxSmartReportErrorsOnHdAlarmFault": rmxSmartReportErrorsOnHdAlarmFault,
       "rmxIllegalMcuVersionAlarmFault": rmxIllegalMcuVersionAlarmFault,
       "rmxDebugCfgExistAlarmFault": rmxDebugCfgExistAlarmFault,
       "rmxInstallingNewVersionAlarmFault": rmxInstallingNewVersionAlarmFault,
       "rmxSshEnabledAlarmFault": rmxSshEnabledAlarmFault,
       "rmxFailedToValidateCertificateAlarmFault": rmxFailedToValidateCertificateAlarmFault,
       "rmxCertificateExpiredAlarmFault": rmxCertificateExpiredAlarmFault,
       "rmxCertificateCommonNameErrorAlarmFault": rmxCertificateCommonNameErrorAlarmFault,
       "rmxCertificateNotValidYetAlarmFault": rmxCertificateNotValidYetAlarmFault,
       "rmxCertificateGoingToBeExpiredAlarmFault": rmxCertificateGoingToBeExpiredAlarmFault,
       "rmxProductTypeMismatchAlarmFault": rmxProductTypeMismatchAlarmFault,
       "rmxUnknownCpuSlotIdAlarmFault": rmxUnknownCpuSlotIdAlarmFault,
       "rmxNoFipsTestResultFromEncryptionkeyserverAlarmFault": rmxNoFipsTestResultFromEncryptionkeyserverAlarmFault,
       "rmxFipsFailureWithinEncryptionkeyserverAlarmFault": rmxFipsFailureWithinEncryptionkeyserverAlarmFault,
       "rmxHttpsDisabledInJitcAlarmFault": rmxHttpsDisabledInJitcAlarmFault,
       "rmxBackupOfCdrFilesIsRequiredAlarmFault": rmxBackupOfCdrFilesIsRequiredAlarmFault,
       "rmxNoMusicSourceAlarmFault": rmxNoMusicSourceAlarmFault,
       "rmxSwitchNotLoadedAlarmFault": rmxSwitchNotLoadedAlarmFault,
       "rmxNoIsdnServiceParamsAlarmFault": rmxNoIsdnServiceParamsAlarmFault,
       "rmxModuleDoesNotExistAlarmFault": rmxModuleDoesNotExistAlarmFault,
       "rmxNoDefaultIsdnServiceAlarmFault": rmxNoDefaultIsdnServiceAlarmFault,
       "rmxExternalAlertEmbAlarmFault": rmxExternalAlertEmbAlarmFault,
       "rmxVersionInstallProgressAlarmFault": rmxVersionInstallProgressAlarmFault,
       "rmxVersionIpmcInstallProgressAlarmFault": rmxVersionIpmcInstallProgressAlarmFault,
       "rmxVoltageProblemAlarmFault": rmxVoltageProblemAlarmFault,
       "rmxTemperatureMajorProblemAlarmFault": rmxTemperatureMajorProblemAlarmFault,
       "rmxTemperatureCriticalProblemAlarmFault": rmxTemperatureCriticalProblemAlarmFault,
       "rmxFailureProblemAlarmFault": rmxFailureProblemAlarmFault,
       "rmxPowerOffProblemAlarmFault": rmxPowerOffProblemAlarmFault,
       "rmxOtherProblemAlarmFault": rmxOtherProblemAlarmFault,
       "rmxNoConnectionWithCardAlarmFault": rmxNoConnectionWithCardAlarmFault,
       "rmxUnitNotRespondingAlarmFault": rmxUnitNotRespondingAlarmFault,
       "rmxMediaIpConfigurationFailureAlarmFault": rmxMediaIpConfigurationFailureAlarmFault,
       "rmxCardFolderMountingFailedAlarmFault": rmxCardFolderMountingFailedAlarmFault,
       "rmxCardStartupFailureAlarmFault": rmxCardStartupFailureAlarmFault,
       "rmxRtmIsdnStartupFailureAlarmFault": rmxRtmIsdnStartupFailureAlarmFault,
       "rmxRtmIsdnStartupProblemAlarmFault": rmxRtmIsdnStartupProblemAlarmFault,
       "rmxNoConnectionWithRtmIsdnAlarmFault": rmxNoConnectionWithRtmIsdnAlarmFault,
       "rmxRedAlarmAlarmFault": rmxRedAlarmAlarmFault,
       "rmxYellowAlarmAlarmFault": rmxYellowAlarmAlarmFault,
       "rmxDChannelNotEstablishedAlarmFault": rmxDChannelNotEstablishedAlarmFault,
       "rmxCardsConfigEventAlarmFault": rmxCardsConfigEventAlarmFault,
       "rmxCardsWrongFileModeAlarmFault": rmxCardsWrongFileModeAlarmFault,
       "rmxCardsFlashAccessProblemAlarmFault": rmxCardsFlashAccessProblemAlarmFault,
       "rmxRtmLanOrIsdnMissingAlarmFault": rmxRtmLanOrIsdnMissingAlarmFault,
       "rmxNoLanConnectionAlarmFault": rmxNoLanConnectionAlarmFault,
       "rmxCanNotEstablishConnectionWithSipRegistrarAlarmFault": rmxCanNotEstablishConnectionWithSipRegistrarAlarmFault,
       "rmxSipRegistrationLimitReachedAlarmFault": rmxSipRegistrationLimitReachedAlarmFault,
       "rmxFailedToAccessDnsServerAlarmFault": rmxFailedToAccessDnsServerAlarmFault,
       "rmxNoIndDnsSuccessAlarmFault": rmxNoIndDnsSuccessAlarmFault,
       "rmxFailedToInitFileSystemAlarmFault": rmxFailedToInitFileSystemAlarmFault,
       "rmxBadFileSystemAlarmFault": rmxBadFileSystemAlarmFault,
       "rmxBadHardDiskAlarmFault": rmxBadHardDiskAlarmFault,
       "rmxBackupOfLogFilesIsRequiredAlarmFault": rmxBackupOfLogFilesIsRequiredAlarmFault,
       "rmxBackupOfAuditFilesIsRequiredAlarmFault": rmxBackupOfAuditFilesIsRequiredAlarmFault,
       "rmxFailedToFillActionRedirectionAlarmFault": rmxFailedToFillActionRedirectionAlarmFault,
       "rmxFailedConfigUserListInLinuxAlarmFault": rmxFailedConfigUserListInLinuxAlarmFault,
       "rmxInsufficientResourcesAlarmFault": rmxInsufficientResourcesAlarmFault,
       "rmxPortConfigurationChangedAlarmFault": rmxPortConfigurationChangedAlarmFault,
       "rmxNoUtilizableUnitForAudioControllerAlarmFault": rmxNoUtilizableUnitForAudioControllerAlarmFault,
       "rmxAllocationModeChangedAlarmFault": rmxAllocationModeChangedAlarmFault,
       "rmxProcessTerminatedAlarmFault": rmxProcessTerminatedAlarmFault,
       "rmxResetMcuByTerminalAlarmFault": rmxResetMcuByTerminalAlarmFault,
       "rmxResetMcuByOperatorAlarmFault": rmxResetMcuByOperatorAlarmFault,
       "rmxResetMcuInternalAlarmFault": rmxResetMcuInternalAlarmFault,
       "rmxResetMcuAlarmFault": rmxResetMcuAlarmFault,
       "rmxResetMcuDiagnosticsAlarmFault": rmxResetMcuDiagnosticsAlarmFault,
       "rmxProcessStartupFailedAlarmFault": rmxProcessStartupFailedAlarmFault,
       "rmxSystemInSafeModeAlarmFault": rmxSystemInSafeModeAlarmFault,
       "rmxGuiSystemConfigIsIllegalAlarmFault": rmxGuiSystemConfigIsIllegalAlarmFault,
       "rmxFileSystemFailedToScanAlarmFault": rmxFileSystemFailedToScanAlarmFault,
       "rmxFileSystemOverflowAlarmFault": rmxFileSystemOverflowAlarmFault,
       "rmxHardDiskFailureAlarmFault": rmxHardDiskFailureAlarmFault,
       "rmxCpuIpcmSoftwareIsNotUpdatedAlarmFault": rmxCpuIpcmSoftwareIsNotUpdatedAlarmFault,
       "rmxNewVersionInstalledAlarmFault": rmxNewVersionInstalledAlarmFault,
       "rmxNewActivationKeyLoadedAlarmFault": rmxNewActivationKeyLoadedAlarmFault,
       "rmxInsufficientUdpPortsAlarmFault": rmxInsufficientUdpPortsAlarmFault,
       "rmxUsersListCorruptedAlarmFault": rmxUsersListCorruptedAlarmFault,
       "rmxDefaultUserExistsAlarmFault": rmxDefaultUserExistsAlarmFault,
       "rmxSupportOperatorIllegalInFederalModeAlarmFault": rmxSupportOperatorIllegalInFederalModeAlarmFault,
       "rmxIsdnServicesConfigurationChangedAlarmFault": rmxIsdnServicesConfigurationChangedAlarmFault,
       "rmxNoIsdnPstnLicensingAlarmFault": rmxNoIsdnPstnLicensingAlarmFault,
       "rmxNoRtmIsdnCardAlarmFault": rmxNoRtmIsdnCardAlarmFault,
       "rmxNoClockSourceAlarmFault": rmxNoClockSourceAlarmFault,
       "rmxSingleClockSourceAlarmFault": rmxSingleClockSourceAlarmFault,
       "rmxGkmngrAvfWrongMcuConfigAlarmFault": rmxGkmngrAvfWrongMcuConfigAlarmFault,
       "rmxGateKeeperErrorAlarmFault": rmxGateKeeperErrorAlarmFault,
       "rmxCanNotEstablishConnectionWithApplicationServerAlarmFault": rmxCanNotEstablishConnectionWithApplicationServerAlarmFault,
       "rmxSystemConfigurationAlarmFault": rmxSystemConfigurationAlarmFault,
       "rmxExternalDbCertificateErrorAlarmFault": rmxExternalDbCertificateErrorAlarmFault,
       "rmxIvrServiceListMissingDefaultServiceAlarmFault": rmxIvrServiceListMissingDefaultServiceAlarmFault,
       "rmxCanNotCreateDefaultProfileAlarmFault": rmxCanNotCreateDefaultProfileAlarmFault,
       "rmxNoReadMrDbReqRecievedFromRsrcAlarmFault": rmxNoReadMrDbReqRecievedFromRsrcAlarmFault,
       "rmxFailedToConnectRecordingLinkAlarmFault": rmxFailedToConnectRecordingLinkAlarmFault,
       "rmxRecordingLinkDisconnecedUnexpectedlyAlarmFault": rmxRecordingLinkDisconnecedUnexpectedlyAlarmFault,
       "rmxSystemBasedModeNotIntializedAlarmFault": rmxSystemBasedModeNotIntializedAlarmFault,
       "rmxConfEncryptionErrorAlarmFault": rmxConfEncryptionErrorAlarmFault,
       "rmxSnmpAgentInitFailedAlarmFault": rmxSnmpAgentInitFailedAlarmFault,
       "rmxRestoreSucceededAlarmFault": rmxRestoreSucceededAlarmFault,
       "rmxRestoreFailedAlarmFault": rmxRestoreFailedAlarmFault,
       "rmxEncryptionServerErrorAlarmFault": rmxEncryptionServerErrorAlarmFault,
       "rmxExchangeServerConnectionErrorAlarmFault": rmxExchangeServerConnectionErrorAlarmFault,
       "rmxNoLicensingAlarmClear": rmxNoLicensingAlarmClear,
       "rmxNoMeetingRoomAlarmClear": rmxNoMeetingRoomAlarmClear,
       "rmxNoIpServiceParamsAlarmClear": rmxNoIpServiceParamsAlarmClear,
       "rmxTaskTerminatedAlarmClear": rmxTaskTerminatedAlarmClear,
       "rmxCfgChangedAlarmClear": rmxCfgChangedAlarmClear,
       "rmxCfgInvalidAlarmClear": rmxCfgInvalidAlarmClear,
       "rmxDebugModeAlarmClear": rmxDebugModeAlarmClear,
       "rmxLowProcessMemoryAlertAlarmClear": rmxLowProcessMemoryAlertAlarmClear,
       "rmxLowSystemMemoryAlertAlarmClear": rmxLowSystemMemoryAlertAlarmClear,
       "rmxSystemCpuUsageAlertAlarmClear": rmxSystemCpuUsageAlertAlarmClear,
       "rmxTestErrorAlarmClear": rmxTestErrorAlarmClear,
       "rmxSipSecuredCommunicationFailedAlarmClear": rmxSipSecuredCommunicationFailedAlarmClear,
       "rmxBadFileAlarmClear": rmxBadFileAlarmClear,
       "rmxHighCpuUsageProcessAlertAlarmClear": rmxHighCpuUsageProcessAlertAlarmClear,
       "rmxIdleDeadlineReachedAlarmClear": rmxIdleDeadlineReachedAlarmClear,
       "rmxStartupConditionConfigurationAlarmClear": rmxStartupConditionConfigurationAlarmClear,
       "rmxRestoringDefaultFactoryAlarmClear": rmxRestoringDefaultFactoryAlarmClear,
       "rmxIpVersionChangedAlarmClear": rmxIpVersionChangedAlarmClear,
       "rmxNoServiceFoundInDbAlarmClear": rmxNoServiceFoundInDbAlarmClear,
       "rmxNoConnectionWithCsAlarmClear": rmxNoConnectionWithCsAlarmClear,
       "rmxCsComponentFatalAlarmClear": rmxCsComponentFatalAlarmClear,
       "rmxCsNotConfiguredAlarmClear": rmxCsNotConfiguredAlarmClear,
       "rmxCsServiceStateFailAlarmClear": rmxCsServiceStateFailAlarmClear,
       "rmxCsStartupFailedAlarmClear": rmxCsStartupFailedAlarmClear,
       "rmxDuplicateIpCsMngmntAlarmClear": rmxDuplicateIpCsMngmntAlarmClear,
       "rmxIpServiceDeletedAlarmClear": rmxIpServiceDeletedAlarmClear,
       "rmxIpServiceChangedAlarmClear": rmxIpServiceChangedAlarmClear,
       "rmxCsRecoveryStatusAlarmClear": rmxCsRecoveryStatusAlarmClear,
       "rmxExternalAlertCsAlarmClear": rmxExternalAlertCsAlarmClear,
       "rmxProductActivationFailureAlarmClear": rmxProductActivationFailureAlarmClear,
       "rmxNoManagementIpInterfaceAlarmClear": rmxNoManagementIpInterfaceAlarmClear,
       "rmxNoTimeConfigurationAlarmClear": rmxNoTimeConfigurationAlarmClear,
       "rmxMplStartupFailureAuthenticationNotReceivedAlarmClear": rmxMplStartupFailureAuthenticationNotReceivedAlarmClear,
       "rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmClear": rmxMplStartupFailureMngmntIpCnfgNotReceivedAlarmClear,
       "rmxNoDnsConfigurationAlarmClear": rmxNoDnsConfigurationAlarmClear,
       "rmxDnsRegistraionFailedAlarmClear": rmxDnsRegistraionFailedAlarmClear,
       "rmxFailedToOpenApacheConfigurationFileAlarmClear": rmxFailedToOpenApacheConfigurationFileAlarmClear,
       "rmxFailedToSaveApacheConfigurationFileAlarmClear": rmxFailedToSaveApacheConfigurationFileAlarmClear,
       "rmxPatchedVersionAlarmClear": rmxPatchedVersionAlarmClear,
       "rmxPrivateVersionAlarmClear": rmxPrivateVersionAlarmClear,
       "rmxNtpSyncFailureAlarmClear": rmxNtpSyncFailureAlarmClear,
       "rmxIllegalTimeAlarmClear": rmxIllegalTimeAlarmClear,
       "rmxExternalNtpServersFailureAlarmClear": rmxExternalNtpServersFailureAlarmClear,
       "rmxRunningVersionMismatchesCurrentVersionAlarmClear": rmxRunningVersionMismatchesCurrentVersionAlarmClear,
       "rmxIdeNotInDmaModeAlarmClear": rmxIdeNotInDmaModeAlarmClear,
       "rmxBadEthernetSettingsAlarmClear": rmxBadEthernetSettingsAlarmClear,
       "rmxSmartReportErrorsOnHdAlarmClear": rmxSmartReportErrorsOnHdAlarmClear,
       "rmxIllegalMcuVersionAlarmClear": rmxIllegalMcuVersionAlarmClear,
       "rmxDebugCfgExistAlarmClear": rmxDebugCfgExistAlarmClear,
       "rmxInstallingNewVersionAlarmClear": rmxInstallingNewVersionAlarmClear,
       "rmxSshEnabledAlarmClear": rmxSshEnabledAlarmClear,
       "rmxFailedToValidateCertificateAlarmClear": rmxFailedToValidateCertificateAlarmClear,
       "rmxCertificateExpiredAlarmClear": rmxCertificateExpiredAlarmClear,
       "rmxCertificateCommonNameErrorAlarmClear": rmxCertificateCommonNameErrorAlarmClear,
       "rmxCertificateNotValidYetAlarmClear": rmxCertificateNotValidYetAlarmClear,
       "rmxCertificateGoingToBeExpiredAlarmClear": rmxCertificateGoingToBeExpiredAlarmClear,
       "rmxProductTypeMismatchAlarmClear": rmxProductTypeMismatchAlarmClear,
       "rmxUnknownCpuSlotIdAlarmClear": rmxUnknownCpuSlotIdAlarmClear,
       "rmxNoFipsTestResultFromEncryptionkeyserverAlarmClear": rmxNoFipsTestResultFromEncryptionkeyserverAlarmClear,
       "rmxFipsFailureWithinEncryptionkeyserverAlarmClear": rmxFipsFailureWithinEncryptionkeyserverAlarmClear,
       "rmxHttpsDisabledInJitcAlarmClear": rmxHttpsDisabledInJitcAlarmClear,
       "rmxBackupOfCdrFilesIsRequiredAlarmClear": rmxBackupOfCdrFilesIsRequiredAlarmClear,
       "rmxNoMusicSourceAlarmClear": rmxNoMusicSourceAlarmClear,
       "rmxSwitchNotLoadedAlarmClear": rmxSwitchNotLoadedAlarmClear,
       "rmxNoIsdnServiceParamsAlarmClear": rmxNoIsdnServiceParamsAlarmClear,
       "rmxModuleDoesNotExistAlarmClear": rmxModuleDoesNotExistAlarmClear,
       "rmxNoDefaultIsdnServiceAlarmClear": rmxNoDefaultIsdnServiceAlarmClear,
       "rmxExternalAlertEmbAlarmClear": rmxExternalAlertEmbAlarmClear,
       "rmxVersionInstallProgressAlarmClear": rmxVersionInstallProgressAlarmClear,
       "rmxVersionIpmcInstallProgressAlarmClear": rmxVersionIpmcInstallProgressAlarmClear,
       "rmxVoltageProblemAlarmClear": rmxVoltageProblemAlarmClear,
       "rmxTemperatureMajorProblemAlarmClear": rmxTemperatureMajorProblemAlarmClear,
       "rmxTemperatureCriticalProblemAlarmClear": rmxTemperatureCriticalProblemAlarmClear,
       "rmxFailureProblemAlarmClear": rmxFailureProblemAlarmClear,
       "rmxPowerOffProblemAlarmClear": rmxPowerOffProblemAlarmClear,
       "rmxOtherProblemAlarmClear": rmxOtherProblemAlarmClear,
       "rmxNoConnectionWithCardAlarmClear": rmxNoConnectionWithCardAlarmClear,
       "rmxUnitNotRespondingAlarmClear": rmxUnitNotRespondingAlarmClear,
       "rmxMediaIpConfigurationFailureAlarmClear": rmxMediaIpConfigurationFailureAlarmClear,
       "rmxCardFolderMountingFailedAlarmClear": rmxCardFolderMountingFailedAlarmClear,
       "rmxCardStartupFailureAlarmClear": rmxCardStartupFailureAlarmClear,
       "rmxRtmIsdnStartupFailureAlarmClear": rmxRtmIsdnStartupFailureAlarmClear,
       "rmxRtmIsdnStartupProblemAlarmClear": rmxRtmIsdnStartupProblemAlarmClear,
       "rmxNoConnectionWithRtmIsdnAlarmClear": rmxNoConnectionWithRtmIsdnAlarmClear,
       "rmxRedAlarmAlarmClear": rmxRedAlarmAlarmClear,
       "rmxYellowAlarmAlarmClear": rmxYellowAlarmAlarmClear,
       "rmxDChannelNotEstablishedAlarmClear": rmxDChannelNotEstablishedAlarmClear,
       "rmxCardsConfigEventAlarmClear": rmxCardsConfigEventAlarmClear,
       "rmxCardsWrongFileModeAlarmClear": rmxCardsWrongFileModeAlarmClear,
       "rmxCardsFlashAccessProblemAlarmClear": rmxCardsFlashAccessProblemAlarmClear,
       "rmxRtmLanOrIsdnMissingAlarmClear": rmxRtmLanOrIsdnMissingAlarmClear,
       "rmxNoLanConnectionAlarmClear": rmxNoLanConnectionAlarmClear,
       "rmxCanNotEstablishConnectionWithSipRegistrarAlarmClear": rmxCanNotEstablishConnectionWithSipRegistrarAlarmClear,
       "rmxSipRegistrationLimitReachedAlarmClear": rmxSipRegistrationLimitReachedAlarmClear,
       "rmxFailedToAccessDnsServerAlarmClear": rmxFailedToAccessDnsServerAlarmClear,
       "rmxNoIndDnsSuccessAlarmClear": rmxNoIndDnsSuccessAlarmClear,
       "rmxFailedToInitFileSystemAlarmClear": rmxFailedToInitFileSystemAlarmClear,
       "rmxBadFileSystemAlarmClear": rmxBadFileSystemAlarmClear,
       "rmxBadHardDiskAlarmClear": rmxBadHardDiskAlarmClear,
       "rmxBackupOfLogFilesIsRequiredAlarmClear": rmxBackupOfLogFilesIsRequiredAlarmClear,
       "rmxBackupOfAuditFilesIsRequiredAlarmClear": rmxBackupOfAuditFilesIsRequiredAlarmClear,
       "rmxFailedToFillActionRedirectionAlarmClear": rmxFailedToFillActionRedirectionAlarmClear,
       "rmxFailedConfigUserListInLinuxAlarmClear": rmxFailedConfigUserListInLinuxAlarmClear,
       "rmxInsufficientResourcesAlarmClear": rmxInsufficientResourcesAlarmClear,
       "rmxPortConfigurationChangedAlarmClear": rmxPortConfigurationChangedAlarmClear,
       "rmxNoUtilizableUnitForAudioControllerAlarmClear": rmxNoUtilizableUnitForAudioControllerAlarmClear,
       "rmxAllocationModeChangedAlarmClear": rmxAllocationModeChangedAlarmClear,
       "rmxProcessTerminatedAlarmClear": rmxProcessTerminatedAlarmClear,
       "rmxResetMcuByTerminalAlarmClear": rmxResetMcuByTerminalAlarmClear,
       "rmxResetMcuByOperatorAlarmClear": rmxResetMcuByOperatorAlarmClear,
       "rmxResetMcuInternalAlarmClear": rmxResetMcuInternalAlarmClear,
       "rmxResetMcuAlarmClear": rmxResetMcuAlarmClear,
       "rmxResetMcuDiagnosticsAlarmClear": rmxResetMcuDiagnosticsAlarmClear,
       "rmxProcessStartupFailedAlarmClear": rmxProcessStartupFailedAlarmClear,
       "rmxSystemInSafeModeAlarmClear": rmxSystemInSafeModeAlarmClear,
       "rmxGuiSystemConfigIsIllegalAlarmClear": rmxGuiSystemConfigIsIllegalAlarmClear,
       "rmxFileSystemFailedToScanAlarmClear": rmxFileSystemFailedToScanAlarmClear,
       "rmxFileSystemOverflowAlarmClear": rmxFileSystemOverflowAlarmClear,
       "rmxHardDiskFailureAlarmClear": rmxHardDiskFailureAlarmClear,
       "rmxCpuIpcmSoftwareIsNotUpdatedAlarmClear": rmxCpuIpcmSoftwareIsNotUpdatedAlarmClear,
       "rmxNewVersionInstalledAlarmClear": rmxNewVersionInstalledAlarmClear,
       "rmxNewActivationKeyLoadedAlarmClear": rmxNewActivationKeyLoadedAlarmClear,
       "rmxInsufficientUdpPortsAlarmClear": rmxInsufficientUdpPortsAlarmClear,
       "rmxUsersListCorruptedAlarmClear": rmxUsersListCorruptedAlarmClear,
       "rmxDefaultUserExistsAlarmClear": rmxDefaultUserExistsAlarmClear,
       "rmxSupportOperatorIllegalInFederalModeAlarmClear": rmxSupportOperatorIllegalInFederalModeAlarmClear,
       "rmxIsdnServicesConfigurationChangedAlarmClear": rmxIsdnServicesConfigurationChangedAlarmClear,
       "rmxNoIsdnPstnLicensingAlarmClear": rmxNoIsdnPstnLicensingAlarmClear,
       "rmxNoRtmIsdnCardAlarmClear": rmxNoRtmIsdnCardAlarmClear,
       "rmxNoClockSourceAlarmClear": rmxNoClockSourceAlarmClear,
       "rmxSingleClockSourceAlarmClear": rmxSingleClockSourceAlarmClear,
       "rmxGkmngrAvfWrongMcuConfigAlarmClear": rmxGkmngrAvfWrongMcuConfigAlarmClear,
       "rmxGateKeeperErrorAlarmClear": rmxGateKeeperErrorAlarmClear,
       "rmxCanNotEstablishConnectionWithApplicationServerAlarmClear": rmxCanNotEstablishConnectionWithApplicationServerAlarmClear,
       "rmxSystemConfigurationAlarmClear": rmxSystemConfigurationAlarmClear,
       "rmxExternalDbCertificateErrorAlarmClear": rmxExternalDbCertificateErrorAlarmClear,
       "rmxIvrServiceListMissingDefaultServiceAlarmClear": rmxIvrServiceListMissingDefaultServiceAlarmClear,
       "rmxCanNotCreateDefaultProfileAlarmClear": rmxCanNotCreateDefaultProfileAlarmClear,
       "rmxNoReadMrDbReqRecievedFromRsrcAlarmClear": rmxNoReadMrDbReqRecievedFromRsrcAlarmClear,
       "rmxFailedToConnectRecordingLinkAlarmClear": rmxFailedToConnectRecordingLinkAlarmClear,
       "rmxRecordingLinkDisconnecedUnexpectedlyAlarmClear": rmxRecordingLinkDisconnecedUnexpectedlyAlarmClear,
       "rmxSystemBasedModeNotIntializedAlarmClear": rmxSystemBasedModeNotIntializedAlarmClear,
       "rmxConfEncryptionErrorAlarmClear": rmxConfEncryptionErrorAlarmClear,
       "rmxSnmpAgentInitFailedAlarmClear": rmxSnmpAgentInitFailedAlarmClear,
       "rmxRestoreSucceededAlarmClear": rmxRestoreSucceededAlarmClear,
       "rmxRestoreFailedAlarmClear": rmxRestoreFailedAlarmClear,
       "rmxEncryptionServerErrorAlarmClear": rmxEncryptionServerErrorAlarmClear,
       "rmxExchangeServerConnectionErrorAlarmClear": rmxExchangeServerConnectionErrorAlarmClear,
       "rmxProducts": rmxProducts,
       "rmx2000": rmx2000,
       "rmx4000": rmx4000}
)
