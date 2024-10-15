# SNMP MIB module (CNT251-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNT251-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:00 2024
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

(cnt2CfgSystemProbe,) = mibBuilder.importSymbols(
    "CNT25-MIB",
    "cnt2CfgSystemProbe")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Cnt2SysChassisType_Type(Integer32):
    """Custom type cnt2SysChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              6,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("osg", 13),
          ("slot-12", 12),
          ("slot-2", 2),
          ("slot-6", 6),
          ("tm", 17),
          ("usd12", 16),
          ("usd6", 15),
          ("usg", 14))
    )


_Cnt2SysChassisType_Type.__name__ = "Integer32"
_Cnt2SysChassisType_Object = MibScalar
cnt2SysChassisType = _Cnt2SysChassisType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 1),
    _Cnt2SysChassisType_Type()
)
cnt2SysChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysChassisType.setStatus("mandatory")


class _Cnt2SysZachCardType_Type(Integer32):
    """Custom type cnt2SysZachCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 1),
          ("rs232", 2))
    )


_Cnt2SysZachCardType_Type.__name__ = "Integer32"
_Cnt2SysZachCardType_Object = MibScalar
cnt2SysZachCardType = _Cnt2SysZachCardType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 2),
    _Cnt2SysZachCardType_Type()
)
cnt2SysZachCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysZachCardType.setStatus("mandatory")
_Cnt2SysHmbFirmwareRevision_Type = Integer32
_Cnt2SysHmbFirmwareRevision_Object = MibScalar
cnt2SysHmbFirmwareRevision = _Cnt2SysHmbFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 3),
    _Cnt2SysHmbFirmwareRevision_Type()
)
cnt2SysHmbFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysHmbFirmwareRevision.setStatus("mandatory")
_Cnt2SysScnrcVersion_Type = Integer32
_Cnt2SysScnrcVersion_Object = MibScalar
cnt2SysScnrcVersion = _Cnt2SysScnrcVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 4),
    _Cnt2SysScnrcVersion_Type()
)
cnt2SysScnrcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysScnrcVersion.setStatus("mandatory")


class _Cnt2SysDatPresent_Type(Integer32):
    """Custom type cnt2SysDatPresent based on Integer32"""
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


_Cnt2SysDatPresent_Type.__name__ = "Integer32"
_Cnt2SysDatPresent_Object = MibScalar
cnt2SysDatPresent = _Cnt2SysDatPresent_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 5),
    _Cnt2SysDatPresent_Type()
)
cnt2SysDatPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysDatPresent.setStatus("mandatory")


class _Cnt2SysCdRomPresent_Type(Integer32):
    """Custom type cnt2SysCdRomPresent based on Integer32"""
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


_Cnt2SysCdRomPresent_Type.__name__ = "Integer32"
_Cnt2SysCdRomPresent_Object = MibScalar
cnt2SysCdRomPresent = _Cnt2SysCdRomPresent_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 6),
    _Cnt2SysCdRomPresent_Type()
)
cnt2SysCdRomPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCdRomPresent.setStatus("mandatory")
_Cnt2SysProbeDateTime_Type = DisplayString
_Cnt2SysProbeDateTime_Object = MibScalar
cnt2SysProbeDateTime = _Cnt2SysProbeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 7),
    _Cnt2SysProbeDateTime_Type()
)
cnt2SysProbeDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysProbeDateTime.setStatus("mandatory")
_Cnt2SysSlotCount_Type = Integer32
_Cnt2SysSlotCount_Object = MibScalar
cnt2SysSlotCount = _Cnt2SysSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 8),
    _Cnt2SysSlotCount_Type()
)
cnt2SysSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysSlotCount.setStatus("mandatory")
_Cnt2SysPowerSupplyTable_Object = MibTable
cnt2SysPowerSupplyTable = _Cnt2SysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 9)
)
if mibBuilder.loadTexts:
    cnt2SysPowerSupplyTable.setStatus("mandatory")
_Cnt2SysPowerSupplyEntry_Object = MibTableRow
cnt2SysPowerSupplyEntry = _Cnt2SysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 9, 1)
)
cnt2SysPowerSupplyEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysPowerSupplyEntry.setStatus("mandatory")
_Cnt2SysPowerSupplyIndex_Type = Integer32
_Cnt2SysPowerSupplyIndex_Object = MibTableColumn
cnt2SysPowerSupplyIndex = _Cnt2SysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 9, 1, 1),
    _Cnt2SysPowerSupplyIndex_Type()
)
cnt2SysPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysPowerSupplyIndex.setStatus("mandatory")


class _Cnt2SysPowerSupplyPresent_Type(Integer32):
    """Custom type cnt2SysPowerSupplyPresent based on Integer32"""
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


_Cnt2SysPowerSupplyPresent_Type.__name__ = "Integer32"
_Cnt2SysPowerSupplyPresent_Object = MibTableColumn
cnt2SysPowerSupplyPresent = _Cnt2SysPowerSupplyPresent_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 9, 1, 2),
    _Cnt2SysPowerSupplyPresent_Type()
)
cnt2SysPowerSupplyPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysPowerSupplyPresent.setStatus("mandatory")
_Cnt2SysFanTable_Object = MibTable
cnt2SysFanTable = _Cnt2SysFanTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 10)
)
if mibBuilder.loadTexts:
    cnt2SysFanTable.setStatus("mandatory")
_Cnt2SysFanEntry_Object = MibTableRow
cnt2SysFanEntry = _Cnt2SysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 10, 1)
)
cnt2SysFanEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysFanIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysFanEntry.setStatus("mandatory")
_Cnt2SysFanIndex_Type = Integer32
_Cnt2SysFanIndex_Object = MibTableColumn
cnt2SysFanIndex = _Cnt2SysFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 10, 1, 1),
    _Cnt2SysFanIndex_Type()
)
cnt2SysFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysFanIndex.setStatus("mandatory")


class _Cnt2SysFanPresent_Type(Integer32):
    """Custom type cnt2SysFanPresent based on Integer32"""
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


_Cnt2SysFanPresent_Type.__name__ = "Integer32"
_Cnt2SysFanPresent_Object = MibTableColumn
cnt2SysFanPresent = _Cnt2SysFanPresent_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 10, 1, 2),
    _Cnt2SysFanPresent_Type()
)
cnt2SysFanPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysFanPresent.setStatus("mandatory")
_Cnt2SysAdapterTable_Object = MibTable
cnt2SysAdapterTable = _Cnt2SysAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11)
)
if mibBuilder.loadTexts:
    cnt2SysAdapterTable.setStatus("mandatory")
_Cnt2SysAdapterEntry_Object = MibTableRow
cnt2SysAdapterEntry = _Cnt2SysAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1)
)
cnt2SysAdapterEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysAdapterIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysAdapterEntry.setStatus("mandatory")
_Cnt2SysAdapterIndex_Type = Integer32
_Cnt2SysAdapterIndex_Object = MibTableColumn
cnt2SysAdapterIndex = _Cnt2SysAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 1),
    _Cnt2SysAdapterIndex_Type()
)
cnt2SysAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterIndex.setStatus("mandatory")


class _Cnt2SysAdapterType_Type(Integer32):
    """Custom type cnt2SysAdapterType based on Integer32"""
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
        *(("absent", 2),
          ("escon", 4),
          ("ppc", 5),
          ("sparc", 3),
          ("unknown", 1))
    )


_Cnt2SysAdapterType_Type.__name__ = "Integer32"
_Cnt2SysAdapterType_Object = MibTableColumn
cnt2SysAdapterType = _Cnt2SysAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 2),
    _Cnt2SysAdapterType_Type()
)
cnt2SysAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterType.setStatus("mandatory")


class _Cnt2SysAdapterName_Type(Integer32):
    """Custom type cnt2SysAdapterName based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("o1x1", 15),
          ("unknown", 2),
          ("usg1", 10),
          ("usg2", 11),
          ("zap1", 5),
          ("zap2", 8),
          ("zap3", 12),
          ("zap4", 13),
          ("zen1", 4),
          ("zen2", 7),
          ("zen3", 9),
          ("zen4", 14),
          ("zsp1", 3),
          ("zsp2", 6))
    )


_Cnt2SysAdapterName_Type.__name__ = "Integer32"
_Cnt2SysAdapterName_Object = MibTableColumn
cnt2SysAdapterName = _Cnt2SysAdapterName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 3),
    _Cnt2SysAdapterName_Type()
)
cnt2SysAdapterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterName.setStatus("mandatory")
_Cnt2SysAdapterPartNumber_Type = Integer32
_Cnt2SysAdapterPartNumber_Object = MibTableColumn
cnt2SysAdapterPartNumber = _Cnt2SysAdapterPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 4),
    _Cnt2SysAdapterPartNumber_Type()
)
cnt2SysAdapterPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterPartNumber.setStatus("mandatory")
_Cnt2SysAdapterSerialNumber_Type = DisplayString
_Cnt2SysAdapterSerialNumber_Object = MibTableColumn
cnt2SysAdapterSerialNumber = _Cnt2SysAdapterSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 5),
    _Cnt2SysAdapterSerialNumber_Type()
)
cnt2SysAdapterSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterSerialNumber.setStatus("mandatory")
_Cnt2SysAdapterHostId_Type = DisplayString
_Cnt2SysAdapterHostId_Object = MibTableColumn
cnt2SysAdapterHostId = _Cnt2SysAdapterHostId_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 6),
    _Cnt2SysAdapterHostId_Type()
)
cnt2SysAdapterHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterHostId.setStatus("mandatory")
_Cnt2SysAdapterBoardRevision_Type = DisplayString
_Cnt2SysAdapterBoardRevision_Object = MibTableColumn
cnt2SysAdapterBoardRevision = _Cnt2SysAdapterBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 7),
    _Cnt2SysAdapterBoardRevision_Type()
)
cnt2SysAdapterBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterBoardRevision.setStatus("mandatory")
_Cnt2SysAdapterFirmwareMajorRevision_Type = Integer32
_Cnt2SysAdapterFirmwareMajorRevision_Object = MibTableColumn
cnt2SysAdapterFirmwareMajorRevision = _Cnt2SysAdapterFirmwareMajorRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 8),
    _Cnt2SysAdapterFirmwareMajorRevision_Type()
)
cnt2SysAdapterFirmwareMajorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterFirmwareMajorRevision.setStatus("mandatory")
_Cnt2SysAdapterFirmwareMinorRevision_Type = Integer32
_Cnt2SysAdapterFirmwareMinorRevision_Object = MibTableColumn
cnt2SysAdapterFirmwareMinorRevision = _Cnt2SysAdapterFirmwareMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 9),
    _Cnt2SysAdapterFirmwareMinorRevision_Type()
)
cnt2SysAdapterFirmwareMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterFirmwareMinorRevision.setStatus("mandatory")
_Cnt2SysAdapterHostName_Type = DisplayString
_Cnt2SysAdapterHostName_Object = MibTableColumn
cnt2SysAdapterHostName = _Cnt2SysAdapterHostName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 10),
    _Cnt2SysAdapterHostName_Type()
)
cnt2SysAdapterHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterHostName.setStatus("mandatory")
_Cnt2SysAdapterOsName_Type = DisplayString
_Cnt2SysAdapterOsName_Object = MibTableColumn
cnt2SysAdapterOsName = _Cnt2SysAdapterOsName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 11),
    _Cnt2SysAdapterOsName_Type()
)
cnt2SysAdapterOsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterOsName.setStatus("mandatory")
_Cnt2SysAdapterOsMajorVersion_Type = Integer32
_Cnt2SysAdapterOsMajorVersion_Object = MibTableColumn
cnt2SysAdapterOsMajorVersion = _Cnt2SysAdapterOsMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 12),
    _Cnt2SysAdapterOsMajorVersion_Type()
)
cnt2SysAdapterOsMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterOsMajorVersion.setStatus("mandatory")
_Cnt2SysAdapterOsMinorVersion_Type = Integer32
_Cnt2SysAdapterOsMinorVersion_Object = MibTableColumn
cnt2SysAdapterOsMinorVersion = _Cnt2SysAdapterOsMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 13),
    _Cnt2SysAdapterOsMinorVersion_Type()
)
cnt2SysAdapterOsMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterOsMinorVersion.setStatus("mandatory")


class _Cnt2SysAdapterServiceMonitorStatus_Type(Integer32):
    """Custom type cnt2SysAdapterServiceMonitorStatus based on Integer32"""
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
          ("primary", 2),
          ("secondary", 3))
    )


_Cnt2SysAdapterServiceMonitorStatus_Type.__name__ = "Integer32"
_Cnt2SysAdapterServiceMonitorStatus_Object = MibTableColumn
cnt2SysAdapterServiceMonitorStatus = _Cnt2SysAdapterServiceMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 11, 1, 14),
    _Cnt2SysAdapterServiceMonitorStatus_Type()
)
cnt2SysAdapterServiceMonitorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysAdapterServiceMonitorStatus.setStatus("mandatory")
_Cnt2SysBusTable_Object = MibTable
cnt2SysBusTable = _Cnt2SysBusTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 12)
)
if mibBuilder.loadTexts:
    cnt2SysBusTable.setStatus("mandatory")
_Cnt2SysBusEntry_Object = MibTableRow
cnt2SysBusEntry = _Cnt2SysBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 12, 1)
)
cnt2SysBusEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysBusAdapterIndex"),
    (0, "CNT251-MIB", "cnt2SysBusIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysBusEntry.setStatus("mandatory")
_Cnt2SysBusAdapterIndex_Type = Integer32
_Cnt2SysBusAdapterIndex_Object = MibTableColumn
cnt2SysBusAdapterIndex = _Cnt2SysBusAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 12, 1, 1),
    _Cnt2SysBusAdapterIndex_Type()
)
cnt2SysBusAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysBusAdapterIndex.setStatus("mandatory")
_Cnt2SysBusIndex_Type = Integer32
_Cnt2SysBusIndex_Object = MibTableColumn
cnt2SysBusIndex = _Cnt2SysBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 12, 1, 2),
    _Cnt2SysBusIndex_Type()
)
cnt2SysBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysBusIndex.setStatus("mandatory")


class _Cnt2SysBusType_Type(Integer32):
    """Custom type cnt2SysBusType based on Integer32"""
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
        *(("pci", 3),
          ("sbus", 2),
          ("unknown", 1),
          ("vme", 4))
    )


_Cnt2SysBusType_Type.__name__ = "Integer32"
_Cnt2SysBusType_Object = MibTableColumn
cnt2SysBusType = _Cnt2SysBusType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 12, 1, 3),
    _Cnt2SysBusType_Type()
)
cnt2SysBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysBusType.setStatus("mandatory")
_Cnt2SysCardTable_Object = MibTable
cnt2SysCardTable = _Cnt2SysCardTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13)
)
if mibBuilder.loadTexts:
    cnt2SysCardTable.setStatus("mandatory")
_Cnt2SysCardEntry_Object = MibTableRow
cnt2SysCardEntry = _Cnt2SysCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1)
)
cnt2SysCardEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysCardAdapterIndex"),
    (0, "CNT251-MIB", "cnt2SysCardBusIndex"),
    (0, "CNT251-MIB", "cnt2SysCardIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysCardEntry.setStatus("mandatory")
_Cnt2SysCardAdapterIndex_Type = Integer32
_Cnt2SysCardAdapterIndex_Object = MibTableColumn
cnt2SysCardAdapterIndex = _Cnt2SysCardAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 1),
    _Cnt2SysCardAdapterIndex_Type()
)
cnt2SysCardAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardAdapterIndex.setStatus("mandatory")
_Cnt2SysCardBusIndex_Type = Integer32
_Cnt2SysCardBusIndex_Object = MibTableColumn
cnt2SysCardBusIndex = _Cnt2SysCardBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 2),
    _Cnt2SysCardBusIndex_Type()
)
cnt2SysCardBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardBusIndex.setStatus("mandatory")
_Cnt2SysCardIndex_Type = Integer32
_Cnt2SysCardIndex_Object = MibTableColumn
cnt2SysCardIndex = _Cnt2SysCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 3),
    _Cnt2SysCardIndex_Type()
)
cnt2SysCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardIndex.setStatus("mandatory")


class _Cnt2SysCardFunction_Type(Integer32):
    """Custom type cnt2SysCardFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compression", 3),
          ("interface", 2),
          ("unknown", 1))
    )


_Cnt2SysCardFunction_Type.__name__ = "Integer32"
_Cnt2SysCardFunction_Object = MibTableColumn
cnt2SysCardFunction = _Cnt2SysCardFunction_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 4),
    _Cnt2SysCardFunction_Type()
)
cnt2SysCardFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardFunction.setStatus("mandatory")
_Cnt2SysCardFirmwareMajorRevision_Type = Integer32
_Cnt2SysCardFirmwareMajorRevision_Object = MibTableColumn
cnt2SysCardFirmwareMajorRevision = _Cnt2SysCardFirmwareMajorRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 5),
    _Cnt2SysCardFirmwareMajorRevision_Type()
)
cnt2SysCardFirmwareMajorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardFirmwareMajorRevision.setStatus("mandatory")
_Cnt2SysCardFirmwareMinorRevision_Type = Integer32
_Cnt2SysCardFirmwareMinorRevision_Object = MibTableColumn
cnt2SysCardFirmwareMinorRevision = _Cnt2SysCardFirmwareMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 6),
    _Cnt2SysCardFirmwareMinorRevision_Type()
)
cnt2SysCardFirmwareMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardFirmwareMinorRevision.setStatus("mandatory")
_Cnt2SysCardVendorOctetString_Type = DisplayString
_Cnt2SysCardVendorOctetString_Object = MibTableColumn
cnt2SysCardVendorOctetString = _Cnt2SysCardVendorOctetString_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 7),
    _Cnt2SysCardVendorOctetString_Type()
)
cnt2SysCardVendorOctetString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardVendorOctetString.setStatus("mandatory")
_Cnt2SysCardVendorDisplayString_Type = DisplayString
_Cnt2SysCardVendorDisplayString_Object = MibTableColumn
cnt2SysCardVendorDisplayString = _Cnt2SysCardVendorDisplayString_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 13, 1, 8),
    _Cnt2SysCardVendorDisplayString_Type()
)
cnt2SysCardVendorDisplayString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysCardVendorDisplayString.setStatus("mandatory")
_Cnt2SysIfTable_Object = MibTable
cnt2SysIfTable = _Cnt2SysIfTable_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14)
)
if mibBuilder.loadTexts:
    cnt2SysIfTable.setStatus("mandatory")
_Cnt2SysIfEntry_Object = MibTableRow
cnt2SysIfEntry = _Cnt2SysIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1)
)
cnt2SysIfEntry.setIndexNames(
    (0, "CNT251-MIB", "cnt2SysIfAdapterIndex"),
    (0, "CNT251-MIB", "cnt2SysIfBusIndex"),
    (0, "CNT251-MIB", "cnt2SysIfIndex"),
)
if mibBuilder.loadTexts:
    cnt2SysIfEntry.setStatus("mandatory")
_Cnt2SysIfAdapterIndex_Type = Integer32
_Cnt2SysIfAdapterIndex_Object = MibTableColumn
cnt2SysIfAdapterIndex = _Cnt2SysIfAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 1),
    _Cnt2SysIfAdapterIndex_Type()
)
cnt2SysIfAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfAdapterIndex.setStatus("mandatory")
_Cnt2SysIfBusIndex_Type = Integer32
_Cnt2SysIfBusIndex_Object = MibTableColumn
cnt2SysIfBusIndex = _Cnt2SysIfBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 2),
    _Cnt2SysIfBusIndex_Type()
)
cnt2SysIfBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfBusIndex.setStatus("mandatory")
_Cnt2SysIfIndex_Type = Integer32
_Cnt2SysIfIndex_Object = MibTableColumn
cnt2SysIfIndex = _Cnt2SysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 3),
    _Cnt2SysIfIndex_Type()
)
cnt2SysIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfIndex.setStatus("mandatory")


class _Cnt2SysIfType_Type(Integer32):
    """Custom type cnt2SysIfType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("async", 3),
          ("atm", 5),
          ("ds3", 9),
          ("escon", 4),
          ("ethernetCsmacd", 2),
          ("fastEther", 11),
          ("fddi", 10),
          ("fibreChannel", 6),
          ("gigabitEthernet", 13),
          ("isdn", 12),
          ("scsi-2", 7),
          ("scsi-3", 8),
          ("unknown", 1))
    )


_Cnt2SysIfType_Type.__name__ = "Integer32"
_Cnt2SysIfType_Object = MibTableColumn
cnt2SysIfType = _Cnt2SysIfType_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 4),
    _Cnt2SysIfType_Type()
)
cnt2SysIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfType.setStatus("mandatory")
_Cnt2SysIfCardIndex_Type = Integer32
_Cnt2SysIfCardIndex_Object = MibTableColumn
cnt2SysIfCardIndex = _Cnt2SysIfCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 5),
    _Cnt2SysIfCardIndex_Type()
)
cnt2SysIfCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfCardIndex.setStatus("mandatory")
_Cnt2SysIfName_Type = DisplayString
_Cnt2SysIfName_Object = MibTableColumn
cnt2SysIfName = _Cnt2SysIfName_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 6),
    _Cnt2SysIfName_Type()
)
cnt2SysIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfName.setStatus("mandatory")


class _Cnt2SysIfConnector_Type(Integer32):
    """Custom type cnt2SysIfConnector based on Integer32"""
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
        *(("absent", 1),
          ("bnc", 8),
          ("hssdc", 9),
          ("micro-d15", 3),
          ("rj45", 7),
          ("rsd-duplex", 10),
          ("sc-duplex", 6),
          ("scsi-2", 4),
          ("scsi-3", 5),
          ("unknown", 2))
    )


_Cnt2SysIfConnector_Type.__name__ = "Integer32"
_Cnt2SysIfConnector_Object = MibTableColumn
cnt2SysIfConnector = _Cnt2SysIfConnector_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 7),
    _Cnt2SysIfConnector_Type()
)
cnt2SysIfConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfConnector.setStatus("mandatory")
_Cnt2SysIfSnmpIndex_Type = Integer32
_Cnt2SysIfSnmpIndex_Object = MibTableColumn
cnt2SysIfSnmpIndex = _Cnt2SysIfSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 14, 1, 8),
    _Cnt2SysIfSnmpIndex_Type()
)
cnt2SysIfSnmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysIfSnmpIndex.setStatus("mandatory")
_Cnt2SysSerialNumber_Type = DisplayString
_Cnt2SysSerialNumber_Object = MibScalar
cnt2SysSerialNumber = _Cnt2SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 15),
    _Cnt2SysSerialNumber_Type()
)
cnt2SysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysSerialNumber.setStatus("mandatory")
_Cnt2SysOsVersion_Type = DisplayString
_Cnt2SysOsVersion_Object = MibScalar
cnt2SysOsVersion = _Cnt2SysOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 333, 2, 5, 1, 16),
    _Cnt2SysOsVersion_Type()
)
cnt2SysOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnt2SysOsVersion.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNT251-MIB",
    **{"cnt2SysChassisType": cnt2SysChassisType,
       "cnt2SysZachCardType": cnt2SysZachCardType,
       "cnt2SysHmbFirmwareRevision": cnt2SysHmbFirmwareRevision,
       "cnt2SysScnrcVersion": cnt2SysScnrcVersion,
       "cnt2SysDatPresent": cnt2SysDatPresent,
       "cnt2SysCdRomPresent": cnt2SysCdRomPresent,
       "cnt2SysProbeDateTime": cnt2SysProbeDateTime,
       "cnt2SysSlotCount": cnt2SysSlotCount,
       "cnt2SysPowerSupplyTable": cnt2SysPowerSupplyTable,
       "cnt2SysPowerSupplyEntry": cnt2SysPowerSupplyEntry,
       "cnt2SysPowerSupplyIndex": cnt2SysPowerSupplyIndex,
       "cnt2SysPowerSupplyPresent": cnt2SysPowerSupplyPresent,
       "cnt2SysFanTable": cnt2SysFanTable,
       "cnt2SysFanEntry": cnt2SysFanEntry,
       "cnt2SysFanIndex": cnt2SysFanIndex,
       "cnt2SysFanPresent": cnt2SysFanPresent,
       "cnt2SysAdapterTable": cnt2SysAdapterTable,
       "cnt2SysAdapterEntry": cnt2SysAdapterEntry,
       "cnt2SysAdapterIndex": cnt2SysAdapterIndex,
       "cnt2SysAdapterType": cnt2SysAdapterType,
       "cnt2SysAdapterName": cnt2SysAdapterName,
       "cnt2SysAdapterPartNumber": cnt2SysAdapterPartNumber,
       "cnt2SysAdapterSerialNumber": cnt2SysAdapterSerialNumber,
       "cnt2SysAdapterHostId": cnt2SysAdapterHostId,
       "cnt2SysAdapterBoardRevision": cnt2SysAdapterBoardRevision,
       "cnt2SysAdapterFirmwareMajorRevision": cnt2SysAdapterFirmwareMajorRevision,
       "cnt2SysAdapterFirmwareMinorRevision": cnt2SysAdapterFirmwareMinorRevision,
       "cnt2SysAdapterHostName": cnt2SysAdapterHostName,
       "cnt2SysAdapterOsName": cnt2SysAdapterOsName,
       "cnt2SysAdapterOsMajorVersion": cnt2SysAdapterOsMajorVersion,
       "cnt2SysAdapterOsMinorVersion": cnt2SysAdapterOsMinorVersion,
       "cnt2SysAdapterServiceMonitorStatus": cnt2SysAdapterServiceMonitorStatus,
       "cnt2SysBusTable": cnt2SysBusTable,
       "cnt2SysBusEntry": cnt2SysBusEntry,
       "cnt2SysBusAdapterIndex": cnt2SysBusAdapterIndex,
       "cnt2SysBusIndex": cnt2SysBusIndex,
       "cnt2SysBusType": cnt2SysBusType,
       "cnt2SysCardTable": cnt2SysCardTable,
       "cnt2SysCardEntry": cnt2SysCardEntry,
       "cnt2SysCardAdapterIndex": cnt2SysCardAdapterIndex,
       "cnt2SysCardBusIndex": cnt2SysCardBusIndex,
       "cnt2SysCardIndex": cnt2SysCardIndex,
       "cnt2SysCardFunction": cnt2SysCardFunction,
       "cnt2SysCardFirmwareMajorRevision": cnt2SysCardFirmwareMajorRevision,
       "cnt2SysCardFirmwareMinorRevision": cnt2SysCardFirmwareMinorRevision,
       "cnt2SysCardVendorOctetString": cnt2SysCardVendorOctetString,
       "cnt2SysCardVendorDisplayString": cnt2SysCardVendorDisplayString,
       "cnt2SysIfTable": cnt2SysIfTable,
       "cnt2SysIfEntry": cnt2SysIfEntry,
       "cnt2SysIfAdapterIndex": cnt2SysIfAdapterIndex,
       "cnt2SysIfBusIndex": cnt2SysIfBusIndex,
       "cnt2SysIfIndex": cnt2SysIfIndex,
       "cnt2SysIfType": cnt2SysIfType,
       "cnt2SysIfCardIndex": cnt2SysIfCardIndex,
       "cnt2SysIfName": cnt2SysIfName,
       "cnt2SysIfConnector": cnt2SysIfConnector,
       "cnt2SysIfSnmpIndex": cnt2SysIfSnmpIndex,
       "cnt2SysSerialNumber": cnt2SysSerialNumber,
       "cnt2SysOsVersion": cnt2SysOsVersion}
)
