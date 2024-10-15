# SNMP MIB module (CPQWCRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQWCRM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:48 2024
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

_CpqWcrm_ObjectIdentity = ObjectIdentity
cpqWcrm = _CpqWcrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167)
)
_CpqWcrmMibRev_ObjectIdentity = ObjectIdentity
cpqWcrmMibRev = _CpqWcrmMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 1)
)


class _CpqWcrmMibMajRev_Type(Integer32):
    """Custom type cpqWcrmMibMajRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqWcrmMibMajRev_Type.__name__ = "Integer32"
_CpqWcrmMibMajRev_Object = MibScalar
cpqWcrmMibMajRev = _CpqWcrmMibMajRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 1, 1),
    _CpqWcrmMibMajRev_Type()
)
cpqWcrmMibMajRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmMibMajRev.setStatus("mandatory")


class _CpqWcrmMibMinRev_Type(Integer32):
    """Custom type cpqWcrmMibMinRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqWcrmMibMinRev_Type.__name__ = "Integer32"
_CpqWcrmMibMinRev_Object = MibScalar
cpqWcrmMibMinRev = _CpqWcrmMibMinRev_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 1, 2),
    _CpqWcrmMibMinRev_Type()
)
cpqWcrmMibMinRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmMibMinRev.setStatus("mandatory")


class _CpqWcrmMibCondition_Type(Integer32):
    """Custom type cpqWcrmMibCondition based on Integer32"""
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
        *(("configChanged", 5),
          ("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqWcrmMibCondition_Type.__name__ = "Integer32"
_CpqWcrmMibCondition_Object = MibScalar
cpqWcrmMibCondition = _CpqWcrmMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 1, 3),
    _CpqWcrmMibCondition_Type()
)
cpqWcrmMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmMibCondition.setStatus("mandatory")
_CpqWcrmStatus_ObjectIdentity = ObjectIdentity
cpqWcrmStatus = _CpqWcrmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2)
)


class _CpqWcrmStatusDeviceEnvironmentalController_Type(Integer32):
    """Custom type cpqWcrmStatusDeviceEnvironmentalController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2))
    )


_CpqWcrmStatusDeviceEnvironmentalController_Type.__name__ = "Integer32"
_CpqWcrmStatusDeviceEnvironmentalController_Object = MibScalar
cpqWcrmStatusDeviceEnvironmentalController = _CpqWcrmStatusDeviceEnvironmentalController_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 1),
    _CpqWcrmStatusDeviceEnvironmentalController_Type()
)
cpqWcrmStatusDeviceEnvironmentalController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmStatusDeviceEnvironmentalController.setStatus("mandatory")
_CpqWcrmUnitsConnected_Type = Integer32
_CpqWcrmUnitsConnected_Object = MibScalar
cpqWcrmUnitsConnected = _CpqWcrmUnitsConnected_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 2),
    _CpqWcrmUnitsConnected_Type()
)
cpqWcrmUnitsConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmUnitsConnected.setStatus("mandatory")
_CpqWcrmStatusSensorInternal_ObjectIdentity = ObjectIdentity
cpqWcrmStatusSensorInternal = _CpqWcrmStatusSensorInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3)
)


class _CpqWcrmInternalTypeOfDevice_Type(Integer32):
    """Custom type cpqWcrmInternalTypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitIO", 3),
          ("unitWcrm", 2))
    )


_CpqWcrmInternalTypeOfDevice_Type.__name__ = "Integer32"
_CpqWcrmInternalTypeOfDevice_Object = MibScalar
cpqWcrmInternalTypeOfDevice = _CpqWcrmInternalTypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 1),
    _CpqWcrmInternalTypeOfDevice_Type()
)
cpqWcrmInternalTypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalTypeOfDevice.setStatus("mandatory")


class _CpqWcrmInternalText_Type(DisplayString):
    """Custom type cpqWcrmInternalText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqWcrmInternalText_Type.__name__ = "DisplayString"
_CpqWcrmInternalText_Object = MibScalar
cpqWcrmInternalText = _CpqWcrmInternalText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 2),
    _CpqWcrmInternalText_Type()
)
cpqWcrmInternalText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmInternalText.setStatus("mandatory")
_CpqWcrmInternalSerial_Type = Integer32
_CpqWcrmInternalSerial_Object = MibScalar
cpqWcrmInternalSerial = _CpqWcrmInternalSerial_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 3),
    _CpqWcrmInternalSerial_Type()
)
cpqWcrmInternalSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalSerial.setStatus("mandatory")


class _CpqWcrmInternalStatus_Type(Integer32):
    """Custom type cpqWcrmInternalStatus based on Integer32"""
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
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("reset", 4),
          ("timeout", 5))
    )


_CpqWcrmInternalStatus_Type.__name__ = "Integer32"
_CpqWcrmInternalStatus_Object = MibScalar
cpqWcrmInternalStatus = _CpqWcrmInternalStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 4),
    _CpqWcrmInternalStatus_Type()
)
cpqWcrmInternalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalStatus.setStatus("mandatory")
_CpqWcrmStatusInternalSensors_ObjectIdentity = ObjectIdentity
cpqWcrmStatusInternalSensors = _CpqWcrmStatusInternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5)
)
_CpqWcrmInternalNumberOfSensors_Type = Integer32
_CpqWcrmInternalNumberOfSensors_Object = MibScalar
cpqWcrmInternalNumberOfSensors = _CpqWcrmInternalNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 1),
    _CpqWcrmInternalNumberOfSensors_Type()
)
cpqWcrmInternalNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalNumberOfSensors.setStatus("mandatory")
_CpqWcrmInternalSensorTable_Object = MibTable
cpqWcrmInternalSensorTable = _CpqWcrmInternalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmInternalSensorTable.setStatus("mandatory")
_CpqWcrmInternalSensorEntry_Object = MibTableRow
cpqWcrmInternalSensorEntry = _CpqWcrmInternalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1)
)
cpqWcrmInternalSensorEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "internalSensorIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmInternalSensorEntry.setStatus("mandatory")


class _InternalSensorIndex_Type(Integer32):
    """Custom type internalSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InternalSensorIndex_Type.__name__ = "Integer32"
_InternalSensorIndex_Object = MibTableColumn
internalSensorIndex = _InternalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 1),
    _InternalSensorIndex_Type()
)
internalSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSensorIndex.setStatus("mandatory")


class _InternalSensorType_Type(Integer32):
    """Custom type internalSensorType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("access", 4),
          ("airFlow", 8),
          ("current4to20", 11),
          ("failure", 2),
          ("fanOK", 19),
          ("humidity", 12),
          ("leakage", 20),
          ("motion", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("smoke", 7),
          ("temperature", 10),
          ("type6", 9),
          ("userNC", 14),
          ("userNO", 13),
          ("vibration", 5),
          ("voltOK", 17),
          ("voltage", 18))
    )


_InternalSensorType_Type.__name__ = "Integer32"
_InternalSensorType_Object = MibTableColumn
internalSensorType = _InternalSensorType_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 2),
    _InternalSensorType_Type()
)
internalSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSensorType.setStatus("mandatory")


class _InternalSensorText_Type(DisplayString):
    """Custom type internalSensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InternalSensorText_Type.__name__ = "DisplayString"
_InternalSensorText_Object = MibTableColumn
internalSensorText = _InternalSensorText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 3),
    _InternalSensorText_Type()
)
internalSensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalSensorText.setStatus("mandatory")


class _InternalSensorStatus_Type(Integer32):
    """Custom type internalSensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_InternalSensorStatus_Type.__name__ = "Integer32"
_InternalSensorStatus_Object = MibTableColumn
internalSensorStatus = _InternalSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 4),
    _InternalSensorStatus_Type()
)
internalSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSensorStatus.setStatus("mandatory")
_InternalSensorValue_Type = Integer32
_InternalSensorValue_Object = MibTableColumn
internalSensorValue = _InternalSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 5),
    _InternalSensorValue_Type()
)
internalSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalSensorValue.setStatus("mandatory")
_InternalSensorSetHigh_Type = Integer32
_InternalSensorSetHigh_Object = MibTableColumn
internalSensorSetHigh = _InternalSensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 6),
    _InternalSensorSetHigh_Type()
)
internalSensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalSensorSetHigh.setStatus("mandatory")
_InternalSensorSetLow_Type = Integer32
_InternalSensorSetLow_Object = MibTableColumn
internalSensorSetLow = _InternalSensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 7),
    _InternalSensorSetLow_Type()
)
internalSensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalSensorSetLow.setStatus("mandatory")
_InternalSensorSetWarn_Type = Integer32
_InternalSensorSetWarn_Object = MibTableColumn
internalSensorSetWarn = _InternalSensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 5, 2, 1, 8),
    _InternalSensorSetWarn_Type()
)
internalSensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalSensorSetWarn.setStatus("mandatory")
_CpqWcrmStatusInternalOutputs_ObjectIdentity = ObjectIdentity
cpqWcrmStatusInternalOutputs = _CpqWcrmStatusInternalOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6)
)
_CpqWcrmInternalNumberOfOutputs_Type = Integer32
_CpqWcrmInternalNumberOfOutputs_Object = MibScalar
cpqWcrmInternalNumberOfOutputs = _CpqWcrmInternalNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 1),
    _CpqWcrmInternalNumberOfOutputs_Type()
)
cpqWcrmInternalNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalNumberOfOutputs.setStatus("mandatory")
_CpqWcrmInternalOutputTable_Object = MibTable
cpqWcrmInternalOutputTable = _CpqWcrmInternalOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmInternalOutputTable.setStatus("mandatory")
_CpqWcrmInternalOutputEntry_Object = MibTableRow
cpqWcrmInternalOutputEntry = _CpqWcrmInternalOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1)
)
cpqWcrmInternalOutputEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "internalOutputIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmInternalOutputEntry.setStatus("mandatory")


class _InternalOutputIndex_Type(Integer32):
    """Custom type internalOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InternalOutputIndex_Type.__name__ = "Integer32"
_InternalOutputIndex_Object = MibTableColumn
internalOutputIndex = _InternalOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 1),
    _InternalOutputIndex_Type()
)
internalOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalOutputIndex.setStatus("mandatory")


class _InternalOutputType_Type(Integer32):
    """Custom type internalOutputType based on Integer32"""
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
        *(("failure", 2),
          ("notAvail", 1),
          ("overflow", 3),
          ("powerOut", 5),
          ("universalOut", 4))
    )


_InternalOutputType_Type.__name__ = "Integer32"
_InternalOutputType_Object = MibTableColumn
internalOutputType = _InternalOutputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 2),
    _InternalOutputType_Type()
)
internalOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalOutputType.setStatus("mandatory")


class _InternalOutputText_Type(DisplayString):
    """Custom type internalOutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InternalOutputText_Type.__name__ = "DisplayString"
_InternalOutputText_Object = MibTableColumn
internalOutputText = _InternalOutputText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 3),
    _InternalOutputText_Type()
)
internalOutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputText.setStatus("mandatory")


class _InternalOutputStatus_Type(Integer32):
    """Custom type internalOutputStatus based on Integer32"""
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
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_InternalOutputStatus_Type.__name__ = "Integer32"
_InternalOutputStatus_Object = MibTableColumn
internalOutputStatus = _InternalOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 4),
    _InternalOutputStatus_Type()
)
internalOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputStatus.setStatus("mandatory")
_InternalOutputValue_Type = Integer32
_InternalOutputValue_Object = MibTableColumn
internalOutputValue = _InternalOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 5),
    _InternalOutputValue_Type()
)
internalOutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputValue.setStatus("mandatory")


class _InternalOutputSet_Type(Integer32):
    """Custom type internalOutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_InternalOutputSet_Type.__name__ = "Integer32"
_InternalOutputSet_Object = MibTableColumn
internalOutputSet = _InternalOutputSet_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 6),
    _InternalOutputSet_Type()
)
internalOutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputSet.setStatus("mandatory")


class _InternalOutputConfig_Type(Integer32):
    """Custom type internalOutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_InternalOutputConfig_Type.__name__ = "Integer32"
_InternalOutputConfig_Object = MibTableColumn
internalOutputConfig = _InternalOutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 7),
    _InternalOutputConfig_Type()
)
internalOutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputConfig.setStatus("mandatory")
_InternalOutputDelay_Type = Integer32
_InternalOutputDelay_Object = MibTableColumn
internalOutputDelay = _InternalOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 8),
    _InternalOutputDelay_Type()
)
internalOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputDelay.setStatus("mandatory")


class _InternalOutputTimeoutAction_Type(Integer32):
    """Custom type internalOutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_InternalOutputTimeoutAction_Type.__name__ = "Integer32"
_InternalOutputTimeoutAction_Object = MibTableColumn
internalOutputTimeoutAction = _InternalOutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 6, 2, 1, 9),
    _InternalOutputTimeoutAction_Type()
)
internalOutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalOutputTimeoutAction.setStatus("mandatory")
_CpqWcrmStatusInternalMsg_ObjectIdentity = ObjectIdentity
cpqWcrmStatusInternalMsg = _CpqWcrmStatusInternalMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7)
)
_CpqWcrmInternalNumberOfMsgs_Type = Integer32
_CpqWcrmInternalNumberOfMsgs_Object = MibScalar
cpqWcrmInternalNumberOfMsgs = _CpqWcrmInternalNumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 1),
    _CpqWcrmInternalNumberOfMsgs_Type()
)
cpqWcrmInternalNumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmInternalNumberOfMsgs.setStatus("mandatory")
_CpqWcrmInternalMsgTable_Object = MibTable
cpqWcrmInternalMsgTable = _CpqWcrmInternalMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmInternalMsgTable.setStatus("mandatory")
_CpqWcrmInternalMsgEntry_Object = MibTableRow
cpqWcrmInternalMsgEntry = _CpqWcrmInternalMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1)
)
cpqWcrmInternalMsgEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "internalMsgIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmInternalMsgEntry.setStatus("mandatory")


class _InternalMsgIndex_Type(Integer32):
    """Custom type internalMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_InternalMsgIndex_Type.__name__ = "Integer32"
_InternalMsgIndex_Object = MibTableColumn
internalMsgIndex = _InternalMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 1),
    _InternalMsgIndex_Type()
)
internalMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMsgIndex.setStatus("mandatory")


class _InternalMsgText_Type(DisplayString):
    """Custom type internalMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InternalMsgText_Type.__name__ = "DisplayString"
_InternalMsgText_Object = MibTableColumn
internalMsgText = _InternalMsgText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 2),
    _InternalMsgText_Type()
)
internalMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgText.setStatus("mandatory")


class _InternalMsgStatus_Type(Integer32):
    """Custom type internalMsgStatus based on Integer32"""
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
        *(("alarm", 5),
          ("configChanged", 2),
          ("error", 3),
          ("notAvail", 1),
          ("ok", 4),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("warning", 6))
    )


_InternalMsgStatus_Type.__name__ = "Integer32"
_InternalMsgStatus_Object = MibTableColumn
internalMsgStatus = _InternalMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 3),
    _InternalMsgStatus_Type()
)
internalMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalMsgStatus.setStatus("mandatory")


class _InternalMsgRelay_Type(Integer32):
    """Custom type internalMsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgRelay_Type.__name__ = "Integer32"
_InternalMsgRelay_Object = MibTableColumn
internalMsgRelay = _InternalMsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 4),
    _InternalMsgRelay_Type()
)
internalMsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgRelay.setStatus("mandatory")


class _InternalMsgBeeper_Type(Integer32):
    """Custom type internalMsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgBeeper_Type.__name__ = "Integer32"
_InternalMsgBeeper_Object = MibTableColumn
internalMsgBeeper = _InternalMsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 5),
    _InternalMsgBeeper_Type()
)
internalMsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgBeeper.setStatus("mandatory")


class _InternalMsgTrap1_Type(Integer32):
    """Custom type internalMsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgTrap1_Type.__name__ = "Integer32"
_InternalMsgTrap1_Object = MibTableColumn
internalMsgTrap1 = _InternalMsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 6),
    _InternalMsgTrap1_Type()
)
internalMsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgTrap1.setStatus("mandatory")


class _InternalMsgTrap2_Type(Integer32):
    """Custom type internalMsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgTrap2_Type.__name__ = "Integer32"
_InternalMsgTrap2_Object = MibTableColumn
internalMsgTrap2 = _InternalMsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 7),
    _InternalMsgTrap2_Type()
)
internalMsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgTrap2.setStatus("mandatory")


class _InternalMsgTrap3_Type(Integer32):
    """Custom type internalMsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgTrap3_Type.__name__ = "Integer32"
_InternalMsgTrap3_Object = MibTableColumn
internalMsgTrap3 = _InternalMsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 8),
    _InternalMsgTrap3_Type()
)
internalMsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgTrap3.setStatus("mandatory")


class _InternalMsgTrap4_Type(Integer32):
    """Custom type internalMsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_InternalMsgTrap4_Type.__name__ = "Integer32"
_InternalMsgTrap4_Object = MibTableColumn
internalMsgTrap4 = _InternalMsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 9),
    _InternalMsgTrap4_Type()
)
internalMsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgTrap4.setStatus("mandatory")


class _InternalMsgReset_Type(Integer32):
    """Custom type internalMsgReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_InternalMsgReset_Type.__name__ = "Integer32"
_InternalMsgReset_Object = MibTableColumn
internalMsgReset = _InternalMsgReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 3, 7, 2, 1, 10),
    _InternalMsgReset_Type()
)
internalMsgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internalMsgReset.setStatus("mandatory")
_CpqWcrmStatusSensorWaterCoolUnit_ObjectIdentity = ObjectIdentity
cpqWcrmStatusSensorWaterCoolUnit = _CpqWcrmStatusSensorWaterCoolUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4)
)


class _CpqWcrmWaterCoolUnitTypeOfDevice_Type(Integer32):
    """Custom type cpqWcrmWaterCoolUnitTypeOfDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvail", 1),
          ("unitIO", 3),
          ("unitWcrm", 2))
    )


_CpqWcrmWaterCoolUnitTypeOfDevice_Type.__name__ = "Integer32"
_CpqWcrmWaterCoolUnitTypeOfDevice_Object = MibScalar
cpqWcrmWaterCoolUnitTypeOfDevice = _CpqWcrmWaterCoolUnitTypeOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 1),
    _CpqWcrmWaterCoolUnitTypeOfDevice_Type()
)
cpqWcrmWaterCoolUnitTypeOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitTypeOfDevice.setStatus("mandatory")


class _CpqWcrmWaterCoolUnitText_Type(DisplayString):
    """Custom type cpqWcrmWaterCoolUnitText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqWcrmWaterCoolUnitText_Type.__name__ = "DisplayString"
_CpqWcrmWaterCoolUnitText_Object = MibScalar
cpqWcrmWaterCoolUnitText = _CpqWcrmWaterCoolUnitText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 2),
    _CpqWcrmWaterCoolUnitText_Type()
)
cpqWcrmWaterCoolUnitText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitText.setStatus("mandatory")
_CpqWcrmWaterCoolUnitSerial_Type = Integer32
_CpqWcrmWaterCoolUnitSerial_Object = MibScalar
cpqWcrmWaterCoolUnitSerial = _CpqWcrmWaterCoolUnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 3),
    _CpqWcrmWaterCoolUnitSerial_Type()
)
cpqWcrmWaterCoolUnitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitSerial.setStatus("mandatory")


class _CpqWcrmWaterCoolUnitStatus_Type(Integer32):
    """Custom type cpqWcrmWaterCoolUnitStatus based on Integer32"""
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
        *(("changed", 3),
          ("detected", 6),
          ("error", 2),
          ("lowPower", 8),
          ("notAvail", 7),
          ("ok", 1),
          ("reset", 4),
          ("timeout", 5))
    )


_CpqWcrmWaterCoolUnitStatus_Type.__name__ = "Integer32"
_CpqWcrmWaterCoolUnitStatus_Object = MibScalar
cpqWcrmWaterCoolUnitStatus = _CpqWcrmWaterCoolUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 4),
    _CpqWcrmWaterCoolUnitStatus_Type()
)
cpqWcrmWaterCoolUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitStatus.setStatus("mandatory")
_CpqWcrmStatusWaterCoolUnitSensors_ObjectIdentity = ObjectIdentity
cpqWcrmStatusWaterCoolUnitSensors = _CpqWcrmStatusWaterCoolUnitSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5)
)
_CpqWcrmWaterCoolUnitNumberOfSensors_Type = Integer32
_CpqWcrmWaterCoolUnitNumberOfSensors_Object = MibScalar
cpqWcrmWaterCoolUnitNumberOfSensors = _CpqWcrmWaterCoolUnitNumberOfSensors_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 1),
    _CpqWcrmWaterCoolUnitNumberOfSensors_Type()
)
cpqWcrmWaterCoolUnitNumberOfSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitNumberOfSensors.setStatus("mandatory")
_CpqWcrmWaterCoolUnitSensorTable_Object = MibTable
cpqWcrmWaterCoolUnitSensorTable = _CpqWcrmWaterCoolUnitSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitSensorTable.setStatus("mandatory")
_CpqWcrmWaterCoolUnitSensorEntry_Object = MibTableRow
cpqWcrmWaterCoolUnitSensorEntry = _CpqWcrmWaterCoolUnitSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1)
)
cpqWcrmWaterCoolUnitSensorEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "waterCoolUnitSensorIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitSensorEntry.setStatus("mandatory")


class _WaterCoolUnitSensorIndex_Type(Integer32):
    """Custom type waterCoolUnitSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WaterCoolUnitSensorIndex_Type.__name__ = "Integer32"
_WaterCoolUnitSensorIndex_Object = MibTableColumn
waterCoolUnitSensorIndex = _WaterCoolUnitSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 1),
    _WaterCoolUnitSensorIndex_Type()
)
waterCoolUnitSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitSensorIndex.setStatus("mandatory")


class _WaterCoolUnitSensorType_Type(Integer32):
    """Custom type waterCoolUnitSensorType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 7),
          ("condensateCycles", 25),
          ("condensateDuration", 24),
          ("failure", 2),
          ("fanSpeed", 12),
          ("heatFlow", 6),
          ("notAvail", 1),
          ("overflow", 3),
          ("rpmFan1", 9),
          ("rpmFan2", 10),
          ("rpmFan3", 11),
          ("rpmFan4", 26),
          ("rpmFan5", 27),
          ("rpmFan6", 28),
          ("status", 23),
          ("tempIn", 4),
          ("tempIn1", 13),
          ("tempIn2", 15),
          ("tempIn3", 17),
          ("tempOut", 5),
          ("tempOut1", 14),
          ("tempOut2", 16),
          ("tempOut3", 18),
          ("tempWaterIn", 19),
          ("tempWaterOut", 20),
          ("transfSwitch", 29),
          ("valve", 22),
          ("valveActValue", 30),
          ("warning", 8),
          ("waterFlow", 21))
    )


_WaterCoolUnitSensorType_Type.__name__ = "Integer32"
_WaterCoolUnitSensorType_Object = MibTableColumn
waterCoolUnitSensorType = _WaterCoolUnitSensorType_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 2),
    _WaterCoolUnitSensorType_Type()
)
waterCoolUnitSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitSensorType.setStatus("mandatory")


class _WaterCoolUnitSensorText_Type(DisplayString):
    """Custom type waterCoolUnitSensorText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WaterCoolUnitSensorText_Type.__name__ = "DisplayString"
_WaterCoolUnitSensorText_Object = MibTableColumn
waterCoolUnitSensorText = _WaterCoolUnitSensorText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 3),
    _WaterCoolUnitSensorText_Type()
)
waterCoolUnitSensorText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitSensorText.setStatus("mandatory")


class _WaterCoolUnitSensorStatus_Type(Integer32):
    """Custom type waterCoolUnitSensorStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("tooHigh", 9),
          ("tooLow", 8),
          ("warning", 7))
    )


_WaterCoolUnitSensorStatus_Type.__name__ = "Integer32"
_WaterCoolUnitSensorStatus_Object = MibTableColumn
waterCoolUnitSensorStatus = _WaterCoolUnitSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 4),
    _WaterCoolUnitSensorStatus_Type()
)
waterCoolUnitSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitSensorStatus.setStatus("mandatory")
_WaterCoolUnitSensorValue_Type = Integer32
_WaterCoolUnitSensorValue_Object = MibTableColumn
waterCoolUnitSensorValue = _WaterCoolUnitSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 5),
    _WaterCoolUnitSensorValue_Type()
)
waterCoolUnitSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitSensorValue.setStatus("mandatory")
_WaterCoolUnitSensorSetHigh_Type = Integer32
_WaterCoolUnitSensorSetHigh_Object = MibTableColumn
waterCoolUnitSensorSetHigh = _WaterCoolUnitSensorSetHigh_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 6),
    _WaterCoolUnitSensorSetHigh_Type()
)
waterCoolUnitSensorSetHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitSensorSetHigh.setStatus("mandatory")
_WaterCoolUnitSensorSetLow_Type = Integer32
_WaterCoolUnitSensorSetLow_Object = MibTableColumn
waterCoolUnitSensorSetLow = _WaterCoolUnitSensorSetLow_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 7),
    _WaterCoolUnitSensorSetLow_Type()
)
waterCoolUnitSensorSetLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitSensorSetLow.setStatus("mandatory")
_WaterCoolUnitSensorSetWarn_Type = Integer32
_WaterCoolUnitSensorSetWarn_Object = MibTableColumn
waterCoolUnitSensorSetWarn = _WaterCoolUnitSensorSetWarn_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 5, 2, 1, 8),
    _WaterCoolUnitSensorSetWarn_Type()
)
waterCoolUnitSensorSetWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitSensorSetWarn.setStatus("mandatory")
_CpqWcrmStatusWaterCoolUnitOutputs_ObjectIdentity = ObjectIdentity
cpqWcrmStatusWaterCoolUnitOutputs = _CpqWcrmStatusWaterCoolUnitOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6)
)
_CpqWcrmWaterCoolUnitNumberOfOutputs_Type = Integer32
_CpqWcrmWaterCoolUnitNumberOfOutputs_Object = MibScalar
cpqWcrmWaterCoolUnitNumberOfOutputs = _CpqWcrmWaterCoolUnitNumberOfOutputs_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 1),
    _CpqWcrmWaterCoolUnitNumberOfOutputs_Type()
)
cpqWcrmWaterCoolUnitNumberOfOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitNumberOfOutputs.setStatus("mandatory")
_CpqWcrmWaterCoolUnitOutputTable_Object = MibTable
cpqWcrmWaterCoolUnitOutputTable = _CpqWcrmWaterCoolUnitOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitOutputTable.setStatus("mandatory")
_CpqWcrmWaterCoolUnitOutputEntry_Object = MibTableRow
cpqWcrmWaterCoolUnitOutputEntry = _CpqWcrmWaterCoolUnitOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1)
)
cpqWcrmWaterCoolUnitOutputEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "waterCoolUnitOutputIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitOutputEntry.setStatus("mandatory")


class _WaterCoolUnitOutputIndex_Type(Integer32):
    """Custom type waterCoolUnitOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WaterCoolUnitOutputIndex_Type.__name__ = "Integer32"
_WaterCoolUnitOutputIndex_Object = MibTableColumn
waterCoolUnitOutputIndex = _WaterCoolUnitOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 1),
    _WaterCoolUnitOutputIndex_Type()
)
waterCoolUnitOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitOutputIndex.setStatus("mandatory")


class _WaterCoolUnitOutputType_Type(Integer32):
    """Custom type waterCoolUnitOutputType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("command", 6),
          ("controlMode", 7),
          ("cpWatert", 11),
          ("dTmax", 10),
          ("dTmin", 9),
          ("doorControl", 17),
          ("failure", 2),
          ("fanSpeedMin", 8),
          ("hysteresis", 5),
          ("notAvail", 1),
          ("overflow", 3),
          ("pidContrKD", 20),
          ("pidContrKI", 19),
          ("pidContrKP", 18),
          ("pidSampleTime", 21),
          ("setCondCycles", 15),
          ("setCondRun", 16),
          ("setEdoFlow", 13),
          ("setEdoHeat", 14),
          ("setHeatload", 12),
          ("setpoint", 4))
    )


_WaterCoolUnitOutputType_Type.__name__ = "Integer32"
_WaterCoolUnitOutputType_Object = MibTableColumn
waterCoolUnitOutputType = _WaterCoolUnitOutputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 2),
    _WaterCoolUnitOutputType_Type()
)
waterCoolUnitOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitOutputType.setStatus("mandatory")


class _WaterCoolUnitOutputText_Type(DisplayString):
    """Custom type waterCoolUnitOutputText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WaterCoolUnitOutputText_Type.__name__ = "DisplayString"
_WaterCoolUnitOutputText_Object = MibTableColumn
waterCoolUnitOutputText = _WaterCoolUnitOutputText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 3),
    _WaterCoolUnitOutputText_Type()
)
waterCoolUnitOutputText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputText.setStatus("mandatory")


class _WaterCoolUnitOutputStatus_Type(Integer32):
    """Custom type waterCoolUnitOutputStatus based on Integer32"""
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
        *(("changed", 3),
          ("lost", 2),
          ("notAvail", 1),
          ("off", 5),
          ("ok", 4),
          ("on", 6),
          ("setOff", 7),
          ("setOn", 8))
    )


_WaterCoolUnitOutputStatus_Type.__name__ = "Integer32"
_WaterCoolUnitOutputStatus_Object = MibTableColumn
waterCoolUnitOutputStatus = _WaterCoolUnitOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 4),
    _WaterCoolUnitOutputStatus_Type()
)
waterCoolUnitOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputStatus.setStatus("mandatory")
_WaterCoolUnitOutputValue_Type = Integer32
_WaterCoolUnitOutputValue_Object = MibTableColumn
waterCoolUnitOutputValue = _WaterCoolUnitOutputValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 5),
    _WaterCoolUnitOutputValue_Type()
)
waterCoolUnitOutputValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputValue.setStatus("mandatory")


class _WaterCoolUnitOutputSet_Type(Integer32):
    """Custom type waterCoolUnitOutputSet based on Integer32"""
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
        *(("lock", 3),
          ("off", 1),
          ("on", 2),
          ("unlock", 4),
          ("unlockDelay", 5))
    )


_WaterCoolUnitOutputSet_Type.__name__ = "Integer32"
_WaterCoolUnitOutputSet_Object = MibTableColumn
waterCoolUnitOutputSet = _WaterCoolUnitOutputSet_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 6),
    _WaterCoolUnitOutputSet_Type()
)
waterCoolUnitOutputSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputSet.setStatus("mandatory")


class _WaterCoolUnitOutputConfig_Type(Integer32):
    """Custom type waterCoolUnitOutputConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disRemote", 1),
          ("enRemote", 2))
    )


_WaterCoolUnitOutputConfig_Type.__name__ = "Integer32"
_WaterCoolUnitOutputConfig_Object = MibTableColumn
waterCoolUnitOutputConfig = _WaterCoolUnitOutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 7),
    _WaterCoolUnitOutputConfig_Type()
)
waterCoolUnitOutputConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputConfig.setStatus("mandatory")
_WaterCoolUnitOutputDelay_Type = Integer32
_WaterCoolUnitOutputDelay_Object = MibTableColumn
waterCoolUnitOutputDelay = _WaterCoolUnitOutputDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 8),
    _WaterCoolUnitOutputDelay_Type()
)
waterCoolUnitOutputDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputDelay.setStatus("mandatory")


class _WaterCoolUnitOutputTimeoutAction_Type(Integer32):
    """Custom type waterCoolUnitOutputTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("stay", 1))
    )


_WaterCoolUnitOutputTimeoutAction_Type.__name__ = "Integer32"
_WaterCoolUnitOutputTimeoutAction_Object = MibTableColumn
waterCoolUnitOutputTimeoutAction = _WaterCoolUnitOutputTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 6, 2, 1, 9),
    _WaterCoolUnitOutputTimeoutAction_Type()
)
waterCoolUnitOutputTimeoutAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitOutputTimeoutAction.setStatus("mandatory")
_CpqWcrmStatusWaterCoolUnitMsg_ObjectIdentity = ObjectIdentity
cpqWcrmStatusWaterCoolUnitMsg = _CpqWcrmStatusWaterCoolUnitMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7)
)
_CpqWcrmWaterCoolUnitNumberOfMsgs_Type = Integer32
_CpqWcrmWaterCoolUnitNumberOfMsgs_Object = MibScalar
cpqWcrmWaterCoolUnitNumberOfMsgs = _CpqWcrmWaterCoolUnitNumberOfMsgs_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 1),
    _CpqWcrmWaterCoolUnitNumberOfMsgs_Type()
)
cpqWcrmWaterCoolUnitNumberOfMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitNumberOfMsgs.setStatus("mandatory")
_CpqWcrmWaterCoolUnitMsgTable_Object = MibTable
cpqWcrmWaterCoolUnitMsgTable = _CpqWcrmWaterCoolUnitMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitMsgTable.setStatus("mandatory")
_CpqWcrmWaterCoolUnitMsgEntry_Object = MibTableRow
cpqWcrmWaterCoolUnitMsgEntry = _CpqWcrmWaterCoolUnitMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1)
)
cpqWcrmWaterCoolUnitMsgEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "waterCoolUnitMsgIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmWaterCoolUnitMsgEntry.setStatus("mandatory")


class _WaterCoolUnitMsgIndex_Type(Integer32):
    """Custom type waterCoolUnitMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WaterCoolUnitMsgIndex_Type.__name__ = "Integer32"
_WaterCoolUnitMsgIndex_Object = MibTableColumn
waterCoolUnitMsgIndex = _WaterCoolUnitMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 1),
    _WaterCoolUnitMsgIndex_Type()
)
waterCoolUnitMsgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitMsgIndex.setStatus("mandatory")


class _WaterCoolUnitMsgText_Type(DisplayString):
    """Custom type waterCoolUnitMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WaterCoolUnitMsgText_Type.__name__ = "DisplayString"
_WaterCoolUnitMsgText_Object = MibTableColumn
waterCoolUnitMsgText = _WaterCoolUnitMsgText_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 2),
    _WaterCoolUnitMsgText_Type()
)
waterCoolUnitMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgText.setStatus("mandatory")


class _WaterCoolUnitMsgStatus_Type(Integer32):
    """Custom type waterCoolUnitMsgStatus based on Integer32"""
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
        *(("alarm", 5),
          ("configChanged", 2),
          ("error", 3),
          ("notAvail", 1),
          ("ok", 4),
          ("setOff", 9),
          ("setOn", 10),
          ("tooHigh", 8),
          ("tooLow", 7),
          ("warning", 6))
    )


_WaterCoolUnitMsgStatus_Type.__name__ = "Integer32"
_WaterCoolUnitMsgStatus_Object = MibTableColumn
waterCoolUnitMsgStatus = _WaterCoolUnitMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 3),
    _WaterCoolUnitMsgStatus_Type()
)
waterCoolUnitMsgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterCoolUnitMsgStatus.setStatus("mandatory")


class _WaterCoolUnitMsgRelay_Type(Integer32):
    """Custom type waterCoolUnitMsgRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgRelay_Type.__name__ = "Integer32"
_WaterCoolUnitMsgRelay_Object = MibTableColumn
waterCoolUnitMsgRelay = _WaterCoolUnitMsgRelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 4),
    _WaterCoolUnitMsgRelay_Type()
)
waterCoolUnitMsgRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgRelay.setStatus("mandatory")


class _WaterCoolUnitMsgBeeper_Type(Integer32):
    """Custom type waterCoolUnitMsgBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgBeeper_Type.__name__ = "Integer32"
_WaterCoolUnitMsgBeeper_Object = MibTableColumn
waterCoolUnitMsgBeeper = _WaterCoolUnitMsgBeeper_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 5),
    _WaterCoolUnitMsgBeeper_Type()
)
waterCoolUnitMsgBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgBeeper.setStatus("mandatory")


class _WaterCoolUnitMsgTrap1_Type(Integer32):
    """Custom type waterCoolUnitMsgTrap1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgTrap1_Type.__name__ = "Integer32"
_WaterCoolUnitMsgTrap1_Object = MibTableColumn
waterCoolUnitMsgTrap1 = _WaterCoolUnitMsgTrap1_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 6),
    _WaterCoolUnitMsgTrap1_Type()
)
waterCoolUnitMsgTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgTrap1.setStatus("mandatory")


class _WaterCoolUnitMsgTrap2_Type(Integer32):
    """Custom type waterCoolUnitMsgTrap2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgTrap2_Type.__name__ = "Integer32"
_WaterCoolUnitMsgTrap2_Object = MibTableColumn
waterCoolUnitMsgTrap2 = _WaterCoolUnitMsgTrap2_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 7),
    _WaterCoolUnitMsgTrap2_Type()
)
waterCoolUnitMsgTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgTrap2.setStatus("mandatory")


class _WaterCoolUnitMsgTrap3_Type(Integer32):
    """Custom type waterCoolUnitMsgTrap3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgTrap3_Type.__name__ = "Integer32"
_WaterCoolUnitMsgTrap3_Object = MibTableColumn
waterCoolUnitMsgTrap3 = _WaterCoolUnitMsgTrap3_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 8),
    _WaterCoolUnitMsgTrap3_Type()
)
waterCoolUnitMsgTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgTrap3.setStatus("mandatory")


class _WaterCoolUnitMsgTrap4_Type(Integer32):
    """Custom type waterCoolUnitMsgTrap4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_WaterCoolUnitMsgTrap4_Type.__name__ = "Integer32"
_WaterCoolUnitMsgTrap4_Object = MibTableColumn
waterCoolUnitMsgTrap4 = _WaterCoolUnitMsgTrap4_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 9),
    _WaterCoolUnitMsgTrap4_Type()
)
waterCoolUnitMsgTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgTrap4.setStatus("mandatory")


class _WaterCoolUnitMsgReset_Type(Integer32):
    """Custom type waterCoolUnitMsgReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_WaterCoolUnitMsgReset_Type.__name__ = "Integer32"
_WaterCoolUnitMsgReset_Object = MibTableColumn
waterCoolUnitMsgReset = _WaterCoolUnitMsgReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 4, 7, 2, 1, 10),
    _WaterCoolUnitMsgReset_Type()
)
waterCoolUnitMsgReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterCoolUnitMsgReset.setStatus("mandatory")


class _CpqWcrmURL_Type(DisplayString):
    """Custom type cpqWcrmURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CpqWcrmURL_Type.__name__ = "DisplayString"
_CpqWcrmURL_Object = MibScalar
cpqWcrmURL = _CpqWcrmURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 2, 7),
    _CpqWcrmURL_Type()
)
cpqWcrmURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmURL.setStatus("mandatory")
_CpqWcrmSetup_ObjectIdentity = ObjectIdentity
cpqWcrmSetup = _CpqWcrmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 3)
)
_CpqWcrmSetupGeneral_ObjectIdentity = ObjectIdentity
cpqWcrmSetupGeneral = _CpqWcrmSetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1)
)


class _CpqWcrmSetTempUnit_Type(Integer32):
    """Custom type cpqWcrmSetTempUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_CpqWcrmSetTempUnit_Type.__name__ = "Integer32"
_CpqWcrmSetTempUnit_Object = MibScalar
cpqWcrmSetTempUnit = _CpqWcrmSetTempUnit_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 1),
    _CpqWcrmSetTempUnit_Type()
)
cpqWcrmSetTempUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmSetTempUnit.setStatus("mandatory")


class _CpqWcrmSetBeeper_Type(Integer32):
    """Custom type cpqWcrmSetBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CpqWcrmSetBeeper_Type.__name__ = "Integer32"
_CpqWcrmSetBeeper_Object = MibScalar
cpqWcrmSetBeeper = _CpqWcrmSetBeeper_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 2),
    _CpqWcrmSetBeeper_Type()
)
cpqWcrmSetBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmSetBeeper.setStatus("mandatory")


class _CpqWcrmResetRelay_Type(Integer32):
    """Custom type cpqWcrmResetRelay based on Integer32"""
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


_CpqWcrmResetRelay_Type.__name__ = "Integer32"
_CpqWcrmResetRelay_Object = MibScalar
cpqWcrmResetRelay = _CpqWcrmResetRelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 3),
    _CpqWcrmResetRelay_Type()
)
cpqWcrmResetRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmResetRelay.setStatus("mandatory")


class _CpqWcrmLogicRelay_Type(Integer32):
    """Custom type cpqWcrmLogicRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closeAtAlarm", 1),
          ("off", 3),
          ("openAtAlarm", 2))
    )


_CpqWcrmLogicRelay_Type.__name__ = "Integer32"
_CpqWcrmLogicRelay_Object = MibScalar
cpqWcrmLogicRelay = _CpqWcrmLogicRelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 4),
    _CpqWcrmLogicRelay_Type()
)
cpqWcrmLogicRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmLogicRelay.setStatus("mandatory")


class _CpqWcrmWebAccess_Type(Integer32):
    """Custom type cpqWcrmWebAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullAccess", 2),
          ("off", 3),
          ("viewOnly", 1))
    )


_CpqWcrmWebAccess_Type.__name__ = "Integer32"
_CpqWcrmWebAccess_Object = MibScalar
cpqWcrmWebAccess = _CpqWcrmWebAccess_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 5),
    _CpqWcrmWebAccess_Type()
)
cpqWcrmWebAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmWebAccess.setStatus("mandatory")


class _CpqWcrmSetupDate_Type(DisplayString):
    """Custom type cpqWcrmSetupDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CpqWcrmSetupDate_Type.__name__ = "DisplayString"
_CpqWcrmSetupDate_Object = MibScalar
cpqWcrmSetupDate = _CpqWcrmSetupDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 6),
    _CpqWcrmSetupDate_Type()
)
cpqWcrmSetupDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmSetupDate.setStatus("mandatory")


class _CpqWcrmSetupTime_Type(DisplayString):
    """Custom type cpqWcrmSetupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CpqWcrmSetupTime_Type.__name__ = "DisplayString"
_CpqWcrmSetupTime_Object = MibScalar
cpqWcrmSetupTime = _CpqWcrmSetupTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 7),
    _CpqWcrmSetupTime_Type()
)
cpqWcrmSetupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmSetupTime.setStatus("mandatory")
_CpqWcrmTimerTable1_ObjectIdentity = ObjectIdentity
cpqWcrmTimerTable1 = _CpqWcrmTimerTable1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8)
)
_CpqWcrmTimerNumber_Type = Integer32
_CpqWcrmTimerNumber_Object = MibScalar
cpqWcrmTimerNumber = _CpqWcrmTimerNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 1),
    _CpqWcrmTimerNumber_Type()
)
cpqWcrmTimerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmTimerNumber.setStatus("mandatory")
_CpqWcrmTimerTable_Object = MibTable
cpqWcrmTimerTable = _CpqWcrmTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmTimerTable.setStatus("mandatory")
_CpqWcrmTimerEntry_Object = MibTableRow
cpqWcrmTimerEntry = _CpqWcrmTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1)
)
cpqWcrmTimerEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "cpqWcrmTimerIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmTimerEntry.setStatus("mandatory")


class _CpqWcrmTimerIndex_Type(Integer32):
    """Custom type cpqWcrmTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqWcrmTimerIndex_Type.__name__ = "Integer32"
_CpqWcrmTimerIndex_Object = MibTableColumn
cpqWcrmTimerIndex = _CpqWcrmTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 1),
    _CpqWcrmTimerIndex_Type()
)
cpqWcrmTimerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmTimerIndex.setStatus("mandatory")


class _CpqWcrmTimerStatus_Type(Integer32):
    """Custom type cpqWcrmTimerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noTime", 3),
          ("switchedOff", 1),
          ("switchedOn", 2))
    )


_CpqWcrmTimerStatus_Type.__name__ = "Integer32"
_CpqWcrmTimerStatus_Object = MibTableColumn
cpqWcrmTimerStatus = _CpqWcrmTimerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 2),
    _CpqWcrmTimerStatus_Type()
)
cpqWcrmTimerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmTimerStatus.setStatus("mandatory")


class _CpqWcrmTimerDayOfWeek_Type(Integer32):
    """Custom type cpqWcrmTimerDayOfWeek based on Integer32"""
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
        *(("fri", 6),
          ("mon", 2),
          ("mon-fri", 9),
          ("mon-sun", 10),
          ("sat", 7),
          ("sat-sun", 8),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_CpqWcrmTimerDayOfWeek_Type.__name__ = "Integer32"
_CpqWcrmTimerDayOfWeek_Object = MibTableColumn
cpqWcrmTimerDayOfWeek = _CpqWcrmTimerDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 3),
    _CpqWcrmTimerDayOfWeek_Type()
)
cpqWcrmTimerDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmTimerDayOfWeek.setStatus("mandatory")


class _CpqWcrmTimeOn_Type(DisplayString):
    """Custom type cpqWcrmTimeOn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqWcrmTimeOn_Type.__name__ = "DisplayString"
_CpqWcrmTimeOn_Object = MibTableColumn
cpqWcrmTimeOn = _CpqWcrmTimeOn_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 4),
    _CpqWcrmTimeOn_Type()
)
cpqWcrmTimeOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmTimeOn.setStatus("mandatory")


class _CpqWcrmTimeOff_Type(DisplayString):
    """Custom type cpqWcrmTimeOff based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_CpqWcrmTimeOff_Type.__name__ = "DisplayString"
_CpqWcrmTimeOff_Object = MibTableColumn
cpqWcrmTimeOff = _CpqWcrmTimeOff_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 5),
    _CpqWcrmTimeOff_Type()
)
cpqWcrmTimeOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmTimeOff.setStatus("mandatory")


class _CpqWcrmTimeControl_Type(Integer32):
    """Custom type cpqWcrmTimeControl based on Integer32"""
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


_CpqWcrmTimeControl_Type.__name__ = "Integer32"
_CpqWcrmTimeControl_Object = MibTableColumn
cpqWcrmTimeControl = _CpqWcrmTimeControl_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 6),
    _CpqWcrmTimeControl_Type()
)
cpqWcrmTimeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmTimeControl.setStatus("mandatory")


class _CpqWcrmTimerFunction_Type(Integer32):
    """Custom type cpqWcrmTimerFunction based on Integer32"""
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
        *(("disTrapRec1", 1),
          ("disTrapRec2", 2),
          ("disTrapRec3", 3),
          ("disTrapRec4", 4),
          ("schedule1", 5),
          ("schedule2", 6),
          ("schedule3", 7),
          ("schedule4", 8))
    )


_CpqWcrmTimerFunction_Type.__name__ = "Integer32"
_CpqWcrmTimerFunction_Object = MibTableColumn
cpqWcrmTimerFunction = _CpqWcrmTimerFunction_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 8, 2, 1, 7),
    _CpqWcrmTimerFunction_Type()
)
cpqWcrmTimerFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmTimerFunction.setStatus("mandatory")


class _CpqWcrmSetFlowUnit_Type(Integer32):
    """Custom type cpqWcrmSetFlowUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gallonMin", 2),
          ("literMin", 1))
    )


_CpqWcrmSetFlowUnit_Type.__name__ = "Integer32"
_CpqWcrmSetFlowUnit_Object = MibScalar
cpqWcrmSetFlowUnit = _CpqWcrmSetFlowUnit_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 3, 1, 9),
    _CpqWcrmSetFlowUnit_Type()
)
cpqWcrmSetFlowUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmSetFlowUnit.setStatus("mandatory")
_CpqWcrmTrapControl_ObjectIdentity = ObjectIdentity
cpqWcrmTrapControl = _CpqWcrmTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 4)
)
_CpqWcrmTraps_ObjectIdentity = ObjectIdentity
cpqWcrmTraps = _CpqWcrmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7)
)
_CpqWcrmTraptableNumber_Type = Integer32
_CpqWcrmTraptableNumber_Object = MibScalar
cpqWcrmTraptableNumber = _CpqWcrmTraptableNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 1),
    _CpqWcrmTraptableNumber_Type()
)
cpqWcrmTraptableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqWcrmTraptableNumber.setStatus("mandatory")
_CpqWcrmTrapTableTable_Object = MibTable
cpqWcrmTrapTableTable = _CpqWcrmTrapTableTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 2)
)
if mibBuilder.loadTexts:
    cpqWcrmTrapTableTable.setStatus("mandatory")
_CpqWcrmTrapTableEntry_Object = MibTableRow
cpqWcrmTrapTableEntry = _CpqWcrmTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 2, 1)
)
cpqWcrmTrapTableEntry.setIndexNames(
    (0, "CPQWCRM-MIB", "trapIndex"),
)
if mibBuilder.loadTexts:
    cpqWcrmTrapTableEntry.setStatus("mandatory")


class _TrapIndex_Type(Integer32):
    """Custom type trapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapIndex_Type.__name__ = "Integer32"
_TrapIndex_Object = MibTableColumn
trapIndex = _TrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 2, 1, 1),
    _TrapIndex_Type()
)
trapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIndex.setStatus("mandatory")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
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


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 2, 1, 2),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")


class _TrapIPaddress_Type(DisplayString):
    """Custom type trapIPaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TrapIPaddress_Type.__name__ = "DisplayString"
_TrapIPaddress_Object = MibTableColumn
trapIPaddress = _TrapIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 4, 7, 2, 1, 3),
    _TrapIPaddress_Type()
)
trapIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIPaddress.setStatus("mandatory")
_CpqWcrmControl_ObjectIdentity = ObjectIdentity
cpqWcrmControl = _CpqWcrmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 167, 5)
)


class _CpqWcrmResetUnit_Type(Integer32):
    """Custom type cpqWcrmResetUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_CpqWcrmResetUnit_Type.__name__ = "Integer32"
_CpqWcrmResetUnit_Object = MibScalar
cpqWcrmResetUnit = _CpqWcrmResetUnit_Object(
    (1, 3, 6, 1, 4, 1, 232, 167, 5, 1),
    _CpqWcrmResetUnit_Type()
)
cpqWcrmResetUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqWcrmResetUnit.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmSensorInternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 167, 0, 1)
)
alarmSensorInternal.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQWCRM-MIB", "internalMsgIndex"),
        ("CPQWCRM-MIB", "internalMsgText"),
        ("CPQWCRM-MIB", "internalMsgStatus"),
        ("CPQWCRM-MIB", "internalSensorValue"),
        ("CPQWCRM-MIB", "cpqWcrmURL"))
)
if mibBuilder.loadTexts:
    alarmSensorInternal.setStatus(
        ""
    )

alarmSensorWaterCoolUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 167, 0, 2)
)
alarmSensorWaterCoolUnit.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQWCRM-MIB", "waterCoolUnitMsgIndex"),
        ("CPQWCRM-MIB", "waterCoolUnitMsgText"),
        ("CPQWCRM-MIB", "waterCoolUnitMsgStatus"),
        ("CPQWCRM-MIB", "waterCoolUnitSensorValue"),
        ("CPQWCRM-MIB", "cpqWcrmURL"))
)
if mibBuilder.loadTexts:
    alarmSensorWaterCoolUnit.setStatus(
        ""
    )

alarmInternal = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 167, 0, 5)
)
alarmInternal.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQWCRM-MIB", "cpqWcrmInternalText"),
        ("CPQWCRM-MIB", "cpqWcrmInternalStatus"),
        ("CPQWCRM-MIB", "cpqWcrmURL"))
)
if mibBuilder.loadTexts:
    alarmInternal.setStatus(
        ""
    )

alarmWaterCoolUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 167, 0, 6)
)
alarmWaterCoolUnit.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQWCRM-MIB", "cpqWcrmWaterCoolUnitText"),
        ("CPQWCRM-MIB", "cpqWcrmWaterCoolUnitStatus"),
        ("CPQWCRM-MIB", "cpqWcrmURL"))
)
if mibBuilder.loadTexts:
    alarmWaterCoolUnit.setStatus(
        ""
    )

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 167, 0, 10)
)
testTrap.setObjects(
      *(("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("CPQWCRM-MIB", "cpqWcrmURL"))
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQWCRM-MIB",
    **{"cpqWcrm": cpqWcrm,
       "alarmSensorInternal": alarmSensorInternal,
       "alarmSensorWaterCoolUnit": alarmSensorWaterCoolUnit,
       "alarmInternal": alarmInternal,
       "alarmWaterCoolUnit": alarmWaterCoolUnit,
       "testTrap": testTrap,
       "cpqWcrmMibRev": cpqWcrmMibRev,
       "cpqWcrmMibMajRev": cpqWcrmMibMajRev,
       "cpqWcrmMibMinRev": cpqWcrmMibMinRev,
       "cpqWcrmMibCondition": cpqWcrmMibCondition,
       "cpqWcrmStatus": cpqWcrmStatus,
       "cpqWcrmStatusDeviceEnvironmentalController": cpqWcrmStatusDeviceEnvironmentalController,
       "cpqWcrmUnitsConnected": cpqWcrmUnitsConnected,
       "cpqWcrmStatusSensorInternal": cpqWcrmStatusSensorInternal,
       "cpqWcrmInternalTypeOfDevice": cpqWcrmInternalTypeOfDevice,
       "cpqWcrmInternalText": cpqWcrmInternalText,
       "cpqWcrmInternalSerial": cpqWcrmInternalSerial,
       "cpqWcrmInternalStatus": cpqWcrmInternalStatus,
       "cpqWcrmStatusInternalSensors": cpqWcrmStatusInternalSensors,
       "cpqWcrmInternalNumberOfSensors": cpqWcrmInternalNumberOfSensors,
       "cpqWcrmInternalSensorTable": cpqWcrmInternalSensorTable,
       "cpqWcrmInternalSensorEntry": cpqWcrmInternalSensorEntry,
       "internalSensorIndex": internalSensorIndex,
       "internalSensorType": internalSensorType,
       "internalSensorText": internalSensorText,
       "internalSensorStatus": internalSensorStatus,
       "internalSensorValue": internalSensorValue,
       "internalSensorSetHigh": internalSensorSetHigh,
       "internalSensorSetLow": internalSensorSetLow,
       "internalSensorSetWarn": internalSensorSetWarn,
       "cpqWcrmStatusInternalOutputs": cpqWcrmStatusInternalOutputs,
       "cpqWcrmInternalNumberOfOutputs": cpqWcrmInternalNumberOfOutputs,
       "cpqWcrmInternalOutputTable": cpqWcrmInternalOutputTable,
       "cpqWcrmInternalOutputEntry": cpqWcrmInternalOutputEntry,
       "internalOutputIndex": internalOutputIndex,
       "internalOutputType": internalOutputType,
       "internalOutputText": internalOutputText,
       "internalOutputStatus": internalOutputStatus,
       "internalOutputValue": internalOutputValue,
       "internalOutputSet": internalOutputSet,
       "internalOutputConfig": internalOutputConfig,
       "internalOutputDelay": internalOutputDelay,
       "internalOutputTimeoutAction": internalOutputTimeoutAction,
       "cpqWcrmStatusInternalMsg": cpqWcrmStatusInternalMsg,
       "cpqWcrmInternalNumberOfMsgs": cpqWcrmInternalNumberOfMsgs,
       "cpqWcrmInternalMsgTable": cpqWcrmInternalMsgTable,
       "cpqWcrmInternalMsgEntry": cpqWcrmInternalMsgEntry,
       "internalMsgIndex": internalMsgIndex,
       "internalMsgText": internalMsgText,
       "internalMsgStatus": internalMsgStatus,
       "internalMsgRelay": internalMsgRelay,
       "internalMsgBeeper": internalMsgBeeper,
       "internalMsgTrap1": internalMsgTrap1,
       "internalMsgTrap2": internalMsgTrap2,
       "internalMsgTrap3": internalMsgTrap3,
       "internalMsgTrap4": internalMsgTrap4,
       "internalMsgReset": internalMsgReset,
       "cpqWcrmStatusSensorWaterCoolUnit": cpqWcrmStatusSensorWaterCoolUnit,
       "cpqWcrmWaterCoolUnitTypeOfDevice": cpqWcrmWaterCoolUnitTypeOfDevice,
       "cpqWcrmWaterCoolUnitText": cpqWcrmWaterCoolUnitText,
       "cpqWcrmWaterCoolUnitSerial": cpqWcrmWaterCoolUnitSerial,
       "cpqWcrmWaterCoolUnitStatus": cpqWcrmWaterCoolUnitStatus,
       "cpqWcrmStatusWaterCoolUnitSensors": cpqWcrmStatusWaterCoolUnitSensors,
       "cpqWcrmWaterCoolUnitNumberOfSensors": cpqWcrmWaterCoolUnitNumberOfSensors,
       "cpqWcrmWaterCoolUnitSensorTable": cpqWcrmWaterCoolUnitSensorTable,
       "cpqWcrmWaterCoolUnitSensorEntry": cpqWcrmWaterCoolUnitSensorEntry,
       "waterCoolUnitSensorIndex": waterCoolUnitSensorIndex,
       "waterCoolUnitSensorType": waterCoolUnitSensorType,
       "waterCoolUnitSensorText": waterCoolUnitSensorText,
       "waterCoolUnitSensorStatus": waterCoolUnitSensorStatus,
       "waterCoolUnitSensorValue": waterCoolUnitSensorValue,
       "waterCoolUnitSensorSetHigh": waterCoolUnitSensorSetHigh,
       "waterCoolUnitSensorSetLow": waterCoolUnitSensorSetLow,
       "waterCoolUnitSensorSetWarn": waterCoolUnitSensorSetWarn,
       "cpqWcrmStatusWaterCoolUnitOutputs": cpqWcrmStatusWaterCoolUnitOutputs,
       "cpqWcrmWaterCoolUnitNumberOfOutputs": cpqWcrmWaterCoolUnitNumberOfOutputs,
       "cpqWcrmWaterCoolUnitOutputTable": cpqWcrmWaterCoolUnitOutputTable,
       "cpqWcrmWaterCoolUnitOutputEntry": cpqWcrmWaterCoolUnitOutputEntry,
       "waterCoolUnitOutputIndex": waterCoolUnitOutputIndex,
       "waterCoolUnitOutputType": waterCoolUnitOutputType,
       "waterCoolUnitOutputText": waterCoolUnitOutputText,
       "waterCoolUnitOutputStatus": waterCoolUnitOutputStatus,
       "waterCoolUnitOutputValue": waterCoolUnitOutputValue,
       "waterCoolUnitOutputSet": waterCoolUnitOutputSet,
       "waterCoolUnitOutputConfig": waterCoolUnitOutputConfig,
       "waterCoolUnitOutputDelay": waterCoolUnitOutputDelay,
       "waterCoolUnitOutputTimeoutAction": waterCoolUnitOutputTimeoutAction,
       "cpqWcrmStatusWaterCoolUnitMsg": cpqWcrmStatusWaterCoolUnitMsg,
       "cpqWcrmWaterCoolUnitNumberOfMsgs": cpqWcrmWaterCoolUnitNumberOfMsgs,
       "cpqWcrmWaterCoolUnitMsgTable": cpqWcrmWaterCoolUnitMsgTable,
       "cpqWcrmWaterCoolUnitMsgEntry": cpqWcrmWaterCoolUnitMsgEntry,
       "waterCoolUnitMsgIndex": waterCoolUnitMsgIndex,
       "waterCoolUnitMsgText": waterCoolUnitMsgText,
       "waterCoolUnitMsgStatus": waterCoolUnitMsgStatus,
       "waterCoolUnitMsgRelay": waterCoolUnitMsgRelay,
       "waterCoolUnitMsgBeeper": waterCoolUnitMsgBeeper,
       "waterCoolUnitMsgTrap1": waterCoolUnitMsgTrap1,
       "waterCoolUnitMsgTrap2": waterCoolUnitMsgTrap2,
       "waterCoolUnitMsgTrap3": waterCoolUnitMsgTrap3,
       "waterCoolUnitMsgTrap4": waterCoolUnitMsgTrap4,
       "waterCoolUnitMsgReset": waterCoolUnitMsgReset,
       "cpqWcrmURL": cpqWcrmURL,
       "cpqWcrmSetup": cpqWcrmSetup,
       "cpqWcrmSetupGeneral": cpqWcrmSetupGeneral,
       "cpqWcrmSetTempUnit": cpqWcrmSetTempUnit,
       "cpqWcrmSetBeeper": cpqWcrmSetBeeper,
       "cpqWcrmResetRelay": cpqWcrmResetRelay,
       "cpqWcrmLogicRelay": cpqWcrmLogicRelay,
       "cpqWcrmWebAccess": cpqWcrmWebAccess,
       "cpqWcrmSetupDate": cpqWcrmSetupDate,
       "cpqWcrmSetupTime": cpqWcrmSetupTime,
       "cpqWcrmTimerTable1": cpqWcrmTimerTable1,
       "cpqWcrmTimerNumber": cpqWcrmTimerNumber,
       "cpqWcrmTimerTable": cpqWcrmTimerTable,
       "cpqWcrmTimerEntry": cpqWcrmTimerEntry,
       "cpqWcrmTimerIndex": cpqWcrmTimerIndex,
       "cpqWcrmTimerStatus": cpqWcrmTimerStatus,
       "cpqWcrmTimerDayOfWeek": cpqWcrmTimerDayOfWeek,
       "cpqWcrmTimeOn": cpqWcrmTimeOn,
       "cpqWcrmTimeOff": cpqWcrmTimeOff,
       "cpqWcrmTimeControl": cpqWcrmTimeControl,
       "cpqWcrmTimerFunction": cpqWcrmTimerFunction,
       "cpqWcrmSetFlowUnit": cpqWcrmSetFlowUnit,
       "cpqWcrmTrapControl": cpqWcrmTrapControl,
       "cpqWcrmTraps": cpqWcrmTraps,
       "cpqWcrmTraptableNumber": cpqWcrmTraptableNumber,
       "cpqWcrmTrapTableTable": cpqWcrmTrapTableTable,
       "cpqWcrmTrapTableEntry": cpqWcrmTrapTableEntry,
       "trapIndex": trapIndex,
       "trapStatus": trapStatus,
       "trapIPaddress": trapIPaddress,
       "cpqWcrmControl": cpqWcrmControl,
       "cpqWcrmResetUnit": cpqWcrmResetUnit}
)
