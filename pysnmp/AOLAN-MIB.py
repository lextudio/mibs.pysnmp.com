# SNMP MIB module (AOLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AOLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:02 2024
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

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2)
)
_Mangement_products_ObjectIdentity = ObjectIdentity
mangement_products = _Mangement_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 8)
)
_TCO_products_ObjectIdentity = ObjectIdentity
tCO_products = _TCO_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1)
)
_Alert_on_LAN_ObjectIdentity = ObjectIdentity
alert_on_LAN = _Alert_on_LAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1)
)


class _SystemName_Type(OctetString):
    """Custom type systemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SystemName_Type.__name__ = "OctetString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemGUID_Type(DisplayString):
    """Custom type systemGUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SystemGUID_Type.__name__ = "DisplayString"
_SystemGUID_Object = MibScalar
systemGUID = _SystemGUID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 2),
    _SystemGUID_Type()
)
systemGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemGUID.setStatus("current")


class _EventString_Type(DisplayString):
    """Custom type eventString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventString_Type.__name__ = "DisplayString"
_EventString_Object = MibScalar
eventString = _EventString_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 3),
    _EventString_Type()
)
eventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventString.setStatus("current")


class _EventInfo_Type(OctetString):
    """Custom type eventInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_EventInfo_Type.__name__ = "OctetString"
_EventInfo_Object = MibScalar
eventInfo = _EventInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 4),
    _EventInfo_Type()
)
eventInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInfo.setStatus("current")


class _IPAddress_Type(OctetString):
    """Custom type iPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IPAddress_Type.__name__ = "OctetString"
_IPAddress_Object = MibScalar
iPAddress = _IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 5),
    _IPAddress_Type()
)
iPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPAddress.setStatus("current")

# Managed Objects groups


# Notification objects

presenceHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 0)
)
presenceHeartbeat.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    presenceHeartbeat.setStatus(
        ""
    )

coverTamper = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 1)
)
coverTamper.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    coverTamper.setStatus(
        ""
    )

voltage_Fan_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 2)
)
voltage_Fan_Temperature.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    voltage_Fan_Temperature.setStatus(
        ""
    )

lANLeash = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 3)
)
lANLeash.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    lANLeash.setStatus(
        ""
    )

temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 4)
)
temperature.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    temperature.setStatus(
        ""
    )

processorMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 5)
)
processorMissing.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    processorMissing.setStatus(
        ""
    )

processorTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 6)
)
processorTemperature.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    processorTemperature.setStatus(
        ""
    )

watchdog = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 7)
)
watchdog.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    watchdog.setStatus(
        ""
    )

p_O_S_T = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 8)
)
p_O_S_T.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    p_O_S_T.setStatus(
        ""
    )

unknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 9)
)
unknownEvent.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    unknownEvent.setStatus(
        ""
    )

processor_0_Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 10)
)
processor_0_Missing.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    processor_0_Missing.setStatus(
        ""
    )

processor_1_Missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 11)
)
processor_1_Missing.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    processor_1_Missing.setStatus(
        ""
    )

voltage_Fan = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 12)
)
voltage_Fan.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    voltage_Fan.setStatus(
        ""
    )

voltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 13)
)
voltage.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    voltage.setStatus(
        ""
    )

fan = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 14)
)
fan.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    fan.setStatus(
        ""
    )

fan_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 15)
)
fan_Temperature.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    fan_Temperature.setStatus(
        ""
    )

voltage_Temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 16)
)
voltage_Temperature.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    voltage_Temperature.setStatus(
        ""
    )

undock = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 17)
)
undock.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    undock.setStatus(
        ""
    )

eventClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 18)
)
eventClear.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    eventClear.setStatus(
        ""
    )

clientAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 19)
)
clientAdded.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    clientAdded.setStatus(
        ""
    )

clientDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 0, 20)
)
clientDeleted.setObjects(
    ("AOLAN-MIB", "systemName")
)
if mibBuilder.loadTexts:
    clientDeleted.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AOLAN-MIB",
    **{"intel": intel,
       "products": products,
       "mangement-products": mangement_products,
       "tCO-products": tCO_products,
       "alert-on-LAN": alert_on_LAN,
       "presenceHeartbeat": presenceHeartbeat,
       "coverTamper": coverTamper,
       "voltage-Fan-Temperature": voltage_Fan_Temperature,
       "lANLeash": lANLeash,
       "temperature": temperature,
       "processorMissing": processorMissing,
       "processorTemperature": processorTemperature,
       "watchdog": watchdog,
       "p-O-S-T": p_O_S_T,
       "unknownEvent": unknownEvent,
       "processor-0-Missing": processor_0_Missing,
       "processor-1-Missing": processor_1_Missing,
       "voltage-Fan": voltage_Fan,
       "voltage": voltage,
       "fan": fan,
       "fan-Temperature": fan_Temperature,
       "voltage-Temperature": voltage_Temperature,
       "undock": undock,
       "eventClear": eventClear,
       "clientAdded": clientAdded,
       "clientDeleted": clientDeleted,
       "systemName": systemName,
       "systemGUID": systemGUID,
       "eventString": eventString,
       "eventInfo": eventInfo,
       "iPAddress": iPAddress}
)
