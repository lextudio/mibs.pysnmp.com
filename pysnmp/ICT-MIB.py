# SNMP MIB module (ICT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ICT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:03 2024
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

_IctPower_ObjectIdentity = ObjectIdentity
ictPower = _IctPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145)
)
_DigitalSeries_ObjectIdentity = ObjectIdentity
digitalSeries = _DigitalSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39145, 11)
)
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 1),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")


class _DeviceHardware_Type(Integer32):
    """Custom type deviceHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_DeviceHardware_Type.__name__ = "Integer32"
_DeviceHardware_Object = MibScalar
deviceHardware = _DeviceHardware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 3),
    _DeviceHardware_Type()
)
deviceHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardware.setStatus("mandatory")
_DeviceFirmware_Type = DisplayString
_DeviceFirmware_Object = MibScalar
deviceFirmware = _DeviceFirmware_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 4),
    _DeviceFirmware_Type()
)
deviceFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmware.setStatus("mandatory")
_DeviceMacAddress_Type = DisplayString
_DeviceMacAddress_Object = MibScalar
deviceMacAddress = _DeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 5),
    _DeviceMacAddress_Type()
)
deviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMacAddress.setStatus("mandatory")
_InputVoltage_Type = DisplayString
_InputVoltage_Object = MibScalar
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 6),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("mandatory")
_OutputVoltage_Type = DisplayString
_OutputVoltage_Object = MibScalar
outputVoltage = _OutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 7),
    _OutputVoltage_Type()
)
outputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVoltage.setStatus("mandatory")
_OutputCurrent_Type = DisplayString
_OutputCurrent_Object = MibScalar
outputCurrent = _OutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 8),
    _OutputCurrent_Type()
)
outputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputCurrent.setStatus("mandatory")


class _OutputEnable_Type(Integer32):
    """Custom type outputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("DISABLED", 2),
          ("ENABLED", 1))
    )


_OutputEnable_Type.__name__ = "Integer32"
_OutputEnable_Object = MibScalar
outputEnable = _OutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 39145, 11, 9),
    _OutputEnable_Type()
)
outputEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ICT-MIB",
    **{"ictPower": ictPower,
       "digitalSeries": digitalSeries,
       "deviceModel": deviceModel,
       "deviceName": deviceName,
       "deviceHardware": deviceHardware,
       "deviceFirmware": deviceFirmware,
       "deviceMacAddress": deviceMacAddress,
       "inputVoltage": inputVoltage,
       "outputVoltage": outputVoltage,
       "outputCurrent": outputCurrent,
       "outputEnable": outputEnable}
)
