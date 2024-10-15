# SNMP MIB module (PICA-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PICA-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:39 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

picaPrivateMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35098)
)
picaPrivateMib.setRevisions(
        ("2011-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HostStatusGroup_ObjectIdentity = ObjectIdentity
hostStatusGroup = _HostStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35098, 1)
)


class _CpuUsage_Type(Integer32):
    """Custom type cpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuUsage_Type.__name__ = "Integer32"
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 1),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_TotalPhyMemory_Type = DisplayString
_TotalPhyMemory_Object = MibScalar
totalPhyMemory = _TotalPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 2),
    _TotalPhyMemory_Type()
)
totalPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPhyMemory.setStatus("current")
_UsedPhyMemory_Type = DisplayString
_UsedPhyMemory_Object = MibScalar
usedPhyMemory = _UsedPhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 3),
    _UsedPhyMemory_Type()
)
usedPhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedPhyMemory.setStatus("current")
_FreePhyMemory_Type = DisplayString
_FreePhyMemory_Object = MibScalar
freePhyMemory = _FreePhyMemory_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 4),
    _FreePhyMemory_Type()
)
freePhyMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freePhyMemory.setStatus("current")


class _SwitchTemperature_Type(Integer32):
    """Custom type switchTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SwitchTemperature_Type.__name__ = "Integer32"
_SwitchTemperature_Object = MibScalar
switchTemperature = _SwitchTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 5),
    _SwitchTemperature_Type()
)
switchTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchTemperature.setStatus("current")


class _CpuTemperature_Type(Integer32):
    """Custom type cpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CpuTemperature_Type.__name__ = "Integer32"
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 6),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")


class _SwitchChipTemperature_Type(Integer32):
    """Custom type switchChipTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_SwitchChipTemperature_Type.__name__ = "Integer32"
_SwitchChipTemperature_Object = MibScalar
switchChipTemperature = _SwitchChipTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 7),
    _SwitchChipTemperature_Type()
)
switchChipTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchChipTemperature.setStatus("current")
_SfpstatusTable_Object = MibTable
sfpstatusTable = _SfpstatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8)
)
if mibBuilder.loadTexts:
    sfpstatusTable.setStatus("current")
_SfpstatusEntry_Object = MibTableRow
sfpstatusEntry = _SfpstatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1)
)
sfpstatusEntry.setIndexNames(
    (0, "PICA-PRIVATE-MIB", "sfpIndex"),
)
if mibBuilder.loadTexts:
    sfpstatusEntry.setStatus("current")


class _SfpIndex_Type(Integer32):
    """Custom type sfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SfpIndex_Type.__name__ = "Integer32"
_SfpIndex_Object = MibTableColumn
sfpIndex = _SfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 1),
    _SfpIndex_Type()
)
sfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpIndex.setStatus("current")
_SfpVendorName_Type = DisplayString
_SfpVendorName_Object = MibTableColumn
sfpVendorName = _SfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 2),
    _SfpVendorName_Type()
)
sfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorName.setStatus("current")
_SfpSerialNumber_Type = DisplayString
_SfpSerialNumber_Object = MibTableColumn
sfpSerialNumber = _SfpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 3),
    _SfpSerialNumber_Type()
)
sfpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpSerialNumber.setStatus("current")
_SfpTemp_Type = Integer32
_SfpTemp_Object = MibTableColumn
sfpTemp = _SfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 4),
    _SfpTemp_Type()
)
sfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemp.setStatus("current")
_SfpVoltage_Type = Integer32
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 5),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
_SfpBias_Type = Integer32
_SfpBias_Object = MibTableColumn
sfpBias = _SfpBias_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 6),
    _SfpBias_Type()
)
sfpBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBias.setStatus("current")
_SfpTxPower_Type = Integer32
_SfpTxPower_Object = MibTableColumn
sfpTxPower = _SfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 7),
    _SfpTxPower_Type()
)
sfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxPower.setStatus("current")
_SfpRxPower_Type = Integer32
_SfpRxPower_Object = MibTableColumn
sfpRxPower = _SfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 8),
    _SfpRxPower_Type()
)
sfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRxPower.setStatus("current")
_SfpType_Type = DisplayString
_SfpType_Object = MibTableColumn
sfpType = _SfpType_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 8, 1, 9),
    _SfpType_Type()
)
sfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpType.setStatus("current")
_RpsustatusTable_Object = MibTable
rpsustatusTable = _RpsustatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 9)
)
if mibBuilder.loadTexts:
    rpsustatusTable.setStatus("current")
_RpsustatusEntry_Object = MibTableRow
rpsustatusEntry = _RpsustatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 9, 1)
)
rpsustatusEntry.setIndexNames(
    (0, "PICA-PRIVATE-MIB", "rpsuIndex"),
)
if mibBuilder.loadTexts:
    rpsustatusEntry.setStatus("current")


class _RpsuIndex_Type(Integer32):
    """Custom type rpsuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpsuIndex_Type.__name__ = "Integer32"
_RpsuIndex_Object = MibTableColumn
rpsuIndex = _RpsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 9, 1, 1),
    _RpsuIndex_Type()
)
rpsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsuIndex.setStatus("current")


class _RpsuStatus_Type(Integer32):
    """Custom type rpsuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RpsuStatus_Type.__name__ = "Integer32"
_RpsuStatus_Object = MibTableColumn
rpsuStatus = _RpsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 35098, 1, 9, 1, 2),
    _RpsuStatus_Type()
)
rpsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpsuStatus.setStatus("current")
_SwitchConfigGroup_ObjectIdentity = ObjectIdentity
switchConfigGroup = _SwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35098, 2)
)


class _TftpConfigFilePath_Type(OctetString):
    """Custom type tftpConfigFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_TftpConfigFilePath_Type.__name__ = "OctetString"
_TftpConfigFilePath_Object = MibScalar
tftpConfigFilePath = _TftpConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35098, 2, 0),
    _TftpConfigFilePath_Type()
)
tftpConfigFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpConfigFilePath.setStatus("current")


class _TftpBatchFilePath_Type(OctetString):
    """Custom type tftpBatchFilePath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_TftpBatchFilePath_Type.__name__ = "OctetString"
_TftpBatchFilePath_Object = MibScalar
tftpBatchFilePath = _TftpBatchFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35098, 2, 1),
    _TftpBatchFilePath_Type()
)
tftpBatchFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpBatchFilePath.setStatus("current")
_PicaConformance_ObjectIdentity = ObjectIdentity
picaConformance = _PicaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35098, 20)
)
_PicaGroups_ObjectIdentity = ObjectIdentity
picaGroups = _PicaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35098, 20, 1)
)
_PicaCompliances_ObjectIdentity = ObjectIdentity
picaCompliances = _PicaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35098, 20, 2)
)

# Managed Objects groups

picaBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35098, 20, 1, 1)
)
picaBasicGroup.setObjects(
      *(("PICA-PRIVATE-MIB", "cpuUsage"),
        ("PICA-PRIVATE-MIB", "totalPhyMemory"),
        ("PICA-PRIVATE-MIB", "usedPhyMemory"),
        ("PICA-PRIVATE-MIB", "freePhyMemory"),
        ("PICA-PRIVATE-MIB", "switchTemperature"),
        ("PICA-PRIVATE-MIB", "cpuTemperature"),
        ("PICA-PRIVATE-MIB", "switchChipTemperature"))
)
if mibBuilder.loadTexts:
    picaBasicGroup.setStatus("current")

picasfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35098, 20, 1, 2)
)
picasfpGroup.setObjects(
      *(("PICA-PRIVATE-MIB", "sfpIndex"),
        ("PICA-PRIVATE-MIB", "sfpVendorName"),
        ("PICA-PRIVATE-MIB", "sfpSerialNumber"),
        ("PICA-PRIVATE-MIB", "sfpTemp"),
        ("PICA-PRIVATE-MIB", "sfpVoltage"),
        ("PICA-PRIVATE-MIB", "sfpBias"),
        ("PICA-PRIVATE-MIB", "sfpTxPower"),
        ("PICA-PRIVATE-MIB", "sfpRxPower"),
        ("PICA-PRIVATE-MIB", "sfpType"))
)
if mibBuilder.loadTexts:
    picasfpGroup.setStatus("current")

picarpsuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35098, 20, 1, 3)
)
picarpsuGroup.setObjects(
      *(("PICA-PRIVATE-MIB", "rpsuIndex"),
        ("PICA-PRIVATE-MIB", "rpsuStatus"))
)
if mibBuilder.loadTexts:
    picarpsuGroup.setStatus("current")

picaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35098, 20, 1, 4)
)
picaConfigGroup.setObjects(
      *(("PICA-PRIVATE-MIB", "tftpConfigFilePath"),
        ("PICA-PRIVATE-MIB", "tftpBatchFilePath"))
)
if mibBuilder.loadTexts:
    picaConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

picaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35098, 20, 2, 1)
)
if mibBuilder.loadTexts:
    picaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PICA-PRIVATE-MIB",
    **{"picaPrivateMib": picaPrivateMib,
       "hostStatusGroup": hostStatusGroup,
       "cpuUsage": cpuUsage,
       "totalPhyMemory": totalPhyMemory,
       "usedPhyMemory": usedPhyMemory,
       "freePhyMemory": freePhyMemory,
       "switchTemperature": switchTemperature,
       "cpuTemperature": cpuTemperature,
       "switchChipTemperature": switchChipTemperature,
       "sfpstatusTable": sfpstatusTable,
       "sfpstatusEntry": sfpstatusEntry,
       "sfpIndex": sfpIndex,
       "sfpVendorName": sfpVendorName,
       "sfpSerialNumber": sfpSerialNumber,
       "sfpTemp": sfpTemp,
       "sfpVoltage": sfpVoltage,
       "sfpBias": sfpBias,
       "sfpTxPower": sfpTxPower,
       "sfpRxPower": sfpRxPower,
       "sfpType": sfpType,
       "rpsustatusTable": rpsustatusTable,
       "rpsustatusEntry": rpsustatusEntry,
       "rpsuIndex": rpsuIndex,
       "rpsuStatus": rpsuStatus,
       "switchConfigGroup": switchConfigGroup,
       "tftpConfigFilePath": tftpConfigFilePath,
       "tftpBatchFilePath": tftpBatchFilePath,
       "picaConformance": picaConformance,
       "picaGroups": picaGroups,
       "picaBasicGroup": picaBasicGroup,
       "picasfpGroup": picasfpGroup,
       "picarpsuGroup": picarpsuGroup,
       "picaConfigGroup": picaConfigGroup,
       "picaCompliances": picaCompliances,
       "picaCompliance": picaCompliance}
)
