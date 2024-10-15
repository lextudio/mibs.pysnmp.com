# SNMP MIB module (CPQPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQPOWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:35 2024
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName")

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

_CpqPower_ObjectIdentity = ObjectIdentity
cpqPower = _CpqPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165)
)
_PowerDevice_ObjectIdentity = ObjectIdentity
powerDevice = _PowerDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1)
)
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1)
)
_TrapCode_Type = Integer32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 1),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("mandatory")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 2),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")


class _TrapDeviceMgmtUrl_Type(DisplayString):
    """Custom type trapDeviceMgmtUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceMgmtUrl_Type.__name__ = "DisplayString"
_TrapDeviceMgmtUrl_Object = MibScalar
trapDeviceMgmtUrl = _TrapDeviceMgmtUrl_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 3),
    _TrapDeviceMgmtUrl_Type()
)
trapDeviceMgmtUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceMgmtUrl.setStatus("mandatory")


class _TrapDeviceDetails_Type(DisplayString):
    """Custom type trapDeviceDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceDetails_Type.__name__ = "DisplayString"
_TrapDeviceDetails_Object = MibScalar
trapDeviceDetails = _TrapDeviceDetails_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 4),
    _TrapDeviceDetails_Type()
)
trapDeviceDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceDetails.setStatus("mandatory")


class _TrapDeviceName_Type(DisplayString):
    """Custom type trapDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceName_Type.__name__ = "DisplayString"
_TrapDeviceName_Object = MibScalar
trapDeviceName = _TrapDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 5),
    _TrapDeviceName_Type()
)
trapDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceName.setStatus("mandatory")
_ManagementModuleIdent_ObjectIdentity = ObjectIdentity
managementModuleIdent = _ManagementModuleIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2)
)
_DeviceManufacturer_Type = DisplayString
_DeviceManufacturer_Object = MibScalar
deviceManufacturer = _DeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 1),
    _DeviceManufacturer_Type()
)
deviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceManufacturer.setStatus("mandatory")
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 2),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceFirmwareVersion_Type = DisplayString
_DeviceFirmwareVersion_Object = MibScalar
deviceFirmwareVersion = _DeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 3),
    _DeviceFirmwareVersion_Type()
)
deviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmwareVersion.setStatus("mandatory")
_DeviceHardwareVersion_Type = DisplayString
_DeviceHardwareVersion_Object = MibScalar
deviceHardwareVersion = _DeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 4),
    _DeviceHardwareVersion_Type()
)
deviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardwareVersion.setStatus("mandatory")
_DeviceIdentName_Type = DisplayString
_DeviceIdentName_Object = MibScalar
deviceIdentName = _DeviceIdentName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 5),
    _DeviceIdentName_Type()
)
deviceIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIdentName.setStatus("mandatory")
_DevicePartNumber_Type = DisplayString
_DevicePartNumber_Object = MibScalar
devicePartNumber = _DevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 6),
    _DevicePartNumber_Type()
)
devicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePartNumber.setStatus("mandatory")
_DeviceSerialNumber_Type = DisplayString
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 7),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("mandatory")
_DeviceMACAddress_Type = DisplayString
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 8),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("mandatory")
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2)
)
_PduIdent_ObjectIdentity = ObjectIdentity
pduIdent = _PduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1)
)


class _NumOfPdu_Type(Integer32):
    """Custom type numOfPdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NumOfPdu_Type.__name__ = "Integer32"
_NumOfPdu_Object = MibScalar
numOfPdu = _NumOfPdu_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 1),
    _NumOfPdu_Type()
)
numOfPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPdu.setStatus("mandatory")
_PduIdentTable_Object = MibTable
pduIdentTable = _PduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pduIdentTable.setStatus("mandatory")
_PduIdentEntry_Object = MibTableRow
pduIdentEntry = _PduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1)
)
pduIdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduIdentIndex"),
)
if mibBuilder.loadTexts:
    pduIdentEntry.setStatus("mandatory")
_PduIdentIndex_Type = Integer32
_PduIdentIndex_Object = MibTableColumn
pduIdentIndex = _PduIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 1),
    _PduIdentIndex_Type()
)
pduIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentIndex.setStatus("mandatory")


class _PduName_Type(DisplayString):
    """Custom type pduName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduName_Type.__name__ = "DisplayString"
_PduName_Object = MibTableColumn
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 2),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("mandatory")


class _PduModel_Type(DisplayString):
    """Custom type pduModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduModel_Type.__name__ = "DisplayString"
_PduModel_Object = MibTableColumn
pduModel = _PduModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 3),
    _PduModel_Type()
)
pduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduModel.setStatus("mandatory")


class _PduManufacturer_Type(DisplayString):
    """Custom type pduManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduManufacturer_Type.__name__ = "DisplayString"
_PduManufacturer_Object = MibTableColumn
pduManufacturer = _PduManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 4),
    _PduManufacturer_Type()
)
pduManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduManufacturer.setStatus("mandatory")


class _PduFirmwareVersion_Type(DisplayString):
    """Custom type pduFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduFirmwareVersion_Type.__name__ = "DisplayString"
_PduFirmwareVersion_Object = MibTableColumn
pduFirmwareVersion = _PduFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 5),
    _PduFirmwareVersion_Type()
)
pduFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFirmwareVersion.setStatus("mandatory")


class _PduPartNumber_Type(DisplayString):
    """Custom type pduPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduPartNumber_Type.__name__ = "DisplayString"
_PduPartNumber_Object = MibTableColumn
pduPartNumber = _PduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 6),
    _PduPartNumber_Type()
)
pduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPartNumber.setStatus("mandatory")


class _PduSerialNumber_Type(DisplayString):
    """Custom type pduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSerialNumber_Type.__name__ = "DisplayString"
_PduSerialNumber_Object = MibTableColumn
pduSerialNumber = _PduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 7),
    _PduSerialNumber_Type()
)
pduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSerialNumber.setStatus("mandatory")


class _PduStatus_Type(Integer32):
    """Custom type pduStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_PduStatus_Type.__name__ = "Integer32"
_PduStatus_Object = MibTableColumn
pduStatus = _PduStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 8),
    _PduStatus_Type()
)
pduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatus.setStatus("mandatory")


class _PduControllable_Type(Integer32):
    """Custom type pduControllable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PduControllable_Type.__name__ = "Integer32"
_PduControllable_Object = MibTableColumn
pduControllable = _PduControllable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 9),
    _PduControllable_Type()
)
pduControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduControllable.setStatus("mandatory")
_PduInput_ObjectIdentity = ObjectIdentity
pduInput = _PduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2)
)
_PduInputTable_Object = MibTable
pduInputTable = _PduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pduInputTable.setStatus("mandatory")
_PduInputEntry_Object = MibTableRow
pduInputEntry = _PduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1)
)
pduInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduInputIndex"),
)
if mibBuilder.loadTexts:
    pduInputEntry.setStatus("mandatory")
_PduInputIndex_Type = Integer32
_PduInputIndex_Object = MibTableColumn
pduInputIndex = _PduInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 1),
    _PduInputIndex_Type()
)
pduInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputIndex.setStatus("mandatory")


class _InputVoltage_Type(Integer32):
    """Custom type inputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InputVoltage_Type.__name__ = "Integer32"
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 2),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("mandatory")


class _InputCurrent_Type(Integer32):
    """Custom type inputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InputCurrent_Type.__name__ = "Integer32"
_InputCurrent_Object = MibTableColumn
inputCurrent = _InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 3),
    _InputCurrent_Type()
)
inputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrent.setStatus("mandatory")
_PduOutput_ObjectIdentity = ObjectIdentity
pduOutput = _PduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3)
)
_PduOutputTable_Object = MibTable
pduOutputTable = _PduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pduOutputTable.setStatus("mandatory")
_PduOutputEntry_Object = MibTableRow
pduOutputEntry = _PduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1)
)
pduOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduOutputIndex"),
)
if mibBuilder.loadTexts:
    pduOutputEntry.setStatus("mandatory")
_PduOutputIndex_Type = Integer32
_PduOutputIndex_Object = MibTableColumn
pduOutputIndex = _PduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 1),
    _PduOutputIndex_Type()
)
pduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputIndex.setStatus("mandatory")


class _PduOutputLoad_Type(Integer32):
    """Custom type pduOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PduOutputLoad_Type.__name__ = "Integer32"
_PduOutputLoad_Object = MibTableColumn
pduOutputLoad = _PduOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 2),
    _PduOutputLoad_Type()
)
pduOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputLoad.setStatus("mandatory")
_PduOutputHeat_Type = Integer32
_PduOutputHeat_Object = MibTableColumn
pduOutputHeat = _PduOutputHeat_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 3),
    _PduOutputHeat_Type()
)
pduOutputHeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputHeat.setStatus("mandatory")
_PduOutputPower_Type = Integer32
_PduOutputPower_Object = MibTableColumn
pduOutputPower = _PduOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 4),
    _PduOutputPower_Type()
)
pduOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPower.setStatus("mandatory")
_PduOutputNumBreakers_Type = Integer32
_PduOutputNumBreakers_Object = MibTableColumn
pduOutputNumBreakers = _PduOutputNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 5),
    _PduOutputNumBreakers_Type()
)
pduOutputNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputNumBreakers.setStatus("mandatory")
_PduOutputBreakerTable_Object = MibTable
pduOutputBreakerTable = _PduOutputBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduOutputBreakerTable.setStatus("mandatory")
_PduOutputBreakerEntry_Object = MibTableRow
pduOutputBreakerEntry = _PduOutputBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1)
)
pduOutputBreakerEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduOutputIndex"),
    (0, "CPQPOWER-MIB", "breakerIndex"),
)
if mibBuilder.loadTexts:
    pduOutputBreakerEntry.setStatus("mandatory")
_BreakerIndex_Type = Integer32
_BreakerIndex_Object = MibTableColumn
breakerIndex = _BreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 1),
    _BreakerIndex_Type()
)
breakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerIndex.setStatus("mandatory")
_BreakerVoltage_Type = Integer32
_BreakerVoltage_Object = MibTableColumn
breakerVoltage = _BreakerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 2),
    _BreakerVoltage_Type()
)
breakerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerVoltage.setStatus("mandatory")
_BreakerCurrent_Type = Integer32
_BreakerCurrent_Object = MibTableColumn
breakerCurrent = _BreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 3),
    _BreakerCurrent_Type()
)
breakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerCurrent.setStatus("mandatory")
_BreakerPercentLoad_Type = Integer32
_BreakerPercentLoad_Object = MibTableColumn
breakerPercentLoad = _BreakerPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 4),
    _BreakerPercentLoad_Type()
)
breakerPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPercentLoad.setStatus("mandatory")


class _BreakerStatus_Type(Integer32):
    """Custom type breakerStatus based on Integer32"""
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
        *(("normal", 1),
          ("overloadCritical", 3),
          ("overloadWarning", 2),
          ("voltageRangeCritical", 5),
          ("voltageRangeWarning", 4))
    )


_BreakerStatus_Type.__name__ = "Integer32"
_BreakerStatus_Object = MibTableColumn
breakerStatus = _BreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 5),
    _BreakerStatus_Type()
)
breakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerStatus.setStatus("mandatory")
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1)
)


class _UpsIdentManufacturer_Type(DisplayString):
    """Custom type upsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentManufacturer_Type.__name__ = "DisplayString"
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("mandatory")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")


class _UpsIdentSoftwareVersions_Type(DisplayString):
    """Custom type upsIdentSoftwareVersions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentSoftwareVersions_Type.__name__ = "DisplayString"
_UpsIdentSoftwareVersions_Object = MibScalar
upsIdentSoftwareVersions = _UpsIdentSoftwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 3),
    _UpsIdentSoftwareVersions_Type()
)
upsIdentSoftwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentSoftwareVersions.setStatus("mandatory")


class _UpsIdentOemCode_Type(Integer32):
    """Custom type upsIdentOemCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UpsIdentOemCode_Type.__name__ = "Integer32"
_UpsIdentOemCode_Object = MibScalar
upsIdentOemCode = _UpsIdentOemCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 4),
    _UpsIdentOemCode_Type()
)
upsIdentOemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOemCode.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2)
)


class _UpsBatTimeRemaining_Type(Integer32):
    """Custom type upsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBatTimeRemaining_Type.__name__ = "Integer32"
_UpsBatTimeRemaining_Object = MibScalar
upsBatTimeRemaining = _UpsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 1),
    _UpsBatTimeRemaining_Type()
)
upsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatTimeRemaining.setStatus("mandatory")


class _UpsBatVoltage_Type(Integer32):
    """Custom type upsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBatVoltage_Type.__name__ = "Integer32"
_UpsBatVoltage_Object = MibScalar
upsBatVoltage = _UpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 2),
    _UpsBatVoltage_Type()
)
upsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatVoltage.setStatus("mandatory")


class _UpsBatCurrent_Type(Integer32):
    """Custom type upsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_UpsBatCurrent_Type.__name__ = "Integer32"
_UpsBatCurrent_Object = MibScalar
upsBatCurrent = _UpsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 3),
    _UpsBatCurrent_Type()
)
upsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatCurrent.setStatus("mandatory")


class _UpsBatCapacity_Type(Integer32):
    """Custom type upsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatCapacity_Type.__name__ = "Integer32"
_UpsBatCapacity_Object = MibScalar
upsBatCapacity = _UpsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 4),
    _UpsBatCapacity_Type()
)
upsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatCapacity.setStatus("mandatory")


class _UpsBatteryAbmStatus_Type(Integer32):
    """Custom type upsBatteryAbmStatus based on Integer32"""
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
        *(("batteryCharging", 1),
          ("batteryDischarging", 2),
          ("batteryFloating", 3),
          ("batteryResting", 4),
          ("unknown", 5))
    )


_UpsBatteryAbmStatus_Type.__name__ = "Integer32"
_UpsBatteryAbmStatus_Object = MibScalar
upsBatteryAbmStatus = _UpsBatteryAbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 5),
    _UpsBatteryAbmStatus_Type()
)
upsBatteryAbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryAbmStatus.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3)
)


class _UpsInputFrequency_Type(Integer32):
    """Custom type upsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputFrequency_Type.__name__ = "Integer32"
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 1),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputLineBads_Type = Counter32
_UpsInputLineBads_Object = MibScalar
upsInputLineBads = _UpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 2),
    _UpsInputLineBads_Type()
)
upsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBads.setStatus("mandatory")


class _UpsInputNumPhases_Type(Integer32):
    """Custom type upsInputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsInputNumPhases_Type.__name__ = "Integer32"
_UpsInputNumPhases_Object = MibScalar
upsInputNumPhases = _UpsInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 3),
    _UpsInputNumPhases_Type()
)
upsInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumPhases.setStatus("mandatory")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1)
)
upsInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsInputPhase"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")


class _UpsInputPhase_Type(Integer32):
    """Custom type upsInputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsInputPhase_Type.__name__ = "Integer32"
_UpsInputPhase_Object = MibTableColumn
upsInputPhase = _UpsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 1),
    _UpsInputPhase_Type()
)
upsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPhase.setStatus("mandatory")


class _UpsInputVoltage_Type(Integer32):
    """Custom type upsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputVoltage_Type.__name__ = "Integer32"
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")


class _UpsInputCurrent_Type(Integer32):
    """Custom type upsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputCurrent_Type.__name__ = "Integer32"
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 3),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("mandatory")


class _UpsInputWatts_Type(Integer32):
    """Custom type upsInputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputWatts_Type.__name__ = "Integer32"
_UpsInputWatts_Object = MibTableColumn
upsInputWatts = _UpsInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 4),
    _UpsInputWatts_Type()
)
upsInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputWatts.setStatus("mandatory")


class _UpsInputSource_Type(Integer32):
    """Custom type upsInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bypassFeed", 4),
          ("flywheel", 7),
          ("fuelcell", 8),
          ("generator", 6),
          ("none", 2),
          ("other", 1),
          ("primaryUtility", 3),
          ("secondaryUtility", 5))
    )


_UpsInputSource_Type.__name__ = "Integer32"
_UpsInputSource_Object = MibScalar
upsInputSource = _UpsInputSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 5),
    _UpsInputSource_Type()
)
upsInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputSource.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4)
)


class _UpsOutputLoad_Type(Integer32):
    """Custom type upsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputLoad_Type.__name__ = "Integer32"
_UpsOutputLoad_Object = MibScalar
upsOutputLoad = _UpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 1),
    _UpsOutputLoad_Type()
)
upsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLoad.setStatus("mandatory")


class _UpsOutputFrequency_Type(Integer32):
    """Custom type upsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputFrequency_Type.__name__ = "Integer32"
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")


class _UpsOutputNumPhases_Type(Integer32):
    """Custom type upsOutputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsOutputNumPhases_Type.__name__ = "Integer32"
_UpsOutputNumPhases_Object = MibScalar
upsOutputNumPhases = _UpsOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 3),
    _UpsOutputNumPhases_Type()
)
upsOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumPhases.setStatus("mandatory")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsOutputPhase"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")


class _UpsOutputPhase_Type(Integer32):
    """Custom type upsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsOutputPhase_Type.__name__ = "Integer32"
_UpsOutputPhase_Object = MibTableColumn
upsOutputPhase = _UpsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 1),
    _UpsOutputPhase_Type()
)
upsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPhase.setStatus("mandatory")


class _UpsOutputVoltage_Type(Integer32):
    """Custom type upsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputVoltage_Type.__name__ = "Integer32"
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")


class _UpsOutputCurrent_Type(Integer32):
    """Custom type upsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputCurrent_Type.__name__ = "Integer32"
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")


class _UpsOutputWatts_Type(Integer32):
    """Custom type upsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputWatts_Type.__name__ = "Integer32"
_UpsOutputWatts_Object = MibTableColumn
upsOutputWatts = _UpsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 4),
    _UpsOutputWatts_Type()
)
upsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputWatts.setStatus("mandatory")


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("battery", 5),
          ("booster", 6),
          ("bypass", 4),
          ("highEfficiencyMode", 10),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("parallelCapacity", 8),
          ("parallelRedundant", 9),
          ("reducer", 7))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 5),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5)
)


class _UpsBypassFrequency_Type(Integer32):
    """Custom type upsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBypassFrequency_Type.__name__ = "Integer32"
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("mandatory")


class _UpsBypassNumPhases_Type(Integer32):
    """Custom type upsBypassNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsBypassNumPhases_Type.__name__ = "Integer32"
_UpsBypassNumPhases_Object = MibScalar
upsBypassNumPhases = _UpsBypassNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 2),
    _UpsBypassNumPhases_Type()
)
upsBypassNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumPhases.setStatus("mandatory")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("mandatory")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsBypassPhase"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("mandatory")


class _UpsBypassPhase_Type(Integer32):
    """Custom type upsBypassPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsBypassPhase_Type.__name__ = "Integer32"
_UpsBypassPhase_Object = MibTableColumn
upsBypassPhase = _UpsBypassPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1, 1),
    _UpsBypassPhase_Type()
)
upsBypassPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPhase.setStatus("mandatory")


class _UpsBypassVoltage_Type(Integer32):
    """Custom type upsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBypassVoltage_Type.__name__ = "Integer32"
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("mandatory")
_UpsEnvironment_ObjectIdentity = ObjectIdentity
upsEnvironment = _UpsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6)
)


class _UpsEnvAmbientTemp_Type(Integer32):
    """Custom type upsEnvAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientTemp_Type.__name__ = "Integer32"
_UpsEnvAmbientTemp_Object = MibScalar
upsEnvAmbientTemp = _UpsEnvAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 1),
    _UpsEnvAmbientTemp_Type()
)
upsEnvAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvAmbientTemp.setStatus("mandatory")


class _UpsEnvAmbientLowerLimit_Type(Integer32):
    """Custom type upsEnvAmbientLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientLowerLimit_Type.__name__ = "Integer32"
_UpsEnvAmbientLowerLimit_Object = MibScalar
upsEnvAmbientLowerLimit = _UpsEnvAmbientLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 2),
    _UpsEnvAmbientLowerLimit_Type()
)
upsEnvAmbientLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvAmbientLowerLimit.setStatus("mandatory")


class _UpsEnvAmbientUpperLimit_Type(Integer32):
    """Custom type upsEnvAmbientUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientUpperLimit_Type.__name__ = "Integer32"
_UpsEnvAmbientUpperLimit_Object = MibScalar
upsEnvAmbientUpperLimit = _UpsEnvAmbientUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 3),
    _UpsEnvAmbientUpperLimit_Type()
)
upsEnvAmbientUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvAmbientUpperLimit.setStatus("mandatory")


class _UpsEnvAmbientHumidity_Type(Integer32):
    """Custom type upsEnvAmbientHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvAmbientHumidity_Type.__name__ = "Integer32"
_UpsEnvAmbientHumidity_Object = MibScalar
upsEnvAmbientHumidity = _UpsEnvAmbientHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 4),
    _UpsEnvAmbientHumidity_Type()
)
upsEnvAmbientHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvAmbientHumidity.setStatus("mandatory")


class _UpsEnvRemoteTemp_Type(Integer32):
    """Custom type upsEnvRemoteTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTemp_Type.__name__ = "Integer32"
_UpsEnvRemoteTemp_Object = MibScalar
upsEnvRemoteTemp = _UpsEnvRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 5),
    _UpsEnvRemoteTemp_Type()
)
upsEnvRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvRemoteTemp.setStatus("mandatory")


class _UpsEnvRemoteHumidity_Type(Integer32):
    """Custom type upsEnvRemoteHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidity_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidity_Object = MibScalar
upsEnvRemoteHumidity = _UpsEnvRemoteHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 6),
    _UpsEnvRemoteHumidity_Type()
)
upsEnvRemoteHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidity.setStatus("mandatory")


class _UpsEnvNumContacts_Type(Integer32):
    """Custom type upsEnvNumContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_UpsEnvNumContacts_Type.__name__ = "Integer32"
_UpsEnvNumContacts_Object = MibScalar
upsEnvNumContacts = _UpsEnvNumContacts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 7),
    _UpsEnvNumContacts_Type()
)
upsEnvNumContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvNumContacts.setStatus("mandatory")
_UpsContactsTable_Object = MibTable
upsContactsTable = _UpsContactsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8)
)
if mibBuilder.loadTexts:
    upsContactsTable.setStatus("mandatory")
_UpsContactsTableEntry_Object = MibTableRow
upsContactsTableEntry = _UpsContactsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1)
)
upsContactsTableEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsContactIndex"),
)
if mibBuilder.loadTexts:
    upsContactsTableEntry.setStatus("mandatory")


class _UpsContactIndex_Type(Integer32):
    """Custom type upsContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_UpsContactIndex_Type.__name__ = "Integer32"
_UpsContactIndex_Object = MibTableColumn
upsContactIndex = _UpsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 1),
    _UpsContactIndex_Type()
)
upsContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsContactIndex.setStatus("mandatory")


class _UpsContactType_Type(Integer32):
    """Custom type upsContactType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("anyChange", 3),
          ("normallyClosed", 2),
          ("normallyOpen", 1),
          ("notUsed", 4))
    )


_UpsContactType_Type.__name__ = "Integer32"
_UpsContactType_Object = MibTableColumn
upsContactType = _UpsContactType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 2),
    _UpsContactType_Type()
)
upsContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsContactType.setStatus("mandatory")


class _UpsContactState_Type(Integer32):
    """Custom type upsContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("closedWithNotice", 4),
          ("open", 1),
          ("openWithNotice", 3))
    )


_UpsContactState_Type.__name__ = "Integer32"
_UpsContactState_Object = MibTableColumn
upsContactState = _UpsContactState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 3),
    _UpsContactState_Type()
)
upsContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsContactState.setStatus("mandatory")


class _UpsContactDescr_Type(DisplayString):
    """Custom type upsContactDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsContactDescr_Type.__name__ = "DisplayString"
_UpsContactDescr_Object = MibTableColumn
upsContactDescr = _UpsContactDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 4),
    _UpsContactDescr_Type()
)
upsContactDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsContactDescr.setStatus("mandatory")


class _UpsEnvRemoteTempLowerLimit_Type(Integer32):
    """Custom type upsEnvRemoteTempLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTempLowerLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteTempLowerLimit_Object = MibScalar
upsEnvRemoteTempLowerLimit = _UpsEnvRemoteTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 9),
    _UpsEnvRemoteTempLowerLimit_Type()
)
upsEnvRemoteTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteTempLowerLimit.setStatus("mandatory")


class _UpsEnvRemoteTempUpperLimit_Type(Integer32):
    """Custom type upsEnvRemoteTempUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTempUpperLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteTempUpperLimit_Object = MibScalar
upsEnvRemoteTempUpperLimit = _UpsEnvRemoteTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 10),
    _UpsEnvRemoteTempUpperLimit_Type()
)
upsEnvRemoteTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteTempUpperLimit.setStatus("mandatory")


class _UpsEnvRemoteHumidityLowerLimit_Type(Integer32):
    """Custom type upsEnvRemoteHumidityLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidityLowerLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidityLowerLimit_Object = MibScalar
upsEnvRemoteHumidityLowerLimit = _UpsEnvRemoteHumidityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 11),
    _UpsEnvRemoteHumidityLowerLimit_Type()
)
upsEnvRemoteHumidityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidityLowerLimit.setStatus("mandatory")


class _UpsEnvRemoteHumidityUpperLimit_Type(Integer32):
    """Custom type upsEnvRemoteHumidityUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidityUpperLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidityUpperLimit_Object = MibScalar
upsEnvRemoteHumidityUpperLimit = _UpsEnvRemoteHumidityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 12),
    _UpsEnvRemoteHumidityUpperLimit_Type()
)
upsEnvRemoteHumidityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidityUpperLimit.setStatus("mandatory")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7)
)


class _UpsTestBattery_Type(Integer32):
    """Custom type upsTestBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTest", 1)
    )


_UpsTestBattery_Type.__name__ = "Integer32"
_UpsTestBattery_Object = MibScalar
upsTestBattery = _UpsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 1),
    _UpsTestBattery_Type()
)
upsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestBattery.setStatus("mandatory")


class _UpsTestBatteryStatus_Type(Integer32):
    """Custom type upsTestBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 4),
          ("inhibited", 6),
          ("notSupported", 5),
          ("passed", 2),
          ("scheduled", 7),
          ("unknown", 1))
    )


_UpsTestBatteryStatus_Type.__name__ = "Integer32"
_UpsTestBatteryStatus_Object = MibScalar
upsTestBatteryStatus = _UpsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 2),
    _UpsTestBatteryStatus_Type()
)
upsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestBatteryStatus.setStatus("mandatory")


class _UpsTestTrap_Type(Integer32):
    """Custom type upsTestTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTestTrap", 1)
    )


_UpsTestTrap_Type.__name__ = "Integer32"
_UpsTestTrap_Object = MibScalar
upsTestTrap = _UpsTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 3),
    _UpsTestTrap_Type()
)
upsTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestTrap.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8)
)


class _UpsControlOutputOffDelay_Type(Integer32):
    """Custom type upsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOffDelay_Type.__name__ = "Integer32"
_UpsControlOutputOffDelay_Object = MibScalar
upsControlOutputOffDelay = _UpsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 1),
    _UpsControlOutputOffDelay_Type()
)
upsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOffDelay.setStatus("mandatory")


class _UpsControlOutputOnDelay_Type(Integer32):
    """Custom type upsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOnDelay_Type.__name__ = "Integer32"
_UpsControlOutputOnDelay_Object = MibScalar
upsControlOutputOnDelay = _UpsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 2),
    _UpsControlOutputOnDelay_Type()
)
upsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOnDelay.setStatus("mandatory")


class _UpsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type upsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_UpsControlOutputOffTrapDelay_Object = MibScalar
upsControlOutputOffTrapDelay = _UpsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 3),
    _UpsControlOutputOffTrapDelay_Type()
)
upsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOffTrapDelay.setStatus("mandatory")


class _UpsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type upsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_UpsControlOutputOnTrapDelay_Object = MibScalar
upsControlOutputOnTrapDelay = _UpsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 4),
    _UpsControlOutputOnTrapDelay_Type()
)
upsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOnTrapDelay.setStatus("deprecated")


class _UpsControlToBypassDelay_Type(Integer32):
    """Custom type upsControlToBypassDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlToBypassDelay_Type.__name__ = "Integer32"
_UpsControlToBypassDelay_Object = MibScalar
upsControlToBypassDelay = _UpsControlToBypassDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 5),
    _UpsControlToBypassDelay_Type()
)
upsControlToBypassDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlToBypassDelay.setStatus("mandatory")


class _UpsLoadShedSecsWithRestart_Type(Integer32):
    """Custom type upsLoadShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsLoadShedSecsWithRestart_Type.__name__ = "Integer32"
_UpsLoadShedSecsWithRestart_Object = MibScalar
upsLoadShedSecsWithRestart = _UpsLoadShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 6),
    _UpsLoadShedSecsWithRestart_Type()
)
upsLoadShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadShedSecsWithRestart.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9)
)


class _UpsConfigOutputVoltage_Type(Integer32):
    """Custom type upsConfigOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputVoltage_Type.__name__ = "Integer32"
_UpsConfigOutputVoltage_Object = MibScalar
upsConfigOutputVoltage = _UpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 1),
    _UpsConfigOutputVoltage_Type()
)
upsConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setStatus("mandatory")


class _UpsConfigInputVoltage_Type(Integer32):
    """Custom type upsConfigInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigInputVoltage_Type.__name__ = "Integer32"
_UpsConfigInputVoltage_Object = MibScalar
upsConfigInputVoltage = _UpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 2),
    _UpsConfigInputVoltage_Type()
)
upsConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setStatus("mandatory")


class _UpsConfigOutputWatts_Type(Integer32):
    """Custom type upsConfigOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputWatts_Type.__name__ = "Integer32"
_UpsConfigOutputWatts_Object = MibScalar
upsConfigOutputWatts = _UpsConfigOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 3),
    _UpsConfigOutputWatts_Type()
)
upsConfigOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputWatts.setStatus("mandatory")


class _UpsConfigOutputFreq_Type(Integer32):
    """Custom type upsConfigOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputFreq_Type.__name__ = "Integer32"
_UpsConfigOutputFreq_Object = MibScalar
upsConfigOutputFreq = _UpsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 4),
    _UpsConfigOutputFreq_Type()
)
upsConfigOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setStatus("mandatory")


class _UpsConfigDateAndTime_Type(DisplayString):
    """Custom type upsConfigDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_UpsConfigDateAndTime_Type.__name__ = "DisplayString"
_UpsConfigDateAndTime_Object = MibScalar
upsConfigDateAndTime = _UpsConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 5),
    _UpsConfigDateAndTime_Type()
)
upsConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigDateAndTime.setStatus("mandatory")


class _UpsConfigLowOutputVoltageLimit_Type(Integer32):
    """Custom type upsConfigLowOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigLowOutputVoltageLimit_Type.__name__ = "Integer32"
_UpsConfigLowOutputVoltageLimit_Object = MibScalar
upsConfigLowOutputVoltageLimit = _UpsConfigLowOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 6),
    _UpsConfigLowOutputVoltageLimit_Type()
)
upsConfigLowOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigLowOutputVoltageLimit.setStatus("mandatory")


class _UpsConfigHighOutputVoltageLimit_Type(Integer32):
    """Custom type upsConfigHighOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigHighOutputVoltageLimit_Type.__name__ = "Integer32"
_UpsConfigHighOutputVoltageLimit_Object = MibScalar
upsConfigHighOutputVoltageLimit = _UpsConfigHighOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 7),
    _UpsConfigHighOutputVoltageLimit_Type()
)
upsConfigHighOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigHighOutputVoltageLimit.setStatus("mandatory")
_UpsRecep_ObjectIdentity = ObjectIdentity
upsRecep = _UpsRecep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10)
)


class _UpsNumReceptacles_Type(Integer32):
    """Custom type upsNumReceptacles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_UpsNumReceptacles_Type.__name__ = "Integer32"
_UpsNumReceptacles_Object = MibScalar
upsNumReceptacles = _UpsNumReceptacles_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 1),
    _UpsNumReceptacles_Type()
)
upsNumReceptacles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsNumReceptacles.setStatus("mandatory")
_UpsRecepTable_Object = MibTable
upsRecepTable = _UpsRecepTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2)
)
if mibBuilder.loadTexts:
    upsRecepTable.setStatus("mandatory")
_UpsRecepEntry_Object = MibTableRow
upsRecepEntry = _UpsRecepEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1)
)
upsRecepEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsRecepIndex"),
)
if mibBuilder.loadTexts:
    upsRecepEntry.setStatus("mandatory")


class _UpsRecepIndex_Type(Integer32):
    """Custom type upsRecepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_UpsRecepIndex_Type.__name__ = "Integer32"
_UpsRecepIndex_Object = MibTableColumn
upsRecepIndex = _UpsRecepIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 1),
    _UpsRecepIndex_Type()
)
upsRecepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRecepIndex.setStatus("mandatory")


class _UpsRecepStatus_Type(Integer32):
    """Custom type upsRecepStatus based on Integer32"""
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
        *(("off", 2),
          ("on", 1),
          ("pendingOff", 3),
          ("pendingOn", 4),
          ("unknown", 5))
    )


_UpsRecepStatus_Type.__name__ = "Integer32"
_UpsRecepStatus_Object = MibTableColumn
upsRecepStatus = _UpsRecepStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 2),
    _UpsRecepStatus_Type()
)
upsRecepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRecepStatus.setStatus("mandatory")


class _UpsRecepOffDelaySecs_Type(Integer32):
    """Custom type upsRecepOffDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsRecepOffDelaySecs_Type.__name__ = "Integer32"
_UpsRecepOffDelaySecs_Object = MibTableColumn
upsRecepOffDelaySecs = _UpsRecepOffDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 3),
    _UpsRecepOffDelaySecs_Type()
)
upsRecepOffDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepOffDelaySecs.setStatus("mandatory")


class _UpsRecepOnDelaySecs_Type(Integer32):
    """Custom type upsRecepOnDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsRecepOnDelaySecs_Type.__name__ = "Integer32"
_UpsRecepOnDelaySecs_Object = MibTableColumn
upsRecepOnDelaySecs = _UpsRecepOnDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 4),
    _UpsRecepOnDelaySecs_Type()
)
upsRecepOnDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepOnDelaySecs.setStatus("mandatory")


class _UpsRecepAutoOffDelay_Type(Integer32):
    """Custom type upsRecepAutoOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsRecepAutoOffDelay_Type.__name__ = "Integer32"
_UpsRecepAutoOffDelay_Object = MibTableColumn
upsRecepAutoOffDelay = _UpsRecepAutoOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 5),
    _UpsRecepAutoOffDelay_Type()
)
upsRecepAutoOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepAutoOffDelay.setStatus("mandatory")


class _UpsRecepAutoOnDelay_Type(Integer32):
    """Custom type upsRecepAutoOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsRecepAutoOnDelay_Type.__name__ = "Integer32"
_UpsRecepAutoOnDelay_Object = MibTableColumn
upsRecepAutoOnDelay = _UpsRecepAutoOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 6),
    _UpsRecepAutoOnDelay_Type()
)
upsRecepAutoOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepAutoOnDelay.setStatus("mandatory")


class _UpsRecepShedSecsWithRestart_Type(Integer32):
    """Custom type upsRecepShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsRecepShedSecsWithRestart_Type.__name__ = "Integer32"
_UpsRecepShedSecsWithRestart_Object = MibTableColumn
upsRecepShedSecsWithRestart = _UpsRecepShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 7),
    _UpsRecepShedSecsWithRestart_Type()
)
upsRecepShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepShedSecsWithRestart.setStatus("mandatory")
_UpsTopology_ObjectIdentity = ObjectIdentity
upsTopology = _UpsTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11)
)


class _UpsTopologyType_Type(Integer32):
    """Custom type upsTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsTopologyType_Type.__name__ = "Integer32"
_UpsTopologyType_Object = MibScalar
upsTopologyType = _UpsTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 1),
    _UpsTopologyType_Type()
)
upsTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopologyType.setStatus("mandatory")


class _UpsTopoMachineCode_Type(Integer32):
    """Custom type upsTopoMachineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsTopoMachineCode_Type.__name__ = "Integer32"
_UpsTopoMachineCode_Object = MibScalar
upsTopoMachineCode = _UpsTopoMachineCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 2),
    _UpsTopoMachineCode_Type()
)
upsTopoMachineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopoMachineCode.setStatus("mandatory")


class _UpsTopoUnitNumber_Type(Integer32):
    """Custom type upsTopoUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_UpsTopoUnitNumber_Type.__name__ = "Integer32"
_UpsTopoUnitNumber_Object = MibScalar
upsTopoUnitNumber = _UpsTopoUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 3),
    _UpsTopoUnitNumber_Type()
)
upsTopoUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopoUnitNumber.setStatus("mandatory")


class _UpsTopoPowerStrategy_Type(Integer32):
    """Custom type upsTopoPowerStrategy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enableHighEfficiency", 3),
          ("highAlert", 1),
          ("immediateHighEfficiency", 4),
          ("standard", 2))
    )


_UpsTopoPowerStrategy_Type.__name__ = "Integer32"
_UpsTopoPowerStrategy_Object = MibScalar
upsTopoPowerStrategy = _UpsTopoPowerStrategy_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 4),
    _UpsTopoPowerStrategy_Type()
)
upsTopoPowerStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTopoPowerStrategy.setStatus("mandatory")
_Pdr_ObjectIdentity = ObjectIdentity
pdr = _Pdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4)
)
_PdrIdent_ObjectIdentity = ObjectIdentity
pdrIdent = _PdrIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1)
)


class _PdrName_Type(DisplayString):
    """Custom type pdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrName_Type.__name__ = "DisplayString"
_PdrName_Object = MibScalar
pdrName = _PdrName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 1),
    _PdrName_Type()
)
pdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdrName.setStatus("mandatory")


class _PdrModel_Type(DisplayString):
    """Custom type pdrModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrModel_Type.__name__ = "DisplayString"
_PdrModel_Object = MibScalar
pdrModel = _PdrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 2),
    _PdrModel_Type()
)
pdrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrModel.setStatus("mandatory")


class _PdrManufacturer_Type(DisplayString):
    """Custom type pdrManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrManufacturer_Type.__name__ = "DisplayString"
_PdrManufacturer_Object = MibScalar
pdrManufacturer = _PdrManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 3),
    _PdrManufacturer_Type()
)
pdrManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrManufacturer.setStatus("mandatory")


class _PdrFirmwareVersion_Type(DisplayString):
    """Custom type pdrFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrFirmwareVersion_Type.__name__ = "DisplayString"
_PdrFirmwareVersion_Object = MibScalar
pdrFirmwareVersion = _PdrFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 4),
    _PdrFirmwareVersion_Type()
)
pdrFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrFirmwareVersion.setStatus("mandatory")


class _PdrPartNumber_Type(DisplayString):
    """Custom type pdrPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrPartNumber_Type.__name__ = "DisplayString"
_PdrPartNumber_Object = MibScalar
pdrPartNumber = _PdrPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 5),
    _PdrPartNumber_Type()
)
pdrPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPartNumber.setStatus("mandatory")


class _PdrSerialNumber_Type(DisplayString):
    """Custom type pdrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrSerialNumber_Type.__name__ = "DisplayString"
_PdrSerialNumber_Object = MibScalar
pdrSerialNumber = _PdrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 6),
    _PdrSerialNumber_Type()
)
pdrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrSerialNumber.setStatus("mandatory")


class _PdrVARating_Type(Integer32):
    """Custom type pdrVARating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrVARating_Type.__name__ = "Integer32"
_PdrVARating_Object = MibScalar
pdrVARating = _PdrVARating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 7),
    _PdrVARating_Type()
)
pdrVARating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrVARating.setStatus("mandatory")


class _PdrNominalOutputVoltage_Type(Integer32):
    """Custom type pdrNominalOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrNominalOutputVoltage_Type.__name__ = "Integer32"
_PdrNominalOutputVoltage_Object = MibScalar
pdrNominalOutputVoltage = _PdrNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 8),
    _PdrNominalOutputVoltage_Type()
)
pdrNominalOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNominalOutputVoltage.setStatus("mandatory")


class _PdrNumPhases_Type(Integer32):
    """Custom type pdrNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PdrNumPhases_Type.__name__ = "Integer32"
_PdrNumPhases_Object = MibScalar
pdrNumPhases = _PdrNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 9),
    _PdrNumPhases_Type()
)
pdrNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumPhases.setStatus("mandatory")


class _PdrNumPanels_Type(Integer32):
    """Custom type pdrNumPanels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PdrNumPanels_Type.__name__ = "Integer32"
_PdrNumPanels_Object = MibScalar
pdrNumPanels = _PdrNumPanels_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 10),
    _PdrNumPanels_Type()
)
pdrNumPanels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumPanels.setStatus("mandatory")


class _PdrNumBreakers_Type(Integer32):
    """Custom type pdrNumBreakers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PdrNumBreakers_Type.__name__ = "Integer32"
_PdrNumBreakers_Object = MibScalar
pdrNumBreakers = _PdrNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 11),
    _PdrNumBreakers_Type()
)
pdrNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumBreakers.setStatus("mandatory")
_PdrPanel_ObjectIdentity = ObjectIdentity
pdrPanel = _PdrPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2)
)
_PdrPanelTable_Object = MibTable
pdrPanelTable = _PdrPanelTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pdrPanelTable.setStatus("mandatory")
_PdrPanelEntry_Object = MibTableRow
pdrPanelEntry = _PdrPanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1)
)
pdrPanelEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdrPanelIndex"),
)
if mibBuilder.loadTexts:
    pdrPanelEntry.setStatus("mandatory")
_PdrPanelIndex_Type = Integer32
_PdrPanelIndex_Object = MibTableColumn
pdrPanelIndex = _PdrPanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 1),
    _PdrPanelIndex_Type()
)
pdrPanelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelIndex.setStatus("mandatory")


class _PdrPanelFrequency_Type(Integer32):
    """Custom type pdrPanelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelFrequency_Type.__name__ = "Integer32"
_PdrPanelFrequency_Object = MibTableColumn
pdrPanelFrequency = _PdrPanelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 2),
    _PdrPanelFrequency_Type()
)
pdrPanelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelFrequency.setStatus("mandatory")


class _PdrPanelPower_Type(Integer32):
    """Custom type pdrPanelPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelPower_Type.__name__ = "Integer32"
_PdrPanelPower_Object = MibTableColumn
pdrPanelPower = _PdrPanelPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 3),
    _PdrPanelPower_Type()
)
pdrPanelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelPower.setStatus("mandatory")


class _PdrPanelRatedCurrent_Type(Integer32):
    """Custom type pdrPanelRatedCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelRatedCurrent_Type.__name__ = "Integer32"
_PdrPanelRatedCurrent_Object = MibTableColumn
pdrPanelRatedCurrent = _PdrPanelRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 4),
    _PdrPanelRatedCurrent_Type()
)
pdrPanelRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelRatedCurrent.setStatus("mandatory")


class _PdrPanelMonthlyKWH_Type(Integer32):
    """Custom type pdrPanelMonthlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelMonthlyKWH_Type.__name__ = "Integer32"
_PdrPanelMonthlyKWH_Object = MibTableColumn
pdrPanelMonthlyKWH = _PdrPanelMonthlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 5),
    _PdrPanelMonthlyKWH_Type()
)
pdrPanelMonthlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelMonthlyKWH.setStatus("mandatory")


class _PdrPanelYearlyKWH_Type(Integer32):
    """Custom type pdrPanelYearlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelYearlyKWH_Type.__name__ = "Integer32"
_PdrPanelYearlyKWH_Object = MibTableColumn
pdrPanelYearlyKWH = _PdrPanelYearlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 6),
    _PdrPanelYearlyKWH_Type()
)
pdrPanelYearlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelYearlyKWH.setStatus("mandatory")


class _PdrPanelTotalKWH_Type(Integer32):
    """Custom type pdrPanelTotalKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelTotalKWH_Type.__name__ = "Integer32"
_PdrPanelTotalKWH_Object = MibTableColumn
pdrPanelTotalKWH = _PdrPanelTotalKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 7),
    _PdrPanelTotalKWH_Type()
)
pdrPanelTotalKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelTotalKWH.setStatus("mandatory")


class _PdrPanelVoltageA_Type(Integer32):
    """Custom type pdrPanelVoltageA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageA_Type.__name__ = "Integer32"
_PdrPanelVoltageA_Object = MibTableColumn
pdrPanelVoltageA = _PdrPanelVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 8),
    _PdrPanelVoltageA_Type()
)
pdrPanelVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageA.setStatus("mandatory")


class _PdrPanelVoltageB_Type(Integer32):
    """Custom type pdrPanelVoltageB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageB_Type.__name__ = "Integer32"
_PdrPanelVoltageB_Object = MibTableColumn
pdrPanelVoltageB = _PdrPanelVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 9),
    _PdrPanelVoltageB_Type()
)
pdrPanelVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageB.setStatus("mandatory")


class _PdrPanelVoltageC_Type(Integer32):
    """Custom type pdrPanelVoltageC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageC_Type.__name__ = "Integer32"
_PdrPanelVoltageC_Object = MibTableColumn
pdrPanelVoltageC = _PdrPanelVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 10),
    _PdrPanelVoltageC_Type()
)
pdrPanelVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageC.setStatus("mandatory")


class _PdrPanelCurrentA_Type(Integer32):
    """Custom type pdrPanelCurrentA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentA_Type.__name__ = "Integer32"
_PdrPanelCurrentA_Object = MibTableColumn
pdrPanelCurrentA = _PdrPanelCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 11),
    _PdrPanelCurrentA_Type()
)
pdrPanelCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentA.setStatus("mandatory")


class _PdrPanelCurrentB_Type(Integer32):
    """Custom type pdrPanelCurrentB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentB_Type.__name__ = "Integer32"
_PdrPanelCurrentB_Object = MibTableColumn
pdrPanelCurrentB = _PdrPanelCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 12),
    _PdrPanelCurrentB_Type()
)
pdrPanelCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentB.setStatus("mandatory")


class _PdrPanelCurrentC_Type(Integer32):
    """Custom type pdrPanelCurrentC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentC_Type.__name__ = "Integer32"
_PdrPanelCurrentC_Object = MibTableColumn
pdrPanelCurrentC = _PdrPanelCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 13),
    _PdrPanelCurrentC_Type()
)
pdrPanelCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentC.setStatus("mandatory")


class _PdrPanelLoadA_Type(Integer32):
    """Custom type pdrPanelLoadA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadA_Type.__name__ = "Integer32"
_PdrPanelLoadA_Object = MibTableColumn
pdrPanelLoadA = _PdrPanelLoadA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 14),
    _PdrPanelLoadA_Type()
)
pdrPanelLoadA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadA.setStatus("mandatory")


class _PdrPanelLoadB_Type(Integer32):
    """Custom type pdrPanelLoadB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadB_Type.__name__ = "Integer32"
_PdrPanelLoadB_Object = MibTableColumn
pdrPanelLoadB = _PdrPanelLoadB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 15),
    _PdrPanelLoadB_Type()
)
pdrPanelLoadB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadB.setStatus("mandatory")


class _PdrPanelLoadC_Type(Integer32):
    """Custom type pdrPanelLoadC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadC_Type.__name__ = "Integer32"
_PdrPanelLoadC_Object = MibTableColumn
pdrPanelLoadC = _PdrPanelLoadC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 16),
    _PdrPanelLoadC_Type()
)
pdrPanelLoadC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadC.setStatus("mandatory")
_PdrBreaker_ObjectIdentity = ObjectIdentity
pdrBreaker = _PdrBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3)
)
_PdrBreakerTable_Object = MibTable
pdrBreakerTable = _PdrBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1)
)
if mibBuilder.loadTexts:
    pdrBreakerTable.setStatus("mandatory")
_PdrBreakerEntry_Object = MibTableRow
pdrBreakerEntry = _PdrBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1)
)
pdrBreakerEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdrPanelIndex"),
    (0, "CPQPOWER-MIB", "pdrBreakerIndex"),
)
if mibBuilder.loadTexts:
    pdrBreakerEntry.setStatus("mandatory")
_PdrBreakerIndex_Type = Integer32
_PdrBreakerIndex_Object = MibTableColumn
pdrBreakerIndex = _PdrBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 1),
    _PdrBreakerIndex_Type()
)
pdrBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerIndex.setStatus("mandatory")
_PdrBreakerPanel_Type = Integer32
_PdrBreakerPanel_Object = MibTableColumn
pdrBreakerPanel = _PdrBreakerPanel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 2),
    _PdrBreakerPanel_Type()
)
pdrBreakerPanel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPanel.setStatus("mandatory")
_PdrBreakerNumPosition_Type = Integer32
_PdrBreakerNumPosition_Object = MibTableColumn
pdrBreakerNumPosition = _PdrBreakerNumPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 3),
    _PdrBreakerNumPosition_Type()
)
pdrBreakerNumPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumPosition.setStatus("mandatory")
_PdrBreakerNumPhases_Type = Integer32
_PdrBreakerNumPhases_Object = MibTableColumn
pdrBreakerNumPhases = _PdrBreakerNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 4),
    _PdrBreakerNumPhases_Type()
)
pdrBreakerNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumPhases.setStatus("mandatory")
_PdrBreakerNumSequence_Type = Integer32
_PdrBreakerNumSequence_Object = MibTableColumn
pdrBreakerNumSequence = _PdrBreakerNumSequence_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 5),
    _PdrBreakerNumSequence_Type()
)
pdrBreakerNumSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumSequence.setStatus("mandatory")
_PdrBreakerRatedCurrent_Type = Integer32
_PdrBreakerRatedCurrent_Object = MibTableColumn
pdrBreakerRatedCurrent = _PdrBreakerRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 6),
    _PdrBreakerRatedCurrent_Type()
)
pdrBreakerRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerRatedCurrent.setStatus("mandatory")


class _PdrBreakerMonthlyKWH_Type(Integer32):
    """Custom type pdrBreakerMonthlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerMonthlyKWH_Type.__name__ = "Integer32"
_PdrBreakerMonthlyKWH_Object = MibTableColumn
pdrBreakerMonthlyKWH = _PdrBreakerMonthlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 7),
    _PdrBreakerMonthlyKWH_Type()
)
pdrBreakerMonthlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerMonthlyKWH.setStatus("mandatory")


class _PdrBreakerYearlyKWH_Type(Integer32):
    """Custom type pdrBreakerYearlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerYearlyKWH_Type.__name__ = "Integer32"
_PdrBreakerYearlyKWH_Object = MibTableColumn
pdrBreakerYearlyKWH = _PdrBreakerYearlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 8),
    _PdrBreakerYearlyKWH_Type()
)
pdrBreakerYearlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerYearlyKWH.setStatus("mandatory")


class _PdrBreakerTotalKWH_Type(Integer32):
    """Custom type pdrBreakerTotalKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerTotalKWH_Type.__name__ = "Integer32"
_PdrBreakerTotalKWH_Object = MibTableColumn
pdrBreakerTotalKWH = _PdrBreakerTotalKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 9),
    _PdrBreakerTotalKWH_Type()
)
pdrBreakerTotalKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerTotalKWH.setStatus("mandatory")


class _PdrBreakerCurrent_Type(Integer32):
    """Custom type pdrBreakerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerCurrent_Type.__name__ = "Integer32"
_PdrBreakerCurrent_Object = MibTableColumn
pdrBreakerCurrent = _PdrBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 10),
    _PdrBreakerCurrent_Type()
)
pdrBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerCurrent.setStatus("mandatory")


class _PdrBreakerCurrentPercent_Type(Integer32):
    """Custom type pdrBreakerCurrentPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrBreakerCurrentPercent_Type.__name__ = "Integer32"
_PdrBreakerCurrentPercent_Object = MibTableColumn
pdrBreakerCurrentPercent = _PdrBreakerCurrentPercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 11),
    _PdrBreakerCurrentPercent_Type()
)
pdrBreakerCurrentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerCurrentPercent.setStatus("mandatory")
_PdrBreakerPower_Type = Integer32
_PdrBreakerPower_Object = MibTableColumn
pdrBreakerPower = _PdrBreakerPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 12),
    _PdrBreakerPower_Type()
)
pdrBreakerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPower.setStatus("mandatory")


class _PdrBreakerPercentWarning_Type(Integer32):
    """Custom type pdrBreakerPercentWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrBreakerPercentWarning_Type.__name__ = "Integer32"
_PdrBreakerPercentWarning_Object = MibTableColumn
pdrBreakerPercentWarning = _PdrBreakerPercentWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 13),
    _PdrBreakerPercentWarning_Type()
)
pdrBreakerPercentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPercentWarning.setStatus("mandatory")
_PdrBreakerPercentOverload_Type = Integer32
_PdrBreakerPercentOverload_Object = MibTableColumn
pdrBreakerPercentOverload = _PdrBreakerPercentOverload_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 14),
    _PdrBreakerPercentOverload_Type()
)
pdrBreakerPercentOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPercentOverload.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 1)
)
trapCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapCritical.setStatus(
        ""
    )

trapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 2)
)
trapWarning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapWarning.setStatus(
        ""
    )

trapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 3)
)
trapInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapInformation.setStatus(
        ""
    )

trapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 4)
)
trapCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapCleared.setStatus(
        ""
    )

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 5)
)
trapTest.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

deviceTrapInitialization = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 6)
)
deviceTrapInitialization.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "deviceIdentName"))
)
if mibBuilder.loadTexts:
    deviceTrapInitialization.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQPOWER-MIB",
    **{"cpqPower": cpqPower,
       "trapCritical": trapCritical,
       "trapWarning": trapWarning,
       "trapInformation": trapInformation,
       "trapCleared": trapCleared,
       "trapTest": trapTest,
       "deviceTrapInitialization": deviceTrapInitialization,
       "powerDevice": powerDevice,
       "trapInfo": trapInfo,
       "trapCode": trapCode,
       "trapDescription": trapDescription,
       "trapDeviceMgmtUrl": trapDeviceMgmtUrl,
       "trapDeviceDetails": trapDeviceDetails,
       "trapDeviceName": trapDeviceName,
       "managementModuleIdent": managementModuleIdent,
       "deviceManufacturer": deviceManufacturer,
       "deviceModel": deviceModel,
       "deviceFirmwareVersion": deviceFirmwareVersion,
       "deviceHardwareVersion": deviceHardwareVersion,
       "deviceIdentName": deviceIdentName,
       "devicePartNumber": devicePartNumber,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceMACAddress": deviceMACAddress,
       "pdu": pdu,
       "pduIdent": pduIdent,
       "numOfPdu": numOfPdu,
       "pduIdentTable": pduIdentTable,
       "pduIdentEntry": pduIdentEntry,
       "pduIdentIndex": pduIdentIndex,
       "pduName": pduName,
       "pduModel": pduModel,
       "pduManufacturer": pduManufacturer,
       "pduFirmwareVersion": pduFirmwareVersion,
       "pduPartNumber": pduPartNumber,
       "pduSerialNumber": pduSerialNumber,
       "pduStatus": pduStatus,
       "pduControllable": pduControllable,
       "pduInput": pduInput,
       "pduInputTable": pduInputTable,
       "pduInputEntry": pduInputEntry,
       "pduInputIndex": pduInputIndex,
       "inputVoltage": inputVoltage,
       "inputCurrent": inputCurrent,
       "pduOutput": pduOutput,
       "pduOutputTable": pduOutputTable,
       "pduOutputEntry": pduOutputEntry,
       "pduOutputIndex": pduOutputIndex,
       "pduOutputLoad": pduOutputLoad,
       "pduOutputHeat": pduOutputHeat,
       "pduOutputPower": pduOutputPower,
       "pduOutputNumBreakers": pduOutputNumBreakers,
       "pduOutputBreakerTable": pduOutputBreakerTable,
       "pduOutputBreakerEntry": pduOutputBreakerEntry,
       "breakerIndex": breakerIndex,
       "breakerVoltage": breakerVoltage,
       "breakerCurrent": breakerCurrent,
       "breakerPercentLoad": breakerPercentLoad,
       "breakerStatus": breakerStatus,
       "ups": ups,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentModel": upsIdentModel,
       "upsIdentSoftwareVersions": upsIdentSoftwareVersions,
       "upsIdentOemCode": upsIdentOemCode,
       "upsBattery": upsBattery,
       "upsBatTimeRemaining": upsBatTimeRemaining,
       "upsBatVoltage": upsBatVoltage,
       "upsBatCurrent": upsBatCurrent,
       "upsBatCapacity": upsBatCapacity,
       "upsBatteryAbmStatus": upsBatteryAbmStatus,
       "upsInput": upsInput,
       "upsInputFrequency": upsInputFrequency,
       "upsInputLineBads": upsInputLineBads,
       "upsInputNumPhases": upsInputNumPhases,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputPhase": upsInputPhase,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputWatts": upsInputWatts,
       "upsInputSource": upsInputSource,
       "upsOutput": upsOutput,
       "upsOutputLoad": upsOutputLoad,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumPhases": upsOutputNumPhases,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputPhase": upsOutputPhase,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputWatts": upsOutputWatts,
       "upsOutputSource": upsOutputSource,
       "upsBypass": upsBypass,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBypassNumPhases": upsBypassNumPhases,
       "upsBypassTable": upsBypassTable,
       "upsBypassEntry": upsBypassEntry,
       "upsBypassPhase": upsBypassPhase,
       "upsBypassVoltage": upsBypassVoltage,
       "upsEnvironment": upsEnvironment,
       "upsEnvAmbientTemp": upsEnvAmbientTemp,
       "upsEnvAmbientLowerLimit": upsEnvAmbientLowerLimit,
       "upsEnvAmbientUpperLimit": upsEnvAmbientUpperLimit,
       "upsEnvAmbientHumidity": upsEnvAmbientHumidity,
       "upsEnvRemoteTemp": upsEnvRemoteTemp,
       "upsEnvRemoteHumidity": upsEnvRemoteHumidity,
       "upsEnvNumContacts": upsEnvNumContacts,
       "upsContactsTable": upsContactsTable,
       "upsContactsTableEntry": upsContactsTableEntry,
       "upsContactIndex": upsContactIndex,
       "upsContactType": upsContactType,
       "upsContactState": upsContactState,
       "upsContactDescr": upsContactDescr,
       "upsEnvRemoteTempLowerLimit": upsEnvRemoteTempLowerLimit,
       "upsEnvRemoteTempUpperLimit": upsEnvRemoteTempUpperLimit,
       "upsEnvRemoteHumidityLowerLimit": upsEnvRemoteHumidityLowerLimit,
       "upsEnvRemoteHumidityUpperLimit": upsEnvRemoteHumidityUpperLimit,
       "upsTest": upsTest,
       "upsTestBattery": upsTestBattery,
       "upsTestBatteryStatus": upsTestBatteryStatus,
       "upsTestTrap": upsTestTrap,
       "upsControl": upsControl,
       "upsControlOutputOffDelay": upsControlOutputOffDelay,
       "upsControlOutputOnDelay": upsControlOutputOnDelay,
       "upsControlOutputOffTrapDelay": upsControlOutputOffTrapDelay,
       "upsControlOutputOnTrapDelay": upsControlOutputOnTrapDelay,
       "upsControlToBypassDelay": upsControlToBypassDelay,
       "upsLoadShedSecsWithRestart": upsLoadShedSecsWithRestart,
       "upsConfig": upsConfig,
       "upsConfigOutputVoltage": upsConfigOutputVoltage,
       "upsConfigInputVoltage": upsConfigInputVoltage,
       "upsConfigOutputWatts": upsConfigOutputWatts,
       "upsConfigOutputFreq": upsConfigOutputFreq,
       "upsConfigDateAndTime": upsConfigDateAndTime,
       "upsConfigLowOutputVoltageLimit": upsConfigLowOutputVoltageLimit,
       "upsConfigHighOutputVoltageLimit": upsConfigHighOutputVoltageLimit,
       "upsRecep": upsRecep,
       "upsNumReceptacles": upsNumReceptacles,
       "upsRecepTable": upsRecepTable,
       "upsRecepEntry": upsRecepEntry,
       "upsRecepIndex": upsRecepIndex,
       "upsRecepStatus": upsRecepStatus,
       "upsRecepOffDelaySecs": upsRecepOffDelaySecs,
       "upsRecepOnDelaySecs": upsRecepOnDelaySecs,
       "upsRecepAutoOffDelay": upsRecepAutoOffDelay,
       "upsRecepAutoOnDelay": upsRecepAutoOnDelay,
       "upsRecepShedSecsWithRestart": upsRecepShedSecsWithRestart,
       "upsTopology": upsTopology,
       "upsTopologyType": upsTopologyType,
       "upsTopoMachineCode": upsTopoMachineCode,
       "upsTopoUnitNumber": upsTopoUnitNumber,
       "upsTopoPowerStrategy": upsTopoPowerStrategy,
       "pdr": pdr,
       "pdrIdent": pdrIdent,
       "pdrName": pdrName,
       "pdrModel": pdrModel,
       "pdrManufacturer": pdrManufacturer,
       "pdrFirmwareVersion": pdrFirmwareVersion,
       "pdrPartNumber": pdrPartNumber,
       "pdrSerialNumber": pdrSerialNumber,
       "pdrVARating": pdrVARating,
       "pdrNominalOutputVoltage": pdrNominalOutputVoltage,
       "pdrNumPhases": pdrNumPhases,
       "pdrNumPanels": pdrNumPanels,
       "pdrNumBreakers": pdrNumBreakers,
       "pdrPanel": pdrPanel,
       "pdrPanelTable": pdrPanelTable,
       "pdrPanelEntry": pdrPanelEntry,
       "pdrPanelIndex": pdrPanelIndex,
       "pdrPanelFrequency": pdrPanelFrequency,
       "pdrPanelPower": pdrPanelPower,
       "pdrPanelRatedCurrent": pdrPanelRatedCurrent,
       "pdrPanelMonthlyKWH": pdrPanelMonthlyKWH,
       "pdrPanelYearlyKWH": pdrPanelYearlyKWH,
       "pdrPanelTotalKWH": pdrPanelTotalKWH,
       "pdrPanelVoltageA": pdrPanelVoltageA,
       "pdrPanelVoltageB": pdrPanelVoltageB,
       "pdrPanelVoltageC": pdrPanelVoltageC,
       "pdrPanelCurrentA": pdrPanelCurrentA,
       "pdrPanelCurrentB": pdrPanelCurrentB,
       "pdrPanelCurrentC": pdrPanelCurrentC,
       "pdrPanelLoadA": pdrPanelLoadA,
       "pdrPanelLoadB": pdrPanelLoadB,
       "pdrPanelLoadC": pdrPanelLoadC,
       "pdrBreaker": pdrBreaker,
       "pdrBreakerTable": pdrBreakerTable,
       "pdrBreakerEntry": pdrBreakerEntry,
       "pdrBreakerIndex": pdrBreakerIndex,
       "pdrBreakerPanel": pdrBreakerPanel,
       "pdrBreakerNumPosition": pdrBreakerNumPosition,
       "pdrBreakerNumPhases": pdrBreakerNumPhases,
       "pdrBreakerNumSequence": pdrBreakerNumSequence,
       "pdrBreakerRatedCurrent": pdrBreakerRatedCurrent,
       "pdrBreakerMonthlyKWH": pdrBreakerMonthlyKWH,
       "pdrBreakerYearlyKWH": pdrBreakerYearlyKWH,
       "pdrBreakerTotalKWH": pdrBreakerTotalKWH,
       "pdrBreakerCurrent": pdrBreakerCurrent,
       "pdrBreakerCurrentPercent": pdrBreakerCurrentPercent,
       "pdrBreakerPower": pdrBreakerPower,
       "pdrBreakerPercentWarning": pdrBreakerPercentWarning,
       "pdrBreakerPercentOverload": pdrBreakerPercentOverload}
)
