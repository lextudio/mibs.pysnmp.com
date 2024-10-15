# SNMP MIB module (CISCO-ADSL-DMT-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ADSL-DMT-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:33 2024
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

(adslLineAlarmConfProfileName,
 adslLineConfProfileName) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineAlarmConfProfileName",
    "adslLineConfProfileName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAdslDmtLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130)
)
ciscoAdslDmtLineMIB.setRevisions(
        ("2001-05-17 16:00",
         "2000-08-22 00:00",
         "2000-05-19 00:00",
         "1999-03-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DmtOverheadFraming(Integer32, TextualConvention):
    status = "current"
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
        *(("structure0", 0),
          ("structure1", 1),
          ("structure2", 2),
          ("structure3", 3))
    )



class DmtFecSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(14, 14),
        ValueRangeConstraint(16, 16),
    )



class DmtCodewordSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAdslDmtLineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBObjects = _CiscoAdslDmtLineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1)
)
_CAdslDmtLineTable_Object = MibTable
cAdslDmtLineTable = _CAdslDmtLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 1)
)
if mibBuilder.loadTexts:
    cAdslDmtLineTable.setStatus("current")
_CAdslDmtLineEntry_Object = MibTableRow
cAdslDmtLineEntry = _CAdslDmtLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 1, 1)
)
cAdslDmtLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslDmtLineEntry.setStatus("current")
_CAdslDmtLineOverheadFraming_Type = DmtOverheadFraming
_CAdslDmtLineOverheadFraming_Object = MibTableColumn
cAdslDmtLineOverheadFraming = _CAdslDmtLineOverheadFraming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 1, 1, 1),
    _CAdslDmtLineOverheadFraming_Type()
)
cAdslDmtLineOverheadFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslDmtLineOverheadFraming.setStatus("current")
_CAdslAtucDmtPhysTable_Object = MibTable
cAdslAtucDmtPhysTable = _CAdslAtucDmtPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 2)
)
if mibBuilder.loadTexts:
    cAdslAtucDmtPhysTable.setStatus("current")
_CAdslAtucDmtPhysEntry_Object = MibTableRow
cAdslAtucDmtPhysEntry = _CAdslAtucDmtPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 2, 1)
)
cAdslAtucDmtPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAtucDmtPhysEntry.setStatus("current")


class _CAdslAtucDmtState_Type(Integer32):
    """Custom type cAdslAtucDmtState based on Integer32"""
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
        *(("downloadFailed", 4),
          ("downloading", 3),
          ("standard", 1),
          ("testing", 5),
          ("unknown", 2))
    )


_CAdslAtucDmtState_Type.__name__ = "Integer32"
_CAdslAtucDmtState_Object = MibTableColumn
cAdslAtucDmtState = _CAdslAtucDmtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 2, 1, 1),
    _CAdslAtucDmtState_Type()
)
cAdslAtucDmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtState.setStatus("current")
_CAdslAtucDmtChanTable_Object = MibTable
cAdslAtucDmtChanTable = _CAdslAtucDmtChanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 4)
)
if mibBuilder.loadTexts:
    cAdslAtucDmtChanTable.setStatus("current")
_CAdslAtucDmtChanEntry_Object = MibTableRow
cAdslAtucDmtChanEntry = _CAdslAtucDmtChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 4, 1)
)
cAdslAtucDmtChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAtucDmtChanEntry.setStatus("current")
_CAdslAtucDmtChanFecSize_Type = DmtFecSize
_CAdslAtucDmtChanFecSize_Object = MibTableColumn
cAdslAtucDmtChanFecSize = _CAdslAtucDmtChanFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 4, 1, 1),
    _CAdslAtucDmtChanFecSize_Type()
)
cAdslAtucDmtChanFecSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtChanFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtChanFecSize.setUnits("bytes")
_CAdslAtucDmtChanCodewordSize_Type = DmtCodewordSize
_CAdslAtucDmtChanCodewordSize_Object = MibTableColumn
cAdslAtucDmtChanCodewordSize = _CAdslAtucDmtChanCodewordSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 4, 1, 2),
    _CAdslAtucDmtChanCodewordSize_Type()
)
cAdslAtucDmtChanCodewordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtChanCodewordSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtChanCodewordSize.setUnits("symbols")
_CAdslAturDmtChanTable_Object = MibTable
cAdslAturDmtChanTable = _CAdslAturDmtChanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 5)
)
if mibBuilder.loadTexts:
    cAdslAturDmtChanTable.setStatus("current")
_CAdslAturDmtChanEntry_Object = MibTableRow
cAdslAturDmtChanEntry = _CAdslAturDmtChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 5, 1)
)
cAdslAturDmtChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cAdslAturDmtChanEntry.setStatus("current")
_CAdslAturDmtChanFecSize_Type = DmtFecSize
_CAdslAturDmtChanFecSize_Object = MibTableColumn
cAdslAturDmtChanFecSize = _CAdslAturDmtChanFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 5, 1, 1),
    _CAdslAturDmtChanFecSize_Type()
)
cAdslAturDmtChanFecSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturDmtChanFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtChanFecSize.setUnits("bytes")
_CAdslAturDmtChanCodewordSize_Type = DmtCodewordSize
_CAdslAturDmtChanCodewordSize_Object = MibTableColumn
cAdslAturDmtChanCodewordSize = _CAdslAturDmtChanCodewordSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 5, 1, 2),
    _CAdslAturDmtChanCodewordSize_Type()
)
cAdslAturDmtChanCodewordSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturDmtChanCodewordSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtChanCodewordSize.setUnits("symbols")
_CAdslDmtLineConfProfileTable_Object = MibTable
cAdslDmtLineConfProfileTable = _CAdslDmtLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14)
)
if mibBuilder.loadTexts:
    cAdslDmtLineConfProfileTable.setStatus("current")
_CAdslDmtLineConfProfileEntry_Object = MibTableRow
cAdslDmtLineConfProfileEntry = _CAdslDmtLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1)
)
cAdslDmtLineConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    cAdslDmtLineConfProfileEntry.setStatus("current")


class _CAdslLineDmtConfOperatingMode_Type(Integer32):
    """Custom type cAdslLineDmtConfOperatingMode based on Integer32"""
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
        *(("automatic", 1),
          ("g992Dot1", 3),
          ("g992Dot2", 4),
          ("splitterless", 2),
          ("t1Dot413", 5))
    )


_CAdslLineDmtConfOperatingMode_Type.__name__ = "Integer32"
_CAdslLineDmtConfOperatingMode_Object = MibTableColumn
cAdslLineDmtConfOperatingMode = _CAdslLineDmtConfOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 1),
    _CAdslLineDmtConfOperatingMode_Type()
)
cAdslLineDmtConfOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslLineDmtConfOperatingMode.setStatus("current")


class _CAdslLineDmtConfTrainingMode_Type(Integer32):
    """Custom type cAdslLineDmtConfTrainingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("standard", 1))
    )


_CAdslLineDmtConfTrainingMode_Type.__name__ = "Integer32"
_CAdslLineDmtConfTrainingMode_Object = MibTableColumn
cAdslLineDmtConfTrainingMode = _CAdslLineDmtConfTrainingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 2),
    _CAdslLineDmtConfTrainingMode_Type()
)
cAdslLineDmtConfTrainingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslLineDmtConfTrainingMode.setStatus("current")


class _CAdslAtucDmtConfFastFecSize_Type(DmtFecSize):
    """Custom type cAdslAtucDmtConfFastFecSize based on DmtFecSize"""
    defaultValue = 16


_CAdslAtucDmtConfFastFecSize_Object = MibTableColumn
cAdslAtucDmtConfFastFecSize = _CAdslAtucDmtConfFastFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 3),
    _CAdslAtucDmtConfFastFecSize_Type()
)
cAdslAtucDmtConfFastFecSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfFastFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfFastFecSize.setUnits("bytes")


class _CAdslAtucDmtConfInterleaveFecSize_Type(DmtFecSize):
    """Custom type cAdslAtucDmtConfInterleaveFecSize based on DmtFecSize"""
    defaultValue = 16


_CAdslAtucDmtConfInterleaveFecSize_Object = MibTableColumn
cAdslAtucDmtConfInterleaveFecSize = _CAdslAtucDmtConfInterleaveFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 4),
    _CAdslAtucDmtConfInterleaveFecSize_Type()
)
cAdslAtucDmtConfInterleaveFecSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfInterleaveFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfInterleaveFecSize.setUnits("bytes")


class _CAdslAtucDmtConfCodewordSize_Type(DmtCodewordSize):
    """Custom type cAdslAtucDmtConfCodewordSize based on DmtCodewordSize"""
    defaultValue = 16


_CAdslAtucDmtConfCodewordSize_Object = MibTableColumn
cAdslAtucDmtConfCodewordSize = _CAdslAtucDmtConfCodewordSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 5),
    _CAdslAtucDmtConfCodewordSize_Type()
)
cAdslAtucDmtConfCodewordSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfCodewordSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfCodewordSize.setUnits("symbols")


class _CAdslAtucDmtConfOverheadFraming_Type(DmtOverheadFraming):
    """Custom type cAdslAtucDmtConfOverheadFraming based on DmtOverheadFraming"""


_CAdslAtucDmtConfOverheadFraming_Object = MibTableColumn
cAdslAtucDmtConfOverheadFraming = _CAdslAtucDmtConfOverheadFraming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 6),
    _CAdslAtucDmtConfOverheadFraming_Type()
)
cAdslAtucDmtConfOverheadFraming.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfOverheadFraming.setStatus("current")


class _CAdslAtucDmtConfBitSwapEnabled_Type(TruthValue):
    """Custom type cAdslAtucDmtConfBitSwapEnabled based on TruthValue"""


_CAdslAtucDmtConfBitSwapEnabled_Object = MibTableColumn
cAdslAtucDmtConfBitSwapEnabled = _CAdslAtucDmtConfBitSwapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 7),
    _CAdslAtucDmtConfBitSwapEnabled_Type()
)
cAdslAtucDmtConfBitSwapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfBitSwapEnabled.setStatus("current")


class _CAdslAtucDmtConfBitSwapFrom_Type(Integer32):
    """Custom type cAdslAtucDmtConfBitSwapFrom based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CAdslAtucDmtConfBitSwapFrom_Type.__name__ = "Integer32"
_CAdslAtucDmtConfBitSwapFrom_Object = MibTableColumn
cAdslAtucDmtConfBitSwapFrom = _CAdslAtucDmtConfBitSwapFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 8),
    _CAdslAtucDmtConfBitSwapFrom_Type()
)
cAdslAtucDmtConfBitSwapFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfBitSwapFrom.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfBitSwapFrom.setUnits("dB")


class _CAdslAtucDmtConfBitSwapTo_Type(Integer32):
    """Custom type cAdslAtucDmtConfBitSwapTo based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CAdslAtucDmtConfBitSwapTo_Type.__name__ = "Integer32"
_CAdslAtucDmtConfBitSwapTo_Object = MibTableColumn
cAdslAtucDmtConfBitSwapTo = _CAdslAtucDmtConfBitSwapTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 9),
    _CAdslAtucDmtConfBitSwapTo_Type()
)
cAdslAtucDmtConfBitSwapTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfBitSwapTo.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfBitSwapTo.setUnits("dB")


class _CAdslAturDmtConfFastFecSize_Type(DmtFecSize):
    """Custom type cAdslAturDmtConfFastFecSize based on DmtFecSize"""
    defaultValue = 16


_CAdslAturDmtConfFastFecSize_Object = MibTableColumn
cAdslAturDmtConfFastFecSize = _CAdslAturDmtConfFastFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 10),
    _CAdslAturDmtConfFastFecSize_Type()
)
cAdslAturDmtConfFastFecSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturDmtConfFastFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtConfFastFecSize.setUnits("bytes")


class _CAdslAturDmtConfInterleaveFecSize_Type(DmtFecSize):
    """Custom type cAdslAturDmtConfInterleaveFecSize based on DmtFecSize"""
    defaultValue = 16


_CAdslAturDmtConfInterleaveFecSize_Object = MibTableColumn
cAdslAturDmtConfInterleaveFecSize = _CAdslAturDmtConfInterleaveFecSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 11),
    _CAdslAturDmtConfInterleaveFecSize_Type()
)
cAdslAturDmtConfInterleaveFecSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturDmtConfInterleaveFecSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtConfInterleaveFecSize.setUnits("bytes")


class _CAdslAturDmtConfCodewordSize_Type(DmtCodewordSize):
    """Custom type cAdslAturDmtConfCodewordSize based on DmtCodewordSize"""
    defaultValue = 16


_CAdslAturDmtConfCodewordSize_Object = MibTableColumn
cAdslAturDmtConfCodewordSize = _CAdslAturDmtConfCodewordSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 12),
    _CAdslAturDmtConfCodewordSize_Type()
)
cAdslAturDmtConfCodewordSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturDmtConfCodewordSize.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtConfCodewordSize.setUnits("symbols")


class _CAdslAtucDmtConfMinrateBlock_Type(TruthValue):
    """Custom type cAdslAtucDmtConfMinrateBlock based on TruthValue"""


_CAdslAtucDmtConfMinrateBlock_Object = MibTableColumn
cAdslAtucDmtConfMinrateBlock = _CAdslAtucDmtConfMinrateBlock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 13),
    _CAdslAtucDmtConfMinrateBlock_Type()
)
cAdslAtucDmtConfMinrateBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtConfMinrateBlock.setStatus("current")


class _CAdslAtucDmtDualBitmapEnabled_Type(TruthValue):
    """Custom type cAdslAtucDmtDualBitmapEnabled based on TruthValue"""


_CAdslAtucDmtDualBitmapEnabled_Object = MibTableColumn
cAdslAtucDmtDualBitmapEnabled = _CAdslAtucDmtDualBitmapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 14, 1, 14),
    _CAdslAtucDmtDualBitmapEnabled_Type()
)
cAdslAtucDmtDualBitmapEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtDualBitmapEnabled.setStatus("current")
_CAdslDmtLineAlarmConfProfileTable_Object = MibTable
cAdslDmtLineAlarmConfProfileTable = _CAdslDmtLineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 15)
)
if mibBuilder.loadTexts:
    cAdslDmtLineAlarmConfProfileTable.setStatus("current")
_CAdslDmtLineAlarmConfProfileEntry_Object = MibTableRow
cAdslDmtLineAlarmConfProfileEntry = _CAdslDmtLineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 15, 1)
)
cAdslDmtLineAlarmConfProfileEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    cAdslDmtLineAlarmConfProfileEntry.setStatus("current")


class _CAdslAtucDmtThreshRateFallback_Type(Integer32):
    """Custom type cAdslAtucDmtThreshRateFallback based on Integer32"""
    defaultValue = 0


_CAdslAtucDmtThreshRateFallback_Object = MibTableColumn
cAdslAtucDmtThreshRateFallback = _CAdslAtucDmtThreshRateFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 15, 1, 1),
    _CAdslAtucDmtThreshRateFallback_Type()
)
cAdslAtucDmtThreshRateFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAtucDmtThreshRateFallback.setStatus("current")


class _CAdslAturDmtThreshRateFallback_Type(Integer32):
    """Custom type cAdslAturDmtThreshRateFallback based on Integer32"""
    defaultValue = 0


_CAdslAturDmtThreshRateFallback_Object = MibTableColumn
cAdslAturDmtThreshRateFallback = _CAdslAturDmtThreshRateFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 15, 1, 2),
    _CAdslAturDmtThreshRateFallback_Type()
)
cAdslAturDmtThreshRateFallback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cAdslAturDmtThreshRateFallback.setStatus("current")
_CAdslDmtBinIfNumber_Type = InterfaceIndexOrZero
_CAdslDmtBinIfNumber_Object = MibScalar
cAdslDmtBinIfNumber = _CAdslDmtBinIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 16),
    _CAdslDmtBinIfNumber_Type()
)
cAdslDmtBinIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAdslDmtBinIfNumber.setStatus("current")


class _CAdslDmtBinIfRqstStatus_Type(Integer32):
    """Custom type cAdslDmtBinIfRqstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
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
        *(("failure", 7),
          ("ifConfigured", 3),
          ("ifUntrained", 6),
          ("lcDownForIf", 5),
          ("noIfConfigured", 2),
          ("pollNow", 1),
          ("reset", -1),
          ("rqstInProgess", 4),
          ("success", 8))
    )


_CAdslDmtBinIfRqstStatus_Type.__name__ = "Integer32"
_CAdslDmtBinIfRqstStatus_Object = MibScalar
cAdslDmtBinIfRqstStatus = _CAdslDmtBinIfRqstStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 17),
    _CAdslDmtBinIfRqstStatus_Type()
)
cAdslDmtBinIfRqstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cAdslDmtBinIfRqstStatus.setStatus("current")
_CAdslDmtBinIfLstRqstUpldTime_Type = DateAndTime
_CAdslDmtBinIfLstRqstUpldTime_Object = MibScalar
cAdslDmtBinIfLstRqstUpldTime = _CAdslDmtBinIfLstRqstUpldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 18),
    _CAdslDmtBinIfLstRqstUpldTime_Type()
)
cAdslDmtBinIfLstRqstUpldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslDmtBinIfLstRqstUpldTime.setStatus("current")
_CAdslAtucDmtBinTable_Object = MibTable
cAdslAtucDmtBinTable = _CAdslAtucDmtBinTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19)
)
if mibBuilder.loadTexts:
    cAdslAtucDmtBinTable.setStatus("current")
_CAdslAtucDmtBinEntry_Object = MibTableRow
cAdslAtucDmtBinEntry = _CAdslAtucDmtBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1)
)
cAdslAtucDmtBinEntry.setIndexNames(
    (0, "CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtBitmapIndex"),
    (0, "CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtBinIndex"),
)
if mibBuilder.loadTexts:
    cAdslAtucDmtBinEntry.setStatus("current")


class _CAdslAtucDmtBitmapIndex_Type(Unsigned32):
    """Custom type cAdslAtucDmtBitmapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CAdslAtucDmtBitmapIndex_Type.__name__ = "Unsigned32"
_CAdslAtucDmtBitmapIndex_Object = MibTableColumn
cAdslAtucDmtBitmapIndex = _CAdslAtucDmtBitmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1, 1),
    _CAdslAtucDmtBitmapIndex_Type()
)
cAdslAtucDmtBitmapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAdslAtucDmtBitmapIndex.setStatus("current")


class _CAdslAtucDmtBinIndex_Type(Unsigned32):
    """Custom type cAdslAtucDmtBinIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CAdslAtucDmtBinIndex_Type.__name__ = "Unsigned32"
_CAdslAtucDmtBinIndex_Object = MibTableColumn
cAdslAtucDmtBinIndex = _CAdslAtucDmtBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1, 2),
    _CAdslAtucDmtBinIndex_Type()
)
cAdslAtucDmtBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinIndex.setStatus("current")


class _CAdslAtucDmtBinBitAlloc_Type(Unsigned32):
    """Custom type cAdslAtucDmtBinBitAlloc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CAdslAtucDmtBinBitAlloc_Type.__name__ = "Unsigned32"
_CAdslAtucDmtBinBitAlloc_Object = MibTableColumn
cAdslAtucDmtBinBitAlloc = _CAdslAtucDmtBinBitAlloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1, 3),
    _CAdslAtucDmtBinBitAlloc_Type()
)
cAdslAtucDmtBinBitAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinBitAlloc.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinBitAlloc.setUnits("bits/Hz")


class _CAdslAtucDmtBinTxGain_Type(Unsigned32):
    """Custom type cAdslAtucDmtBinTxGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_CAdslAtucDmtBinTxGain_Type.__name__ = "Unsigned32"
_CAdslAtucDmtBinTxGain_Object = MibTableColumn
cAdslAtucDmtBinTxGain = _CAdslAtucDmtBinTxGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1, 4),
    _CAdslAtucDmtBinTxGain_Type()
)
cAdslAtucDmtBinTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinTxGain.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinTxGain.setUnits("tenth dB")


class _CAdslAtucDmtBinNumber_Type(Unsigned32):
    """Custom type cAdslAtucDmtBinNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CAdslAtucDmtBinNumber_Type.__name__ = "Unsigned32"
_CAdslAtucDmtBinNumber_Object = MibTableColumn
cAdslAtucDmtBinNumber = _CAdslAtucDmtBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 19, 1, 5),
    _CAdslAtucDmtBinNumber_Type()
)
cAdslAtucDmtBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAtucDmtBinNumber.setStatus("current")
_CAdslAturDmtBinTable_Object = MibTable
cAdslAturDmtBinTable = _CAdslAturDmtBinTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20)
)
if mibBuilder.loadTexts:
    cAdslAturDmtBinTable.setStatus("current")
_CAdslAturDmtBinEntry_Object = MibTableRow
cAdslAturDmtBinEntry = _CAdslAturDmtBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1)
)
cAdslAturDmtBinEntry.setIndexNames(
    (0, "CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtBitmapIndex"),
    (0, "CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtBinIndex"),
)
if mibBuilder.loadTexts:
    cAdslAturDmtBinEntry.setStatus("current")


class _CAdslAturDmtBitmapIndex_Type(Unsigned32):
    """Custom type cAdslAturDmtBitmapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CAdslAturDmtBitmapIndex_Type.__name__ = "Unsigned32"
_CAdslAturDmtBitmapIndex_Object = MibTableColumn
cAdslAturDmtBitmapIndex = _CAdslAturDmtBitmapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1, 1),
    _CAdslAturDmtBitmapIndex_Type()
)
cAdslAturDmtBitmapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAdslAturDmtBitmapIndex.setStatus("current")


class _CAdslAturDmtBinIndex_Type(Unsigned32):
    """Custom type cAdslAturDmtBinIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CAdslAturDmtBinIndex_Type.__name__ = "Unsigned32"
_CAdslAturDmtBinIndex_Object = MibTableColumn
cAdslAturDmtBinIndex = _CAdslAturDmtBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1, 2),
    _CAdslAturDmtBinIndex_Type()
)
cAdslAturDmtBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cAdslAturDmtBinIndex.setStatus("current")


class _CAdslAturDmtBinBitAlloc_Type(Unsigned32):
    """Custom type cAdslAturDmtBinBitAlloc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CAdslAturDmtBinBitAlloc_Type.__name__ = "Unsigned32"
_CAdslAturDmtBinBitAlloc_Object = MibTableColumn
cAdslAturDmtBinBitAlloc = _CAdslAturDmtBinBitAlloc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1, 3),
    _CAdslAturDmtBinBitAlloc_Type()
)
cAdslAturDmtBinBitAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturDmtBinBitAlloc.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtBinBitAlloc.setUnits("bits/Hz")


class _CAdslAturDmtBinTxGain_Type(Unsigned32):
    """Custom type cAdslAturDmtBinTxGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_CAdslAturDmtBinTxGain_Type.__name__ = "Unsigned32"
_CAdslAturDmtBinTxGain_Object = MibTableColumn
cAdslAturDmtBinTxGain = _CAdslAturDmtBinTxGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1, 4),
    _CAdslAturDmtBinTxGain_Type()
)
cAdslAturDmtBinTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturDmtBinTxGain.setStatus("current")
if mibBuilder.loadTexts:
    cAdslAturDmtBinTxGain.setUnits("hundredth dB")


class _CAdslAturDmtBinNumber_Type(Unsigned32):
    """Custom type cAdslAturDmtBinNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CAdslAturDmtBinNumber_Type.__name__ = "Unsigned32"
_CAdslAturDmtBinNumber_Object = MibTableColumn
cAdslAturDmtBinNumber = _CAdslAturDmtBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 1, 20, 1, 5),
    _CAdslAturDmtBinNumber_Type()
)
cAdslAturDmtBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cAdslAturDmtBinNumber.setStatus("current")
_CiscoAdslDmtLineMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBNotificationsPrefix = _CiscoAdslDmtLineMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 2)
)
_CiscoAdslDmtLineMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBNotifications = _CiscoAdslDmtLineMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 2, 0)
)
_CiscoAdslDmtLineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBConformance = _CiscoAdslDmtLineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3)
)
_CiscoAdslDmtLineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBCompliances = _CiscoAdslDmtLineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 1)
)
_CiscoAdslDmtLineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAdslDmtLineMIBGroups = _CiscoAdslDmtLineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2)
)

# Managed Objects groups

cAdslDmtLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 1)
)
cAdslDmtLineGroup.setObjects(
    ("CISCO-ADSL-DMT-LINE-MIB", "cAdslDmtLineOverheadFraming")
)
if mibBuilder.loadTexts:
    cAdslDmtLineGroup.setStatus("current")

cAdslAtucDmtPhysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 2)
)
cAdslAtucDmtPhysGroup.setObjects(
    ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtState")
)
if mibBuilder.loadTexts:
    cAdslAtucDmtPhysGroup.setStatus("current")

cAdslAtucDmtChanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 3)
)
cAdslAtucDmtChanGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtChanFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtChanCodewordSize"))
)
if mibBuilder.loadTexts:
    cAdslAtucDmtChanGroup.setStatus("current")

cAdslAturDmtChanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 4)
)
cAdslAturDmtChanGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtChanFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtChanCodewordSize"))
)
if mibBuilder.loadTexts:
    cAdslAturDmtChanGroup.setStatus("current")

cAdslDmtLineConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 5)
)
cAdslDmtLineConfProfileGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslLineDmtConfOperatingMode"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslLineDmtConfTrainingMode"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfFastFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfInterleaveFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfCodewordSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfOverheadFraming"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapEnabled"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapFrom"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapTo"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfInterleaveFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfFastFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfCodewordSize"))
)
if mibBuilder.loadTexts:
    cAdslDmtLineConfProfileGroup.setStatus("deprecated")

cAdslDmtLineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 6)
)
cAdslDmtLineAlarmConfProfileGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtThreshRateFallback"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtThreshRateFallback"))
)
if mibBuilder.loadTexts:
    cAdslDmtLineAlarmConfProfileGroup.setStatus("current")

cAdslDmtBinIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 7)
)
cAdslDmtBinIfGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslDmtBinIfNumber"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslDmtBinIfRqstStatus"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslDmtBinIfLstRqstUpldTime"))
)
if mibBuilder.loadTexts:
    cAdslDmtBinIfGroup.setStatus("current")

cAdslAtucDmtBinDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 8)
)
cAdslAtucDmtBinDataGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtBinBitAlloc"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtBinTxGain"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtBinNumber"))
)
if mibBuilder.loadTexts:
    cAdslAtucDmtBinDataGroup.setStatus("current")

cAdslAturDmtBinDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 9)
)
cAdslAturDmtBinDataGroup.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtBinBitAlloc"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtBinTxGain"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtBinNumber"))
)
if mibBuilder.loadTexts:
    cAdslAturDmtBinDataGroup.setStatus("current")

cAdslDmtLineConfProfileGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 2, 10)
)
cAdslDmtLineConfProfileGroupRev1.setObjects(
      *(("CISCO-ADSL-DMT-LINE-MIB", "cAdslLineDmtConfOperatingMode"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslLineDmtConfTrainingMode"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfFastFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfInterleaveFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfCodewordSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfOverheadFraming"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapEnabled"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapFrom"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfBitSwapTo"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfInterleaveFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfFastFecSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAturDmtConfCodewordSize"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtConfMinrateBlock"),
        ("CISCO-ADSL-DMT-LINE-MIB", "cAdslAtucDmtDualBitmapEnabled"))
)
if mibBuilder.loadTexts:
    cAdslDmtLineConfProfileGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAdslDmtLineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAdslDmtLineMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAdslDmtLineMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 130, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAdslDmtLineMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ADSL-DMT-LINE-MIB",
    **{"DmtOverheadFraming": DmtOverheadFraming,
       "DmtFecSize": DmtFecSize,
       "DmtCodewordSize": DmtCodewordSize,
       "ciscoAdslDmtLineMIB": ciscoAdslDmtLineMIB,
       "ciscoAdslDmtLineMIBObjects": ciscoAdslDmtLineMIBObjects,
       "cAdslDmtLineTable": cAdslDmtLineTable,
       "cAdslDmtLineEntry": cAdslDmtLineEntry,
       "cAdslDmtLineOverheadFraming": cAdslDmtLineOverheadFraming,
       "cAdslAtucDmtPhysTable": cAdslAtucDmtPhysTable,
       "cAdslAtucDmtPhysEntry": cAdslAtucDmtPhysEntry,
       "cAdslAtucDmtState": cAdslAtucDmtState,
       "cAdslAtucDmtChanTable": cAdslAtucDmtChanTable,
       "cAdslAtucDmtChanEntry": cAdslAtucDmtChanEntry,
       "cAdslAtucDmtChanFecSize": cAdslAtucDmtChanFecSize,
       "cAdslAtucDmtChanCodewordSize": cAdslAtucDmtChanCodewordSize,
       "cAdslAturDmtChanTable": cAdslAturDmtChanTable,
       "cAdslAturDmtChanEntry": cAdslAturDmtChanEntry,
       "cAdslAturDmtChanFecSize": cAdslAturDmtChanFecSize,
       "cAdslAturDmtChanCodewordSize": cAdslAturDmtChanCodewordSize,
       "cAdslDmtLineConfProfileTable": cAdslDmtLineConfProfileTable,
       "cAdslDmtLineConfProfileEntry": cAdslDmtLineConfProfileEntry,
       "cAdslLineDmtConfOperatingMode": cAdslLineDmtConfOperatingMode,
       "cAdslLineDmtConfTrainingMode": cAdslLineDmtConfTrainingMode,
       "cAdslAtucDmtConfFastFecSize": cAdslAtucDmtConfFastFecSize,
       "cAdslAtucDmtConfInterleaveFecSize": cAdslAtucDmtConfInterleaveFecSize,
       "cAdslAtucDmtConfCodewordSize": cAdslAtucDmtConfCodewordSize,
       "cAdslAtucDmtConfOverheadFraming": cAdslAtucDmtConfOverheadFraming,
       "cAdslAtucDmtConfBitSwapEnabled": cAdslAtucDmtConfBitSwapEnabled,
       "cAdslAtucDmtConfBitSwapFrom": cAdslAtucDmtConfBitSwapFrom,
       "cAdslAtucDmtConfBitSwapTo": cAdslAtucDmtConfBitSwapTo,
       "cAdslAturDmtConfFastFecSize": cAdslAturDmtConfFastFecSize,
       "cAdslAturDmtConfInterleaveFecSize": cAdslAturDmtConfInterleaveFecSize,
       "cAdslAturDmtConfCodewordSize": cAdslAturDmtConfCodewordSize,
       "cAdslAtucDmtConfMinrateBlock": cAdslAtucDmtConfMinrateBlock,
       "cAdslAtucDmtDualBitmapEnabled": cAdslAtucDmtDualBitmapEnabled,
       "cAdslDmtLineAlarmConfProfileTable": cAdslDmtLineAlarmConfProfileTable,
       "cAdslDmtLineAlarmConfProfileEntry": cAdslDmtLineAlarmConfProfileEntry,
       "cAdslAtucDmtThreshRateFallback": cAdslAtucDmtThreshRateFallback,
       "cAdslAturDmtThreshRateFallback": cAdslAturDmtThreshRateFallback,
       "cAdslDmtBinIfNumber": cAdslDmtBinIfNumber,
       "cAdslDmtBinIfRqstStatus": cAdslDmtBinIfRqstStatus,
       "cAdslDmtBinIfLstRqstUpldTime": cAdslDmtBinIfLstRqstUpldTime,
       "cAdslAtucDmtBinTable": cAdslAtucDmtBinTable,
       "cAdslAtucDmtBinEntry": cAdslAtucDmtBinEntry,
       "cAdslAtucDmtBitmapIndex": cAdslAtucDmtBitmapIndex,
       "cAdslAtucDmtBinIndex": cAdslAtucDmtBinIndex,
       "cAdslAtucDmtBinBitAlloc": cAdslAtucDmtBinBitAlloc,
       "cAdslAtucDmtBinTxGain": cAdslAtucDmtBinTxGain,
       "cAdslAtucDmtBinNumber": cAdslAtucDmtBinNumber,
       "cAdslAturDmtBinTable": cAdslAturDmtBinTable,
       "cAdslAturDmtBinEntry": cAdslAturDmtBinEntry,
       "cAdslAturDmtBitmapIndex": cAdslAturDmtBitmapIndex,
       "cAdslAturDmtBinIndex": cAdslAturDmtBinIndex,
       "cAdslAturDmtBinBitAlloc": cAdslAturDmtBinBitAlloc,
       "cAdslAturDmtBinTxGain": cAdslAturDmtBinTxGain,
       "cAdslAturDmtBinNumber": cAdslAturDmtBinNumber,
       "ciscoAdslDmtLineMIBNotificationsPrefix": ciscoAdslDmtLineMIBNotificationsPrefix,
       "ciscoAdslDmtLineMIBNotifications": ciscoAdslDmtLineMIBNotifications,
       "ciscoAdslDmtLineMIBConformance": ciscoAdslDmtLineMIBConformance,
       "ciscoAdslDmtLineMIBCompliances": ciscoAdslDmtLineMIBCompliances,
       "ciscoAdslDmtLineMIBCompliance": ciscoAdslDmtLineMIBCompliance,
       "ciscoAdslDmtLineMIBComplianceRev1": ciscoAdslDmtLineMIBComplianceRev1,
       "ciscoAdslDmtLineMIBGroups": ciscoAdslDmtLineMIBGroups,
       "cAdslDmtLineGroup": cAdslDmtLineGroup,
       "cAdslAtucDmtPhysGroup": cAdslAtucDmtPhysGroup,
       "cAdslAtucDmtChanGroup": cAdslAtucDmtChanGroup,
       "cAdslAturDmtChanGroup": cAdslAturDmtChanGroup,
       "cAdslDmtLineConfProfileGroup": cAdslDmtLineConfProfileGroup,
       "cAdslDmtLineAlarmConfProfileGroup": cAdslDmtLineAlarmConfProfileGroup,
       "cAdslDmtBinIfGroup": cAdslDmtBinIfGroup,
       "cAdslAtucDmtBinDataGroup": cAdslAtucDmtBinDataGroup,
       "cAdslAturDmtBinDataGroup": cAdslAturDmtBinDataGroup,
       "cAdslDmtLineConfProfileGroupRev1": cAdslDmtLineConfProfileGroupRev1}
)
