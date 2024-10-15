# SNMP MIB module (PRETUPS-MIB-new) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PRETUPS-MIB-new
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:40 2024
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

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

btsl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19338)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SubAgent_ObjectIdentity = ObjectIdentity
subAgent = _SubAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 1)
)
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4)
)
_Stdvars1_ObjectIdentity = ObjectIdentity
stdvars1 = _Stdvars1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0)
)
_ManagedObject_Type = OctetString
_ManagedObject_Object = MibScalar
managedObject = _ManagedObject_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 0),
    _ManagedObject_Type()
)
managedObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managedObject.setStatus("current")
_AlarmType_Type = OctetString
_AlarmType_Object = MibScalar
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 1),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")
_AlarmSeverity_Type = OctetString
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 2),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_SpecificProblem_Type = OctetString
_SpecificProblem_Object = MibScalar
specificProblem = _SpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 3),
    _SpecificProblem_Type()
)
specificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificProblem.setStatus("current")
_AlarmId_Type = OctetString
_AlarmId_Object = MibScalar
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 4),
    _AlarmId_Type()
)
alarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmClass_Type = OctetString
_AlarmClass_Object = MibScalar
alarmClass = _AlarmClass_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 5),
    _AlarmClass_Type()
)
alarmClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClass.setStatus("current")
_ProblableCause_Type = OctetString
_ProblableCause_Object = MibScalar
problableCause = _ProblableCause_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 6),
    _ProblableCause_Type()
)
problableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    problableCause.setStatus("current")
_AlarmSpecificProblem_Type = OctetString
_AlarmSpecificProblem_Object = MibScalar
alarmSpecificProblem = _AlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 19338, 1, 4, 0, 7),
    _AlarmSpecificProblem_Type()
)
alarmSpecificProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSpecificProblem.setStatus("current")
_Pretups_ObjectIdentity = ObjectIdentity
pretups = _Pretups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9)
)
_UrlMonitoring_ObjectIdentity = ObjectIdentity
urlMonitoring = _UrlMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 1)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 1, 1)
)
_Oam_ObjectIdentity = ObjectIdentity
oam = _Oam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 1, 1, 6)
)
_Pretupsnotification_ObjectIdentity = ObjectIdentity
pretupsnotification = _Pretupsnotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2)
)
_Pretupsnotification1_ObjectIdentity = ObjectIdentity
pretupsnotification1 = _Pretupsnotification1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0)
)
_Database_ObjectIdentity = ObjectIdentity
database = _Database_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 1)
)
_Systemerrorerror_ObjectIdentity = ObjectIdentity
systemerrorerror = _Systemerrorerror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 2)
)
_Systeminfo_ObjectIdentity = ObjectIdentity
systeminfo = _Systeminfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 3)
)
_Interfaceinvaliedresponse_ObjectIdentity = ObjectIdentity
interfaceinvaliedresponse = _Interfaceinvaliedresponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 4)
)
_Retry_ObjectIdentity = ObjectIdentity
retry = _Retry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 5)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 6)
)
_Interfaceresponse_ObjectIdentity = ObjectIdentity
interfaceresponse = _Interfaceresponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 7)
)
_Adminopt_ObjectIdentity = ObjectIdentity
adminopt = _Adminopt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 8)
)

# Managed Objects groups


# Notification objects

loadBlancer1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 1, 1, 6, 0)
)
if mibBuilder.loadTexts:
    loadBlancer1.setStatus(
        "current"
    )

loadBlancer2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    loadBlancer2.setStatus(
        "current"
    )

databasedown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 1, 0)
)
if mibBuilder.loadTexts:
    databasedown.setStatus(
        "current"
    )

databaseup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 1, 1)
)
if mibBuilder.loadTexts:
    databaseup.setStatus(
        "current"
    )

systemerrorerrordown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 2, 0)
)
if mibBuilder.loadTexts:
    systemerrorerrordown.setStatus(
        "current"
    )

systemerrorerrorup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 2, 1)
)
if mibBuilder.loadTexts:
    systemerrorerrorup.setStatus(
        "current"
    )

systeminfodown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 3, 0)
)
if mibBuilder.loadTexts:
    systeminfodown.setStatus(
        "current"
    )

systeminfoup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 3, 1)
)
if mibBuilder.loadTexts:
    systeminfoup.setStatus(
        "current"
    )

interfaceinvaliedresponsedown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 4, 0)
)
if mibBuilder.loadTexts:
    interfaceinvaliedresponsedown.setStatus(
        "current"
    )

interfaceinvaliedresponseup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 4, 1)
)
if mibBuilder.loadTexts:
    interfaceinvaliedresponseup.setStatus(
        "current"
    )

retrydown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 5, 0)
)
if mibBuilder.loadTexts:
    retrydown.setStatus(
        "current"
    )

retryup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 5, 1)
)
if mibBuilder.loadTexts:
    retryup.setStatus(
        "current"
    )

interfacedown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 6, 0)
)
if mibBuilder.loadTexts:
    interfacedown.setStatus(
        "current"
    )

interfaceup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 6, 1)
)
if mibBuilder.loadTexts:
    interfaceup.setStatus(
        "current"
    )

interfaceresponsedown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 7, 0)
)
if mibBuilder.loadTexts:
    interfaceresponsedown.setStatus(
        "current"
    )

interfaceresponseup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 7, 1)
)
if mibBuilder.loadTexts:
    interfaceresponseup.setStatus(
        "current"
    )

adminoptdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 8, 0)
)
if mibBuilder.loadTexts:
    adminoptdown.setStatus(
        "current"
    )

adminoptup = NotificationType(
    (1, 3, 6, 1, 4, 1, 19338, 9, 2, 0, 8, 1)
)
if mibBuilder.loadTexts:
    adminoptup.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRETUPS-MIB-new",
    **{"btsl": btsl,
       "subAgent": subAgent,
       "alarms": alarms,
       "stdvars1": stdvars1,
       "managedObject": managedObject,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "specificProblem": specificProblem,
       "alarmId": alarmId,
       "alarmClass": alarmClass,
       "problableCause": problableCause,
       "alarmSpecificProblem": alarmSpecificProblem,
       "pretups": pretups,
       "urlMonitoring": urlMonitoring,
       "alarm": alarm,
       "oam": oam,
       "loadBlancer1": loadBlancer1,
       "loadBlancer2": loadBlancer2,
       "pretupsnotification": pretupsnotification,
       "pretupsnotification1": pretupsnotification1,
       "database": database,
       "databasedown": databasedown,
       "databaseup": databaseup,
       "systemerrorerror": systemerrorerror,
       "systemerrorerrordown": systemerrorerrordown,
       "systemerrorerrorup": systemerrorerrorup,
       "systeminfo": systeminfo,
       "systeminfodown": systeminfodown,
       "systeminfoup": systeminfoup,
       "interfaceinvaliedresponse": interfaceinvaliedresponse,
       "interfaceinvaliedresponsedown": interfaceinvaliedresponsedown,
       "interfaceinvaliedresponseup": interfaceinvaliedresponseup,
       "retry": retry,
       "retrydown": retrydown,
       "retryup": retryup,
       "interface": interface,
       "interfacedown": interfacedown,
       "interfaceup": interfaceup,
       "interfaceresponse": interfaceresponse,
       "interfaceresponsedown": interfaceresponsedown,
       "interfaceresponseup": interfaceresponseup,
       "adminopt": adminopt,
       "adminoptdown": adminoptdown,
       "adminoptup": adminoptup}
)
