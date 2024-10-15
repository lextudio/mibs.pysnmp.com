# SNMP MIB module (MRV-IN-REACH-ALARM-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-ALARM-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:35 2024
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

(basicAlarmMasterInputManufacturer,
 basicAlarmMasterInputModel,
 basicAlarmMasterInputName,
 basicAlarmMasterInputPoint,
 basicAlarmMasterInputPort,
 basicAlarmMasterInputRelatedEquipment,
 basicAlarmMasterInputSiteId,
 basicAlarmMasterInputSlot,
 basicAlarmMasterInputStatus,
 basicAlarmMasterInputValue,
 basicAlarmMasterInputZone) = mibBuilder.importSymbols(
    "MRV-IN-REACH-CHARACTER-MIB",
    "basicAlarmMasterInputManufacturer",
    "basicAlarmMasterInputModel",
    "basicAlarmMasterInputName",
    "basicAlarmMasterInputPoint",
    "basicAlarmMasterInputPort",
    "basicAlarmMasterInputRelatedEquipment",
    "basicAlarmMasterInputSiteId",
    "basicAlarmMasterInputSlot",
    "basicAlarmMasterInputStatus",
    "basicAlarmMasterInputValue",
    "basicAlarmMasterInputZone")

(mrvInReachProductDivision,) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "mrvInReachProductDivision")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

_XAlarm_ObjectIdentity = ObjectIdentity
xAlarm = _XAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 49)
)

# Managed Objects groups


# Notification objects

alarmInputHighDensity0001Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30001)
)
alarmInputHighDensity0001Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0001Alarm.setStatus(
        ""
    )

alarmInputHighDensity0002Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30002)
)
alarmInputHighDensity0002Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0002Alarm.setStatus(
        ""
    )

alarmInputHighDensity0003Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30003)
)
alarmInputHighDensity0003Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0003Alarm.setStatus(
        ""
    )

alarmInputHighDensity0004Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30004)
)
alarmInputHighDensity0004Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0004Alarm.setStatus(
        ""
    )

alarmInputHighDensity0005Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30005)
)
alarmInputHighDensity0005Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0005Alarm.setStatus(
        ""
    )

alarmInputHighDensity0006Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30006)
)
alarmInputHighDensity0006Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0006Alarm.setStatus(
        ""
    )

alarmInputHighDensity0007Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30007)
)
alarmInputHighDensity0007Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0007Alarm.setStatus(
        ""
    )

alarmInputHighDensity0008Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30008)
)
alarmInputHighDensity0008Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0008Alarm.setStatus(
        ""
    )

alarmInputHighDensity0009Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30009)
)
alarmInputHighDensity0009Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0009Alarm.setStatus(
        ""
    )

alarmInputHighDensity0010Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30010)
)
alarmInputHighDensity0010Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0010Alarm.setStatus(
        ""
    )

alarmInputHighDensity0011Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30011)
)
alarmInputHighDensity0011Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0011Alarm.setStatus(
        ""
    )

alarmInputHighDensity0012Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30012)
)
alarmInputHighDensity0012Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0012Alarm.setStatus(
        ""
    )

alarmInputHighDensity0013Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30013)
)
alarmInputHighDensity0013Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0013Alarm.setStatus(
        ""
    )

alarmInputHighDensity0014Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30014)
)
alarmInputHighDensity0014Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0014Alarm.setStatus(
        ""
    )

alarmInputHighDensity0015Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30015)
)
alarmInputHighDensity0015Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0015Alarm.setStatus(
        ""
    )

alarmInputHighDensity0016Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30016)
)
alarmInputHighDensity0016Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0016Alarm.setStatus(
        ""
    )

alarmInputHighDensity0017Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30017)
)
alarmInputHighDensity0017Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0017Alarm.setStatus(
        ""
    )

alarmInputHighDensity0018Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30018)
)
alarmInputHighDensity0018Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0018Alarm.setStatus(
        ""
    )

alarmInputHighDensity0019Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30019)
)
alarmInputHighDensity0019Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0019Alarm.setStatus(
        ""
    )

alarmInputHighDensity0020Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30020)
)
alarmInputHighDensity0020Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0020Alarm.setStatus(
        ""
    )

alarmInputHighDensity0021Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30021)
)
alarmInputHighDensity0021Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0021Alarm.setStatus(
        ""
    )

alarmInputHighDensity0022Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30022)
)
alarmInputHighDensity0022Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0022Alarm.setStatus(
        ""
    )

alarmInputHighDensity0023Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30023)
)
alarmInputHighDensity0023Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0023Alarm.setStatus(
        ""
    )

alarmInputHighDensity0024Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30024)
)
alarmInputHighDensity0024Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0024Alarm.setStatus(
        ""
    )

alarmInputHighDensity0025Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30025)
)
alarmInputHighDensity0025Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0025Alarm.setStatus(
        ""
    )

alarmInputHighDensity0026Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30026)
)
alarmInputHighDensity0026Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0026Alarm.setStatus(
        ""
    )

alarmInputHighDensity0027Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30027)
)
alarmInputHighDensity0027Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0027Alarm.setStatus(
        ""
    )

alarmInputHighDensity0028Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30028)
)
alarmInputHighDensity0028Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0028Alarm.setStatus(
        ""
    )

alarmInputHighDensity0029Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30029)
)
alarmInputHighDensity0029Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0029Alarm.setStatus(
        ""
    )

alarmInputHighDensity0030Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30030)
)
alarmInputHighDensity0030Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0030Alarm.setStatus(
        ""
    )

alarmInputHighDensity0031Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30031)
)
alarmInputHighDensity0031Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0031Alarm.setStatus(
        ""
    )

alarmInputHighDensity0032Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30032)
)
alarmInputHighDensity0032Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0032Alarm.setStatus(
        ""
    )

alarmInputHighDensity0033Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30033)
)
alarmInputHighDensity0033Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0033Alarm.setStatus(
        ""
    )

alarmInputHighDensity0034Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30034)
)
alarmInputHighDensity0034Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0034Alarm.setStatus(
        ""
    )

alarmInputHighDensity0035Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30035)
)
alarmInputHighDensity0035Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0035Alarm.setStatus(
        ""
    )

alarmInputHighDensity0036Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30036)
)
alarmInputHighDensity0036Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0036Alarm.setStatus(
        ""
    )

alarmInputHighDensity0037Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30037)
)
alarmInputHighDensity0037Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0037Alarm.setStatus(
        ""
    )

alarmInputHighDensity0038Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30038)
)
alarmInputHighDensity0038Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0038Alarm.setStatus(
        ""
    )

alarmInputHighDensity0039Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30039)
)
alarmInputHighDensity0039Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0039Alarm.setStatus(
        ""
    )

alarmInputHighDensity0040Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30040)
)
alarmInputHighDensity0040Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0040Alarm.setStatus(
        ""
    )

alarmInputHighDensity0041Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30041)
)
alarmInputHighDensity0041Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0041Alarm.setStatus(
        ""
    )

alarmInputHighDensity0042Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30042)
)
alarmInputHighDensity0042Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0042Alarm.setStatus(
        ""
    )

alarmInputHighDensity0043Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30043)
)
alarmInputHighDensity0043Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0043Alarm.setStatus(
        ""
    )

alarmInputHighDensity0044Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30044)
)
alarmInputHighDensity0044Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0044Alarm.setStatus(
        ""
    )

alarmInputHighDensity0045Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30045)
)
alarmInputHighDensity0045Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0045Alarm.setStatus(
        ""
    )

alarmInputHighDensity0046Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30046)
)
alarmInputHighDensity0046Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0046Alarm.setStatus(
        ""
    )

alarmInputHighDensity0047Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30047)
)
alarmInputHighDensity0047Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0047Alarm.setStatus(
        ""
    )

alarmInputHighDensity0048Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30048)
)
alarmInputHighDensity0048Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0048Alarm.setStatus(
        ""
    )

alarmInputHighDensity0049Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30049)
)
alarmInputHighDensity0049Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0049Alarm.setStatus(
        ""
    )

alarmInputHighDensity0050Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30050)
)
alarmInputHighDensity0050Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0050Alarm.setStatus(
        ""
    )

alarmInputHighDensity0051Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30051)
)
alarmInputHighDensity0051Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0051Alarm.setStatus(
        ""
    )

alarmInputHighDensity0052Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30052)
)
alarmInputHighDensity0052Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0052Alarm.setStatus(
        ""
    )

alarmInputHighDensity0053Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30053)
)
alarmInputHighDensity0053Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0053Alarm.setStatus(
        ""
    )

alarmInputHighDensity0054Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30054)
)
alarmInputHighDensity0054Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0054Alarm.setStatus(
        ""
    )

alarmInputHighDensity0055Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30055)
)
alarmInputHighDensity0055Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0055Alarm.setStatus(
        ""
    )

alarmInputHighDensity0056Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30056)
)
alarmInputHighDensity0056Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0056Alarm.setStatus(
        ""
    )

alarmInputHighDensity0057Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30057)
)
alarmInputHighDensity0057Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0057Alarm.setStatus(
        ""
    )

alarmInputHighDensity0058Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30058)
)
alarmInputHighDensity0058Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0058Alarm.setStatus(
        ""
    )

alarmInputHighDensity0059Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30059)
)
alarmInputHighDensity0059Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0059Alarm.setStatus(
        ""
    )

alarmInputHighDensity0060Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30060)
)
alarmInputHighDensity0060Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0060Alarm.setStatus(
        ""
    )

alarmInputHighDensity0061Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30061)
)
alarmInputHighDensity0061Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0061Alarm.setStatus(
        ""
    )

alarmInputHighDensity0062Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30062)
)
alarmInputHighDensity0062Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0062Alarm.setStatus(
        ""
    )

alarmInputHighDensity0063Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30063)
)
alarmInputHighDensity0063Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0063Alarm.setStatus(
        ""
    )

alarmInputHighDensity0064Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30064)
)
alarmInputHighDensity0064Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0064Alarm.setStatus(
        ""
    )

alarmInputHighDensity0065Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30065)
)
alarmInputHighDensity0065Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0065Alarm.setStatus(
        ""
    )

alarmInputHighDensity0066Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30066)
)
alarmInputHighDensity0066Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0066Alarm.setStatus(
        ""
    )

alarmInputHighDensity0067Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30067)
)
alarmInputHighDensity0067Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0067Alarm.setStatus(
        ""
    )

alarmInputHighDensity0068Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30068)
)
alarmInputHighDensity0068Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0068Alarm.setStatus(
        ""
    )

alarmInputHighDensity0069Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30069)
)
alarmInputHighDensity0069Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0069Alarm.setStatus(
        ""
    )

alarmInputHighDensity0070Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30070)
)
alarmInputHighDensity0070Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0070Alarm.setStatus(
        ""
    )

alarmInputHighDensity0071Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30071)
)
alarmInputHighDensity0071Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0071Alarm.setStatus(
        ""
    )

alarmInputHighDensity0072Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30072)
)
alarmInputHighDensity0072Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0072Alarm.setStatus(
        ""
    )

alarmInputHighDensity0073Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30073)
)
alarmInputHighDensity0073Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0073Alarm.setStatus(
        ""
    )

alarmInputHighDensity0074Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30074)
)
alarmInputHighDensity0074Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0074Alarm.setStatus(
        ""
    )

alarmInputHighDensity0075Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30075)
)
alarmInputHighDensity0075Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0075Alarm.setStatus(
        ""
    )

alarmInputHighDensity0076Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30076)
)
alarmInputHighDensity0076Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0076Alarm.setStatus(
        ""
    )

alarmInputHighDensity0077Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30077)
)
alarmInputHighDensity0077Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0077Alarm.setStatus(
        ""
    )

alarmInputHighDensity0078Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30078)
)
alarmInputHighDensity0078Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0078Alarm.setStatus(
        ""
    )

alarmInputHighDensity0079Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30079)
)
alarmInputHighDensity0079Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0079Alarm.setStatus(
        ""
    )

alarmInputHighDensity0080Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30080)
)
alarmInputHighDensity0080Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0080Alarm.setStatus(
        ""
    )

alarmInputHighDensity0081Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30081)
)
alarmInputHighDensity0081Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0081Alarm.setStatus(
        ""
    )

alarmInputHighDensity0082Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30082)
)
alarmInputHighDensity0082Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0082Alarm.setStatus(
        ""
    )

alarmInputHighDensity0083Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30083)
)
alarmInputHighDensity0083Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0083Alarm.setStatus(
        ""
    )

alarmInputHighDensity0084Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30084)
)
alarmInputHighDensity0084Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0084Alarm.setStatus(
        ""
    )

alarmInputHighDensity0085Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30085)
)
alarmInputHighDensity0085Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0085Alarm.setStatus(
        ""
    )

alarmInputHighDensity0086Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30086)
)
alarmInputHighDensity0086Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0086Alarm.setStatus(
        ""
    )

alarmInputHighDensity0087Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30087)
)
alarmInputHighDensity0087Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0087Alarm.setStatus(
        ""
    )

alarmInputHighDensity0088Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30088)
)
alarmInputHighDensity0088Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0088Alarm.setStatus(
        ""
    )

alarmInputHighDensity0089Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30089)
)
alarmInputHighDensity0089Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0089Alarm.setStatus(
        ""
    )

alarmInputHighDensity0090Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30090)
)
alarmInputHighDensity0090Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0090Alarm.setStatus(
        ""
    )

alarmInputHighDensity0091Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30091)
)
alarmInputHighDensity0091Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0091Alarm.setStatus(
        ""
    )

alarmInputHighDensity0092Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30092)
)
alarmInputHighDensity0092Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0092Alarm.setStatus(
        ""
    )

alarmInputHighDensity0093Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30093)
)
alarmInputHighDensity0093Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0093Alarm.setStatus(
        ""
    )

alarmInputHighDensity0094Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30094)
)
alarmInputHighDensity0094Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0094Alarm.setStatus(
        ""
    )

alarmInputHighDensity0095Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30095)
)
alarmInputHighDensity0095Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0095Alarm.setStatus(
        ""
    )

alarmInputHighDensity0096Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30096)
)
alarmInputHighDensity0096Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0096Alarm.setStatus(
        ""
    )

alarmInputHighDensity0097Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30097)
)
alarmInputHighDensity0097Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0097Alarm.setStatus(
        ""
    )

alarmInputHighDensity0098Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30098)
)
alarmInputHighDensity0098Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0098Alarm.setStatus(
        ""
    )

alarmInputHighDensity0099Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30099)
)
alarmInputHighDensity0099Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0099Alarm.setStatus(
        ""
    )

alarmInputHighDensity0100Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30100)
)
alarmInputHighDensity0100Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0100Alarm.setStatus(
        ""
    )

alarmInputHighDensity0101Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30101)
)
alarmInputHighDensity0101Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0101Alarm.setStatus(
        ""
    )

alarmInputHighDensity0102Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30102)
)
alarmInputHighDensity0102Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0102Alarm.setStatus(
        ""
    )

alarmInputHighDensity0103Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30103)
)
alarmInputHighDensity0103Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0103Alarm.setStatus(
        ""
    )

alarmInputHighDensity0104Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30104)
)
alarmInputHighDensity0104Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0104Alarm.setStatus(
        ""
    )

alarmInputHighDensity0105Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30105)
)
alarmInputHighDensity0105Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0105Alarm.setStatus(
        ""
    )

alarmInputHighDensity0106Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30106)
)
alarmInputHighDensity0106Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0106Alarm.setStatus(
        ""
    )

alarmInputHighDensity0107Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30107)
)
alarmInputHighDensity0107Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0107Alarm.setStatus(
        ""
    )

alarmInputHighDensity0108Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30108)
)
alarmInputHighDensity0108Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0108Alarm.setStatus(
        ""
    )

alarmInputHighDensity0109Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30109)
)
alarmInputHighDensity0109Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0109Alarm.setStatus(
        ""
    )

alarmInputHighDensity0110Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30110)
)
alarmInputHighDensity0110Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0110Alarm.setStatus(
        ""
    )

alarmInputHighDensity0111Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30111)
)
alarmInputHighDensity0111Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0111Alarm.setStatus(
        ""
    )

alarmInputHighDensity0112Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30112)
)
alarmInputHighDensity0112Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0112Alarm.setStatus(
        ""
    )

alarmInputHighDensity0113Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30113)
)
alarmInputHighDensity0113Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0113Alarm.setStatus(
        ""
    )

alarmInputHighDensity0114Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30114)
)
alarmInputHighDensity0114Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0114Alarm.setStatus(
        ""
    )

alarmInputHighDensity0115Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30115)
)
alarmInputHighDensity0115Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0115Alarm.setStatus(
        ""
    )

alarmInputHighDensity0116Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30116)
)
alarmInputHighDensity0116Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0116Alarm.setStatus(
        ""
    )

alarmInputHighDensity0117Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30117)
)
alarmInputHighDensity0117Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0117Alarm.setStatus(
        ""
    )

alarmInputHighDensity0118Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30118)
)
alarmInputHighDensity0118Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0118Alarm.setStatus(
        ""
    )

alarmInputHighDensity0119Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30119)
)
alarmInputHighDensity0119Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0119Alarm.setStatus(
        ""
    )

alarmInputHighDensity0120Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30120)
)
alarmInputHighDensity0120Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0120Alarm.setStatus(
        ""
    )

alarmInputHighDensity0121Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30121)
)
alarmInputHighDensity0121Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0121Alarm.setStatus(
        ""
    )

alarmInputHighDensity0122Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30122)
)
alarmInputHighDensity0122Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0122Alarm.setStatus(
        ""
    )

alarmInputHighDensity0123Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30123)
)
alarmInputHighDensity0123Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0123Alarm.setStatus(
        ""
    )

alarmInputHighDensity0124Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30124)
)
alarmInputHighDensity0124Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0124Alarm.setStatus(
        ""
    )

alarmInputHighDensity0125Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30125)
)
alarmInputHighDensity0125Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0125Alarm.setStatus(
        ""
    )

alarmInputHighDensity0126Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30126)
)
alarmInputHighDensity0126Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0126Alarm.setStatus(
        ""
    )

alarmInputHighDensity0127Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30127)
)
alarmInputHighDensity0127Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0127Alarm.setStatus(
        ""
    )

alarmInputHighDensity0128Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30128)
)
alarmInputHighDensity0128Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0128Alarm.setStatus(
        ""
    )

alarmInputHighDensity0129Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30129)
)
alarmInputHighDensity0129Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0129Alarm.setStatus(
        ""
    )

alarmInputHighDensity0130Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30130)
)
alarmInputHighDensity0130Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0130Alarm.setStatus(
        ""
    )

alarmInputHighDensity0131Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30131)
)
alarmInputHighDensity0131Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0131Alarm.setStatus(
        ""
    )

alarmInputHighDensity0132Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30132)
)
alarmInputHighDensity0132Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0132Alarm.setStatus(
        ""
    )

alarmInputHighDensity0133Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30133)
)
alarmInputHighDensity0133Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0133Alarm.setStatus(
        ""
    )

alarmInputHighDensity0134Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30134)
)
alarmInputHighDensity0134Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0134Alarm.setStatus(
        ""
    )

alarmInputHighDensity0135Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30135)
)
alarmInputHighDensity0135Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0135Alarm.setStatus(
        ""
    )

alarmInputHighDensity0136Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30136)
)
alarmInputHighDensity0136Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0136Alarm.setStatus(
        ""
    )

alarmInputHighDensity0137Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30137)
)
alarmInputHighDensity0137Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0137Alarm.setStatus(
        ""
    )

alarmInputHighDensity0138Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30138)
)
alarmInputHighDensity0138Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0138Alarm.setStatus(
        ""
    )

alarmInputHighDensity0139Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30139)
)
alarmInputHighDensity0139Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0139Alarm.setStatus(
        ""
    )

alarmInputHighDensity0140Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30140)
)
alarmInputHighDensity0140Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0140Alarm.setStatus(
        ""
    )

alarmInputHighDensity0141Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30141)
)
alarmInputHighDensity0141Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0141Alarm.setStatus(
        ""
    )

alarmInputHighDensity0142Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30142)
)
alarmInputHighDensity0142Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0142Alarm.setStatus(
        ""
    )

alarmInputHighDensity0143Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30143)
)
alarmInputHighDensity0143Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0143Alarm.setStatus(
        ""
    )

alarmInputHighDensity0144Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30144)
)
alarmInputHighDensity0144Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0144Alarm.setStatus(
        ""
    )

alarmInputHighDensity0145Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30145)
)
alarmInputHighDensity0145Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0145Alarm.setStatus(
        ""
    )

alarmInputHighDensity0146Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30146)
)
alarmInputHighDensity0146Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0146Alarm.setStatus(
        ""
    )

alarmInputHighDensity0147Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30147)
)
alarmInputHighDensity0147Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0147Alarm.setStatus(
        ""
    )

alarmInputHighDensity0148Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30148)
)
alarmInputHighDensity0148Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0148Alarm.setStatus(
        ""
    )

alarmInputHighDensity0149Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30149)
)
alarmInputHighDensity0149Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0149Alarm.setStatus(
        ""
    )

alarmInputHighDensity0150Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30150)
)
alarmInputHighDensity0150Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0150Alarm.setStatus(
        ""
    )

alarmInputHighDensity0151Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30151)
)
alarmInputHighDensity0151Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0151Alarm.setStatus(
        ""
    )

alarmInputHighDensity0152Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30152)
)
alarmInputHighDensity0152Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0152Alarm.setStatus(
        ""
    )

alarmInputHighDensity0153Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30153)
)
alarmInputHighDensity0153Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0153Alarm.setStatus(
        ""
    )

alarmInputHighDensity0154Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30154)
)
alarmInputHighDensity0154Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0154Alarm.setStatus(
        ""
    )

alarmInputHighDensity0155Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30155)
)
alarmInputHighDensity0155Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0155Alarm.setStatus(
        ""
    )

alarmInputHighDensity0156Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30156)
)
alarmInputHighDensity0156Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0156Alarm.setStatus(
        ""
    )

alarmInputHighDensity0157Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30157)
)
alarmInputHighDensity0157Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0157Alarm.setStatus(
        ""
    )

alarmInputHighDensity0158Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30158)
)
alarmInputHighDensity0158Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0158Alarm.setStatus(
        ""
    )

alarmInputHighDensity0159Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30159)
)
alarmInputHighDensity0159Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0159Alarm.setStatus(
        ""
    )

alarmInputHighDensity0160Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30160)
)
alarmInputHighDensity0160Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0160Alarm.setStatus(
        ""
    )

alarmInputHighDensity0161Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30161)
)
alarmInputHighDensity0161Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0161Alarm.setStatus(
        ""
    )

alarmInputHighDensity0162Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30162)
)
alarmInputHighDensity0162Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0162Alarm.setStatus(
        ""
    )

alarmInputHighDensity0163Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30163)
)
alarmInputHighDensity0163Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0163Alarm.setStatus(
        ""
    )

alarmInputHighDensity0164Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30164)
)
alarmInputHighDensity0164Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0164Alarm.setStatus(
        ""
    )

alarmInputHighDensity0165Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30165)
)
alarmInputHighDensity0165Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0165Alarm.setStatus(
        ""
    )

alarmInputHighDensity0166Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30166)
)
alarmInputHighDensity0166Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0166Alarm.setStatus(
        ""
    )

alarmInputHighDensity0167Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30167)
)
alarmInputHighDensity0167Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0167Alarm.setStatus(
        ""
    )

alarmInputHighDensity0168Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30168)
)
alarmInputHighDensity0168Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0168Alarm.setStatus(
        ""
    )

alarmInputHighDensity0169Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30169)
)
alarmInputHighDensity0169Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0169Alarm.setStatus(
        ""
    )

alarmInputHighDensity0170Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30170)
)
alarmInputHighDensity0170Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0170Alarm.setStatus(
        ""
    )

alarmInputHighDensity0171Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30171)
)
alarmInputHighDensity0171Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0171Alarm.setStatus(
        ""
    )

alarmInputHighDensity0172Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30172)
)
alarmInputHighDensity0172Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0172Alarm.setStatus(
        ""
    )

alarmInputHighDensity0173Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30173)
)
alarmInputHighDensity0173Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0173Alarm.setStatus(
        ""
    )

alarmInputHighDensity0174Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30174)
)
alarmInputHighDensity0174Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0174Alarm.setStatus(
        ""
    )

alarmInputHighDensity0175Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30175)
)
alarmInputHighDensity0175Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0175Alarm.setStatus(
        ""
    )

alarmInputHighDensity0176Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30176)
)
alarmInputHighDensity0176Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0176Alarm.setStatus(
        ""
    )

alarmInputHighDensity0177Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30177)
)
alarmInputHighDensity0177Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0177Alarm.setStatus(
        ""
    )

alarmInputHighDensity0178Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30178)
)
alarmInputHighDensity0178Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0178Alarm.setStatus(
        ""
    )

alarmInputHighDensity0179Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30179)
)
alarmInputHighDensity0179Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0179Alarm.setStatus(
        ""
    )

alarmInputHighDensity0180Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30180)
)
alarmInputHighDensity0180Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0180Alarm.setStatus(
        ""
    )

alarmInputHighDensity0181Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30181)
)
alarmInputHighDensity0181Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0181Alarm.setStatus(
        ""
    )

alarmInputHighDensity0182Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30182)
)
alarmInputHighDensity0182Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0182Alarm.setStatus(
        ""
    )

alarmInputHighDensity0183Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30183)
)
alarmInputHighDensity0183Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0183Alarm.setStatus(
        ""
    )

alarmInputHighDensity0184Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30184)
)
alarmInputHighDensity0184Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0184Alarm.setStatus(
        ""
    )

alarmInputHighDensity0185Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30185)
)
alarmInputHighDensity0185Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0185Alarm.setStatus(
        ""
    )

alarmInputHighDensity0186Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30186)
)
alarmInputHighDensity0186Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0186Alarm.setStatus(
        ""
    )

alarmInputHighDensity0187Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30187)
)
alarmInputHighDensity0187Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0187Alarm.setStatus(
        ""
    )

alarmInputHighDensity0188Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30188)
)
alarmInputHighDensity0188Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0188Alarm.setStatus(
        ""
    )

alarmInputHighDensity0189Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30189)
)
alarmInputHighDensity0189Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0189Alarm.setStatus(
        ""
    )

alarmInputHighDensity0190Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30190)
)
alarmInputHighDensity0190Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0190Alarm.setStatus(
        ""
    )

alarmInputHighDensity0191Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30191)
)
alarmInputHighDensity0191Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0191Alarm.setStatus(
        ""
    )

alarmInputHighDensity0192Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30192)
)
alarmInputHighDensity0192Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0192Alarm.setStatus(
        ""
    )

alarmInputHighDensity0193Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30193)
)
alarmInputHighDensity0193Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0193Alarm.setStatus(
        ""
    )

alarmInputHighDensity0194Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30194)
)
alarmInputHighDensity0194Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0194Alarm.setStatus(
        ""
    )

alarmInputHighDensity0195Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30195)
)
alarmInputHighDensity0195Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0195Alarm.setStatus(
        ""
    )

alarmInputHighDensity0196Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30196)
)
alarmInputHighDensity0196Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0196Alarm.setStatus(
        ""
    )

alarmInputHighDensity0197Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30197)
)
alarmInputHighDensity0197Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0197Alarm.setStatus(
        ""
    )

alarmInputHighDensity0198Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30198)
)
alarmInputHighDensity0198Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0198Alarm.setStatus(
        ""
    )

alarmInputHighDensity0199Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30199)
)
alarmInputHighDensity0199Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0199Alarm.setStatus(
        ""
    )

alarmInputHighDensity0200Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30200)
)
alarmInputHighDensity0200Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0200Alarm.setStatus(
        ""
    )

alarmInputHighDensity0201Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30201)
)
alarmInputHighDensity0201Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0201Alarm.setStatus(
        ""
    )

alarmInputHighDensity0202Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30202)
)
alarmInputHighDensity0202Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0202Alarm.setStatus(
        ""
    )

alarmInputHighDensity0203Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30203)
)
alarmInputHighDensity0203Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0203Alarm.setStatus(
        ""
    )

alarmInputHighDensity0204Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30204)
)
alarmInputHighDensity0204Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0204Alarm.setStatus(
        ""
    )

alarmInputHighDensity0205Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30205)
)
alarmInputHighDensity0205Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0205Alarm.setStatus(
        ""
    )

alarmInputHighDensity0206Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30206)
)
alarmInputHighDensity0206Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0206Alarm.setStatus(
        ""
    )

alarmInputHighDensity0207Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30207)
)
alarmInputHighDensity0207Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0207Alarm.setStatus(
        ""
    )

alarmInputHighDensity0208Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30208)
)
alarmInputHighDensity0208Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0208Alarm.setStatus(
        ""
    )

alarmInputHighDensity0209Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30209)
)
alarmInputHighDensity0209Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0209Alarm.setStatus(
        ""
    )

alarmInputHighDensity0210Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30210)
)
alarmInputHighDensity0210Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0210Alarm.setStatus(
        ""
    )

alarmInputHighDensity0211Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30211)
)
alarmInputHighDensity0211Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0211Alarm.setStatus(
        ""
    )

alarmInputHighDensity0212Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30212)
)
alarmInputHighDensity0212Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0212Alarm.setStatus(
        ""
    )

alarmInputHighDensity0213Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30213)
)
alarmInputHighDensity0213Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0213Alarm.setStatus(
        ""
    )

alarmInputHighDensity0214Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30214)
)
alarmInputHighDensity0214Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0214Alarm.setStatus(
        ""
    )

alarmInputHighDensity0215Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30215)
)
alarmInputHighDensity0215Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0215Alarm.setStatus(
        ""
    )

alarmInputHighDensity0216Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30216)
)
alarmInputHighDensity0216Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0216Alarm.setStatus(
        ""
    )

alarmInputHighDensity0217Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30217)
)
alarmInputHighDensity0217Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0217Alarm.setStatus(
        ""
    )

alarmInputHighDensity0218Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30218)
)
alarmInputHighDensity0218Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0218Alarm.setStatus(
        ""
    )

alarmInputHighDensity0219Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30219)
)
alarmInputHighDensity0219Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0219Alarm.setStatus(
        ""
    )

alarmInputHighDensity0220Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30220)
)
alarmInputHighDensity0220Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0220Alarm.setStatus(
        ""
    )

alarmInputHighDensity0221Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30221)
)
alarmInputHighDensity0221Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0221Alarm.setStatus(
        ""
    )

alarmInputHighDensity0222Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30222)
)
alarmInputHighDensity0222Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0222Alarm.setStatus(
        ""
    )

alarmInputHighDensity0223Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30223)
)
alarmInputHighDensity0223Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0223Alarm.setStatus(
        ""
    )

alarmInputHighDensity0224Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30224)
)
alarmInputHighDensity0224Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0224Alarm.setStatus(
        ""
    )

alarmInputHighDensity0225Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30225)
)
alarmInputHighDensity0225Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0225Alarm.setStatus(
        ""
    )

alarmInputHighDensity0226Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30226)
)
alarmInputHighDensity0226Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0226Alarm.setStatus(
        ""
    )

alarmInputHighDensity0227Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30227)
)
alarmInputHighDensity0227Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0227Alarm.setStatus(
        ""
    )

alarmInputHighDensity0228Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30228)
)
alarmInputHighDensity0228Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0228Alarm.setStatus(
        ""
    )

alarmInputHighDensity0229Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30229)
)
alarmInputHighDensity0229Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0229Alarm.setStatus(
        ""
    )

alarmInputHighDensity0230Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30230)
)
alarmInputHighDensity0230Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0230Alarm.setStatus(
        ""
    )

alarmInputHighDensity0231Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30231)
)
alarmInputHighDensity0231Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0231Alarm.setStatus(
        ""
    )

alarmInputHighDensity0232Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30232)
)
alarmInputHighDensity0232Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0232Alarm.setStatus(
        ""
    )

alarmInputHighDensity0233Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30233)
)
alarmInputHighDensity0233Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0233Alarm.setStatus(
        ""
    )

alarmInputHighDensity0234Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30234)
)
alarmInputHighDensity0234Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0234Alarm.setStatus(
        ""
    )

alarmInputHighDensity0235Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30235)
)
alarmInputHighDensity0235Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0235Alarm.setStatus(
        ""
    )

alarmInputHighDensity0236Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30236)
)
alarmInputHighDensity0236Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0236Alarm.setStatus(
        ""
    )

alarmInputHighDensity0237Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30237)
)
alarmInputHighDensity0237Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0237Alarm.setStatus(
        ""
    )

alarmInputHighDensity0238Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30238)
)
alarmInputHighDensity0238Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0238Alarm.setStatus(
        ""
    )

alarmInputHighDensity0239Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30239)
)
alarmInputHighDensity0239Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0239Alarm.setStatus(
        ""
    )

alarmInputHighDensity0240Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30240)
)
alarmInputHighDensity0240Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0240Alarm.setStatus(
        ""
    )

alarmInputHighDensity0241Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30241)
)
alarmInputHighDensity0241Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0241Alarm.setStatus(
        ""
    )

alarmInputHighDensity0242Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30242)
)
alarmInputHighDensity0242Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0242Alarm.setStatus(
        ""
    )

alarmInputHighDensity0243Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30243)
)
alarmInputHighDensity0243Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0243Alarm.setStatus(
        ""
    )

alarmInputHighDensity0244Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30244)
)
alarmInputHighDensity0244Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0244Alarm.setStatus(
        ""
    )

alarmInputHighDensity0245Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30245)
)
alarmInputHighDensity0245Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0245Alarm.setStatus(
        ""
    )

alarmInputHighDensity0246Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30246)
)
alarmInputHighDensity0246Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0246Alarm.setStatus(
        ""
    )

alarmInputHighDensity0247Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30247)
)
alarmInputHighDensity0247Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0247Alarm.setStatus(
        ""
    )

alarmInputHighDensity0248Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30248)
)
alarmInputHighDensity0248Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0248Alarm.setStatus(
        ""
    )

alarmInputHighDensity0249Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30249)
)
alarmInputHighDensity0249Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0249Alarm.setStatus(
        ""
    )

alarmInputHighDensity0250Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30250)
)
alarmInputHighDensity0250Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0250Alarm.setStatus(
        ""
    )

alarmInputHighDensity0251Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30251)
)
alarmInputHighDensity0251Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0251Alarm.setStatus(
        ""
    )

alarmInputHighDensity0252Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30252)
)
alarmInputHighDensity0252Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0252Alarm.setStatus(
        ""
    )

alarmInputHighDensity0253Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30253)
)
alarmInputHighDensity0253Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0253Alarm.setStatus(
        ""
    )

alarmInputHighDensity0254Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30254)
)
alarmInputHighDensity0254Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0254Alarm.setStatus(
        ""
    )

alarmInputHighDensity0255Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30255)
)
alarmInputHighDensity0255Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0255Alarm.setStatus(
        ""
    )

alarmInputHighDensity0256Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30256)
)
alarmInputHighDensity0256Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0256Alarm.setStatus(
        ""
    )

alarmInputHighDensity0257Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30257)
)
alarmInputHighDensity0257Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0257Alarm.setStatus(
        ""
    )

alarmInputHighDensity0258Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30258)
)
alarmInputHighDensity0258Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0258Alarm.setStatus(
        ""
    )

alarmInputHighDensity0259Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30259)
)
alarmInputHighDensity0259Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0259Alarm.setStatus(
        ""
    )

alarmInputHighDensity0260Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30260)
)
alarmInputHighDensity0260Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0260Alarm.setStatus(
        ""
    )

alarmInputHighDensity0261Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30261)
)
alarmInputHighDensity0261Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0261Alarm.setStatus(
        ""
    )

alarmInputHighDensity0262Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30262)
)
alarmInputHighDensity0262Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0262Alarm.setStatus(
        ""
    )

alarmInputHighDensity0263Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30263)
)
alarmInputHighDensity0263Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0263Alarm.setStatus(
        ""
    )

alarmInputHighDensity0264Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30264)
)
alarmInputHighDensity0264Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0264Alarm.setStatus(
        ""
    )

alarmInputHighDensity0265Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30265)
)
alarmInputHighDensity0265Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0265Alarm.setStatus(
        ""
    )

alarmInputHighDensity0266Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30266)
)
alarmInputHighDensity0266Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0266Alarm.setStatus(
        ""
    )

alarmInputHighDensity0267Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30267)
)
alarmInputHighDensity0267Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0267Alarm.setStatus(
        ""
    )

alarmInputHighDensity0268Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30268)
)
alarmInputHighDensity0268Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0268Alarm.setStatus(
        ""
    )

alarmInputHighDensity0269Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30269)
)
alarmInputHighDensity0269Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0269Alarm.setStatus(
        ""
    )

alarmInputHighDensity0270Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30270)
)
alarmInputHighDensity0270Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0270Alarm.setStatus(
        ""
    )

alarmInputHighDensity0271Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30271)
)
alarmInputHighDensity0271Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0271Alarm.setStatus(
        ""
    )

alarmInputHighDensity0272Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30272)
)
alarmInputHighDensity0272Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0272Alarm.setStatus(
        ""
    )

alarmInputHighDensity0273Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30273)
)
alarmInputHighDensity0273Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0273Alarm.setStatus(
        ""
    )

alarmInputHighDensity0274Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30274)
)
alarmInputHighDensity0274Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0274Alarm.setStatus(
        ""
    )

alarmInputHighDensity0275Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30275)
)
alarmInputHighDensity0275Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0275Alarm.setStatus(
        ""
    )

alarmInputHighDensity0276Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30276)
)
alarmInputHighDensity0276Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0276Alarm.setStatus(
        ""
    )

alarmInputHighDensity0277Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30277)
)
alarmInputHighDensity0277Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0277Alarm.setStatus(
        ""
    )

alarmInputHighDensity0278Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30278)
)
alarmInputHighDensity0278Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0278Alarm.setStatus(
        ""
    )

alarmInputHighDensity0279Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30279)
)
alarmInputHighDensity0279Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0279Alarm.setStatus(
        ""
    )

alarmInputHighDensity0280Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30280)
)
alarmInputHighDensity0280Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0280Alarm.setStatus(
        ""
    )

alarmInputHighDensity0281Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30281)
)
alarmInputHighDensity0281Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0281Alarm.setStatus(
        ""
    )

alarmInputHighDensity0282Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30282)
)
alarmInputHighDensity0282Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0282Alarm.setStatus(
        ""
    )

alarmInputHighDensity0283Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30283)
)
alarmInputHighDensity0283Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0283Alarm.setStatus(
        ""
    )

alarmInputHighDensity0284Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30284)
)
alarmInputHighDensity0284Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0284Alarm.setStatus(
        ""
    )

alarmInputHighDensity0285Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30285)
)
alarmInputHighDensity0285Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0285Alarm.setStatus(
        ""
    )

alarmInputHighDensity0286Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30286)
)
alarmInputHighDensity0286Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0286Alarm.setStatus(
        ""
    )

alarmInputHighDensity0287Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30287)
)
alarmInputHighDensity0287Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0287Alarm.setStatus(
        ""
    )

alarmInputHighDensity0288Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30288)
)
alarmInputHighDensity0288Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0288Alarm.setStatus(
        ""
    )

alarmInputHighDensity0289Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30289)
)
alarmInputHighDensity0289Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0289Alarm.setStatus(
        ""
    )

alarmInputHighDensity0290Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30290)
)
alarmInputHighDensity0290Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0290Alarm.setStatus(
        ""
    )

alarmInputHighDensity0291Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30291)
)
alarmInputHighDensity0291Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0291Alarm.setStatus(
        ""
    )

alarmInputHighDensity0292Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30292)
)
alarmInputHighDensity0292Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0292Alarm.setStatus(
        ""
    )

alarmInputHighDensity0293Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30293)
)
alarmInputHighDensity0293Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0293Alarm.setStatus(
        ""
    )

alarmInputHighDensity0294Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30294)
)
alarmInputHighDensity0294Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0294Alarm.setStatus(
        ""
    )

alarmInputHighDensity0295Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30295)
)
alarmInputHighDensity0295Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0295Alarm.setStatus(
        ""
    )

alarmInputHighDensity0296Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30296)
)
alarmInputHighDensity0296Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0296Alarm.setStatus(
        ""
    )

alarmInputHighDensity0297Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30297)
)
alarmInputHighDensity0297Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0297Alarm.setStatus(
        ""
    )

alarmInputHighDensity0298Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30298)
)
alarmInputHighDensity0298Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0298Alarm.setStatus(
        ""
    )

alarmInputHighDensity0299Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30299)
)
alarmInputHighDensity0299Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0299Alarm.setStatus(
        ""
    )

alarmInputHighDensity0300Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30300)
)
alarmInputHighDensity0300Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0300Alarm.setStatus(
        ""
    )

alarmInputHighDensity0301Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30301)
)
alarmInputHighDensity0301Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0301Alarm.setStatus(
        ""
    )

alarmInputHighDensity0302Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30302)
)
alarmInputHighDensity0302Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0302Alarm.setStatus(
        ""
    )

alarmInputHighDensity0303Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30303)
)
alarmInputHighDensity0303Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0303Alarm.setStatus(
        ""
    )

alarmInputHighDensity0304Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30304)
)
alarmInputHighDensity0304Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0304Alarm.setStatus(
        ""
    )

alarmInputHighDensity0305Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30305)
)
alarmInputHighDensity0305Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0305Alarm.setStatus(
        ""
    )

alarmInputHighDensity0306Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30306)
)
alarmInputHighDensity0306Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0306Alarm.setStatus(
        ""
    )

alarmInputHighDensity0307Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30307)
)
alarmInputHighDensity0307Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0307Alarm.setStatus(
        ""
    )

alarmInputHighDensity0308Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30308)
)
alarmInputHighDensity0308Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0308Alarm.setStatus(
        ""
    )

alarmInputHighDensity0309Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30309)
)
alarmInputHighDensity0309Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0309Alarm.setStatus(
        ""
    )

alarmInputHighDensity0310Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30310)
)
alarmInputHighDensity0310Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0310Alarm.setStatus(
        ""
    )

alarmInputHighDensity0311Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30311)
)
alarmInputHighDensity0311Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0311Alarm.setStatus(
        ""
    )

alarmInputHighDensity0312Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30312)
)
alarmInputHighDensity0312Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0312Alarm.setStatus(
        ""
    )

alarmInputHighDensity0313Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30313)
)
alarmInputHighDensity0313Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0313Alarm.setStatus(
        ""
    )

alarmInputHighDensity0314Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30314)
)
alarmInputHighDensity0314Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0314Alarm.setStatus(
        ""
    )

alarmInputHighDensity0315Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30315)
)
alarmInputHighDensity0315Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0315Alarm.setStatus(
        ""
    )

alarmInputHighDensity0316Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30316)
)
alarmInputHighDensity0316Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0316Alarm.setStatus(
        ""
    )

alarmInputHighDensity0317Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30317)
)
alarmInputHighDensity0317Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0317Alarm.setStatus(
        ""
    )

alarmInputHighDensity0318Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30318)
)
alarmInputHighDensity0318Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0318Alarm.setStatus(
        ""
    )

alarmInputHighDensity0319Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30319)
)
alarmInputHighDensity0319Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0319Alarm.setStatus(
        ""
    )

alarmInputHighDensity0320Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30320)
)
alarmInputHighDensity0320Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0320Alarm.setStatus(
        ""
    )

alarmInputHighDensity0321Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30321)
)
alarmInputHighDensity0321Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0321Alarm.setStatus(
        ""
    )

alarmInputHighDensity0322Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30322)
)
alarmInputHighDensity0322Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0322Alarm.setStatus(
        ""
    )

alarmInputHighDensity0323Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30323)
)
alarmInputHighDensity0323Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0323Alarm.setStatus(
        ""
    )

alarmInputHighDensity0324Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30324)
)
alarmInputHighDensity0324Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0324Alarm.setStatus(
        ""
    )

alarmInputHighDensity0325Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30325)
)
alarmInputHighDensity0325Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0325Alarm.setStatus(
        ""
    )

alarmInputHighDensity0326Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30326)
)
alarmInputHighDensity0326Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0326Alarm.setStatus(
        ""
    )

alarmInputHighDensity0327Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30327)
)
alarmInputHighDensity0327Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0327Alarm.setStatus(
        ""
    )

alarmInputHighDensity0328Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30328)
)
alarmInputHighDensity0328Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0328Alarm.setStatus(
        ""
    )

alarmInputHighDensity0329Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30329)
)
alarmInputHighDensity0329Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0329Alarm.setStatus(
        ""
    )

alarmInputHighDensity0330Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30330)
)
alarmInputHighDensity0330Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0330Alarm.setStatus(
        ""
    )

alarmInputHighDensity0331Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30331)
)
alarmInputHighDensity0331Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0331Alarm.setStatus(
        ""
    )

alarmInputHighDensity0332Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30332)
)
alarmInputHighDensity0332Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0332Alarm.setStatus(
        ""
    )

alarmInputHighDensity0333Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30333)
)
alarmInputHighDensity0333Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0333Alarm.setStatus(
        ""
    )

alarmInputHighDensity0334Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30334)
)
alarmInputHighDensity0334Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0334Alarm.setStatus(
        ""
    )

alarmInputHighDensity0335Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30335)
)
alarmInputHighDensity0335Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0335Alarm.setStatus(
        ""
    )

alarmInputHighDensity0336Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30336)
)
alarmInputHighDensity0336Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0336Alarm.setStatus(
        ""
    )

alarmInputHighDensity0337Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30337)
)
alarmInputHighDensity0337Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0337Alarm.setStatus(
        ""
    )

alarmInputHighDensity0338Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30338)
)
alarmInputHighDensity0338Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0338Alarm.setStatus(
        ""
    )

alarmInputHighDensity0339Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30339)
)
alarmInputHighDensity0339Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0339Alarm.setStatus(
        ""
    )

alarmInputHighDensity0340Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30340)
)
alarmInputHighDensity0340Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0340Alarm.setStatus(
        ""
    )

alarmInputHighDensity0341Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30341)
)
alarmInputHighDensity0341Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0341Alarm.setStatus(
        ""
    )

alarmInputHighDensity0342Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30342)
)
alarmInputHighDensity0342Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0342Alarm.setStatus(
        ""
    )

alarmInputHighDensity0343Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30343)
)
alarmInputHighDensity0343Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0343Alarm.setStatus(
        ""
    )

alarmInputHighDensity0344Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30344)
)
alarmInputHighDensity0344Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0344Alarm.setStatus(
        ""
    )

alarmInputHighDensity0345Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30345)
)
alarmInputHighDensity0345Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0345Alarm.setStatus(
        ""
    )

alarmInputHighDensity0346Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30346)
)
alarmInputHighDensity0346Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0346Alarm.setStatus(
        ""
    )

alarmInputHighDensity0347Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30347)
)
alarmInputHighDensity0347Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0347Alarm.setStatus(
        ""
    )

alarmInputHighDensity0348Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30348)
)
alarmInputHighDensity0348Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0348Alarm.setStatus(
        ""
    )

alarmInputHighDensity0349Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30349)
)
alarmInputHighDensity0349Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0349Alarm.setStatus(
        ""
    )

alarmInputHighDensity0350Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30350)
)
alarmInputHighDensity0350Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0350Alarm.setStatus(
        ""
    )

alarmInputHighDensity0351Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30351)
)
alarmInputHighDensity0351Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0351Alarm.setStatus(
        ""
    )

alarmInputHighDensity0352Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30352)
)
alarmInputHighDensity0352Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0352Alarm.setStatus(
        ""
    )

alarmInputHighDensity0353Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30353)
)
alarmInputHighDensity0353Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0353Alarm.setStatus(
        ""
    )

alarmInputHighDensity0354Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30354)
)
alarmInputHighDensity0354Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0354Alarm.setStatus(
        ""
    )

alarmInputHighDensity0355Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30355)
)
alarmInputHighDensity0355Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0355Alarm.setStatus(
        ""
    )

alarmInputHighDensity0356Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30356)
)
alarmInputHighDensity0356Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0356Alarm.setStatus(
        ""
    )

alarmInputHighDensity0357Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30357)
)
alarmInputHighDensity0357Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0357Alarm.setStatus(
        ""
    )

alarmInputHighDensity0358Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30358)
)
alarmInputHighDensity0358Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0358Alarm.setStatus(
        ""
    )

alarmInputHighDensity0359Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30359)
)
alarmInputHighDensity0359Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0359Alarm.setStatus(
        ""
    )

alarmInputHighDensity0360Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30360)
)
alarmInputHighDensity0360Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0360Alarm.setStatus(
        ""
    )

alarmInputHighDensity0361Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30361)
)
alarmInputHighDensity0361Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0361Alarm.setStatus(
        ""
    )

alarmInputHighDensity0362Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30362)
)
alarmInputHighDensity0362Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0362Alarm.setStatus(
        ""
    )

alarmInputHighDensity0363Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30363)
)
alarmInputHighDensity0363Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0363Alarm.setStatus(
        ""
    )

alarmInputHighDensity0364Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30364)
)
alarmInputHighDensity0364Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0364Alarm.setStatus(
        ""
    )

alarmInputHighDensity0365Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30365)
)
alarmInputHighDensity0365Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0365Alarm.setStatus(
        ""
    )

alarmInputHighDensity0366Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30366)
)
alarmInputHighDensity0366Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0366Alarm.setStatus(
        ""
    )

alarmInputHighDensity0367Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30367)
)
alarmInputHighDensity0367Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0367Alarm.setStatus(
        ""
    )

alarmInputHighDensity0368Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30368)
)
alarmInputHighDensity0368Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0368Alarm.setStatus(
        ""
    )

alarmInputHighDensity0369Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30369)
)
alarmInputHighDensity0369Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0369Alarm.setStatus(
        ""
    )

alarmInputHighDensity0370Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30370)
)
alarmInputHighDensity0370Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0370Alarm.setStatus(
        ""
    )

alarmInputHighDensity0371Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30371)
)
alarmInputHighDensity0371Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0371Alarm.setStatus(
        ""
    )

alarmInputHighDensity0372Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30372)
)
alarmInputHighDensity0372Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0372Alarm.setStatus(
        ""
    )

alarmInputHighDensity0373Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30373)
)
alarmInputHighDensity0373Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0373Alarm.setStatus(
        ""
    )

alarmInputHighDensity0374Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30374)
)
alarmInputHighDensity0374Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0374Alarm.setStatus(
        ""
    )

alarmInputHighDensity0375Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30375)
)
alarmInputHighDensity0375Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0375Alarm.setStatus(
        ""
    )

alarmInputHighDensity0376Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30376)
)
alarmInputHighDensity0376Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0376Alarm.setStatus(
        ""
    )

alarmInputHighDensity0377Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30377)
)
alarmInputHighDensity0377Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0377Alarm.setStatus(
        ""
    )

alarmInputHighDensity0378Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30378)
)
alarmInputHighDensity0378Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0378Alarm.setStatus(
        ""
    )

alarmInputHighDensity0379Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30379)
)
alarmInputHighDensity0379Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0379Alarm.setStatus(
        ""
    )

alarmInputHighDensity0380Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30380)
)
alarmInputHighDensity0380Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0380Alarm.setStatus(
        ""
    )

alarmInputHighDensity0381Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30381)
)
alarmInputHighDensity0381Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0381Alarm.setStatus(
        ""
    )

alarmInputHighDensity0382Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30382)
)
alarmInputHighDensity0382Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0382Alarm.setStatus(
        ""
    )

alarmInputHighDensity0383Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30383)
)
alarmInputHighDensity0383Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0383Alarm.setStatus(
        ""
    )

alarmInputHighDensity0384Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 30384)
)
alarmInputHighDensity0384Alarm.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0384Alarm.setStatus(
        ""
    )

alarmInputHighDensity0001Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40001)
)
alarmInputHighDensity0001Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0001Normal.setStatus(
        ""
    )

alarmInputHighDensity0002Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40002)
)
alarmInputHighDensity0002Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0002Normal.setStatus(
        ""
    )

alarmInputHighDensity0003Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40003)
)
alarmInputHighDensity0003Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0003Normal.setStatus(
        ""
    )

alarmInputHighDensity0004Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40004)
)
alarmInputHighDensity0004Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0004Normal.setStatus(
        ""
    )

alarmInputHighDensity0005Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40005)
)
alarmInputHighDensity0005Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0005Normal.setStatus(
        ""
    )

alarmInputHighDensity0006Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40006)
)
alarmInputHighDensity0006Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0006Normal.setStatus(
        ""
    )

alarmInputHighDensity0007Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40007)
)
alarmInputHighDensity0007Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0007Normal.setStatus(
        ""
    )

alarmInputHighDensity0008Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40008)
)
alarmInputHighDensity0008Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0008Normal.setStatus(
        ""
    )

alarmInputHighDensity0009Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40009)
)
alarmInputHighDensity0009Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0009Normal.setStatus(
        ""
    )

alarmInputHighDensity0010Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40010)
)
alarmInputHighDensity0010Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0010Normal.setStatus(
        ""
    )

alarmInputHighDensity0011Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40011)
)
alarmInputHighDensity0011Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0011Normal.setStatus(
        ""
    )

alarmInputHighDensity0012Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40012)
)
alarmInputHighDensity0012Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0012Normal.setStatus(
        ""
    )

alarmInputHighDensity0013Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40013)
)
alarmInputHighDensity0013Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0013Normal.setStatus(
        ""
    )

alarmInputHighDensity0014Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40014)
)
alarmInputHighDensity0014Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0014Normal.setStatus(
        ""
    )

alarmInputHighDensity0015Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40015)
)
alarmInputHighDensity0015Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0015Normal.setStatus(
        ""
    )

alarmInputHighDensity0016Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40016)
)
alarmInputHighDensity0016Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0016Normal.setStatus(
        ""
    )

alarmInputHighDensity0017Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40017)
)
alarmInputHighDensity0017Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0017Normal.setStatus(
        ""
    )

alarmInputHighDensity0018Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40018)
)
alarmInputHighDensity0018Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0018Normal.setStatus(
        ""
    )

alarmInputHighDensity0019Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40019)
)
alarmInputHighDensity0019Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0019Normal.setStatus(
        ""
    )

alarmInputHighDensity0020Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40020)
)
alarmInputHighDensity0020Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0020Normal.setStatus(
        ""
    )

alarmInputHighDensity0021Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40021)
)
alarmInputHighDensity0021Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0021Normal.setStatus(
        ""
    )

alarmInputHighDensity0022Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40022)
)
alarmInputHighDensity0022Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0022Normal.setStatus(
        ""
    )

alarmInputHighDensity0023Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40023)
)
alarmInputHighDensity0023Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0023Normal.setStatus(
        ""
    )

alarmInputHighDensity0024Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40024)
)
alarmInputHighDensity0024Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0024Normal.setStatus(
        ""
    )

alarmInputHighDensity0025Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40025)
)
alarmInputHighDensity0025Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0025Normal.setStatus(
        ""
    )

alarmInputHighDensity0026Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40026)
)
alarmInputHighDensity0026Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0026Normal.setStatus(
        ""
    )

alarmInputHighDensity0027Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40027)
)
alarmInputHighDensity0027Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0027Normal.setStatus(
        ""
    )

alarmInputHighDensity0028Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40028)
)
alarmInputHighDensity0028Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0028Normal.setStatus(
        ""
    )

alarmInputHighDensity0029Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40029)
)
alarmInputHighDensity0029Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0029Normal.setStatus(
        ""
    )

alarmInputHighDensity0030Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40030)
)
alarmInputHighDensity0030Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0030Normal.setStatus(
        ""
    )

alarmInputHighDensity0031Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40031)
)
alarmInputHighDensity0031Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0031Normal.setStatus(
        ""
    )

alarmInputHighDensity0032Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40032)
)
alarmInputHighDensity0032Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0032Normal.setStatus(
        ""
    )

alarmInputHighDensity0033Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40033)
)
alarmInputHighDensity0033Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0033Normal.setStatus(
        ""
    )

alarmInputHighDensity0034Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40034)
)
alarmInputHighDensity0034Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0034Normal.setStatus(
        ""
    )

alarmInputHighDensity0035Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40035)
)
alarmInputHighDensity0035Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0035Normal.setStatus(
        ""
    )

alarmInputHighDensity0036Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40036)
)
alarmInputHighDensity0036Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0036Normal.setStatus(
        ""
    )

alarmInputHighDensity0037Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40037)
)
alarmInputHighDensity0037Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0037Normal.setStatus(
        ""
    )

alarmInputHighDensity0038Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40038)
)
alarmInputHighDensity0038Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0038Normal.setStatus(
        ""
    )

alarmInputHighDensity0039Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40039)
)
alarmInputHighDensity0039Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0039Normal.setStatus(
        ""
    )

alarmInputHighDensity0040Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40040)
)
alarmInputHighDensity0040Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0040Normal.setStatus(
        ""
    )

alarmInputHighDensity0041Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40041)
)
alarmInputHighDensity0041Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0041Normal.setStatus(
        ""
    )

alarmInputHighDensity0042Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40042)
)
alarmInputHighDensity0042Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0042Normal.setStatus(
        ""
    )

alarmInputHighDensity0043Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40043)
)
alarmInputHighDensity0043Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0043Normal.setStatus(
        ""
    )

alarmInputHighDensity0044Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40044)
)
alarmInputHighDensity0044Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0044Normal.setStatus(
        ""
    )

alarmInputHighDensity0045Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40045)
)
alarmInputHighDensity0045Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0045Normal.setStatus(
        ""
    )

alarmInputHighDensity0046Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40046)
)
alarmInputHighDensity0046Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0046Normal.setStatus(
        ""
    )

alarmInputHighDensity0047Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40047)
)
alarmInputHighDensity0047Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0047Normal.setStatus(
        ""
    )

alarmInputHighDensity0048Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40048)
)
alarmInputHighDensity0048Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0048Normal.setStatus(
        ""
    )

alarmInputHighDensity0049Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40049)
)
alarmInputHighDensity0049Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0049Normal.setStatus(
        ""
    )

alarmInputHighDensity0050Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40050)
)
alarmInputHighDensity0050Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0050Normal.setStatus(
        ""
    )

alarmInputHighDensity0051Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40051)
)
alarmInputHighDensity0051Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0051Normal.setStatus(
        ""
    )

alarmInputHighDensity0052Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40052)
)
alarmInputHighDensity0052Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0052Normal.setStatus(
        ""
    )

alarmInputHighDensity0053Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40053)
)
alarmInputHighDensity0053Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0053Normal.setStatus(
        ""
    )

alarmInputHighDensity0054Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40054)
)
alarmInputHighDensity0054Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0054Normal.setStatus(
        ""
    )

alarmInputHighDensity0055Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40055)
)
alarmInputHighDensity0055Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0055Normal.setStatus(
        ""
    )

alarmInputHighDensity0056Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40056)
)
alarmInputHighDensity0056Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0056Normal.setStatus(
        ""
    )

alarmInputHighDensity0057Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40057)
)
alarmInputHighDensity0057Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0057Normal.setStatus(
        ""
    )

alarmInputHighDensity0058Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40058)
)
alarmInputHighDensity0058Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0058Normal.setStatus(
        ""
    )

alarmInputHighDensity0059Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40059)
)
alarmInputHighDensity0059Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0059Normal.setStatus(
        ""
    )

alarmInputHighDensity0060Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40060)
)
alarmInputHighDensity0060Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0060Normal.setStatus(
        ""
    )

alarmInputHighDensity0061Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40061)
)
alarmInputHighDensity0061Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0061Normal.setStatus(
        ""
    )

alarmInputHighDensity0062Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40062)
)
alarmInputHighDensity0062Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0062Normal.setStatus(
        ""
    )

alarmInputHighDensity0063Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40063)
)
alarmInputHighDensity0063Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0063Normal.setStatus(
        ""
    )

alarmInputHighDensity0064Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40064)
)
alarmInputHighDensity0064Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0064Normal.setStatus(
        ""
    )

alarmInputHighDensity0065Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40065)
)
alarmInputHighDensity0065Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0065Normal.setStatus(
        ""
    )

alarmInputHighDensity0066Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40066)
)
alarmInputHighDensity0066Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0066Normal.setStatus(
        ""
    )

alarmInputHighDensity0067Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40067)
)
alarmInputHighDensity0067Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0067Normal.setStatus(
        ""
    )

alarmInputHighDensity0068Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40068)
)
alarmInputHighDensity0068Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0068Normal.setStatus(
        ""
    )

alarmInputHighDensity0069Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40069)
)
alarmInputHighDensity0069Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0069Normal.setStatus(
        ""
    )

alarmInputHighDensity0070Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40070)
)
alarmInputHighDensity0070Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0070Normal.setStatus(
        ""
    )

alarmInputHighDensity0071Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40071)
)
alarmInputHighDensity0071Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0071Normal.setStatus(
        ""
    )

alarmInputHighDensity0072Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40072)
)
alarmInputHighDensity0072Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0072Normal.setStatus(
        ""
    )

alarmInputHighDensity0073Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40073)
)
alarmInputHighDensity0073Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0073Normal.setStatus(
        ""
    )

alarmInputHighDensity0074Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40074)
)
alarmInputHighDensity0074Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0074Normal.setStatus(
        ""
    )

alarmInputHighDensity0075Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40075)
)
alarmInputHighDensity0075Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0075Normal.setStatus(
        ""
    )

alarmInputHighDensity0076Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40076)
)
alarmInputHighDensity0076Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0076Normal.setStatus(
        ""
    )

alarmInputHighDensity0077Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40077)
)
alarmInputHighDensity0077Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0077Normal.setStatus(
        ""
    )

alarmInputHighDensity0078Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40078)
)
alarmInputHighDensity0078Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0078Normal.setStatus(
        ""
    )

alarmInputHighDensity0079Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40079)
)
alarmInputHighDensity0079Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0079Normal.setStatus(
        ""
    )

alarmInputHighDensity0080Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40080)
)
alarmInputHighDensity0080Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0080Normal.setStatus(
        ""
    )

alarmInputHighDensity0081Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40081)
)
alarmInputHighDensity0081Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0081Normal.setStatus(
        ""
    )

alarmInputHighDensity0082Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40082)
)
alarmInputHighDensity0082Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0082Normal.setStatus(
        ""
    )

alarmInputHighDensity0083Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40083)
)
alarmInputHighDensity0083Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0083Normal.setStatus(
        ""
    )

alarmInputHighDensity0084Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40084)
)
alarmInputHighDensity0084Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0084Normal.setStatus(
        ""
    )

alarmInputHighDensity0085Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40085)
)
alarmInputHighDensity0085Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0085Normal.setStatus(
        ""
    )

alarmInputHighDensity0086Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40086)
)
alarmInputHighDensity0086Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0086Normal.setStatus(
        ""
    )

alarmInputHighDensity0087Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40087)
)
alarmInputHighDensity0087Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0087Normal.setStatus(
        ""
    )

alarmInputHighDensity0088Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40088)
)
alarmInputHighDensity0088Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0088Normal.setStatus(
        ""
    )

alarmInputHighDensity0089Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40089)
)
alarmInputHighDensity0089Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0089Normal.setStatus(
        ""
    )

alarmInputHighDensity0090Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40090)
)
alarmInputHighDensity0090Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0090Normal.setStatus(
        ""
    )

alarmInputHighDensity0091Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40091)
)
alarmInputHighDensity0091Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0091Normal.setStatus(
        ""
    )

alarmInputHighDensity0092Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40092)
)
alarmInputHighDensity0092Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0092Normal.setStatus(
        ""
    )

alarmInputHighDensity0093Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40093)
)
alarmInputHighDensity0093Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0093Normal.setStatus(
        ""
    )

alarmInputHighDensity0094Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40094)
)
alarmInputHighDensity0094Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0094Normal.setStatus(
        ""
    )

alarmInputHighDensity0095Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40095)
)
alarmInputHighDensity0095Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0095Normal.setStatus(
        ""
    )

alarmInputHighDensity0096Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40096)
)
alarmInputHighDensity0096Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0096Normal.setStatus(
        ""
    )

alarmInputHighDensity0097Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40097)
)
alarmInputHighDensity0097Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0097Normal.setStatus(
        ""
    )

alarmInputHighDensity0098Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40098)
)
alarmInputHighDensity0098Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0098Normal.setStatus(
        ""
    )

alarmInputHighDensity0099Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40099)
)
alarmInputHighDensity0099Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0099Normal.setStatus(
        ""
    )

alarmInputHighDensity0100Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40100)
)
alarmInputHighDensity0100Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0100Normal.setStatus(
        ""
    )

alarmInputHighDensity0101Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40101)
)
alarmInputHighDensity0101Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0101Normal.setStatus(
        ""
    )

alarmInputHighDensity0102Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40102)
)
alarmInputHighDensity0102Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0102Normal.setStatus(
        ""
    )

alarmInputHighDensity0103Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40103)
)
alarmInputHighDensity0103Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0103Normal.setStatus(
        ""
    )

alarmInputHighDensity0104Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40104)
)
alarmInputHighDensity0104Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0104Normal.setStatus(
        ""
    )

alarmInputHighDensity0105Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40105)
)
alarmInputHighDensity0105Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0105Normal.setStatus(
        ""
    )

alarmInputHighDensity0106Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40106)
)
alarmInputHighDensity0106Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0106Normal.setStatus(
        ""
    )

alarmInputHighDensity0107Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40107)
)
alarmInputHighDensity0107Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0107Normal.setStatus(
        ""
    )

alarmInputHighDensity0108Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40108)
)
alarmInputHighDensity0108Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0108Normal.setStatus(
        ""
    )

alarmInputHighDensity0109Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40109)
)
alarmInputHighDensity0109Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0109Normal.setStatus(
        ""
    )

alarmInputHighDensity0110Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40110)
)
alarmInputHighDensity0110Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0110Normal.setStatus(
        ""
    )

alarmInputHighDensity0111Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40111)
)
alarmInputHighDensity0111Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0111Normal.setStatus(
        ""
    )

alarmInputHighDensity0112Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40112)
)
alarmInputHighDensity0112Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0112Normal.setStatus(
        ""
    )

alarmInputHighDensity0113Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40113)
)
alarmInputHighDensity0113Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0113Normal.setStatus(
        ""
    )

alarmInputHighDensity0114Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40114)
)
alarmInputHighDensity0114Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0114Normal.setStatus(
        ""
    )

alarmInputHighDensity0115Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40115)
)
alarmInputHighDensity0115Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0115Normal.setStatus(
        ""
    )

alarmInputHighDensity0116Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40116)
)
alarmInputHighDensity0116Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0116Normal.setStatus(
        ""
    )

alarmInputHighDensity0117Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40117)
)
alarmInputHighDensity0117Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0117Normal.setStatus(
        ""
    )

alarmInputHighDensity0118Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40118)
)
alarmInputHighDensity0118Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0118Normal.setStatus(
        ""
    )

alarmInputHighDensity0119Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40119)
)
alarmInputHighDensity0119Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0119Normal.setStatus(
        ""
    )

alarmInputHighDensity0120Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40120)
)
alarmInputHighDensity0120Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0120Normal.setStatus(
        ""
    )

alarmInputHighDensity0121Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40121)
)
alarmInputHighDensity0121Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0121Normal.setStatus(
        ""
    )

alarmInputHighDensity0122Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40122)
)
alarmInputHighDensity0122Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0122Normal.setStatus(
        ""
    )

alarmInputHighDensity0123Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40123)
)
alarmInputHighDensity0123Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0123Normal.setStatus(
        ""
    )

alarmInputHighDensity0124Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40124)
)
alarmInputHighDensity0124Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0124Normal.setStatus(
        ""
    )

alarmInputHighDensity0125Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40125)
)
alarmInputHighDensity0125Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0125Normal.setStatus(
        ""
    )

alarmInputHighDensity0126Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40126)
)
alarmInputHighDensity0126Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0126Normal.setStatus(
        ""
    )

alarmInputHighDensity0127Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40127)
)
alarmInputHighDensity0127Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0127Normal.setStatus(
        ""
    )

alarmInputHighDensity0128Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40128)
)
alarmInputHighDensity0128Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0128Normal.setStatus(
        ""
    )

alarmInputHighDensity0129Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40129)
)
alarmInputHighDensity0129Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0129Normal.setStatus(
        ""
    )

alarmInputHighDensity0130Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40130)
)
alarmInputHighDensity0130Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0130Normal.setStatus(
        ""
    )

alarmInputHighDensity0131Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40131)
)
alarmInputHighDensity0131Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0131Normal.setStatus(
        ""
    )

alarmInputHighDensity0132Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40132)
)
alarmInputHighDensity0132Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0132Normal.setStatus(
        ""
    )

alarmInputHighDensity0133Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40133)
)
alarmInputHighDensity0133Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0133Normal.setStatus(
        ""
    )

alarmInputHighDensity0134Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40134)
)
alarmInputHighDensity0134Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0134Normal.setStatus(
        ""
    )

alarmInputHighDensity0135Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40135)
)
alarmInputHighDensity0135Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0135Normal.setStatus(
        ""
    )

alarmInputHighDensity0136Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40136)
)
alarmInputHighDensity0136Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0136Normal.setStatus(
        ""
    )

alarmInputHighDensity0137Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40137)
)
alarmInputHighDensity0137Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0137Normal.setStatus(
        ""
    )

alarmInputHighDensity0138Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40138)
)
alarmInputHighDensity0138Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0138Normal.setStatus(
        ""
    )

alarmInputHighDensity0139Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40139)
)
alarmInputHighDensity0139Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0139Normal.setStatus(
        ""
    )

alarmInputHighDensity0140Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40140)
)
alarmInputHighDensity0140Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0140Normal.setStatus(
        ""
    )

alarmInputHighDensity0141Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40141)
)
alarmInputHighDensity0141Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0141Normal.setStatus(
        ""
    )

alarmInputHighDensity0142Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40142)
)
alarmInputHighDensity0142Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0142Normal.setStatus(
        ""
    )

alarmInputHighDensity0143Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40143)
)
alarmInputHighDensity0143Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0143Normal.setStatus(
        ""
    )

alarmInputHighDensity0144Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40144)
)
alarmInputHighDensity0144Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0144Normal.setStatus(
        ""
    )

alarmInputHighDensity0145Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40145)
)
alarmInputHighDensity0145Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0145Normal.setStatus(
        ""
    )

alarmInputHighDensity0146Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40146)
)
alarmInputHighDensity0146Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0146Normal.setStatus(
        ""
    )

alarmInputHighDensity0147Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40147)
)
alarmInputHighDensity0147Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0147Normal.setStatus(
        ""
    )

alarmInputHighDensity0148Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40148)
)
alarmInputHighDensity0148Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0148Normal.setStatus(
        ""
    )

alarmInputHighDensity0149Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40149)
)
alarmInputHighDensity0149Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0149Normal.setStatus(
        ""
    )

alarmInputHighDensity0150Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40150)
)
alarmInputHighDensity0150Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0150Normal.setStatus(
        ""
    )

alarmInputHighDensity0151Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40151)
)
alarmInputHighDensity0151Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0151Normal.setStatus(
        ""
    )

alarmInputHighDensity0152Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40152)
)
alarmInputHighDensity0152Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0152Normal.setStatus(
        ""
    )

alarmInputHighDensity0153Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40153)
)
alarmInputHighDensity0153Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0153Normal.setStatus(
        ""
    )

alarmInputHighDensity0154Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40154)
)
alarmInputHighDensity0154Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0154Normal.setStatus(
        ""
    )

alarmInputHighDensity0155Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40155)
)
alarmInputHighDensity0155Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0155Normal.setStatus(
        ""
    )

alarmInputHighDensity0156Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40156)
)
alarmInputHighDensity0156Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0156Normal.setStatus(
        ""
    )

alarmInputHighDensity0157Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40157)
)
alarmInputHighDensity0157Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0157Normal.setStatus(
        ""
    )

alarmInputHighDensity0158Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40158)
)
alarmInputHighDensity0158Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0158Normal.setStatus(
        ""
    )

alarmInputHighDensity0159Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40159)
)
alarmInputHighDensity0159Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0159Normal.setStatus(
        ""
    )

alarmInputHighDensity0160Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40160)
)
alarmInputHighDensity0160Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0160Normal.setStatus(
        ""
    )

alarmInputHighDensity0161Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40161)
)
alarmInputHighDensity0161Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0161Normal.setStatus(
        ""
    )

alarmInputHighDensity0162Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40162)
)
alarmInputHighDensity0162Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0162Normal.setStatus(
        ""
    )

alarmInputHighDensity0163Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40163)
)
alarmInputHighDensity0163Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0163Normal.setStatus(
        ""
    )

alarmInputHighDensity0164Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40164)
)
alarmInputHighDensity0164Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0164Normal.setStatus(
        ""
    )

alarmInputHighDensity0165Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40165)
)
alarmInputHighDensity0165Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0165Normal.setStatus(
        ""
    )

alarmInputHighDensity0166Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40166)
)
alarmInputHighDensity0166Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0166Normal.setStatus(
        ""
    )

alarmInputHighDensity0167Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40167)
)
alarmInputHighDensity0167Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0167Normal.setStatus(
        ""
    )

alarmInputHighDensity0168Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40168)
)
alarmInputHighDensity0168Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0168Normal.setStatus(
        ""
    )

alarmInputHighDensity0169Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40169)
)
alarmInputHighDensity0169Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0169Normal.setStatus(
        ""
    )

alarmInputHighDensity0170Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40170)
)
alarmInputHighDensity0170Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0170Normal.setStatus(
        ""
    )

alarmInputHighDensity0171Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40171)
)
alarmInputHighDensity0171Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0171Normal.setStatus(
        ""
    )

alarmInputHighDensity0172Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40172)
)
alarmInputHighDensity0172Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0172Normal.setStatus(
        ""
    )

alarmInputHighDensity0173Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40173)
)
alarmInputHighDensity0173Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0173Normal.setStatus(
        ""
    )

alarmInputHighDensity0174Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40174)
)
alarmInputHighDensity0174Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0174Normal.setStatus(
        ""
    )

alarmInputHighDensity0175Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40175)
)
alarmInputHighDensity0175Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0175Normal.setStatus(
        ""
    )

alarmInputHighDensity0176Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40176)
)
alarmInputHighDensity0176Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0176Normal.setStatus(
        ""
    )

alarmInputHighDensity0177Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40177)
)
alarmInputHighDensity0177Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0177Normal.setStatus(
        ""
    )

alarmInputHighDensity0178Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40178)
)
alarmInputHighDensity0178Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0178Normal.setStatus(
        ""
    )

alarmInputHighDensity0179Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40179)
)
alarmInputHighDensity0179Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0179Normal.setStatus(
        ""
    )

alarmInputHighDensity0180Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40180)
)
alarmInputHighDensity0180Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0180Normal.setStatus(
        ""
    )

alarmInputHighDensity0181Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40181)
)
alarmInputHighDensity0181Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0181Normal.setStatus(
        ""
    )

alarmInputHighDensity0182Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40182)
)
alarmInputHighDensity0182Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0182Normal.setStatus(
        ""
    )

alarmInputHighDensity0183Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40183)
)
alarmInputHighDensity0183Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0183Normal.setStatus(
        ""
    )

alarmInputHighDensity0184Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40184)
)
alarmInputHighDensity0184Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0184Normal.setStatus(
        ""
    )

alarmInputHighDensity0185Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40185)
)
alarmInputHighDensity0185Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0185Normal.setStatus(
        ""
    )

alarmInputHighDensity0186Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40186)
)
alarmInputHighDensity0186Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0186Normal.setStatus(
        ""
    )

alarmInputHighDensity0187Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40187)
)
alarmInputHighDensity0187Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0187Normal.setStatus(
        ""
    )

alarmInputHighDensity0188Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40188)
)
alarmInputHighDensity0188Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0188Normal.setStatus(
        ""
    )

alarmInputHighDensity0189Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40189)
)
alarmInputHighDensity0189Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0189Normal.setStatus(
        ""
    )

alarmInputHighDensity0190Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40190)
)
alarmInputHighDensity0190Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0190Normal.setStatus(
        ""
    )

alarmInputHighDensity0191Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40191)
)
alarmInputHighDensity0191Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0191Normal.setStatus(
        ""
    )

alarmInputHighDensity0192Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40192)
)
alarmInputHighDensity0192Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0192Normal.setStatus(
        ""
    )

alarmInputHighDensity0193Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40193)
)
alarmInputHighDensity0193Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0193Normal.setStatus(
        ""
    )

alarmInputHighDensity0194Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40194)
)
alarmInputHighDensity0194Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0194Normal.setStatus(
        ""
    )

alarmInputHighDensity0195Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40195)
)
alarmInputHighDensity0195Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0195Normal.setStatus(
        ""
    )

alarmInputHighDensity0196Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40196)
)
alarmInputHighDensity0196Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0196Normal.setStatus(
        ""
    )

alarmInputHighDensity0197Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40197)
)
alarmInputHighDensity0197Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0197Normal.setStatus(
        ""
    )

alarmInputHighDensity0198Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40198)
)
alarmInputHighDensity0198Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0198Normal.setStatus(
        ""
    )

alarmInputHighDensity0199Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40199)
)
alarmInputHighDensity0199Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0199Normal.setStatus(
        ""
    )

alarmInputHighDensity0200Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40200)
)
alarmInputHighDensity0200Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0200Normal.setStatus(
        ""
    )

alarmInputHighDensity0201Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40201)
)
alarmInputHighDensity0201Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0201Normal.setStatus(
        ""
    )

alarmInputHighDensity0202Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40202)
)
alarmInputHighDensity0202Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0202Normal.setStatus(
        ""
    )

alarmInputHighDensity0203Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40203)
)
alarmInputHighDensity0203Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0203Normal.setStatus(
        ""
    )

alarmInputHighDensity0204Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40204)
)
alarmInputHighDensity0204Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0204Normal.setStatus(
        ""
    )

alarmInputHighDensity0205Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40205)
)
alarmInputHighDensity0205Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0205Normal.setStatus(
        ""
    )

alarmInputHighDensity0206Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40206)
)
alarmInputHighDensity0206Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0206Normal.setStatus(
        ""
    )

alarmInputHighDensity0207Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40207)
)
alarmInputHighDensity0207Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0207Normal.setStatus(
        ""
    )

alarmInputHighDensity0208Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40208)
)
alarmInputHighDensity0208Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0208Normal.setStatus(
        ""
    )

alarmInputHighDensity0209Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40209)
)
alarmInputHighDensity0209Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0209Normal.setStatus(
        ""
    )

alarmInputHighDensity0210Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40210)
)
alarmInputHighDensity0210Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0210Normal.setStatus(
        ""
    )

alarmInputHighDensity0211Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40211)
)
alarmInputHighDensity0211Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0211Normal.setStatus(
        ""
    )

alarmInputHighDensity0212Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40212)
)
alarmInputHighDensity0212Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0212Normal.setStatus(
        ""
    )

alarmInputHighDensity0213Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40213)
)
alarmInputHighDensity0213Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0213Normal.setStatus(
        ""
    )

alarmInputHighDensity0214Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40214)
)
alarmInputHighDensity0214Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0214Normal.setStatus(
        ""
    )

alarmInputHighDensity0215Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40215)
)
alarmInputHighDensity0215Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0215Normal.setStatus(
        ""
    )

alarmInputHighDensity0216Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40216)
)
alarmInputHighDensity0216Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0216Normal.setStatus(
        ""
    )

alarmInputHighDensity0217Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40217)
)
alarmInputHighDensity0217Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0217Normal.setStatus(
        ""
    )

alarmInputHighDensity0218Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40218)
)
alarmInputHighDensity0218Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0218Normal.setStatus(
        ""
    )

alarmInputHighDensity0219Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40219)
)
alarmInputHighDensity0219Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0219Normal.setStatus(
        ""
    )

alarmInputHighDensity0220Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40220)
)
alarmInputHighDensity0220Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0220Normal.setStatus(
        ""
    )

alarmInputHighDensity0221Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40221)
)
alarmInputHighDensity0221Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0221Normal.setStatus(
        ""
    )

alarmInputHighDensity0222Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40222)
)
alarmInputHighDensity0222Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0222Normal.setStatus(
        ""
    )

alarmInputHighDensity0223Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40223)
)
alarmInputHighDensity0223Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0223Normal.setStatus(
        ""
    )

alarmInputHighDensity0224Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40224)
)
alarmInputHighDensity0224Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0224Normal.setStatus(
        ""
    )

alarmInputHighDensity0225Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40225)
)
alarmInputHighDensity0225Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0225Normal.setStatus(
        ""
    )

alarmInputHighDensity0226Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40226)
)
alarmInputHighDensity0226Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0226Normal.setStatus(
        ""
    )

alarmInputHighDensity0227Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40227)
)
alarmInputHighDensity0227Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0227Normal.setStatus(
        ""
    )

alarmInputHighDensity0228Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40228)
)
alarmInputHighDensity0228Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0228Normal.setStatus(
        ""
    )

alarmInputHighDensity0229Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40229)
)
alarmInputHighDensity0229Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0229Normal.setStatus(
        ""
    )

alarmInputHighDensity0230Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40230)
)
alarmInputHighDensity0230Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0230Normal.setStatus(
        ""
    )

alarmInputHighDensity0231Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40231)
)
alarmInputHighDensity0231Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0231Normal.setStatus(
        ""
    )

alarmInputHighDensity0232Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40232)
)
alarmInputHighDensity0232Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0232Normal.setStatus(
        ""
    )

alarmInputHighDensity0233Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40233)
)
alarmInputHighDensity0233Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0233Normal.setStatus(
        ""
    )

alarmInputHighDensity0234Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40234)
)
alarmInputHighDensity0234Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0234Normal.setStatus(
        ""
    )

alarmInputHighDensity0235Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40235)
)
alarmInputHighDensity0235Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0235Normal.setStatus(
        ""
    )

alarmInputHighDensity0236Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40236)
)
alarmInputHighDensity0236Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0236Normal.setStatus(
        ""
    )

alarmInputHighDensity0237Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40237)
)
alarmInputHighDensity0237Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0237Normal.setStatus(
        ""
    )

alarmInputHighDensity0238Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40238)
)
alarmInputHighDensity0238Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0238Normal.setStatus(
        ""
    )

alarmInputHighDensity0239Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40239)
)
alarmInputHighDensity0239Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0239Normal.setStatus(
        ""
    )

alarmInputHighDensity0240Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40240)
)
alarmInputHighDensity0240Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0240Normal.setStatus(
        ""
    )

alarmInputHighDensity0241Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40241)
)
alarmInputHighDensity0241Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0241Normal.setStatus(
        ""
    )

alarmInputHighDensity0242Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40242)
)
alarmInputHighDensity0242Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0242Normal.setStatus(
        ""
    )

alarmInputHighDensity0243Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40243)
)
alarmInputHighDensity0243Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0243Normal.setStatus(
        ""
    )

alarmInputHighDensity0244Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40244)
)
alarmInputHighDensity0244Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0244Normal.setStatus(
        ""
    )

alarmInputHighDensity0245Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40245)
)
alarmInputHighDensity0245Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0245Normal.setStatus(
        ""
    )

alarmInputHighDensity0246Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40246)
)
alarmInputHighDensity0246Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0246Normal.setStatus(
        ""
    )

alarmInputHighDensity0247Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40247)
)
alarmInputHighDensity0247Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0247Normal.setStatus(
        ""
    )

alarmInputHighDensity0248Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40248)
)
alarmInputHighDensity0248Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0248Normal.setStatus(
        ""
    )

alarmInputHighDensity0249Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40249)
)
alarmInputHighDensity0249Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0249Normal.setStatus(
        ""
    )

alarmInputHighDensity0250Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40250)
)
alarmInputHighDensity0250Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0250Normal.setStatus(
        ""
    )

alarmInputHighDensity0251Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40251)
)
alarmInputHighDensity0251Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0251Normal.setStatus(
        ""
    )

alarmInputHighDensity0252Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40252)
)
alarmInputHighDensity0252Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0252Normal.setStatus(
        ""
    )

alarmInputHighDensity0253Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40253)
)
alarmInputHighDensity0253Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0253Normal.setStatus(
        ""
    )

alarmInputHighDensity0254Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40254)
)
alarmInputHighDensity0254Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0254Normal.setStatus(
        ""
    )

alarmInputHighDensity0255Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40255)
)
alarmInputHighDensity0255Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0255Normal.setStatus(
        ""
    )

alarmInputHighDensity0256Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40256)
)
alarmInputHighDensity0256Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0256Normal.setStatus(
        ""
    )

alarmInputHighDensity0257Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40257)
)
alarmInputHighDensity0257Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0257Normal.setStatus(
        ""
    )

alarmInputHighDensity0258Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40258)
)
alarmInputHighDensity0258Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0258Normal.setStatus(
        ""
    )

alarmInputHighDensity0259Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40259)
)
alarmInputHighDensity0259Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0259Normal.setStatus(
        ""
    )

alarmInputHighDensity0260Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40260)
)
alarmInputHighDensity0260Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0260Normal.setStatus(
        ""
    )

alarmInputHighDensity0261Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40261)
)
alarmInputHighDensity0261Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0261Normal.setStatus(
        ""
    )

alarmInputHighDensity0262Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40262)
)
alarmInputHighDensity0262Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0262Normal.setStatus(
        ""
    )

alarmInputHighDensity0263Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40263)
)
alarmInputHighDensity0263Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0263Normal.setStatus(
        ""
    )

alarmInputHighDensity0264Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40264)
)
alarmInputHighDensity0264Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0264Normal.setStatus(
        ""
    )

alarmInputHighDensity0265Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40265)
)
alarmInputHighDensity0265Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0265Normal.setStatus(
        ""
    )

alarmInputHighDensity0266Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40266)
)
alarmInputHighDensity0266Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0266Normal.setStatus(
        ""
    )

alarmInputHighDensity0267Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40267)
)
alarmInputHighDensity0267Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0267Normal.setStatus(
        ""
    )

alarmInputHighDensity0268Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40268)
)
alarmInputHighDensity0268Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0268Normal.setStatus(
        ""
    )

alarmInputHighDensity0269Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40269)
)
alarmInputHighDensity0269Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0269Normal.setStatus(
        ""
    )

alarmInputHighDensity0270Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40270)
)
alarmInputHighDensity0270Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0270Normal.setStatus(
        ""
    )

alarmInputHighDensity0271Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40271)
)
alarmInputHighDensity0271Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0271Normal.setStatus(
        ""
    )

alarmInputHighDensity0272Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40272)
)
alarmInputHighDensity0272Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0272Normal.setStatus(
        ""
    )

alarmInputHighDensity0273Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40273)
)
alarmInputHighDensity0273Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0273Normal.setStatus(
        ""
    )

alarmInputHighDensity0274Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40274)
)
alarmInputHighDensity0274Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0274Normal.setStatus(
        ""
    )

alarmInputHighDensity0275Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40275)
)
alarmInputHighDensity0275Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0275Normal.setStatus(
        ""
    )

alarmInputHighDensity0276Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40276)
)
alarmInputHighDensity0276Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0276Normal.setStatus(
        ""
    )

alarmInputHighDensity0277Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40277)
)
alarmInputHighDensity0277Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0277Normal.setStatus(
        ""
    )

alarmInputHighDensity0278Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40278)
)
alarmInputHighDensity0278Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0278Normal.setStatus(
        ""
    )

alarmInputHighDensity0279Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40279)
)
alarmInputHighDensity0279Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0279Normal.setStatus(
        ""
    )

alarmInputHighDensity0280Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40280)
)
alarmInputHighDensity0280Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0280Normal.setStatus(
        ""
    )

alarmInputHighDensity0281Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40281)
)
alarmInputHighDensity0281Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0281Normal.setStatus(
        ""
    )

alarmInputHighDensity0282Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40282)
)
alarmInputHighDensity0282Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0282Normal.setStatus(
        ""
    )

alarmInputHighDensity0283Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40283)
)
alarmInputHighDensity0283Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0283Normal.setStatus(
        ""
    )

alarmInputHighDensity0284Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40284)
)
alarmInputHighDensity0284Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0284Normal.setStatus(
        ""
    )

alarmInputHighDensity0285Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40285)
)
alarmInputHighDensity0285Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0285Normal.setStatus(
        ""
    )

alarmInputHighDensity0286Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40286)
)
alarmInputHighDensity0286Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0286Normal.setStatus(
        ""
    )

alarmInputHighDensity0287Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40287)
)
alarmInputHighDensity0287Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0287Normal.setStatus(
        ""
    )

alarmInputHighDensity0288Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40288)
)
alarmInputHighDensity0288Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0288Normal.setStatus(
        ""
    )

alarmInputHighDensity0289Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40289)
)
alarmInputHighDensity0289Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0289Normal.setStatus(
        ""
    )

alarmInputHighDensity0290Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40290)
)
alarmInputHighDensity0290Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0290Normal.setStatus(
        ""
    )

alarmInputHighDensity0291Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40291)
)
alarmInputHighDensity0291Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0291Normal.setStatus(
        ""
    )

alarmInputHighDensity0292Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40292)
)
alarmInputHighDensity0292Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0292Normal.setStatus(
        ""
    )

alarmInputHighDensity0293Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40293)
)
alarmInputHighDensity0293Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0293Normal.setStatus(
        ""
    )

alarmInputHighDensity0294Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40294)
)
alarmInputHighDensity0294Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0294Normal.setStatus(
        ""
    )

alarmInputHighDensity0295Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40295)
)
alarmInputHighDensity0295Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0295Normal.setStatus(
        ""
    )

alarmInputHighDensity0296Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40296)
)
alarmInputHighDensity0296Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0296Normal.setStatus(
        ""
    )

alarmInputHighDensity0297Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40297)
)
alarmInputHighDensity0297Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0297Normal.setStatus(
        ""
    )

alarmInputHighDensity0298Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40298)
)
alarmInputHighDensity0298Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0298Normal.setStatus(
        ""
    )

alarmInputHighDensity0299Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40299)
)
alarmInputHighDensity0299Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0299Normal.setStatus(
        ""
    )

alarmInputHighDensity0300Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40300)
)
alarmInputHighDensity0300Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0300Normal.setStatus(
        ""
    )

alarmInputHighDensity0301Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40301)
)
alarmInputHighDensity0301Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0301Normal.setStatus(
        ""
    )

alarmInputHighDensity0302Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40302)
)
alarmInputHighDensity0302Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0302Normal.setStatus(
        ""
    )

alarmInputHighDensity0303Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40303)
)
alarmInputHighDensity0303Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0303Normal.setStatus(
        ""
    )

alarmInputHighDensity0304Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40304)
)
alarmInputHighDensity0304Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0304Normal.setStatus(
        ""
    )

alarmInputHighDensity0305Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40305)
)
alarmInputHighDensity0305Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0305Normal.setStatus(
        ""
    )

alarmInputHighDensity0306Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40306)
)
alarmInputHighDensity0306Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0306Normal.setStatus(
        ""
    )

alarmInputHighDensity0307Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40307)
)
alarmInputHighDensity0307Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0307Normal.setStatus(
        ""
    )

alarmInputHighDensity0308Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40308)
)
alarmInputHighDensity0308Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0308Normal.setStatus(
        ""
    )

alarmInputHighDensity0309Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40309)
)
alarmInputHighDensity0309Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0309Normal.setStatus(
        ""
    )

alarmInputHighDensity0310Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40310)
)
alarmInputHighDensity0310Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0310Normal.setStatus(
        ""
    )

alarmInputHighDensity0311Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40311)
)
alarmInputHighDensity0311Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0311Normal.setStatus(
        ""
    )

alarmInputHighDensity0312Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40312)
)
alarmInputHighDensity0312Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0312Normal.setStatus(
        ""
    )

alarmInputHighDensity0313Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40313)
)
alarmInputHighDensity0313Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0313Normal.setStatus(
        ""
    )

alarmInputHighDensity0314Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40314)
)
alarmInputHighDensity0314Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0314Normal.setStatus(
        ""
    )

alarmInputHighDensity0315Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40315)
)
alarmInputHighDensity0315Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0315Normal.setStatus(
        ""
    )

alarmInputHighDensity0316Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40316)
)
alarmInputHighDensity0316Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0316Normal.setStatus(
        ""
    )

alarmInputHighDensity0317Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40317)
)
alarmInputHighDensity0317Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0317Normal.setStatus(
        ""
    )

alarmInputHighDensity0318Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40318)
)
alarmInputHighDensity0318Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0318Normal.setStatus(
        ""
    )

alarmInputHighDensity0319Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40319)
)
alarmInputHighDensity0319Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0319Normal.setStatus(
        ""
    )

alarmInputHighDensity0320Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40320)
)
alarmInputHighDensity0320Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0320Normal.setStatus(
        ""
    )

alarmInputHighDensity0321Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40321)
)
alarmInputHighDensity0321Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0321Normal.setStatus(
        ""
    )

alarmInputHighDensity0322Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40322)
)
alarmInputHighDensity0322Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0322Normal.setStatus(
        ""
    )

alarmInputHighDensity0323Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40323)
)
alarmInputHighDensity0323Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0323Normal.setStatus(
        ""
    )

alarmInputHighDensity0324Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40324)
)
alarmInputHighDensity0324Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0324Normal.setStatus(
        ""
    )

alarmInputHighDensity0325Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40325)
)
alarmInputHighDensity0325Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0325Normal.setStatus(
        ""
    )

alarmInputHighDensity0326Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40326)
)
alarmInputHighDensity0326Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0326Normal.setStatus(
        ""
    )

alarmInputHighDensity0327Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40327)
)
alarmInputHighDensity0327Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0327Normal.setStatus(
        ""
    )

alarmInputHighDensity0328Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40328)
)
alarmInputHighDensity0328Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0328Normal.setStatus(
        ""
    )

alarmInputHighDensity0329Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40329)
)
alarmInputHighDensity0329Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0329Normal.setStatus(
        ""
    )

alarmInputHighDensity0330Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40330)
)
alarmInputHighDensity0330Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0330Normal.setStatus(
        ""
    )

alarmInputHighDensity0331Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40331)
)
alarmInputHighDensity0331Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0331Normal.setStatus(
        ""
    )

alarmInputHighDensity0332Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40332)
)
alarmInputHighDensity0332Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0332Normal.setStatus(
        ""
    )

alarmInputHighDensity0333Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40333)
)
alarmInputHighDensity0333Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0333Normal.setStatus(
        ""
    )

alarmInputHighDensity0334Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40334)
)
alarmInputHighDensity0334Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0334Normal.setStatus(
        ""
    )

alarmInputHighDensity0335Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40335)
)
alarmInputHighDensity0335Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0335Normal.setStatus(
        ""
    )

alarmInputHighDensity0336Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40336)
)
alarmInputHighDensity0336Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0336Normal.setStatus(
        ""
    )

alarmInputHighDensity0337Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40337)
)
alarmInputHighDensity0337Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0337Normal.setStatus(
        ""
    )

alarmInputHighDensity0338Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40338)
)
alarmInputHighDensity0338Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0338Normal.setStatus(
        ""
    )

alarmInputHighDensity0339Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40339)
)
alarmInputHighDensity0339Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0339Normal.setStatus(
        ""
    )

alarmInputHighDensity0340Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40340)
)
alarmInputHighDensity0340Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0340Normal.setStatus(
        ""
    )

alarmInputHighDensity0341Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40341)
)
alarmInputHighDensity0341Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0341Normal.setStatus(
        ""
    )

alarmInputHighDensity0342Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40342)
)
alarmInputHighDensity0342Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0342Normal.setStatus(
        ""
    )

alarmInputHighDensity0343Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40343)
)
alarmInputHighDensity0343Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0343Normal.setStatus(
        ""
    )

alarmInputHighDensity0344Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40344)
)
alarmInputHighDensity0344Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0344Normal.setStatus(
        ""
    )

alarmInputHighDensity0345Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40345)
)
alarmInputHighDensity0345Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0345Normal.setStatus(
        ""
    )

alarmInputHighDensity0346Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40346)
)
alarmInputHighDensity0346Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0346Normal.setStatus(
        ""
    )

alarmInputHighDensity0347Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40347)
)
alarmInputHighDensity0347Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0347Normal.setStatus(
        ""
    )

alarmInputHighDensity0348Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40348)
)
alarmInputHighDensity0348Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0348Normal.setStatus(
        ""
    )

alarmInputHighDensity0349Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40349)
)
alarmInputHighDensity0349Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0349Normal.setStatus(
        ""
    )

alarmInputHighDensity0350Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40350)
)
alarmInputHighDensity0350Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0350Normal.setStatus(
        ""
    )

alarmInputHighDensity0351Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40351)
)
alarmInputHighDensity0351Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0351Normal.setStatus(
        ""
    )

alarmInputHighDensity0352Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40352)
)
alarmInputHighDensity0352Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0352Normal.setStatus(
        ""
    )

alarmInputHighDensity0353Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40353)
)
alarmInputHighDensity0353Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0353Normal.setStatus(
        ""
    )

alarmInputHighDensity0354Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40354)
)
alarmInputHighDensity0354Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0354Normal.setStatus(
        ""
    )

alarmInputHighDensity0355Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40355)
)
alarmInputHighDensity0355Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0355Normal.setStatus(
        ""
    )

alarmInputHighDensity0356Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40356)
)
alarmInputHighDensity0356Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0356Normal.setStatus(
        ""
    )

alarmInputHighDensity0357Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40357)
)
alarmInputHighDensity0357Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0357Normal.setStatus(
        ""
    )

alarmInputHighDensity0358Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40358)
)
alarmInputHighDensity0358Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0358Normal.setStatus(
        ""
    )

alarmInputHighDensity0359Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40359)
)
alarmInputHighDensity0359Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0359Normal.setStatus(
        ""
    )

alarmInputHighDensity0360Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40360)
)
alarmInputHighDensity0360Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0360Normal.setStatus(
        ""
    )

alarmInputHighDensity0361Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40361)
)
alarmInputHighDensity0361Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0361Normal.setStatus(
        ""
    )

alarmInputHighDensity0362Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40362)
)
alarmInputHighDensity0362Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0362Normal.setStatus(
        ""
    )

alarmInputHighDensity0363Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40363)
)
alarmInputHighDensity0363Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0363Normal.setStatus(
        ""
    )

alarmInputHighDensity0364Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40364)
)
alarmInputHighDensity0364Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0364Normal.setStatus(
        ""
    )

alarmInputHighDensity0365Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40365)
)
alarmInputHighDensity0365Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0365Normal.setStatus(
        ""
    )

alarmInputHighDensity0366Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40366)
)
alarmInputHighDensity0366Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0366Normal.setStatus(
        ""
    )

alarmInputHighDensity0367Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40367)
)
alarmInputHighDensity0367Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0367Normal.setStatus(
        ""
    )

alarmInputHighDensity0368Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40368)
)
alarmInputHighDensity0368Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0368Normal.setStatus(
        ""
    )

alarmInputHighDensity0369Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40369)
)
alarmInputHighDensity0369Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0369Normal.setStatus(
        ""
    )

alarmInputHighDensity0370Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40370)
)
alarmInputHighDensity0370Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0370Normal.setStatus(
        ""
    )

alarmInputHighDensity0371Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40371)
)
alarmInputHighDensity0371Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0371Normal.setStatus(
        ""
    )

alarmInputHighDensity0372Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40372)
)
alarmInputHighDensity0372Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0372Normal.setStatus(
        ""
    )

alarmInputHighDensity0373Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40373)
)
alarmInputHighDensity0373Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0373Normal.setStatus(
        ""
    )

alarmInputHighDensity0374Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40374)
)
alarmInputHighDensity0374Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0374Normal.setStatus(
        ""
    )

alarmInputHighDensity0375Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40375)
)
alarmInputHighDensity0375Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0375Normal.setStatus(
        ""
    )

alarmInputHighDensity0376Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40376)
)
alarmInputHighDensity0376Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0376Normal.setStatus(
        ""
    )

alarmInputHighDensity0377Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40377)
)
alarmInputHighDensity0377Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0377Normal.setStatus(
        ""
    )

alarmInputHighDensity0378Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40378)
)
alarmInputHighDensity0378Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0378Normal.setStatus(
        ""
    )

alarmInputHighDensity0379Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40379)
)
alarmInputHighDensity0379Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0379Normal.setStatus(
        ""
    )

alarmInputHighDensity0380Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40380)
)
alarmInputHighDensity0380Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0380Normal.setStatus(
        ""
    )

alarmInputHighDensity0381Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40381)
)
alarmInputHighDensity0381Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0381Normal.setStatus(
        ""
    )

alarmInputHighDensity0382Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40382)
)
alarmInputHighDensity0382Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0382Normal.setStatus(
        ""
    )

alarmInputHighDensity0383Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40383)
)
alarmInputHighDensity0383Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0383Normal.setStatus(
        ""
    )

alarmInputHighDensity0384Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 0, 40384)
)
alarmInputHighDensity0384Normal.setObjects(
      *(("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputValue"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPort"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputStatus"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSlot"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputPoint"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputZone"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputRelatedEquipment"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputSiteId"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputManufacturer"),
        ("MRV-IN-REACH-CHARACTER-MIB", "basicAlarmMasterInputModel"))
)
if mibBuilder.loadTexts:
    alarmInputHighDensity0384Normal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-ALARM-EXTENSION-MIB",
    **{"alarmInputHighDensity0001Alarm": alarmInputHighDensity0001Alarm,
       "alarmInputHighDensity0002Alarm": alarmInputHighDensity0002Alarm,
       "alarmInputHighDensity0003Alarm": alarmInputHighDensity0003Alarm,
       "alarmInputHighDensity0004Alarm": alarmInputHighDensity0004Alarm,
       "alarmInputHighDensity0005Alarm": alarmInputHighDensity0005Alarm,
       "alarmInputHighDensity0006Alarm": alarmInputHighDensity0006Alarm,
       "alarmInputHighDensity0007Alarm": alarmInputHighDensity0007Alarm,
       "alarmInputHighDensity0008Alarm": alarmInputHighDensity0008Alarm,
       "alarmInputHighDensity0009Alarm": alarmInputHighDensity0009Alarm,
       "alarmInputHighDensity0010Alarm": alarmInputHighDensity0010Alarm,
       "alarmInputHighDensity0011Alarm": alarmInputHighDensity0011Alarm,
       "alarmInputHighDensity0012Alarm": alarmInputHighDensity0012Alarm,
       "alarmInputHighDensity0013Alarm": alarmInputHighDensity0013Alarm,
       "alarmInputHighDensity0014Alarm": alarmInputHighDensity0014Alarm,
       "alarmInputHighDensity0015Alarm": alarmInputHighDensity0015Alarm,
       "alarmInputHighDensity0016Alarm": alarmInputHighDensity0016Alarm,
       "alarmInputHighDensity0017Alarm": alarmInputHighDensity0017Alarm,
       "alarmInputHighDensity0018Alarm": alarmInputHighDensity0018Alarm,
       "alarmInputHighDensity0019Alarm": alarmInputHighDensity0019Alarm,
       "alarmInputHighDensity0020Alarm": alarmInputHighDensity0020Alarm,
       "alarmInputHighDensity0021Alarm": alarmInputHighDensity0021Alarm,
       "alarmInputHighDensity0022Alarm": alarmInputHighDensity0022Alarm,
       "alarmInputHighDensity0023Alarm": alarmInputHighDensity0023Alarm,
       "alarmInputHighDensity0024Alarm": alarmInputHighDensity0024Alarm,
       "alarmInputHighDensity0025Alarm": alarmInputHighDensity0025Alarm,
       "alarmInputHighDensity0026Alarm": alarmInputHighDensity0026Alarm,
       "alarmInputHighDensity0027Alarm": alarmInputHighDensity0027Alarm,
       "alarmInputHighDensity0028Alarm": alarmInputHighDensity0028Alarm,
       "alarmInputHighDensity0029Alarm": alarmInputHighDensity0029Alarm,
       "alarmInputHighDensity0030Alarm": alarmInputHighDensity0030Alarm,
       "alarmInputHighDensity0031Alarm": alarmInputHighDensity0031Alarm,
       "alarmInputHighDensity0032Alarm": alarmInputHighDensity0032Alarm,
       "alarmInputHighDensity0033Alarm": alarmInputHighDensity0033Alarm,
       "alarmInputHighDensity0034Alarm": alarmInputHighDensity0034Alarm,
       "alarmInputHighDensity0035Alarm": alarmInputHighDensity0035Alarm,
       "alarmInputHighDensity0036Alarm": alarmInputHighDensity0036Alarm,
       "alarmInputHighDensity0037Alarm": alarmInputHighDensity0037Alarm,
       "alarmInputHighDensity0038Alarm": alarmInputHighDensity0038Alarm,
       "alarmInputHighDensity0039Alarm": alarmInputHighDensity0039Alarm,
       "alarmInputHighDensity0040Alarm": alarmInputHighDensity0040Alarm,
       "alarmInputHighDensity0041Alarm": alarmInputHighDensity0041Alarm,
       "alarmInputHighDensity0042Alarm": alarmInputHighDensity0042Alarm,
       "alarmInputHighDensity0043Alarm": alarmInputHighDensity0043Alarm,
       "alarmInputHighDensity0044Alarm": alarmInputHighDensity0044Alarm,
       "alarmInputHighDensity0045Alarm": alarmInputHighDensity0045Alarm,
       "alarmInputHighDensity0046Alarm": alarmInputHighDensity0046Alarm,
       "alarmInputHighDensity0047Alarm": alarmInputHighDensity0047Alarm,
       "alarmInputHighDensity0048Alarm": alarmInputHighDensity0048Alarm,
       "alarmInputHighDensity0049Alarm": alarmInputHighDensity0049Alarm,
       "alarmInputHighDensity0050Alarm": alarmInputHighDensity0050Alarm,
       "alarmInputHighDensity0051Alarm": alarmInputHighDensity0051Alarm,
       "alarmInputHighDensity0052Alarm": alarmInputHighDensity0052Alarm,
       "alarmInputHighDensity0053Alarm": alarmInputHighDensity0053Alarm,
       "alarmInputHighDensity0054Alarm": alarmInputHighDensity0054Alarm,
       "alarmInputHighDensity0055Alarm": alarmInputHighDensity0055Alarm,
       "alarmInputHighDensity0056Alarm": alarmInputHighDensity0056Alarm,
       "alarmInputHighDensity0057Alarm": alarmInputHighDensity0057Alarm,
       "alarmInputHighDensity0058Alarm": alarmInputHighDensity0058Alarm,
       "alarmInputHighDensity0059Alarm": alarmInputHighDensity0059Alarm,
       "alarmInputHighDensity0060Alarm": alarmInputHighDensity0060Alarm,
       "alarmInputHighDensity0061Alarm": alarmInputHighDensity0061Alarm,
       "alarmInputHighDensity0062Alarm": alarmInputHighDensity0062Alarm,
       "alarmInputHighDensity0063Alarm": alarmInputHighDensity0063Alarm,
       "alarmInputHighDensity0064Alarm": alarmInputHighDensity0064Alarm,
       "alarmInputHighDensity0065Alarm": alarmInputHighDensity0065Alarm,
       "alarmInputHighDensity0066Alarm": alarmInputHighDensity0066Alarm,
       "alarmInputHighDensity0067Alarm": alarmInputHighDensity0067Alarm,
       "alarmInputHighDensity0068Alarm": alarmInputHighDensity0068Alarm,
       "alarmInputHighDensity0069Alarm": alarmInputHighDensity0069Alarm,
       "alarmInputHighDensity0070Alarm": alarmInputHighDensity0070Alarm,
       "alarmInputHighDensity0071Alarm": alarmInputHighDensity0071Alarm,
       "alarmInputHighDensity0072Alarm": alarmInputHighDensity0072Alarm,
       "alarmInputHighDensity0073Alarm": alarmInputHighDensity0073Alarm,
       "alarmInputHighDensity0074Alarm": alarmInputHighDensity0074Alarm,
       "alarmInputHighDensity0075Alarm": alarmInputHighDensity0075Alarm,
       "alarmInputHighDensity0076Alarm": alarmInputHighDensity0076Alarm,
       "alarmInputHighDensity0077Alarm": alarmInputHighDensity0077Alarm,
       "alarmInputHighDensity0078Alarm": alarmInputHighDensity0078Alarm,
       "alarmInputHighDensity0079Alarm": alarmInputHighDensity0079Alarm,
       "alarmInputHighDensity0080Alarm": alarmInputHighDensity0080Alarm,
       "alarmInputHighDensity0081Alarm": alarmInputHighDensity0081Alarm,
       "alarmInputHighDensity0082Alarm": alarmInputHighDensity0082Alarm,
       "alarmInputHighDensity0083Alarm": alarmInputHighDensity0083Alarm,
       "alarmInputHighDensity0084Alarm": alarmInputHighDensity0084Alarm,
       "alarmInputHighDensity0085Alarm": alarmInputHighDensity0085Alarm,
       "alarmInputHighDensity0086Alarm": alarmInputHighDensity0086Alarm,
       "alarmInputHighDensity0087Alarm": alarmInputHighDensity0087Alarm,
       "alarmInputHighDensity0088Alarm": alarmInputHighDensity0088Alarm,
       "alarmInputHighDensity0089Alarm": alarmInputHighDensity0089Alarm,
       "alarmInputHighDensity0090Alarm": alarmInputHighDensity0090Alarm,
       "alarmInputHighDensity0091Alarm": alarmInputHighDensity0091Alarm,
       "alarmInputHighDensity0092Alarm": alarmInputHighDensity0092Alarm,
       "alarmInputHighDensity0093Alarm": alarmInputHighDensity0093Alarm,
       "alarmInputHighDensity0094Alarm": alarmInputHighDensity0094Alarm,
       "alarmInputHighDensity0095Alarm": alarmInputHighDensity0095Alarm,
       "alarmInputHighDensity0096Alarm": alarmInputHighDensity0096Alarm,
       "alarmInputHighDensity0097Alarm": alarmInputHighDensity0097Alarm,
       "alarmInputHighDensity0098Alarm": alarmInputHighDensity0098Alarm,
       "alarmInputHighDensity0099Alarm": alarmInputHighDensity0099Alarm,
       "alarmInputHighDensity0100Alarm": alarmInputHighDensity0100Alarm,
       "alarmInputHighDensity0101Alarm": alarmInputHighDensity0101Alarm,
       "alarmInputHighDensity0102Alarm": alarmInputHighDensity0102Alarm,
       "alarmInputHighDensity0103Alarm": alarmInputHighDensity0103Alarm,
       "alarmInputHighDensity0104Alarm": alarmInputHighDensity0104Alarm,
       "alarmInputHighDensity0105Alarm": alarmInputHighDensity0105Alarm,
       "alarmInputHighDensity0106Alarm": alarmInputHighDensity0106Alarm,
       "alarmInputHighDensity0107Alarm": alarmInputHighDensity0107Alarm,
       "alarmInputHighDensity0108Alarm": alarmInputHighDensity0108Alarm,
       "alarmInputHighDensity0109Alarm": alarmInputHighDensity0109Alarm,
       "alarmInputHighDensity0110Alarm": alarmInputHighDensity0110Alarm,
       "alarmInputHighDensity0111Alarm": alarmInputHighDensity0111Alarm,
       "alarmInputHighDensity0112Alarm": alarmInputHighDensity0112Alarm,
       "alarmInputHighDensity0113Alarm": alarmInputHighDensity0113Alarm,
       "alarmInputHighDensity0114Alarm": alarmInputHighDensity0114Alarm,
       "alarmInputHighDensity0115Alarm": alarmInputHighDensity0115Alarm,
       "alarmInputHighDensity0116Alarm": alarmInputHighDensity0116Alarm,
       "alarmInputHighDensity0117Alarm": alarmInputHighDensity0117Alarm,
       "alarmInputHighDensity0118Alarm": alarmInputHighDensity0118Alarm,
       "alarmInputHighDensity0119Alarm": alarmInputHighDensity0119Alarm,
       "alarmInputHighDensity0120Alarm": alarmInputHighDensity0120Alarm,
       "alarmInputHighDensity0121Alarm": alarmInputHighDensity0121Alarm,
       "alarmInputHighDensity0122Alarm": alarmInputHighDensity0122Alarm,
       "alarmInputHighDensity0123Alarm": alarmInputHighDensity0123Alarm,
       "alarmInputHighDensity0124Alarm": alarmInputHighDensity0124Alarm,
       "alarmInputHighDensity0125Alarm": alarmInputHighDensity0125Alarm,
       "alarmInputHighDensity0126Alarm": alarmInputHighDensity0126Alarm,
       "alarmInputHighDensity0127Alarm": alarmInputHighDensity0127Alarm,
       "alarmInputHighDensity0128Alarm": alarmInputHighDensity0128Alarm,
       "alarmInputHighDensity0129Alarm": alarmInputHighDensity0129Alarm,
       "alarmInputHighDensity0130Alarm": alarmInputHighDensity0130Alarm,
       "alarmInputHighDensity0131Alarm": alarmInputHighDensity0131Alarm,
       "alarmInputHighDensity0132Alarm": alarmInputHighDensity0132Alarm,
       "alarmInputHighDensity0133Alarm": alarmInputHighDensity0133Alarm,
       "alarmInputHighDensity0134Alarm": alarmInputHighDensity0134Alarm,
       "alarmInputHighDensity0135Alarm": alarmInputHighDensity0135Alarm,
       "alarmInputHighDensity0136Alarm": alarmInputHighDensity0136Alarm,
       "alarmInputHighDensity0137Alarm": alarmInputHighDensity0137Alarm,
       "alarmInputHighDensity0138Alarm": alarmInputHighDensity0138Alarm,
       "alarmInputHighDensity0139Alarm": alarmInputHighDensity0139Alarm,
       "alarmInputHighDensity0140Alarm": alarmInputHighDensity0140Alarm,
       "alarmInputHighDensity0141Alarm": alarmInputHighDensity0141Alarm,
       "alarmInputHighDensity0142Alarm": alarmInputHighDensity0142Alarm,
       "alarmInputHighDensity0143Alarm": alarmInputHighDensity0143Alarm,
       "alarmInputHighDensity0144Alarm": alarmInputHighDensity0144Alarm,
       "alarmInputHighDensity0145Alarm": alarmInputHighDensity0145Alarm,
       "alarmInputHighDensity0146Alarm": alarmInputHighDensity0146Alarm,
       "alarmInputHighDensity0147Alarm": alarmInputHighDensity0147Alarm,
       "alarmInputHighDensity0148Alarm": alarmInputHighDensity0148Alarm,
       "alarmInputHighDensity0149Alarm": alarmInputHighDensity0149Alarm,
       "alarmInputHighDensity0150Alarm": alarmInputHighDensity0150Alarm,
       "alarmInputHighDensity0151Alarm": alarmInputHighDensity0151Alarm,
       "alarmInputHighDensity0152Alarm": alarmInputHighDensity0152Alarm,
       "alarmInputHighDensity0153Alarm": alarmInputHighDensity0153Alarm,
       "alarmInputHighDensity0154Alarm": alarmInputHighDensity0154Alarm,
       "alarmInputHighDensity0155Alarm": alarmInputHighDensity0155Alarm,
       "alarmInputHighDensity0156Alarm": alarmInputHighDensity0156Alarm,
       "alarmInputHighDensity0157Alarm": alarmInputHighDensity0157Alarm,
       "alarmInputHighDensity0158Alarm": alarmInputHighDensity0158Alarm,
       "alarmInputHighDensity0159Alarm": alarmInputHighDensity0159Alarm,
       "alarmInputHighDensity0160Alarm": alarmInputHighDensity0160Alarm,
       "alarmInputHighDensity0161Alarm": alarmInputHighDensity0161Alarm,
       "alarmInputHighDensity0162Alarm": alarmInputHighDensity0162Alarm,
       "alarmInputHighDensity0163Alarm": alarmInputHighDensity0163Alarm,
       "alarmInputHighDensity0164Alarm": alarmInputHighDensity0164Alarm,
       "alarmInputHighDensity0165Alarm": alarmInputHighDensity0165Alarm,
       "alarmInputHighDensity0166Alarm": alarmInputHighDensity0166Alarm,
       "alarmInputHighDensity0167Alarm": alarmInputHighDensity0167Alarm,
       "alarmInputHighDensity0168Alarm": alarmInputHighDensity0168Alarm,
       "alarmInputHighDensity0169Alarm": alarmInputHighDensity0169Alarm,
       "alarmInputHighDensity0170Alarm": alarmInputHighDensity0170Alarm,
       "alarmInputHighDensity0171Alarm": alarmInputHighDensity0171Alarm,
       "alarmInputHighDensity0172Alarm": alarmInputHighDensity0172Alarm,
       "alarmInputHighDensity0173Alarm": alarmInputHighDensity0173Alarm,
       "alarmInputHighDensity0174Alarm": alarmInputHighDensity0174Alarm,
       "alarmInputHighDensity0175Alarm": alarmInputHighDensity0175Alarm,
       "alarmInputHighDensity0176Alarm": alarmInputHighDensity0176Alarm,
       "alarmInputHighDensity0177Alarm": alarmInputHighDensity0177Alarm,
       "alarmInputHighDensity0178Alarm": alarmInputHighDensity0178Alarm,
       "alarmInputHighDensity0179Alarm": alarmInputHighDensity0179Alarm,
       "alarmInputHighDensity0180Alarm": alarmInputHighDensity0180Alarm,
       "alarmInputHighDensity0181Alarm": alarmInputHighDensity0181Alarm,
       "alarmInputHighDensity0182Alarm": alarmInputHighDensity0182Alarm,
       "alarmInputHighDensity0183Alarm": alarmInputHighDensity0183Alarm,
       "alarmInputHighDensity0184Alarm": alarmInputHighDensity0184Alarm,
       "alarmInputHighDensity0185Alarm": alarmInputHighDensity0185Alarm,
       "alarmInputHighDensity0186Alarm": alarmInputHighDensity0186Alarm,
       "alarmInputHighDensity0187Alarm": alarmInputHighDensity0187Alarm,
       "alarmInputHighDensity0188Alarm": alarmInputHighDensity0188Alarm,
       "alarmInputHighDensity0189Alarm": alarmInputHighDensity0189Alarm,
       "alarmInputHighDensity0190Alarm": alarmInputHighDensity0190Alarm,
       "alarmInputHighDensity0191Alarm": alarmInputHighDensity0191Alarm,
       "alarmInputHighDensity0192Alarm": alarmInputHighDensity0192Alarm,
       "alarmInputHighDensity0193Alarm": alarmInputHighDensity0193Alarm,
       "alarmInputHighDensity0194Alarm": alarmInputHighDensity0194Alarm,
       "alarmInputHighDensity0195Alarm": alarmInputHighDensity0195Alarm,
       "alarmInputHighDensity0196Alarm": alarmInputHighDensity0196Alarm,
       "alarmInputHighDensity0197Alarm": alarmInputHighDensity0197Alarm,
       "alarmInputHighDensity0198Alarm": alarmInputHighDensity0198Alarm,
       "alarmInputHighDensity0199Alarm": alarmInputHighDensity0199Alarm,
       "alarmInputHighDensity0200Alarm": alarmInputHighDensity0200Alarm,
       "alarmInputHighDensity0201Alarm": alarmInputHighDensity0201Alarm,
       "alarmInputHighDensity0202Alarm": alarmInputHighDensity0202Alarm,
       "alarmInputHighDensity0203Alarm": alarmInputHighDensity0203Alarm,
       "alarmInputHighDensity0204Alarm": alarmInputHighDensity0204Alarm,
       "alarmInputHighDensity0205Alarm": alarmInputHighDensity0205Alarm,
       "alarmInputHighDensity0206Alarm": alarmInputHighDensity0206Alarm,
       "alarmInputHighDensity0207Alarm": alarmInputHighDensity0207Alarm,
       "alarmInputHighDensity0208Alarm": alarmInputHighDensity0208Alarm,
       "alarmInputHighDensity0209Alarm": alarmInputHighDensity0209Alarm,
       "alarmInputHighDensity0210Alarm": alarmInputHighDensity0210Alarm,
       "alarmInputHighDensity0211Alarm": alarmInputHighDensity0211Alarm,
       "alarmInputHighDensity0212Alarm": alarmInputHighDensity0212Alarm,
       "alarmInputHighDensity0213Alarm": alarmInputHighDensity0213Alarm,
       "alarmInputHighDensity0214Alarm": alarmInputHighDensity0214Alarm,
       "alarmInputHighDensity0215Alarm": alarmInputHighDensity0215Alarm,
       "alarmInputHighDensity0216Alarm": alarmInputHighDensity0216Alarm,
       "alarmInputHighDensity0217Alarm": alarmInputHighDensity0217Alarm,
       "alarmInputHighDensity0218Alarm": alarmInputHighDensity0218Alarm,
       "alarmInputHighDensity0219Alarm": alarmInputHighDensity0219Alarm,
       "alarmInputHighDensity0220Alarm": alarmInputHighDensity0220Alarm,
       "alarmInputHighDensity0221Alarm": alarmInputHighDensity0221Alarm,
       "alarmInputHighDensity0222Alarm": alarmInputHighDensity0222Alarm,
       "alarmInputHighDensity0223Alarm": alarmInputHighDensity0223Alarm,
       "alarmInputHighDensity0224Alarm": alarmInputHighDensity0224Alarm,
       "alarmInputHighDensity0225Alarm": alarmInputHighDensity0225Alarm,
       "alarmInputHighDensity0226Alarm": alarmInputHighDensity0226Alarm,
       "alarmInputHighDensity0227Alarm": alarmInputHighDensity0227Alarm,
       "alarmInputHighDensity0228Alarm": alarmInputHighDensity0228Alarm,
       "alarmInputHighDensity0229Alarm": alarmInputHighDensity0229Alarm,
       "alarmInputHighDensity0230Alarm": alarmInputHighDensity0230Alarm,
       "alarmInputHighDensity0231Alarm": alarmInputHighDensity0231Alarm,
       "alarmInputHighDensity0232Alarm": alarmInputHighDensity0232Alarm,
       "alarmInputHighDensity0233Alarm": alarmInputHighDensity0233Alarm,
       "alarmInputHighDensity0234Alarm": alarmInputHighDensity0234Alarm,
       "alarmInputHighDensity0235Alarm": alarmInputHighDensity0235Alarm,
       "alarmInputHighDensity0236Alarm": alarmInputHighDensity0236Alarm,
       "alarmInputHighDensity0237Alarm": alarmInputHighDensity0237Alarm,
       "alarmInputHighDensity0238Alarm": alarmInputHighDensity0238Alarm,
       "alarmInputHighDensity0239Alarm": alarmInputHighDensity0239Alarm,
       "alarmInputHighDensity0240Alarm": alarmInputHighDensity0240Alarm,
       "alarmInputHighDensity0241Alarm": alarmInputHighDensity0241Alarm,
       "alarmInputHighDensity0242Alarm": alarmInputHighDensity0242Alarm,
       "alarmInputHighDensity0243Alarm": alarmInputHighDensity0243Alarm,
       "alarmInputHighDensity0244Alarm": alarmInputHighDensity0244Alarm,
       "alarmInputHighDensity0245Alarm": alarmInputHighDensity0245Alarm,
       "alarmInputHighDensity0246Alarm": alarmInputHighDensity0246Alarm,
       "alarmInputHighDensity0247Alarm": alarmInputHighDensity0247Alarm,
       "alarmInputHighDensity0248Alarm": alarmInputHighDensity0248Alarm,
       "alarmInputHighDensity0249Alarm": alarmInputHighDensity0249Alarm,
       "alarmInputHighDensity0250Alarm": alarmInputHighDensity0250Alarm,
       "alarmInputHighDensity0251Alarm": alarmInputHighDensity0251Alarm,
       "alarmInputHighDensity0252Alarm": alarmInputHighDensity0252Alarm,
       "alarmInputHighDensity0253Alarm": alarmInputHighDensity0253Alarm,
       "alarmInputHighDensity0254Alarm": alarmInputHighDensity0254Alarm,
       "alarmInputHighDensity0255Alarm": alarmInputHighDensity0255Alarm,
       "alarmInputHighDensity0256Alarm": alarmInputHighDensity0256Alarm,
       "alarmInputHighDensity0257Alarm": alarmInputHighDensity0257Alarm,
       "alarmInputHighDensity0258Alarm": alarmInputHighDensity0258Alarm,
       "alarmInputHighDensity0259Alarm": alarmInputHighDensity0259Alarm,
       "alarmInputHighDensity0260Alarm": alarmInputHighDensity0260Alarm,
       "alarmInputHighDensity0261Alarm": alarmInputHighDensity0261Alarm,
       "alarmInputHighDensity0262Alarm": alarmInputHighDensity0262Alarm,
       "alarmInputHighDensity0263Alarm": alarmInputHighDensity0263Alarm,
       "alarmInputHighDensity0264Alarm": alarmInputHighDensity0264Alarm,
       "alarmInputHighDensity0265Alarm": alarmInputHighDensity0265Alarm,
       "alarmInputHighDensity0266Alarm": alarmInputHighDensity0266Alarm,
       "alarmInputHighDensity0267Alarm": alarmInputHighDensity0267Alarm,
       "alarmInputHighDensity0268Alarm": alarmInputHighDensity0268Alarm,
       "alarmInputHighDensity0269Alarm": alarmInputHighDensity0269Alarm,
       "alarmInputHighDensity0270Alarm": alarmInputHighDensity0270Alarm,
       "alarmInputHighDensity0271Alarm": alarmInputHighDensity0271Alarm,
       "alarmInputHighDensity0272Alarm": alarmInputHighDensity0272Alarm,
       "alarmInputHighDensity0273Alarm": alarmInputHighDensity0273Alarm,
       "alarmInputHighDensity0274Alarm": alarmInputHighDensity0274Alarm,
       "alarmInputHighDensity0275Alarm": alarmInputHighDensity0275Alarm,
       "alarmInputHighDensity0276Alarm": alarmInputHighDensity0276Alarm,
       "alarmInputHighDensity0277Alarm": alarmInputHighDensity0277Alarm,
       "alarmInputHighDensity0278Alarm": alarmInputHighDensity0278Alarm,
       "alarmInputHighDensity0279Alarm": alarmInputHighDensity0279Alarm,
       "alarmInputHighDensity0280Alarm": alarmInputHighDensity0280Alarm,
       "alarmInputHighDensity0281Alarm": alarmInputHighDensity0281Alarm,
       "alarmInputHighDensity0282Alarm": alarmInputHighDensity0282Alarm,
       "alarmInputHighDensity0283Alarm": alarmInputHighDensity0283Alarm,
       "alarmInputHighDensity0284Alarm": alarmInputHighDensity0284Alarm,
       "alarmInputHighDensity0285Alarm": alarmInputHighDensity0285Alarm,
       "alarmInputHighDensity0286Alarm": alarmInputHighDensity0286Alarm,
       "alarmInputHighDensity0287Alarm": alarmInputHighDensity0287Alarm,
       "alarmInputHighDensity0288Alarm": alarmInputHighDensity0288Alarm,
       "alarmInputHighDensity0289Alarm": alarmInputHighDensity0289Alarm,
       "alarmInputHighDensity0290Alarm": alarmInputHighDensity0290Alarm,
       "alarmInputHighDensity0291Alarm": alarmInputHighDensity0291Alarm,
       "alarmInputHighDensity0292Alarm": alarmInputHighDensity0292Alarm,
       "alarmInputHighDensity0293Alarm": alarmInputHighDensity0293Alarm,
       "alarmInputHighDensity0294Alarm": alarmInputHighDensity0294Alarm,
       "alarmInputHighDensity0295Alarm": alarmInputHighDensity0295Alarm,
       "alarmInputHighDensity0296Alarm": alarmInputHighDensity0296Alarm,
       "alarmInputHighDensity0297Alarm": alarmInputHighDensity0297Alarm,
       "alarmInputHighDensity0298Alarm": alarmInputHighDensity0298Alarm,
       "alarmInputHighDensity0299Alarm": alarmInputHighDensity0299Alarm,
       "alarmInputHighDensity0300Alarm": alarmInputHighDensity0300Alarm,
       "alarmInputHighDensity0301Alarm": alarmInputHighDensity0301Alarm,
       "alarmInputHighDensity0302Alarm": alarmInputHighDensity0302Alarm,
       "alarmInputHighDensity0303Alarm": alarmInputHighDensity0303Alarm,
       "alarmInputHighDensity0304Alarm": alarmInputHighDensity0304Alarm,
       "alarmInputHighDensity0305Alarm": alarmInputHighDensity0305Alarm,
       "alarmInputHighDensity0306Alarm": alarmInputHighDensity0306Alarm,
       "alarmInputHighDensity0307Alarm": alarmInputHighDensity0307Alarm,
       "alarmInputHighDensity0308Alarm": alarmInputHighDensity0308Alarm,
       "alarmInputHighDensity0309Alarm": alarmInputHighDensity0309Alarm,
       "alarmInputHighDensity0310Alarm": alarmInputHighDensity0310Alarm,
       "alarmInputHighDensity0311Alarm": alarmInputHighDensity0311Alarm,
       "alarmInputHighDensity0312Alarm": alarmInputHighDensity0312Alarm,
       "alarmInputHighDensity0313Alarm": alarmInputHighDensity0313Alarm,
       "alarmInputHighDensity0314Alarm": alarmInputHighDensity0314Alarm,
       "alarmInputHighDensity0315Alarm": alarmInputHighDensity0315Alarm,
       "alarmInputHighDensity0316Alarm": alarmInputHighDensity0316Alarm,
       "alarmInputHighDensity0317Alarm": alarmInputHighDensity0317Alarm,
       "alarmInputHighDensity0318Alarm": alarmInputHighDensity0318Alarm,
       "alarmInputHighDensity0319Alarm": alarmInputHighDensity0319Alarm,
       "alarmInputHighDensity0320Alarm": alarmInputHighDensity0320Alarm,
       "alarmInputHighDensity0321Alarm": alarmInputHighDensity0321Alarm,
       "alarmInputHighDensity0322Alarm": alarmInputHighDensity0322Alarm,
       "alarmInputHighDensity0323Alarm": alarmInputHighDensity0323Alarm,
       "alarmInputHighDensity0324Alarm": alarmInputHighDensity0324Alarm,
       "alarmInputHighDensity0325Alarm": alarmInputHighDensity0325Alarm,
       "alarmInputHighDensity0326Alarm": alarmInputHighDensity0326Alarm,
       "alarmInputHighDensity0327Alarm": alarmInputHighDensity0327Alarm,
       "alarmInputHighDensity0328Alarm": alarmInputHighDensity0328Alarm,
       "alarmInputHighDensity0329Alarm": alarmInputHighDensity0329Alarm,
       "alarmInputHighDensity0330Alarm": alarmInputHighDensity0330Alarm,
       "alarmInputHighDensity0331Alarm": alarmInputHighDensity0331Alarm,
       "alarmInputHighDensity0332Alarm": alarmInputHighDensity0332Alarm,
       "alarmInputHighDensity0333Alarm": alarmInputHighDensity0333Alarm,
       "alarmInputHighDensity0334Alarm": alarmInputHighDensity0334Alarm,
       "alarmInputHighDensity0335Alarm": alarmInputHighDensity0335Alarm,
       "alarmInputHighDensity0336Alarm": alarmInputHighDensity0336Alarm,
       "alarmInputHighDensity0337Alarm": alarmInputHighDensity0337Alarm,
       "alarmInputHighDensity0338Alarm": alarmInputHighDensity0338Alarm,
       "alarmInputHighDensity0339Alarm": alarmInputHighDensity0339Alarm,
       "alarmInputHighDensity0340Alarm": alarmInputHighDensity0340Alarm,
       "alarmInputHighDensity0341Alarm": alarmInputHighDensity0341Alarm,
       "alarmInputHighDensity0342Alarm": alarmInputHighDensity0342Alarm,
       "alarmInputHighDensity0343Alarm": alarmInputHighDensity0343Alarm,
       "alarmInputHighDensity0344Alarm": alarmInputHighDensity0344Alarm,
       "alarmInputHighDensity0345Alarm": alarmInputHighDensity0345Alarm,
       "alarmInputHighDensity0346Alarm": alarmInputHighDensity0346Alarm,
       "alarmInputHighDensity0347Alarm": alarmInputHighDensity0347Alarm,
       "alarmInputHighDensity0348Alarm": alarmInputHighDensity0348Alarm,
       "alarmInputHighDensity0349Alarm": alarmInputHighDensity0349Alarm,
       "alarmInputHighDensity0350Alarm": alarmInputHighDensity0350Alarm,
       "alarmInputHighDensity0351Alarm": alarmInputHighDensity0351Alarm,
       "alarmInputHighDensity0352Alarm": alarmInputHighDensity0352Alarm,
       "alarmInputHighDensity0353Alarm": alarmInputHighDensity0353Alarm,
       "alarmInputHighDensity0354Alarm": alarmInputHighDensity0354Alarm,
       "alarmInputHighDensity0355Alarm": alarmInputHighDensity0355Alarm,
       "alarmInputHighDensity0356Alarm": alarmInputHighDensity0356Alarm,
       "alarmInputHighDensity0357Alarm": alarmInputHighDensity0357Alarm,
       "alarmInputHighDensity0358Alarm": alarmInputHighDensity0358Alarm,
       "alarmInputHighDensity0359Alarm": alarmInputHighDensity0359Alarm,
       "alarmInputHighDensity0360Alarm": alarmInputHighDensity0360Alarm,
       "alarmInputHighDensity0361Alarm": alarmInputHighDensity0361Alarm,
       "alarmInputHighDensity0362Alarm": alarmInputHighDensity0362Alarm,
       "alarmInputHighDensity0363Alarm": alarmInputHighDensity0363Alarm,
       "alarmInputHighDensity0364Alarm": alarmInputHighDensity0364Alarm,
       "alarmInputHighDensity0365Alarm": alarmInputHighDensity0365Alarm,
       "alarmInputHighDensity0366Alarm": alarmInputHighDensity0366Alarm,
       "alarmInputHighDensity0367Alarm": alarmInputHighDensity0367Alarm,
       "alarmInputHighDensity0368Alarm": alarmInputHighDensity0368Alarm,
       "alarmInputHighDensity0369Alarm": alarmInputHighDensity0369Alarm,
       "alarmInputHighDensity0370Alarm": alarmInputHighDensity0370Alarm,
       "alarmInputHighDensity0371Alarm": alarmInputHighDensity0371Alarm,
       "alarmInputHighDensity0372Alarm": alarmInputHighDensity0372Alarm,
       "alarmInputHighDensity0373Alarm": alarmInputHighDensity0373Alarm,
       "alarmInputHighDensity0374Alarm": alarmInputHighDensity0374Alarm,
       "alarmInputHighDensity0375Alarm": alarmInputHighDensity0375Alarm,
       "alarmInputHighDensity0376Alarm": alarmInputHighDensity0376Alarm,
       "alarmInputHighDensity0377Alarm": alarmInputHighDensity0377Alarm,
       "alarmInputHighDensity0378Alarm": alarmInputHighDensity0378Alarm,
       "alarmInputHighDensity0379Alarm": alarmInputHighDensity0379Alarm,
       "alarmInputHighDensity0380Alarm": alarmInputHighDensity0380Alarm,
       "alarmInputHighDensity0381Alarm": alarmInputHighDensity0381Alarm,
       "alarmInputHighDensity0382Alarm": alarmInputHighDensity0382Alarm,
       "alarmInputHighDensity0383Alarm": alarmInputHighDensity0383Alarm,
       "alarmInputHighDensity0384Alarm": alarmInputHighDensity0384Alarm,
       "alarmInputHighDensity0001Normal": alarmInputHighDensity0001Normal,
       "alarmInputHighDensity0002Normal": alarmInputHighDensity0002Normal,
       "alarmInputHighDensity0003Normal": alarmInputHighDensity0003Normal,
       "alarmInputHighDensity0004Normal": alarmInputHighDensity0004Normal,
       "alarmInputHighDensity0005Normal": alarmInputHighDensity0005Normal,
       "alarmInputHighDensity0006Normal": alarmInputHighDensity0006Normal,
       "alarmInputHighDensity0007Normal": alarmInputHighDensity0007Normal,
       "alarmInputHighDensity0008Normal": alarmInputHighDensity0008Normal,
       "alarmInputHighDensity0009Normal": alarmInputHighDensity0009Normal,
       "alarmInputHighDensity0010Normal": alarmInputHighDensity0010Normal,
       "alarmInputHighDensity0011Normal": alarmInputHighDensity0011Normal,
       "alarmInputHighDensity0012Normal": alarmInputHighDensity0012Normal,
       "alarmInputHighDensity0013Normal": alarmInputHighDensity0013Normal,
       "alarmInputHighDensity0014Normal": alarmInputHighDensity0014Normal,
       "alarmInputHighDensity0015Normal": alarmInputHighDensity0015Normal,
       "alarmInputHighDensity0016Normal": alarmInputHighDensity0016Normal,
       "alarmInputHighDensity0017Normal": alarmInputHighDensity0017Normal,
       "alarmInputHighDensity0018Normal": alarmInputHighDensity0018Normal,
       "alarmInputHighDensity0019Normal": alarmInputHighDensity0019Normal,
       "alarmInputHighDensity0020Normal": alarmInputHighDensity0020Normal,
       "alarmInputHighDensity0021Normal": alarmInputHighDensity0021Normal,
       "alarmInputHighDensity0022Normal": alarmInputHighDensity0022Normal,
       "alarmInputHighDensity0023Normal": alarmInputHighDensity0023Normal,
       "alarmInputHighDensity0024Normal": alarmInputHighDensity0024Normal,
       "alarmInputHighDensity0025Normal": alarmInputHighDensity0025Normal,
       "alarmInputHighDensity0026Normal": alarmInputHighDensity0026Normal,
       "alarmInputHighDensity0027Normal": alarmInputHighDensity0027Normal,
       "alarmInputHighDensity0028Normal": alarmInputHighDensity0028Normal,
       "alarmInputHighDensity0029Normal": alarmInputHighDensity0029Normal,
       "alarmInputHighDensity0030Normal": alarmInputHighDensity0030Normal,
       "alarmInputHighDensity0031Normal": alarmInputHighDensity0031Normal,
       "alarmInputHighDensity0032Normal": alarmInputHighDensity0032Normal,
       "alarmInputHighDensity0033Normal": alarmInputHighDensity0033Normal,
       "alarmInputHighDensity0034Normal": alarmInputHighDensity0034Normal,
       "alarmInputHighDensity0035Normal": alarmInputHighDensity0035Normal,
       "alarmInputHighDensity0036Normal": alarmInputHighDensity0036Normal,
       "alarmInputHighDensity0037Normal": alarmInputHighDensity0037Normal,
       "alarmInputHighDensity0038Normal": alarmInputHighDensity0038Normal,
       "alarmInputHighDensity0039Normal": alarmInputHighDensity0039Normal,
       "alarmInputHighDensity0040Normal": alarmInputHighDensity0040Normal,
       "alarmInputHighDensity0041Normal": alarmInputHighDensity0041Normal,
       "alarmInputHighDensity0042Normal": alarmInputHighDensity0042Normal,
       "alarmInputHighDensity0043Normal": alarmInputHighDensity0043Normal,
       "alarmInputHighDensity0044Normal": alarmInputHighDensity0044Normal,
       "alarmInputHighDensity0045Normal": alarmInputHighDensity0045Normal,
       "alarmInputHighDensity0046Normal": alarmInputHighDensity0046Normal,
       "alarmInputHighDensity0047Normal": alarmInputHighDensity0047Normal,
       "alarmInputHighDensity0048Normal": alarmInputHighDensity0048Normal,
       "alarmInputHighDensity0049Normal": alarmInputHighDensity0049Normal,
       "alarmInputHighDensity0050Normal": alarmInputHighDensity0050Normal,
       "alarmInputHighDensity0051Normal": alarmInputHighDensity0051Normal,
       "alarmInputHighDensity0052Normal": alarmInputHighDensity0052Normal,
       "alarmInputHighDensity0053Normal": alarmInputHighDensity0053Normal,
       "alarmInputHighDensity0054Normal": alarmInputHighDensity0054Normal,
       "alarmInputHighDensity0055Normal": alarmInputHighDensity0055Normal,
       "alarmInputHighDensity0056Normal": alarmInputHighDensity0056Normal,
       "alarmInputHighDensity0057Normal": alarmInputHighDensity0057Normal,
       "alarmInputHighDensity0058Normal": alarmInputHighDensity0058Normal,
       "alarmInputHighDensity0059Normal": alarmInputHighDensity0059Normal,
       "alarmInputHighDensity0060Normal": alarmInputHighDensity0060Normal,
       "alarmInputHighDensity0061Normal": alarmInputHighDensity0061Normal,
       "alarmInputHighDensity0062Normal": alarmInputHighDensity0062Normal,
       "alarmInputHighDensity0063Normal": alarmInputHighDensity0063Normal,
       "alarmInputHighDensity0064Normal": alarmInputHighDensity0064Normal,
       "alarmInputHighDensity0065Normal": alarmInputHighDensity0065Normal,
       "alarmInputHighDensity0066Normal": alarmInputHighDensity0066Normal,
       "alarmInputHighDensity0067Normal": alarmInputHighDensity0067Normal,
       "alarmInputHighDensity0068Normal": alarmInputHighDensity0068Normal,
       "alarmInputHighDensity0069Normal": alarmInputHighDensity0069Normal,
       "alarmInputHighDensity0070Normal": alarmInputHighDensity0070Normal,
       "alarmInputHighDensity0071Normal": alarmInputHighDensity0071Normal,
       "alarmInputHighDensity0072Normal": alarmInputHighDensity0072Normal,
       "alarmInputHighDensity0073Normal": alarmInputHighDensity0073Normal,
       "alarmInputHighDensity0074Normal": alarmInputHighDensity0074Normal,
       "alarmInputHighDensity0075Normal": alarmInputHighDensity0075Normal,
       "alarmInputHighDensity0076Normal": alarmInputHighDensity0076Normal,
       "alarmInputHighDensity0077Normal": alarmInputHighDensity0077Normal,
       "alarmInputHighDensity0078Normal": alarmInputHighDensity0078Normal,
       "alarmInputHighDensity0079Normal": alarmInputHighDensity0079Normal,
       "alarmInputHighDensity0080Normal": alarmInputHighDensity0080Normal,
       "alarmInputHighDensity0081Normal": alarmInputHighDensity0081Normal,
       "alarmInputHighDensity0082Normal": alarmInputHighDensity0082Normal,
       "alarmInputHighDensity0083Normal": alarmInputHighDensity0083Normal,
       "alarmInputHighDensity0084Normal": alarmInputHighDensity0084Normal,
       "alarmInputHighDensity0085Normal": alarmInputHighDensity0085Normal,
       "alarmInputHighDensity0086Normal": alarmInputHighDensity0086Normal,
       "alarmInputHighDensity0087Normal": alarmInputHighDensity0087Normal,
       "alarmInputHighDensity0088Normal": alarmInputHighDensity0088Normal,
       "alarmInputHighDensity0089Normal": alarmInputHighDensity0089Normal,
       "alarmInputHighDensity0090Normal": alarmInputHighDensity0090Normal,
       "alarmInputHighDensity0091Normal": alarmInputHighDensity0091Normal,
       "alarmInputHighDensity0092Normal": alarmInputHighDensity0092Normal,
       "alarmInputHighDensity0093Normal": alarmInputHighDensity0093Normal,
       "alarmInputHighDensity0094Normal": alarmInputHighDensity0094Normal,
       "alarmInputHighDensity0095Normal": alarmInputHighDensity0095Normal,
       "alarmInputHighDensity0096Normal": alarmInputHighDensity0096Normal,
       "alarmInputHighDensity0097Normal": alarmInputHighDensity0097Normal,
       "alarmInputHighDensity0098Normal": alarmInputHighDensity0098Normal,
       "alarmInputHighDensity0099Normal": alarmInputHighDensity0099Normal,
       "alarmInputHighDensity0100Normal": alarmInputHighDensity0100Normal,
       "alarmInputHighDensity0101Normal": alarmInputHighDensity0101Normal,
       "alarmInputHighDensity0102Normal": alarmInputHighDensity0102Normal,
       "alarmInputHighDensity0103Normal": alarmInputHighDensity0103Normal,
       "alarmInputHighDensity0104Normal": alarmInputHighDensity0104Normal,
       "alarmInputHighDensity0105Normal": alarmInputHighDensity0105Normal,
       "alarmInputHighDensity0106Normal": alarmInputHighDensity0106Normal,
       "alarmInputHighDensity0107Normal": alarmInputHighDensity0107Normal,
       "alarmInputHighDensity0108Normal": alarmInputHighDensity0108Normal,
       "alarmInputHighDensity0109Normal": alarmInputHighDensity0109Normal,
       "alarmInputHighDensity0110Normal": alarmInputHighDensity0110Normal,
       "alarmInputHighDensity0111Normal": alarmInputHighDensity0111Normal,
       "alarmInputHighDensity0112Normal": alarmInputHighDensity0112Normal,
       "alarmInputHighDensity0113Normal": alarmInputHighDensity0113Normal,
       "alarmInputHighDensity0114Normal": alarmInputHighDensity0114Normal,
       "alarmInputHighDensity0115Normal": alarmInputHighDensity0115Normal,
       "alarmInputHighDensity0116Normal": alarmInputHighDensity0116Normal,
       "alarmInputHighDensity0117Normal": alarmInputHighDensity0117Normal,
       "alarmInputHighDensity0118Normal": alarmInputHighDensity0118Normal,
       "alarmInputHighDensity0119Normal": alarmInputHighDensity0119Normal,
       "alarmInputHighDensity0120Normal": alarmInputHighDensity0120Normal,
       "alarmInputHighDensity0121Normal": alarmInputHighDensity0121Normal,
       "alarmInputHighDensity0122Normal": alarmInputHighDensity0122Normal,
       "alarmInputHighDensity0123Normal": alarmInputHighDensity0123Normal,
       "alarmInputHighDensity0124Normal": alarmInputHighDensity0124Normal,
       "alarmInputHighDensity0125Normal": alarmInputHighDensity0125Normal,
       "alarmInputHighDensity0126Normal": alarmInputHighDensity0126Normal,
       "alarmInputHighDensity0127Normal": alarmInputHighDensity0127Normal,
       "alarmInputHighDensity0128Normal": alarmInputHighDensity0128Normal,
       "alarmInputHighDensity0129Normal": alarmInputHighDensity0129Normal,
       "alarmInputHighDensity0130Normal": alarmInputHighDensity0130Normal,
       "alarmInputHighDensity0131Normal": alarmInputHighDensity0131Normal,
       "alarmInputHighDensity0132Normal": alarmInputHighDensity0132Normal,
       "alarmInputHighDensity0133Normal": alarmInputHighDensity0133Normal,
       "alarmInputHighDensity0134Normal": alarmInputHighDensity0134Normal,
       "alarmInputHighDensity0135Normal": alarmInputHighDensity0135Normal,
       "alarmInputHighDensity0136Normal": alarmInputHighDensity0136Normal,
       "alarmInputHighDensity0137Normal": alarmInputHighDensity0137Normal,
       "alarmInputHighDensity0138Normal": alarmInputHighDensity0138Normal,
       "alarmInputHighDensity0139Normal": alarmInputHighDensity0139Normal,
       "alarmInputHighDensity0140Normal": alarmInputHighDensity0140Normal,
       "alarmInputHighDensity0141Normal": alarmInputHighDensity0141Normal,
       "alarmInputHighDensity0142Normal": alarmInputHighDensity0142Normal,
       "alarmInputHighDensity0143Normal": alarmInputHighDensity0143Normal,
       "alarmInputHighDensity0144Normal": alarmInputHighDensity0144Normal,
       "alarmInputHighDensity0145Normal": alarmInputHighDensity0145Normal,
       "alarmInputHighDensity0146Normal": alarmInputHighDensity0146Normal,
       "alarmInputHighDensity0147Normal": alarmInputHighDensity0147Normal,
       "alarmInputHighDensity0148Normal": alarmInputHighDensity0148Normal,
       "alarmInputHighDensity0149Normal": alarmInputHighDensity0149Normal,
       "alarmInputHighDensity0150Normal": alarmInputHighDensity0150Normal,
       "alarmInputHighDensity0151Normal": alarmInputHighDensity0151Normal,
       "alarmInputHighDensity0152Normal": alarmInputHighDensity0152Normal,
       "alarmInputHighDensity0153Normal": alarmInputHighDensity0153Normal,
       "alarmInputHighDensity0154Normal": alarmInputHighDensity0154Normal,
       "alarmInputHighDensity0155Normal": alarmInputHighDensity0155Normal,
       "alarmInputHighDensity0156Normal": alarmInputHighDensity0156Normal,
       "alarmInputHighDensity0157Normal": alarmInputHighDensity0157Normal,
       "alarmInputHighDensity0158Normal": alarmInputHighDensity0158Normal,
       "alarmInputHighDensity0159Normal": alarmInputHighDensity0159Normal,
       "alarmInputHighDensity0160Normal": alarmInputHighDensity0160Normal,
       "alarmInputHighDensity0161Normal": alarmInputHighDensity0161Normal,
       "alarmInputHighDensity0162Normal": alarmInputHighDensity0162Normal,
       "alarmInputHighDensity0163Normal": alarmInputHighDensity0163Normal,
       "alarmInputHighDensity0164Normal": alarmInputHighDensity0164Normal,
       "alarmInputHighDensity0165Normal": alarmInputHighDensity0165Normal,
       "alarmInputHighDensity0166Normal": alarmInputHighDensity0166Normal,
       "alarmInputHighDensity0167Normal": alarmInputHighDensity0167Normal,
       "alarmInputHighDensity0168Normal": alarmInputHighDensity0168Normal,
       "alarmInputHighDensity0169Normal": alarmInputHighDensity0169Normal,
       "alarmInputHighDensity0170Normal": alarmInputHighDensity0170Normal,
       "alarmInputHighDensity0171Normal": alarmInputHighDensity0171Normal,
       "alarmInputHighDensity0172Normal": alarmInputHighDensity0172Normal,
       "alarmInputHighDensity0173Normal": alarmInputHighDensity0173Normal,
       "alarmInputHighDensity0174Normal": alarmInputHighDensity0174Normal,
       "alarmInputHighDensity0175Normal": alarmInputHighDensity0175Normal,
       "alarmInputHighDensity0176Normal": alarmInputHighDensity0176Normal,
       "alarmInputHighDensity0177Normal": alarmInputHighDensity0177Normal,
       "alarmInputHighDensity0178Normal": alarmInputHighDensity0178Normal,
       "alarmInputHighDensity0179Normal": alarmInputHighDensity0179Normal,
       "alarmInputHighDensity0180Normal": alarmInputHighDensity0180Normal,
       "alarmInputHighDensity0181Normal": alarmInputHighDensity0181Normal,
       "alarmInputHighDensity0182Normal": alarmInputHighDensity0182Normal,
       "alarmInputHighDensity0183Normal": alarmInputHighDensity0183Normal,
       "alarmInputHighDensity0184Normal": alarmInputHighDensity0184Normal,
       "alarmInputHighDensity0185Normal": alarmInputHighDensity0185Normal,
       "alarmInputHighDensity0186Normal": alarmInputHighDensity0186Normal,
       "alarmInputHighDensity0187Normal": alarmInputHighDensity0187Normal,
       "alarmInputHighDensity0188Normal": alarmInputHighDensity0188Normal,
       "alarmInputHighDensity0189Normal": alarmInputHighDensity0189Normal,
       "alarmInputHighDensity0190Normal": alarmInputHighDensity0190Normal,
       "alarmInputHighDensity0191Normal": alarmInputHighDensity0191Normal,
       "alarmInputHighDensity0192Normal": alarmInputHighDensity0192Normal,
       "alarmInputHighDensity0193Normal": alarmInputHighDensity0193Normal,
       "alarmInputHighDensity0194Normal": alarmInputHighDensity0194Normal,
       "alarmInputHighDensity0195Normal": alarmInputHighDensity0195Normal,
       "alarmInputHighDensity0196Normal": alarmInputHighDensity0196Normal,
       "alarmInputHighDensity0197Normal": alarmInputHighDensity0197Normal,
       "alarmInputHighDensity0198Normal": alarmInputHighDensity0198Normal,
       "alarmInputHighDensity0199Normal": alarmInputHighDensity0199Normal,
       "alarmInputHighDensity0200Normal": alarmInputHighDensity0200Normal,
       "alarmInputHighDensity0201Normal": alarmInputHighDensity0201Normal,
       "alarmInputHighDensity0202Normal": alarmInputHighDensity0202Normal,
       "alarmInputHighDensity0203Normal": alarmInputHighDensity0203Normal,
       "alarmInputHighDensity0204Normal": alarmInputHighDensity0204Normal,
       "alarmInputHighDensity0205Normal": alarmInputHighDensity0205Normal,
       "alarmInputHighDensity0206Normal": alarmInputHighDensity0206Normal,
       "alarmInputHighDensity0207Normal": alarmInputHighDensity0207Normal,
       "alarmInputHighDensity0208Normal": alarmInputHighDensity0208Normal,
       "alarmInputHighDensity0209Normal": alarmInputHighDensity0209Normal,
       "alarmInputHighDensity0210Normal": alarmInputHighDensity0210Normal,
       "alarmInputHighDensity0211Normal": alarmInputHighDensity0211Normal,
       "alarmInputHighDensity0212Normal": alarmInputHighDensity0212Normal,
       "alarmInputHighDensity0213Normal": alarmInputHighDensity0213Normal,
       "alarmInputHighDensity0214Normal": alarmInputHighDensity0214Normal,
       "alarmInputHighDensity0215Normal": alarmInputHighDensity0215Normal,
       "alarmInputHighDensity0216Normal": alarmInputHighDensity0216Normal,
       "alarmInputHighDensity0217Normal": alarmInputHighDensity0217Normal,
       "alarmInputHighDensity0218Normal": alarmInputHighDensity0218Normal,
       "alarmInputHighDensity0219Normal": alarmInputHighDensity0219Normal,
       "alarmInputHighDensity0220Normal": alarmInputHighDensity0220Normal,
       "alarmInputHighDensity0221Normal": alarmInputHighDensity0221Normal,
       "alarmInputHighDensity0222Normal": alarmInputHighDensity0222Normal,
       "alarmInputHighDensity0223Normal": alarmInputHighDensity0223Normal,
       "alarmInputHighDensity0224Normal": alarmInputHighDensity0224Normal,
       "alarmInputHighDensity0225Normal": alarmInputHighDensity0225Normal,
       "alarmInputHighDensity0226Normal": alarmInputHighDensity0226Normal,
       "alarmInputHighDensity0227Normal": alarmInputHighDensity0227Normal,
       "alarmInputHighDensity0228Normal": alarmInputHighDensity0228Normal,
       "alarmInputHighDensity0229Normal": alarmInputHighDensity0229Normal,
       "alarmInputHighDensity0230Normal": alarmInputHighDensity0230Normal,
       "alarmInputHighDensity0231Normal": alarmInputHighDensity0231Normal,
       "alarmInputHighDensity0232Normal": alarmInputHighDensity0232Normal,
       "alarmInputHighDensity0233Normal": alarmInputHighDensity0233Normal,
       "alarmInputHighDensity0234Normal": alarmInputHighDensity0234Normal,
       "alarmInputHighDensity0235Normal": alarmInputHighDensity0235Normal,
       "alarmInputHighDensity0236Normal": alarmInputHighDensity0236Normal,
       "alarmInputHighDensity0237Normal": alarmInputHighDensity0237Normal,
       "alarmInputHighDensity0238Normal": alarmInputHighDensity0238Normal,
       "alarmInputHighDensity0239Normal": alarmInputHighDensity0239Normal,
       "alarmInputHighDensity0240Normal": alarmInputHighDensity0240Normal,
       "alarmInputHighDensity0241Normal": alarmInputHighDensity0241Normal,
       "alarmInputHighDensity0242Normal": alarmInputHighDensity0242Normal,
       "alarmInputHighDensity0243Normal": alarmInputHighDensity0243Normal,
       "alarmInputHighDensity0244Normal": alarmInputHighDensity0244Normal,
       "alarmInputHighDensity0245Normal": alarmInputHighDensity0245Normal,
       "alarmInputHighDensity0246Normal": alarmInputHighDensity0246Normal,
       "alarmInputHighDensity0247Normal": alarmInputHighDensity0247Normal,
       "alarmInputHighDensity0248Normal": alarmInputHighDensity0248Normal,
       "alarmInputHighDensity0249Normal": alarmInputHighDensity0249Normal,
       "alarmInputHighDensity0250Normal": alarmInputHighDensity0250Normal,
       "alarmInputHighDensity0251Normal": alarmInputHighDensity0251Normal,
       "alarmInputHighDensity0252Normal": alarmInputHighDensity0252Normal,
       "alarmInputHighDensity0253Normal": alarmInputHighDensity0253Normal,
       "alarmInputHighDensity0254Normal": alarmInputHighDensity0254Normal,
       "alarmInputHighDensity0255Normal": alarmInputHighDensity0255Normal,
       "alarmInputHighDensity0256Normal": alarmInputHighDensity0256Normal,
       "alarmInputHighDensity0257Normal": alarmInputHighDensity0257Normal,
       "alarmInputHighDensity0258Normal": alarmInputHighDensity0258Normal,
       "alarmInputHighDensity0259Normal": alarmInputHighDensity0259Normal,
       "alarmInputHighDensity0260Normal": alarmInputHighDensity0260Normal,
       "alarmInputHighDensity0261Normal": alarmInputHighDensity0261Normal,
       "alarmInputHighDensity0262Normal": alarmInputHighDensity0262Normal,
       "alarmInputHighDensity0263Normal": alarmInputHighDensity0263Normal,
       "alarmInputHighDensity0264Normal": alarmInputHighDensity0264Normal,
       "alarmInputHighDensity0265Normal": alarmInputHighDensity0265Normal,
       "alarmInputHighDensity0266Normal": alarmInputHighDensity0266Normal,
       "alarmInputHighDensity0267Normal": alarmInputHighDensity0267Normal,
       "alarmInputHighDensity0268Normal": alarmInputHighDensity0268Normal,
       "alarmInputHighDensity0269Normal": alarmInputHighDensity0269Normal,
       "alarmInputHighDensity0270Normal": alarmInputHighDensity0270Normal,
       "alarmInputHighDensity0271Normal": alarmInputHighDensity0271Normal,
       "alarmInputHighDensity0272Normal": alarmInputHighDensity0272Normal,
       "alarmInputHighDensity0273Normal": alarmInputHighDensity0273Normal,
       "alarmInputHighDensity0274Normal": alarmInputHighDensity0274Normal,
       "alarmInputHighDensity0275Normal": alarmInputHighDensity0275Normal,
       "alarmInputHighDensity0276Normal": alarmInputHighDensity0276Normal,
       "alarmInputHighDensity0277Normal": alarmInputHighDensity0277Normal,
       "alarmInputHighDensity0278Normal": alarmInputHighDensity0278Normal,
       "alarmInputHighDensity0279Normal": alarmInputHighDensity0279Normal,
       "alarmInputHighDensity0280Normal": alarmInputHighDensity0280Normal,
       "alarmInputHighDensity0281Normal": alarmInputHighDensity0281Normal,
       "alarmInputHighDensity0282Normal": alarmInputHighDensity0282Normal,
       "alarmInputHighDensity0283Normal": alarmInputHighDensity0283Normal,
       "alarmInputHighDensity0284Normal": alarmInputHighDensity0284Normal,
       "alarmInputHighDensity0285Normal": alarmInputHighDensity0285Normal,
       "alarmInputHighDensity0286Normal": alarmInputHighDensity0286Normal,
       "alarmInputHighDensity0287Normal": alarmInputHighDensity0287Normal,
       "alarmInputHighDensity0288Normal": alarmInputHighDensity0288Normal,
       "alarmInputHighDensity0289Normal": alarmInputHighDensity0289Normal,
       "alarmInputHighDensity0290Normal": alarmInputHighDensity0290Normal,
       "alarmInputHighDensity0291Normal": alarmInputHighDensity0291Normal,
       "alarmInputHighDensity0292Normal": alarmInputHighDensity0292Normal,
       "alarmInputHighDensity0293Normal": alarmInputHighDensity0293Normal,
       "alarmInputHighDensity0294Normal": alarmInputHighDensity0294Normal,
       "alarmInputHighDensity0295Normal": alarmInputHighDensity0295Normal,
       "alarmInputHighDensity0296Normal": alarmInputHighDensity0296Normal,
       "alarmInputHighDensity0297Normal": alarmInputHighDensity0297Normal,
       "alarmInputHighDensity0298Normal": alarmInputHighDensity0298Normal,
       "alarmInputHighDensity0299Normal": alarmInputHighDensity0299Normal,
       "alarmInputHighDensity0300Normal": alarmInputHighDensity0300Normal,
       "alarmInputHighDensity0301Normal": alarmInputHighDensity0301Normal,
       "alarmInputHighDensity0302Normal": alarmInputHighDensity0302Normal,
       "alarmInputHighDensity0303Normal": alarmInputHighDensity0303Normal,
       "alarmInputHighDensity0304Normal": alarmInputHighDensity0304Normal,
       "alarmInputHighDensity0305Normal": alarmInputHighDensity0305Normal,
       "alarmInputHighDensity0306Normal": alarmInputHighDensity0306Normal,
       "alarmInputHighDensity0307Normal": alarmInputHighDensity0307Normal,
       "alarmInputHighDensity0308Normal": alarmInputHighDensity0308Normal,
       "alarmInputHighDensity0309Normal": alarmInputHighDensity0309Normal,
       "alarmInputHighDensity0310Normal": alarmInputHighDensity0310Normal,
       "alarmInputHighDensity0311Normal": alarmInputHighDensity0311Normal,
       "alarmInputHighDensity0312Normal": alarmInputHighDensity0312Normal,
       "alarmInputHighDensity0313Normal": alarmInputHighDensity0313Normal,
       "alarmInputHighDensity0314Normal": alarmInputHighDensity0314Normal,
       "alarmInputHighDensity0315Normal": alarmInputHighDensity0315Normal,
       "alarmInputHighDensity0316Normal": alarmInputHighDensity0316Normal,
       "alarmInputHighDensity0317Normal": alarmInputHighDensity0317Normal,
       "alarmInputHighDensity0318Normal": alarmInputHighDensity0318Normal,
       "alarmInputHighDensity0319Normal": alarmInputHighDensity0319Normal,
       "alarmInputHighDensity0320Normal": alarmInputHighDensity0320Normal,
       "alarmInputHighDensity0321Normal": alarmInputHighDensity0321Normal,
       "alarmInputHighDensity0322Normal": alarmInputHighDensity0322Normal,
       "alarmInputHighDensity0323Normal": alarmInputHighDensity0323Normal,
       "alarmInputHighDensity0324Normal": alarmInputHighDensity0324Normal,
       "alarmInputHighDensity0325Normal": alarmInputHighDensity0325Normal,
       "alarmInputHighDensity0326Normal": alarmInputHighDensity0326Normal,
       "alarmInputHighDensity0327Normal": alarmInputHighDensity0327Normal,
       "alarmInputHighDensity0328Normal": alarmInputHighDensity0328Normal,
       "alarmInputHighDensity0329Normal": alarmInputHighDensity0329Normal,
       "alarmInputHighDensity0330Normal": alarmInputHighDensity0330Normal,
       "alarmInputHighDensity0331Normal": alarmInputHighDensity0331Normal,
       "alarmInputHighDensity0332Normal": alarmInputHighDensity0332Normal,
       "alarmInputHighDensity0333Normal": alarmInputHighDensity0333Normal,
       "alarmInputHighDensity0334Normal": alarmInputHighDensity0334Normal,
       "alarmInputHighDensity0335Normal": alarmInputHighDensity0335Normal,
       "alarmInputHighDensity0336Normal": alarmInputHighDensity0336Normal,
       "alarmInputHighDensity0337Normal": alarmInputHighDensity0337Normal,
       "alarmInputHighDensity0338Normal": alarmInputHighDensity0338Normal,
       "alarmInputHighDensity0339Normal": alarmInputHighDensity0339Normal,
       "alarmInputHighDensity0340Normal": alarmInputHighDensity0340Normal,
       "alarmInputHighDensity0341Normal": alarmInputHighDensity0341Normal,
       "alarmInputHighDensity0342Normal": alarmInputHighDensity0342Normal,
       "alarmInputHighDensity0343Normal": alarmInputHighDensity0343Normal,
       "alarmInputHighDensity0344Normal": alarmInputHighDensity0344Normal,
       "alarmInputHighDensity0345Normal": alarmInputHighDensity0345Normal,
       "alarmInputHighDensity0346Normal": alarmInputHighDensity0346Normal,
       "alarmInputHighDensity0347Normal": alarmInputHighDensity0347Normal,
       "alarmInputHighDensity0348Normal": alarmInputHighDensity0348Normal,
       "alarmInputHighDensity0349Normal": alarmInputHighDensity0349Normal,
       "alarmInputHighDensity0350Normal": alarmInputHighDensity0350Normal,
       "alarmInputHighDensity0351Normal": alarmInputHighDensity0351Normal,
       "alarmInputHighDensity0352Normal": alarmInputHighDensity0352Normal,
       "alarmInputHighDensity0353Normal": alarmInputHighDensity0353Normal,
       "alarmInputHighDensity0354Normal": alarmInputHighDensity0354Normal,
       "alarmInputHighDensity0355Normal": alarmInputHighDensity0355Normal,
       "alarmInputHighDensity0356Normal": alarmInputHighDensity0356Normal,
       "alarmInputHighDensity0357Normal": alarmInputHighDensity0357Normal,
       "alarmInputHighDensity0358Normal": alarmInputHighDensity0358Normal,
       "alarmInputHighDensity0359Normal": alarmInputHighDensity0359Normal,
       "alarmInputHighDensity0360Normal": alarmInputHighDensity0360Normal,
       "alarmInputHighDensity0361Normal": alarmInputHighDensity0361Normal,
       "alarmInputHighDensity0362Normal": alarmInputHighDensity0362Normal,
       "alarmInputHighDensity0363Normal": alarmInputHighDensity0363Normal,
       "alarmInputHighDensity0364Normal": alarmInputHighDensity0364Normal,
       "alarmInputHighDensity0365Normal": alarmInputHighDensity0365Normal,
       "alarmInputHighDensity0366Normal": alarmInputHighDensity0366Normal,
       "alarmInputHighDensity0367Normal": alarmInputHighDensity0367Normal,
       "alarmInputHighDensity0368Normal": alarmInputHighDensity0368Normal,
       "alarmInputHighDensity0369Normal": alarmInputHighDensity0369Normal,
       "alarmInputHighDensity0370Normal": alarmInputHighDensity0370Normal,
       "alarmInputHighDensity0371Normal": alarmInputHighDensity0371Normal,
       "alarmInputHighDensity0372Normal": alarmInputHighDensity0372Normal,
       "alarmInputHighDensity0373Normal": alarmInputHighDensity0373Normal,
       "alarmInputHighDensity0374Normal": alarmInputHighDensity0374Normal,
       "alarmInputHighDensity0375Normal": alarmInputHighDensity0375Normal,
       "alarmInputHighDensity0376Normal": alarmInputHighDensity0376Normal,
       "alarmInputHighDensity0377Normal": alarmInputHighDensity0377Normal,
       "alarmInputHighDensity0378Normal": alarmInputHighDensity0378Normal,
       "alarmInputHighDensity0379Normal": alarmInputHighDensity0379Normal,
       "alarmInputHighDensity0380Normal": alarmInputHighDensity0380Normal,
       "alarmInputHighDensity0381Normal": alarmInputHighDensity0381Normal,
       "alarmInputHighDensity0382Normal": alarmInputHighDensity0382Normal,
       "alarmInputHighDensity0383Normal": alarmInputHighDensity0383Normal,
       "alarmInputHighDensity0384Normal": alarmInputHighDensity0384Normal,
       "xAlarm": xAlarm}
)
