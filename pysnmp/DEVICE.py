# SNMP MIB module (DEVICE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVICE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:09 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

deviceInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pepwave_ObjectIdentity = ObjectIdentity
pepwave = _Pepwave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662)
)
_ProductMib_ObjectIdentity = ObjectIdentity
productMib = _ProductMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200)
)
_GeneralMib_ObjectIdentity = ObjectIdentity
generalMib = _GeneralMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1)
)
_DeviceMib_ObjectIdentity = ObjectIdentity
deviceMib = _DeviceMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1)
)
_DeviceInfoSystem_ObjectIdentity = ObjectIdentity
deviceInfoSystem = _DeviceInfoSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1)
)
_DeviceModel_Type = OctetString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_DeviceSerialNumber_Type = OctetString
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 2),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")
_DeviceFirmwareVersion_Type = OctetString
_DeviceFirmwareVersion_Object = MibScalar
deviceFirmwareVersion = _DeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 1, 3),
    _DeviceFirmwareVersion_Type()
)
deviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmwareVersion.setStatus("current")
_DeviceInfoTime_ObjectIdentity = ObjectIdentity
deviceInfoTime = _DeviceInfoTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2)
)
_DeviceSystemTime_Type = OctetString
_DeviceSystemTime_Object = MibScalar
deviceSystemTime = _DeviceSystemTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 1),
    _DeviceSystemTime_Type()
)
deviceSystemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSystemTime.setStatus("current")
_DeviceSystemUpTime_Type = OctetString
_DeviceSystemUpTime_Object = MibScalar
deviceSystemUpTime = _DeviceSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 2, 2),
    _DeviceSystemUpTime_Type()
)
deviceSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSystemUpTime.setStatus("current")
_DeviceInfoUsage_ObjectIdentity = ObjectIdentity
deviceInfoUsage = _DeviceInfoUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 3)
)


class _DeviceCpuLoad_Type(Integer32):
    """Custom type deviceCpuLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DeviceCpuLoad_Type.__name__ = "Integer32"
_DeviceCpuLoad_Object = MibScalar
deviceCpuLoad = _DeviceCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 3, 1),
    _DeviceCpuLoad_Type()
)
deviceCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoad.setStatus("current")
_DeviceTotalMemory_Type = Integer32
_DeviceTotalMemory_Object = MibScalar
deviceTotalMemory = _DeviceTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 3, 2),
    _DeviceTotalMemory_Type()
)
deviceTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceTotalMemory.setStatus("current")
_DeviceMemoryUsage_Type = Integer32
_DeviceMemoryUsage_Object = MibScalar
deviceMemoryUsage = _DeviceMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 27662, 200, 1, 1, 1, 3, 3),
    _DeviceMemoryUsage_Type()
)
deviceMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMemoryUsage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVICE",
    **{"pepwave": pepwave,
       "productMib": productMib,
       "generalMib": generalMib,
       "deviceMib": deviceMib,
       "deviceInfo": deviceInfo,
       "deviceInfoSystem": deviceInfoSystem,
       "deviceModel": deviceModel,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceFirmwareVersion": deviceFirmwareVersion,
       "deviceInfoTime": deviceInfoTime,
       "deviceSystemTime": deviceSystemTime,
       "deviceSystemUpTime": deviceSystemUpTime,
       "deviceInfoUsage": deviceInfoUsage,
       "deviceCpuLoad": deviceCpuLoad,
       "deviceTotalMemory": deviceTotalMemory,
       "deviceMemoryUsage": deviceMemoryUsage}
)
