# SNMP MIB module (CXDDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXDDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:17 2024
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

(Alias,
 SapIndex,
 cxDds) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxDds")

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

_DdsSlotTable_Object = MibTable
ddsSlotTable = _DdsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1)
)
if mibBuilder.loadTexts:
    ddsSlotTable.setStatus("mandatory")
_DdsSlotEntry_Object = MibTableRow
ddsSlotEntry = _DdsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1)
)
ddsSlotEntry.setIndexNames(
    (0, "CXDDS-MIB", "ddsSlotNumber"),
)
if mibBuilder.loadTexts:
    ddsSlotEntry.setStatus("mandatory")
_DdsSlotNumber_Type = SapIndex
_DdsSlotNumber_Object = MibTableColumn
ddsSlotNumber = _DdsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 1),
    _DdsSlotNumber_Type()
)
ddsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotNumber.setStatus("mandatory")
_DdsSlotAlias_Type = Alias
_DdsSlotAlias_Object = MibTableColumn
ddsSlotAlias = _DdsSlotAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 2),
    _DdsSlotAlias_Type()
)
ddsSlotAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotAlias.setStatus("mandatory")


class _DdsSlotRowStatus_Type(Integer32):
    """Custom type ddsSlotRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_DdsSlotRowStatus_Type.__name__ = "Integer32"
_DdsSlotRowStatus_Object = MibTableColumn
ddsSlotRowStatus = _DdsSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 3),
    _DdsSlotRowStatus_Type()
)
ddsSlotRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotRowStatus.setStatus("mandatory")


class _DdsSlotStatus_Type(Integer32):
    """Custom type ddsSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dds-not-present", 1),
          ("dds-present", 2),
          ("dds-present-failed", 3))
    )


_DdsSlotStatus_Type.__name__ = "Integer32"
_DdsSlotStatus_Object = MibTableColumn
ddsSlotStatus = _DdsSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 4),
    _DdsSlotStatus_Type()
)
ddsSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotStatus.setStatus("mandatory")


class _DdsSlotConfigLineType_Type(Integer32):
    """Custom type ddsSlotConfigLineType based on Integer32"""
    defaultValue = 1

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
        *(("ldm-timing-master", 4),
          ("ldm-timing-slave", 3),
          ("telco-multipt", 2),
          ("telco-point-to-point", 1))
    )


_DdsSlotConfigLineType_Type.__name__ = "Integer32"
_DdsSlotConfigLineType_Object = MibTableColumn
ddsSlotConfigLineType = _DdsSlotConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 5),
    _DdsSlotConfigLineType_Type()
)
ddsSlotConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigLineType.setStatus("mandatory")


class _DdsSlotConfigLineService_Type(Integer32):
    """Custom type ddsSlotConfigLineService based on Integer32"""
    defaultValue = 3

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
        *(("clear-channel-64K", 1),
          ("dds-19200", 4),
          ("dds-2400", 7),
          ("dds-4800", 6),
          ("dds-56K", 3),
          ("dds-9600", 5),
          ("switched-56K", 2))
    )


_DdsSlotConfigLineService_Type.__name__ = "Integer32"
_DdsSlotConfigLineService_Object = MibTableColumn
ddsSlotConfigLineService = _DdsSlotConfigLineService_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 6),
    _DdsSlotConfigLineService_Type()
)
ddsSlotConfigLineService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigLineService.setStatus("mandatory")


class _DdsSlotConfigLoopback_Type(Integer32):
    """Custom type ddsSlotConfigLoopback based on Integer32"""
    defaultValue = 1

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
        *(("dte-loopback", 2),
          ("loop2", 3),
          ("loop3", 4),
          ("loop4", 5),
          ("no-loopback", 1),
          ("remote-loop2", 6))
    )


_DdsSlotConfigLoopback_Type.__name__ = "Integer32"
_DdsSlotConfigLoopback_Object = MibTableColumn
ddsSlotConfigLoopback = _DdsSlotConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 7),
    _DdsSlotConfigLoopback_Type()
)
ddsSlotConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigLoopback.setStatus("mandatory")


class _DdsSlotConfigRemLoop2LocalAddress_Type(Integer32):
    """Custom type ddsSlotConfigRemLoop2LocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdsSlotConfigRemLoop2LocalAddress_Type.__name__ = "Integer32"
_DdsSlotConfigRemLoop2LocalAddress_Object = MibTableColumn
ddsSlotConfigRemLoop2LocalAddress = _DdsSlotConfigRemLoop2LocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 8),
    _DdsSlotConfigRemLoop2LocalAddress_Type()
)
ddsSlotConfigRemLoop2LocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigRemLoop2LocalAddress.setStatus("mandatory")


class _DdsSlotConfigRemLoop2RemoteAddress_Type(Integer32):
    """Custom type ddsSlotConfigRemLoop2RemoteAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdsSlotConfigRemLoop2RemoteAddress_Type.__name__ = "Integer32"
_DdsSlotConfigRemLoop2RemoteAddress_Object = MibTableColumn
ddsSlotConfigRemLoop2RemoteAddress = _DdsSlotConfigRemLoop2RemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 9),
    _DdsSlotConfigRemLoop2RemoteAddress_Type()
)
ddsSlotConfigRemLoop2RemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigRemLoop2RemoteAddress.setStatus("mandatory")


class _DdsSlotConfigPatternGen_Type(Integer32):
    """Custom type ddsSlotConfigPatternGen based on Integer32"""
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
        *(("no-pattern", 1),
          ("pattern-511", 2),
          ("pattern-511-with-errors", 3))
    )


_DdsSlotConfigPatternGen_Type.__name__ = "Integer32"
_DdsSlotConfigPatternGen_Object = MibTableColumn
ddsSlotConfigPatternGen = _DdsSlotConfigPatternGen_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 10),
    _DdsSlotConfigPatternGen_Type()
)
ddsSlotConfigPatternGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotConfigPatternGen.setStatus("mandatory")


class _DdsSlotDialNumber_Type(DisplayString):
    """Custom type ddsSlotDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DdsSlotDialNumber_Type.__name__ = "DisplayString"
_DdsSlotDialNumber_Object = MibTableColumn
ddsSlotDialNumber = _DdsSlotDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 11),
    _DdsSlotDialNumber_Type()
)
ddsSlotDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotDialNumber.setStatus("mandatory")


class _DdsSlotSoftwareRevision_Type(Integer32):
    """Custom type ddsSlotSoftwareRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdsSlotSoftwareRevision_Type.__name__ = "Integer32"
_DdsSlotSoftwareRevision_Object = MibTableColumn
ddsSlotSoftwareRevision = _DdsSlotSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 12),
    _DdsSlotSoftwareRevision_Type()
)
ddsSlotSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotSoftwareRevision.setStatus("mandatory")


class _DdsSlotStuffingOption_Type(Integer32):
    """Custom type ddsSlotStuffingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccc-installed", 1),
          ("ccc-not-installed", 2))
    )


_DdsSlotStuffingOption_Type.__name__ = "Integer32"
_DdsSlotStuffingOption_Object = MibTableColumn
ddsSlotStuffingOption = _DdsSlotStuffingOption_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 13),
    _DdsSlotStuffingOption_Type()
)
ddsSlotStuffingOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotStuffingOption.setStatus("mandatory")


class _DdsSlotLineQuality_Type(Integer32):
    """Custom type ddsSlotLineQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("network-error-oos", 3),
          ("no-link", 2))
    )


_DdsSlotLineQuality_Type.__name__ = "Integer32"
_DdsSlotLineQuality_Object = MibTableColumn
ddsSlotLineQuality = _DdsSlotLineQuality_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 14),
    _DdsSlotLineQuality_Type()
)
ddsSlotLineQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotLineQuality.setStatus("mandatory")


class _DdsSlotLineRelativeReceiveLevelMin_Type(Integer32):
    """Custom type ddsSlotLineRelativeReceiveLevelMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdsSlotLineRelativeReceiveLevelMin_Type.__name__ = "Integer32"
_DdsSlotLineRelativeReceiveLevelMin_Object = MibTableColumn
ddsSlotLineRelativeReceiveLevelMin = _DdsSlotLineRelativeReceiveLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 15),
    _DdsSlotLineRelativeReceiveLevelMin_Type()
)
ddsSlotLineRelativeReceiveLevelMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotLineRelativeReceiveLevelMin.setStatus("mandatory")


class _DdsSlotLineRelativeReceiveLevelMax_Type(Integer32):
    """Custom type ddsSlotLineRelativeReceiveLevelMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DdsSlotLineRelativeReceiveLevelMax_Type.__name__ = "Integer32"
_DdsSlotLineRelativeReceiveLevelMax_Object = MibTableColumn
ddsSlotLineRelativeReceiveLevelMax = _DdsSlotLineRelativeReceiveLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 16),
    _DdsSlotLineRelativeReceiveLevelMax_Type()
)
ddsSlotLineRelativeReceiveLevelMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotLineRelativeReceiveLevelMax.setStatus("mandatory")


class _DdsSlotLineLoopback_Type(Integer32):
    """Custom type ddsSlotLineLoopback based on Integer32"""
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
        *(("csu-loopback", 2),
          ("dsu-loopback", 3),
          ("dte-loopback", 4),
          ("loop2", 5),
          ("loop3", 6),
          ("loop4", 7),
          ("none", 1),
          ("remote-loop2", 8))
    )


_DdsSlotLineLoopback_Type.__name__ = "Integer32"
_DdsSlotLineLoopback_Object = MibTableColumn
ddsSlotLineLoopback = _DdsSlotLineLoopback_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 17),
    _DdsSlotLineLoopback_Type()
)
ddsSlotLineLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotLineLoopback.setStatus("mandatory")


class _DdsSlotResultErtPatternDetect_Type(Integer32):
    """Custom type ddsSlotResultErtPatternDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving-pattern", 1),
          ("receiving-patt-with-errors", 3),
          ("receiving-pattern", 2))
    )


_DdsSlotResultErtPatternDetect_Type.__name__ = "Integer32"
_DdsSlotResultErtPatternDetect_Object = MibTableColumn
ddsSlotResultErtPatternDetect = _DdsSlotResultErtPatternDetect_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 18),
    _DdsSlotResultErtPatternDetect_Type()
)
ddsSlotResultErtPatternDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotResultErtPatternDetect.setStatus("mandatory")


class _DdsSlotResultPatternGen_Type(Integer32):
    """Custom type ddsSlotResultPatternGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ert-pattern", 2),
          ("ert-with-errors", 3),
          ("no-pattern", 1))
    )


_DdsSlotResultPatternGen_Type.__name__ = "Integer32"
_DdsSlotResultPatternGen_Object = MibTableColumn
ddsSlotResultPatternGen = _DdsSlotResultPatternGen_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 19),
    _DdsSlotResultPatternGen_Type()
)
ddsSlotResultPatternGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotResultPatternGen.setStatus("mandatory")


class _DdsSlotResultDialing_Type(Integer32):
    """Custom type ddsSlotResultDialing based on Integer32"""
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
        *(("connection-made", 3),
          ("dialing-idle", 1),
          ("dialing-now", 2),
          ("err-invalid-wink", 8),
          ("err-no-answer", 9),
          ("err-no-link", 5),
          ("err-no-num-from-host", 4),
          ("err-no-rx-idle", 6),
          ("err-no-wink", 7))
    )


_DdsSlotResultDialing_Type.__name__ = "Integer32"
_DdsSlotResultDialing_Object = MibTableColumn
ddsSlotResultDialing = _DdsSlotResultDialing_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 20),
    _DdsSlotResultDialing_Type()
)
ddsSlotResultDialing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotResultDialing.setStatus("mandatory")


class _DdsSlotModel_Type(Integer32):
    """Custom type ddsSlotModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DdsSlotModel_Type.__name__ = "Integer32"
_DdsSlotModel_Object = MibTableColumn
ddsSlotModel = _DdsSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 21),
    _DdsSlotModel_Type()
)
ddsSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotModel.setStatus("mandatory")


class _DdsSlotRevision_Type(Integer32):
    """Custom type ddsSlotRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DdsSlotRevision_Type.__name__ = "Integer32"
_DdsSlotRevision_Object = MibTableColumn
ddsSlotRevision = _DdsSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 22),
    _DdsSlotRevision_Type()
)
ddsSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotRevision.setStatus("mandatory")


class _DdsSlotEco_Type(Integer32):
    """Custom type ddsSlotEco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DdsSlotEco_Type.__name__ = "Integer32"
_DdsSlotEco_Object = MibTableColumn
ddsSlotEco = _DdsSlotEco_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 23),
    _DdsSlotEco_Type()
)
ddsSlotEco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsSlotEco.setStatus("mandatory")


class _DdsSlotLineTrap_Type(Integer32):
    """Custom type ddsSlotLineTrap based on Integer32"""
    defaultValue = 1

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


_DdsSlotLineTrap_Type.__name__ = "Integer32"
_DdsSlotLineTrap_Object = MibTableColumn
ddsSlotLineTrap = _DdsSlotLineTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 24),
    _DdsSlotLineTrap_Type()
)
ddsSlotLineTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotLineTrap.setStatus("mandatory")


class _DdsSlotLoopTrap_Type(Integer32):
    """Custom type ddsSlotLoopTrap based on Integer32"""
    defaultValue = 1

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


_DdsSlotLoopTrap_Type.__name__ = "Integer32"
_DdsSlotLoopTrap_Object = MibTableColumn
ddsSlotLoopTrap = _DdsSlotLoopTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 25),
    _DdsSlotLoopTrap_Type()
)
ddsSlotLoopTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsSlotLoopTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ddsSlotLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 0, 1)
)
ddsSlotLineStatusChange.setObjects(
      *(("CXDDS-MIB", "ddsSlotNumber"),
        ("CXDDS-MIB", "ddsSlotLineQuality"))
)
if mibBuilder.loadTexts:
    ddsSlotLineStatusChange.setStatus(
        ""
    )

ddsSlotLoopStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 0, 2)
)
ddsSlotLoopStatusChange.setObjects(
      *(("CXDDS-MIB", "ddsSlotNumber"),
        ("CXDDS-MIB", "ddsSlotLineLoopback"))
)
if mibBuilder.loadTexts:
    ddsSlotLoopStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXDDS-MIB",
    **{"ddsSlotLineStatusChange": ddsSlotLineStatusChange,
       "ddsSlotLoopStatusChange": ddsSlotLoopStatusChange,
       "ddsSlotTable": ddsSlotTable,
       "ddsSlotEntry": ddsSlotEntry,
       "ddsSlotNumber": ddsSlotNumber,
       "ddsSlotAlias": ddsSlotAlias,
       "ddsSlotRowStatus": ddsSlotRowStatus,
       "ddsSlotStatus": ddsSlotStatus,
       "ddsSlotConfigLineType": ddsSlotConfigLineType,
       "ddsSlotConfigLineService": ddsSlotConfigLineService,
       "ddsSlotConfigLoopback": ddsSlotConfigLoopback,
       "ddsSlotConfigRemLoop2LocalAddress": ddsSlotConfigRemLoop2LocalAddress,
       "ddsSlotConfigRemLoop2RemoteAddress": ddsSlotConfigRemLoop2RemoteAddress,
       "ddsSlotConfigPatternGen": ddsSlotConfigPatternGen,
       "ddsSlotDialNumber": ddsSlotDialNumber,
       "ddsSlotSoftwareRevision": ddsSlotSoftwareRevision,
       "ddsSlotStuffingOption": ddsSlotStuffingOption,
       "ddsSlotLineQuality": ddsSlotLineQuality,
       "ddsSlotLineRelativeReceiveLevelMin": ddsSlotLineRelativeReceiveLevelMin,
       "ddsSlotLineRelativeReceiveLevelMax": ddsSlotLineRelativeReceiveLevelMax,
       "ddsSlotLineLoopback": ddsSlotLineLoopback,
       "ddsSlotResultErtPatternDetect": ddsSlotResultErtPatternDetect,
       "ddsSlotResultPatternGen": ddsSlotResultPatternGen,
       "ddsSlotResultDialing": ddsSlotResultDialing,
       "ddsSlotModel": ddsSlotModel,
       "ddsSlotRevision": ddsSlotRevision,
       "ddsSlotEco": ddsSlotEco,
       "ddsSlotLineTrap": ddsSlotLineTrap,
       "ddsSlotLoopTrap": ddsSlotLoopTrap}
)
