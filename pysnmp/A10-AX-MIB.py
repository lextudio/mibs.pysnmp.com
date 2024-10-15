# SNMP MIB module (A10-AX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A10-AX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:07 2024
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

(a10Mgmt,) = mibBuilder.importSymbols(
    "A10-COMMON-MIB",
    "a10Mgmt")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxSystem_ObjectIdentity = ObjectIdentity
axSystem = _AxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1)
)
_AxSysVersion_ObjectIdentity = ObjectIdentity
axSysVersion = _AxSysVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 1)
)


class _AxSysPrimaryVersionOnDisk_Type(OctetString):
    """Custom type axSysPrimaryVersionOnDisk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysPrimaryVersionOnDisk_Type.__name__ = "OctetString"
_AxSysPrimaryVersionOnDisk_Object = MibScalar
axSysPrimaryVersionOnDisk = _AxSysPrimaryVersionOnDisk_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 1, 1),
    _AxSysPrimaryVersionOnDisk_Type()
)
axSysPrimaryVersionOnDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysPrimaryVersionOnDisk.setStatus("current")


class _AxSysSecondaryVersionOnDisk_Type(OctetString):
    """Custom type axSysSecondaryVersionOnDisk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysSecondaryVersionOnDisk_Type.__name__ = "OctetString"
_AxSysSecondaryVersionOnDisk_Object = MibScalar
axSysSecondaryVersionOnDisk = _AxSysSecondaryVersionOnDisk_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 1, 2),
    _AxSysSecondaryVersionOnDisk_Type()
)
axSysSecondaryVersionOnDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysSecondaryVersionOnDisk.setStatus("current")


class _AxSysPrimaryVersionOnCF_Type(OctetString):
    """Custom type axSysPrimaryVersionOnCF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysPrimaryVersionOnCF_Type.__name__ = "OctetString"
_AxSysPrimaryVersionOnCF_Object = MibScalar
axSysPrimaryVersionOnCF = _AxSysPrimaryVersionOnCF_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 1, 3),
    _AxSysPrimaryVersionOnCF_Type()
)
axSysPrimaryVersionOnCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysPrimaryVersionOnCF.setStatus("current")


class _AxSysSecondaryVersionOnCF_Type(OctetString):
    """Custom type axSysSecondaryVersionOnCF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysSecondaryVersionOnCF_Type.__name__ = "OctetString"
_AxSysSecondaryVersionOnCF_Object = MibScalar
axSysSecondaryVersionOnCF = _AxSysSecondaryVersionOnCF_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 1, 4),
    _AxSysSecondaryVersionOnCF_Type()
)
axSysSecondaryVersionOnCF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysSecondaryVersionOnCF.setStatus("current")
_AxSysMemory_ObjectIdentity = ObjectIdentity
axSysMemory = _AxSysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 2)
)
_AxSysMemoryTotal_Type = Integer32
_AxSysMemoryTotal_Object = MibScalar
axSysMemoryTotal = _AxSysMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 2, 1),
    _AxSysMemoryTotal_Type()
)
axSysMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysMemoryTotal.setStatus("current")
_AxSysMemoryUsage_Type = Integer32
_AxSysMemoryUsage_Object = MibScalar
axSysMemoryUsage = _AxSysMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 2, 2),
    _AxSysMemoryUsage_Type()
)
axSysMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysMemoryUsage.setStatus("current")
_AxSysCpu_ObjectIdentity = ObjectIdentity
axSysCpu = _AxSysCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3)
)
_AxSysCpuNumber_Type = Integer32
_AxSysCpuNumber_Object = MibScalar
axSysCpuNumber = _AxSysCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 1),
    _AxSysCpuNumber_Type()
)
axSysCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuNumber.setStatus("current")
_AxSysCpuTable_Object = MibTable
axSysCpuTable = _AxSysCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    axSysCpuTable.setStatus("current")
_AxSysCpuEntry_Object = MibTableRow
axSysCpuEntry = _AxSysCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 2, 1)
)
axSysCpuEntry.setIndexNames(
    (0, "A10-AX-MIB", "axSysCpuIndex"),
)
if mibBuilder.loadTexts:
    axSysCpuEntry.setStatus("current")
_AxSysCpuIndex_Type = Integer32
_AxSysCpuIndex_Object = MibTableColumn
axSysCpuIndex = _AxSysCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 2, 1, 1),
    _AxSysCpuIndex_Type()
)
axSysCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuIndex.setStatus("current")
_AxSysCpuUsage_Type = DisplayString
_AxSysCpuUsage_Object = MibTableColumn
axSysCpuUsage = _AxSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 2, 1, 2),
    _AxSysCpuUsage_Type()
)
axSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuUsage.setStatus("current")
_AxSysCpuUsageValue_Type = Integer32
_AxSysCpuUsageValue_Object = MibTableColumn
axSysCpuUsageValue = _AxSysCpuUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 2, 1, 3),
    _AxSysCpuUsageValue_Type()
)
axSysCpuUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuUsageValue.setStatus("current")
_AxSysAverageCpuUsage_Type = Integer32
_AxSysAverageCpuUsage_Object = MibScalar
axSysAverageCpuUsage = _AxSysAverageCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 3),
    _AxSysAverageCpuUsage_Type()
)
axSysAverageCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysAverageCpuUsage.setStatus("current")
_AxSysAverageControlCpuUsage_Type = Integer32
_AxSysAverageControlCpuUsage_Object = MibScalar
axSysAverageControlCpuUsage = _AxSysAverageControlCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 4),
    _AxSysAverageControlCpuUsage_Type()
)
axSysAverageControlCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysAverageControlCpuUsage.setStatus("current")
_AxSysAverageDataCpuUsage_Type = Integer32
_AxSysAverageDataCpuUsage_Object = MibScalar
axSysAverageDataCpuUsage = _AxSysAverageDataCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 5),
    _AxSysAverageDataCpuUsage_Type()
)
axSysAverageDataCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysAverageDataCpuUsage.setStatus("current")
_AxSysCpuUsageTable_Object = MibTable
axSysCpuUsageTable = _AxSysCpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 6)
)
if mibBuilder.loadTexts:
    axSysCpuUsageTable.setStatus("current")
_AxSysCpuUsageEntry_Object = MibTableRow
axSysCpuUsageEntry = _AxSysCpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 6, 1)
)
axSysCpuUsageEntry.setIndexNames(
    (0, "A10-AX-MIB", "axSysCpuIndexInUsage"),
    (0, "A10-AX-MIB", "axSysCpuUsagePeriodIndex"),
)
if mibBuilder.loadTexts:
    axSysCpuUsageEntry.setStatus("current")
_AxSysCpuIndexInUsage_Type = Integer32
_AxSysCpuIndexInUsage_Object = MibTableColumn
axSysCpuIndexInUsage = _AxSysCpuIndexInUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 6, 1, 1),
    _AxSysCpuIndexInUsage_Type()
)
axSysCpuIndexInUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuIndexInUsage.setStatus("current")


class _AxSysCpuUsagePeriodIndex_Type(Integer32):
    """Custom type axSysCpuUsagePeriodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AxSysCpuUsagePeriodIndex_Type.__name__ = "Integer32"
_AxSysCpuUsagePeriodIndex_Object = MibTableColumn
axSysCpuUsagePeriodIndex = _AxSysCpuUsagePeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 6, 1, 2),
    _AxSysCpuUsagePeriodIndex_Type()
)
axSysCpuUsagePeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuUsagePeriodIndex.setStatus("current")
_AxSysCpuUsageValueAtPeriod_Type = Integer32
_AxSysCpuUsageValueAtPeriod_Object = MibTableColumn
axSysCpuUsageValueAtPeriod = _AxSysCpuUsageValueAtPeriod_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 3, 6, 1, 3),
    _AxSysCpuUsageValueAtPeriod_Type()
)
axSysCpuUsageValueAtPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysCpuUsageValueAtPeriod.setStatus("current")
_AxSysDisk_ObjectIdentity = ObjectIdentity
axSysDisk = _AxSysDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 4)
)
_AxSysDiskTotalSpace_Type = Integer32
_AxSysDiskTotalSpace_Object = MibScalar
axSysDiskTotalSpace = _AxSysDiskTotalSpace_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 4, 1),
    _AxSysDiskTotalSpace_Type()
)
axSysDiskTotalSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysDiskTotalSpace.setStatus("current")
_AxSysDiskFreeSpace_Type = Integer32
_AxSysDiskFreeSpace_Object = MibScalar
axSysDiskFreeSpace = _AxSysDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 4, 2),
    _AxSysDiskFreeSpace_Type()
)
axSysDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysDiskFreeSpace.setStatus("current")
_AxSysHwInfo_ObjectIdentity = ObjectIdentity
axSysHwInfo = _AxSysHwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5)
)
_AxSysHwPhySystemTemp_Type = Integer32
_AxSysHwPhySystemTemp_Object = MibScalar
axSysHwPhySystemTemp = _AxSysHwPhySystemTemp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 1),
    _AxSysHwPhySystemTemp_Type()
)
axSysHwPhySystemTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysHwPhySystemTemp.setStatus("current")
_AxSysHwFan1Speed_Type = Integer32
_AxSysHwFan1Speed_Object = MibScalar
axSysHwFan1Speed = _AxSysHwFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 2),
    _AxSysHwFan1Speed_Type()
)
axSysHwFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysHwFan1Speed.setStatus("current")
_AxSysHwFan2Speed_Type = Integer32
_AxSysHwFan2Speed_Object = MibScalar
axSysHwFan2Speed = _AxSysHwFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 3),
    _AxSysHwFan2Speed_Type()
)
axSysHwFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysHwFan2Speed.setStatus("current")
_AxSysHwFan3Speed_Type = Integer32
_AxSysHwFan3Speed_Object = MibScalar
axSysHwFan3Speed = _AxSysHwFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 4),
    _AxSysHwFan3Speed_Type()
)
axSysHwFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysHwFan3Speed.setStatus("current")


class _AxSysLowerPowerSupplyStatus_Type(Integer32):
    """Custom type axSysLowerPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -1))
    )


_AxSysLowerPowerSupplyStatus_Type.__name__ = "Integer32"
_AxSysLowerPowerSupplyStatus_Object = MibScalar
axSysLowerPowerSupplyStatus = _AxSysLowerPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 7),
    _AxSysLowerPowerSupplyStatus_Type()
)
axSysLowerPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysLowerPowerSupplyStatus.setStatus("current")


class _AxSysUpperPowerSupplyStatus_Type(Integer32):
    """Custom type axSysUpperPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", -1))
    )


_AxSysUpperPowerSupplyStatus_Type.__name__ = "Integer32"
_AxSysUpperPowerSupplyStatus_Object = MibScalar
axSysUpperPowerSupplyStatus = _AxSysUpperPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 8),
    _AxSysUpperPowerSupplyStatus_Type()
)
axSysUpperPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysUpperPowerSupplyStatus.setStatus("current")
_AxSysFanStatusTable_Object = MibTable
axSysFanStatusTable = _AxSysFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 9)
)
if mibBuilder.loadTexts:
    axSysFanStatusTable.setStatus("current")
_AxSysFanStatusEntry_Object = MibTableRow
axSysFanStatusEntry = _AxSysFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 9, 1)
)
axSysFanStatusEntry.setIndexNames(
    (0, "A10-AX-MIB", "axFanIndex"),
)
if mibBuilder.loadTexts:
    axSysFanStatusEntry.setStatus("current")
_AxFanIndex_Type = Integer32
_AxFanIndex_Object = MibTableColumn
axFanIndex = _AxFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 9, 1, 1),
    _AxFanIndex_Type()
)
axFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanIndex.setStatus("current")
_AxFanName_Type = DisplayString
_AxFanName_Object = MibTableColumn
axFanName = _AxFanName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 9, 1, 2),
    _AxFanName_Type()
)
axFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanName.setStatus("current")


class _AxFanStatus_Type(Integer32):
    """Custom type axFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("notReady", -2),
          ("okFixedHigh", 4),
          ("okLowMed", 5),
          ("okMedHigh", 7),
          ("okMedMed", 6),
          ("unknown", -1))
    )


_AxFanStatus_Type.__name__ = "Integer32"
_AxFanStatus_Object = MibTableColumn
axFanStatus = _AxFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 5, 9, 1, 3),
    _AxFanStatus_Type()
)
axFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanStatus.setStatus("current")
_AxSysInfo_ObjectIdentity = ObjectIdentity
axSysInfo = _AxSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 6)
)


class _AxSysStartupMode_Type(Integer32):
    """Custom type axSysStartupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("primaryCF", 3),
          ("primaryDisk", 1),
          ("secondaryCF", 4),
          ("secondaryDisk", 2),
          ("unknown", 0))
    )


_AxSysStartupMode_Type.__name__ = "Integer32"
_AxSysStartupMode_Object = MibScalar
axSysStartupMode = _AxSysStartupMode_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 6, 1),
    _AxSysStartupMode_Type()
)
axSysStartupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysStartupMode.setStatus("current")


class _AxSysSerialNumber_Type(OctetString):
    """Custom type axSysSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysSerialNumber_Type.__name__ = "OctetString"
_AxSysSerialNumber_Object = MibScalar
axSysSerialNumber = _AxSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 6, 2),
    _AxSysSerialNumber_Type()
)
axSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysSerialNumber.setStatus("current")


class _AxSysFirmwareVersion_Type(OctetString):
    """Custom type axSysFirmwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysFirmwareVersion_Type.__name__ = "OctetString"
_AxSysFirmwareVersion_Object = MibScalar
axSysFirmwareVersion = _AxSysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 6, 3),
    _AxSysFirmwareVersion_Type()
)
axSysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysFirmwareVersion.setStatus("current")


class _AxSysAFleXEngineVersion_Type(OctetString):
    """Custom type axSysAFleXEngineVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AxSysAFleXEngineVersion_Type.__name__ = "OctetString"
_AxSysAFleXEngineVersion_Object = MibScalar
axSysAFleXEngineVersion = _AxSysAFleXEngineVersion_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 6, 4),
    _AxSysAFleXEngineVersion_Type()
)
axSysAFleXEngineVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSysAFleXEngineVersion.setStatus("current")
_AxNetwork_ObjectIdentity = ObjectIdentity
axNetwork = _AxNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7)
)
_AxInterfaces_ObjectIdentity = ObjectIdentity
axInterfaces = _AxInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1)
)
_AxInterface_ObjectIdentity = ObjectIdentity
axInterface = _AxInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1)
)
_AxInterfaceCount_Type = Integer32
_AxInterfaceCount_Object = MibScalar
axInterfaceCount = _AxInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 1),
    _AxInterfaceCount_Type()
)
axInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceCount.setStatus("current")
_AxInterfaceTable_Object = MibTable
axInterfaceTable = _AxInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    axInterfaceTable.setStatus("current")
_AxInterfaceEntry_Object = MibTableRow
axInterfaceEntry = _AxInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1)
)
axInterfaceEntry.setIndexNames(
    (0, "A10-AX-MIB", "axInterfaceIndex"),
)
if mibBuilder.loadTexts:
    axInterfaceEntry.setStatus("current")
_AxInterfaceIndex_Type = Integer32
_AxInterfaceIndex_Object = MibTableColumn
axInterfaceIndex = _AxInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 1),
    _AxInterfaceIndex_Type()
)
axInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceIndex.setStatus("current")
_AxInterfaceName_Type = DisplayString
_AxInterfaceName_Object = MibTableColumn
axInterfaceName = _AxInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 2),
    _AxInterfaceName_Type()
)
axInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceName.setStatus("current")
_AxInterfaceMediaMaxSpeed_Type = Integer32
_AxInterfaceMediaMaxSpeed_Object = MibTableColumn
axInterfaceMediaMaxSpeed = _AxInterfaceMediaMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 3),
    _AxInterfaceMediaMaxSpeed_Type()
)
axInterfaceMediaMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMediaMaxSpeed.setStatus("current")


class _AxInterfaceMediaMaxDuplex_Type(Integer32):
    """Custom type axInterfaceMediaMaxDuplex based on Integer32"""
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
        *(("auto", 3),
          ("full", 2),
          ("half", 1),
          ("none", 0))
    )


_AxInterfaceMediaMaxDuplex_Type.__name__ = "Integer32"
_AxInterfaceMediaMaxDuplex_Object = MibTableColumn
axInterfaceMediaMaxDuplex = _AxInterfaceMediaMaxDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 4),
    _AxInterfaceMediaMaxDuplex_Type()
)
axInterfaceMediaMaxDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMediaMaxDuplex.setStatus("current")
_AxInterfaceMediaActiveSpeed_Type = Integer32
_AxInterfaceMediaActiveSpeed_Object = MibTableColumn
axInterfaceMediaActiveSpeed = _AxInterfaceMediaActiveSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 5),
    _AxInterfaceMediaActiveSpeed_Type()
)
axInterfaceMediaActiveSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMediaActiveSpeed.setStatus("current")


class _AxInterfaceMediaActiveDuplex_Type(Integer32):
    """Custom type axInterfaceMediaActiveDuplex based on Integer32"""
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
        *(("auto", 3),
          ("full", 2),
          ("half", 1),
          ("none", 0))
    )


_AxInterfaceMediaActiveDuplex_Type.__name__ = "Integer32"
_AxInterfaceMediaActiveDuplex_Object = MibTableColumn
axInterfaceMediaActiveDuplex = _AxInterfaceMediaActiveDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 6),
    _AxInterfaceMediaActiveDuplex_Type()
)
axInterfaceMediaActiveDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMediaActiveDuplex.setStatus("current")
_AxInterfaceMacAddr_Type = PhysAddress
_AxInterfaceMacAddr_Object = MibTableColumn
axInterfaceMacAddr = _AxInterfaceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 7),
    _AxInterfaceMacAddr_Type()
)
axInterfaceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMacAddr.setStatus("current")
_AxInterfaceMtu_Type = Integer32
_AxInterfaceMtu_Object = MibTableColumn
axInterfaceMtu = _AxInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 8),
    _AxInterfaceMtu_Type()
)
axInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceMtu.setStatus("current")


class _AxInterfaceAdminStatus_Type(Integer32):
    """Custom type axInterfaceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AxInterfaceAdminStatus_Type.__name__ = "Integer32"
_AxInterfaceAdminStatus_Object = MibTableColumn
axInterfaceAdminStatus = _AxInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 9),
    _AxInterfaceAdminStatus_Type()
)
axInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceAdminStatus.setStatus("current")


class _AxInterfaceStatus_Type(Integer32):
    """Custom type axInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("down", 1),
          ("up", 0))
    )


_AxInterfaceStatus_Type.__name__ = "Integer32"
_AxInterfaceStatus_Object = MibTableColumn
axInterfaceStatus = _AxInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 10),
    _AxInterfaceStatus_Type()
)
axInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatus.setStatus("current")
_AxInterfaceAlias_Type = DisplayString
_AxInterfaceAlias_Object = MibTableColumn
axInterfaceAlias = _AxInterfaceAlias_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 11),
    _AxInterfaceAlias_Type()
)
axInterfaceAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceAlias.setStatus("current")


class _AxInterfaceFlowCtrlAdminStatus_Type(Integer32):
    """Custom type axInterfaceFlowCtrlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxInterfaceFlowCtrlAdminStatus_Type.__name__ = "Integer32"
_AxInterfaceFlowCtrlAdminStatus_Object = MibTableColumn
axInterfaceFlowCtrlAdminStatus = _AxInterfaceFlowCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 12),
    _AxInterfaceFlowCtrlAdminStatus_Type()
)
axInterfaceFlowCtrlAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceFlowCtrlAdminStatus.setStatus("current")


class _AxInterfaceFlowCtrlOperStatus_Type(Integer32):
    """Custom type axInterfaceFlowCtrlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AxInterfaceFlowCtrlOperStatus_Type.__name__ = "Integer32"
_AxInterfaceFlowCtrlOperStatus_Object = MibTableColumn
axInterfaceFlowCtrlOperStatus = _AxInterfaceFlowCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 1, 2, 1, 13),
    _AxInterfaceFlowCtrlOperStatus_Type()
)
axInterfaceFlowCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceFlowCtrlOperStatus.setStatus("current")
_AxInterfaceStat_ObjectIdentity = ObjectIdentity
axInterfaceStat = _AxInterfaceStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2)
)
_AxInterfaceStatTable_Object = MibTable
axInterfaceStatTable = _AxInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    axInterfaceStatTable.setStatus("current")
_AxInterfaceStatEntry_Object = MibTableRow
axInterfaceStatEntry = _AxInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1)
)
axInterfaceStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axInterfaceStatIndex"),
)
if mibBuilder.loadTexts:
    axInterfaceStatEntry.setStatus("current")
_AxInterfaceStatIndex_Type = Integer32
_AxInterfaceStatIndex_Object = MibTableColumn
axInterfaceStatIndex = _AxInterfaceStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 1),
    _AxInterfaceStatIndex_Type()
)
axInterfaceStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatIndex.setStatus("current")
_AxInterfaceStatPktsIn_Type = Counter64
_AxInterfaceStatPktsIn_Object = MibTableColumn
axInterfaceStatPktsIn = _AxInterfaceStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 2),
    _AxInterfaceStatPktsIn_Type()
)
axInterfaceStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatPktsIn.setStatus("current")
_AxInterfaceStatBytesIn_Type = Counter64
_AxInterfaceStatBytesIn_Object = MibTableColumn
axInterfaceStatBytesIn = _AxInterfaceStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 3),
    _AxInterfaceStatBytesIn_Type()
)
axInterfaceStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatBytesIn.setStatus("current")
_AxInterfaceStatPktsOut_Type = Counter64
_AxInterfaceStatPktsOut_Object = MibTableColumn
axInterfaceStatPktsOut = _AxInterfaceStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 4),
    _AxInterfaceStatPktsOut_Type()
)
axInterfaceStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatPktsOut.setStatus("current")
_AxInterfaceStatBytesOut_Type = Counter64
_AxInterfaceStatBytesOut_Object = MibTableColumn
axInterfaceStatBytesOut = _AxInterfaceStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 5),
    _AxInterfaceStatBytesOut_Type()
)
axInterfaceStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatBytesOut.setStatus("current")
_AxInterfaceStatMcastIn_Type = Counter64
_AxInterfaceStatMcastIn_Object = MibTableColumn
axInterfaceStatMcastIn = _AxInterfaceStatMcastIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 6),
    _AxInterfaceStatMcastIn_Type()
)
axInterfaceStatMcastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatMcastIn.setStatus("current")
_AxInterfaceStatMcastOut_Type = Counter64
_AxInterfaceStatMcastOut_Object = MibTableColumn
axInterfaceStatMcastOut = _AxInterfaceStatMcastOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 7),
    _AxInterfaceStatMcastOut_Type()
)
axInterfaceStatMcastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatMcastOut.setStatus("current")
_AxInterfaceStatErrorsIn_Type = Counter64
_AxInterfaceStatErrorsIn_Object = MibTableColumn
axInterfaceStatErrorsIn = _AxInterfaceStatErrorsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 8),
    _AxInterfaceStatErrorsIn_Type()
)
axInterfaceStatErrorsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatErrorsIn.setStatus("current")
_AxInterfaceStatErrorsOut_Type = Counter64
_AxInterfaceStatErrorsOut_Object = MibTableColumn
axInterfaceStatErrorsOut = _AxInterfaceStatErrorsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 9),
    _AxInterfaceStatErrorsOut_Type()
)
axInterfaceStatErrorsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatErrorsOut.setStatus("current")
_AxInterfaceStatDropsIn_Type = Counter64
_AxInterfaceStatDropsIn_Object = MibTableColumn
axInterfaceStatDropsIn = _AxInterfaceStatDropsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 10),
    _AxInterfaceStatDropsIn_Type()
)
axInterfaceStatDropsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatDropsIn.setStatus("current")
_AxInterfaceStatDropsOut_Type = Counter64
_AxInterfaceStatDropsOut_Object = MibTableColumn
axInterfaceStatDropsOut = _AxInterfaceStatDropsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 11),
    _AxInterfaceStatDropsOut_Type()
)
axInterfaceStatDropsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatDropsOut.setStatus("current")
_AxInterfaceStatCollisions_Type = Counter64
_AxInterfaceStatCollisions_Object = MibTableColumn
axInterfaceStatCollisions = _AxInterfaceStatCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 1, 2, 1, 1, 12),
    _AxInterfaceStatCollisions_Type()
)
axInterfaceStatCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axInterfaceStatCollisions.setStatus("current")
_AxVlans_ObjectIdentity = ObjectIdentity
axVlans = _AxVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2)
)
_AxVlanCfg_ObjectIdentity = ObjectIdentity
axVlanCfg = _AxVlanCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1)
)
_AxVlanCfgTable_Object = MibTable
axVlanCfgTable = _AxVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    axVlanCfgTable.setStatus("current")
_AxVlanCfgEntry_Object = MibTableRow
axVlanCfgEntry = _AxVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 1, 1)
)
axVlanCfgEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVlanId"),
)
if mibBuilder.loadTexts:
    axVlanCfgEntry.setStatus("current")
_AxVlanId_Type = Integer32
_AxVlanId_Object = MibTableColumn
axVlanId = _AxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 1, 1, 1),
    _AxVlanId_Type()
)
axVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanId.setStatus("current")
_AxVlanName_Type = DisplayString
_AxVlanName_Object = MibTableColumn
axVlanName = _AxVlanName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 1, 1, 2),
    _AxVlanName_Type()
)
axVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanName.setStatus("current")
_AxVlanRouterInterface_Type = Integer32
_AxVlanRouterInterface_Object = MibTableColumn
axVlanRouterInterface = _AxVlanRouterInterface_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 1, 1, 3),
    _AxVlanRouterInterface_Type()
)
axVlanRouterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanRouterInterface.setStatus("current")
_AxVlanCfgMemberTable_Object = MibTable
axVlanCfgMemberTable = _AxVlanCfgMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    axVlanCfgMemberTable.setStatus("current")
_AxVlanCfgMemberEntry_Object = MibTableRow
axVlanCfgMemberEntry = _AxVlanCfgMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 2, 1)
)
axVlanCfgMemberEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVlanMemberVlanId"),
    (0, "A10-AX-MIB", "axVlanMemberIntfId"),
)
if mibBuilder.loadTexts:
    axVlanCfgMemberEntry.setStatus("current")
_AxVlanMemberVlanId_Type = Integer32
_AxVlanMemberVlanId_Object = MibTableColumn
axVlanMemberVlanId = _AxVlanMemberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 2, 1, 1),
    _AxVlanMemberVlanId_Type()
)
axVlanMemberVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanMemberVlanId.setStatus("current")
_AxVlanMemberIntfId_Type = Integer32
_AxVlanMemberIntfId_Object = MibTableColumn
axVlanMemberIntfId = _AxVlanMemberIntfId_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 2, 1, 2),
    _AxVlanMemberIntfId_Type()
)
axVlanMemberIntfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanMemberIntfId.setStatus("current")


class _AxVlanMemberTagged_Type(Integer32):
    """Custom type axVlanMemberTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AxVlanMemberTagged_Type.__name__ = "Integer32"
_AxVlanMemberTagged_Object = MibTableColumn
axVlanMemberTagged = _AxVlanMemberTagged_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 1, 7, 2, 1, 2, 1, 3),
    _AxVlanMemberTagged_Type()
)
axVlanMemberTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVlanMemberTagged.setStatus("current")
_AxLogging_ObjectIdentity = ObjectIdentity
axLogging = _AxLogging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2)
)


class _AxLogBufferSize_Type(Integer32):
    """Custom type axLogBufferSize based on Integer32"""
    defaultValue = 100000


_AxLogBufferSize_Object = MibScalar
axLogBufferSize = _AxLogBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 1),
    _AxLogBufferSize_Type()
)
axLogBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogBufferSize.setStatus("current")


class _AxLogBufferPri_Type(Integer32):
    """Custom type axLogBufferPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notDefined", -1),
          ("notice", 5),
          ("warning", 4))
    )


_AxLogBufferPri_Type.__name__ = "Integer32"
_AxLogBufferPri_Object = MibScalar
axLogBufferPri = _AxLogBufferPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 2),
    _AxLogBufferPri_Type()
)
axLogBufferPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogBufferPri.setStatus("current")


class _AxLogConsolePri_Type(Integer32):
    """Custom type axLogConsolePri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notDefined", -1),
          ("notice", 5),
          ("warning", 4))
    )


_AxLogConsolePri_Type.__name__ = "Integer32"
_AxLogConsolePri_Object = MibScalar
axLogConsolePri = _AxLogConsolePri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 3),
    _AxLogConsolePri_Type()
)
axLogConsolePri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogConsolePri.setStatus("current")


class _AxLogEmailPri_Type(Integer32):
    """Custom type axLogEmailPri based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notDefined", -1),
          ("notice", 5),
          ("warning", 4))
    )


_AxLogEmailPri_Type.__name__ = "Integer32"
_AxLogEmailPri_Object = MibScalar
axLogEmailPri = _AxLogEmailPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 4),
    _AxLogEmailPri_Type()
)
axLogEmailPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogEmailPri.setStatus("current")
_AxLogEmailAddr_Type = DisplayString
_AxLogEmailAddr_Object = MibScalar
axLogEmailAddr = _AxLogEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 5),
    _AxLogEmailAddr_Type()
)
axLogEmailAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogEmailAddr.setStatus("current")


class _AxLogSyslogPri_Type(Integer32):
    """Custom type axLogSyslogPri based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notDefined", -1),
          ("notice", 5),
          ("warning", 4))
    )


_AxLogSyslogPri_Type.__name__ = "Integer32"
_AxLogSyslogPri_Object = MibScalar
axLogSyslogPri = _AxLogSyslogPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 8),
    _AxLogSyslogPri_Type()
)
axLogSyslogPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogSyslogPri.setStatus("current")
_AxLogSyslogHostTable_Object = MibTable
axLogSyslogHostTable = _AxLogSyslogHostTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 9)
)
if mibBuilder.loadTexts:
    axLogSyslogHostTable.setStatus("current")
_AxLogSyslogHostEntry_Object = MibTableRow
axLogSyslogHostEntry = _AxLogSyslogHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 9, 1)
)
axLogSyslogHostEntry.setIndexNames(
    (0, "A10-AX-MIB", "axLogSyslogHostIndex"),
)
if mibBuilder.loadTexts:
    axLogSyslogHostEntry.setStatus("current")
_AxLogSyslogHostIndex_Type = Integer32
_AxLogSyslogHostIndex_Object = MibTableColumn
axLogSyslogHostIndex = _AxLogSyslogHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 9, 1, 1),
    _AxLogSyslogHostIndex_Type()
)
axLogSyslogHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogSyslogHostIndex.setStatus("current")
_AxLogSyslogHost_Type = DisplayString
_AxLogSyslogHost_Object = MibTableColumn
axLogSyslogHost = _AxLogSyslogHost_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 9, 1, 2),
    _AxLogSyslogHost_Type()
)
axLogSyslogHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogSyslogHost.setStatus("current")


class _AxLogSyslogPort_Type(Integer32):
    """Custom type axLogSyslogPort based on Integer32"""
    defaultValue = 514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AxLogSyslogPort_Type.__name__ = "Integer32"
_AxLogSyslogPort_Object = MibScalar
axLogSyslogPort = _AxLogSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 10),
    _AxLogSyslogPort_Type()
)
axLogSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogSyslogPort.setStatus("current")


class _AxLogMonitorPri_Type(Integer32):
    """Custom type axLogMonitorPri based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notDefined", -1),
          ("notice", 5),
          ("warning", 4))
    )


_AxLogMonitorPri_Type.__name__ = "Integer32"
_AxLogMonitorPri_Object = MibScalar
axLogMonitorPri = _AxLogMonitorPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 11),
    _AxLogMonitorPri_Type()
)
axLogMonitorPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLogMonitorPri.setStatus("current")
_AxSyslogTrapPrefix_ObjectIdentity = ObjectIdentity
axSyslogTrapPrefix = _AxSyslogTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 100)
)
if mibBuilder.loadTexts:
    axSyslogTrapPrefix.setStatus("current")
_AxSyslogTrapObjects_ObjectIdentity = ObjectIdentity
axSyslogTrapObjects = _AxSyslogTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101)
)
if mibBuilder.loadTexts:
    axSyslogTrapObjects.setStatus("current")


class _AxSyslogModuleName_Type(DisplayString):
    """Custom type axSyslogModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AxSyslogModuleName_Type.__name__ = "DisplayString"
_AxSyslogModuleName_Object = MibScalar
axSyslogModuleName = _AxSyslogModuleName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 1),
    _AxSyslogModuleName_Type()
)
axSyslogModuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogModuleName.setStatus("current")


class _AxSyslogPriority_Type(Integer32):
    """Custom type axSyslogPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AxSyslogPriority_Type.__name__ = "Integer32"
_AxSyslogPriority_Object = MibScalar
axSyslogPriority = _AxSyslogPriority_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 2),
    _AxSyslogPriority_Type()
)
axSyslogPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogPriority.setStatus("current")


class _AxSyslogMsg_Type(OctetString):
    """Custom type axSyslogMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )


_AxSyslogMsg_Type.__name__ = "OctetString"
_AxSyslogMsg_Object = MibScalar
axSyslogMsg = _AxSyslogMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 101, 3),
    _AxSyslogMsg_Type()
)
axSyslogMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    axSyslogMsg.setStatus("current")
_AxApp_ObjectIdentity = ObjectIdentity
axApp = _AxApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3)
)
_AxAppGlobals_ObjectIdentity = ObjectIdentity
axAppGlobals = _AxAppGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1)
)
_AxAppGlobalSetting_ObjectIdentity = ObjectIdentity
axAppGlobalSetting = _AxAppGlobalSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1)
)
_AxAppGlobalSystemResourceUsageTable_Object = MibTable
axAppGlobalSystemResourceUsageTable = _AxAppGlobalSystemResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axAppGlobalSystemResourceUsageTable.setStatus("current")
_AxAppGlobalSystemResourceUsageEntry_Object = MibTableRow
axAppGlobalSystemResourceUsageEntry = _AxAppGlobalSystemResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1)
)
axAppGlobalSystemResourceUsageEntry.setIndexNames(
    (0, "A10-AX-MIB", "axAppGlobalSystemResourceIndex"),
)
if mibBuilder.loadTexts:
    axAppGlobalSystemResourceUsageEntry.setStatus("current")
_AxAppGlobalSystemResourceIndex_Type = Integer32
_AxAppGlobalSystemResourceIndex_Object = MibTableColumn
axAppGlobalSystemResourceIndex = _AxAppGlobalSystemResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 1),
    _AxAppGlobalSystemResourceIndex_Type()
)
axAppGlobalSystemResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalSystemResourceIndex.setStatus("current")
_AxAppGlobalSystemResourceName_Type = DisplayString
_AxAppGlobalSystemResourceName_Object = MibTableColumn
axAppGlobalSystemResourceName = _AxAppGlobalSystemResourceName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 2),
    _AxAppGlobalSystemResourceName_Type()
)
axAppGlobalSystemResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalSystemResourceName.setStatus("current")
_AxAppGlobalAllowedCurrentValue_Type = Integer32
_AxAppGlobalAllowedCurrentValue_Object = MibTableColumn
axAppGlobalAllowedCurrentValue = _AxAppGlobalAllowedCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 3),
    _AxAppGlobalAllowedCurrentValue_Type()
)
axAppGlobalAllowedCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalAllowedCurrentValue.setStatus("current")
_AxAppGlobalAllowedDefaultValue_Type = Integer32
_AxAppGlobalAllowedDefaultValue_Object = MibTableColumn
axAppGlobalAllowedDefaultValue = _AxAppGlobalAllowedDefaultValue_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 4),
    _AxAppGlobalAllowedDefaultValue_Type()
)
axAppGlobalAllowedDefaultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalAllowedDefaultValue.setStatus("current")
_AxAppGlobalAllowedMinValue_Type = Integer32
_AxAppGlobalAllowedMinValue_Object = MibTableColumn
axAppGlobalAllowedMinValue = _AxAppGlobalAllowedMinValue_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 5),
    _AxAppGlobalAllowedMinValue_Type()
)
axAppGlobalAllowedMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalAllowedMinValue.setStatus("current")
_AxAppGlobalAllowedMaxValue_Type = Integer32
_AxAppGlobalAllowedMaxValue_Object = MibTableColumn
axAppGlobalAllowedMaxValue = _AxAppGlobalAllowedMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 1, 1, 1, 6),
    _AxAppGlobalAllowedMaxValue_Type()
)
axAppGlobalAllowedMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalAllowedMaxValue.setStatus("current")
_AxAppGlobalStats_ObjectIdentity = ObjectIdentity
axAppGlobalStats = _AxAppGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2)
)


class _AxAppGlobalTotalCurrentConnections_Type(Counter64):
    """Custom type axAppGlobalTotalCurrentConnections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalCurrentConnections_Object = MibScalar
axAppGlobalTotalCurrentConnections = _AxAppGlobalTotalCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 1),
    _AxAppGlobalTotalCurrentConnections_Type()
)
axAppGlobalTotalCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalCurrentConnections.setStatus("current")


class _AxAppGlobalTotalNewConnections_Type(Counter64):
    """Custom type axAppGlobalTotalNewConnections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalNewConnections_Object = MibScalar
axAppGlobalTotalNewConnections = _AxAppGlobalTotalNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 2),
    _AxAppGlobalTotalNewConnections_Type()
)
axAppGlobalTotalNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalNewConnections.setStatus("current")


class _AxAppGlobalTotalNewL4Connections_Type(Counter64):
    """Custom type axAppGlobalTotalNewL4Connections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalNewL4Connections_Object = MibScalar
axAppGlobalTotalNewL4Connections = _AxAppGlobalTotalNewL4Connections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 3),
    _AxAppGlobalTotalNewL4Connections_Type()
)
axAppGlobalTotalNewL4Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalNewL4Connections.setStatus("current")


class _AxAppGlobalTotalNewL7Connections_Type(Counter64):
    """Custom type axAppGlobalTotalNewL7Connections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalNewL7Connections_Object = MibScalar
axAppGlobalTotalNewL7Connections = _AxAppGlobalTotalNewL7Connections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 4),
    _AxAppGlobalTotalNewL7Connections_Type()
)
axAppGlobalTotalNewL7Connections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalNewL7Connections.setStatus("current")


class _AxAppGlobalTotalNewIPNatConnections_Type(Counter64):
    """Custom type axAppGlobalTotalNewIPNatConnections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalNewIPNatConnections_Object = MibScalar
axAppGlobalTotalNewIPNatConnections = _AxAppGlobalTotalNewIPNatConnections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 5),
    _AxAppGlobalTotalNewIPNatConnections_Type()
)
axAppGlobalTotalNewIPNatConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalNewIPNatConnections.setStatus("current")


class _AxAppGlobalTotalSSLConnections_Type(Counter64):
    """Custom type axAppGlobalTotalSSLConnections based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalSSLConnections_Object = MibScalar
axAppGlobalTotalSSLConnections = _AxAppGlobalTotalSSLConnections_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 6),
    _AxAppGlobalTotalSSLConnections_Type()
)
axAppGlobalTotalSSLConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalSSLConnections.setStatus("current")


class _AxAppGlobalTotalL7Requests_Type(Counter64):
    """Custom type axAppGlobalTotalL7Requests based on Counter64"""
    defaultValue = 0


_AxAppGlobalTotalL7Requests_Object = MibScalar
axAppGlobalTotalL7Requests = _AxAppGlobalTotalL7Requests_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 7),
    _AxAppGlobalTotalL7Requests_Type()
)
axAppGlobalTotalL7Requests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalTotalL7Requests.setStatus("current")


class _AxGlobalAppPacketDrop_Type(Integer32):
    """Custom type axGlobalAppPacketDrop based on Integer32"""
    defaultValue = 0


_AxGlobalAppPacketDrop_Object = MibScalar
axGlobalAppPacketDrop = _AxGlobalAppPacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 8),
    _AxGlobalAppPacketDrop_Type()
)
axGlobalAppPacketDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axGlobalAppPacketDrop.setStatus("current")


class _AxGlobalTotalAppPacketDrop_Type(Counter64):
    """Custom type axGlobalTotalAppPacketDrop based on Counter64"""
    defaultValue = 0


_AxGlobalTotalAppPacketDrop_Object = MibScalar
axGlobalTotalAppPacketDrop = _AxGlobalTotalAppPacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 9),
    _AxGlobalTotalAppPacketDrop_Type()
)
axGlobalTotalAppPacketDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axGlobalTotalAppPacketDrop.setStatus("current")


class _AxGlobalTotalL4Session_Type(Counter64):
    """Custom type axGlobalTotalL4Session based on Counter64"""
    defaultValue = 0


_AxGlobalTotalL4Session_Object = MibScalar
axGlobalTotalL4Session = _AxGlobalTotalL4Session_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 2, 10),
    _AxGlobalTotalL4Session_Type()
)
axGlobalTotalL4Session.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axGlobalTotalL4Session.setStatus("current")
_AxGlobalAppBuffer_ObjectIdentity = ObjectIdentity
axGlobalAppBuffer = _AxGlobalAppBuffer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 3)
)


class _AxAppGlobalBufferConfigLimit_Type(Integer32):
    """Custom type axAppGlobalBufferConfigLimit based on Integer32"""
    defaultValue = 0


_AxAppGlobalBufferConfigLimit_Object = MibScalar
axAppGlobalBufferConfigLimit = _AxAppGlobalBufferConfigLimit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 3, 1),
    _AxAppGlobalBufferConfigLimit_Type()
)
axAppGlobalBufferConfigLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalBufferConfigLimit.setStatus("current")


class _AxAppGlobalBufferCurrentUsage_Type(Integer32):
    """Custom type axAppGlobalBufferCurrentUsage based on Integer32"""
    defaultValue = 0


_AxAppGlobalBufferCurrentUsage_Object = MibScalar
axAppGlobalBufferCurrentUsage = _AxAppGlobalBufferCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 1, 3, 2),
    _AxAppGlobalBufferCurrentUsage_Type()
)
axAppGlobalBufferCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAppGlobalBufferCurrentUsage.setStatus("current")
_AxServers_ObjectIdentity = ObjectIdentity
axServers = _AxServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2)
)
_AxServer_ObjectIdentity = ObjectIdentity
axServer = _AxServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1)
)
_AxServerCount_Type = Integer32
_AxServerCount_Object = MibScalar
axServerCount = _AxServerCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 1),
    _AxServerCount_Type()
)
axServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerCount.setStatus("current")
_AxServerTable_Object = MibTable
axServerTable = _AxServerTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    axServerTable.setStatus("current")
_AxServerEntry_Object = MibTableRow
axServerEntry = _AxServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1)
)
axServerEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServerName"),
)
if mibBuilder.loadTexts:
    axServerEntry.setStatus("current")
_AxServerName_Type = DisplayString
_AxServerName_Object = MibTableColumn
axServerName = _AxServerName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1, 1),
    _AxServerName_Type()
)
axServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerName.setStatus("current")
_AxServerAddress_Type = DisplayString
_AxServerAddress_Object = MibTableColumn
axServerAddress = _AxServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1, 2),
    _AxServerAddress_Type()
)
axServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerAddress.setStatus("current")


class _AxServerEnabledState_Type(Integer32):
    """Custom type axServerEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxServerEnabledState_Type.__name__ = "Integer32"
_AxServerEnabledState_Object = MibTableColumn
axServerEnabledState = _AxServerEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1, 3),
    _AxServerEnabledState_Type()
)
axServerEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerEnabledState.setStatus("current")
_AxServerHealthMonitor_Type = DisplayString
_AxServerHealthMonitor_Object = MibTableColumn
axServerHealthMonitor = _AxServerHealthMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1, 4),
    _AxServerHealthMonitor_Type()
)
axServerHealthMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerHealthMonitor.setStatus("current")


class _AxServerMonitorState_Type(Integer32):
    """Custom type axServerMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerMonitorState_Type.__name__ = "Integer32"
_AxServerMonitorState_Object = MibTableColumn
axServerMonitorState = _AxServerMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 1, 2, 1, 5),
    _AxServerMonitorState_Type()
)
axServerMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerMonitorState.setStatus("current")
_AxServerStat_ObjectIdentity = ObjectIdentity
axServerStat = _AxServerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2)
)
_AxServerStatCount_Type = Integer32
_AxServerStatCount_Object = MibScalar
axServerStatCount = _AxServerStatCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 1),
    _AxServerStatCount_Type()
)
axServerStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatCount.setStatus("current")
_AxServerStatTable_Object = MibTable
axServerStatTable = _AxServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    axServerStatTable.setStatus("current")
_AxServerStatEntry_Object = MibTableRow
axServerStatEntry = _AxServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1)
)
axServerStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServerStatAddress"),
)
if mibBuilder.loadTexts:
    axServerStatEntry.setStatus("current")
_AxServerStatAddress_Type = DisplayString
_AxServerStatAddress_Object = MibTableColumn
axServerStatAddress = _AxServerStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 1),
    _AxServerStatAddress_Type()
)
axServerStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatAddress.setStatus("current")
_AxServerStatName_Type = DisplayString
_AxServerStatName_Object = MibTableColumn
axServerStatName = _AxServerStatName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 2),
    _AxServerStatName_Type()
)
axServerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatName.setStatus("current")
_AxServerStatServerPktsIn_Type = Counter64
_AxServerStatServerPktsIn_Object = MibTableColumn
axServerStatServerPktsIn = _AxServerStatServerPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 3),
    _AxServerStatServerPktsIn_Type()
)
axServerStatServerPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerPktsIn.setStatus("current")
_AxServerStatServerBytesIn_Type = Counter64
_AxServerStatServerBytesIn_Object = MibTableColumn
axServerStatServerBytesIn = _AxServerStatServerBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 4),
    _AxServerStatServerBytesIn_Type()
)
axServerStatServerBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerBytesIn.setStatus("current")
_AxServerStatServerPktsOut_Type = Counter64
_AxServerStatServerPktsOut_Object = MibTableColumn
axServerStatServerPktsOut = _AxServerStatServerPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 5),
    _AxServerStatServerPktsOut_Type()
)
axServerStatServerPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerPktsOut.setStatus("current")
_AxServerStatServerBytesOut_Type = Counter64
_AxServerStatServerBytesOut_Object = MibTableColumn
axServerStatServerBytesOut = _AxServerStatServerBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 6),
    _AxServerStatServerBytesOut_Type()
)
axServerStatServerBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerBytesOut.setStatus("current")
_AxServerStatServerTotalConns_Type = Counter64
_AxServerStatServerTotalConns_Object = MibTableColumn
axServerStatServerTotalConns = _AxServerStatServerTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 7),
    _AxServerStatServerTotalConns_Type()
)
axServerStatServerTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerTotalConns.setStatus("current")
_AxServerStatServerCurConns_Type = Integer32
_AxServerStatServerCurConns_Object = MibTableColumn
axServerStatServerCurConns = _AxServerStatServerCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 8),
    _AxServerStatServerCurConns_Type()
)
axServerStatServerCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerCurConns.setStatus("current")
_AxServerStatServerPersistConns_Type = Integer32
_AxServerStatServerPersistConns_Object = MibTableColumn
axServerStatServerPersistConns = _AxServerStatServerPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 9),
    _AxServerStatServerPersistConns_Type()
)
axServerStatServerPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerPersistConns.setStatus("deprecated")


class _AxServerStatServerStatus_Type(Integer32):
    """Custom type axServerStatServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerStatServerStatus_Type.__name__ = "Integer32"
_AxServerStatServerStatus_Object = MibTableColumn
axServerStatServerStatus = _AxServerStatServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 10),
    _AxServerStatServerStatus_Type()
)
axServerStatServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerStatus.setStatus("current")
_AxServerStatServerTotalL7Reqs_Type = Counter64
_AxServerStatServerTotalL7Reqs_Object = MibTableColumn
axServerStatServerTotalL7Reqs = _AxServerStatServerTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 11),
    _AxServerStatServerTotalL7Reqs_Type()
)
axServerStatServerTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerTotalL7Reqs.setStatus("current")
_AxServerStatServerTotalCurrL7Reqs_Type = Counter64
_AxServerStatServerTotalCurrL7Reqs_Object = MibTableColumn
axServerStatServerTotalCurrL7Reqs = _AxServerStatServerTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 12),
    _AxServerStatServerTotalCurrL7Reqs_Type()
)
axServerStatServerTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerTotalCurrL7Reqs.setStatus("current")
_AxServerStatServerTotalSuccL7Reqs_Type = Counter64
_AxServerStatServerTotalSuccL7Reqs_Object = MibTableColumn
axServerStatServerTotalSuccL7Reqs = _AxServerStatServerTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 2, 2, 1, 13),
    _AxServerStatServerTotalSuccL7Reqs_Type()
)
axServerStatServerTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatServerTotalSuccL7Reqs.setStatus("current")
_AxServerPort_ObjectIdentity = ObjectIdentity
axServerPort = _AxServerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3)
)
_AxServerPortTable_Object = MibTable
axServerPortTable = _AxServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    axServerPortTable.setStatus("current")
_AxServerPortEntry_Object = MibTableRow
axServerPortEntry = _AxServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1)
)
axServerPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServerNameInPort"),
    (0, "A10-AX-MIB", "axServerPortType"),
    (0, "A10-AX-MIB", "axServerPortNum"),
)
if mibBuilder.loadTexts:
    axServerPortEntry.setStatus("current")
_AxServerNameInPort_Type = DisplayString
_AxServerNameInPort_Object = MibTableColumn
axServerNameInPort = _AxServerNameInPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 1),
    _AxServerNameInPort_Type()
)
axServerNameInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerNameInPort.setStatus("current")


class _AxServerPortType_Type(Integer32):
    """Custom type axServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 3))
    )


_AxServerPortType_Type.__name__ = "Integer32"
_AxServerPortType_Object = MibTableColumn
axServerPortType = _AxServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 2),
    _AxServerPortType_Type()
)
axServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortType.setStatus("current")
_AxServerPortNum_Type = Integer32
_AxServerPortNum_Object = MibTableColumn
axServerPortNum = _AxServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 3),
    _AxServerPortNum_Type()
)
axServerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortNum.setStatus("current")
_AxServerAddressInPort_Type = DisplayString
_AxServerAddressInPort_Object = MibTableColumn
axServerAddressInPort = _AxServerAddressInPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 4),
    _AxServerAddressInPort_Type()
)
axServerAddressInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerAddressInPort.setStatus("current")


class _AxServerPortEnabledState_Type(Integer32):
    """Custom type axServerPortEnabledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxServerPortEnabledState_Type.__name__ = "Integer32"
_AxServerPortEnabledState_Object = MibTableColumn
axServerPortEnabledState = _AxServerPortEnabledState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 5),
    _AxServerPortEnabledState_Type()
)
axServerPortEnabledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortEnabledState.setStatus("current")
_AxServerPortHealthMonitor_Type = DisplayString
_AxServerPortHealthMonitor_Object = MibTableColumn
axServerPortHealthMonitor = _AxServerPortHealthMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 6),
    _AxServerPortHealthMonitor_Type()
)
axServerPortHealthMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortHealthMonitor.setStatus("current")
_AxServerPortConnLimit_Type = Integer32
_AxServerPortConnLimit_Object = MibTableColumn
axServerPortConnLimit = _AxServerPortConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 7),
    _AxServerPortConnLimit_Type()
)
axServerPortConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortConnLimit.setStatus("current")
_AxServerPortWeight_Type = Integer32
_AxServerPortWeight_Object = MibTableColumn
axServerPortWeight = _AxServerPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 8),
    _AxServerPortWeight_Type()
)
axServerPortWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortWeight.setStatus("current")


class _AxServerPortMonitorState_Type(Integer32):
    """Custom type axServerPortMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerPortMonitorState_Type.__name__ = "Integer32"
_AxServerPortMonitorState_Object = MibTableColumn
axServerPortMonitorState = _AxServerPortMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 3, 1, 1, 9),
    _AxServerPortMonitorState_Type()
)
axServerPortMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortMonitorState.setStatus("current")
_AxServerPortStat_ObjectIdentity = ObjectIdentity
axServerPortStat = _AxServerPortStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4)
)
_AxServerPortStatTable_Object = MibTable
axServerPortStatTable = _AxServerPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    axServerPortStatTable.setStatus("current")
_AxServerPortStatEntry_Object = MibTableRow
axServerPortStatEntry = _AxServerPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1)
)
axServerPortStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServerStatAddrInPort"),
    (0, "A10-AX-MIB", "axServerStatPortType"),
    (0, "A10-AX-MIB", "axServerStatPortNum"),
)
if mibBuilder.loadTexts:
    axServerPortStatEntry.setStatus("current")
_AxServerStatAddrInPort_Type = DisplayString
_AxServerStatAddrInPort_Object = MibTableColumn
axServerStatAddrInPort = _AxServerStatAddrInPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 1),
    _AxServerStatAddrInPort_Type()
)
axServerStatAddrInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatAddrInPort.setStatus("current")


class _AxServerStatPortType_Type(Integer32):
    """Custom type axServerStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("udp", 3))
    )


_AxServerStatPortType_Type.__name__ = "Integer32"
_AxServerStatPortType_Object = MibTableColumn
axServerStatPortType = _AxServerStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 2),
    _AxServerStatPortType_Type()
)
axServerStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatPortType.setStatus("current")
_AxServerStatPortNum_Type = Integer32
_AxServerStatPortNum_Object = MibTableColumn
axServerStatPortNum = _AxServerStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 3),
    _AxServerStatPortNum_Type()
)
axServerStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatPortNum.setStatus("current")
_AxServerStatNameInPort_Type = DisplayString
_AxServerStatNameInPort_Object = MibTableColumn
axServerStatNameInPort = _AxServerStatNameInPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 4),
    _AxServerStatNameInPort_Type()
)
axServerStatNameInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerStatNameInPort.setStatus("current")
_AxServerPortStatPktsIn_Type = Counter64
_AxServerPortStatPktsIn_Object = MibTableColumn
axServerPortStatPktsIn = _AxServerPortStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 5),
    _AxServerPortStatPktsIn_Type()
)
axServerPortStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatPktsIn.setStatus("current")
_AxServerPortStatBytesIn_Type = Counter64
_AxServerPortStatBytesIn_Object = MibTableColumn
axServerPortStatBytesIn = _AxServerPortStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 6),
    _AxServerPortStatBytesIn_Type()
)
axServerPortStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatBytesIn.setStatus("current")
_AxServerPortStatPktsOut_Type = Counter64
_AxServerPortStatPktsOut_Object = MibTableColumn
axServerPortStatPktsOut = _AxServerPortStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 7),
    _AxServerPortStatPktsOut_Type()
)
axServerPortStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatPktsOut.setStatus("current")
_AxServerPortStatBytesOut_Type = Counter64
_AxServerPortStatBytesOut_Object = MibTableColumn
axServerPortStatBytesOut = _AxServerPortStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 8),
    _AxServerPortStatBytesOut_Type()
)
axServerPortStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatBytesOut.setStatus("current")
_AxServerPortStatTotalConns_Type = Counter64
_AxServerPortStatTotalConns_Object = MibTableColumn
axServerPortStatTotalConns = _AxServerPortStatTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 9),
    _AxServerPortStatTotalConns_Type()
)
axServerPortStatTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatTotalConns.setStatus("current")
_AxServerPortStatCurConns_Type = Integer32
_AxServerPortStatCurConns_Object = MibTableColumn
axServerPortStatCurConns = _AxServerPortStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 10),
    _AxServerPortStatCurConns_Type()
)
axServerPortStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatCurConns.setStatus("current")
_AxServerPortStatPersistConns_Type = Integer32
_AxServerPortStatPersistConns_Object = MibTableColumn
axServerPortStatPersistConns = _AxServerPortStatPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 11),
    _AxServerPortStatPersistConns_Type()
)
axServerPortStatPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatPersistConns.setStatus("deprecated")


class _AxServerPortStatStatus_Type(Integer32):
    """Custom type axServerPortStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerPortStatStatus_Type.__name__ = "Integer32"
_AxServerPortStatStatus_Object = MibTableColumn
axServerPortStatStatus = _AxServerPortStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 12),
    _AxServerPortStatStatus_Type()
)
axServerPortStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatStatus.setStatus("current")
_AxServerPortStatTotalL7Reqs_Type = Counter64
_AxServerPortStatTotalL7Reqs_Object = MibTableColumn
axServerPortStatTotalL7Reqs = _AxServerPortStatTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 13),
    _AxServerPortStatTotalL7Reqs_Type()
)
axServerPortStatTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatTotalL7Reqs.setStatus("current")
_AxServerPortStatTotalCurrL7Reqs_Type = Counter64
_AxServerPortStatTotalCurrL7Reqs_Object = MibTableColumn
axServerPortStatTotalCurrL7Reqs = _AxServerPortStatTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 14),
    _AxServerPortStatTotalCurrL7Reqs_Type()
)
axServerPortStatTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatTotalCurrL7Reqs.setStatus("current")
_AxServerPortStatTotalSuccL7Reqs_Type = Counter64
_AxServerPortStatTotalSuccL7Reqs_Object = MibTableColumn
axServerPortStatTotalSuccL7Reqs = _AxServerPortStatTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 2, 4, 1, 1, 15),
    _AxServerPortStatTotalSuccL7Reqs_Type()
)
axServerPortStatTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatTotalSuccL7Reqs.setStatus("current")
_AxServiceGroups_ObjectIdentity = ObjectIdentity
axServiceGroups = _AxServiceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3)
)
_AxServiceGroup_ObjectIdentity = ObjectIdentity
axServiceGroup = _AxServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1)
)
_AxServiceGroupCount_Type = Integer32
_AxServiceGroupCount_Object = MibScalar
axServiceGroupCount = _AxServiceGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 1),
    _AxServiceGroupCount_Type()
)
axServiceGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupCount.setStatus("current")
_AxServiceGroupTable_Object = MibTable
axServiceGroupTable = _AxServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    axServiceGroupTable.setStatus("current")
_AxServiceGroupEntry_Object = MibTableRow
axServiceGroupEntry = _AxServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2, 1)
)
axServiceGroupEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServiceGroupName"),
)
if mibBuilder.loadTexts:
    axServiceGroupEntry.setStatus("current")
_AxServiceGroupName_Type = DisplayString
_AxServiceGroupName_Object = MibTableColumn
axServiceGroupName = _AxServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2, 1, 1),
    _AxServiceGroupName_Type()
)
axServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupName.setStatus("current")


class _AxServiceGroupType_Type(Integer32):
    """Custom type axServiceGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_AxServiceGroupType_Type.__name__ = "Integer32"
_AxServiceGroupType_Object = MibTableColumn
axServiceGroupType = _AxServiceGroupType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2, 1, 2),
    _AxServiceGroupType_Type()
)
axServiceGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupType.setStatus("current")


class _AxServiceGroupLbAlgorithm_Type(Integer32):
    """Custom type axServiceGroupLbAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("fastResponseTime", 6),
          ("leastConnection", 2),
          ("leastRequest", 7),
          ("roundRobin", 0),
          ("roundRobinStrict", 8),
          ("serviceLeastConnection", 4),
          ("serviceWeightLeastConnection", 5),
          ("weightLeastConnection", 3),
          ("weightRoundRobin", 1))
    )


_AxServiceGroupLbAlgorithm_Type.__name__ = "Integer32"
_AxServiceGroupLbAlgorithm_Object = MibTableColumn
axServiceGroupLbAlgorithm = _AxServiceGroupLbAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2, 1, 3),
    _AxServiceGroupLbAlgorithm_Type()
)
axServiceGroupLbAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupLbAlgorithm.setStatus("current")


class _AxServiceGroupDisplayStatus_Type(Integer32):
    """Custom type axServiceGroupDisplayStatus based on Integer32"""
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
        *(("allUp", 1),
          ("functionalUp", 2),
          ("partialUp", 3),
          ("stopped", 4))
    )


_AxServiceGroupDisplayStatus_Type.__name__ = "Integer32"
_AxServiceGroupDisplayStatus_Object = MibTableColumn
axServiceGroupDisplayStatus = _AxServiceGroupDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 1, 2, 1, 4),
    _AxServiceGroupDisplayStatus_Type()
)
axServiceGroupDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupDisplayStatus.setStatus("current")
_AxServiceGroupStat_ObjectIdentity = ObjectIdentity
axServiceGroupStat = _AxServiceGroupStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2)
)
_AxServiceGroupStatTable_Object = MibTable
axServiceGroupStatTable = _AxServiceGroupStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    axServiceGroupStatTable.setStatus("current")
_AxServiceGroupStatEntry_Object = MibTableRow
axServiceGroupStatEntry = _AxServiceGroupStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1)
)
axServiceGroupStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServiceGroupStatName"),
)
if mibBuilder.loadTexts:
    axServiceGroupStatEntry.setStatus("current")
_AxServiceGroupStatName_Type = DisplayString
_AxServiceGroupStatName_Object = MibTableColumn
axServiceGroupStatName = _AxServiceGroupStatName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 1),
    _AxServiceGroupStatName_Type()
)
axServiceGroupStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatName.setStatus("current")
_AxServiceGroupStatPktsIn_Type = Counter64
_AxServiceGroupStatPktsIn_Object = MibTableColumn
axServiceGroupStatPktsIn = _AxServiceGroupStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 2),
    _AxServiceGroupStatPktsIn_Type()
)
axServiceGroupStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatPktsIn.setStatus("current")
_AxServiceGroupStatBytesIn_Type = Counter64
_AxServiceGroupStatBytesIn_Object = MibTableColumn
axServiceGroupStatBytesIn = _AxServiceGroupStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 3),
    _AxServiceGroupStatBytesIn_Type()
)
axServiceGroupStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatBytesIn.setStatus("current")
_AxServiceGroupStatPktsOut_Type = Counter64
_AxServiceGroupStatPktsOut_Object = MibTableColumn
axServiceGroupStatPktsOut = _AxServiceGroupStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 4),
    _AxServiceGroupStatPktsOut_Type()
)
axServiceGroupStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatPktsOut.setStatus("current")
_AxServiceGroupStatBytesOut_Type = Counter64
_AxServiceGroupStatBytesOut_Object = MibTableColumn
axServiceGroupStatBytesOut = _AxServiceGroupStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 5),
    _AxServiceGroupStatBytesOut_Type()
)
axServiceGroupStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatBytesOut.setStatus("current")
_AxServiceGroupStatTotConns_Type = Counter64
_AxServiceGroupStatTotConns_Object = MibTableColumn
axServiceGroupStatTotConns = _AxServiceGroupStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 6),
    _AxServiceGroupStatTotConns_Type()
)
axServiceGroupStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatTotConns.setStatus("current")
_AxServiceGroupStatCurConns_Type = Integer32
_AxServiceGroupStatCurConns_Object = MibTableColumn
axServiceGroupStatCurConns = _AxServiceGroupStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 7),
    _AxServiceGroupStatCurConns_Type()
)
axServiceGroupStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatCurConns.setStatus("current")
_AxServiceGroupStatPersistConns_Type = Integer32
_AxServiceGroupStatPersistConns_Object = MibTableColumn
axServiceGroupStatPersistConns = _AxServiceGroupStatPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 8),
    _AxServiceGroupStatPersistConns_Type()
)
axServiceGroupStatPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatPersistConns.setStatus("deprecated")


class _AxServiceGroupStatDisplayStatus_Type(Integer32):
    """Custom type axServiceGroupStatDisplayStatus based on Integer32"""
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
        *(("allUp", 1),
          ("functionalUp", 2),
          ("partialUp", 3),
          ("stopped", 4))
    )


_AxServiceGroupStatDisplayStatus_Type.__name__ = "Integer32"
_AxServiceGroupStatDisplayStatus_Object = MibTableColumn
axServiceGroupStatDisplayStatus = _AxServiceGroupStatDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 9),
    _AxServiceGroupStatDisplayStatus_Type()
)
axServiceGroupStatDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatDisplayStatus.setStatus("current")
_AxServiceGroupStatTotalL7Reqs_Type = Counter64
_AxServiceGroupStatTotalL7Reqs_Object = MibTableColumn
axServiceGroupStatTotalL7Reqs = _AxServiceGroupStatTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 10),
    _AxServiceGroupStatTotalL7Reqs_Type()
)
axServiceGroupStatTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatTotalL7Reqs.setStatus("current")
_AxServiceGroupStatTotalCurrL7Reqs_Type = Counter64
_AxServiceGroupStatTotalCurrL7Reqs_Object = MibTableColumn
axServiceGroupStatTotalCurrL7Reqs = _AxServiceGroupStatTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 11),
    _AxServiceGroupStatTotalCurrL7Reqs_Type()
)
axServiceGroupStatTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatTotalCurrL7Reqs.setStatus("current")
_AxServiceGroupStatTotalSuccL7Reqs_Type = Counter64
_AxServiceGroupStatTotalSuccL7Reqs_Object = MibTableColumn
axServiceGroupStatTotalSuccL7Reqs = _AxServiceGroupStatTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 2, 1, 1, 12),
    _AxServiceGroupStatTotalSuccL7Reqs_Type()
)
axServiceGroupStatTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupStatTotalSuccL7Reqs.setStatus("current")
_AxServiceGroupMember_ObjectIdentity = ObjectIdentity
axServiceGroupMember = _AxServiceGroupMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3)
)
_AxServiceGroupMemberTable_Object = MibTable
axServiceGroupMemberTable = _AxServiceGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    axServiceGroupMemberTable.setStatus("current")
_AxServiceGroupMemberEntry_Object = MibTableRow
axServiceGroupMemberEntry = _AxServiceGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1)
)
axServiceGroupMemberEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServiceGroupNameInMember"),
    (0, "A10-AX-MIB", "axServiceGroupMemberAddrType"),
    (0, "A10-AX-MIB", "axServerNameInServiceGroupMember"),
    (0, "A10-AX-MIB", "axServerPortNumInServiceGroupMember"),
)
if mibBuilder.loadTexts:
    axServiceGroupMemberEntry.setStatus("current")
_AxServiceGroupNameInMember_Type = DisplayString
_AxServiceGroupNameInMember_Object = MibTableColumn
axServiceGroupNameInMember = _AxServiceGroupNameInMember_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 1),
    _AxServiceGroupNameInMember_Type()
)
axServiceGroupNameInMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupNameInMember.setStatus("current")


class _AxServiceGroupMemberAddrType_Type(Integer32):
    """Custom type axServiceGroupMemberAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_AxServiceGroupMemberAddrType_Type.__name__ = "Integer32"
_AxServiceGroupMemberAddrType_Object = MibTableColumn
axServiceGroupMemberAddrType = _AxServiceGroupMemberAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 2),
    _AxServiceGroupMemberAddrType_Type()
)
axServiceGroupMemberAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberAddrType.setStatus("current")
_AxServerNameInServiceGroupMember_Type = DisplayString
_AxServerNameInServiceGroupMember_Object = MibTableColumn
axServerNameInServiceGroupMember = _AxServerNameInServiceGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 3),
    _AxServerNameInServiceGroupMember_Type()
)
axServerNameInServiceGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerNameInServiceGroupMember.setStatus("current")
_AxServerPortNumInServiceGroupMember_Type = Integer32
_AxServerPortNumInServiceGroupMember_Object = MibTableColumn
axServerPortNumInServiceGroupMember = _AxServerPortNumInServiceGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 4),
    _AxServerPortNumInServiceGroupMember_Type()
)
axServerPortNumInServiceGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortNumInServiceGroupMember.setStatus("current")
_AxServerPortPriorityInServiceGroupMember_Type = Integer32
_AxServerPortPriorityInServiceGroupMember_Object = MibTableColumn
axServerPortPriorityInServiceGroupMember = _AxServerPortPriorityInServiceGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 5),
    _AxServerPortPriorityInServiceGroupMember_Type()
)
axServerPortPriorityInServiceGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortPriorityInServiceGroupMember.setStatus("current")


class _AxServerPortStatusInServiceGroupMember_Type(Integer32):
    """Custom type axServerPortStatusInServiceGroupMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerPortStatusInServiceGroupMember_Type.__name__ = "Integer32"
_AxServerPortStatusInServiceGroupMember_Object = MibTableColumn
axServerPortStatusInServiceGroupMember = _AxServerPortStatusInServiceGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 3, 1, 1, 6),
    _AxServerPortStatusInServiceGroupMember_Type()
)
axServerPortStatusInServiceGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatusInServiceGroupMember.setStatus("current")
_AxServiceGroupMemberStat_ObjectIdentity = ObjectIdentity
axServiceGroupMemberStat = _AxServiceGroupMemberStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4)
)
_AxServiceGroupMemberStatTable_Object = MibTable
axServiceGroupMemberStatTable = _AxServiceGroupMemberStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    axServiceGroupMemberStatTable.setStatus("current")
_AxServiceGroupMemberStatEntry_Object = MibTableRow
axServiceGroupMemberStatEntry = _AxServiceGroupMemberStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1)
)
axServiceGroupMemberStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axServiceGroupMemberStatName"),
    (0, "A10-AX-MIB", "axServiceGroupMemberStatAddrType"),
    (0, "A10-AX-MIB", "axServerNameInServiceGroupMemberStat"),
    (0, "A10-AX-MIB", "axServerPortNumInServiceGroupMemberStat"),
)
if mibBuilder.loadTexts:
    axServiceGroupMemberStatEntry.setStatus("current")
_AxServiceGroupMemberStatName_Type = DisplayString
_AxServiceGroupMemberStatName_Object = MibTableColumn
axServiceGroupMemberStatName = _AxServiceGroupMemberStatName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 1),
    _AxServiceGroupMemberStatName_Type()
)
axServiceGroupMemberStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatName.setStatus("current")


class _AxServiceGroupMemberStatAddrType_Type(Integer32):
    """Custom type axServiceGroupMemberStatAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_AxServiceGroupMemberStatAddrType_Type.__name__ = "Integer32"
_AxServiceGroupMemberStatAddrType_Object = MibTableColumn
axServiceGroupMemberStatAddrType = _AxServiceGroupMemberStatAddrType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 2),
    _AxServiceGroupMemberStatAddrType_Type()
)
axServiceGroupMemberStatAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatAddrType.setStatus("current")
_AxServerNameInServiceGroupMemberStat_Type = DisplayString
_AxServerNameInServiceGroupMemberStat_Object = MibTableColumn
axServerNameInServiceGroupMemberStat = _AxServerNameInServiceGroupMemberStat_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 3),
    _AxServerNameInServiceGroupMemberStat_Type()
)
axServerNameInServiceGroupMemberStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerNameInServiceGroupMemberStat.setStatus("current")
_AxServerPortNumInServiceGroupMemberStat_Type = Integer32
_AxServerPortNumInServiceGroupMemberStat_Object = MibTableColumn
axServerPortNumInServiceGroupMemberStat = _AxServerPortNumInServiceGroupMemberStat_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 4),
    _AxServerPortNumInServiceGroupMemberStat_Type()
)
axServerPortNumInServiceGroupMemberStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortNumInServiceGroupMemberStat.setStatus("current")
_AxServiceGroupMemberStatPktsIn_Type = Counter64
_AxServiceGroupMemberStatPktsIn_Object = MibTableColumn
axServiceGroupMemberStatPktsIn = _AxServiceGroupMemberStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 5),
    _AxServiceGroupMemberStatPktsIn_Type()
)
axServiceGroupMemberStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatPktsIn.setStatus("current")
_AxServiceGroupMemberStatBytesIn_Type = Counter64
_AxServiceGroupMemberStatBytesIn_Object = MibTableColumn
axServiceGroupMemberStatBytesIn = _AxServiceGroupMemberStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 6),
    _AxServiceGroupMemberStatBytesIn_Type()
)
axServiceGroupMemberStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatBytesIn.setStatus("current")
_AxServiceGroupMemberStatPktsOut_Type = Counter64
_AxServiceGroupMemberStatPktsOut_Object = MibTableColumn
axServiceGroupMemberStatPktsOut = _AxServiceGroupMemberStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 7),
    _AxServiceGroupMemberStatPktsOut_Type()
)
axServiceGroupMemberStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatPktsOut.setStatus("current")
_AxServiceGroupMemberStatBytesOut_Type = Counter64
_AxServiceGroupMemberStatBytesOut_Object = MibTableColumn
axServiceGroupMemberStatBytesOut = _AxServiceGroupMemberStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 8),
    _AxServiceGroupMemberStatBytesOut_Type()
)
axServiceGroupMemberStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatBytesOut.setStatus("current")
_AxServiceGroupMemberStatPersistConns_Type = Integer32
_AxServiceGroupMemberStatPersistConns_Object = MibTableColumn
axServiceGroupMemberStatPersistConns = _AxServiceGroupMemberStatPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 9),
    _AxServiceGroupMemberStatPersistConns_Type()
)
axServiceGroupMemberStatPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatPersistConns.setStatus("deprecated")
_AxServiceGroupMemberStatTotConns_Type = Counter64
_AxServiceGroupMemberStatTotConns_Object = MibTableColumn
axServiceGroupMemberStatTotConns = _AxServiceGroupMemberStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 10),
    _AxServiceGroupMemberStatTotConns_Type()
)
axServiceGroupMemberStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatTotConns.setStatus("current")
_AxServiceGroupMemberStatCurConns_Type = Integer32
_AxServiceGroupMemberStatCurConns_Object = MibTableColumn
axServiceGroupMemberStatCurConns = _AxServiceGroupMemberStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 11),
    _AxServiceGroupMemberStatCurConns_Type()
)
axServiceGroupMemberStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatCurConns.setStatus("current")


class _AxServerPortStatusInServiceGroupMemberStat_Type(Integer32):
    """Custom type axServerPortStatusInServiceGroupMemberStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("down", 2),
          ("up", 1))
    )


_AxServerPortStatusInServiceGroupMemberStat_Type.__name__ = "Integer32"
_AxServerPortStatusInServiceGroupMemberStat_Object = MibTableColumn
axServerPortStatusInServiceGroupMemberStat = _AxServerPortStatusInServiceGroupMemberStat_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 12),
    _AxServerPortStatusInServiceGroupMemberStat_Type()
)
axServerPortStatusInServiceGroupMemberStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServerPortStatusInServiceGroupMemberStat.setStatus("current")
_AxServiceGroupMemberStatTotalL7Reqs_Type = Counter64
_AxServiceGroupMemberStatTotalL7Reqs_Object = MibTableColumn
axServiceGroupMemberStatTotalL7Reqs = _AxServiceGroupMemberStatTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 13),
    _AxServiceGroupMemberStatTotalL7Reqs_Type()
)
axServiceGroupMemberStatTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatTotalL7Reqs.setStatus("current")
_AxServiceGroupMemberStatTotalCurrL7Reqs_Type = Counter64
_AxServiceGroupMemberStatTotalCurrL7Reqs_Object = MibTableColumn
axServiceGroupMemberStatTotalCurrL7Reqs = _AxServiceGroupMemberStatTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 14),
    _AxServiceGroupMemberStatTotalCurrL7Reqs_Type()
)
axServiceGroupMemberStatTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatTotalCurrL7Reqs.setStatus("current")
_AxServiceGroupMemberStatTotalSuccL7Reqs_Type = Counter64
_AxServiceGroupMemberStatTotalSuccL7Reqs_Object = MibTableColumn
axServiceGroupMemberStatTotalSuccL7Reqs = _AxServiceGroupMemberStatTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 15),
    _AxServiceGroupMemberStatTotalSuccL7Reqs_Type()
)
axServiceGroupMemberStatTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatTotalSuccL7Reqs.setStatus("current")
_AxServiceGroupMemberStatResponseTime_Type = Integer32
_AxServiceGroupMemberStatResponseTime_Object = MibTableColumn
axServiceGroupMemberStatResponseTime = _AxServiceGroupMemberStatResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 3, 4, 1, 1, 16),
    _AxServiceGroupMemberStatResponseTime_Type()
)
axServiceGroupMemberStatResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axServiceGroupMemberStatResponseTime.setStatus("current")
_AxVirtualServers_ObjectIdentity = ObjectIdentity
axVirtualServers = _AxVirtualServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4)
)
_AxVirtualServer_ObjectIdentity = ObjectIdentity
axVirtualServer = _AxVirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1)
)
_AxVirtualServerCount_Type = Integer32
_AxVirtualServerCount_Object = MibScalar
axVirtualServerCount = _AxVirtualServerCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 1),
    _AxVirtualServerCount_Type()
)
axVirtualServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerCount.setStatus("current")
_AxVirtualServerTable_Object = MibTable
axVirtualServerTable = _AxVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    axVirtualServerTable.setStatus("current")
_AxVirtualServerEntry_Object = MibTableRow
axVirtualServerEntry = _AxVirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1)
)
axVirtualServerEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVirtualServerName"),
)
if mibBuilder.loadTexts:
    axVirtualServerEntry.setStatus("current")
_AxVirtualServerName_Type = DisplayString
_AxVirtualServerName_Object = MibTableColumn
axVirtualServerName = _AxVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1, 1),
    _AxVirtualServerName_Type()
)
axVirtualServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerName.setStatus("current")
_AxVirtualServerAddress_Type = DisplayString
_AxVirtualServerAddress_Object = MibTableColumn
axVirtualServerAddress = _AxVirtualServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1, 2),
    _AxVirtualServerAddress_Type()
)
axVirtualServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerAddress.setStatus("current")


class _AxVirtualServerEnabled_Type(Integer32):
    """Custom type axVirtualServerEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxVirtualServerEnabled_Type.__name__ = "Integer32"
_AxVirtualServerEnabled_Object = MibTableColumn
axVirtualServerEnabled = _AxVirtualServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1, 3),
    _AxVirtualServerEnabled_Type()
)
axVirtualServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerEnabled.setStatus("current")
_AxVirtualServerHAGroup_Type = DisplayString
_AxVirtualServerHAGroup_Object = MibTableColumn
axVirtualServerHAGroup = _AxVirtualServerHAGroup_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1, 4),
    _AxVirtualServerHAGroup_Type()
)
axVirtualServerHAGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerHAGroup.setStatus("current")


class _AxVirtualServerDisplayStatus_Type(Integer32):
    """Custom type axVirtualServerDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUp", 1),
          ("disabled", 0),
          ("functionalUp", 2),
          ("partialUp", 3),
          ("stopped", 4))
    )


_AxVirtualServerDisplayStatus_Type.__name__ = "Integer32"
_AxVirtualServerDisplayStatus_Object = MibTableColumn
axVirtualServerDisplayStatus = _AxVirtualServerDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 1, 2, 1, 5),
    _AxVirtualServerDisplayStatus_Type()
)
axVirtualServerDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerDisplayStatus.setStatus("current")
_AxVirtualServerStat_ObjectIdentity = ObjectIdentity
axVirtualServerStat = _AxVirtualServerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2)
)
_AxVirtualServerStatTable_Object = MibTable
axVirtualServerStatTable = _AxVirtualServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    axVirtualServerStatTable.setStatus("current")
_AxVirtualServerStatEntry_Object = MibTableRow
axVirtualServerStatEntry = _AxVirtualServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1)
)
axVirtualServerStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVirtualServerStatAddress"),
)
if mibBuilder.loadTexts:
    axVirtualServerStatEntry.setStatus("current")
_AxVirtualServerStatAddress_Type = DisplayString
_AxVirtualServerStatAddress_Object = MibTableColumn
axVirtualServerStatAddress = _AxVirtualServerStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 1),
    _AxVirtualServerStatAddress_Type()
)
axVirtualServerStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatAddress.setStatus("current")
_AxVirtualServerStatName_Type = DisplayString
_AxVirtualServerStatName_Object = MibTableColumn
axVirtualServerStatName = _AxVirtualServerStatName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 2),
    _AxVirtualServerStatName_Type()
)
axVirtualServerStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatName.setStatus("current")
_AxVirtualServerStatPktsIn_Type = Counter64
_AxVirtualServerStatPktsIn_Object = MibTableColumn
axVirtualServerStatPktsIn = _AxVirtualServerStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 3),
    _AxVirtualServerStatPktsIn_Type()
)
axVirtualServerStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPktsIn.setStatus("current")
_AxVirtualServerStatBytesIn_Type = Counter64
_AxVirtualServerStatBytesIn_Object = MibTableColumn
axVirtualServerStatBytesIn = _AxVirtualServerStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 4),
    _AxVirtualServerStatBytesIn_Type()
)
axVirtualServerStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatBytesIn.setStatus("current")
_AxVirtualServerStatPktsOut_Type = Counter64
_AxVirtualServerStatPktsOut_Object = MibTableColumn
axVirtualServerStatPktsOut = _AxVirtualServerStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 5),
    _AxVirtualServerStatPktsOut_Type()
)
axVirtualServerStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPktsOut.setStatus("current")
_AxVirtualServerStatBytesOut_Type = Counter64
_AxVirtualServerStatBytesOut_Object = MibTableColumn
axVirtualServerStatBytesOut = _AxVirtualServerStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 6),
    _AxVirtualServerStatBytesOut_Type()
)
axVirtualServerStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatBytesOut.setStatus("current")
_AxVirtualServerStatPersistConns_Type = Integer32
_AxVirtualServerStatPersistConns_Object = MibTableColumn
axVirtualServerStatPersistConns = _AxVirtualServerStatPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 7),
    _AxVirtualServerStatPersistConns_Type()
)
axVirtualServerStatPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPersistConns.setStatus("deprecated")
_AxVirtualServerStatTotConns_Type = Counter64
_AxVirtualServerStatTotConns_Object = MibTableColumn
axVirtualServerStatTotConns = _AxVirtualServerStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 8),
    _AxVirtualServerStatTotConns_Type()
)
axVirtualServerStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatTotConns.setStatus("current")
_AxVirtualServerStatCurConns_Type = Integer32
_AxVirtualServerStatCurConns_Object = MibTableColumn
axVirtualServerStatCurConns = _AxVirtualServerStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 9),
    _AxVirtualServerStatCurConns_Type()
)
axVirtualServerStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatCurConns.setStatus("current")


class _AxVirtualServerStatStatus_Type(Integer32):
    """Custom type axVirtualServerStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_AxVirtualServerStatStatus_Type.__name__ = "Integer32"
_AxVirtualServerStatStatus_Object = MibTableColumn
axVirtualServerStatStatus = _AxVirtualServerStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 10),
    _AxVirtualServerStatStatus_Type()
)
axVirtualServerStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatStatus.setStatus("current")


class _AxVirtualServerStatDisplayStatus_Type(Integer32):
    """Custom type axVirtualServerStatDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUp", 1),
          ("disabled", 0),
          ("functionalUp", 2),
          ("partialUp", 3),
          ("stopped", 4))
    )


_AxVirtualServerStatDisplayStatus_Type.__name__ = "Integer32"
_AxVirtualServerStatDisplayStatus_Object = MibTableColumn
axVirtualServerStatDisplayStatus = _AxVirtualServerStatDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 11),
    _AxVirtualServerStatDisplayStatus_Type()
)
axVirtualServerStatDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatDisplayStatus.setStatus("current")
_AxVirtualServerStatTotalL7Reqs_Type = Counter64
_AxVirtualServerStatTotalL7Reqs_Object = MibTableColumn
axVirtualServerStatTotalL7Reqs = _AxVirtualServerStatTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 12),
    _AxVirtualServerStatTotalL7Reqs_Type()
)
axVirtualServerStatTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatTotalL7Reqs.setStatus("current")
_AxVirtualServerStatTotalCurrL7Reqs_Type = Counter64
_AxVirtualServerStatTotalCurrL7Reqs_Object = MibTableColumn
axVirtualServerStatTotalCurrL7Reqs = _AxVirtualServerStatTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 13),
    _AxVirtualServerStatTotalCurrL7Reqs_Type()
)
axVirtualServerStatTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatTotalCurrL7Reqs.setStatus("current")
_AxVirtualServerStatTotalSuccL7Reqs_Type = Counter64
_AxVirtualServerStatTotalSuccL7Reqs_Object = MibTableColumn
axVirtualServerStatTotalSuccL7Reqs = _AxVirtualServerStatTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 2, 1, 1, 14),
    _AxVirtualServerStatTotalSuccL7Reqs_Type()
)
axVirtualServerStatTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatTotalSuccL7Reqs.setStatus("current")
_AxVirtualServerPort_ObjectIdentity = ObjectIdentity
axVirtualServerPort = _AxVirtualServerPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3)
)
_AxVirtualServerPortTable_Object = MibTable
axVirtualServerPortTable = _AxVirtualServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    axVirtualServerPortTable.setStatus("current")
_AxVirtualServerPortEntry_Object = MibTableRow
axVirtualServerPortEntry = _AxVirtualServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1)
)
axVirtualServerPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVirtualServerPortName"),
    (0, "A10-AX-MIB", "axVirtualServerPortType"),
    (0, "A10-AX-MIB", "axVirtualServerPortNum"),
)
if mibBuilder.loadTexts:
    axVirtualServerPortEntry.setStatus("current")
_AxVirtualServerPortName_Type = DisplayString
_AxVirtualServerPortName_Object = MibTableColumn
axVirtualServerPortName = _AxVirtualServerPortName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 1),
    _AxVirtualServerPortName_Type()
)
axVirtualServerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortName.setStatus("current")


class _AxVirtualServerPortType_Type(Integer32):
    """Custom type axVirtualServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fastHTTP", 12),
          ("firewall", 1),
          ("ftp", 9),
          ("http", 14),
          ("https", 15),
          ("mms", 10),
          ("others", 5),
          ("rtsp", 8),
          ("sip", 11),
          ("sip-TCP", 18),
          ("sips", 19),
          ("smtp", 17),
          ("sslProxy", 16),
          ("tcp", 2),
          ("udp", 3))
    )


_AxVirtualServerPortType_Type.__name__ = "Integer32"
_AxVirtualServerPortType_Object = MibTableColumn
axVirtualServerPortType = _AxVirtualServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 2),
    _AxVirtualServerPortType_Type()
)
axVirtualServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortType.setStatus("current")
_AxVirtualServerPortNum_Type = Integer32
_AxVirtualServerPortNum_Object = MibTableColumn
axVirtualServerPortNum = _AxVirtualServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 3),
    _AxVirtualServerPortNum_Type()
)
axVirtualServerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortNum.setStatus("current")
_AxVirtualServerPortAddress_Type = DisplayString
_AxVirtualServerPortAddress_Object = MibTableColumn
axVirtualServerPortAddress = _AxVirtualServerPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 4),
    _AxVirtualServerPortAddress_Type()
)
axVirtualServerPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortAddress.setStatus("current")


class _AxVirtualServerPortEnabled_Type(Integer32):
    """Custom type axVirtualServerPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxVirtualServerPortEnabled_Type.__name__ = "Integer32"
_AxVirtualServerPortEnabled_Object = MibTableColumn
axVirtualServerPortEnabled = _AxVirtualServerPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 5),
    _AxVirtualServerPortEnabled_Type()
)
axVirtualServerPortEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortEnabled.setStatus("current")
_AxVirtualServerPortServiceGroup_Type = DisplayString
_AxVirtualServerPortServiceGroup_Object = MibTableColumn
axVirtualServerPortServiceGroup = _AxVirtualServerPortServiceGroup_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 6),
    _AxVirtualServerPortServiceGroup_Type()
)
axVirtualServerPortServiceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortServiceGroup.setStatus("current")
_AxVirtualServerPortHaGroupID_Type = Integer32
_AxVirtualServerPortHaGroupID_Object = MibTableColumn
axVirtualServerPortHaGroupID = _AxVirtualServerPortHaGroupID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 7),
    _AxVirtualServerPortHaGroupID_Type()
)
axVirtualServerPortHaGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortHaGroupID.setStatus("current")


class _AxVirtualServerPortPersistTemplateType_Type(Integer32):
    """Custom type axVirtualServerPortPersistTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cookiePersist", 1),
          ("destinationIPPersist", 3),
          ("sourcIPPersist", 2),
          ("sslIDPersist", 4),
          ("unknown", 0))
    )


_AxVirtualServerPortPersistTemplateType_Type.__name__ = "Integer32"
_AxVirtualServerPortPersistTemplateType_Object = MibTableColumn
axVirtualServerPortPersistTemplateType = _AxVirtualServerPortPersistTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 8),
    _AxVirtualServerPortPersistTemplateType_Type()
)
axVirtualServerPortPersistTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortPersistTemplateType.setStatus("current")
_AxVirtualServerPortPersistTempl_Type = DisplayString
_AxVirtualServerPortPersistTempl_Object = MibTableColumn
axVirtualServerPortPersistTempl = _AxVirtualServerPortPersistTempl_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 9),
    _AxVirtualServerPortPersistTempl_Type()
)
axVirtualServerPortPersistTempl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortPersistTempl.setStatus("current")
_AxVirtualServerPortTemplate_Type = DisplayString
_AxVirtualServerPortTemplate_Object = MibTableColumn
axVirtualServerPortTemplate = _AxVirtualServerPortTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 10),
    _AxVirtualServerPortTemplate_Type()
)
axVirtualServerPortTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortTemplate.setStatus("current")
_AxVirtualServerPortPolicyTemplate_Type = DisplayString
_AxVirtualServerPortPolicyTemplate_Object = MibTableColumn
axVirtualServerPortPolicyTemplate = _AxVirtualServerPortPolicyTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 11),
    _AxVirtualServerPortPolicyTemplate_Type()
)
axVirtualServerPortPolicyTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortPolicyTemplate.setStatus("current")
_AxVirtualServerPortTCPTemplate_Type = DisplayString
_AxVirtualServerPortTCPTemplate_Object = MibTableColumn
axVirtualServerPortTCPTemplate = _AxVirtualServerPortTCPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 12),
    _AxVirtualServerPortTCPTemplate_Type()
)
axVirtualServerPortTCPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortTCPTemplate.setStatus("current")
_AxVirtualServerPortHTTPTemplate_Type = DisplayString
_AxVirtualServerPortHTTPTemplate_Object = MibTableColumn
axVirtualServerPortHTTPTemplate = _AxVirtualServerPortHTTPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 13),
    _AxVirtualServerPortHTTPTemplate_Type()
)
axVirtualServerPortHTTPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortHTTPTemplate.setStatus("current")
_AxVirtualServerPortRamCacheTemplate_Type = DisplayString
_AxVirtualServerPortRamCacheTemplate_Object = MibTableColumn
axVirtualServerPortRamCacheTemplate = _AxVirtualServerPortRamCacheTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 14),
    _AxVirtualServerPortRamCacheTemplate_Type()
)
axVirtualServerPortRamCacheTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortRamCacheTemplate.setStatus("current")
_AxVirtualServerPortConnReuseTemplate_Type = DisplayString
_AxVirtualServerPortConnReuseTemplate_Object = MibTableColumn
axVirtualServerPortConnReuseTemplate = _AxVirtualServerPortConnReuseTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 15),
    _AxVirtualServerPortConnReuseTemplate_Type()
)
axVirtualServerPortConnReuseTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortConnReuseTemplate.setStatus("current")
_AxVirtualServerPortTCPProxyTemplate_Type = DisplayString
_AxVirtualServerPortTCPProxyTemplate_Object = MibTableColumn
axVirtualServerPortTCPProxyTemplate = _AxVirtualServerPortTCPProxyTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 16),
    _AxVirtualServerPortTCPProxyTemplate_Type()
)
axVirtualServerPortTCPProxyTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortTCPProxyTemplate.setStatus("current")
_AxVirtualServerPortClientSSLTemplate_Type = DisplayString
_AxVirtualServerPortClientSSLTemplate_Object = MibTableColumn
axVirtualServerPortClientSSLTemplate = _AxVirtualServerPortClientSSLTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 17),
    _AxVirtualServerPortClientSSLTemplate_Type()
)
axVirtualServerPortClientSSLTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortClientSSLTemplate.setStatus("current")
_AxVirtualServerPortServerSSLTemplate_Type = DisplayString
_AxVirtualServerPortServerSSLTemplate_Object = MibTableColumn
axVirtualServerPortServerSSLTemplate = _AxVirtualServerPortServerSSLTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 18),
    _AxVirtualServerPortServerSSLTemplate_Type()
)
axVirtualServerPortServerSSLTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortServerSSLTemplate.setStatus("current")
_AxVirtualServerPortRTSPTemplate_Type = DisplayString
_AxVirtualServerPortRTSPTemplate_Object = MibTableColumn
axVirtualServerPortRTSPTemplate = _AxVirtualServerPortRTSPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 19),
    _AxVirtualServerPortRTSPTemplate_Type()
)
axVirtualServerPortRTSPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortRTSPTemplate.setStatus("current")
_AxVirtualServerPortSMTPTemplate_Type = DisplayString
_AxVirtualServerPortSMTPTemplate_Object = MibTableColumn
axVirtualServerPortSMTPTemplate = _AxVirtualServerPortSMTPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 20),
    _AxVirtualServerPortSMTPTemplate_Type()
)
axVirtualServerPortSMTPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortSMTPTemplate.setStatus("current")
_AxVirtualServerPortSIPTemplate_Type = DisplayString
_AxVirtualServerPortSIPTemplate_Object = MibTableColumn
axVirtualServerPortSIPTemplate = _AxVirtualServerPortSIPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 21),
    _AxVirtualServerPortSIPTemplate_Type()
)
axVirtualServerPortSIPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortSIPTemplate.setStatus("current")
_AxVirtualServerPortUDPTemplate_Type = DisplayString
_AxVirtualServerPortUDPTemplate_Object = MibTableColumn
axVirtualServerPortUDPTemplate = _AxVirtualServerPortUDPTemplate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 22),
    _AxVirtualServerPortUDPTemplate_Type()
)
axVirtualServerPortUDPTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortUDPTemplate.setStatus("current")


class _AxVirtualServerPortDisplayStatus_Type(Integer32):
    """Custom type axVirtualServerPortDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUp", 1),
          ("disabled", 0),
          ("functionalUp", 2),
          ("stopped", 4))
    )


_AxVirtualServerPortDisplayStatus_Type.__name__ = "Integer32"
_AxVirtualServerPortDisplayStatus_Object = MibTableColumn
axVirtualServerPortDisplayStatus = _AxVirtualServerPortDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 3, 1, 1, 23),
    _AxVirtualServerPortDisplayStatus_Type()
)
axVirtualServerPortDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortDisplayStatus.setStatus("current")
_AxVirtualServerPortStat_ObjectIdentity = ObjectIdentity
axVirtualServerPortStat = _AxVirtualServerPortStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4)
)
_AxVirtualServerPortStatTable_Object = MibTable
axVirtualServerPortStatTable = _AxVirtualServerPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    axVirtualServerPortStatTable.setStatus("current")
_AxVirtualServerPortStatEntry_Object = MibTableRow
axVirtualServerPortStatEntry = _AxVirtualServerPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1)
)
axVirtualServerPortStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axVirtualServerPortStatAddress"),
    (0, "A10-AX-MIB", "axVirtualServerStatPortType"),
    (0, "A10-AX-MIB", "axVirtualServerStatPortNum"),
)
if mibBuilder.loadTexts:
    axVirtualServerPortStatEntry.setStatus("current")
_AxVirtualServerPortStatAddress_Type = DisplayString
_AxVirtualServerPortStatAddress_Object = MibTableColumn
axVirtualServerPortStatAddress = _AxVirtualServerPortStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 1),
    _AxVirtualServerPortStatAddress_Type()
)
axVirtualServerPortStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatAddress.setStatus("current")


class _AxVirtualServerStatPortType_Type(Integer32):
    """Custom type axVirtualServerStatPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fastHTTP", 12),
          ("firewall", 1),
          ("ftp", 9),
          ("http", 14),
          ("https", 15),
          ("mms", 10),
          ("others", 5),
          ("rtsp", 8),
          ("sip", 11),
          ("sip-tcp", 18),
          ("sips", 19),
          ("smtp", 17),
          ("sslProxy", 16),
          ("tcp", 2),
          ("udp", 3))
    )


_AxVirtualServerStatPortType_Type.__name__ = "Integer32"
_AxVirtualServerStatPortType_Object = MibTableColumn
axVirtualServerStatPortType = _AxVirtualServerStatPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 2),
    _AxVirtualServerStatPortType_Type()
)
axVirtualServerStatPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPortType.setStatus("current")
_AxVirtualServerStatPortNum_Type = Integer32
_AxVirtualServerStatPortNum_Object = MibTableColumn
axVirtualServerStatPortNum = _AxVirtualServerStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 3),
    _AxVirtualServerStatPortNum_Type()
)
axVirtualServerStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPortNum.setStatus("current")
_AxVirtualServerPortStatName_Type = DisplayString
_AxVirtualServerPortStatName_Object = MibTableColumn
axVirtualServerPortStatName = _AxVirtualServerPortStatName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 4),
    _AxVirtualServerPortStatName_Type()
)
axVirtualServerPortStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatName.setStatus("current")


class _AxVirtualServerStatPortStatus_Type(Integer32):
    """Custom type axVirtualServerStatPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("down", 2),
          ("up", 1))
    )


_AxVirtualServerStatPortStatus_Type.__name__ = "Integer32"
_AxVirtualServerStatPortStatus_Object = MibTableColumn
axVirtualServerStatPortStatus = _AxVirtualServerStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 5),
    _AxVirtualServerStatPortStatus_Type()
)
axVirtualServerStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPortStatus.setStatus("current")
_AxVirtualServerPortStatPktsIn_Type = Counter64
_AxVirtualServerPortStatPktsIn_Object = MibTableColumn
axVirtualServerPortStatPktsIn = _AxVirtualServerPortStatPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 6),
    _AxVirtualServerPortStatPktsIn_Type()
)
axVirtualServerPortStatPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatPktsIn.setStatus("current")
_AxVirtualServerPortStatBytesIn_Type = Counter64
_AxVirtualServerPortStatBytesIn_Object = MibTableColumn
axVirtualServerPortStatBytesIn = _AxVirtualServerPortStatBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 7),
    _AxVirtualServerPortStatBytesIn_Type()
)
axVirtualServerPortStatBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatBytesIn.setStatus("current")
_AxVirtualServerPortStatPktsOut_Type = Counter64
_AxVirtualServerPortStatPktsOut_Object = MibTableColumn
axVirtualServerPortStatPktsOut = _AxVirtualServerPortStatPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 8),
    _AxVirtualServerPortStatPktsOut_Type()
)
axVirtualServerPortStatPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatPktsOut.setStatus("current")
_AxVirtualServerPortStatBytesOut_Type = Counter64
_AxVirtualServerPortStatBytesOut_Object = MibTableColumn
axVirtualServerPortStatBytesOut = _AxVirtualServerPortStatBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 9),
    _AxVirtualServerPortStatBytesOut_Type()
)
axVirtualServerPortStatBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatBytesOut.setStatus("current")
_AxVirtualServerPortStatPersistConns_Type = Integer32
_AxVirtualServerPortStatPersistConns_Object = MibTableColumn
axVirtualServerPortStatPersistConns = _AxVirtualServerPortStatPersistConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 10),
    _AxVirtualServerPortStatPersistConns_Type()
)
axVirtualServerPortStatPersistConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatPersistConns.setStatus("deprecated")
_AxVirtualServerPortStatTotConns_Type = Counter64
_AxVirtualServerPortStatTotConns_Object = MibTableColumn
axVirtualServerPortStatTotConns = _AxVirtualServerPortStatTotConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 11),
    _AxVirtualServerPortStatTotConns_Type()
)
axVirtualServerPortStatTotConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatTotConns.setStatus("current")
_AxVirtualServerPortStatCurConns_Type = Integer32
_AxVirtualServerPortStatCurConns_Object = MibTableColumn
axVirtualServerPortStatCurConns = _AxVirtualServerPortStatCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 12),
    _AxVirtualServerPortStatCurConns_Type()
)
axVirtualServerPortStatCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatCurConns.setStatus("current")


class _AxVirtualServerStatPortDisplayStatus_Type(Integer32):
    """Custom type axVirtualServerStatPortDisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("allUp", 1),
          ("disabled", 0),
          ("functionalUp", 2),
          ("stopped", 4))
    )


_AxVirtualServerStatPortDisplayStatus_Type.__name__ = "Integer32"
_AxVirtualServerStatPortDisplayStatus_Object = MibTableColumn
axVirtualServerStatPortDisplayStatus = _AxVirtualServerStatPortDisplayStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 13),
    _AxVirtualServerStatPortDisplayStatus_Type()
)
axVirtualServerStatPortDisplayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerStatPortDisplayStatus.setStatus("current")
_AxVirtualServerPortStatTotalL7Reqs_Type = Counter64
_AxVirtualServerPortStatTotalL7Reqs_Object = MibTableColumn
axVirtualServerPortStatTotalL7Reqs = _AxVirtualServerPortStatTotalL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 14),
    _AxVirtualServerPortStatTotalL7Reqs_Type()
)
axVirtualServerPortStatTotalL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatTotalL7Reqs.setStatus("current")
_AxVirtualServerPortStatTotalCurrL7Reqs_Type = Counter64
_AxVirtualServerPortStatTotalCurrL7Reqs_Object = MibTableColumn
axVirtualServerPortStatTotalCurrL7Reqs = _AxVirtualServerPortStatTotalCurrL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 15),
    _AxVirtualServerPortStatTotalCurrL7Reqs_Type()
)
axVirtualServerPortStatTotalCurrL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatTotalCurrL7Reqs.setStatus("current")
_AxVirtualServerPortStatTotalSuccL7Reqs_Type = Counter64
_AxVirtualServerPortStatTotalSuccL7Reqs_Object = MibTableColumn
axVirtualServerPortStatTotalSuccL7Reqs = _AxVirtualServerPortStatTotalSuccL7Reqs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 4, 4, 1, 1, 16),
    _AxVirtualServerPortStatTotalSuccL7Reqs_Type()
)
axVirtualServerPortStatTotalSuccL7Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axVirtualServerPortStatTotalSuccL7Reqs.setStatus("current")
_AxConnReuseStats_ObjectIdentity = ObjectIdentity
axConnReuseStats = _AxConnReuseStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5)
)


class _AxConnReuseStatTotalOpenPersist_Type(Integer32):
    """Custom type axConnReuseStatTotalOpenPersist based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalOpenPersist_Object = MibScalar
axConnReuseStatTotalOpenPersist = _AxConnReuseStatTotalOpenPersist_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 1),
    _AxConnReuseStatTotalOpenPersist_Type()
)
axConnReuseStatTotalOpenPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalOpenPersist.setStatus("current")


class _AxConnReuseStatTotalActivePersist_Type(Integer32):
    """Custom type axConnReuseStatTotalActivePersist based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalActivePersist_Object = MibScalar
axConnReuseStatTotalActivePersist = _AxConnReuseStatTotalActivePersist_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 2),
    _AxConnReuseStatTotalActivePersist_Type()
)
axConnReuseStatTotalActivePersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalActivePersist.setStatus("current")


class _AxConnReuseStatTotalEstablished_Type(Integer32):
    """Custom type axConnReuseStatTotalEstablished based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalEstablished_Object = MibScalar
axConnReuseStatTotalEstablished = _AxConnReuseStatTotalEstablished_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 3),
    _AxConnReuseStatTotalEstablished_Type()
)
axConnReuseStatTotalEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalEstablished.setStatus("current")
_AxConnReuseStatTotalTerminated_Type = Integer32
_AxConnReuseStatTotalTerminated_Object = MibScalar
axConnReuseStatTotalTerminated = _AxConnReuseStatTotalTerminated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 4),
    _AxConnReuseStatTotalTerminated_Type()
)
axConnReuseStatTotalTerminated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalTerminated.setStatus("current")


class _AxConnReuseStatTotalBound_Type(Integer32):
    """Custom type axConnReuseStatTotalBound based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalBound_Object = MibScalar
axConnReuseStatTotalBound = _AxConnReuseStatTotalBound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 5),
    _AxConnReuseStatTotalBound_Type()
)
axConnReuseStatTotalBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalBound.setStatus("current")


class _AxConnReuseStatTotalUNBound_Type(Integer32):
    """Custom type axConnReuseStatTotalUNBound based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalUNBound_Object = MibScalar
axConnReuseStatTotalUNBound = _AxConnReuseStatTotalUNBound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 6),
    _AxConnReuseStatTotalUNBound_Type()
)
axConnReuseStatTotalUNBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalUNBound.setStatus("current")
_AxConnReuseStatTable_Object = MibTable
axConnReuseStatTable = _AxConnReuseStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7)
)
if mibBuilder.loadTexts:
    axConnReuseStatTable.setStatus("current")
_AxConnReuseStatEntry_Object = MibTableRow
axConnReuseStatEntry = _AxConnReuseStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1)
)
axConnReuseStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axConnReuseStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axConnReuseStatEntry.setStatus("current")
_AxConnReuseStatCpuIndex_Type = Integer32
_AxConnReuseStatCpuIndex_Object = MibTableColumn
axConnReuseStatCpuIndex = _AxConnReuseStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 1),
    _AxConnReuseStatCpuIndex_Type()
)
axConnReuseStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatCpuIndex.setStatus("current")


class _AxConnReuseStatOpenPersist_Type(Counter32):
    """Custom type axConnReuseStatOpenPersist based on Counter32"""
    defaultValue = 0


_AxConnReuseStatOpenPersist_Object = MibTableColumn
axConnReuseStatOpenPersist = _AxConnReuseStatOpenPersist_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 2),
    _AxConnReuseStatOpenPersist_Type()
)
axConnReuseStatOpenPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatOpenPersist.setStatus("current")


class _AxConnReuseStatActivePersist_Type(Counter32):
    """Custom type axConnReuseStatActivePersist based on Counter32"""
    defaultValue = 0


_AxConnReuseStatActivePersist_Object = MibTableColumn
axConnReuseStatActivePersist = _AxConnReuseStatActivePersist_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 3),
    _AxConnReuseStatActivePersist_Type()
)
axConnReuseStatActivePersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatActivePersist.setStatus("current")


class _AxConnReuseStatTotalEst_Type(Counter32):
    """Custom type axConnReuseStatTotalEst based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalEst_Object = MibTableColumn
axConnReuseStatTotalEst = _AxConnReuseStatTotalEst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 4),
    _AxConnReuseStatTotalEst_Type()
)
axConnReuseStatTotalEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalEst.setStatus("current")


class _AxConnReuseStatTotalTerm_Type(Counter32):
    """Custom type axConnReuseStatTotalTerm based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalTerm_Object = MibTableColumn
axConnReuseStatTotalTerm = _AxConnReuseStatTotalTerm_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 5),
    _AxConnReuseStatTotalTerm_Type()
)
axConnReuseStatTotalTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalTerm.setStatus("current")


class _AxConnReuseStatTotalBind_Type(Counter32):
    """Custom type axConnReuseStatTotalBind based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalBind_Object = MibTableColumn
axConnReuseStatTotalBind = _AxConnReuseStatTotalBind_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 6),
    _AxConnReuseStatTotalBind_Type()
)
axConnReuseStatTotalBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalBind.setStatus("current")


class _AxConnReuseStatTotalUNBind_Type(Counter32):
    """Custom type axConnReuseStatTotalUNBind based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalUNBind_Object = MibTableColumn
axConnReuseStatTotalUNBind = _AxConnReuseStatTotalUNBind_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 7),
    _AxConnReuseStatTotalUNBind_Type()
)
axConnReuseStatTotalUNBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalUNBind.setStatus("current")


class _AxConnReuseStatTotalDelayedUNBind_Type(Counter32):
    """Custom type axConnReuseStatTotalDelayedUNBind based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalDelayedUNBind_Object = MibTableColumn
axConnReuseStatTotalDelayedUNBind = _AxConnReuseStatTotalDelayedUNBind_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 8),
    _AxConnReuseStatTotalDelayedUNBind_Type()
)
axConnReuseStatTotalDelayedUNBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalDelayedUNBind.setStatus("current")


class _AxConnReuseStatTotalLongRes_Type(Counter32):
    """Custom type axConnReuseStatTotalLongRes based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalLongRes_Object = MibTableColumn
axConnReuseStatTotalLongRes = _AxConnReuseStatTotalLongRes_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 9),
    _AxConnReuseStatTotalLongRes_Type()
)
axConnReuseStatTotalLongRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalLongRes.setStatus("current")


class _AxConnReuseStatTotalMissedRes_Type(Counter32):
    """Custom type axConnReuseStatTotalMissedRes based on Counter32"""
    defaultValue = 0


_AxConnReuseStatTotalMissedRes_Object = MibTableColumn
axConnReuseStatTotalMissedRes = _AxConnReuseStatTotalMissedRes_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 7, 1, 10),
    _AxConnReuseStatTotalMissedRes_Type()
)
axConnReuseStatTotalMissedRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalMissedRes.setStatus("current")


class _AxConnReuseStatTotalDelayedUNBound_Type(Integer32):
    """Custom type axConnReuseStatTotalDelayedUNBound based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalDelayedUNBound_Object = MibScalar
axConnReuseStatTotalDelayedUNBound = _AxConnReuseStatTotalDelayedUNBound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 8),
    _AxConnReuseStatTotalDelayedUNBound_Type()
)
axConnReuseStatTotalDelayedUNBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalDelayedUNBound.setStatus("current")


class _AxConnReuseStatTotalLongResponse_Type(Integer32):
    """Custom type axConnReuseStatTotalLongResponse based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalLongResponse_Object = MibScalar
axConnReuseStatTotalLongResponse = _AxConnReuseStatTotalLongResponse_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 9),
    _AxConnReuseStatTotalLongResponse_Type()
)
axConnReuseStatTotalLongResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalLongResponse.setStatus("current")


class _AxConnReuseStatTotalMissedResponse_Type(Integer32):
    """Custom type axConnReuseStatTotalMissedResponse based on Integer32"""
    defaultValue = 0


_AxConnReuseStatTotalMissedResponse_Object = MibScalar
axConnReuseStatTotalMissedResponse = _AxConnReuseStatTotalMissedResponse_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 5, 10),
    _AxConnReuseStatTotalMissedResponse_Type()
)
axConnReuseStatTotalMissedResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axConnReuseStatTotalMissedResponse.setStatus("current")
_AxFastHttpProxyStats_ObjectIdentity = ObjectIdentity
axFastHttpProxyStats = _AxFastHttpProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6)
)


class _AxFastHttpProxyStatTotalConn_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalConn based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalConn_Object = MibScalar
axFastHttpProxyStatTotalConn = _AxFastHttpProxyStatTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 1),
    _AxFastHttpProxyStatTotalConn_Type()
)
axFastHttpProxyStatTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalConn.setStatus("current")


class _AxFastHttpProxyStatTotalReq_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalReq based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalReq_Object = MibScalar
axFastHttpProxyStatTotalReq = _AxFastHttpProxyStatTotalReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 2),
    _AxFastHttpProxyStatTotalReq_Type()
)
axFastHttpProxyStatTotalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalReq.setStatus("current")


class _AxFastHttpProxyStatTotalSuccReq_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSuccReq based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSuccReq_Object = MibScalar
axFastHttpProxyStatTotalSuccReq = _AxFastHttpProxyStatTotalSuccReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 3),
    _AxFastHttpProxyStatTotalSuccReq_Type()
)
axFastHttpProxyStatTotalSuccReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSuccReq.setStatus("current")


class _AxFastHttpProxyStatTotalNoProxy_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalNoProxy based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalNoProxy_Object = MibScalar
axFastHttpProxyStatTotalNoProxy = _AxFastHttpProxyStatTotalNoProxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 4),
    _AxFastHttpProxyStatTotalNoProxy_Type()
)
axFastHttpProxyStatTotalNoProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalNoProxy.setStatus("current")


class _AxFastHttpProxyStatTotalCRst_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalCRst based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalCRst_Object = MibScalar
axFastHttpProxyStatTotalCRst = _AxFastHttpProxyStatTotalCRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 5),
    _AxFastHttpProxyStatTotalCRst_Type()
)
axFastHttpProxyStatTotalCRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalCRst.setStatus("current")


class _AxFastHttpProxyStatTotalSRst_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSRst based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSRst_Object = MibScalar
axFastHttpProxyStatTotalSRst = _AxFastHttpProxyStatTotalSRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 6),
    _AxFastHttpProxyStatTotalSRst_Type()
)
axFastHttpProxyStatTotalSRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSRst.setStatus("current")


class _AxFastHttpProxyStatTotalNoTuple_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalNoTuple based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalNoTuple_Object = MibScalar
axFastHttpProxyStatTotalNoTuple = _AxFastHttpProxyStatTotalNoTuple_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 7),
    _AxFastHttpProxyStatTotalNoTuple_Type()
)
axFastHttpProxyStatTotalNoTuple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalNoTuple.setStatus("current")


class _AxFastHttpProxyStatTotalReqErr_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalReqErr based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalReqErr_Object = MibScalar
axFastHttpProxyStatTotalReqErr = _AxFastHttpProxyStatTotalReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 8),
    _AxFastHttpProxyStatTotalReqErr_Type()
)
axFastHttpProxyStatTotalReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalReqErr.setStatus("current")


class _AxFastHttpProxyStatTotalSvrSelErr_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSvrSelErr based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSvrSelErr_Object = MibScalar
axFastHttpProxyStatTotalSvrSelErr = _AxFastHttpProxyStatTotalSvrSelErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 9),
    _AxFastHttpProxyStatTotalSvrSelErr_Type()
)
axFastHttpProxyStatTotalSvrSelErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSvrSelErr.setStatus("current")


class _AxFastHttpProxyStatTotalFwdReqErr_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalFwdReqErr based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalFwdReqErr_Object = MibScalar
axFastHttpProxyStatTotalFwdReqErr = _AxFastHttpProxyStatTotalFwdReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 10),
    _AxFastHttpProxyStatTotalFwdReqErr_Type()
)
axFastHttpProxyStatTotalFwdReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalFwdReqErr.setStatus("current")


class _AxFastHttpProxyStatTotalFwdDataReqErr_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalFwdDataReqErr based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalFwdDataReqErr_Object = MibScalar
axFastHttpProxyStatTotalFwdDataReqErr = _AxFastHttpProxyStatTotalFwdDataReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 11),
    _AxFastHttpProxyStatTotalFwdDataReqErr_Type()
)
axFastHttpProxyStatTotalFwdDataReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalFwdDataReqErr.setStatus("current")


class _AxFastHttpProxyStatTotalReqReXmit_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalReqReXmit based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalReqReXmit_Object = MibScalar
axFastHttpProxyStatTotalReqReXmit = _AxFastHttpProxyStatTotalReqReXmit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 12),
    _AxFastHttpProxyStatTotalReqReXmit_Type()
)
axFastHttpProxyStatTotalReqReXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalReqReXmit.setStatus("current")


class _AxFastHttpProxyStatTotalReqPktOutOrder_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalReqPktOutOrder based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalReqPktOutOrder_Object = MibScalar
axFastHttpProxyStatTotalReqPktOutOrder = _AxFastHttpProxyStatTotalReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 13),
    _AxFastHttpProxyStatTotalReqPktOutOrder_Type()
)
axFastHttpProxyStatTotalReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalReqPktOutOrder.setStatus("current")


class _AxFastHttpProxyStatTotalSvrReSel_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSvrReSel based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSvrReSel_Object = MibScalar
axFastHttpProxyStatTotalSvrReSel = _AxFastHttpProxyStatTotalSvrReSel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 14),
    _AxFastHttpProxyStatTotalSvrReSel_Type()
)
axFastHttpProxyStatTotalSvrReSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSvrReSel.setStatus("current")


class _AxFastHttpProxyStatTotalPreMatureClose_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalPreMatureClose based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalPreMatureClose_Object = MibScalar
axFastHttpProxyStatTotalPreMatureClose = _AxFastHttpProxyStatTotalPreMatureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 15),
    _AxFastHttpProxyStatTotalPreMatureClose_Type()
)
axFastHttpProxyStatTotalPreMatureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalPreMatureClose.setStatus("current")


class _AxFastHttpProxyStatTotalSvrConn_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSvrConn based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSvrConn_Object = MibScalar
axFastHttpProxyStatTotalSvrConn = _AxFastHttpProxyStatTotalSvrConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 16),
    _AxFastHttpProxyStatTotalSvrConn_Type()
)
axFastHttpProxyStatTotalSvrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSvrConn.setStatus("current")


class _AxFastHttpProxyStatTotalSNATErr_Type(Integer32):
    """Custom type axFastHttpProxyStatTotalSNATErr based on Integer32"""
    defaultValue = 0


_AxFastHttpProxyStatTotalSNATErr_Object = MibScalar
axFastHttpProxyStatTotalSNATErr = _AxFastHttpProxyStatTotalSNATErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 17),
    _AxFastHttpProxyStatTotalSNATErr_Type()
)
axFastHttpProxyStatTotalSNATErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalSNATErr.setStatus("current")
_AxFastHttpProxyStatTable_Object = MibTable
axFastHttpProxyStatTable = _AxFastHttpProxyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18)
)
if mibBuilder.loadTexts:
    axFastHttpProxyStatTable.setStatus("current")
_AxFastHttpProxyStatEntry_Object = MibTableRow
axFastHttpProxyStatEntry = _AxFastHttpProxyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1)
)
axFastHttpProxyStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axFastHttpProxyStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axFastHttpProxyStatEntry.setStatus("current")
_AxFastHttpProxyStatCpuIndex_Type = Integer32
_AxFastHttpProxyStatCpuIndex_Object = MibTableColumn
axFastHttpProxyStatCpuIndex = _AxFastHttpProxyStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 1),
    _AxFastHttpProxyStatCpuIndex_Type()
)
axFastHttpProxyStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatCpuIndex.setStatus("current")


class _AxFastHttpProxyStatCurrProxyConns_Type(Counter32):
    """Custom type axFastHttpProxyStatCurrProxyConns based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatCurrProxyConns_Object = MibTableColumn
axFastHttpProxyStatCurrProxyConns = _AxFastHttpProxyStatCurrProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 2),
    _AxFastHttpProxyStatCurrProxyConns_Type()
)
axFastHttpProxyStatCurrProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatCurrProxyConns.setStatus("current")
_AxFastHttpProxyStatTotalProxyConns_Type = Counter32
_AxFastHttpProxyStatTotalProxyConns_Object = MibTableColumn
axFastHttpProxyStatTotalProxyConns = _AxFastHttpProxyStatTotalProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 3),
    _AxFastHttpProxyStatTotalProxyConns_Type()
)
axFastHttpProxyStatTotalProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatTotalProxyConns.setStatus("current")


class _AxFastHttpProxyStatHttpReq_Type(Counter32):
    """Custom type axFastHttpProxyStatHttpReq based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatHttpReq_Object = MibTableColumn
axFastHttpProxyStatHttpReq = _AxFastHttpProxyStatHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 4),
    _AxFastHttpProxyStatHttpReq_Type()
)
axFastHttpProxyStatHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatHttpReq.setStatus("current")


class _AxFastHttpProxyStatHttpReqSucc_Type(Counter32):
    """Custom type axFastHttpProxyStatHttpReqSucc based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatHttpReqSucc_Object = MibTableColumn
axFastHttpProxyStatHttpReqSucc = _AxFastHttpProxyStatHttpReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 5),
    _AxFastHttpProxyStatHttpReqSucc_Type()
)
axFastHttpProxyStatHttpReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatHttpReqSucc.setStatus("current")


class _AxFastHttpProxyStatNoProxyErr_Type(Counter32):
    """Custom type axFastHttpProxyStatNoProxyErr based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatNoProxyErr_Object = MibTableColumn
axFastHttpProxyStatNoProxyErr = _AxFastHttpProxyStatNoProxyErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 6),
    _AxFastHttpProxyStatNoProxyErr_Type()
)
axFastHttpProxyStatNoProxyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatNoProxyErr.setStatus("current")


class _AxFastHttpProxyStatClientRst_Type(Counter32):
    """Custom type axFastHttpProxyStatClientRst based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatClientRst_Object = MibTableColumn
axFastHttpProxyStatClientRst = _AxFastHttpProxyStatClientRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 7),
    _AxFastHttpProxyStatClientRst_Type()
)
axFastHttpProxyStatClientRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatClientRst.setStatus("current")


class _AxFastHttpProxyStatServerRst_Type(Counter32):
    """Custom type axFastHttpProxyStatServerRst based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatServerRst_Object = MibTableColumn
axFastHttpProxyStatServerRst = _AxFastHttpProxyStatServerRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 8),
    _AxFastHttpProxyStatServerRst_Type()
)
axFastHttpProxyStatServerRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatServerRst.setStatus("current")


class _AxFastHttpProxyStatNoTupleErr_Type(Counter32):
    """Custom type axFastHttpProxyStatNoTupleErr based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatNoTupleErr_Object = MibTableColumn
axFastHttpProxyStatNoTupleErr = _AxFastHttpProxyStatNoTupleErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 9),
    _AxFastHttpProxyStatNoTupleErr_Type()
)
axFastHttpProxyStatNoTupleErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatNoTupleErr.setStatus("current")


class _AxFastHttpProxyStatParseReqFail_Type(Counter32):
    """Custom type axFastHttpProxyStatParseReqFail based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatParseReqFail_Object = MibTableColumn
axFastHttpProxyStatParseReqFail = _AxFastHttpProxyStatParseReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 10),
    _AxFastHttpProxyStatParseReqFail_Type()
)
axFastHttpProxyStatParseReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatParseReqFail.setStatus("current")


class _AxFastHttpProxyStatServerSelFail_Type(Counter32):
    """Custom type axFastHttpProxyStatServerSelFail based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatServerSelFail_Object = MibTableColumn
axFastHttpProxyStatServerSelFail = _AxFastHttpProxyStatServerSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 11),
    _AxFastHttpProxyStatServerSelFail_Type()
)
axFastHttpProxyStatServerSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatServerSelFail.setStatus("current")


class _AxFastHttpProxyStatFwdReqFail_Type(Counter32):
    """Custom type axFastHttpProxyStatFwdReqFail based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatFwdReqFail_Object = MibTableColumn
axFastHttpProxyStatFwdReqFail = _AxFastHttpProxyStatFwdReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 12),
    _AxFastHttpProxyStatFwdReqFail_Type()
)
axFastHttpProxyStatFwdReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatFwdReqFail.setStatus("current")


class _AxFastHttpProxyStatFwdReqDataFail_Type(Counter32):
    """Custom type axFastHttpProxyStatFwdReqDataFail based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatFwdReqDataFail_Object = MibTableColumn
axFastHttpProxyStatFwdReqDataFail = _AxFastHttpProxyStatFwdReqDataFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 13),
    _AxFastHttpProxyStatFwdReqDataFail_Type()
)
axFastHttpProxyStatFwdReqDataFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatFwdReqDataFail.setStatus("current")


class _AxFastHttpProxyStatReqReTran_Type(Counter32):
    """Custom type axFastHttpProxyStatReqReTran based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatReqReTran_Object = MibTableColumn
axFastHttpProxyStatReqReTran = _AxFastHttpProxyStatReqReTran_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 14),
    _AxFastHttpProxyStatReqReTran_Type()
)
axFastHttpProxyStatReqReTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatReqReTran.setStatus("current")


class _AxFastHttpProxyStatReqPktOutOrder_Type(Counter32):
    """Custom type axFastHttpProxyStatReqPktOutOrder based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatReqPktOutOrder_Object = MibTableColumn
axFastHttpProxyStatReqPktOutOrder = _AxFastHttpProxyStatReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 15),
    _AxFastHttpProxyStatReqPktOutOrder_Type()
)
axFastHttpProxyStatReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatReqPktOutOrder.setStatus("current")


class _AxFastHttpProxyStatServerReSel_Type(Counter32):
    """Custom type axFastHttpProxyStatServerReSel based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatServerReSel_Object = MibTableColumn
axFastHttpProxyStatServerReSel = _AxFastHttpProxyStatServerReSel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 16),
    _AxFastHttpProxyStatServerReSel_Type()
)
axFastHttpProxyStatServerReSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatServerReSel.setStatus("current")


class _AxFastHttpProxyStatServerPreMatureClose_Type(Counter32):
    """Custom type axFastHttpProxyStatServerPreMatureClose based on Counter32"""
    defaultValue = 0


_AxFastHttpProxyStatServerPreMatureClose_Object = MibTableColumn
axFastHttpProxyStatServerPreMatureClose = _AxFastHttpProxyStatServerPreMatureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 17),
    _AxFastHttpProxyStatServerPreMatureClose_Type()
)
axFastHttpProxyStatServerPreMatureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatServerPreMatureClose.setStatus("current")
_AxFastHttpProxyStatServerConnMade_Type = Counter32
_AxFastHttpProxyStatServerConnMade_Object = MibTableColumn
axFastHttpProxyStatServerConnMade = _AxFastHttpProxyStatServerConnMade_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 6, 18, 1, 18),
    _AxFastHttpProxyStatServerConnMade_Type()
)
axFastHttpProxyStatServerConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFastHttpProxyStatServerConnMade.setStatus("current")
_AxHttpProxyStats_ObjectIdentity = ObjectIdentity
axHttpProxyStats = _AxHttpProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7)
)


class _AxHttpProxyStatTotalConn_Type(Integer32):
    """Custom type axHttpProxyStatTotalConn based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalConn_Object = MibScalar
axHttpProxyStatTotalConn = _AxHttpProxyStatTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 1),
    _AxHttpProxyStatTotalConn_Type()
)
axHttpProxyStatTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalConn.setStatus("current")


class _AxHttpProxyStatTotalReq_Type(Integer32):
    """Custom type axHttpProxyStatTotalReq based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalReq_Object = MibScalar
axHttpProxyStatTotalReq = _AxHttpProxyStatTotalReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 2),
    _AxHttpProxyStatTotalReq_Type()
)
axHttpProxyStatTotalReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalReq.setStatus("current")


class _AxHttpProxyStatTotalSuccReq_Type(Integer32):
    """Custom type axHttpProxyStatTotalSuccReq based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSuccReq_Object = MibScalar
axHttpProxyStatTotalSuccReq = _AxHttpProxyStatTotalSuccReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 3),
    _AxHttpProxyStatTotalSuccReq_Type()
)
axHttpProxyStatTotalSuccReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSuccReq.setStatus("current")


class _AxHttpProxyStatTotalNoProxy_Type(Integer32):
    """Custom type axHttpProxyStatTotalNoProxy based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalNoProxy_Object = MibScalar
axHttpProxyStatTotalNoProxy = _AxHttpProxyStatTotalNoProxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 4),
    _AxHttpProxyStatTotalNoProxy_Type()
)
axHttpProxyStatTotalNoProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalNoProxy.setStatus("current")


class _AxHttpProxyStatTotalCRst_Type(Integer32):
    """Custom type axHttpProxyStatTotalCRst based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalCRst_Object = MibScalar
axHttpProxyStatTotalCRst = _AxHttpProxyStatTotalCRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 5),
    _AxHttpProxyStatTotalCRst_Type()
)
axHttpProxyStatTotalCRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalCRst.setStatus("current")


class _AxHttpProxyStatTotalSRst_Type(Integer32):
    """Custom type axHttpProxyStatTotalSRst based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSRst_Object = MibScalar
axHttpProxyStatTotalSRst = _AxHttpProxyStatTotalSRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 6),
    _AxHttpProxyStatTotalSRst_Type()
)
axHttpProxyStatTotalSRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSRst.setStatus("current")


class _AxHttpProxyStatTotalNoTuple_Type(Integer32):
    """Custom type axHttpProxyStatTotalNoTuple based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalNoTuple_Object = MibScalar
axHttpProxyStatTotalNoTuple = _AxHttpProxyStatTotalNoTuple_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 7),
    _AxHttpProxyStatTotalNoTuple_Type()
)
axHttpProxyStatTotalNoTuple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalNoTuple.setStatus("current")


class _AxHttpProxyStatTotalReqErr_Type(Integer32):
    """Custom type axHttpProxyStatTotalReqErr based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalReqErr_Object = MibScalar
axHttpProxyStatTotalReqErr = _AxHttpProxyStatTotalReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 8),
    _AxHttpProxyStatTotalReqErr_Type()
)
axHttpProxyStatTotalReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalReqErr.setStatus("current")


class _AxHttpProxyStatTotalSvrSelErr_Type(Integer32):
    """Custom type axHttpProxyStatTotalSvrSelErr based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSvrSelErr_Object = MibScalar
axHttpProxyStatTotalSvrSelErr = _AxHttpProxyStatTotalSvrSelErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 9),
    _AxHttpProxyStatTotalSvrSelErr_Type()
)
axHttpProxyStatTotalSvrSelErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSvrSelErr.setStatus("current")


class _AxHttpProxyStatTotalFwdReqErr_Type(Integer32):
    """Custom type axHttpProxyStatTotalFwdReqErr based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalFwdReqErr_Object = MibScalar
axHttpProxyStatTotalFwdReqErr = _AxHttpProxyStatTotalFwdReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 10),
    _AxHttpProxyStatTotalFwdReqErr_Type()
)
axHttpProxyStatTotalFwdReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalFwdReqErr.setStatus("current")


class _AxHttpProxyStatTotalFwdDataReqErr_Type(Integer32):
    """Custom type axHttpProxyStatTotalFwdDataReqErr based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalFwdDataReqErr_Object = MibScalar
axHttpProxyStatTotalFwdDataReqErr = _AxHttpProxyStatTotalFwdDataReqErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 11),
    _AxHttpProxyStatTotalFwdDataReqErr_Type()
)
axHttpProxyStatTotalFwdDataReqErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalFwdDataReqErr.setStatus("current")


class _AxHttpProxyStatTotalReqReXmit_Type(Integer32):
    """Custom type axHttpProxyStatTotalReqReXmit based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalReqReXmit_Object = MibScalar
axHttpProxyStatTotalReqReXmit = _AxHttpProxyStatTotalReqReXmit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 12),
    _AxHttpProxyStatTotalReqReXmit_Type()
)
axHttpProxyStatTotalReqReXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalReqReXmit.setStatus("current")


class _AxHttpProxyStatTotalReqPktOutOrder_Type(Integer32):
    """Custom type axHttpProxyStatTotalReqPktOutOrder based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalReqPktOutOrder_Object = MibScalar
axHttpProxyStatTotalReqPktOutOrder = _AxHttpProxyStatTotalReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 13),
    _AxHttpProxyStatTotalReqPktOutOrder_Type()
)
axHttpProxyStatTotalReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalReqPktOutOrder.setStatus("current")


class _AxHttpProxyStatTotalSvrReSel_Type(Integer32):
    """Custom type axHttpProxyStatTotalSvrReSel based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSvrReSel_Object = MibScalar
axHttpProxyStatTotalSvrReSel = _AxHttpProxyStatTotalSvrReSel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 14),
    _AxHttpProxyStatTotalSvrReSel_Type()
)
axHttpProxyStatTotalSvrReSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSvrReSel.setStatus("current")


class _AxHttpProxyStatTotalPreMatureClose_Type(Integer32):
    """Custom type axHttpProxyStatTotalPreMatureClose based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalPreMatureClose_Object = MibScalar
axHttpProxyStatTotalPreMatureClose = _AxHttpProxyStatTotalPreMatureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 15),
    _AxHttpProxyStatTotalPreMatureClose_Type()
)
axHttpProxyStatTotalPreMatureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalPreMatureClose.setStatus("current")


class _AxHttpProxyStatTotalSvrConn_Type(Integer32):
    """Custom type axHttpProxyStatTotalSvrConn based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSvrConn_Object = MibScalar
axHttpProxyStatTotalSvrConn = _AxHttpProxyStatTotalSvrConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 16),
    _AxHttpProxyStatTotalSvrConn_Type()
)
axHttpProxyStatTotalSvrConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSvrConn.setStatus("current")


class _AxHttpProxyStatTotalSNATErr_Type(Integer32):
    """Custom type axHttpProxyStatTotalSNATErr based on Integer32"""
    defaultValue = 0


_AxHttpProxyStatTotalSNATErr_Object = MibScalar
axHttpProxyStatTotalSNATErr = _AxHttpProxyStatTotalSNATErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 17),
    _AxHttpProxyStatTotalSNATErr_Type()
)
axHttpProxyStatTotalSNATErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalSNATErr.setStatus("current")
_AxHttpProxyStatTable_Object = MibTable
axHttpProxyStatTable = _AxHttpProxyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18)
)
if mibBuilder.loadTexts:
    axHttpProxyStatTable.setStatus("current")
_AxHttpProxyStatEntry_Object = MibTableRow
axHttpProxyStatEntry = _AxHttpProxyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1)
)
axHttpProxyStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axHttpProxyStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axHttpProxyStatEntry.setStatus("current")
_AxHttpProxyStatCpuIndex_Type = Integer32
_AxHttpProxyStatCpuIndex_Object = MibTableColumn
axHttpProxyStatCpuIndex = _AxHttpProxyStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 1),
    _AxHttpProxyStatCpuIndex_Type()
)
axHttpProxyStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatCpuIndex.setStatus("current")


class _AxHttpProxyStatCurrProxyConns_Type(Counter32):
    """Custom type axHttpProxyStatCurrProxyConns based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatCurrProxyConns_Object = MibTableColumn
axHttpProxyStatCurrProxyConns = _AxHttpProxyStatCurrProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 2),
    _AxHttpProxyStatCurrProxyConns_Type()
)
axHttpProxyStatCurrProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatCurrProxyConns.setStatus("current")
_AxHttpProxyStatTotalProxyConns_Type = Counter32
_AxHttpProxyStatTotalProxyConns_Object = MibTableColumn
axHttpProxyStatTotalProxyConns = _AxHttpProxyStatTotalProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 3),
    _AxHttpProxyStatTotalProxyConns_Type()
)
axHttpProxyStatTotalProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatTotalProxyConns.setStatus("current")


class _AxHttpProxyStatHttpReq_Type(Counter32):
    """Custom type axHttpProxyStatHttpReq based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatHttpReq_Object = MibTableColumn
axHttpProxyStatHttpReq = _AxHttpProxyStatHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 4),
    _AxHttpProxyStatHttpReq_Type()
)
axHttpProxyStatHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatHttpReq.setStatus("current")


class _AxHttpProxyStatHttpReqSucc_Type(Counter32):
    """Custom type axHttpProxyStatHttpReqSucc based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatHttpReqSucc_Object = MibTableColumn
axHttpProxyStatHttpReqSucc = _AxHttpProxyStatHttpReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 5),
    _AxHttpProxyStatHttpReqSucc_Type()
)
axHttpProxyStatHttpReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatHttpReqSucc.setStatus("current")


class _AxHttpProxyStatNoProxyErr_Type(Counter32):
    """Custom type axHttpProxyStatNoProxyErr based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatNoProxyErr_Object = MibTableColumn
axHttpProxyStatNoProxyErr = _AxHttpProxyStatNoProxyErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 6),
    _AxHttpProxyStatNoProxyErr_Type()
)
axHttpProxyStatNoProxyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatNoProxyErr.setStatus("current")


class _AxHttpProxyStatClientRst_Type(Counter32):
    """Custom type axHttpProxyStatClientRst based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatClientRst_Object = MibTableColumn
axHttpProxyStatClientRst = _AxHttpProxyStatClientRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 7),
    _AxHttpProxyStatClientRst_Type()
)
axHttpProxyStatClientRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatClientRst.setStatus("current")


class _AxHttpProxyStatServerRst_Type(Counter32):
    """Custom type axHttpProxyStatServerRst based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatServerRst_Object = MibTableColumn
axHttpProxyStatServerRst = _AxHttpProxyStatServerRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 8),
    _AxHttpProxyStatServerRst_Type()
)
axHttpProxyStatServerRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatServerRst.setStatus("current")


class _AxHttpProxyStatNoTupleErr_Type(Counter32):
    """Custom type axHttpProxyStatNoTupleErr based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatNoTupleErr_Object = MibTableColumn
axHttpProxyStatNoTupleErr = _AxHttpProxyStatNoTupleErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 9),
    _AxHttpProxyStatNoTupleErr_Type()
)
axHttpProxyStatNoTupleErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatNoTupleErr.setStatus("current")


class _AxHttpProxyStatParseReqFail_Type(Counter32):
    """Custom type axHttpProxyStatParseReqFail based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatParseReqFail_Object = MibTableColumn
axHttpProxyStatParseReqFail = _AxHttpProxyStatParseReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 10),
    _AxHttpProxyStatParseReqFail_Type()
)
axHttpProxyStatParseReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatParseReqFail.setStatus("current")


class _AxHttpProxyStatServerSelFail_Type(Counter32):
    """Custom type axHttpProxyStatServerSelFail based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatServerSelFail_Object = MibTableColumn
axHttpProxyStatServerSelFail = _AxHttpProxyStatServerSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 11),
    _AxHttpProxyStatServerSelFail_Type()
)
axHttpProxyStatServerSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatServerSelFail.setStatus("current")


class _AxHttpProxyStatFwdReqFail_Type(Counter32):
    """Custom type axHttpProxyStatFwdReqFail based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatFwdReqFail_Object = MibTableColumn
axHttpProxyStatFwdReqFail = _AxHttpProxyStatFwdReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 12),
    _AxHttpProxyStatFwdReqFail_Type()
)
axHttpProxyStatFwdReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatFwdReqFail.setStatus("current")


class _AxHttpProxyStatFwdReqDataFail_Type(Counter32):
    """Custom type axHttpProxyStatFwdReqDataFail based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatFwdReqDataFail_Object = MibTableColumn
axHttpProxyStatFwdReqDataFail = _AxHttpProxyStatFwdReqDataFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 13),
    _AxHttpProxyStatFwdReqDataFail_Type()
)
axHttpProxyStatFwdReqDataFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatFwdReqDataFail.setStatus("current")


class _AxHttpProxyStatReqReTran_Type(Counter32):
    """Custom type axHttpProxyStatReqReTran based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatReqReTran_Object = MibTableColumn
axHttpProxyStatReqReTran = _AxHttpProxyStatReqReTran_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 14),
    _AxHttpProxyStatReqReTran_Type()
)
axHttpProxyStatReqReTran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatReqReTran.setStatus("current")


class _AxHttpProxyStatReqPktOutOrder_Type(Counter32):
    """Custom type axHttpProxyStatReqPktOutOrder based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatReqPktOutOrder_Object = MibTableColumn
axHttpProxyStatReqPktOutOrder = _AxHttpProxyStatReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 15),
    _AxHttpProxyStatReqPktOutOrder_Type()
)
axHttpProxyStatReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatReqPktOutOrder.setStatus("current")


class _AxHttpProxyStatServerReSel_Type(Counter32):
    """Custom type axHttpProxyStatServerReSel based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatServerReSel_Object = MibTableColumn
axHttpProxyStatServerReSel = _AxHttpProxyStatServerReSel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 16),
    _AxHttpProxyStatServerReSel_Type()
)
axHttpProxyStatServerReSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatServerReSel.setStatus("current")


class _AxHttpProxyStatServerPreMatureClose_Type(Counter32):
    """Custom type axHttpProxyStatServerPreMatureClose based on Counter32"""
    defaultValue = 0


_AxHttpProxyStatServerPreMatureClose_Object = MibTableColumn
axHttpProxyStatServerPreMatureClose = _AxHttpProxyStatServerPreMatureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 17),
    _AxHttpProxyStatServerPreMatureClose_Type()
)
axHttpProxyStatServerPreMatureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatServerPreMatureClose.setStatus("current")
_AxHttpProxyStatServerConnMade_Type = Counter32
_AxHttpProxyStatServerConnMade_Object = MibTableColumn
axHttpProxyStatServerConnMade = _AxHttpProxyStatServerConnMade_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 7, 18, 1, 18),
    _AxHttpProxyStatServerConnMade_Type()
)
axHttpProxyStatServerConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHttpProxyStatServerConnMade.setStatus("current")
_AxTcpProxyStats_ObjectIdentity = ObjectIdentity
axTcpProxyStats = _AxTcpProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8)
)


class _AxTcpProxyStatTotalCurrEstConn_Type(Integer32):
    """Custom type axTcpProxyStatTotalCurrEstConn based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalCurrEstConn_Object = MibScalar
axTcpProxyStatTotalCurrEstConn = _AxTcpProxyStatTotalCurrEstConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 1),
    _AxTcpProxyStatTotalCurrEstConn_Type()
)
axTcpProxyStatTotalCurrEstConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalCurrEstConn.setStatus("current")


class _AxTcpProxyStatTotalActiveOpenConn_Type(Integer32):
    """Custom type axTcpProxyStatTotalActiveOpenConn based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalActiveOpenConn_Object = MibScalar
axTcpProxyStatTotalActiveOpenConn = _AxTcpProxyStatTotalActiveOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 2),
    _AxTcpProxyStatTotalActiveOpenConn_Type()
)
axTcpProxyStatTotalActiveOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalActiveOpenConn.setStatus("current")


class _AxTcpProxyStatTotalPassiveOpenConn_Type(Integer32):
    """Custom type axTcpProxyStatTotalPassiveOpenConn based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalPassiveOpenConn_Object = MibScalar
axTcpProxyStatTotalPassiveOpenConn = _AxTcpProxyStatTotalPassiveOpenConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 3),
    _AxTcpProxyStatTotalPassiveOpenConn_Type()
)
axTcpProxyStatTotalPassiveOpenConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalPassiveOpenConn.setStatus("current")


class _AxTcpProxyStatTotalConnAttemptFail_Type(Integer32):
    """Custom type axTcpProxyStatTotalConnAttemptFail based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalConnAttemptFail_Object = MibScalar
axTcpProxyStatTotalConnAttemptFail = _AxTcpProxyStatTotalConnAttemptFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 4),
    _AxTcpProxyStatTotalConnAttemptFail_Type()
)
axTcpProxyStatTotalConnAttemptFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalConnAttemptFail.setStatus("current")


class _AxTcpProxyStatTotalInTCPPacket_Type(Integer32):
    """Custom type axTcpProxyStatTotalInTCPPacket based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalInTCPPacket_Object = MibScalar
axTcpProxyStatTotalInTCPPacket = _AxTcpProxyStatTotalInTCPPacket_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 5),
    _AxTcpProxyStatTotalInTCPPacket_Type()
)
axTcpProxyStatTotalInTCPPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalInTCPPacket.setStatus("current")


class _AxTcpProxyStatTotalOutTCPPkt_Type(Integer32):
    """Custom type axTcpProxyStatTotalOutTCPPkt based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalOutTCPPkt_Object = MibScalar
axTcpProxyStatTotalOutTCPPkt = _AxTcpProxyStatTotalOutTCPPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 6),
    _AxTcpProxyStatTotalOutTCPPkt_Type()
)
axTcpProxyStatTotalOutTCPPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalOutTCPPkt.setStatus("current")


class _AxTcpProxyStatTotalReXmitPkt_Type(Integer32):
    """Custom type axTcpProxyStatTotalReXmitPkt based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalReXmitPkt_Object = MibScalar
axTcpProxyStatTotalReXmitPkt = _AxTcpProxyStatTotalReXmitPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 7),
    _AxTcpProxyStatTotalReXmitPkt_Type()
)
axTcpProxyStatTotalReXmitPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalReXmitPkt.setStatus("current")


class _AxTcpProxyStatTotalRstRcvOnEstConn_Type(Integer32):
    """Custom type axTcpProxyStatTotalRstRcvOnEstConn based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalRstRcvOnEstConn_Object = MibScalar
axTcpProxyStatTotalRstRcvOnEstConn = _AxTcpProxyStatTotalRstRcvOnEstConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 8),
    _AxTcpProxyStatTotalRstRcvOnEstConn_Type()
)
axTcpProxyStatTotalRstRcvOnEstConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalRstRcvOnEstConn.setStatus("current")


class _AxTcpProxyStatTotalRstSent_Type(Integer32):
    """Custom type axTcpProxyStatTotalRstSent based on Integer32"""
    defaultValue = 0


_AxTcpProxyStatTotalRstSent_Object = MibScalar
axTcpProxyStatTotalRstSent = _AxTcpProxyStatTotalRstSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 9),
    _AxTcpProxyStatTotalRstSent_Type()
)
axTcpProxyStatTotalRstSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalRstSent.setStatus("current")
_AxTCPProxyStatTable_Object = MibTable
axTCPProxyStatTable = _AxTCPProxyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10)
)
if mibBuilder.loadTexts:
    axTCPProxyStatTable.setStatus("current")
_AxTCPProxyStatEntry_Object = MibTableRow
axTCPProxyStatEntry = _AxTCPProxyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1)
)
axTCPProxyStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axTcpProxyStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axTCPProxyStatEntry.setStatus("current")
_AxTcpProxyStatCpuIndex_Type = Integer32
_AxTcpProxyStatCpuIndex_Object = MibTableColumn
axTcpProxyStatCpuIndex = _AxTcpProxyStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 1),
    _AxTcpProxyStatCpuIndex_Type()
)
axTcpProxyStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatCpuIndex.setStatus("current")


class _AxTcpProxyStatCurrEstConns_Type(Counter32):
    """Custom type axTcpProxyStatCurrEstConns based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatCurrEstConns_Object = MibTableColumn
axTcpProxyStatCurrEstConns = _AxTcpProxyStatCurrEstConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 2),
    _AxTcpProxyStatCurrEstConns_Type()
)
axTcpProxyStatCurrEstConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatCurrEstConns.setStatus("current")


class _AxTcpProxyStatActiveOpenConns_Type(Counter32):
    """Custom type axTcpProxyStatActiveOpenConns based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatActiveOpenConns_Object = MibTableColumn
axTcpProxyStatActiveOpenConns = _AxTcpProxyStatActiveOpenConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 3),
    _AxTcpProxyStatActiveOpenConns_Type()
)
axTcpProxyStatActiveOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatActiveOpenConns.setStatus("current")


class _AxTcpProxyStatPassiveOpenConns_Type(Counter32):
    """Custom type axTcpProxyStatPassiveOpenConns based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatPassiveOpenConns_Object = MibTableColumn
axTcpProxyStatPassiveOpenConns = _AxTcpProxyStatPassiveOpenConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 4),
    _AxTcpProxyStatPassiveOpenConns_Type()
)
axTcpProxyStatPassiveOpenConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatPassiveOpenConns.setStatus("current")


class _AxTcpProxyStatConnAttempFail_Type(Counter32):
    """Custom type axTcpProxyStatConnAttempFail based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatConnAttempFail_Object = MibTableColumn
axTcpProxyStatConnAttempFail = _AxTcpProxyStatConnAttempFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 5),
    _AxTcpProxyStatConnAttempFail_Type()
)
axTcpProxyStatConnAttempFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatConnAttempFail.setStatus("current")


class _AxTcpProxyStatTotalInTCPPkt_Type(Counter32):
    """Custom type axTcpProxyStatTotalInTCPPkt based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTotalInTCPPkt_Object = MibTableColumn
axTcpProxyStatTotalInTCPPkt = _AxTcpProxyStatTotalInTCPPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 6),
    _AxTcpProxyStatTotalInTCPPkt_Type()
)
axTcpProxyStatTotalInTCPPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalInTCPPkt.setStatus("current")


class _AxTcpProxyStatTotalOutPkt_Type(Counter32):
    """Custom type axTcpProxyStatTotalOutPkt based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTotalOutPkt_Object = MibTableColumn
axTcpProxyStatTotalOutPkt = _AxTcpProxyStatTotalOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 7),
    _AxTcpProxyStatTotalOutPkt_Type()
)
axTcpProxyStatTotalOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalOutPkt.setStatus("current")


class _AxTcpProxyStatReTranPkt_Type(Counter32):
    """Custom type axTcpProxyStatReTranPkt based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatReTranPkt_Object = MibTableColumn
axTcpProxyStatReTranPkt = _AxTcpProxyStatReTranPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 8),
    _AxTcpProxyStatReTranPkt_Type()
)
axTcpProxyStatReTranPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatReTranPkt.setStatus("current")


class _AxTcpProxyStatRstRvdEstConn_Type(Counter32):
    """Custom type axTcpProxyStatRstRvdEstConn based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatRstRvdEstConn_Object = MibTableColumn
axTcpProxyStatRstRvdEstConn = _AxTcpProxyStatRstRvdEstConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 9),
    _AxTcpProxyStatRstRvdEstConn_Type()
)
axTcpProxyStatRstRvdEstConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatRstRvdEstConn.setStatus("current")


class _AxTcpProxyStatRstSent_Type(Counter32):
    """Custom type axTcpProxyStatRstSent based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatRstSent_Object = MibTableColumn
axTcpProxyStatRstSent = _AxTcpProxyStatRstSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 10),
    _AxTcpProxyStatRstSent_Type()
)
axTcpProxyStatRstSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatRstSent.setStatus("current")


class _AxTcpProxyStatInputErr_Type(Counter32):
    """Custom type axTcpProxyStatInputErr based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatInputErr_Object = MibTableColumn
axTcpProxyStatInputErr = _AxTcpProxyStatInputErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 11),
    _AxTcpProxyStatInputErr_Type()
)
axTcpProxyStatInputErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatInputErr.setStatus("current")


class _AxTcpProxyStatSocketAlloc_Type(Counter32):
    """Custom type axTcpProxyStatSocketAlloc based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatSocketAlloc_Object = MibTableColumn
axTcpProxyStatSocketAlloc = _AxTcpProxyStatSocketAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 12),
    _AxTcpProxyStatSocketAlloc_Type()
)
axTcpProxyStatSocketAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatSocketAlloc.setStatus("current")


class _AxTcpProxyStatOrphanSocket_Type(Counter32):
    """Custom type axTcpProxyStatOrphanSocket based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatOrphanSocket_Object = MibTableColumn
axTcpProxyStatOrphanSocket = _AxTcpProxyStatOrphanSocket_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 13),
    _AxTcpProxyStatOrphanSocket_Type()
)
axTcpProxyStatOrphanSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatOrphanSocket.setStatus("current")


class _AxTcpProxyStatMemAlloc_Type(Counter32):
    """Custom type axTcpProxyStatMemAlloc based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatMemAlloc_Object = MibTableColumn
axTcpProxyStatMemAlloc = _AxTcpProxyStatMemAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 14),
    _AxTcpProxyStatMemAlloc_Type()
)
axTcpProxyStatMemAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatMemAlloc.setStatus("current")


class _AxTcpProxyStatTotalRxBuf_Type(Counter32):
    """Custom type axTcpProxyStatTotalRxBuf based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTotalRxBuf_Object = MibTableColumn
axTcpProxyStatTotalRxBuf = _AxTcpProxyStatTotalRxBuf_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 15),
    _AxTcpProxyStatTotalRxBuf_Type()
)
axTcpProxyStatTotalRxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalRxBuf.setStatus("current")


class _AxTcpProxyStatTotalTxBuf_Type(Counter32):
    """Custom type axTcpProxyStatTotalTxBuf based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTotalTxBuf_Object = MibTableColumn
axTcpProxyStatTotalTxBuf = _AxTcpProxyStatTotalTxBuf_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 16),
    _AxTcpProxyStatTotalTxBuf_Type()
)
axTcpProxyStatTotalTxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTotalTxBuf.setStatus("current")


class _AxTcpProxyStatTCPSYNSNTState_Type(Counter32):
    """Custom type axTcpProxyStatTCPSYNSNTState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPSYNSNTState_Object = MibTableColumn
axTcpProxyStatTCPSYNSNTState = _AxTcpProxyStatTCPSYNSNTState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 17),
    _AxTcpProxyStatTCPSYNSNTState_Type()
)
axTcpProxyStatTCPSYNSNTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPSYNSNTState.setStatus("current")


class _AxTcpProxyStatTCPSYNRCVState_Type(Counter32):
    """Custom type axTcpProxyStatTCPSYNRCVState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPSYNRCVState_Object = MibTableColumn
axTcpProxyStatTCPSYNRCVState = _AxTcpProxyStatTCPSYNRCVState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 18),
    _AxTcpProxyStatTCPSYNRCVState_Type()
)
axTcpProxyStatTCPSYNRCVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPSYNRCVState.setStatus("current")


class _AxTcpProxyStatTCPFINW1State_Type(Counter32):
    """Custom type axTcpProxyStatTCPFINW1State based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPFINW1State_Object = MibTableColumn
axTcpProxyStatTCPFINW1State = _AxTcpProxyStatTCPFINW1State_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 19),
    _AxTcpProxyStatTCPFINW1State_Type()
)
axTcpProxyStatTCPFINW1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPFINW1State.setStatus("current")


class _AxTcpProxyStatTCPFINW2State_Type(Counter32):
    """Custom type axTcpProxyStatTCPFINW2State based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPFINW2State_Object = MibTableColumn
axTcpProxyStatTCPFINW2State = _AxTcpProxyStatTCPFINW2State_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 20),
    _AxTcpProxyStatTCPFINW2State_Type()
)
axTcpProxyStatTCPFINW2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPFINW2State.setStatus("current")


class _AxTcpProxyStatTimeWstate_Type(Counter32):
    """Custom type axTcpProxyStatTimeWstate based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTimeWstate_Object = MibTableColumn
axTcpProxyStatTimeWstate = _AxTcpProxyStatTimeWstate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 21),
    _AxTcpProxyStatTimeWstate_Type()
)
axTcpProxyStatTimeWstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTimeWstate.setStatus("current")


class _AxTcpProxyStatTCPCloseState_Type(Counter32):
    """Custom type axTcpProxyStatTCPCloseState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPCloseState_Object = MibTableColumn
axTcpProxyStatTCPCloseState = _AxTcpProxyStatTCPCloseState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 22),
    _AxTcpProxyStatTCPCloseState_Type()
)
axTcpProxyStatTCPCloseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPCloseState.setStatus("current")


class _AxTcpProxyStatTCPCloseWState_Type(Counter32):
    """Custom type axTcpProxyStatTCPCloseWState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPCloseWState_Object = MibTableColumn
axTcpProxyStatTCPCloseWState = _AxTcpProxyStatTCPCloseWState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 23),
    _AxTcpProxyStatTCPCloseWState_Type()
)
axTcpProxyStatTCPCloseWState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPCloseWState.setStatus("current")


class _AxTcpProxyStatTCPLastACKState_Type(Counter32):
    """Custom type axTcpProxyStatTCPLastACKState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPLastACKState_Object = MibTableColumn
axTcpProxyStatTCPLastACKState = _AxTcpProxyStatTCPLastACKState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 24),
    _AxTcpProxyStatTCPLastACKState_Type()
)
axTcpProxyStatTCPLastACKState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPLastACKState.setStatus("current")


class _AxTcpProxyStatTCPListenState_Type(Counter32):
    """Custom type axTcpProxyStatTCPListenState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPListenState_Object = MibTableColumn
axTcpProxyStatTCPListenState = _AxTcpProxyStatTCPListenState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 25),
    _AxTcpProxyStatTCPListenState_Type()
)
axTcpProxyStatTCPListenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPListenState.setStatus("current")


class _AxTcpProxyStatTCPClosingState_Type(Counter32):
    """Custom type axTcpProxyStatTCPClosingState based on Counter32"""
    defaultValue = 0


_AxTcpProxyStatTCPClosingState_Object = MibTableColumn
axTcpProxyStatTCPClosingState = _AxTcpProxyStatTCPClosingState_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 8, 10, 1, 26),
    _AxTcpProxyStatTCPClosingState_Type()
)
axTcpProxyStatTCPClosingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTcpProxyStatTCPClosingState.setStatus("current")
_AxSslStats_ObjectIdentity = ObjectIdentity
axSslStats = _AxSslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9)
)


class _AxSslStatSSLModNum_Type(Integer32):
    """Custom type axSslStatSSLModNum based on Integer32"""
    defaultValue = 1


_AxSslStatSSLModNum_Object = MibScalar
axSslStatSSLModNum = _AxSslStatSSLModNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 1),
    _AxSslStatSSLModNum_Type()
)
axSslStatSSLModNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLModNum.setStatus("current")


class _AxSslStatCurrSSLConn_Type(Integer32):
    """Custom type axSslStatCurrSSLConn based on Integer32"""
    defaultValue = 0


_AxSslStatCurrSSLConn_Object = MibScalar
axSslStatCurrSSLConn = _AxSslStatCurrSSLConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 2),
    _AxSslStatCurrSSLConn_Type()
)
axSslStatCurrSSLConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatCurrSSLConn.setStatus("current")


class _AxSslStatTotalSSLConn_Type(Integer32):
    """Custom type axSslStatTotalSSLConn based on Integer32"""
    defaultValue = 0


_AxSslStatTotalSSLConn_Object = MibScalar
axSslStatTotalSSLConn = _AxSslStatTotalSSLConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 3),
    _AxSslStatTotalSSLConn_Type()
)
axSslStatTotalSSLConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatTotalSSLConn.setStatus("current")


class _AxSslStatFailSSLHandshake_Type(Integer32):
    """Custom type axSslStatFailSSLHandshake based on Integer32"""
    defaultValue = 0


_AxSslStatFailSSLHandshake_Object = MibScalar
axSslStatFailSSLHandshake = _AxSslStatFailSSLHandshake_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 4),
    _AxSslStatFailSSLHandshake_Type()
)
axSslStatFailSSLHandshake.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatFailSSLHandshake.setStatus("current")


class _AxSslStatSSLMemUsage_Type(Integer32):
    """Custom type axSslStatSSLMemUsage based on Integer32"""
    defaultValue = 0


_AxSslStatSSLMemUsage_Object = MibScalar
axSslStatSSLMemUsage = _AxSslStatSSLMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 5),
    _AxSslStatSSLMemUsage_Type()
)
axSslStatSSLMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLMemUsage.setStatus("current")
_AxSslStatTable_Object = MibTable
axSslStatTable = _AxSslStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 6)
)
if mibBuilder.loadTexts:
    axSslStatTable.setStatus("current")
_AxSslStatEntry_Object = MibTableRow
axSslStatEntry = _AxSslStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 6, 1)
)
axSslStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axSslStatModuleIndex"),
)
if mibBuilder.loadTexts:
    axSslStatEntry.setStatus("current")
_AxSslStatModuleIndex_Type = Integer32
_AxSslStatModuleIndex_Object = MibTableColumn
axSslStatModuleIndex = _AxSslStatModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 6, 1, 1),
    _AxSslStatModuleIndex_Type()
)
axSslStatModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatModuleIndex.setStatus("current")


class _AxSslStatEnableCryptoEngine_Type(Counter32):
    """Custom type axSslStatEnableCryptoEngine based on Counter32"""
    defaultValue = 22


_AxSslStatEnableCryptoEngine_Object = MibTableColumn
axSslStatEnableCryptoEngine = _AxSslStatEnableCryptoEngine_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 6, 1, 2),
    _AxSslStatEnableCryptoEngine_Type()
)
axSslStatEnableCryptoEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatEnableCryptoEngine.setStatus("current")


class _AxSslStatAvailCryptoEngine_Type(Counter32):
    """Custom type axSslStatAvailCryptoEngine based on Counter32"""
    defaultValue = 22


_AxSslStatAvailCryptoEngine_Object = MibTableColumn
axSslStatAvailCryptoEngine = _AxSslStatAvailCryptoEngine_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 6, 1, 3),
    _AxSslStatAvailCryptoEngine_Type()
)
axSslStatAvailCryptoEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatAvailCryptoEngine.setStatus("current")


class _AxSslStatSSLFailedCAVfy_Type(Integer32):
    """Custom type axSslStatSSLFailedCAVfy based on Integer32"""
    defaultValue = 0


_AxSslStatSSLFailedCAVfy_Object = MibScalar
axSslStatSSLFailedCAVfy = _AxSslStatSSLFailedCAVfy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 7),
    _AxSslStatSSLFailedCAVfy_Type()
)
axSslStatSSLFailedCAVfy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLFailedCAVfy.setStatus("current")


class _AxSslStatSSLNoHWContextMem_Type(Integer32):
    """Custom type axSslStatSSLNoHWContextMem based on Integer32"""
    defaultValue = 0


_AxSslStatSSLNoHWContextMem_Object = MibScalar
axSslStatSSLNoHWContextMem = _AxSslStatSSLNoHWContextMem_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 8),
    _AxSslStatSSLNoHWContextMem_Type()
)
axSslStatSSLNoHWContextMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLNoHWContextMem.setStatus("current")


class _AxSslStatSSLHWRingFull_Type(Integer32):
    """Custom type axSslStatSSLHWRingFull based on Integer32"""
    defaultValue = 0


_AxSslStatSSLHWRingFull_Object = MibScalar
axSslStatSSLHWRingFull = _AxSslStatSSLHWRingFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 9),
    _AxSslStatSSLHWRingFull_Type()
)
axSslStatSSLHWRingFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLHWRingFull.setStatus("current")


class _AxSslStatSSLFailedCryptoOperation_Type(Integer32):
    """Custom type axSslStatSSLFailedCryptoOperation based on Integer32"""
    defaultValue = 0


_AxSslStatSSLFailedCryptoOperation_Object = MibScalar
axSslStatSSLFailedCryptoOperation = _AxSslStatSSLFailedCryptoOperation_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 9, 10),
    _AxSslStatSSLFailedCryptoOperation_Type()
)
axSslStatSSLFailedCryptoOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslStatSSLFailedCryptoOperation.setStatus("current")
_AxFtpStats_ObjectIdentity = ObjectIdentity
axFtpStats = _AxFtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10)
)


class _AxFtpStatTotalCtrlSession_Type(Integer32):
    """Custom type axFtpStatTotalCtrlSession based on Integer32"""
    defaultValue = 0


_AxFtpStatTotalCtrlSession_Object = MibScalar
axFtpStatTotalCtrlSession = _AxFtpStatTotalCtrlSession_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 1),
    _AxFtpStatTotalCtrlSession_Type()
)
axFtpStatTotalCtrlSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatTotalCtrlSession.setStatus("current")


class _AxFtpStatTotalALGPkt_Type(Integer32):
    """Custom type axFtpStatTotalALGPkt based on Integer32"""
    defaultValue = 0


_AxFtpStatTotalALGPkt_Object = MibScalar
axFtpStatTotalALGPkt = _AxFtpStatTotalALGPkt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 2),
    _AxFtpStatTotalALGPkt_Type()
)
axFtpStatTotalALGPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatTotalALGPkt.setStatus("current")


class _AxFtpStatALGPktReXmit_Type(Integer32):
    """Custom type axFtpStatALGPktReXmit based on Integer32"""
    defaultValue = 0


_AxFtpStatALGPktReXmit_Object = MibScalar
axFtpStatALGPktReXmit = _AxFtpStatALGPktReXmit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 3),
    _AxFtpStatALGPktReXmit_Type()
)
axFtpStatALGPktReXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatALGPktReXmit.setStatus("current")


class _AxFtpStatOutConnCtrl_Type(Integer32):
    """Custom type axFtpStatOutConnCtrl based on Integer32"""
    defaultValue = 0


_AxFtpStatOutConnCtrl_Object = MibScalar
axFtpStatOutConnCtrl = _AxFtpStatOutConnCtrl_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 4),
    _AxFtpStatOutConnCtrl_Type()
)
axFtpStatOutConnCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatOutConnCtrl.setStatus("current")


class _AxFtpStatTotalDataSession_Type(Integer32):
    """Custom type axFtpStatTotalDataSession based on Integer32"""
    defaultValue = 0


_AxFtpStatTotalDataSession_Object = MibScalar
axFtpStatTotalDataSession = _AxFtpStatTotalDataSession_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 5),
    _AxFtpStatTotalDataSession_Type()
)
axFtpStatTotalDataSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatTotalDataSession.setStatus("current")


class _AxFtpStatOutConnData_Type(Integer32):
    """Custom type axFtpStatOutConnData based on Integer32"""
    defaultValue = 0


_AxFtpStatOutConnData_Object = MibScalar
axFtpStatOutConnData = _AxFtpStatOutConnData_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 10, 6),
    _AxFtpStatOutConnData_Type()
)
axFtpStatOutConnData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFtpStatOutConnData.setStatus("current")
_AxNetStats_ObjectIdentity = ObjectIdentity
axNetStats = _AxNetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11)
)


class _AxNetStatIPOutNoRoute_Type(Counter32):
    """Custom type axNetStatIPOutNoRoute based on Counter32"""
    defaultValue = 0


_AxNetStatIPOutNoRoute_Object = MibScalar
axNetStatIPOutNoRoute = _AxNetStatIPOutNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 1),
    _AxNetStatIPOutNoRoute_Type()
)
axNetStatIPOutNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatIPOutNoRoute.setStatus("current")


class _AxNetStatTCPOutRst_Type(Counter32):
    """Custom type axNetStatTCPOutRst based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRst_Object = MibScalar
axNetStatTCPOutRst = _AxNetStatTCPOutRst_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 2),
    _AxNetStatTCPOutRst_Type()
)
axNetStatTCPOutRst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRst.setStatus("current")


class _AxNetStatTCPSynRcv_Type(Counter32):
    """Custom type axNetStatTCPSynRcv based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSynRcv_Object = MibScalar
axNetStatTCPSynRcv = _AxNetStatTCPSynRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 3),
    _AxNetStatTCPSynRcv_Type()
)
axNetStatTCPSynRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSynRcv.setStatus("current")


class _AxNetStatTCPSYNCookieSent_Type(Counter32):
    """Custom type axNetStatTCPSYNCookieSent based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSYNCookieSent_Object = MibScalar
axNetStatTCPSYNCookieSent = _AxNetStatTCPSYNCookieSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 4),
    _AxNetStatTCPSYNCookieSent_Type()
)
axNetStatTCPSYNCookieSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSYNCookieSent.setStatus("current")


class _AxNetStatTCPSYNCookieSentFail_Type(Counter32):
    """Custom type axNetStatTCPSYNCookieSentFail based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSYNCookieSentFail_Object = MibScalar
axNetStatTCPSYNCookieSentFail = _AxNetStatTCPSYNCookieSentFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 5),
    _AxNetStatTCPSYNCookieSentFail_Type()
)
axNetStatTCPSYNCookieSentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSYNCookieSentFail.setStatus("current")


class _AxNetStatTCPReceive_Type(Counter32):
    """Custom type axNetStatTCPReceive based on Counter32"""
    defaultValue = 0


_AxNetStatTCPReceive_Object = MibScalar
axNetStatTCPReceive = _AxNetStatTCPReceive_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 6),
    _AxNetStatTCPReceive_Type()
)
axNetStatTCPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPReceive.setStatus("current")


class _AxNetStatUDPReceive_Type(Counter32):
    """Custom type axNetStatUDPReceive based on Counter32"""
    defaultValue = 0


_AxNetStatUDPReceive_Object = MibScalar
axNetStatUDPReceive = _AxNetStatUDPReceive_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 7),
    _AxNetStatUDPReceive_Type()
)
axNetStatUDPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatUDPReceive.setStatus("current")


class _AxNetStatServerSelFail_Type(Counter32):
    """Custom type axNetStatServerSelFail based on Counter32"""
    defaultValue = 0


_AxNetStatServerSelFail_Object = MibScalar
axNetStatServerSelFail = _AxNetStatServerSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 8),
    _AxNetStatServerSelFail_Type()
)
axNetStatServerSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSelFail.setStatus("current")


class _AxNetStatSourceNATFail_Type(Counter32):
    """Custom type axNetStatSourceNATFail based on Counter32"""
    defaultValue = 0


_AxNetStatSourceNATFail_Object = MibScalar
axNetStatSourceNATFail = _AxNetStatSourceNATFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 9),
    _AxNetStatSourceNATFail_Type()
)
axNetStatSourceNATFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSourceNATFail.setStatus("current")


class _AxNetStatTCPSynCookieFail_Type(Counter32):
    """Custom type axNetStatTCPSynCookieFail based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSynCookieFail_Object = MibScalar
axNetStatTCPSynCookieFail = _AxNetStatTCPSynCookieFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 10),
    _AxNetStatTCPSynCookieFail_Type()
)
axNetStatTCPSynCookieFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSynCookieFail.setStatus("current")


class _AxNetStatNoVportDrop_Type(Counter32):
    """Custom type axNetStatNoVportDrop based on Counter32"""
    defaultValue = 0


_AxNetStatNoVportDrop_Object = MibScalar
axNetStatNoVportDrop = _AxNetStatNoVportDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 11),
    _AxNetStatNoVportDrop_Type()
)
axNetStatNoVportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoVportDrop.setStatus("current")


class _AxNetStatNoSynPktDrop_Type(Counter32):
    """Custom type axNetStatNoSynPktDrop based on Counter32"""
    defaultValue = 0


_AxNetStatNoSynPktDrop_Object = MibScalar
axNetStatNoSynPktDrop = _AxNetStatNoSynPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 12),
    _AxNetStatNoSynPktDrop_Type()
)
axNetStatNoSynPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoSynPktDrop.setStatus("current")


class _AxNetStatConnLimitDrop_Type(Counter32):
    """Custom type axNetStatConnLimitDrop based on Counter32"""
    defaultValue = 0


_AxNetStatConnLimitDrop_Object = MibScalar
axNetStatConnLimitDrop = _AxNetStatConnLimitDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 13),
    _AxNetStatConnLimitDrop_Type()
)
axNetStatConnLimitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnLimitDrop.setStatus("current")


class _AxNetStatConnLimitReset_Type(Counter32):
    """Custom type axNetStatConnLimitReset based on Counter32"""
    defaultValue = 0


_AxNetStatConnLimitReset_Object = MibScalar
axNetStatConnLimitReset = _AxNetStatConnLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 14),
    _AxNetStatConnLimitReset_Type()
)
axNetStatConnLimitReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnLimitReset.setStatus("current")


class _AxNetStatProxyNoSockDrop_Type(Counter32):
    """Custom type axNetStatProxyNoSockDrop based on Counter32"""
    defaultValue = 0


_AxNetStatProxyNoSockDrop_Object = MibScalar
axNetStatProxyNoSockDrop = _AxNetStatProxyNoSockDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 15),
    _AxNetStatProxyNoSockDrop_Type()
)
axNetStatProxyNoSockDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatProxyNoSockDrop.setStatus("current")


class _AxNetStataFlexDrop_Type(Counter32):
    """Custom type axNetStataFlexDrop based on Counter32"""
    defaultValue = 0


_AxNetStataFlexDrop_Object = MibScalar
axNetStataFlexDrop = _AxNetStataFlexDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 16),
    _AxNetStataFlexDrop_Type()
)
axNetStataFlexDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStataFlexDrop.setStatus("current")


class _AxNetStatSessionAgingOut_Type(Counter32):
    """Custom type axNetStatSessionAgingOut based on Counter32"""
    defaultValue = 0


_AxNetStatSessionAgingOut_Object = MibScalar
axNetStatSessionAgingOut = _AxNetStatSessionAgingOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 17),
    _AxNetStatSessionAgingOut_Type()
)
axNetStatSessionAgingOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSessionAgingOut.setStatus("current")


class _AxNetStatTCPNoSLB_Type(Counter32):
    """Custom type axNetStatTCPNoSLB based on Counter32"""
    defaultValue = 0


_AxNetStatTCPNoSLB_Object = MibScalar
axNetStatTCPNoSLB = _AxNetStatTCPNoSLB_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 18),
    _AxNetStatTCPNoSLB_Type()
)
axNetStatTCPNoSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPNoSLB.setStatus("current")


class _AxNetStatUDPNoSLB_Type(Counter32):
    """Custom type axNetStatUDPNoSLB based on Counter32"""
    defaultValue = 0


_AxNetStatUDPNoSLB_Object = MibScalar
axNetStatUDPNoSLB = _AxNetStatUDPNoSLB_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 19),
    _AxNetStatUDPNoSLB_Type()
)
axNetStatUDPNoSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatUDPNoSLB.setStatus("current")


class _AxNetStatTCPOutRSTNoSYN_Type(Counter32):
    """Custom type axNetStatTCPOutRSTNoSYN based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTNoSYN_Object = MibScalar
axNetStatTCPOutRSTNoSYN = _AxNetStatTCPOutRSTNoSYN_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 20),
    _AxNetStatTCPOutRSTNoSYN_Type()
)
axNetStatTCPOutRSTNoSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTNoSYN.setStatus("current")


class _AxNetStatTCPOutRSTL4Proxy_Type(Counter32):
    """Custom type axNetStatTCPOutRSTL4Proxy based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTL4Proxy_Object = MibScalar
axNetStatTCPOutRSTL4Proxy = _AxNetStatTCPOutRSTL4Proxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 21),
    _AxNetStatTCPOutRSTL4Proxy_Type()
)
axNetStatTCPOutRSTL4Proxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTL4Proxy.setStatus("current")


class _AxNetStatTCPOutRSTACKattack_Type(Counter32):
    """Custom type axNetStatTCPOutRSTACKattack based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTACKattack_Object = MibScalar
axNetStatTCPOutRSTACKattack = _AxNetStatTCPOutRSTACKattack_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 22),
    _AxNetStatTCPOutRSTACKattack_Type()
)
axNetStatTCPOutRSTACKattack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTACKattack.setStatus("current")


class _AxNetStatTCPOutRSTAFleX_Type(Counter32):
    """Custom type axNetStatTCPOutRSTAFleX based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTAFleX_Object = MibScalar
axNetStatTCPOutRSTAFleX = _AxNetStatTCPOutRSTAFleX_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 23),
    _AxNetStatTCPOutRSTAFleX_Type()
)
axNetStatTCPOutRSTAFleX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTAFleX.setStatus("current")


class _AxNetStatTCPOutRSTStaleSess_Type(Counter32):
    """Custom type axNetStatTCPOutRSTStaleSess based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTStaleSess_Object = MibScalar
axNetStatTCPOutRSTStaleSess = _AxNetStatTCPOutRSTStaleSess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 24),
    _AxNetStatTCPOutRSTStaleSess_Type()
)
axNetStatTCPOutRSTStaleSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTStaleSess.setStatus("current")


class _AxNetStatTCPOutRSTProxy_Type(Counter32):
    """Custom type axNetStatTCPOutRSTProxy based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutRSTProxy_Object = MibScalar
axNetStatTCPOutRSTProxy = _AxNetStatTCPOutRSTProxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 25),
    _AxNetStatTCPOutRSTProxy_Type()
)
axNetStatTCPOutRSTProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutRSTProxy.setStatus("current")


class _AxNetStatNoSYNPktDropFIN_Type(Counter32):
    """Custom type axNetStatNoSYNPktDropFIN based on Counter32"""
    defaultValue = 0


_AxNetStatNoSYNPktDropFIN_Object = MibScalar
axNetStatNoSYNPktDropFIN = _AxNetStatNoSYNPktDropFIN_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 26),
    _AxNetStatNoSYNPktDropFIN_Type()
)
axNetStatNoSYNPktDropFIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoSYNPktDropFIN.setStatus("current")


class _AxNetStatNoSYNPktDropRST_Type(Counter32):
    """Custom type axNetStatNoSYNPktDropRST based on Counter32"""
    defaultValue = 0


_AxNetStatNoSYNPktDropRST_Object = MibScalar
axNetStatNoSYNPktDropRST = _AxNetStatNoSYNPktDropRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 27),
    _AxNetStatNoSYNPktDropRST_Type()
)
axNetStatNoSYNPktDropRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoSYNPktDropRST.setStatus("current")


class _AxNetStatNoSYNPktDropACK_Type(Counter32):
    """Custom type axNetStatNoSYNPktDropACK based on Counter32"""
    defaultValue = 0


_AxNetStatNoSYNPktDropACK_Object = MibScalar
axNetStatNoSYNPktDropACK = _AxNetStatNoSYNPktDropACK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 28),
    _AxNetStatNoSYNPktDropACK_Type()
)
axNetStatNoSYNPktDropACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoSYNPktDropACK.setStatus("current")


class _AxNetStatSYNThrotte_Type(Counter32):
    """Custom type axNetStatSYNThrotte based on Counter32"""
    defaultValue = 0


_AxNetStatSYNThrotte_Object = MibScalar
axNetStatSYNThrotte = _AxNetStatSYNThrotte_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 29),
    _AxNetStatSYNThrotte_Type()
)
axNetStatSYNThrotte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSYNThrotte.setStatus("current")


class _AxNetStatSSLSIDPersistSucc_Type(Counter32):
    """Custom type axNetStatSSLSIDPersistSucc based on Counter32"""
    defaultValue = 0


_AxNetStatSSLSIDPersistSucc_Object = MibScalar
axNetStatSSLSIDPersistSucc = _AxNetStatSSLSIDPersistSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 30),
    _AxNetStatSSLSIDPersistSucc_Type()
)
axNetStatSSLSIDPersistSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSSLSIDPersistSucc.setStatus("current")


class _AxNetStatSSLSIDPersistFail_Type(Counter32):
    """Custom type axNetStatSSLSIDPersistFail based on Counter32"""
    defaultValue = 0


_AxNetStatSSLSIDPersistFail_Object = MibScalar
axNetStatSSLSIDPersistFail = _AxNetStatSSLSIDPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 31),
    _AxNetStatSSLSIDPersistFail_Type()
)
axNetStatSSLSIDPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSSLSIDPersistFail.setStatus("current")


class _AxNetStatClientSSLSIDNotFound_Type(Counter32):
    """Custom type axNetStatClientSSLSIDNotFound based on Counter32"""
    defaultValue = 0


_AxNetStatClientSSLSIDNotFound_Object = MibScalar
axNetStatClientSSLSIDNotFound = _AxNetStatClientSSLSIDNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 32),
    _AxNetStatClientSSLSIDNotFound_Type()
)
axNetStatClientSSLSIDNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatClientSSLSIDNotFound.setStatus("current")


class _AxNetStatClientSSLSIDMatch_Type(Counter32):
    """Custom type axNetStatClientSSLSIDMatch based on Counter32"""
    defaultValue = 0


_AxNetStatClientSSLSIDMatch_Object = MibScalar
axNetStatClientSSLSIDMatch = _AxNetStatClientSSLSIDMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 33),
    _AxNetStatClientSSLSIDMatch_Type()
)
axNetStatClientSSLSIDMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatClientSSLSIDMatch.setStatus("current")


class _AxNetStatClientSSLSIDNotMatch_Type(Counter32):
    """Custom type axNetStatClientSSLSIDNotMatch based on Counter32"""
    defaultValue = 0


_AxNetStatClientSSLSIDNotMatch_Object = MibScalar
axNetStatClientSSLSIDNotMatch = _AxNetStatClientSSLSIDNotMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 34),
    _AxNetStatClientSSLSIDNotMatch_Type()
)
axNetStatClientSSLSIDNotMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatClientSSLSIDNotMatch.setStatus("current")


class _AxNetStatServerSSLSIDNotFound_Type(Counter32):
    """Custom type axNetStatServerSSLSIDNotFound based on Counter32"""
    defaultValue = 0


_AxNetStatServerSSLSIDNotFound_Object = MibScalar
axNetStatServerSSLSIDNotFound = _AxNetStatServerSSLSIDNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 35),
    _AxNetStatServerSSLSIDNotFound_Type()
)
axNetStatServerSSLSIDNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSSLSIDNotFound.setStatus("current")


class _AxNetStatServerSSLSIDReset_Type(Counter32):
    """Custom type axNetStatServerSSLSIDReset based on Counter32"""
    defaultValue = 0


_AxNetStatServerSSLSIDReset_Object = MibScalar
axNetStatServerSSLSIDReset = _AxNetStatServerSSLSIDReset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 36),
    _AxNetStatServerSSLSIDReset_Type()
)
axNetStatServerSSLSIDReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSSLSIDReset.setStatus("current")


class _AxNetStatServerSSLSIDMatch_Type(Counter32):
    """Custom type axNetStatServerSSLSIDMatch based on Counter32"""
    defaultValue = 0


_AxNetStatServerSSLSIDMatch_Object = MibScalar
axNetStatServerSSLSIDMatch = _AxNetStatServerSSLSIDMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 37),
    _AxNetStatServerSSLSIDMatch_Type()
)
axNetStatServerSSLSIDMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSSLSIDMatch.setStatus("current")


class _AxNetStatServerSSLSIDNotMatch_Type(Counter32):
    """Custom type axNetStatServerSSLSIDNotMatch based on Counter32"""
    defaultValue = 0


_AxNetStatServerSSLSIDNotMatch_Object = MibScalar
axNetStatServerSSLSIDNotMatch = _AxNetStatServerSSLSIDNotMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 38),
    _AxNetStatServerSSLSIDNotMatch_Type()
)
axNetStatServerSSLSIDNotMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSSLSIDNotMatch.setStatus("current")


class _AxNetStatCreateSSLSIDSucc_Type(Counter32):
    """Custom type axNetStatCreateSSLSIDSucc based on Counter32"""
    defaultValue = 0


_AxNetStatCreateSSLSIDSucc_Object = MibScalar
axNetStatCreateSSLSIDSucc = _AxNetStatCreateSSLSIDSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 39),
    _AxNetStatCreateSSLSIDSucc_Type()
)
axNetStatCreateSSLSIDSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatCreateSSLSIDSucc.setStatus("current")


class _AxNetStatCreateSSLSIDFail_Type(Counter32):
    """Custom type axNetStatCreateSSLSIDFail based on Counter32"""
    defaultValue = 0


_AxNetStatCreateSSLSIDFail_Object = MibScalar
axNetStatCreateSSLSIDFail = _AxNetStatCreateSSLSIDFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 40),
    _AxNetStatCreateSSLSIDFail_Type()
)
axNetStatCreateSSLSIDFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatCreateSSLSIDFail.setStatus("current")


class _AxNetStatConnRateLimitDrops_Type(Counter32):
    """Custom type axNetStatConnRateLimitDrops based on Counter32"""
    defaultValue = 0


_AxNetStatConnRateLimitDrops_Object = MibScalar
axNetStatConnRateLimitDrops = _AxNetStatConnRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 41),
    _AxNetStatConnRateLimitDrops_Type()
)
axNetStatConnRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnRateLimitDrops.setStatus("current")


class _AxNetStatConnRateLimitResets_Type(Counter32):
    """Custom type axNetStatConnRateLimitResets based on Counter32"""
    defaultValue = 0


_AxNetStatConnRateLimitResets_Object = MibScalar
axNetStatConnRateLimitResets = _AxNetStatConnRateLimitResets_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 42),
    _AxNetStatConnRateLimitResets_Type()
)
axNetStatConnRateLimitResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnRateLimitResets.setStatus("current")


class _AxNetStatInbandHMRetry_Type(Counter32):
    """Custom type axNetStatInbandHMRetry based on Counter32"""
    defaultValue = 0


_AxNetStatInbandHMRetry_Object = MibScalar
axNetStatInbandHMRetry = _AxNetStatInbandHMRetry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 43),
    _AxNetStatInbandHMRetry_Type()
)
axNetStatInbandHMRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatInbandHMRetry.setStatus("current")


class _AxNetStatInbandHMReassign_Type(Counter32):
    """Custom type axNetStatInbandHMReassign based on Counter32"""
    defaultValue = 0


_AxNetStatInbandHMReassign_Object = MibScalar
axNetStatInbandHMReassign = _AxNetStatInbandHMReassign_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 44),
    _AxNetStatInbandHMReassign_Type()
)
axNetStatInbandHMReassign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatInbandHMReassign.setStatus("current")


class _AxNetStat2TCPReceive_Type(Counter64):
    """Custom type axNetStat2TCPReceive based on Counter64"""
    defaultValue = 0


_AxNetStat2TCPReceive_Object = MibScalar
axNetStat2TCPReceive = _AxNetStat2TCPReceive_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 45),
    _AxNetStat2TCPReceive_Type()
)
axNetStat2TCPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStat2TCPReceive.setStatus("current")


class _AxNetStat2UDPReceive_Type(Counter64):
    """Custom type axNetStat2UDPReceive based on Counter64"""
    defaultValue = 0


_AxNetStat2UDPReceive_Object = MibScalar
axNetStat2UDPReceive = _AxNetStat2UDPReceive_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 46),
    _AxNetStat2UDPReceive_Type()
)
axNetStat2UDPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStat2UDPReceive.setStatus("current")
_AxNetStatTable_Object = MibTable
axNetStatTable = _AxNetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100)
)
if mibBuilder.loadTexts:
    axNetStatTable.setStatus("current")
_AxNetStatEntry_Object = MibTableRow
axNetStatEntry = _AxNetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1)
)
axNetStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axNetStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axNetStatEntry.setStatus("current")
_AxNetStatCpuIndex_Type = Counter32
_AxNetStatCpuIndex_Object = MibTableColumn
axNetStatCpuIndex = _AxNetStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 1),
    _AxNetStatCpuIndex_Type()
)
axNetStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatCpuIndex.setStatus("current")


class _AxNetStatIPOutNoRt_Type(Counter32):
    """Custom type axNetStatIPOutNoRt based on Counter32"""
    defaultValue = 0


_AxNetStatIPOutNoRt_Object = MibTableColumn
axNetStatIPOutNoRt = _AxNetStatIPOutNoRt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 2),
    _AxNetStatIPOutNoRt_Type()
)
axNetStatIPOutNoRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatIPOutNoRt.setStatus("current")


class _AxNetStatTCPOutReset_Type(Counter32):
    """Custom type axNetStatTCPOutReset based on Counter32"""
    defaultValue = 0


_AxNetStatTCPOutReset_Object = MibTableColumn
axNetStatTCPOutReset = _AxNetStatTCPOutReset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 3),
    _AxNetStatTCPOutReset_Type()
)
axNetStatTCPOutReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPOutReset.setStatus("current")


class _AxNetStatTCPSynRecv_Type(Counter32):
    """Custom type axNetStatTCPSynRecv based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSynRecv_Object = MibTableColumn
axNetStatTCPSynRecv = _AxNetStatTCPSynRecv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 4),
    _AxNetStatTCPSynRecv_Type()
)
axNetStatTCPSynRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSynRecv.setStatus("current")


class _AxNetStatTCPSYNCookieSnt_Type(Counter32):
    """Custom type axNetStatTCPSYNCookieSnt based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSYNCookieSnt_Object = MibTableColumn
axNetStatTCPSYNCookieSnt = _AxNetStatTCPSYNCookieSnt_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 5),
    _AxNetStatTCPSYNCookieSnt_Type()
)
axNetStatTCPSYNCookieSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSYNCookieSnt.setStatus("current")


class _AxNetStatTCPSYNCookieSntFail_Type(Counter32):
    """Custom type axNetStatTCPSYNCookieSntFail based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSYNCookieSntFail_Object = MibTableColumn
axNetStatTCPSYNCookieSntFail = _AxNetStatTCPSYNCookieSntFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 6),
    _AxNetStatTCPSYNCookieSntFail_Type()
)
axNetStatTCPSYNCookieSntFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSYNCookieSntFail.setStatus("current")


class _AxNetStatTCPRcv_Type(Counter32):
    """Custom type axNetStatTCPRcv based on Counter32"""
    defaultValue = 0


_AxNetStatTCPRcv_Object = MibTableColumn
axNetStatTCPRcv = _AxNetStatTCPRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 7),
    _AxNetStatTCPRcv_Type()
)
axNetStatTCPRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPRcv.setStatus("current")


class _AxNetStatUDPRcv_Type(Counter32):
    """Custom type axNetStatUDPRcv based on Counter32"""
    defaultValue = 0


_AxNetStatUDPRcv_Object = MibTableColumn
axNetStatUDPRcv = _AxNetStatUDPRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 8),
    _AxNetStatUDPRcv_Type()
)
axNetStatUDPRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatUDPRcv.setStatus("current")


class _AxNetStatServerSelFails_Type(Counter32):
    """Custom type axNetStatServerSelFails based on Counter32"""
    defaultValue = 0


_AxNetStatServerSelFails_Object = MibTableColumn
axNetStatServerSelFails = _AxNetStatServerSelFails_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 9),
    _AxNetStatServerSelFails_Type()
)
axNetStatServerSelFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatServerSelFails.setStatus("current")


class _AxNetStatSourceNATFails_Type(Counter32):
    """Custom type axNetStatSourceNATFails based on Counter32"""
    defaultValue = 0


_AxNetStatSourceNATFails_Object = MibTableColumn
axNetStatSourceNATFails = _AxNetStatSourceNATFails_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 10),
    _AxNetStatSourceNATFails_Type()
)
axNetStatSourceNATFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSourceNATFails.setStatus("current")


class _AxNetStatTCPSynCookieFails_Type(Counter32):
    """Custom type axNetStatTCPSynCookieFails based on Counter32"""
    defaultValue = 0


_AxNetStatTCPSynCookieFails_Object = MibTableColumn
axNetStatTCPSynCookieFails = _AxNetStatTCPSynCookieFails_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 11),
    _AxNetStatTCPSynCookieFails_Type()
)
axNetStatTCPSynCookieFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPSynCookieFails.setStatus("current")


class _AxNetStatNoVportDrops_Type(Counter32):
    """Custom type axNetStatNoVportDrops based on Counter32"""
    defaultValue = 0


_AxNetStatNoVportDrops_Object = MibTableColumn
axNetStatNoVportDrops = _AxNetStatNoVportDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 12),
    _AxNetStatNoVportDrops_Type()
)
axNetStatNoVportDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoVportDrops.setStatus("current")


class _AxNetStatNoSynPktDrops_Type(Counter32):
    """Custom type axNetStatNoSynPktDrops based on Counter32"""
    defaultValue = 0


_AxNetStatNoSynPktDrops_Object = MibTableColumn
axNetStatNoSynPktDrops = _AxNetStatNoSynPktDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 13),
    _AxNetStatNoSynPktDrops_Type()
)
axNetStatNoSynPktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatNoSynPktDrops.setStatus("current")


class _AxNetStatConnLimitDrops_Type(Counter32):
    """Custom type axNetStatConnLimitDrops based on Counter32"""
    defaultValue = 0


_AxNetStatConnLimitDrops_Object = MibTableColumn
axNetStatConnLimitDrops = _AxNetStatConnLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 14),
    _AxNetStatConnLimitDrops_Type()
)
axNetStatConnLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnLimitDrops.setStatus("current")


class _AxNetStatConnLimitResets_Type(Counter32):
    """Custom type axNetStatConnLimitResets based on Counter32"""
    defaultValue = 0


_AxNetStatConnLimitResets_Object = MibTableColumn
axNetStatConnLimitResets = _AxNetStatConnLimitResets_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 15),
    _AxNetStatConnLimitResets_Type()
)
axNetStatConnLimitResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatConnLimitResets.setStatus("current")


class _AxNetStatProxyNoSockDrops_Type(Counter32):
    """Custom type axNetStatProxyNoSockDrops based on Counter32"""
    defaultValue = 0


_AxNetStatProxyNoSockDrops_Object = MibTableColumn
axNetStatProxyNoSockDrops = _AxNetStatProxyNoSockDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 16),
    _AxNetStatProxyNoSockDrops_Type()
)
axNetStatProxyNoSockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatProxyNoSockDrops.setStatus("current")


class _AxNetStataFlexDrops_Type(Counter32):
    """Custom type axNetStataFlexDrops based on Counter32"""
    defaultValue = 0


_AxNetStataFlexDrops_Object = MibTableColumn
axNetStataFlexDrops = _AxNetStataFlexDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 17),
    _AxNetStataFlexDrops_Type()
)
axNetStataFlexDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStataFlexDrops.setStatus("current")


class _AxNetStatSessionsAgingOut_Type(Counter32):
    """Custom type axNetStatSessionsAgingOut based on Counter32"""
    defaultValue = 0


_AxNetStatSessionsAgingOut_Object = MibTableColumn
axNetStatSessionsAgingOut = _AxNetStatSessionsAgingOut_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 18),
    _AxNetStatSessionsAgingOut_Type()
)
axNetStatSessionsAgingOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatSessionsAgingOut.setStatus("current")


class _AxNetStatTCPsNoSLB_Type(Counter32):
    """Custom type axNetStatTCPsNoSLB based on Counter32"""
    defaultValue = 0


_AxNetStatTCPsNoSLB_Object = MibTableColumn
axNetStatTCPsNoSLB = _AxNetStatTCPsNoSLB_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 19),
    _AxNetStatTCPsNoSLB_Type()
)
axNetStatTCPsNoSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatTCPsNoSLB.setStatus("current")


class _AxNetStatUDPsNoSLB_Type(Counter32):
    """Custom type axNetStatUDPsNoSLB based on Counter32"""
    defaultValue = 0


_AxNetStatUDPsNoSLB_Object = MibTableColumn
axNetStatUDPsNoSLB = _AxNetStatUDPsNoSLB_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 20),
    _AxNetStatUDPsNoSLB_Type()
)
axNetStatUDPsNoSLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatUDPsNoSLB.setStatus("current")


class _AxNetStatEntryTCPOutRSTNoSYN_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTNoSYN based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTNoSYN_Object = MibTableColumn
axNetStatEntryTCPOutRSTNoSYN = _AxNetStatEntryTCPOutRSTNoSYN_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 21),
    _AxNetStatEntryTCPOutRSTNoSYN_Type()
)
axNetStatEntryTCPOutRSTNoSYN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTNoSYN.setStatus("current")


class _AxNetStatEntryTCPOutRSTL4Proxy_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTL4Proxy based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTL4Proxy_Object = MibTableColumn
axNetStatEntryTCPOutRSTL4Proxy = _AxNetStatEntryTCPOutRSTL4Proxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 22),
    _AxNetStatEntryTCPOutRSTL4Proxy_Type()
)
axNetStatEntryTCPOutRSTL4Proxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTL4Proxy.setStatus("current")


class _AxNetStatEntryTCPOutRSTACKattack_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTACKattack based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTACKattack_Object = MibTableColumn
axNetStatEntryTCPOutRSTACKattack = _AxNetStatEntryTCPOutRSTACKattack_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 23),
    _AxNetStatEntryTCPOutRSTACKattack_Type()
)
axNetStatEntryTCPOutRSTACKattack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTACKattack.setStatus("current")


class _AxNetStatEntryTCPOutRSTAFleX_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTAFleX based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTAFleX_Object = MibTableColumn
axNetStatEntryTCPOutRSTAFleX = _AxNetStatEntryTCPOutRSTAFleX_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 24),
    _AxNetStatEntryTCPOutRSTAFleX_Type()
)
axNetStatEntryTCPOutRSTAFleX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTAFleX.setStatus("current")


class _AxNetStatEntryTCPOutRSTStaleSess_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTStaleSess based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTStaleSess_Object = MibTableColumn
axNetStatEntryTCPOutRSTStaleSess = _AxNetStatEntryTCPOutRSTStaleSess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 25),
    _AxNetStatEntryTCPOutRSTStaleSess_Type()
)
axNetStatEntryTCPOutRSTStaleSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTStaleSess.setStatus("current")


class _AxNetStatEntryTCPOutRSTProxy_Type(Counter32):
    """Custom type axNetStatEntryTCPOutRSTProxy based on Counter32"""
    defaultValue = 0


_AxNetStatEntryTCPOutRSTProxy_Object = MibTableColumn
axNetStatEntryTCPOutRSTProxy = _AxNetStatEntryTCPOutRSTProxy_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 26),
    _AxNetStatEntryTCPOutRSTProxy_Type()
)
axNetStatEntryTCPOutRSTProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryTCPOutRSTProxy.setStatus("current")


class _AxNetStatEntryNoSYNPktDropFIN_Type(Counter32):
    """Custom type axNetStatEntryNoSYNPktDropFIN based on Counter32"""
    defaultValue = 0


_AxNetStatEntryNoSYNPktDropFIN_Object = MibTableColumn
axNetStatEntryNoSYNPktDropFIN = _AxNetStatEntryNoSYNPktDropFIN_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 27),
    _AxNetStatEntryNoSYNPktDropFIN_Type()
)
axNetStatEntryNoSYNPktDropFIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryNoSYNPktDropFIN.setStatus("current")


class _AxNetStatEntryNoSYNPktDropRST_Type(Counter32):
    """Custom type axNetStatEntryNoSYNPktDropRST based on Counter32"""
    defaultValue = 0


_AxNetStatEntryNoSYNPktDropRST_Object = MibTableColumn
axNetStatEntryNoSYNPktDropRST = _AxNetStatEntryNoSYNPktDropRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 28),
    _AxNetStatEntryNoSYNPktDropRST_Type()
)
axNetStatEntryNoSYNPktDropRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryNoSYNPktDropRST.setStatus("current")


class _AxNetStatEntryNoSYNPktDropACK_Type(Counter32):
    """Custom type axNetStatEntryNoSYNPktDropACK based on Counter32"""
    defaultValue = 0


_AxNetStatEntryNoSYNPktDropACK_Object = MibTableColumn
axNetStatEntryNoSYNPktDropACK = _AxNetStatEntryNoSYNPktDropACK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 29),
    _AxNetStatEntryNoSYNPktDropACK_Type()
)
axNetStatEntryNoSYNPktDropACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryNoSYNPktDropACK.setStatus("current")


class _AxNetStatEntrySYNThrotte_Type(Counter32):
    """Custom type axNetStatEntrySYNThrotte based on Counter32"""
    defaultValue = 0


_AxNetStatEntrySYNThrotte_Object = MibTableColumn
axNetStatEntrySYNThrotte = _AxNetStatEntrySYNThrotte_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 30),
    _AxNetStatEntrySYNThrotte_Type()
)
axNetStatEntrySYNThrotte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntrySYNThrotte.setStatus("current")


class _AxNetStatEntrySSLSIDPersistSucc_Type(Counter32):
    """Custom type axNetStatEntrySSLSIDPersistSucc based on Counter32"""
    defaultValue = 0


_AxNetStatEntrySSLSIDPersistSucc_Object = MibTableColumn
axNetStatEntrySSLSIDPersistSucc = _AxNetStatEntrySSLSIDPersistSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 31),
    _AxNetStatEntrySSLSIDPersistSucc_Type()
)
axNetStatEntrySSLSIDPersistSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntrySSLSIDPersistSucc.setStatus("current")


class _AxNetStatEntrySSLSIDPersistFail_Type(Counter32):
    """Custom type axNetStatEntrySSLSIDPersistFail based on Counter32"""
    defaultValue = 0


_AxNetStatEntrySSLSIDPersistFail_Object = MibTableColumn
axNetStatEntrySSLSIDPersistFail = _AxNetStatEntrySSLSIDPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 32),
    _AxNetStatEntrySSLSIDPersistFail_Type()
)
axNetStatEntrySSLSIDPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntrySSLSIDPersistFail.setStatus("current")


class _AxNetStatEntryClientSSLSIDNotFound_Type(Counter32):
    """Custom type axNetStatEntryClientSSLSIDNotFound based on Counter32"""
    defaultValue = 0


_AxNetStatEntryClientSSLSIDNotFound_Object = MibTableColumn
axNetStatEntryClientSSLSIDNotFound = _AxNetStatEntryClientSSLSIDNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 33),
    _AxNetStatEntryClientSSLSIDNotFound_Type()
)
axNetStatEntryClientSSLSIDNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryClientSSLSIDNotFound.setStatus("current")


class _AxNetStatEntryClientSSLSIDMatch_Type(Counter32):
    """Custom type axNetStatEntryClientSSLSIDMatch based on Counter32"""
    defaultValue = 0


_AxNetStatEntryClientSSLSIDMatch_Object = MibTableColumn
axNetStatEntryClientSSLSIDMatch = _AxNetStatEntryClientSSLSIDMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 34),
    _AxNetStatEntryClientSSLSIDMatch_Type()
)
axNetStatEntryClientSSLSIDMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryClientSSLSIDMatch.setStatus("current")


class _AxNetStatEntryClientSSLSIDNotMatch_Type(Counter32):
    """Custom type axNetStatEntryClientSSLSIDNotMatch based on Counter32"""
    defaultValue = 0


_AxNetStatEntryClientSSLSIDNotMatch_Object = MibTableColumn
axNetStatEntryClientSSLSIDNotMatch = _AxNetStatEntryClientSSLSIDNotMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 35),
    _AxNetStatEntryClientSSLSIDNotMatch_Type()
)
axNetStatEntryClientSSLSIDNotMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryClientSSLSIDNotMatch.setStatus("current")


class _AxNetStatEntryServerSSLSIDNotFound_Type(Counter32):
    """Custom type axNetStatEntryServerSSLSIDNotFound based on Counter32"""
    defaultValue = 0


_AxNetStatEntryServerSSLSIDNotFound_Object = MibTableColumn
axNetStatEntryServerSSLSIDNotFound = _AxNetStatEntryServerSSLSIDNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 36),
    _AxNetStatEntryServerSSLSIDNotFound_Type()
)
axNetStatEntryServerSSLSIDNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryServerSSLSIDNotFound.setStatus("current")


class _AxNetStatEntryServerSSLSIDReset_Type(Counter32):
    """Custom type axNetStatEntryServerSSLSIDReset based on Counter32"""
    defaultValue = 0


_AxNetStatEntryServerSSLSIDReset_Object = MibTableColumn
axNetStatEntryServerSSLSIDReset = _AxNetStatEntryServerSSLSIDReset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 37),
    _AxNetStatEntryServerSSLSIDReset_Type()
)
axNetStatEntryServerSSLSIDReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryServerSSLSIDReset.setStatus("current")


class _AxNetStatEntryServerSSLSIDMatch_Type(Counter32):
    """Custom type axNetStatEntryServerSSLSIDMatch based on Counter32"""
    defaultValue = 0


_AxNetStatEntryServerSSLSIDMatch_Object = MibTableColumn
axNetStatEntryServerSSLSIDMatch = _AxNetStatEntryServerSSLSIDMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 38),
    _AxNetStatEntryServerSSLSIDMatch_Type()
)
axNetStatEntryServerSSLSIDMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryServerSSLSIDMatch.setStatus("current")


class _AxNetStatEntryServerSSLSIDNotMatch_Type(Counter32):
    """Custom type axNetStatEntryServerSSLSIDNotMatch based on Counter32"""
    defaultValue = 0


_AxNetStatEntryServerSSLSIDNotMatch_Object = MibTableColumn
axNetStatEntryServerSSLSIDNotMatch = _AxNetStatEntryServerSSLSIDNotMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 39),
    _AxNetStatEntryServerSSLSIDNotMatch_Type()
)
axNetStatEntryServerSSLSIDNotMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryServerSSLSIDNotMatch.setStatus("current")


class _AxNetStatEntryCreateSSLSIDSucc_Type(Counter32):
    """Custom type axNetStatEntryCreateSSLSIDSucc based on Counter32"""
    defaultValue = 0


_AxNetStatEntryCreateSSLSIDSucc_Object = MibTableColumn
axNetStatEntryCreateSSLSIDSucc = _AxNetStatEntryCreateSSLSIDSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 40),
    _AxNetStatEntryCreateSSLSIDSucc_Type()
)
axNetStatEntryCreateSSLSIDSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryCreateSSLSIDSucc.setStatus("current")


class _AxNetStatEntryCreateSSLSIDFail_Type(Counter32):
    """Custom type axNetStatEntryCreateSSLSIDFail based on Counter32"""
    defaultValue = 0


_AxNetStatEntryCreateSSLSIDFail_Object = MibTableColumn
axNetStatEntryCreateSSLSIDFail = _AxNetStatEntryCreateSSLSIDFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 41),
    _AxNetStatEntryCreateSSLSIDFail_Type()
)
axNetStatEntryCreateSSLSIDFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryCreateSSLSIDFail.setStatus("current")


class _AxNetStatEntryConnRateLimitDrops_Type(Counter32):
    """Custom type axNetStatEntryConnRateLimitDrops based on Counter32"""
    defaultValue = 0


_AxNetStatEntryConnRateLimitDrops_Object = MibTableColumn
axNetStatEntryConnRateLimitDrops = _AxNetStatEntryConnRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 42),
    _AxNetStatEntryConnRateLimitDrops_Type()
)
axNetStatEntryConnRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryConnRateLimitDrops.setStatus("current")


class _AxNetStatEntryConnRateLimitResets_Type(Counter32):
    """Custom type axNetStatEntryConnRateLimitResets based on Counter32"""
    defaultValue = 0


_AxNetStatEntryConnRateLimitResets_Object = MibTableColumn
axNetStatEntryConnRateLimitResets = _AxNetStatEntryConnRateLimitResets_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 43),
    _AxNetStatEntryConnRateLimitResets_Type()
)
axNetStatEntryConnRateLimitResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryConnRateLimitResets.setStatus("current")


class _AxNetStatEntryInbandHMRetry_Type(Counter32):
    """Custom type axNetStatEntryInbandHMRetry based on Counter32"""
    defaultValue = 0


_AxNetStatEntryInbandHMRetry_Object = MibTableColumn
axNetStatEntryInbandHMRetry = _AxNetStatEntryInbandHMRetry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 44),
    _AxNetStatEntryInbandHMRetry_Type()
)
axNetStatEntryInbandHMRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryInbandHMRetry.setStatus("current")


class _AxNetStatEntryInbandHMReassign_Type(Counter32):
    """Custom type axNetStatEntryInbandHMReassign based on Counter32"""
    defaultValue = 0


_AxNetStatEntryInbandHMReassign_Object = MibTableColumn
axNetStatEntryInbandHMReassign = _AxNetStatEntryInbandHMReassign_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 11, 100, 1, 45),
    _AxNetStatEntryInbandHMReassign_Type()
)
axNetStatEntryInbandHMReassign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNetStatEntryInbandHMReassign.setStatus("current")
_AxNotification_ObjectIdentity = ObjectIdentity
axNotification = _AxNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12)
)
_AxNotificationObjects_ObjectIdentity = ObjectIdentity
axNotificationObjects = _AxNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1)
)
_AxNotificationMsg_Type = DisplayString
_AxNotificationMsg_Object = MibScalar
axNotificationMsg = _AxNotificationMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 1),
    _AxNotificationMsg_Type()
)
axNotificationMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationMsg.setStatus("current")
_AxNotificationSLBServer_Type = DisplayString
_AxNotificationSLBServer_Object = MibScalar
axNotificationSLBServer = _AxNotificationSLBServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 2),
    _AxNotificationSLBServer_Type()
)
axNotificationSLBServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBServer.setStatus("current")
_AxNotificationSLBPort_Type = Integer32
_AxNotificationSLBPort_Object = MibScalar
axNotificationSLBPort = _AxNotificationSLBPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 3),
    _AxNotificationSLBPort_Type()
)
axNotificationSLBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBPort.setStatus("current")
_AxNotificationSLBCurConns_Type = Counter32
_AxNotificationSLBCurConns_Object = MibScalar
axNotificationSLBCurConns = _AxNotificationSLBCurConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 4),
    _AxNotificationSLBCurConns_Type()
)
axNotificationSLBCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationSLBCurConns.setStatus("current")
_AxNotificationVirtualServer_Type = DisplayString
_AxNotificationVirtualServer_Object = MibScalar
axNotificationVirtualServer = _AxNotificationVirtualServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 5),
    _AxNotificationVirtualServer_Type()
)
axNotificationVirtualServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServer.setStatus("current")
_AxNotificationVirtualServerPort_Type = Integer32
_AxNotificationVirtualServerPort_Object = MibScalar
axNotificationVirtualServerPort = _AxNotificationVirtualServerPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 6),
    _AxNotificationVirtualServerPort_Type()
)
axNotificationVirtualServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServerPort.setStatus("current")


class _AxNotificationVirtualServerPortType_Type(Integer32):
    """Custom type axNotificationVirtualServerPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fastHTTP", 12),
          ("firewall", 1),
          ("ftp", 9),
          ("http", 14),
          ("https", 15),
          ("mms", 10),
          ("others", 5),
          ("rtsp", 8),
          ("sip", 11),
          ("sip-TCP", 18),
          ("sips", 19),
          ("smtp", 17),
          ("sslProxy", 16),
          ("tcp", 2),
          ("udp", 3))
    )


_AxNotificationVirtualServerPortType_Type.__name__ = "Integer32"
_AxNotificationVirtualServerPortType_Object = MibScalar
axNotificationVirtualServerPortType = _AxNotificationVirtualServerPortType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 7),
    _AxNotificationVirtualServerPortType_Type()
)
axNotificationVirtualServerPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationVirtualServerPortType.setStatus("current")
_AxNotificationDropEventReason_Type = Integer32
_AxNotificationDropEventReason_Object = MibScalar
axNotificationDropEventReason = _AxNotificationDropEventReason_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 8),
    _AxNotificationDropEventReason_Type()
)
axNotificationDropEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationDropEventReason.setStatus("current")
_AxNotificationConfiguredThreshold_Type = Integer32
_AxNotificationConfiguredThreshold_Object = MibScalar
axNotificationConfiguredThreshold = _AxNotificationConfiguredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 9),
    _AxNotificationConfiguredThreshold_Type()
)
axNotificationConfiguredThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationConfiguredThreshold.setStatus("current")
_AxNotificationCurrentUsage_Type = Integer32
_AxNotificationCurrentUsage_Object = MibScalar
axNotificationCurrentUsage = _AxNotificationCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 10),
    _AxNotificationCurrentUsage_Type()
)
axNotificationCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationCurrentUsage.setStatus("current")
_AxNotificationConnLimit_Type = Integer32
_AxNotificationConnLimit_Object = MibScalar
axNotificationConnLimit = _AxNotificationConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 11),
    _AxNotificationConnLimit_Type()
)
axNotificationConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationConnLimit.setStatus("current")
_AxNotificationTrunkID_Type = Integer32
_AxNotificationTrunkID_Object = MibScalar
axNotificationTrunkID = _AxNotificationTrunkID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 12),
    _AxNotificationTrunkID_Type()
)
axNotificationTrunkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationTrunkID.setStatus("current")
_AxNotificationPortThreshold_Type = Integer32
_AxNotificationPortThreshold_Object = MibScalar
axNotificationPortThreshold = _AxNotificationPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 13),
    _AxNotificationPortThreshold_Type()
)
axNotificationPortThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPortThreshold.setStatus("current")
_AxNotificationCurrentUpPorts_Type = Integer32
_AxNotificationCurrentUpPorts_Object = MibScalar
axNotificationCurrentUpPorts = _AxNotificationCurrentUpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 14),
    _AxNotificationCurrentUpPorts_Type()
)
axNotificationCurrentUpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationCurrentUpPorts.setStatus("current")
_AxNotificationFanName_Type = DisplayString
_AxNotificationFanName_Object = MibScalar
axNotificationFanName = _AxNotificationFanName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 15),
    _AxNotificationFanName_Type()
)
axNotificationFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationFanName.setStatus("current")
_AxNotificationPowerSupplyName_Type = DisplayString
_AxNotificationPowerSupplyName_Object = MibScalar
axNotificationPowerSupplyName = _AxNotificationPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 1, 16),
    _AxNotificationPowerSupplyName_Type()
)
axNotificationPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNotificationPowerSupplyName.setStatus("current")
_AxNotifications_ObjectIdentity = ObjectIdentity
axNotifications = _AxNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2)
)
_AxSystemNotifications_ObjectIdentity = ObjectIdentity
axSystemNotifications = _AxSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1)
)
_AxAppNotifications_ObjectIdentity = ObjectIdentity
axAppNotifications = _AxAppNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2)
)
_AxNetworkNotifications_ObjectIdentity = ObjectIdentity
axNetworkNotifications = _AxNetworkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 3)
)
_AxSmtpProxyStats_ObjectIdentity = ObjectIdentity
axSmtpProxyStats = _AxSmtpProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13)
)


class _AxSmtpProxyStatsCurrProxyConns_Type(Integer32):
    """Custom type axSmtpProxyStatsCurrProxyConns based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsCurrProxyConns_Object = MibScalar
axSmtpProxyStatsCurrProxyConns = _AxSmtpProxyStatsCurrProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 1),
    _AxSmtpProxyStatsCurrProxyConns_Type()
)
axSmtpProxyStatsCurrProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsCurrProxyConns.setStatus("current")


class _AxSmtpProxyStatsTotalProxyConns_Type(Integer32):
    """Custom type axSmtpProxyStatsTotalProxyConns based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsTotalProxyConns_Object = MibScalar
axSmtpProxyStatsTotalProxyConns = _AxSmtpProxyStatsTotalProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 2),
    _AxSmtpProxyStatsTotalProxyConns_Type()
)
axSmtpProxyStatsTotalProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsTotalProxyConns.setStatus("current")


class _AxSmtpProxyStatsSmtpRequests_Type(Integer32):
    """Custom type axSmtpProxyStatsSmtpRequests based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsSmtpRequests_Object = MibScalar
axSmtpProxyStatsSmtpRequests = _AxSmtpProxyStatsSmtpRequests_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 3),
    _AxSmtpProxyStatsSmtpRequests_Type()
)
axSmtpProxyStatsSmtpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsSmtpRequests.setStatus("current")


class _AxSmtpProxyStatsSmtpReqSuccs_Type(Integer32):
    """Custom type axSmtpProxyStatsSmtpReqSuccs based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsSmtpReqSuccs_Object = MibScalar
axSmtpProxyStatsSmtpReqSuccs = _AxSmtpProxyStatsSmtpReqSuccs_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 4),
    _AxSmtpProxyStatsSmtpReqSuccs_Type()
)
axSmtpProxyStatsSmtpReqSuccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsSmtpReqSuccs.setStatus("current")


class _AxSmtpProxyStatsNoProxyError_Type(Integer32):
    """Custom type axSmtpProxyStatsNoProxyError based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsNoProxyError_Object = MibScalar
axSmtpProxyStatsNoProxyError = _AxSmtpProxyStatsNoProxyError_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 5),
    _AxSmtpProxyStatsNoProxyError_Type()
)
axSmtpProxyStatsNoProxyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsNoProxyError.setStatus("current")


class _AxSmtpProxyStatsClientRST_Type(Integer32):
    """Custom type axSmtpProxyStatsClientRST based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsClientRST_Object = MibScalar
axSmtpProxyStatsClientRST = _AxSmtpProxyStatsClientRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 6),
    _AxSmtpProxyStatsClientRST_Type()
)
axSmtpProxyStatsClientRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsClientRST.setStatus("current")


class _AxSmtpProxyStatsServerRST_Type(Integer32):
    """Custom type axSmtpProxyStatsServerRST based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsServerRST_Object = MibScalar
axSmtpProxyStatsServerRST = _AxSmtpProxyStatsServerRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 7),
    _AxSmtpProxyStatsServerRST_Type()
)
axSmtpProxyStatsServerRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsServerRST.setStatus("current")


class _AxSmtpProxyStatsNoTupleError_Type(Integer32):
    """Custom type axSmtpProxyStatsNoTupleError based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsNoTupleError_Object = MibScalar
axSmtpProxyStatsNoTupleError = _AxSmtpProxyStatsNoTupleError_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 8),
    _AxSmtpProxyStatsNoTupleError_Type()
)
axSmtpProxyStatsNoTupleError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsNoTupleError.setStatus("current")


class _AxSmtpProxyStatsParseReqFail_Type(Integer32):
    """Custom type axSmtpProxyStatsParseReqFail based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsParseReqFail_Object = MibScalar
axSmtpProxyStatsParseReqFail = _AxSmtpProxyStatsParseReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 9),
    _AxSmtpProxyStatsParseReqFail_Type()
)
axSmtpProxyStatsParseReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsParseReqFail.setStatus("current")


class _AxSmtpProxyStatsServerSelFail_Type(Integer32):
    """Custom type axSmtpProxyStatsServerSelFail based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsServerSelFail_Object = MibScalar
axSmtpProxyStatsServerSelFail = _AxSmtpProxyStatsServerSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 10),
    _AxSmtpProxyStatsServerSelFail_Type()
)
axSmtpProxyStatsServerSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsServerSelFail.setStatus("current")


class _AxSmtpProxyStatsFwdReqFail_Type(Integer32):
    """Custom type axSmtpProxyStatsFwdReqFail based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsFwdReqFail_Object = MibScalar
axSmtpProxyStatsFwdReqFail = _AxSmtpProxyStatsFwdReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 11),
    _AxSmtpProxyStatsFwdReqFail_Type()
)
axSmtpProxyStatsFwdReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsFwdReqFail.setStatus("current")


class _AxSmtpProxyStatsFwdReqDataFail_Type(Integer32):
    """Custom type axSmtpProxyStatsFwdReqDataFail based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsFwdReqDataFail_Object = MibScalar
axSmtpProxyStatsFwdReqDataFail = _AxSmtpProxyStatsFwdReqDataFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 12),
    _AxSmtpProxyStatsFwdReqDataFail_Type()
)
axSmtpProxyStatsFwdReqDataFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsFwdReqDataFail.setStatus("current")


class _AxSmtpProxyStatsReqRetrans_Type(Integer32):
    """Custom type axSmtpProxyStatsReqRetrans based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsReqRetrans_Object = MibScalar
axSmtpProxyStatsReqRetrans = _AxSmtpProxyStatsReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 13),
    _AxSmtpProxyStatsReqRetrans_Type()
)
axSmtpProxyStatsReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsReqRetrans.setStatus("current")


class _AxSmtpProxyStatsReqPktOutOrder_Type(Integer32):
    """Custom type axSmtpProxyStatsReqPktOutOrder based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsReqPktOutOrder_Object = MibScalar
axSmtpProxyStatsReqPktOutOrder = _AxSmtpProxyStatsReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 14),
    _AxSmtpProxyStatsReqPktOutOrder_Type()
)
axSmtpProxyStatsReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsReqPktOutOrder.setStatus("current")


class _AxSmtpProxyStatsServerResel_Type(Integer32):
    """Custom type axSmtpProxyStatsServerResel based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsServerResel_Object = MibScalar
axSmtpProxyStatsServerResel = _AxSmtpProxyStatsServerResel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 15),
    _AxSmtpProxyStatsServerResel_Type()
)
axSmtpProxyStatsServerResel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsServerResel.setStatus("current")


class _AxSmtpProxyStatsSvrPrematureClose_Type(Integer32):
    """Custom type axSmtpProxyStatsSvrPrematureClose based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsSvrPrematureClose_Object = MibScalar
axSmtpProxyStatsSvrPrematureClose = _AxSmtpProxyStatsSvrPrematureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 16),
    _AxSmtpProxyStatsSvrPrematureClose_Type()
)
axSmtpProxyStatsSvrPrematureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsSvrPrematureClose.setStatus("current")


class _AxSmtpProxyStatsSvrConnMade_Type(Integer32):
    """Custom type axSmtpProxyStatsSvrConnMade based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsSvrConnMade_Object = MibScalar
axSmtpProxyStatsSvrConnMade = _AxSmtpProxyStatsSvrConnMade_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 17),
    _AxSmtpProxyStatsSvrConnMade_Type()
)
axSmtpProxyStatsSvrConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsSvrConnMade.setStatus("current")


class _AxSmtpProxyStatsSNATFail_Type(Integer32):
    """Custom type axSmtpProxyStatsSNATFail based on Integer32"""
    defaultValue = 0


_AxSmtpProxyStatsSNATFail_Object = MibScalar
axSmtpProxyStatsSNATFail = _AxSmtpProxyStatsSNATFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 18),
    _AxSmtpProxyStatsSNATFail_Type()
)
axSmtpProxyStatsSNATFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatsSNATFail.setStatus("current")
_AxSmtpProxyStatTable_Object = MibTable
axSmtpProxyStatTable = _AxSmtpProxyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19)
)
if mibBuilder.loadTexts:
    axSmtpProxyStatTable.setStatus("current")
_AxSmtpProxyStatEntry_Object = MibTableRow
axSmtpProxyStatEntry = _AxSmtpProxyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1)
)
axSmtpProxyStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axSmtpProxyStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axSmtpProxyStatEntry.setStatus("current")
_AxSmtpProxyStatCpuIndex_Type = Integer32
_AxSmtpProxyStatCpuIndex_Object = MibTableColumn
axSmtpProxyStatCpuIndex = _AxSmtpProxyStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 1),
    _AxSmtpProxyStatCpuIndex_Type()
)
axSmtpProxyStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatCpuIndex.setStatus("current")


class _AxSmtpProxyStatCurrProxyConn_Type(Counter32):
    """Custom type axSmtpProxyStatCurrProxyConn based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatCurrProxyConn_Object = MibTableColumn
axSmtpProxyStatCurrProxyConn = _AxSmtpProxyStatCurrProxyConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 2),
    _AxSmtpProxyStatCurrProxyConn_Type()
)
axSmtpProxyStatCurrProxyConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatCurrProxyConn.setStatus("current")


class _AxSmtpProxyStatTotalProxyConn_Type(Counter32):
    """Custom type axSmtpProxyStatTotalProxyConn based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatTotalProxyConn_Object = MibTableColumn
axSmtpProxyStatTotalProxyConn = _AxSmtpProxyStatTotalProxyConn_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 3),
    _AxSmtpProxyStatTotalProxyConn_Type()
)
axSmtpProxyStatTotalProxyConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatTotalProxyConn.setStatus("current")


class _AxSmtpProxyStatSmtpReq_Type(Counter32):
    """Custom type axSmtpProxyStatSmtpReq based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatSmtpReq_Object = MibTableColumn
axSmtpProxyStatSmtpReq = _AxSmtpProxyStatSmtpReq_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 4),
    _AxSmtpProxyStatSmtpReq_Type()
)
axSmtpProxyStatSmtpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatSmtpReq.setStatus("current")


class _AxSmtpProxyStatSmtpReqSucc_Type(Counter32):
    """Custom type axSmtpProxyStatSmtpReqSucc based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatSmtpReqSucc_Object = MibTableColumn
axSmtpProxyStatSmtpReqSucc = _AxSmtpProxyStatSmtpReqSucc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 5),
    _AxSmtpProxyStatSmtpReqSucc_Type()
)
axSmtpProxyStatSmtpReqSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatSmtpReqSucc.setStatus("current")


class _AxSmtpProxyStatNoProxyError_Type(Counter32):
    """Custom type axSmtpProxyStatNoProxyError based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatNoProxyError_Object = MibTableColumn
axSmtpProxyStatNoProxyError = _AxSmtpProxyStatNoProxyError_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 6),
    _AxSmtpProxyStatNoProxyError_Type()
)
axSmtpProxyStatNoProxyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatNoProxyError.setStatus("current")


class _AxSmtpProxyStatClientRST_Type(Counter32):
    """Custom type axSmtpProxyStatClientRST based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatClientRST_Object = MibTableColumn
axSmtpProxyStatClientRST = _AxSmtpProxyStatClientRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 7),
    _AxSmtpProxyStatClientRST_Type()
)
axSmtpProxyStatClientRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatClientRST.setStatus("current")


class _AxSmtpProxyStatServerRST_Type(Counter32):
    """Custom type axSmtpProxyStatServerRST based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatServerRST_Object = MibTableColumn
axSmtpProxyStatServerRST = _AxSmtpProxyStatServerRST_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 8),
    _AxSmtpProxyStatServerRST_Type()
)
axSmtpProxyStatServerRST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatServerRST.setStatus("current")


class _AxSmtpProxyStatNoTupleError_Type(Counter32):
    """Custom type axSmtpProxyStatNoTupleError based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatNoTupleError_Object = MibTableColumn
axSmtpProxyStatNoTupleError = _AxSmtpProxyStatNoTupleError_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 9),
    _AxSmtpProxyStatNoTupleError_Type()
)
axSmtpProxyStatNoTupleError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatNoTupleError.setStatus("current")


class _AxSmtpProxyStatParseReqFail_Type(Counter32):
    """Custom type axSmtpProxyStatParseReqFail based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatParseReqFail_Object = MibTableColumn
axSmtpProxyStatParseReqFail = _AxSmtpProxyStatParseReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 10),
    _AxSmtpProxyStatParseReqFail_Type()
)
axSmtpProxyStatParseReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatParseReqFail.setStatus("current")


class _AxSmtpProxyStatServerSelFail_Type(Counter32):
    """Custom type axSmtpProxyStatServerSelFail based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatServerSelFail_Object = MibTableColumn
axSmtpProxyStatServerSelFail = _AxSmtpProxyStatServerSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 11),
    _AxSmtpProxyStatServerSelFail_Type()
)
axSmtpProxyStatServerSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatServerSelFail.setStatus("current")


class _AxSmtpProxyStatFwdReqFail_Type(Counter32):
    """Custom type axSmtpProxyStatFwdReqFail based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatFwdReqFail_Object = MibTableColumn
axSmtpProxyStatFwdReqFail = _AxSmtpProxyStatFwdReqFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 12),
    _AxSmtpProxyStatFwdReqFail_Type()
)
axSmtpProxyStatFwdReqFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatFwdReqFail.setStatus("current")


class _AxSmtpProxyStatFwdReqDataFail_Type(Counter32):
    """Custom type axSmtpProxyStatFwdReqDataFail based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatFwdReqDataFail_Object = MibTableColumn
axSmtpProxyStatFwdReqDataFail = _AxSmtpProxyStatFwdReqDataFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 13),
    _AxSmtpProxyStatFwdReqDataFail_Type()
)
axSmtpProxyStatFwdReqDataFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatFwdReqDataFail.setStatus("current")


class _AxSmtpProxyStatReqRetrans_Type(Counter32):
    """Custom type axSmtpProxyStatReqRetrans based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatReqRetrans_Object = MibTableColumn
axSmtpProxyStatReqRetrans = _AxSmtpProxyStatReqRetrans_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 14),
    _AxSmtpProxyStatReqRetrans_Type()
)
axSmtpProxyStatReqRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatReqRetrans.setStatus("current")


class _AxSmtpProxyStatReqPktOutOrder_Type(Counter32):
    """Custom type axSmtpProxyStatReqPktOutOrder based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatReqPktOutOrder_Object = MibTableColumn
axSmtpProxyStatReqPktOutOrder = _AxSmtpProxyStatReqPktOutOrder_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 15),
    _AxSmtpProxyStatReqPktOutOrder_Type()
)
axSmtpProxyStatReqPktOutOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatReqPktOutOrder.setStatus("current")


class _AxSmtpProxyStatServerResel_Type(Counter32):
    """Custom type axSmtpProxyStatServerResel based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatServerResel_Object = MibTableColumn
axSmtpProxyStatServerResel = _AxSmtpProxyStatServerResel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 16),
    _AxSmtpProxyStatServerResel_Type()
)
axSmtpProxyStatServerResel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatServerResel.setStatus("current")


class _AxSmtpProxyStatSvrPrematureClose_Type(Counter32):
    """Custom type axSmtpProxyStatSvrPrematureClose based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatSvrPrematureClose_Object = MibTableColumn
axSmtpProxyStatSvrPrematureClose = _AxSmtpProxyStatSvrPrematureClose_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 17),
    _AxSmtpProxyStatSvrPrematureClose_Type()
)
axSmtpProxyStatSvrPrematureClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatSvrPrematureClose.setStatus("current")


class _AxSmtpProxyStatSvrConnMade_Type(Counter32):
    """Custom type axSmtpProxyStatSvrConnMade based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatSvrConnMade_Object = MibTableColumn
axSmtpProxyStatSvrConnMade = _AxSmtpProxyStatSvrConnMade_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 18),
    _AxSmtpProxyStatSvrConnMade_Type()
)
axSmtpProxyStatSvrConnMade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatSvrConnMade.setStatus("current")


class _AxSmtpProxyStatSNATFail_Type(Counter32):
    """Custom type axSmtpProxyStatSNATFail based on Counter32"""
    defaultValue = 0


_AxSmtpProxyStatSNATFail_Object = MibTableColumn
axSmtpProxyStatSNATFail = _AxSmtpProxyStatSNATFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 13, 19, 1, 19),
    _AxSmtpProxyStatSNATFail_Type()
)
axSmtpProxyStatSNATFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmtpProxyStatSNATFail.setStatus("current")
_AxSslProxyStats_ObjectIdentity = ObjectIdentity
axSslProxyStats = _AxSslProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14)
)


class _AxSslProxyStatsCurrProxyConns_Type(Integer32):
    """Custom type axSslProxyStatsCurrProxyConns based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsCurrProxyConns_Object = MibScalar
axSslProxyStatsCurrProxyConns = _AxSslProxyStatsCurrProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 1),
    _AxSslProxyStatsCurrProxyConns_Type()
)
axSslProxyStatsCurrProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsCurrProxyConns.setStatus("current")


class _AxSslProxyStatsTotalProxyConns_Type(Integer32):
    """Custom type axSslProxyStatsTotalProxyConns based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsTotalProxyConns_Object = MibScalar
axSslProxyStatsTotalProxyConns = _AxSslProxyStatsTotalProxyConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 2),
    _AxSslProxyStatsTotalProxyConns_Type()
)
axSslProxyStatsTotalProxyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsTotalProxyConns.setStatus("current")


class _AxSslProxyStatsClientErr_Type(Integer32):
    """Custom type axSslProxyStatsClientErr based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsClientErr_Object = MibScalar
axSslProxyStatsClientErr = _AxSslProxyStatsClientErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 3),
    _AxSslProxyStatsClientErr_Type()
)
axSslProxyStatsClientErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsClientErr.setStatus("current")


class _AxSslProxyStatsServerErr_Type(Integer32):
    """Custom type axSslProxyStatsServerErr based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsServerErr_Object = MibScalar
axSslProxyStatsServerErr = _AxSslProxyStatsServerErr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 4),
    _AxSslProxyStatsServerErr_Type()
)
axSslProxyStatsServerErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsServerErr.setStatus("current")


class _AxSslProxyStatsSessNotFound_Type(Integer32):
    """Custom type axSslProxyStatsSessNotFound based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsSessNotFound_Object = MibScalar
axSslProxyStatsSessNotFound = _AxSslProxyStatsSessNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 5),
    _AxSslProxyStatsSessNotFound_Type()
)
axSslProxyStatsSessNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsSessNotFound.setStatus("current")


class _AxSslProxyStatsNoRoute_Type(Integer32):
    """Custom type axSslProxyStatsNoRoute based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsNoRoute_Object = MibScalar
axSslProxyStatsNoRoute = _AxSslProxyStatsNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 6),
    _AxSslProxyStatsNoRoute_Type()
)
axSslProxyStatsNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsNoRoute.setStatus("current")


class _AxSslProxyStatsSvrSelFail_Type(Integer32):
    """Custom type axSslProxyStatsSvrSelFail based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsSvrSelFail_Object = MibScalar
axSslProxyStatsSvrSelFail = _AxSslProxyStatsSvrSelFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 7),
    _AxSslProxyStatsSvrSelFail_Type()
)
axSslProxyStatsSvrSelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsSvrSelFail.setStatus("current")


class _AxSslProxyStatsSNATFail_Type(Integer32):
    """Custom type axSslProxyStatsSNATFail based on Integer32"""
    defaultValue = 0


_AxSslProxyStatsSNATFail_Object = MibScalar
axSslProxyStatsSNATFail = _AxSslProxyStatsSNATFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 14, 8),
    _AxSslProxyStatsSNATFail_Type()
)
axSslProxyStatsSNATFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSslProxyStatsSNATFail.setStatus("current")
_AxPersistentStats_ObjectIdentity = ObjectIdentity
axPersistentStats = _AxPersistentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15)
)


class _AxPersistentStatsUrlHashPersistOKPri_Type(Integer32):
    """Custom type axPersistentStatsUrlHashPersistOKPri based on Integer32"""
    defaultValue = 0


_AxPersistentStatsUrlHashPersistOKPri_Object = MibScalar
axPersistentStatsUrlHashPersistOKPri = _AxPersistentStatsUrlHashPersistOKPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 1),
    _AxPersistentStatsUrlHashPersistOKPri_Type()
)
axPersistentStatsUrlHashPersistOKPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsUrlHashPersistOKPri.setStatus("current")


class _AxPersistentStatsUrlHashPersistOKSec_Type(Integer32):
    """Custom type axPersistentStatsUrlHashPersistOKSec based on Integer32"""
    defaultValue = 0


_AxPersistentStatsUrlHashPersistOKSec_Object = MibScalar
axPersistentStatsUrlHashPersistOKSec = _AxPersistentStatsUrlHashPersistOKSec_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 2),
    _AxPersistentStatsUrlHashPersistOKSec_Type()
)
axPersistentStatsUrlHashPersistOKSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsUrlHashPersistOKSec.setStatus("current")


class _AxPersistentStatsUrlHashPersistFail_Type(Integer32):
    """Custom type axPersistentStatsUrlHashPersistFail based on Integer32"""
    defaultValue = 0


_AxPersistentStatsUrlHashPersistFail_Object = MibScalar
axPersistentStatsUrlHashPersistFail = _AxPersistentStatsUrlHashPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 3),
    _AxPersistentStatsUrlHashPersistFail_Type()
)
axPersistentStatsUrlHashPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsUrlHashPersistFail.setStatus("current")


class _AxPersistentStatsSIPPersistOK_Type(Integer32):
    """Custom type axPersistentStatsSIPPersistOK based on Integer32"""
    defaultValue = 0


_AxPersistentStatsSIPPersistOK_Object = MibScalar
axPersistentStatsSIPPersistOK = _AxPersistentStatsSIPPersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 4),
    _AxPersistentStatsSIPPersistOK_Type()
)
axPersistentStatsSIPPersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsSIPPersistOK.setStatus("current")


class _AxPersistentStatsSIPPersistFail_Type(Integer32):
    """Custom type axPersistentStatsSIPPersistFail based on Integer32"""
    defaultValue = 0


_AxPersistentStatsSIPPersistFail_Object = MibScalar
axPersistentStatsSIPPersistFail = _AxPersistentStatsSIPPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 5),
    _AxPersistentStatsSIPPersistFail_Type()
)
axPersistentStatsSIPPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsSIPPersistFail.setStatus("current")


class _AxPersistentStatsSSLSIDPersistOK_Type(Integer32):
    """Custom type axPersistentStatsSSLSIDPersistOK based on Integer32"""
    defaultValue = 0


_AxPersistentStatsSSLSIDPersistOK_Object = MibScalar
axPersistentStatsSSLSIDPersistOK = _AxPersistentStatsSSLSIDPersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 6),
    _AxPersistentStatsSSLSIDPersistOK_Type()
)
axPersistentStatsSSLSIDPersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsSSLSIDPersistOK.setStatus("current")


class _AxPersistentStatsSSLSIDPersistFail_Type(Integer32):
    """Custom type axPersistentStatsSSLSIDPersistFail based on Integer32"""
    defaultValue = 0


_AxPersistentStatsSSLSIDPersistFail_Object = MibScalar
axPersistentStatsSSLSIDPersistFail = _AxPersistentStatsSSLSIDPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 7),
    _AxPersistentStatsSSLSIDPersistFail_Type()
)
axPersistentStatsSSLSIDPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsSSLSIDPersistFail.setStatus("current")


class _AxPersistentStatsCookiePersistOK_Type(Integer32):
    """Custom type axPersistentStatsCookiePersistOK based on Integer32"""
    defaultValue = 0


_AxPersistentStatsCookiePersistOK_Object = MibScalar
axPersistentStatsCookiePersistOK = _AxPersistentStatsCookiePersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 8),
    _AxPersistentStatsCookiePersistOK_Type()
)
axPersistentStatsCookiePersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsCookiePersistOK.setStatus("current")


class _AxPersistentStatsCookiePersistFail_Type(Integer32):
    """Custom type axPersistentStatsCookiePersistFail based on Integer32"""
    defaultValue = 0


_AxPersistentStatsCookiePersistFail_Object = MibScalar
axPersistentStatsCookiePersistFail = _AxPersistentStatsCookiePersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 9),
    _AxPersistentStatsCookiePersistFail_Type()
)
axPersistentStatsCookiePersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsCookiePersistFail.setStatus("current")


class _AxPersistentStatsPersistCookieNotFound_Type(Integer32):
    """Custom type axPersistentStatsPersistCookieNotFound based on Integer32"""
    defaultValue = 0


_AxPersistentStatsPersistCookieNotFound_Object = MibScalar
axPersistentStatsPersistCookieNotFound = _AxPersistentStatsPersistCookieNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 10),
    _AxPersistentStatsPersistCookieNotFound_Type()
)
axPersistentStatsPersistCookieNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatsPersistCookieNotFound.setStatus("current")
_AxPersistentStatTable_Object = MibTable
axPersistentStatTable = _AxPersistentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11)
)
if mibBuilder.loadTexts:
    axPersistentStatTable.setStatus("current")
_AxPersistentStatEntry_Object = MibTableRow
axPersistentStatEntry = _AxPersistentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1)
)
axPersistentStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axPersistentStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axPersistentStatEntry.setStatus("current")
_AxPersistentStatCpuIndex_Type = Integer32
_AxPersistentStatCpuIndex_Object = MibTableColumn
axPersistentStatCpuIndex = _AxPersistentStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 1),
    _AxPersistentStatCpuIndex_Type()
)
axPersistentStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatCpuIndex.setStatus("current")


class _AxPersistentStatUrlHashPersistOKPri_Type(Counter32):
    """Custom type axPersistentStatUrlHashPersistOKPri based on Counter32"""
    defaultValue = 0


_AxPersistentStatUrlHashPersistOKPri_Object = MibTableColumn
axPersistentStatUrlHashPersistOKPri = _AxPersistentStatUrlHashPersistOKPri_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 2),
    _AxPersistentStatUrlHashPersistOKPri_Type()
)
axPersistentStatUrlHashPersistOKPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatUrlHashPersistOKPri.setStatus("current")


class _AxPersistentStatUrlHashPersistOKSec_Type(Counter32):
    """Custom type axPersistentStatUrlHashPersistOKSec based on Counter32"""
    defaultValue = 0


_AxPersistentStatUrlHashPersistOKSec_Object = MibTableColumn
axPersistentStatUrlHashPersistOKSec = _AxPersistentStatUrlHashPersistOKSec_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 3),
    _AxPersistentStatUrlHashPersistOKSec_Type()
)
axPersistentStatUrlHashPersistOKSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatUrlHashPersistOKSec.setStatus("current")


class _AxPersistentStatUrlHashPersistFail_Type(Counter32):
    """Custom type axPersistentStatUrlHashPersistFail based on Counter32"""
    defaultValue = 0


_AxPersistentStatUrlHashPersistFail_Object = MibTableColumn
axPersistentStatUrlHashPersistFail = _AxPersistentStatUrlHashPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 4),
    _AxPersistentStatUrlHashPersistFail_Type()
)
axPersistentStatUrlHashPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatUrlHashPersistFail.setStatus("current")


class _AxPersistentStatSIPPersistOK_Type(Counter32):
    """Custom type axPersistentStatSIPPersistOK based on Counter32"""
    defaultValue = 0


_AxPersistentStatSIPPersistOK_Object = MibTableColumn
axPersistentStatSIPPersistOK = _AxPersistentStatSIPPersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 5),
    _AxPersistentStatSIPPersistOK_Type()
)
axPersistentStatSIPPersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatSIPPersistOK.setStatus("current")


class _AxPersistentStatSIPPersistFail_Type(Counter32):
    """Custom type axPersistentStatSIPPersistFail based on Counter32"""
    defaultValue = 0


_AxPersistentStatSIPPersistFail_Object = MibTableColumn
axPersistentStatSIPPersistFail = _AxPersistentStatSIPPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 6),
    _AxPersistentStatSIPPersistFail_Type()
)
axPersistentStatSIPPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatSIPPersistFail.setStatus("current")


class _AxPersistentStatSSLSIDPersistOK_Type(Counter32):
    """Custom type axPersistentStatSSLSIDPersistOK based on Counter32"""
    defaultValue = 0


_AxPersistentStatSSLSIDPersistOK_Object = MibTableColumn
axPersistentStatSSLSIDPersistOK = _AxPersistentStatSSLSIDPersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 7),
    _AxPersistentStatSSLSIDPersistOK_Type()
)
axPersistentStatSSLSIDPersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatSSLSIDPersistOK.setStatus("current")


class _AxPersistentStatSSLSIDPersistFail_Type(Counter32):
    """Custom type axPersistentStatSSLSIDPersistFail based on Counter32"""
    defaultValue = 0


_AxPersistentStatSSLSIDPersistFail_Object = MibTableColumn
axPersistentStatSSLSIDPersistFail = _AxPersistentStatSSLSIDPersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 8),
    _AxPersistentStatSSLSIDPersistFail_Type()
)
axPersistentStatSSLSIDPersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatSSLSIDPersistFail.setStatus("current")


class _AxPersistentStatCookiePersistOK_Type(Counter32):
    """Custom type axPersistentStatCookiePersistOK based on Counter32"""
    defaultValue = 0


_AxPersistentStatCookiePersistOK_Object = MibTableColumn
axPersistentStatCookiePersistOK = _AxPersistentStatCookiePersistOK_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 9),
    _AxPersistentStatCookiePersistOK_Type()
)
axPersistentStatCookiePersistOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatCookiePersistOK.setStatus("current")


class _AxPersistentStatCookiePersistFail_Type(Counter32):
    """Custom type axPersistentStatCookiePersistFail based on Counter32"""
    defaultValue = 0


_AxPersistentStatCookiePersistFail_Object = MibTableColumn
axPersistentStatCookiePersistFail = _AxPersistentStatCookiePersistFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 10),
    _AxPersistentStatCookiePersistFail_Type()
)
axPersistentStatCookiePersistFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatCookiePersistFail.setStatus("current")


class _AxPersistentStatPersistCookieNotFound_Type(Counter32):
    """Custom type axPersistentStatPersistCookieNotFound based on Counter32"""
    defaultValue = 0


_AxPersistentStatPersistCookieNotFound_Object = MibTableColumn
axPersistentStatPersistCookieNotFound = _AxPersistentStatPersistCookieNotFound_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 15, 11, 1, 11),
    _AxPersistentStatPersistCookieNotFound_Type()
)
axPersistentStatPersistCookieNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPersistentStatPersistCookieNotFound.setStatus("current")
_AxSwitchStats_ObjectIdentity = ObjectIdentity
axSwitchStats = _AxSwitchStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16)
)


class _AxSwitchStatsL2Forward_Type(Integer32):
    """Custom type axSwitchStatsL2Forward based on Integer32"""
    defaultValue = 0


_AxSwitchStatsL2Forward_Object = MibScalar
axSwitchStatsL2Forward = _AxSwitchStatsL2Forward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 1),
    _AxSwitchStatsL2Forward_Type()
)
axSwitchStatsL2Forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsL2Forward.setStatus("current")


class _AxSwitchStatsL3IPForward_Type(Integer32):
    """Custom type axSwitchStatsL3IPForward based on Integer32"""
    defaultValue = 0


_AxSwitchStatsL3IPForward_Object = MibScalar
axSwitchStatsL3IPForward = _AxSwitchStatsL3IPForward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 2),
    _AxSwitchStatsL3IPForward_Type()
)
axSwitchStatsL3IPForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsL3IPForward.setStatus("current")


class _AxSwitchStatsIPv4NoRouteDrop_Type(Integer32):
    """Custom type axSwitchStatsIPv4NoRouteDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPv4NoRouteDrop_Object = MibScalar
axSwitchStatsIPv4NoRouteDrop = _AxSwitchStatsIPv4NoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 3),
    _AxSwitchStatsIPv4NoRouteDrop_Type()
)
axSwitchStatsIPv4NoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPv4NoRouteDrop.setStatus("current")


class _AxSwitchStatsL3IPv6Forward_Type(Integer32):
    """Custom type axSwitchStatsL3IPv6Forward based on Integer32"""
    defaultValue = 0


_AxSwitchStatsL3IPv6Forward_Object = MibScalar
axSwitchStatsL3IPv6Forward = _AxSwitchStatsL3IPv6Forward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 4),
    _AxSwitchStatsL3IPv6Forward_Type()
)
axSwitchStatsL3IPv6Forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsL3IPv6Forward.setStatus("current")


class _AxSwitchStatsIPv6NoRouteDrop_Type(Integer32):
    """Custom type axSwitchStatsIPv6NoRouteDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPv6NoRouteDrop_Object = MibScalar
axSwitchStatsIPv6NoRouteDrop = _AxSwitchStatsIPv6NoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 5),
    _AxSwitchStatsIPv6NoRouteDrop_Type()
)
axSwitchStatsIPv6NoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPv6NoRouteDrop.setStatus("current")


class _AxSwitchStatsL4Process_Type(Integer32):
    """Custom type axSwitchStatsL4Process based on Integer32"""
    defaultValue = 0


_AxSwitchStatsL4Process_Object = MibScalar
axSwitchStatsL4Process = _AxSwitchStatsL4Process_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 6),
    _AxSwitchStatsL4Process_Type()
)
axSwitchStatsL4Process.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsL4Process.setStatus("current")


class _AxSwitchStatsIncorrectLenDrop_Type(Integer32):
    """Custom type axSwitchStatsIncorrectLenDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIncorrectLenDrop_Object = MibScalar
axSwitchStatsIncorrectLenDrop = _AxSwitchStatsIncorrectLenDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 7),
    _AxSwitchStatsIncorrectLenDrop_Type()
)
axSwitchStatsIncorrectLenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIncorrectLenDrop.setStatus("current")


class _AxSwitchStatsProtoDownDrop_Type(Integer32):
    """Custom type axSwitchStatsProtoDownDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsProtoDownDrop_Object = MibScalar
axSwitchStatsProtoDownDrop = _AxSwitchStatsProtoDownDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 8),
    _AxSwitchStatsProtoDownDrop_Type()
)
axSwitchStatsProtoDownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsProtoDownDrop.setStatus("current")


class _AxSwitchStatsUnknownProtoDrop_Type(Integer32):
    """Custom type axSwitchStatsUnknownProtoDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsUnknownProtoDrop_Object = MibScalar
axSwitchStatsUnknownProtoDrop = _AxSwitchStatsUnknownProtoDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 9),
    _AxSwitchStatsUnknownProtoDrop_Type()
)
axSwitchStatsUnknownProtoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsUnknownProtoDrop.setStatus("current")


class _AxSwitchStatsTTLExceedDrop_Type(Integer32):
    """Custom type axSwitchStatsTTLExceedDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsTTLExceedDrop_Object = MibScalar
axSwitchStatsTTLExceedDrop = _AxSwitchStatsTTLExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 10),
    _AxSwitchStatsTTLExceedDrop_Type()
)
axSwitchStatsTTLExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsTTLExceedDrop.setStatus("current")


class _AxSwitchStatsLinkdownDrop_Type(Integer32):
    """Custom type axSwitchStatsLinkdownDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsLinkdownDrop_Object = MibScalar
axSwitchStatsLinkdownDrop = _AxSwitchStatsLinkdownDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 11),
    _AxSwitchStatsLinkdownDrop_Type()
)
axSwitchStatsLinkdownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsLinkdownDrop.setStatus("current")


class _AxSwitchStatsSRCPortSuppress_Type(Integer32):
    """Custom type axSwitchStatsSRCPortSuppress based on Integer32"""
    defaultValue = 0


_AxSwitchStatsSRCPortSuppress_Object = MibScalar
axSwitchStatsSRCPortSuppress = _AxSwitchStatsSRCPortSuppress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 12),
    _AxSwitchStatsSRCPortSuppress_Type()
)
axSwitchStatsSRCPortSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsSRCPortSuppress.setStatus("current")


class _AxSwitchStatsVLANFlood_Type(Integer32):
    """Custom type axSwitchStatsVLANFlood based on Integer32"""
    defaultValue = 0


_AxSwitchStatsVLANFlood_Object = MibScalar
axSwitchStatsVLANFlood = _AxSwitchStatsVLANFlood_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 13),
    _AxSwitchStatsVLANFlood_Type()
)
axSwitchStatsVLANFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsVLANFlood.setStatus("current")


class _AxSwitchStatsIPFragRcv_Type(Integer32):
    """Custom type axSwitchStatsIPFragRcv based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPFragRcv_Object = MibScalar
axSwitchStatsIPFragRcv = _AxSwitchStatsIPFragRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 14),
    _AxSwitchStatsIPFragRcv_Type()
)
axSwitchStatsIPFragRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPFragRcv.setStatus("current")


class _AxSwitchStatsARPReqRcv_Type(Integer32):
    """Custom type axSwitchStatsARPReqRcv based on Integer32"""
    defaultValue = 0


_AxSwitchStatsARPReqRcv_Object = MibScalar
axSwitchStatsARPReqRcv = _AxSwitchStatsARPReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 15),
    _AxSwitchStatsARPReqRcv_Type()
)
axSwitchStatsARPReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsARPReqRcv.setStatus("current")


class _AxSwitchStatsARPRespRcv_Type(Integer32):
    """Custom type axSwitchStatsARPRespRcv based on Integer32"""
    defaultValue = 0


_AxSwitchStatsARPRespRcv_Object = MibScalar
axSwitchStatsARPRespRcv = _AxSwitchStatsARPRespRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 16),
    _AxSwitchStatsARPRespRcv_Type()
)
axSwitchStatsARPRespRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsARPRespRcv.setStatus("current")


class _AxSwitchStatsFwdKernel_Type(Integer32):
    """Custom type axSwitchStatsFwdKernel based on Integer32"""
    defaultValue = 0


_AxSwitchStatsFwdKernel_Object = MibScalar
axSwitchStatsFwdKernel = _AxSwitchStatsFwdKernel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 17),
    _AxSwitchStatsFwdKernel_Type()
)
axSwitchStatsFwdKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsFwdKernel.setStatus("current")


class _AxSwitchStatsIPTCPFragRcv_Type(Integer32):
    """Custom type axSwitchStatsIPTCPFragRcv based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPTCPFragRcv_Object = MibScalar
axSwitchStatsIPTCPFragRcv = _AxSwitchStatsIPTCPFragRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 18),
    _AxSwitchStatsIPTCPFragRcv_Type()
)
axSwitchStatsIPTCPFragRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPTCPFragRcv.setStatus("current")


class _AxSwitchStatsIPFragOverlap_Type(Integer32):
    """Custom type axSwitchStatsIPFragOverlap based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPFragOverlap_Object = MibScalar
axSwitchStatsIPFragOverlap = _AxSwitchStatsIPFragOverlap_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 19),
    _AxSwitchStatsIPFragOverlap_Type()
)
axSwitchStatsIPFragOverlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPFragOverlap.setStatus("current")


class _AxSwitchStatsIPFragOverlapDrop_Type(Integer32):
    """Custom type axSwitchStatsIPFragOverlapDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPFragOverlapDrop_Object = MibScalar
axSwitchStatsIPFragOverlapDrop = _AxSwitchStatsIPFragOverlapDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 20),
    _AxSwitchStatsIPFragOverlapDrop_Type()
)
axSwitchStatsIPFragOverlapDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPFragOverlapDrop.setStatus("current")


class _AxSwitchStatsIPFragReasmOk_Type(Integer32):
    """Custom type axSwitchStatsIPFragReasmOk based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPFragReasmOk_Object = MibScalar
axSwitchStatsIPFragReasmOk = _AxSwitchStatsIPFragReasmOk_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 21),
    _AxSwitchStatsIPFragReasmOk_Type()
)
axSwitchStatsIPFragReasmOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPFragReasmOk.setStatus("current")


class _AxSwitchStatsIPFragReasmFail_Type(Integer32):
    """Custom type axSwitchStatsIPFragReasmFail based on Integer32"""
    defaultValue = 0


_AxSwitchStatsIPFragReasmFail_Object = MibScalar
axSwitchStatsIPFragReasmFail = _AxSwitchStatsIPFragReasmFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 22),
    _AxSwitchStatsIPFragReasmFail_Type()
)
axSwitchStatsIPFragReasmFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsIPFragReasmFail.setStatus("current")


class _AxSwitchStatsAnomLanAttackDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomLanAttackDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomLanAttackDrop_Object = MibScalar
axSwitchStatsAnomLanAttackDrop = _AxSwitchStatsAnomLanAttackDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 23),
    _AxSwitchStatsAnomLanAttackDrop_Type()
)
axSwitchStatsAnomLanAttackDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomLanAttackDrop.setStatus("current")


class _AxSwitchStatsAnomIPOptionDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomIPOptionDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomIPOptionDrop_Object = MibScalar
axSwitchStatsAnomIPOptionDrop = _AxSwitchStatsAnomIPOptionDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 24),
    _AxSwitchStatsAnomIPOptionDrop_Type()
)
axSwitchStatsAnomIPOptionDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomIPOptionDrop.setStatus("current")


class _AxSwitchStatsAnomPingDeathDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomPingDeathDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomPingDeathDrop_Object = MibScalar
axSwitchStatsAnomPingDeathDrop = _AxSwitchStatsAnomPingDeathDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 25),
    _AxSwitchStatsAnomPingDeathDrop_Type()
)
axSwitchStatsAnomPingDeathDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomPingDeathDrop.setStatus("current")


class _AxSwitchStatsAnomAllFragDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomAllFragDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomAllFragDrop_Object = MibScalar
axSwitchStatsAnomAllFragDrop = _AxSwitchStatsAnomAllFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 26),
    _AxSwitchStatsAnomAllFragDrop_Type()
)
axSwitchStatsAnomAllFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomAllFragDrop.setStatus("current")


class _AxSwitchStatsAnomTCPNoFragDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomTCPNoFragDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomTCPNoFragDrop_Object = MibScalar
axSwitchStatsAnomTCPNoFragDrop = _AxSwitchStatsAnomTCPNoFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 27),
    _AxSwitchStatsAnomTCPNoFragDrop_Type()
)
axSwitchStatsAnomTCPNoFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomTCPNoFragDrop.setStatus("current")


class _AxSwitchStatsAnomSYNFragDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomSYNFragDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomSYNFragDrop_Object = MibScalar
axSwitchStatsAnomSYNFragDrop = _AxSwitchStatsAnomSYNFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 28),
    _AxSwitchStatsAnomSYNFragDrop_Type()
)
axSwitchStatsAnomSYNFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomSYNFragDrop.setStatus("current")


class _AxSwitchStatsAnomTCPSynFinDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomTCPSynFinDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomTCPSynFinDrop_Object = MibScalar
axSwitchStatsAnomTCPSynFinDrop = _AxSwitchStatsAnomTCPSynFinDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 29),
    _AxSwitchStatsAnomTCPSynFinDrop_Type()
)
axSwitchStatsAnomTCPSynFinDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomTCPSynFinDrop.setStatus("current")


class _AxSwitchStatsAnomAnyDrop_Type(Integer32):
    """Custom type axSwitchStatsAnomAnyDrop based on Integer32"""
    defaultValue = 0


_AxSwitchStatsAnomAnyDrop_Object = MibScalar
axSwitchStatsAnomAnyDrop = _AxSwitchStatsAnomAnyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 30),
    _AxSwitchStatsAnomAnyDrop_Type()
)
axSwitchStatsAnomAnyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatsAnomAnyDrop.setStatus("current")
_AxSwitchStatTable_Object = MibTable
axSwitchStatTable = _AxSwitchStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31)
)
if mibBuilder.loadTexts:
    axSwitchStatTable.setStatus("current")
_AxSwitchStatEntry_Object = MibTableRow
axSwitchStatEntry = _AxSwitchStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1)
)
axSwitchStatEntry.setIndexNames(
    (0, "A10-AX-MIB", "axSwitchStatCpuIndex"),
)
if mibBuilder.loadTexts:
    axSwitchStatEntry.setStatus("current")
_AxSwitchStatCpuIndex_Type = Integer32
_AxSwitchStatCpuIndex_Object = MibTableColumn
axSwitchStatCpuIndex = _AxSwitchStatCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 1),
    _AxSwitchStatCpuIndex_Type()
)
axSwitchStatCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatCpuIndex.setStatus("current")


class _AxSwitchStatL2Forward_Type(Counter32):
    """Custom type axSwitchStatL2Forward based on Counter32"""
    defaultValue = 0


_AxSwitchStatL2Forward_Object = MibTableColumn
axSwitchStatL2Forward = _AxSwitchStatL2Forward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 2),
    _AxSwitchStatL2Forward_Type()
)
axSwitchStatL2Forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatL2Forward.setStatus("current")


class _AxSwitchStatL3IPForward_Type(Counter32):
    """Custom type axSwitchStatL3IPForward based on Counter32"""
    defaultValue = 0


_AxSwitchStatL3IPForward_Object = MibTableColumn
axSwitchStatL3IPForward = _AxSwitchStatL3IPForward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 3),
    _AxSwitchStatL3IPForward_Type()
)
axSwitchStatL3IPForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatL3IPForward.setStatus("current")


class _AxSwitchStatIPv4NoRouteDrop_Type(Counter32):
    """Custom type axSwitchStatIPv4NoRouteDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPv4NoRouteDrop_Object = MibTableColumn
axSwitchStatIPv4NoRouteDrop = _AxSwitchStatIPv4NoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 4),
    _AxSwitchStatIPv4NoRouteDrop_Type()
)
axSwitchStatIPv4NoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPv4NoRouteDrop.setStatus("current")


class _AxSwitchStatL3IPv6Forward_Type(Counter32):
    """Custom type axSwitchStatL3IPv6Forward based on Counter32"""
    defaultValue = 0


_AxSwitchStatL3IPv6Forward_Object = MibTableColumn
axSwitchStatL3IPv6Forward = _AxSwitchStatL3IPv6Forward_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 5),
    _AxSwitchStatL3IPv6Forward_Type()
)
axSwitchStatL3IPv6Forward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatL3IPv6Forward.setStatus("current")


class _AxSwitchStatIPv6NoRouteDrop_Type(Counter32):
    """Custom type axSwitchStatIPv6NoRouteDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPv6NoRouteDrop_Object = MibTableColumn
axSwitchStatIPv6NoRouteDrop = _AxSwitchStatIPv6NoRouteDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 6),
    _AxSwitchStatIPv6NoRouteDrop_Type()
)
axSwitchStatIPv6NoRouteDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPv6NoRouteDrop.setStatus("current")


class _AxSwitchStatL4Process_Type(Counter32):
    """Custom type axSwitchStatL4Process based on Counter32"""
    defaultValue = 0


_AxSwitchStatL4Process_Object = MibTableColumn
axSwitchStatL4Process = _AxSwitchStatL4Process_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 7),
    _AxSwitchStatL4Process_Type()
)
axSwitchStatL4Process.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatL4Process.setStatus("current")


class _AxSwitchStatIncorrectLenDrop_Type(Counter32):
    """Custom type axSwitchStatIncorrectLenDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatIncorrectLenDrop_Object = MibTableColumn
axSwitchStatIncorrectLenDrop = _AxSwitchStatIncorrectLenDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 8),
    _AxSwitchStatIncorrectLenDrop_Type()
)
axSwitchStatIncorrectLenDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIncorrectLenDrop.setStatus("current")


class _AxSwitchStatProtoDownDrop_Type(Counter32):
    """Custom type axSwitchStatProtoDownDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatProtoDownDrop_Object = MibTableColumn
axSwitchStatProtoDownDrop = _AxSwitchStatProtoDownDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 9),
    _AxSwitchStatProtoDownDrop_Type()
)
axSwitchStatProtoDownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatProtoDownDrop.setStatus("current")


class _AxSwitchStatUnknownProtoDrop_Type(Counter32):
    """Custom type axSwitchStatUnknownProtoDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatUnknownProtoDrop_Object = MibTableColumn
axSwitchStatUnknownProtoDrop = _AxSwitchStatUnknownProtoDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 10),
    _AxSwitchStatUnknownProtoDrop_Type()
)
axSwitchStatUnknownProtoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatUnknownProtoDrop.setStatus("current")


class _AxSwitchStatTTLExceedDrop_Type(Counter32):
    """Custom type axSwitchStatTTLExceedDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatTTLExceedDrop_Object = MibTableColumn
axSwitchStatTTLExceedDrop = _AxSwitchStatTTLExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 11),
    _AxSwitchStatTTLExceedDrop_Type()
)
axSwitchStatTTLExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatTTLExceedDrop.setStatus("current")


class _AxSwitchStatLinkdownDrop_Type(Counter32):
    """Custom type axSwitchStatLinkdownDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatLinkdownDrop_Object = MibTableColumn
axSwitchStatLinkdownDrop = _AxSwitchStatLinkdownDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 12),
    _AxSwitchStatLinkdownDrop_Type()
)
axSwitchStatLinkdownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatLinkdownDrop.setStatus("current")


class _AxSwitchStatSRCPortSuppress_Type(Counter32):
    """Custom type axSwitchStatSRCPortSuppress based on Counter32"""
    defaultValue = 0


_AxSwitchStatSRCPortSuppress_Object = MibTableColumn
axSwitchStatSRCPortSuppress = _AxSwitchStatSRCPortSuppress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 13),
    _AxSwitchStatSRCPortSuppress_Type()
)
axSwitchStatSRCPortSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatSRCPortSuppress.setStatus("current")


class _AxSwitchStatVLANFlood_Type(Counter32):
    """Custom type axSwitchStatVLANFlood based on Counter32"""
    defaultValue = 0


_AxSwitchStatVLANFlood_Object = MibTableColumn
axSwitchStatVLANFlood = _AxSwitchStatVLANFlood_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 14),
    _AxSwitchStatVLANFlood_Type()
)
axSwitchStatVLANFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatVLANFlood.setStatus("current")


class _AxSwitchStatIPFragRcv_Type(Counter32):
    """Custom type axSwitchStatIPFragRcv based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPFragRcv_Object = MibTableColumn
axSwitchStatIPFragRcv = _AxSwitchStatIPFragRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 15),
    _AxSwitchStatIPFragRcv_Type()
)
axSwitchStatIPFragRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPFragRcv.setStatus("current")


class _AxSwitchStatARPReqRcv_Type(Counter32):
    """Custom type axSwitchStatARPReqRcv based on Counter32"""
    defaultValue = 0


_AxSwitchStatARPReqRcv_Object = MibTableColumn
axSwitchStatARPReqRcv = _AxSwitchStatARPReqRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 16),
    _AxSwitchStatARPReqRcv_Type()
)
axSwitchStatARPReqRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatARPReqRcv.setStatus("current")


class _AxSwitchStatARPRespRcv_Type(Counter32):
    """Custom type axSwitchStatARPRespRcv based on Counter32"""
    defaultValue = 0


_AxSwitchStatARPRespRcv_Object = MibTableColumn
axSwitchStatARPRespRcv = _AxSwitchStatARPRespRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 17),
    _AxSwitchStatARPRespRcv_Type()
)
axSwitchStatARPRespRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatARPRespRcv.setStatus("current")


class _AxSwitchStatFwdKernel_Type(Counter32):
    """Custom type axSwitchStatFwdKernel based on Counter32"""
    defaultValue = 0


_AxSwitchStatFwdKernel_Object = MibTableColumn
axSwitchStatFwdKernel = _AxSwitchStatFwdKernel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 18),
    _AxSwitchStatFwdKernel_Type()
)
axSwitchStatFwdKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatFwdKernel.setStatus("current")


class _AxSwitchStatIPTCPFragRcv_Type(Counter32):
    """Custom type axSwitchStatIPTCPFragRcv based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPTCPFragRcv_Object = MibTableColumn
axSwitchStatIPTCPFragRcv = _AxSwitchStatIPTCPFragRcv_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 19),
    _AxSwitchStatIPTCPFragRcv_Type()
)
axSwitchStatIPTCPFragRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPTCPFragRcv.setStatus("current")


class _AxSwitchStatIPFragOverlap_Type(Counter32):
    """Custom type axSwitchStatIPFragOverlap based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPFragOverlap_Object = MibTableColumn
axSwitchStatIPFragOverlap = _AxSwitchStatIPFragOverlap_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 20),
    _AxSwitchStatIPFragOverlap_Type()
)
axSwitchStatIPFragOverlap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPFragOverlap.setStatus("current")


class _AxSwitchStatIPFragOverlapDrop_Type(Counter32):
    """Custom type axSwitchStatIPFragOverlapDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPFragOverlapDrop_Object = MibTableColumn
axSwitchStatIPFragOverlapDrop = _AxSwitchStatIPFragOverlapDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 21),
    _AxSwitchStatIPFragOverlapDrop_Type()
)
axSwitchStatIPFragOverlapDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPFragOverlapDrop.setStatus("current")


class _AxSwitchStatIPFragReasmOk_Type(Counter32):
    """Custom type axSwitchStatIPFragReasmOk based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPFragReasmOk_Object = MibTableColumn
axSwitchStatIPFragReasmOk = _AxSwitchStatIPFragReasmOk_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 22),
    _AxSwitchStatIPFragReasmOk_Type()
)
axSwitchStatIPFragReasmOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPFragReasmOk.setStatus("current")


class _AxSwitchStatIPFragReasmFail_Type(Counter32):
    """Custom type axSwitchStatIPFragReasmFail based on Counter32"""
    defaultValue = 0


_AxSwitchStatIPFragReasmFail_Object = MibTableColumn
axSwitchStatIPFragReasmFail = _AxSwitchStatIPFragReasmFail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 23),
    _AxSwitchStatIPFragReasmFail_Type()
)
axSwitchStatIPFragReasmFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatIPFragReasmFail.setStatus("current")


class _AxSwitchStatAnomLanAttackDrop_Type(Counter32):
    """Custom type axSwitchStatAnomLanAttackDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomLanAttackDrop_Object = MibTableColumn
axSwitchStatAnomLanAttackDrop = _AxSwitchStatAnomLanAttackDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 24),
    _AxSwitchStatAnomLanAttackDrop_Type()
)
axSwitchStatAnomLanAttackDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomLanAttackDrop.setStatus("current")


class _AxSwitchStatAnomIPOptionDrop_Type(Counter32):
    """Custom type axSwitchStatAnomIPOptionDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomIPOptionDrop_Object = MibTableColumn
axSwitchStatAnomIPOptionDrop = _AxSwitchStatAnomIPOptionDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 25),
    _AxSwitchStatAnomIPOptionDrop_Type()
)
axSwitchStatAnomIPOptionDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomIPOptionDrop.setStatus("current")


class _AxSwitchStatAnomPingDeathDrop_Type(Counter32):
    """Custom type axSwitchStatAnomPingDeathDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomPingDeathDrop_Object = MibTableColumn
axSwitchStatAnomPingDeathDrop = _AxSwitchStatAnomPingDeathDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 26),
    _AxSwitchStatAnomPingDeathDrop_Type()
)
axSwitchStatAnomPingDeathDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomPingDeathDrop.setStatus("current")


class _AxSwitchStatAnomAllFragDrop_Type(Counter32):
    """Custom type axSwitchStatAnomAllFragDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomAllFragDrop_Object = MibTableColumn
axSwitchStatAnomAllFragDrop = _AxSwitchStatAnomAllFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 27),
    _AxSwitchStatAnomAllFragDrop_Type()
)
axSwitchStatAnomAllFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomAllFragDrop.setStatus("current")


class _AxSwitchStatAnomTCPNoFragDrop_Type(Counter32):
    """Custom type axSwitchStatAnomTCPNoFragDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomTCPNoFragDrop_Object = MibTableColumn
axSwitchStatAnomTCPNoFragDrop = _AxSwitchStatAnomTCPNoFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 28),
    _AxSwitchStatAnomTCPNoFragDrop_Type()
)
axSwitchStatAnomTCPNoFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomTCPNoFragDrop.setStatus("current")


class _AxSwitchStatAnomSYNFragDrop_Type(Counter32):
    """Custom type axSwitchStatAnomSYNFragDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomSYNFragDrop_Object = MibTableColumn
axSwitchStatAnomSYNFragDrop = _AxSwitchStatAnomSYNFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 29),
    _AxSwitchStatAnomSYNFragDrop_Type()
)
axSwitchStatAnomSYNFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomSYNFragDrop.setStatus("current")


class _AxSwitchStatAnomTCPSynFinDrop_Type(Counter32):
    """Custom type axSwitchStatAnomTCPSynFinDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomTCPSynFinDrop_Object = MibTableColumn
axSwitchStatAnomTCPSynFinDrop = _AxSwitchStatAnomTCPSynFinDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 30),
    _AxSwitchStatAnomTCPSynFinDrop_Type()
)
axSwitchStatAnomTCPSynFinDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomTCPSynFinDrop.setStatus("current")


class _AxSwitchStatAnomAnyDrop_Type(Counter32):
    """Custom type axSwitchStatAnomAnyDrop based on Counter32"""
    defaultValue = 0


_AxSwitchStatAnomAnyDrop_Object = MibTableColumn
axSwitchStatAnomAnyDrop = _AxSwitchStatAnomAnyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 16, 31, 1, 31),
    _AxSwitchStatAnomAnyDrop_Type()
)
axSwitchStatAnomAnyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSwitchStatAnomAnyDrop.setStatus("current")
_AxHA_ObjectIdentity = ObjectIdentity
axHA = _AxHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17)
)
_AxHAGlobalConfig_ObjectIdentity = ObjectIdentity
axHAGlobalConfig = _AxHAGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1)
)


class _AxHAConfigEnabled_Type(Integer32):
    """Custom type axHAConfigEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxHAConfigEnabled_Type.__name__ = "Integer32"
_AxHAConfigEnabled_Object = MibScalar
axHAConfigEnabled = _AxHAConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 1),
    _AxHAConfigEnabled_Type()
)
axHAConfigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAConfigEnabled.setStatus("current")
_AxHAID_Type = Integer32
_AxHAID_Object = MibScalar
axHAID = _AxHAID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 2),
    _AxHAID_Type()
)
axHAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAID.setStatus("current")
_AxHASetID_Type = Integer32
_AxHASetID_Object = MibScalar
axHASetID = _AxHASetID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 3),
    _AxHASetID_Type()
)
axHASetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHASetID.setStatus("current")


class _AxHAPreemptStatusEnabled_Type(Integer32):
    """Custom type axHAPreemptStatusEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AxHAPreemptStatusEnabled_Type.__name__ = "Integer32"
_AxHAPreemptStatusEnabled_Object = MibScalar
axHAPreemptStatusEnabled = _AxHAPreemptStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 4),
    _AxHAPreemptStatusEnabled_Type()
)
axHAPreemptStatusEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAPreemptStatusEnabled.setStatus("current")
_AxHATimeoutInterval_Type = Integer32
_AxHATimeoutInterval_Object = MibScalar
axHATimeoutInterval = _AxHATimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 5),
    _AxHATimeoutInterval_Type()
)
axHATimeoutInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHATimeoutInterval.setStatus("current")
_AxHATimeoutRetry_Type = Integer32
_AxHATimeoutRetry_Object = MibScalar
axHATimeoutRetry = _AxHATimeoutRetry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 6),
    _AxHATimeoutRetry_Type()
)
axHATimeoutRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHATimeoutRetry.setStatus("current")
_AxHAARPRetry_Type = Integer32
_AxHAARPRetry_Object = MibScalar
axHAARPRetry = _AxHAARPRetry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 1, 7),
    _AxHAARPRetry_Type()
)
axHAARPRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAARPRetry.setStatus("current")
_AxHAGroup_ObjectIdentity = ObjectIdentity
axHAGroup = _AxHAGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2)
)
_AxHAGroupCount_Type = Integer32
_AxHAGroupCount_Object = MibScalar
axHAGroupCount = _AxHAGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 1),
    _AxHAGroupCount_Type()
)
axHAGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupCount.setStatus("current")
_AxHAGroupStatusTable_Object = MibTable
axHAGroupStatusTable = _AxHAGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2)
)
if mibBuilder.loadTexts:
    axHAGroupStatusTable.setStatus("current")
_AxHAGroupStatusEntry_Object = MibTableRow
axHAGroupStatusEntry = _AxHAGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1)
)
axHAGroupStatusEntry.setIndexNames(
    (0, "A10-AX-MIB", "axHAGroupID"),
)
if mibBuilder.loadTexts:
    axHAGroupStatusEntry.setStatus("current")
_AxHAGroupID_Type = Integer32
_AxHAGroupID_Object = MibTableColumn
axHAGroupID = _AxHAGroupID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1, 1),
    _AxHAGroupID_Type()
)
axHAGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupID.setStatus("current")


class _AxHAGroupLocalStatus_Type(Integer32):
    """Custom type axHAGroupLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notConfigured", 9),
          ("standby", 0))
    )


_AxHAGroupLocalStatus_Type.__name__ = "Integer32"
_AxHAGroupLocalStatus_Object = MibTableColumn
axHAGroupLocalStatus = _AxHAGroupLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1, 2),
    _AxHAGroupLocalStatus_Type()
)
axHAGroupLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupLocalStatus.setStatus("current")
_AxHAGroupLocalPriority_Type = Integer32
_AxHAGroupLocalPriority_Object = MibTableColumn
axHAGroupLocalPriority = _AxHAGroupLocalPriority_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1, 3),
    _AxHAGroupLocalPriority_Type()
)
axHAGroupLocalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupLocalPriority.setStatus("current")


class _AxHAGroupPeerStatus_Type(Integer32):
    """Custom type axHAGroupPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notConfigured", 9),
          ("standby", 0))
    )


_AxHAGroupPeerStatus_Type.__name__ = "Integer32"
_AxHAGroupPeerStatus_Object = MibTableColumn
axHAGroupPeerStatus = _AxHAGroupPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1, 4),
    _AxHAGroupPeerStatus_Type()
)
axHAGroupPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupPeerStatus.setStatus("current")
_AxHAGroupPeerPriority_Type = Integer32
_AxHAGroupPeerPriority_Object = MibTableColumn
axHAGroupPeerPriority = _AxHAGroupPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 2, 2, 1, 5),
    _AxHAGroupPeerPriority_Type()
)
axHAGroupPeerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAGroupPeerPriority.setStatus("current")
_AxHAFloatingIP_ObjectIdentity = ObjectIdentity
axHAFloatingIP = _AxHAFloatingIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3)
)
_AxHAFloatingIPCount_Type = Integer32
_AxHAFloatingIPCount_Object = MibScalar
axHAFloatingIPCount = _AxHAFloatingIPCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 1),
    _AxHAFloatingIPCount_Type()
)
axHAFloatingIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAFloatingIPCount.setStatus("current")
_AxHAFloatingIPTable_Object = MibTable
axHAFloatingIPTable = _AxHAFloatingIPTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 2)
)
if mibBuilder.loadTexts:
    axHAFloatingIPTable.setStatus("current")
_AxHAFloatingIPEntry_Object = MibTableRow
axHAFloatingIPEntry = _AxHAFloatingIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 2, 1)
)
axHAFloatingIPEntry.setIndexNames(
    (0, "A10-AX-MIB", "axHAFloatingIPIndex"),
)
if mibBuilder.loadTexts:
    axHAFloatingIPEntry.setStatus("current")
_AxHAFloatingIPIndex_Type = Integer32
_AxHAFloatingIPIndex_Object = MibTableColumn
axHAFloatingIPIndex = _AxHAFloatingIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 2, 1, 1),
    _AxHAFloatingIPIndex_Type()
)
axHAFloatingIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAFloatingIPIndex.setStatus("current")
_AxHAFloatingIPAddress_Type = DisplayString
_AxHAFloatingIPAddress_Object = MibTableColumn
axHAFloatingIPAddress = _AxHAFloatingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 2, 1, 2),
    _AxHAFloatingIPAddress_Type()
)
axHAFloatingIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAFloatingIPAddress.setStatus("current")
_AxHAFloatingIPHaGroupID_Type = Integer32
_AxHAFloatingIPHaGroupID_Object = MibTableColumn
axHAFloatingIPHaGroupID = _AxHAFloatingIPHaGroupID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 17, 3, 2, 1, 3),
    _AxHAFloatingIPHaGroupID_Type()
)
axHAFloatingIPHaGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axHAFloatingIPHaGroupID.setStatus("current")
_AxIpNatStats_ObjectIdentity = ObjectIdentity
axIpNatStats = _AxIpNatStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18)
)
_AxIpNatStatsGlobal_ObjectIdentity = ObjectIdentity
axIpNatStatsGlobal = _AxIpNatStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 1)
)


class _AxIpNatStatsGlobalHits_Type(Integer32):
    """Custom type axIpNatStatsGlobalHits based on Integer32"""
    defaultValue = 0


_AxIpNatStatsGlobalHits_Object = MibScalar
axIpNatStatsGlobalHits = _AxIpNatStatsGlobalHits_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 1, 1),
    _AxIpNatStatsGlobalHits_Type()
)
axIpNatStatsGlobalHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsGlobalHits.setStatus("current")


class _AxIpNatStatsGlobalMisses_Type(Integer32):
    """Custom type axIpNatStatsGlobalMisses based on Integer32"""
    defaultValue = 0


_AxIpNatStatsGlobalMisses_Object = MibScalar
axIpNatStatsGlobalMisses = _AxIpNatStatsGlobalMisses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 1, 2),
    _AxIpNatStatsGlobalMisses_Type()
)
axIpNatStatsGlobalMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsGlobalMisses.setStatus("current")
_AxIpNatStatsIntfInsideOutside_ObjectIdentity = ObjectIdentity
axIpNatStatsIntfInsideOutside = _AxIpNatStatsIntfInsideOutside_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2)
)
_AxIpNatStatsIntfInsideOutsideTable_Object = MibTable
axIpNatStatsIntfInsideOutsideTable = _AxIpNatStatsIntfInsideOutsideTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2, 1)
)
if mibBuilder.loadTexts:
    axIpNatStatsIntfInsideOutsideTable.setStatus("current")
_AxIpNatStatsIntfInsideOutsideEntry_Object = MibTableRow
axIpNatStatsIntfInsideOutsideEntry = _AxIpNatStatsIntfInsideOutsideEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2, 1, 1)
)
axIpNatStatsIntfInsideOutsideEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatStatsInsideOutsideIntfIndex"),
)
if mibBuilder.loadTexts:
    axIpNatStatsIntfInsideOutsideEntry.setStatus("current")
_AxIpNatStatsInsideOutsideIntfIndex_Type = Integer32
_AxIpNatStatsInsideOutsideIntfIndex_Object = MibTableColumn
axIpNatStatsInsideOutsideIntfIndex = _AxIpNatStatsInsideOutsideIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2, 1, 1, 1),
    _AxIpNatStatsInsideOutsideIntfIndex_Type()
)
axIpNatStatsInsideOutsideIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsInsideOutsideIntfIndex.setStatus("current")
_AxIpNatStatsInsideOutsideIntfName_Type = DisplayString
_AxIpNatStatsInsideOutsideIntfName_Object = MibTableColumn
axIpNatStatsInsideOutsideIntfName = _AxIpNatStatsInsideOutsideIntfName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2, 1, 1, 2),
    _AxIpNatStatsInsideOutsideIntfName_Type()
)
axIpNatStatsInsideOutsideIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsInsideOutsideIntfName.setStatus("current")


class _AxIpNatStatsInsideOutsideIntfDirection_Type(Integer32):
    """Custom type axIpNatStatsInsideOutsideIntfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inside", 0),
          ("outside", 1))
    )


_AxIpNatStatsInsideOutsideIntfDirection_Type.__name__ = "Integer32"
_AxIpNatStatsInsideOutsideIntfDirection_Object = MibTableColumn
axIpNatStatsInsideOutsideIntfDirection = _AxIpNatStatsInsideOutsideIntfDirection_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 2, 1, 1, 3),
    _AxIpNatStatsInsideOutsideIntfDirection_Type()
)
axIpNatStatsInsideOutsideIntfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsInsideOutsideIntfDirection.setStatus("current")
_AxIpNatStatsDynamicMapping_ObjectIdentity = ObjectIdentity
axIpNatStatsDynamicMapping = _AxIpNatStatsDynamicMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3)
)
_AxIpNatStatsDynamicMappingTable_Object = MibTable
axIpNatStatsDynamicMappingTable = _AxIpNatStatsDynamicMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1)
)
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingTable.setStatus("current")
_AxIpNatStatsDynamicMappingEntry_Object = MibTableRow
axIpNatStatsDynamicMappingEntry = _AxIpNatStatsDynamicMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1)
)
axIpNatStatsDynamicMappingEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatStatsDynamicMappingAccessListID"),
)
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingEntry.setStatus("current")
_AxIpNatStatsDynamicMappingAccessListID_Type = Integer32
_AxIpNatStatsDynamicMappingAccessListID_Object = MibTableColumn
axIpNatStatsDynamicMappingAccessListID = _AxIpNatStatsDynamicMappingAccessListID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 1),
    _AxIpNatStatsDynamicMappingAccessListID_Type()
)
axIpNatStatsDynamicMappingAccessListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAccessListID.setStatus("current")
_AxIpNatStatsDynamicMappingPoolName_Type = DisplayString
_AxIpNatStatsDynamicMappingPoolName_Object = MibTableColumn
axIpNatStatsDynamicMappingPoolName = _AxIpNatStatsDynamicMappingPoolName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 2),
    _AxIpNatStatsDynamicMappingPoolName_Type()
)
axIpNatStatsDynamicMappingPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingPoolName.setStatus("current")
_AxIpNatStatsDynamicMappingStartAddress_Type = DisplayString
_AxIpNatStatsDynamicMappingStartAddress_Object = MibTableColumn
axIpNatStatsDynamicMappingStartAddress = _AxIpNatStatsDynamicMappingStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 3),
    _AxIpNatStatsDynamicMappingStartAddress_Type()
)
axIpNatStatsDynamicMappingStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingStartAddress.setStatus("current")
_AxIpNatStatsDynamicMappingEndAddress_Type = DisplayString
_AxIpNatStatsDynamicMappingEndAddress_Object = MibTableColumn
axIpNatStatsDynamicMappingEndAddress = _AxIpNatStatsDynamicMappingEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 4),
    _AxIpNatStatsDynamicMappingEndAddress_Type()
)
axIpNatStatsDynamicMappingEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingEndAddress.setStatus("current")
_AxIpNatStatsDynamicMappingTotalAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingTotalAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingTotalAddresses = _AxIpNatStatsDynamicMappingTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 5),
    _AxIpNatStatsDynamicMappingTotalAddresses_Type()
)
axIpNatStatsDynamicMappingTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingTotalAddresses.setStatus("current")
_AxIpNatStatsDynamicMappingAllocAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingAllocAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingAllocAddresses = _AxIpNatStatsDynamicMappingAllocAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 6),
    _AxIpNatStatsDynamicMappingAllocAddresses_Type()
)
axIpNatStatsDynamicMappingAllocAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAllocAddresses.setStatus("current")
_AxIpNatStatsDynamicMappingMissAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingMissAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingMissAddresses = _AxIpNatStatsDynamicMappingMissAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 3, 1, 1, 7),
    _AxIpNatStatsDynamicMappingMissAddresses_Type()
)
axIpNatStatsDynamicMappingMissAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingMissAddresses.setStatus("current")
_AxIpNatLsnStats_ObjectIdentity = ObjectIdentity
axIpNatLsnStats = _AxIpNatLsnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4)
)
_AxIpNatLsnGobalStats_ObjectIdentity = ObjectIdentity
axIpNatLsnGobalStats = _AxIpNatLsnGobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1)
)


class _AxIpNatLsnTotalUserQuotaSessions_Type(Counter64):
    """Custom type axIpNatLsnTotalUserQuotaSessions based on Counter64"""
    defaultValue = 0


_AxIpNatLsnTotalUserQuotaSessions_Object = MibScalar
axIpNatLsnTotalUserQuotaSessions = _AxIpNatLsnTotalUserQuotaSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 1),
    _AxIpNatLsnTotalUserQuotaSessions_Type()
)
axIpNatLsnTotalUserQuotaSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalUserQuotaSessions.setStatus("current")


class _AxIpNatLsnTotalIpAddrTranslated_Type(Counter64):
    """Custom type axIpNatLsnTotalIpAddrTranslated based on Counter64"""
    defaultValue = 0


_AxIpNatLsnTotalIpAddrTranslated_Object = MibScalar
axIpNatLsnTotalIpAddrTranslated = _AxIpNatLsnTotalIpAddrTranslated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 2),
    _AxIpNatLsnTotalIpAddrTranslated_Type()
)
axIpNatLsnTotalIpAddrTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalIpAddrTranslated.setStatus("current")


class _AxIpNatLsnTotalFullConeSessions_Type(Counter64):
    """Custom type axIpNatLsnTotalFullConeSessions based on Counter64"""
    defaultValue = 0


_AxIpNatLsnTotalFullConeSessions_Object = MibScalar
axIpNatLsnTotalFullConeSessions = _AxIpNatLsnTotalFullConeSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 3),
    _AxIpNatLsnTotalFullConeSessions_Type()
)
axIpNatLsnTotalFullConeSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalFullConeSessions.setStatus("current")
_AxIpNatLsnTrafficStats_ObjectIdentity = ObjectIdentity
axIpNatLsnTrafficStats = _AxIpNatLsnTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4)
)
_AxIpNatLsnTrafficFullConeSessionCreated_Type = Counter64
_AxIpNatLsnTrafficFullConeSessionCreated_Object = MibScalar
axIpNatLsnTrafficFullConeSessionCreated = _AxIpNatLsnTrafficFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 1),
    _AxIpNatLsnTrafficFullConeSessionCreated_Type()
)
axIpNatLsnTrafficFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFullConeSessionCreated.setStatus("current")
_AxIpNatLsnTrafficFullConeSessionFreed_Type = Counter64
_AxIpNatLsnTrafficFullConeSessionFreed_Object = MibScalar
axIpNatLsnTrafficFullConeSessionFreed = _AxIpNatLsnTrafficFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 2),
    _AxIpNatLsnTrafficFullConeSessionFreed_Type()
)
axIpNatLsnTrafficFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFullConeSessionFreed.setStatus("current")
_AxIpNatLsnTrafficFailsInFullConeSessionCreation_Type = Counter64
_AxIpNatLsnTrafficFailsInFullConeSessionCreation_Object = MibScalar
axIpNatLsnTrafficFailsInFullConeSessionCreation = _AxIpNatLsnTrafficFailsInFullConeSessionCreation_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 3),
    _AxIpNatLsnTrafficFailsInFullConeSessionCreation_Type()
)
axIpNatLsnTrafficFailsInFullConeSessionCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFailsInFullConeSessionCreation.setStatus("current")
_AxIpNatLsnTrafficHairpinSessionCreated_Type = Counter64
_AxIpNatLsnTrafficHairpinSessionCreated_Object = MibScalar
axIpNatLsnTrafficHairpinSessionCreated = _AxIpNatLsnTrafficHairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 4),
    _AxIpNatLsnTrafficHairpinSessionCreated_Type()
)
axIpNatLsnTrafficHairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficHairpinSessionCreated.setStatus("current")
_AxIpNatLsnTrafficEndpointIndepMapMatch_Type = Counter64
_AxIpNatLsnTrafficEndpointIndepMapMatch_Object = MibScalar
axIpNatLsnTrafficEndpointIndepMapMatch = _AxIpNatLsnTrafficEndpointIndepMapMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 5),
    _AxIpNatLsnTrafficEndpointIndepMapMatch_Type()
)
axIpNatLsnTrafficEndpointIndepMapMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficEndpointIndepMapMatch.setStatus("current")
_AxIpNatLsnTrafficEndpointIndepFilterMatch_Type = Counter64
_AxIpNatLsnTrafficEndpointIndepFilterMatch_Object = MibScalar
axIpNatLsnTrafficEndpointIndepFilterMatch = _AxIpNatLsnTrafficEndpointIndepFilterMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 6),
    _AxIpNatLsnTrafficEndpointIndepFilterMatch_Type()
)
axIpNatLsnTrafficEndpointIndepFilterMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficEndpointIndepFilterMatch.setStatus("current")
_AxIpNatLsnTrafficUserQuotasCreated_Type = Counter64
_AxIpNatLsnTrafficUserQuotasCreated_Object = MibScalar
axIpNatLsnTrafficUserQuotasCreated = _AxIpNatLsnTrafficUserQuotasCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 7),
    _AxIpNatLsnTrafficUserQuotasCreated_Type()
)
axIpNatLsnTrafficUserQuotasCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUserQuotasCreated.setStatus("current")
_AxIpNatLsnTrafficUserQuotasFreed_Type = Counter64
_AxIpNatLsnTrafficUserQuotasFreed_Object = MibScalar
axIpNatLsnTrafficUserQuotasFreed = _AxIpNatLsnTrafficUserQuotasFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 8),
    _AxIpNatLsnTrafficUserQuotasFreed_Type()
)
axIpNatLsnTrafficUserQuotasFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUserQuotasFreed.setStatus("current")
_AxIpNatLsnTrafficFailsInUserQuotasCreation_Type = Counter64
_AxIpNatLsnTrafficFailsInUserQuotasCreation_Object = MibScalar
axIpNatLsnTrafficFailsInUserQuotasCreation = _AxIpNatLsnTrafficFailsInUserQuotasCreation_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 9),
    _AxIpNatLsnTrafficFailsInUserQuotasCreation_Type()
)
axIpNatLsnTrafficFailsInUserQuotasCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFailsInUserQuotasCreation.setStatus("current")
_AxIpNatLsnTrafficIcmpUserQuotasExceeded_Type = Counter64
_AxIpNatLsnTrafficIcmpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficIcmpUserQuotasExceeded = _AxIpNatLsnTrafficIcmpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 10),
    _AxIpNatLsnTrafficIcmpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficIcmpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficIcmpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficUdpUserQuotasExceeded_Type = Counter64
_AxIpNatLsnTrafficUdpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficUdpUserQuotasExceeded = _AxIpNatLsnTrafficUdpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 11),
    _AxIpNatLsnTrafficUdpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficUdpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUdpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficTcpUserQuotasExceeded_Type = Counter64
_AxIpNatLsnTrafficTcpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficTcpUserQuotasExceeded = _AxIpNatLsnTrafficTcpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 12),
    _AxIpNatLsnTrafficTcpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficTcpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficTcpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficExtendedUserQuotasMatch_Type = Counter64
_AxIpNatLsnTrafficExtendedUserQuotasMatch_Object = MibScalar
axIpNatLsnTrafficExtendedUserQuotasMatch = _AxIpNatLsnTrafficExtendedUserQuotasMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 13),
    _AxIpNatLsnTrafficExtendedUserQuotasMatch_Type()
)
axIpNatLsnTrafficExtendedUserQuotasMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficExtendedUserQuotasMatch.setStatus("current")
_AxIpNatLsnTrafficExtendedUserQuotasExceeded_Type = Counter64
_AxIpNatLsnTrafficExtendedUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficExtendedUserQuotasExceeded = _AxIpNatLsnTrafficExtendedUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 14),
    _AxIpNatLsnTrafficExtendedUserQuotasExceeded_Type()
)
axIpNatLsnTrafficExtendedUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficExtendedUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficNatPortUnavailable_Type = Counter64
_AxIpNatLsnTrafficNatPortUnavailable_Object = MibScalar
axIpNatLsnTrafficNatPortUnavailable = _AxIpNatLsnTrafficNatPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 15),
    _AxIpNatLsnTrafficNatPortUnavailable_Type()
)
axIpNatLsnTrafficNatPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficNatPortUnavailable.setStatus("current")
_AxIpNatLsnTrafficNewUserResourceUnavailable_Type = Counter64
_AxIpNatLsnTrafficNewUserResourceUnavailable_Object = MibScalar
axIpNatLsnTrafficNewUserResourceUnavailable = _AxIpNatLsnTrafficNewUserResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 16),
    _AxIpNatLsnTrafficNewUserResourceUnavailable_Type()
)
axIpNatLsnTrafficNewUserResourceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficNewUserResourceUnavailable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotSessions = _AxIpNatLsnTop5PrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2)
)
_AxIpNatLsnTop5PrivateIpAddrTotSessionTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotSessionTable = _AxIpNatLsnTop5PrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotSessionTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotSessionEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotSessionEntry = _AxIpNatLsnTop5PrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5PrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotSessionEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddr_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddr_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddr = _AxIpNatLsnTop5PrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddr_Type()
)
axIpNatLsnTop5PrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddr.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumSessions = _AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumSessions.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddr = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddr.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotTcpPorts = _AxIpNatLsnTop5PrivateIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3)
)
_AxIpNatLsnTop5PrivateIpAddrTotTcpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotTcpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotTcpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotTcpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5PrivateIpAddrInTcpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInTcpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInTcpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInTcpPort = _AxIpNatLsnTop5PrivateIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInTcpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInTcpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotUdpPorts = _AxIpNatLsnTop5PrivateIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4)
)
_AxIpNatLsnTop5PrivateIpAddrTotUdpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotUdpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotUdpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotUdpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5PrivateIpAddrInUdpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInUdpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInUdpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInUdpPort = _AxIpNatLsnTop5PrivateIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInUdpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInUdpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotIcmpPorts = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5)
)
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5PrivateIpAddrInIcmpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInIcmpPort = _AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInIcmpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5UserPrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddr_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddr_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddr = _AxIpNatLsnTop5UserPrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddr_Type()
)
axIpNatLsnTop5UserPrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddr.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5UserPrivateIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInTcp = _AxIpNatLsnTop5UserPrivateIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInTcp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5UserPrivateIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInUdp = _AxIpNatLsnTop5UserPrivateIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInUdp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5UserPrivateIpAddrInIcmp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInIcmp = _AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInIcmp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUsers_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotUsers = _AxIpNatLsnTop5GlobalPoolIpAddrTotUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotUserTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotUserTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotUserTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUserTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUserEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5GlobalPoolIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddr_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddr_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddr = _AxIpNatLsnTop5GlobalPoolIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddr_Type()
)
axIpNatLsnTop5GlobalPoolIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddr.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5GlobalPoolIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrInTcp = _AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-MIB", "axIpNatLsnTop5GlobalPoolIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrInUdp = _AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts.setStatus("current")
_AxSessionStats_ObjectIdentity = ObjectIdentity
axSessionStats = _AxSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19)
)
_AxSessionStatsGlobal_ObjectIdentity = ObjectIdentity
axSessionStatsGlobal = _AxSessionStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1)
)


class _AxSessionGlobalStatTCPEstablished_Type(Counter32):
    """Custom type axSessionGlobalStatTCPEstablished based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatTCPEstablished_Object = MibScalar
axSessionGlobalStatTCPEstablished = _AxSessionGlobalStatTCPEstablished_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 1),
    _AxSessionGlobalStatTCPEstablished_Type()
)
axSessionGlobalStatTCPEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatTCPEstablished.setStatus("current")


class _AxSessionGlobalStatTCPHalfOpen_Type(Counter32):
    """Custom type axSessionGlobalStatTCPHalfOpen based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatTCPHalfOpen_Object = MibScalar
axSessionGlobalStatTCPHalfOpen = _AxSessionGlobalStatTCPHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 2),
    _AxSessionGlobalStatTCPHalfOpen_Type()
)
axSessionGlobalStatTCPHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatTCPHalfOpen.setStatus("current")


class _AxSessionGlobalStatUDP_Type(Counter32):
    """Custom type axSessionGlobalStatUDP based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatUDP_Object = MibScalar
axSessionGlobalStatUDP = _AxSessionGlobalStatUDP_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 3),
    _AxSessionGlobalStatUDP_Type()
)
axSessionGlobalStatUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatUDP.setStatus("current")


class _AxSessionGlobalStatNonTcpUdpIPSession_Type(Counter32):
    """Custom type axSessionGlobalStatNonTcpUdpIPSession based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatNonTcpUdpIPSession_Object = MibScalar
axSessionGlobalStatNonTcpUdpIPSession = _AxSessionGlobalStatNonTcpUdpIPSession_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 4),
    _AxSessionGlobalStatNonTcpUdpIPSession_Type()
)
axSessionGlobalStatNonTcpUdpIPSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatNonTcpUdpIPSession.setStatus("current")


class _AxSessionGlobalStatOther_Type(Counter32):
    """Custom type axSessionGlobalStatOther based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatOther_Object = MibScalar
axSessionGlobalStatOther = _AxSessionGlobalStatOther_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 5),
    _AxSessionGlobalStatOther_Type()
)
axSessionGlobalStatOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatOther.setStatus("current")


class _AxSessionGlobalStatReverseNATTCP_Type(Counter32):
    """Custom type axSessionGlobalStatReverseNATTCP based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatReverseNATTCP_Object = MibScalar
axSessionGlobalStatReverseNATTCP = _AxSessionGlobalStatReverseNATTCP_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 6),
    _AxSessionGlobalStatReverseNATTCP_Type()
)
axSessionGlobalStatReverseNATTCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatReverseNATTCP.setStatus("current")


class _AxSessionGlobalStatReverseNATUDP_Type(Counter32):
    """Custom type axSessionGlobalStatReverseNATUDP based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatReverseNATUDP_Object = MibScalar
axSessionGlobalStatReverseNATUDP = _AxSessionGlobalStatReverseNATUDP_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 7),
    _AxSessionGlobalStatReverseNATUDP_Type()
)
axSessionGlobalStatReverseNATUDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatReverseNATUDP.setStatus("current")


class _AxSessionGlobalStatFreeBufferCount_Type(Counter32):
    """Custom type axSessionGlobalStatFreeBufferCount based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatFreeBufferCount_Object = MibScalar
axSessionGlobalStatFreeBufferCount = _AxSessionGlobalStatFreeBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 8),
    _AxSessionGlobalStatFreeBufferCount_Type()
)
axSessionGlobalStatFreeBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatFreeBufferCount.setStatus("current")


class _AxSessionGlobalStatFreeCurrentConns_Type(Counter32):
    """Custom type axSessionGlobalStatFreeCurrentConns based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatFreeCurrentConns_Object = MibScalar
axSessionGlobalStatFreeCurrentConns = _AxSessionGlobalStatFreeCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 9),
    _AxSessionGlobalStatFreeCurrentConns_Type()
)
axSessionGlobalStatFreeCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatFreeCurrentConns.setStatus("current")


class _AxSessionGlobalStatConnCount_Type(Counter32):
    """Custom type axSessionGlobalStatConnCount based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatConnCount_Object = MibScalar
axSessionGlobalStatConnCount = _AxSessionGlobalStatConnCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 10),
    _AxSessionGlobalStatConnCount_Type()
)
axSessionGlobalStatConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatConnCount.setStatus("current")


class _AxSessionGlobalStatConnFree_Type(Counter32):
    """Custom type axSessionGlobalStatConnFree based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatConnFree_Object = MibScalar
axSessionGlobalStatConnFree = _AxSessionGlobalStatConnFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 11),
    _AxSessionGlobalStatConnFree_Type()
)
axSessionGlobalStatConnFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatConnFree.setStatus("current")


class _AxSessionGlobalStatTCPSynHalfOpen_Type(Counter32):
    """Custom type axSessionGlobalStatTCPSynHalfOpen based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatTCPSynHalfOpen_Object = MibScalar
axSessionGlobalStatTCPSynHalfOpen = _AxSessionGlobalStatTCPSynHalfOpen_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 12),
    _AxSessionGlobalStatTCPSynHalfOpen_Type()
)
axSessionGlobalStatTCPSynHalfOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatTCPSynHalfOpen.setStatus("current")


class _AxSessionGlobalStatConnSMPAllocated_Type(Counter32):
    """Custom type axSessionGlobalStatConnSMPAllocated based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatConnSMPAllocated_Object = MibScalar
axSessionGlobalStatConnSMPAllocated = _AxSessionGlobalStatConnSMPAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 13),
    _AxSessionGlobalStatConnSMPAllocated_Type()
)
axSessionGlobalStatConnSMPAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatConnSMPAllocated.setStatus("current")


class _AxSessionGlobalStatConnSMPFree_Type(Counter32):
    """Custom type axSessionGlobalStatConnSMPFree based on Counter32"""
    defaultValue = 0


_AxSessionGlobalStatConnSMPFree_Object = MibScalar
axSessionGlobalStatConnSMPFree = _AxSessionGlobalStatConnSMPFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 19, 1, 14),
    _AxSessionGlobalStatConnSMPFree_Type()
)
axSessionGlobalStatConnSMPFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSessionGlobalStatConnSMPFree.setStatus("current")

# Managed Objects groups


# Notification objects

axSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 2, 100, 1)
)
axSyslogTrap.setObjects(
      *(("A10-AX-MIB", "axSyslogModuleName"),
        ("A10-AX-MIB", "axSyslogPriority"),
        ("A10-AX-MIB", "axSyslogMsg"))
)
if mibBuilder.loadTexts:
    axSyslogTrap.setStatus(
        "current"
    )

axSystemStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 1)
)
if mibBuilder.loadTexts:
    axSystemStart.setStatus(
        "current"
    )

axSystemShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 2)
)
if mibBuilder.loadTexts:
    axSystemShutdown.setStatus(
        "current"
    )

axSystemTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 3)
)
if mibBuilder.loadTexts:
    axSystemTempHigh.setStatus(
        "current"
    )

axFan1Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 4)
)
if mibBuilder.loadTexts:
    axFan1Failure.setStatus(
        "deprecated"
    )

axFan2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 5)
)
if mibBuilder.loadTexts:
    axFan2Failure.setStatus(
        "deprecated"
    )

axFan3Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 6)
)
if mibBuilder.loadTexts:
    axFan3Failure.setStatus(
        "deprecated"
    )

axUpperPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 9)
)
if mibBuilder.loadTexts:
    axUpperPowerSupplyFailure.setStatus(
        "deprecated"
    )

axLowerPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 10)
)
if mibBuilder.loadTexts:
    axLowerPowerSupplyFailure.setStatus(
        "deprecated"
    )

axPrimaryHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 11)
)
if mibBuilder.loadTexts:
    axPrimaryHardDiskFailure.setStatus(
        "current"
    )

axSecondaryHardDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 12)
)
if mibBuilder.loadTexts:
    axSecondaryHardDiskFailure.setStatus(
        "current"
    )

axHardDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 13)
)
if mibBuilder.loadTexts:
    axHardDiskUsageHigh.setStatus(
        "current"
    )

axMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 14)
)
if mibBuilder.loadTexts:
    axMemoryUsageHigh.setStatus(
        "current"
    )

axSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 15)
)
if mibBuilder.loadTexts:
    axSystemRestart.setStatus(
        "current"
    )

axSystemDropPacketEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 16)
)
axSystemDropPacketEvent.setObjects(
    ("A10-AX-MIB", "axNotificationDropEventReason")
)
if mibBuilder.loadTexts:
    axSystemDropPacketEvent.setStatus(
        "current"
    )

axSystemRelieveDropPacketEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 17)
)
axSystemRelieveDropPacketEvent.setObjects(
    ("A10-AX-MIB", "axNotificationDropEventReason")
)
if mibBuilder.loadTexts:
    axSystemRelieveDropPacketEvent.setStatus(
        "current"
    )

axSystemControlCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 18)
)
axSystemControlCpuHigh.setObjects(
      *(("A10-AX-MIB", "axNotificationConfiguredThreshold"),
        ("A10-AX-MIB", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemControlCpuHigh.setStatus(
        "current"
    )

axSystemDataCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 19)
)
axSystemDataCpuHigh.setObjects(
      *(("A10-AX-MIB", "axNotificationConfiguredThreshold"),
        ("A10-AX-MIB", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axSystemDataCpuHigh.setStatus(
        "current"
    )

axSystemFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 20)
)
axSystemFanFailure.setObjects(
    ("A10-AX-MIB", "axNotificationFanName")
)
if mibBuilder.loadTexts:
    axSystemFanFailure.setStatus(
        "current"
    )

axSystemPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 1, 21)
)
axSystemPowerSupplyFailure.setObjects(
    ("A10-AX-MIB", "axNotificationPowerSupplyName")
)
if mibBuilder.loadTexts:
    axSystemPowerSupplyFailure.setStatus(
        "current"
    )

axHAStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 1)
)
axHAStandby.setObjects(
    ("A10-AX-MIB", "axNotificationMsg")
)
if mibBuilder.loadTexts:
    axHAStandby.setStatus(
        "current"
    )

axHAActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 2)
)
axHAActive.setObjects(
    ("A10-AX-MIB", "axNotificationMsg")
)
if mibBuilder.loadTexts:
    axHAActive.setStatus(
        "current"
    )

axHAActiveActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 3)
)
axHAActiveActive.setObjects(
    ("A10-AX-MIB", "axNotificationMsg")
)
if mibBuilder.loadTexts:
    axHAActiveActive.setStatus(
        "current"
    )

axServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 4)
)
axServiceDown.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"))
)
if mibBuilder.loadTexts:
    axServiceDown.setStatus(
        "current"
    )

axServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 5)
)
axServiceUp.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"))
)
if mibBuilder.loadTexts:
    axServiceUp.setStatus(
        "current"
    )

axServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 6)
)
axServerDown.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"))
)
if mibBuilder.loadTexts:
    axServerDown.setStatus(
        "current"
    )

axServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 7)
)
axServerUp.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"))
)
if mibBuilder.loadTexts:
    axServerUp.setStatus(
        "current"
    )

axServerConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 8)
)
axServerConnLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnLimit.setStatus(
        "current"
    )

axServerConnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 9)
)
axServerConnResume.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnResume.setStatus(
        "current"
    )

axServiceConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 10)
)
axServiceConnLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnLimit.setStatus(
        "current"
    )

axServiceConnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 11)
)
axServiceConnResume.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnResume.setStatus(
        "current"
    )

axVirtualServerPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 12)
)
axVirtualServerPortDown.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationVirtualServer"),
        ("A10-AX-MIB", "axNotificationVirtualServerPort"),
        ("A10-AX-MIB", "axNotificationVirtualServerPortType"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortDown.setStatus(
        "current"
    )

axVirtualServerPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 13)
)
axVirtualServerPortUp.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationVirtualServer"),
        ("A10-AX-MIB", "axNotificationVirtualServerPort"),
        ("A10-AX-MIB", "axNotificationVirtualServerPortType"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortUp.setStatus(
        "current"
    )

axApplicationBufferReachLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 14)
)
axApplicationBufferReachLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationConfiguredThreshold"),
        ("A10-AX-MIB", "axNotificationCurrentUsage"))
)
if mibBuilder.loadTexts:
    axApplicationBufferReachLimit.setStatus(
        "current"
    )

axVirtualServerPortReachConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 15)
)
axVirtualServerPortReachConnLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"),
        ("A10-AX-MIB", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortReachConnLimit.setStatus(
        "current"
    )

axVirtualServerPortReachConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 16)
)
axVirtualServerPortReachConnRateLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"),
        ("A10-AX-MIB", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerPortReachConnRateLimit.setStatus(
        "current"
    )

axVirtualServerReachConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 17)
)
axVirtualServerReachConnLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerReachConnLimit.setStatus(
        "current"
    )

axVirtualServerReachConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 18)
)
axVirtualServerReachConnRateLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationConnLimit"))
)
if mibBuilder.loadTexts:
    axVirtualServerReachConnRateLimit.setStatus(
        "current"
    )

axServerConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 19)
)
axServerConnRateLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServerConnRateLimit.setStatus(
        "current"
    )

axServiceConnRateLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 2, 20)
)
axServiceConnRateLimit.setObjects(
      *(("A10-AX-MIB", "axNotificationMsg"),
        ("A10-AX-MIB", "axNotificationSLBServer"),
        ("A10-AX-MIB", "axNotificationSLBPort"),
        ("A10-AX-MIB", "axNotificationSLBCurConns"))
)
if mibBuilder.loadTexts:
    axServiceConnRateLimit.setStatus(
        "current"
    )

axNetworkTrunkPortsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 12, 2, 3, 1)
)
axNetworkTrunkPortsThreshold.setObjects(
      *(("A10-AX-MIB", "axNotificationTrunkID"),
        ("A10-AX-MIB", "axNotificationPortThreshold"),
        ("A10-AX-MIB", "axNotificationCurrentUpPorts"))
)
if mibBuilder.loadTexts:
    axNetworkTrunkPortsThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A10-AX-MIB",
    **{"axMgmt": axMgmt,
       "axSystem": axSystem,
       "axSysVersion": axSysVersion,
       "axSysPrimaryVersionOnDisk": axSysPrimaryVersionOnDisk,
       "axSysSecondaryVersionOnDisk": axSysSecondaryVersionOnDisk,
       "axSysPrimaryVersionOnCF": axSysPrimaryVersionOnCF,
       "axSysSecondaryVersionOnCF": axSysSecondaryVersionOnCF,
       "axSysMemory": axSysMemory,
       "axSysMemoryTotal": axSysMemoryTotal,
       "axSysMemoryUsage": axSysMemoryUsage,
       "axSysCpu": axSysCpu,
       "axSysCpuNumber": axSysCpuNumber,
       "axSysCpuTable": axSysCpuTable,
       "axSysCpuEntry": axSysCpuEntry,
       "axSysCpuIndex": axSysCpuIndex,
       "axSysCpuUsage": axSysCpuUsage,
       "axSysCpuUsageValue": axSysCpuUsageValue,
       "axSysAverageCpuUsage": axSysAverageCpuUsage,
       "axSysAverageControlCpuUsage": axSysAverageControlCpuUsage,
       "axSysAverageDataCpuUsage": axSysAverageDataCpuUsage,
       "axSysCpuUsageTable": axSysCpuUsageTable,
       "axSysCpuUsageEntry": axSysCpuUsageEntry,
       "axSysCpuIndexInUsage": axSysCpuIndexInUsage,
       "axSysCpuUsagePeriodIndex": axSysCpuUsagePeriodIndex,
       "axSysCpuUsageValueAtPeriod": axSysCpuUsageValueAtPeriod,
       "axSysDisk": axSysDisk,
       "axSysDiskTotalSpace": axSysDiskTotalSpace,
       "axSysDiskFreeSpace": axSysDiskFreeSpace,
       "axSysHwInfo": axSysHwInfo,
       "axSysHwPhySystemTemp": axSysHwPhySystemTemp,
       "axSysHwFan1Speed": axSysHwFan1Speed,
       "axSysHwFan2Speed": axSysHwFan2Speed,
       "axSysHwFan3Speed": axSysHwFan3Speed,
       "axSysLowerPowerSupplyStatus": axSysLowerPowerSupplyStatus,
       "axSysUpperPowerSupplyStatus": axSysUpperPowerSupplyStatus,
       "axSysFanStatusTable": axSysFanStatusTable,
       "axSysFanStatusEntry": axSysFanStatusEntry,
       "axFanIndex": axFanIndex,
       "axFanName": axFanName,
       "axFanStatus": axFanStatus,
       "axSysInfo": axSysInfo,
       "axSysStartupMode": axSysStartupMode,
       "axSysSerialNumber": axSysSerialNumber,
       "axSysFirmwareVersion": axSysFirmwareVersion,
       "axSysAFleXEngineVersion": axSysAFleXEngineVersion,
       "axNetwork": axNetwork,
       "axInterfaces": axInterfaces,
       "axInterface": axInterface,
       "axInterfaceCount": axInterfaceCount,
       "axInterfaceTable": axInterfaceTable,
       "axInterfaceEntry": axInterfaceEntry,
       "axInterfaceIndex": axInterfaceIndex,
       "axInterfaceName": axInterfaceName,
       "axInterfaceMediaMaxSpeed": axInterfaceMediaMaxSpeed,
       "axInterfaceMediaMaxDuplex": axInterfaceMediaMaxDuplex,
       "axInterfaceMediaActiveSpeed": axInterfaceMediaActiveSpeed,
       "axInterfaceMediaActiveDuplex": axInterfaceMediaActiveDuplex,
       "axInterfaceMacAddr": axInterfaceMacAddr,
       "axInterfaceMtu": axInterfaceMtu,
       "axInterfaceAdminStatus": axInterfaceAdminStatus,
       "axInterfaceStatus": axInterfaceStatus,
       "axInterfaceAlias": axInterfaceAlias,
       "axInterfaceFlowCtrlAdminStatus": axInterfaceFlowCtrlAdminStatus,
       "axInterfaceFlowCtrlOperStatus": axInterfaceFlowCtrlOperStatus,
       "axInterfaceStat": axInterfaceStat,
       "axInterfaceStatTable": axInterfaceStatTable,
       "axInterfaceStatEntry": axInterfaceStatEntry,
       "axInterfaceStatIndex": axInterfaceStatIndex,
       "axInterfaceStatPktsIn": axInterfaceStatPktsIn,
       "axInterfaceStatBytesIn": axInterfaceStatBytesIn,
       "axInterfaceStatPktsOut": axInterfaceStatPktsOut,
       "axInterfaceStatBytesOut": axInterfaceStatBytesOut,
       "axInterfaceStatMcastIn": axInterfaceStatMcastIn,
       "axInterfaceStatMcastOut": axInterfaceStatMcastOut,
       "axInterfaceStatErrorsIn": axInterfaceStatErrorsIn,
       "axInterfaceStatErrorsOut": axInterfaceStatErrorsOut,
       "axInterfaceStatDropsIn": axInterfaceStatDropsIn,
       "axInterfaceStatDropsOut": axInterfaceStatDropsOut,
       "axInterfaceStatCollisions": axInterfaceStatCollisions,
       "axVlans": axVlans,
       "axVlanCfg": axVlanCfg,
       "axVlanCfgTable": axVlanCfgTable,
       "axVlanCfgEntry": axVlanCfgEntry,
       "axVlanId": axVlanId,
       "axVlanName": axVlanName,
       "axVlanRouterInterface": axVlanRouterInterface,
       "axVlanCfgMemberTable": axVlanCfgMemberTable,
       "axVlanCfgMemberEntry": axVlanCfgMemberEntry,
       "axVlanMemberVlanId": axVlanMemberVlanId,
       "axVlanMemberIntfId": axVlanMemberIntfId,
       "axVlanMemberTagged": axVlanMemberTagged,
       "axLogging": axLogging,
       "axLogBufferSize": axLogBufferSize,
       "axLogBufferPri": axLogBufferPri,
       "axLogConsolePri": axLogConsolePri,
       "axLogEmailPri": axLogEmailPri,
       "axLogEmailAddr": axLogEmailAddr,
       "axLogSyslogPri": axLogSyslogPri,
       "axLogSyslogHostTable": axLogSyslogHostTable,
       "axLogSyslogHostEntry": axLogSyslogHostEntry,
       "axLogSyslogHostIndex": axLogSyslogHostIndex,
       "axLogSyslogHost": axLogSyslogHost,
       "axLogSyslogPort": axLogSyslogPort,
       "axLogMonitorPri": axLogMonitorPri,
       "axSyslogTrapPrefix": axSyslogTrapPrefix,
       "axSyslogTrap": axSyslogTrap,
       "axSyslogTrapObjects": axSyslogTrapObjects,
       "axSyslogModuleName": axSyslogModuleName,
       "axSyslogPriority": axSyslogPriority,
       "axSyslogMsg": axSyslogMsg,
       "axApp": axApp,
       "axAppGlobals": axAppGlobals,
       "axAppGlobalSetting": axAppGlobalSetting,
       "axAppGlobalSystemResourceUsageTable": axAppGlobalSystemResourceUsageTable,
       "axAppGlobalSystemResourceUsageEntry": axAppGlobalSystemResourceUsageEntry,
       "axAppGlobalSystemResourceIndex": axAppGlobalSystemResourceIndex,
       "axAppGlobalSystemResourceName": axAppGlobalSystemResourceName,
       "axAppGlobalAllowedCurrentValue": axAppGlobalAllowedCurrentValue,
       "axAppGlobalAllowedDefaultValue": axAppGlobalAllowedDefaultValue,
       "axAppGlobalAllowedMinValue": axAppGlobalAllowedMinValue,
       "axAppGlobalAllowedMaxValue": axAppGlobalAllowedMaxValue,
       "axAppGlobalStats": axAppGlobalStats,
       "axAppGlobalTotalCurrentConnections": axAppGlobalTotalCurrentConnections,
       "axAppGlobalTotalNewConnections": axAppGlobalTotalNewConnections,
       "axAppGlobalTotalNewL4Connections": axAppGlobalTotalNewL4Connections,
       "axAppGlobalTotalNewL7Connections": axAppGlobalTotalNewL7Connections,
       "axAppGlobalTotalNewIPNatConnections": axAppGlobalTotalNewIPNatConnections,
       "axAppGlobalTotalSSLConnections": axAppGlobalTotalSSLConnections,
       "axAppGlobalTotalL7Requests": axAppGlobalTotalL7Requests,
       "axGlobalAppPacketDrop": axGlobalAppPacketDrop,
       "axGlobalTotalAppPacketDrop": axGlobalTotalAppPacketDrop,
       "axGlobalTotalL4Session": axGlobalTotalL4Session,
       "axGlobalAppBuffer": axGlobalAppBuffer,
       "axAppGlobalBufferConfigLimit": axAppGlobalBufferConfigLimit,
       "axAppGlobalBufferCurrentUsage": axAppGlobalBufferCurrentUsage,
       "axServers": axServers,
       "axServer": axServer,
       "axServerCount": axServerCount,
       "axServerTable": axServerTable,
       "axServerEntry": axServerEntry,
       "axServerName": axServerName,
       "axServerAddress": axServerAddress,
       "axServerEnabledState": axServerEnabledState,
       "axServerHealthMonitor": axServerHealthMonitor,
       "axServerMonitorState": axServerMonitorState,
       "axServerStat": axServerStat,
       "axServerStatCount": axServerStatCount,
       "axServerStatTable": axServerStatTable,
       "axServerStatEntry": axServerStatEntry,
       "axServerStatAddress": axServerStatAddress,
       "axServerStatName": axServerStatName,
       "axServerStatServerPktsIn": axServerStatServerPktsIn,
       "axServerStatServerBytesIn": axServerStatServerBytesIn,
       "axServerStatServerPktsOut": axServerStatServerPktsOut,
       "axServerStatServerBytesOut": axServerStatServerBytesOut,
       "axServerStatServerTotalConns": axServerStatServerTotalConns,
       "axServerStatServerCurConns": axServerStatServerCurConns,
       "axServerStatServerPersistConns": axServerStatServerPersistConns,
       "axServerStatServerStatus": axServerStatServerStatus,
       "axServerStatServerTotalL7Reqs": axServerStatServerTotalL7Reqs,
       "axServerStatServerTotalCurrL7Reqs": axServerStatServerTotalCurrL7Reqs,
       "axServerStatServerTotalSuccL7Reqs": axServerStatServerTotalSuccL7Reqs,
       "axServerPort": axServerPort,
       "axServerPortTable": axServerPortTable,
       "axServerPortEntry": axServerPortEntry,
       "axServerNameInPort": axServerNameInPort,
       "axServerPortType": axServerPortType,
       "axServerPortNum": axServerPortNum,
       "axServerAddressInPort": axServerAddressInPort,
       "axServerPortEnabledState": axServerPortEnabledState,
       "axServerPortHealthMonitor": axServerPortHealthMonitor,
       "axServerPortConnLimit": axServerPortConnLimit,
       "axServerPortWeight": axServerPortWeight,
       "axServerPortMonitorState": axServerPortMonitorState,
       "axServerPortStat": axServerPortStat,
       "axServerPortStatTable": axServerPortStatTable,
       "axServerPortStatEntry": axServerPortStatEntry,
       "axServerStatAddrInPort": axServerStatAddrInPort,
       "axServerStatPortType": axServerStatPortType,
       "axServerStatPortNum": axServerStatPortNum,
       "axServerStatNameInPort": axServerStatNameInPort,
       "axServerPortStatPktsIn": axServerPortStatPktsIn,
       "axServerPortStatBytesIn": axServerPortStatBytesIn,
       "axServerPortStatPktsOut": axServerPortStatPktsOut,
       "axServerPortStatBytesOut": axServerPortStatBytesOut,
       "axServerPortStatTotalConns": axServerPortStatTotalConns,
       "axServerPortStatCurConns": axServerPortStatCurConns,
       "axServerPortStatPersistConns": axServerPortStatPersistConns,
       "axServerPortStatStatus": axServerPortStatStatus,
       "axServerPortStatTotalL7Reqs": axServerPortStatTotalL7Reqs,
       "axServerPortStatTotalCurrL7Reqs": axServerPortStatTotalCurrL7Reqs,
       "axServerPortStatTotalSuccL7Reqs": axServerPortStatTotalSuccL7Reqs,
       "axServiceGroups": axServiceGroups,
       "axServiceGroup": axServiceGroup,
       "axServiceGroupCount": axServiceGroupCount,
       "axServiceGroupTable": axServiceGroupTable,
       "axServiceGroupEntry": axServiceGroupEntry,
       "axServiceGroupName": axServiceGroupName,
       "axServiceGroupType": axServiceGroupType,
       "axServiceGroupLbAlgorithm": axServiceGroupLbAlgorithm,
       "axServiceGroupDisplayStatus": axServiceGroupDisplayStatus,
       "axServiceGroupStat": axServiceGroupStat,
       "axServiceGroupStatTable": axServiceGroupStatTable,
       "axServiceGroupStatEntry": axServiceGroupStatEntry,
       "axServiceGroupStatName": axServiceGroupStatName,
       "axServiceGroupStatPktsIn": axServiceGroupStatPktsIn,
       "axServiceGroupStatBytesIn": axServiceGroupStatBytesIn,
       "axServiceGroupStatPktsOut": axServiceGroupStatPktsOut,
       "axServiceGroupStatBytesOut": axServiceGroupStatBytesOut,
       "axServiceGroupStatTotConns": axServiceGroupStatTotConns,
       "axServiceGroupStatCurConns": axServiceGroupStatCurConns,
       "axServiceGroupStatPersistConns": axServiceGroupStatPersistConns,
       "axServiceGroupStatDisplayStatus": axServiceGroupStatDisplayStatus,
       "axServiceGroupStatTotalL7Reqs": axServiceGroupStatTotalL7Reqs,
       "axServiceGroupStatTotalCurrL7Reqs": axServiceGroupStatTotalCurrL7Reqs,
       "axServiceGroupStatTotalSuccL7Reqs": axServiceGroupStatTotalSuccL7Reqs,
       "axServiceGroupMember": axServiceGroupMember,
       "axServiceGroupMemberTable": axServiceGroupMemberTable,
       "axServiceGroupMemberEntry": axServiceGroupMemberEntry,
       "axServiceGroupNameInMember": axServiceGroupNameInMember,
       "axServiceGroupMemberAddrType": axServiceGroupMemberAddrType,
       "axServerNameInServiceGroupMember": axServerNameInServiceGroupMember,
       "axServerPortNumInServiceGroupMember": axServerPortNumInServiceGroupMember,
       "axServerPortPriorityInServiceGroupMember": axServerPortPriorityInServiceGroupMember,
       "axServerPortStatusInServiceGroupMember": axServerPortStatusInServiceGroupMember,
       "axServiceGroupMemberStat": axServiceGroupMemberStat,
       "axServiceGroupMemberStatTable": axServiceGroupMemberStatTable,
       "axServiceGroupMemberStatEntry": axServiceGroupMemberStatEntry,
       "axServiceGroupMemberStatName": axServiceGroupMemberStatName,
       "axServiceGroupMemberStatAddrType": axServiceGroupMemberStatAddrType,
       "axServerNameInServiceGroupMemberStat": axServerNameInServiceGroupMemberStat,
       "axServerPortNumInServiceGroupMemberStat": axServerPortNumInServiceGroupMemberStat,
       "axServiceGroupMemberStatPktsIn": axServiceGroupMemberStatPktsIn,
       "axServiceGroupMemberStatBytesIn": axServiceGroupMemberStatBytesIn,
       "axServiceGroupMemberStatPktsOut": axServiceGroupMemberStatPktsOut,
       "axServiceGroupMemberStatBytesOut": axServiceGroupMemberStatBytesOut,
       "axServiceGroupMemberStatPersistConns": axServiceGroupMemberStatPersistConns,
       "axServiceGroupMemberStatTotConns": axServiceGroupMemberStatTotConns,
       "axServiceGroupMemberStatCurConns": axServiceGroupMemberStatCurConns,
       "axServerPortStatusInServiceGroupMemberStat": axServerPortStatusInServiceGroupMemberStat,
       "axServiceGroupMemberStatTotalL7Reqs": axServiceGroupMemberStatTotalL7Reqs,
       "axServiceGroupMemberStatTotalCurrL7Reqs": axServiceGroupMemberStatTotalCurrL7Reqs,
       "axServiceGroupMemberStatTotalSuccL7Reqs": axServiceGroupMemberStatTotalSuccL7Reqs,
       "axServiceGroupMemberStatResponseTime": axServiceGroupMemberStatResponseTime,
       "axVirtualServers": axVirtualServers,
       "axVirtualServer": axVirtualServer,
       "axVirtualServerCount": axVirtualServerCount,
       "axVirtualServerTable": axVirtualServerTable,
       "axVirtualServerEntry": axVirtualServerEntry,
       "axVirtualServerName": axVirtualServerName,
       "axVirtualServerAddress": axVirtualServerAddress,
       "axVirtualServerEnabled": axVirtualServerEnabled,
       "axVirtualServerHAGroup": axVirtualServerHAGroup,
       "axVirtualServerDisplayStatus": axVirtualServerDisplayStatus,
       "axVirtualServerStat": axVirtualServerStat,
       "axVirtualServerStatTable": axVirtualServerStatTable,
       "axVirtualServerStatEntry": axVirtualServerStatEntry,
       "axVirtualServerStatAddress": axVirtualServerStatAddress,
       "axVirtualServerStatName": axVirtualServerStatName,
       "axVirtualServerStatPktsIn": axVirtualServerStatPktsIn,
       "axVirtualServerStatBytesIn": axVirtualServerStatBytesIn,
       "axVirtualServerStatPktsOut": axVirtualServerStatPktsOut,
       "axVirtualServerStatBytesOut": axVirtualServerStatBytesOut,
       "axVirtualServerStatPersistConns": axVirtualServerStatPersistConns,
       "axVirtualServerStatTotConns": axVirtualServerStatTotConns,
       "axVirtualServerStatCurConns": axVirtualServerStatCurConns,
       "axVirtualServerStatStatus": axVirtualServerStatStatus,
       "axVirtualServerStatDisplayStatus": axVirtualServerStatDisplayStatus,
       "axVirtualServerStatTotalL7Reqs": axVirtualServerStatTotalL7Reqs,
       "axVirtualServerStatTotalCurrL7Reqs": axVirtualServerStatTotalCurrL7Reqs,
       "axVirtualServerStatTotalSuccL7Reqs": axVirtualServerStatTotalSuccL7Reqs,
       "axVirtualServerPort": axVirtualServerPort,
       "axVirtualServerPortTable": axVirtualServerPortTable,
       "axVirtualServerPortEntry": axVirtualServerPortEntry,
       "axVirtualServerPortName": axVirtualServerPortName,
       "axVirtualServerPortType": axVirtualServerPortType,
       "axVirtualServerPortNum": axVirtualServerPortNum,
       "axVirtualServerPortAddress": axVirtualServerPortAddress,
       "axVirtualServerPortEnabled": axVirtualServerPortEnabled,
       "axVirtualServerPortServiceGroup": axVirtualServerPortServiceGroup,
       "axVirtualServerPortHaGroupID": axVirtualServerPortHaGroupID,
       "axVirtualServerPortPersistTemplateType": axVirtualServerPortPersistTemplateType,
       "axVirtualServerPortPersistTempl": axVirtualServerPortPersistTempl,
       "axVirtualServerPortTemplate": axVirtualServerPortTemplate,
       "axVirtualServerPortPolicyTemplate": axVirtualServerPortPolicyTemplate,
       "axVirtualServerPortTCPTemplate": axVirtualServerPortTCPTemplate,
       "axVirtualServerPortHTTPTemplate": axVirtualServerPortHTTPTemplate,
       "axVirtualServerPortRamCacheTemplate": axVirtualServerPortRamCacheTemplate,
       "axVirtualServerPortConnReuseTemplate": axVirtualServerPortConnReuseTemplate,
       "axVirtualServerPortTCPProxyTemplate": axVirtualServerPortTCPProxyTemplate,
       "axVirtualServerPortClientSSLTemplate": axVirtualServerPortClientSSLTemplate,
       "axVirtualServerPortServerSSLTemplate": axVirtualServerPortServerSSLTemplate,
       "axVirtualServerPortRTSPTemplate": axVirtualServerPortRTSPTemplate,
       "axVirtualServerPortSMTPTemplate": axVirtualServerPortSMTPTemplate,
       "axVirtualServerPortSIPTemplate": axVirtualServerPortSIPTemplate,
       "axVirtualServerPortUDPTemplate": axVirtualServerPortUDPTemplate,
       "axVirtualServerPortDisplayStatus": axVirtualServerPortDisplayStatus,
       "axVirtualServerPortStat": axVirtualServerPortStat,
       "axVirtualServerPortStatTable": axVirtualServerPortStatTable,
       "axVirtualServerPortStatEntry": axVirtualServerPortStatEntry,
       "axVirtualServerPortStatAddress": axVirtualServerPortStatAddress,
       "axVirtualServerStatPortType": axVirtualServerStatPortType,
       "axVirtualServerStatPortNum": axVirtualServerStatPortNum,
       "axVirtualServerPortStatName": axVirtualServerPortStatName,
       "axVirtualServerStatPortStatus": axVirtualServerStatPortStatus,
       "axVirtualServerPortStatPktsIn": axVirtualServerPortStatPktsIn,
       "axVirtualServerPortStatBytesIn": axVirtualServerPortStatBytesIn,
       "axVirtualServerPortStatPktsOut": axVirtualServerPortStatPktsOut,
       "axVirtualServerPortStatBytesOut": axVirtualServerPortStatBytesOut,
       "axVirtualServerPortStatPersistConns": axVirtualServerPortStatPersistConns,
       "axVirtualServerPortStatTotConns": axVirtualServerPortStatTotConns,
       "axVirtualServerPortStatCurConns": axVirtualServerPortStatCurConns,
       "axVirtualServerStatPortDisplayStatus": axVirtualServerStatPortDisplayStatus,
       "axVirtualServerPortStatTotalL7Reqs": axVirtualServerPortStatTotalL7Reqs,
       "axVirtualServerPortStatTotalCurrL7Reqs": axVirtualServerPortStatTotalCurrL7Reqs,
       "axVirtualServerPortStatTotalSuccL7Reqs": axVirtualServerPortStatTotalSuccL7Reqs,
       "axConnReuseStats": axConnReuseStats,
       "axConnReuseStatTotalOpenPersist": axConnReuseStatTotalOpenPersist,
       "axConnReuseStatTotalActivePersist": axConnReuseStatTotalActivePersist,
       "axConnReuseStatTotalEstablished": axConnReuseStatTotalEstablished,
       "axConnReuseStatTotalTerminated": axConnReuseStatTotalTerminated,
       "axConnReuseStatTotalBound": axConnReuseStatTotalBound,
       "axConnReuseStatTotalUNBound": axConnReuseStatTotalUNBound,
       "axConnReuseStatTable": axConnReuseStatTable,
       "axConnReuseStatEntry": axConnReuseStatEntry,
       "axConnReuseStatCpuIndex": axConnReuseStatCpuIndex,
       "axConnReuseStatOpenPersist": axConnReuseStatOpenPersist,
       "axConnReuseStatActivePersist": axConnReuseStatActivePersist,
       "axConnReuseStatTotalEst": axConnReuseStatTotalEst,
       "axConnReuseStatTotalTerm": axConnReuseStatTotalTerm,
       "axConnReuseStatTotalBind": axConnReuseStatTotalBind,
       "axConnReuseStatTotalUNBind": axConnReuseStatTotalUNBind,
       "axConnReuseStatTotalDelayedUNBind": axConnReuseStatTotalDelayedUNBind,
       "axConnReuseStatTotalLongRes": axConnReuseStatTotalLongRes,
       "axConnReuseStatTotalMissedRes": axConnReuseStatTotalMissedRes,
       "axConnReuseStatTotalDelayedUNBound": axConnReuseStatTotalDelayedUNBound,
       "axConnReuseStatTotalLongResponse": axConnReuseStatTotalLongResponse,
       "axConnReuseStatTotalMissedResponse": axConnReuseStatTotalMissedResponse,
       "axFastHttpProxyStats": axFastHttpProxyStats,
       "axFastHttpProxyStatTotalConn": axFastHttpProxyStatTotalConn,
       "axFastHttpProxyStatTotalReq": axFastHttpProxyStatTotalReq,
       "axFastHttpProxyStatTotalSuccReq": axFastHttpProxyStatTotalSuccReq,
       "axFastHttpProxyStatTotalNoProxy": axFastHttpProxyStatTotalNoProxy,
       "axFastHttpProxyStatTotalCRst": axFastHttpProxyStatTotalCRst,
       "axFastHttpProxyStatTotalSRst": axFastHttpProxyStatTotalSRst,
       "axFastHttpProxyStatTotalNoTuple": axFastHttpProxyStatTotalNoTuple,
       "axFastHttpProxyStatTotalReqErr": axFastHttpProxyStatTotalReqErr,
       "axFastHttpProxyStatTotalSvrSelErr": axFastHttpProxyStatTotalSvrSelErr,
       "axFastHttpProxyStatTotalFwdReqErr": axFastHttpProxyStatTotalFwdReqErr,
       "axFastHttpProxyStatTotalFwdDataReqErr": axFastHttpProxyStatTotalFwdDataReqErr,
       "axFastHttpProxyStatTotalReqReXmit": axFastHttpProxyStatTotalReqReXmit,
       "axFastHttpProxyStatTotalReqPktOutOrder": axFastHttpProxyStatTotalReqPktOutOrder,
       "axFastHttpProxyStatTotalSvrReSel": axFastHttpProxyStatTotalSvrReSel,
       "axFastHttpProxyStatTotalPreMatureClose": axFastHttpProxyStatTotalPreMatureClose,
       "axFastHttpProxyStatTotalSvrConn": axFastHttpProxyStatTotalSvrConn,
       "axFastHttpProxyStatTotalSNATErr": axFastHttpProxyStatTotalSNATErr,
       "axFastHttpProxyStatTable": axFastHttpProxyStatTable,
       "axFastHttpProxyStatEntry": axFastHttpProxyStatEntry,
       "axFastHttpProxyStatCpuIndex": axFastHttpProxyStatCpuIndex,
       "axFastHttpProxyStatCurrProxyConns": axFastHttpProxyStatCurrProxyConns,
       "axFastHttpProxyStatTotalProxyConns": axFastHttpProxyStatTotalProxyConns,
       "axFastHttpProxyStatHttpReq": axFastHttpProxyStatHttpReq,
       "axFastHttpProxyStatHttpReqSucc": axFastHttpProxyStatHttpReqSucc,
       "axFastHttpProxyStatNoProxyErr": axFastHttpProxyStatNoProxyErr,
       "axFastHttpProxyStatClientRst": axFastHttpProxyStatClientRst,
       "axFastHttpProxyStatServerRst": axFastHttpProxyStatServerRst,
       "axFastHttpProxyStatNoTupleErr": axFastHttpProxyStatNoTupleErr,
       "axFastHttpProxyStatParseReqFail": axFastHttpProxyStatParseReqFail,
       "axFastHttpProxyStatServerSelFail": axFastHttpProxyStatServerSelFail,
       "axFastHttpProxyStatFwdReqFail": axFastHttpProxyStatFwdReqFail,
       "axFastHttpProxyStatFwdReqDataFail": axFastHttpProxyStatFwdReqDataFail,
       "axFastHttpProxyStatReqReTran": axFastHttpProxyStatReqReTran,
       "axFastHttpProxyStatReqPktOutOrder": axFastHttpProxyStatReqPktOutOrder,
       "axFastHttpProxyStatServerReSel": axFastHttpProxyStatServerReSel,
       "axFastHttpProxyStatServerPreMatureClose": axFastHttpProxyStatServerPreMatureClose,
       "axFastHttpProxyStatServerConnMade": axFastHttpProxyStatServerConnMade,
       "axHttpProxyStats": axHttpProxyStats,
       "axHttpProxyStatTotalConn": axHttpProxyStatTotalConn,
       "axHttpProxyStatTotalReq": axHttpProxyStatTotalReq,
       "axHttpProxyStatTotalSuccReq": axHttpProxyStatTotalSuccReq,
       "axHttpProxyStatTotalNoProxy": axHttpProxyStatTotalNoProxy,
       "axHttpProxyStatTotalCRst": axHttpProxyStatTotalCRst,
       "axHttpProxyStatTotalSRst": axHttpProxyStatTotalSRst,
       "axHttpProxyStatTotalNoTuple": axHttpProxyStatTotalNoTuple,
       "axHttpProxyStatTotalReqErr": axHttpProxyStatTotalReqErr,
       "axHttpProxyStatTotalSvrSelErr": axHttpProxyStatTotalSvrSelErr,
       "axHttpProxyStatTotalFwdReqErr": axHttpProxyStatTotalFwdReqErr,
       "axHttpProxyStatTotalFwdDataReqErr": axHttpProxyStatTotalFwdDataReqErr,
       "axHttpProxyStatTotalReqReXmit": axHttpProxyStatTotalReqReXmit,
       "axHttpProxyStatTotalReqPktOutOrder": axHttpProxyStatTotalReqPktOutOrder,
       "axHttpProxyStatTotalSvrReSel": axHttpProxyStatTotalSvrReSel,
       "axHttpProxyStatTotalPreMatureClose": axHttpProxyStatTotalPreMatureClose,
       "axHttpProxyStatTotalSvrConn": axHttpProxyStatTotalSvrConn,
       "axHttpProxyStatTotalSNATErr": axHttpProxyStatTotalSNATErr,
       "axHttpProxyStatTable": axHttpProxyStatTable,
       "axHttpProxyStatEntry": axHttpProxyStatEntry,
       "axHttpProxyStatCpuIndex": axHttpProxyStatCpuIndex,
       "axHttpProxyStatCurrProxyConns": axHttpProxyStatCurrProxyConns,
       "axHttpProxyStatTotalProxyConns": axHttpProxyStatTotalProxyConns,
       "axHttpProxyStatHttpReq": axHttpProxyStatHttpReq,
       "axHttpProxyStatHttpReqSucc": axHttpProxyStatHttpReqSucc,
       "axHttpProxyStatNoProxyErr": axHttpProxyStatNoProxyErr,
       "axHttpProxyStatClientRst": axHttpProxyStatClientRst,
       "axHttpProxyStatServerRst": axHttpProxyStatServerRst,
       "axHttpProxyStatNoTupleErr": axHttpProxyStatNoTupleErr,
       "axHttpProxyStatParseReqFail": axHttpProxyStatParseReqFail,
       "axHttpProxyStatServerSelFail": axHttpProxyStatServerSelFail,
       "axHttpProxyStatFwdReqFail": axHttpProxyStatFwdReqFail,
       "axHttpProxyStatFwdReqDataFail": axHttpProxyStatFwdReqDataFail,
       "axHttpProxyStatReqReTran": axHttpProxyStatReqReTran,
       "axHttpProxyStatReqPktOutOrder": axHttpProxyStatReqPktOutOrder,
       "axHttpProxyStatServerReSel": axHttpProxyStatServerReSel,
       "axHttpProxyStatServerPreMatureClose": axHttpProxyStatServerPreMatureClose,
       "axHttpProxyStatServerConnMade": axHttpProxyStatServerConnMade,
       "axTcpProxyStats": axTcpProxyStats,
       "axTcpProxyStatTotalCurrEstConn": axTcpProxyStatTotalCurrEstConn,
       "axTcpProxyStatTotalActiveOpenConn": axTcpProxyStatTotalActiveOpenConn,
       "axTcpProxyStatTotalPassiveOpenConn": axTcpProxyStatTotalPassiveOpenConn,
       "axTcpProxyStatTotalConnAttemptFail": axTcpProxyStatTotalConnAttemptFail,
       "axTcpProxyStatTotalInTCPPacket": axTcpProxyStatTotalInTCPPacket,
       "axTcpProxyStatTotalOutTCPPkt": axTcpProxyStatTotalOutTCPPkt,
       "axTcpProxyStatTotalReXmitPkt": axTcpProxyStatTotalReXmitPkt,
       "axTcpProxyStatTotalRstRcvOnEstConn": axTcpProxyStatTotalRstRcvOnEstConn,
       "axTcpProxyStatTotalRstSent": axTcpProxyStatTotalRstSent,
       "axTCPProxyStatTable": axTCPProxyStatTable,
       "axTCPProxyStatEntry": axTCPProxyStatEntry,
       "axTcpProxyStatCpuIndex": axTcpProxyStatCpuIndex,
       "axTcpProxyStatCurrEstConns": axTcpProxyStatCurrEstConns,
       "axTcpProxyStatActiveOpenConns": axTcpProxyStatActiveOpenConns,
       "axTcpProxyStatPassiveOpenConns": axTcpProxyStatPassiveOpenConns,
       "axTcpProxyStatConnAttempFail": axTcpProxyStatConnAttempFail,
       "axTcpProxyStatTotalInTCPPkt": axTcpProxyStatTotalInTCPPkt,
       "axTcpProxyStatTotalOutPkt": axTcpProxyStatTotalOutPkt,
       "axTcpProxyStatReTranPkt": axTcpProxyStatReTranPkt,
       "axTcpProxyStatRstRvdEstConn": axTcpProxyStatRstRvdEstConn,
       "axTcpProxyStatRstSent": axTcpProxyStatRstSent,
       "axTcpProxyStatInputErr": axTcpProxyStatInputErr,
       "axTcpProxyStatSocketAlloc": axTcpProxyStatSocketAlloc,
       "axTcpProxyStatOrphanSocket": axTcpProxyStatOrphanSocket,
       "axTcpProxyStatMemAlloc": axTcpProxyStatMemAlloc,
       "axTcpProxyStatTotalRxBuf": axTcpProxyStatTotalRxBuf,
       "axTcpProxyStatTotalTxBuf": axTcpProxyStatTotalTxBuf,
       "axTcpProxyStatTCPSYNSNTState": axTcpProxyStatTCPSYNSNTState,
       "axTcpProxyStatTCPSYNRCVState": axTcpProxyStatTCPSYNRCVState,
       "axTcpProxyStatTCPFINW1State": axTcpProxyStatTCPFINW1State,
       "axTcpProxyStatTCPFINW2State": axTcpProxyStatTCPFINW2State,
       "axTcpProxyStatTimeWstate": axTcpProxyStatTimeWstate,
       "axTcpProxyStatTCPCloseState": axTcpProxyStatTCPCloseState,
       "axTcpProxyStatTCPCloseWState": axTcpProxyStatTCPCloseWState,
       "axTcpProxyStatTCPLastACKState": axTcpProxyStatTCPLastACKState,
       "axTcpProxyStatTCPListenState": axTcpProxyStatTCPListenState,
       "axTcpProxyStatTCPClosingState": axTcpProxyStatTCPClosingState,
       "axSslStats": axSslStats,
       "axSslStatSSLModNum": axSslStatSSLModNum,
       "axSslStatCurrSSLConn": axSslStatCurrSSLConn,
       "axSslStatTotalSSLConn": axSslStatTotalSSLConn,
       "axSslStatFailSSLHandshake": axSslStatFailSSLHandshake,
       "axSslStatSSLMemUsage": axSslStatSSLMemUsage,
       "axSslStatTable": axSslStatTable,
       "axSslStatEntry": axSslStatEntry,
       "axSslStatModuleIndex": axSslStatModuleIndex,
       "axSslStatEnableCryptoEngine": axSslStatEnableCryptoEngine,
       "axSslStatAvailCryptoEngine": axSslStatAvailCryptoEngine,
       "axSslStatSSLFailedCAVfy": axSslStatSSLFailedCAVfy,
       "axSslStatSSLNoHWContextMem": axSslStatSSLNoHWContextMem,
       "axSslStatSSLHWRingFull": axSslStatSSLHWRingFull,
       "axSslStatSSLFailedCryptoOperation": axSslStatSSLFailedCryptoOperation,
       "axFtpStats": axFtpStats,
       "axFtpStatTotalCtrlSession": axFtpStatTotalCtrlSession,
       "axFtpStatTotalALGPkt": axFtpStatTotalALGPkt,
       "axFtpStatALGPktReXmit": axFtpStatALGPktReXmit,
       "axFtpStatOutConnCtrl": axFtpStatOutConnCtrl,
       "axFtpStatTotalDataSession": axFtpStatTotalDataSession,
       "axFtpStatOutConnData": axFtpStatOutConnData,
       "axNetStats": axNetStats,
       "axNetStatIPOutNoRoute": axNetStatIPOutNoRoute,
       "axNetStatTCPOutRst": axNetStatTCPOutRst,
       "axNetStatTCPSynRcv": axNetStatTCPSynRcv,
       "axNetStatTCPSYNCookieSent": axNetStatTCPSYNCookieSent,
       "axNetStatTCPSYNCookieSentFail": axNetStatTCPSYNCookieSentFail,
       "axNetStatTCPReceive": axNetStatTCPReceive,
       "axNetStatUDPReceive": axNetStatUDPReceive,
       "axNetStatServerSelFail": axNetStatServerSelFail,
       "axNetStatSourceNATFail": axNetStatSourceNATFail,
       "axNetStatTCPSynCookieFail": axNetStatTCPSynCookieFail,
       "axNetStatNoVportDrop": axNetStatNoVportDrop,
       "axNetStatNoSynPktDrop": axNetStatNoSynPktDrop,
       "axNetStatConnLimitDrop": axNetStatConnLimitDrop,
       "axNetStatConnLimitReset": axNetStatConnLimitReset,
       "axNetStatProxyNoSockDrop": axNetStatProxyNoSockDrop,
       "axNetStataFlexDrop": axNetStataFlexDrop,
       "axNetStatSessionAgingOut": axNetStatSessionAgingOut,
       "axNetStatTCPNoSLB": axNetStatTCPNoSLB,
       "axNetStatUDPNoSLB": axNetStatUDPNoSLB,
       "axNetStatTCPOutRSTNoSYN": axNetStatTCPOutRSTNoSYN,
       "axNetStatTCPOutRSTL4Proxy": axNetStatTCPOutRSTL4Proxy,
       "axNetStatTCPOutRSTACKattack": axNetStatTCPOutRSTACKattack,
       "axNetStatTCPOutRSTAFleX": axNetStatTCPOutRSTAFleX,
       "axNetStatTCPOutRSTStaleSess": axNetStatTCPOutRSTStaleSess,
       "axNetStatTCPOutRSTProxy": axNetStatTCPOutRSTProxy,
       "axNetStatNoSYNPktDropFIN": axNetStatNoSYNPktDropFIN,
       "axNetStatNoSYNPktDropRST": axNetStatNoSYNPktDropRST,
       "axNetStatNoSYNPktDropACK": axNetStatNoSYNPktDropACK,
       "axNetStatSYNThrotte": axNetStatSYNThrotte,
       "axNetStatSSLSIDPersistSucc": axNetStatSSLSIDPersistSucc,
       "axNetStatSSLSIDPersistFail": axNetStatSSLSIDPersistFail,
       "axNetStatClientSSLSIDNotFound": axNetStatClientSSLSIDNotFound,
       "axNetStatClientSSLSIDMatch": axNetStatClientSSLSIDMatch,
       "axNetStatClientSSLSIDNotMatch": axNetStatClientSSLSIDNotMatch,
       "axNetStatServerSSLSIDNotFound": axNetStatServerSSLSIDNotFound,
       "axNetStatServerSSLSIDReset": axNetStatServerSSLSIDReset,
       "axNetStatServerSSLSIDMatch": axNetStatServerSSLSIDMatch,
       "axNetStatServerSSLSIDNotMatch": axNetStatServerSSLSIDNotMatch,
       "axNetStatCreateSSLSIDSucc": axNetStatCreateSSLSIDSucc,
       "axNetStatCreateSSLSIDFail": axNetStatCreateSSLSIDFail,
       "axNetStatConnRateLimitDrops": axNetStatConnRateLimitDrops,
       "axNetStatConnRateLimitResets": axNetStatConnRateLimitResets,
       "axNetStatInbandHMRetry": axNetStatInbandHMRetry,
       "axNetStatInbandHMReassign": axNetStatInbandHMReassign,
       "axNetStat2TCPReceive": axNetStat2TCPReceive,
       "axNetStat2UDPReceive": axNetStat2UDPReceive,
       "axNetStatTable": axNetStatTable,
       "axNetStatEntry": axNetStatEntry,
       "axNetStatCpuIndex": axNetStatCpuIndex,
       "axNetStatIPOutNoRt": axNetStatIPOutNoRt,
       "axNetStatTCPOutReset": axNetStatTCPOutReset,
       "axNetStatTCPSynRecv": axNetStatTCPSynRecv,
       "axNetStatTCPSYNCookieSnt": axNetStatTCPSYNCookieSnt,
       "axNetStatTCPSYNCookieSntFail": axNetStatTCPSYNCookieSntFail,
       "axNetStatTCPRcv": axNetStatTCPRcv,
       "axNetStatUDPRcv": axNetStatUDPRcv,
       "axNetStatServerSelFails": axNetStatServerSelFails,
       "axNetStatSourceNATFails": axNetStatSourceNATFails,
       "axNetStatTCPSynCookieFails": axNetStatTCPSynCookieFails,
       "axNetStatNoVportDrops": axNetStatNoVportDrops,
       "axNetStatNoSynPktDrops": axNetStatNoSynPktDrops,
       "axNetStatConnLimitDrops": axNetStatConnLimitDrops,
       "axNetStatConnLimitResets": axNetStatConnLimitResets,
       "axNetStatProxyNoSockDrops": axNetStatProxyNoSockDrops,
       "axNetStataFlexDrops": axNetStataFlexDrops,
       "axNetStatSessionsAgingOut": axNetStatSessionsAgingOut,
       "axNetStatTCPsNoSLB": axNetStatTCPsNoSLB,
       "axNetStatUDPsNoSLB": axNetStatUDPsNoSLB,
       "axNetStatEntryTCPOutRSTNoSYN": axNetStatEntryTCPOutRSTNoSYN,
       "axNetStatEntryTCPOutRSTL4Proxy": axNetStatEntryTCPOutRSTL4Proxy,
       "axNetStatEntryTCPOutRSTACKattack": axNetStatEntryTCPOutRSTACKattack,
       "axNetStatEntryTCPOutRSTAFleX": axNetStatEntryTCPOutRSTAFleX,
       "axNetStatEntryTCPOutRSTStaleSess": axNetStatEntryTCPOutRSTStaleSess,
       "axNetStatEntryTCPOutRSTProxy": axNetStatEntryTCPOutRSTProxy,
       "axNetStatEntryNoSYNPktDropFIN": axNetStatEntryNoSYNPktDropFIN,
       "axNetStatEntryNoSYNPktDropRST": axNetStatEntryNoSYNPktDropRST,
       "axNetStatEntryNoSYNPktDropACK": axNetStatEntryNoSYNPktDropACK,
       "axNetStatEntrySYNThrotte": axNetStatEntrySYNThrotte,
       "axNetStatEntrySSLSIDPersistSucc": axNetStatEntrySSLSIDPersistSucc,
       "axNetStatEntrySSLSIDPersistFail": axNetStatEntrySSLSIDPersistFail,
       "axNetStatEntryClientSSLSIDNotFound": axNetStatEntryClientSSLSIDNotFound,
       "axNetStatEntryClientSSLSIDMatch": axNetStatEntryClientSSLSIDMatch,
       "axNetStatEntryClientSSLSIDNotMatch": axNetStatEntryClientSSLSIDNotMatch,
       "axNetStatEntryServerSSLSIDNotFound": axNetStatEntryServerSSLSIDNotFound,
       "axNetStatEntryServerSSLSIDReset": axNetStatEntryServerSSLSIDReset,
       "axNetStatEntryServerSSLSIDMatch": axNetStatEntryServerSSLSIDMatch,
       "axNetStatEntryServerSSLSIDNotMatch": axNetStatEntryServerSSLSIDNotMatch,
       "axNetStatEntryCreateSSLSIDSucc": axNetStatEntryCreateSSLSIDSucc,
       "axNetStatEntryCreateSSLSIDFail": axNetStatEntryCreateSSLSIDFail,
       "axNetStatEntryConnRateLimitDrops": axNetStatEntryConnRateLimitDrops,
       "axNetStatEntryConnRateLimitResets": axNetStatEntryConnRateLimitResets,
       "axNetStatEntryInbandHMRetry": axNetStatEntryInbandHMRetry,
       "axNetStatEntryInbandHMReassign": axNetStatEntryInbandHMReassign,
       "axNotification": axNotification,
       "axNotificationObjects": axNotificationObjects,
       "axNotificationMsg": axNotificationMsg,
       "axNotificationSLBServer": axNotificationSLBServer,
       "axNotificationSLBPort": axNotificationSLBPort,
       "axNotificationSLBCurConns": axNotificationSLBCurConns,
       "axNotificationVirtualServer": axNotificationVirtualServer,
       "axNotificationVirtualServerPort": axNotificationVirtualServerPort,
       "axNotificationVirtualServerPortType": axNotificationVirtualServerPortType,
       "axNotificationDropEventReason": axNotificationDropEventReason,
       "axNotificationConfiguredThreshold": axNotificationConfiguredThreshold,
       "axNotificationCurrentUsage": axNotificationCurrentUsage,
       "axNotificationConnLimit": axNotificationConnLimit,
       "axNotificationTrunkID": axNotificationTrunkID,
       "axNotificationPortThreshold": axNotificationPortThreshold,
       "axNotificationCurrentUpPorts": axNotificationCurrentUpPorts,
       "axNotificationFanName": axNotificationFanName,
       "axNotificationPowerSupplyName": axNotificationPowerSupplyName,
       "axNotifications": axNotifications,
       "axSystemNotifications": axSystemNotifications,
       "axSystemStart": axSystemStart,
       "axSystemShutdown": axSystemShutdown,
       "axSystemTempHigh": axSystemTempHigh,
       "axFan1Failure": axFan1Failure,
       "axFan2Failure": axFan2Failure,
       "axFan3Failure": axFan3Failure,
       "axUpperPowerSupplyFailure": axUpperPowerSupplyFailure,
       "axLowerPowerSupplyFailure": axLowerPowerSupplyFailure,
       "axPrimaryHardDiskFailure": axPrimaryHardDiskFailure,
       "axSecondaryHardDiskFailure": axSecondaryHardDiskFailure,
       "axHardDiskUsageHigh": axHardDiskUsageHigh,
       "axMemoryUsageHigh": axMemoryUsageHigh,
       "axSystemRestart": axSystemRestart,
       "axSystemDropPacketEvent": axSystemDropPacketEvent,
       "axSystemRelieveDropPacketEvent": axSystemRelieveDropPacketEvent,
       "axSystemControlCpuHigh": axSystemControlCpuHigh,
       "axSystemDataCpuHigh": axSystemDataCpuHigh,
       "axSystemFanFailure": axSystemFanFailure,
       "axSystemPowerSupplyFailure": axSystemPowerSupplyFailure,
       "axAppNotifications": axAppNotifications,
       "axHAStandby": axHAStandby,
       "axHAActive": axHAActive,
       "axHAActiveActive": axHAActiveActive,
       "axServiceDown": axServiceDown,
       "axServiceUp": axServiceUp,
       "axServerDown": axServerDown,
       "axServerUp": axServerUp,
       "axServerConnLimit": axServerConnLimit,
       "axServerConnResume": axServerConnResume,
       "axServiceConnLimit": axServiceConnLimit,
       "axServiceConnResume": axServiceConnResume,
       "axVirtualServerPortDown": axVirtualServerPortDown,
       "axVirtualServerPortUp": axVirtualServerPortUp,
       "axApplicationBufferReachLimit": axApplicationBufferReachLimit,
       "axVirtualServerPortReachConnLimit": axVirtualServerPortReachConnLimit,
       "axVirtualServerPortReachConnRateLimit": axVirtualServerPortReachConnRateLimit,
       "axVirtualServerReachConnLimit": axVirtualServerReachConnLimit,
       "axVirtualServerReachConnRateLimit": axVirtualServerReachConnRateLimit,
       "axServerConnRateLimit": axServerConnRateLimit,
       "axServiceConnRateLimit": axServiceConnRateLimit,
       "axNetworkNotifications": axNetworkNotifications,
       "axNetworkTrunkPortsThreshold": axNetworkTrunkPortsThreshold,
       "axSmtpProxyStats": axSmtpProxyStats,
       "axSmtpProxyStatsCurrProxyConns": axSmtpProxyStatsCurrProxyConns,
       "axSmtpProxyStatsTotalProxyConns": axSmtpProxyStatsTotalProxyConns,
       "axSmtpProxyStatsSmtpRequests": axSmtpProxyStatsSmtpRequests,
       "axSmtpProxyStatsSmtpReqSuccs": axSmtpProxyStatsSmtpReqSuccs,
       "axSmtpProxyStatsNoProxyError": axSmtpProxyStatsNoProxyError,
       "axSmtpProxyStatsClientRST": axSmtpProxyStatsClientRST,
       "axSmtpProxyStatsServerRST": axSmtpProxyStatsServerRST,
       "axSmtpProxyStatsNoTupleError": axSmtpProxyStatsNoTupleError,
       "axSmtpProxyStatsParseReqFail": axSmtpProxyStatsParseReqFail,
       "axSmtpProxyStatsServerSelFail": axSmtpProxyStatsServerSelFail,
       "axSmtpProxyStatsFwdReqFail": axSmtpProxyStatsFwdReqFail,
       "axSmtpProxyStatsFwdReqDataFail": axSmtpProxyStatsFwdReqDataFail,
       "axSmtpProxyStatsReqRetrans": axSmtpProxyStatsReqRetrans,
       "axSmtpProxyStatsReqPktOutOrder": axSmtpProxyStatsReqPktOutOrder,
       "axSmtpProxyStatsServerResel": axSmtpProxyStatsServerResel,
       "axSmtpProxyStatsSvrPrematureClose": axSmtpProxyStatsSvrPrematureClose,
       "axSmtpProxyStatsSvrConnMade": axSmtpProxyStatsSvrConnMade,
       "axSmtpProxyStatsSNATFail": axSmtpProxyStatsSNATFail,
       "axSmtpProxyStatTable": axSmtpProxyStatTable,
       "axSmtpProxyStatEntry": axSmtpProxyStatEntry,
       "axSmtpProxyStatCpuIndex": axSmtpProxyStatCpuIndex,
       "axSmtpProxyStatCurrProxyConn": axSmtpProxyStatCurrProxyConn,
       "axSmtpProxyStatTotalProxyConn": axSmtpProxyStatTotalProxyConn,
       "axSmtpProxyStatSmtpReq": axSmtpProxyStatSmtpReq,
       "axSmtpProxyStatSmtpReqSucc": axSmtpProxyStatSmtpReqSucc,
       "axSmtpProxyStatNoProxyError": axSmtpProxyStatNoProxyError,
       "axSmtpProxyStatClientRST": axSmtpProxyStatClientRST,
       "axSmtpProxyStatServerRST": axSmtpProxyStatServerRST,
       "axSmtpProxyStatNoTupleError": axSmtpProxyStatNoTupleError,
       "axSmtpProxyStatParseReqFail": axSmtpProxyStatParseReqFail,
       "axSmtpProxyStatServerSelFail": axSmtpProxyStatServerSelFail,
       "axSmtpProxyStatFwdReqFail": axSmtpProxyStatFwdReqFail,
       "axSmtpProxyStatFwdReqDataFail": axSmtpProxyStatFwdReqDataFail,
       "axSmtpProxyStatReqRetrans": axSmtpProxyStatReqRetrans,
       "axSmtpProxyStatReqPktOutOrder": axSmtpProxyStatReqPktOutOrder,
       "axSmtpProxyStatServerResel": axSmtpProxyStatServerResel,
       "axSmtpProxyStatSvrPrematureClose": axSmtpProxyStatSvrPrematureClose,
       "axSmtpProxyStatSvrConnMade": axSmtpProxyStatSvrConnMade,
       "axSmtpProxyStatSNATFail": axSmtpProxyStatSNATFail,
       "axSslProxyStats": axSslProxyStats,
       "axSslProxyStatsCurrProxyConns": axSslProxyStatsCurrProxyConns,
       "axSslProxyStatsTotalProxyConns": axSslProxyStatsTotalProxyConns,
       "axSslProxyStatsClientErr": axSslProxyStatsClientErr,
       "axSslProxyStatsServerErr": axSslProxyStatsServerErr,
       "axSslProxyStatsSessNotFound": axSslProxyStatsSessNotFound,
       "axSslProxyStatsNoRoute": axSslProxyStatsNoRoute,
       "axSslProxyStatsSvrSelFail": axSslProxyStatsSvrSelFail,
       "axSslProxyStatsSNATFail": axSslProxyStatsSNATFail,
       "axPersistentStats": axPersistentStats,
       "axPersistentStatsUrlHashPersistOKPri": axPersistentStatsUrlHashPersistOKPri,
       "axPersistentStatsUrlHashPersistOKSec": axPersistentStatsUrlHashPersistOKSec,
       "axPersistentStatsUrlHashPersistFail": axPersistentStatsUrlHashPersistFail,
       "axPersistentStatsSIPPersistOK": axPersistentStatsSIPPersistOK,
       "axPersistentStatsSIPPersistFail": axPersistentStatsSIPPersistFail,
       "axPersistentStatsSSLSIDPersistOK": axPersistentStatsSSLSIDPersistOK,
       "axPersistentStatsSSLSIDPersistFail": axPersistentStatsSSLSIDPersistFail,
       "axPersistentStatsCookiePersistOK": axPersistentStatsCookiePersistOK,
       "axPersistentStatsCookiePersistFail": axPersistentStatsCookiePersistFail,
       "axPersistentStatsPersistCookieNotFound": axPersistentStatsPersistCookieNotFound,
       "axPersistentStatTable": axPersistentStatTable,
       "axPersistentStatEntry": axPersistentStatEntry,
       "axPersistentStatCpuIndex": axPersistentStatCpuIndex,
       "axPersistentStatUrlHashPersistOKPri": axPersistentStatUrlHashPersistOKPri,
       "axPersistentStatUrlHashPersistOKSec": axPersistentStatUrlHashPersistOKSec,
       "axPersistentStatUrlHashPersistFail": axPersistentStatUrlHashPersistFail,
       "axPersistentStatSIPPersistOK": axPersistentStatSIPPersistOK,
       "axPersistentStatSIPPersistFail": axPersistentStatSIPPersistFail,
       "axPersistentStatSSLSIDPersistOK": axPersistentStatSSLSIDPersistOK,
       "axPersistentStatSSLSIDPersistFail": axPersistentStatSSLSIDPersistFail,
       "axPersistentStatCookiePersistOK": axPersistentStatCookiePersistOK,
       "axPersistentStatCookiePersistFail": axPersistentStatCookiePersistFail,
       "axPersistentStatPersistCookieNotFound": axPersistentStatPersistCookieNotFound,
       "axSwitchStats": axSwitchStats,
       "axSwitchStatsL2Forward": axSwitchStatsL2Forward,
       "axSwitchStatsL3IPForward": axSwitchStatsL3IPForward,
       "axSwitchStatsIPv4NoRouteDrop": axSwitchStatsIPv4NoRouteDrop,
       "axSwitchStatsL3IPv6Forward": axSwitchStatsL3IPv6Forward,
       "axSwitchStatsIPv6NoRouteDrop": axSwitchStatsIPv6NoRouteDrop,
       "axSwitchStatsL4Process": axSwitchStatsL4Process,
       "axSwitchStatsIncorrectLenDrop": axSwitchStatsIncorrectLenDrop,
       "axSwitchStatsProtoDownDrop": axSwitchStatsProtoDownDrop,
       "axSwitchStatsUnknownProtoDrop": axSwitchStatsUnknownProtoDrop,
       "axSwitchStatsTTLExceedDrop": axSwitchStatsTTLExceedDrop,
       "axSwitchStatsLinkdownDrop": axSwitchStatsLinkdownDrop,
       "axSwitchStatsSRCPortSuppress": axSwitchStatsSRCPortSuppress,
       "axSwitchStatsVLANFlood": axSwitchStatsVLANFlood,
       "axSwitchStatsIPFragRcv": axSwitchStatsIPFragRcv,
       "axSwitchStatsARPReqRcv": axSwitchStatsARPReqRcv,
       "axSwitchStatsARPRespRcv": axSwitchStatsARPRespRcv,
       "axSwitchStatsFwdKernel": axSwitchStatsFwdKernel,
       "axSwitchStatsIPTCPFragRcv": axSwitchStatsIPTCPFragRcv,
       "axSwitchStatsIPFragOverlap": axSwitchStatsIPFragOverlap,
       "axSwitchStatsIPFragOverlapDrop": axSwitchStatsIPFragOverlapDrop,
       "axSwitchStatsIPFragReasmOk": axSwitchStatsIPFragReasmOk,
       "axSwitchStatsIPFragReasmFail": axSwitchStatsIPFragReasmFail,
       "axSwitchStatsAnomLanAttackDrop": axSwitchStatsAnomLanAttackDrop,
       "axSwitchStatsAnomIPOptionDrop": axSwitchStatsAnomIPOptionDrop,
       "axSwitchStatsAnomPingDeathDrop": axSwitchStatsAnomPingDeathDrop,
       "axSwitchStatsAnomAllFragDrop": axSwitchStatsAnomAllFragDrop,
       "axSwitchStatsAnomTCPNoFragDrop": axSwitchStatsAnomTCPNoFragDrop,
       "axSwitchStatsAnomSYNFragDrop": axSwitchStatsAnomSYNFragDrop,
       "axSwitchStatsAnomTCPSynFinDrop": axSwitchStatsAnomTCPSynFinDrop,
       "axSwitchStatsAnomAnyDrop": axSwitchStatsAnomAnyDrop,
       "axSwitchStatTable": axSwitchStatTable,
       "axSwitchStatEntry": axSwitchStatEntry,
       "axSwitchStatCpuIndex": axSwitchStatCpuIndex,
       "axSwitchStatL2Forward": axSwitchStatL2Forward,
       "axSwitchStatL3IPForward": axSwitchStatL3IPForward,
       "axSwitchStatIPv4NoRouteDrop": axSwitchStatIPv4NoRouteDrop,
       "axSwitchStatL3IPv6Forward": axSwitchStatL3IPv6Forward,
       "axSwitchStatIPv6NoRouteDrop": axSwitchStatIPv6NoRouteDrop,
       "axSwitchStatL4Process": axSwitchStatL4Process,
       "axSwitchStatIncorrectLenDrop": axSwitchStatIncorrectLenDrop,
       "axSwitchStatProtoDownDrop": axSwitchStatProtoDownDrop,
       "axSwitchStatUnknownProtoDrop": axSwitchStatUnknownProtoDrop,
       "axSwitchStatTTLExceedDrop": axSwitchStatTTLExceedDrop,
       "axSwitchStatLinkdownDrop": axSwitchStatLinkdownDrop,
       "axSwitchStatSRCPortSuppress": axSwitchStatSRCPortSuppress,
       "axSwitchStatVLANFlood": axSwitchStatVLANFlood,
       "axSwitchStatIPFragRcv": axSwitchStatIPFragRcv,
       "axSwitchStatARPReqRcv": axSwitchStatARPReqRcv,
       "axSwitchStatARPRespRcv": axSwitchStatARPRespRcv,
       "axSwitchStatFwdKernel": axSwitchStatFwdKernel,
       "axSwitchStatIPTCPFragRcv": axSwitchStatIPTCPFragRcv,
       "axSwitchStatIPFragOverlap": axSwitchStatIPFragOverlap,
       "axSwitchStatIPFragOverlapDrop": axSwitchStatIPFragOverlapDrop,
       "axSwitchStatIPFragReasmOk": axSwitchStatIPFragReasmOk,
       "axSwitchStatIPFragReasmFail": axSwitchStatIPFragReasmFail,
       "axSwitchStatAnomLanAttackDrop": axSwitchStatAnomLanAttackDrop,
       "axSwitchStatAnomIPOptionDrop": axSwitchStatAnomIPOptionDrop,
       "axSwitchStatAnomPingDeathDrop": axSwitchStatAnomPingDeathDrop,
       "axSwitchStatAnomAllFragDrop": axSwitchStatAnomAllFragDrop,
       "axSwitchStatAnomTCPNoFragDrop": axSwitchStatAnomTCPNoFragDrop,
       "axSwitchStatAnomSYNFragDrop": axSwitchStatAnomSYNFragDrop,
       "axSwitchStatAnomTCPSynFinDrop": axSwitchStatAnomTCPSynFinDrop,
       "axSwitchStatAnomAnyDrop": axSwitchStatAnomAnyDrop,
       "axHA": axHA,
       "axHAGlobalConfig": axHAGlobalConfig,
       "axHAConfigEnabled": axHAConfigEnabled,
       "axHAID": axHAID,
       "axHASetID": axHASetID,
       "axHAPreemptStatusEnabled": axHAPreemptStatusEnabled,
       "axHATimeoutInterval": axHATimeoutInterval,
       "axHATimeoutRetry": axHATimeoutRetry,
       "axHAARPRetry": axHAARPRetry,
       "axHAGroup": axHAGroup,
       "axHAGroupCount": axHAGroupCount,
       "axHAGroupStatusTable": axHAGroupStatusTable,
       "axHAGroupStatusEntry": axHAGroupStatusEntry,
       "axHAGroupID": axHAGroupID,
       "axHAGroupLocalStatus": axHAGroupLocalStatus,
       "axHAGroupLocalPriority": axHAGroupLocalPriority,
       "axHAGroupPeerStatus": axHAGroupPeerStatus,
       "axHAGroupPeerPriority": axHAGroupPeerPriority,
       "axHAFloatingIP": axHAFloatingIP,
       "axHAFloatingIPCount": axHAFloatingIPCount,
       "axHAFloatingIPTable": axHAFloatingIPTable,
       "axHAFloatingIPEntry": axHAFloatingIPEntry,
       "axHAFloatingIPIndex": axHAFloatingIPIndex,
       "axHAFloatingIPAddress": axHAFloatingIPAddress,
       "axHAFloatingIPHaGroupID": axHAFloatingIPHaGroupID,
       "axIpNatStats": axIpNatStats,
       "axIpNatStatsGlobal": axIpNatStatsGlobal,
       "axIpNatStatsGlobalHits": axIpNatStatsGlobalHits,
       "axIpNatStatsGlobalMisses": axIpNatStatsGlobalMisses,
       "axIpNatStatsIntfInsideOutside": axIpNatStatsIntfInsideOutside,
       "axIpNatStatsIntfInsideOutsideTable": axIpNatStatsIntfInsideOutsideTable,
       "axIpNatStatsIntfInsideOutsideEntry": axIpNatStatsIntfInsideOutsideEntry,
       "axIpNatStatsInsideOutsideIntfIndex": axIpNatStatsInsideOutsideIntfIndex,
       "axIpNatStatsInsideOutsideIntfName": axIpNatStatsInsideOutsideIntfName,
       "axIpNatStatsInsideOutsideIntfDirection": axIpNatStatsInsideOutsideIntfDirection,
       "axIpNatStatsDynamicMapping": axIpNatStatsDynamicMapping,
       "axIpNatStatsDynamicMappingTable": axIpNatStatsDynamicMappingTable,
       "axIpNatStatsDynamicMappingEntry": axIpNatStatsDynamicMappingEntry,
       "axIpNatStatsDynamicMappingAccessListID": axIpNatStatsDynamicMappingAccessListID,
       "axIpNatStatsDynamicMappingPoolName": axIpNatStatsDynamicMappingPoolName,
       "axIpNatStatsDynamicMappingStartAddress": axIpNatStatsDynamicMappingStartAddress,
       "axIpNatStatsDynamicMappingEndAddress": axIpNatStatsDynamicMappingEndAddress,
       "axIpNatStatsDynamicMappingTotalAddresses": axIpNatStatsDynamicMappingTotalAddresses,
       "axIpNatStatsDynamicMappingAllocAddresses": axIpNatStatsDynamicMappingAllocAddresses,
       "axIpNatStatsDynamicMappingMissAddresses": axIpNatStatsDynamicMappingMissAddresses,
       "axIpNatLsnStats": axIpNatLsnStats,
       "axIpNatLsnGobalStats": axIpNatLsnGobalStats,
       "axIpNatLsnTotalUserQuotaSessions": axIpNatLsnTotalUserQuotaSessions,
       "axIpNatLsnTotalIpAddrTranslated": axIpNatLsnTotalIpAddrTranslated,
       "axIpNatLsnTotalFullConeSessions": axIpNatLsnTotalFullConeSessions,
       "axIpNatLsnTrafficStats": axIpNatLsnTrafficStats,
       "axIpNatLsnTrafficFullConeSessionCreated": axIpNatLsnTrafficFullConeSessionCreated,
       "axIpNatLsnTrafficFullConeSessionFreed": axIpNatLsnTrafficFullConeSessionFreed,
       "axIpNatLsnTrafficFailsInFullConeSessionCreation": axIpNatLsnTrafficFailsInFullConeSessionCreation,
       "axIpNatLsnTrafficHairpinSessionCreated": axIpNatLsnTrafficHairpinSessionCreated,
       "axIpNatLsnTrafficEndpointIndepMapMatch": axIpNatLsnTrafficEndpointIndepMapMatch,
       "axIpNatLsnTrafficEndpointIndepFilterMatch": axIpNatLsnTrafficEndpointIndepFilterMatch,
       "axIpNatLsnTrafficUserQuotasCreated": axIpNatLsnTrafficUserQuotasCreated,
       "axIpNatLsnTrafficUserQuotasFreed": axIpNatLsnTrafficUserQuotasFreed,
       "axIpNatLsnTrafficFailsInUserQuotasCreation": axIpNatLsnTrafficFailsInUserQuotasCreation,
       "axIpNatLsnTrafficIcmpUserQuotasExceeded": axIpNatLsnTrafficIcmpUserQuotasExceeded,
       "axIpNatLsnTrafficUdpUserQuotasExceeded": axIpNatLsnTrafficUdpUserQuotasExceeded,
       "axIpNatLsnTrafficTcpUserQuotasExceeded": axIpNatLsnTrafficTcpUserQuotasExceeded,
       "axIpNatLsnTrafficExtendedUserQuotasMatch": axIpNatLsnTrafficExtendedUserQuotasMatch,
       "axIpNatLsnTrafficExtendedUserQuotasExceeded": axIpNatLsnTrafficExtendedUserQuotasExceeded,
       "axIpNatLsnTrafficNatPortUnavailable": axIpNatLsnTrafficNatPortUnavailable,
       "axIpNatLsnTrafficNewUserResourceUnavailable": axIpNatLsnTrafficNewUserResourceUnavailable,
       "axIpNatLsnTop5PrivateIpAddrTotSessions": axIpNatLsnTop5PrivateIpAddrTotSessions,
       "axIpNatLsnTop5PrivateIpAddrTotSessionTable": axIpNatLsnTop5PrivateIpAddrTotSessionTable,
       "axIpNatLsnTop5PrivateIpAddrTotSessionEntry": axIpNatLsnTop5PrivateIpAddrTotSessionEntry,
       "axIpNatLsnTop5PrivateIpAddr": axIpNatLsnTop5PrivateIpAddr,
       "axIpNatLsnTop5PrivateIpAddrTotNumSessions": axIpNatLsnTop5PrivateIpAddrTotNumSessions,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddr": axIpNatLsnTop5PrivateIpAddrGlobalIpAddr,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPorts": axIpNatLsnTop5PrivateIpAddrTotTcpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPortTable": axIpNatLsnTop5PrivateIpAddrTotTcpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry": axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInTcpPort": axIpNatLsnTop5PrivateIpAddrInTcpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts": axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPorts": axIpNatLsnTop5PrivateIpAddrTotUdpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPortTable": axIpNatLsnTop5PrivateIpAddrTotUdpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry": axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInUdpPort": axIpNatLsnTop5PrivateIpAddrInUdpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts": axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPorts": axIpNatLsnTop5PrivateIpAddrTotIcmpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable": axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry": axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInIcmpPort": axIpNatLsnTop5PrivateIpAddrInIcmpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts": axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessions": axIpNatLsnTop5UserPrivateIpAddrTotSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddr": axIpNatLsnTop5UserPrivateIpAddr,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInTcp": axIpNatLsnTop5UserPrivateIpAddrInTcp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInUdp": axIpNatLsnTop5UserPrivateIpAddrInUdp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInIcmp": axIpNatLsnTop5UserPrivateIpAddrInIcmp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUsers": axIpNatLsnTop5GlobalPoolIpAddrTotUsers,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUserTable": axIpNatLsnTop5GlobalPoolIpAddrTotUserTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry": axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry,
       "axIpNatLsnTop5GlobalPoolIpAddr": axIpNatLsnTop5GlobalPoolIpAddr,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers": axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry,
       "axIpNatLsnTop5GlobalPoolIpAddrInTcp": axIpNatLsnTop5GlobalPoolIpAddrInTcp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry,
       "axIpNatLsnTop5GlobalPoolIpAddrInUdp": axIpNatLsnTop5GlobalPoolIpAddrInUdp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts,
       "axSessionStats": axSessionStats,
       "axSessionStatsGlobal": axSessionStatsGlobal,
       "axSessionGlobalStatTCPEstablished": axSessionGlobalStatTCPEstablished,
       "axSessionGlobalStatTCPHalfOpen": axSessionGlobalStatTCPHalfOpen,
       "axSessionGlobalStatUDP": axSessionGlobalStatUDP,
       "axSessionGlobalStatNonTcpUdpIPSession": axSessionGlobalStatNonTcpUdpIPSession,
       "axSessionGlobalStatOther": axSessionGlobalStatOther,
       "axSessionGlobalStatReverseNATTCP": axSessionGlobalStatReverseNATTCP,
       "axSessionGlobalStatReverseNATUDP": axSessionGlobalStatReverseNATUDP,
       "axSessionGlobalStatFreeBufferCount": axSessionGlobalStatFreeBufferCount,
       "axSessionGlobalStatFreeCurrentConns": axSessionGlobalStatFreeCurrentConns,
       "axSessionGlobalStatConnCount": axSessionGlobalStatConnCount,
       "axSessionGlobalStatConnFree": axSessionGlobalStatConnFree,
       "axSessionGlobalStatTCPSynHalfOpen": axSessionGlobalStatTCPSynHalfOpen,
       "axSessionGlobalStatConnSMPAllocated": axSessionGlobalStatConnSMPAllocated,
       "axSessionGlobalStatConnSMPFree": axSessionGlobalStatConnSMPFree}
)
