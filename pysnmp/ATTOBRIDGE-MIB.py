# SNMP MIB module (ATTOBRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATTOBRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:22 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TimeTicks,
 Unsigned32,
 enterprises,
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

bridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Attotech_ObjectIdentity = ObjectIdentity
attotech = _Attotech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1)
)
_BridgeConfig_ObjectIdentity = ObjectIdentity
bridgeConfig = _BridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 1)
)


class _TrapsEnabled_Type(Integer32):
    """Custom type trapsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TrapsEnabled_Type.__name__ = "Integer32"
_TrapsEnabled_Object = MibScalar
trapsEnabled = _TrapsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 1),
    _TrapsEnabled_Type()
)
trapsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsEnabled.setStatus("mandatory")


class _SnmpUpdatesEnabled_Type(Integer32):
    """Custom type snmpUpdatesEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SnmpUpdatesEnabled_Type.__name__ = "Integer32"
_SnmpUpdatesEnabled_Object = MibScalar
snmpUpdatesEnabled = _SnmpUpdatesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 2),
    _SnmpUpdatesEnabled_Type()
)
snmpUpdatesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUpdatesEnabled.setStatus("mandatory")


class _SnmpExtendedEnabled_Type(Integer32):
    """Custom type snmpExtendedEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SnmpExtendedEnabled_Type.__name__ = "Integer32"
_SnmpExtendedEnabled_Object = MibScalar
snmpExtendedEnabled = _SnmpExtendedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 1, 3),
    _SnmpExtendedEnabled_Type()
)
snmpExtendedEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpExtendedEnabled.setStatus("mandatory")
_BridgeStatus_ObjectIdentity = ObjectIdentity
bridgeStatus = _BridgeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2)
)
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("mandatory")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1)
)
tempSensorEntry.setIndexNames(
    (0, "ATTOBRIDGE-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("mandatory")


class _TempSensorIndex_Type(Integer32):
    """Custom type tempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TempSensorIndex_Type.__name__ = "Integer32"
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 1),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("mandatory")


class _TempSensorStatus_Type(Integer32):
    """Custom type tempSensorStatus based on Integer32"""
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
        *(("critical", 3),
          ("normal", 1),
          ("unknown", 4),
          ("warning", 2))
    )


_TempSensorStatus_Type.__name__ = "Integer32"
_TempSensorStatus_Object = MibTableColumn
tempSensorStatus = _TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 2),
    _TempSensorStatus_Type()
)
tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorStatus.setStatus("mandatory")
_Temperature_Type = Integer32
_Temperature_Object = MibTableColumn
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 1, 1, 3),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("mandatory")
_VoltageSensorTable_Object = MibTable
voltageSensorTable = _VoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    voltageSensorTable.setStatus("mandatory")
_VoltageSensorEntry_Object = MibTableRow
voltageSensorEntry = _VoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1)
)
voltageSensorEntry.setIndexNames(
    (0, "ATTOBRIDGE-MIB", "voltageSensorIndex"),
)
if mibBuilder.loadTexts:
    voltageSensorEntry.setStatus("mandatory")


class _VoltageSensorIndex_Type(Integer32):
    """Custom type voltageSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_VoltageSensorIndex_Type.__name__ = "Integer32"
_VoltageSensorIndex_Object = MibTableColumn
voltageSensorIndex = _VoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 1),
    _VoltageSensorIndex_Type()
)
voltageSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorIndex.setStatus("mandatory")


class _VoltageSensorStatus_Type(Integer32):
    """Custom type voltageSensorStatus based on Integer32"""
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
        *(("critical", 3),
          ("normal", 1),
          ("unknown", 4),
          ("warning", 2))
    )


_VoltageSensorStatus_Type.__name__ = "Integer32"
_VoltageSensorStatus_Object = MibTableColumn
voltageSensorStatus = _VoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 2),
    _VoltageSensorStatus_Type()
)
voltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorStatus.setStatus("mandatory")
_Voltage_Type = Integer32
_Voltage_Object = MibTableColumn
voltage = _Voltage_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 2, 1, 3),
    _Voltage_Type()
)
voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltage.setStatus("mandatory")
_DeviceCount_Type = Counter32
_DeviceCount_Object = MibScalar
deviceCount = _DeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 4),
    _DeviceCount_Type()
)
deviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCount.setStatus("mandatory")
_DeviceCacheTable_Object = MibTable
deviceCacheTable = _DeviceCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    deviceCacheTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1)
)
deviceEntry.setIndexNames(
    (0, "ATTOBRIDGE-MIB", "deviceCacheIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")


class _DeviceCacheIndex_Type(Integer32):
    """Custom type deviceCacheIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DeviceCacheIndex_Type.__name__ = "Integer32"
_DeviceCacheIndex_Object = MibTableColumn
deviceCacheIndex = _DeviceCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 1),
    _DeviceCacheIndex_Type()
)
deviceCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCacheIndex.setStatus("mandatory")


class _DeviceSource_Type(DisplayString):
    """Custom type deviceSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_DeviceSource_Type.__name__ = "DisplayString"
_DeviceSource_Object = MibTableColumn
deviceSource = _DeviceSource_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 2),
    _DeviceSource_Type()
)
deviceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSource.setStatus("mandatory")


class _DeviceDestination_Type(DisplayString):
    """Custom type deviceDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_DeviceDestination_Type.__name__ = "DisplayString"
_DeviceDestination_Object = MibTableColumn
deviceDestination = _DeviceDestination_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 3),
    _DeviceDestination_Type()
)
deviceDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDestination.setStatus("mandatory")


class _DeviceType_Type(DisplayString):
    """Custom type deviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceType_Type.__name__ = "DisplayString"
_DeviceType_Object = MibTableColumn
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 4),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("mandatory")


class _DeviceVendor_Type(DisplayString):
    """Custom type deviceVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DeviceVendor_Type.__name__ = "DisplayString"
_DeviceVendor_Object = MibTableColumn
deviceVendor = _DeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 5),
    _DeviceVendor_Type()
)
deviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceVendor.setStatus("mandatory")


class _DeviceProduct_Type(DisplayString):
    """Custom type deviceProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceProduct_Type.__name__ = "DisplayString"
_DeviceProduct_Object = MibTableColumn
deviceProduct = _DeviceProduct_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 6),
    _DeviceProduct_Type()
)
deviceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceProduct.setStatus("mandatory")


class _DeviceRevision_Type(DisplayString):
    """Custom type deviceRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DeviceRevision_Type.__name__ = "DisplayString"
_DeviceRevision_Object = MibTableColumn
deviceRevision = _DeviceRevision_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 7),
    _DeviceRevision_Type()
)
deviceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRevision.setStatus("mandatory")


class _DeviceState_Type(Integer32):
    """Custom type deviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("online", 1))
    )


_DeviceState_Type.__name__ = "Integer32"
_DeviceState_Object = MibTableColumn
deviceState = _DeviceState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 5, 1, 8),
    _DeviceState_Type()
)
deviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceState.setStatus("mandatory")
_ErrorCount_Type = Counter32
_ErrorCount_Object = MibScalar
errorCount = _ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 6),
    _ErrorCount_Type()
)
errorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCount.setStatus("mandatory")
_ErrorsSinceUpdate_Type = Counter32
_ErrorsSinceUpdate_Object = MibScalar
errorsSinceUpdate = _ErrorsSinceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 7),
    _ErrorsSinceUpdate_Type()
)
errorsSinceUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorsSinceUpdate.setStatus("mandatory")
_ErrorTable_Object = MibTable
errorTable = _ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    errorTable.setStatus("mandatory")
_ErrorEntry_Object = MibTableRow
errorEntry = _ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1)
)
errorEntry.setIndexNames(
    (0, "ATTOBRIDGE-MIB", "errorIndex"),
)
if mibBuilder.loadTexts:
    errorEntry.setStatus("mandatory")
_ErrorIndex_Type = Integer32
_ErrorIndex_Object = MibTableColumn
errorIndex = _ErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 1),
    _ErrorIndex_Type()
)
errorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorIndex.setStatus("mandatory")


class _ErrorDateStamp_Type(DisplayString):
    """Custom type errorDateStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_ErrorDateStamp_Type.__name__ = "DisplayString"
_ErrorDateStamp_Object = MibTableColumn
errorDateStamp = _ErrorDateStamp_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 2),
    _ErrorDateStamp_Type()
)
errorDateStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDateStamp.setStatus("mandatory")


class _ErrorTimeStamp_Type(DisplayString):
    """Custom type errorTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ErrorTimeStamp_Type.__name__ = "DisplayString"
_ErrorTimeStamp_Object = MibTableColumn
errorTimeStamp = _ErrorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 3),
    _ErrorTimeStamp_Type()
)
errorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorTimeStamp.setStatus("mandatory")


class _ErrorInitiator_Type(DisplayString):
    """Custom type errorInitiator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ErrorInitiator_Type.__name__ = "DisplayString"
_ErrorInitiator_Object = MibTableColumn
errorInitiator = _ErrorInitiator_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 4),
    _ErrorInitiator_Type()
)
errorInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorInitiator.setStatus("mandatory")


class _ErrorSource_Type(DisplayString):
    """Custom type errorSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ErrorSource_Type.__name__ = "DisplayString"
_ErrorSource_Object = MibTableColumn
errorSource = _ErrorSource_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 5),
    _ErrorSource_Type()
)
errorSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorSource.setStatus("mandatory")
_ErrorOpCode_Type = Integer32
_ErrorOpCode_Object = MibTableColumn
errorOpCode = _ErrorOpCode_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 6),
    _ErrorOpCode_Type()
)
errorOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorOpCode.setStatus("mandatory")
_ErrorSenseKey_Type = Integer32
_ErrorSenseKey_Object = MibTableColumn
errorSenseKey = _ErrorSenseKey_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 7),
    _ErrorSenseKey_Type()
)
errorSenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorSenseKey.setStatus("mandatory")
_ErrorASC_Type = Integer32
_ErrorASC_Object = MibTableColumn
errorASC = _ErrorASC_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 8),
    _ErrorASC_Type()
)
errorASC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorASC.setStatus("mandatory")
_ErrorASCQ_Type = Integer32
_ErrorASCQ_Object = MibTableColumn
errorASCQ = _ErrorASCQ_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 9),
    _ErrorASCQ_Type()
)
errorASCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorASCQ.setStatus("mandatory")


class _ErrorLogSense_Type(OctetString):
    """Custom type errorLogSense based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ErrorLogSense_Type.__name__ = "OctetString"
_ErrorLogSense_Object = MibTableColumn
errorLogSense = _ErrorLogSense_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 2, 8, 1, 10),
    _ErrorLogSense_Type()
)
errorLogSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorLogSense.setStatus("mandatory")
_BridgeTrapInfo_ObjectIdentity = ObjectIdentity
bridgeTrapInfo = _BridgeTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3)
)
_TrapMaxClients_Type = Integer32
_TrapMaxClients_Object = MibScalar
trapMaxClients = _TrapMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 1),
    _TrapMaxClients_Type()
)
trapMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMaxClients.setStatus("mandatory")
_TrapClientTable_Object = MibTable
trapClientTable = _TrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    trapClientTable.setStatus("mandatory")
_TrapClientEntry_Object = MibTableRow
trapClientEntry = _TrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1)
)
trapClientEntry.setIndexNames(
    (0, "ATTOBRIDGE-MIB", "trapClientIndex"),
)
if mibBuilder.loadTexts:
    trapClientEntry.setStatus("mandatory")
_TrapClientIndex_Type = Integer32
_TrapClientIndex_Object = MibTableColumn
trapClientIndex = _TrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 1),
    _TrapClientIndex_Type()
)
trapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientIndex.setStatus("mandatory")
_TrapClientIpAddress_Type = IpAddress
_TrapClientIpAddress_Object = MibTableColumn
trapClientIpAddress = _TrapClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 2),
    _TrapClientIpAddress_Type()
)
trapClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientIpAddress.setStatus("mandatory")


class _TrapClientPort_Type(Integer32):
    """Custom type trapClientPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapClientPort_Type.__name__ = "Integer32"
_TrapClientPort_Object = MibTableColumn
trapClientPort = _TrapClientPort_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 3),
    _TrapClientPort_Type()
)
trapClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientPort.setStatus("mandatory")


class _TrapClientFilter_Type(Integer32):
    """Custom type trapClientFilter based on Integer32"""
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
        *(("all", 5),
          ("critical", 2),
          ("informational", 4),
          ("none", 1),
          ("warning", 3))
    )


_TrapClientFilter_Type.__name__ = "Integer32"
_TrapClientFilter_Object = MibTableColumn
trapClientFilter = _TrapClientFilter_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 4),
    _TrapClientFilter_Type()
)
trapClientFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientFilter.setStatus("mandatory")


class _TrapClientRowState_Type(Integer32):
    """Custom type trapClientRowState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rowActive", 3),
          ("rowDestroy", 1),
          ("rowInactive", 2))
    )


_TrapClientRowState_Type.__name__ = "Integer32"
_TrapClientRowState_Object = MibTableColumn
trapClientRowState = _TrapClientRowState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 1, 2, 3, 3, 1, 5),
    _TrapClientRowState_Type()
)
trapClientRowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientRowState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bridgeTempStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 0, 1)
)
bridgeTempStatusChanged.setObjects(
      *(("ATTOBRIDGE-MIB", "tempSensorIndex"),
        ("ATTOBRIDGE-MIB", "tempSensorStatus"),
        ("ATTOBRIDGE-MIB", "temperature"))
)
if mibBuilder.loadTexts:
    bridgeTempStatusChanged.setStatus(
        ""
    )

bridgeVoltageStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 0, 2)
)
bridgeVoltageStatusChanged.setObjects(
      *(("ATTOBRIDGE-MIB", "voltageSensorIndex"),
        ("ATTOBRIDGE-MIB", "voltageSensorStatus"),
        ("ATTOBRIDGE-MIB", "voltage"))
)
if mibBuilder.loadTexts:
    bridgeVoltageStatusChanged.setStatus(
        ""
    )

bridgeDeviceTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 0, 4)
)
bridgeDeviceTransition.setObjects(
      *(("ATTOBRIDGE-MIB", "deviceCacheIndex"),
        ("ATTOBRIDGE-MIB", "deviceSource"),
        ("ATTOBRIDGE-MIB", "deviceState"))
)
if mibBuilder.loadTexts:
    bridgeDeviceTransition.setStatus(
        ""
    )

bridgeDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 0, 5)
)
bridgeDeviceError.setObjects(
      *(("ATTOBRIDGE-MIB", "errorSource"),
        ("ATTOBRIDGE-MIB", "errorOpCode"),
        ("ATTOBRIDGE-MIB", "errorSenseKey"),
        ("ATTOBRIDGE-MIB", "errorASC"),
        ("ATTOBRIDGE-MIB", "errorASCQ"),
        ("ATTOBRIDGE-MIB", "errorsSinceUpdate"))
)
if mibBuilder.loadTexts:
    bridgeDeviceError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATTOBRIDGE-MIB",
    **{"attotech": attotech,
       "bridgeTempStatusChanged": bridgeTempStatusChanged,
       "bridgeVoltageStatusChanged": bridgeVoltageStatusChanged,
       "bridgeDeviceTransition": bridgeDeviceTransition,
       "bridgeDeviceError": bridgeDeviceError,
       "products": products,
       "bridge": bridge,
       "bridgeConfig": bridgeConfig,
       "trapsEnabled": trapsEnabled,
       "snmpUpdatesEnabled": snmpUpdatesEnabled,
       "snmpExtendedEnabled": snmpExtendedEnabled,
       "bridgeStatus": bridgeStatus,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorIndex": tempSensorIndex,
       "tempSensorStatus": tempSensorStatus,
       "temperature": temperature,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorIndex": voltageSensorIndex,
       "voltageSensorStatus": voltageSensorStatus,
       "voltage": voltage,
       "deviceCount": deviceCount,
       "deviceCacheTable": deviceCacheTable,
       "deviceEntry": deviceEntry,
       "deviceCacheIndex": deviceCacheIndex,
       "deviceSource": deviceSource,
       "deviceDestination": deviceDestination,
       "deviceType": deviceType,
       "deviceVendor": deviceVendor,
       "deviceProduct": deviceProduct,
       "deviceRevision": deviceRevision,
       "deviceState": deviceState,
       "errorCount": errorCount,
       "errorsSinceUpdate": errorsSinceUpdate,
       "errorTable": errorTable,
       "errorEntry": errorEntry,
       "errorIndex": errorIndex,
       "errorDateStamp": errorDateStamp,
       "errorTimeStamp": errorTimeStamp,
       "errorInitiator": errorInitiator,
       "errorSource": errorSource,
       "errorOpCode": errorOpCode,
       "errorSenseKey": errorSenseKey,
       "errorASC": errorASC,
       "errorASCQ": errorASCQ,
       "errorLogSense": errorLogSense,
       "bridgeTrapInfo": bridgeTrapInfo,
       "trapMaxClients": trapMaxClients,
       "trapClientTable": trapClientTable,
       "trapClientEntry": trapClientEntry,
       "trapClientIndex": trapClientIndex,
       "trapClientIpAddress": trapClientIpAddress,
       "trapClientPort": trapClientPort,
       "trapClientFilter": trapClientFilter,
       "trapClientRowState": trapClientRowState}
)
