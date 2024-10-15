# SNMP MIB module (MRV-IR-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IR-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:47 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

irSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1)
)


# Types definitions



class TrapSeverity(Integer32):
    """Custom type TrapSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("critical", 6),
          ("informational", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )





class TarCreator(Integer32):
    """Custom type TarCreator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("snmp", 3),
          ("system", 2))
    )





class TarTrigType(Integer32):
    """Custom type TarTrigType based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 10),
          ("analog", 13),
          ("bootp", 9),
          ("compound", 8),
          ("duration", 17),
          ("hdam", 11),
          ("hdampower", 18),
          ("hdampowerInput", 20),
          ("hdampowerReg", 19),
          ("humidity", 3),
          ("inputSignal", 7),
          ("instant", 4),
          ("onboardTemp", 16),
          ("other", 1),
          ("pattern", 6),
          ("ping", 5),
          ("power", 12),
          ("powerContact", 23),
          ("powerInput", 15),
          ("powerLoad", 21),
          ("powerLoadInput", 22),
          ("powerReg", 14),
          ("temp", 2),
          ("upsBattery", 24))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MrvBpd_ObjectIdentity = ObjectIdentity
mrvBpd = _MrvBpd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_MrvLx_ObjectIdentity = ObjectIdentity
mrvLx = _MrvLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100)
)
_IrSysSystem_ObjectIdentity = ObjectIdentity
irSysSystem = _IrSysSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1)
)
_IrSysImageFilename_Type = DisplayString
_IrSysImageFilename_Object = MibScalar
irSysImageFilename = _IrSysImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 1),
    _IrSysImageFilename_Type()
)
irSysImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysImageFilename.setStatus("current")


class _IrSysImageSource_Type(Integer32):
    """Custom type irSysImageSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("network", 2))
    )


_IrSysImageSource_Type.__name__ = "Integer32"
_IrSysImageSource_Object = MibScalar
irSysImageSource = _IrSysImageSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 2),
    _IrSysImageSource_Type()
)
irSysImageSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysImageSource.setStatus("current")
_IrSysImageServer_Type = IpAddress
_IrSysImageServer_Object = MibScalar
irSysImageServer = _IrSysImageServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 3),
    _IrSysImageServer_Type()
)
irSysImageServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysImageServer.setStatus("current")
_IrSysSwVersion_Type = DisplayString
_IrSysSwVersion_Object = MibScalar
irSysSwVersion = _IrSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 4),
    _IrSysSwVersion_Type()
)
irSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysSwVersion.setStatus("current")
_IrSysSwBootVersion_Type = DisplayString
_IrSysSwBootVersion_Object = MibScalar
irSysSwBootVersion = _IrSysSwBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 5),
    _IrSysSwBootVersion_Type()
)
irSysSwBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysSwBootVersion.setStatus("current")
_IrSysIpAddress_Type = IpAddress
_IrSysIpAddress_Object = MibScalar
irSysIpAddress = _IrSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 6),
    _IrSysIpAddress_Type()
)
irSysIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysIpAddress.setStatus("current")
_IrSysSubnetMask_Type = IpAddress
_IrSysSubnetMask_Object = MibScalar
irSysSubnetMask = _IrSysSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 7),
    _IrSysSubnetMask_Type()
)
irSysSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysSubnetMask.setStatus("current")
_IrSysBcastAddress_Type = IpAddress
_IrSysBcastAddress_Object = MibScalar
irSysBcastAddress = _IrSysBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 8),
    _IrSysBcastAddress_Type()
)
irSysBcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysBcastAddress.setStatus("current")
_IrSysGateway_Type = IpAddress
_IrSysGateway_Object = MibScalar
irSysGateway = _IrSysGateway_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 9),
    _IrSysGateway_Type()
)
irSysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysGateway.setStatus("current")


class _IrSysAction_Type(Integer32):
    """Custom type irSysAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 3),
          ("saveConfig", 2))
    )


_IrSysAction_Type.__name__ = "Integer32"
_IrSysAction_Object = MibScalar
irSysAction = _IrSysAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 10),
    _IrSysAction_Type()
)
irSysAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysAction.setStatus("current")
_IrSysSnmpSetErrorString_Type = DisplayString
_IrSysSnmpSetErrorString_Object = MibScalar
irSysSnmpSetErrorString = _IrSysSnmpSetErrorString_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 11),
    _IrSysSnmpSetErrorString_Type()
)
irSysSnmpSetErrorString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysSnmpSetErrorString.setStatus("current")
_IrSysModelType_Type = DisplayString
_IrSysModelType_Object = MibScalar
irSysModelType = _IrSysModelType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 12),
    _IrSysModelType_Type()
)
irSysModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysModelType.setStatus("current")


class _IrSysPowerType_Type(Integer32):
    """Custom type irSysPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerAC", 1),
          ("powerDC", 2))
    )


_IrSysPowerType_Type.__name__ = "Integer32"
_IrSysPowerType_Object = MibScalar
irSysPowerType = _IrSysPowerType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 13),
    _IrSysPowerType_Type()
)
irSysPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysPowerType.setStatus("current")
_IrSysCurrentTemp_Type = Integer32
_IrSysCurrentTemp_Object = MibScalar
irSysCurrentTemp = _IrSysCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 14),
    _IrSysCurrentTemp_Type()
)
irSysCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysCurrentTemp.setStatus("current")
_IrSysTempThresholdLow_Type = Integer32
_IrSysTempThresholdLow_Object = MibScalar
irSysTempThresholdLow = _IrSysTempThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 15),
    _IrSysTempThresholdLow_Type()
)
irSysTempThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysTempThresholdLow.setStatus("current")
_IrSysTempThresholdHigh_Type = Integer32
_IrSysTempThresholdHigh_Object = MibScalar
irSysTempThresholdHigh = _IrSysTempThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 16),
    _IrSysTempThresholdHigh_Type()
)
irSysTempThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysTempThresholdHigh.setStatus("current")


class _IrSysTempHysteresis_Type(Integer32):
    """Custom type irSysTempHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_IrSysTempHysteresis_Type.__name__ = "Integer32"
_IrSysTempHysteresis_Object = MibScalar
irSysTempHysteresis = _IrSysTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 18),
    _IrSysTempHysteresis_Type()
)
irSysTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysTempHysteresis.setStatus("current")
_IrSysPowerLostTimestamp_Type = DisplayString
_IrSysPowerLostTimestamp_Object = MibScalar
irSysPowerLostTimestamp = _IrSysPowerLostTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 19),
    _IrSysPowerLostTimestamp_Type()
)
irSysPowerLostTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysPowerLostTimestamp.setStatus("current")


class _IrSysFipsMode_Type(Integer32):
    """Custom type irSysFipsMode based on Integer32"""
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


_IrSysFipsMode_Type.__name__ = "Integer32"
_IrSysFipsMode_Object = MibScalar
irSysFipsMode = _IrSysFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 20),
    _IrSysFipsMode_Type()
)
irSysFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysFipsMode.setStatus("current")


class _IrSysFlashMemSize_Type(Integer32):
    """Custom type irSysFlashMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s16M", 2),
          ("s8M", 1))
    )


_IrSysFlashMemSize_Type.__name__ = "Integer32"
_IrSysFlashMemSize_Object = MibScalar
irSysFlashMemSize = _IrSysFlashMemSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 21),
    _IrSysFlashMemSize_Type()
)
irSysFlashMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysFlashMemSize.setStatus("current")


class _IrSysAssetTag_Type(DisplayString):
    """Custom type irSysAssetTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrSysAssetTag_Type.__name__ = "DisplayString"
_IrSysAssetTag_Object = MibScalar
irSysAssetTag = _IrSysAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 22),
    _IrSysAssetTag_Type()
)
irSysAssetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irSysAssetTag.setStatus("current")
_IrSysPowerCurrentLoad_Type = DisplayString
_IrSysPowerCurrentLoad_Object = MibScalar
irSysPowerCurrentLoad = _IrSysPowerCurrentLoad_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 1, 23),
    _IrSysPowerCurrentLoad_Type()
)
irSysPowerCurrentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irSysPowerCurrentLoad.setStatus("current")
_IrDevices_ObjectIdentity = ObjectIdentity
irDevices = _IrDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2)
)
_IrDeviceLx_ObjectIdentity = ObjectIdentity
irDeviceLx = _IrDeviceLx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1)
)
_IrLx1001_ObjectIdentity = ObjectIdentity
irLx1001 = _IrLx1001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 1)
)
_IrLx1002_ObjectIdentity = ObjectIdentity
irLx1002 = _IrLx1002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 2)
)
_IrLx1004_ObjectIdentity = ObjectIdentity
irLx1004 = _IrLx1004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 3)
)
_IrLx4008_ObjectIdentity = ObjectIdentity
irLx4008 = _IrLx4008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 4)
)
_IrLx4016_ObjectIdentity = ObjectIdentity
irLx4016 = _IrLx4016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 5)
)
_IrLx4032_ObjectIdentity = ObjectIdentity
irLx4032 = _IrLx4032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 6)
)
_IrLx4048_ObjectIdentity = ObjectIdentity
irLx4048 = _IrLx4048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 7)
)
_IrLxEm316_ObjectIdentity = ObjectIdentity
irLxEm316 = _IrLxEm316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 8)
)
_IrLx8020_ObjectIdentity = ObjectIdentity
irLx8020 = _IrLx8020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 9)
)
_IrLx8040_ObjectIdentity = ObjectIdentity
irLx8040 = _IrLx8040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 10)
)
_IrLx4000T_ObjectIdentity = ObjectIdentity
irLx4000T = _IrLx4000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 11)
)
_IrLx7304T_ObjectIdentity = ObjectIdentity
irLx7304T = _IrLx7304T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 12)
)
_IrLx4108T_ObjectIdentity = ObjectIdentity
irLx4108T = _IrLx4108T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 2, 1, 13)
)
_IrTraps_ObjectIdentity = ObjectIdentity
irTraps = _IrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 3)
)
_IrCluster_ObjectIdentity = ObjectIdentity
irCluster = _IrCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4)
)
_IrClusterGrp_ObjectIdentity = ObjectIdentity
irClusterGrp = _IrClusterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 1)
)


class _IrClusterCfgStatus_Type(Integer32):
    """Custom type irClusterCfgStatus based on Integer32"""
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


_IrClusterCfgStatus_Type.__name__ = "Integer32"
_IrClusterCfgStatus_Object = MibScalar
irClusterCfgStatus = _IrClusterCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 1, 1),
    _IrClusterCfgStatus_Type()
)
irClusterCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irClusterCfgStatus.setStatus("current")


class _IrClusterName_Type(DisplayString):
    """Custom type irClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrClusterName_Type.__name__ = "DisplayString"
_IrClusterName_Object = MibScalar
irClusterName = _IrClusterName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 1, 2),
    _IrClusterName_Type()
)
irClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irClusterName.setStatus("current")


class _IrClusterSyncStatus_Type(Integer32):
    """Custom type irClusterSyncStatus based on Integer32"""
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
        *(("idle", 1),
          ("syncCompletedError", 4),
          ("syncCompletedSuccess", 3),
          ("syncInProgress", 2))
    )


_IrClusterSyncStatus_Type.__name__ = "Integer32"
_IrClusterSyncStatus_Object = MibScalar
irClusterSyncStatus = _IrClusterSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 1, 3),
    _IrClusterSyncStatus_Type()
)
irClusterSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irClusterSyncStatus.setStatus("current")


class _IrClusterAction_Type(Integer32):
    """Custom type irClusterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushAll", 2),
          ("other", 1))
    )


_IrClusterAction_Type.__name__ = "Integer32"
_IrClusterAction_Object = MibScalar
irClusterAction = _IrClusterAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 1, 4),
    _IrClusterAction_Type()
)
irClusterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irClusterAction.setStatus("current")
_IrClusterTable_Object = MibTable
irClusterTable = _IrClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 2)
)
if mibBuilder.loadTexts:
    irClusterTable.setStatus("current")
_IrClusterEntry_Object = MibTableRow
irClusterEntry = _IrClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 2, 1)
)
irClusterEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "irClusterIpAddr"),
)
if mibBuilder.loadTexts:
    irClusterEntry.setStatus("current")
_IrClusterIpAddr_Type = IpAddress
_IrClusterIpAddr_Object = MibTableColumn
irClusterIpAddr = _IrClusterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 2, 1, 1),
    _IrClusterIpAddr_Type()
)
irClusterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irClusterIpAddr.setStatus("current")
_IrClusterStatus_Type = RowStatus
_IrClusterStatus_Object = MibTableColumn
irClusterStatus = _IrClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 4, 2, 1, 2),
    _IrClusterStatus_Type()
)
irClusterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    irClusterStatus.setStatus("current")
_IrEthernet_ObjectIdentity = ObjectIdentity
irEthernet = _IrEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5)
)
_IrEnetPortConfigTable_Object = MibTable
irEnetPortConfigTable = _IrEnetPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1)
)
if mibBuilder.loadTexts:
    irEnetPortConfigTable.setStatus("current")
_IrEnetPortConfigEntry_Object = MibTableRow
irEnetPortConfigEntry = _IrEnetPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1)
)
irEnetPortConfigEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "irEnetPortIndex"),
)
if mibBuilder.loadTexts:
    irEnetPortConfigEntry.setStatus("current")
_IrEnetPortIndex_Type = Integer32
_IrEnetPortIndex_Object = MibTableColumn
irEnetPortIndex = _IrEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 1),
    _IrEnetPortIndex_Type()
)
irEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortIndex.setStatus("current")


class _IrEnetPortSpeed_Type(Integer32):
    """Custom type irEnetPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sp100M", 2),
          ("sp10M", 1))
    )


_IrEnetPortSpeed_Type.__name__ = "Integer32"
_IrEnetPortSpeed_Object = MibTableColumn
irEnetPortSpeed = _IrEnetPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 2),
    _IrEnetPortSpeed_Type()
)
irEnetPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortSpeed.setStatus("current")


class _IrEnetPortDuplexMode_Type(Integer32):
    """Custom type irEnetPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("none", 1))
    )


_IrEnetPortDuplexMode_Type.__name__ = "Integer32"
_IrEnetPortDuplexMode_Object = MibTableColumn
irEnetPortDuplexMode = _IrEnetPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 3),
    _IrEnetPortDuplexMode_Type()
)
irEnetPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortDuplexMode.setStatus("current")


class _IrEnetPortAutoNegotiation_Type(Integer32):
    """Custom type irEnetPortAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("none", 1))
    )


_IrEnetPortAutoNegotiation_Type.__name__ = "Integer32"
_IrEnetPortAutoNegotiation_Object = MibTableColumn
irEnetPortAutoNegotiation = _IrEnetPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 4),
    _IrEnetPortAutoNegotiation_Type()
)
irEnetPortAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortAutoNegotiation.setStatus("current")


class _IrEnetPortPhysMedia_Type(Integer32):
    """Custom type irEnetPortPhysMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet", 1),
          ("sfp", 2))
    )


_IrEnetPortPhysMedia_Type.__name__ = "Integer32"
_IrEnetPortPhysMedia_Object = MibTableColumn
irEnetPortPhysMedia = _IrEnetPortPhysMedia_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 5),
    _IrEnetPortPhysMedia_Type()
)
irEnetPortPhysMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortPhysMedia.setStatus("current")


class _IrEnetPortLinkStatus_Type(Integer32):
    """Custom type irEnetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_IrEnetPortLinkStatus_Type.__name__ = "Integer32"
_IrEnetPortLinkStatus_Object = MibTableColumn
irEnetPortLinkStatus = _IrEnetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 6),
    _IrEnetPortLinkStatus_Type()
)
irEnetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortLinkStatus.setStatus("current")


class _IrEnetPortBondingStatus_Type(Integer32):
    """Custom type irEnetPortBondingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("backup", 3),
          ("none", 1))
    )


_IrEnetPortBondingStatus_Type.__name__ = "Integer32"
_IrEnetPortBondingStatus_Object = MibTableColumn
irEnetPortBondingStatus = _IrEnetPortBondingStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 1, 1, 7),
    _IrEnetPortBondingStatus_Type()
)
irEnetPortBondingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortBondingStatus.setStatus("current")
_IrEnetPortStatsTable_Object = MibTable
irEnetPortStatsTable = _IrEnetPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2)
)
if mibBuilder.loadTexts:
    irEnetPortStatsTable.setStatus("current")
_IrEnetPortStatsEntry_Object = MibTableRow
irEnetPortStatsEntry = _IrEnetPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    irEnetPortStatsEntry.setStatus("current")
_IrEnetPortRecvBytes_Type = Counter32
_IrEnetPortRecvBytes_Object = MibTableColumn
irEnetPortRecvBytes = _IrEnetPortRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 1),
    _IrEnetPortRecvBytes_Type()
)
irEnetPortRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvBytes.setStatus("current")
_IrEnetPortRecvPackets_Type = Counter32
_IrEnetPortRecvPackets_Object = MibTableColumn
irEnetPortRecvPackets = _IrEnetPortRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 2),
    _IrEnetPortRecvPackets_Type()
)
irEnetPortRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvPackets.setStatus("current")
_IrEnetPortRecvErrors_Type = Counter32
_IrEnetPortRecvErrors_Object = MibTableColumn
irEnetPortRecvErrors = _IrEnetPortRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 3),
    _IrEnetPortRecvErrors_Type()
)
irEnetPortRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvErrors.setStatus("current")
_IrEnetPortRecvDropped_Type = Counter32
_IrEnetPortRecvDropped_Object = MibTableColumn
irEnetPortRecvDropped = _IrEnetPortRecvDropped_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 4),
    _IrEnetPortRecvDropped_Type()
)
irEnetPortRecvDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvDropped.setStatus("current")
_IrEnetPortRecvOverruns_Type = Counter32
_IrEnetPortRecvOverruns_Object = MibTableColumn
irEnetPortRecvOverruns = _IrEnetPortRecvOverruns_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 5),
    _IrEnetPortRecvOverruns_Type()
)
irEnetPortRecvOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvOverruns.setStatus("current")
_IrEnetPortRecvFrameErrors_Type = Counter32
_IrEnetPortRecvFrameErrors_Object = MibTableColumn
irEnetPortRecvFrameErrors = _IrEnetPortRecvFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 6),
    _IrEnetPortRecvFrameErrors_Type()
)
irEnetPortRecvFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvFrameErrors.setStatus("current")
_IrEnetPortRecvMulticast_Type = Counter32
_IrEnetPortRecvMulticast_Object = MibTableColumn
irEnetPortRecvMulticast = _IrEnetPortRecvMulticast_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 7),
    _IrEnetPortRecvMulticast_Type()
)
irEnetPortRecvMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvMulticast.setStatus("current")
_IrEnetPortRecvCompressed_Type = Counter32
_IrEnetPortRecvCompressed_Object = MibTableColumn
irEnetPortRecvCompressed = _IrEnetPortRecvCompressed_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 8),
    _IrEnetPortRecvCompressed_Type()
)
irEnetPortRecvCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortRecvCompressed.setStatus("current")
_IrEnetPortXmitBytes_Type = Counter32
_IrEnetPortXmitBytes_Object = MibTableColumn
irEnetPortXmitBytes = _IrEnetPortXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 9),
    _IrEnetPortXmitBytes_Type()
)
irEnetPortXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitBytes.setStatus("current")
_IrEnetPortXmitPackets_Type = Counter32
_IrEnetPortXmitPackets_Object = MibTableColumn
irEnetPortXmitPackets = _IrEnetPortXmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 10),
    _IrEnetPortXmitPackets_Type()
)
irEnetPortXmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitPackets.setStatus("current")
_IrEnetPortXmitErrors_Type = Counter32
_IrEnetPortXmitErrors_Object = MibTableColumn
irEnetPortXmitErrors = _IrEnetPortXmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 11),
    _IrEnetPortXmitErrors_Type()
)
irEnetPortXmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitErrors.setStatus("current")
_IrEnetPortXmitDropped_Type = Counter32
_IrEnetPortXmitDropped_Object = MibTableColumn
irEnetPortXmitDropped = _IrEnetPortXmitDropped_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 12),
    _IrEnetPortXmitDropped_Type()
)
irEnetPortXmitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitDropped.setStatus("current")
_IrEnetPortXmitOverruns_Type = Counter32
_IrEnetPortXmitOverruns_Object = MibTableColumn
irEnetPortXmitOverruns = _IrEnetPortXmitOverruns_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 13),
    _IrEnetPortXmitOverruns_Type()
)
irEnetPortXmitOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitOverruns.setStatus("current")
_IrEnetPortXmitCollisions_Type = Counter32
_IrEnetPortXmitCollisions_Object = MibTableColumn
irEnetPortXmitCollisions = _IrEnetPortXmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 14),
    _IrEnetPortXmitCollisions_Type()
)
irEnetPortXmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitCollisions.setStatus("current")
_IrEnetPortXmitCompressed_Type = Counter32
_IrEnetPortXmitCompressed_Object = MibTableColumn
irEnetPortXmitCompressed = _IrEnetPortXmitCompressed_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 15),
    _IrEnetPortXmitCompressed_Type()
)
irEnetPortXmitCompressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitCompressed.setStatus("current")
_IrEnetPortXmitCarrier_Type = Counter32
_IrEnetPortXmitCarrier_Object = MibTableColumn
irEnetPortXmitCarrier = _IrEnetPortXmitCarrier_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 5, 2, 1, 16),
    _IrEnetPortXmitCarrier_Type()
)
irEnetPortXmitCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irEnetPortXmitCarrier.setStatus("current")
_IrPower_ObjectIdentity = ObjectIdentity
irPower = _IrPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6)
)
_IrPowerSupplyTable_Object = MibTable
irPowerSupplyTable = _IrPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1)
)
if mibBuilder.loadTexts:
    irPowerSupplyTable.setStatus("current")
_IrPowerSupplyEntry_Object = MibTableRow
irPowerSupplyEntry = _IrPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1)
)
irPowerSupplyEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "irPowerIndex"),
)
if mibBuilder.loadTexts:
    irPowerSupplyEntry.setStatus("current")
_IrPowerIndex_Type = Integer32
_IrPowerIndex_Object = MibTableColumn
irPowerIndex = _IrPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 1),
    _IrPowerIndex_Type()
)
irPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerIndex.setStatus("current")


class _IrPowerUnitPresent_Type(Integer32):
    """Custom type irPowerUnitPresent based on Integer32"""
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


_IrPowerUnitPresent_Type.__name__ = "Integer32"
_IrPowerUnitPresent_Object = MibTableColumn
irPowerUnitPresent = _IrPowerUnitPresent_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 2),
    _IrPowerUnitPresent_Type()
)
irPowerUnitPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerUnitPresent.setStatus("current")


class _IrPowerInputStatus_Type(Integer32):
    """Custom type irPowerInputStatus based on Integer32"""
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


_IrPowerInputStatus_Type.__name__ = "Integer32"
_IrPowerInputStatus_Object = MibTableColumn
irPowerInputStatus = _IrPowerInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 3),
    _IrPowerInputStatus_Type()
)
irPowerInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerInputStatus.setStatus("current")


class _IrPowerOutputStatus_Type(Integer32):
    """Custom type irPowerOutputStatus based on Integer32"""
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


_IrPowerOutputStatus_Type.__name__ = "Integer32"
_IrPowerOutputStatus_Object = MibTableColumn
irPowerOutputStatus = _IrPowerOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 4),
    _IrPowerOutputStatus_Type()
)
irPowerOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutputStatus.setStatus("current")


class _IrPowerStatus_Type(Integer32):
    """Custom type irPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("off", 2),
          ("on", 1))
    )


_IrPowerStatus_Type.__name__ = "Integer32"
_IrPowerStatus_Object = MibTableColumn
irPowerStatus = _IrPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 5),
    _IrPowerStatus_Type()
)
irPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerStatus.setStatus("current")
_IrPowerInputVoltage_Type = DisplayString
_IrPowerInputVoltage_Object = MibTableColumn
irPowerInputVoltage = _IrPowerInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 6),
    _IrPowerInputVoltage_Type()
)
irPowerInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerInputVoltage.setStatus("current")
_IrPowerOutputVoltage_Type = DisplayString
_IrPowerOutputVoltage_Object = MibTableColumn
irPowerOutputVoltage = _IrPowerOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 6, 1, 1, 7),
    _IrPowerOutputVoltage_Type()
)
irPowerOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutputVoltage.setStatus("current")
_IrInterfaces_ObjectIdentity = ObjectIdentity
irInterfaces = _IrInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7)
)
_IrIfTable_Object = MibTable
irIfTable = _IrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1)
)
if mibBuilder.loadTexts:
    irIfTable.setStatus("current")
_IrIfEntry_Object = MibTableRow
irIfEntry = _IrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1)
)
irIfEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "irIfIndex"),
)
if mibBuilder.loadTexts:
    irIfEntry.setStatus("current")
_IrIfIndex_Type = Integer32
_IrIfIndex_Object = MibTableColumn
irIfIndex = _IrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 1),
    _IrIfIndex_Type()
)
irIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfIndex.setStatus("current")
_IrIfIpAddress_Type = IpAddress
_IrIfIpAddress_Object = MibTableColumn
irIfIpAddress = _IrIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 2),
    _IrIfIpAddress_Type()
)
irIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfIpAddress.setStatus("current")
_IrIfIpSubnetMask_Type = IpAddress
_IrIfIpSubnetMask_Object = MibTableColumn
irIfIpSubnetMask = _IrIfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 3),
    _IrIfIpSubnetMask_Type()
)
irIfIpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfIpSubnetMask.setStatus("current")
_IrIfIpBcastAddress_Type = IpAddress
_IrIfIpBcastAddress_Object = MibTableColumn
irIfIpBcastAddress = _IrIfIpBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 4),
    _IrIfIpBcastAddress_Type()
)
irIfIpBcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfIpBcastAddress.setStatus("current")


class _IrIfMtu_Type(Integer32):
    """Custom type irIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_IrIfMtu_Type.__name__ = "Integer32"
_IrIfMtu_Object = MibTableColumn
irIfMtu = _IrIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 5),
    _IrIfMtu_Type()
)
irIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfMtu.setStatus("current")


class _IrIfName_Type(DisplayString):
    """Custom type irIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrIfName_Type.__name__ = "DisplayString"
_IrIfName_Object = MibTableColumn
irIfName = _IrIfName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 6),
    _IrIfName_Type()
)
irIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfName.setStatus("current")


class _IrIfBoundTo_Type(DisplayString):
    """Custom type irIfBoundTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrIfBoundTo_Type.__name__ = "DisplayString"
_IrIfBoundTo_Object = MibTableColumn
irIfBoundTo = _IrIfBoundTo_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 7),
    _IrIfBoundTo_Type()
)
irIfBoundTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfBoundTo.setStatus("current")


class _IrIfTelnetPort_Type(Integer32):
    """Custom type irIfTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IrIfTelnetPort_Type.__name__ = "Integer32"
_IrIfTelnetPort_Object = MibTableColumn
irIfTelnetPort = _IrIfTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 8),
    _IrIfTelnetPort_Type()
)
irIfTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfTelnetPort.setStatus("current")


class _IrIfSshPort_Type(Integer32):
    """Custom type irIfSshPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IrIfSshPort_Type.__name__ = "Integer32"
_IrIfSshPort_Object = MibTableColumn
irIfSshPort = _IrIfSshPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 7, 1, 1, 9),
    _IrIfSshPort_Type()
)
irIfSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIfSshPort.setStatus("current")
_IrTar_ObjectIdentity = ObjectIdentity
irTar = _IrTar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8)
)
_IrTarSys_ObjectIdentity = ObjectIdentity
irTarSys = _IrTarSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 1)
)


class _TarNextFreeTrigIndex_Type(Integer32):
    """Custom type tarNextFreeTrigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TarNextFreeTrigIndex_Type.__name__ = "Integer32"
_TarNextFreeTrigIndex_Object = MibScalar
tarNextFreeTrigIndex = _TarNextFreeTrigIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 1, 1),
    _TarNextFreeTrigIndex_Type()
)
tarNextFreeTrigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarNextFreeTrigIndex.setStatus("current")


class _TarNextFreeActionIndex_Type(Integer32):
    """Custom type tarNextFreeActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TarNextFreeActionIndex_Type.__name__ = "Integer32"
_TarNextFreeActionIndex_Object = MibScalar
tarNextFreeActionIndex = _TarNextFreeActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 1, 2),
    _TarNextFreeActionIndex_Type()
)
tarNextFreeActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarNextFreeActionIndex.setStatus("current")


class _TarNextFreeRuleIndex_Type(Integer32):
    """Custom type tarNextFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_TarNextFreeRuleIndex_Type.__name__ = "Integer32"
_TarNextFreeRuleIndex_Object = MibScalar
tarNextFreeRuleIndex = _TarNextFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 1, 3),
    _TarNextFreeRuleIndex_Type()
)
tarNextFreeRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarNextFreeRuleIndex.setStatus("current")
_IrTarTable_ObjectIdentity = ObjectIdentity
irTarTable = _IrTarTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2)
)
_TarTrigTable_Object = MibTable
tarTrigTable = _TarTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    tarTrigTable.setStatus("current")
_TarTrigEntry_Object = MibTableRow
tarTrigEntry = _TarTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1)
)
tarTrigEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "tarTrigIndex"),
)
if mibBuilder.loadTexts:
    tarTrigEntry.setStatus("current")
_TarTrigIndex_Type = Integer32
_TarTrigIndex_Object = MibTableColumn
tarTrigIndex = _TarTrigIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1, 1),
    _TarTrigIndex_Type()
)
tarTrigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarTrigIndex.setStatus("current")


class _TarTrigName_Type(DisplayString):
    """Custom type tarTrigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TarTrigName_Type.__name__ = "DisplayString"
_TarTrigName_Object = MibTableColumn
tarTrigName = _TarTrigName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1, 2),
    _TarTrigName_Type()
)
tarTrigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTrigName.setStatus("current")
_TarTrigType_Type = TarTrigType
_TarTrigType_Object = MibTableColumn
tarTrigType = _TarTrigType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1, 3),
    _TarTrigType_Type()
)
tarTrigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTrigType.setStatus("current")
_TarTrigCreator_Type = TarCreator
_TarTrigCreator_Object = MibTableColumn
tarTrigCreator = _TarTrigCreator_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1, 4),
    _TarTrigCreator_Type()
)
tarTrigCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarTrigCreator.setStatus("current")
_TarTrigRowStatus_Type = RowStatus
_TarTrigRowStatus_Object = MibTableColumn
tarTrigRowStatus = _TarTrigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 1, 1, 5),
    _TarTrigRowStatus_Type()
)
tarTrigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTrigRowStatus.setStatus("current")
_TarActionTable_Object = MibTable
tarActionTable = _TarActionTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    tarActionTable.setStatus("current")
_TarActionEntry_Object = MibTableRow
tarActionEntry = _TarActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1)
)
tarActionEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "tarActionIndex"),
)
if mibBuilder.loadTexts:
    tarActionEntry.setStatus("current")
_TarActionIndex_Type = Integer32
_TarActionIndex_Object = MibTableColumn
tarActionIndex = _TarActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1, 1),
    _TarActionIndex_Type()
)
tarActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarActionIndex.setStatus("current")


class _TarActionName_Type(DisplayString):
    """Custom type tarActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_TarActionName_Type.__name__ = "DisplayString"
_TarActionName_Object = MibTableColumn
tarActionName = _TarActionName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1, 2),
    _TarActionName_Type()
)
tarActionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarActionName.setStatus("current")


class _TarActionCommand_Type(DisplayString):
    """Custom type tarActionCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 135),
    )


_TarActionCommand_Type.__name__ = "DisplayString"
_TarActionCommand_Object = MibTableColumn
tarActionCommand = _TarActionCommand_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1, 3),
    _TarActionCommand_Type()
)
tarActionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarActionCommand.setStatus("current")
_TarActionCreator_Type = TarCreator
_TarActionCreator_Object = MibTableColumn
tarActionCreator = _TarActionCreator_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1, 4),
    _TarActionCreator_Type()
)
tarActionCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarActionCreator.setStatus("current")
_TarActionRowStatus_Type = RowStatus
_TarActionRowStatus_Object = MibTableColumn
tarActionRowStatus = _TarActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 2, 1, 5),
    _TarActionRowStatus_Type()
)
tarActionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarActionRowStatus.setStatus("current")
_TarRuleTable_Object = MibTable
tarRuleTable = _TarRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    tarRuleTable.setStatus("current")
_TarRuleEntry_Object = MibTableRow
tarRuleEntry = _TarRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1)
)
tarRuleEntry.setIndexNames(
    (0, "MRV-IR-SYSTEM-MIB", "tarRuleIndex"),
)
if mibBuilder.loadTexts:
    tarRuleEntry.setStatus("current")
_TarRuleIndex_Type = Integer32
_TarRuleIndex_Object = MibTableColumn
tarRuleIndex = _TarRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 1),
    _TarRuleIndex_Type()
)
tarRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarRuleIndex.setStatus("current")


class _TarRuleName_Type(DisplayString):
    """Custom type tarRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TarRuleName_Type.__name__ = "DisplayString"
_TarRuleName_Object = MibTableColumn
tarRuleName = _TarRuleName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 2),
    _TarRuleName_Type()
)
tarRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarRuleName.setStatus("current")
_TarRuleTrigId_Type = Integer32
_TarRuleTrigId_Object = MibTableColumn
tarRuleTrigId = _TarRuleTrigId_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 3),
    _TarRuleTrigId_Type()
)
tarRuleTrigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarRuleTrigId.setStatus("current")
_TarRuleActionId_Type = Integer32
_TarRuleActionId_Object = MibTableColumn
tarRuleActionId = _TarRuleActionId_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 4),
    _TarRuleActionId_Type()
)
tarRuleActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarRuleActionId.setStatus("current")


class _TarRuleStatus_Type(Integer32):
    """Custom type tarRuleStatus based on Integer32"""
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


_TarRuleStatus_Type.__name__ = "Integer32"
_TarRuleStatus_Object = MibTableColumn
tarRuleStatus = _TarRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 5),
    _TarRuleStatus_Type()
)
tarRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarRuleStatus.setStatus("current")
_TarRuleExecCount_Type = Counter32
_TarRuleExecCount_Object = MibTableColumn
tarRuleExecCount = _TarRuleExecCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 6),
    _TarRuleExecCount_Type()
)
tarRuleExecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarRuleExecCount.setStatus("current")
_TarRuleErrorCount_Type = Counter32
_TarRuleErrorCount_Object = MibTableColumn
tarRuleErrorCount = _TarRuleErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 7),
    _TarRuleErrorCount_Type()
)
tarRuleErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarRuleErrorCount.setStatus("current")
_TarRuleCreator_Type = TarCreator
_TarRuleCreator_Object = MibTableColumn
tarRuleCreator = _TarRuleCreator_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 8),
    _TarRuleCreator_Type()
)
tarRuleCreator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tarRuleCreator.setStatus("current")
_TarRuleRowStatus_Type = RowStatus
_TarRuleRowStatus_Object = MibTableColumn
tarRuleRowStatus = _TarRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 3, 1, 9),
    _TarRuleRowStatus_Type()
)
tarRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarRuleRowStatus.setStatus("current")
_TarTempTrigTable_Object = MibTable
tarTempTrigTable = _TarTempTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4)
)
if mibBuilder.loadTexts:
    tarTempTrigTable.setStatus("current")
_TarTempTrigEntry_Object = MibTableRow
tarTempTrigEntry = _TarTempTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tarTempTrigEntry.setStatus("current")


class _TarTempTrigPort_Type(Integer32):
    """Custom type tarTempTrigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TarTempTrigPort_Type.__name__ = "Integer32"
_TarTempTrigPort_Object = MibTableColumn
tarTempTrigPort = _TarTempTrigPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1, 1),
    _TarTempTrigPort_Type()
)
tarTempTrigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTempTrigPort.setStatus("current")


class _TarTempTrigOperator_Type(Integer32):
    """Custom type tarTempTrigOperator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greaterThan", 2),
          ("lessThan", 1))
    )


_TarTempTrigOperator_Type.__name__ = "Integer32"
_TarTempTrigOperator_Object = MibTableColumn
tarTempTrigOperator = _TarTempTrigOperator_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1, 2),
    _TarTempTrigOperator_Type()
)
tarTempTrigOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTempTrigOperator.setStatus("current")


class _TarTempTrigThresholdValue_Type(Integer32):
    """Custom type tarTempTrigThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TarTempTrigThresholdValue_Type.__name__ = "Integer32"
_TarTempTrigThresholdValue_Object = MibTableColumn
tarTempTrigThresholdValue = _TarTempTrigThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1, 3),
    _TarTempTrigThresholdValue_Type()
)
tarTempTrigThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTempTrigThresholdValue.setStatus("current")


class _TarTempTrigUnits_Type(Integer32):
    """Custom type tarTempTrigUnits based on Integer32"""
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


_TarTempTrigUnits_Type.__name__ = "Integer32"
_TarTempTrigUnits_Object = MibTableColumn
tarTempTrigUnits = _TarTempTrigUnits_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1, 4),
    _TarTempTrigUnits_Type()
)
tarTempTrigUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTempTrigUnits.setStatus("current")


class _TarTempTrigHysteresis_Type(Integer32):
    """Custom type tarTempTrigHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TarTempTrigHysteresis_Type.__name__ = "Integer32"
_TarTempTrigHysteresis_Object = MibTableColumn
tarTempTrigHysteresis = _TarTempTrigHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 4, 1, 5),
    _TarTempTrigHysteresis_Type()
)
tarTempTrigHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarTempTrigHysteresis.setStatus("current")
_TarSigTrigTable_Object = MibTable
tarSigTrigTable = _TarSigTrigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 6)
)
if mibBuilder.loadTexts:
    tarSigTrigTable.setStatus("current")
_TarSigTrigEntry_Object = MibTableRow
tarSigTrigEntry = _TarSigTrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 6, 1)
)
if mibBuilder.loadTexts:
    tarSigTrigEntry.setStatus("current")


class _TarSigTrigPort_Type(Integer32):
    """Custom type tarSigTrigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_TarSigTrigPort_Type.__name__ = "Integer32"
_TarSigTrigPort_Object = MibTableColumn
tarSigTrigPort = _TarSigTrigPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 6, 1, 1),
    _TarSigTrigPort_Type()
)
tarSigTrigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarSigTrigPort.setStatus("current")


class _TarSigTrigSignal_Type(Integer32):
    """Custom type tarSigTrigSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cts", 1),
          ("dsr", 2))
    )


_TarSigTrigSignal_Type.__name__ = "Integer32"
_TarSigTrigSignal_Object = MibTableColumn
tarSigTrigSignal = _TarSigTrigSignal_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 6, 1, 2),
    _TarSigTrigSignal_Type()
)
tarSigTrigSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarSigTrigSignal.setStatus("current")


class _TarSigTrigState_Type(Integer32):
    """Custom type tarSigTrigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_TarSigTrigState_Type.__name__ = "Integer32"
_TarSigTrigState_Object = MibTableColumn
tarSigTrigState = _TarSigTrigState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 8, 2, 6, 1, 3),
    _TarSigTrigState_Type()
)
tarSigTrigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tarSigTrigState.setStatus("current")
_IrIpmi_ObjectIdentity = ObjectIdentity
irIpmi = _IrIpmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9)
)
_IrIpmiSys_ObjectIdentity = ObjectIdentity
irIpmiSys = _IrIpmiSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1)
)


class _IpmiDiscreteOffset_Type(Integer32):
    """Custom type ipmiDiscreteOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_IpmiDiscreteOffset_Type.__name__ = "Integer32"
_IpmiDiscreteOffset_Object = MibScalar
ipmiDiscreteOffset = _IpmiDiscreteOffset_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 1),
    _IpmiDiscreteOffset_Type()
)
ipmiDiscreteOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiDiscreteOffset.setStatus("current")


class _IpmiDiscreteSensorName_Type(DisplayString):
    """Custom type ipmiDiscreteSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 98),
    )


_IpmiDiscreteSensorName_Type.__name__ = "DisplayString"
_IpmiDiscreteSensorName_Object = MibScalar
ipmiDiscreteSensorName = _IpmiDiscreteSensorName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 2),
    _IpmiDiscreteSensorName_Type()
)
ipmiDiscreteSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiDiscreteSensorName.setStatus("current")


class _IpmiThresholdType_Type(Integer32):
    """Custom type ipmiThresholdType based on Integer32"""
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
        *(("lowerCritical", 2),
          ("lowerNonCritical", 1),
          ("lowerNonRecoverable", 3),
          ("upperCritical", 5),
          ("upperNonCritical", 4),
          ("upperNonRecoverable", 6))
    )


_IpmiThresholdType_Type.__name__ = "Integer32"
_IpmiThresholdType_Object = MibScalar
ipmiThresholdType = _IpmiThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 3),
    _IpmiThresholdType_Type()
)
ipmiThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiThresholdType.setStatus("current")


class _IpmiThresholdSensorName_Type(DisplayString):
    """Custom type ipmiThresholdSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 98),
    )


_IpmiThresholdSensorName_Type.__name__ = "DisplayString"
_IpmiThresholdSensorName_Object = MibScalar
ipmiThresholdSensorName = _IpmiThresholdSensorName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 4),
    _IpmiThresholdSensorName_Type()
)
ipmiThresholdSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiThresholdSensorName.setStatus("current")


class _IpmiThresholdDirection_Type(Integer32):
    """Custom type ipmiThresholdDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goingHigh", 2),
          ("goingLow", 1))
    )


_IpmiThresholdDirection_Type.__name__ = "Integer32"
_IpmiThresholdDirection_Object = MibScalar
ipmiThresholdDirection = _IpmiThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 5),
    _IpmiThresholdDirection_Type()
)
ipmiThresholdDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiThresholdDirection.setStatus("current")


class _IpmiThresholdAssert_Type(Integer32):
    """Custom type ipmiThresholdAssert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assertion", 1),
          ("deassertion", 2))
    )


_IpmiThresholdAssert_Type.__name__ = "Integer32"
_IpmiThresholdAssert_Object = MibScalar
ipmiThresholdAssert = _IpmiThresholdAssert_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 1, 9, 1, 6),
    _IpmiThresholdAssert_Type()
)
ipmiThresholdAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmiThresholdAssert.setStatus("current")
irEnetPortConfigEntry.registerAugmentions(
    ("MRV-IR-SYSTEM-MIB",
     "irEnetPortStatsEntry")
)
irEnetPortStatsEntry.setIndexNames(*irEnetPortConfigEntry.getIndexNames())
tarTrigEntry.registerAugmentions(
    ("MRV-IR-SYSTEM-MIB",
     "tarTempTrigEntry")
)
tarTempTrigEntry.setIndexNames(*tarTrigEntry.getIndexNames())
tarTrigEntry.registerAugmentions(
    ("MRV-IR-SYSTEM-MIB",
     "tarSigTrigEntry")
)
tarSigTrigEntry.setIndexNames(*tarTrigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IR-SYSTEM-MIB",
    **{"TrapSeverity": TrapSeverity,
       "TarCreator": TarCreator,
       "TarTrigType": TarTrigType,
       "mrvBpd": mrvBpd,
       "mrvLx": mrvLx,
       "irSystemMib": irSystemMib,
       "irSysSystem": irSysSystem,
       "irSysImageFilename": irSysImageFilename,
       "irSysImageSource": irSysImageSource,
       "irSysImageServer": irSysImageServer,
       "irSysSwVersion": irSysSwVersion,
       "irSysSwBootVersion": irSysSwBootVersion,
       "irSysIpAddress": irSysIpAddress,
       "irSysSubnetMask": irSysSubnetMask,
       "irSysBcastAddress": irSysBcastAddress,
       "irSysGateway": irSysGateway,
       "irSysAction": irSysAction,
       "irSysSnmpSetErrorString": irSysSnmpSetErrorString,
       "irSysModelType": irSysModelType,
       "irSysPowerType": irSysPowerType,
       "irSysCurrentTemp": irSysCurrentTemp,
       "irSysTempThresholdLow": irSysTempThresholdLow,
       "irSysTempThresholdHigh": irSysTempThresholdHigh,
       "irSysTempHysteresis": irSysTempHysteresis,
       "irSysPowerLostTimestamp": irSysPowerLostTimestamp,
       "irSysFipsMode": irSysFipsMode,
       "irSysFlashMemSize": irSysFlashMemSize,
       "irSysAssetTag": irSysAssetTag,
       "irSysPowerCurrentLoad": irSysPowerCurrentLoad,
       "irDevices": irDevices,
       "irDeviceLx": irDeviceLx,
       "irLx1001": irLx1001,
       "irLx1002": irLx1002,
       "irLx1004": irLx1004,
       "irLx4008": irLx4008,
       "irLx4016": irLx4016,
       "irLx4032": irLx4032,
       "irLx4048": irLx4048,
       "irLxEm316": irLxEm316,
       "irLx8020": irLx8020,
       "irLx8040": irLx8040,
       "irLx4000T": irLx4000T,
       "irLx7304T": irLx7304T,
       "irLx4108T": irLx4108T,
       "irTraps": irTraps,
       "irCluster": irCluster,
       "irClusterGrp": irClusterGrp,
       "irClusterCfgStatus": irClusterCfgStatus,
       "irClusterName": irClusterName,
       "irClusterSyncStatus": irClusterSyncStatus,
       "irClusterAction": irClusterAction,
       "irClusterTable": irClusterTable,
       "irClusterEntry": irClusterEntry,
       "irClusterIpAddr": irClusterIpAddr,
       "irClusterStatus": irClusterStatus,
       "irEthernet": irEthernet,
       "irEnetPortConfigTable": irEnetPortConfigTable,
       "irEnetPortConfigEntry": irEnetPortConfigEntry,
       "irEnetPortIndex": irEnetPortIndex,
       "irEnetPortSpeed": irEnetPortSpeed,
       "irEnetPortDuplexMode": irEnetPortDuplexMode,
       "irEnetPortAutoNegotiation": irEnetPortAutoNegotiation,
       "irEnetPortPhysMedia": irEnetPortPhysMedia,
       "irEnetPortLinkStatus": irEnetPortLinkStatus,
       "irEnetPortBondingStatus": irEnetPortBondingStatus,
       "irEnetPortStatsTable": irEnetPortStatsTable,
       "irEnetPortStatsEntry": irEnetPortStatsEntry,
       "irEnetPortRecvBytes": irEnetPortRecvBytes,
       "irEnetPortRecvPackets": irEnetPortRecvPackets,
       "irEnetPortRecvErrors": irEnetPortRecvErrors,
       "irEnetPortRecvDropped": irEnetPortRecvDropped,
       "irEnetPortRecvOverruns": irEnetPortRecvOverruns,
       "irEnetPortRecvFrameErrors": irEnetPortRecvFrameErrors,
       "irEnetPortRecvMulticast": irEnetPortRecvMulticast,
       "irEnetPortRecvCompressed": irEnetPortRecvCompressed,
       "irEnetPortXmitBytes": irEnetPortXmitBytes,
       "irEnetPortXmitPackets": irEnetPortXmitPackets,
       "irEnetPortXmitErrors": irEnetPortXmitErrors,
       "irEnetPortXmitDropped": irEnetPortXmitDropped,
       "irEnetPortXmitOverruns": irEnetPortXmitOverruns,
       "irEnetPortXmitCollisions": irEnetPortXmitCollisions,
       "irEnetPortXmitCompressed": irEnetPortXmitCompressed,
       "irEnetPortXmitCarrier": irEnetPortXmitCarrier,
       "irPower": irPower,
       "irPowerSupplyTable": irPowerSupplyTable,
       "irPowerSupplyEntry": irPowerSupplyEntry,
       "irPowerIndex": irPowerIndex,
       "irPowerUnitPresent": irPowerUnitPresent,
       "irPowerInputStatus": irPowerInputStatus,
       "irPowerOutputStatus": irPowerOutputStatus,
       "irPowerStatus": irPowerStatus,
       "irPowerInputVoltage": irPowerInputVoltage,
       "irPowerOutputVoltage": irPowerOutputVoltage,
       "irInterfaces": irInterfaces,
       "irIfTable": irIfTable,
       "irIfEntry": irIfEntry,
       "irIfIndex": irIfIndex,
       "irIfIpAddress": irIfIpAddress,
       "irIfIpSubnetMask": irIfIpSubnetMask,
       "irIfIpBcastAddress": irIfIpBcastAddress,
       "irIfMtu": irIfMtu,
       "irIfName": irIfName,
       "irIfBoundTo": irIfBoundTo,
       "irIfTelnetPort": irIfTelnetPort,
       "irIfSshPort": irIfSshPort,
       "irTar": irTar,
       "irTarSys": irTarSys,
       "tarNextFreeTrigIndex": tarNextFreeTrigIndex,
       "tarNextFreeActionIndex": tarNextFreeActionIndex,
       "tarNextFreeRuleIndex": tarNextFreeRuleIndex,
       "irTarTable": irTarTable,
       "tarTrigTable": tarTrigTable,
       "tarTrigEntry": tarTrigEntry,
       "tarTrigIndex": tarTrigIndex,
       "tarTrigName": tarTrigName,
       "tarTrigType": tarTrigType,
       "tarTrigCreator": tarTrigCreator,
       "tarTrigRowStatus": tarTrigRowStatus,
       "tarActionTable": tarActionTable,
       "tarActionEntry": tarActionEntry,
       "tarActionIndex": tarActionIndex,
       "tarActionName": tarActionName,
       "tarActionCommand": tarActionCommand,
       "tarActionCreator": tarActionCreator,
       "tarActionRowStatus": tarActionRowStatus,
       "tarRuleTable": tarRuleTable,
       "tarRuleEntry": tarRuleEntry,
       "tarRuleIndex": tarRuleIndex,
       "tarRuleName": tarRuleName,
       "tarRuleTrigId": tarRuleTrigId,
       "tarRuleActionId": tarRuleActionId,
       "tarRuleStatus": tarRuleStatus,
       "tarRuleExecCount": tarRuleExecCount,
       "tarRuleErrorCount": tarRuleErrorCount,
       "tarRuleCreator": tarRuleCreator,
       "tarRuleRowStatus": tarRuleRowStatus,
       "tarTempTrigTable": tarTempTrigTable,
       "tarTempTrigEntry": tarTempTrigEntry,
       "tarTempTrigPort": tarTempTrigPort,
       "tarTempTrigOperator": tarTempTrigOperator,
       "tarTempTrigThresholdValue": tarTempTrigThresholdValue,
       "tarTempTrigUnits": tarTempTrigUnits,
       "tarTempTrigHysteresis": tarTempTrigHysteresis,
       "tarSigTrigTable": tarSigTrigTable,
       "tarSigTrigEntry": tarSigTrigEntry,
       "tarSigTrigPort": tarSigTrigPort,
       "tarSigTrigSignal": tarSigTrigSignal,
       "tarSigTrigState": tarSigTrigState,
       "irIpmi": irIpmi,
       "irIpmiSys": irIpmiSys,
       "ipmiDiscreteOffset": ipmiDiscreteOffset,
       "ipmiDiscreteSensorName": ipmiDiscreteSensorName,
       "ipmiThresholdType": ipmiThresholdType,
       "ipmiThresholdSensorName": ipmiThresholdSensorName,
       "ipmiThresholdDirection": ipmiThresholdDirection,
       "ipmiThresholdAssert": ipmiThresholdAssert}
)
