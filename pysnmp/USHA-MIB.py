# SNMP MIB module (USHA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/USHA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:43 2024
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

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ingrasys_ObjectIdentity = ObjectIdentity
ingrasys = _Ingrasys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1)
)
_UpsAgent_ObjectIdentity = ObjectIdentity
upsAgent = _UpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2)
)
_Ushap_ObjectIdentity = ObjectIdentity
ushap = _Ushap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1)
)
_UpsObjectGroup_ObjectIdentity = ObjectIdentity
upsObjectGroup = _UpsObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1)
)
_UpsIdentGroup_ObjectIdentity = ObjectIdentity
upsIdentGroup = _UpsIdentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1)
)


class _UpsIdentGroupManufacturer_Type(DisplayString):
    """Custom type upsIdentGroupManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentGroupManufacturer_Type.__name__ = "DisplayString"
_UpsIdentGroupManufacturer_Object = MibScalar
upsIdentGroupManufacturer = _UpsIdentGroupManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 1),
    _UpsIdentGroupManufacturer_Type()
)
upsIdentGroupManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentGroupManufacturer.setStatus("mandatory")


class _UpsIdentGroupModel_Type(DisplayString):
    """Custom type upsIdentGroupModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentGroupModel_Type.__name__ = "DisplayString"
_UpsIdentGroupModel_Object = MibScalar
upsIdentGroupModel = _UpsIdentGroupModel_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 2),
    _UpsIdentGroupModel_Type()
)
upsIdentGroupModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentGroupModel.setStatus("mandatory")


class _UpsIdentGroupUPSFirmwareVersion_Type(DisplayString):
    """Custom type upsIdentGroupUPSFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentGroupUPSFirmwareVersion_Type.__name__ = "DisplayString"
_UpsIdentGroupUPSFirmwareVersion_Object = MibScalar
upsIdentGroupUPSFirmwareVersion = _UpsIdentGroupUPSFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 3),
    _UpsIdentGroupUPSFirmwareVersion_Type()
)
upsIdentGroupUPSFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentGroupUPSFirmwareVersion.setStatus("mandatory")


class _UpsIdentGroupAgentSoftwareVersion_Type(DisplayString):
    """Custom type upsIdentGroupAgentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentGroupAgentSoftwareVersion_Type.__name__ = "DisplayString"
_UpsIdentGroupAgentSoftwareVersion_Object = MibScalar
upsIdentGroupAgentSoftwareVersion = _UpsIdentGroupAgentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 4),
    _UpsIdentGroupAgentSoftwareVersion_Type()
)
upsIdentGroupAgentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentGroupAgentSoftwareVersion.setStatus("mandatory")


class _UpsIdentGroupName_Type(DisplayString):
    """Custom type upsIdentGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentGroupName_Type.__name__ = "DisplayString"
_UpsIdentGroupName_Object = MibScalar
upsIdentGroupName = _UpsIdentGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 5),
    _UpsIdentGroupName_Type()
)
upsIdentGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentGroupName.setStatus("mandatory")


class _UpsIdentGroupAttachedDevices_Type(DisplayString):
    """Custom type upsIdentGroupAttachedDevices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentGroupAttachedDevices_Type.__name__ = "DisplayString"
_UpsIdentGroupAttachedDevices_Object = MibScalar
upsIdentGroupAttachedDevices = _UpsIdentGroupAttachedDevices_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 6),
    _UpsIdentGroupAttachedDevices_Type()
)
upsIdentGroupAttachedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdentGroupAttachedDevices.setStatus("mandatory")


class _UpsIdentGroupUpsSerialNumber_Type(DisplayString):
    """Custom type upsIdentGroupUpsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsIdentGroupUpsSerialNumber_Type.__name__ = "DisplayString"
_UpsIdentGroupUpsSerialNumber_Object = MibScalar
upsIdentGroupUpsSerialNumber = _UpsIdentGroupUpsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 1, 7),
    _UpsIdentGroupUpsSerialNumber_Type()
)
upsIdentGroupUpsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentGroupUpsSerialNumber.setStatus("mandatory")
_UpsBatteryGroup_ObjectIdentity = ObjectIdentity
upsBatteryGroup = _UpsBatteryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2)
)


class _UpsBatteryGroupStatus_Type(Integer32):
    """Custom type upsBatteryGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("batteryDepleted", 4),
          ("batteryDischarging", 5),
          ("batteryFailure", 6),
          ("batteryLow", 3),
          ("batteryNormal", 2),
          ("unknown", 1))
    )


_UpsBatteryGroupStatus_Type.__name__ = "Integer32"
_UpsBatteryGroupStatus_Object = MibScalar
upsBatteryGroupStatus = _UpsBatteryGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 1),
    _UpsBatteryGroupStatus_Type()
)
upsBatteryGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupStatus.setStatus("mandatory")
_UpsBatteryGroupSecondsOnBattery_Type = Integer32
_UpsBatteryGroupSecondsOnBattery_Object = MibScalar
upsBatteryGroupSecondsOnBattery = _UpsBatteryGroupSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 2),
    _UpsBatteryGroupSecondsOnBattery_Type()
)
upsBatteryGroupSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupSecondsOnBattery.setStatus("mandatory")
_UpsBatteryGroupEstimatedMinutesRemaining_Type = Integer32
_UpsBatteryGroupEstimatedMinutesRemaining_Object = MibScalar
upsBatteryGroupEstimatedMinutesRemaining = _UpsBatteryGroupEstimatedMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 3),
    _UpsBatteryGroupEstimatedMinutesRemaining_Type()
)
upsBatteryGroupEstimatedMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupEstimatedMinutesRemaining.setStatus("mandatory")
_UpsBatteryGroupEstimatedChargeRemaining_Type = Integer32
_UpsBatteryGroupEstimatedChargeRemaining_Object = MibScalar
upsBatteryGroupEstimatedChargeRemaining = _UpsBatteryGroupEstimatedChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 4),
    _UpsBatteryGroupEstimatedChargeRemaining_Type()
)
upsBatteryGroupEstimatedChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupEstimatedChargeRemaining.setStatus("mandatory")
_UpsBatteryGroupVoltage_Type = Integer32
_UpsBatteryGroupVoltage_Object = MibScalar
upsBatteryGroupVoltage = _UpsBatteryGroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 5),
    _UpsBatteryGroupVoltage_Type()
)
upsBatteryGroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupVoltage.setStatus("mandatory")
_UpsBatteryGroupMandatory_Type = Integer32
_UpsBatteryGroupMandatory_Object = MibScalar
upsBatteryGroupMandatory = _UpsBatteryGroupMandatory_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 6),
    _UpsBatteryGroupMandatory_Type()
)
upsBatteryGroupMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupMandatory.setStatus("mandatory")
_UpsBatteryGroupTemperature_Type = Integer32
_UpsBatteryGroupTemperature_Object = MibScalar
upsBatteryGroupTemperature = _UpsBatteryGroupTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 2, 7),
    _UpsBatteryGroupTemperature_Type()
)
upsBatteryGroupTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryGroupTemperature.setStatus("mandatory")
_UpsInputGroup_ObjectIdentity = ObjectIdentity
upsInputGroup = _UpsInputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3)
)
_UpsInputGroupLineBads_Type = Counter32
_UpsInputGroupLineBads_Object = MibScalar
upsInputGroupLineBads = _UpsInputGroupLineBads_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 1),
    _UpsInputGroupLineBads_Type()
)
upsInputGroupLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupLineBads.setStatus("mandatory")
_UpsInputGroupNumLines_Type = Integer32
_UpsInputGroupNumLines_Object = MibScalar
upsInputGroupNumLines = _UpsInputGroupNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 2),
    _UpsInputGroupNumLines_Type()
)
upsInputGroupNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupNumLines.setStatus("mandatory")
_UpsInputGroupTable_Object = MibTable
upsInputGroupTable = _UpsInputGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    upsInputGroupTable.setStatus("mandatory")
_UpsInputGroupEntry_Object = MibTableRow
upsInputGroupEntry = _UpsInputGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1)
)
upsInputGroupEntry.setIndexNames(
    (0, "USHA-MIB", "upsInputGroupLineIndex"),
)
if mibBuilder.loadTexts:
    upsInputGroupEntry.setStatus("mandatory")


class _UpsInputGroupLineIndex_Type(PositiveInteger):
    """Custom type upsInputGroupLineIndex based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsInputGroupLineIndex_Type.__name__ = "PositiveInteger"
_UpsInputGroupLineIndex_Object = MibTableColumn
upsInputGroupLineIndex = _UpsInputGroupLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 1),
    _UpsInputGroupLineIndex_Type()
)
upsInputGroupLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupLineIndex.setStatus("mandatory")
_UpsInputGroupFrequency_Type = NonNegativeInteger
_UpsInputGroupFrequency_Object = MibTableColumn
upsInputGroupFrequency = _UpsInputGroupFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 2),
    _UpsInputGroupFrequency_Type()
)
upsInputGroupFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupFrequency.setStatus("mandatory")
_UpsInputGroupVoltage_Type = NonNegativeInteger
_UpsInputGroupVoltage_Object = MibTableColumn
upsInputGroupVoltage = _UpsInputGroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 3),
    _UpsInputGroupVoltage_Type()
)
upsInputGroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupVoltage.setStatus("mandatory")
_UpsInputGroupCurrent_Type = NonNegativeInteger
_UpsInputGroupCurrent_Object = MibTableColumn
upsInputGroupCurrent = _UpsInputGroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 4),
    _UpsInputGroupCurrent_Type()
)
upsInputGroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupCurrent.setStatus("mandatory")
_UpsInputGroupTruePower_Type = NonNegativeInteger
_UpsInputGroupTruePower_Object = MibTableColumn
upsInputGroupTruePower = _UpsInputGroupTruePower_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 5),
    _UpsInputGroupTruePower_Type()
)
upsInputGroupTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupTruePower.setStatus("mandatory")
_UpsInputGroupVoltageMax_Type = NonNegativeInteger
_UpsInputGroupVoltageMax_Object = MibTableColumn
upsInputGroupVoltageMax = _UpsInputGroupVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 6),
    _UpsInputGroupVoltageMax_Type()
)
upsInputGroupVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupVoltageMax.setStatus("mandatory")
_UpsInputGroupVoltageMin_Type = NonNegativeInteger
_UpsInputGroupVoltageMin_Object = MibTableColumn
upsInputGroupVoltageMin = _UpsInputGroupVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 3, 3, 1, 7),
    _UpsInputGroupVoltageMin_Type()
)
upsInputGroupVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputGroupVoltageMin.setStatus("mandatory")
_UpsOutputGroup_ObjectIdentity = ObjectIdentity
upsOutputGroup = _UpsOutputGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4)
)


class _UpsOutputGroupSource_Type(Integer32):
    """Custom type upsOutputGroupSource based on Integer32"""
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
        *(("battery", 5),
          ("booster", 6),
          ("bypass", 4),
          ("none", 2),
          ("normal", 3),
          ("other", 1),
          ("reducer", 7))
    )


_UpsOutputGroupSource_Type.__name__ = "Integer32"
_UpsOutputGroupSource_Object = MibScalar
upsOutputGroupSource = _UpsOutputGroupSource_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 1),
    _UpsOutputGroupSource_Type()
)
upsOutputGroupSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupSource.setStatus("mandatory")
_UpsOutputGroupFrequency_Type = Integer32
_UpsOutputGroupFrequency_Object = MibScalar
upsOutputGroupFrequency = _UpsOutputGroupFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 2),
    _UpsOutputGroupFrequency_Type()
)
upsOutputGroupFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupFrequency.setStatus("mandatory")
_UpsOutputGroupNumLines_Type = Integer32
_UpsOutputGroupNumLines_Object = MibScalar
upsOutputGroupNumLines = _UpsOutputGroupNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 3),
    _UpsOutputGroupNumLines_Type()
)
upsOutputGroupNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupNumLines.setStatus("mandatory")
_UpsOutputGroupTable_Object = MibTable
upsOutputGroupTable = _UpsOutputGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputGroupTable.setStatus("mandatory")
_UpsOutputGroupEntry_Object = MibTableRow
upsOutputGroupEntry = _UpsOutputGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1)
)
upsOutputGroupEntry.setIndexNames(
    (0, "USHA-MIB", "upsOutputGroupLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutputGroupEntry.setStatus("mandatory")


class _UpsOutputGroupLineIndex_Type(PositiveInteger):
    """Custom type upsOutputGroupLineIndex based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsOutputGroupLineIndex_Type.__name__ = "PositiveInteger"
_UpsOutputGroupLineIndex_Object = MibTableColumn
upsOutputGroupLineIndex = _UpsOutputGroupLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1, 1),
    _UpsOutputGroupLineIndex_Type()
)
upsOutputGroupLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupLineIndex.setStatus("mandatory")
_UpsOutputGroupVoltage_Type = NonNegativeInteger
_UpsOutputGroupVoltage_Object = MibTableColumn
upsOutputGroupVoltage = _UpsOutputGroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1, 2),
    _UpsOutputGroupVoltage_Type()
)
upsOutputGroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupVoltage.setStatus("mandatory")
_UpsOutputGroupCurrent_Type = NonNegativeInteger
_UpsOutputGroupCurrent_Object = MibTableColumn
upsOutputGroupCurrent = _UpsOutputGroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1, 3),
    _UpsOutputGroupCurrent_Type()
)
upsOutputGroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupCurrent.setStatus("mandatory")
_UpsOutputGroupPower_Type = NonNegativeInteger
_UpsOutputGroupPower_Object = MibTableColumn
upsOutputGroupPower = _UpsOutputGroupPower_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1, 4),
    _UpsOutputGroupPower_Type()
)
upsOutputGroupPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupPower.setStatus("mandatory")
_UpsOutputGroupPercentLoad_Type = Integer32
_UpsOutputGroupPercentLoad_Object = MibTableColumn
upsOutputGroupPercentLoad = _UpsOutputGroupPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 4, 4, 1, 5),
    _UpsOutputGroupPercentLoad_Type()
)
upsOutputGroupPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputGroupPercentLoad.setStatus("mandatory")
_UpsBypassGroup_ObjectIdentity = ObjectIdentity
upsBypassGroup = _UpsBypassGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5)
)
_UpsBypassGroupFrequency_Type = Integer32
_UpsBypassGroupFrequency_Object = MibScalar
upsBypassGroupFrequency = _UpsBypassGroupFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 1),
    _UpsBypassGroupFrequency_Type()
)
upsBypassGroupFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupFrequency.setStatus("mandatory")
_UpsBypassGroupNumLines_Type = Integer32
_UpsBypassGroupNumLines_Object = MibScalar
upsBypassGroupNumLines = _UpsBypassGroupNumLines_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 2),
    _UpsBypassGroupNumLines_Type()
)
upsBypassGroupNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupNumLines.setStatus("mandatory")
_UpsBypassGroupTable_Object = MibTable
upsBypassGroupTable = _UpsBypassGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassGroupTable.setStatus("mandatory")
_UpsBypassGroupEntry_Object = MibTableRow
upsBypassGroupEntry = _UpsBypassGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3, 1)
)
upsBypassGroupEntry.setIndexNames(
    (0, "USHA-MIB", "upsBypassGroupLineIndex"),
)
if mibBuilder.loadTexts:
    upsBypassGroupEntry.setStatus("mandatory")


class _UpsBypassGroupLineIndex_Type(PositiveInteger):
    """Custom type upsBypassGroupLineIndex based on PositiveInteger"""
    subtypeSpec = PositiveInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsBypassGroupLineIndex_Type.__name__ = "PositiveInteger"
_UpsBypassGroupLineIndex_Object = MibTableColumn
upsBypassGroupLineIndex = _UpsBypassGroupLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3, 1, 1),
    _UpsBypassGroupLineIndex_Type()
)
upsBypassGroupLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupLineIndex.setStatus("mandatory")
_UpsBypassGroupVoltage_Type = NonNegativeInteger
_UpsBypassGroupVoltage_Object = MibTableColumn
upsBypassGroupVoltage = _UpsBypassGroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3, 1, 2),
    _UpsBypassGroupVoltage_Type()
)
upsBypassGroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupVoltage.setStatus("mandatory")
_UpsBypassGroupCurrent_Type = NonNegativeInteger
_UpsBypassGroupCurrent_Object = MibTableColumn
upsBypassGroupCurrent = _UpsBypassGroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3, 1, 3),
    _UpsBypassGroupCurrent_Type()
)
upsBypassGroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupCurrent.setStatus("mandatory")
_UpsBypassGroupPower_Type = NonNegativeInteger
_UpsBypassGroupPower_Object = MibTableColumn
upsBypassGroupPower = _UpsBypassGroupPower_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 5, 3, 1, 4),
    _UpsBypassGroupPower_Type()
)
upsBypassGroupPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassGroupPower.setStatus("mandatory")
_UpsTestGroup_ObjectIdentity = ObjectIdentity
upsTestGroup = _UpsTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6)
)
_UpsTestBatteryTestSettingTime_Type = Integer32
_UpsTestBatteryTestSettingTime_Object = MibScalar
upsTestBatteryTestSettingTime = _UpsTestBatteryTestSettingTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 1),
    _UpsTestBatteryTestSettingTime_Type()
)
upsTestBatteryTestSettingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestBatteryTestSettingTime.setStatus("mandatory")


class _UpsBatteryTest_Type(Integer32):
    """Custom type upsBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("battTest10sec", 2),
          ("battTestCancelTest", 5),
          ("battTestClearInfo", 6),
          ("battTestUntilLow", 3),
          ("battTestWithTime", 4),
          ("none", 1))
    )


_UpsBatteryTest_Type.__name__ = "Integer32"
_UpsBatteryTest_Object = MibScalar
upsBatteryTest = _UpsBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 2),
    _UpsBatteryTest_Type()
)
upsBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTest.setStatus("mandatory")


class _UpsTestBatteryTestResult_Type(Integer32):
    """Custom type upsTestBatteryTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("doneError", 3),
          ("donePassed", 1),
          ("doneWarning", 2),
          ("inProgress", 5),
          ("noTestsInitiated", 6))
    )


_UpsTestBatteryTestResult_Type.__name__ = "Integer32"
_UpsTestBatteryTestResult_Object = MibScalar
upsTestBatteryTestResult = _UpsTestBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 3),
    _UpsTestBatteryTestResult_Type()
)
upsTestBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestBatteryTestResult.setStatus("mandatory")


class _UpsTestBatteryTestStartTime_Type(DisplayString):
    """Custom type upsTestBatteryTestStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_UpsTestBatteryTestStartTime_Type.__name__ = "DisplayString"
_UpsTestBatteryTestStartTime_Object = MibScalar
upsTestBatteryTestStartTime = _UpsTestBatteryTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 4),
    _UpsTestBatteryTestStartTime_Type()
)
upsTestBatteryTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestBatteryTestStartTime.setStatus("mandatory")


class _UpsTestBatteryTestElapsedTime_Type(DisplayString):
    """Custom type upsTestBatteryTestElapsedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_UpsTestBatteryTestElapsedTime_Type.__name__ = "DisplayString"
_UpsTestBatteryTestElapsedTime_Object = MibScalar
upsTestBatteryTestElapsedTime = _UpsTestBatteryTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 5),
    _UpsTestBatteryTestElapsedTime_Type()
)
upsTestBatteryTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestBatteryTestElapsedTime.setStatus("mandatory")
_UpsBatteryTestScheduleTable_Object = MibTable
upsBatteryTestScheduleTable = _UpsBatteryTestScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    upsBatteryTestScheduleTable.setStatus("mandatory")
_UpsBatteryTestScheduleEntry_Object = MibTableRow
upsBatteryTestScheduleEntry = _UpsBatteryTestScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1)
)
upsBatteryTestScheduleEntry.setIndexNames(
    (0, "USHA-MIB", "upsBatteryTestScheduleIndex"),
)
if mibBuilder.loadTexts:
    upsBatteryTestScheduleEntry.setStatus("mandatory")


class _UpsBatteryTestScheduleIndex_Type(Integer32):
    """Custom type upsBatteryTestScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsBatteryTestScheduleIndex_Type.__name__ = "Integer32"
_UpsBatteryTestScheduleIndex_Object = MibTableColumn
upsBatteryTestScheduleIndex = _UpsBatteryTestScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 1),
    _UpsBatteryTestScheduleIndex_Type()
)
upsBatteryTestScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleIndex.setStatus("mandatory")


class _UpsBatteryTestScheduleDay_Type(Integer32):
    """Custom type upsBatteryTestScheduleDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 9),
          ("saturday", 7),
          ("specialDay", 8),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsBatteryTestScheduleDay_Type.__name__ = "Integer32"
_UpsBatteryTestScheduleDay_Object = MibTableColumn
upsBatteryTestScheduleDay = _UpsBatteryTestScheduleDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 2),
    _UpsBatteryTestScheduleDay_Type()
)
upsBatteryTestScheduleDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleDay.setStatus("mandatory")


class _UpsBatteryTestScheduleTime_Type(DisplayString):
    """Custom type upsBatteryTestScheduleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsBatteryTestScheduleTime_Type.__name__ = "DisplayString"
_UpsBatteryTestScheduleTime_Object = MibTableColumn
upsBatteryTestScheduleTime = _UpsBatteryTestScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 3),
    _UpsBatteryTestScheduleTime_Type()
)
upsBatteryTestScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleTime.setStatus("mandatory")


class _UpsBatteryTestScheduleType_Type(Integer32):
    """Custom type upsBatteryTestScheduleType based on Integer32"""
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
        *(("battTest10sec", 2),
          ("battTestUntilLow", 3),
          ("battTestWithTime", 4),
          ("none", 1))
    )


_UpsBatteryTestScheduleType_Type.__name__ = "Integer32"
_UpsBatteryTestScheduleType_Object = MibTableColumn
upsBatteryTestScheduleType = _UpsBatteryTestScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 4),
    _UpsBatteryTestScheduleType_Type()
)
upsBatteryTestScheduleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleType.setStatus("mandatory")


class _UpsBatteryTestScheduleTestWithTime_Type(Integer32):
    """Custom type upsBatteryTestScheduleTestWithTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 2),
          ("supported", 1))
    )


_UpsBatteryTestScheduleTestWithTime_Type.__name__ = "Integer32"
_UpsBatteryTestScheduleTestWithTime_Object = MibTableColumn
upsBatteryTestScheduleTestWithTime = _UpsBatteryTestScheduleTestWithTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 5),
    _UpsBatteryTestScheduleTestWithTime_Type()
)
upsBatteryTestScheduleTestWithTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleTestWithTime.setStatus("mandatory")


class _UpsBatteryTestScheduleSpecialDay_Type(DisplayString):
    """Custom type upsBatteryTestScheduleSpecialDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsBatteryTestScheduleSpecialDay_Type.__name__ = "DisplayString"
_UpsBatteryTestScheduleSpecialDay_Object = MibTableColumn
upsBatteryTestScheduleSpecialDay = _UpsBatteryTestScheduleSpecialDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 6, 6, 1, 6),
    _UpsBatteryTestScheduleSpecialDay_Type()
)
upsBatteryTestScheduleSpecialDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsBatteryTestScheduleSpecialDay.setStatus("mandatory")
_UpsControlGroup_ObjectIdentity = ObjectIdentity
upsControlGroup = _UpsControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7)
)
_UpsControlUpsShutdownDelay_Type = Integer32
_UpsControlUpsShutdownDelay_Object = MibScalar
upsControlUpsShutdownDelay = _UpsControlUpsShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 1),
    _UpsControlUpsShutdownDelay_Type()
)
upsControlUpsShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlUpsShutdownDelay.setStatus("mandatory")
_UpsControlUpsSleepTime_Type = Integer32
_UpsControlUpsSleepTime_Object = MibScalar
upsControlUpsSleepTime = _UpsControlUpsSleepTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 2),
    _UpsControlUpsSleepTime_Type()
)
upsControlUpsSleepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlUpsSleepTime.setStatus("mandatory")


class _UpsControlUpsOnOffControl_Type(Integer32):
    """Custom type upsControlUpsOnOffControl based on Integer32"""
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
        *(("none", 4),
          ("putUpsToSleep", 2),
          ("turnOnUpsOrCancelShutdown", 3),
          ("turnUpsOff", 1))
    )


_UpsControlUpsOnOffControl_Type.__name__ = "Integer32"
_UpsControlUpsOnOffControl_Object = MibScalar
upsControlUpsOnOffControl = _UpsControlUpsOnOffControl_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 3),
    _UpsControlUpsOnOffControl_Type()
)
upsControlUpsOnOffControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlUpsOnOffControl.setStatus("mandatory")
_UpsControlShutdownParametersTable_Object = MibTable
upsControlShutdownParametersTable = _UpsControlShutdownParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4)
)
if mibBuilder.loadTexts:
    upsControlShutdownParametersTable.setStatus("mandatory")
_UpsControlShutdownParametersEntry_Object = MibTableRow
upsControlShutdownParametersEntry = _UpsControlShutdownParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1)
)
upsControlShutdownParametersEntry.setIndexNames(
    (0, "USHA-MIB", "upsControlEvent"),
)
if mibBuilder.loadTexts:
    upsControlShutdownParametersEntry.setStatus("mandatory")


class _UpsControlEvent_Type(Integer32):
    """Custom type upsControlEvent based on Integer32"""
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
        *(("acFail", 1),
          ("batteryLow", 2),
          ("emdAlarm1", 8),
          ("emdAlarm2", 9),
          ("emdTemperatureOverThreshold", 7),
          ("specialDaySchedule", 6),
          ("upsOverTempeature", 4),
          ("upsOverload", 3),
          ("weeklySchedule", 5))
    )


_UpsControlEvent_Type.__name__ = "Integer32"
_UpsControlEvent_Object = MibTableColumn
upsControlEvent = _UpsControlEvent_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1, 1),
    _UpsControlEvent_Type()
)
upsControlEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlEvent.setStatus("mandatory")


class _UpsControlEventStatus_Type(Integer32):
    """Custom type upsControlEventStatus based on Integer32"""
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
        *(("clientShutdown", 3),
          ("disable", 1),
          ("upsTurnOff", 4),
          ("warning", 2))
    )


_UpsControlEventStatus_Type.__name__ = "Integer32"
_UpsControlEventStatus_Object = MibTableColumn
upsControlEventStatus = _UpsControlEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1, 2),
    _UpsControlEventStatus_Type()
)
upsControlEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlEventStatus.setStatus("mandatory")


class _UpsControlDelay_Type(Integer32):
    """Custom type upsControlDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_UpsControlDelay_Type.__name__ = "Integer32"
_UpsControlDelay_Object = MibTableColumn
upsControlDelay = _UpsControlDelay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1, 3),
    _UpsControlDelay_Type()
)
upsControlDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlDelay.setStatus("mandatory")


class _UpsControlFirstWarning_Type(Integer32):
    """Custom type upsControlFirstWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_UpsControlFirstWarning_Type.__name__ = "Integer32"
_UpsControlFirstWarning_Object = MibTableColumn
upsControlFirstWarning = _UpsControlFirstWarning_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1, 4),
    _UpsControlFirstWarning_Type()
)
upsControlFirstWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlFirstWarning.setStatus("mandatory")


class _UpsControlWarningInterval_Type(Integer32):
    """Custom type upsControlWarningInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_UpsControlWarningInterval_Type.__name__ = "Integer32"
_UpsControlWarningInterval_Object = MibTableColumn
upsControlWarningInterval = _UpsControlWarningInterval_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 4, 1, 5),
    _UpsControlWarningInterval_Type()
)
upsControlWarningInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWarningInterval.setStatus("mandatory")
_UpsControlWeeklyScheduleTable_Object = MibTable
upsControlWeeklyScheduleTable = _UpsControlWeeklyScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5)
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleTable.setStatus("mandatory")
_UpsControlWeeklyScheduleEntry_Object = MibTableRow
upsControlWeeklyScheduleEntry = _UpsControlWeeklyScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1)
)
upsControlWeeklyScheduleEntry.setIndexNames(
    (0, "USHA-MIB", "upsControlWeeklyIndex"),
)
if mibBuilder.loadTexts:
    upsControlWeeklyScheduleEntry.setStatus("mandatory")


class _UpsControlWeeklyIndex_Type(Integer32):
    """Custom type upsControlWeeklyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsControlWeeklyIndex_Type.__name__ = "Integer32"
_UpsControlWeeklyIndex_Object = MibTableColumn
upsControlWeeklyIndex = _UpsControlWeeklyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1, 1),
    _UpsControlWeeklyIndex_Type()
)
upsControlWeeklyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlWeeklyIndex.setStatus("mandatory")


class _UpsControlWeeklyShutdownDay_Type(Integer32):
    """Custom type upsControlWeeklyShutdownDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlWeeklyShutdownDay_Type.__name__ = "Integer32"
_UpsControlWeeklyShutdownDay_Object = MibTableColumn
upsControlWeeklyShutdownDay = _UpsControlWeeklyShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1, 2),
    _UpsControlWeeklyShutdownDay_Type()
)
upsControlWeeklyShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownDay.setStatus("mandatory")


class _UpsControlWeeklyShutdownTime_Type(DisplayString):
    """Custom type upsControlWeeklyShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlWeeklyShutdownTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyShutdownTime_Object = MibTableColumn
upsControlWeeklyShutdownTime = _UpsControlWeeklyShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1, 3),
    _UpsControlWeeklyShutdownTime_Type()
)
upsControlWeeklyShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyShutdownTime.setStatus("mandatory")


class _UpsControlWeeklyRestartDay_Type(Integer32):
    """Custom type upsControlWeeklyRestartDay based on Integer32"""
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
        *(("friday", 6),
          ("monday", 2),
          ("none", 8),
          ("saturday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsControlWeeklyRestartDay_Type.__name__ = "Integer32"
_UpsControlWeeklyRestartDay_Object = MibTableColumn
upsControlWeeklyRestartDay = _UpsControlWeeklyRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1, 4),
    _UpsControlWeeklyRestartDay_Type()
)
upsControlWeeklyRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartDay.setStatus("mandatory")


class _UpsControlWeeklyRestartTime_Type(DisplayString):
    """Custom type upsControlWeeklyRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlWeeklyRestartTime_Type.__name__ = "DisplayString"
_UpsControlWeeklyRestartTime_Object = MibTableColumn
upsControlWeeklyRestartTime = _UpsControlWeeklyRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 5, 1, 5),
    _UpsControlWeeklyRestartTime_Type()
)
upsControlWeeklyRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlWeeklyRestartTime.setStatus("mandatory")
_UpsControlSpecialScheduleTable_Object = MibTable
upsControlSpecialScheduleTable = _UpsControlSpecialScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6)
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleTable.setStatus("mandatory")
_UpsControlSpecialScheduleEntry_Object = MibTableRow
upsControlSpecialScheduleEntry = _UpsControlSpecialScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1)
)
upsControlSpecialScheduleEntry.setIndexNames(
    (0, "USHA-MIB", "upsControlSpecialIndex"),
)
if mibBuilder.loadTexts:
    upsControlSpecialScheduleEntry.setStatus("mandatory")


class _UpsControlSpecialIndex_Type(Integer32):
    """Custom type upsControlSpecialIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsControlSpecialIndex_Type.__name__ = "Integer32"
_UpsControlSpecialIndex_Object = MibTableColumn
upsControlSpecialIndex = _UpsControlSpecialIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1, 1),
    _UpsControlSpecialIndex_Type()
)
upsControlSpecialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsControlSpecialIndex.setStatus("mandatory")


class _UpsControlSpecialShutdownDay_Type(DisplayString):
    """Custom type upsControlSpecialShutdownDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsControlSpecialShutdownDay_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownDay_Object = MibTableColumn
upsControlSpecialShutdownDay = _UpsControlSpecialShutdownDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1, 2),
    _UpsControlSpecialShutdownDay_Type()
)
upsControlSpecialShutdownDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownDay.setStatus("mandatory")


class _UpsControlSpecialShutdownTime_Type(DisplayString):
    """Custom type upsControlSpecialShutdownTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlSpecialShutdownTime_Type.__name__ = "DisplayString"
_UpsControlSpecialShutdownTime_Object = MibTableColumn
upsControlSpecialShutdownTime = _UpsControlSpecialShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1, 3),
    _UpsControlSpecialShutdownTime_Type()
)
upsControlSpecialShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialShutdownTime.setStatus("mandatory")


class _UpsControlSpecialRestartDay_Type(DisplayString):
    """Custom type upsControlSpecialRestartDay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_UpsControlSpecialRestartDay_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartDay_Object = MibTableColumn
upsControlSpecialRestartDay = _UpsControlSpecialRestartDay_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1, 4),
    _UpsControlSpecialRestartDay_Type()
)
upsControlSpecialRestartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartDay.setStatus("mandatory")


class _UpsControlSpecialRestartTime_Type(DisplayString):
    """Custom type upsControlSpecialRestartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_UpsControlSpecialRestartTime_Type.__name__ = "DisplayString"
_UpsControlSpecialRestartTime_Object = MibTableColumn
upsControlSpecialRestartTime = _UpsControlSpecialRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 7, 6, 1, 5),
    _UpsControlSpecialRestartTime_Type()
)
upsControlSpecialRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlSpecialRestartTime.setStatus("mandatory")
_UpsConfigGroup_ObjectIdentity = ObjectIdentity
upsConfigGroup = _UpsConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8)
)
_UpsConfigGroupInputVoltage_Type = Integer32
_UpsConfigGroupInputVoltage_Object = MibScalar
upsConfigGroupInputVoltage = _UpsConfigGroupInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 1),
    _UpsConfigGroupInputVoltage_Type()
)
upsConfigGroupInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupInputVoltage.setStatus("mandatory")
_UpsConfigGroupInputFreq_Type = Integer32
_UpsConfigGroupInputFreq_Object = MibScalar
upsConfigGroupInputFreq = _UpsConfigGroupInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 2),
    _UpsConfigGroupInputFreq_Type()
)
upsConfigGroupInputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupInputFreq.setStatus("mandatory")
_UpsConfigGroupOutputVoltage_Type = Integer32
_UpsConfigGroupOutputVoltage_Object = MibScalar
upsConfigGroupOutputVoltage = _UpsConfigGroupOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 3),
    _UpsConfigGroupOutputVoltage_Type()
)
upsConfigGroupOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupOutputVoltage.setStatus("mandatory")
_UpsConfigGroupOutputFreq_Type = Integer32
_UpsConfigGroupOutputFreq_Object = MibScalar
upsConfigGroupOutputFreq = _UpsConfigGroupOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 4),
    _UpsConfigGroupOutputFreq_Type()
)
upsConfigGroupOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupOutputFreq.setStatus("mandatory")
_UpsConfigGroupOutputVA_Type = NonNegativeInteger
_UpsConfigGroupOutputVA_Object = MibScalar
upsConfigGroupOutputVA = _UpsConfigGroupOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 5),
    _UpsConfigGroupOutputVA_Type()
)
upsConfigGroupOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupOutputVA.setStatus("mandatory")
_UpsConfigGroupOutputPower_Type = NonNegativeInteger
_UpsConfigGroupOutputPower_Object = MibScalar
upsConfigGroupOutputPower = _UpsConfigGroupOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 6),
    _UpsConfigGroupOutputPower_Type()
)
upsConfigGroupOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigGroupOutputPower.setStatus("mandatory")


class _UpsConfigGroupOverTemperatureSetPoint_Type(NonNegativeInteger):
    """Custom type upsConfigGroupOverTemperatureSetPoint based on NonNegativeInteger"""
    subtypeSpec = NonNegativeInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 70),
    )


_UpsConfigGroupOverTemperatureSetPoint_Type.__name__ = "NonNegativeInteger"
_UpsConfigGroupOverTemperatureSetPoint_Object = MibScalar
upsConfigGroupOverTemperatureSetPoint = _UpsConfigGroupOverTemperatureSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 7),
    _UpsConfigGroupOverTemperatureSetPoint_Type()
)
upsConfigGroupOverTemperatureSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigGroupOverTemperatureSetPoint.setStatus("mandatory")


class _UpsConfigGroupOverLoadSetPoint_Type(NonNegativeInteger):
    """Custom type upsConfigGroupOverLoadSetPoint based on NonNegativeInteger"""
    subtypeSpec = NonNegativeInteger.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_UpsConfigGroupOverLoadSetPoint_Type.__name__ = "NonNegativeInteger"
_UpsConfigGroupOverLoadSetPoint_Object = MibScalar
upsConfigGroupOverLoadSetPoint = _UpsConfigGroupOverLoadSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 8, 8),
    _UpsConfigGroupOverLoadSetPoint_Type()
)
upsConfigGroupOverLoadSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigGroupOverLoadSetPoint.setStatus("mandatory")
_UpsClients_ObjectIdentity = ObjectIdentity
upsClients = _UpsClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9)
)
_UpsClientsConnectedNum_Type = NonNegativeInteger
_UpsClientsConnectedNum_Object = MibScalar
upsClientsConnectedNum = _UpsClientsConnectedNum_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 1),
    _UpsClientsConnectedNum_Type()
)
upsClientsConnectedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsClientsConnectedNum.setStatus("mandatory")
_UpsDevicesTable_Object = MibTable
upsDevicesTable = _UpsDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    upsDevicesTable.setStatus("mandatory")
_UpsDevicesEntry_Object = MibTableRow
upsDevicesEntry = _UpsDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1)
)
upsDevicesEntry.setIndexNames(
    (0, "USHA-MIB", "indexOfDevice"),
)
if mibBuilder.loadTexts:
    upsDevicesEntry.setStatus("mandatory")
_IndexOfDevice_Type = NonNegativeInteger
_IndexOfDevice_Object = MibTableColumn
indexOfDevice = _IndexOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 1),
    _IndexOfDevice_Type()
)
indexOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    indexOfDevice.setStatus("mandatory")
_AddrOfDevice_Type = IpAddress
_AddrOfDevice_Object = MibTableColumn
addrOfDevice = _AddrOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 2),
    _AddrOfDevice_Type()
)
addrOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    addrOfDevice.setStatus("mandatory")


class _NameOfDevice_Type(DisplayString):
    """Custom type nameOfDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_NameOfDevice_Type.__name__ = "DisplayString"
_NameOfDevice_Object = MibTableColumn
nameOfDevice = _NameOfDevice_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 3),
    _NameOfDevice_Type()
)
nameOfDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameOfDevice.setStatus("mandatory")
_TimeOfConnection_Type = DisplayString
_TimeOfConnection_Object = MibTableColumn
timeOfConnection = _TimeOfConnection_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 4),
    _TimeOfConnection_Type()
)
timeOfConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfConnection.setStatus("mandatory")
_TimeOfConnectionTime_Type = DisplayString
_TimeOfConnectionTime_Object = MibTableColumn
timeOfConnectionTime = _TimeOfConnectionTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 5),
    _TimeOfConnectionTime_Type()
)
timeOfConnectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfConnectionTime.setStatus("mandatory")
_TimeOfConnectionTimeout_Type = Integer32
_TimeOfConnectionTimeout_Object = MibTableColumn
timeOfConnectionTimeout = _TimeOfConnectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 9, 2, 1, 6),
    _TimeOfConnectionTimeout_Type()
)
timeOfConnectionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeOfConnectionTimeout.setStatus("mandatory")
_AgentConfig_ObjectIdentity = ObjectIdentity
agentConfig = _AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10)
)
_AgentConfigIpaddress_Type = IpAddress
_AgentConfigIpaddress_Object = MibScalar
agentConfigIpaddress = _AgentConfigIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 1),
    _AgentConfigIpaddress_Type()
)
agentConfigIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigIpaddress.setStatus("mandatory")
_AgentConfigGateway_Type = IpAddress
_AgentConfigGateway_Object = MibScalar
agentConfigGateway = _AgentConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 2),
    _AgentConfigGateway_Type()
)
agentConfigGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigGateway.setStatus("mandatory")
_AgentConfigSubnetMask_Type = IpAddress
_AgentConfigSubnetMask_Object = MibScalar
agentConfigSubnetMask = _AgentConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 3),
    _AgentConfigSubnetMask_Type()
)
agentConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigSubnetMask.setStatus("mandatory")


class _AgentConfigDate_Type(DisplayString):
    """Custom type agentConfigDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_AgentConfigDate_Type.__name__ = "DisplayString"
_AgentConfigDate_Object = MibScalar
agentConfigDate = _AgentConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 4),
    _AgentConfigDate_Type()
)
agentConfigDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDate.setStatus("mandatory")


class _AgentConfigTime_Type(DisplayString):
    """Custom type agentConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_AgentConfigTime_Type.__name__ = "DisplayString"
_AgentConfigTime_Object = MibScalar
agentConfigTime = _AgentConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 5),
    _AgentConfigTime_Type()
)
agentConfigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTime.setStatus("mandatory")
_AgentConfigPrimaryTimeServer_Type = IpAddress
_AgentConfigPrimaryTimeServer_Object = MibScalar
agentConfigPrimaryTimeServer = _AgentConfigPrimaryTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 6),
    _AgentConfigPrimaryTimeServer_Type()
)
agentConfigPrimaryTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigPrimaryTimeServer.setStatus("mandatory")
_AgentConfigSecondaryTimeServer_Type = IpAddress
_AgentConfigSecondaryTimeServer_Object = MibScalar
agentConfigSecondaryTimeServer = _AgentConfigSecondaryTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 7),
    _AgentConfigSecondaryTimeServer_Type()
)
agentConfigSecondaryTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigSecondaryTimeServer.setStatus("mandatory")


class _AgentConfigHistoryLogFrequency_Type(Integer32):
    """Custom type agentConfigHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 28800),
    )


_AgentConfigHistoryLogFrequency_Type.__name__ = "Integer32"
_AgentConfigHistoryLogFrequency_Object = MibScalar
agentConfigHistoryLogFrequency = _AgentConfigHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 8),
    _AgentConfigHistoryLogFrequency_Type()
)
agentConfigHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigHistoryLogFrequency.setStatus("mandatory")


class _AgentConfigExtHistoryLogFrequency_Type(Integer32):
    """Custom type agentConfigExtHistoryLogFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10080),
    )


_AgentConfigExtHistoryLogFrequency_Type.__name__ = "Integer32"
_AgentConfigExtHistoryLogFrequency_Object = MibScalar
agentConfigExtHistoryLogFrequency = _AgentConfigExtHistoryLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 9),
    _AgentConfigExtHistoryLogFrequency_Type()
)
agentConfigExtHistoryLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigExtHistoryLogFrequency.setStatus("mandatory")


class _AgentConfigPollRate_Type(Integer32):
    """Custom type agentConfigPollRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_AgentConfigPollRate_Type.__name__ = "Integer32"
_AgentConfigPollRate_Object = MibScalar
agentConfigPollRate = _AgentConfigPollRate_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 10),
    _AgentConfigPollRate_Type()
)
agentConfigPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigPollRate.setStatus("mandatory")
_AgentConfigBaudRate_Type = Integer32
_AgentConfigBaudRate_Object = MibScalar
agentConfigBaudRate = _AgentConfigBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 11),
    _AgentConfigBaudRate_Type()
)
agentConfigBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigBaudRate.setStatus("mandatory")


class _AgentConfigDhcpStatue_Type(Integer32):
    """Custom type agentConfigDhcpStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AgentConfigDhcpStatue_Type.__name__ = "Integer32"
_AgentConfigDhcpStatue_Object = MibScalar
agentConfigDhcpStatue = _AgentConfigDhcpStatue_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 12),
    _AgentConfigDhcpStatue_Type()
)
agentConfigDhcpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDhcpStatue.setStatus("mandatory")


class _AgentConfigTelnetStatue_Type(Integer32):
    """Custom type agentConfigTelnetStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AgentConfigTelnetStatue_Type.__name__ = "Integer32"
_AgentConfigTelnetStatue_Object = MibScalar
agentConfigTelnetStatue = _AgentConfigTelnetStatue_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 13),
    _AgentConfigTelnetStatue_Type()
)
agentConfigTelnetStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTelnetStatue.setStatus("mandatory")


class _AgentConfigTftpStatue_Type(Integer32):
    """Custom type agentConfigTftpStatue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AgentConfigTftpStatue_Type.__name__ = "Integer32"
_AgentConfigTftpStatue_Object = MibScalar
agentConfigTftpStatue = _AgentConfigTftpStatue_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 14),
    _AgentConfigTftpStatue_Type()
)
agentConfigTftpStatue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTftpStatue.setStatus("mandatory")


class _AgentConfigResetToDefault_Type(Integer32):
    """Custom type agentConfigResetToDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("reset", 1))
    )


_AgentConfigResetToDefault_Type.__name__ = "Integer32"
_AgentConfigResetToDefault_Object = MibScalar
agentConfigResetToDefault = _AgentConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 15),
    _AgentConfigResetToDefault_Type()
)
agentConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigResetToDefault.setStatus("mandatory")


class _AgentConfigRestart_Type(Integer32):
    """Custom type agentConfigRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 2),
          ("restart", 1))
    )


_AgentConfigRestart_Type.__name__ = "Integer32"
_AgentConfigRestart_Object = MibScalar
agentConfigRestart = _AgentConfigRestart_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 16),
    _AgentConfigRestart_Type()
)
agentConfigRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigRestart.setStatus("mandatory")


class _AgentConfigClearAgentLog_Type(Integer32):
    """Custom type agentConfigClearAgentLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearAgentLog_Type.__name__ = "Integer32"
_AgentConfigClearAgentLog_Object = MibScalar
agentConfigClearAgentLog = _AgentConfigClearAgentLog_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 17),
    _AgentConfigClearAgentLog_Type()
)
agentConfigClearAgentLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearAgentLog.setStatus("mandatory")


class _AgentConfigClearEventLog_Type(Integer32):
    """Custom type agentConfigClearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearEventLog_Type.__name__ = "Integer32"
_AgentConfigClearEventLog_Object = MibScalar
agentConfigClearEventLog = _AgentConfigClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 18),
    _AgentConfigClearEventLog_Type()
)
agentConfigClearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearEventLog.setStatus("mandatory")


class _AgentConfigClearExtHistoryLog_Type(Integer32):
    """Custom type agentConfigClearExtHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearExtHistoryLog_Type.__name__ = "Integer32"
_AgentConfigClearExtHistoryLog_Object = MibScalar
agentConfigClearExtHistoryLog = _AgentConfigClearExtHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 19),
    _AgentConfigClearExtHistoryLog_Type()
)
agentConfigClearExtHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearExtHistoryLog.setStatus("mandatory")


class _AgentConfigClearHistoryLog_Type(Integer32):
    """Custom type agentConfigClearHistoryLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("nothing", 2))
    )


_AgentConfigClearHistoryLog_Type.__name__ = "Integer32"
_AgentConfigClearHistoryLog_Object = MibScalar
agentConfigClearHistoryLog = _AgentConfigClearHistoryLog_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 20),
    _AgentConfigClearHistoryLog_Type()
)
agentConfigClearHistoryLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigClearHistoryLog.setStatus("mandatory")
_AgentConfigTrapRetryCount_Type = Integer32
_AgentConfigTrapRetryCount_Object = MibScalar
agentConfigTrapRetryCount = _AgentConfigTrapRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 21),
    _AgentConfigTrapRetryCount_Type()
)
agentConfigTrapRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapRetryCount.setStatus("mandatory")
_AgentConfigTrapRetryTime_Type = Integer32
_AgentConfigTrapRetryTime_Object = MibScalar
agentConfigTrapRetryTime = _AgentConfigTrapRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 22),
    _AgentConfigTrapRetryTime_Type()
)
agentConfigTrapRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapRetryTime.setStatus("mandatory")
_AgentConfigTrapAckSignature_Type = Integer32
_AgentConfigTrapAckSignature_Object = MibScalar
agentConfigTrapAckSignature = _AgentConfigTrapAckSignature_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 23),
    _AgentConfigTrapAckSignature_Type()
)
agentConfigTrapAckSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigTrapAckSignature.setStatus("mandatory")
_AgentConfigMibVersion_Type = Integer32
_AgentConfigMibVersion_Object = MibScalar
agentConfigMibVersion = _AgentConfigMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 24),
    _AgentConfigMibVersion_Type()
)
agentConfigMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentConfigMibVersion.setStatus("mandatory")
_AgentConfigTrapsReceiversTable_Object = MibTable
agentConfigTrapsReceiversTable = _AgentConfigTrapsReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25)
)
if mibBuilder.loadTexts:
    agentConfigTrapsReceiversTable.setStatus("mandatory")
_AgentConfigTrapsReceiversEntry_Object = MibTableRow
agentConfigTrapsReceiversEntry = _AgentConfigTrapsReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1)
)
agentConfigTrapsReceiversEntry.setIndexNames(
    (0, "USHA-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    agentConfigTrapsReceiversEntry.setStatus("mandatory")


class _TrapsIndex_Type(Integer32):
    """Custom type trapsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrapsIndex_Type.__name__ = "Integer32"
_TrapsIndex_Object = MibTableColumn
trapsIndex = _TrapsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 1),
    _TrapsIndex_Type()
)
trapsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsIndex.setStatus("mandatory")
_TrapsReceiverAddr_Type = IpAddress
_TrapsReceiverAddr_Object = MibTableColumn
trapsReceiverAddr = _TrapsReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 2),
    _TrapsReceiverAddr_Type()
)
trapsReceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsReceiverAddr.setStatus("mandatory")


class _ReceiverCommunityString_Type(DisplayString):
    """Custom type receiverCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ReceiverCommunityString_Type.__name__ = "DisplayString"
_ReceiverCommunityString_Object = MibTableColumn
receiverCommunityString = _ReceiverCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 3),
    _ReceiverCommunityString_Type()
)
receiverCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverCommunityString.setStatus("mandatory")


class _ReceiverNmsType_Type(Integer32):
    """Custom type receiverNmsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rfc1628-trap", 2),
          ("usha-trap", 3))
    )


_ReceiverNmsType_Type.__name__ = "Integer32"
_ReceiverNmsType_Object = MibTableColumn
receiverNmsType = _ReceiverNmsType_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 4),
    _ReceiverNmsType_Type()
)
receiverNmsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverNmsType.setStatus("mandatory")


class _ReceiverSeverityLevel_Type(Integer32):
    """Custom type receiverSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("informational", 1),
          ("severe", 3),
          ("warning", 2))
    )


_ReceiverSeverityLevel_Type.__name__ = "Integer32"
_ReceiverSeverityLevel_Object = MibTableColumn
receiverSeverityLevel = _ReceiverSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 5),
    _ReceiverSeverityLevel_Type()
)
receiverSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverSeverityLevel.setStatus("mandatory")


class _ReceiverDescription_Type(DisplayString):
    """Custom type receiverDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ReceiverDescription_Type.__name__ = "DisplayString"
_ReceiverDescription_Object = MibTableColumn
receiverDescription = _ReceiverDescription_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 25, 1, 6),
    _ReceiverDescription_Type()
)
receiverDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    receiverDescription.setStatus("mandatory")
_AgentConfigAccessControlTable_Object = MibTable
agentConfigAccessControlTable = _AgentConfigAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26)
)
if mibBuilder.loadTexts:
    agentConfigAccessControlTable.setStatus("mandatory")
_AgentConfigAccessControlEntry_Object = MibTableRow
agentConfigAccessControlEntry = _AgentConfigAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26, 1)
)
agentConfigAccessControlEntry.setIndexNames(
    (0, "USHA-MIB", "trapsIndex"),
)
if mibBuilder.loadTexts:
    agentConfigAccessControlEntry.setStatus("mandatory")
_AccessIndex_Type = Integer32
_AccessIndex_Object = MibTableColumn
accessIndex = _AccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26, 1, 1),
    _AccessIndex_Type()
)
accessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessIndex.setStatus("mandatory")
_AccessControlAddr_Type = IpAddress
_AccessControlAddr_Object = MibTableColumn
accessControlAddr = _AccessControlAddr_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26, 1, 2),
    _AccessControlAddr_Type()
)
accessControlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlAddr.setStatus("mandatory")


class _AccessCommunityString_Type(DisplayString):
    """Custom type accessCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_AccessCommunityString_Type.__name__ = "DisplayString"
_AccessCommunityString_Object = MibTableColumn
accessCommunityString = _AccessCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26, 1, 3),
    _AccessCommunityString_Type()
)
accessCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCommunityString.setStatus("mandatory")


class _AccessControlMode_Type(Integer32):
    """Custom type accessControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAccess", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_AccessControlMode_Type.__name__ = "Integer32"
_AccessControlMode_Object = MibTableColumn
accessControlMode = _AccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 26, 1, 4),
    _AccessControlMode_Type()
)
accessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessControlMode.setStatus("mandatory")


class _AgentConfigDefaultLanguage_Type(Integer32):
    """Custom type agentConfigDefaultLanguage based on Integer32"""
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
        *(("auto", 1),
          ("english", 2),
          ("simplifiedChinese", 4),
          ("traditionalChinese", 3))
    )


_AgentConfigDefaultLanguage_Type.__name__ = "Integer32"
_AgentConfigDefaultLanguage_Object = MibScalar
agentConfigDefaultLanguage = _AgentConfigDefaultLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 10, 27),
    _AgentConfigDefaultLanguage_Type()
)
agentConfigDefaultLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDefaultLanguage.setStatus("mandatory")
_EmdStatus_ObjectIdentity = ObjectIdentity
emdStatus = _EmdStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11)
)


class _EmdSatatusEmdType_Type(Integer32):
    """Custom type emdSatatusEmdType based on Integer32"""
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
        *(("disabled", 2),
          ("emdHT", 3),
          ("emdT", 4),
          ("unknown", 1))
    )


_EmdSatatusEmdType_Type.__name__ = "Integer32"
_EmdSatatusEmdType_Object = MibScalar
emdSatatusEmdType = _EmdSatatusEmdType_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11, 1),
    _EmdSatatusEmdType_Type()
)
emdSatatusEmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusEmdType.setStatus("mandatory")
_EmdSatatusTemperature_Type = Integer32
_EmdSatatusTemperature_Object = MibScalar
emdSatatusTemperature = _EmdSatatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11, 2),
    _EmdSatatusTemperature_Type()
)
emdSatatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusTemperature.setStatus("mandatory")
_EmdSatatusHumidity_Type = Integer32
_EmdSatatusHumidity_Object = MibScalar
emdSatatusHumidity = _EmdSatatusHumidity_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11, 3),
    _EmdSatatusHumidity_Type()
)
emdSatatusHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusHumidity.setStatus("mandatory")


class _EmdSatatusAlarm1_Type(Integer32):
    """Custom type emdSatatusAlarm1 based on Integer32"""
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
        *(("active", 3),
          ("disabled", 2),
          ("inactive", 4),
          ("unknow", 1))
    )


_EmdSatatusAlarm1_Type.__name__ = "Integer32"
_EmdSatatusAlarm1_Object = MibScalar
emdSatatusAlarm1 = _EmdSatatusAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11, 4),
    _EmdSatatusAlarm1_Type()
)
emdSatatusAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusAlarm1.setStatus("mandatory")


class _EmdSatatusAlarm2_Type(Integer32):
    """Custom type emdSatatusAlarm2 based on Integer32"""
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
        *(("active", 3),
          ("disabled", 2),
          ("inactive", 4),
          ("unknow", 1))
    )


_EmdSatatusAlarm2_Type.__name__ = "Integer32"
_EmdSatatusAlarm2_Object = MibScalar
emdSatatusAlarm2 = _EmdSatatusAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 11, 5),
    _EmdSatatusAlarm2_Type()
)
emdSatatusAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emdSatatusAlarm2.setStatus("mandatory")
_EmdConfig_ObjectIdentity = ObjectIdentity
emdConfig = _EmdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12)
)


class _UsahEmdConfigEmdConfig_Type(Integer32):
    """Custom type usahEmdConfigEmdConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disabled", 1))
    )


_UsahEmdConfigEmdConfig_Type.__name__ = "Integer32"
_UsahEmdConfigEmdConfig_Object = MibScalar
usahEmdConfigEmdConfig = _UsahEmdConfigEmdConfig_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 1),
    _UsahEmdConfigEmdConfig_Type()
)
usahEmdConfigEmdConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usahEmdConfigEmdConfig.setStatus("mandatory")


class _EmdConfigEmdName_Type(DisplayString):
    """Custom type emdConfigEmdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigEmdName_Type.__name__ = "DisplayString"
_EmdConfigEmdName_Object = MibScalar
emdConfigEmdName = _EmdConfigEmdName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 2),
    _EmdConfigEmdName_Type()
)
emdConfigEmdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigEmdName.setStatus("mandatory")
_EmdConfigTemperature_ObjectIdentity = ObjectIdentity
emdConfigTemperature = _EmdConfigTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3)
)


class _EmdConfigTempName_Type(DisplayString):
    """Custom type emdConfigTempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigTempName_Type.__name__ = "DisplayString"
_EmdConfigTempName_Object = MibScalar
emdConfigTempName = _EmdConfigTempName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 1),
    _EmdConfigTempName_Type()
)
emdConfigTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempName.setStatus("mandatory")
_EmdConfigTempHighSetPoint_Type = Integer32
_EmdConfigTempHighSetPoint_Object = MibScalar
emdConfigTempHighSetPoint = _EmdConfigTempHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 2),
    _EmdConfigTempHighSetPoint_Type()
)
emdConfigTempHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempHighSetPoint.setStatus("mandatory")


class _EmdConfigTempHighStatus_Type(Integer32):
    """Custom type emdConfigTempHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EmdConfigTempHighStatus_Type.__name__ = "Integer32"
_EmdConfigTempHighStatus_Object = MibScalar
emdConfigTempHighStatus = _EmdConfigTempHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 3),
    _EmdConfigTempHighStatus_Type()
)
emdConfigTempHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempHighStatus.setStatus("mandatory")
_EmdConfigTempLowSetPoint_Type = Integer32
_EmdConfigTempLowSetPoint_Object = MibScalar
emdConfigTempLowSetPoint = _EmdConfigTempLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 4),
    _EmdConfigTempLowSetPoint_Type()
)
emdConfigTempLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempLowSetPoint.setStatus("mandatory")


class _EmdConfigTempLowStatus_Type(Integer32):
    """Custom type emdConfigTempLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EmdConfigTempLowStatus_Type.__name__ = "Integer32"
_EmdConfigTempLowStatus_Object = MibScalar
emdConfigTempLowStatus = _EmdConfigTempLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 5),
    _EmdConfigTempLowStatus_Type()
)
emdConfigTempLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempLowStatus.setStatus("mandatory")
_EmdConfigTempOffset_Type = Integer32
_EmdConfigTempOffset_Object = MibScalar
emdConfigTempOffset = _EmdConfigTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 3, 6),
    _EmdConfigTempOffset_Type()
)
emdConfigTempOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigTempOffset.setStatus("mandatory")
_EmdConfigHumidity_ObjectIdentity = ObjectIdentity
emdConfigHumidity = _EmdConfigHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4)
)


class _EmdConfigHumidityName_Type(DisplayString):
    """Custom type emdConfigHumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigHumidityName_Type.__name__ = "DisplayString"
_EmdConfigHumidityName_Object = MibScalar
emdConfigHumidityName = _EmdConfigHumidityName_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 1),
    _EmdConfigHumidityName_Type()
)
emdConfigHumidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityName.setStatus("mandatory")
_EmdConfigHumidityHighSetPoint_Type = Integer32
_EmdConfigHumidityHighSetPoint_Object = MibScalar
emdConfigHumidityHighSetPoint = _EmdConfigHumidityHighSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 2),
    _EmdConfigHumidityHighSetPoint_Type()
)
emdConfigHumidityHighSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityHighSetPoint.setStatus("mandatory")


class _EmdConfigHumidityLowStatus_Type(Integer32):
    """Custom type emdConfigHumidityLowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EmdConfigHumidityLowStatus_Type.__name__ = "Integer32"
_EmdConfigHumidityLowStatus_Object = MibScalar
emdConfigHumidityLowStatus = _EmdConfigHumidityLowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 3),
    _EmdConfigHumidityLowStatus_Type()
)
emdConfigHumidityLowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityLowStatus.setStatus("mandatory")
_EmdConfigHumidityLowSetPoint_Type = Integer32
_EmdConfigHumidityLowSetPoint_Object = MibScalar
emdConfigHumidityLowSetPoint = _EmdConfigHumidityLowSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 4),
    _EmdConfigHumidityLowSetPoint_Type()
)
emdConfigHumidityLowSetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityLowSetPoint.setStatus("mandatory")


class _EmdConfigHumidityHighStatus_Type(Integer32):
    """Custom type emdConfigHumidityHighStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EmdConfigHumidityHighStatus_Type.__name__ = "Integer32"
_EmdConfigHumidityHighStatus_Object = MibScalar
emdConfigHumidityHighStatus = _EmdConfigHumidityHighStatus_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 5),
    _EmdConfigHumidityHighStatus_Type()
)
emdConfigHumidityHighStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityHighStatus.setStatus("mandatory")
_EmdConfigHumidityOffset_Type = Integer32
_EmdConfigHumidityOffset_Object = MibScalar
emdConfigHumidityOffset = _EmdConfigHumidityOffset_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 4, 6),
    _EmdConfigHumidityOffset_Type()
)
emdConfigHumidityOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigHumidityOffset.setStatus("mandatory")
_EmdConfigAlarm1_ObjectIdentity = ObjectIdentity
emdConfigAlarm1 = _EmdConfigAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 5)
)


class _EmdConfigAlarm1Name_Type(DisplayString):
    """Custom type emdConfigAlarm1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigAlarm1Name_Type.__name__ = "DisplayString"
_EmdConfigAlarm1Name_Object = MibScalar
emdConfigAlarm1Name = _EmdConfigAlarm1Name_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 5, 1),
    _EmdConfigAlarm1Name_Type()
)
emdConfigAlarm1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm1Name.setStatus("mandatory")


class _EmdConfigAlarm1Type_Type(Integer32):
    """Custom type emdConfigAlarm1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("nomralOpen", 2),
          ("normalClose", 3))
    )


_EmdConfigAlarm1Type_Type.__name__ = "Integer32"
_EmdConfigAlarm1Type_Object = MibScalar
emdConfigAlarm1Type = _EmdConfigAlarm1Type_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 5, 2),
    _EmdConfigAlarm1Type_Type()
)
emdConfigAlarm1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm1Type.setStatus("mandatory")
_EmdConfigAlarm2_ObjectIdentity = ObjectIdentity
emdConfigAlarm2 = _EmdConfigAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 6)
)


class _EmdConfigAlarm2Name_Type(DisplayString):
    """Custom type emdConfigAlarm2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_EmdConfigAlarm2Name_Type.__name__ = "DisplayString"
_EmdConfigAlarm2Name_Object = MibScalar
emdConfigAlarm2Name = _EmdConfigAlarm2Name_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 6, 1),
    _EmdConfigAlarm2Name_Type()
)
emdConfigAlarm2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm2Name.setStatus("mandatory")


class _EmdConfigAlarm2Type_Type(Integer32):
    """Custom type emdConfigAlarm2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("nomralOpen", 2),
          ("normalClose", 3))
    )


_EmdConfigAlarm2Type_Type.__name__ = "Integer32"
_EmdConfigAlarm2Type_Object = MibScalar
emdConfigAlarm2Type = _EmdConfigAlarm2Type_Object(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 1, 12, 6, 2),
    _EmdConfigAlarm2Type_Type()
)
emdConfigAlarm2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emdConfigAlarm2Type.setStatus("mandatory")
_UpsTrapGroup_ObjectIdentity = ObjectIdentity
upsTrapGroup = _UpsTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2)
)

# Managed Objects groups


# Notification objects

ushaPowerRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    ushaPowerRestored.setStatus(
        ""
    )

ushaPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    ushaPowerFail.setStatus(
        ""
    )

ushaReturnFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 3)
)
if mibBuilder.loadTexts:
    ushaReturnFromLowBattery.setStatus(
        ""
    )

ushaLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 4)
)
if mibBuilder.loadTexts:
    ushaLowBattery.setStatus(
        ""
    )

ushaUpsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    ushaUpsOk.setStatus(
        ""
    )

ushaUpsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 6)
)
if mibBuilder.loadTexts:
    ushaUpsFailed.setStatus(
        ""
    )

ushaUpsNotOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 7)
)
if mibBuilder.loadTexts:
    ushaUpsNotOnBattery.setStatus(
        ""
    )

ushaUpsOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 8)
)
ushaUpsOnBattery.setObjects(
      *(("USHA-MIB", "upsBatteryGroupEstimatedChargeRemaining"),
        ("USHA-MIB", "upsBatteryGroupVoltage"),
        ("USHA-MIB", "upsBatteryGroupSecondsOnBattery"))
)
if mibBuilder.loadTexts:
    ushaUpsOnBattery.setStatus(
        ""
    )

ushaTestOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 9)
)
ushaTestOver.setObjects(
      *(("USHA-MIB", "upsBatteryTest"),
        ("USHA-MIB", "upsTestBatteryTestSettingTime"),
        ("USHA-MIB", "upsTestBatteryTestResult"),
        ("USHA-MIB", "upsTestBatteryTestStartTime"),
        ("USHA-MIB", "upsTestBatteryTestElapsedTime"))
)
if mibBuilder.loadTexts:
    ushaTestOver.setStatus(
        ""
    )

ushaTestInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    ushaTestInProgress.setStatus(
        ""
    )

ushaBypassOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    ushaBypassOn.setStatus(
        ""
    )

ushaUpsOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    ushaUpsOnline.setStatus(
        ""
    )

ushaCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 13)
)
if mibBuilder.loadTexts:
    ushaCommunicationLost.setStatus(
        ""
    )

ushaCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 14)
)
if mibBuilder.loadTexts:
    ushaCommunicationEstablished.setStatus(
        ""
    )

ushaUpsGoingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 15)
)
if mibBuilder.loadTexts:
    ushaUpsGoingDown.setStatus(
        ""
    )

ushaUpsTurnedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 16)
)
if mibBuilder.loadTexts:
    ushaUpsTurnedOff.setStatus(
        ""
    )

ushaUpsSleeping = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 17)
)
ushaUpsSleeping.setObjects(
    ("USHA-MIB", "upsControlUpsSleepTime")
)
if mibBuilder.loadTexts:
    ushaUpsSleeping.setStatus(
        ""
    )

ushaUpsWokeUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 18)
)
if mibBuilder.loadTexts:
    ushaUpsWokeUp.setStatus(
        ""
    )

ushaUpsRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    ushaUpsRebooted.setStatus(
        ""
    )

ushaUpsShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    ushaUpsShutdownCancelled.setStatus(
        ""
    )

ushaUpsNotOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 21)
)
ushaUpsNotOverTemperature.setObjects(
      *(("USHA-MIB", "upsBatteryGroupTemperature"),
        ("USHA-MIB", "upsConfigGroupOverTemperatureSetPoint"))
)
if mibBuilder.loadTexts:
    ushaUpsNotOverTemperature.setStatus(
        ""
    )

ushaUpsOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 22)
)
ushaUpsOverTemperature.setObjects(
      *(("USHA-MIB", "upsBatteryGroupTemperature"),
        ("USHA-MIB", "upsConfigGroupOverTemperatureSetPoint"))
)
if mibBuilder.loadTexts:
    ushaUpsOverTemperature.setStatus(
        ""
    )

ushaUpsNotOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 23)
)
ushaUpsNotOverLoad.setObjects(
      *(("USHA-MIB", "upsOutputGroupPercentLoad"),
        ("USHA-MIB", "upsConfigGroupOverLoadSetPoint"))
)
if mibBuilder.loadTexts:
    ushaUpsNotOverLoad.setStatus(
        ""
    )

ushaUpsOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 24)
)
ushaUpsOverLoad.setObjects(
      *(("USHA-MIB", "upsOutputGroupPercentLoad"),
        ("USHA-MIB", "upsConfigGroupOverLoadSetPoint"))
)
if mibBuilder.loadTexts:
    ushaUpsOverLoad.setStatus(
        ""
    )

ushaUpsModuleInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 25)
)
if mibBuilder.loadTexts:
    ushaUpsModuleInserted.setStatus(
        ""
    )

ushaUpsModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 26)
)
if mibBuilder.loadTexts:
    ushaUpsModuleRemoved.setStatus(
        ""
    )

emdTemperatureNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 27)
)
emdTemperatureNotHigh.setObjects(
      *(("USHA-MIB", "emdSatatusTemperature"),
        ("USHA-MIB", "emdConfigTempHighSetPoint"),
        ("USHA-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureNotHigh.setStatus(
        ""
    )

emdTemperatureTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 28)
)
emdTemperatureTooHigh.setObjects(
      *(("USHA-MIB", "emdSatatusTemperature"),
        ("USHA-MIB", "emdConfigTempHighSetPoint"),
        ("USHA-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureTooHigh.setStatus(
        ""
    )

emdTemperatureNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 29)
)
emdTemperatureNotLow.setObjects(
      *(("USHA-MIB", "emdSatatusTemperature"),
        ("USHA-MIB", "emdConfigTempLowSetPoint"),
        ("USHA-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureNotLow.setStatus(
        ""
    )

emdTemperatureTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 30)
)
emdTemperatureTooLow.setObjects(
      *(("USHA-MIB", "emdSatatusTemperature"),
        ("USHA-MIB", "emdConfigTempLowSetPoint"),
        ("USHA-MIB", "emdConfigTempName"))
)
if mibBuilder.loadTexts:
    emdTemperatureTooLow.setStatus(
        ""
    )

emdHumidityNotHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 31)
)
emdHumidityNotHigh.setObjects(
      *(("USHA-MIB", "emdSatatusHumidity"),
        ("USHA-MIB", "emdConfigHumidityHighSetPoint"),
        ("USHA-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityNotHigh.setStatus(
        ""
    )

emdHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 32)
)
emdHumidityTooHigh.setObjects(
      *(("USHA-MIB", "emdSatatusHumidity"),
        ("USHA-MIB", "emdConfigHumidityHighSetPoint"),
        ("USHA-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityTooHigh.setStatus(
        ""
    )

emdHumidityNotLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 33)
)
emdHumidityNotLow.setObjects(
      *(("USHA-MIB", "emdSatatusHumidity"),
        ("USHA-MIB", "emdConfigHumidityLowSetPoint"),
        ("USHA-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityNotLow.setStatus(
        ""
    )

emdHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 34)
)
emdHumidityTooLow.setObjects(
      *(("USHA-MIB", "emdSatatusHumidity"),
        ("USHA-MIB", "emdConfigHumidityLowSetPoint"),
        ("USHA-MIB", "emdConfigHumidityName"))
)
if mibBuilder.loadTexts:
    emdHumidityTooLow.setStatus(
        ""
    )

emdAlarm1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 35)
)
emdAlarm1Normal.setObjects(
      *(("USHA-MIB", "emdConfigAlarm1Type"),
        ("USHA-MIB", "emdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    emdAlarm1Normal.setStatus(
        ""
    )

emdAlarm1Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 36)
)
emdAlarm1Active.setObjects(
      *(("USHA-MIB", "emdConfigAlarm1Type"),
        ("USHA-MIB", "emdConfigAlarm1Name"))
)
if mibBuilder.loadTexts:
    emdAlarm1Active.setStatus(
        ""
    )

emdAlarm2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 37)
)
emdAlarm2Normal.setObjects(
      *(("USHA-MIB", "emdConfigAlarm2Type"),
        ("USHA-MIB", "emdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    emdAlarm2Normal.setStatus(
        ""
    )

emdAlarm2Active = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 38)
)
emdAlarm2Active.setObjects(
      *(("USHA-MIB", "emdConfigAlarm2Type"),
        ("USHA-MIB", "emdConfigAlarm2Name"))
)
if mibBuilder.loadTexts:
    emdAlarm2Active.setStatus(
        ""
    )

ushaUpsInternalwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 39)
)
if mibBuilder.loadTexts:
    ushaUpsInternalwarning.setStatus(
        ""
    )

ushaUpsReturnFromInternalwarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 40)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromInternalwarning.setStatus(
        ""
    )

ushaUpsEPOActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 41)
)
if mibBuilder.loadTexts:
    ushaUpsEPOActive.setStatus(
        ""
    )

ushaUpsReturnFromEPOActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 42)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromEPOActive.setStatus(
        ""
    )

ushaUpsModuleUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 43)
)
if mibBuilder.loadTexts:
    ushaUpsModuleUnlock.setStatus(
        ""
    )

ushaUpsReturnFromModuleUnlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 44)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromModuleUnlock.setStatus(
        ""
    )

ushaUpsMain1Neutralloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 45)
)
if mibBuilder.loadTexts:
    ushaUpsMain1Neutralloss.setStatus(
        ""
    )

ushaUpsReturnFromMain1Neutralloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 46)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromMain1Neutralloss.setStatus(
        ""
    )

ushaUpsMain1phaseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 47)
)
if mibBuilder.loadTexts:
    ushaUpsMain1phaseerror.setStatus(
        ""
    )

ushaUpsReturnFromMain1phaseerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 48)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromMain1phaseerror.setStatus(
        ""
    )

ushaUpsSitefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 49)
)
if mibBuilder.loadTexts:
    ushaUpsSitefault.setStatus(
        ""
    )

ushaUpsReturnFromSitefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 50)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromSitefault.setStatus(
        ""
    )

ushaUpsBypassAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 51)
)
if mibBuilder.loadTexts:
    ushaUpsBypassAbnormal.setStatus(
        ""
    )

ushaUpsReturnFromBypassAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 52)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBypassAbnormal.setStatus(
        ""
    )

ushaUpsBypassPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 53)
)
if mibBuilder.loadTexts:
    ushaUpsBypassPhaseError.setStatus(
        ""
    )

ushaUpsReturnFromBypassPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 54)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBypassPhaseError.setStatus(
        ""
    )

ushaUpsBatteryOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 55)
)
if mibBuilder.loadTexts:
    ushaUpsBatteryOpen.setStatus(
        ""
    )

ushaUpsReturnFromBatteryOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 56)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBatteryOpen.setStatus(
        ""
    )

ushaUpsBatteryOverCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 57)
)
if mibBuilder.loadTexts:
    ushaUpsBatteryOverCharge.setStatus(
        ""
    )

ushaUpsReturnFromBatteryOverCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 58)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBatteryOverCharge.setStatus(
        ""
    )

ushaUpsBatteryReverse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 59)
)
if mibBuilder.loadTexts:
    ushaUpsBatteryReverse.setStatus(
        ""
    )

ushaUpsReturnFromBatteryReverse = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 60)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBatteryReverse.setStatus(
        ""
    )

ushaUpsOverloadforewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 61)
)
if mibBuilder.loadTexts:
    ushaUpsOverloadforewarning.setStatus(
        ""
    )

ushaUpsReturnFromOverloadforewarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 62)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromOverloadforewarning.setStatus(
        ""
    )

ushaUpsOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 63)
)
if mibBuilder.loadTexts:
    ushaUpsOverloadWarning.setStatus(
        ""
    )

ushaUpsReturnFromOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 64)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromOverloadWarning.setStatus(
        ""
    )

ushaUpsFanLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 65)
)
if mibBuilder.loadTexts:
    ushaUpsFanLock.setStatus(
        ""
    )

ushaUpsReturnFromFanLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 66)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromFanLock.setStatus(
        ""
    )

ushaUpsMaintaincoverisopen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 67)
)
if mibBuilder.loadTexts:
    ushaUpsMaintaincoverisopen.setStatus(
        ""
    )

ushaUpsReturnFromMaintaincoverisopen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 68)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromMaintaincoverisopen.setStatus(
        ""
    )

ushaUpsChargerfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 69)
)
if mibBuilder.loadTexts:
    ushaUpsChargerfault.setStatus(
        ""
    )

ushaUpsReturnFromChargerfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 70)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromChargerfault.setStatus(
        ""
    )

ushaUpsModulelocationerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 71)
)
if mibBuilder.loadTexts:
    ushaUpsModulelocationerror.setStatus(
        ""
    )

ushaUpsReturnFromModulelocationerror = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 72)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromModulelocationerror.setStatus(
        ""
    )

ushaUpsTurnonabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 73)
)
if mibBuilder.loadTexts:
    ushaUpsTurnonabnormal.setStatus(
        ""
    )

ushaUpsReturnFromTurnonabnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 74)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromTurnonabnormal.setStatus(
        ""
    )

ushaUpsRedundancyloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 75)
)
if mibBuilder.loadTexts:
    ushaUpsRedundancyloss.setStatus(
        ""
    )

ushaUpsReturnFromRedundancyloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 76)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromRedundancyloss.setStatus(
        ""
    )

ushaUpsHotSwapActived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 77)
)
if mibBuilder.loadTexts:
    ushaUpsHotSwapActived.setStatus(
        ""
    )

ushaUpsReturnFromHotSwapActived = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 78)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromHotSwapActived.setStatus(
        ""
    )

ushaUpsBatteryInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 79)
)
if mibBuilder.loadTexts:
    ushaUpsBatteryInform.setStatus(
        ""
    )

ushaUpsReturnFromBatteryInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 80)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBatteryInform.setStatus(
        ""
    )

ushaUpsInspectionInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 81)
)
if mibBuilder.loadTexts:
    ushaUpsInspectionInform.setStatus(
        ""
    )

ushaUpsReturnFromInspectionInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 82)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromInspectionInform.setStatus(
        ""
    )

ushaUpsGuaranteeInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 83)
)
if mibBuilder.loadTexts:
    ushaUpsGuaranteeInform.setStatus(
        ""
    )

ushaUpsReturnFromGuaranteeInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 84)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromGuaranteeInform.setStatus(
        ""
    )

ushaUpsTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 85)
)
if mibBuilder.loadTexts:
    ushaUpsTemperatureLow.setStatus(
        ""
    )

ushaUpsReturnFromTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 86)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromTemperatureLow.setStatus(
        ""
    )

ushaUpsTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 87)
)
if mibBuilder.loadTexts:
    ushaUpsTemperatureHigh.setStatus(
        ""
    )

ushaUpsReturnFromTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 88)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromTemperatureHigh.setStatus(
        ""
    )

ushaUpsBatteryOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 89)
)
if mibBuilder.loadTexts:
    ushaUpsBatteryOverTemperature.setStatus(
        ""
    )

ushaUpsReturnFromBatteryOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 90)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBatteryOverTemperature.setStatus(
        ""
    )

ushaUpsFanMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 91)
)
if mibBuilder.loadTexts:
    ushaUpsFanMaintainInform.setStatus(
        ""
    )

ushaUpsReturnFromFanMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 92)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromFanMaintainInform.setStatus(
        ""
    )

ushaUpsBusCapacitanceMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 93)
)
if mibBuilder.loadTexts:
    ushaUpsBusCapacitanceMaintainInform.setStatus(
        ""
    )

ushaUpsReturnFromBusCapacitanceMaintainInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 94)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromBusCapacitanceMaintainInform.setStatus(
        ""
    )

ushaUpsSystemOverCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 95)
)
if mibBuilder.loadTexts:
    ushaUpsSystemOverCapacity.setStatus(
        ""
    )

ushaUpsReturnFromSystemOverCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 2468, 1, 2, 1, 2, 0, 96)
)
if mibBuilder.loadTexts:
    ushaUpsReturnFromSystemOverCapacity.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "USHA-MIB",
    **{"ingrasys": ingrasys,
       "product": product,
       "upsAgent": upsAgent,
       "ushap": ushap,
       "upsObjectGroup": upsObjectGroup,
       "upsIdentGroup": upsIdentGroup,
       "upsIdentGroupManufacturer": upsIdentGroupManufacturer,
       "upsIdentGroupModel": upsIdentGroupModel,
       "upsIdentGroupUPSFirmwareVersion": upsIdentGroupUPSFirmwareVersion,
       "upsIdentGroupAgentSoftwareVersion": upsIdentGroupAgentSoftwareVersion,
       "upsIdentGroupName": upsIdentGroupName,
       "upsIdentGroupAttachedDevices": upsIdentGroupAttachedDevices,
       "upsIdentGroupUpsSerialNumber": upsIdentGroupUpsSerialNumber,
       "upsBatteryGroup": upsBatteryGroup,
       "upsBatteryGroupStatus": upsBatteryGroupStatus,
       "upsBatteryGroupSecondsOnBattery": upsBatteryGroupSecondsOnBattery,
       "upsBatteryGroupEstimatedMinutesRemaining": upsBatteryGroupEstimatedMinutesRemaining,
       "upsBatteryGroupEstimatedChargeRemaining": upsBatteryGroupEstimatedChargeRemaining,
       "upsBatteryGroupVoltage": upsBatteryGroupVoltage,
       "upsBatteryGroupMandatory": upsBatteryGroupMandatory,
       "upsBatteryGroupTemperature": upsBatteryGroupTemperature,
       "upsInputGroup": upsInputGroup,
       "upsInputGroupLineBads": upsInputGroupLineBads,
       "upsInputGroupNumLines": upsInputGroupNumLines,
       "upsInputGroupTable": upsInputGroupTable,
       "upsInputGroupEntry": upsInputGroupEntry,
       "upsInputGroupLineIndex": upsInputGroupLineIndex,
       "upsInputGroupFrequency": upsInputGroupFrequency,
       "upsInputGroupVoltage": upsInputGroupVoltage,
       "upsInputGroupCurrent": upsInputGroupCurrent,
       "upsInputGroupTruePower": upsInputGroupTruePower,
       "upsInputGroupVoltageMax": upsInputGroupVoltageMax,
       "upsInputGroupVoltageMin": upsInputGroupVoltageMin,
       "upsOutputGroup": upsOutputGroup,
       "upsOutputGroupSource": upsOutputGroupSource,
       "upsOutputGroupFrequency": upsOutputGroupFrequency,
       "upsOutputGroupNumLines": upsOutputGroupNumLines,
       "upsOutputGroupTable": upsOutputGroupTable,
       "upsOutputGroupEntry": upsOutputGroupEntry,
       "upsOutputGroupLineIndex": upsOutputGroupLineIndex,
       "upsOutputGroupVoltage": upsOutputGroupVoltage,
       "upsOutputGroupCurrent": upsOutputGroupCurrent,
       "upsOutputGroupPower": upsOutputGroupPower,
       "upsOutputGroupPercentLoad": upsOutputGroupPercentLoad,
       "upsBypassGroup": upsBypassGroup,
       "upsBypassGroupFrequency": upsBypassGroupFrequency,
       "upsBypassGroupNumLines": upsBypassGroupNumLines,
       "upsBypassGroupTable": upsBypassGroupTable,
       "upsBypassGroupEntry": upsBypassGroupEntry,
       "upsBypassGroupLineIndex": upsBypassGroupLineIndex,
       "upsBypassGroupVoltage": upsBypassGroupVoltage,
       "upsBypassGroupCurrent": upsBypassGroupCurrent,
       "upsBypassGroupPower": upsBypassGroupPower,
       "upsTestGroup": upsTestGroup,
       "upsTestBatteryTestSettingTime": upsTestBatteryTestSettingTime,
       "upsBatteryTest": upsBatteryTest,
       "upsTestBatteryTestResult": upsTestBatteryTestResult,
       "upsTestBatteryTestStartTime": upsTestBatteryTestStartTime,
       "upsTestBatteryTestElapsedTime": upsTestBatteryTestElapsedTime,
       "upsBatteryTestScheduleTable": upsBatteryTestScheduleTable,
       "upsBatteryTestScheduleEntry": upsBatteryTestScheduleEntry,
       "upsBatteryTestScheduleIndex": upsBatteryTestScheduleIndex,
       "upsBatteryTestScheduleDay": upsBatteryTestScheduleDay,
       "upsBatteryTestScheduleTime": upsBatteryTestScheduleTime,
       "upsBatteryTestScheduleType": upsBatteryTestScheduleType,
       "upsBatteryTestScheduleTestWithTime": upsBatteryTestScheduleTestWithTime,
       "upsBatteryTestScheduleSpecialDay": upsBatteryTestScheduleSpecialDay,
       "upsControlGroup": upsControlGroup,
       "upsControlUpsShutdownDelay": upsControlUpsShutdownDelay,
       "upsControlUpsSleepTime": upsControlUpsSleepTime,
       "upsControlUpsOnOffControl": upsControlUpsOnOffControl,
       "upsControlShutdownParametersTable": upsControlShutdownParametersTable,
       "upsControlShutdownParametersEntry": upsControlShutdownParametersEntry,
       "upsControlEvent": upsControlEvent,
       "upsControlEventStatus": upsControlEventStatus,
       "upsControlDelay": upsControlDelay,
       "upsControlFirstWarning": upsControlFirstWarning,
       "upsControlWarningInterval": upsControlWarningInterval,
       "upsControlWeeklyScheduleTable": upsControlWeeklyScheduleTable,
       "upsControlWeeklyScheduleEntry": upsControlWeeklyScheduleEntry,
       "upsControlWeeklyIndex": upsControlWeeklyIndex,
       "upsControlWeeklyShutdownDay": upsControlWeeklyShutdownDay,
       "upsControlWeeklyShutdownTime": upsControlWeeklyShutdownTime,
       "upsControlWeeklyRestartDay": upsControlWeeklyRestartDay,
       "upsControlWeeklyRestartTime": upsControlWeeklyRestartTime,
       "upsControlSpecialScheduleTable": upsControlSpecialScheduleTable,
       "upsControlSpecialScheduleEntry": upsControlSpecialScheduleEntry,
       "upsControlSpecialIndex": upsControlSpecialIndex,
       "upsControlSpecialShutdownDay": upsControlSpecialShutdownDay,
       "upsControlSpecialShutdownTime": upsControlSpecialShutdownTime,
       "upsControlSpecialRestartDay": upsControlSpecialRestartDay,
       "upsControlSpecialRestartTime": upsControlSpecialRestartTime,
       "upsConfigGroup": upsConfigGroup,
       "upsConfigGroupInputVoltage": upsConfigGroupInputVoltage,
       "upsConfigGroupInputFreq": upsConfigGroupInputFreq,
       "upsConfigGroupOutputVoltage": upsConfigGroupOutputVoltage,
       "upsConfigGroupOutputFreq": upsConfigGroupOutputFreq,
       "upsConfigGroupOutputVA": upsConfigGroupOutputVA,
       "upsConfigGroupOutputPower": upsConfigGroupOutputPower,
       "upsConfigGroupOverTemperatureSetPoint": upsConfigGroupOverTemperatureSetPoint,
       "upsConfigGroupOverLoadSetPoint": upsConfigGroupOverLoadSetPoint,
       "upsClients": upsClients,
       "upsClientsConnectedNum": upsClientsConnectedNum,
       "upsDevicesTable": upsDevicesTable,
       "upsDevicesEntry": upsDevicesEntry,
       "indexOfDevice": indexOfDevice,
       "addrOfDevice": addrOfDevice,
       "nameOfDevice": nameOfDevice,
       "timeOfConnection": timeOfConnection,
       "timeOfConnectionTime": timeOfConnectionTime,
       "timeOfConnectionTimeout": timeOfConnectionTimeout,
       "agentConfig": agentConfig,
       "agentConfigIpaddress": agentConfigIpaddress,
       "agentConfigGateway": agentConfigGateway,
       "agentConfigSubnetMask": agentConfigSubnetMask,
       "agentConfigDate": agentConfigDate,
       "agentConfigTime": agentConfigTime,
       "agentConfigPrimaryTimeServer": agentConfigPrimaryTimeServer,
       "agentConfigSecondaryTimeServer": agentConfigSecondaryTimeServer,
       "agentConfigHistoryLogFrequency": agentConfigHistoryLogFrequency,
       "agentConfigExtHistoryLogFrequency": agentConfigExtHistoryLogFrequency,
       "agentConfigPollRate": agentConfigPollRate,
       "agentConfigBaudRate": agentConfigBaudRate,
       "agentConfigDhcpStatue": agentConfigDhcpStatue,
       "agentConfigTelnetStatue": agentConfigTelnetStatue,
       "agentConfigTftpStatue": agentConfigTftpStatue,
       "agentConfigResetToDefault": agentConfigResetToDefault,
       "agentConfigRestart": agentConfigRestart,
       "agentConfigClearAgentLog": agentConfigClearAgentLog,
       "agentConfigClearEventLog": agentConfigClearEventLog,
       "agentConfigClearExtHistoryLog": agentConfigClearExtHistoryLog,
       "agentConfigClearHistoryLog": agentConfigClearHistoryLog,
       "agentConfigTrapRetryCount": agentConfigTrapRetryCount,
       "agentConfigTrapRetryTime": agentConfigTrapRetryTime,
       "agentConfigTrapAckSignature": agentConfigTrapAckSignature,
       "agentConfigMibVersion": agentConfigMibVersion,
       "agentConfigTrapsReceiversTable": agentConfigTrapsReceiversTable,
       "agentConfigTrapsReceiversEntry": agentConfigTrapsReceiversEntry,
       "trapsIndex": trapsIndex,
       "trapsReceiverAddr": trapsReceiverAddr,
       "receiverCommunityString": receiverCommunityString,
       "receiverNmsType": receiverNmsType,
       "receiverSeverityLevel": receiverSeverityLevel,
       "receiverDescription": receiverDescription,
       "agentConfigAccessControlTable": agentConfigAccessControlTable,
       "agentConfigAccessControlEntry": agentConfigAccessControlEntry,
       "accessIndex": accessIndex,
       "accessControlAddr": accessControlAddr,
       "accessCommunityString": accessCommunityString,
       "accessControlMode": accessControlMode,
       "agentConfigDefaultLanguage": agentConfigDefaultLanguage,
       "emdStatus": emdStatus,
       "emdSatatusEmdType": emdSatatusEmdType,
       "emdSatatusTemperature": emdSatatusTemperature,
       "emdSatatusHumidity": emdSatatusHumidity,
       "emdSatatusAlarm1": emdSatatusAlarm1,
       "emdSatatusAlarm2": emdSatatusAlarm2,
       "emdConfig": emdConfig,
       "usahEmdConfigEmdConfig": usahEmdConfigEmdConfig,
       "emdConfigEmdName": emdConfigEmdName,
       "emdConfigTemperature": emdConfigTemperature,
       "emdConfigTempName": emdConfigTempName,
       "emdConfigTempHighSetPoint": emdConfigTempHighSetPoint,
       "emdConfigTempHighStatus": emdConfigTempHighStatus,
       "emdConfigTempLowSetPoint": emdConfigTempLowSetPoint,
       "emdConfigTempLowStatus": emdConfigTempLowStatus,
       "emdConfigTempOffset": emdConfigTempOffset,
       "emdConfigHumidity": emdConfigHumidity,
       "emdConfigHumidityName": emdConfigHumidityName,
       "emdConfigHumidityHighSetPoint": emdConfigHumidityHighSetPoint,
       "emdConfigHumidityLowStatus": emdConfigHumidityLowStatus,
       "emdConfigHumidityLowSetPoint": emdConfigHumidityLowSetPoint,
       "emdConfigHumidityHighStatus": emdConfigHumidityHighStatus,
       "emdConfigHumidityOffset": emdConfigHumidityOffset,
       "emdConfigAlarm1": emdConfigAlarm1,
       "emdConfigAlarm1Name": emdConfigAlarm1Name,
       "emdConfigAlarm1Type": emdConfigAlarm1Type,
       "emdConfigAlarm2": emdConfigAlarm2,
       "emdConfigAlarm2Name": emdConfigAlarm2Name,
       "emdConfigAlarm2Type": emdConfigAlarm2Type,
       "upsTrapGroup": upsTrapGroup,
       "ushaPowerRestored": ushaPowerRestored,
       "ushaPowerFail": ushaPowerFail,
       "ushaReturnFromLowBattery": ushaReturnFromLowBattery,
       "ushaLowBattery": ushaLowBattery,
       "ushaUpsOk": ushaUpsOk,
       "ushaUpsFailed": ushaUpsFailed,
       "ushaUpsNotOnBattery": ushaUpsNotOnBattery,
       "ushaUpsOnBattery": ushaUpsOnBattery,
       "ushaTestOver": ushaTestOver,
       "ushaTestInProgress": ushaTestInProgress,
       "ushaBypassOn": ushaBypassOn,
       "ushaUpsOnline": ushaUpsOnline,
       "ushaCommunicationLost": ushaCommunicationLost,
       "ushaCommunicationEstablished": ushaCommunicationEstablished,
       "ushaUpsGoingDown": ushaUpsGoingDown,
       "ushaUpsTurnedOff": ushaUpsTurnedOff,
       "ushaUpsSleeping": ushaUpsSleeping,
       "ushaUpsWokeUp": ushaUpsWokeUp,
       "ushaUpsRebooted": ushaUpsRebooted,
       "ushaUpsShutdownCancelled": ushaUpsShutdownCancelled,
       "ushaUpsNotOverTemperature": ushaUpsNotOverTemperature,
       "ushaUpsOverTemperature": ushaUpsOverTemperature,
       "ushaUpsNotOverLoad": ushaUpsNotOverLoad,
       "ushaUpsOverLoad": ushaUpsOverLoad,
       "ushaUpsModuleInserted": ushaUpsModuleInserted,
       "ushaUpsModuleRemoved": ushaUpsModuleRemoved,
       "emdTemperatureNotHigh": emdTemperatureNotHigh,
       "emdTemperatureTooHigh": emdTemperatureTooHigh,
       "emdTemperatureNotLow": emdTemperatureNotLow,
       "emdTemperatureTooLow": emdTemperatureTooLow,
       "emdHumidityNotHigh": emdHumidityNotHigh,
       "emdHumidityTooHigh": emdHumidityTooHigh,
       "emdHumidityNotLow": emdHumidityNotLow,
       "emdHumidityTooLow": emdHumidityTooLow,
       "emdAlarm1Normal": emdAlarm1Normal,
       "emdAlarm1Active": emdAlarm1Active,
       "emdAlarm2Normal": emdAlarm2Normal,
       "emdAlarm2Active": emdAlarm2Active,
       "ushaUpsInternalwarning": ushaUpsInternalwarning,
       "ushaUpsReturnFromInternalwarning": ushaUpsReturnFromInternalwarning,
       "ushaUpsEPOActive": ushaUpsEPOActive,
       "ushaUpsReturnFromEPOActive": ushaUpsReturnFromEPOActive,
       "ushaUpsModuleUnlock": ushaUpsModuleUnlock,
       "ushaUpsReturnFromModuleUnlock": ushaUpsReturnFromModuleUnlock,
       "ushaUpsMain1Neutralloss": ushaUpsMain1Neutralloss,
       "ushaUpsReturnFromMain1Neutralloss": ushaUpsReturnFromMain1Neutralloss,
       "ushaUpsMain1phaseerror": ushaUpsMain1phaseerror,
       "ushaUpsReturnFromMain1phaseerror": ushaUpsReturnFromMain1phaseerror,
       "ushaUpsSitefault": ushaUpsSitefault,
       "ushaUpsReturnFromSitefault": ushaUpsReturnFromSitefault,
       "ushaUpsBypassAbnormal": ushaUpsBypassAbnormal,
       "ushaUpsReturnFromBypassAbnormal": ushaUpsReturnFromBypassAbnormal,
       "ushaUpsBypassPhaseError": ushaUpsBypassPhaseError,
       "ushaUpsReturnFromBypassPhaseError": ushaUpsReturnFromBypassPhaseError,
       "ushaUpsBatteryOpen": ushaUpsBatteryOpen,
       "ushaUpsReturnFromBatteryOpen": ushaUpsReturnFromBatteryOpen,
       "ushaUpsBatteryOverCharge": ushaUpsBatteryOverCharge,
       "ushaUpsReturnFromBatteryOverCharge": ushaUpsReturnFromBatteryOverCharge,
       "ushaUpsBatteryReverse": ushaUpsBatteryReverse,
       "ushaUpsReturnFromBatteryReverse": ushaUpsReturnFromBatteryReverse,
       "ushaUpsOverloadforewarning": ushaUpsOverloadforewarning,
       "ushaUpsReturnFromOverloadforewarning": ushaUpsReturnFromOverloadforewarning,
       "ushaUpsOverloadWarning": ushaUpsOverloadWarning,
       "ushaUpsReturnFromOverloadWarning": ushaUpsReturnFromOverloadWarning,
       "ushaUpsFanLock": ushaUpsFanLock,
       "ushaUpsReturnFromFanLock": ushaUpsReturnFromFanLock,
       "ushaUpsMaintaincoverisopen": ushaUpsMaintaincoverisopen,
       "ushaUpsReturnFromMaintaincoverisopen": ushaUpsReturnFromMaintaincoverisopen,
       "ushaUpsChargerfault": ushaUpsChargerfault,
       "ushaUpsReturnFromChargerfault": ushaUpsReturnFromChargerfault,
       "ushaUpsModulelocationerror": ushaUpsModulelocationerror,
       "ushaUpsReturnFromModulelocationerror": ushaUpsReturnFromModulelocationerror,
       "ushaUpsTurnonabnormal": ushaUpsTurnonabnormal,
       "ushaUpsReturnFromTurnonabnormal": ushaUpsReturnFromTurnonabnormal,
       "ushaUpsRedundancyloss": ushaUpsRedundancyloss,
       "ushaUpsReturnFromRedundancyloss": ushaUpsReturnFromRedundancyloss,
       "ushaUpsHotSwapActived": ushaUpsHotSwapActived,
       "ushaUpsReturnFromHotSwapActived": ushaUpsReturnFromHotSwapActived,
       "ushaUpsBatteryInform": ushaUpsBatteryInform,
       "ushaUpsReturnFromBatteryInform": ushaUpsReturnFromBatteryInform,
       "ushaUpsInspectionInform": ushaUpsInspectionInform,
       "ushaUpsReturnFromInspectionInform": ushaUpsReturnFromInspectionInform,
       "ushaUpsGuaranteeInform": ushaUpsGuaranteeInform,
       "ushaUpsReturnFromGuaranteeInform": ushaUpsReturnFromGuaranteeInform,
       "ushaUpsTemperatureLow": ushaUpsTemperatureLow,
       "ushaUpsReturnFromTemperatureLow": ushaUpsReturnFromTemperatureLow,
       "ushaUpsTemperatureHigh": ushaUpsTemperatureHigh,
       "ushaUpsReturnFromTemperatureHigh": ushaUpsReturnFromTemperatureHigh,
       "ushaUpsBatteryOverTemperature": ushaUpsBatteryOverTemperature,
       "ushaUpsReturnFromBatteryOverTemperature": ushaUpsReturnFromBatteryOverTemperature,
       "ushaUpsFanMaintainInform": ushaUpsFanMaintainInform,
       "ushaUpsReturnFromFanMaintainInform": ushaUpsReturnFromFanMaintainInform,
       "ushaUpsBusCapacitanceMaintainInform": ushaUpsBusCapacitanceMaintainInform,
       "ushaUpsReturnFromBusCapacitanceMaintainInform": ushaUpsReturnFromBusCapacitanceMaintainInform,
       "ushaUpsSystemOverCapacity": ushaUpsSystemOverCapacity,
       "ushaUpsReturnFromSystemOverCapacity": ushaUpsReturnFromSystemOverCapacity}
)
