# SNMP MIB module (SM7-10MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SM7-10MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:29 2024
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

_Symbios_ObjectIdentity = ObjectIdentity
symbios = _Symbios_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123)
)
_Wichita_ObjectIdentity = ObjectIdentity
wichita = _Wichita_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 1)
)
_Sm7_10_ObjectIdentity = ObjectIdentity
sm7_10 = _Sm7_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204)
)
_InfoTable_Object = MibTable
infoTable = _InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1)
)
if mibBuilder.loadTexts:
    infoTable.setStatus("mandatory")
_InfoEntry_Object = MibTableRow
infoEntry = _InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1)
)
infoEntry.setIndexNames(
    (0, "SM7-10MIB", "deviceHostIP"),
)
if mibBuilder.loadTexts:
    infoEntry.setStatus("mandatory")
_DeviceHostIP_Type = IpAddress
_DeviceHostIP_Object = MibTableColumn
deviceHostIP = _DeviceHostIP_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 1),
    _DeviceHostIP_Type()
)
deviceHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostIP.setStatus("mandatory")


class _DeviceHostName_Type(DisplayString):
    """Custom type deviceHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DeviceHostName_Type.__name__ = "DisplayString"
_DeviceHostName_Object = MibTableColumn
deviceHostName = _DeviceHostName_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 2),
    _DeviceHostName_Type()
)
deviceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHostName.setStatus("mandatory")


class _DeviceUserLabel_Type(DisplayString):
    """Custom type deviceUserLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DeviceUserLabel_Type.__name__ = "DisplayString"
_DeviceUserLabel_Object = MibTableColumn
deviceUserLabel = _DeviceUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 3),
    _DeviceUserLabel_Type()
)
deviceUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceUserLabel.setStatus("mandatory")


class _DeviceErrorCode_Type(DisplayString):
    """Custom type deviceErrorCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_DeviceErrorCode_Type.__name__ = "DisplayString"
_DeviceErrorCode_Object = MibTableColumn
deviceErrorCode = _DeviceErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 4),
    _DeviceErrorCode_Type()
)
deviceErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceErrorCode.setStatus("mandatory")


class _EventTime_Type(DisplayString):
    """Custom type eventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_EventTime_Type.__name__ = "DisplayString"
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 5),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("mandatory")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 69),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibTableColumn
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 6),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")


class _ComponentType_Type(DisplayString):
    """Custom type componentType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_ComponentType_Type.__name__ = "DisplayString"
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 7),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("mandatory")


class _ComponentLocation_Type(DisplayString):
    """Custom type componentLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_ComponentLocation_Type.__name__ = "DisplayString"
_ComponentLocation_Object = MibTableColumn
componentLocation = _ComponentLocation_Object(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 1, 1, 8),
    _ComponentLocation_Type()
)
componentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLocation.setStatus("mandatory")
_Ftcollins_ObjectIdentity = ObjectIdentity
ftcollins = _Ftcollins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 2)
)
_Cosprings_ObjectIdentity = ObjectIdentity
cosprings = _Cosprings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1123, 3)
)

# Managed Objects groups


# Notification objects

storageArrayCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1123, 1, 204, 0, 1)
)
storageArrayCritical.setObjects(
      *(("SM7-10MIB", "deviceHostIP"),
        ("SM7-10MIB", "deviceHostName"),
        ("SM7-10MIB", "deviceUserLabel"),
        ("SM7-10MIB", "deviceErrorCode"),
        ("SM7-10MIB", "eventTime"),
        ("SM7-10MIB", "trapDescription"),
        ("SM7-10MIB", "componentType"),
        ("SM7-10MIB", "componentLocation"))
)
if mibBuilder.loadTexts:
    storageArrayCritical.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SM7-10MIB",
    **{"symbios": symbios,
       "wichita": wichita,
       "sm7-10": sm7_10,
       "storageArrayCritical": storageArrayCritical,
       "infoTable": infoTable,
       "infoEntry": infoEntry,
       "deviceHostIP": deviceHostIP,
       "deviceHostName": deviceHostName,
       "deviceUserLabel": deviceUserLabel,
       "deviceErrorCode": deviceErrorCode,
       "eventTime": eventTime,
       "trapDescription": trapDescription,
       "componentType": componentType,
       "componentLocation": componentLocation,
       "ftcollins": ftcollins,
       "cosprings": cosprings}
)
