# SNMP MIB module (EXALINK-FUSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXALINK-FUSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:02 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

exaFusion = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3)
)
exaFusion.setRevisions(
        ("2015-10-20 00:00",
         "2015-07-30 00:00",
         "2015-04-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FusionInfo_ObjectIdentity = ObjectIdentity
fusionInfo = _FusionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1)
)
_FusionInfoSerial_Type = SnmpAdminString
_FusionInfoSerial_Object = MibScalar
fusionInfoSerial = _FusionInfoSerial_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 1),
    _FusionInfoSerial_Type()
)
fusionInfoSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionInfoSerial.setStatus("current")
_FusionInfoVersion_Type = SnmpAdminString
_FusionInfoVersion_Object = MibScalar
fusionInfoVersion = _FusionInfoVersion_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 2),
    _FusionInfoVersion_Type()
)
fusionInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionInfoVersion.setStatus("current")
_FusionInfoBoard_Type = SnmpAdminString
_FusionInfoBoard_Object = MibScalar
fusionInfoBoard = _FusionInfoBoard_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 3),
    _FusionInfoBoard_Type()
)
fusionInfoBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionInfoBoard.setStatus("current")
_FusionInfoSoftware_Type = SnmpAdminString
_FusionInfoSoftware_Object = MibScalar
fusionInfoSoftware = _FusionInfoSoftware_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 4),
    _FusionInfoSoftware_Type()
)
fusionInfoSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionInfoSoftware.setStatus("current")
_FusionLineCardTable_Object = MibTable
fusionLineCardTable = _FusionLineCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 5)
)
if mibBuilder.loadTexts:
    fusionLineCardTable.setStatus("current")
_FusionLineCard_Object = MibTableRow
fusionLineCard = _FusionLineCard_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 5, 1)
)
fusionLineCard.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionLineCardIndex"),
)
if mibBuilder.loadTexts:
    fusionLineCard.setStatus("current")


class _FusionLineCardIndex_Type(Integer32):
    """Custom type fusionLineCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionLineCardIndex_Type.__name__ = "Integer32"
_FusionLineCardIndex_Object = MibTableColumn
fusionLineCardIndex = _FusionLineCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 5, 1, 1),
    _FusionLineCardIndex_Type()
)
fusionLineCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionLineCardIndex.setStatus("current")
_FusionLineCardName_Type = SnmpAdminString
_FusionLineCardName_Object = MibTableColumn
fusionLineCardName = _FusionLineCardName_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 5, 1, 2),
    _FusionLineCardName_Type()
)
fusionLineCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionLineCardName.setStatus("current")
_FusionLineCardBoard_Type = SnmpAdminString
_FusionLineCardBoard_Object = MibTableColumn
fusionLineCardBoard = _FusionLineCardBoard_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 5, 1, 3),
    _FusionLineCardBoard_Type()
)
fusionLineCardBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionLineCardBoard.setStatus("current")
_FusionModuleTable_Object = MibTable
fusionModuleTable = _FusionModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6)
)
if mibBuilder.loadTexts:
    fusionModuleTable.setStatus("current")
_FusionModule_Object = MibTableRow
fusionModule = _FusionModule_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6, 1)
)
fusionModule.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionModuleIndex"),
)
if mibBuilder.loadTexts:
    fusionModule.setStatus("current")


class _FusionModuleIndex_Type(Integer32):
    """Custom type fusionModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionModuleIndex_Type.__name__ = "Integer32"
_FusionModuleIndex_Object = MibTableColumn
fusionModuleIndex = _FusionModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6, 1, 1),
    _FusionModuleIndex_Type()
)
fusionModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionModuleIndex.setStatus("current")
_FusionModuleName_Type = SnmpAdminString
_FusionModuleName_Object = MibTableColumn
fusionModuleName = _FusionModuleName_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6, 1, 2),
    _FusionModuleName_Type()
)
fusionModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionModuleName.setStatus("current")
_FusionModuleBoard_Type = SnmpAdminString
_FusionModuleBoard_Object = MibTableColumn
fusionModuleBoard = _FusionModuleBoard_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6, 1, 3),
    _FusionModuleBoard_Type()
)
fusionModuleBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionModuleBoard.setStatus("current")
_FusionModuleFunction_Type = SnmpAdminString
_FusionModuleFunction_Object = MibTableColumn
fusionModuleFunction = _FusionModuleFunction_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 6, 1, 4),
    _FusionModuleFunction_Type()
)
fusionModuleFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionModuleFunction.setStatus("current")
_FusionSysInfo_ObjectIdentity = ObjectIdentity
fusionSysInfo = _FusionSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 7)
)
_FusionSysInfoLoadAverage_Type = Integer32
_FusionSysInfoLoadAverage_Object = MibScalar
fusionSysInfoLoadAverage = _FusionSysInfoLoadAverage_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 7, 1),
    _FusionSysInfoLoadAverage_Type()
)
fusionSysInfoLoadAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionSysInfoLoadAverage.setStatus("current")
_FusionSysInfoAvailMem_Type = Integer32
_FusionSysInfoAvailMem_Object = MibScalar
fusionSysInfoAvailMem = _FusionSysInfoAvailMem_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 7, 2),
    _FusionSysInfoAvailMem_Type()
)
fusionSysInfoAvailMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionSysInfoAvailMem.setStatus("current")
_FusionSysInfoNumProcesses_Type = Integer32
_FusionSysInfoNumProcesses_Object = MibScalar
fusionSysInfoNumProcesses = _FusionSysInfoNumProcesses_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 1, 7, 3),
    _FusionSysInfoNumProcesses_Type()
)
fusionSysInfoNumProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionSysInfoNumProcesses.setStatus("current")
_FusionSensor_ObjectIdentity = ObjectIdentity
fusionSensor = _FusionSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2)
)
_FusionTempSensorTable_Object = MibTable
fusionTempSensorTable = _FusionTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 1)
)
if mibBuilder.loadTexts:
    fusionTempSensorTable.setStatus("current")
_FusionTempSensor_Object = MibTableRow
fusionTempSensor = _FusionTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 1, 1)
)
fusionTempSensor.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionTempSensorIndex"),
)
if mibBuilder.loadTexts:
    fusionTempSensor.setStatus("current")


class _FusionTempSensorIndex_Type(Integer32):
    """Custom type fusionTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionTempSensorIndex_Type.__name__ = "Integer32"
_FusionTempSensorIndex_Object = MibTableColumn
fusionTempSensorIndex = _FusionTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 1, 1, 1),
    _FusionTempSensorIndex_Type()
)
fusionTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionTempSensorIndex.setStatus("current")
_FusionTempSensorName_Type = SnmpAdminString
_FusionTempSensorName_Object = MibTableColumn
fusionTempSensorName = _FusionTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 1, 1, 2),
    _FusionTempSensorName_Type()
)
fusionTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionTempSensorName.setStatus("current")
_FusionTempSensorValue_Type = Integer32
_FusionTempSensorValue_Object = MibTableColumn
fusionTempSensorValue = _FusionTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 1, 1, 3),
    _FusionTempSensorValue_Type()
)
fusionTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionTempSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    fusionTempSensorValue.setUnits("Celsius")
_FusionFanSensorTable_Object = MibTable
fusionFanSensorTable = _FusionFanSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fusionFanSensorTable.setStatus("current")
_FusionFanSensor_Object = MibTableRow
fusionFanSensor = _FusionFanSensor_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 2, 1)
)
fusionFanSensor.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionFanSensorIndex"),
)
if mibBuilder.loadTexts:
    fusionFanSensor.setStatus("current")


class _FusionFanSensorIndex_Type(Integer32):
    """Custom type fusionFanSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionFanSensorIndex_Type.__name__ = "Integer32"
_FusionFanSensorIndex_Object = MibTableColumn
fusionFanSensorIndex = _FusionFanSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 2, 1, 1),
    _FusionFanSensorIndex_Type()
)
fusionFanSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionFanSensorIndex.setStatus("current")
_FusionFanSensorName_Type = SnmpAdminString
_FusionFanSensorName_Object = MibTableColumn
fusionFanSensorName = _FusionFanSensorName_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 2, 1, 2),
    _FusionFanSensorName_Type()
)
fusionFanSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionFanSensorName.setStatus("current")
_FusionFanSensorValue_Type = Integer32
_FusionFanSensorValue_Object = MibTableColumn
fusionFanSensorValue = _FusionFanSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 2, 2, 1, 3),
    _FusionFanSensorValue_Type()
)
fusionFanSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionFanSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    fusionFanSensorValue.setUnits("RPM")
_FusionPsuTable_Object = MibTable
fusionPsuTable = _FusionPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3)
)
if mibBuilder.loadTexts:
    fusionPsuTable.setStatus("current")
_FusionPsu_Object = MibTableRow
fusionPsu = _FusionPsu_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1)
)
fusionPsu.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionPsuIndex"),
)
if mibBuilder.loadTexts:
    fusionPsu.setStatus("current")


class _FusionPsuIndex_Type(Integer32):
    """Custom type fusionPsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionPsuIndex_Type.__name__ = "Integer32"
_FusionPsuIndex_Object = MibTableColumn
fusionPsuIndex = _FusionPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 1),
    _FusionPsuIndex_Type()
)
fusionPsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuIndex.setStatus("current")
_FusionPsuType_Type = SnmpAdminString
_FusionPsuType_Object = MibTableColumn
fusionPsuType = _FusionPsuType_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 2),
    _FusionPsuType_Type()
)
fusionPsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuType.setStatus("current")
_FusionPsuPresent_Type = TruthValue
_FusionPsuPresent_Object = MibTableColumn
fusionPsuPresent = _FusionPsuPresent_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 3),
    _FusionPsuPresent_Type()
)
fusionPsuPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuPresent.setStatus("current")
_FusionPsuTemperature_Type = Integer32
_FusionPsuTemperature_Object = MibTableColumn
fusionPsuTemperature = _FusionPsuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 4),
    _FusionPsuTemperature_Type()
)
fusionPsuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuTemperature.setStatus("current")
if mibBuilder.loadTexts:
    fusionPsuTemperature.setUnits("Celsius")
_FusionPsuPowerIn_Type = Integer32
_FusionPsuPowerIn_Object = MibTableColumn
fusionPsuPowerIn = _FusionPsuPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 5),
    _FusionPsuPowerIn_Type()
)
fusionPsuPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuPowerIn.setStatus("current")
if mibBuilder.loadTexts:
    fusionPsuPowerIn.setUnits("Watts")
_FusionPsuPowerOut_Type = Integer32
_FusionPsuPowerOut_Object = MibTableColumn
fusionPsuPowerOut = _FusionPsuPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 3, 1, 6),
    _FusionPsuPowerOut_Type()
)
fusionPsuPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    fusionPsuPowerOut.setUnits("Watts")
_FusionPortTable_Object = MibTable
fusionPortTable = _FusionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4)
)
if mibBuilder.loadTexts:
    fusionPortTable.setStatus("current")
_FusionPort_Object = MibTableRow
fusionPort = _FusionPort_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1)
)
fusionPort.setIndexNames(
    (0, "EXALINK-FUSION-MIB", "fusionPortLineCard"),
    (0, "EXALINK-FUSION-MIB", "fusionPortIndex"),
)
if mibBuilder.loadTexts:
    fusionPort.setStatus("current")


class _FusionPortLineCard_Type(Integer32):
    """Custom type fusionPortLineCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionPortLineCard_Type.__name__ = "Integer32"
_FusionPortLineCard_Object = MibTableColumn
fusionPortLineCard = _FusionPortLineCard_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 1),
    _FusionPortLineCard_Type()
)
fusionPortLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortLineCard.setStatus("current")


class _FusionPortIndex_Type(Integer32):
    """Custom type fusionPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FusionPortIndex_Type.__name__ = "Integer32"
_FusionPortIndex_Object = MibTableColumn
fusionPortIndex = _FusionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 2),
    _FusionPortIndex_Type()
)
fusionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortIndex.setStatus("current")
_FusionPortName_Type = SnmpAdminString
_FusionPortName_Object = MibTableColumn
fusionPortName = _FusionPortName_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 3),
    _FusionPortName_Type()
)
fusionPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortName.setStatus("current")
_FusionPortPresent_Type = TruthValue
_FusionPortPresent_Object = MibTableColumn
fusionPortPresent = _FusionPortPresent_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 4),
    _FusionPortPresent_Type()
)
fusionPortPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortPresent.setStatus("current")
_FusionPortHasSignal_Type = TruthValue
_FusionPortHasSignal_Object = MibTableColumn
fusionPortHasSignal = _FusionPortHasSignal_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 5),
    _FusionPortHasSignal_Type()
)
fusionPortHasSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortHasSignal.setStatus("current")
_FusionPortEnabled_Type = TruthValue
_FusionPortEnabled_Object = MibTableColumn
fusionPortEnabled = _FusionPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 6),
    _FusionPortEnabled_Type()
)
fusionPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortEnabled.setStatus("current")
_FusionPortAlias_Type = SnmpAdminString
_FusionPortAlias_Object = MibTableColumn
fusionPortAlias = _FusionPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 7),
    _FusionPortAlias_Type()
)
fusionPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionPortAlias.setStatus("current")
_FusionPortSpeed_Type = Integer32
_FusionPortSpeed_Object = MibTableColumn
fusionPortSpeed = _FusionPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 4, 1, 8),
    _FusionPortSpeed_Type()
)
fusionPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fusionPortSpeed.setStatus("current")
if mibBuilder.loadTexts:
    fusionPortSpeed.setUnits("Mbps")
_FusionTrapValues_ObjectIdentity = ObjectIdentity
fusionTrapValues = _FusionTrapValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5)
)
_FusionLidOpenStatus_Type = TruthValue
_FusionLidOpenStatus_Object = MibScalar
fusionLidOpenStatus = _FusionLidOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 1),
    _FusionLidOpenStatus_Type()
)
fusionLidOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionLidOpenStatus.setStatus("current")
_FusionFanFaultStatus_Type = TruthValue
_FusionFanFaultStatus_Object = MibScalar
fusionFanFaultStatus = _FusionFanFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 2),
    _FusionFanFaultStatus_Type()
)
fusionFanFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionFanFaultStatus.setStatus("current")
_FusionHighTempStatus_Type = TruthValue
_FusionHighTempStatus_Object = MibScalar
fusionHighTempStatus = _FusionHighTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 3),
    _FusionHighTempStatus_Type()
)
fusionHighTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionHighTempStatus.setStatus("current")


class _FusionPortUsageStatus_Type(Integer32):
    """Custom type fusionPortUsageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("off", 0),
          ("ok", 3),
          ("unused", 2))
    )


_FusionPortUsageStatus_Type.__name__ = "Integer32"
_FusionPortUsageStatus_Object = MibScalar
fusionPortUsageStatus = _FusionPortUsageStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 4),
    _FusionPortUsageStatus_Type()
)
fusionPortUsageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortUsageStatus.setStatus("current")


class _FusionPortLinkStatus_Type(Integer32):
    """Custom type fusionPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("off", 0),
          ("ok", 3),
          ("unused", 2))
    )


_FusionPortLinkStatus_Type.__name__ = "Integer32"
_FusionPortLinkStatus_Object = MibScalar
fusionPortLinkStatus = _FusionPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 5),
    _FusionPortLinkStatus_Type()
)
fusionPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPortLinkStatus.setStatus("current")
_FusionPsuFaultStatus_Type = TruthValue
_FusionPsuFaultStatus_Object = MibScalar
fusionPsuFaultStatus = _FusionPsuFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 43296, 3, 5, 6),
    _FusionPsuFaultStatus_Type()
)
fusionPsuFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fusionPsuFaultStatus.setStatus("current")
_FusionTraps_ObjectIdentity = ObjectIdentity
fusionTraps = _FusionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6)
)

# Managed Objects groups


# Notification objects

fusionPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 1)
)
if mibBuilder.loadTexts:
    fusionPowerFail.setStatus(
        "current"
    )

fusionTamperAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 2)
)
fusionTamperAlert.setObjects(
    ("EXALINK-FUSION-MIB", "fusionLidOpenStatus")
)
if mibBuilder.loadTexts:
    fusionTamperAlert.setStatus(
        "current"
    )

fusionTempAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 3)
)
fusionTempAlert.setObjects(
      *(("EXALINK-FUSION-MIB", "fusionTempSensorName"),
        ("EXALINK-FUSION-MIB", "fusionHighTempStatus"))
)
if mibBuilder.loadTexts:
    fusionTempAlert.setStatus(
        "current"
    )

fusionPsuAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 4)
)
fusionPsuAlert.setObjects(
    ("EXALINK-FUSION-MIB", "fusionPsuFaultStatus")
)
if mibBuilder.loadTexts:
    fusionPsuAlert.setStatus(
        "current"
    )

fusionSystemAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 5)
)
if mibBuilder.loadTexts:
    fusionSystemAlert.setStatus(
        "current"
    )

fusionFanAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 6)
)
fusionFanAlert.setObjects(
    ("EXALINK-FUSION-MIB", "fusionFanFaultStatus")
)
if mibBuilder.loadTexts:
    fusionFanAlert.setStatus(
        "current"
    )

fusionPortAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 7)
)
fusionPortAlert.setObjects(
      *(("EXALINK-FUSION-MIB", "fusionPortName"),
        ("EXALINK-FUSION-MIB", "fusionPortLinkStatus"),
        ("EXALINK-FUSION-MIB", "fusionPortUsageStatus"))
)
if mibBuilder.loadTexts:
    fusionPortAlert.setStatus(
        "current"
    )

fusionConfigUpdateAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 43296, 3, 6, 8)
)
if mibBuilder.loadTexts:
    fusionConfigUpdateAlert.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXALINK-FUSION-MIB",
    **{"exaFusion": exaFusion,
       "fusionInfo": fusionInfo,
       "fusionInfoSerial": fusionInfoSerial,
       "fusionInfoVersion": fusionInfoVersion,
       "fusionInfoBoard": fusionInfoBoard,
       "fusionInfoSoftware": fusionInfoSoftware,
       "fusionLineCardTable": fusionLineCardTable,
       "fusionLineCard": fusionLineCard,
       "fusionLineCardIndex": fusionLineCardIndex,
       "fusionLineCardName": fusionLineCardName,
       "fusionLineCardBoard": fusionLineCardBoard,
       "fusionModuleTable": fusionModuleTable,
       "fusionModule": fusionModule,
       "fusionModuleIndex": fusionModuleIndex,
       "fusionModuleName": fusionModuleName,
       "fusionModuleBoard": fusionModuleBoard,
       "fusionModuleFunction": fusionModuleFunction,
       "fusionSysInfo": fusionSysInfo,
       "fusionSysInfoLoadAverage": fusionSysInfoLoadAverage,
       "fusionSysInfoAvailMem": fusionSysInfoAvailMem,
       "fusionSysInfoNumProcesses": fusionSysInfoNumProcesses,
       "fusionSensor": fusionSensor,
       "fusionTempSensorTable": fusionTempSensorTable,
       "fusionTempSensor": fusionTempSensor,
       "fusionTempSensorIndex": fusionTempSensorIndex,
       "fusionTempSensorName": fusionTempSensorName,
       "fusionTempSensorValue": fusionTempSensorValue,
       "fusionFanSensorTable": fusionFanSensorTable,
       "fusionFanSensor": fusionFanSensor,
       "fusionFanSensorIndex": fusionFanSensorIndex,
       "fusionFanSensorName": fusionFanSensorName,
       "fusionFanSensorValue": fusionFanSensorValue,
       "fusionPsuTable": fusionPsuTable,
       "fusionPsu": fusionPsu,
       "fusionPsuIndex": fusionPsuIndex,
       "fusionPsuType": fusionPsuType,
       "fusionPsuPresent": fusionPsuPresent,
       "fusionPsuTemperature": fusionPsuTemperature,
       "fusionPsuPowerIn": fusionPsuPowerIn,
       "fusionPsuPowerOut": fusionPsuPowerOut,
       "fusionPortTable": fusionPortTable,
       "fusionPort": fusionPort,
       "fusionPortLineCard": fusionPortLineCard,
       "fusionPortIndex": fusionPortIndex,
       "fusionPortName": fusionPortName,
       "fusionPortPresent": fusionPortPresent,
       "fusionPortHasSignal": fusionPortHasSignal,
       "fusionPortEnabled": fusionPortEnabled,
       "fusionPortAlias": fusionPortAlias,
       "fusionPortSpeed": fusionPortSpeed,
       "fusionTrapValues": fusionTrapValues,
       "fusionLidOpenStatus": fusionLidOpenStatus,
       "fusionFanFaultStatus": fusionFanFaultStatus,
       "fusionHighTempStatus": fusionHighTempStatus,
       "fusionPortUsageStatus": fusionPortUsageStatus,
       "fusionPortLinkStatus": fusionPortLinkStatus,
       "fusionPsuFaultStatus": fusionPsuFaultStatus,
       "fusionTraps": fusionTraps,
       "fusionPowerFail": fusionPowerFail,
       "fusionTamperAlert": fusionTamperAlert,
       "fusionTempAlert": fusionTempAlert,
       "fusionPsuAlert": fusionPsuAlert,
       "fusionSystemAlert": fusionSystemAlert,
       "fusionFanAlert": fusionFanAlert,
       "fusionPortAlert": fusionPortAlert,
       "fusionConfigUpdateAlert": fusionConfigUpdateAlert}
)
