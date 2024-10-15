# SNMP MIB module (Fore-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:12 2024
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

(asx,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "asx")

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

foreSonetModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetConfGroup_ObjectIdentity = ObjectIdentity
sonetConfGroup = _SonetConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1)
)
_SonetConfTable_Object = MibTable
sonetConfTable = _SonetConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sonetConfTable.setStatus("current")
_SonetConfEntry_Object = MibTableRow
sonetConfEntry = _SonetConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1)
)
sonetConfEntry.setIndexNames(
    (0, "Fore-SONET-MIB", "sonetConfBoard"),
    (0, "Fore-SONET-MIB", "sonetConfModule"),
    (0, "Fore-SONET-MIB", "sonetConfPort"),
)
if mibBuilder.loadTexts:
    sonetConfEntry.setStatus("current")
_SonetConfBoard_Type = Integer32
_SonetConfBoard_Object = MibTableColumn
sonetConfBoard = _SonetConfBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 1),
    _SonetConfBoard_Type()
)
sonetConfBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetConfBoard.setStatus("current")
_SonetConfModule_Type = Integer32
_SonetConfModule_Object = MibTableColumn
sonetConfModule = _SonetConfModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 2),
    _SonetConfModule_Type()
)
sonetConfModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetConfModule.setStatus("current")
_SonetConfPort_Type = Integer32
_SonetConfPort_Object = MibTableColumn
sonetConfPort = _SonetConfPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 3),
    _SonetConfPort_Type()
)
sonetConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetConfPort.setStatus("current")


class _SonetLineType_Type(Integer32):
    """Custom type sonetLineType based on Integer32"""
    defaultValue = 4

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
        *(("sonetCoax", 6),
          ("sonetMultiMode", 4),
          ("sonetOther", 1),
          ("sonetSingleModeMediumRange", 3),
          ("sonetSingleModeShortRange", 2),
          ("sonetUTP", 5))
    )


_SonetLineType_Type.__name__ = "Integer32"
_SonetLineType_Object = MibTableColumn
sonetLineType = _SonetLineType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 4),
    _SonetLineType_Type()
)
sonetLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineType.setStatus("current")


class _SonetLineCoding_Type(Integer32):
    """Custom type sonetLineCoding based on Integer32"""
    defaultValue = 4

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
        *(("sonetB3ZS", 2),
          ("sonetCMI", 3),
          ("sonetNRZ", 4),
          ("sonetOther", 1),
          ("sonetRZ", 5))
    )


_SonetLineCoding_Type.__name__ = "Integer32"
_SonetLineCoding_Object = MibTableColumn
sonetLineCoding = _SonetLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 5),
    _SonetLineCoding_Type()
)
sonetLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineCoding.setStatus("current")


class _SonetFramingStandardDefault_Type(Integer32):
    """Custom type sonetFramingStandardDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmSDH", 2),
          ("atmSONET", 1))
    )


_SonetFramingStandardDefault_Type.__name__ = "Integer32"
_SonetFramingStandardDefault_Object = MibTableColumn
sonetFramingStandardDefault = _SonetFramingStandardDefault_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 6),
    _SonetFramingStandardDefault_Type()
)
sonetFramingStandardDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetFramingStandardDefault.setStatus("current")


class _SonetFramingStandardOper_Type(Integer32):
    """Custom type sonetFramingStandardOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmSDH", 2),
          ("atmSONET", 1))
    )


_SonetFramingStandardOper_Type.__name__ = "Integer32"
_SonetFramingStandardOper_Object = MibTableColumn
sonetFramingStandardOper = _SonetFramingStandardOper_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 7),
    _SonetFramingStandardOper_Type()
)
sonetFramingStandardOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFramingStandardOper.setStatus("current")


class _SonetPathWidth_Type(Integer32):
    """Custom type sonetPathWidth based on Integer32"""
    defaultValue = 2

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
        *(("sts1", 1),
          ("sts12c", 4),
          ("sts24c", 5),
          ("sts3c", 2),
          ("sts48c", 6),
          ("sts9c", 3))
    )


_SonetPathWidth_Type.__name__ = "Integer32"
_SonetPathWidth_Object = MibTableColumn
sonetPathWidth = _SonetPathWidth_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 8),
    _SonetPathWidth_Type()
)
sonetPathWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathWidth.setStatus("current")


class _SonetLoopbackConfig_Type(Integer32):
    """Custom type sonetLoopbackConfig based on Integer32"""
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
        *(("sonetDiagLoop", 3),
          ("sonetLineLoop", 2),
          ("sonetNoLoop", 1),
          ("sonetOtherLoop", 4),
          ("sonetPathLoop", 5))
    )


_SonetLoopbackConfig_Type.__name__ = "Integer32"
_SonetLoopbackConfig_Object = MibTableColumn
sonetLoopbackConfig = _SonetLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 9),
    _SonetLoopbackConfig_Type()
)
sonetLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLoopbackConfig.setStatus("current")


class _SonetTxClockSource_Type(Integer32):
    """Custom type sonetTxClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("rxTiming", 1))
    )


_SonetTxClockSource_Type.__name__ = "Integer32"
_SonetTxClockSource_Object = MibTableColumn
sonetTxClockSource = _SonetTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 10),
    _SonetTxClockSource_Type()
)
sonetTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTxClockSource.setStatus("current")


class _SonetRxScrambling_Type(Integer32):
    """Custom type sonetRxScrambling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("descrambling", 1),
          ("noDescrambling", 2))
    )


_SonetRxScrambling_Type.__name__ = "Integer32"
_SonetRxScrambling_Object = MibTableColumn
sonetRxScrambling = _SonetRxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 11),
    _SonetRxScrambling_Type()
)
sonetRxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetRxScrambling.setStatus("current")


class _SonetTxScrambling_Type(Integer32):
    """Custom type sonetTxScrambling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noScrambling", 2),
          ("scrambling", 1))
    )


_SonetTxScrambling_Type.__name__ = "Integer32"
_SonetTxScrambling_Object = MibTableColumn
sonetTxScrambling = _SonetTxScrambling_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 12),
    _SonetTxScrambling_Type()
)
sonetTxScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTxScrambling.setStatus("current")


class _SonetSectionStatus_Type(Integer32):
    """Custom type sonetSectionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonetSectionStatus_Type.__name__ = "Integer32"
_SonetSectionStatus_Object = MibTableColumn
sonetSectionStatus = _SonetSectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 13),
    _SonetSectionStatus_Type()
)
sonetSectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionStatus.setStatus("current")


class _SonetLineStatus_Type(Integer32):
    """Custom type sonetLineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonetLineStatus_Type.__name__ = "Integer32"
_SonetLineStatus_Object = MibTableColumn
sonetLineStatus = _SonetLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 14),
    _SonetLineStatus_Type()
)
sonetLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineStatus.setStatus("current")


class _SonetPathStatus_Type(Integer32):
    """Custom type sonetPathStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 62),
    )


_SonetPathStatus_Type.__name__ = "Integer32"
_SonetPathStatus_Object = MibTableColumn
sonetPathStatus = _SonetPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 15),
    _SonetPathStatus_Type()
)
sonetPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathStatus.setStatus("current")


class _SonetIdleUnassignedCells_Type(Integer32):
    """Custom type sonetIdleUnassignedCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("unassigned", 1))
    )


_SonetIdleUnassignedCells_Type.__name__ = "Integer32"
_SonetIdleUnassignedCells_Object = MibTableColumn
sonetIdleUnassignedCells = _SonetIdleUnassignedCells_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 16),
    _SonetIdleUnassignedCells_Type()
)
sonetIdleUnassignedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetIdleUnassignedCells.setStatus("current")


class _SonetAtmStatus_Type(Integer32):
    """Custom type sonetAtmStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonetAtmStatus_Type.__name__ = "Integer32"
_SonetAtmStatus_Object = MibTableColumn
sonetAtmStatus = _SonetAtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 17),
    _SonetAtmStatus_Type()
)
sonetAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmStatus.setStatus("current")


class _SonetLineAis_Type(Integer32):
    """Custom type sonetLineAis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonetLineAisOff", 1),
          ("sonetLineAisOn", 2))
    )


_SonetLineAis_Type.__name__ = "Integer32"
_SonetLineAis_Object = MibTableColumn
sonetLineAis = _SonetLineAis_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 18),
    _SonetLineAis_Type()
)
sonetLineAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineAis.setStatus("current")


class _SonetLineRdi_Type(Integer32):
    """Custom type sonetLineRdi based on Integer32"""
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
        *(("sonetLineRdiAuto", 3),
          ("sonetLineRdiOff", 1),
          ("sonetLineRdiOn", 2))
    )


_SonetLineRdi_Type.__name__ = "Integer32"
_SonetLineRdi_Object = MibTableColumn
sonetLineRdi = _SonetLineRdi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 19),
    _SonetLineRdi_Type()
)
sonetLineRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineRdi.setStatus("current")


class _SonetPathAis_Type(Integer32):
    """Custom type sonetPathAis based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sonetPathAisOff", 1),
          ("sonetPathAisOn", 2))
    )


_SonetPathAis_Type.__name__ = "Integer32"
_SonetPathAis_Object = MibTableColumn
sonetPathAis = _SonetPathAis_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 20),
    _SonetPathAis_Type()
)
sonetPathAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathAis.setStatus("current")


class _SonetPathRdi_Type(Integer32):
    """Custom type sonetPathRdi based on Integer32"""
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
        *(("sonetPathRdiAuto", 3),
          ("sonetPathRdiOff", 1),
          ("sonetPathRdiOn", 2))
    )


_SonetPathRdi_Type.__name__ = "Integer32"
_SonetPathRdi_Object = MibTableColumn
sonetPathRdi = _SonetPathRdi_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 21),
    _SonetPathRdi_Type()
)
sonetPathRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathRdi.setStatus("current")


class _SonetFebe_Type(Integer32):
    """Custom type sonetFebe based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sonetFebeAuto", 3),
          ("sonetFebeOff", 1))
    )


_SonetFebe_Type.__name__ = "Integer32"
_SonetFebe_Object = MibTableColumn
sonetFebe = _SonetFebe_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 22),
    _SonetFebe_Type()
)
sonetFebe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetFebe.setStatus("current")


class _SonetRxPathSignalLabel_Type(Integer32):
    """Custom type sonetRxPathSignalLabel based on Integer32"""
    defaultValue = 19


_SonetRxPathSignalLabel_Object = MibTableColumn
sonetRxPathSignalLabel = _SonetRxPathSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 23),
    _SonetRxPathSignalLabel_Type()
)
sonetRxPathSignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetRxPathSignalLabel.setStatus("current")


class _SonetTxPathSignalLabel_Type(Integer32):
    """Custom type sonetTxPathSignalLabel based on Integer32"""
    defaultValue = 19


_SonetTxPathSignalLabel_Object = MibTableColumn
sonetTxPathSignalLabel = _SonetTxPathSignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 24),
    _SonetTxPathSignalLabel_Type()
)
sonetTxPathSignalLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetTxPathSignalLabel.setStatus("current")


class _SonetArbitraryPointer_Type(Integer32):
    """Custom type sonetArbitraryPointer based on Integer32"""
    defaultValue = 522


_SonetArbitraryPointer_Object = MibTableColumn
sonetArbitraryPointer = _SonetArbitraryPointer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 25),
    _SonetArbitraryPointer_Type()
)
sonetArbitraryPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetArbitraryPointer.setStatus("current")


class _SonetSectionDiagnostic_Type(Integer32):
    """Custom type sonetSectionDiagnostic based on Integer32"""
    defaultValue = 1


_SonetSectionDiagnostic_Object = MibTableColumn
sonetSectionDiagnostic = _SonetSectionDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 26),
    _SonetSectionDiagnostic_Type()
)
sonetSectionDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetSectionDiagnostic.setStatus("current")


class _SonetLineDiagnostic_Type(Integer32):
    """Custom type sonetLineDiagnostic based on Integer32"""
    defaultValue = 1


_SonetLineDiagnostic_Object = MibTableColumn
sonetLineDiagnostic = _SonetLineDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 27),
    _SonetLineDiagnostic_Type()
)
sonetLineDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineDiagnostic.setStatus("current")


class _SonetPathDiagnostic_Type(Integer32):
    """Custom type sonetPathDiagnostic based on Integer32"""
    defaultValue = 1


_SonetPathDiagnostic_Object = MibTableColumn
sonetPathDiagnostic = _SonetPathDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 28),
    _SonetPathDiagnostic_Type()
)
sonetPathDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathDiagnostic.setStatus("current")


class _SonetPathPointerDiagnostic_Type(Integer32):
    """Custom type sonetPathPointerDiagnostic based on Integer32"""
    defaultValue = 1


_SonetPathPointerDiagnostic_Object = MibTableColumn
sonetPathPointerDiagnostic = _SonetPathPointerDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 29),
    _SonetPathPointerDiagnostic_Type()
)
sonetPathPointerDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetPathPointerDiagnostic.setStatus("current")


class _SonetAtmDiagnostic_Type(Integer32):
    """Custom type sonetAtmDiagnostic based on Integer32"""
    defaultValue = 1


_SonetAtmDiagnostic_Object = MibTableColumn
sonetAtmDiagnostic = _SonetAtmDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 30),
    _SonetAtmDiagnostic_Type()
)
sonetAtmDiagnostic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetAtmDiagnostic.setStatus("current")


class _SonetLineBipThrSeconds_Type(Integer32):
    """Custom type sonetLineBipThrSeconds based on Integer32"""
    defaultValue = 10


_SonetLineBipThrSeconds_Object = MibTableColumn
sonetLineBipThrSeconds = _SonetLineBipThrSeconds_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 31),
    _SonetLineBipThrSeconds_Type()
)
sonetLineBipThrSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineBipThrSeconds.setStatus("current")
_SonetLineBipThrErrors_Type = Integer32
_SonetLineBipThrErrors_Object = MibTableColumn
sonetLineBipThrErrors = _SonetLineBipThrErrors_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 32),
    _SonetLineBipThrErrors_Type()
)
sonetLineBipThrErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineBipThrErrors.setStatus("current")


class _SonetLineBipFailEnable_Type(Integer32):
    """Custom type sonetLineBipFailEnable based on Integer32"""
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


_SonetLineBipFailEnable_Type.__name__ = "Integer32"
_SonetLineBipFailEnable_Object = MibTableColumn
sonetLineBipFailEnable = _SonetLineBipFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 33),
    _SonetLineBipFailEnable_Type()
)
sonetLineBipFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineBipFailEnable.setStatus("current")
_SonetLineSignalDegradeBer_Type = Integer32
_SonetLineSignalDegradeBer_Object = MibTableColumn
sonetLineSignalDegradeBer = _SonetLineSignalDegradeBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 34),
    _SonetLineSignalDegradeBer_Type()
)
sonetLineSignalDegradeBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineSignalDegradeBer.setStatus("current")
_SonetLineSignalFailBer_Type = Integer32
_SonetLineSignalFailBer_Object = MibTableColumn
sonetLineSignalFailBer = _SonetLineSignalFailBer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 35),
    _SonetLineSignalFailBer_Type()
)
sonetLineSignalFailBer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineSignalFailBer.setStatus("current")


class _SonetLineBerErrorModel_Type(Integer32):
    """Custom type sonetLineBerErrorModel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorModelBurst", 2),
          ("errorModelNone", 0),
          ("errorModelRandom", 1))
    )


_SonetLineBerErrorModel_Type.__name__ = "Integer32"
_SonetLineBerErrorModel_Object = MibTableColumn
sonetLineBerErrorModel = _SonetLineBerErrorModel_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 36),
    _SonetLineBerErrorModel_Type()
)
sonetLineBerErrorModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetLineBerErrorModel.setStatus("current")


class _SonetLineBerState_Type(Integer32):
    """Custom type sonetLineBerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("berStateOk", 0),
          ("berStateSigDegrade", 1),
          ("berStateSigFail", 2))
    )


_SonetLineBerState_Type.__name__ = "Integer32"
_SonetLineBerState_Object = MibTableColumn
sonetLineBerState = _SonetLineBerState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 1, 1, 1, 37),
    _SonetLineBerState_Type()
)
sonetLineBerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineBerState.setStatus("current")
_SonetStatsGroup_ObjectIdentity = ObjectIdentity
sonetStatsGroup = _SonetStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2)
)
_SonetSectionTable_Object = MibTable
sonetSectionTable = _SonetSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sonetSectionTable.setStatus("current")
_SonetSectionEntry_Object = MibTableRow
sonetSectionEntry = _SonetSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1)
)
sonetSectionEntry.setIndexNames(
    (0, "Fore-SONET-MIB", "sonetSectionBoard"),
    (0, "Fore-SONET-MIB", "sonetSectionModule"),
    (0, "Fore-SONET-MIB", "sonetSectionPort"),
)
if mibBuilder.loadTexts:
    sonetSectionEntry.setStatus("current")
_SonetSectionBoard_Type = Integer32
_SonetSectionBoard_Object = MibTableColumn
sonetSectionBoard = _SonetSectionBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 1),
    _SonetSectionBoard_Type()
)
sonetSectionBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionBoard.setStatus("current")
_SonetSectionModule_Type = Integer32
_SonetSectionModule_Object = MibTableColumn
sonetSectionModule = _SonetSectionModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 2),
    _SonetSectionModule_Type()
)
sonetSectionModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionModule.setStatus("current")
_SonetSectionPort_Type = Integer32
_SonetSectionPort_Object = MibTableColumn
sonetSectionPort = _SonetSectionPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 3),
    _SonetSectionPort_Type()
)
sonetSectionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionPort.setStatus("current")
_SonetSectionBIPs_Type = Counter32
_SonetSectionBIPs_Object = MibTableColumn
sonetSectionBIPs = _SonetSectionBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 4),
    _SonetSectionBIPs_Type()
)
sonetSectionBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionBIPs.setStatus("current")
_SonetSectionLOSs_Type = Counter32
_SonetSectionLOSs_Object = MibTableColumn
sonetSectionLOSs = _SonetSectionLOSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 5),
    _SonetSectionLOSs_Type()
)
sonetSectionLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionLOSs.setStatus("current")
_SonetSectionLOFs_Type = Counter32
_SonetSectionLOFs_Object = MibTableColumn
sonetSectionLOFs = _SonetSectionLOFs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 1, 1, 6),
    _SonetSectionLOFs_Type()
)
sonetSectionLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetSectionLOFs.setStatus("current")
_SonetLineTable_Object = MibTable
sonetLineTable = _SonetLineTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    sonetLineTable.setStatus("current")
_SonetLineEntry_Object = MibTableRow
sonetLineEntry = _SonetLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1)
)
sonetLineEntry.setIndexNames(
    (0, "Fore-SONET-MIB", "sonetLineBoard"),
    (0, "Fore-SONET-MIB", "sonetLineModule"),
    (0, "Fore-SONET-MIB", "sonetLinePort"),
)
if mibBuilder.loadTexts:
    sonetLineEntry.setStatus("current")
_SonetLineBoard_Type = Integer32
_SonetLineBoard_Object = MibTableColumn
sonetLineBoard = _SonetLineBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 1),
    _SonetLineBoard_Type()
)
sonetLineBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineBoard.setStatus("current")
_SonetLineModule_Type = Integer32
_SonetLineModule_Object = MibTableColumn
sonetLineModule = _SonetLineModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 2),
    _SonetLineModule_Type()
)
sonetLineModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineModule.setStatus("current")
_SonetLinePort_Type = Integer32
_SonetLinePort_Object = MibTableColumn
sonetLinePort = _SonetLinePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 3),
    _SonetLinePort_Type()
)
sonetLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLinePort.setStatus("current")
_SonetLineBIPs_Type = Counter32
_SonetLineBIPs_Object = MibTableColumn
sonetLineBIPs = _SonetLineBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 4),
    _SonetLineBIPs_Type()
)
sonetLineBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineBIPs.setStatus("current")
_SonetLineFEBEs_Type = Counter32
_SonetLineFEBEs_Object = MibTableColumn
sonetLineFEBEs = _SonetLineFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 5),
    _SonetLineFEBEs_Type()
)
sonetLineFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineFEBEs.setStatus("current")
_SonetLineAISs_Type = Counter32
_SonetLineAISs_Object = MibTableColumn
sonetLineAISs = _SonetLineAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 6),
    _SonetLineAISs_Type()
)
sonetLineAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineAISs.setStatus("current")
_SonetLineRDIs_Type = Counter32
_SonetLineRDIs_Object = MibTableColumn
sonetLineRDIs = _SonetLineRDIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 2, 1, 7),
    _SonetLineRDIs_Type()
)
sonetLineRDIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetLineRDIs.setStatus("current")
_SonetPathTable_Object = MibTable
sonetPathTable = _SonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    sonetPathTable.setStatus("current")
_SonetPathEntry_Object = MibTableRow
sonetPathEntry = _SonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1)
)
sonetPathEntry.setIndexNames(
    (0, "Fore-SONET-MIB", "sonetPathBoard"),
    (0, "Fore-SONET-MIB", "sonetPathModule"),
    (0, "Fore-SONET-MIB", "sonetPathPort"),
)
if mibBuilder.loadTexts:
    sonetPathEntry.setStatus("current")
_SonetPathBoard_Type = Integer32
_SonetPathBoard_Object = MibTableColumn
sonetPathBoard = _SonetPathBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 1),
    _SonetPathBoard_Type()
)
sonetPathBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathBoard.setStatus("current")
_SonetPathModule_Type = Integer32
_SonetPathModule_Object = MibTableColumn
sonetPathModule = _SonetPathModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 2),
    _SonetPathModule_Type()
)
sonetPathModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathModule.setStatus("current")
_SonetPathPort_Type = Integer32
_SonetPathPort_Object = MibTableColumn
sonetPathPort = _SonetPathPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 3),
    _SonetPathPort_Type()
)
sonetPathPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathPort.setStatus("current")
_SonetPathBIPs_Type = Counter32
_SonetPathBIPs_Object = MibTableColumn
sonetPathBIPs = _SonetPathBIPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 4),
    _SonetPathBIPs_Type()
)
sonetPathBIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathBIPs.setStatus("current")
_SonetPathFEBEs_Type = Counter32
_SonetPathFEBEs_Object = MibTableColumn
sonetPathFEBEs = _SonetPathFEBEs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 5),
    _SonetPathFEBEs_Type()
)
sonetPathFEBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathFEBEs.setStatus("current")
_SonetPathLOPs_Type = Counter32
_SonetPathLOPs_Object = MibTableColumn
sonetPathLOPs = _SonetPathLOPs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 6),
    _SonetPathLOPs_Type()
)
sonetPathLOPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathLOPs.setStatus("current")
_SonetPathAISs_Type = Counter32
_SonetPathAISs_Object = MibTableColumn
sonetPathAISs = _SonetPathAISs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 7),
    _SonetPathAISs_Type()
)
sonetPathAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathAISs.setStatus("current")
_SonetPathRDIs_Type = Counter32
_SonetPathRDIs_Object = MibTableColumn
sonetPathRDIs = _SonetPathRDIs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 8),
    _SonetPathRDIs_Type()
)
sonetPathRDIs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathRDIs.setStatus("current")
_SonetPathUNEQs_Type = Counter32
_SonetPathUNEQs_Object = MibTableColumn
sonetPathUNEQs = _SonetPathUNEQs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 9),
    _SonetPathUNEQs_Type()
)
sonetPathUNEQs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathUNEQs.setStatus("current")
_SonetPathPLMs_Type = Counter32
_SonetPathPLMs_Object = MibTableColumn
sonetPathPLMs = _SonetPathPLMs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 3, 1, 10),
    _SonetPathPLMs_Type()
)
sonetPathPLMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetPathPLMs.setStatus("current")
_SonetAtmTable_Object = MibTable
sonetAtmTable = _SonetAtmTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    sonetAtmTable.setStatus("current")
_SonetAtmEntry_Object = MibTableRow
sonetAtmEntry = _SonetAtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1)
)
sonetAtmEntry.setIndexNames(
    (0, "Fore-SONET-MIB", "sonetAtmBoard"),
    (0, "Fore-SONET-MIB", "sonetAtmModule"),
    (0, "Fore-SONET-MIB", "sonetAtmPort"),
)
if mibBuilder.loadTexts:
    sonetAtmEntry.setStatus("current")
_SonetAtmBoard_Type = Integer32
_SonetAtmBoard_Object = MibTableColumn
sonetAtmBoard = _SonetAtmBoard_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 1),
    _SonetAtmBoard_Type()
)
sonetAtmBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmBoard.setStatus("current")
_SonetAtmModule_Type = Integer32
_SonetAtmModule_Object = MibTableColumn
sonetAtmModule = _SonetAtmModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 2),
    _SonetAtmModule_Type()
)
sonetAtmModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmModule.setStatus("current")
_SonetAtmPort_Type = Integer32
_SonetAtmPort_Object = MibTableColumn
sonetAtmPort = _SonetAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 3),
    _SonetAtmPort_Type()
)
sonetAtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmPort.setStatus("current")
_SonetAtmCorrectableHCSs_Type = Counter32
_SonetAtmCorrectableHCSs_Object = MibTableColumn
sonetAtmCorrectableHCSs = _SonetAtmCorrectableHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 4),
    _SonetAtmCorrectableHCSs_Type()
)
sonetAtmCorrectableHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmCorrectableHCSs.setStatus("current")
_SonetAtmUncorrectableHCSs_Type = Counter32
_SonetAtmUncorrectableHCSs_Object = MibTableColumn
sonetAtmUncorrectableHCSs = _SonetAtmUncorrectableHCSs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 5),
    _SonetAtmUncorrectableHCSs_Type()
)
sonetAtmUncorrectableHCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmUncorrectableHCSs.setStatus("current")
_SonetAtmLCDs_Type = Counter32
_SonetAtmLCDs_Object = MibTableColumn
sonetAtmLCDs = _SonetAtmLCDs_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 4, 2, 4, 1, 6),
    _SonetAtmLCDs_Type()
)
sonetAtmLCDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetAtmLCDs.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-SONET-MIB",
    **{"foreSonetModule": foreSonetModule,
       "sonetConfGroup": sonetConfGroup,
       "sonetConfTable": sonetConfTable,
       "sonetConfEntry": sonetConfEntry,
       "sonetConfBoard": sonetConfBoard,
       "sonetConfModule": sonetConfModule,
       "sonetConfPort": sonetConfPort,
       "sonetLineType": sonetLineType,
       "sonetLineCoding": sonetLineCoding,
       "sonetFramingStandardDefault": sonetFramingStandardDefault,
       "sonetFramingStandardOper": sonetFramingStandardOper,
       "sonetPathWidth": sonetPathWidth,
       "sonetLoopbackConfig": sonetLoopbackConfig,
       "sonetTxClockSource": sonetTxClockSource,
       "sonetRxScrambling": sonetRxScrambling,
       "sonetTxScrambling": sonetTxScrambling,
       "sonetSectionStatus": sonetSectionStatus,
       "sonetLineStatus": sonetLineStatus,
       "sonetPathStatus": sonetPathStatus,
       "sonetIdleUnassignedCells": sonetIdleUnassignedCells,
       "sonetAtmStatus": sonetAtmStatus,
       "sonetLineAis": sonetLineAis,
       "sonetLineRdi": sonetLineRdi,
       "sonetPathAis": sonetPathAis,
       "sonetPathRdi": sonetPathRdi,
       "sonetFebe": sonetFebe,
       "sonetRxPathSignalLabel": sonetRxPathSignalLabel,
       "sonetTxPathSignalLabel": sonetTxPathSignalLabel,
       "sonetArbitraryPointer": sonetArbitraryPointer,
       "sonetSectionDiagnostic": sonetSectionDiagnostic,
       "sonetLineDiagnostic": sonetLineDiagnostic,
       "sonetPathDiagnostic": sonetPathDiagnostic,
       "sonetPathPointerDiagnostic": sonetPathPointerDiagnostic,
       "sonetAtmDiagnostic": sonetAtmDiagnostic,
       "sonetLineBipThrSeconds": sonetLineBipThrSeconds,
       "sonetLineBipThrErrors": sonetLineBipThrErrors,
       "sonetLineBipFailEnable": sonetLineBipFailEnable,
       "sonetLineSignalDegradeBer": sonetLineSignalDegradeBer,
       "sonetLineSignalFailBer": sonetLineSignalFailBer,
       "sonetLineBerErrorModel": sonetLineBerErrorModel,
       "sonetLineBerState": sonetLineBerState,
       "sonetStatsGroup": sonetStatsGroup,
       "sonetSectionTable": sonetSectionTable,
       "sonetSectionEntry": sonetSectionEntry,
       "sonetSectionBoard": sonetSectionBoard,
       "sonetSectionModule": sonetSectionModule,
       "sonetSectionPort": sonetSectionPort,
       "sonetSectionBIPs": sonetSectionBIPs,
       "sonetSectionLOSs": sonetSectionLOSs,
       "sonetSectionLOFs": sonetSectionLOFs,
       "sonetLineTable": sonetLineTable,
       "sonetLineEntry": sonetLineEntry,
       "sonetLineBoard": sonetLineBoard,
       "sonetLineModule": sonetLineModule,
       "sonetLinePort": sonetLinePort,
       "sonetLineBIPs": sonetLineBIPs,
       "sonetLineFEBEs": sonetLineFEBEs,
       "sonetLineAISs": sonetLineAISs,
       "sonetLineRDIs": sonetLineRDIs,
       "sonetPathTable": sonetPathTable,
       "sonetPathEntry": sonetPathEntry,
       "sonetPathBoard": sonetPathBoard,
       "sonetPathModule": sonetPathModule,
       "sonetPathPort": sonetPathPort,
       "sonetPathBIPs": sonetPathBIPs,
       "sonetPathFEBEs": sonetPathFEBEs,
       "sonetPathLOPs": sonetPathLOPs,
       "sonetPathAISs": sonetPathAISs,
       "sonetPathRDIs": sonetPathRDIs,
       "sonetPathUNEQs": sonetPathUNEQs,
       "sonetPathPLMs": sonetPathPLMs,
       "sonetAtmTable": sonetAtmTable,
       "sonetAtmEntry": sonetAtmEntry,
       "sonetAtmBoard": sonetAtmBoard,
       "sonetAtmModule": sonetAtmModule,
       "sonetAtmPort": sonetAtmPort,
       "sonetAtmCorrectableHCSs": sonetAtmCorrectableHCSs,
       "sonetAtmUncorrectableHCSs": sonetAtmUncorrectableHCSs,
       "sonetAtmLCDs": sonetAtmLCDs}
)
