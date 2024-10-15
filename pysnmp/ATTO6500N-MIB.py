# SNMP MIB module (ATTO6500N-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATTO6500N-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:21 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

bridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3)
)
bridge.setRevisions(
        ("2013-04-19 00:00",
         "2013-04-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayWWN(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class QSFPTech(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activecopper", 2),
          ("optical", 1),
          ("passivecopper", 3),
          ("unknown", -1))
    )



class PHYStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unknown", -1))
    )



# MIB Managed Objects in the order of their OIDs

_Attotech_ObjectIdentity = ObjectIdentity
attotech = _Attotech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547)
)
_AttoProducts_ObjectIdentity = ObjectIdentity
attoProducts = _AttoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1)
)
_AttoMgmt_ObjectIdentity = ObjectIdentity
attoMgmt = _AttoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2)
)
_BridgeTraps_ObjectIdentity = ObjectIdentity
bridgeTraps = _BridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 0)
)
_BridgeIdentity_ObjectIdentity = ObjectIdentity
bridgeIdentity = _BridgeIdentity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1)
)
_BridgeUniqueId_Type = DisplayWWN
_BridgeUniqueId_Object = MibScalar
bridgeUniqueId = _BridgeUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 1),
    _BridgeUniqueId_Type()
)
bridgeUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeUniqueId.setStatus("current")


class _VendorID_Type(DisplayString):
    """Custom type vendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VendorID_Type.__name__ = "DisplayString"
_VendorID_Object = MibScalar
vendorID = _VendorID_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 2),
    _VendorID_Type()
)
vendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorID.setStatus("current")


class _ModelName_Type(DisplayString):
    """Custom type modelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModelName_Type.__name__ = "DisplayString"
_ModelName_Object = MibScalar
modelName = _ModelName_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 3),
    _ModelName_Type()
)
modelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelName.setStatus("current")


class _PrimaryFirmwareRevision_Type(DisplayString):
    """Custom type primaryFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PrimaryFirmwareRevision_Type.__name__ = "DisplayString"
_PrimaryFirmwareRevision_Object = MibScalar
primaryFirmwareRevision = _PrimaryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 4),
    _PrimaryFirmwareRevision_Type()
)
primaryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryFirmwareRevision.setStatus("current")


class _PrimaryFirmwareBuildDate_Type(DateAndTime):
    """Custom type primaryFirmwareBuildDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_PrimaryFirmwareBuildDate_Type.__name__ = "DateAndTime"
_PrimaryFirmwareBuildDate_Object = MibScalar
primaryFirmwareBuildDate = _PrimaryFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 5),
    _PrimaryFirmwareBuildDate_Type()
)
primaryFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryFirmwareBuildDate.setStatus("current")
_HardwareVersion_Type = Integer32
_HardwareVersion_Object = MibScalar
hardwareVersion = _HardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 6),
    _HardwareVersion_Type()
)
hardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareVersion.setStatus("current")


class _SecondaryFirmwareRevision_Type(DisplayString):
    """Custom type secondaryFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SecondaryFirmwareRevision_Type.__name__ = "DisplayString"
_SecondaryFirmwareRevision_Object = MibScalar
secondaryFirmwareRevision = _SecondaryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 7),
    _SecondaryFirmwareRevision_Type()
)
secondaryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryFirmwareRevision.setStatus("current")


class _SecondaryFirmwareBuildDate_Type(DateAndTime):
    """Custom type secondaryFirmwareBuildDate based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SecondaryFirmwareBuildDate_Type.__name__ = "DateAndTime"
_SecondaryFirmwareBuildDate_Object = MibScalar
secondaryFirmwareBuildDate = _SecondaryFirmwareBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 8),
    _SecondaryFirmwareBuildDate_Type()
)
secondaryFirmwareBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secondaryFirmwareBuildDate.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 9),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _BridgeName_Type(DisplayString):
    """Custom type bridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BridgeName_Type.__name__ = "DisplayString"
_BridgeName_Object = MibScalar
bridgeName = _BridgeName_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 1, 10),
    _BridgeName_Type()
)
bridgeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeName.setStatus("current")
_BridgeChassis_ObjectIdentity = ObjectIdentity
bridgeChassis = _BridgeChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2)
)


class _LastReboot_Type(DateAndTime):
    """Custom type lastReboot based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LastReboot_Type.__name__ = "DateAndTime"
_LastReboot_Object = MibScalar
lastReboot = _LastReboot_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 1),
    _LastReboot_Type()
)
lastReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastReboot.setStatus("current")
_Uptime_Type = TimeInterval
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 2),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")


class _LastRebootReason_Type(DisplayString):
    """Custom type lastRebootReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_LastRebootReason_Type.__name__ = "DisplayString"
_LastRebootReason_Object = MibScalar
lastRebootReason = _LastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 3),
    _LastRebootReason_Type()
)
lastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastRebootReason.setStatus("current")
_MinimumOperatingTemp_Type = Integer32
_MinimumOperatingTemp_Object = MibScalar
minimumOperatingTemp = _MinimumOperatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 4),
    _MinimumOperatingTemp_Type()
)
minimumOperatingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minimumOperatingTemp.setStatus("current")
_MaximumOperatingTemp_Type = Integer32
_MaximumOperatingTemp_Object = MibScalar
maximumOperatingTemp = _MaximumOperatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 5),
    _MaximumOperatingTemp_Type()
)
maximumOperatingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumOperatingTemp.setStatus("current")
_TemperatureHighAlertSetting_Type = Integer32
_TemperatureHighAlertSetting_Object = MibScalar
temperatureHighAlertSetting = _TemperatureHighAlertSetting_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 6),
    _TemperatureHighAlertSetting_Type()
)
temperatureHighAlertSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureHighAlertSetting.setStatus("current")
_TemperatureLowAlertSetting_Type = Integer32
_TemperatureLowAlertSetting_Object = MibScalar
temperatureLowAlertSetting = _TemperatureLowAlertSetting_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 7),
    _TemperatureLowAlertSetting_Type()
)
temperatureLowAlertSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureLowAlertSetting.setStatus("current")
_ChassisTemperature_Type = Integer32
_ChassisTemperature_Object = MibScalar
chassisTemperature = _ChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 8),
    _ChassisTemperature_Type()
)
chassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperature.setStatus("current")


class _ChassisTemperatureStatus_Type(Integer32):
    """Custom type chassisTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("normal", 1),
          ("warning", 2))
    )


_ChassisTemperatureStatus_Type.__name__ = "Integer32"
_ChassisTemperatureStatus_Object = MibScalar
chassisTemperatureStatus = _ChassisTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 9),
    _ChassisTemperatureStatus_Type()
)
chassisTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTemperatureStatus.setStatus("current")
_DramSingleBitErrorCount_Type = Integer32
_DramSingleBitErrorCount_Object = MibScalar
dramSingleBitErrorCount = _DramSingleBitErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 10),
    _DramSingleBitErrorCount_Type()
)
dramSingleBitErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dramSingleBitErrorCount.setStatus("current")


class _ChassisThroughputStatus_Type(Integer32):
    """Custom type chassisThroughputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2))
    )


_ChassisThroughputStatus_Type.__name__ = "Integer32"
_ChassisThroughputStatus_Object = MibScalar
chassisThroughputStatus = _ChassisThroughputStatus_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 11),
    _ChassisThroughputStatus_Type()
)
chassisThroughputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisThroughputStatus.setStatus("current")
_FcSFPInfoTable_Object = MibTable
fcSFPInfoTable = _FcSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12)
)
if mibBuilder.loadTexts:
    fcSFPInfoTable.setStatus("current")
_FcSFPInfoEntry_Object = MibTableRow
fcSFPInfoEntry = _FcSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1)
)
fcSFPInfoEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "fcSFPIndex"),
)
if mibBuilder.loadTexts:
    fcSFPInfoEntry.setStatus("current")


class _FcSFPIndex_Type(Integer32):
    """Custom type fcSFPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FcSFPIndex_Type.__name__ = "Integer32"
_FcSFPIndex_Object = MibTableColumn
fcSFPIndex = _FcSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1, 1),
    _FcSFPIndex_Type()
)
fcSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcSFPIndex.setStatus("current")


class _FcSFPVendor_Type(DisplayString):
    """Custom type fcSFPVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FcSFPVendor_Type.__name__ = "DisplayString"
_FcSFPVendor_Object = MibTableColumn
fcSFPVendor = _FcSFPVendor_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1, 2),
    _FcSFPVendor_Type()
)
fcSFPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSFPVendor.setStatus("current")


class _FcSFPSerialNum_Type(DisplayString):
    """Custom type fcSFPSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FcSFPSerialNum_Type.__name__ = "DisplayString"
_FcSFPSerialNum_Object = MibTableColumn
fcSFPSerialNum = _FcSFPSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1, 3),
    _FcSFPSerialNum_Type()
)
fcSFPSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSFPSerialNum.setStatus("current")


class _FcSFPPartNum_Type(DisplayString):
    """Custom type fcSFPPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FcSFPPartNum_Type.__name__ = "DisplayString"
_FcSFPPartNum_Object = MibTableColumn
fcSFPPartNum = _FcSFPPartNum_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1, 4),
    _FcSFPPartNum_Type()
)
fcSFPPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSFPPartNum.setStatus("current")


class _FcSFPDataRateCapability_Type(Integer32):
    """Custom type fcSFPDataRateCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("gb16", 16),
          ("gb2", 2),
          ("gb4", 4),
          ("gb8", 8))
    )


_FcSFPDataRateCapability_Type.__name__ = "Integer32"
_FcSFPDataRateCapability_Object = MibTableColumn
fcSFPDataRateCapability = _FcSFPDataRateCapability_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 12, 1, 5),
    _FcSFPDataRateCapability_Type()
)
fcSFPDataRateCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSFPDataRateCapability.setStatus("current")
_SasQSFPInfoTable_Object = MibTable
sasQSFPInfoTable = _SasQSFPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13)
)
if mibBuilder.loadTexts:
    sasQSFPInfoTable.setStatus("current")
_SasQSFPInfoEntry_Object = MibTableRow
sasQSFPInfoEntry = _SasQSFPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1)
)
sasQSFPInfoEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "sasQSFPIndex"),
)
if mibBuilder.loadTexts:
    sasQSFPInfoEntry.setStatus("current")


class _SasQSFPIndex_Type(Integer32):
    """Custom type sasQSFPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SasQSFPIndex_Type.__name__ = "Integer32"
_SasQSFPIndex_Object = MibTableColumn
sasQSFPIndex = _SasQSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1, 1),
    _SasQSFPIndex_Type()
)
sasQSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sasQSFPIndex.setStatus("current")


class _SasQSFPVendor_Type(DisplayString):
    """Custom type sasQSFPVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SasQSFPVendor_Type.__name__ = "DisplayString"
_SasQSFPVendor_Object = MibTableColumn
sasQSFPVendor = _SasQSFPVendor_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1, 2),
    _SasQSFPVendor_Type()
)
sasQSFPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasQSFPVendor.setStatus("current")


class _SasQSFPSerialNum_Type(DisplayString):
    """Custom type sasQSFPSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SasQSFPSerialNum_Type.__name__ = "DisplayString"
_SasQSFPSerialNum_Object = MibTableColumn
sasQSFPSerialNum = _SasQSFPSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1, 3),
    _SasQSFPSerialNum_Type()
)
sasQSFPSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasQSFPSerialNum.setStatus("current")
_SasQSFPType_Type = QSFPTech
_SasQSFPType_Object = MibTableColumn
sasQSFPType = _SasQSFPType_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1, 4),
    _SasQSFPType_Type()
)
sasQSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasQSFPType.setStatus("current")


class _SasQSFPPartNum_Type(DisplayString):
    """Custom type sasQSFPPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SasQSFPPartNum_Type.__name__ = "DisplayString"
_SasQSFPPartNum_Object = MibTableColumn
sasQSFPPartNum = _SasQSFPPartNum_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 2, 13, 1, 5),
    _SasQSFPPartNum_Type()
)
sasQSFPPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasQSFPPartNum.setStatus("current")
_BridgePorts_ObjectIdentity = ObjectIdentity
bridgePorts = _BridgePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3)
)
_FcPortInfoTable_Object = MibTable
fcPortInfoTable = _FcPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    fcPortInfoTable.setStatus("current")
_FcPortInfoEntry_Object = MibTableRow
fcPortInfoEntry = _FcPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1)
)
fcPortInfoEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "fcPortIndex"),
)
if mibBuilder.loadTexts:
    fcPortInfoEntry.setStatus("current")


class _FcPortIndex_Type(Integer32):
    """Custom type fcPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FcPortIndex_Type.__name__ = "Integer32"
_FcPortIndex_Object = MibTableColumn
fcPortIndex = _FcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 1),
    _FcPortIndex_Type()
)
fcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcPortIndex.setStatus("current")


class _FcPortPortNumber_Type(Integer32):
    """Custom type fcPortPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FcPortPortNumber_Type.__name__ = "Integer32"
_FcPortPortNumber_Object = MibTableColumn
fcPortPortNumber = _FcPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 2),
    _FcPortPortNumber_Type()
)
fcPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortPortNumber.setStatus("current")


class _FcPortOperationalState_Type(Integer32):
    """Custom type fcPortOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("unknown", -1))
    )


_FcPortOperationalState_Type.__name__ = "Integer32"
_FcPortOperationalState_Object = MibTableColumn
fcPortOperationalState = _FcPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 3),
    _FcPortOperationalState_Type()
)
fcPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortOperationalState.setStatus("current")


class _FcPortAdminState_Type(Integer32):
    """Custom type fcPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", -1))
    )


_FcPortAdminState_Type.__name__ = "Integer32"
_FcPortAdminState_Object = MibTableColumn
fcPortAdminState = _FcPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 4),
    _FcPortAdminState_Type()
)
fcPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortAdminState.setStatus("current")


class _FcPortDataRateNegotiated_Type(Integer32):
    """Custom type fcPortDataRateNegotiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("gb2", 2),
          ("gb4", 4),
          ("gb8", 8),
          ("unknown", -1))
    )


_FcPortDataRateNegotiated_Type.__name__ = "Integer32"
_FcPortDataRateNegotiated_Object = MibTableColumn
fcPortDataRateNegotiated = _FcPortDataRateNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 5),
    _FcPortDataRateNegotiated_Type()
)
fcPortDataRateNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortDataRateNegotiated.setStatus("current")


class _FcPortConnModeNegotiated_Type(Integer32):
    """Custom type fcPortConnModeNegotiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("ptp", 2),
          ("unknown", -1))
    )


_FcPortConnModeNegotiated_Type.__name__ = "Integer32"
_FcPortConnModeNegotiated_Object = MibTableColumn
fcPortConnModeNegotiated = _FcPortConnModeNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 6),
    _FcPortConnModeNegotiated_Type()
)
fcPortConnModeNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortConnModeNegotiated.setStatus("current")


class _FcPortDataRateConfigured_Type(Integer32):
    """Custom type fcPortDataRateConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", -1),
          ("gb2", 2),
          ("gb4", 4),
          ("gb8", 8))
    )


_FcPortDataRateConfigured_Type.__name__ = "Integer32"
_FcPortDataRateConfigured_Object = MibTableColumn
fcPortDataRateConfigured = _FcPortDataRateConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 7),
    _FcPortDataRateConfigured_Type()
)
fcPortDataRateConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortDataRateConfigured.setStatus("current")


class _FcPortConnModeConfigured_Type(Integer32):
    """Custom type fcPortConnModeConfigured based on Integer32"""
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
        *(("loop", 1),
          ("looppreferred", 3),
          ("ptp", 2),
          ("ptppreferred", 4))
    )


_FcPortConnModeConfigured_Type.__name__ = "Integer32"
_FcPortConnModeConfigured_Object = MibTableColumn
fcPortConnModeConfigured = _FcPortConnModeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 8),
    _FcPortConnModeConfigured_Type()
)
fcPortConnModeConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortConnModeConfigured.setStatus("current")


class _FcPortDataRateCapability_Type(Integer32):
    """Custom type fcPortDataRateCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("gb2", 2),
          ("gb4", 4),
          ("gb8", 8))
    )


_FcPortDataRateCapability_Type.__name__ = "Integer32"
_FcPortDataRateCapability_Object = MibTableColumn
fcPortDataRateCapability = _FcPortDataRateCapability_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 9),
    _FcPortDataRateCapability_Type()
)
fcPortDataRateCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortDataRateCapability.setStatus("current")
_FcPortNodeName_Type = DisplayWWN
_FcPortNodeName_Object = MibTableColumn
fcPortNodeName = _FcPortNodeName_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 10),
    _FcPortNodeName_Type()
)
fcPortNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortNodeName.setStatus("current")
_FcPortPortName_Type = DisplayWWN
_FcPortPortName_Object = MibTableColumn
fcPortPortName = _FcPortPortName_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 11),
    _FcPortPortName_Type()
)
fcPortPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortPortName.setStatus("current")
_FcPortPeerName_Type = DisplayWWN
_FcPortPeerName_Object = MibTableColumn
fcPortPeerName = _FcPortPeerName_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 1, 1, 12),
    _FcPortPeerName_Type()
)
fcPortPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPortPeerName.setStatus("current")
_FcPortStatisticsTable_Object = MibTable
fcPortStatisticsTable = _FcPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    fcPortStatisticsTable.setStatus("current")
_FcPortStatisticsEntry_Object = MibTableRow
fcPortStatisticsEntry = _FcPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1)
)
fcPortStatisticsEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "fcStatsIndex"),
)
if mibBuilder.loadTexts:
    fcPortStatisticsEntry.setStatus("current")


class _FcStatsIndex_Type(Integer32):
    """Custom type fcStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FcStatsIndex_Type.__name__ = "Integer32"
_FcStatsIndex_Object = MibTableColumn
fcStatsIndex = _FcStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 1),
    _FcStatsIndex_Type()
)
fcStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcStatsIndex.setStatus("current")
_FcStatsTxWords_Type = Unsigned32
_FcStatsTxWords_Object = MibTableColumn
fcStatsTxWords = _FcStatsTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 2),
    _FcStatsTxWords_Type()
)
fcStatsTxWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsTxWords.setStatus("current")
_FcStatsRxWords_Type = Unsigned32
_FcStatsRxWords_Object = MibTableColumn
fcStatsRxWords = _FcStatsRxWords_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 3),
    _FcStatsRxWords_Type()
)
fcStatsRxWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsRxWords.setStatus("current")
_FcStatsTimeSinceReset_Type = TimeInterval
_FcStatsTimeSinceReset_Object = MibTableColumn
fcStatsTimeSinceReset = _FcStatsTimeSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 4),
    _FcStatsTimeSinceReset_Type()
)
fcStatsTimeSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcStatsTimeSinceReset.setStatus("current")
_FcStatsErrLinkFailure_Type = Unsigned32
_FcStatsErrLinkFailure_Object = MibTableColumn
fcStatsErrLinkFailure = _FcStatsErrLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 5),
    _FcStatsErrLinkFailure_Type()
)
fcStatsErrLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrLinkFailure.setStatus("current")
_FcStatsErrLossOfSync_Type = Unsigned32
_FcStatsErrLossOfSync_Object = MibTableColumn
fcStatsErrLossOfSync = _FcStatsErrLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 6),
    _FcStatsErrLossOfSync_Type()
)
fcStatsErrLossOfSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrLossOfSync.setStatus("current")
_FcStatsErrInvalidCRC_Type = Unsigned32
_FcStatsErrInvalidCRC_Object = MibTableColumn
fcStatsErrInvalidCRC = _FcStatsErrInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 7),
    _FcStatsErrInvalidCRC_Type()
)
fcStatsErrInvalidCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrInvalidCRC.setStatus("current")
_FcStatsErrInvalidTxWords_Type = Unsigned32
_FcStatsErrInvalidTxWords_Object = MibTableColumn
fcStatsErrInvalidTxWords = _FcStatsErrInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 8),
    _FcStatsErrInvalidTxWords_Type()
)
fcStatsErrInvalidTxWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrInvalidTxWords.setStatus("current")
_FcStatsErrLipCount_Type = Unsigned32
_FcStatsErrLipCount_Object = MibTableColumn
fcStatsErrLipCount = _FcStatsErrLipCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 9),
    _FcStatsErrLipCount_Type()
)
fcStatsErrLipCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrLipCount.setStatus("current")
_FcStatsErrNOSCount_Type = Unsigned32
_FcStatsErrNOSCount_Object = MibTableColumn
fcStatsErrNOSCount = _FcStatsErrNOSCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 10),
    _FcStatsErrNOSCount_Type()
)
fcStatsErrNOSCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrNOSCount.setStatus("current")
_FcStatsErrSignalLoss_Type = Unsigned32
_FcStatsErrSignalLoss_Object = MibTableColumn
fcStatsErrSignalLoss = _FcStatsErrSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 11),
    _FcStatsErrSignalLoss_Type()
)
fcStatsErrSignalLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrSignalLoss.setStatus("current")
_FcStatsErrPrimitive_Type = Unsigned32
_FcStatsErrPrimitive_Object = MibTableColumn
fcStatsErrPrimitive = _FcStatsErrPrimitive_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 2, 1, 12),
    _FcStatsErrPrimitive_Type()
)
fcStatsErrPrimitive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcStatsErrPrimitive.setStatus("current")
_SasPortInfoTable_Object = MibTable
sasPortInfoTable = _SasPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    sasPortInfoTable.setStatus("current")
_SasPortInfoEntry_Object = MibTableRow
sasPortInfoEntry = _SasPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1)
)
sasPortInfoEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "sasPortIndex"),
)
if mibBuilder.loadTexts:
    sasPortInfoEntry.setStatus("current")


class _SasPortIndex_Type(Integer32):
    """Custom type sasPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SasPortIndex_Type.__name__ = "Integer32"
_SasPortIndex_Object = MibTableColumn
sasPortIndex = _SasPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 1),
    _SasPortIndex_Type()
)
sasPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sasPortIndex.setStatus("current")


class _SasPortPortNumber_Type(Integer32):
    """Custom type sasPortPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SasPortPortNumber_Type.__name__ = "Integer32"
_SasPortPortNumber_Object = MibTableColumn
sasPortPortNumber = _SasPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 2),
    _SasPortPortNumber_Type()
)
sasPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortPortNumber.setStatus("current")


class _SasPortOperationalState_Type(Integer32):
    """Custom type sasPortOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("degraded", 3),
          ("offline", 2),
          ("online", 1),
          ("unknown", -1))
    )


_SasPortOperationalState_Type.__name__ = "Integer32"
_SasPortOperationalState_Object = MibTableColumn
sasPortOperationalState = _SasPortOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 3),
    _SasPortOperationalState_Type()
)
sasPortOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortOperationalState.setStatus("current")
_SasPortPhy1State_Type = PHYStatus
_SasPortPhy1State_Object = MibTableColumn
sasPortPhy1State = _SasPortPhy1State_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 4),
    _SasPortPhy1State_Type()
)
sasPortPhy1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortPhy1State.setStatus("current")
_SasPortPhy2State_Type = PHYStatus
_SasPortPhy2State_Object = MibTableColumn
sasPortPhy2State = _SasPortPhy2State_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 5),
    _SasPortPhy2State_Type()
)
sasPortPhy2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortPhy2State.setStatus("current")
_SasPortPhy3State_Type = PHYStatus
_SasPortPhy3State_Object = MibTableColumn
sasPortPhy3State = _SasPortPhy3State_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 6),
    _SasPortPhy3State_Type()
)
sasPortPhy3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortPhy3State.setStatus("current")
_SasPortPhy4State_Type = PHYStatus
_SasPortPhy4State_Object = MibTableColumn
sasPortPhy4State = _SasPortPhy4State_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 7),
    _SasPortPhy4State_Type()
)
sasPortPhy4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortPhy4State.setStatus("current")


class _SasPortAdminState_Type(Integer32):
    """Custom type sasPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", -1))
    )


_SasPortAdminState_Type.__name__ = "Integer32"
_SasPortAdminState_Object = MibTableColumn
sasPortAdminState = _SasPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 8),
    _SasPortAdminState_Type()
)
sasPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortAdminState.setStatus("current")


class _SasPortDataRateCapability_Type(Integer32):
    """Custom type sasPortDataRateCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gb1point5", 1),
          ("gb3", 3),
          ("gb6", 6))
    )


_SasPortDataRateCapability_Type.__name__ = "Integer32"
_SasPortDataRateCapability_Object = MibTableColumn
sasPortDataRateCapability = _SasPortDataRateCapability_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 9),
    _SasPortDataRateCapability_Type()
)
sasPortDataRateCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortDataRateCapability.setStatus("current")


class _SasPortDataRateNegotiated_Type(Integer32):
    """Custom type sasPortDataRateNegotiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gb1point5", 1),
          ("gb3", 3),
          ("gb6", 6))
    )


_SasPortDataRateNegotiated_Type.__name__ = "Integer32"
_SasPortDataRateNegotiated_Object = MibTableColumn
sasPortDataRateNegotiated = _SasPortDataRateNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 10),
    _SasPortDataRateNegotiated_Type()
)
sasPortDataRateNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortDataRateNegotiated.setStatus("current")
_SasPortAddress_Type = DisplayWWN
_SasPortAddress_Object = MibTableColumn
sasPortAddress = _SasPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 3, 1, 11),
    _SasPortAddress_Type()
)
sasPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPortAddress.setStatus("current")
_SasPhyStatisticsTable_Object = MibTable
sasPhyStatisticsTable = _SasPhyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    sasPhyStatisticsTable.setStatus("current")
_SasPhyStatisticsEntry_Object = MibTableRow
sasPhyStatisticsEntry = _SasPhyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1)
)
sasPhyStatisticsEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "sasPhyStatsIndex"),
)
if mibBuilder.loadTexts:
    sasPhyStatisticsEntry.setStatus("current")


class _SasPhyStatsIndex_Type(Integer32):
    """Custom type sasPhyStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SasPhyStatsIndex_Type.__name__ = "Integer32"
_SasPhyStatsIndex_Object = MibTableColumn
sasPhyStatsIndex = _SasPhyStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 1),
    _SasPhyStatsIndex_Type()
)
sasPhyStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sasPhyStatsIndex.setStatus("current")
_SasPhyStatsTimeSinceReset_Type = TimeInterval
_SasPhyStatsTimeSinceReset_Object = MibTableColumn
sasPhyStatsTimeSinceReset = _SasPhyStatsTimeSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 2),
    _SasPhyStatsTimeSinceReset_Type()
)
sasPhyStatsTimeSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sasPhyStatsTimeSinceReset.setStatus("current")
_SasPhyStatsErrLinkChanged_Type = Unsigned32
_SasPhyStatsErrLinkChanged_Object = MibTableColumn
sasPhyStatsErrLinkChanged = _SasPhyStatsErrLinkChanged_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 3),
    _SasPhyStatsErrLinkChanged_Type()
)
sasPhyStatsErrLinkChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrLinkChanged.setStatus("current")
_SasPhyStatsErrInvalidCRC_Type = Unsigned32
_SasPhyStatsErrInvalidCRC_Object = MibTableColumn
sasPhyStatsErrInvalidCRC = _SasPhyStatsErrInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 4),
    _SasPhyStatsErrInvalidCRC_Type()
)
sasPhyStatsErrInvalidCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrInvalidCRC.setStatus("current")
_SasPhyStatsErrPhyReset_Type = Unsigned32
_SasPhyStatsErrPhyReset_Object = MibTableColumn
sasPhyStatsErrPhyReset = _SasPhyStatsErrPhyReset_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 5),
    _SasPhyStatsErrPhyReset_Type()
)
sasPhyStatsErrPhyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrPhyReset.setStatus("current")
_SasPhyStatsErrLossOfSync_Type = Unsigned32
_SasPhyStatsErrLossOfSync_Object = MibTableColumn
sasPhyStatsErrLossOfSync = _SasPhyStatsErrLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 6),
    _SasPhyStatsErrLossOfSync_Type()
)
sasPhyStatsErrLossOfSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrLossOfSync.setStatus("current")
_SasPhyStatsErrDisparityCount_Type = Unsigned32
_SasPhyStatsErrDisparityCount_Object = MibTableColumn
sasPhyStatsErrDisparityCount = _SasPhyStatsErrDisparityCount_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 7),
    _SasPhyStatsErrDisparityCount_Type()
)
sasPhyStatsErrDisparityCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrDisparityCount.setStatus("current")
_SasPhyStatsErrInvalidDwords_Type = Unsigned32
_SasPhyStatsErrInvalidDwords_Object = MibTableColumn
sasPhyStatsErrInvalidDwords = _SasPhyStatsErrInvalidDwords_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 3, 4, 1, 8),
    _SasPhyStatsErrInvalidDwords_Type()
)
sasPhyStatsErrInvalidDwords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sasPhyStatsErrInvalidDwords.setStatus("current")
_BridgeConfig_ObjectIdentity = ObjectIdentity
bridgeConfig = _BridgeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 4)
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
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 4, 1),
    _TrapsEnabled_Type()
)
trapsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsEnabled.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 4, 2),
    _SnmpUpdatesEnabled_Type()
)
snmpUpdatesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUpdatesEnabled.setStatus("current")
_BridgeTrapInfo_ObjectIdentity = ObjectIdentity
bridgeTrapInfo = _BridgeTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5)
)
_TrapMaxClients_Type = Integer32
_TrapMaxClients_Object = MibScalar
trapMaxClients = _TrapMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 1),
    _TrapMaxClients_Type()
)
trapMaxClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapMaxClients.setStatus("current")
_TrapClientTable_Object = MibTable
trapClientTable = _TrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    trapClientTable.setStatus("current")
_TrapClientEntry_Object = MibTableRow
trapClientEntry = _TrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2, 1)
)
trapClientEntry.setIndexNames(
    (0, "ATTO6500N-MIB", "trapClientIndex"),
)
if mibBuilder.loadTexts:
    trapClientEntry.setStatus("current")


class _TrapClientIndex_Type(Integer32):
    """Custom type trapClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_TrapClientIndex_Type.__name__ = "Integer32"
_TrapClientIndex_Object = MibTableColumn
trapClientIndex = _TrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2, 1, 1),
    _TrapClientIndex_Type()
)
trapClientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapClientIndex.setStatus("current")


class _TrapClientIpAddress_Type(DisplayString):
    """Custom type trapClientIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TrapClientIpAddress_Type.__name__ = "DisplayString"
_TrapClientIpAddress_Object = MibTableColumn
trapClientIpAddress = _TrapClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2, 1, 2),
    _TrapClientIpAddress_Type()
)
trapClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientIpAddress.setStatus("current")


class _TrapClientPort_Type(Integer32):
    """Custom type trapClientPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapClientPort_Type.__name__ = "Integer32"
_TrapClientPort_Object = MibTableColumn
trapClientPort = _TrapClientPort_Object(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2, 1, 3),
    _TrapClientPort_Type()
)
trapClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientPort.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 5, 2, 1, 4),
    _TrapClientFilter_Type()
)
trapClientFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientFilter.setStatus("current")
_BridgeMIBConformance_ObjectIdentity = ObjectIdentity
bridgeMIBConformance = _BridgeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6)
)
_BridgeMIBCompliances_ObjectIdentity = ObjectIdentity
bridgeMIBCompliances = _BridgeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 1)
)
_BridgeMIBGroups_ObjectIdentity = ObjectIdentity
bridgeMIBGroups = _BridgeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2)
)
_AttoModules_ObjectIdentity = ObjectIdentity
attoModules = _AttoModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 3)
)
_AttoAgentCapability_ObjectIdentity = ObjectIdentity
attoAgentCapability = _AttoAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 4)
)

# Managed Objects groups

bridgeIdentityBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 1)
)
bridgeIdentityBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "bridgeUniqueId"),
        ("ATTO6500N-MIB", "vendorID"),
        ("ATTO6500N-MIB", "modelName"),
        ("ATTO6500N-MIB", "primaryFirmwareRevision"),
        ("ATTO6500N-MIB", "primaryFirmwareBuildDate"),
        ("ATTO6500N-MIB", "hardwareVersion"),
        ("ATTO6500N-MIB", "secondaryFirmwareRevision"),
        ("ATTO6500N-MIB", "secondaryFirmwareBuildDate"),
        ("ATTO6500N-MIB", "serialNumber"),
        ("ATTO6500N-MIB", "bridgeName"))
)
if mibBuilder.loadTexts:
    bridgeIdentityBasicGroup.setStatus("current")

bridgeChassisBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 2)
)
bridgeChassisBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "lastReboot"),
        ("ATTO6500N-MIB", "uptime"),
        ("ATTO6500N-MIB", "lastRebootReason"),
        ("ATTO6500N-MIB", "minimumOperatingTemp"),
        ("ATTO6500N-MIB", "maximumOperatingTemp"),
        ("ATTO6500N-MIB", "temperatureHighAlertSetting"),
        ("ATTO6500N-MIB", "temperatureLowAlertSetting"),
        ("ATTO6500N-MIB", "chassisTemperature"),
        ("ATTO6500N-MIB", "chassisTemperatureStatus"),
        ("ATTO6500N-MIB", "dramSingleBitErrorCount"),
        ("ATTO6500N-MIB", "chassisThroughputStatus"),
        ("ATTO6500N-MIB", "fcSFPVendor"),
        ("ATTO6500N-MIB", "fcSFPSerialNum"),
        ("ATTO6500N-MIB", "fcSFPPartNum"),
        ("ATTO6500N-MIB", "fcSFPDataRateCapability"),
        ("ATTO6500N-MIB", "sasQSFPVendor"),
        ("ATTO6500N-MIB", "sasQSFPSerialNum"),
        ("ATTO6500N-MIB", "sasQSFPType"),
        ("ATTO6500N-MIB", "sasQSFPPartNum"))
)
if mibBuilder.loadTexts:
    bridgeChassisBasicGroup.setStatus("current")

bridgFcPortInfoBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 3)
)
bridgFcPortInfoBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "fcPortPortNumber"),
        ("ATTO6500N-MIB", "fcPortOperationalState"),
        ("ATTO6500N-MIB", "fcPortAdminState"),
        ("ATTO6500N-MIB", "fcPortDataRateNegotiated"),
        ("ATTO6500N-MIB", "fcPortConnModeNegotiated"),
        ("ATTO6500N-MIB", "fcPortDataRateConfigured"),
        ("ATTO6500N-MIB", "fcPortConnModeConfigured"),
        ("ATTO6500N-MIB", "fcPortDataRateCapability"),
        ("ATTO6500N-MIB", "fcPortNodeName"),
        ("ATTO6500N-MIB", "fcPortPortName"),
        ("ATTO6500N-MIB", "fcPortPeerName"))
)
if mibBuilder.loadTexts:
    bridgFcPortInfoBasicGroup.setStatus("current")

bridgeFcPortStatisicsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 4)
)
bridgeFcPortStatisicsBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "fcStatsTxWords"),
        ("ATTO6500N-MIB", "fcStatsRxWords"),
        ("ATTO6500N-MIB", "fcStatsTimeSinceReset"),
        ("ATTO6500N-MIB", "fcStatsErrLinkFailure"),
        ("ATTO6500N-MIB", "fcStatsErrLossOfSync"),
        ("ATTO6500N-MIB", "fcStatsErrInvalidCRC"),
        ("ATTO6500N-MIB", "fcStatsErrInvalidTxWords"),
        ("ATTO6500N-MIB", "fcStatsErrLipCount"),
        ("ATTO6500N-MIB", "fcStatsErrNOSCount"),
        ("ATTO6500N-MIB", "fcStatsErrSignalLoss"),
        ("ATTO6500N-MIB", "fcStatsErrPrimitive"))
)
if mibBuilder.loadTexts:
    bridgeFcPortStatisicsBasicGroup.setStatus("current")

bridgeSasPortInfoBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 5)
)
bridgeSasPortInfoBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "sasPortPortNumber"),
        ("ATTO6500N-MIB", "sasPortOperationalState"),
        ("ATTO6500N-MIB", "sasPortPhy1State"),
        ("ATTO6500N-MIB", "sasPortPhy2State"),
        ("ATTO6500N-MIB", "sasPortPhy3State"),
        ("ATTO6500N-MIB", "sasPortPhy4State"),
        ("ATTO6500N-MIB", "sasPortAdminState"),
        ("ATTO6500N-MIB", "sasPortDataRateCapability"),
        ("ATTO6500N-MIB", "sasPortDataRateNegotiated"),
        ("ATTO6500N-MIB", "sasPortAddress"))
)
if mibBuilder.loadTexts:
    bridgeSasPortInfoBasicGroup.setStatus("current")

bridgeSasPortStatisicsBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 6)
)
bridgeSasPortStatisicsBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "sasPhyStatsTimeSinceReset"),
        ("ATTO6500N-MIB", "sasPhyStatsErrLinkChanged"),
        ("ATTO6500N-MIB", "sasPhyStatsErrInvalidCRC"),
        ("ATTO6500N-MIB", "sasPhyStatsErrPhyReset"),
        ("ATTO6500N-MIB", "sasPhyStatsErrLossOfSync"),
        ("ATTO6500N-MIB", "sasPhyStatsErrDisparityCount"),
        ("ATTO6500N-MIB", "sasPhyStatsErrInvalidDwords"))
)
if mibBuilder.loadTexts:
    bridgeSasPortStatisicsBasicGroup.setStatus("current")

bridgeConfigBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 7)
)
bridgeConfigBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "trapsEnabled"),
        ("ATTO6500N-MIB", "snmpUpdatesEnabled"))
)
if mibBuilder.loadTexts:
    bridgeConfigBasicGroup.setStatus("current")

bridgeTrapInfoBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 8)
)
bridgeTrapInfoBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "trapMaxClients"),
        ("ATTO6500N-MIB", "trapClientIpAddress"),
        ("ATTO6500N-MIB", "trapClientPort"),
        ("ATTO6500N-MIB", "trapClientFilter"))
)
if mibBuilder.loadTexts:
    bridgeTrapInfoBasicGroup.setStatus("current")


# Notification objects

bridgeTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 0, 1)
)
bridgeTemperatureWarning.setObjects(
      *(("ATTO6500N-MIB", "chassisTemperatureStatus"),
        ("ATTO6500N-MIB", "chassisTemperature"))
)
if mibBuilder.loadTexts:
    bridgeTemperatureWarning.setStatus(
        "current"
    )

fcPortTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 0, 2)
)
fcPortTransition.setObjects(
      *(("ATTO6500N-MIB", "fcPortPortNumber"),
        ("ATTO6500N-MIB", "fcPortOperationalState"))
)
if mibBuilder.loadTexts:
    fcPortTransition.setStatus(
        "current"
    )

sasPortTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 0, 3)
)
sasPortTransition.setObjects(
      *(("ATTO6500N-MIB", "sasPortPortNumber"),
        ("ATTO6500N-MIB", "sasPortOperationalState"))
)
if mibBuilder.loadTexts:
    sasPortTransition.setStatus(
        "current"
    )

bridgeThroughputWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 0, 4)
)
bridgeThroughputWarning.setObjects(
    ("ATTO6500N-MIB", "chassisThroughputStatus")
)
if mibBuilder.loadTexts:
    bridgeThroughputWarning.setStatus(
        "current"
    )


# Notifications groups

bridgeTrapsBasicGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 2, 9)
)
bridgeTrapsBasicGroup.setObjects(
      *(("ATTO6500N-MIB", "bridgeTemperatureWarning"),
        ("ATTO6500N-MIB", "fcPortTransition"),
        ("ATTO6500N-MIB", "sasPortTransition"),
        ("ATTO6500N-MIB", "bridgeThroughputWarning"))
)
if mibBuilder.loadTexts:
    bridgeTrapsBasicGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bridgeBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4547, 2, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    bridgeBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATTO6500N-MIB",
    **{"DisplayWWN": DisplayWWN,
       "QSFPTech": QSFPTech,
       "PHYStatus": PHYStatus,
       "attotech": attotech,
       "attoProducts": attoProducts,
       "attoMgmt": attoMgmt,
       "bridge": bridge,
       "bridgeTraps": bridgeTraps,
       "bridgeTemperatureWarning": bridgeTemperatureWarning,
       "fcPortTransition": fcPortTransition,
       "sasPortTransition": sasPortTransition,
       "bridgeThroughputWarning": bridgeThroughputWarning,
       "bridgeIdentity": bridgeIdentity,
       "bridgeUniqueId": bridgeUniqueId,
       "vendorID": vendorID,
       "modelName": modelName,
       "primaryFirmwareRevision": primaryFirmwareRevision,
       "primaryFirmwareBuildDate": primaryFirmwareBuildDate,
       "hardwareVersion": hardwareVersion,
       "secondaryFirmwareRevision": secondaryFirmwareRevision,
       "secondaryFirmwareBuildDate": secondaryFirmwareBuildDate,
       "serialNumber": serialNumber,
       "bridgeName": bridgeName,
       "bridgeChassis": bridgeChassis,
       "lastReboot": lastReboot,
       "uptime": uptime,
       "lastRebootReason": lastRebootReason,
       "minimumOperatingTemp": minimumOperatingTemp,
       "maximumOperatingTemp": maximumOperatingTemp,
       "temperatureHighAlertSetting": temperatureHighAlertSetting,
       "temperatureLowAlertSetting": temperatureLowAlertSetting,
       "chassisTemperature": chassisTemperature,
       "chassisTemperatureStatus": chassisTemperatureStatus,
       "dramSingleBitErrorCount": dramSingleBitErrorCount,
       "chassisThroughputStatus": chassisThroughputStatus,
       "fcSFPInfoTable": fcSFPInfoTable,
       "fcSFPInfoEntry": fcSFPInfoEntry,
       "fcSFPIndex": fcSFPIndex,
       "fcSFPVendor": fcSFPVendor,
       "fcSFPSerialNum": fcSFPSerialNum,
       "fcSFPPartNum": fcSFPPartNum,
       "fcSFPDataRateCapability": fcSFPDataRateCapability,
       "sasQSFPInfoTable": sasQSFPInfoTable,
       "sasQSFPInfoEntry": sasQSFPInfoEntry,
       "sasQSFPIndex": sasQSFPIndex,
       "sasQSFPVendor": sasQSFPVendor,
       "sasQSFPSerialNum": sasQSFPSerialNum,
       "sasQSFPType": sasQSFPType,
       "sasQSFPPartNum": sasQSFPPartNum,
       "bridgePorts": bridgePorts,
       "fcPortInfoTable": fcPortInfoTable,
       "fcPortInfoEntry": fcPortInfoEntry,
       "fcPortIndex": fcPortIndex,
       "fcPortPortNumber": fcPortPortNumber,
       "fcPortOperationalState": fcPortOperationalState,
       "fcPortAdminState": fcPortAdminState,
       "fcPortDataRateNegotiated": fcPortDataRateNegotiated,
       "fcPortConnModeNegotiated": fcPortConnModeNegotiated,
       "fcPortDataRateConfigured": fcPortDataRateConfigured,
       "fcPortConnModeConfigured": fcPortConnModeConfigured,
       "fcPortDataRateCapability": fcPortDataRateCapability,
       "fcPortNodeName": fcPortNodeName,
       "fcPortPortName": fcPortPortName,
       "fcPortPeerName": fcPortPeerName,
       "fcPortStatisticsTable": fcPortStatisticsTable,
       "fcPortStatisticsEntry": fcPortStatisticsEntry,
       "fcStatsIndex": fcStatsIndex,
       "fcStatsTxWords": fcStatsTxWords,
       "fcStatsRxWords": fcStatsRxWords,
       "fcStatsTimeSinceReset": fcStatsTimeSinceReset,
       "fcStatsErrLinkFailure": fcStatsErrLinkFailure,
       "fcStatsErrLossOfSync": fcStatsErrLossOfSync,
       "fcStatsErrInvalidCRC": fcStatsErrInvalidCRC,
       "fcStatsErrInvalidTxWords": fcStatsErrInvalidTxWords,
       "fcStatsErrLipCount": fcStatsErrLipCount,
       "fcStatsErrNOSCount": fcStatsErrNOSCount,
       "fcStatsErrSignalLoss": fcStatsErrSignalLoss,
       "fcStatsErrPrimitive": fcStatsErrPrimitive,
       "sasPortInfoTable": sasPortInfoTable,
       "sasPortInfoEntry": sasPortInfoEntry,
       "sasPortIndex": sasPortIndex,
       "sasPortPortNumber": sasPortPortNumber,
       "sasPortOperationalState": sasPortOperationalState,
       "sasPortPhy1State": sasPortPhy1State,
       "sasPortPhy2State": sasPortPhy2State,
       "sasPortPhy3State": sasPortPhy3State,
       "sasPortPhy4State": sasPortPhy4State,
       "sasPortAdminState": sasPortAdminState,
       "sasPortDataRateCapability": sasPortDataRateCapability,
       "sasPortDataRateNegotiated": sasPortDataRateNegotiated,
       "sasPortAddress": sasPortAddress,
       "sasPhyStatisticsTable": sasPhyStatisticsTable,
       "sasPhyStatisticsEntry": sasPhyStatisticsEntry,
       "sasPhyStatsIndex": sasPhyStatsIndex,
       "sasPhyStatsTimeSinceReset": sasPhyStatsTimeSinceReset,
       "sasPhyStatsErrLinkChanged": sasPhyStatsErrLinkChanged,
       "sasPhyStatsErrInvalidCRC": sasPhyStatsErrInvalidCRC,
       "sasPhyStatsErrPhyReset": sasPhyStatsErrPhyReset,
       "sasPhyStatsErrLossOfSync": sasPhyStatsErrLossOfSync,
       "sasPhyStatsErrDisparityCount": sasPhyStatsErrDisparityCount,
       "sasPhyStatsErrInvalidDwords": sasPhyStatsErrInvalidDwords,
       "bridgeConfig": bridgeConfig,
       "trapsEnabled": trapsEnabled,
       "snmpUpdatesEnabled": snmpUpdatesEnabled,
       "bridgeTrapInfo": bridgeTrapInfo,
       "trapMaxClients": trapMaxClients,
       "trapClientTable": trapClientTable,
       "trapClientEntry": trapClientEntry,
       "trapClientIndex": trapClientIndex,
       "trapClientIpAddress": trapClientIpAddress,
       "trapClientPort": trapClientPort,
       "trapClientFilter": trapClientFilter,
       "bridgeMIBConformance": bridgeMIBConformance,
       "bridgeMIBCompliances": bridgeMIBCompliances,
       "bridgeBasicCompliance": bridgeBasicCompliance,
       "bridgeMIBGroups": bridgeMIBGroups,
       "bridgeIdentityBasicGroup": bridgeIdentityBasicGroup,
       "bridgeChassisBasicGroup": bridgeChassisBasicGroup,
       "bridgFcPortInfoBasicGroup": bridgFcPortInfoBasicGroup,
       "bridgeFcPortStatisicsBasicGroup": bridgeFcPortStatisicsBasicGroup,
       "bridgeSasPortInfoBasicGroup": bridgeSasPortInfoBasicGroup,
       "bridgeSasPortStatisicsBasicGroup": bridgeSasPortStatisicsBasicGroup,
       "bridgeConfigBasicGroup": bridgeConfigBasicGroup,
       "bridgeTrapInfoBasicGroup": bridgeTrapInfoBasicGroup,
       "bridgeTrapsBasicGroup": bridgeTrapsBasicGroup,
       "attoModules": attoModules,
       "attoAgentCapability": attoAgentCapability}
)
