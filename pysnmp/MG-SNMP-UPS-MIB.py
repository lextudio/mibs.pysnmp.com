# SNMP MIB module (MG-SNMP-UPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MG-SNMP-UPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:21 2024
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

_MerlinGerin_ObjectIdentity = ObjectIdentity
merlinGerin = _MerlinGerin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705)
)
_Upsmg_ObjectIdentity = ObjectIdentity
upsmg = _Upsmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1)
)
_UpsmgIdent_ObjectIdentity = ObjectIdentity
upsmgIdent = _UpsmgIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 1)
)


class _UpsmgIdentFamilyName_Type(DisplayString):
    """Custom type upsmgIdentFamilyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentFamilyName_Type.__name__ = "DisplayString"
_UpsmgIdentFamilyName_Object = MibScalar
upsmgIdentFamilyName = _UpsmgIdentFamilyName_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 1),
    _UpsmgIdentFamilyName_Type()
)
upsmgIdentFamilyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentFamilyName.setStatus("mandatory")


class _UpsmgIdentModelName_Type(DisplayString):
    """Custom type upsmgIdentModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentModelName_Type.__name__ = "DisplayString"
_UpsmgIdentModelName_Object = MibScalar
upsmgIdentModelName = _UpsmgIdentModelName_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 2),
    _UpsmgIdentModelName_Type()
)
upsmgIdentModelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentModelName.setStatus("mandatory")


class _UpsmgIdentRevisionLevel_Type(DisplayString):
    """Custom type upsmgIdentRevisionLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentRevisionLevel_Type.__name__ = "DisplayString"
_UpsmgIdentRevisionLevel_Object = MibScalar
upsmgIdentRevisionLevel = _UpsmgIdentRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 3),
    _UpsmgIdentRevisionLevel_Type()
)
upsmgIdentRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentRevisionLevel.setStatus("mandatory")


class _UpsmgIdentFirmwareVersion_Type(DisplayString):
    """Custom type upsmgIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentFirmwareVersion_Type.__name__ = "DisplayString"
_UpsmgIdentFirmwareVersion_Object = MibScalar
upsmgIdentFirmwareVersion = _UpsmgIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 4),
    _UpsmgIdentFirmwareVersion_Type()
)
upsmgIdentFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentFirmwareVersion.setStatus("mandatory")


class _UpsmgIdentUserID_Type(DisplayString):
    """Custom type upsmgIdentUserID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentUserID_Type.__name__ = "DisplayString"
_UpsmgIdentUserID_Object = MibScalar
upsmgIdentUserID = _UpsmgIdentUserID_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 5),
    _UpsmgIdentUserID_Type()
)
upsmgIdentUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentUserID.setStatus("mandatory")


class _UpsmgIdentInstallationDate_Type(DisplayString):
    """Custom type upsmgIdentInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentInstallationDate_Type.__name__ = "DisplayString"
_UpsmgIdentInstallationDate_Object = MibScalar
upsmgIdentInstallationDate = _UpsmgIdentInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 6),
    _UpsmgIdentInstallationDate_Type()
)
upsmgIdentInstallationDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentInstallationDate.setStatus("mandatory")


class _UpsmgIdentSerialNumber_Type(DisplayString):
    """Custom type upsmgIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgIdentSerialNumber_Type.__name__ = "DisplayString"
_UpsmgIdentSerialNumber_Object = MibScalar
upsmgIdentSerialNumber = _UpsmgIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 1, 7),
    _UpsmgIdentSerialNumber_Type()
)
upsmgIdentSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgIdentSerialNumber.setStatus("mandatory")
_UpsmgManagement_ObjectIdentity = ObjectIdentity
upsmgManagement = _UpsmgManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 2)
)
_UpsmgManagersNum_Type = Integer32
_UpsmgManagersNum_Object = MibScalar
upsmgManagersNum = _UpsmgManagersNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 1),
    _UpsmgManagersNum_Type()
)
upsmgManagersNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgManagersNum.setStatus("mandatory")
_UpsmgManagersTable_Object = MibTable
upsmgManagersTable = _UpsmgManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2)
)
if mibBuilder.loadTexts:
    upsmgManagersTable.setStatus("mandatory")
_UpsmgManagersEntry_Object = MibTableRow
upsmgManagersEntry = _UpsmgManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1)
)
upsmgManagersEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgmanagerIndex"),
)
if mibBuilder.loadTexts:
    upsmgManagersEntry.setStatus("mandatory")


class _MgmanagerIndex_Type(Integer32):
    """Custom type mgmanagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgmanagerIndex_Type.__name__ = "Integer32"
_MgmanagerIndex_Object = MibTableColumn
mgmanagerIndex = _MgmanagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 1),
    _MgmanagerIndex_Type()
)
mgmanagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmanagerIndex.setStatus("mandatory")
_MgmanagerDeviceNumber_Type = Integer32
_MgmanagerDeviceNumber_Object = MibTableColumn
mgmanagerDeviceNumber = _MgmanagerDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 2),
    _MgmanagerDeviceNumber_Type()
)
mgmanagerDeviceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerDeviceNumber.setStatus("mandatory")


class _MgmanagerNMSType_Type(Integer32):
    """Custom type mgmanagerNMSType based on Integer32"""
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
        *(("autolearning", 10),
          ("decnetview", 2),
          ("dview", 4),
          ("hpopenview", 5),
          ("ibmnetview", 8),
          ("novellnms", 7),
          ("other", 9),
          ("sunnetmanager", 6),
          ("umclient", 1),
          ("umview", 3))
    )


_MgmanagerNMSType_Type.__name__ = "Integer32"
_MgmanagerNMSType_Object = MibTableColumn
mgmanagerNMSType = _MgmanagerNMSType_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 3),
    _MgmanagerNMSType_Type()
)
mgmanagerNMSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerNMSType.setStatus("mandatory")


class _MgmanagerCommType_Type(Integer32):
    """Custom type mgmanagerCommType based on Integer32"""
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
        *(("cmip", 3),
          ("invalid", 2),
          ("other", 1),
          ("snmpv1", 4),
          ("snmpv2", 5))
    )


_MgmanagerCommType_Type.__name__ = "Integer32"
_MgmanagerCommType_Object = MibTableColumn
mgmanagerCommType = _MgmanagerCommType_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 4),
    _MgmanagerCommType_Type()
)
mgmanagerCommType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerCommType.setStatus("mandatory")


class _MgmanagerDescr_Type(DisplayString):
    """Custom type mgmanagerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgmanagerDescr_Type.__name__ = "DisplayString"
_MgmanagerDescr_Object = MibTableColumn
mgmanagerDescr = _MgmanagerDescr_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 5),
    _MgmanagerDescr_Type()
)
mgmanagerDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerDescr.setStatus("mandatory")
_MgmanagerAddress_Type = IpAddress
_MgmanagerAddress_Object = MibTableColumn
mgmanagerAddress = _MgmanagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 6),
    _MgmanagerAddress_Type()
)
mgmanagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerAddress.setStatus("mandatory")


class _MgmanagerCommunity_Type(DisplayString):
    """Custom type mgmanagerCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgmanagerCommunity_Type.__name__ = "DisplayString"
_MgmanagerCommunity_Object = MibTableColumn
mgmanagerCommunity = _MgmanagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 7),
    _MgmanagerCommunity_Type()
)
mgmanagerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerCommunity.setStatus("mandatory")
_MgmanagerSeverityLevel_Type = Integer32
_MgmanagerSeverityLevel_Object = MibTableColumn
mgmanagerSeverityLevel = _MgmanagerSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 8),
    _MgmanagerSeverityLevel_Type()
)
mgmanagerSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerSeverityLevel.setStatus("mandatory")


class _MgmanagerTrapAck_Type(Integer32):
    """Custom type mgmanagerTrapAck based on Integer32"""
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
        *(("cpqnoack", 5),
          ("mgack", 1),
          ("mgacks", 4),
          ("mgnoack", 2),
          ("stdnomg", 3))
    )


_MgmanagerTrapAck_Type.__name__ = "Integer32"
_MgmanagerTrapAck_Object = MibTableColumn
mgmanagerTrapAck = _MgmanagerTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 2, 2, 1, 9),
    _MgmanagerTrapAck_Type()
)
mgmanagerTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmanagerTrapAck.setStatus("mandatory")
_UpsmgReceptacle_ObjectIdentity = ObjectIdentity
upsmgReceptacle = _UpsmgReceptacle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 3)
)
_UpsmgReceptaclesNum_Type = Integer32
_UpsmgReceptaclesNum_Object = MibScalar
upsmgReceptaclesNum = _UpsmgReceptaclesNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 1),
    _UpsmgReceptaclesNum_Type()
)
upsmgReceptaclesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgReceptaclesNum.setStatus("mandatory")
_UpsmgReceptaclesTable_Object = MibTable
upsmgReceptaclesTable = _UpsmgReceptaclesTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2)
)
if mibBuilder.loadTexts:
    upsmgReceptaclesTable.setStatus("mandatory")
_UpsmgReceptaclesEntry_Object = MibTableRow
upsmgReceptaclesEntry = _UpsmgReceptaclesEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1)
)
upsmgReceptaclesEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
)
if mibBuilder.loadTexts:
    upsmgReceptaclesEntry.setStatus("mandatory")


class _MgreceptacleIndex_Type(Integer32):
    """Custom type mgreceptacleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgreceptacleIndex_Type.__name__ = "Integer32"
_MgreceptacleIndex_Object = MibTableColumn
mgreceptacleIndex = _MgreceptacleIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 1),
    _MgreceptacleIndex_Type()
)
mgreceptacleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleIndex.setStatus("mandatory")
_MgreceptacleLevel_Type = Integer32
_MgreceptacleLevel_Object = MibTableColumn
mgreceptacleLevel = _MgreceptacleLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 2),
    _MgreceptacleLevel_Type()
)
mgreceptacleLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleLevel.setStatus("mandatory")


class _MgreceptacleType_Type(DisplayString):
    """Custom type mgreceptacleType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgreceptacleType_Type.__name__ = "DisplayString"
_MgreceptacleType_Object = MibTableColumn
mgreceptacleType = _MgreceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 3),
    _MgreceptacleType_Type()
)
mgreceptacleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleType.setStatus("mandatory")


class _MgreceptacleIdent_Type(DisplayString):
    """Custom type mgreceptacleIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgreceptacleIdent_Type.__name__ = "DisplayString"
_MgreceptacleIdent_Object = MibTableColumn
mgreceptacleIdent = _MgreceptacleIdent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 4),
    _MgreceptacleIdent_Type()
)
mgreceptacleIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleIdent.setStatus("mandatory")


class _MgreceptacleState_Type(Integer32):
    """Custom type mgreceptacleState based on Integer32"""
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
        *(("controlOFF", 6),
          ("controlON", 5),
          ("manualOFF", 2),
          ("manualON", 1),
          ("normalOFF", 4),
          ("normalON", 3),
          ("scheduleOFF", 8),
          ("scheduleON", 7))
    )


_MgreceptacleState_Type.__name__ = "Integer32"
_MgreceptacleState_Object = MibTableColumn
mgreceptacleState = _MgreceptacleState_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 5),
    _MgreceptacleState_Type()
)
mgreceptacleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleState.setStatus("mandatory")
_MgreceptacleReceptacle_Type = Integer32
_MgreceptacleReceptacle_Object = MibTableColumn
mgreceptacleReceptacle = _MgreceptacleReceptacle_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 6),
    _MgreceptacleReceptacle_Type()
)
mgreceptacleReceptacle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleReceptacle.setStatus("mandatory")
_MgreceptaclePowerCons_Type = Integer32
_MgreceptaclePowerCons_Object = MibTableColumn
mgreceptaclePowerCons = _MgreceptaclePowerCons_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 7),
    _MgreceptaclePowerCons_Type()
)
mgreceptaclePowerCons.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptaclePowerCons.setStatus("mandatory")
_MgreceptacleOverload_Type = Integer32
_MgreceptacleOverload_Object = MibTableColumn
mgreceptacleOverload = _MgreceptacleOverload_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 8),
    _MgreceptacleOverload_Type()
)
mgreceptacleOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleOverload.setStatus("mandatory")
_MgreceptacleAutonomy_Type = Integer32
_MgreceptacleAutonomy_Object = MibTableColumn
mgreceptacleAutonomy = _MgreceptacleAutonomy_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 3, 2, 1, 9),
    _MgreceptacleAutonomy_Type()
)
mgreceptacleAutonomy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleAutonomy.setStatus("mandatory")
_UpsmgConfig_ObjectIdentity = ObjectIdentity
upsmgConfig = _UpsmgConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 4)
)


class _UpsmgConfigBatteryInstalled_Type(Integer32):
    """Custom type upsmgConfigBatteryInstalled based on Integer32"""
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


_UpsmgConfigBatteryInstalled_Type.__name__ = "Integer32"
_UpsmgConfigBatteryInstalled_Object = MibScalar
upsmgConfigBatteryInstalled = _UpsmgConfigBatteryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 1),
    _UpsmgConfigBatteryInstalled_Type()
)
upsmgConfigBatteryInstalled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigBatteryInstalled.setStatus("mandatory")
_UpsmgConfigNominalBatteryVoltage_Type = Integer32
_UpsmgConfigNominalBatteryVoltage_Object = MibScalar
upsmgConfigNominalBatteryVoltage = _UpsmgConfigNominalBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 2),
    _UpsmgConfigNominalBatteryVoltage_Type()
)
upsmgConfigNominalBatteryVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigNominalBatteryVoltage.setStatus("mandatory")
_UpsmgConfigNominalBatteryTime_Type = Integer32
_UpsmgConfigNominalBatteryTime_Object = MibScalar
upsmgConfigNominalBatteryTime = _UpsmgConfigNominalBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 3),
    _UpsmgConfigNominalBatteryTime_Type()
)
upsmgConfigNominalBatteryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigNominalBatteryTime.setStatus("mandatory")
_UpsmgConfigNominalRechargeTime_Type = Integer32
_UpsmgConfigNominalRechargeTime_Object = MibScalar
upsmgConfigNominalRechargeTime = _UpsmgConfigNominalRechargeTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 4),
    _UpsmgConfigNominalRechargeTime_Type()
)
upsmgConfigNominalRechargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigNominalRechargeTime.setStatus("mandatory")
_UpsmgConfigMinRechargeLevel_Type = Integer32
_UpsmgConfigMinRechargeLevel_Object = MibScalar
upsmgConfigMinRechargeLevel = _UpsmgConfigMinRechargeLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 5),
    _UpsmgConfigMinRechargeLevel_Type()
)
upsmgConfigMinRechargeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigMinRechargeLevel.setStatus("mandatory")
_UpsmgConfigMaxRechargeTime_Type = Integer32
_UpsmgConfigMaxRechargeTime_Object = MibScalar
upsmgConfigMaxRechargeTime = _UpsmgConfigMaxRechargeTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 6),
    _UpsmgConfigMaxRechargeTime_Type()
)
upsmgConfigMaxRechargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigMaxRechargeTime.setStatus("mandatory")
_UpsmgConfigLowBatteryTime_Type = Integer32
_UpsmgConfigLowBatteryTime_Object = MibScalar
upsmgConfigLowBatteryTime = _UpsmgConfigLowBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 7),
    _UpsmgConfigLowBatteryTime_Type()
)
upsmgConfigLowBatteryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigLowBatteryTime.setStatus("mandatory")
_UpsmgConfigLowBatteryLevel_Type = Integer32
_UpsmgConfigLowBatteryLevel_Object = MibScalar
upsmgConfigLowBatteryLevel = _UpsmgConfigLowBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 8),
    _UpsmgConfigLowBatteryLevel_Type()
)
upsmgConfigLowBatteryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigLowBatteryLevel.setStatus("mandatory")


class _UpsmgConfigAutoRestart_Type(Integer32):
    """Custom type upsmgConfigAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("never", 2),
          ("onmain", 3))
    )


_UpsmgConfigAutoRestart_Type.__name__ = "Integer32"
_UpsmgConfigAutoRestart_Object = MibScalar
upsmgConfigAutoRestart = _UpsmgConfigAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 9),
    _UpsmgConfigAutoRestart_Type()
)
upsmgConfigAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigAutoRestart.setStatus("mandatory")
_UpsmgConfigShutdownTimer_Type = Integer32
_UpsmgConfigShutdownTimer_Object = MibScalar
upsmgConfigShutdownTimer = _UpsmgConfigShutdownTimer_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 10),
    _UpsmgConfigShutdownTimer_Type()
)
upsmgConfigShutdownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigShutdownTimer.setStatus("mandatory")
_UpsmgConfigSysShutDuration_Type = Integer32
_UpsmgConfigSysShutDuration_Object = MibScalar
upsmgConfigSysShutDuration = _UpsmgConfigSysShutDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 11),
    _UpsmgConfigSysShutDuration_Type()
)
upsmgConfigSysShutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigSysShutDuration.setStatus("mandatory")
_UpsmgConfigVARating_Type = Integer32
_UpsmgConfigVARating_Object = MibScalar
upsmgConfigVARating = _UpsmgConfigVARating_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 12),
    _UpsmgConfigVARating_Type()
)
upsmgConfigVARating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigVARating.setStatus("mandatory")
_UpsmgConfigLowTransfer_Type = Integer32
_UpsmgConfigLowTransfer_Object = MibScalar
upsmgConfigLowTransfer = _UpsmgConfigLowTransfer_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 13),
    _UpsmgConfigLowTransfer_Type()
)
upsmgConfigLowTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigLowTransfer.setStatus("mandatory")
_UpsmgConfigHighTransfer_Type = Integer32
_UpsmgConfigHighTransfer_Object = MibScalar
upsmgConfigHighTransfer = _UpsmgConfigHighTransfer_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 14),
    _UpsmgConfigHighTransfer_Type()
)
upsmgConfigHighTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHighTransfer.setStatus("mandatory")
_UpsmgConfigOutputNominalVoltage_Type = Integer32
_UpsmgConfigOutputNominalVoltage_Object = MibScalar
upsmgConfigOutputNominalVoltage = _UpsmgConfigOutputNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 15),
    _UpsmgConfigOutputNominalVoltage_Type()
)
upsmgConfigOutputNominalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigOutputNominalVoltage.setStatus("mandatory")
_UpsmgConfigOutputNominalCurrent_Type = Integer32
_UpsmgConfigOutputNominalCurrent_Object = MibScalar
upsmgConfigOutputNominalCurrent = _UpsmgConfigOutputNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 16),
    _UpsmgConfigOutputNominalCurrent_Type()
)
upsmgConfigOutputNominalCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigOutputNominalCurrent.setStatus("mandatory")
_UpsmgConfigOutputNomFrequency_Type = Integer32
_UpsmgConfigOutputNomFrequency_Object = MibScalar
upsmgConfigOutputNomFrequency = _UpsmgConfigOutputNomFrequency_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 17),
    _UpsmgConfigOutputNomFrequency_Type()
)
upsmgConfigOutputNomFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigOutputNomFrequency.setStatus("mandatory")


class _UpsmgConfigByPassType_Type(Integer32):
    """Custom type upsmgConfigByPassType based on Integer32"""
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
          ("relay", 2),
          ("static", 3))
    )


_UpsmgConfigByPassType_Type.__name__ = "Integer32"
_UpsmgConfigByPassType_Object = MibScalar
upsmgConfigByPassType = _UpsmgConfigByPassType_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 18),
    _UpsmgConfigByPassType_Type()
)
upsmgConfigByPassType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigByPassType.setStatus("mandatory")


class _UpsmgConfigAlarmAudible_Type(Integer32):
    """Custom type upsmgConfigAlarmAudible based on Integer32"""
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


_UpsmgConfigAlarmAudible_Type.__name__ = "Integer32"
_UpsmgConfigAlarmAudible_Object = MibScalar
upsmgConfigAlarmAudible = _UpsmgConfigAlarmAudible_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 19),
    _UpsmgConfigAlarmAudible_Type()
)
upsmgConfigAlarmAudible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigAlarmAudible.setStatus("mandatory")
_UpsmgConfigAlarmTimeDelay_Type = Integer32
_UpsmgConfigAlarmTimeDelay_Object = MibScalar
upsmgConfigAlarmTimeDelay = _UpsmgConfigAlarmTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 20),
    _UpsmgConfigAlarmTimeDelay_Type()
)
upsmgConfigAlarmTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigAlarmTimeDelay.setStatus("mandatory")
_UpsmgConfigDevicesNum_Type = Integer32
_UpsmgConfigDevicesNum_Object = MibScalar
upsmgConfigDevicesNum = _UpsmgConfigDevicesNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 21),
    _UpsmgConfigDevicesNum_Type()
)
upsmgConfigDevicesNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigDevicesNum.setStatus("mandatory")
_UpsmgConfigDevicesTable_Object = MibTable
upsmgConfigDevicesTable = _UpsmgConfigDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22)
)
if mibBuilder.loadTexts:
    upsmgConfigDevicesTable.setStatus("mandatory")
_UpsmgConfigDevicesEntry_Object = MibTableRow
upsmgConfigDevicesEntry = _UpsmgConfigDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1)
)
upsmgConfigDevicesEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgdeviceIndex"),
)
if mibBuilder.loadTexts:
    upsmgConfigDevicesEntry.setStatus("mandatory")


class _MgdeviceIndex_Type(Integer32):
    """Custom type mgdeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgdeviceIndex_Type.__name__ = "Integer32"
_MgdeviceIndex_Object = MibTableColumn
mgdeviceIndex = _MgdeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 1),
    _MgdeviceIndex_Type()
)
mgdeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgdeviceIndex.setStatus("mandatory")
_MgdeviceReceptacleNum_Type = Integer32
_MgdeviceReceptacleNum_Object = MibTableColumn
mgdeviceReceptacleNum = _MgdeviceReceptacleNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 2),
    _MgdeviceReceptacleNum_Type()
)
mgdeviceReceptacleNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceReceptacleNum.setStatus("mandatory")


class _MgdeviceIdent_Type(DisplayString):
    """Custom type mgdeviceIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgdeviceIdent_Type.__name__ = "DisplayString"
_MgdeviceIdent_Object = MibTableColumn
mgdeviceIdent = _MgdeviceIdent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 3),
    _MgdeviceIdent_Type()
)
mgdeviceIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceIdent.setStatus("mandatory")
_MgdeviceVaRating_Type = Integer32
_MgdeviceVaRating_Object = MibTableColumn
mgdeviceVaRating = _MgdeviceVaRating_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 4),
    _MgdeviceVaRating_Type()
)
mgdeviceVaRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceVaRating.setStatus("mandatory")
_MgdeviceSequenceOff_Type = Integer32
_MgdeviceSequenceOff_Object = MibTableColumn
mgdeviceSequenceOff = _MgdeviceSequenceOff_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 5),
    _MgdeviceSequenceOff_Type()
)
mgdeviceSequenceOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceSequenceOff.setStatus("mandatory")
_MgdeviceSequenceOn_Type = Integer32
_MgdeviceSequenceOn_Object = MibTableColumn
mgdeviceSequenceOn = _MgdeviceSequenceOn_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 6),
    _MgdeviceSequenceOn_Type()
)
mgdeviceSequenceOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceSequenceOn.setStatus("mandatory")
_MgdeviceShutdownDuration_Type = Integer32
_MgdeviceShutdownDuration_Object = MibTableColumn
mgdeviceShutdownDuration = _MgdeviceShutdownDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 7),
    _MgdeviceShutdownDuration_Type()
)
mgdeviceShutdownDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceShutdownDuration.setStatus("mandatory")
_MgdeviceBootUpDuration_Type = Integer32
_MgdeviceBootUpDuration_Object = MibTableColumn
mgdeviceBootUpDuration = _MgdeviceBootUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 22, 1, 8),
    _MgdeviceBootUpDuration_Type()
)
mgdeviceBootUpDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgdeviceBootUpDuration.setStatus("mandatory")
_UpsmgConfigReceptaclesTable_Object = MibTable
upsmgConfigReceptaclesTable = _UpsmgConfigReceptaclesTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23)
)
if mibBuilder.loadTexts:
    upsmgConfigReceptaclesTable.setStatus("mandatory")
_UpsmgConfigReceptaclesEntry_Object = MibTableRow
upsmgConfigReceptaclesEntry = _UpsmgConfigReceptaclesEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1)
)
upsmgConfigReceptaclesEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgreceptacleIndexb"),
)
if mibBuilder.loadTexts:
    upsmgConfigReceptaclesEntry.setStatus("mandatory")


class _MgreceptacleIndexb_Type(Integer32):
    """Custom type mgreceptacleIndexb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgreceptacleIndexb_Type.__name__ = "Integer32"
_MgreceptacleIndexb_Object = MibTableColumn
mgreceptacleIndexb = _MgreceptacleIndexb_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 1),
    _MgreceptacleIndexb_Type()
)
mgreceptacleIndexb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleIndexb.setStatus("mandatory")


class _MgreceptacleStateTurnOn_Type(Integer32):
    """Custom type mgreceptacleStateTurnOn based on Integer32"""
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
        *(("last", 3),
          ("off", 2),
          ("on", 1),
          ("schedule", 4))
    )


_MgreceptacleStateTurnOn_Type.__name__ = "Integer32"
_MgreceptacleStateTurnOn_Object = MibTableColumn
mgreceptacleStateTurnOn = _MgreceptacleStateTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 2),
    _MgreceptacleStateTurnOn_Type()
)
mgreceptacleStateTurnOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleStateTurnOn.setStatus("mandatory")


class _MgreceptacleStateMainReturn_Type(Integer32):
    """Custom type mgreceptacleStateMainReturn based on Integer32"""
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
        *(("last", 3),
          ("off", 2),
          ("on", 1),
          ("schedule", 4))
    )


_MgreceptacleStateMainReturn_Type.__name__ = "Integer32"
_MgreceptacleStateMainReturn_Object = MibTableColumn
mgreceptacleStateMainReturn = _MgreceptacleStateMainReturn_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 3),
    _MgreceptacleStateMainReturn_Type()
)
mgreceptacleStateMainReturn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleStateMainReturn.setStatus("mandatory")


class _MgreceptacleStateDischarge_Type(Integer32):
    """Custom type mgreceptacleStateDischarge based on Integer32"""
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
        *(("last", 3),
          ("off", 2),
          ("on", 1),
          ("schedule", 4))
    )


_MgreceptacleStateDischarge_Type.__name__ = "Integer32"
_MgreceptacleStateDischarge_Object = MibTableColumn
mgreceptacleStateDischarge = _MgreceptacleStateDischarge_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 4),
    _MgreceptacleStateDischarge_Type()
)
mgreceptacleStateDischarge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleStateDischarge.setStatus("mandatory")
_MgreceptacleShutoffLevel_Type = Integer32
_MgreceptacleShutoffLevel_Object = MibTableColumn
mgreceptacleShutoffLevel = _MgreceptacleShutoffLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 5),
    _MgreceptacleShutoffLevel_Type()
)
mgreceptacleShutoffLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleShutoffLevel.setStatus("mandatory")
_MgreceptacleShutoffTimer_Type = Integer32
_MgreceptacleShutoffTimer_Object = MibTableColumn
mgreceptacleShutoffTimer = _MgreceptacleShutoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 6),
    _MgreceptacleShutoffTimer_Type()
)
mgreceptacleShutoffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleShutoffTimer.setStatus("mandatory")
_MgreceptacleRestartLevel_Type = Integer32
_MgreceptacleRestartLevel_Object = MibTableColumn
mgreceptacleRestartLevel = _MgreceptacleRestartLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 7),
    _MgreceptacleRestartLevel_Type()
)
mgreceptacleRestartLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleRestartLevel.setStatus("mandatory")
_MgreceptacleRestartDelay_Type = Integer32
_MgreceptacleRestartDelay_Object = MibTableColumn
mgreceptacleRestartDelay = _MgreceptacleRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 8),
    _MgreceptacleRestartDelay_Type()
)
mgreceptacleRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleRestartDelay.setStatus("mandatory")
_MgreceptacleShutdownDuration_Type = Integer32
_MgreceptacleShutdownDuration_Object = MibTableColumn
mgreceptacleShutdownDuration = _MgreceptacleShutdownDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 9),
    _MgreceptacleShutdownDuration_Type()
)
mgreceptacleShutdownDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleShutdownDuration.setStatus("mandatory")
_MgreceptacleBootUpDuration_Type = Integer32
_MgreceptacleBootUpDuration_Object = MibTableColumn
mgreceptacleBootUpDuration = _MgreceptacleBootUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 23, 1, 10),
    _MgreceptacleBootUpDuration_Type()
)
mgreceptacleBootUpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleBootUpDuration.setStatus("mandatory")
_UpsmgConfigExtAlarmNum_Type = Integer32
_UpsmgConfigExtAlarmNum_Object = MibScalar
upsmgConfigExtAlarmNum = _UpsmgConfigExtAlarmNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 24),
    _UpsmgConfigExtAlarmNum_Type()
)
upsmgConfigExtAlarmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgConfigExtAlarmNum.setStatus("mandatory")
_UpsmgConfigExtAlarmTable_Object = MibTable
upsmgConfigExtAlarmTable = _UpsmgConfigExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 25)
)
if mibBuilder.loadTexts:
    upsmgConfigExtAlarmTable.setStatus("mandatory")
_UpsmgConfigExtAlarmEntry_Object = MibTableRow
upsmgConfigExtAlarmEntry = _UpsmgConfigExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 25, 1)
)
upsmgConfigExtAlarmEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgextAlarmIndex"),
)
if mibBuilder.loadTexts:
    upsmgConfigExtAlarmEntry.setStatus("mandatory")


class _MgextAlarmIndex_Type(Integer32):
    """Custom type mgextAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgextAlarmIndex_Type.__name__ = "Integer32"
_MgextAlarmIndex_Object = MibTableColumn
mgextAlarmIndex = _MgextAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 25, 1, 1),
    _MgextAlarmIndex_Type()
)
mgextAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgextAlarmIndex.setStatus("mandatory")


class _MgextAlarmUID_Type(DisplayString):
    """Custom type mgextAlarmUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MgextAlarmUID_Type.__name__ = "DisplayString"
_MgextAlarmUID_Object = MibTableColumn
mgextAlarmUID = _MgextAlarmUID_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 25, 1, 2),
    _MgextAlarmUID_Type()
)
mgextAlarmUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgextAlarmUID.setStatus("mandatory")


class _UpsmgConfigEmergencyTestFail_Type(Integer32):
    """Custom type upsmgConfigEmergencyTestFail based on Integer32"""
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


_UpsmgConfigEmergencyTestFail_Type.__name__ = "Integer32"
_UpsmgConfigEmergencyTestFail_Object = MibScalar
upsmgConfigEmergencyTestFail = _UpsmgConfigEmergencyTestFail_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 26),
    _UpsmgConfigEmergencyTestFail_Type()
)
upsmgConfigEmergencyTestFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigEmergencyTestFail.setStatus("mandatory")


class _UpsmgConfigEmergencyOnByPass_Type(Integer32):
    """Custom type upsmgConfigEmergencyOnByPass based on Integer32"""
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


_UpsmgConfigEmergencyOnByPass_Type.__name__ = "Integer32"
_UpsmgConfigEmergencyOnByPass_Object = MibScalar
upsmgConfigEmergencyOnByPass = _UpsmgConfigEmergencyOnByPass_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 27),
    _UpsmgConfigEmergencyOnByPass_Type()
)
upsmgConfigEmergencyOnByPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigEmergencyOnByPass.setStatus("mandatory")


class _UpsmgConfigEmergencyOverload_Type(Integer32):
    """Custom type upsmgConfigEmergencyOverload based on Integer32"""
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


_UpsmgConfigEmergencyOverload_Type.__name__ = "Integer32"
_UpsmgConfigEmergencyOverload_Object = MibScalar
upsmgConfigEmergencyOverload = _UpsmgConfigEmergencyOverload_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 28),
    _UpsmgConfigEmergencyOverload_Type()
)
upsmgConfigEmergencyOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigEmergencyOverload.setStatus("mandatory")
_UpsmgConfigControlDayTable_Object = MibTable
upsmgConfigControlDayTable = _UpsmgConfigControlDayTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 29)
)
if mibBuilder.loadTexts:
    upsmgConfigControlDayTable.setStatus("mandatory")
_UpsmgConfigControlDayEntry_Object = MibTableRow
upsmgConfigControlDayEntry = _UpsmgConfigControlDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 29, 1)
)
upsmgConfigControlDayEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgcontrolDayIndex"),
)
if mibBuilder.loadTexts:
    upsmgConfigControlDayEntry.setStatus("mandatory")


class _MgcontrolDayIndex_Type(Integer32):
    """Custom type mgcontrolDayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgcontrolDayIndex_Type.__name__ = "Integer32"
_MgcontrolDayIndex_Object = MibTableColumn
mgcontrolDayIndex = _MgcontrolDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 29, 1, 1),
    _MgcontrolDayIndex_Type()
)
mgcontrolDayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgcontrolDayIndex.setStatus("mandatory")
_MgcontrolDayOn_Type = Integer32
_MgcontrolDayOn_Object = MibTableColumn
mgcontrolDayOn = _MgcontrolDayOn_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 29, 1, 2),
    _MgcontrolDayOn_Type()
)
mgcontrolDayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcontrolDayOn.setStatus("mandatory")
_MgcontrolDayOff_Type = Integer32
_MgcontrolDayOff_Object = MibTableColumn
mgcontrolDayOff = _MgcontrolDayOff_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 29, 1, 3),
    _MgcontrolDayOff_Type()
)
mgcontrolDayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgcontrolDayOff.setStatus("mandatory")
_UpsmgConfigLowBooster_Type = Integer32
_UpsmgConfigLowBooster_Object = MibScalar
upsmgConfigLowBooster = _UpsmgConfigLowBooster_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 30),
    _UpsmgConfigLowBooster_Type()
)
upsmgConfigLowBooster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigLowBooster.setStatus("mandatory")
_UpsmgConfigHighBooster_Type = Integer32
_UpsmgConfigHighBooster_Object = MibScalar
upsmgConfigHighBooster = _UpsmgConfigHighBooster_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 31),
    _UpsmgConfigHighBooster_Type()
)
upsmgConfigHighBooster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHighBooster.setStatus("mandatory")
_UpsmgConfigLowFader_Type = Integer32
_UpsmgConfigLowFader_Object = MibScalar
upsmgConfigLowFader = _UpsmgConfigLowFader_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 32),
    _UpsmgConfigLowFader_Type()
)
upsmgConfigLowFader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigLowFader.setStatus("mandatory")
_UpsmgConfigHighFader_Type = Integer32
_UpsmgConfigHighFader_Object = MibScalar
upsmgConfigHighFader = _UpsmgConfigHighFader_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 33),
    _UpsmgConfigHighFader_Type()
)
upsmgConfigHighFader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHighFader.setStatus("mandatory")
_UpsmgConfigEnvironmentTable_Object = MibTable
upsmgConfigEnvironmentTable = _UpsmgConfigEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34)
)
if mibBuilder.loadTexts:
    upsmgConfigEnvironmentTable.setStatus("mandatory")
_UpsmgConfigEnvironmentEntry_Object = MibTableRow
upsmgConfigEnvironmentEntry = _UpsmgConfigEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1)
)
upsmgConfigEnvironmentEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "upsmgConfigSensorIndex"),
)
if mibBuilder.loadTexts:
    upsmgConfigEnvironmentEntry.setStatus("mandatory")


class _UpsmgConfigSensorIndex_Type(Integer32):
    """Custom type upsmgConfigSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_UpsmgConfigSensorIndex_Type.__name__ = "Integer32"
_UpsmgConfigSensorIndex_Object = MibTableColumn
upsmgConfigSensorIndex = _UpsmgConfigSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 1),
    _UpsmgConfigSensorIndex_Type()
)
upsmgConfigSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgConfigSensorIndex.setStatus("mandatory")


class _UpsmgConfigSensorName_Type(DisplayString):
    """Custom type upsmgConfigSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_UpsmgConfigSensorName_Type.__name__ = "DisplayString"
_UpsmgConfigSensorName_Object = MibTableColumn
upsmgConfigSensorName = _UpsmgConfigSensorName_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 2),
    _UpsmgConfigSensorName_Type()
)
upsmgConfigSensorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigSensorName.setStatus("mandatory")
_UpsmgConfigTemperatureLow_Type = Integer32
_UpsmgConfigTemperatureLow_Object = MibTableColumn
upsmgConfigTemperatureLow = _UpsmgConfigTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 3),
    _UpsmgConfigTemperatureLow_Type()
)
upsmgConfigTemperatureLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigTemperatureLow.setStatus("mandatory")
_UpsmgConfigTemperatureHigh_Type = Integer32
_UpsmgConfigTemperatureHigh_Object = MibTableColumn
upsmgConfigTemperatureHigh = _UpsmgConfigTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 4),
    _UpsmgConfigTemperatureHigh_Type()
)
upsmgConfigTemperatureHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigTemperatureHigh.setStatus("mandatory")
_UpsmgConfigTemperatureHysteresis_Type = Integer32
_UpsmgConfigTemperatureHysteresis_Object = MibTableColumn
upsmgConfigTemperatureHysteresis = _UpsmgConfigTemperatureHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 5),
    _UpsmgConfigTemperatureHysteresis_Type()
)
upsmgConfigTemperatureHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigTemperatureHysteresis.setStatus("mandatory")
_UpsmgConfigHumidityLow_Type = Integer32
_UpsmgConfigHumidityLow_Object = MibTableColumn
upsmgConfigHumidityLow = _UpsmgConfigHumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 6),
    _UpsmgConfigHumidityLow_Type()
)
upsmgConfigHumidityLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHumidityLow.setStatus("mandatory")
_UpsmgConfigHumidityHigh_Type = Integer32
_UpsmgConfigHumidityHigh_Object = MibTableColumn
upsmgConfigHumidityHigh = _UpsmgConfigHumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 7),
    _UpsmgConfigHumidityHigh_Type()
)
upsmgConfigHumidityHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHumidityHigh.setStatus("mandatory")
_UpsmgConfigHumidityHysteresis_Type = Integer32
_UpsmgConfigHumidityHysteresis_Object = MibTableColumn
upsmgConfigHumidityHysteresis = _UpsmgConfigHumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 8),
    _UpsmgConfigHumidityHysteresis_Type()
)
upsmgConfigHumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigHumidityHysteresis.setStatus("mandatory")


class _UpsmgConfigInput1Name_Type(DisplayString):
    """Custom type upsmgConfigInput1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_UpsmgConfigInput1Name_Type.__name__ = "DisplayString"
_UpsmgConfigInput1Name_Object = MibTableColumn
upsmgConfigInput1Name = _UpsmgConfigInput1Name_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 9),
    _UpsmgConfigInput1Name_Type()
)
upsmgConfigInput1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput1Name.setStatus("mandatory")


class _UpsmgConfigInput1ClosedLabel_Type(DisplayString):
    """Custom type upsmgConfigInput1ClosedLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_UpsmgConfigInput1ClosedLabel_Type.__name__ = "DisplayString"
_UpsmgConfigInput1ClosedLabel_Object = MibTableColumn
upsmgConfigInput1ClosedLabel = _UpsmgConfigInput1ClosedLabel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 10),
    _UpsmgConfigInput1ClosedLabel_Type()
)
upsmgConfigInput1ClosedLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput1ClosedLabel.setStatus("mandatory")


class _UpsmgConfigInput1OpenLabel_Type(DisplayString):
    """Custom type upsmgConfigInput1OpenLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_UpsmgConfigInput1OpenLabel_Type.__name__ = "DisplayString"
_UpsmgConfigInput1OpenLabel_Object = MibTableColumn
upsmgConfigInput1OpenLabel = _UpsmgConfigInput1OpenLabel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 11),
    _UpsmgConfigInput1OpenLabel_Type()
)
upsmgConfigInput1OpenLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput1OpenLabel.setStatus("mandatory")


class _UpsmgConfigInput2Name_Type(DisplayString):
    """Custom type upsmgConfigInput2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_UpsmgConfigInput2Name_Type.__name__ = "DisplayString"
_UpsmgConfigInput2Name_Object = MibTableColumn
upsmgConfigInput2Name = _UpsmgConfigInput2Name_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 12),
    _UpsmgConfigInput2Name_Type()
)
upsmgConfigInput2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput2Name.setStatus("mandatory")


class _UpsmgConfigInput2ClosedLabel_Type(DisplayString):
    """Custom type upsmgConfigInput2ClosedLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_UpsmgConfigInput2ClosedLabel_Type.__name__ = "DisplayString"
_UpsmgConfigInput2ClosedLabel_Object = MibTableColumn
upsmgConfigInput2ClosedLabel = _UpsmgConfigInput2ClosedLabel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 13),
    _UpsmgConfigInput2ClosedLabel_Type()
)
upsmgConfigInput2ClosedLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput2ClosedLabel.setStatus("mandatory")


class _UpsmgConfigInput2OpenLabel_Type(DisplayString):
    """Custom type upsmgConfigInput2OpenLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_UpsmgConfigInput2OpenLabel_Type.__name__ = "DisplayString"
_UpsmgConfigInput2OpenLabel_Object = MibTableColumn
upsmgConfigInput2OpenLabel = _UpsmgConfigInput2OpenLabel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 4, 34, 1, 14),
    _UpsmgConfigInput2OpenLabel_Type()
)
upsmgConfigInput2OpenLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgConfigInput2OpenLabel.setStatus("mandatory")
_UpsmgBattery_ObjectIdentity = ObjectIdentity
upsmgBattery = _UpsmgBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 5)
)
_UpsmgBatteryRemainingTime_Type = Integer32
_UpsmgBatteryRemainingTime_Object = MibScalar
upsmgBatteryRemainingTime = _UpsmgBatteryRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 1),
    _UpsmgBatteryRemainingTime_Type()
)
upsmgBatteryRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryRemainingTime.setStatus("mandatory")
_UpsmgBatteryLevel_Type = Integer32
_UpsmgBatteryLevel_Object = MibScalar
upsmgBatteryLevel = _UpsmgBatteryLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 2),
    _UpsmgBatteryLevel_Type()
)
upsmgBatteryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryLevel.setStatus("mandatory")
_UpsmgBatteryRechargeTime_Type = Integer32
_UpsmgBatteryRechargeTime_Object = MibScalar
upsmgBatteryRechargeTime = _UpsmgBatteryRechargeTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 3),
    _UpsmgBatteryRechargeTime_Type()
)
upsmgBatteryRechargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryRechargeTime.setStatus("mandatory")
_UpsmgBatteryRechargeLevel_Type = Integer32
_UpsmgBatteryRechargeLevel_Object = MibScalar
upsmgBatteryRechargeLevel = _UpsmgBatteryRechargeLevel_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 4),
    _UpsmgBatteryRechargeLevel_Type()
)
upsmgBatteryRechargeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryRechargeLevel.setStatus("mandatory")
_UpsmgBatteryVoltage_Type = Integer32
_UpsmgBatteryVoltage_Object = MibScalar
upsmgBatteryVoltage = _UpsmgBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 5),
    _UpsmgBatteryVoltage_Type()
)
upsmgBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryVoltage.setStatus("mandatory")
_UpsmgBatteryCurrent_Type = Integer32
_UpsmgBatteryCurrent_Object = MibScalar
upsmgBatteryCurrent = _UpsmgBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 6),
    _UpsmgBatteryCurrent_Type()
)
upsmgBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryCurrent.setStatus("mandatory")
_UpsmgBatteryTemperature_Type = Integer32
_UpsmgBatteryTemperature_Object = MibScalar
upsmgBatteryTemperature = _UpsmgBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 7),
    _UpsmgBatteryTemperature_Type()
)
upsmgBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryTemperature.setStatus("mandatory")
_UpsmgBatteryFullRechargeTime_Type = Integer32
_UpsmgBatteryFullRechargeTime_Object = MibScalar
upsmgBatteryFullRechargeTime = _UpsmgBatteryFullRechargeTime_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 8),
    _UpsmgBatteryFullRechargeTime_Type()
)
upsmgBatteryFullRechargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryFullRechargeTime.setStatus("mandatory")


class _UpsmgBatteryFaultBattery_Type(Integer32):
    """Custom type upsmgBatteryFaultBattery based on Integer32"""
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


_UpsmgBatteryFaultBattery_Type.__name__ = "Integer32"
_UpsmgBatteryFaultBattery_Object = MibScalar
upsmgBatteryFaultBattery = _UpsmgBatteryFaultBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 9),
    _UpsmgBatteryFaultBattery_Type()
)
upsmgBatteryFaultBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryFaultBattery.setStatus("mandatory")


class _UpsmgBatteryNoBattery_Type(Integer32):
    """Custom type upsmgBatteryNoBattery based on Integer32"""
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


_UpsmgBatteryNoBattery_Type.__name__ = "Integer32"
_UpsmgBatteryNoBattery_Object = MibScalar
upsmgBatteryNoBattery = _UpsmgBatteryNoBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 10),
    _UpsmgBatteryNoBattery_Type()
)
upsmgBatteryNoBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryNoBattery.setStatus("mandatory")


class _UpsmgBatteryReplacement_Type(Integer32):
    """Custom type upsmgBatteryReplacement based on Integer32"""
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


_UpsmgBatteryReplacement_Type.__name__ = "Integer32"
_UpsmgBatteryReplacement_Object = MibScalar
upsmgBatteryReplacement = _UpsmgBatteryReplacement_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 11),
    _UpsmgBatteryReplacement_Type()
)
upsmgBatteryReplacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryReplacement.setStatus("mandatory")


class _UpsmgBatteryUnavailableBattery_Type(Integer32):
    """Custom type upsmgBatteryUnavailableBattery based on Integer32"""
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


_UpsmgBatteryUnavailableBattery_Type.__name__ = "Integer32"
_UpsmgBatteryUnavailableBattery_Object = MibScalar
upsmgBatteryUnavailableBattery = _UpsmgBatteryUnavailableBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 12),
    _UpsmgBatteryUnavailableBattery_Type()
)
upsmgBatteryUnavailableBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryUnavailableBattery.setStatus("mandatory")


class _UpsmgBatteryNotHighCharge_Type(Integer32):
    """Custom type upsmgBatteryNotHighCharge based on Integer32"""
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


_UpsmgBatteryNotHighCharge_Type.__name__ = "Integer32"
_UpsmgBatteryNotHighCharge_Object = MibScalar
upsmgBatteryNotHighCharge = _UpsmgBatteryNotHighCharge_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 13),
    _UpsmgBatteryNotHighCharge_Type()
)
upsmgBatteryNotHighCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryNotHighCharge.setStatus("mandatory")


class _UpsmgBatteryLowBattery_Type(Integer32):
    """Custom type upsmgBatteryLowBattery based on Integer32"""
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


_UpsmgBatteryLowBattery_Type.__name__ = "Integer32"
_UpsmgBatteryLowBattery_Object = MibScalar
upsmgBatteryLowBattery = _UpsmgBatteryLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 14),
    _UpsmgBatteryLowBattery_Type()
)
upsmgBatteryLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryLowBattery.setStatus("mandatory")


class _UpsmgBatteryChargerFault_Type(Integer32):
    """Custom type upsmgBatteryChargerFault based on Integer32"""
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


_UpsmgBatteryChargerFault_Type.__name__ = "Integer32"
_UpsmgBatteryChargerFault_Object = MibScalar
upsmgBatteryChargerFault = _UpsmgBatteryChargerFault_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 15),
    _UpsmgBatteryChargerFault_Type()
)
upsmgBatteryChargerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryChargerFault.setStatus("mandatory")


class _UpsmgBatteryLowCondition_Type(Integer32):
    """Custom type upsmgBatteryLowCondition based on Integer32"""
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


_UpsmgBatteryLowCondition_Type.__name__ = "Integer32"
_UpsmgBatteryLowCondition_Object = MibScalar
upsmgBatteryLowCondition = _UpsmgBatteryLowCondition_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 16),
    _UpsmgBatteryLowCondition_Type()
)
upsmgBatteryLowCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryLowCondition.setStatus("mandatory")


class _UpsmgBatteryLowRecharge_Type(Integer32):
    """Custom type upsmgBatteryLowRecharge based on Integer32"""
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


_UpsmgBatteryLowRecharge_Type.__name__ = "Integer32"
_UpsmgBatteryLowRecharge_Object = MibScalar
upsmgBatteryLowRecharge = _UpsmgBatteryLowRecharge_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 5, 17),
    _UpsmgBatteryLowRecharge_Type()
)
upsmgBatteryLowRecharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgBatteryLowRecharge.setStatus("mandatory")
_UpsmgInput_ObjectIdentity = ObjectIdentity
upsmgInput = _UpsmgInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 6)
)
_UpsmgInputPhaseNum_Type = Integer32
_UpsmgInputPhaseNum_Object = MibScalar
upsmgInputPhaseNum = _UpsmgInputPhaseNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 1),
    _UpsmgInputPhaseNum_Type()
)
upsmgInputPhaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgInputPhaseNum.setStatus("mandatory")
_UpsmgInputPhaseTable_Object = MibTable
upsmgInputPhaseTable = _UpsmgInputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2)
)
if mibBuilder.loadTexts:
    upsmgInputPhaseTable.setStatus("mandatory")
_UpsmgInputPhaseEntry_Object = MibTableRow
upsmgInputPhaseEntry = _UpsmgInputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1)
)
upsmgInputPhaseEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mginputIndex"),
)
if mibBuilder.loadTexts:
    upsmgInputPhaseEntry.setStatus("mandatory")


class _MginputIndex_Type(Integer32):
    """Custom type mginputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MginputIndex_Type.__name__ = "Integer32"
_MginputIndex_Object = MibTableColumn
mginputIndex = _MginputIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 1),
    _MginputIndex_Type()
)
mginputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputIndex.setStatus("mandatory")
_MginputVoltage_Type = Integer32
_MginputVoltage_Object = MibTableColumn
mginputVoltage = _MginputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 2),
    _MginputVoltage_Type()
)
mginputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputVoltage.setStatus("mandatory")
_MginputFrequency_Type = Integer32
_MginputFrequency_Object = MibTableColumn
mginputFrequency = _MginputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 3),
    _MginputFrequency_Type()
)
mginputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputFrequency.setStatus("mandatory")
_MginputMinimumVoltage_Type = Integer32
_MginputMinimumVoltage_Object = MibTableColumn
mginputMinimumVoltage = _MginputMinimumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 4),
    _MginputMinimumVoltage_Type()
)
mginputMinimumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputMinimumVoltage.setStatus("mandatory")
_MginputMaximumVoltage_Type = Integer32
_MginputMaximumVoltage_Object = MibTableColumn
mginputMaximumVoltage = _MginputMaximumVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 5),
    _MginputMaximumVoltage_Type()
)
mginputMaximumVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputMaximumVoltage.setStatus("mandatory")
_MginputCurrent_Type = Integer32
_MginputCurrent_Object = MibTableColumn
mginputCurrent = _MginputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 2, 1, 6),
    _MginputCurrent_Type()
)
mginputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mginputCurrent.setStatus("mandatory")


class _UpsmgInputBadStatus_Type(Integer32):
    """Custom type upsmgInputBadStatus based on Integer32"""
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


_UpsmgInputBadStatus_Type.__name__ = "Integer32"
_UpsmgInputBadStatus_Object = MibScalar
upsmgInputBadStatus = _UpsmgInputBadStatus_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 3),
    _UpsmgInputBadStatus_Type()
)
upsmgInputBadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgInputBadStatus.setStatus("mandatory")


class _UpsmgInputLineFailCause_Type(Integer32):
    """Custom type upsmgInputLineFailCause based on Integer32"""
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
        *(("no", 1),
          ("outoftolfreq", 3),
          ("outoftolvolt", 2),
          ("utilityoff", 4))
    )


_UpsmgInputLineFailCause_Type.__name__ = "Integer32"
_UpsmgInputLineFailCause_Object = MibScalar
upsmgInputLineFailCause = _UpsmgInputLineFailCause_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 6, 4),
    _UpsmgInputLineFailCause_Type()
)
upsmgInputLineFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgInputLineFailCause.setStatus("mandatory")
_UpsmgOutput_ObjectIdentity = ObjectIdentity
upsmgOutput = _UpsmgOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 7)
)
_UpsmgOutputPhaseNum_Type = Integer32
_UpsmgOutputPhaseNum_Object = MibScalar
upsmgOutputPhaseNum = _UpsmgOutputPhaseNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 1),
    _UpsmgOutputPhaseNum_Type()
)
upsmgOutputPhaseNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputPhaseNum.setStatus("mandatory")
_UpsmgOutputPhaseTable_Object = MibTable
upsmgOutputPhaseTable = _UpsmgOutputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2)
)
if mibBuilder.loadTexts:
    upsmgOutputPhaseTable.setStatus("mandatory")
_UpsmgOutputPhaseEntry_Object = MibTableRow
upsmgOutputPhaseEntry = _UpsmgOutputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1)
)
upsmgOutputPhaseEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgoutputPhaseIndex"),
)
if mibBuilder.loadTexts:
    upsmgOutputPhaseEntry.setStatus("mandatory")


class _MgoutputPhaseIndex_Type(Integer32):
    """Custom type mgoutputPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgoutputPhaseIndex_Type.__name__ = "Integer32"
_MgoutputPhaseIndex_Object = MibTableColumn
mgoutputPhaseIndex = _MgoutputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1, 1),
    _MgoutputPhaseIndex_Type()
)
mgoutputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgoutputPhaseIndex.setStatus("mandatory")
_MgoutputVoltage_Type = Integer32
_MgoutputVoltage_Object = MibTableColumn
mgoutputVoltage = _MgoutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1, 2),
    _MgoutputVoltage_Type()
)
mgoutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgoutputVoltage.setStatus("mandatory")
_MgoutputFrequency_Type = Integer32
_MgoutputFrequency_Object = MibTableColumn
mgoutputFrequency = _MgoutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1, 3),
    _MgoutputFrequency_Type()
)
mgoutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgoutputFrequency.setStatus("mandatory")
_MgoutputLoadPerPhase_Type = Integer32
_MgoutputLoadPerPhase_Object = MibTableColumn
mgoutputLoadPerPhase = _MgoutputLoadPerPhase_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1, 4),
    _MgoutputLoadPerPhase_Type()
)
mgoutputLoadPerPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgoutputLoadPerPhase.setStatus("mandatory")
_MgoutputCurrent_Type = Integer32
_MgoutputCurrent_Object = MibTableColumn
mgoutputCurrent = _MgoutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 2, 1, 5),
    _MgoutputCurrent_Type()
)
mgoutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgoutputCurrent.setStatus("mandatory")


class _UpsmgOutputOnBattery_Type(Integer32):
    """Custom type upsmgOutputOnBattery based on Integer32"""
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


_UpsmgOutputOnBattery_Type.__name__ = "Integer32"
_UpsmgOutputOnBattery_Object = MibScalar
upsmgOutputOnBattery = _UpsmgOutputOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 3),
    _UpsmgOutputOnBattery_Type()
)
upsmgOutputOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOnBattery.setStatus("mandatory")


class _UpsmgOutputOnByPass_Type(Integer32):
    """Custom type upsmgOutputOnByPass based on Integer32"""
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


_UpsmgOutputOnByPass_Type.__name__ = "Integer32"
_UpsmgOutputOnByPass_Object = MibScalar
upsmgOutputOnByPass = _UpsmgOutputOnByPass_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 4),
    _UpsmgOutputOnByPass_Type()
)
upsmgOutputOnByPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOnByPass.setStatus("mandatory")


class _UpsmgOutputUnavailableByPass_Type(Integer32):
    """Custom type upsmgOutputUnavailableByPass based on Integer32"""
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


_UpsmgOutputUnavailableByPass_Type.__name__ = "Integer32"
_UpsmgOutputUnavailableByPass_Object = MibScalar
upsmgOutputUnavailableByPass = _UpsmgOutputUnavailableByPass_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 5),
    _UpsmgOutputUnavailableByPass_Type()
)
upsmgOutputUnavailableByPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputUnavailableByPass.setStatus("mandatory")


class _UpsmgOutputNoByPass_Type(Integer32):
    """Custom type upsmgOutputNoByPass based on Integer32"""
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


_UpsmgOutputNoByPass_Type.__name__ = "Integer32"
_UpsmgOutputNoByPass_Object = MibScalar
upsmgOutputNoByPass = _UpsmgOutputNoByPass_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 6),
    _UpsmgOutputNoByPass_Type()
)
upsmgOutputNoByPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputNoByPass.setStatus("mandatory")


class _UpsmgOutputUtilityOff_Type(Integer32):
    """Custom type upsmgOutputUtilityOff based on Integer32"""
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


_UpsmgOutputUtilityOff_Type.__name__ = "Integer32"
_UpsmgOutputUtilityOff_Object = MibScalar
upsmgOutputUtilityOff = _UpsmgOutputUtilityOff_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 7),
    _UpsmgOutputUtilityOff_Type()
)
upsmgOutputUtilityOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputUtilityOff.setStatus("mandatory")


class _UpsmgOutputOnBoost_Type(Integer32):
    """Custom type upsmgOutputOnBoost based on Integer32"""
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


_UpsmgOutputOnBoost_Type.__name__ = "Integer32"
_UpsmgOutputOnBoost_Object = MibScalar
upsmgOutputOnBoost = _UpsmgOutputOnBoost_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 8),
    _UpsmgOutputOnBoost_Type()
)
upsmgOutputOnBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOnBoost.setStatus("mandatory")


class _UpsmgOutputInverterOff_Type(Integer32):
    """Custom type upsmgOutputInverterOff based on Integer32"""
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


_UpsmgOutputInverterOff_Type.__name__ = "Integer32"
_UpsmgOutputInverterOff_Object = MibScalar
upsmgOutputInverterOff = _UpsmgOutputInverterOff_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 9),
    _UpsmgOutputInverterOff_Type()
)
upsmgOutputInverterOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputInverterOff.setStatus("mandatory")


class _UpsmgOutputOverLoad_Type(Integer32):
    """Custom type upsmgOutputOverLoad based on Integer32"""
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


_UpsmgOutputOverLoad_Type.__name__ = "Integer32"
_UpsmgOutputOverLoad_Object = MibScalar
upsmgOutputOverLoad = _UpsmgOutputOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 10),
    _UpsmgOutputOverLoad_Type()
)
upsmgOutputOverLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOverLoad.setStatus("mandatory")


class _UpsmgOutputOverTemp_Type(Integer32):
    """Custom type upsmgOutputOverTemp based on Integer32"""
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


_UpsmgOutputOverTemp_Type.__name__ = "Integer32"
_UpsmgOutputOverTemp_Object = MibScalar
upsmgOutputOverTemp = _UpsmgOutputOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 11),
    _UpsmgOutputOverTemp_Type()
)
upsmgOutputOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOverTemp.setStatus("mandatory")
_UpsmgOutputOnBuck_Type = Integer32
_UpsmgOutputOnBuck_Object = MibScalar
upsmgOutputOnBuck = _UpsmgOutputOnBuck_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 7, 12),
    _UpsmgOutputOnBuck_Type()
)
upsmgOutputOnBuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgOutputOnBuck.setStatus("mandatory")
_UpsmgEnviron_ObjectIdentity = ObjectIdentity
upsmgEnviron = _UpsmgEnviron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 8)
)
_UpsmgEnvironAmbientTemp_Type = Integer32
_UpsmgEnvironAmbientTemp_Object = MibScalar
upsmgEnvironAmbientTemp = _UpsmgEnvironAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 1),
    _UpsmgEnvironAmbientTemp_Type()
)
upsmgEnvironAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironAmbientTemp.setStatus("mandatory")
_UpsmgEnvironAmbientHumidity_Type = Integer32
_UpsmgEnvironAmbientHumidity_Object = MibScalar
upsmgEnvironAmbientHumidity = _UpsmgEnvironAmbientHumidity_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 2),
    _UpsmgEnvironAmbientHumidity_Type()
)
upsmgEnvironAmbientHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironAmbientHumidity.setStatus("mandatory")
_UpsmgEnvironExtAlarmTable_Object = MibTable
upsmgEnvironExtAlarmTable = _UpsmgEnvironExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 3)
)
if mibBuilder.loadTexts:
    upsmgEnvironExtAlarmTable.setStatus("mandatory")
_UpsmgEnvironExtAlarmEntry_Object = MibTableRow
upsmgEnvironExtAlarmEntry = _UpsmgEnvironExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 3, 1)
)
upsmgEnvironExtAlarmEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgalarmNum"),
)
if mibBuilder.loadTexts:
    upsmgEnvironExtAlarmEntry.setStatus("mandatory")


class _MgalarmNum_Type(Integer32):
    """Custom type mgalarmNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgalarmNum_Type.__name__ = "Integer32"
_MgalarmNum_Object = MibTableColumn
mgalarmNum = _MgalarmNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 3, 1, 1),
    _MgalarmNum_Type()
)
mgalarmNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgalarmNum.setStatus("mandatory")


class _MgalarmState_Type(Integer32):
    """Custom type mgalarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MgalarmState_Type.__name__ = "Integer32"
_MgalarmState_Object = MibTableColumn
mgalarmState = _MgalarmState_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 3, 1, 2),
    _MgalarmState_Type()
)
mgalarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgalarmState.setStatus("mandatory")
_UpsmgEnvironSensorNum_Type = Integer32
_UpsmgEnvironSensorNum_Object = MibScalar
upsmgEnvironSensorNum = _UpsmgEnvironSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 4),
    _UpsmgEnvironSensorNum_Type()
)
upsmgEnvironSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironSensorNum.setStatus("mandatory")
_UpsmgEnvironSensorTable_Object = MibTable
upsmgEnvironSensorTable = _UpsmgEnvironSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 5)
)
if mibBuilder.loadTexts:
    upsmgEnvironSensorTable.setStatus("mandatory")
_UpsmgEnvironSensorEntry_Object = MibTableRow
upsmgEnvironSensorEntry = _UpsmgEnvironSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 5, 1)
)
upsmgEnvironSensorEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgsensorNum"),
)
if mibBuilder.loadTexts:
    upsmgEnvironSensorEntry.setStatus("mandatory")


class _MgsensorNum_Type(Integer32):
    """Custom type mgsensorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgsensorNum_Type.__name__ = "Integer32"
_MgsensorNum_Object = MibTableColumn
mgsensorNum = _MgsensorNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 5, 1, 1),
    _MgsensorNum_Type()
)
mgsensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgsensorNum.setStatus("mandatory")
_MgsensorTemp_Type = Integer32
_MgsensorTemp_Object = MibTableColumn
mgsensorTemp = _MgsensorTemp_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 5, 1, 2),
    _MgsensorTemp_Type()
)
mgsensorTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgsensorTemp.setStatus("mandatory")
_MgsensorHumidity_Type = Integer32
_MgsensorHumidity_Object = MibTableColumn
mgsensorHumidity = _MgsensorHumidity_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 5, 1, 3),
    _MgsensorHumidity_Type()
)
mgsensorHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgsensorHumidity.setStatus("mandatory")
_UpsmgEnvironmentNum_Type = Integer32
_UpsmgEnvironmentNum_Object = MibScalar
upsmgEnvironmentNum = _UpsmgEnvironmentNum_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 6),
    _UpsmgEnvironmentNum_Type()
)
upsmgEnvironmentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentNum.setStatus("mandatory")
_UpsmgEnvironmentSensorTable_Object = MibTable
upsmgEnvironmentSensorTable = _UpsmgEnvironmentSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7)
)
if mibBuilder.loadTexts:
    upsmgEnvironmentSensorTable.setStatus("mandatory")
_UpsmgEnvironmentSensorEntry_Object = MibTableRow
upsmgEnvironmentSensorEntry = _UpsmgEnvironmentSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1)
)
upsmgEnvironmentSensorEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "upsmgEnvironmentIndex"),
)
if mibBuilder.loadTexts:
    upsmgEnvironmentSensorEntry.setStatus("mandatory")


class _UpsmgEnvironmentIndex_Type(Integer32):
    """Custom type upsmgEnvironmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_UpsmgEnvironmentIndex_Type.__name__ = "Integer32"
_UpsmgEnvironmentIndex_Object = MibTableColumn
upsmgEnvironmentIndex = _UpsmgEnvironmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 1),
    _UpsmgEnvironmentIndex_Type()
)
upsmgEnvironmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentIndex.setStatus("mandatory")


class _UpsmgEnvironmentComFailure_Type(Integer32):
    """Custom type upsmgEnvironmentComFailure based on Integer32"""
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


_UpsmgEnvironmentComFailure_Type.__name__ = "Integer32"
_UpsmgEnvironmentComFailure_Object = MibTableColumn
upsmgEnvironmentComFailure = _UpsmgEnvironmentComFailure_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 2),
    _UpsmgEnvironmentComFailure_Type()
)
upsmgEnvironmentComFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentComFailure.setStatus("mandatory")
_UpsmgEnvironmentTemperature_Type = Integer32
_UpsmgEnvironmentTemperature_Object = MibTableColumn
upsmgEnvironmentTemperature = _UpsmgEnvironmentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 3),
    _UpsmgEnvironmentTemperature_Type()
)
upsmgEnvironmentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentTemperature.setStatus("mandatory")


class _UpsmgEnvironmentTemperatureLow_Type(Integer32):
    """Custom type upsmgEnvironmentTemperatureLow based on Integer32"""
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


_UpsmgEnvironmentTemperatureLow_Type.__name__ = "Integer32"
_UpsmgEnvironmentTemperatureLow_Object = MibTableColumn
upsmgEnvironmentTemperatureLow = _UpsmgEnvironmentTemperatureLow_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 4),
    _UpsmgEnvironmentTemperatureLow_Type()
)
upsmgEnvironmentTemperatureLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentTemperatureLow.setStatus("mandatory")


class _UpsmgEnvironmentTemperatureHigh_Type(Integer32):
    """Custom type upsmgEnvironmentTemperatureHigh based on Integer32"""
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


_UpsmgEnvironmentTemperatureHigh_Type.__name__ = "Integer32"
_UpsmgEnvironmentTemperatureHigh_Object = MibTableColumn
upsmgEnvironmentTemperatureHigh = _UpsmgEnvironmentTemperatureHigh_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 5),
    _UpsmgEnvironmentTemperatureHigh_Type()
)
upsmgEnvironmentTemperatureHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentTemperatureHigh.setStatus("mandatory")
_UpsmgEnvironmentHumidity_Type = Integer32
_UpsmgEnvironmentHumidity_Object = MibTableColumn
upsmgEnvironmentHumidity = _UpsmgEnvironmentHumidity_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 6),
    _UpsmgEnvironmentHumidity_Type()
)
upsmgEnvironmentHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentHumidity.setStatus("mandatory")


class _UpsmgEnvironmentHumidityLow_Type(Integer32):
    """Custom type upsmgEnvironmentHumidityLow based on Integer32"""
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


_UpsmgEnvironmentHumidityLow_Type.__name__ = "Integer32"
_UpsmgEnvironmentHumidityLow_Object = MibTableColumn
upsmgEnvironmentHumidityLow = _UpsmgEnvironmentHumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 7),
    _UpsmgEnvironmentHumidityLow_Type()
)
upsmgEnvironmentHumidityLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentHumidityLow.setStatus("mandatory")


class _UpsmgEnvironmentHumidityHigh_Type(Integer32):
    """Custom type upsmgEnvironmentHumidityHigh based on Integer32"""
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


_UpsmgEnvironmentHumidityHigh_Type.__name__ = "Integer32"
_UpsmgEnvironmentHumidityHigh_Object = MibTableColumn
upsmgEnvironmentHumidityHigh = _UpsmgEnvironmentHumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 8),
    _UpsmgEnvironmentHumidityHigh_Type()
)
upsmgEnvironmentHumidityHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentHumidityHigh.setStatus("mandatory")


class _UpsmgEnvironmentInput1State_Type(Integer32):
    """Custom type upsmgEnvironmentInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_UpsmgEnvironmentInput1State_Type.__name__ = "Integer32"
_UpsmgEnvironmentInput1State_Object = MibTableColumn
upsmgEnvironmentInput1State = _UpsmgEnvironmentInput1State_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 9),
    _UpsmgEnvironmentInput1State_Type()
)
upsmgEnvironmentInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentInput1State.setStatus("mandatory")


class _UpsmgEnvironmentInput2State_Type(Integer32):
    """Custom type upsmgEnvironmentInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_UpsmgEnvironmentInput2State_Type.__name__ = "Integer32"
_UpsmgEnvironmentInput2State_Object = MibTableColumn
upsmgEnvironmentInput2State = _UpsmgEnvironmentInput2State_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 8, 7, 1, 10),
    _UpsmgEnvironmentInput2State_Type()
)
upsmgEnvironmentInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgEnvironmentInput2State.setStatus("mandatory")
_UpsmgControl_ObjectIdentity = ObjectIdentity
upsmgControl = _UpsmgControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 9)
)
_UpsmgControlReceptaclesTable_Object = MibTable
upsmgControlReceptaclesTable = _UpsmgControlReceptaclesTable_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1)
)
if mibBuilder.loadTexts:
    upsmgControlReceptaclesTable.setStatus("mandatory")
_UpsmgControlReceptaclesEntry_Object = MibTableRow
upsmgControlReceptaclesEntry = _UpsmgControlReceptaclesEntry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1)
)
upsmgControlReceptaclesEntry.setIndexNames(
    (0, "MG-SNMP-UPS-MIB", "mgreceptacleIndexc"),
)
if mibBuilder.loadTexts:
    upsmgControlReceptaclesEntry.setStatus("mandatory")


class _MgreceptacleIndexc_Type(Integer32):
    """Custom type mgreceptacleIndexc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MgreceptacleIndexc_Type.__name__ = "Integer32"
_MgreceptacleIndexc_Object = MibTableColumn
mgreceptacleIndexc = _MgreceptacleIndexc_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 1),
    _MgreceptacleIndexc_Type()
)
mgreceptacleIndexc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleIndexc.setStatus("mandatory")
_MgreceptacleOnDelay_Type = Integer32
_MgreceptacleOnDelay_Object = MibTableColumn
mgreceptacleOnDelay = _MgreceptacleOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 2),
    _MgreceptacleOnDelay_Type()
)
mgreceptacleOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleOnDelay.setStatus("mandatory")


class _MgreceptacleOnCtrl_Type(Integer32):
    """Custom type mgreceptacleOnCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("start", 2),
          ("stop", 3))
    )


_MgreceptacleOnCtrl_Type.__name__ = "Integer32"
_MgreceptacleOnCtrl_Object = MibTableColumn
mgreceptacleOnCtrl = _MgreceptacleOnCtrl_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 3),
    _MgreceptacleOnCtrl_Type()
)
mgreceptacleOnCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleOnCtrl.setStatus("mandatory")


class _MgreceptacleOnStatus_Type(Integer32):
    """Custom type mgreceptacleOnStatus based on Integer32"""
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
        *(("completed", 4),
          ("inprogressinups", 3),
          ("none", 1),
          ("started", 2))
    )


_MgreceptacleOnStatus_Type.__name__ = "Integer32"
_MgreceptacleOnStatus_Object = MibTableColumn
mgreceptacleOnStatus = _MgreceptacleOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 4),
    _MgreceptacleOnStatus_Type()
)
mgreceptacleOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleOnStatus.setStatus("mandatory")
_MgreceptacleOffDelay_Type = Integer32
_MgreceptacleOffDelay_Object = MibTableColumn
mgreceptacleOffDelay = _MgreceptacleOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 5),
    _MgreceptacleOffDelay_Type()
)
mgreceptacleOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleOffDelay.setStatus("mandatory")


class _MgreceptacleOffCtrl_Type(Integer32):
    """Custom type mgreceptacleOffCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("start", 2),
          ("stop", 3))
    )


_MgreceptacleOffCtrl_Type.__name__ = "Integer32"
_MgreceptacleOffCtrl_Object = MibTableColumn
mgreceptacleOffCtrl = _MgreceptacleOffCtrl_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 6),
    _MgreceptacleOffCtrl_Type()
)
mgreceptacleOffCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleOffCtrl.setStatus("mandatory")


class _MgreceptacleOffStatus_Type(Integer32):
    """Custom type mgreceptacleOffStatus based on Integer32"""
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
        *(("completed", 4),
          ("inprogressinups", 3),
          ("none", 1),
          ("started", 2))
    )


_MgreceptacleOffStatus_Type.__name__ = "Integer32"
_MgreceptacleOffStatus_Object = MibTableColumn
mgreceptacleOffStatus = _MgreceptacleOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 7),
    _MgreceptacleOffStatus_Type()
)
mgreceptacleOffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleOffStatus.setStatus("mandatory")
_MgreceptacleToggleDelay_Type = Integer32
_MgreceptacleToggleDelay_Object = MibTableColumn
mgreceptacleToggleDelay = _MgreceptacleToggleDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 8),
    _MgreceptacleToggleDelay_Type()
)
mgreceptacleToggleDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleToggleDelay.setStatus("mandatory")


class _MgreceptacleToggleCtrl_Type(Integer32):
    """Custom type mgreceptacleToggleCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("start", 2),
          ("stop", 3))
    )


_MgreceptacleToggleCtrl_Type.__name__ = "Integer32"
_MgreceptacleToggleCtrl_Object = MibTableColumn
mgreceptacleToggleCtrl = _MgreceptacleToggleCtrl_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 9),
    _MgreceptacleToggleCtrl_Type()
)
mgreceptacleToggleCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleToggleCtrl.setStatus("mandatory")


class _MgreceptacleToggleStatus_Type(Integer32):
    """Custom type mgreceptacleToggleStatus based on Integer32"""
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
        *(("completed", 4),
          ("inprogressinups", 3),
          ("none", 1),
          ("started", 2))
    )


_MgreceptacleToggleStatus_Type.__name__ = "Integer32"
_MgreceptacleToggleStatus_Object = MibTableColumn
mgreceptacleToggleStatus = _MgreceptacleToggleStatus_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 10),
    _MgreceptacleToggleStatus_Type()
)
mgreceptacleToggleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgreceptacleToggleStatus.setStatus("mandatory")
_MgreceptacleToggleDuration_Type = Integer32
_MgreceptacleToggleDuration_Object = MibTableColumn
mgreceptacleToggleDuration = _MgreceptacleToggleDuration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 1, 1, 11),
    _MgreceptacleToggleDuration_Type()
)
mgreceptacleToggleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgreceptacleToggleDuration.setStatus("mandatory")


class _UpsmgControlDayOff_Type(Integer32):
    """Custom type upsmgControlDayOff based on Integer32"""
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
          ("saterday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsmgControlDayOff_Type.__name__ = "Integer32"
_UpsmgControlDayOff_Object = MibScalar
upsmgControlDayOff = _UpsmgControlDayOff_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 2),
    _UpsmgControlDayOff_Type()
)
upsmgControlDayOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgControlDayOff.setStatus("mandatory")


class _UpsmgControlDayOn_Type(Integer32):
    """Custom type upsmgControlDayOn based on Integer32"""
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
          ("saterday", 7),
          ("sunday", 1),
          ("thursday", 5),
          ("tuesday", 3),
          ("wednesday", 4))
    )


_UpsmgControlDayOn_Type.__name__ = "Integer32"
_UpsmgControlDayOn_Object = MibScalar
upsmgControlDayOn = _UpsmgControlDayOn_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 9, 3),
    _UpsmgControlDayOn_Type()
)
upsmgControlDayOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgControlDayOn.setStatus("mandatory")
_UpsmgTest_ObjectIdentity = ObjectIdentity
upsmgTest = _UpsmgTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 10)
)


class _UpsmgTestBatterySchedule_Type(Integer32):
    """Custom type upsmgTestBatterySchedule based on Integer32"""
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
        *(("atturnon", 4),
          ("dayly", 6),
          ("monthly", 3),
          ("none", 5),
          ("unknown", 1),
          ("weekly", 2))
    )


_UpsmgTestBatterySchedule_Type.__name__ = "Integer32"
_UpsmgTestBatterySchedule_Object = MibScalar
upsmgTestBatterySchedule = _UpsmgTestBatterySchedule_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 1),
    _UpsmgTestBatterySchedule_Type()
)
upsmgTestBatterySchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestBatterySchedule.setStatus("mandatory")


class _UpsmgTestDiagnostics_Type(Integer32):
    """Custom type upsmgTestDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("start", 2))
    )


_UpsmgTestDiagnostics_Type.__name__ = "Integer32"
_UpsmgTestDiagnostics_Object = MibScalar
upsmgTestDiagnostics = _UpsmgTestDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 2),
    _UpsmgTestDiagnostics_Type()
)
upsmgTestDiagnostics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestDiagnostics.setStatus("mandatory")


class _UpsmgTestDiagResult_Type(Integer32):
    """Custom type upsmgTestDiagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("none", 3),
          ("success", 1))
    )


_UpsmgTestDiagResult_Type.__name__ = "Integer32"
_UpsmgTestDiagResult_Object = MibScalar
upsmgTestDiagResult = _UpsmgTestDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 3),
    _UpsmgTestDiagResult_Type()
)
upsmgTestDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgTestDiagResult.setStatus("mandatory")


class _UpsmgTestBatteryCalibration_Type(Integer32):
    """Custom type upsmgTestBatteryCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("start", 2))
    )


_UpsmgTestBatteryCalibration_Type.__name__ = "Integer32"
_UpsmgTestBatteryCalibration_Object = MibScalar
upsmgTestBatteryCalibration = _UpsmgTestBatteryCalibration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 4),
    _UpsmgTestBatteryCalibration_Type()
)
upsmgTestBatteryCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestBatteryCalibration.setStatus("mandatory")
_UpsmgTestLastCalibration_Type = Integer32
_UpsmgTestLastCalibration_Object = MibScalar
upsmgTestLastCalibration = _UpsmgTestLastCalibration_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 5),
    _UpsmgTestLastCalibration_Type()
)
upsmgTestLastCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgTestLastCalibration.setStatus("mandatory")
_UpsmgTestIndicators_Type = Integer32
_UpsmgTestIndicators_Object = MibScalar
upsmgTestIndicators = _UpsmgTestIndicators_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 6),
    _UpsmgTestIndicators_Type()
)
upsmgTestIndicators.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestIndicators.setStatus("mandatory")


class _UpsmgTestCommandLine_Type(DisplayString):
    """Custom type upsmgTestCommandLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgTestCommandLine_Type.__name__ = "DisplayString"
_UpsmgTestCommandLine_Object = MibScalar
upsmgTestCommandLine = _UpsmgTestCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 7),
    _UpsmgTestCommandLine_Type()
)
upsmgTestCommandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestCommandLine.setStatus("mandatory")


class _UpsmgTestCommandReady_Type(Integer32):
    """Custom type upsmgTestCommandReady based on Integer32"""
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


_UpsmgTestCommandReady_Type.__name__ = "Integer32"
_UpsmgTestCommandReady_Object = MibScalar
upsmgTestCommandReady = _UpsmgTestCommandReady_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 8),
    _UpsmgTestCommandReady_Type()
)
upsmgTestCommandReady.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgTestCommandReady.setStatus("mandatory")


class _UpsmgTestResponseLine_Type(DisplayString):
    """Custom type upsmgTestResponseLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgTestResponseLine_Type.__name__ = "DisplayString"
_UpsmgTestResponseLine_Object = MibScalar
upsmgTestResponseLine = _UpsmgTestResponseLine_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 9),
    _UpsmgTestResponseLine_Type()
)
upsmgTestResponseLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgTestResponseLine.setStatus("mandatory")


class _UpsmgTestResponseReady_Type(Integer32):
    """Custom type upsmgTestResponseReady based on Integer32"""
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


_UpsmgTestResponseReady_Type.__name__ = "Integer32"
_UpsmgTestResponseReady_Object = MibScalar
upsmgTestResponseReady = _UpsmgTestResponseReady_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 10),
    _UpsmgTestResponseReady_Type()
)
upsmgTestResponseReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgTestResponseReady.setStatus("mandatory")


class _UpsmgTestBatteryResult_Type(Integer32):
    """Custom type upsmgTestBatteryResult based on Integer32"""
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
        *(("mfailed", 2),
          ("msuccess", 1),
          ("none", 5),
          ("sfailed", 4),
          ("ssuccess", 3))
    )


_UpsmgTestBatteryResult_Type.__name__ = "Integer32"
_UpsmgTestBatteryResult_Object = MibScalar
upsmgTestBatteryResult = _UpsmgTestBatteryResult_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 10, 11),
    _UpsmgTestBatteryResult_Type()
)
upsmgTestBatteryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgTestBatteryResult.setStatus("mandatory")
_UpsmgTraps_ObjectIdentity = ObjectIdentity
upsmgTraps = _UpsmgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 11)
)
_UpsmgAgent_ObjectIdentity = ObjectIdentity
upsmgAgent = _UpsmgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 12)
)
_UpsmgAgentIpaddress_Type = IpAddress
_UpsmgAgentIpaddress_Object = MibScalar
upsmgAgentIpaddress = _UpsmgAgentIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 1),
    _UpsmgAgentIpaddress_Type()
)
upsmgAgentIpaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentIpaddress.setStatus("mandatory")
_UpsmgAgentSubnetMask_Type = IpAddress
_UpsmgAgentSubnetMask_Object = MibScalar
upsmgAgentSubnetMask = _UpsmgAgentSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 2),
    _UpsmgAgentSubnetMask_Type()
)
upsmgAgentSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentSubnetMask.setStatus("mandatory")
_UpsmgAgentDefGateway_Type = IpAddress
_UpsmgAgentDefGateway_Object = MibScalar
upsmgAgentDefGateway = _UpsmgAgentDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 3),
    _UpsmgAgentDefGateway_Type()
)
upsmgAgentDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentDefGateway.setStatus("mandatory")
_UpsmgAgentBaudRate_Type = Integer32
_UpsmgAgentBaudRate_Object = MibScalar
upsmgAgentBaudRate = _UpsmgAgentBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 4),
    _UpsmgAgentBaudRate_Type()
)
upsmgAgentBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentBaudRate.setStatus("mandatory")
_UpsmgAgentPollRate_Type = Integer32
_UpsmgAgentPollRate_Object = MibScalar
upsmgAgentPollRate = _UpsmgAgentPollRate_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 5),
    _UpsmgAgentPollRate_Type()
)
upsmgAgentPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentPollRate.setStatus("mandatory")


class _UpsmgAgentType_Type(Integer32):
    """Custom type upsmgAgentType based on Integer32"""
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
        *(("deviceEth", 1),
          ("deviceTR", 2),
          ("other", 5),
          ("proxyEth", 3),
          ("proxyTR", 4))
    )


_UpsmgAgentType_Type.__name__ = "Integer32"
_UpsmgAgentType_Object = MibScalar
upsmgAgentType = _UpsmgAgentType_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 6),
    _UpsmgAgentType_Type()
)
upsmgAgentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentType.setStatus("mandatory")
_UpsmgAgentTrapAlarmDelay_Type = Integer32
_UpsmgAgentTrapAlarmDelay_Object = MibScalar
upsmgAgentTrapAlarmDelay = _UpsmgAgentTrapAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 7),
    _UpsmgAgentTrapAlarmDelay_Type()
)
upsmgAgentTrapAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentTrapAlarmDelay.setStatus("mandatory")
_UpsmgAgentTrapAlarmRetry_Type = Integer32
_UpsmgAgentTrapAlarmRetry_Object = MibScalar
upsmgAgentTrapAlarmRetry = _UpsmgAgentTrapAlarmRetry_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 8),
    _UpsmgAgentTrapAlarmRetry_Type()
)
upsmgAgentTrapAlarmRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentTrapAlarmRetry.setStatus("mandatory")


class _UpsmgAgentReset_Type(Integer32):
    """Custom type upsmgAgentReset based on Integer32"""
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


_UpsmgAgentReset_Type.__name__ = "Integer32"
_UpsmgAgentReset_Object = MibScalar
upsmgAgentReset = _UpsmgAgentReset_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 9),
    _UpsmgAgentReset_Type()
)
upsmgAgentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentReset.setStatus("mandatory")


class _UpsmgAgentFactReset_Type(Integer32):
    """Custom type upsmgAgentFactReset based on Integer32"""
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


_UpsmgAgentFactReset_Type.__name__ = "Integer32"
_UpsmgAgentFactReset_Object = MibScalar
upsmgAgentFactReset = _UpsmgAgentFactReset_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 10),
    _UpsmgAgentFactReset_Type()
)
upsmgAgentFactReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentFactReset.setStatus("mandatory")
_UpsmgAgentMibVersion_Type = Integer32
_UpsmgAgentMibVersion_Object = MibScalar
upsmgAgentMibVersion = _UpsmgAgentMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 11),
    _UpsmgAgentMibVersion_Type()
)
upsmgAgentMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgAgentMibVersion.setStatus("mandatory")


class _UpsmgAgentFirmwareVersion_Type(DisplayString):
    """Custom type upsmgAgentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpsmgAgentFirmwareVersion_Type.__name__ = "DisplayString"
_UpsmgAgentFirmwareVersion_Object = MibScalar
upsmgAgentFirmwareVersion = _UpsmgAgentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 12),
    _UpsmgAgentFirmwareVersion_Type()
)
upsmgAgentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgAgentFirmwareVersion.setStatus("mandatory")
_UpsmgAgentCommUPS_Type = Integer32
_UpsmgAgentCommUPS_Object = MibScalar
upsmgAgentCommUPS = _UpsmgAgentCommUPS_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 13),
    _UpsmgAgentCommUPS_Type()
)
upsmgAgentCommUPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgAgentCommUPS.setStatus("mandatory")
_UpsmgAgentTrapAck_Type = Integer32
_UpsmgAgentTrapAck_Object = MibScalar
upsmgAgentTrapAck = _UpsmgAgentTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 14),
    _UpsmgAgentTrapAck_Type()
)
upsmgAgentTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentTrapAck.setStatus("mandatory")


class _UpsmgAgentAutoLearning_Type(Integer32):
    """Custom type upsmgAgentAutoLearning based on Integer32"""
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


_UpsmgAgentAutoLearning_Type.__name__ = "Integer32"
_UpsmgAgentAutoLearning_Object = MibScalar
upsmgAgentAutoLearning = _UpsmgAgentAutoLearning_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 15),
    _UpsmgAgentAutoLearning_Type()
)
upsmgAgentAutoLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentAutoLearning.setStatus("mandatory")


class _UpsmgAgentBootP_Type(Integer32):
    """Custom type upsmgAgentBootP based on Integer32"""
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


_UpsmgAgentBootP_Type.__name__ = "Integer32"
_UpsmgAgentBootP_Object = MibScalar
upsmgAgentBootP = _UpsmgAgentBootP_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 16),
    _UpsmgAgentBootP_Type()
)
upsmgAgentBootP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentBootP.setStatus("mandatory")


class _UpsmgAgentTFTP_Type(Integer32):
    """Custom type upsmgAgentTFTP based on Integer32"""
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


_UpsmgAgentTFTP_Type.__name__ = "Integer32"
_UpsmgAgentTFTP_Object = MibScalar
upsmgAgentTFTP = _UpsmgAgentTFTP_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 17),
    _UpsmgAgentTFTP_Type()
)
upsmgAgentTFTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgAgentTFTP.setStatus("mandatory")
_UpsmgAgentTrapSignature_Type = Integer32
_UpsmgAgentTrapSignature_Object = MibScalar
upsmgAgentTrapSignature = _UpsmgAgentTrapSignature_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 12, 18),
    _UpsmgAgentTrapSignature_Type()
)
upsmgAgentTrapSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsmgAgentTrapSignature.setStatus("mandatory")
_UpsmgRemote_ObjectIdentity = ObjectIdentity
upsmgRemote = _UpsmgRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 705, 1, 13)
)
_UpsmgRemoteOnBattery_Type = Integer32
_UpsmgRemoteOnBattery_Object = MibScalar
upsmgRemoteOnBattery = _UpsmgRemoteOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 13, 1),
    _UpsmgRemoteOnBattery_Type()
)
upsmgRemoteOnBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgRemoteOnBattery.setStatus("mandatory")
_UpsmgRemoteIpAddress_Type = IpAddress
_UpsmgRemoteIpAddress_Object = MibScalar
upsmgRemoteIpAddress = _UpsmgRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 705, 1, 13, 2),
    _UpsmgRemoteIpAddress_Type()
)
upsmgRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsmgRemoteIpAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

upsmgBatteryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    upsmgBatteryFault.setStatus(
        ""
    )

upsmgBatteryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 2)
)
if mibBuilder.loadTexts:
    upsmgBatteryOK.setStatus(
        ""
    )

upsmgBatteryReplacementIndicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 3)
)
if mibBuilder.loadTexts:
    upsmgBatteryReplacementIndicated.setStatus(
        ""
    )

upsmgBatteryReplaceNotIndicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    upsmgBatteryReplaceNotIndicated.setStatus(
        ""
    )

upsmgAtLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 5)
)
upsmgAtLowBattery.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgAtLowBattery.setStatus(
        ""
    )

upsmgFromLowBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 6)
)
upsmgFromLowBattery.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgFromLowBattery.setStatus(
        ""
    )

upsmgChargerFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 7)
)
if mibBuilder.loadTexts:
    upsmgChargerFault.setStatus(
        ""
    )

upsmgChargerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 8)
)
if mibBuilder.loadTexts:
    upsmgChargerOK.setStatus(
        ""
    )

upsmgAtLowCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 9)
)
upsmgAtLowCondition.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgAtLowCondition.setStatus(
        ""
    )

upsmgFromLowCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 10)
)
upsmgFromLowCondition.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgFromLowCondition.setStatus(
        ""
    )

upsmgOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 11)
)
upsmgOnBattery.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgOnBattery.setStatus(
        ""
    )

upsmgReturnFromBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 12)
)
upsmgReturnFromBattery.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgReturnFromBattery.setStatus(
        ""
    )

upsmgOnByPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 13)
)
if mibBuilder.loadTexts:
    upsmgOnByPass.setStatus(
        ""
    )

upsmgReturnFromByPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 14)
)
if mibBuilder.loadTexts:
    upsmgReturnFromByPass.setStatus(
        ""
    )

upsmgByPassUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 15)
)
if mibBuilder.loadTexts:
    upsmgByPassUnavailable.setStatus(
        ""
    )

upsmgByPassAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 16)
)
if mibBuilder.loadTexts:
    upsmgByPassAvailable.setStatus(
        ""
    )

upsmgUtilityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 17)
)
if mibBuilder.loadTexts:
    upsmgUtilityFailure.setStatus(
        ""
    )

upsmgUtilityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 18)
)
if mibBuilder.loadTexts:
    upsmgUtilityRestored.setStatus(
        ""
    )

upsmgOnBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 19)
)
if mibBuilder.loadTexts:
    upsmgOnBoost.setStatus(
        ""
    )

upsmgReturnFromBoost = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 20)
)
if mibBuilder.loadTexts:
    upsmgReturnFromBoost.setStatus(
        ""
    )

upsmgOverLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 21)
)
if mibBuilder.loadTexts:
    upsmgOverLoad.setStatus(
        ""
    )

upsmgLoadOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 22)
)
if mibBuilder.loadTexts:
    upsmgLoadOK.setStatus(
        ""
    )

upsmgOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 23)
)
if mibBuilder.loadTexts:
    upsmgOverTemperature.setStatus(
        ""
    )

upsmgTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 24)
)
if mibBuilder.loadTexts:
    upsmgTemperatureOK.setStatus(
        ""
    )

upsmgOnToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 25)
)
upsmgOnToStart.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleState"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOnDelay"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleRestartDelay"))
)
if mibBuilder.loadTexts:
    upsmgOnToStart.setStatus(
        ""
    )

upsmgOnAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 26)
)
upsmgOnAbort.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOnDelay"))
)
if mibBuilder.loadTexts:
    upsmgOnAbort.setStatus(
        ""
    )

upsmgOnInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 27)
)
upsmgOnInProgress.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleState"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleBootUpDuration"))
)
if mibBuilder.loadTexts:
    upsmgOnInProgress.setStatus(
        ""
    )

upsmgOnComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 28)
)
upsmgOnComplete.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOnDelay"))
)
if mibBuilder.loadTexts:
    upsmgOnComplete.setStatus(
        ""
    )

upsmgOffToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 29)
)
upsmgOffToStart.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleState"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOffDelay"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleShutoffTimer"),
        ("MG-SNMP-UPS-MIB", "upsmgConfigSysShutDuration"))
)
if mibBuilder.loadTexts:
    upsmgOffToStart.setStatus(
        ""
    )

upsmgOffAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 30)
)
upsmgOffAbort.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOffDelay"))
)
if mibBuilder.loadTexts:
    upsmgOffAbort.setStatus(
        ""
    )

upsmgOffInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 31)
)
upsmgOffInProgress.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleState"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleShutdownDuration"))
)
if mibBuilder.loadTexts:
    upsmgOffInProgress.setStatus(
        ""
    )

upsmgOffComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 32)
)
upsmgOffComplete.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleOffDelay"))
)
if mibBuilder.loadTexts:
    upsmgOffComplete.setStatus(
        ""
    )

upsmgToggleToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 33)
)
upsmgToggleToStart.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleToggleDelay"))
)
if mibBuilder.loadTexts:
    upsmgToggleToStart.setStatus(
        ""
    )

upsmgToggleAbort = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 34)
)
upsmgToggleAbort.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleToggleDelay"))
)
if mibBuilder.loadTexts:
    upsmgToggleAbort.setStatus(
        ""
    )

upsmgToggleInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 35)
)
upsmgToggleInProgress.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleToggleDuration"))
)
if mibBuilder.loadTexts:
    upsmgToggleInProgress.setStatus(
        ""
    )

upsmgToggleComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 36)
)
upsmgToggleComplete.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgreceptacleIndex"),
        ("MG-SNMP-UPS-MIB", "mgreceptacleToggleDuration"))
)
if mibBuilder.loadTexts:
    upsmgToggleComplete.setStatus(
        ""
    )

upsmgCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 37)
)
if mibBuilder.loadTexts:
    upsmgCommunicationFailure.setStatus(
        ""
    )

upsmgCommunicationRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 38)
)
if mibBuilder.loadTexts:
    upsmgCommunicationRestored.setStatus(
        ""
    )

upsmgInputBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 39)
)
if mibBuilder.loadTexts:
    upsmgInputBad.setStatus(
        ""
    )

upsmgInputOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 40)
)
if mibBuilder.loadTexts:
    upsmgInputOK.setStatus(
        ""
    )

upsmgBatteryUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 41)
)
if mibBuilder.loadTexts:
    upsmgBatteryUnavailable.setStatus(
        ""
    )

upsmgBatteryAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 42)
)
if mibBuilder.loadTexts:
    upsmgBatteryAvailable.setStatus(
        ""
    )

upsmgAtLowRecharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 43)
)
upsmgAtLowRecharge.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgAtLowRecharge.setStatus(
        ""
    )

upsmgFromLowRecharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 44)
)
upsmgFromLowRecharge.setObjects(
      *(("MG-SNMP-UPS-MIB", "upsmgBatteryRemainingTime"),
        ("MG-SNMP-UPS-MIB", "upsmgBatteryLevel"))
)
if mibBuilder.loadTexts:
    upsmgFromLowRecharge.setStatus(
        ""
    )

upsmgDiagnosticTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 45)
)
if mibBuilder.loadTexts:
    upsmgDiagnosticTestFail.setStatus(
        ""
    )

upsmgDiagnosticTestOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 46)
)
if mibBuilder.loadTexts:
    upsmgDiagnosticTestOK.setStatus(
        ""
    )

upsmgBatteryTestOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 47)
)
if mibBuilder.loadTexts:
    upsmgBatteryTestOK.setStatus(
        ""
    )

upsmgBatteryTestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 48)
)
if mibBuilder.loadTexts:
    upsmgBatteryTestFail.setStatus(
        ""
    )

upsmgExternalAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 49)
)
upsmgExternalAlarmActive.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgextAlarmIndex"),
        ("MG-SNMP-UPS-MIB", "mgextAlarmUID"))
)
if mibBuilder.loadTexts:
    upsmgExternalAlarmActive.setStatus(
        ""
    )

upsmgExternalAlarmInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 50)
)
upsmgExternalAlarmInactive.setObjects(
      *(("MG-SNMP-UPS-MIB", "mgextAlarmIndex"),
        ("MG-SNMP-UPS-MIB", "mgextAlarmUID"))
)
if mibBuilder.loadTexts:
    upsmgExternalAlarmInactive.setStatus(
        ""
    )

upsmgOnBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 51)
)
if mibBuilder.loadTexts:
    upsmgOnBuck.setStatus(
        ""
    )

upsmgReturnFromBuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 52)
)
if mibBuilder.loadTexts:
    upsmgReturnFromBuck.setStatus(
        ""
    )

upsmgEnvironComFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 53)
)
if mibBuilder.loadTexts:
    upsmgEnvironComFailure.setStatus(
        ""
    )

upsmgEnvironComOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 54)
)
if mibBuilder.loadTexts:
    upsmgEnvironComOK.setStatus(
        ""
    )

upsmgEnvironTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 55)
)
if mibBuilder.loadTexts:
    upsmgEnvironTemperatureLow.setStatus(
        ""
    )

upsmgEnvironTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 56)
)
if mibBuilder.loadTexts:
    upsmgEnvironTemperatureHigh.setStatus(
        ""
    )

upsmgEnvironTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 57)
)
if mibBuilder.loadTexts:
    upsmgEnvironTemperatureOK.setStatus(
        ""
    )

upsmgEnvironHumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 58)
)
if mibBuilder.loadTexts:
    upsmgEnvironHumidityLow.setStatus(
        ""
    )

upsmgEnvironHumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 59)
)
if mibBuilder.loadTexts:
    upsmgEnvironHumidityHigh.setStatus(
        ""
    )

upsmgEnvironHumidityOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 60)
)
if mibBuilder.loadTexts:
    upsmgEnvironHumidityOK.setStatus(
        ""
    )

upsmgEnvironInput1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 61)
)
if mibBuilder.loadTexts:
    upsmgEnvironInput1Closed.setStatus(
        ""
    )

upsmgEnvironInput1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 62)
)
if mibBuilder.loadTexts:
    upsmgEnvironInput1Open.setStatus(
        ""
    )

upsmgEnvironInput2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 63)
)
if mibBuilder.loadTexts:
    upsmgEnvironInput2Closed.setStatus(
        ""
    )

upsmgEnvironInput2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 705, 1, 11, 0, 64)
)
if mibBuilder.loadTexts:
    upsmgEnvironInput2Open.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MG-SNMP-UPS-MIB",
    **{"merlinGerin": merlinGerin,
       "upsmg": upsmg,
       "upsmgIdent": upsmgIdent,
       "upsmgIdentFamilyName": upsmgIdentFamilyName,
       "upsmgIdentModelName": upsmgIdentModelName,
       "upsmgIdentRevisionLevel": upsmgIdentRevisionLevel,
       "upsmgIdentFirmwareVersion": upsmgIdentFirmwareVersion,
       "upsmgIdentUserID": upsmgIdentUserID,
       "upsmgIdentInstallationDate": upsmgIdentInstallationDate,
       "upsmgIdentSerialNumber": upsmgIdentSerialNumber,
       "upsmgManagement": upsmgManagement,
       "upsmgManagersNum": upsmgManagersNum,
       "upsmgManagersTable": upsmgManagersTable,
       "upsmgManagersEntry": upsmgManagersEntry,
       "mgmanagerIndex": mgmanagerIndex,
       "mgmanagerDeviceNumber": mgmanagerDeviceNumber,
       "mgmanagerNMSType": mgmanagerNMSType,
       "mgmanagerCommType": mgmanagerCommType,
       "mgmanagerDescr": mgmanagerDescr,
       "mgmanagerAddress": mgmanagerAddress,
       "mgmanagerCommunity": mgmanagerCommunity,
       "mgmanagerSeverityLevel": mgmanagerSeverityLevel,
       "mgmanagerTrapAck": mgmanagerTrapAck,
       "upsmgReceptacle": upsmgReceptacle,
       "upsmgReceptaclesNum": upsmgReceptaclesNum,
       "upsmgReceptaclesTable": upsmgReceptaclesTable,
       "upsmgReceptaclesEntry": upsmgReceptaclesEntry,
       "mgreceptacleIndex": mgreceptacleIndex,
       "mgreceptacleLevel": mgreceptacleLevel,
       "mgreceptacleType": mgreceptacleType,
       "mgreceptacleIdent": mgreceptacleIdent,
       "mgreceptacleState": mgreceptacleState,
       "mgreceptacleReceptacle": mgreceptacleReceptacle,
       "mgreceptaclePowerCons": mgreceptaclePowerCons,
       "mgreceptacleOverload": mgreceptacleOverload,
       "mgreceptacleAutonomy": mgreceptacleAutonomy,
       "upsmgConfig": upsmgConfig,
       "upsmgConfigBatteryInstalled": upsmgConfigBatteryInstalled,
       "upsmgConfigNominalBatteryVoltage": upsmgConfigNominalBatteryVoltage,
       "upsmgConfigNominalBatteryTime": upsmgConfigNominalBatteryTime,
       "upsmgConfigNominalRechargeTime": upsmgConfigNominalRechargeTime,
       "upsmgConfigMinRechargeLevel": upsmgConfigMinRechargeLevel,
       "upsmgConfigMaxRechargeTime": upsmgConfigMaxRechargeTime,
       "upsmgConfigLowBatteryTime": upsmgConfigLowBatteryTime,
       "upsmgConfigLowBatteryLevel": upsmgConfigLowBatteryLevel,
       "upsmgConfigAutoRestart": upsmgConfigAutoRestart,
       "upsmgConfigShutdownTimer": upsmgConfigShutdownTimer,
       "upsmgConfigSysShutDuration": upsmgConfigSysShutDuration,
       "upsmgConfigVARating": upsmgConfigVARating,
       "upsmgConfigLowTransfer": upsmgConfigLowTransfer,
       "upsmgConfigHighTransfer": upsmgConfigHighTransfer,
       "upsmgConfigOutputNominalVoltage": upsmgConfigOutputNominalVoltage,
       "upsmgConfigOutputNominalCurrent": upsmgConfigOutputNominalCurrent,
       "upsmgConfigOutputNomFrequency": upsmgConfigOutputNomFrequency,
       "upsmgConfigByPassType": upsmgConfigByPassType,
       "upsmgConfigAlarmAudible": upsmgConfigAlarmAudible,
       "upsmgConfigAlarmTimeDelay": upsmgConfigAlarmTimeDelay,
       "upsmgConfigDevicesNum": upsmgConfigDevicesNum,
       "upsmgConfigDevicesTable": upsmgConfigDevicesTable,
       "upsmgConfigDevicesEntry": upsmgConfigDevicesEntry,
       "mgdeviceIndex": mgdeviceIndex,
       "mgdeviceReceptacleNum": mgdeviceReceptacleNum,
       "mgdeviceIdent": mgdeviceIdent,
       "mgdeviceVaRating": mgdeviceVaRating,
       "mgdeviceSequenceOff": mgdeviceSequenceOff,
       "mgdeviceSequenceOn": mgdeviceSequenceOn,
       "mgdeviceShutdownDuration": mgdeviceShutdownDuration,
       "mgdeviceBootUpDuration": mgdeviceBootUpDuration,
       "upsmgConfigReceptaclesTable": upsmgConfigReceptaclesTable,
       "upsmgConfigReceptaclesEntry": upsmgConfigReceptaclesEntry,
       "mgreceptacleIndexb": mgreceptacleIndexb,
       "mgreceptacleStateTurnOn": mgreceptacleStateTurnOn,
       "mgreceptacleStateMainReturn": mgreceptacleStateMainReturn,
       "mgreceptacleStateDischarge": mgreceptacleStateDischarge,
       "mgreceptacleShutoffLevel": mgreceptacleShutoffLevel,
       "mgreceptacleShutoffTimer": mgreceptacleShutoffTimer,
       "mgreceptacleRestartLevel": mgreceptacleRestartLevel,
       "mgreceptacleRestartDelay": mgreceptacleRestartDelay,
       "mgreceptacleShutdownDuration": mgreceptacleShutdownDuration,
       "mgreceptacleBootUpDuration": mgreceptacleBootUpDuration,
       "upsmgConfigExtAlarmNum": upsmgConfigExtAlarmNum,
       "upsmgConfigExtAlarmTable": upsmgConfigExtAlarmTable,
       "upsmgConfigExtAlarmEntry": upsmgConfigExtAlarmEntry,
       "mgextAlarmIndex": mgextAlarmIndex,
       "mgextAlarmUID": mgextAlarmUID,
       "upsmgConfigEmergencyTestFail": upsmgConfigEmergencyTestFail,
       "upsmgConfigEmergencyOnByPass": upsmgConfigEmergencyOnByPass,
       "upsmgConfigEmergencyOverload": upsmgConfigEmergencyOverload,
       "upsmgConfigControlDayTable": upsmgConfigControlDayTable,
       "upsmgConfigControlDayEntry": upsmgConfigControlDayEntry,
       "mgcontrolDayIndex": mgcontrolDayIndex,
       "mgcontrolDayOn": mgcontrolDayOn,
       "mgcontrolDayOff": mgcontrolDayOff,
       "upsmgConfigLowBooster": upsmgConfigLowBooster,
       "upsmgConfigHighBooster": upsmgConfigHighBooster,
       "upsmgConfigLowFader": upsmgConfigLowFader,
       "upsmgConfigHighFader": upsmgConfigHighFader,
       "upsmgConfigEnvironmentTable": upsmgConfigEnvironmentTable,
       "upsmgConfigEnvironmentEntry": upsmgConfigEnvironmentEntry,
       "upsmgConfigSensorIndex": upsmgConfigSensorIndex,
       "upsmgConfigSensorName": upsmgConfigSensorName,
       "upsmgConfigTemperatureLow": upsmgConfigTemperatureLow,
       "upsmgConfigTemperatureHigh": upsmgConfigTemperatureHigh,
       "upsmgConfigTemperatureHysteresis": upsmgConfigTemperatureHysteresis,
       "upsmgConfigHumidityLow": upsmgConfigHumidityLow,
       "upsmgConfigHumidityHigh": upsmgConfigHumidityHigh,
       "upsmgConfigHumidityHysteresis": upsmgConfigHumidityHysteresis,
       "upsmgConfigInput1Name": upsmgConfigInput1Name,
       "upsmgConfigInput1ClosedLabel": upsmgConfigInput1ClosedLabel,
       "upsmgConfigInput1OpenLabel": upsmgConfigInput1OpenLabel,
       "upsmgConfigInput2Name": upsmgConfigInput2Name,
       "upsmgConfigInput2ClosedLabel": upsmgConfigInput2ClosedLabel,
       "upsmgConfigInput2OpenLabel": upsmgConfigInput2OpenLabel,
       "upsmgBattery": upsmgBattery,
       "upsmgBatteryRemainingTime": upsmgBatteryRemainingTime,
       "upsmgBatteryLevel": upsmgBatteryLevel,
       "upsmgBatteryRechargeTime": upsmgBatteryRechargeTime,
       "upsmgBatteryRechargeLevel": upsmgBatteryRechargeLevel,
       "upsmgBatteryVoltage": upsmgBatteryVoltage,
       "upsmgBatteryCurrent": upsmgBatteryCurrent,
       "upsmgBatteryTemperature": upsmgBatteryTemperature,
       "upsmgBatteryFullRechargeTime": upsmgBatteryFullRechargeTime,
       "upsmgBatteryFaultBattery": upsmgBatteryFaultBattery,
       "upsmgBatteryNoBattery": upsmgBatteryNoBattery,
       "upsmgBatteryReplacement": upsmgBatteryReplacement,
       "upsmgBatteryUnavailableBattery": upsmgBatteryUnavailableBattery,
       "upsmgBatteryNotHighCharge": upsmgBatteryNotHighCharge,
       "upsmgBatteryLowBattery": upsmgBatteryLowBattery,
       "upsmgBatteryChargerFault": upsmgBatteryChargerFault,
       "upsmgBatteryLowCondition": upsmgBatteryLowCondition,
       "upsmgBatteryLowRecharge": upsmgBatteryLowRecharge,
       "upsmgInput": upsmgInput,
       "upsmgInputPhaseNum": upsmgInputPhaseNum,
       "upsmgInputPhaseTable": upsmgInputPhaseTable,
       "upsmgInputPhaseEntry": upsmgInputPhaseEntry,
       "mginputIndex": mginputIndex,
       "mginputVoltage": mginputVoltage,
       "mginputFrequency": mginputFrequency,
       "mginputMinimumVoltage": mginputMinimumVoltage,
       "mginputMaximumVoltage": mginputMaximumVoltage,
       "mginputCurrent": mginputCurrent,
       "upsmgInputBadStatus": upsmgInputBadStatus,
       "upsmgInputLineFailCause": upsmgInputLineFailCause,
       "upsmgOutput": upsmgOutput,
       "upsmgOutputPhaseNum": upsmgOutputPhaseNum,
       "upsmgOutputPhaseTable": upsmgOutputPhaseTable,
       "upsmgOutputPhaseEntry": upsmgOutputPhaseEntry,
       "mgoutputPhaseIndex": mgoutputPhaseIndex,
       "mgoutputVoltage": mgoutputVoltage,
       "mgoutputFrequency": mgoutputFrequency,
       "mgoutputLoadPerPhase": mgoutputLoadPerPhase,
       "mgoutputCurrent": mgoutputCurrent,
       "upsmgOutputOnBattery": upsmgOutputOnBattery,
       "upsmgOutputOnByPass": upsmgOutputOnByPass,
       "upsmgOutputUnavailableByPass": upsmgOutputUnavailableByPass,
       "upsmgOutputNoByPass": upsmgOutputNoByPass,
       "upsmgOutputUtilityOff": upsmgOutputUtilityOff,
       "upsmgOutputOnBoost": upsmgOutputOnBoost,
       "upsmgOutputInverterOff": upsmgOutputInverterOff,
       "upsmgOutputOverLoad": upsmgOutputOverLoad,
       "upsmgOutputOverTemp": upsmgOutputOverTemp,
       "upsmgOutputOnBuck": upsmgOutputOnBuck,
       "upsmgEnviron": upsmgEnviron,
       "upsmgEnvironAmbientTemp": upsmgEnvironAmbientTemp,
       "upsmgEnvironAmbientHumidity": upsmgEnvironAmbientHumidity,
       "upsmgEnvironExtAlarmTable": upsmgEnvironExtAlarmTable,
       "upsmgEnvironExtAlarmEntry": upsmgEnvironExtAlarmEntry,
       "mgalarmNum": mgalarmNum,
       "mgalarmState": mgalarmState,
       "upsmgEnvironSensorNum": upsmgEnvironSensorNum,
       "upsmgEnvironSensorTable": upsmgEnvironSensorTable,
       "upsmgEnvironSensorEntry": upsmgEnvironSensorEntry,
       "mgsensorNum": mgsensorNum,
       "mgsensorTemp": mgsensorTemp,
       "mgsensorHumidity": mgsensorHumidity,
       "upsmgEnvironmentNum": upsmgEnvironmentNum,
       "upsmgEnvironmentSensorTable": upsmgEnvironmentSensorTable,
       "upsmgEnvironmentSensorEntry": upsmgEnvironmentSensorEntry,
       "upsmgEnvironmentIndex": upsmgEnvironmentIndex,
       "upsmgEnvironmentComFailure": upsmgEnvironmentComFailure,
       "upsmgEnvironmentTemperature": upsmgEnvironmentTemperature,
       "upsmgEnvironmentTemperatureLow": upsmgEnvironmentTemperatureLow,
       "upsmgEnvironmentTemperatureHigh": upsmgEnvironmentTemperatureHigh,
       "upsmgEnvironmentHumidity": upsmgEnvironmentHumidity,
       "upsmgEnvironmentHumidityLow": upsmgEnvironmentHumidityLow,
       "upsmgEnvironmentHumidityHigh": upsmgEnvironmentHumidityHigh,
       "upsmgEnvironmentInput1State": upsmgEnvironmentInput1State,
       "upsmgEnvironmentInput2State": upsmgEnvironmentInput2State,
       "upsmgControl": upsmgControl,
       "upsmgControlReceptaclesTable": upsmgControlReceptaclesTable,
       "upsmgControlReceptaclesEntry": upsmgControlReceptaclesEntry,
       "mgreceptacleIndexc": mgreceptacleIndexc,
       "mgreceptacleOnDelay": mgreceptacleOnDelay,
       "mgreceptacleOnCtrl": mgreceptacleOnCtrl,
       "mgreceptacleOnStatus": mgreceptacleOnStatus,
       "mgreceptacleOffDelay": mgreceptacleOffDelay,
       "mgreceptacleOffCtrl": mgreceptacleOffCtrl,
       "mgreceptacleOffStatus": mgreceptacleOffStatus,
       "mgreceptacleToggleDelay": mgreceptacleToggleDelay,
       "mgreceptacleToggleCtrl": mgreceptacleToggleCtrl,
       "mgreceptacleToggleStatus": mgreceptacleToggleStatus,
       "mgreceptacleToggleDuration": mgreceptacleToggleDuration,
       "upsmgControlDayOff": upsmgControlDayOff,
       "upsmgControlDayOn": upsmgControlDayOn,
       "upsmgTest": upsmgTest,
       "upsmgTestBatterySchedule": upsmgTestBatterySchedule,
       "upsmgTestDiagnostics": upsmgTestDiagnostics,
       "upsmgTestDiagResult": upsmgTestDiagResult,
       "upsmgTestBatteryCalibration": upsmgTestBatteryCalibration,
       "upsmgTestLastCalibration": upsmgTestLastCalibration,
       "upsmgTestIndicators": upsmgTestIndicators,
       "upsmgTestCommandLine": upsmgTestCommandLine,
       "upsmgTestCommandReady": upsmgTestCommandReady,
       "upsmgTestResponseLine": upsmgTestResponseLine,
       "upsmgTestResponseReady": upsmgTestResponseReady,
       "upsmgTestBatteryResult": upsmgTestBatteryResult,
       "upsmgTraps": upsmgTraps,
       "upsmgBatteryFault": upsmgBatteryFault,
       "upsmgBatteryOK": upsmgBatteryOK,
       "upsmgBatteryReplacementIndicated": upsmgBatteryReplacementIndicated,
       "upsmgBatteryReplaceNotIndicated": upsmgBatteryReplaceNotIndicated,
       "upsmgAtLowBattery": upsmgAtLowBattery,
       "upsmgFromLowBattery": upsmgFromLowBattery,
       "upsmgChargerFault": upsmgChargerFault,
       "upsmgChargerOK": upsmgChargerOK,
       "upsmgAtLowCondition": upsmgAtLowCondition,
       "upsmgFromLowCondition": upsmgFromLowCondition,
       "upsmgOnBattery": upsmgOnBattery,
       "upsmgReturnFromBattery": upsmgReturnFromBattery,
       "upsmgOnByPass": upsmgOnByPass,
       "upsmgReturnFromByPass": upsmgReturnFromByPass,
       "upsmgByPassUnavailable": upsmgByPassUnavailable,
       "upsmgByPassAvailable": upsmgByPassAvailable,
       "upsmgUtilityFailure": upsmgUtilityFailure,
       "upsmgUtilityRestored": upsmgUtilityRestored,
       "upsmgOnBoost": upsmgOnBoost,
       "upsmgReturnFromBoost": upsmgReturnFromBoost,
       "upsmgOverLoad": upsmgOverLoad,
       "upsmgLoadOK": upsmgLoadOK,
       "upsmgOverTemperature": upsmgOverTemperature,
       "upsmgTemperatureOK": upsmgTemperatureOK,
       "upsmgOnToStart": upsmgOnToStart,
       "upsmgOnAbort": upsmgOnAbort,
       "upsmgOnInProgress": upsmgOnInProgress,
       "upsmgOnComplete": upsmgOnComplete,
       "upsmgOffToStart": upsmgOffToStart,
       "upsmgOffAbort": upsmgOffAbort,
       "upsmgOffInProgress": upsmgOffInProgress,
       "upsmgOffComplete": upsmgOffComplete,
       "upsmgToggleToStart": upsmgToggleToStart,
       "upsmgToggleAbort": upsmgToggleAbort,
       "upsmgToggleInProgress": upsmgToggleInProgress,
       "upsmgToggleComplete": upsmgToggleComplete,
       "upsmgCommunicationFailure": upsmgCommunicationFailure,
       "upsmgCommunicationRestored": upsmgCommunicationRestored,
       "upsmgInputBad": upsmgInputBad,
       "upsmgInputOK": upsmgInputOK,
       "upsmgBatteryUnavailable": upsmgBatteryUnavailable,
       "upsmgBatteryAvailable": upsmgBatteryAvailable,
       "upsmgAtLowRecharge": upsmgAtLowRecharge,
       "upsmgFromLowRecharge": upsmgFromLowRecharge,
       "upsmgDiagnosticTestFail": upsmgDiagnosticTestFail,
       "upsmgDiagnosticTestOK": upsmgDiagnosticTestOK,
       "upsmgBatteryTestOK": upsmgBatteryTestOK,
       "upsmgBatteryTestFail": upsmgBatteryTestFail,
       "upsmgExternalAlarmActive": upsmgExternalAlarmActive,
       "upsmgExternalAlarmInactive": upsmgExternalAlarmInactive,
       "upsmgOnBuck": upsmgOnBuck,
       "upsmgReturnFromBuck": upsmgReturnFromBuck,
       "upsmgEnvironComFailure": upsmgEnvironComFailure,
       "upsmgEnvironComOK": upsmgEnvironComOK,
       "upsmgEnvironTemperatureLow": upsmgEnvironTemperatureLow,
       "upsmgEnvironTemperatureHigh": upsmgEnvironTemperatureHigh,
       "upsmgEnvironTemperatureOK": upsmgEnvironTemperatureOK,
       "upsmgEnvironHumidityLow": upsmgEnvironHumidityLow,
       "upsmgEnvironHumidityHigh": upsmgEnvironHumidityHigh,
       "upsmgEnvironHumidityOK": upsmgEnvironHumidityOK,
       "upsmgEnvironInput1Closed": upsmgEnvironInput1Closed,
       "upsmgEnvironInput1Open": upsmgEnvironInput1Open,
       "upsmgEnvironInput2Closed": upsmgEnvironInput2Closed,
       "upsmgEnvironInput2Open": upsmgEnvironInput2Open,
       "upsmgAgent": upsmgAgent,
       "upsmgAgentIpaddress": upsmgAgentIpaddress,
       "upsmgAgentSubnetMask": upsmgAgentSubnetMask,
       "upsmgAgentDefGateway": upsmgAgentDefGateway,
       "upsmgAgentBaudRate": upsmgAgentBaudRate,
       "upsmgAgentPollRate": upsmgAgentPollRate,
       "upsmgAgentType": upsmgAgentType,
       "upsmgAgentTrapAlarmDelay": upsmgAgentTrapAlarmDelay,
       "upsmgAgentTrapAlarmRetry": upsmgAgentTrapAlarmRetry,
       "upsmgAgentReset": upsmgAgentReset,
       "upsmgAgentFactReset": upsmgAgentFactReset,
       "upsmgAgentMibVersion": upsmgAgentMibVersion,
       "upsmgAgentFirmwareVersion": upsmgAgentFirmwareVersion,
       "upsmgAgentCommUPS": upsmgAgentCommUPS,
       "upsmgAgentTrapAck": upsmgAgentTrapAck,
       "upsmgAgentAutoLearning": upsmgAgentAutoLearning,
       "upsmgAgentBootP": upsmgAgentBootP,
       "upsmgAgentTFTP": upsmgAgentTFTP,
       "upsmgAgentTrapSignature": upsmgAgentTrapSignature,
       "upsmgRemote": upsmgRemote,
       "upsmgRemoteOnBattery": upsmgRemoteOnBattery,
       "upsmgRemoteIpAddress": upsmgRemoteIpAddress}
)
