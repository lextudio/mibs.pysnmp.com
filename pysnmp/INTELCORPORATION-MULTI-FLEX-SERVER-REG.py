# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:05 2024
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

multiFlexServerRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 1)
)
multiFlexServerRegModule.setRevisions(
        ("2007-10-01 18:20",
         "2007-08-21 17:00",
         "2007-08-16 13:30",
         "2007-05-30 10:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-29 15:30",
         "2006-11-01 10:00",
         "2006-10-02 12:00",
         "2006-09-28 17:32")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Modularsystems_ObjectIdentity = ObjectIdentity
modularsystems = _Modularsystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19)
)
_MultiFlexServer_ObjectIdentity = ObjectIdentity
multiFlexServer = _MultiFlexServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1)
)
_Notifications_ObjectIdentity = ObjectIdentity
notifications = _Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 0)
)
if mibBuilder.loadTexts:
    notifications.setStatus("current")
_Registry_ObjectIdentity = ObjectIdentity
registry = _Registry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1)
)
_RegModule_ObjectIdentity = ObjectIdentity
regModule = _RegModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1)
)
_RegComponents_ObjectIdentity = ObjectIdentity
regComponents = _RegComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2)
)
_RegChassis_ObjectIdentity = ObjectIdentity
regChassis = _RegChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 1)
)
_MultiFlexServer1_ObjectIdentity = ObjectIdentity
multiFlexServer1 = _MultiFlexServer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    multiFlexServer1.setStatus("current")
_RegSwitches_ObjectIdentity = ObjectIdentity
regSwitches = _RegSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 2)
)
_Esm1_ObjectIdentity = ObjectIdentity
esm1 = _Esm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    esm1.setStatus("current")
_RegScms_ObjectIdentity = ObjectIdentity
regScms = _RegScms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 3)
)
_Scm1_ObjectIdentity = ObjectIdentity
scm1 = _Scm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    scm1.setStatus("current")
_RegBlades_ObjectIdentity = ObjectIdentity
regBlades = _RegBlades_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 4)
)
_RegPowerSupplies_ObjectIdentity = ObjectIdentity
regPowerSupplies = _RegPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 5)
)
_RegFans_ObjectIdentity = ObjectIdentity
regFans = _RegFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 2, 6)
)
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2)
)
_Mib_ObjectIdentity = ObjectIdentity
mib = _Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2)
)
_NotificationInfo_ObjectIdentity = ObjectIdentity
notificationInfo = _NotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3)
)
_Component_Type = DisplayString
_Component_Object = MibScalar
component = _Component_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 1),
    _Component_Type()
)
component.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    component.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("good", 2),
          ("info", 3),
          ("neutral", 1),
          ("unknown", 0),
          ("warning", 4))
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 2),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_EventType_Type = DisplayString
_EventType_Object = MibScalar
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_User_Type = DisplayString
_User_Object = MibScalar
user = _User_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 4),
    _User_Type()
)
user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user.setStatus("current")
_InstanceId_Type = DisplayString
_InstanceId_Object = MibScalar
instanceId = _InstanceId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 5),
    _InstanceId_Type()
)
instanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instanceId.setStatus("current")
_Detail_Type = DisplayString
_Detail_Object = MibScalar
detail = _Detail_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 6),
    _Detail_Type()
)
detail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    detail.setStatus("current")
_EventId_Type = Integer32
_EventId_Object = MibScalar
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 3, 7),
    _EventId_Type()
)
eventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventId.setStatus("current")

# Managed Objects groups

chassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 1)
)
chassisGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "component"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "severity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "user"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "instanceId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "detail"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventId"))
)
if mibBuilder.loadTexts:
    chassisGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    **{"intel": intel,
       "products": products,
       "modularsystems": modularsystems,
       "multiFlexServer": multiFlexServer,
       "notifications": notifications,
       "registry": registry,
       "regModule": regModule,
       "multiFlexServerRegModule": multiFlexServerRegModule,
       "regComponents": regComponents,
       "regChassis": regChassis,
       "multiFlexServer1": multiFlexServer1,
       "regSwitches": regSwitches,
       "esm1": esm1,
       "regScms": regScms,
       "scm1": scm1,
       "regBlades": regBlades,
       "regPowerSupplies": regPowerSupplies,
       "regFans": regFans,
       "components": components,
       "mib": mib,
       "groups": groups,
       "chassisGroup": chassisGroup,
       "notificationInfo": notificationInfo,
       "component": component,
       "severity": severity,
       "eventType": eventType,
       "user": user,
       "instanceId": instanceId,
       "detail": detail,
       "eventId": eventId}
)
