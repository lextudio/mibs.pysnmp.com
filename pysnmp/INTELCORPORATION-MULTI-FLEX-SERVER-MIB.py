# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-MIB
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

(component,
 components,
 detail,
 eventId,
 eventType,
 groups,
 instanceId,
 notifications,
 regModule,
 severity,
 user) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "component",
    "components",
    "detail",
    "eventId",
    "eventType",
    "groups",
    "instanceId",
    "notifications",
    "regModule",
    "severity",
    "user")

(IdromBinary16,
 Power) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "IdromBinary16",
    "Power")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 10)
)
multiFlexServerMibModule.setRevisions(
        ("2007-08-21 17:00",
         "2007-08-16 13:30",
         "2007-07-16 11:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-30 13:30",
         "2007-05-30 10:30",
         "2007-04-09 10:30",
         "2007-03-12 18:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-01 10:00",
         "2006-09-29 15:29",
         "2006-09-28 17:32",
         "2006-09-01 06:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10)
)
if mibBuilder.loadTexts:
    chassis.setStatus("current")
_ChassisVendor_Type = DisplayString
_ChassisVendor_Object = MibScalar
chassisVendor = _ChassisVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 1),
    _ChassisVendor_Type()
)
chassisVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisVendor.setStatus("current")
_ChassisMfgDate_Type = DisplayString
_ChassisMfgDate_Object = MibScalar
chassisMfgDate = _ChassisMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 2),
    _ChassisMfgDate_Type()
)
chassisMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMfgDate.setStatus("current")
_ChassisDeviceName_Type = DisplayString
_ChassisDeviceName_Object = MibScalar
chassisDeviceName = _ChassisDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 3),
    _ChassisDeviceName_Type()
)
chassisDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisDeviceName.setStatus("current")
_ChassisPart_Type = IdromBinary16
_ChassisPart_Object = MibScalar
chassisPart = _ChassisPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 4),
    _ChassisPart_Type()
)
chassisPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPart.setStatus("current")
_ChassisSerialNo_Type = IdromBinary16
_ChassisSerialNo_Object = MibScalar
chassisSerialNo = _ChassisSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 5),
    _ChassisSerialNo_Type()
)
chassisSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNo.setStatus("current")
_ChassisMaximumPower_Type = Power
_ChassisMaximumPower_Object = MibScalar
chassisMaximumPower = _ChassisMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 6),
    _ChassisMaximumPower_Type()
)
chassisMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMaximumPower.setStatus("current")
_ChassisNominalPower_Type = Power
_ChassisNominalPower_Object = MibScalar
chassisNominalPower = _ChassisNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 7),
    _ChassisNominalPower_Type()
)
chassisNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNominalPower.setStatus("current")
_ChassisAssetTag_Type = IdromBinary16
_ChassisAssetTag_Object = MibScalar
chassisAssetTag = _ChassisAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 8),
    _ChassisAssetTag_Type()
)
chassisAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisAssetTag.setStatus("current")

# Managed Objects groups

chassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 10)
)
chassisGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisAssetTag"))
)
if mibBuilder.loadTexts:
    chassisGroup.setStatus("current")


# Notification objects

genericChassisEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 0, 10)
)
genericChassisEvent.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "component"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "severity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "user"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "instanceId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "detail"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventId"))
)
if mibBuilder.loadTexts:
    genericChassisEvent.setStatus(
        "current"
    )


# Notifications groups

chassisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 110)
)
chassisNotificationGroup.setObjects(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "genericChassisEvent")
)
if mibBuilder.loadTexts:
    chassisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    **{"genericChassisEvent": genericChassisEvent,
       "multiFlexServerMibModule": multiFlexServerMibModule,
       "chassisGroup": chassisGroup,
       "chassisNotificationGroup": chassisNotificationGroup,
       "chassis": chassis,
       "chassisVendor": chassisVendor,
       "chassisMfgDate": chassisMfgDate,
       "chassisDeviceName": chassisDeviceName,
       "chassisPart": chassisPart,
       "chassisSerialNo": chassisSerialNo,
       "chassisMaximumPower": chassisMaximumPower,
       "chassisNominalPower": chassisNominalPower,
       "chassisAssetTag": chassisAssetTag}
)
