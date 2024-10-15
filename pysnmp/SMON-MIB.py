# SNMP MIB module (SMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:22 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(DataSource,
 LastCreateTime,
 probeConfig,
 rmonConformance) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "DataSource",
    "LastCreateTime",
    "probeConfig",
    "rmonConformance")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

switchRMON = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SmonDataSource(ObjectIdentifier, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs



class _SmonCapabilities_Type(Bits):
    """Custom type smonCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("dataSource", 2),
          ("portCopy", 4),
          ("smonPrioStats", 1),
          ("smonUnusedBit", 3),
          ("smonVlanStats", 0))
    )

_SmonCapabilities_Type.__name__ = "Bits"
_SmonCapabilities_Object = MibScalar
smonCapabilities = _SmonCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 16, 19, 15),
    _SmonCapabilities_Type()
)
smonCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonCapabilities.setStatus("current")
_SmonMIBCompliances_ObjectIdentity = ObjectIdentity
smonMIBCompliances = _SmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 3)
)
_SmonMIBGroups_ObjectIdentity = ObjectIdentity
smonMIBGroups = _SmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 20, 4)
)
_SmonMIBObjects_ObjectIdentity = ObjectIdentity
smonMIBObjects = _SmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1)
)
_DataSourceCaps_ObjectIdentity = ObjectIdentity
dataSourceCaps = _DataSourceCaps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1)
)
_DataSourceCapsTable_Object = MibTable
dataSourceCapsTable = _DataSourceCapsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dataSourceCapsTable.setStatus("current")
_DataSourceCapsEntry_Object = MibTableRow
dataSourceCapsEntry = _DataSourceCapsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1)
)
dataSourceCapsEntry.setIndexNames(
    (1, "SMON-MIB", "dataSourceCapsObject"),
)
if mibBuilder.loadTexts:
    dataSourceCapsEntry.setStatus("current")
_DataSourceCapsObject_Type = SmonDataSource
_DataSourceCapsObject_Object = MibTableColumn
dataSourceCapsObject = _DataSourceCapsObject_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 1),
    _DataSourceCapsObject_Type()
)
dataSourceCapsObject.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dataSourceCapsObject.setStatus("current")


class _DataSourceRmonCaps_Type(Bits):
    """Custom type dataSourceRmonCaps based on Bits"""
    namedValues = NamedValues(
        *(("babyGiantsCountAsGood", 3),
          ("countAllGoodFrames", 1),
          ("countAnyRmonTables", 2),
          ("countErrFrames", 0))
    )

_DataSourceRmonCaps_Type.__name__ = "Bits"
_DataSourceRmonCaps_Object = MibTableColumn
dataSourceRmonCaps = _DataSourceRmonCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 2),
    _DataSourceRmonCaps_Type()
)
dataSourceRmonCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSourceRmonCaps.setStatus("current")


class _DataSourceCopyCaps_Type(Bits):
    """Custom type dataSourceCopyCaps based on Bits"""
    namedValues = NamedValues(
        *(("copyAllGoodFrames", 7),
          ("copyDestPort", 1),
          ("copyErrFrames", 5),
          ("copySourcePort", 0),
          ("copySrcRxTraffic", 3),
          ("copySrcTxTraffic", 2),
          ("copyUnalteredFrames", 6),
          ("countDestDropEvents", 4))
    )

_DataSourceCopyCaps_Type.__name__ = "Bits"
_DataSourceCopyCaps_Object = MibTableColumn
dataSourceCopyCaps = _DataSourceCopyCaps_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 3),
    _DataSourceCopyCaps_Type()
)
dataSourceCopyCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSourceCopyCaps.setStatus("current")
_DataSourceCapsIfIndex_Type = InterfaceIndex
_DataSourceCapsIfIndex_Object = MibTableColumn
dataSourceCapsIfIndex = _DataSourceCapsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 1, 1, 1, 4),
    _DataSourceCapsIfIndex_Type()
)
dataSourceCapsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataSourceCapsIfIndex.setStatus("current")
_SmonStats_ObjectIdentity = ObjectIdentity
smonStats = _SmonStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2)
)
_SmonVlanStatsControlTable_Object = MibTable
smonVlanStatsControlTable = _SmonVlanStatsControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    smonVlanStatsControlTable.setStatus("current")
_SmonVlanStatsControlEntry_Object = MibTableRow
smonVlanStatsControlEntry = _SmonVlanStatsControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1)
)
smonVlanStatsControlEntry.setIndexNames(
    (0, "SMON-MIB", "smonVlanStatsControlIndex"),
)
if mibBuilder.loadTexts:
    smonVlanStatsControlEntry.setStatus("current")


class _SmonVlanStatsControlIndex_Type(Integer32):
    """Custom type smonVlanStatsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmonVlanStatsControlIndex_Type.__name__ = "Integer32"
_SmonVlanStatsControlIndex_Object = MibTableColumn
smonVlanStatsControlIndex = _SmonVlanStatsControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 1),
    _SmonVlanStatsControlIndex_Type()
)
smonVlanStatsControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smonVlanStatsControlIndex.setStatus("current")
_SmonVlanStatsControlDataSource_Type = DataSource
_SmonVlanStatsControlDataSource_Object = MibTableColumn
smonVlanStatsControlDataSource = _SmonVlanStatsControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 2),
    _SmonVlanStatsControlDataSource_Type()
)
smonVlanStatsControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonVlanStatsControlDataSource.setStatus("current")
_SmonVlanStatsControlCreateTime_Type = LastCreateTime
_SmonVlanStatsControlCreateTime_Object = MibTableColumn
smonVlanStatsControlCreateTime = _SmonVlanStatsControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 3),
    _SmonVlanStatsControlCreateTime_Type()
)
smonVlanStatsControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanStatsControlCreateTime.setStatus("current")
_SmonVlanStatsControlOwner_Type = OwnerString
_SmonVlanStatsControlOwner_Object = MibTableColumn
smonVlanStatsControlOwner = _SmonVlanStatsControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 4),
    _SmonVlanStatsControlOwner_Type()
)
smonVlanStatsControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonVlanStatsControlOwner.setStatus("current")
_SmonVlanStatsControlStatus_Type = RowStatus
_SmonVlanStatsControlStatus_Object = MibTableColumn
smonVlanStatsControlStatus = _SmonVlanStatsControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 1, 1, 5),
    _SmonVlanStatsControlStatus_Type()
)
smonVlanStatsControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonVlanStatsControlStatus.setStatus("current")
_SmonVlanIdStatsTable_Object = MibTable
smonVlanIdStatsTable = _SmonVlanIdStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    smonVlanIdStatsTable.setStatus("current")
_SmonVlanIdStatsEntry_Object = MibTableRow
smonVlanIdStatsEntry = _SmonVlanIdStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1)
)
smonVlanIdStatsEntry.setIndexNames(
    (0, "SMON-MIB", "smonVlanStatsControlIndex"),
    (0, "SMON-MIB", "smonVlanIdStatsId"),
)
if mibBuilder.loadTexts:
    smonVlanIdStatsEntry.setStatus("current")


class _SmonVlanIdStatsId_Type(Integer32):
    """Custom type smonVlanIdStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SmonVlanIdStatsId_Type.__name__ = "Integer32"
_SmonVlanIdStatsId_Object = MibTableColumn
smonVlanIdStatsId = _SmonVlanIdStatsId_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 1),
    _SmonVlanIdStatsId_Type()
)
smonVlanIdStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smonVlanIdStatsId.setStatus("current")
_SmonVlanIdStatsTotalPkts_Type = Counter32
_SmonVlanIdStatsTotalPkts_Object = MibTableColumn
smonVlanIdStatsTotalPkts = _SmonVlanIdStatsTotalPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 2),
    _SmonVlanIdStatsTotalPkts_Type()
)
smonVlanIdStatsTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalPkts.setUnits("packets")
_SmonVlanIdStatsTotalOverflowPkts_Type = Counter32
_SmonVlanIdStatsTotalOverflowPkts_Object = MibTableColumn
smonVlanIdStatsTotalOverflowPkts = _SmonVlanIdStatsTotalOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 3),
    _SmonVlanIdStatsTotalOverflowPkts_Type()
)
smonVlanIdStatsTotalOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOverflowPkts.setUnits("packets")
_SmonVlanIdStatsTotalHCPkts_Type = Counter64
_SmonVlanIdStatsTotalHCPkts_Object = MibTableColumn
smonVlanIdStatsTotalHCPkts = _SmonVlanIdStatsTotalHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 4),
    _SmonVlanIdStatsTotalHCPkts_Type()
)
smonVlanIdStatsTotalHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalHCPkts.setUnits("packets")
_SmonVlanIdStatsTotalOctets_Type = Counter32
_SmonVlanIdStatsTotalOctets_Object = MibTableColumn
smonVlanIdStatsTotalOctets = _SmonVlanIdStatsTotalOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 5),
    _SmonVlanIdStatsTotalOctets_Type()
)
smonVlanIdStatsTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOctets.setUnits("octets")
_SmonVlanIdStatsTotalOverflowOctets_Type = Counter32
_SmonVlanIdStatsTotalOverflowOctets_Object = MibTableColumn
smonVlanIdStatsTotalOverflowOctets = _SmonVlanIdStatsTotalOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 6),
    _SmonVlanIdStatsTotalOverflowOctets_Type()
)
smonVlanIdStatsTotalOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalOverflowOctets.setUnits("octets")
_SmonVlanIdStatsTotalHCOctets_Type = Counter64
_SmonVlanIdStatsTotalHCOctets_Object = MibTableColumn
smonVlanIdStatsTotalHCOctets = _SmonVlanIdStatsTotalHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 7),
    _SmonVlanIdStatsTotalHCOctets_Type()
)
smonVlanIdStatsTotalHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsTotalHCOctets.setUnits("octets")
_SmonVlanIdStatsNUcastPkts_Type = Counter32
_SmonVlanIdStatsNUcastPkts_Object = MibTableColumn
smonVlanIdStatsNUcastPkts = _SmonVlanIdStatsNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 8),
    _SmonVlanIdStatsNUcastPkts_Type()
)
smonVlanIdStatsNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastPkts.setUnits("packets")
_SmonVlanIdStatsNUcastOverflowPkts_Type = Counter32
_SmonVlanIdStatsNUcastOverflowPkts_Object = MibTableColumn
smonVlanIdStatsNUcastOverflowPkts = _SmonVlanIdStatsNUcastOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 9),
    _SmonVlanIdStatsNUcastOverflowPkts_Type()
)
smonVlanIdStatsNUcastOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOverflowPkts.setUnits("packets")
_SmonVlanIdStatsNUcastHCPkts_Type = Counter64
_SmonVlanIdStatsNUcastHCPkts_Object = MibTableColumn
smonVlanIdStatsNUcastHCPkts = _SmonVlanIdStatsNUcastHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 10),
    _SmonVlanIdStatsNUcastHCPkts_Type()
)
smonVlanIdStatsNUcastHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastHCPkts.setUnits("packets")
_SmonVlanIdStatsNUcastOctets_Type = Counter32
_SmonVlanIdStatsNUcastOctets_Object = MibTableColumn
smonVlanIdStatsNUcastOctets = _SmonVlanIdStatsNUcastOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 11),
    _SmonVlanIdStatsNUcastOctets_Type()
)
smonVlanIdStatsNUcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOctets.setUnits("octets")
_SmonVlanIdStatsNUcastOverflowOctets_Type = Counter32
_SmonVlanIdStatsNUcastOverflowOctets_Object = MibTableColumn
smonVlanIdStatsNUcastOverflowOctets = _SmonVlanIdStatsNUcastOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 12),
    _SmonVlanIdStatsNUcastOverflowOctets_Type()
)
smonVlanIdStatsNUcastOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastOverflowOctets.setUnits("octets")
_SmonVlanIdStatsNUcastHCOctets_Type = Counter64
_SmonVlanIdStatsNUcastHCOctets_Object = MibTableColumn
smonVlanIdStatsNUcastHCOctets = _SmonVlanIdStatsNUcastHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 13),
    _SmonVlanIdStatsNUcastHCOctets_Type()
)
smonVlanIdStatsNUcastHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonVlanIdStatsNUcastHCOctets.setUnits("octets")
_SmonVlanIdStatsCreateTime_Type = LastCreateTime
_SmonVlanIdStatsCreateTime_Object = MibTableColumn
smonVlanIdStatsCreateTime = _SmonVlanIdStatsCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 2, 1, 14),
    _SmonVlanIdStatsCreateTime_Type()
)
smonVlanIdStatsCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonVlanIdStatsCreateTime.setStatus("current")
_SmonPrioStatsControlTable_Object = MibTable
smonPrioStatsControlTable = _SmonPrioStatsControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3)
)
if mibBuilder.loadTexts:
    smonPrioStatsControlTable.setStatus("current")
_SmonPrioStatsControlEntry_Object = MibTableRow
smonPrioStatsControlEntry = _SmonPrioStatsControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1)
)
smonPrioStatsControlEntry.setIndexNames(
    (0, "SMON-MIB", "smonPrioStatsControlIndex"),
)
if mibBuilder.loadTexts:
    smonPrioStatsControlEntry.setStatus("current")


class _SmonPrioStatsControlIndex_Type(Integer32):
    """Custom type smonPrioStatsControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SmonPrioStatsControlIndex_Type.__name__ = "Integer32"
_SmonPrioStatsControlIndex_Object = MibTableColumn
smonPrioStatsControlIndex = _SmonPrioStatsControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 1),
    _SmonPrioStatsControlIndex_Type()
)
smonPrioStatsControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smonPrioStatsControlIndex.setStatus("current")
_SmonPrioStatsControlDataSource_Type = DataSource
_SmonPrioStatsControlDataSource_Object = MibTableColumn
smonPrioStatsControlDataSource = _SmonPrioStatsControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 2),
    _SmonPrioStatsControlDataSource_Type()
)
smonPrioStatsControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonPrioStatsControlDataSource.setStatus("current")
_SmonPrioStatsControlCreateTime_Type = LastCreateTime
_SmonPrioStatsControlCreateTime_Object = MibTableColumn
smonPrioStatsControlCreateTime = _SmonPrioStatsControlCreateTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 3),
    _SmonPrioStatsControlCreateTime_Type()
)
smonPrioStatsControlCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsControlCreateTime.setStatus("current")
_SmonPrioStatsControlOwner_Type = OwnerString
_SmonPrioStatsControlOwner_Object = MibTableColumn
smonPrioStatsControlOwner = _SmonPrioStatsControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 4),
    _SmonPrioStatsControlOwner_Type()
)
smonPrioStatsControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonPrioStatsControlOwner.setStatus("current")
_SmonPrioStatsControlStatus_Type = RowStatus
_SmonPrioStatsControlStatus_Object = MibTableColumn
smonPrioStatsControlStatus = _SmonPrioStatsControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 3, 1, 5),
    _SmonPrioStatsControlStatus_Type()
)
smonPrioStatsControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smonPrioStatsControlStatus.setStatus("current")
_SmonPrioStatsTable_Object = MibTable
smonPrioStatsTable = _SmonPrioStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4)
)
if mibBuilder.loadTexts:
    smonPrioStatsTable.setStatus("current")
_SmonPrioStatsEntry_Object = MibTableRow
smonPrioStatsEntry = _SmonPrioStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1)
)
smonPrioStatsEntry.setIndexNames(
    (0, "SMON-MIB", "smonPrioStatsControlIndex"),
    (0, "SMON-MIB", "smonPrioStatsId"),
)
if mibBuilder.loadTexts:
    smonPrioStatsEntry.setStatus("current")


class _SmonPrioStatsId_Type(Integer32):
    """Custom type smonPrioStatsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SmonPrioStatsId_Type.__name__ = "Integer32"
_SmonPrioStatsId_Object = MibTableColumn
smonPrioStatsId = _SmonPrioStatsId_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 1),
    _SmonPrioStatsId_Type()
)
smonPrioStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smonPrioStatsId.setStatus("current")
_SmonPrioStatsPkts_Type = Counter32
_SmonPrioStatsPkts_Object = MibTableColumn
smonPrioStatsPkts = _SmonPrioStatsPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 2),
    _SmonPrioStatsPkts_Type()
)
smonPrioStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsPkts.setUnits("packets")
_SmonPrioStatsOverflowPkts_Type = Counter32
_SmonPrioStatsOverflowPkts_Object = MibTableColumn
smonPrioStatsOverflowPkts = _SmonPrioStatsOverflowPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 3),
    _SmonPrioStatsOverflowPkts_Type()
)
smonPrioStatsOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsOverflowPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsOverflowPkts.setUnits("packets")
_SmonPrioStatsHCPkts_Type = Counter64
_SmonPrioStatsHCPkts_Object = MibTableColumn
smonPrioStatsHCPkts = _SmonPrioStatsHCPkts_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 4),
    _SmonPrioStatsHCPkts_Type()
)
smonPrioStatsHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsHCPkts.setUnits("packets")
_SmonPrioStatsOctets_Type = Counter32
_SmonPrioStatsOctets_Object = MibTableColumn
smonPrioStatsOctets = _SmonPrioStatsOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 5),
    _SmonPrioStatsOctets_Type()
)
smonPrioStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsOctets.setUnits("octets")
_SmonPrioStatsOverflowOctets_Type = Counter32
_SmonPrioStatsOverflowOctets_Object = MibTableColumn
smonPrioStatsOverflowOctets = _SmonPrioStatsOverflowOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 6),
    _SmonPrioStatsOverflowOctets_Type()
)
smonPrioStatsOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsOverflowOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsOverflowOctets.setUnits("octets")
_SmonPrioStatsHCOctets_Type = Counter64
_SmonPrioStatsHCOctets_Object = MibTableColumn
smonPrioStatsHCOctets = _SmonPrioStatsHCOctets_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 2, 4, 1, 7),
    _SmonPrioStatsHCOctets_Type()
)
smonPrioStatsHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smonPrioStatsHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    smonPrioStatsHCOctets.setUnits("octets")
_PortCopyConfig_ObjectIdentity = ObjectIdentity
portCopyConfig = _PortCopyConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3)
)
_PortCopyTable_Object = MibTable
portCopyTable = _PortCopyTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    portCopyTable.setStatus("current")
_PortCopyEntry_Object = MibTableRow
portCopyEntry = _PortCopyEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1)
)
portCopyEntry.setIndexNames(
    (0, "SMON-MIB", "portCopySource"),
    (0, "SMON-MIB", "portCopyDest"),
)
if mibBuilder.loadTexts:
    portCopyEntry.setStatus("current")
_PortCopySource_Type = InterfaceIndex
_PortCopySource_Object = MibTableColumn
portCopySource = _PortCopySource_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 1),
    _PortCopySource_Type()
)
portCopySource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCopySource.setStatus("current")
_PortCopyDest_Type = InterfaceIndex
_PortCopyDest_Object = MibTableColumn
portCopyDest = _PortCopyDest_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 2),
    _PortCopyDest_Type()
)
portCopyDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCopyDest.setStatus("current")
_PortCopyDestDropEvents_Type = Counter32
_PortCopyDestDropEvents_Object = MibTableColumn
portCopyDestDropEvents = _PortCopyDestDropEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 3),
    _PortCopyDestDropEvents_Type()
)
portCopyDestDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCopyDestDropEvents.setStatus("current")
if mibBuilder.loadTexts:
    portCopyDestDropEvents.setUnits("events")


class _PortCopyDirection_Type(Integer32):
    """Custom type portCopyDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyBoth", 3),
          ("copyRxOnly", 1),
          ("copyTxOnly", 2))
    )


_PortCopyDirection_Type.__name__ = "Integer32"
_PortCopyDirection_Object = MibTableColumn
portCopyDirection = _PortCopyDirection_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 4),
    _PortCopyDirection_Type()
)
portCopyDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyDirection.setStatus("current")
_PortCopyStatus_Type = RowStatus
_PortCopyStatus_Object = MibTableColumn
portCopyStatus = _PortCopyStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 3, 1, 1, 5),
    _PortCopyStatus_Type()
)
portCopyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portCopyStatus.setStatus("current")
_SmonRegistrationPoints_ObjectIdentity = ObjectIdentity
smonRegistrationPoints = _SmonRegistrationPoints_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 4)
)
_SmonVlanDataSource_ObjectIdentity = ObjectIdentity
smonVlanDataSource = _SmonVlanDataSource_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 22, 1, 4, 1)
)

# Managed Objects groups

dataSourceCapsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 1)
)
dataSourceCapsGroup.setObjects(
      *(("SMON-MIB", "dataSourceRmonCaps"),
        ("SMON-MIB", "dataSourceCopyCaps"),
        ("SMON-MIB", "dataSourceCapsIfIndex"))
)
if mibBuilder.loadTexts:
    dataSourceCapsGroup.setStatus("current")

smonVlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 2)
)
smonVlanStatsGroup.setObjects(
      *(("SMON-MIB", "smonVlanStatsControlDataSource"),
        ("SMON-MIB", "smonVlanStatsControlCreateTime"),
        ("SMON-MIB", "smonVlanStatsControlOwner"),
        ("SMON-MIB", "smonVlanStatsControlStatus"),
        ("SMON-MIB", "smonVlanIdStatsTotalPkts"),
        ("SMON-MIB", "smonVlanIdStatsTotalOctets"),
        ("SMON-MIB", "smonVlanIdStatsNUcastPkts"),
        ("SMON-MIB", "smonVlanIdStatsCreateTime"))
)
if mibBuilder.loadTexts:
    smonVlanStatsGroup.setStatus("current")

smonPrioStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 3)
)
smonPrioStatsGroup.setObjects(
      *(("SMON-MIB", "smonPrioStatsControlDataSource"),
        ("SMON-MIB", "smonPrioStatsControlCreateTime"),
        ("SMON-MIB", "smonPrioStatsControlOwner"),
        ("SMON-MIB", "smonPrioStatsControlStatus"),
        ("SMON-MIB", "smonPrioStatsPkts"),
        ("SMON-MIB", "smonPrioStatsOctets"))
)
if mibBuilder.loadTexts:
    smonPrioStatsGroup.setStatus("current")

smonHcTo100mbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 4)
)
smonHcTo100mbGroup.setObjects(
      *(("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"),
        ("SMON-MIB", "smonPrioStatsOverflowOctets"),
        ("SMON-MIB", "smonPrioStatsHCOctets"))
)
if mibBuilder.loadTexts:
    smonHcTo100mbGroup.setStatus("current")

smonHc100mbPlusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 5)
)
smonHc100mbPlusGroup.setObjects(
      *(("SMON-MIB", "smonVlanIdStatsTotalOverflowPkts"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCPkts"),
        ("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"),
        ("SMON-MIB", "smonVlanIdStatsNUcastOverflowPkts"),
        ("SMON-MIB", "smonVlanIdStatsNUcastHCPkts"),
        ("SMON-MIB", "smonPrioStatsOverflowPkts"),
        ("SMON-MIB", "smonPrioStatsHCPkts"),
        ("SMON-MIB", "smonPrioStatsOverflowOctets"),
        ("SMON-MIB", "smonPrioStatsHCOctets"))
)
if mibBuilder.loadTexts:
    smonHc100mbPlusGroup.setStatus("current")

hcVlanTo100mbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 6)
)
hcVlanTo100mbGroup.setObjects(
      *(("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"))
)
if mibBuilder.loadTexts:
    hcVlanTo100mbGroup.setStatus("current")

hcVlan100mbPlusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 7)
)
hcVlan100mbPlusGroup.setObjects(
      *(("SMON-MIB", "smonVlanIdStatsTotalOverflowPkts"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCPkts"),
        ("SMON-MIB", "smonVlanIdStatsTotalOverflowOctets"),
        ("SMON-MIB", "smonVlanIdStatsTotalHCOctets"),
        ("SMON-MIB", "smonVlanIdStatsNUcastOverflowPkts"),
        ("SMON-MIB", "smonVlanIdStatsNUcastHCPkts"))
)
if mibBuilder.loadTexts:
    hcVlan100mbPlusGroup.setStatus("current")

hcPrioTo100mbGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 8)
)
hcPrioTo100mbGroup.setObjects(
      *(("SMON-MIB", "smonPrioStatsOverflowOctets"),
        ("SMON-MIB", "smonPrioStatsHCOctets"))
)
if mibBuilder.loadTexts:
    hcPrioTo100mbGroup.setStatus("current")

hcPrio100mbPlusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 9)
)
hcPrio100mbPlusGroup.setObjects(
      *(("SMON-MIB", "smonPrioStatsOverflowPkts"),
        ("SMON-MIB", "smonPrioStatsHCPkts"),
        ("SMON-MIB", "smonPrioStatsOverflowOctets"),
        ("SMON-MIB", "smonPrioStatsHCOctets"))
)
if mibBuilder.loadTexts:
    hcPrio100mbPlusGroup.setStatus("current")

smonVlanStatsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 10)
)
smonVlanStatsExtGroup.setObjects(
      *(("SMON-MIB", "smonVlanIdStatsNUcastOctets"),
        ("SMON-MIB", "smonVlanIdStatsNUcastOverflowOctets"),
        ("SMON-MIB", "smonVlanIdStatsNUcastHCOctets"))
)
if mibBuilder.loadTexts:
    smonVlanStatsExtGroup.setStatus("current")

smonInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 11)
)
smonInformationGroup.setObjects(
    ("SMON-MIB", "smonCapabilities")
)
if mibBuilder.loadTexts:
    smonInformationGroup.setStatus("current")

portCopyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 4, 12)
)
portCopyConfigGroup.setObjects(
      *(("SMON-MIB", "portCopyDestDropEvents"),
        ("SMON-MIB", "portCopyDirection"),
        ("SMON-MIB", "portCopyStatus"))
)
if mibBuilder.loadTexts:
    portCopyConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 3, 1)
)
if mibBuilder.loadTexts:
    smonMIBCompliance.setStatus(
        "current"
    )

smonMIBVlanStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 3, 2)
)
if mibBuilder.loadTexts:
    smonMIBVlanStatsCompliance.setStatus(
        "current"
    )

smonMIBPrioStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 3, 3)
)
if mibBuilder.loadTexts:
    smonMIBPrioStatsCompliance.setStatus(
        "current"
    )

portCopyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 20, 3, 4)
)
if mibBuilder.loadTexts:
    portCopyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMON-MIB",
    **{"SmonDataSource": SmonDataSource,
       "smonCapabilities": smonCapabilities,
       "smonMIBCompliances": smonMIBCompliances,
       "smonMIBCompliance": smonMIBCompliance,
       "smonMIBVlanStatsCompliance": smonMIBVlanStatsCompliance,
       "smonMIBPrioStatsCompliance": smonMIBPrioStatsCompliance,
       "portCopyCompliance": portCopyCompliance,
       "smonMIBGroups": smonMIBGroups,
       "dataSourceCapsGroup": dataSourceCapsGroup,
       "smonVlanStatsGroup": smonVlanStatsGroup,
       "smonPrioStatsGroup": smonPrioStatsGroup,
       "smonHcTo100mbGroup": smonHcTo100mbGroup,
       "smonHc100mbPlusGroup": smonHc100mbPlusGroup,
       "hcVlanTo100mbGroup": hcVlanTo100mbGroup,
       "hcVlan100mbPlusGroup": hcVlan100mbPlusGroup,
       "hcPrioTo100mbGroup": hcPrioTo100mbGroup,
       "hcPrio100mbPlusGroup": hcPrio100mbPlusGroup,
       "smonVlanStatsExtGroup": smonVlanStatsExtGroup,
       "smonInformationGroup": smonInformationGroup,
       "portCopyConfigGroup": portCopyConfigGroup,
       "switchRMON": switchRMON,
       "smonMIBObjects": smonMIBObjects,
       "dataSourceCaps": dataSourceCaps,
       "dataSourceCapsTable": dataSourceCapsTable,
       "dataSourceCapsEntry": dataSourceCapsEntry,
       "dataSourceCapsObject": dataSourceCapsObject,
       "dataSourceRmonCaps": dataSourceRmonCaps,
       "dataSourceCopyCaps": dataSourceCopyCaps,
       "dataSourceCapsIfIndex": dataSourceCapsIfIndex,
       "smonStats": smonStats,
       "smonVlanStatsControlTable": smonVlanStatsControlTable,
       "smonVlanStatsControlEntry": smonVlanStatsControlEntry,
       "smonVlanStatsControlIndex": smonVlanStatsControlIndex,
       "smonVlanStatsControlDataSource": smonVlanStatsControlDataSource,
       "smonVlanStatsControlCreateTime": smonVlanStatsControlCreateTime,
       "smonVlanStatsControlOwner": smonVlanStatsControlOwner,
       "smonVlanStatsControlStatus": smonVlanStatsControlStatus,
       "smonVlanIdStatsTable": smonVlanIdStatsTable,
       "smonVlanIdStatsEntry": smonVlanIdStatsEntry,
       "smonVlanIdStatsId": smonVlanIdStatsId,
       "smonVlanIdStatsTotalPkts": smonVlanIdStatsTotalPkts,
       "smonVlanIdStatsTotalOverflowPkts": smonVlanIdStatsTotalOverflowPkts,
       "smonVlanIdStatsTotalHCPkts": smonVlanIdStatsTotalHCPkts,
       "smonVlanIdStatsTotalOctets": smonVlanIdStatsTotalOctets,
       "smonVlanIdStatsTotalOverflowOctets": smonVlanIdStatsTotalOverflowOctets,
       "smonVlanIdStatsTotalHCOctets": smonVlanIdStatsTotalHCOctets,
       "smonVlanIdStatsNUcastPkts": smonVlanIdStatsNUcastPkts,
       "smonVlanIdStatsNUcastOverflowPkts": smonVlanIdStatsNUcastOverflowPkts,
       "smonVlanIdStatsNUcastHCPkts": smonVlanIdStatsNUcastHCPkts,
       "smonVlanIdStatsNUcastOctets": smonVlanIdStatsNUcastOctets,
       "smonVlanIdStatsNUcastOverflowOctets": smonVlanIdStatsNUcastOverflowOctets,
       "smonVlanIdStatsNUcastHCOctets": smonVlanIdStatsNUcastHCOctets,
       "smonVlanIdStatsCreateTime": smonVlanIdStatsCreateTime,
       "smonPrioStatsControlTable": smonPrioStatsControlTable,
       "smonPrioStatsControlEntry": smonPrioStatsControlEntry,
       "smonPrioStatsControlIndex": smonPrioStatsControlIndex,
       "smonPrioStatsControlDataSource": smonPrioStatsControlDataSource,
       "smonPrioStatsControlCreateTime": smonPrioStatsControlCreateTime,
       "smonPrioStatsControlOwner": smonPrioStatsControlOwner,
       "smonPrioStatsControlStatus": smonPrioStatsControlStatus,
       "smonPrioStatsTable": smonPrioStatsTable,
       "smonPrioStatsEntry": smonPrioStatsEntry,
       "smonPrioStatsId": smonPrioStatsId,
       "smonPrioStatsPkts": smonPrioStatsPkts,
       "smonPrioStatsOverflowPkts": smonPrioStatsOverflowPkts,
       "smonPrioStatsHCPkts": smonPrioStatsHCPkts,
       "smonPrioStatsOctets": smonPrioStatsOctets,
       "smonPrioStatsOverflowOctets": smonPrioStatsOverflowOctets,
       "smonPrioStatsHCOctets": smonPrioStatsHCOctets,
       "portCopyConfig": portCopyConfig,
       "portCopyTable": portCopyTable,
       "portCopyEntry": portCopyEntry,
       "portCopySource": portCopySource,
       "portCopyDest": portCopyDest,
       "portCopyDestDropEvents": portCopyDestDropEvents,
       "portCopyDirection": portCopyDirection,
       "portCopyStatus": portCopyStatus,
       "smonRegistrationPoints": smonRegistrationPoints,
       "smonVlanDataSource": smonVlanDataSource}
)
