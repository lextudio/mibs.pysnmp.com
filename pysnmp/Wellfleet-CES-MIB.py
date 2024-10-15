# SNMP MIB module (Wellfleet-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-CES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:56 2024
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

(wfAtmInterfaceGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAtmInterfaceGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAtmCESGroup_ObjectIdentity = ObjectIdentity
wfAtmCESGroup = _WfAtmCESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4)
)
_WfAtmCESObjects_ObjectIdentity = ObjectIdentity
wfAtmCESObjects = _WfAtmCESObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1)
)
_WfAtmCESConfTable_Object = MibTable
wfAtmCESConfTable = _WfAtmCESConfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wfAtmCESConfTable.setStatus("mandatory")
_WfAtmCESConfEntry_Object = MibTableRow
wfAtmCESConfEntry = _WfAtmCESConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1)
)
wfAtmCESConfEntry.setIndexNames(
    (0, "Wellfleet-CES-MIB", "wfAtmCESConfAtmIndex"),
    (0, "Wellfleet-CES-MIB", "wfAtmCESConfCbrIndex"),
)
if mibBuilder.loadTexts:
    wfAtmCESConfEntry.setStatus("mandatory")


class _WfAtmCESConfDelete_Type(Integer32):
    """Custom type wfAtmCESConfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAtmCESConfDelete_Type.__name__ = "Integer32"
_WfAtmCESConfDelete_Object = MibTableColumn
wfAtmCESConfDelete = _WfAtmCESConfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 1),
    _WfAtmCESConfDelete_Type()
)
wfAtmCESConfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfDelete.setStatus("mandatory")


class _WfAtmCESConfDisable_Type(Integer32):
    """Custom type wfAtmCESConfDisable based on Integer32"""
    defaultValue = 1

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


_WfAtmCESConfDisable_Type.__name__ = "Integer32"
_WfAtmCESConfDisable_Object = MibTableColumn
wfAtmCESConfDisable = _WfAtmCESConfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 2),
    _WfAtmCESConfDisable_Type()
)
wfAtmCESConfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfDisable.setStatus("mandatory")
_WfAtmCESConfAtmIndex_Type = Integer32
_WfAtmCESConfAtmIndex_Object = MibTableColumn
wfAtmCESConfAtmIndex = _WfAtmCESConfAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 3),
    _WfAtmCESConfAtmIndex_Type()
)
wfAtmCESConfAtmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESConfAtmIndex.setStatus("mandatory")
_WfAtmCESConfCbrIndex_Type = Integer32
_WfAtmCESConfCbrIndex_Object = MibTableColumn
wfAtmCESConfCbrIndex = _WfAtmCESConfCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 4),
    _WfAtmCESConfCbrIndex_Type()
)
wfAtmCESConfCbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESConfCbrIndex.setStatus("mandatory")
_WfAtmCESConfAtmVpi_Type = Integer32
_WfAtmCESConfAtmVpi_Object = MibTableColumn
wfAtmCESConfAtmVpi = _WfAtmCESConfAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 5),
    _WfAtmCESConfAtmVpi_Type()
)
wfAtmCESConfAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESConfAtmVpi.setStatus("mandatory")
_WfAtmCESConfAtmVci_Type = Integer32
_WfAtmCESConfAtmVci_Object = MibTableColumn
wfAtmCESConfAtmVci = _WfAtmCESConfAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 6),
    _WfAtmCESConfAtmVci_Type()
)
wfAtmCESConfAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESConfAtmVci.setStatus("mandatory")
_WfAtmCESConfCfgAtmVpi_Type = Integer32
_WfAtmCESConfCfgAtmVpi_Object = MibTableColumn
wfAtmCESConfCfgAtmVpi = _WfAtmCESConfCfgAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 7),
    _WfAtmCESConfCfgAtmVpi_Type()
)
wfAtmCESConfCfgAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCfgAtmVpi.setStatus("mandatory")
_WfAtmCESConfCfgAtmVci_Type = Integer32
_WfAtmCESConfCfgAtmVci_Object = MibTableColumn
wfAtmCESConfCfgAtmVci = _WfAtmCESConfCfgAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 8),
    _WfAtmCESConfCfgAtmVci_Type()
)
wfAtmCESConfCfgAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCfgAtmVci.setStatus("mandatory")
_WfAtmCESConfVclCct_Type = Integer32
_WfAtmCESConfVclCct_Object = MibTableColumn
wfAtmCESConfVclCct = _WfAtmCESConfVclCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 9),
    _WfAtmCESConfVclCct_Type()
)
wfAtmCESConfVclCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfVclCct.setStatus("mandatory")


class _WfAtmCESConfCbrService_Type(Integer32):
    """Custom type wfAtmCESConfCbrService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("structured", 2),
          ("unstructured", 1))
    )


_WfAtmCESConfCbrService_Type.__name__ = "Integer32"
_WfAtmCESConfCbrService_Object = MibTableColumn
wfAtmCESConfCbrService = _WfAtmCESConfCbrService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 10),
    _WfAtmCESConfCbrService_Type()
)
wfAtmCESConfCbrService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCbrService.setStatus("mandatory")


class _WfAtmCESConfCbrClockMode_Type(Integer32):
    """Custom type wfAtmCESConfCbrClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("srts", 2),
          ("synchronous", 1))
    )


_WfAtmCESConfCbrClockMode_Type.__name__ = "Integer32"
_WfAtmCESConfCbrClockMode_Object = MibTableColumn
wfAtmCESConfCbrClockMode = _WfAtmCESConfCbrClockMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 11),
    _WfAtmCESConfCbrClockMode_Type()
)
wfAtmCESConfCbrClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCbrClockMode.setStatus("mandatory")


class _WfAtmCESConfCas_Type(Integer32):
    """Custom type wfAtmCESConfCas based on Integer32"""
    defaultValue = 1

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
        *(("basic", 1),
          ("ds1EsfCas", 4),
          ("ds1SfCas", 3),
          ("e1Cas", 2),
          ("j2Cas", 5))
    )


_WfAtmCESConfCas_Type.__name__ = "Integer32"
_WfAtmCESConfCas_Object = MibTableColumn
wfAtmCESConfCas = _WfAtmCESConfCas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 12),
    _WfAtmCESConfCas_Type()
)
wfAtmCESConfCas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCas.setStatus("mandatory")


class _WfAtmCESConfPartialFill_Type(Integer32):
    """Custom type wfAtmCESConfPartialFill based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_WfAtmCESConfPartialFill_Type.__name__ = "Integer32"
_WfAtmCESConfPartialFill_Object = MibTableColumn
wfAtmCESConfPartialFill = _WfAtmCESConfPartialFill_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 13),
    _WfAtmCESConfPartialFill_Type()
)
wfAtmCESConfPartialFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfPartialFill.setStatus("mandatory")


class _WfAtmCESConfBufMaxSize_Type(Integer32):
    """Custom type wfAtmCESConfBufMaxSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WfAtmCESConfBufMaxSize_Type.__name__ = "Integer32"
_WfAtmCESConfBufMaxSize_Object = MibTableColumn
wfAtmCESConfBufMaxSize = _WfAtmCESConfBufMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 14),
    _WfAtmCESConfBufMaxSize_Type()
)
wfAtmCESConfBufMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfBufMaxSize.setStatus("mandatory")


class _WfAtmCESConfCdvRxT_Type(Integer32):
    """Custom type wfAtmCESConfCdvRxT based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfAtmCESConfCdvRxT_Type.__name__ = "Integer32"
_WfAtmCESConfCdvRxT_Object = MibTableColumn
wfAtmCESConfCdvRxT = _WfAtmCESConfCdvRxT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 15),
    _WfAtmCESConfCdvRxT_Type()
)
wfAtmCESConfCdvRxT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCdvRxT.setStatus("mandatory")


class _WfAtmCESConfCellLossIntegrationPeriod_Type(Integer32):
    """Custom type wfAtmCESConfCellLossIntegrationPeriod based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_WfAtmCESConfCellLossIntegrationPeriod_Type.__name__ = "Integer32"
_WfAtmCESConfCellLossIntegrationPeriod_Object = MibTableColumn
wfAtmCESConfCellLossIntegrationPeriod = _WfAtmCESConfCellLossIntegrationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 16),
    _WfAtmCESConfCellLossIntegrationPeriod_Type()
)
wfAtmCESConfCellLossIntegrationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfCellLossIntegrationPeriod.setStatus("mandatory")


class _WfAtmCESConfConnType_Type(Integer32):
    """Custom type wfAtmCESConfConnType based on Integer32"""
    defaultValue = 2

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
        *(("activeSvc", 3),
          ("other", 1),
          ("passiveSvc", 4),
          ("pvc", 2))
    )


_WfAtmCESConfConnType_Type.__name__ = "Integer32"
_WfAtmCESConfConnType_Object = MibTableColumn
wfAtmCESConfConnType = _WfAtmCESConfConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 17),
    _WfAtmCESConfConnType_Type()
)
wfAtmCESConfConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfConnType.setStatus("mandatory")
_WfAtmCESConfLocalAddr_Type = OctetString
_WfAtmCESConfLocalAddr_Object = MibTableColumn
wfAtmCESConfLocalAddr = _WfAtmCESConfLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 18),
    _WfAtmCESConfLocalAddr_Type()
)
wfAtmCESConfLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfLocalAddr.setStatus("mandatory")


class _WfAtmCESConfAdminStatus_Type(Integer32):
    """Custom type wfAtmCESConfAdminStatus based on Integer32"""
    defaultValue = 1

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


_WfAtmCESConfAdminStatus_Type.__name__ = "Integer32"
_WfAtmCESConfAdminStatus_Object = MibTableColumn
wfAtmCESConfAdminStatus = _WfAtmCESConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 19),
    _WfAtmCESConfAdminStatus_Type()
)
wfAtmCESConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAtmCESConfAdminStatus.setStatus("mandatory")


class _WfAtmCESConfOperStatus_Type(Integer32):
    """Custom type wfAtmCESConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WfAtmCESConfOperStatus_Type.__name__ = "Integer32"
_WfAtmCESConfOperStatus_Object = MibTableColumn
wfAtmCESConfOperStatus = _WfAtmCESConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 1, 1, 20),
    _WfAtmCESConfOperStatus_Type()
)
wfAtmCESConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESConfOperStatus.setStatus("mandatory")
_WfAtmCESStatsTable_Object = MibTable
wfAtmCESStatsTable = _WfAtmCESStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wfAtmCESStatsTable.setStatus("mandatory")
_WfAtmCESStatsEntry_Object = MibTableRow
wfAtmCESStatsEntry = _WfAtmCESStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1)
)
wfAtmCESStatsEntry.setIndexNames(
    (0, "Wellfleet-CES-MIB", "wfAtmCESStatsAtmIndex"),
    (0, "Wellfleet-CES-MIB", "wfAtmCESStatsAtmVpi"),
    (0, "Wellfleet-CES-MIB", "wfAtmCESStatsAtmVci"),
)
if mibBuilder.loadTexts:
    wfAtmCESStatsEntry.setStatus("mandatory")
_WfAtmCESStatsAtmIndex_Type = Integer32
_WfAtmCESStatsAtmIndex_Object = MibTableColumn
wfAtmCESStatsAtmIndex = _WfAtmCESStatsAtmIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 1),
    _WfAtmCESStatsAtmIndex_Type()
)
wfAtmCESStatsAtmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsAtmIndex.setStatus("mandatory")
_WfAtmCESStatsAtmVpi_Type = Integer32
_WfAtmCESStatsAtmVpi_Object = MibTableColumn
wfAtmCESStatsAtmVpi = _WfAtmCESStatsAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 2),
    _WfAtmCESStatsAtmVpi_Type()
)
wfAtmCESStatsAtmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsAtmVpi.setStatus("mandatory")
_WfAtmCESStatsAtmVci_Type = Integer32
_WfAtmCESStatsAtmVci_Object = MibTableColumn
wfAtmCESStatsAtmVci = _WfAtmCESStatsAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 3),
    _WfAtmCESStatsAtmVci_Type()
)
wfAtmCESStatsAtmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsAtmVci.setStatus("mandatory")
_WfAtmCESStatsCbrIndex_Type = Integer32
_WfAtmCESStatsCbrIndex_Object = MibTableColumn
wfAtmCESStatsCbrIndex = _WfAtmCESStatsCbrIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 4),
    _WfAtmCESStatsCbrIndex_Type()
)
wfAtmCESStatsCbrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsCbrIndex.setStatus("mandatory")
_WfAtmCESStatsVclCct_Type = Integer32
_WfAtmCESStatsVclCct_Object = MibTableColumn
wfAtmCESStatsVclCct = _WfAtmCESStatsVclCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 5),
    _WfAtmCESStatsVclCct_Type()
)
wfAtmCESStatsVclCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsVclCct.setStatus("mandatory")
_WfAtmCESStatsReassCells_Type = Counter32
_WfAtmCESStatsReassCells_Object = MibTableColumn
wfAtmCESStatsReassCells = _WfAtmCESStatsReassCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 6),
    _WfAtmCESStatsReassCells_Type()
)
wfAtmCESStatsReassCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsReassCells.setStatus("mandatory")
_WfAtmCESStatsHdrErrors_Type = Counter32
_WfAtmCESStatsHdrErrors_Object = MibTableColumn
wfAtmCESStatsHdrErrors = _WfAtmCESStatsHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 7),
    _WfAtmCESStatsHdrErrors_Type()
)
wfAtmCESStatsHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsHdrErrors.setStatus("mandatory")
_WfAtmCESStatsPointerReframes_Type = Counter32
_WfAtmCESStatsPointerReframes_Object = MibTableColumn
wfAtmCESStatsPointerReframes = _WfAtmCESStatsPointerReframes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 8),
    _WfAtmCESStatsPointerReframes_Type()
)
wfAtmCESStatsPointerReframes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsPointerReframes.setStatus("mandatory")
_WfAtmCESStatsPointerParityErrors_Type = Counter32
_WfAtmCESStatsPointerParityErrors_Object = MibTableColumn
wfAtmCESStatsPointerParityErrors = _WfAtmCESStatsPointerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 9),
    _WfAtmCESStatsPointerParityErrors_Type()
)
wfAtmCESStatsPointerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsPointerParityErrors.setStatus("mandatory")
_WfAtmCESStatsAal1SeqErrors_Type = Counter32
_WfAtmCESStatsAal1SeqErrors_Object = MibTableColumn
wfAtmCESStatsAal1SeqErrors = _WfAtmCESStatsAal1SeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 10),
    _WfAtmCESStatsAal1SeqErrors_Type()
)
wfAtmCESStatsAal1SeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsAal1SeqErrors.setStatus("mandatory")
_WfAtmCESStatsLostCells_Type = Counter32
_WfAtmCESStatsLostCells_Object = MibTableColumn
wfAtmCESStatsLostCells = _WfAtmCESStatsLostCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 11),
    _WfAtmCESStatsLostCells_Type()
)
wfAtmCESStatsLostCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsLostCells.setStatus("mandatory")
_WfAtmCESStatsMisinsertedCells_Type = Counter32
_WfAtmCESStatsMisinsertedCells_Object = MibTableColumn
wfAtmCESStatsMisinsertedCells = _WfAtmCESStatsMisinsertedCells_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 12),
    _WfAtmCESStatsMisinsertedCells_Type()
)
wfAtmCESStatsMisinsertedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsMisinsertedCells.setStatus("mandatory")
_WfAtmCESStatsBufUnderflows_Type = Counter32
_WfAtmCESStatsBufUnderflows_Object = MibTableColumn
wfAtmCESStatsBufUnderflows = _WfAtmCESStatsBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 13),
    _WfAtmCESStatsBufUnderflows_Type()
)
wfAtmCESStatsBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsBufUnderflows.setStatus("mandatory")
_WfAtmCESStatsBufOverflows_Type = Counter32
_WfAtmCESStatsBufOverflows_Object = MibTableColumn
wfAtmCESStatsBufOverflows = _WfAtmCESStatsBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 14),
    _WfAtmCESStatsBufOverflows_Type()
)
wfAtmCESStatsBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsBufOverflows.setStatus("mandatory")


class _WfAtmCESStatsCellLossStatus_Type(Integer32):
    """Custom type wfAtmCESStatsCellLossStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 2),
          ("noLoss", 1))
    )


_WfAtmCESStatsCellLossStatus_Type.__name__ = "Integer32"
_WfAtmCESStatsCellLossStatus_Object = MibTableColumn
wfAtmCESStatsCellLossStatus = _WfAtmCESStatsCellLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 23, 4, 1, 2, 1, 15),
    _WfAtmCESStatsCellLossStatus_Type()
)
wfAtmCESStatsCellLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAtmCESStatsCellLossStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-CES-MIB",
    **{"wfAtmCESGroup": wfAtmCESGroup,
       "wfAtmCESObjects": wfAtmCESObjects,
       "wfAtmCESConfTable": wfAtmCESConfTable,
       "wfAtmCESConfEntry": wfAtmCESConfEntry,
       "wfAtmCESConfDelete": wfAtmCESConfDelete,
       "wfAtmCESConfDisable": wfAtmCESConfDisable,
       "wfAtmCESConfAtmIndex": wfAtmCESConfAtmIndex,
       "wfAtmCESConfCbrIndex": wfAtmCESConfCbrIndex,
       "wfAtmCESConfAtmVpi": wfAtmCESConfAtmVpi,
       "wfAtmCESConfAtmVci": wfAtmCESConfAtmVci,
       "wfAtmCESConfCfgAtmVpi": wfAtmCESConfCfgAtmVpi,
       "wfAtmCESConfCfgAtmVci": wfAtmCESConfCfgAtmVci,
       "wfAtmCESConfVclCct": wfAtmCESConfVclCct,
       "wfAtmCESConfCbrService": wfAtmCESConfCbrService,
       "wfAtmCESConfCbrClockMode": wfAtmCESConfCbrClockMode,
       "wfAtmCESConfCas": wfAtmCESConfCas,
       "wfAtmCESConfPartialFill": wfAtmCESConfPartialFill,
       "wfAtmCESConfBufMaxSize": wfAtmCESConfBufMaxSize,
       "wfAtmCESConfCdvRxT": wfAtmCESConfCdvRxT,
       "wfAtmCESConfCellLossIntegrationPeriod": wfAtmCESConfCellLossIntegrationPeriod,
       "wfAtmCESConfConnType": wfAtmCESConfConnType,
       "wfAtmCESConfLocalAddr": wfAtmCESConfLocalAddr,
       "wfAtmCESConfAdminStatus": wfAtmCESConfAdminStatus,
       "wfAtmCESConfOperStatus": wfAtmCESConfOperStatus,
       "wfAtmCESStatsTable": wfAtmCESStatsTable,
       "wfAtmCESStatsEntry": wfAtmCESStatsEntry,
       "wfAtmCESStatsAtmIndex": wfAtmCESStatsAtmIndex,
       "wfAtmCESStatsAtmVpi": wfAtmCESStatsAtmVpi,
       "wfAtmCESStatsAtmVci": wfAtmCESStatsAtmVci,
       "wfAtmCESStatsCbrIndex": wfAtmCESStatsCbrIndex,
       "wfAtmCESStatsVclCct": wfAtmCESStatsVclCct,
       "wfAtmCESStatsReassCells": wfAtmCESStatsReassCells,
       "wfAtmCESStatsHdrErrors": wfAtmCESStatsHdrErrors,
       "wfAtmCESStatsPointerReframes": wfAtmCESStatsPointerReframes,
       "wfAtmCESStatsPointerParityErrors": wfAtmCESStatsPointerParityErrors,
       "wfAtmCESStatsAal1SeqErrors": wfAtmCESStatsAal1SeqErrors,
       "wfAtmCESStatsLostCells": wfAtmCESStatsLostCells,
       "wfAtmCESStatsMisinsertedCells": wfAtmCESStatsMisinsertedCells,
       "wfAtmCESStatsBufUnderflows": wfAtmCESStatsBufUnderflows,
       "wfAtmCESStatsBufOverflows": wfAtmCESStatsBufOverflows,
       "wfAtmCESStatsCellLossStatus": wfAtmCESStatsCellLossStatus}
)
