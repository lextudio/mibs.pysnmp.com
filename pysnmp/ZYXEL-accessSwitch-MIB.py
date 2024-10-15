# SNMP MIB module (ZYXEL-accessSwitch-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-accessSwitch-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:11 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ASSlotNum(Integer32):
    """Custom type ASSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slot1", 1),
          ("slot2", 2))
    )





class ASModuleType(Integer32):
    """Custom type ASModuleType based on Integer32"""
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
        *(("aam1008-61", 3),
          ("aam1008-63", 4),
          ("aes-100", 1),
          ("aes-100-1", 2),
          ("sam1008", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_AccessSwitchCommon_ObjectIdentity = ObjectIdentity
accessSwitchCommon = _AccessSwitchCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1)
)
_AccessSwitchMgnt_ObjectIdentity = ObjectIdentity
accessSwitchMgnt = _AccessSwitchMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1)
)


class _AccessSwitchSystemCurrentStatus_Type(Integer32):
    """Custom type accessSwitchSystemCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccessSwitchSystemCurrentStatus_Type.__name__ = "Integer32"
_AccessSwitchSystemCurrentStatus_Object = MibScalar
accessSwitchSystemCurrentStatus = _AccessSwitchSystemCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 1),
    _AccessSwitchSystemCurrentStatus_Type()
)
accessSwitchSystemCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSystemCurrentStatus.setStatus("mandatory")
_AccessSwitchProblemCause_Type = DisplayString
_AccessSwitchProblemCause_Object = MibScalar
accessSwitchProblemCause = _AccessSwitchProblemCause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 2),
    _AccessSwitchProblemCause_Type()
)
accessSwitchProblemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchProblemCause.setStatus("mandatory")
_AccessSwitchSystemTemperature_Type = DisplayString
_AccessSwitchSystemTemperature_Object = MibScalar
accessSwitchSystemTemperature = _AccessSwitchSystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 3),
    _AccessSwitchSystemTemperature_Type()
)
accessSwitchSystemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSystemTemperature.setStatus("mandatory")
_AccessSwitchFanRpmTable_Object = MibTable
accessSwitchFanRpmTable = _AccessSwitchFanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    accessSwitchFanRpmTable.setStatus("mandatory")
_AccessSwitchFanRpmEntry_Object = MibTableRow
accessSwitchFanRpmEntry = _AccessSwitchFanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1)
)
accessSwitchFanRpmEntry.setIndexNames(
    (0, "ZYXEL-accessSwitch-MIB", "accessSwitchFanRpmIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchFanRpmEntry.setStatus("mandatory")
_AccessSwitchFanRpmIndex_Type = Integer32
_AccessSwitchFanRpmIndex_Object = MibTableColumn
accessSwitchFanRpmIndex = _AccessSwitchFanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 1),
    _AccessSwitchFanRpmIndex_Type()
)
accessSwitchFanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmIndex.setStatus("mandatory")
_AccessSwitchFanRpmCurValue_Type = Integer32
_AccessSwitchFanRpmCurValue_Object = MibTableColumn
accessSwitchFanRpmCurValue = _AccessSwitchFanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 2),
    _AccessSwitchFanRpmCurValue_Type()
)
accessSwitchFanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmCurValue.setStatus("mandatory")
_AccessSwitchFanRpmMaxValue_Type = Integer32
_AccessSwitchFanRpmMaxValue_Object = MibTableColumn
accessSwitchFanRpmMaxValue = _AccessSwitchFanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 3),
    _AccessSwitchFanRpmMaxValue_Type()
)
accessSwitchFanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmMaxValue.setStatus("mandatory")
_AccessSwitchFanRpmMinValue_Type = Integer32
_AccessSwitchFanRpmMinValue_Object = MibTableColumn
accessSwitchFanRpmMinValue = _AccessSwitchFanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 4),
    _AccessSwitchFanRpmMinValue_Type()
)
accessSwitchFanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmMinValue.setStatus("mandatory")
_AccessSwitchFanRpmLowThresh_Type = Integer32
_AccessSwitchFanRpmLowThresh_Object = MibTableColumn
accessSwitchFanRpmLowThresh = _AccessSwitchFanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 5),
    _AccessSwitchFanRpmLowThresh_Type()
)
accessSwitchFanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmLowThresh.setStatus("mandatory")
_AccessSwitchFanRpmDescr_Type = DisplayString
_AccessSwitchFanRpmDescr_Object = MibTableColumn
accessSwitchFanRpmDescr = _AccessSwitchFanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 4, 1, 6),
    _AccessSwitchFanRpmDescr_Type()
)
accessSwitchFanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFanRpmDescr.setStatus("mandatory")
_AccessSwitchVoltageTable_Object = MibTable
accessSwitchVoltageTable = _AccessSwitchVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    accessSwitchVoltageTable.setStatus("mandatory")
_AccessSwitchVoltageEntry_Object = MibTableRow
accessSwitchVoltageEntry = _AccessSwitchVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1)
)
accessSwitchVoltageEntry.setIndexNames(
    (0, "ZYXEL-accessSwitch-MIB", "accessSwitchVoltageIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchVoltageEntry.setStatus("mandatory")
_AccessSwitchVoltageIndex_Type = Integer32
_AccessSwitchVoltageIndex_Object = MibTableColumn
accessSwitchVoltageIndex = _AccessSwitchVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 1),
    _AccessSwitchVoltageIndex_Type()
)
accessSwitchVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageIndex.setStatus("mandatory")
_AccessSwitchVoltageCurValue_Type = Integer32
_AccessSwitchVoltageCurValue_Object = MibTableColumn
accessSwitchVoltageCurValue = _AccessSwitchVoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 2),
    _AccessSwitchVoltageCurValue_Type()
)
accessSwitchVoltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageCurValue.setStatus("mandatory")
_AccessSwitchVoltageMaxValue_Type = Integer32
_AccessSwitchVoltageMaxValue_Object = MibTableColumn
accessSwitchVoltageMaxValue = _AccessSwitchVoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 3),
    _AccessSwitchVoltageMaxValue_Type()
)
accessSwitchVoltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageMaxValue.setStatus("mandatory")
_AccessSwitchVoltageMinValue_Type = Integer32
_AccessSwitchVoltageMinValue_Object = MibTableColumn
accessSwitchVoltageMinValue = _AccessSwitchVoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 4),
    _AccessSwitchVoltageMinValue_Type()
)
accessSwitchVoltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageMinValue.setStatus("mandatory")
_AccessSwitchVoltageNominalValue_Type = Integer32
_AccessSwitchVoltageNominalValue_Object = MibTableColumn
accessSwitchVoltageNominalValue = _AccessSwitchVoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 5),
    _AccessSwitchVoltageNominalValue_Type()
)
accessSwitchVoltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageNominalValue.setStatus("mandatory")
_AccessSwitchVoltageLowThresh_Type = Integer32
_AccessSwitchVoltageLowThresh_Object = MibTableColumn
accessSwitchVoltageLowThresh = _AccessSwitchVoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 6),
    _AccessSwitchVoltageLowThresh_Type()
)
accessSwitchVoltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageLowThresh.setStatus("mandatory")
_AccessSwitchVoltageDescr_Type = DisplayString
_AccessSwitchVoltageDescr_Object = MibTableColumn
accessSwitchVoltageDescr = _AccessSwitchVoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 5, 1, 7),
    _AccessSwitchVoltageDescr_Type()
)
accessSwitchVoltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchVoltageDescr.setStatus("mandatory")
_AccessSwitchSysTempTable_Object = MibTable
accessSwitchSysTempTable = _AccessSwitchSysTempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    accessSwitchSysTempTable.setStatus("mandatory")
_AccessSwitchSysTempEntry_Object = MibTableRow
accessSwitchSysTempEntry = _AccessSwitchSysTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1)
)
accessSwitchSysTempEntry.setIndexNames(
    (0, "ZYXEL-accessSwitch-MIB", "accessSwitchSysTempIndex"),
)
if mibBuilder.loadTexts:
    accessSwitchSysTempEntry.setStatus("mandatory")
_AccessSwitchSysTempIndex_Type = Integer32
_AccessSwitchSysTempIndex_Object = MibTableColumn
accessSwitchSysTempIndex = _AccessSwitchSysTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 1),
    _AccessSwitchSysTempIndex_Type()
)
accessSwitchSysTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempIndex.setStatus("mandatory")
_AccessSwitchSysTempCurValue_Type = Integer32
_AccessSwitchSysTempCurValue_Object = MibTableColumn
accessSwitchSysTempCurValue = _AccessSwitchSysTempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 2),
    _AccessSwitchSysTempCurValue_Type()
)
accessSwitchSysTempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempCurValue.setStatus("mandatory")
_AccessSwitchSysTempMaxValue_Type = Integer32
_AccessSwitchSysTempMaxValue_Object = MibTableColumn
accessSwitchSysTempMaxValue = _AccessSwitchSysTempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 3),
    _AccessSwitchSysTempMaxValue_Type()
)
accessSwitchSysTempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempMaxValue.setStatus("mandatory")
_AccessSwitchSysTempMinValue_Type = Integer32
_AccessSwitchSysTempMinValue_Object = MibTableColumn
accessSwitchSysTempMinValue = _AccessSwitchSysTempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 4),
    _AccessSwitchSysTempMinValue_Type()
)
accessSwitchSysTempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempMinValue.setStatus("mandatory")
_AccessSwitchSysTempHighThresh_Type = Integer32
_AccessSwitchSysTempHighThresh_Object = MibTableColumn
accessSwitchSysTempHighThresh = _AccessSwitchSysTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 5),
    _AccessSwitchSysTempHighThresh_Type()
)
accessSwitchSysTempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempHighThresh.setStatus("mandatory")
_AccessSwitchSysTempDescr_Type = DisplayString
_AccessSwitchSysTempDescr_Object = MibTableColumn
accessSwitchSysTempDescr = _AccessSwitchSysTempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 6, 1, 6),
    _AccessSwitchSysTempDescr_Type()
)
accessSwitchSysTempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchSysTempDescr.setStatus("mandatory")
_AccessSwitchMaintenance_Type = Integer32
_AccessSwitchMaintenance_Object = MibScalar
accessSwitchMaintenance = _AccessSwitchMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 7),
    _AccessSwitchMaintenance_Type()
)
accessSwitchMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchMaintenance.setStatus("mandatory")
_AccessSwitchMaintenancePort_Type = Integer32
_AccessSwitchMaintenancePort_Object = MibScalar
accessSwitchMaintenancePort = _AccessSwitchMaintenancePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 8),
    _AccessSwitchMaintenancePort_Type()
)
accessSwitchMaintenancePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchMaintenancePort.setStatus("mandatory")
_AccessSwitchMaxNumOfStaticVlans_Type = Integer32
_AccessSwitchMaxNumOfStaticVlans_Object = MibScalar
accessSwitchMaxNumOfStaticVlans = _AccessSwitchMaxNumOfStaticVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 9),
    _AccessSwitchMaxNumOfStaticVlans_Type()
)
accessSwitchMaxNumOfStaticVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchMaxNumOfStaticVlans.setStatus("mandatory")
_AcccessSwitchChassisId_Type = Integer32
_AcccessSwitchChassisId_Object = MibScalar
acccessSwitchChassisId = _AcccessSwitchChassisId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 10),
    _AcccessSwitchChassisId_Type()
)
acccessSwitchChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acccessSwitchChassisId.setStatus("mandatory")
_AccessSwitchSlotId_Type = ASSlotNum
_AccessSwitchSlotId_Object = MibScalar
accessSwitchSlotId = _AccessSwitchSlotId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 11),
    _AccessSwitchSlotId_Type()
)
accessSwitchSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchSlotId.setStatus("mandatory")
_AccessSwitchModuleType_Type = ASModuleType
_AccessSwitchModuleType_Object = MibScalar
accessSwitchModuleType = _AccessSwitchModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 12),
    _AccessSwitchModuleType_Type()
)
accessSwitchModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchModuleType.setStatus("mandatory")
_AccessSwitchFWVersion_Type = DisplayString
_AccessSwitchFWVersion_Object = MibScalar
accessSwitchFWVersion = _AccessSwitchFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 13),
    _AccessSwitchFWVersion_Type()
)
accessSwitchFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchFWVersion.setStatus("mandatory")
_AccessSwitchDriverVersion_Type = DisplayString
_AccessSwitchDriverVersion_Object = MibScalar
accessSwitchDriverVersion = _AccessSwitchDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 14),
    _AccessSwitchDriverVersion_Type()
)
accessSwitchDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchDriverVersion.setStatus("mandatory")
_AccessSwitchModemCodeVersion_Type = DisplayString
_AccessSwitchModemCodeVersion_Object = MibScalar
accessSwitchModemCodeVersion = _AccessSwitchModemCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 15),
    _AccessSwitchModemCodeVersion_Type()
)
accessSwitchModemCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessSwitchModemCodeVersion.setStatus("mandatory")
_AccessSwitchDSLConfOps_Type = Integer32
_AccessSwitchDSLConfOps_Object = MibScalar
accessSwitchDSLConfOps = _AccessSwitchDSLConfOps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 16),
    _AccessSwitchDSLConfOps_Type()
)
accessSwitchDSLConfOps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchDSLConfOps.setStatus("mandatory")
_AccessSwitchDSLConfTarget_Type = OctetString
_AccessSwitchDSLConfTarget_Object = MibScalar
accessSwitchDSLConfTarget = _AccessSwitchDSLConfTarget_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 17),
    _AccessSwitchDSLConfTarget_Type()
)
accessSwitchDSLConfTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchDSLConfTarget.setStatus("mandatory")


class _AccessSwitchDSLConfProfileName_Type(DisplayString):
    """Custom type accessSwitchDSLConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AccessSwitchDSLConfProfileName_Type.__name__ = "DisplayString"
_AccessSwitchDSLConfProfileName_Object = MibScalar
accessSwitchDSLConfProfileName = _AccessSwitchDSLConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 18),
    _AccessSwitchDSLConfProfileName_Type()
)
accessSwitchDSLConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchDSLConfProfileName.setStatus("mandatory")
_AccessSwitchDSLConfMode_Type = Integer32
_AccessSwitchDSLConfMode_Object = MibScalar
accessSwitchDSLConfMode = _AccessSwitchDSLConfMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 19),
    _AccessSwitchDSLConfMode_Type()
)
accessSwitchDSLConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessSwitchDSLConfMode.setStatus("mandatory")
_AsPacketForwardingTable_Object = MibTable
asPacketForwardingTable = _AsPacketForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 20)
)
if mibBuilder.loadTexts:
    asPacketForwardingTable.setStatus("mandatory")
_AsPacketForwardingEntry_Object = MibTableRow
asPacketForwardingEntry = _AsPacketForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 20, 1)
)
asPacketForwardingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asPacketForwardingEntry.setStatus("mandatory")
_AsPacketForwardingPortList_Type = PortList
_AsPacketForwardingPortList_Object = MibTableColumn
asPacketForwardingPortList = _AsPacketForwardingPortList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 20, 1, 1),
    _AsPacketForwardingPortList_Type()
)
asPacketForwardingPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asPacketForwardingPortList.setStatus("mandatory")


class _AsDhcpRelayEnable_Type(Integer32):
    """Custom type asDhcpRelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AsDhcpRelayEnable_Type.__name__ = "Integer32"
_AsDhcpRelayEnable_Object = MibScalar
asDhcpRelayEnable = _AsDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 21),
    _AsDhcpRelayEnable_Type()
)
asDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDhcpRelayEnable.setStatus("mandatory")


class _AsDhcpRelayOption82Enable_Type(Integer32):
    """Custom type asDhcpRelayOption82Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AsDhcpRelayOption82Enable_Type.__name__ = "Integer32"
_AsDhcpRelayOption82Enable_Object = MibScalar
asDhcpRelayOption82Enable = _AsDhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 22),
    _AsDhcpRelayOption82Enable_Type()
)
asDhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDhcpRelayOption82Enable.setStatus("mandatory")
_AsDhcpRelayOption82Info_Type = DisplayString
_AsDhcpRelayOption82Info_Object = MibScalar
asDhcpRelayOption82Info = _AsDhcpRelayOption82Info_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 23),
    _AsDhcpRelayOption82Info_Type()
)
asDhcpRelayOption82Info.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDhcpRelayOption82Info.setStatus("mandatory")
_AsMaxNumOfDhcpServers_Type = Integer32
_AsMaxNumOfDhcpServers_Object = MibScalar
asMaxNumOfDhcpServers = _AsMaxNumOfDhcpServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 24),
    _AsMaxNumOfDhcpServers_Type()
)
asMaxNumOfDhcpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxNumOfDhcpServers.setStatus("mandatory")
_AsDhcpServerTable_Object = MibTable
asDhcpServerTable = _AsDhcpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 25)
)
if mibBuilder.loadTexts:
    asDhcpServerTable.setStatus("mandatory")
_AsDhcpServerEntry_Object = MibTableRow
asDhcpServerEntry = _AsDhcpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 25, 1)
)
asDhcpServerEntry.setIndexNames(
    (0, "ZYXEL-accessSwitch-MIB", "asDhcpServerIp"),
)
if mibBuilder.loadTexts:
    asDhcpServerEntry.setStatus("mandatory")
_AsDhcpServerIp_Type = IpAddress
_AsDhcpServerIp_Object = MibTableColumn
asDhcpServerIp = _AsDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 25, 1, 1),
    _AsDhcpServerIp_Type()
)
asDhcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDhcpServerIp.setStatus("mandatory")
_AsDhcpServerRowStatus_Type = RowStatus
_AsDhcpServerRowStatus_Object = MibTableColumn
asDhcpServerRowStatus = _AsDhcpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 25, 1, 2),
    _AsDhcpServerRowStatus_Type()
)
asDhcpServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDhcpServerRowStatus.setStatus("mandatory")
_AsMaxNumberOfRadiusServers_Type = Integer32
_AsMaxNumberOfRadiusServers_Object = MibScalar
asMaxNumberOfRadiusServers = _AsMaxNumberOfRadiusServers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 28),
    _AsMaxNumberOfRadiusServers_Type()
)
asMaxNumberOfRadiusServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxNumberOfRadiusServers.setStatus("mandatory")
_AsRadiusServerTable_Object = MibTable
asRadiusServerTable = _AsRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29)
)
if mibBuilder.loadTexts:
    asRadiusServerTable.setStatus("mandatory")
_AsRadiusServerEntry_Object = MibTableRow
asRadiusServerEntry = _AsRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1)
)
asRadiusServerEntry.setIndexNames(
    (0, "ZYXEL-accessSwitch-MIB", "asRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    asRadiusServerEntry.setStatus("mandatory")
_AsRadiusServerIndex_Type = Integer32
_AsRadiusServerIndex_Object = MibTableColumn
asRadiusServerIndex = _AsRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1, 1),
    _AsRadiusServerIndex_Type()
)
asRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asRadiusServerIndex.setStatus("mandatory")
_AsRadiusServerIp_Type = IpAddress
_AsRadiusServerIp_Object = MibTableColumn
asRadiusServerIp = _AsRadiusServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1, 2),
    _AsRadiusServerIp_Type()
)
asRadiusServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asRadiusServerIp.setStatus("mandatory")
_AsRadiusServerPort_Type = Integer32
_AsRadiusServerPort_Object = MibTableColumn
asRadiusServerPort = _AsRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1, 3),
    _AsRadiusServerPort_Type()
)
asRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asRadiusServerPort.setStatus("mandatory")
_AsRadiusSharedSecret_Type = DisplayString
_AsRadiusSharedSecret_Object = MibTableColumn
asRadiusSharedSecret = _AsRadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1, 4),
    _AsRadiusSharedSecret_Type()
)
asRadiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asRadiusSharedSecret.setStatus("mandatory")
_AsRadiusServerRowStatus_Type = RowStatus
_AsRadiusServerRowStatus_Object = MibTableColumn
asRadiusServerRowStatus = _AsRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 29, 1, 5),
    _AsRadiusServerRowStatus_Type()
)
asRadiusServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asRadiusServerRowStatus.setStatus("mandatory")


class _AsDot1xEnable_Type(Integer32):
    """Custom type asDot1xEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AsDot1xEnable_Type.__name__ = "Integer32"
_AsDot1xEnable_Object = MibScalar
asDot1xEnable = _AsDot1xEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 30),
    _AsDot1xEnable_Type()
)
asDot1xEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDot1xEnable.setStatus("mandatory")
_AsDot1xPortTable_Object = MibTable
asDot1xPortTable = _AsDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31)
)
if mibBuilder.loadTexts:
    asDot1xPortTable.setStatus("mandatory")
_AsDot1xPortEntry_Object = MibTableRow
asDot1xPortEntry = _AsDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31, 1)
)
asDot1xPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asDot1xPortEntry.setStatus("mandatory")


class _AsDot1xPortEnable_Type(Integer32):
    """Custom type asDot1xPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AsDot1xPortEnable_Type.__name__ = "Integer32"
_AsDot1xPortEnable_Object = MibTableColumn
asDot1xPortEnable = _AsDot1xPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31, 1, 1),
    _AsDot1xPortEnable_Type()
)
asDot1xPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDot1xPortEnable.setStatus("mandatory")


class _AsDot1xPortControl_Type(Integer32):
    """Custom type asDot1xPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("forceAuth", 2),
          ("forceUnAuth", 3))
    )


_AsDot1xPortControl_Type.__name__ = "Integer32"
_AsDot1xPortControl_Object = MibTableColumn
asDot1xPortControl = _AsDot1xPortControl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31, 1, 2),
    _AsDot1xPortControl_Type()
)
asDot1xPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDot1xPortControl.setStatus("mandatory")


class _AsDot1xPortReAuthEnable_Type(Integer32):
    """Custom type asDot1xPortReAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AsDot1xPortReAuthEnable_Type.__name__ = "Integer32"
_AsDot1xPortReAuthEnable_Object = MibTableColumn
asDot1xPortReAuthEnable = _AsDot1xPortReAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31, 1, 3),
    _AsDot1xPortReAuthEnable_Type()
)
asDot1xPortReAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDot1xPortReAuthEnable.setStatus("mandatory")
_AsDot1xPortReAuthPeriod_Type = Integer32
_AsDot1xPortReAuthPeriod_Object = MibTableColumn
asDot1xPortReAuthPeriod = _AsDot1xPortReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 1, 1, 31, 1, 4),
    _AsDot1xPortReAuthPeriod_Type()
)
asDot1xPortReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asDot1xPortReAuthPeriod.setStatus("mandatory")

# Managed Objects groups


# Notification objects

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 1)
)
reboot.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        ""
    )

systemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 2)
)
systemShutdown.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    systemShutdown.setStatus(
        ""
    )

overheat = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 3)
)
overheat.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchSysTempIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSysTempCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    overheat.setStatus(
        ""
    )

overheatOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 4)
)
overheatOver.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchSysTempIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSysTempCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    overheatOver.setStatus(
        ""
    )

errLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 5)
)
errLog.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    errLog.setStatus(
        ""
    )

fanRpmLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 6)
)
fanRpmLow.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchFanRpmIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchFanRpmCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    fanRpmLow.setStatus(
        ""
    )

fanRpmNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 7)
)
fanRpmNormal.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchFanRpmIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchFanRpmCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    fanRpmNormal.setStatus(
        ""
    )

voltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 8)
)
voltageOutOfRange.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchVoltageIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchVoltageCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    voltageOutOfRange.setStatus(
        ""
    )

voltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 9)
)
voltageNormal.setObjects(
      *(("ZYXEL-accessSwitch-MIB", "accessSwitchVoltageIndex"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchVoltageCurValue"),
        ("ZYXEL-accessSwitch-MIB", "accessSwitchSystemCurrentStatus"))
)
if mibBuilder.loadTexts:
    voltageNormal.setStatus(
        ""
    )

systemMaintenanceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 10)
)
systemMaintenanceFailure.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    systemMaintenanceFailure.setStatus(
        ""
    )

configChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 11)
)
configChange.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    configChange.setStatus(
        ""
    )

thermalSensorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 0, 12)
)
thermalSensorFailure.setObjects(
    ("ZYXEL-accessSwitch-MIB", "accessSwitchProblemCause")
)
if mibBuilder.loadTexts:
    thermalSensorFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-accessSwitch-MIB",
    **{"ASSlotNum": ASSlotNum,
       "ASModuleType": ASModuleType,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "reboot": reboot,
       "systemShutdown": systemShutdown,
       "overheat": overheat,
       "overheatOver": overheatOver,
       "errLog": errLog,
       "fanRpmLow": fanRpmLow,
       "fanRpmNormal": fanRpmNormal,
       "voltageOutOfRange": voltageOutOfRange,
       "voltageNormal": voltageNormal,
       "systemMaintenanceFailure": systemMaintenanceFailure,
       "configChange": configChange,
       "thermalSensorFailure": thermalSensorFailure,
       "accessSwitchCommon": accessSwitchCommon,
       "accessSwitchMgnt": accessSwitchMgnt,
       "accessSwitchSystemCurrentStatus": accessSwitchSystemCurrentStatus,
       "accessSwitchProblemCause": accessSwitchProblemCause,
       "accessSwitchSystemTemperature": accessSwitchSystemTemperature,
       "accessSwitchFanRpmTable": accessSwitchFanRpmTable,
       "accessSwitchFanRpmEntry": accessSwitchFanRpmEntry,
       "accessSwitchFanRpmIndex": accessSwitchFanRpmIndex,
       "accessSwitchFanRpmCurValue": accessSwitchFanRpmCurValue,
       "accessSwitchFanRpmMaxValue": accessSwitchFanRpmMaxValue,
       "accessSwitchFanRpmMinValue": accessSwitchFanRpmMinValue,
       "accessSwitchFanRpmLowThresh": accessSwitchFanRpmLowThresh,
       "accessSwitchFanRpmDescr": accessSwitchFanRpmDescr,
       "accessSwitchVoltageTable": accessSwitchVoltageTable,
       "accessSwitchVoltageEntry": accessSwitchVoltageEntry,
       "accessSwitchVoltageIndex": accessSwitchVoltageIndex,
       "accessSwitchVoltageCurValue": accessSwitchVoltageCurValue,
       "accessSwitchVoltageMaxValue": accessSwitchVoltageMaxValue,
       "accessSwitchVoltageMinValue": accessSwitchVoltageMinValue,
       "accessSwitchVoltageNominalValue": accessSwitchVoltageNominalValue,
       "accessSwitchVoltageLowThresh": accessSwitchVoltageLowThresh,
       "accessSwitchVoltageDescr": accessSwitchVoltageDescr,
       "accessSwitchSysTempTable": accessSwitchSysTempTable,
       "accessSwitchSysTempEntry": accessSwitchSysTempEntry,
       "accessSwitchSysTempIndex": accessSwitchSysTempIndex,
       "accessSwitchSysTempCurValue": accessSwitchSysTempCurValue,
       "accessSwitchSysTempMaxValue": accessSwitchSysTempMaxValue,
       "accessSwitchSysTempMinValue": accessSwitchSysTempMinValue,
       "accessSwitchSysTempHighThresh": accessSwitchSysTempHighThresh,
       "accessSwitchSysTempDescr": accessSwitchSysTempDescr,
       "accessSwitchMaintenance": accessSwitchMaintenance,
       "accessSwitchMaintenancePort": accessSwitchMaintenancePort,
       "accessSwitchMaxNumOfStaticVlans": accessSwitchMaxNumOfStaticVlans,
       "acccessSwitchChassisId": acccessSwitchChassisId,
       "accessSwitchSlotId": accessSwitchSlotId,
       "accessSwitchModuleType": accessSwitchModuleType,
       "accessSwitchFWVersion": accessSwitchFWVersion,
       "accessSwitchDriverVersion": accessSwitchDriverVersion,
       "accessSwitchModemCodeVersion": accessSwitchModemCodeVersion,
       "accessSwitchDSLConfOps": accessSwitchDSLConfOps,
       "accessSwitchDSLConfTarget": accessSwitchDSLConfTarget,
       "accessSwitchDSLConfProfileName": accessSwitchDSLConfProfileName,
       "accessSwitchDSLConfMode": accessSwitchDSLConfMode,
       "asPacketForwardingTable": asPacketForwardingTable,
       "asPacketForwardingEntry": asPacketForwardingEntry,
       "asPacketForwardingPortList": asPacketForwardingPortList,
       "asDhcpRelayEnable": asDhcpRelayEnable,
       "asDhcpRelayOption82Enable": asDhcpRelayOption82Enable,
       "asDhcpRelayOption82Info": asDhcpRelayOption82Info,
       "asMaxNumOfDhcpServers": asMaxNumOfDhcpServers,
       "asDhcpServerTable": asDhcpServerTable,
       "asDhcpServerEntry": asDhcpServerEntry,
       "asDhcpServerIp": asDhcpServerIp,
       "asDhcpServerRowStatus": asDhcpServerRowStatus,
       "asMaxNumberOfRadiusServers": asMaxNumberOfRadiusServers,
       "asRadiusServerTable": asRadiusServerTable,
       "asRadiusServerEntry": asRadiusServerEntry,
       "asRadiusServerIndex": asRadiusServerIndex,
       "asRadiusServerIp": asRadiusServerIp,
       "asRadiusServerPort": asRadiusServerPort,
       "asRadiusSharedSecret": asRadiusSharedSecret,
       "asRadiusServerRowStatus": asRadiusServerRowStatus,
       "asDot1xEnable": asDot1xEnable,
       "asDot1xPortTable": asDot1xPortTable,
       "asDot1xPortEntry": asDot1xPortEntry,
       "asDot1xPortEnable": asDot1xPortEnable,
       "asDot1xPortControl": asDot1xPortControl,
       "asDot1xPortReAuthEnable": asDot1xPortReAuthEnable,
       "asDot1xPortReAuthPeriod": asDot1xPortReAuthPeriod}
)
