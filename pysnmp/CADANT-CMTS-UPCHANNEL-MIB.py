# SNMP MIB module (CADANT-CMTS-UPCHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-UPCHANNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:25 2024
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

(cadSpectrum,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadSpectrum")

(CardId,) = mibBuilder.importSymbols(
    "CADANT-TC",
    "CardId")

(DocsisUpstreamType,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsisUpstreamType")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cadUpchannelMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3)
)
cadUpchannelMib.setRevisions(
        ("2014-04-25 00:00",
         "2014-02-24 00:00",
         "2014-02-07 00:00",
         "2013-10-22 00:00",
         "2013-09-26 00:00",
         "2013-04-25 00:00",
         "2013-01-15 00:00",
         "2012-11-29 00:00",
         "2012-09-18 00:00",
         "2012-05-22 00:00",
         "2008-06-26 00:00",
         "2008-04-08 00:00",
         "2008-03-31 00:00",
         "2007-04-04 00:00",
         "2007-02-05 00:00",
         "2007-01-16 00:00",
         "2006-09-11 00:00",
         "2006-03-02 00:00",
         "2005-11-29 00:00",
         "2005-11-10 00:00",
         "2005-10-04 00:00",
         "2005-08-19 00:00",
         "2005-02-24 00:00",
         "2004-06-11 00:00",
         "2004-03-04 00:00",
         "2004-02-18 00:00",
         "2004-02-15 00:00",
         "2004-02-06 00:00",
         "2003-09-26 00:00",
         "2003-07-31 00:00",
         "2003-06-23 00:00",
         "2003-05-21 00:00",
         "2003-03-05 00:00",
         "2003-02-18 00:00",
         "2002-12-03 00:00",
         "2002-12-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadIfCmtsModulationTable_Object = MibTable
cadIfCmtsModulationTable = _CadIfCmtsModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    cadIfCmtsModulationTable.setStatus("current")
_CadIfCmtsModulationEntry_Object = MibTableRow
cadIfCmtsModulationEntry = _CadIfCmtsModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1)
)
cadIfCmtsModulationEntry.setIndexNames(
    (0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModIndex"),
    (0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModIntervalUsageCode"),
)
if mibBuilder.loadTexts:
    cadIfCmtsModulationEntry.setStatus("current")


class _CadIfCmtsModIndex_Type(Integer32):
    """Custom type cadIfCmtsModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CadIfCmtsModIndex_Type.__name__ = "Integer32"
_CadIfCmtsModIndex_Object = MibTableColumn
cadIfCmtsModIndex = _CadIfCmtsModIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 1),
    _CadIfCmtsModIndex_Type()
)
cadIfCmtsModIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsModIndex.setStatus("current")


class _CadIfCmtsModIntervalUsageCode_Type(Integer32):
    """Custom type cadIfCmtsModIntervalUsageCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("advPhyLongData", 10),
          ("advPhyShortData", 9),
          ("initialRanging", 3),
          ("longData", 6),
          ("periodicRanging", 4),
          ("request", 1),
          ("requestData", 2),
          ("shortData", 5),
          ("ugs", 11))
    )


_CadIfCmtsModIntervalUsageCode_Type.__name__ = "Integer32"
_CadIfCmtsModIntervalUsageCode_Object = MibTableColumn
cadIfCmtsModIntervalUsageCode = _CadIfCmtsModIntervalUsageCode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 2),
    _CadIfCmtsModIntervalUsageCode_Type()
)
cadIfCmtsModIntervalUsageCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfCmtsModIntervalUsageCode.setStatus("current")
_CadIfCmtsModControl_Type = RowStatus
_CadIfCmtsModControl_Object = MibTableColumn
cadIfCmtsModControl = _CadIfCmtsModControl_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 3),
    _CadIfCmtsModControl_Type()
)
cadIfCmtsModControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModControl.setStatus("current")


class _CadIfCmtsModType_Type(Integer32):
    """Custom type cadIfCmtsModType based on Integer32"""
    defaultValue = 2

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
        *(("other", 1),
          ("qam128", 7),
          ("qam16", 3),
          ("qam32", 5),
          ("qam64", 6),
          ("qam8", 4),
          ("qpsk", 2))
    )


_CadIfCmtsModType_Type.__name__ = "Integer32"
_CadIfCmtsModType_Object = MibTableColumn
cadIfCmtsModType = _CadIfCmtsModType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 4),
    _CadIfCmtsModType_Type()
)
cadIfCmtsModType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModType.setStatus("current")


class _CadIfCmtsModPreambleLen_Type(Integer32):
    """Custom type cadIfCmtsModPreambleLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_CadIfCmtsModPreambleLen_Type.__name__ = "Integer32"
_CadIfCmtsModPreambleLen_Object = MibTableColumn
cadIfCmtsModPreambleLen = _CadIfCmtsModPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 5),
    _CadIfCmtsModPreambleLen_Type()
)
cadIfCmtsModPreambleLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModPreambleLen.setStatus("current")


class _CadIfCmtsModDifferentialEncoding_Type(TruthValue):
    """Custom type cadIfCmtsModDifferentialEncoding based on TruthValue"""


_CadIfCmtsModDifferentialEncoding_Object = MibTableColumn
cadIfCmtsModDifferentialEncoding = _CadIfCmtsModDifferentialEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 6),
    _CadIfCmtsModDifferentialEncoding_Type()
)
cadIfCmtsModDifferentialEncoding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModDifferentialEncoding.setStatus("current")


class _CadIfCmtsModFECErrorCorrection_Type(Integer32):
    """Custom type cadIfCmtsModFECErrorCorrection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CadIfCmtsModFECErrorCorrection_Type.__name__ = "Integer32"
_CadIfCmtsModFECErrorCorrection_Object = MibTableColumn
cadIfCmtsModFECErrorCorrection = _CadIfCmtsModFECErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 7),
    _CadIfCmtsModFECErrorCorrection_Type()
)
cadIfCmtsModFECErrorCorrection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModFECErrorCorrection.setStatus("current")


class _CadIfCmtsModFECCodewordLength_Type(Integer32):
    """Custom type cadIfCmtsModFECCodewordLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 253),
    )


_CadIfCmtsModFECCodewordLength_Type.__name__ = "Integer32"
_CadIfCmtsModFECCodewordLength_Object = MibTableColumn
cadIfCmtsModFECCodewordLength = _CadIfCmtsModFECCodewordLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 8),
    _CadIfCmtsModFECCodewordLength_Type()
)
cadIfCmtsModFECCodewordLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModFECCodewordLength.setStatus("current")


class _CadIfCmtsModScramblerSeed_Type(Integer32):
    """Custom type cadIfCmtsModScramblerSeed based on Integer32"""
    defaultValue = 338

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CadIfCmtsModScramblerSeed_Type.__name__ = "Integer32"
_CadIfCmtsModScramblerSeed_Object = MibTableColumn
cadIfCmtsModScramblerSeed = _CadIfCmtsModScramblerSeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 9),
    _CadIfCmtsModScramblerSeed_Type()
)
cadIfCmtsModScramblerSeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModScramblerSeed.setStatus("current")


class _CadIfCmtsModMaxBurstSize_Type(Integer32):
    """Custom type cadIfCmtsModMaxBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadIfCmtsModMaxBurstSize_Type.__name__ = "Integer32"
_CadIfCmtsModMaxBurstSize_Object = MibTableColumn
cadIfCmtsModMaxBurstSize = _CadIfCmtsModMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 10),
    _CadIfCmtsModMaxBurstSize_Type()
)
cadIfCmtsModMaxBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModMaxBurstSize.setStatus("current")


class _CadIfCmtsModGuardTimeSize_Type(Unsigned32):
    """Custom type cadIfCmtsModGuardTimeSize based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 96),
    )


_CadIfCmtsModGuardTimeSize_Type.__name__ = "Unsigned32"
_CadIfCmtsModGuardTimeSize_Object = MibTableColumn
cadIfCmtsModGuardTimeSize = _CadIfCmtsModGuardTimeSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 11),
    _CadIfCmtsModGuardTimeSize_Type()
)
cadIfCmtsModGuardTimeSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModGuardTimeSize.setStatus("current")


class _CadIfCmtsModLastCodewordShortened_Type(TruthValue):
    """Custom type cadIfCmtsModLastCodewordShortened based on TruthValue"""


_CadIfCmtsModLastCodewordShortened_Object = MibTableColumn
cadIfCmtsModLastCodewordShortened = _CadIfCmtsModLastCodewordShortened_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 12),
    _CadIfCmtsModLastCodewordShortened_Type()
)
cadIfCmtsModLastCodewordShortened.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModLastCodewordShortened.setStatus("current")


class _CadIfCmtsModScrambler_Type(TruthValue):
    """Custom type cadIfCmtsModScrambler based on TruthValue"""


_CadIfCmtsModScrambler_Object = MibTableColumn
cadIfCmtsModScrambler = _CadIfCmtsModScrambler_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 13),
    _CadIfCmtsModScrambler_Type()
)
cadIfCmtsModScrambler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModScrambler.setStatus("current")


class _CadIfCmtsModPreambleValueOffset_Type(Integer32):
    """Custom type cadIfCmtsModPreambleValueOffset based on Integer32"""
    defaultValue = 0


_CadIfCmtsModPreambleValueOffset_Object = MibTableColumn
cadIfCmtsModPreambleValueOffset = _CadIfCmtsModPreambleValueOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 14),
    _CadIfCmtsModPreambleValueOffset_Type()
)
cadIfCmtsModPreambleValueOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsModPreambleValueOffset.setStatus("current")


class _CadIfCmtsModBroadcomUwLength_Type(Integer32):
    """Custom type cadIfCmtsModBroadcomUwLength based on Integer32"""
    defaultValue = 2


_CadIfCmtsModBroadcomUwLength_Object = MibTableColumn
cadIfCmtsModBroadcomUwLength = _CadIfCmtsModBroadcomUwLength_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 15),
    _CadIfCmtsModBroadcomUwLength_Type()
)
cadIfCmtsModBroadcomUwLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsModBroadcomUwLength.setStatus("current")


class _CadIfCmtsModBroadcomUwPattern_Type(OctetString):
    """Custom type cadIfCmtsModBroadcomUwPattern based on OctetString"""
    defaultHexValue = "0d0d00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CadIfCmtsModBroadcomUwPattern_Type.__name__ = "OctetString"
_CadIfCmtsModBroadcomUwPattern_Object = MibTableColumn
cadIfCmtsModBroadcomUwPattern = _CadIfCmtsModBroadcomUwPattern_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 16),
    _CadIfCmtsModBroadcomUwPattern_Type()
)
cadIfCmtsModBroadcomUwPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsModBroadcomUwPattern.setStatus("current")


class _CadIfCmtsModBroadcomUwDetectionWindow_Type(OctetString):
    """Custom type cadIfCmtsModBroadcomUwDetectionWindow based on OctetString"""
    defaultHexValue = "04"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CadIfCmtsModBroadcomUwDetectionWindow_Type.__name__ = "OctetString"
_CadIfCmtsModBroadcomUwDetectionWindow_Object = MibTableColumn
cadIfCmtsModBroadcomUwDetectionWindow = _CadIfCmtsModBroadcomUwDetectionWindow_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 17),
    _CadIfCmtsModBroadcomUwDetectionWindow_Type()
)
cadIfCmtsModBroadcomUwDetectionWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsModBroadcomUwDetectionWindow.setStatus("current")


class _CadIfCmtsModBroadcomUwMismatchThreshold_Type(OctetString):
    """Custom type cadIfCmtsModBroadcomUwMismatchThreshold based on OctetString"""
    defaultHexValue = "01"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CadIfCmtsModBroadcomUwMismatchThreshold_Type.__name__ = "OctetString"
_CadIfCmtsModBroadcomUwMismatchThreshold_Object = MibTableColumn
cadIfCmtsModBroadcomUwMismatchThreshold = _CadIfCmtsModBroadcomUwMismatchThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 18),
    _CadIfCmtsModBroadcomUwMismatchThreshold_Type()
)
cadIfCmtsModBroadcomUwMismatchThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfCmtsModBroadcomUwMismatchThreshold.setStatus("current")


class _CadIfCmtsModByteInterleaverDepth_Type(Unsigned32):
    """Custom type cadIfCmtsModByteInterleaverDepth based on Unsigned32"""
    defaultValue = 1


_CadIfCmtsModByteInterleaverDepth_Object = MibTableColumn
cadIfCmtsModByteInterleaverDepth = _CadIfCmtsModByteInterleaverDepth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 19),
    _CadIfCmtsModByteInterleaverDepth_Type()
)
cadIfCmtsModByteInterleaverDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModByteInterleaverDepth.setStatus("current")


class _CadIfCmtsModByteInterleaverBlockSize_Type(Unsigned32):
    """Custom type cadIfCmtsModByteInterleaverBlockSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(36, 2048),
    )


_CadIfCmtsModByteInterleaverBlockSize_Type.__name__ = "Unsigned32"
_CadIfCmtsModByteInterleaverBlockSize_Object = MibTableColumn
cadIfCmtsModByteInterleaverBlockSize = _CadIfCmtsModByteInterleaverBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 20),
    _CadIfCmtsModByteInterleaverBlockSize_Type()
)
cadIfCmtsModByteInterleaverBlockSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModByteInterleaverBlockSize.setStatus("current")


class _CadIfCmtsModPreambleType_Type(Integer32):
    """Custom type cadIfCmtsModPreambleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qpsk0", 1),
          ("qpsk1", 2))
    )


_CadIfCmtsModPreambleType_Type.__name__ = "Integer32"
_CadIfCmtsModPreambleType_Object = MibTableColumn
cadIfCmtsModPreambleType = _CadIfCmtsModPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 21),
    _CadIfCmtsModPreambleType_Type()
)
cadIfCmtsModPreambleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModPreambleType.setStatus("current")


class _CadIfCmtsModTcmErrorCorrectionOn_Type(TruthValue):
    """Custom type cadIfCmtsModTcmErrorCorrectionOn based on TruthValue"""


_CadIfCmtsModTcmErrorCorrectionOn_Object = MibTableColumn
cadIfCmtsModTcmErrorCorrectionOn = _CadIfCmtsModTcmErrorCorrectionOn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 22),
    _CadIfCmtsModTcmErrorCorrectionOn_Type()
)
cadIfCmtsModTcmErrorCorrectionOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModTcmErrorCorrectionOn.setStatus("current")


class _CadIfCmtsModScdmaInterleaverStepSize_Type(Unsigned32):
    """Custom type cadIfCmtsModScdmaInterleaverStepSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_CadIfCmtsModScdmaInterleaverStepSize_Type.__name__ = "Unsigned32"
_CadIfCmtsModScdmaInterleaverStepSize_Object = MibTableColumn
cadIfCmtsModScdmaInterleaverStepSize = _CadIfCmtsModScdmaInterleaverStepSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 23),
    _CadIfCmtsModScdmaInterleaverStepSize_Type()
)
cadIfCmtsModScdmaInterleaverStepSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModScdmaInterleaverStepSize.setStatus("current")


class _CadIfCmtsModScdmaSpreaderEnable_Type(TruthValue):
    """Custom type cadIfCmtsModScdmaSpreaderEnable based on TruthValue"""


_CadIfCmtsModScdmaSpreaderEnable_Object = MibTableColumn
cadIfCmtsModScdmaSpreaderEnable = _CadIfCmtsModScdmaSpreaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 24),
    _CadIfCmtsModScdmaSpreaderEnable_Type()
)
cadIfCmtsModScdmaSpreaderEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModScdmaSpreaderEnable.setStatus("current")


class _CadIfCmtsModScdmaSubframeCodes_Type(Unsigned32):
    """Custom type cadIfCmtsModScdmaSubframeCodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 128),
    )


_CadIfCmtsModScdmaSubframeCodes_Type.__name__ = "Unsigned32"
_CadIfCmtsModScdmaSubframeCodes_Object = MibTableColumn
cadIfCmtsModScdmaSubframeCodes = _CadIfCmtsModScdmaSubframeCodes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 25),
    _CadIfCmtsModScdmaSubframeCodes_Type()
)
cadIfCmtsModScdmaSubframeCodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModScdmaSubframeCodes.setStatus("current")


class _CadIfCmtsModChannelType_Type(DocsisUpstreamType):
    """Custom type cadIfCmtsModChannelType based on DocsisUpstreamType"""


_CadIfCmtsModChannelType_Object = MibTableColumn
cadIfCmtsModChannelType = _CadIfCmtsModChannelType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 1, 1, 26),
    _CadIfCmtsModChannelType_Type()
)
cadIfCmtsModChannelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadIfCmtsModChannelType.setStatus("current")
_CadIfUpstreamChannelTable_Object = MibTable
cadIfUpstreamChannelTable = _CadIfUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2)
)
if mibBuilder.loadTexts:
    cadIfUpstreamChannelTable.setStatus("current")
_CadIfUpstreamChannelEntry_Object = MibTableRow
cadIfUpstreamChannelEntry = _CadIfUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1)
)
cadIfUpstreamChannelEntry.setIndexNames(
    (0, "CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIfIndex"),
)
if mibBuilder.loadTexts:
    cadIfUpstreamChannelEntry.setStatus("current")
_CadIfUpChannelCardNumber_Type = CardId
_CadIfUpChannelCardNumber_Object = MibTableColumn
cadIfUpChannelCardNumber = _CadIfUpChannelCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 1),
    _CadIfUpChannelCardNumber_Type()
)
cadIfUpChannelCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfUpChannelCardNumber.setStatus("current")


class _CadIfUpChannelId_Type(Integer32):
    """Custom type cadIfUpChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CadIfUpChannelId_Type.__name__ = "Integer32"
_CadIfUpChannelId_Object = MibTableColumn
cadIfUpChannelId = _CadIfUpChannelId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 2),
    _CadIfUpChannelId_Type()
)
cadIfUpChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadIfUpChannelId.setStatus("current")


class _CadIfUpChannelFrequency_Type(Integer32):
    """Custom type cadIfUpChannelFrequency based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 85000000),
    )


_CadIfUpChannelFrequency_Type.__name__ = "Integer32"
_CadIfUpChannelFrequency_Object = MibTableColumn
cadIfUpChannelFrequency = _CadIfUpChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 4),
    _CadIfUpChannelFrequency_Type()
)
cadIfUpChannelFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelFrequency.setUnits("hertz")


class _CadIfUpChannelWidth_Type(Integer32):
    """Custom type cadIfUpChannelWidth based on Integer32"""
    defaultValue = 3200000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(200000, 200000),
        ValueRangeConstraint(400000, 400000),
        ValueRangeConstraint(800000, 800000),
        ValueRangeConstraint(1600000, 1600000),
        ValueRangeConstraint(3200000, 3200000),
        ValueRangeConstraint(6400000, 6400000),
    )


_CadIfUpChannelWidth_Type.__name__ = "Integer32"
_CadIfUpChannelWidth_Object = MibTableColumn
cadIfUpChannelWidth = _CadIfUpChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 5),
    _CadIfUpChannelWidth_Type()
)
cadIfUpChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelWidth.setUnits("hertz")


class _CadIfUpChannelModulationProfile_Type(Integer32):
    """Custom type cadIfUpChannelModulationProfile based on Integer32"""
    defaultValue = 0


_CadIfUpChannelModulationProfile_Object = MibTableColumn
cadIfUpChannelModulationProfile = _CadIfUpChannelModulationProfile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 6),
    _CadIfUpChannelModulationProfile_Type()
)
cadIfUpChannelModulationProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelModulationProfile.setStatus("current")


class _CadIfUpChannelPowerDesired_Type(Integer32):
    """Custom type cadIfUpChannelPowerDesired based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-16, 29),
    )


_CadIfUpChannelPowerDesired_Type.__name__ = "Integer32"
_CadIfUpChannelPowerDesired_Object = MibTableColumn
cadIfUpChannelPowerDesired = _CadIfUpChannelPowerDesired_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 7),
    _CadIfUpChannelPowerDesired_Type()
)
cadIfUpChannelPowerDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPowerDesired.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPowerDesired.setUnits("dBmV")


class _CadIfUpChannelSlotSize_Type(Unsigned32):
    """Custom type cadIfUpChannelSlotSize based on Unsigned32"""
    defaultValue = 4


_CadIfUpChannelSlotSize_Object = MibTableColumn
cadIfUpChannelSlotSize = _CadIfUpChannelSlotSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 8),
    _CadIfUpChannelSlotSize_Type()
)
cadIfUpChannelSlotSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelSlotSize.setStatus("current")


class _CadIfUpChannelRangingBackoffStart_Type(Integer32):
    """Custom type cadIfUpChannelRangingBackoffStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CadIfUpChannelRangingBackoffStart_Type.__name__ = "Integer32"
_CadIfUpChannelRangingBackoffStart_Object = MibTableColumn
cadIfUpChannelRangingBackoffStart = _CadIfUpChannelRangingBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 9),
    _CadIfUpChannelRangingBackoffStart_Type()
)
cadIfUpChannelRangingBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelRangingBackoffStart.setStatus("current")


class _CadIfUpChannelRangingBackoffEnd_Type(Integer32):
    """Custom type cadIfUpChannelRangingBackoffEnd based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CadIfUpChannelRangingBackoffEnd_Type.__name__ = "Integer32"
_CadIfUpChannelRangingBackoffEnd_Object = MibTableColumn
cadIfUpChannelRangingBackoffEnd = _CadIfUpChannelRangingBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 10),
    _CadIfUpChannelRangingBackoffEnd_Type()
)
cadIfUpChannelRangingBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelRangingBackoffEnd.setStatus("current")


class _CadIfUpChannelTxBackoffStart_Type(Integer32):
    """Custom type cadIfUpChannelTxBackoffStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CadIfUpChannelTxBackoffStart_Type.__name__ = "Integer32"
_CadIfUpChannelTxBackoffStart_Object = MibTableColumn
cadIfUpChannelTxBackoffStart = _CadIfUpChannelTxBackoffStart_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 11),
    _CadIfUpChannelTxBackoffStart_Type()
)
cadIfUpChannelTxBackoffStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelTxBackoffStart.setStatus("current")


class _CadIfUpChannelTxBackoffEnd_Type(Integer32):
    """Custom type cadIfUpChannelTxBackoffEnd based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CadIfUpChannelTxBackoffEnd_Type.__name__ = "Integer32"
_CadIfUpChannelTxBackoffEnd_Object = MibTableColumn
cadIfUpChannelTxBackoffEnd = _CadIfUpChannelTxBackoffEnd_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 12),
    _CadIfUpChannelTxBackoffEnd_Type()
)
cadIfUpChannelTxBackoffEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelTxBackoffEnd.setStatus("current")


class _CadIfUpChannelMapSize_Type(Integer32):
    """Custom type cadIfUpChannelMapSize based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_CadIfUpChannelMapSize_Type.__name__ = "Integer32"
_CadIfUpChannelMapSize_Object = MibTableColumn
cadIfUpChannelMapSize = _CadIfUpChannelMapSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 13),
    _CadIfUpChannelMapSize_Type()
)
cadIfUpChannelMapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelMapSize.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelMapSize.setUnits("800microsecondTicks")


class _CadIfUpChannelMaxPowerAdjust_Type(Integer32):
    """Custom type cadIfUpChannelMaxPowerAdjust based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_CadIfUpChannelMaxPowerAdjust_Type.__name__ = "Integer32"
_CadIfUpChannelMaxPowerAdjust_Object = MibTableColumn
cadIfUpChannelMaxPowerAdjust = _CadIfUpChannelMaxPowerAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 17),
    _CadIfUpChannelMaxPowerAdjust_Type()
)
cadIfUpChannelMaxPowerAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelMaxPowerAdjust.setStatus("current")


class _CadIfUpChannelThresholdPowerOffset_Type(Integer32):
    """Custom type cadIfUpChannelThresholdPowerOffset based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 48),
    )


_CadIfUpChannelThresholdPowerOffset_Type.__name__ = "Integer32"
_CadIfUpChannelThresholdPowerOffset_Object = MibTableColumn
cadIfUpChannelThresholdPowerOffset = _CadIfUpChannelThresholdPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 18),
    _CadIfUpChannelThresholdPowerOffset_Type()
)
cadIfUpChannelThresholdPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelThresholdPowerOffset.setStatus("current")


class _CadIfUpChannelZeroPowerAdjust_Type(TruthValue):
    """Custom type cadIfUpChannelZeroPowerAdjust based on TruthValue"""


_CadIfUpChannelZeroPowerAdjust_Object = MibTableColumn
cadIfUpChannelZeroPowerAdjust = _CadIfUpChannelZeroPowerAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 19),
    _CadIfUpChannelZeroPowerAdjust_Type()
)
cadIfUpChannelZeroPowerAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelZeroPowerAdjust.setStatus("current")


class _CadIfUpChannelZeroFreqAdjust_Type(TruthValue):
    """Custom type cadIfUpChannelZeroFreqAdjust based on TruthValue"""


_CadIfUpChannelZeroFreqAdjust_Object = MibTableColumn
cadIfUpChannelZeroFreqAdjust = _CadIfUpChannelZeroFreqAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 20),
    _CadIfUpChannelZeroFreqAdjust_Type()
)
cadIfUpChannelZeroFreqAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelZeroFreqAdjust.setStatus("current")


class _CadIfUpChannelZeroTimingAdjust_Type(TruthValue):
    """Custom type cadIfUpChannelZeroTimingAdjust based on TruthValue"""


_CadIfUpChannelZeroTimingAdjust_Object = MibTableColumn
cadIfUpChannelZeroTimingAdjust = _CadIfUpChannelZeroTimingAdjust_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 21),
    _CadIfUpChannelZeroTimingAdjust_Type()
)
cadIfUpChannelZeroTimingAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelZeroTimingAdjust.setStatus("current")


class _CadIfUpChannelPreEqEnable_Type(TruthValue):
    """Custom type cadIfUpChannelPreEqEnable based on TruthValue"""


_CadIfUpChannelPreEqEnable_Object = MibTableColumn
cadIfUpChannelPreEqEnable = _CadIfUpChannelPreEqEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 22),
    _CadIfUpChannelPreEqEnable_Type()
)
cadIfUpChannelPreEqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPreEqEnable.setStatus("current")


class _CadIfUpChannelPCNormAllowedUsage_Type(Integer32):
    """Custom type cadIfUpChannelPCNormAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfUpChannelPCNormAllowedUsage_Type.__name__ = "Integer32"
_CadIfUpChannelPCNormAllowedUsage_Object = MibTableColumn
cadIfUpChannelPCNormAllowedUsage = _CadIfUpChannelPCNormAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 52),
    _CadIfUpChannelPCNormAllowedUsage_Type()
)
cadIfUpChannelPCNormAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCNormAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPCNormAllowedUsage.setUnits("percent")


class _CadIfUpChannelPCNormResUsage_Type(Integer32):
    """Custom type cadIfUpChannelPCNormResUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfUpChannelPCNormResUsage_Type.__name__ = "Integer32"
_CadIfUpChannelPCNormResUsage_Object = MibTableColumn
cadIfUpChannelPCNormResUsage = _CadIfUpChannelPCNormResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 53),
    _CadIfUpChannelPCNormResUsage_Type()
)
cadIfUpChannelPCNormResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCNormResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPCNormResUsage.setUnits("percent")


class _CadIfUpChannelPCEmerAllowedUsage_Type(Integer32):
    """Custom type cadIfUpChannelPCEmerAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfUpChannelPCEmerAllowedUsage_Type.__name__ = "Integer32"
_CadIfUpChannelPCEmerAllowedUsage_Object = MibTableColumn
cadIfUpChannelPCEmerAllowedUsage = _CadIfUpChannelPCEmerAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 54),
    _CadIfUpChannelPCEmerAllowedUsage_Type()
)
cadIfUpChannelPCEmerAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCEmerAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPCEmerAllowedUsage.setUnits("percent")


class _CadIfUpChannelPCEmerResUsage_Type(Integer32):
    """Custom type cadIfUpChannelPCEmerResUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfUpChannelPCEmerResUsage_Type.__name__ = "Integer32"
_CadIfUpChannelPCEmerResUsage_Object = MibTableColumn
cadIfUpChannelPCEmerResUsage = _CadIfUpChannelPCEmerResUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 55),
    _CadIfUpChannelPCEmerResUsage_Type()
)
cadIfUpChannelPCEmerResUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCEmerResUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPCEmerResUsage.setUnits("percent")


class _CadIfUpChannelPCTotalAllowedUsage_Type(Integer32):
    """Custom type cadIfUpChannelPCTotalAllowedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CadIfUpChannelPCTotalAllowedUsage_Type.__name__ = "Integer32"
_CadIfUpChannelPCTotalAllowedUsage_Object = MibTableColumn
cadIfUpChannelPCTotalAllowedUsage = _CadIfUpChannelPCTotalAllowedUsage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 56),
    _CadIfUpChannelPCTotalAllowedUsage_Type()
)
cadIfUpChannelPCTotalAllowedUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCTotalAllowedUsage.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelPCTotalAllowedUsage.setUnits("percent")
_CadIfUpChannelIfIndex_Type = InterfaceIndex
_CadIfUpChannelIfIndex_Object = MibTableColumn
cadIfUpChannelIfIndex = _CadIfUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 57),
    _CadIfUpChannelIfIndex_Type()
)
cadIfUpChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfUpChannelIfIndex.setStatus("current")


class _CadIfUpChannelScdmaActiveCodes_Type(Unsigned32):
    """Custom type cadIfUpChannelScdmaActiveCodes based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 128),
    )


_CadIfUpChannelScdmaActiveCodes_Type.__name__ = "Unsigned32"
_CadIfUpChannelScdmaActiveCodes_Object = MibTableColumn
cadIfUpChannelScdmaActiveCodes = _CadIfUpChannelScdmaActiveCodes_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 58),
    _CadIfUpChannelScdmaActiveCodes_Type()
)
cadIfUpChannelScdmaActiveCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelScdmaActiveCodes.setStatus("current")


class _CadIfUpChannelScdmaCodesPerSlot_Type(Integer32):
    """Custom type cadIfUpChannelScdmaCodesPerSlot based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 32),
    )


_CadIfUpChannelScdmaCodesPerSlot_Type.__name__ = "Integer32"
_CadIfUpChannelScdmaCodesPerSlot_Object = MibTableColumn
cadIfUpChannelScdmaCodesPerSlot = _CadIfUpChannelScdmaCodesPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 59),
    _CadIfUpChannelScdmaCodesPerSlot_Type()
)
cadIfUpChannelScdmaCodesPerSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelScdmaCodesPerSlot.setStatus("current")


class _CadIfUpChannelScdmaFrameSize_Type(Unsigned32):
    """Custom type cadIfUpChannelScdmaFrameSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_CadIfUpChannelScdmaFrameSize_Type.__name__ = "Unsigned32"
_CadIfUpChannelScdmaFrameSize_Object = MibTableColumn
cadIfUpChannelScdmaFrameSize = _CadIfUpChannelScdmaFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 60),
    _CadIfUpChannelScdmaFrameSize_Type()
)
cadIfUpChannelScdmaFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelScdmaFrameSize.setStatus("current")


class _CadIfUpChannelScdmaHoppingSeed_Type(Unsigned32):
    """Custom type cadIfUpChannelScdmaHoppingSeed based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CadIfUpChannelScdmaHoppingSeed_Type.__name__ = "Unsigned32"
_CadIfUpChannelScdmaHoppingSeed_Object = MibTableColumn
cadIfUpChannelScdmaHoppingSeed = _CadIfUpChannelScdmaHoppingSeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 61),
    _CadIfUpChannelScdmaHoppingSeed_Type()
)
cadIfUpChannelScdmaHoppingSeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelScdmaHoppingSeed.setStatus("current")


class _CadIfUpChannelType_Type(DocsisUpstreamType):
    """Custom type cadIfUpChannelType based on DocsisUpstreamType"""


_CadIfUpChannelType_Object = MibTableColumn
cadIfUpChannelType = _CadIfUpChannelType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 62),
    _CadIfUpChannelType_Type()
)
cadIfUpChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelType.setStatus("current")


class _CadIfUpChannelCMKeepSpectralDensity_Type(TruthValue):
    """Custom type cadIfUpChannelCMKeepSpectralDensity based on TruthValue"""


_CadIfUpChannelCMKeepSpectralDensity_Object = MibTableColumn
cadIfUpChannelCMKeepSpectralDensity = _CadIfUpChannelCMKeepSpectralDensity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 63),
    _CadIfUpChannelCMKeepSpectralDensity_Type()
)
cadIfUpChannelCMKeepSpectralDensity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadIfUpChannelCMKeepSpectralDensity.setStatus("current")


class _CadIfUpChannelIngressCancellationInterval_Type(Unsigned32):
    """Custom type cadIfUpChannelIngressCancellationInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CadIfUpChannelIngressCancellationInterval_Type.__name__ = "Unsigned32"
_CadIfUpChannelIngressCancellationInterval_Object = MibTableColumn
cadIfUpChannelIngressCancellationInterval = _CadIfUpChannelIngressCancellationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 64),
    _CadIfUpChannelIngressCancellationInterval_Type()
)
cadIfUpChannelIngressCancellationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelIngressCancellationInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelIngressCancellationInterval.setUnits("milliseconds")


class _CadIfUpChannelIngressCancellationSize_Type(Unsigned32):
    """Custom type cadIfUpChannelIngressCancellationSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CadIfUpChannelIngressCancellationSize_Type.__name__ = "Unsigned32"
_CadIfUpChannelIngressCancellationSize_Object = MibTableColumn
cadIfUpChannelIngressCancellationSize = _CadIfUpChannelIngressCancellationSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 65),
    _CadIfUpChannelIngressCancellationSize_Type()
)
cadIfUpChannelIngressCancellationSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelIngressCancellationSize.setStatus("current")
if mibBuilder.loadTexts:
    cadIfUpChannelIngressCancellationSize.setUnits("minislots")
_CadIfUpChannelPCPreemptionAllowed_Type = TruthValue
_CadIfUpChannelPCPreemptionAllowed_Object = MibTableColumn
cadIfUpChannelPCPreemptionAllowed = _CadIfUpChannelPCPreemptionAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 66),
    _CadIfUpChannelPCPreemptionAllowed_Type()
)
cadIfUpChannelPCPreemptionAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelPCPreemptionAllowed.setStatus("current")


class _CadIfUpChannelSpGroupIndex_Type(Integer32):
    """Custom type cadIfUpChannelSpGroupIndex based on Integer32"""
    defaultValue = 0


_CadIfUpChannelSpGroupIndex_Object = MibTableColumn
cadIfUpChannelSpGroupIndex = _CadIfUpChannelSpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 69),
    _CadIfUpChannelSpGroupIndex_Type()
)
cadIfUpChannelSpGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelSpGroupIndex.setStatus("current")


class _CadIfUpChannelNumberEqTaps_Type(Unsigned32):
    """Custom type cadIfUpChannelNumberEqTaps based on Unsigned32"""
    defaultValue = 24

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(24, 24),
    )


_CadIfUpChannelNumberEqTaps_Type.__name__ = "Unsigned32"
_CadIfUpChannelNumberEqTaps_Object = MibTableColumn
cadIfUpChannelNumberEqTaps = _CadIfUpChannelNumberEqTaps_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 2, 1, 70),
    _CadIfUpChannelNumberEqTaps_Type()
)
cadIfUpChannelNumberEqTaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadIfUpChannelNumberEqTaps.setStatus("current")
_CadUpchannelParams_ObjectIdentity = ObjectIdentity
cadUpchannelParams = _CadUpchannelParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5)
)


class _CadUpchannelFreqRange_Type(Integer32):
    """Custom type cadUpchannelFreqRange based on Integer32"""
    defaultValue = 3

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
        *(("european", 1),
          ("extendedRange", 4),
          ("japanese", 2),
          ("none", 0),
          ("northAmerican", 3))
    )


_CadUpchannelFreqRange_Type.__name__ = "Integer32"
_CadUpchannelFreqRange_Object = MibScalar
cadUpchannelFreqRange = _CadUpchannelFreqRange_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 6),
    _CadUpchannelFreqRange_Type()
)
cadUpchannelFreqRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelFreqRange.setStatus("current")


class _CadUpchannelRtpsPiggybackEnable_Type(TruthValue):
    """Custom type cadUpchannelRtpsPiggybackEnable based on TruthValue"""


_CadUpchannelRtpsPiggybackEnable_Object = MibScalar
cadUpchannelRtpsPiggybackEnable = _CadUpchannelRtpsPiggybackEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 7),
    _CadUpchannelRtpsPiggybackEnable_Type()
)
cadUpchannelRtpsPiggybackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelRtpsPiggybackEnable.setStatus("current")


class _CadUpchannelCaCertDropEnable_Type(TruthValue):
    """Custom type cadUpchannelCaCertDropEnable based on TruthValue"""


_CadUpchannelCaCertDropEnable_Object = MibScalar
cadUpchannelCaCertDropEnable = _CadUpchannelCaCertDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 8),
    _CadUpchannelCaCertDropEnable_Type()
)
cadUpchannelCaCertDropEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelCaCertDropEnable.setStatus("current")


class _CadUpchannelRangingTimingOffset_Type(Integer32):
    """Custom type cadUpchannelRangingTimingOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-512, 512),
    )


_CadUpchannelRangingTimingOffset_Type.__name__ = "Integer32"
_CadUpchannelRangingTimingOffset_Object = MibScalar
cadUpchannelRangingTimingOffset = _CadUpchannelRangingTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 9),
    _CadUpchannelRangingTimingOffset_Type()
)
cadUpchannelRangingTimingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelRangingTimingOffset.setStatus("current")


class _CadUpchannelRecoverImpairedOnAck_Type(Integer32):
    """Custom type cadUpchannelRecoverImpairedOnAck based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("attemptIndefiniteRecovery", 1),
          ("disable", 0))
    )


_CadUpchannelRecoverImpairedOnAck_Type.__name__ = "Integer32"
_CadUpchannelRecoverImpairedOnAck_Object = MibScalar
cadUpchannelRecoverImpairedOnAck = _CadUpchannelRecoverImpairedOnAck_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 10),
    _CadUpchannelRecoverImpairedOnAck_Type()
)
cadUpchannelRecoverImpairedOnAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelRecoverImpairedOnAck.setStatus("current")


class _CadUpchannelDsaRspSidTlvOverride_Type(TruthValue):
    """Custom type cadUpchannelDsaRspSidTlvOverride based on TruthValue"""


_CadUpchannelDsaRspSidTlvOverride_Object = MibScalar
cadUpchannelDsaRspSidTlvOverride = _CadUpchannelDsaRspSidTlvOverride_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 5, 11),
    _CadUpchannelDsaRspSidTlvOverride_Type()
)
cadUpchannelDsaRspSidTlvOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUpchannelDsaRspSidTlvOverride.setStatus("current")
_CadUnicastPollingTable_Object = MibTable
cadUnicastPollingTable = _CadUnicastPollingTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6)
)
if mibBuilder.loadTexts:
    cadUnicastPollingTable.setStatus("current")
_CadUnicastPollingEntry_Object = MibTableRow
cadUnicastPollingEntry = _CadUnicastPollingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1)
)
cadUnicastPollingEntry.setIndexNames(
    (0, "CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastPriority"),
)
if mibBuilder.loadTexts:
    cadUnicastPollingEntry.setStatus("current")


class _CadUnicastPriority_Type(Integer32):
    """Custom type cadUnicastPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CadUnicastPriority_Type.__name__ = "Integer32"
_CadUnicastPriority_Object = MibTableColumn
cadUnicastPriority = _CadUnicastPriority_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 1),
    _CadUnicastPriority_Type()
)
cadUnicastPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadUnicastPriority.setStatus("current")


class _CadUnicastSlowPollInterval_Type(Integer32):
    """Custom type cadUnicastSlowPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1000),
    )


_CadUnicastSlowPollInterval_Type.__name__ = "Integer32"
_CadUnicastSlowPollInterval_Object = MibTableColumn
cadUnicastSlowPollInterval = _CadUnicastSlowPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 2),
    _CadUnicastSlowPollInterval_Type()
)
cadUnicastSlowPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUnicastSlowPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadUnicastSlowPollInterval.setUnits("tens of milliseconds")


class _CadUnicastFastPollInterval_Type(Integer32):
    """Custom type cadUnicastFastPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 1000),
    )


_CadUnicastFastPollInterval_Type.__name__ = "Integer32"
_CadUnicastFastPollInterval_Object = MibTableColumn
cadUnicastFastPollInterval = _CadUnicastFastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 3),
    _CadUnicastFastPollInterval_Type()
)
cadUnicastFastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUnicastFastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    cadUnicastFastPollInterval.setUnits("tens of milliseconds")


class _CadUnicastFastPollTimeout_Type(Integer32):
    """Custom type cadUnicastFastPollTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 5000),
    )


_CadUnicastFastPollTimeout_Type.__name__ = "Integer32"
_CadUnicastFastPollTimeout_Object = MibTableColumn
cadUnicastFastPollTimeout = _CadUnicastFastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 6, 1, 4),
    _CadUnicastFastPollTimeout_Type()
)
cadUnicastFastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadUnicastFastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cadUnicastFastPollTimeout.setUnits("tens of milliseconds")
_CadUpchannelConformance_ObjectIdentity = ObjectIdentity
cadUpchannelConformance = _CadUpchannelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7)
)
_CadUpchannelCompliances_ObjectIdentity = ObjectIdentity
cadUpchannelCompliances = _CadUpchannelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 1)
)
_CadUpchannelGroups_ObjectIdentity = ObjectIdentity
cadUpchannelGroups = _CadUpchannelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 2)
)

# Managed Objects groups

cadUpchannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 2, 1)
)
cadUpchannelGroup.setObjects(
      *(("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModControl"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModType"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleLen"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModDifferentialEncoding"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModFECErrorCorrection"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModFECCodewordLength"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScramblerSeed"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModMaxBurstSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModGuardTimeSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModLastCodewordShortened"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScrambler"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleValueOffset"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwLength"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwPattern"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwDetectionWindow"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModBroadcomUwMismatchThreshold"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModByteInterleaverDepth"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModByteInterleaverBlockSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModPreambleType"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModTcmErrorCorrectionOn"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaInterleaverStepSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaSpreaderEnable"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModScdmaSubframeCodes"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfCmtsModChannelType"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelFrequency"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelWidth"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelModulationProfile"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPowerDesired"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelSlotSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelRangingBackoffStart"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelRangingBackoffEnd"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelTxBackoffStart"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelTxBackoffEnd"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelMapSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelMaxPowerAdjust"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelThresholdPowerOffset"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroPowerAdjust"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroFreqAdjust"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelZeroTimingAdjust"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPreEqEnable"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCNormAllowedUsage"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCNormResUsage"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCEmerAllowedUsage"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCEmerResUsage"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCTotalAllowedUsage"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaActiveCodes"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaCodesPerSlot"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaFrameSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelScdmaHoppingSeed"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelType"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIngressCancellationInterval"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelIngressCancellationSize"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadIfUpChannelPCPreemptionAllowed"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadUpchannelFreqRange"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastSlowPollInterval"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastFastPollInterval"),
        ("CADANT-CMTS-UPCHANNEL-MIB", "cadUnicastFastPollTimeout"))
)
if mibBuilder.loadTexts:
    cadUpchannelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cadUpchannelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 15, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    cadUpchannelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-UPCHANNEL-MIB",
    **{"cadUpchannelMib": cadUpchannelMib,
       "cadIfCmtsModulationTable": cadIfCmtsModulationTable,
       "cadIfCmtsModulationEntry": cadIfCmtsModulationEntry,
       "cadIfCmtsModIndex": cadIfCmtsModIndex,
       "cadIfCmtsModIntervalUsageCode": cadIfCmtsModIntervalUsageCode,
       "cadIfCmtsModControl": cadIfCmtsModControl,
       "cadIfCmtsModType": cadIfCmtsModType,
       "cadIfCmtsModPreambleLen": cadIfCmtsModPreambleLen,
       "cadIfCmtsModDifferentialEncoding": cadIfCmtsModDifferentialEncoding,
       "cadIfCmtsModFECErrorCorrection": cadIfCmtsModFECErrorCorrection,
       "cadIfCmtsModFECCodewordLength": cadIfCmtsModFECCodewordLength,
       "cadIfCmtsModScramblerSeed": cadIfCmtsModScramblerSeed,
       "cadIfCmtsModMaxBurstSize": cadIfCmtsModMaxBurstSize,
       "cadIfCmtsModGuardTimeSize": cadIfCmtsModGuardTimeSize,
       "cadIfCmtsModLastCodewordShortened": cadIfCmtsModLastCodewordShortened,
       "cadIfCmtsModScrambler": cadIfCmtsModScrambler,
       "cadIfCmtsModPreambleValueOffset": cadIfCmtsModPreambleValueOffset,
       "cadIfCmtsModBroadcomUwLength": cadIfCmtsModBroadcomUwLength,
       "cadIfCmtsModBroadcomUwPattern": cadIfCmtsModBroadcomUwPattern,
       "cadIfCmtsModBroadcomUwDetectionWindow": cadIfCmtsModBroadcomUwDetectionWindow,
       "cadIfCmtsModBroadcomUwMismatchThreshold": cadIfCmtsModBroadcomUwMismatchThreshold,
       "cadIfCmtsModByteInterleaverDepth": cadIfCmtsModByteInterleaverDepth,
       "cadIfCmtsModByteInterleaverBlockSize": cadIfCmtsModByteInterleaverBlockSize,
       "cadIfCmtsModPreambleType": cadIfCmtsModPreambleType,
       "cadIfCmtsModTcmErrorCorrectionOn": cadIfCmtsModTcmErrorCorrectionOn,
       "cadIfCmtsModScdmaInterleaverStepSize": cadIfCmtsModScdmaInterleaverStepSize,
       "cadIfCmtsModScdmaSpreaderEnable": cadIfCmtsModScdmaSpreaderEnable,
       "cadIfCmtsModScdmaSubframeCodes": cadIfCmtsModScdmaSubframeCodes,
       "cadIfCmtsModChannelType": cadIfCmtsModChannelType,
       "cadIfUpstreamChannelTable": cadIfUpstreamChannelTable,
       "cadIfUpstreamChannelEntry": cadIfUpstreamChannelEntry,
       "cadIfUpChannelCardNumber": cadIfUpChannelCardNumber,
       "cadIfUpChannelId": cadIfUpChannelId,
       "cadIfUpChannelFrequency": cadIfUpChannelFrequency,
       "cadIfUpChannelWidth": cadIfUpChannelWidth,
       "cadIfUpChannelModulationProfile": cadIfUpChannelModulationProfile,
       "cadIfUpChannelPowerDesired": cadIfUpChannelPowerDesired,
       "cadIfUpChannelSlotSize": cadIfUpChannelSlotSize,
       "cadIfUpChannelRangingBackoffStart": cadIfUpChannelRangingBackoffStart,
       "cadIfUpChannelRangingBackoffEnd": cadIfUpChannelRangingBackoffEnd,
       "cadIfUpChannelTxBackoffStart": cadIfUpChannelTxBackoffStart,
       "cadIfUpChannelTxBackoffEnd": cadIfUpChannelTxBackoffEnd,
       "cadIfUpChannelMapSize": cadIfUpChannelMapSize,
       "cadIfUpChannelMaxPowerAdjust": cadIfUpChannelMaxPowerAdjust,
       "cadIfUpChannelThresholdPowerOffset": cadIfUpChannelThresholdPowerOffset,
       "cadIfUpChannelZeroPowerAdjust": cadIfUpChannelZeroPowerAdjust,
       "cadIfUpChannelZeroFreqAdjust": cadIfUpChannelZeroFreqAdjust,
       "cadIfUpChannelZeroTimingAdjust": cadIfUpChannelZeroTimingAdjust,
       "cadIfUpChannelPreEqEnable": cadIfUpChannelPreEqEnable,
       "cadIfUpChannelPCNormAllowedUsage": cadIfUpChannelPCNormAllowedUsage,
       "cadIfUpChannelPCNormResUsage": cadIfUpChannelPCNormResUsage,
       "cadIfUpChannelPCEmerAllowedUsage": cadIfUpChannelPCEmerAllowedUsage,
       "cadIfUpChannelPCEmerResUsage": cadIfUpChannelPCEmerResUsage,
       "cadIfUpChannelPCTotalAllowedUsage": cadIfUpChannelPCTotalAllowedUsage,
       "cadIfUpChannelIfIndex": cadIfUpChannelIfIndex,
       "cadIfUpChannelScdmaActiveCodes": cadIfUpChannelScdmaActiveCodes,
       "cadIfUpChannelScdmaCodesPerSlot": cadIfUpChannelScdmaCodesPerSlot,
       "cadIfUpChannelScdmaFrameSize": cadIfUpChannelScdmaFrameSize,
       "cadIfUpChannelScdmaHoppingSeed": cadIfUpChannelScdmaHoppingSeed,
       "cadIfUpChannelType": cadIfUpChannelType,
       "cadIfUpChannelCMKeepSpectralDensity": cadIfUpChannelCMKeepSpectralDensity,
       "cadIfUpChannelIngressCancellationInterval": cadIfUpChannelIngressCancellationInterval,
       "cadIfUpChannelIngressCancellationSize": cadIfUpChannelIngressCancellationSize,
       "cadIfUpChannelPCPreemptionAllowed": cadIfUpChannelPCPreemptionAllowed,
       "cadIfUpChannelSpGroupIndex": cadIfUpChannelSpGroupIndex,
       "cadIfUpChannelNumberEqTaps": cadIfUpChannelNumberEqTaps,
       "cadUpchannelParams": cadUpchannelParams,
       "cadUpchannelFreqRange": cadUpchannelFreqRange,
       "cadUpchannelRtpsPiggybackEnable": cadUpchannelRtpsPiggybackEnable,
       "cadUpchannelCaCertDropEnable": cadUpchannelCaCertDropEnable,
       "cadUpchannelRangingTimingOffset": cadUpchannelRangingTimingOffset,
       "cadUpchannelRecoverImpairedOnAck": cadUpchannelRecoverImpairedOnAck,
       "cadUpchannelDsaRspSidTlvOverride": cadUpchannelDsaRspSidTlvOverride,
       "cadUnicastPollingTable": cadUnicastPollingTable,
       "cadUnicastPollingEntry": cadUnicastPollingEntry,
       "cadUnicastPriority": cadUnicastPriority,
       "cadUnicastSlowPollInterval": cadUnicastSlowPollInterval,
       "cadUnicastFastPollInterval": cadUnicastFastPollInterval,
       "cadUnicastFastPollTimeout": cadUnicastFastPollTimeout,
       "cadUpchannelConformance": cadUpchannelConformance,
       "cadUpchannelCompliances": cadUpchannelCompliances,
       "cadUpchannelCompliance": cadUpchannelCompliance,
       "cadUpchannelGroups": cadUpchannelGroups,
       "cadUpchannelGroup": cadUpchannelGroup}
)
