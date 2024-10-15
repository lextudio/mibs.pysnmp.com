# SNMP MIB module (COPPER-MOUNTAIN-NETWORKS-DSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COPPER-MOUNTAIN-NETWORKS-DSL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:03 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""




class PerfTotalCount(Gauge32):
    """Custom type PerfTotalCount based on Gauge32"""




class CmObjectPII(Integer32):
    """Custom type CmObjectPII based on Integer32"""




class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Coppermountain_ObjectIdentity = ObjectIdentity
coppermountain = _Coppermountain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996)
)
_CmRegistry_ObjectIdentity = ObjectIdentity
cmRegistry = _CmRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 1)
)
_CmCE120Platform_ObjectIdentity = ObjectIdentity
cmCE120Platform = _CmCE120Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 1, 1)
)
_CmCE150Platform_ObjectIdentity = ObjectIdentity
cmCE150Platform = _CmCE150Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 1, 2)
)
_CmCE200Platform_ObjectIdentity = ObjectIdentity
cmCE200Platform = _CmCE200Platform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 1, 3)
)
_CmTransmission_ObjectIdentity = ObjectIdentity
cmTransmission = _CmTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10)
)
_CmHDSL_ObjectIdentity = ObjectIdentity
cmHDSL = _CmHDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3)
)
_CmHDSLModemTable_Object = MibTable
cmHDSLModemTable = _CmHDSLModemTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1)
)
if mibBuilder.loadTexts:
    cmHDSLModemTable.setStatus("mandatory")
_CmHDSLModemEntry_Object = MibTableRow
cmHDSLModemEntry = _CmHDSLModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1)
)
cmHDSLModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmHDSLModemEntry.setStatus("mandatory")
_CmHDSLModemIndex_Type = Integer32
_CmHDSLModemIndex_Object = MibTableColumn
cmHDSLModemIndex = _CmHDSLModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 1),
    _CmHDSLModemIndex_Type()
)
cmHDSLModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemIndex.setStatus("mandatory")


class _CmHDSLModemType_Type(Integer32):
    """Custom type cmHDSLModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("central", 0),
          ("remote", 1))
    )


_CmHDSLModemType_Type.__name__ = "Integer32"
_CmHDSLModemType_Object = MibTableColumn
cmHDSLModemType = _CmHDSLModemType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 2),
    _CmHDSLModemType_Type()
)
cmHDSLModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemType.setStatus("mandatory")
_CmHDSLModemTxGain_Type = Integer32
_CmHDSLModemTxGain_Object = MibTableColumn
cmHDSLModemTxGain = _CmHDSLModemTxGain_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 3),
    _CmHDSLModemTxGain_Type()
)
cmHDSLModemTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemTxGain.setStatus("mandatory")


class _CmHDSLModemTestMode_Type(Integer32):
    """Custom type cmHDSLModemTestMode based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("continuous-2level-txmission", 9),
          ("continuous-4level-txmission", 8),
          ("digital-far-loopback", 3),
          ("digital-near-loopback", 2),
          ("external-analog-loopback", 1),
          ("internal-analog-loopback", 13),
          ("isolated-analog-loopback", 14),
          ("none", 0),
          ("set-maximum-VCXO-frequency", 12),
          ("set-minimum-VCXO-frequency", 11),
          ("set-nominal-VCXO-frequency", 10),
          ("tx-isolated-minus1-pulse", 6),
          ("tx-isolated-minus3-pulse", 7),
          ("tx-isolated-plus1-pulse", 5),
          ("tx-isolated-plus3-pulse", 4))
    )


_CmHDSLModemTestMode_Type.__name__ = "Integer32"
_CmHDSLModemTestMode_Object = MibTableColumn
cmHDSLModemTestMode = _CmHDSLModemTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 4),
    _CmHDSLModemTestMode_Type()
)
cmHDSLModemTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemTestMode.setStatus("mandatory")
_CmHDSLModemNoiseMargin_Type = Integer32
_CmHDSLModemNoiseMargin_Object = MibTableColumn
cmHDSLModemNoiseMargin = _CmHDSLModemNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 5),
    _CmHDSLModemNoiseMargin_Type()
)
cmHDSLModemNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemNoiseMargin.setStatus("mandatory")
_CmHDSLModemBPSwMajorVersion_Type = Integer32
_CmHDSLModemBPSwMajorVersion_Object = MibTableColumn
cmHDSLModemBPSwMajorVersion = _CmHDSLModemBPSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 7),
    _CmHDSLModemBPSwMajorVersion_Type()
)
cmHDSLModemBPSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemBPSwMajorVersion.setStatus("mandatory")
_CmHDSLModemBPSwMinorVersion_Type = Integer32
_CmHDSLModemBPSwMinorVersion_Object = MibTableColumn
cmHDSLModemBPSwMinorVersion = _CmHDSLModemBPSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 8),
    _CmHDSLModemBPSwMinorVersion_Type()
)
cmHDSLModemBPSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemBPSwMinorVersion.setStatus("mandatory")
_CmHDSLModemBPHwVersion_Type = Integer32
_CmHDSLModemBPHwVersion_Object = MibTableColumn
cmHDSLModemBPHwVersion = _CmHDSLModemBPHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 9),
    _CmHDSLModemBPHwVersion_Type()
)
cmHDSLModemBPHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemBPHwVersion.setStatus("mandatory")


class _CmHDSLModemDataRate_Type(Integer32):
    """Custom type cmHDSLModemDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(160,
              208,
              320,
              416,
              784,
              1040,
              1568)
        )
    )
    namedValues = NamedValues(
        *(("dr1040Kbps", 1040),
          ("dr1568Kbps", 1568),
          ("dr160Kbps", 160),
          ("dr208Kbps", 208),
          ("dr320Kbps", 320),
          ("dr416Kbps", 416),
          ("dr784Kbps", 784))
    )


_CmHDSLModemDataRate_Type.__name__ = "Integer32"
_CmHDSLModemDataRate_Object = MibTableColumn
cmHDSLModemDataRate = _CmHDSLModemDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 14),
    _CmHDSLModemDataRate_Type()
)
cmHDSLModemDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHDSLModemDataRate.setStatus("mandatory")
_CmHDSLModemCpeCode_Type = Integer32
_CmHDSLModemCpeCode_Object = MibTableColumn
cmHDSLModemCpeCode = _CmHDSLModemCpeCode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 15),
    _CmHDSLModemCpeCode_Type()
)
cmHDSLModemCpeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHDSLModemCpeCode.setStatus("mandatory")
_CmHDSLModemSuccessfulTrains_Type = Counter32
_CmHDSLModemSuccessfulTrains_Object = MibTableColumn
cmHDSLModemSuccessfulTrains = _CmHDSLModemSuccessfulTrains_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 16),
    _CmHDSLModemSuccessfulTrains_Type()
)
cmHDSLModemSuccessfulTrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemSuccessfulTrains.setStatus("mandatory")
_CmHDSLModemFailedTrainingAttempts_Type = Counter32
_CmHDSLModemFailedTrainingAttempts_Object = MibTableColumn
cmHDSLModemFailedTrainingAttempts = _CmHDSLModemFailedTrainingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 17),
    _CmHDSLModemFailedTrainingAttempts_Type()
)
cmHDSLModemFailedTrainingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemFailedTrainingAttempts.setStatus("mandatory")
_CmHDSLModemCpeResponses_Type = Counter32
_CmHDSLModemCpeResponses_Object = MibTableColumn
cmHDSLModemCpeResponses = _CmHDSLModemCpeResponses_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 18),
    _CmHDSLModemCpeResponses_Type()
)
cmHDSLModemCpeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemCpeResponses.setStatus("mandatory")


class _CmHDSLModemMinRate_Type(Integer32):
    """Custom type cmHDSLModemMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              160,
              208,
              320,
              416,
              784,
              1040,
              1568)
        )
    )
    namedValues = NamedValues(
        *(("dr1040Kbps", 1040),
          ("dr1568Kbps", 1568),
          ("dr160Kbps", 160),
          ("dr208Kbps", 208),
          ("dr320Kbps", 320),
          ("dr416Kbps", 416),
          ("dr784Kbps", 784),
          ("none", 2))
    )


_CmHDSLModemMinRate_Type.__name__ = "Integer32"
_CmHDSLModemMinRate_Object = MibTableColumn
cmHDSLModemMinRate = _CmHDSLModemMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 19),
    _CmHDSLModemMinRate_Type()
)
cmHDSLModemMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHDSLModemMinRate.setStatus("mandatory")


class _CmHDSLModemCurrentRate_Type(Integer32):
    """Custom type cmHDSLModemCurrentRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              160,
              208,
              320,
              416,
              784,
              1040,
              1568)
        )
    )
    namedValues = NamedValues(
        *(("dr1040Kbps", 1040),
          ("dr1568Kbps", 1568),
          ("dr160Kbps", 160),
          ("dr208Kbps", 208),
          ("dr320Kbps", 320),
          ("dr416Kbps", 416),
          ("dr784Kbps", 784),
          ("unknown", 1))
    )


_CmHDSLModemCurrentRate_Type.__name__ = "Integer32"
_CmHDSLModemCurrentRate_Object = MibTableColumn
cmHDSLModemCurrentRate = _CmHDSLModemCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 20),
    _CmHDSLModemCurrentRate_Type()
)
cmHDSLModemCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHDSLModemCurrentRate.setStatus("mandatory")


class _CmHDSLModemCommand_Type(Integer32):
    """Custom type cmHDSLModemCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("retrain", 2))
    )


_CmHDSLModemCommand_Type.__name__ = "Integer32"
_CmHDSLModemCommand_Object = MibTableColumn
cmHDSLModemCommand = _CmHDSLModemCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 1, 1, 21),
    _CmHDSLModemCommand_Type()
)
cmHDSLModemCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHDSLModemCommand.setStatus("mandatory")
_CmHDSLPerfIntervalTable_Object = MibTable
cmHDSLPerfIntervalTable = _CmHDSLPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2)
)
if mibBuilder.loadTexts:
    cmHDSLPerfIntervalTable.setStatus("obsolete")
_CmHDSLPerfIntervalEntry_Object = MibTableRow
cmHDSLPerfIntervalEntry = _CmHDSLPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1)
)
cmHDSLPerfIntervalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLPerfIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    cmHDSLPerfIntervalEntry.setStatus("obsolete")
_CmHDSLPerfIndex_Type = Integer32
_CmHDSLPerfIndex_Object = MibTableColumn
cmHDSLPerfIndex = _CmHDSLPerfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 1),
    _CmHDSLPerfIndex_Type()
)
cmHDSLPerfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfIndex.setStatus("obsolete")


class _CmHDSLPerfIntervalNumber_Type(Integer32):
    """Custom type cmHDSLPerfIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CmHDSLPerfIntervalNumber_Type.__name__ = "Integer32"
_CmHDSLPerfIntervalNumber_Object = MibTableColumn
cmHDSLPerfIntervalNumber = _CmHDSLPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 2),
    _CmHDSLPerfIntervalNumber_Type()
)
cmHDSLPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfIntervalNumber.setStatus("obsolete")
_CmHDSLPerfTxUnderruns_Type = Counter32
_CmHDSLPerfTxUnderruns_Object = MibTableColumn
cmHDSLPerfTxUnderruns = _CmHDSLPerfTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 3),
    _CmHDSLPerfTxUnderruns_Type()
)
cmHDSLPerfTxUnderruns.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfTxUnderruns.setStatus("obsolete")
_CmHDSLPerfRxTruncated_Type = Counter32
_CmHDSLPerfRxTruncated_Object = MibTableColumn
cmHDSLPerfRxTruncated = _CmHDSLPerfRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 4),
    _CmHDSLPerfRxTruncated_Type()
)
cmHDSLPerfRxTruncated.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxTruncated.setStatus("obsolete")
_CmHDSLPerfRxBig_Type = Counter32
_CmHDSLPerfRxBig_Object = MibTableColumn
cmHDSLPerfRxBig = _CmHDSLPerfRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 5),
    _CmHDSLPerfRxBig_Type()
)
cmHDSLPerfRxBig.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxBig.setStatus("obsolete")
_CmHDSLPerfRxAborts_Type = Counter32
_CmHDSLPerfRxAborts_Object = MibTableColumn
cmHDSLPerfRxAborts = _CmHDSLPerfRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 6),
    _CmHDSLPerfRxAborts_Type()
)
cmHDSLPerfRxAborts.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxAborts.setStatus("obsolete")
_CmHDSLPerfRxAlignmentErrors_Type = Counter32
_CmHDSLPerfRxAlignmentErrors_Object = MibTableColumn
cmHDSLPerfRxAlignmentErrors = _CmHDSLPerfRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 7),
    _CmHDSLPerfRxAlignmentErrors_Type()
)
cmHDSLPerfRxAlignmentErrors.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxAlignmentErrors.setStatus("obsolete")
_CmHDSLPerfRxCRCErrors_Type = Counter32
_CmHDSLPerfRxCRCErrors_Object = MibTableColumn
cmHDSLPerfRxCRCErrors = _CmHDSLPerfRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 8),
    _CmHDSLPerfRxCRCErrors_Type()
)
cmHDSLPerfRxCRCErrors.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxCRCErrors.setStatus("obsolete")
_CmHDSLPerfRxOverruns_Type = Counter32
_CmHDSLPerfRxOverruns_Object = MibTableColumn
cmHDSLPerfRxOverruns = _CmHDSLPerfRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 9),
    _CmHDSLPerfRxOverruns_Type()
)
cmHDSLPerfRxOverruns.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxOverruns.setStatus("obsolete")
_CmHDSLPerfRxValidFrames_Type = Counter32
_CmHDSLPerfRxValidFrames_Object = MibTableColumn
cmHDSLPerfRxValidFrames = _CmHDSLPerfRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 10),
    _CmHDSLPerfRxValidFrames_Type()
)
cmHDSLPerfRxValidFrames.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxValidFrames.setStatus("obsolete")
_CmHDSLPerfTxValidFrames_Type = Counter32
_CmHDSLPerfTxValidFrames_Object = MibTableColumn
cmHDSLPerfTxValidFrames = _CmHDSLPerfTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 11),
    _CmHDSLPerfTxValidFrames_Type()
)
cmHDSLPerfTxValidFrames.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfTxValidFrames.setStatus("obsolete")
_CmHDSLPerfRxNoBuffers_Type = Counter32
_CmHDSLPerfRxNoBuffers_Object = MibTableColumn
cmHDSLPerfRxNoBuffers = _CmHDSLPerfRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 2, 1, 12),
    _CmHDSLPerfRxNoBuffers_Type()
)
cmHDSLPerfRxNoBuffers.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmHDSLPerfRxNoBuffers.setStatus("obsolete")
_CmCpeHDSLModemTable_Object = MibTable
cmCpeHDSLModemTable = _CmCpeHDSLModemTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3)
)
if mibBuilder.loadTexts:
    cmCpeHDSLModemTable.setStatus("mandatory")
_CmCpeHDSLModemEntry_Object = MibTableRow
cmCpeHDSLModemEntry = _CmCpeHDSLModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1)
)
cmCpeHDSLModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmCpeHDSLModemEntry.setStatus("mandatory")
_CmCpeHDSLModemIndex_Type = Integer32
_CmCpeHDSLModemIndex_Object = MibTableColumn
cmCpeHDSLModemIndex = _CmCpeHDSLModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 1),
    _CmCpeHDSLModemIndex_Type()
)
cmCpeHDSLModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemIndex.setStatus("mandatory")


class _CmCpeHDSLModemType_Type(Integer32):
    """Custom type cmCpeHDSLModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("central", 0),
          ("remote", 1))
    )


_CmCpeHDSLModemType_Type.__name__ = "Integer32"
_CmCpeHDSLModemType_Object = MibTableColumn
cmCpeHDSLModemType = _CmCpeHDSLModemType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 2),
    _CmCpeHDSLModemType_Type()
)
cmCpeHDSLModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemType.setStatus("mandatory")
_CmCpeHDSLModemTxGain_Type = Integer32
_CmCpeHDSLModemTxGain_Object = MibTableColumn
cmCpeHDSLModemTxGain = _CmCpeHDSLModemTxGain_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 3),
    _CmCpeHDSLModemTxGain_Type()
)
cmCpeHDSLModemTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemTxGain.setStatus("mandatory")


class _CmCpeHDSLModemTestMode_Type(Integer32):
    """Custom type cmCpeHDSLModemTestMode based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("continuous-2level-txmission", 9),
          ("continuous-4level-txmission", 8),
          ("digital-far-loopback", 3),
          ("digital-near-loopback", 2),
          ("external-analog-loopback", 1),
          ("internal-analog-loopback", 13),
          ("isolated-analog-loopback", 14),
          ("none", 0),
          ("set-maximum-VCXO-frequency", 12),
          ("set-minimum-VCXO-frequency", 11),
          ("set-nominal-VCXO-frequency", 10),
          ("tx-isolated-minus1-pulse", 6),
          ("tx-isolated-minus3-pulse", 7),
          ("tx-isolated-plus1-pulse", 5),
          ("tx-isolated-plus3-pulse", 4))
    )


_CmCpeHDSLModemTestMode_Type.__name__ = "Integer32"
_CmCpeHDSLModemTestMode_Object = MibTableColumn
cmCpeHDSLModemTestMode = _CmCpeHDSLModemTestMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 4),
    _CmCpeHDSLModemTestMode_Type()
)
cmCpeHDSLModemTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemTestMode.setStatus("mandatory")
_CmCpeHDSLModemNoiseMargin_Type = Integer32
_CmCpeHDSLModemNoiseMargin_Object = MibTableColumn
cmCpeHDSLModemNoiseMargin = _CmCpeHDSLModemNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 5),
    _CmCpeHDSLModemNoiseMargin_Type()
)
cmCpeHDSLModemNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemNoiseMargin.setStatus("mandatory")
_CmCpeHDSLModemBPSwMajorVersion_Type = Integer32
_CmCpeHDSLModemBPSwMajorVersion_Object = MibTableColumn
cmCpeHDSLModemBPSwMajorVersion = _CmCpeHDSLModemBPSwMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 7),
    _CmCpeHDSLModemBPSwMajorVersion_Type()
)
cmCpeHDSLModemBPSwMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemBPSwMajorVersion.setStatus("mandatory")
_CmCpeHDSLModemBPSwMinorVersion_Type = Integer32
_CmCpeHDSLModemBPSwMinorVersion_Object = MibTableColumn
cmCpeHDSLModemBPSwMinorVersion = _CmCpeHDSLModemBPSwMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 8),
    _CmCpeHDSLModemBPSwMinorVersion_Type()
)
cmCpeHDSLModemBPSwMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemBPSwMinorVersion.setStatus("mandatory")
_CmCpeHDSLModemBPHwVersion_Type = Integer32
_CmCpeHDSLModemBPHwVersion_Object = MibTableColumn
cmCpeHDSLModemBPHwVersion = _CmCpeHDSLModemBPHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 9),
    _CmCpeHDSLModemBPHwVersion_Type()
)
cmCpeHDSLModemBPHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemBPHwVersion.setStatus("mandatory")


class _CmCpeHDSLModemDataRate_Type(Integer32):
    """Custom type cmCpeHDSLModemDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(160,
              208,
              320,
              416,
              784,
              1040,
              1568)
        )
    )
    namedValues = NamedValues(
        *(("dr1040Kbps", 1040),
          ("dr1568Kbps", 1568),
          ("dr160Kbps", 160),
          ("dr208Kbps", 208),
          ("dr320Kbps", 320),
          ("dr416Kbps", 416),
          ("dr784Kbps", 784))
    )


_CmCpeHDSLModemDataRate_Type.__name__ = "Integer32"
_CmCpeHDSLModemDataRate_Object = MibTableColumn
cmCpeHDSLModemDataRate = _CmCpeHDSLModemDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 3, 1, 14),
    _CmCpeHDSLModemDataRate_Type()
)
cmCpeHDSLModemDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeHDSLModemDataRate.setStatus("mandatory")
_CmSDSLTestTable_Object = MibTable
cmSDSLTestTable = _CmSDSLTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4)
)
if mibBuilder.loadTexts:
    cmSDSLTestTable.setStatus("mandatory")
_CmSDSLTestEntry_Object = MibTableRow
cmSDSLTestEntry = _CmSDSLTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1)
)
cmSDSLTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmSDSLTestEntry.setStatus("mandatory")
_CmSDSLTestIndex_Type = CmObjectPII
_CmSDSLTestIndex_Object = MibTableColumn
cmSDSLTestIndex = _CmSDSLTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 1),
    _CmSDSLTestIndex_Type()
)
cmSDSLTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestIndex.setStatus("mandatory")


class _CmSDSLTestAction_Type(Integer32):
    """Custom type cmSDSLTestAction based on Integer32"""
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
          ("start", 2),
          ("stop", 3))
    )


_CmSDSLTestAction_Type.__name__ = "Integer32"
_CmSDSLTestAction_Object = MibTableColumn
cmSDSLTestAction = _CmSDSLTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 2),
    _CmSDSLTestAction_Type()
)
cmSDSLTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSDSLTestAction.setStatus("mandatory")


class _CmSDSLTestStatus_Type(Integer32):
    """Custom type cmSDSLTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("inProgress", 3),
          ("none", 1))
    )


_CmSDSLTestStatus_Type.__name__ = "Integer32"
_CmSDSLTestStatus_Object = MibTableColumn
cmSDSLTestStatus = _CmSDSLTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 3),
    _CmSDSLTestStatus_Type()
)
cmSDSLTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestStatus.setStatus("mandatory")
_CmSDSLTestTestCompleteTime_Type = DisplayString
_CmSDSLTestTestCompleteTime_Object = MibTableColumn
cmSDSLTestTestCompleteTime = _CmSDSLTestTestCompleteTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 4),
    _CmSDSLTestTestCompleteTime_Type()
)
cmSDSLTestTestCompleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestTestCompleteTime.setStatus("mandatory")
_CmSDSLTestContinuityTestResult_Type = Integer32
_CmSDSLTestContinuityTestResult_Object = MibTableColumn
cmSDSLTestContinuityTestResult = _CmSDSLTestContinuityTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 5),
    _CmSDSLTestContinuityTestResult_Type()
)
cmSDSLTestContinuityTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestContinuityTestResult.setStatus("mandatory")


class _CmSDSLTestNearEndLoopProfile_Type(Integer32):
    """Custom type cmSDSLTestNearEndLoopProfile based on Integer32"""
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
        *(("cpeTalking", 5),
          ("normal", 1),
          ("pending", 4),
          ("possibleOpen", 3),
          ("possibleShort", 2))
    )


_CmSDSLTestNearEndLoopProfile_Type.__name__ = "Integer32"
_CmSDSLTestNearEndLoopProfile_Object = MibTableColumn
cmSDSLTestNearEndLoopProfile = _CmSDSLTestNearEndLoopProfile_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 6),
    _CmSDSLTestNearEndLoopProfile_Type()
)
cmSDSLTestNearEndLoopProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestNearEndLoopProfile.setStatus("mandatory")
_CmSDSLTestDebugResult_Type = Integer32
_CmSDSLTestDebugResult_Object = MibTableColumn
cmSDSLTestDebugResult = _CmSDSLTestDebugResult_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 7),
    _CmSDSLTestDebugResult_Type()
)
cmSDSLTestDebugResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestDebugResult.setStatus("mandatory")


class _CmSDSLTestType_Type(Integer32):
    """Custom type cmSDSLTestType based on Integer32"""
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
        *(("cpeDownload", 4),
          ("none", 1),
          ("profile", 2),
          ("seekMaxRate", 3))
    )


_CmSDSLTestType_Type.__name__ = "Integer32"
_CmSDSLTestType_Object = MibTableColumn
cmSDSLTestType = _CmSDSLTestType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 8),
    _CmSDSLTestType_Type()
)
cmSDSLTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSDSLTestType.setStatus("mandatory")


class _CmSDSLTestMaxRate_Type(Integer32):
    """Custom type cmSDSLTestMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              160,
              208,
              320,
              416,
              784,
              1040,
              1568)
        )
    )
    namedValues = NamedValues(
        *(("dr1040Kbps", 1040),
          ("dr1568Kbps", 1568),
          ("dr160Kbps", 160),
          ("dr208Kbps", 208),
          ("dr320Kbps", 320),
          ("dr416Kbps", 416),
          ("dr784Kbps", 784),
          ("unknown", 1))
    )


_CmSDSLTestMaxRate_Type.__name__ = "Integer32"
_CmSDSLTestMaxRate_Object = MibTableColumn
cmSDSLTestMaxRate = _CmSDSLTestMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 3, 4, 1, 9),
    _CmSDSLTestMaxRate_Type()
)
cmSDSLTestMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSDSLTestMaxRate.setStatus("mandatory")
_CmIface_ObjectIdentity = ObjectIdentity
cmIface = _CmIface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4)
)
_CmIfaceTable_Object = MibTable
cmIfaceTable = _CmIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1)
)
if mibBuilder.loadTexts:
    cmIfaceTable.setStatus("mandatory")
_CmIfaceEntry_Object = MibTableRow
cmIfaceEntry = _CmIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1)
)
cmIfaceEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIfacePII"),
)
if mibBuilder.loadTexts:
    cmIfaceEntry.setStatus("mandatory")
_CmIfacePII_Type = CmObjectPII
_CmIfacePII_Object = MibTableColumn
cmIfacePII = _CmIfacePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 1),
    _CmIfacePII_Type()
)
cmIfacePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIfacePII.setStatus("mandatory")
_CmIfaceIfIndex_Type = Integer32
_CmIfaceIfIndex_Object = MibTableColumn
cmIfaceIfIndex = _CmIfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 2),
    _CmIfaceIfIndex_Type()
)
cmIfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIfaceIfIndex.setStatus("mandatory")


class _CmIfaceNetModel_Type(Integer32):
    """Custom type cmIfaceNetModel based on Integer32"""
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
        *(("copperVPN", 5),
          ("frame", 4),
          ("ip", 2),
          ("none", 1),
          ("vwan", 3))
    )


_CmIfaceNetModel_Type.__name__ = "Integer32"
_CmIfaceNetModel_Object = MibTableColumn
cmIfaceNetModel = _CmIfaceNetModel_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 3),
    _CmIfaceNetModel_Type()
)
cmIfaceNetModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceNetModel.setStatus("mandatory")
_CmIfaceIpAddr_Type = IpAddress
_CmIfaceIpAddr_Object = MibTableColumn
cmIfaceIpAddr = _CmIfaceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 4),
    _CmIfaceIpAddr_Type()
)
cmIfaceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceIpAddr.setStatus("mandatory")
_CmIfaceNetMask_Type = IpAddress
_CmIfaceNetMask_Object = MibTableColumn
cmIfaceNetMask = _CmIfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 5),
    _CmIfaceNetMask_Type()
)
cmIfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceNetMask.setStatus("mandatory")
_CmIfaceMacAddr_Type = OctetString
_CmIfaceMacAddr_Object = MibTableColumn
cmIfaceMacAddr = _CmIfaceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 6),
    _CmIfaceMacAddr_Type()
)
cmIfaceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIfaceMacAddr.setStatus("mandatory")
_CmIfaceBurnedInMacAddr_Type = OctetString
_CmIfaceBurnedInMacAddr_Object = MibTableColumn
cmIfaceBurnedInMacAddr = _CmIfaceBurnedInMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 7),
    _CmIfaceBurnedInMacAddr_Type()
)
cmIfaceBurnedInMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIfaceBurnedInMacAddr.setStatus("mandatory")
_CmIfaceFarEndAddr_Type = IpAddress
_CmIfaceFarEndAddr_Object = MibTableColumn
cmIfaceFarEndAddr = _CmIfaceFarEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 8),
    _CmIfaceFarEndAddr_Type()
)
cmIfaceFarEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceFarEndAddr.setStatus("mandatory")
_CmIfaceDestPII_Type = CmObjectPII
_CmIfaceDestPII_Object = MibTableColumn
cmIfaceDestPII = _CmIfaceDestPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 9),
    _CmIfaceDestPII_Type()
)
cmIfaceDestPII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceDestPII.setStatus("mandatory")


class _CmIfaceFwdMode_Type(Integer32):
    """Custom type cmIfaceFwdMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("copperVPN", 9),
          ("copperVPNauto", 10),
          ("frame-mux", 7),
          ("frf8-1490-1483", 14),
          ("fullIP", 2),
          ("hdlc-vc-payload", 11),
          ("none", 1),
          ("policyIP", 3),
          ("policyIP-enet", 6),
          ("ppp-hdlc-1973", 13),
          ("vc-vc-payload", 12),
          ("vwan-bridge", 5),
          ("vwan-pp", 4))
    )


_CmIfaceFwdMode_Type.__name__ = "Integer32"
_CmIfaceFwdMode_Object = MibTableColumn
cmIfaceFwdMode = _CmIfaceFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 10),
    _CmIfaceFwdMode_Type()
)
cmIfaceFwdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIfaceFwdMode.setStatus("mandatory")


class _CmIfaceName_Type(DisplayString):
    """Custom type cmIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CmIfaceName_Type.__name__ = "DisplayString"
_CmIfaceName_Object = MibTableColumn
cmIfaceName = _CmIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 11),
    _CmIfaceName_Type()
)
cmIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceName.setStatus("mandatory")


class _CmIfaceAdditionalInfo_Type(DisplayString):
    """Custom type cmIfaceAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CmIfaceAdditionalInfo_Type.__name__ = "DisplayString"
_CmIfaceAdditionalInfo_Object = MibTableColumn
cmIfaceAdditionalInfo = _CmIfaceAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 12),
    _CmIfaceAdditionalInfo_Type()
)
cmIfaceAdditionalInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceAdditionalInfo.setStatus("mandatory")


class _CmIfaceCMCPCompatible_Type(Integer32):
    """Custom type cmIfaceCMCPCompatible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmIfaceCMCPCompatible_Type.__name__ = "Integer32"
_CmIfaceCMCPCompatible_Object = MibTableColumn
cmIfaceCMCPCompatible = _CmIfaceCMCPCompatible_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 13),
    _CmIfaceCMCPCompatible_Type()
)
cmIfaceCMCPCompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceCMCPCompatible.setStatus("mandatory")


class _CmIfaceEncapsulationType_Type(Integer32):
    """Custom type cmIfaceEncapsulationType based on Integer32"""
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
        *(("hdlc", 4),
          ("none", 1),
          ("ppp-hdlc", 5),
          ("q922", 7),
          ("q922-1490", 8),
          ("rfc1483", 2),
          ("rfc1490", 3),
          ("rfc1973", 6))
    )


_CmIfaceEncapsulationType_Type.__name__ = "Integer32"
_CmIfaceEncapsulationType_Object = MibTableColumn
cmIfaceEncapsulationType = _CmIfaceEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 14),
    _CmIfaceEncapsulationType_Type()
)
cmIfaceEncapsulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceEncapsulationType.setStatus("mandatory")


class _CmIfaceGroupName_Type(DisplayString):
    """Custom type cmIfaceGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CmIfaceGroupName_Type.__name__ = "DisplayString"
_CmIfaceGroupName_Object = MibTableColumn
cmIfaceGroupName = _CmIfaceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 15),
    _CmIfaceGroupName_Type()
)
cmIfaceGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceGroupName.setStatus("mandatory")


class _CmIfaceServiceClass_Type(Integer32):
    """Custom type cmIfaceServiceClass based on Integer32"""
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
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("none", 1))
    )


_CmIfaceServiceClass_Type.__name__ = "Integer32"
_CmIfaceServiceClass_Object = MibTableColumn
cmIfaceServiceClass = _CmIfaceServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 1, 1, 16),
    _CmIfaceServiceClass_Type()
)
cmIfaceServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIfaceServiceClass.setStatus("mandatory")
_CmSubIfaceTable_Object = MibTable
cmSubIfaceTable = _CmSubIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2)
)
if mibBuilder.loadTexts:
    cmSubIfaceTable.setStatus("mandatory")
_CmSubIfaceEntry_Object = MibTableRow
cmSubIfaceEntry = _CmSubIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1)
)
cmSubIfaceEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmSubIfacePII"),
)
if mibBuilder.loadTexts:
    cmSubIfaceEntry.setStatus("mandatory")
_CmSubIfacePII_Type = Integer32
_CmSubIfacePII_Object = MibTableColumn
cmSubIfacePII = _CmSubIfacePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1, 1),
    _CmSubIfacePII_Type()
)
cmSubIfacePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSubIfacePII.setStatus("mandatory")
_CmSubIfaceDestPII_Type = CmObjectPII
_CmSubIfaceDestPII_Object = MibTableColumn
cmSubIfaceDestPII = _CmSubIfaceDestPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1, 2),
    _CmSubIfaceDestPII_Type()
)
cmSubIfaceDestPII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSubIfaceDestPII.setStatus("mandatory")


class _CmSubIfaceName_Type(DisplayString):
    """Custom type cmSubIfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CmSubIfaceName_Type.__name__ = "DisplayString"
_CmSubIfaceName_Object = MibTableColumn
cmSubIfaceName = _CmSubIfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1, 3),
    _CmSubIfaceName_Type()
)
cmSubIfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSubIfaceName.setStatus("mandatory")


class _CmSubIfaceRowStatus_Type(Integer32):
    """Custom type cmSubIfaceRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CmSubIfaceRowStatus_Type.__name__ = "Integer32"
_CmSubIfaceRowStatus_Object = MibTableColumn
cmSubIfaceRowStatus = _CmSubIfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1, 4),
    _CmSubIfaceRowStatus_Type()
)
cmSubIfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSubIfaceRowStatus.setStatus("mandatory")


class _CmSubIfacePriority_Type(Integer32):
    """Custom type cmSubIfacePriority based on Integer32"""
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


_CmSubIfacePriority_Type.__name__ = "Integer32"
_CmSubIfacePriority_Object = MibTableColumn
cmSubIfacePriority = _CmSubIfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 4, 2, 1, 5),
    _CmSubIfacePriority_Type()
)
cmSubIfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSubIfacePriority.setStatus("mandatory")
_CmEthernet_ObjectIdentity = ObjectIdentity
cmEthernet = _CmEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5)
)
_CmCpeEthernetIntervalTable_Object = MibTable
cmCpeEthernetIntervalTable = _CmCpeEthernetIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1)
)
if mibBuilder.loadTexts:
    cmCpeEthernetIntervalTable.setStatus("mandatory")
_CmCpeEthernetIntervalEntry_Object = MibTableRow
cmCpeEthernetIntervalEntry = _CmCpeEthernetIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1)
)
cmCpeEthernetIntervalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeEthernetIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeEthernetIntervalNumber"),
)
if mibBuilder.loadTexts:
    cmCpeEthernetIntervalEntry.setStatus("mandatory")
_CmCpeEthernetIndex_Type = Integer32
_CmCpeEthernetIndex_Object = MibTableColumn
cmCpeEthernetIndex = _CmCpeEthernetIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 1),
    _CmCpeEthernetIndex_Type()
)
cmCpeEthernetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetIndex.setStatus("mandatory")


class _CmCpeEthernetIntervalNumber_Type(Integer32):
    """Custom type cmCpeEthernetIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CmCpeEthernetIntervalNumber_Type.__name__ = "Integer32"
_CmCpeEthernetIntervalNumber_Object = MibTableColumn
cmCpeEthernetIntervalNumber = _CmCpeEthernetIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 2),
    _CmCpeEthernetIntervalNumber_Type()
)
cmCpeEthernetIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetIntervalNumber.setStatus("mandatory")
_CmCpeEthernetIntUnknowns_Type = Counter32
_CmCpeEthernetIntUnknowns_Object = MibTableColumn
cmCpeEthernetIntUnknowns = _CmCpeEthernetIntUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 3),
    _CmCpeEthernetIntUnknowns_Type()
)
cmCpeEthernetIntUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetIntUnknowns.setStatus("mandatory")
_CmCpeEthernetRxOK_Type = Counter32
_CmCpeEthernetRxOK_Object = MibTableColumn
cmCpeEthernetRxOK = _CmCpeEthernetRxOK_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 4),
    _CmCpeEthernetRxOK_Type()
)
cmCpeEthernetRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxOK.setStatus("mandatory")
_CmCpeEthernetRxNoBufs_Type = Counter32
_CmCpeEthernetRxNoBufs_Object = MibTableColumn
cmCpeEthernetRxNoBufs = _CmCpeEthernetRxNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 5),
    _CmCpeEthernetRxNoBufs_Type()
)
cmCpeEthernetRxNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxNoBufs.setStatus("mandatory")
_CmCpeEthernetRxMiss_Type = Counter32
_CmCpeEthernetRxMiss_Object = MibTableColumn
cmCpeEthernetRxMiss = _CmCpeEthernetRxMiss_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 6),
    _CmCpeEthernetRxMiss_Type()
)
cmCpeEthernetRxMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxMiss.setStatus("mandatory")
_CmCpeEthernetRxSkip_Type = Counter32
_CmCpeEthernetRxSkip_Object = MibTableColumn
cmCpeEthernetRxSkip = _CmCpeEthernetRxSkip_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 7),
    _CmCpeEthernetRxSkip_Type()
)
cmCpeEthernetRxSkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxSkip.setStatus("mandatory")
_CmCpeEthernetRxRunt_Type = Counter32
_CmCpeEthernetRxRunt_Object = MibTableColumn
cmCpeEthernetRxRunt = _CmCpeEthernetRxRunt_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 8),
    _CmCpeEthernetRxRunt_Type()
)
cmCpeEthernetRxRunt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxRunt.setStatus("mandatory")
_CmCpeEthernetRxExtraData_Type = Counter32
_CmCpeEthernetRxExtraData_Object = MibTableColumn
cmCpeEthernetRxExtraData = _CmCpeEthernetRxExtraData_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 9),
    _CmCpeEthernetRxExtraData_Type()
)
cmCpeEthernetRxExtraData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxExtraData.setStatus("mandatory")
_CmCpeEthernetRxCRCError_Type = Counter32
_CmCpeEthernetRxCRCError_Object = MibTableColumn
cmCpeEthernetRxCRCError = _CmCpeEthernetRxCRCError_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 10),
    _CmCpeEthernetRxCRCError_Type()
)
cmCpeEthernetRxCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxCRCError.setStatus("mandatory")
_CmCpeEthernetRxAlignError_Type = Counter32
_CmCpeEthernetRxAlignError_Object = MibTableColumn
cmCpeEthernetRxAlignError = _CmCpeEthernetRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 11),
    _CmCpeEthernetRxAlignError_Type()
)
cmCpeEthernetRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxAlignError.setStatus("mandatory")
_CmCpeEthernetRxDribbleBits_Type = Counter32
_CmCpeEthernetRxDribbleBits_Object = MibTableColumn
cmCpeEthernetRxDribbleBits = _CmCpeEthernetRxDribbleBits_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 12),
    _CmCpeEthernetRxDribbleBits_Type()
)
cmCpeEthernetRxDribbleBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetRxDribbleBits.setStatus("mandatory")
_CmCpeEthernetTxTooBig_Type = Counter32
_CmCpeEthernetTxTooBig_Object = MibTableColumn
cmCpeEthernetTxTooBig = _CmCpeEthernetTxTooBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 13),
    _CmCpeEthernetTxTooBig_Type()
)
cmCpeEthernetTxTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxTooBig.setStatus("mandatory")
_CmCpeEthernetTxNotReady_Type = Counter32
_CmCpeEthernetTxNotReady_Object = MibTableColumn
cmCpeEthernetTxNotReady = _CmCpeEthernetTxNotReady_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 14),
    _CmCpeEthernetTxNotReady_Type()
)
cmCpeEthernetTxNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxNotReady.setStatus("mandatory")
_CmCpeEthernetTxLossCRS_Type = Counter32
_CmCpeEthernetTxLossCRS_Object = MibTableColumn
cmCpeEthernetTxLossCRS = _CmCpeEthernetTxLossCRS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 15),
    _CmCpeEthernetTxLossCRS_Type()
)
cmCpeEthernetTxLossCRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxLossCRS.setStatus("mandatory")
_CmCpeEthernetTxSQEErr_Type = Counter32
_CmCpeEthernetTxSQEErr_Object = MibTableColumn
cmCpeEthernetTxSQEErr = _CmCpeEthernetTxSQEErr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 16),
    _CmCpeEthernetTxSQEErr_Type()
)
cmCpeEthernetTxSQEErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxSQEErr.setStatus("mandatory")
_CmCpeEthernetTxOutOfWindow_Type = Counter32
_CmCpeEthernetTxOutOfWindow_Object = MibTableColumn
cmCpeEthernetTxOutOfWindow = _CmCpeEthernetTxOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 17),
    _CmCpeEthernetTxOutOfWindow_Type()
)
cmCpeEthernetTxOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxOutOfWindow.setStatus("mandatory")
_CmCpeEthernetTxJabber_Type = Counter32
_CmCpeEthernetTxJabber_Object = MibTableColumn
cmCpeEthernetTxJabber = _CmCpeEthernetTxJabber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 18),
    _CmCpeEthernetTxJabber_Type()
)
cmCpeEthernetTxJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxJabber.setStatus("mandatory")
_CmCpeEthernetTx16Collisions_Type = Counter32
_CmCpeEthernetTx16Collisions_Object = MibTableColumn
cmCpeEthernetTx16Collisions = _CmCpeEthernetTx16Collisions_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 19),
    _CmCpeEthernetTx16Collisions_Type()
)
cmCpeEthernetTx16Collisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTx16Collisions.setStatus("mandatory")
_CmCpeEthernetTxCollisions_Type = Counter32
_CmCpeEthernetTxCollisions_Object = MibTableColumn
cmCpeEthernetTxCollisions = _CmCpeEthernetTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 20),
    _CmCpeEthernetTxCollisions_Type()
)
cmCpeEthernetTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxCollisions.setStatus("mandatory")
_CmCpeEthernetTxOK_Type = Counter32
_CmCpeEthernetTxOK_Object = MibTableColumn
cmCpeEthernetTxOK = _CmCpeEthernetTxOK_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 5, 1, 1, 21),
    _CmCpeEthernetTxOK_Type()
)
cmCpeEthernetTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeEthernetTxOK.setStatus("mandatory")
_CmFilter_ObjectIdentity = ObjectIdentity
cmFilter = _CmFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6)
)
_CmFilterTable_Object = MibTable
cmFilterTable = _CmFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1)
)
if mibBuilder.loadTexts:
    cmFilterTable.setStatus("mandatory")
_CmFilterEntry_Object = MibTableRow
cmFilterEntry = _CmFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1)
)
cmFilterEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmFilterIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmFilterFilterNumber"),
)
if mibBuilder.loadTexts:
    cmFilterEntry.setStatus("mandatory")
_CmFilterIndex_Type = Integer32
_CmFilterIndex_Object = MibTableColumn
cmFilterIndex = _CmFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 1),
    _CmFilterIndex_Type()
)
cmFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFilterIndex.setStatus("mandatory")
_CmFilterFilterNumber_Type = Integer32
_CmFilterFilterNumber_Object = MibTableColumn
cmFilterFilterNumber = _CmFilterFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 2),
    _CmFilterFilterNumber_Type()
)
cmFilterFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFilterFilterNumber.setStatus("mandatory")


class _CmFilterFunction_Type(Integer32):
    """Custom type cmFilterFunction based on Integer32"""
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
        *(("active", 1),
          ("delete", 3),
          ("deleteList", 4),
          ("insert", 2))
    )


_CmFilterFunction_Type.__name__ = "Integer32"
_CmFilterFunction_Object = MibTableColumn
cmFilterFunction = _CmFilterFunction_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 3),
    _CmFilterFunction_Type()
)
cmFilterFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterFunction.setStatus("mandatory")
_CmFilterSrcMask_Type = IpAddress
_CmFilterSrcMask_Object = MibTableColumn
cmFilterSrcMask = _CmFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 4),
    _CmFilterSrcMask_Type()
)
cmFilterSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterSrcMask.setStatus("mandatory")
_CmFilterSrcAdrs_Type = IpAddress
_CmFilterSrcAdrs_Object = MibTableColumn
cmFilterSrcAdrs = _CmFilterSrcAdrs_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 5),
    _CmFilterSrcAdrs_Type()
)
cmFilterSrcAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterSrcAdrs.setStatus("mandatory")
_CmFilterDstMask_Type = IpAddress
_CmFilterDstMask_Object = MibTableColumn
cmFilterDstMask = _CmFilterDstMask_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 6),
    _CmFilterDstMask_Type()
)
cmFilterDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterDstMask.setStatus("mandatory")
_CmFilterDstAdrs_Type = IpAddress
_CmFilterDstAdrs_Object = MibTableColumn
cmFilterDstAdrs = _CmFilterDstAdrs_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 7),
    _CmFilterDstAdrs_Type()
)
cmFilterDstAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterDstAdrs.setStatus("mandatory")
_CmFilterIpProtocol_Type = Integer32
_CmFilterIpProtocol_Object = MibTableColumn
cmFilterIpProtocol = _CmFilterIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 8),
    _CmFilterIpProtocol_Type()
)
cmFilterIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterIpProtocol.setStatus("mandatory")


class _CmFilterSrcPortCompare_Type(Integer32):
    """Custom type cmFilterSrcPortCompare based on Integer32"""
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
        *(("any", 1),
          ("equal", 3),
          ("greater", 4),
          ("less", 2),
          ("notEqual", 5))
    )


_CmFilterSrcPortCompare_Type.__name__ = "Integer32"
_CmFilterSrcPortCompare_Object = MibTableColumn
cmFilterSrcPortCompare = _CmFilterSrcPortCompare_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 9),
    _CmFilterSrcPortCompare_Type()
)
cmFilterSrcPortCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterSrcPortCompare.setStatus("mandatory")
_CmFilterSrcPort_Type = Integer32
_CmFilterSrcPort_Object = MibTableColumn
cmFilterSrcPort = _CmFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 10),
    _CmFilterSrcPort_Type()
)
cmFilterSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterSrcPort.setStatus("mandatory")


class _CmFilterDstPortCompare_Type(Integer32):
    """Custom type cmFilterDstPortCompare based on Integer32"""
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
        *(("any", 1),
          ("equal", 3),
          ("greater", 4),
          ("less", 2),
          ("notEqual", 5))
    )


_CmFilterDstPortCompare_Type.__name__ = "Integer32"
_CmFilterDstPortCompare_Object = MibTableColumn
cmFilterDstPortCompare = _CmFilterDstPortCompare_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 11),
    _CmFilterDstPortCompare_Type()
)
cmFilterDstPortCompare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterDstPortCompare.setStatus("mandatory")
_CmFilterDstPort_Type = Integer32
_CmFilterDstPort_Object = MibTableColumn
cmFilterDstPort = _CmFilterDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 12),
    _CmFilterDstPort_Type()
)
cmFilterDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterDstPort.setStatus("mandatory")


class _CmFilterAction_Type(Integer32):
    """Custom type cmFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("chain", 3),
          ("pass", 1))
    )


_CmFilterAction_Type.__name__ = "Integer32"
_CmFilterAction_Object = MibTableColumn
cmFilterAction = _CmFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 6, 1, 1, 13),
    _CmFilterAction_Type()
)
cmFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFilterAction.setStatus("mandatory")
_CmDSL_ObjectIdentity = ObjectIdentity
cmDSL = _CmDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7)
)
_CmDSLIntervalTable_Object = MibTable
cmDSLIntervalTable = _CmDSLIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1)
)
if mibBuilder.loadTexts:
    cmDSLIntervalTable.setStatus("mandatory")
_CmDSLIntervalEntry_Object = MibTableRow
cmDSLIntervalEntry = _CmDSLIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1)
)
cmDSLIntervalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSLIntervalIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSLIntervalNumber"),
)
if mibBuilder.loadTexts:
    cmDSLIntervalEntry.setStatus("mandatory")
_CmDSLIntervalIndex_Type = Integer32
_CmDSLIntervalIndex_Object = MibTableColumn
cmDSLIntervalIndex = _CmDSLIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 1),
    _CmDSLIntervalIndex_Type()
)
cmDSLIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalIndex.setStatus("mandatory")


class _CmDSLIntervalNumber_Type(Integer32):
    """Custom type cmDSLIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CmDSLIntervalNumber_Type.__name__ = "Integer32"
_CmDSLIntervalNumber_Object = MibTableColumn
cmDSLIntervalNumber = _CmDSLIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 2),
    _CmDSLIntervalNumber_Type()
)
cmDSLIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalNumber.setStatus("mandatory")
_CmDSLIntervalTxUnderruns_Type = PerfTotalCount
_CmDSLIntervalTxUnderruns_Object = MibTableColumn
cmDSLIntervalTxUnderruns = _CmDSLIntervalTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 3),
    _CmDSLIntervalTxUnderruns_Type()
)
cmDSLIntervalTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalTxUnderruns.setStatus("mandatory")
_CmDSLIntervalRxTruncated_Type = PerfTotalCount
_CmDSLIntervalRxTruncated_Object = MibTableColumn
cmDSLIntervalRxTruncated = _CmDSLIntervalRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 4),
    _CmDSLIntervalRxTruncated_Type()
)
cmDSLIntervalRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxTruncated.setStatus("mandatory")
_CmDSLIntervalRxBig_Type = PerfTotalCount
_CmDSLIntervalRxBig_Object = MibTableColumn
cmDSLIntervalRxBig = _CmDSLIntervalRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 5),
    _CmDSLIntervalRxBig_Type()
)
cmDSLIntervalRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxBig.setStatus("mandatory")
_CmDSLIntervalRxAborts_Type = PerfTotalCount
_CmDSLIntervalRxAborts_Object = MibTableColumn
cmDSLIntervalRxAborts = _CmDSLIntervalRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 6),
    _CmDSLIntervalRxAborts_Type()
)
cmDSLIntervalRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxAborts.setStatus("mandatory")
_CmDSLIntervalRxAlignmentErrors_Type = PerfTotalCount
_CmDSLIntervalRxAlignmentErrors_Object = MibTableColumn
cmDSLIntervalRxAlignmentErrors = _CmDSLIntervalRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 7),
    _CmDSLIntervalRxAlignmentErrors_Type()
)
cmDSLIntervalRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxAlignmentErrors.setStatus("mandatory")
_CmDSLIntervalRxCRCErrors_Type = PerfTotalCount
_CmDSLIntervalRxCRCErrors_Object = MibTableColumn
cmDSLIntervalRxCRCErrors = _CmDSLIntervalRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 8),
    _CmDSLIntervalRxCRCErrors_Type()
)
cmDSLIntervalRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxCRCErrors.setStatus("mandatory")
_CmDSLIntervalRxOverruns_Type = PerfTotalCount
_CmDSLIntervalRxOverruns_Object = MibTableColumn
cmDSLIntervalRxOverruns = _CmDSLIntervalRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 9),
    _CmDSLIntervalRxOverruns_Type()
)
cmDSLIntervalRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxOverruns.setStatus("mandatory")
_CmDSLIntervalRxValidFrames_Type = PerfTotalCount
_CmDSLIntervalRxValidFrames_Object = MibTableColumn
cmDSLIntervalRxValidFrames = _CmDSLIntervalRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 10),
    _CmDSLIntervalRxValidFrames_Type()
)
cmDSLIntervalRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxValidFrames.setStatus("mandatory")
_CmDSLIntervalTxValidFrames_Type = PerfTotalCount
_CmDSLIntervalTxValidFrames_Object = MibTableColumn
cmDSLIntervalTxValidFrames = _CmDSLIntervalTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 11),
    _CmDSLIntervalTxValidFrames_Type()
)
cmDSLIntervalTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalTxValidFrames.setStatus("mandatory")
_CmDSLIntervalRxNoBuffers_Type = PerfTotalCount
_CmDSLIntervalRxNoBuffers_Object = MibTableColumn
cmDSLIntervalRxNoBuffers = _CmDSLIntervalRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 12),
    _CmDSLIntervalRxNoBuffers_Type()
)
cmDSLIntervalRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxNoBuffers.setStatus("mandatory")
_CmDSLIntervalTimeTagBegin_Type = DisplayString
_CmDSLIntervalTimeTagBegin_Object = MibTableColumn
cmDSLIntervalTimeTagBegin = _CmDSLIntervalTimeTagBegin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 13),
    _CmDSLIntervalTimeTagBegin_Type()
)
cmDSLIntervalTimeTagBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalTimeTagBegin.setStatus("mandatory")
_CmDSLIntervalTimeTagEnd_Type = DisplayString
_CmDSLIntervalTimeTagEnd_Object = MibTableColumn
cmDSLIntervalTimeTagEnd = _CmDSLIntervalTimeTagEnd_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 14),
    _CmDSLIntervalTimeTagEnd_Type()
)
cmDSLIntervalTimeTagEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalTimeTagEnd.setStatus("mandatory")
_CmDSLIntervalMinNoiseMargin_Type = Integer32
_CmDSLIntervalMinNoiseMargin_Object = MibTableColumn
cmDSLIntervalMinNoiseMargin = _CmDSLIntervalMinNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 15),
    _CmDSLIntervalMinNoiseMargin_Type()
)
cmDSLIntervalMinNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalMinNoiseMargin.setStatus("mandatory")
_CmDSLIntervalRxValidOctets_Type = PerfTotalCount
_CmDSLIntervalRxValidOctets_Object = MibTableColumn
cmDSLIntervalRxValidOctets = _CmDSLIntervalRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 16),
    _CmDSLIntervalRxValidOctets_Type()
)
cmDSLIntervalRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalRxValidOctets.setStatus("mandatory")
_CmDSLIntervalTxValidOctets_Type = PerfTotalCount
_CmDSLIntervalTxValidOctets_Object = MibTableColumn
cmDSLIntervalTxValidOctets = _CmDSLIntervalTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 17),
    _CmDSLIntervalTxValidOctets_Type()
)
cmDSLIntervalTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalTxValidOctets.setStatus("mandatory")
_CmDSLIntervalPortUpTime_Type = PerfTotalCount
_CmDSLIntervalPortUpTime_Object = MibTableColumn
cmDSLIntervalPortUpTime = _CmDSLIntervalPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 1, 1, 18),
    _CmDSLIntervalPortUpTime_Type()
)
cmDSLIntervalPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLIntervalPortUpTime.setStatus("mandatory")
_CmDSLCurrentTable_Object = MibTable
cmDSLCurrentTable = _CmDSLCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2)
)
if mibBuilder.loadTexts:
    cmDSLCurrentTable.setStatus("mandatory")
_CmDSLCurrentEntry_Object = MibTableRow
cmDSLCurrentEntry = _CmDSLCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1)
)
cmDSLCurrentEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSLCurrentIndex"),
)
if mibBuilder.loadTexts:
    cmDSLCurrentEntry.setStatus("mandatory")
_CmDSLCurrentIndex_Type = Integer32
_CmDSLCurrentIndex_Object = MibTableColumn
cmDSLCurrentIndex = _CmDSLCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 1),
    _CmDSLCurrentIndex_Type()
)
cmDSLCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentIndex.setStatus("mandatory")
_CmDSLCurrentTxUnderruns_Type = PerfTotalCount
_CmDSLCurrentTxUnderruns_Object = MibTableColumn
cmDSLCurrentTxUnderruns = _CmDSLCurrentTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 3),
    _CmDSLCurrentTxUnderruns_Type()
)
cmDSLCurrentTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentTxUnderruns.setStatus("mandatory")
_CmDSLCurrentRxTruncated_Type = PerfTotalCount
_CmDSLCurrentRxTruncated_Object = MibTableColumn
cmDSLCurrentRxTruncated = _CmDSLCurrentRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 4),
    _CmDSLCurrentRxTruncated_Type()
)
cmDSLCurrentRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxTruncated.setStatus("mandatory")
_CmDSLCurrentRxBig_Type = PerfTotalCount
_CmDSLCurrentRxBig_Object = MibTableColumn
cmDSLCurrentRxBig = _CmDSLCurrentRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 5),
    _CmDSLCurrentRxBig_Type()
)
cmDSLCurrentRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxBig.setStatus("mandatory")
_CmDSLCurrentRxAborts_Type = PerfTotalCount
_CmDSLCurrentRxAborts_Object = MibTableColumn
cmDSLCurrentRxAborts = _CmDSLCurrentRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 6),
    _CmDSLCurrentRxAborts_Type()
)
cmDSLCurrentRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxAborts.setStatus("mandatory")
_CmDSLCurrentRxAlignmentErrors_Type = PerfTotalCount
_CmDSLCurrentRxAlignmentErrors_Object = MibTableColumn
cmDSLCurrentRxAlignmentErrors = _CmDSLCurrentRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 7),
    _CmDSLCurrentRxAlignmentErrors_Type()
)
cmDSLCurrentRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxAlignmentErrors.setStatus("mandatory")
_CmDSLCurrentRxCRCErrors_Type = PerfTotalCount
_CmDSLCurrentRxCRCErrors_Object = MibTableColumn
cmDSLCurrentRxCRCErrors = _CmDSLCurrentRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 8),
    _CmDSLCurrentRxCRCErrors_Type()
)
cmDSLCurrentRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxCRCErrors.setStatus("mandatory")
_CmDSLCurrentRxOverruns_Type = PerfTotalCount
_CmDSLCurrentRxOverruns_Object = MibTableColumn
cmDSLCurrentRxOverruns = _CmDSLCurrentRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 9),
    _CmDSLCurrentRxOverruns_Type()
)
cmDSLCurrentRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxOverruns.setStatus("mandatory")
_CmDSLCurrentRxValidFrames_Type = PerfTotalCount
_CmDSLCurrentRxValidFrames_Object = MibTableColumn
cmDSLCurrentRxValidFrames = _CmDSLCurrentRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 10),
    _CmDSLCurrentRxValidFrames_Type()
)
cmDSLCurrentRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxValidFrames.setStatus("mandatory")
_CmDSLCurrentTxValidFrames_Type = PerfTotalCount
_CmDSLCurrentTxValidFrames_Object = MibTableColumn
cmDSLCurrentTxValidFrames = _CmDSLCurrentTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 11),
    _CmDSLCurrentTxValidFrames_Type()
)
cmDSLCurrentTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentTxValidFrames.setStatus("mandatory")
_CmDSLCurrentRxNoBuffers_Type = PerfTotalCount
_CmDSLCurrentRxNoBuffers_Object = MibTableColumn
cmDSLCurrentRxNoBuffers = _CmDSLCurrentRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 12),
    _CmDSLCurrentRxNoBuffers_Type()
)
cmDSLCurrentRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxNoBuffers.setStatus("mandatory")
_CmDSLCurrentMinNoiseMargin_Type = Integer32
_CmDSLCurrentMinNoiseMargin_Object = MibTableColumn
cmDSLCurrentMinNoiseMargin = _CmDSLCurrentMinNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 13),
    _CmDSLCurrentMinNoiseMargin_Type()
)
cmDSLCurrentMinNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentMinNoiseMargin.setStatus("mandatory")
_CmDSLCurrentRxValidOctets_Type = PerfTotalCount
_CmDSLCurrentRxValidOctets_Object = MibTableColumn
cmDSLCurrentRxValidOctets = _CmDSLCurrentRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 14),
    _CmDSLCurrentRxValidOctets_Type()
)
cmDSLCurrentRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentRxValidOctets.setStatus("mandatory")
_CmDSLCurrentTxValidOctets_Type = PerfTotalCount
_CmDSLCurrentTxValidOctets_Object = MibTableColumn
cmDSLCurrentTxValidOctets = _CmDSLCurrentTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 15),
    _CmDSLCurrentTxValidOctets_Type()
)
cmDSLCurrentTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentTxValidOctets.setStatus("mandatory")
_CmDSLCurrentPortUpTime_Type = PerfTotalCount
_CmDSLCurrentPortUpTime_Object = MibTableColumn
cmDSLCurrentPortUpTime = _CmDSLCurrentPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 2, 1, 16),
    _CmDSLCurrentPortUpTime_Type()
)
cmDSLCurrentPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLCurrentPortUpTime.setStatus("mandatory")
_CmDSLYesterdaysTable_Object = MibTable
cmDSLYesterdaysTable = _CmDSLYesterdaysTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3)
)
if mibBuilder.loadTexts:
    cmDSLYesterdaysTable.setStatus("mandatory")
_CmDSLYesterdaysEntry_Object = MibTableRow
cmDSLYesterdaysEntry = _CmDSLYesterdaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1)
)
cmDSLYesterdaysEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSLYesterdaysIndex"),
)
if mibBuilder.loadTexts:
    cmDSLYesterdaysEntry.setStatus("mandatory")
_CmDSLYesterdaysIndex_Type = Integer32
_CmDSLYesterdaysIndex_Object = MibTableColumn
cmDSLYesterdaysIndex = _CmDSLYesterdaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 1),
    _CmDSLYesterdaysIndex_Type()
)
cmDSLYesterdaysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysIndex.setStatus("mandatory")
_CmDSLYesterdaysTxUnderruns_Type = PerfTotalCount
_CmDSLYesterdaysTxUnderruns_Object = MibTableColumn
cmDSLYesterdaysTxUnderruns = _CmDSLYesterdaysTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 2),
    _CmDSLYesterdaysTxUnderruns_Type()
)
cmDSLYesterdaysTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysTxUnderruns.setStatus("mandatory")
_CmDSLYesterdaysRxTruncated_Type = PerfTotalCount
_CmDSLYesterdaysRxTruncated_Object = MibTableColumn
cmDSLYesterdaysRxTruncated = _CmDSLYesterdaysRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 3),
    _CmDSLYesterdaysRxTruncated_Type()
)
cmDSLYesterdaysRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxTruncated.setStatus("mandatory")
_CmDSLYesterdaysRxBig_Type = PerfTotalCount
_CmDSLYesterdaysRxBig_Object = MibTableColumn
cmDSLYesterdaysRxBig = _CmDSLYesterdaysRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 4),
    _CmDSLYesterdaysRxBig_Type()
)
cmDSLYesterdaysRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxBig.setStatus("mandatory")
_CmDSLYesterdaysRxAborts_Type = PerfTotalCount
_CmDSLYesterdaysRxAborts_Object = MibTableColumn
cmDSLYesterdaysRxAborts = _CmDSLYesterdaysRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 5),
    _CmDSLYesterdaysRxAborts_Type()
)
cmDSLYesterdaysRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxAborts.setStatus("mandatory")
_CmDSLYesterdaysRxAlignmentErrors_Type = PerfTotalCount
_CmDSLYesterdaysRxAlignmentErrors_Object = MibTableColumn
cmDSLYesterdaysRxAlignmentErrors = _CmDSLYesterdaysRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 6),
    _CmDSLYesterdaysRxAlignmentErrors_Type()
)
cmDSLYesterdaysRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxAlignmentErrors.setStatus("mandatory")
_CmDSLYesterdaysRxCRCErrors_Type = PerfTotalCount
_CmDSLYesterdaysRxCRCErrors_Object = MibTableColumn
cmDSLYesterdaysRxCRCErrors = _CmDSLYesterdaysRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 7),
    _CmDSLYesterdaysRxCRCErrors_Type()
)
cmDSLYesterdaysRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxCRCErrors.setStatus("mandatory")
_CmDSLYesterdaysRxOverruns_Type = PerfTotalCount
_CmDSLYesterdaysRxOverruns_Object = MibTableColumn
cmDSLYesterdaysRxOverruns = _CmDSLYesterdaysRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 8),
    _CmDSLYesterdaysRxOverruns_Type()
)
cmDSLYesterdaysRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxOverruns.setStatus("mandatory")
_CmDSLYesterdaysRxValidFrames_Type = PerfTotalCount
_CmDSLYesterdaysRxValidFrames_Object = MibTableColumn
cmDSLYesterdaysRxValidFrames = _CmDSLYesterdaysRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 9),
    _CmDSLYesterdaysRxValidFrames_Type()
)
cmDSLYesterdaysRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxValidFrames.setStatus("mandatory")
_CmDSLYesterdaysTxValidFrames_Type = PerfTotalCount
_CmDSLYesterdaysTxValidFrames_Object = MibTableColumn
cmDSLYesterdaysTxValidFrames = _CmDSLYesterdaysTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 10),
    _CmDSLYesterdaysTxValidFrames_Type()
)
cmDSLYesterdaysTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysTxValidFrames.setStatus("mandatory")
_CmDSLYesterdaysRxNoBuffers_Type = PerfTotalCount
_CmDSLYesterdaysRxNoBuffers_Object = MibTableColumn
cmDSLYesterdaysRxNoBuffers = _CmDSLYesterdaysRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 11),
    _CmDSLYesterdaysRxNoBuffers_Type()
)
cmDSLYesterdaysRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxNoBuffers.setStatus("mandatory")
_CmDSLYesterdaysMinNoiseMargin_Type = Integer32
_CmDSLYesterdaysMinNoiseMargin_Object = MibTableColumn
cmDSLYesterdaysMinNoiseMargin = _CmDSLYesterdaysMinNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 12),
    _CmDSLYesterdaysMinNoiseMargin_Type()
)
cmDSLYesterdaysMinNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysMinNoiseMargin.setStatus("mandatory")
_CmDSLYesterdaysRxValidOctets_Type = PerfTotalCount
_CmDSLYesterdaysRxValidOctets_Object = MibTableColumn
cmDSLYesterdaysRxValidOctets = _CmDSLYesterdaysRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 13),
    _CmDSLYesterdaysRxValidOctets_Type()
)
cmDSLYesterdaysRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysRxValidOctets.setStatus("mandatory")
_CmDSLYesterdaysTxValidOctets_Type = PerfTotalCount
_CmDSLYesterdaysTxValidOctets_Object = MibTableColumn
cmDSLYesterdaysTxValidOctets = _CmDSLYesterdaysTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 14),
    _CmDSLYesterdaysTxValidOctets_Type()
)
cmDSLYesterdaysTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysTxValidOctets.setStatus("mandatory")
_CmDSLYesterdaysPortUpTime_Type = PerfTotalCount
_CmDSLYesterdaysPortUpTime_Object = MibTableColumn
cmDSLYesterdaysPortUpTime = _CmDSLYesterdaysPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 3, 1, 15),
    _CmDSLYesterdaysPortUpTime_Type()
)
cmDSLYesterdaysPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLYesterdaysPortUpTime.setStatus("mandatory")
_CmDSLTodaysTable_Object = MibTable
cmDSLTodaysTable = _CmDSLTodaysTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4)
)
if mibBuilder.loadTexts:
    cmDSLTodaysTable.setStatus("mandatory")
_CmDSLTodaysEntry_Object = MibTableRow
cmDSLTodaysEntry = _CmDSLTodaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1)
)
cmDSLTodaysEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSLTodaysIndex"),
)
if mibBuilder.loadTexts:
    cmDSLTodaysEntry.setStatus("mandatory")
_CmDSLTodaysIndex_Type = Integer32
_CmDSLTodaysIndex_Object = MibTableColumn
cmDSLTodaysIndex = _CmDSLTodaysIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 1),
    _CmDSLTodaysIndex_Type()
)
cmDSLTodaysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysIndex.setStatus("mandatory")
_CmDSLTodaysTxUnderruns_Type = PerfTotalCount
_CmDSLTodaysTxUnderruns_Object = MibTableColumn
cmDSLTodaysTxUnderruns = _CmDSLTodaysTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 2),
    _CmDSLTodaysTxUnderruns_Type()
)
cmDSLTodaysTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysTxUnderruns.setStatus("mandatory")
_CmDSLTodaysRxTruncated_Type = PerfTotalCount
_CmDSLTodaysRxTruncated_Object = MibTableColumn
cmDSLTodaysRxTruncated = _CmDSLTodaysRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 3),
    _CmDSLTodaysRxTruncated_Type()
)
cmDSLTodaysRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxTruncated.setStatus("mandatory")
_CmDSLTodaysRxBig_Type = PerfTotalCount
_CmDSLTodaysRxBig_Object = MibTableColumn
cmDSLTodaysRxBig = _CmDSLTodaysRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 4),
    _CmDSLTodaysRxBig_Type()
)
cmDSLTodaysRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxBig.setStatus("mandatory")
_CmDSLTodaysRxAborts_Type = PerfTotalCount
_CmDSLTodaysRxAborts_Object = MibTableColumn
cmDSLTodaysRxAborts = _CmDSLTodaysRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 5),
    _CmDSLTodaysRxAborts_Type()
)
cmDSLTodaysRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxAborts.setStatus("mandatory")
_CmDSLTodaysRxAlignmentErrors_Type = PerfTotalCount
_CmDSLTodaysRxAlignmentErrors_Object = MibTableColumn
cmDSLTodaysRxAlignmentErrors = _CmDSLTodaysRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 6),
    _CmDSLTodaysRxAlignmentErrors_Type()
)
cmDSLTodaysRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxAlignmentErrors.setStatus("mandatory")
_CmDSLTodaysRxCRCErrors_Type = PerfTotalCount
_CmDSLTodaysRxCRCErrors_Object = MibTableColumn
cmDSLTodaysRxCRCErrors = _CmDSLTodaysRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 7),
    _CmDSLTodaysRxCRCErrors_Type()
)
cmDSLTodaysRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxCRCErrors.setStatus("mandatory")
_CmDSLTodaysRxOverruns_Type = PerfTotalCount
_CmDSLTodaysRxOverruns_Object = MibTableColumn
cmDSLTodaysRxOverruns = _CmDSLTodaysRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 8),
    _CmDSLTodaysRxOverruns_Type()
)
cmDSLTodaysRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxOverruns.setStatus("mandatory")
_CmDSLTodaysRxValidFrames_Type = PerfTotalCount
_CmDSLTodaysRxValidFrames_Object = MibTableColumn
cmDSLTodaysRxValidFrames = _CmDSLTodaysRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 9),
    _CmDSLTodaysRxValidFrames_Type()
)
cmDSLTodaysRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxValidFrames.setStatus("mandatory")
_CmDSLTodaysTxValidFrames_Type = PerfTotalCount
_CmDSLTodaysTxValidFrames_Object = MibTableColumn
cmDSLTodaysTxValidFrames = _CmDSLTodaysTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 10),
    _CmDSLTodaysTxValidFrames_Type()
)
cmDSLTodaysTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysTxValidFrames.setStatus("mandatory")
_CmDSLTodaysRxNoBuffers_Type = PerfTotalCount
_CmDSLTodaysRxNoBuffers_Object = MibTableColumn
cmDSLTodaysRxNoBuffers = _CmDSLTodaysRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 11),
    _CmDSLTodaysRxNoBuffers_Type()
)
cmDSLTodaysRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxNoBuffers.setStatus("mandatory")
_CmDSLTodaysMinNoiseMargin_Type = Integer32
_CmDSLTodaysMinNoiseMargin_Object = MibTableColumn
cmDSLTodaysMinNoiseMargin = _CmDSLTodaysMinNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 12),
    _CmDSLTodaysMinNoiseMargin_Type()
)
cmDSLTodaysMinNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysMinNoiseMargin.setStatus("mandatory")
_CmDSLTodaysRxValidOctets_Type = PerfTotalCount
_CmDSLTodaysRxValidOctets_Object = MibTableColumn
cmDSLTodaysRxValidOctets = _CmDSLTodaysRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 13),
    _CmDSLTodaysRxValidOctets_Type()
)
cmDSLTodaysRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysRxValidOctets.setStatus("mandatory")
_CmDSLTodaysTxValidOctets_Type = PerfTotalCount
_CmDSLTodaysTxValidOctets_Object = MibTableColumn
cmDSLTodaysTxValidOctets = _CmDSLTodaysTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 14),
    _CmDSLTodaysTxValidOctets_Type()
)
cmDSLTodaysTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysTxValidOctets.setStatus("mandatory")
_CmDSLTodaysPortUpTime_Type = PerfTotalCount
_CmDSLTodaysPortUpTime_Object = MibTableColumn
cmDSLTodaysPortUpTime = _CmDSLTodaysPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 4, 1, 15),
    _CmDSLTodaysPortUpTime_Type()
)
cmDSLTodaysPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSLTodaysPortUpTime.setStatus("mandatory")
_CmDSL24HrTable_Object = MibTable
cmDSL24HrTable = _CmDSL24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5)
)
if mibBuilder.loadTexts:
    cmDSL24HrTable.setStatus("mandatory")
_CmDSL24HrEntry_Object = MibTableRow
cmDSL24HrEntry = _CmDSL24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1)
)
cmDSL24HrEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDSL24HrIndex"),
)
if mibBuilder.loadTexts:
    cmDSL24HrEntry.setStatus("mandatory")
_CmDSL24HrIndex_Type = Integer32
_CmDSL24HrIndex_Object = MibTableColumn
cmDSL24HrIndex = _CmDSL24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 1),
    _CmDSL24HrIndex_Type()
)
cmDSL24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrIndex.setStatus("mandatory")
_CmDSL24HrTxUnderruns_Type = PerfTotalCount
_CmDSL24HrTxUnderruns_Object = MibTableColumn
cmDSL24HrTxUnderruns = _CmDSL24HrTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 2),
    _CmDSL24HrTxUnderruns_Type()
)
cmDSL24HrTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrTxUnderruns.setStatus("mandatory")
_CmDSL24HrRxTruncated_Type = PerfTotalCount
_CmDSL24HrRxTruncated_Object = MibTableColumn
cmDSL24HrRxTruncated = _CmDSL24HrRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 3),
    _CmDSL24HrRxTruncated_Type()
)
cmDSL24HrRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxTruncated.setStatus("mandatory")
_CmDSL24HrRxBig_Type = PerfTotalCount
_CmDSL24HrRxBig_Object = MibTableColumn
cmDSL24HrRxBig = _CmDSL24HrRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 4),
    _CmDSL24HrRxBig_Type()
)
cmDSL24HrRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxBig.setStatus("mandatory")
_CmDSL24HrRxAborts_Type = PerfTotalCount
_CmDSL24HrRxAborts_Object = MibTableColumn
cmDSL24HrRxAborts = _CmDSL24HrRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 5),
    _CmDSL24HrRxAborts_Type()
)
cmDSL24HrRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxAborts.setStatus("mandatory")
_CmDSL24HrRxAlignmentErrors_Type = PerfTotalCount
_CmDSL24HrRxAlignmentErrors_Object = MibTableColumn
cmDSL24HrRxAlignmentErrors = _CmDSL24HrRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 6),
    _CmDSL24HrRxAlignmentErrors_Type()
)
cmDSL24HrRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxAlignmentErrors.setStatus("mandatory")
_CmDSL24HrRxCRCErrors_Type = PerfTotalCount
_CmDSL24HrRxCRCErrors_Object = MibTableColumn
cmDSL24HrRxCRCErrors = _CmDSL24HrRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 7),
    _CmDSL24HrRxCRCErrors_Type()
)
cmDSL24HrRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxCRCErrors.setStatus("mandatory")
_CmDSL24HrRxOverruns_Type = PerfTotalCount
_CmDSL24HrRxOverruns_Object = MibTableColumn
cmDSL24HrRxOverruns = _CmDSL24HrRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 8),
    _CmDSL24HrRxOverruns_Type()
)
cmDSL24HrRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxOverruns.setStatus("mandatory")
_CmDSL24HrRxValidFrames_Type = PerfTotalCount
_CmDSL24HrRxValidFrames_Object = MibTableColumn
cmDSL24HrRxValidFrames = _CmDSL24HrRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 9),
    _CmDSL24HrRxValidFrames_Type()
)
cmDSL24HrRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxValidFrames.setStatus("mandatory")
_CmDSL24HrTxValidFrames_Type = PerfTotalCount
_CmDSL24HrTxValidFrames_Object = MibTableColumn
cmDSL24HrTxValidFrames = _CmDSL24HrTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 10),
    _CmDSL24HrTxValidFrames_Type()
)
cmDSL24HrTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrTxValidFrames.setStatus("mandatory")
_CmDSL24HrRxNoBuffers_Type = PerfTotalCount
_CmDSL24HrRxNoBuffers_Object = MibTableColumn
cmDSL24HrRxNoBuffers = _CmDSL24HrRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 11),
    _CmDSL24HrRxNoBuffers_Type()
)
cmDSL24HrRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxNoBuffers.setStatus("mandatory")
_CmDSL24HrMinNoiseMargin_Type = Integer32
_CmDSL24HrMinNoiseMargin_Object = MibTableColumn
cmDSL24HrMinNoiseMargin = _CmDSL24HrMinNoiseMargin_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 12),
    _CmDSL24HrMinNoiseMargin_Type()
)
cmDSL24HrMinNoiseMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrMinNoiseMargin.setStatus("mandatory")
_CmDSL24HrRxValidOctets_Type = PerfTotalCount
_CmDSL24HrRxValidOctets_Object = MibTableColumn
cmDSL24HrRxValidOctets = _CmDSL24HrRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 13),
    _CmDSL24HrRxValidOctets_Type()
)
cmDSL24HrRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrRxValidOctets.setStatus("mandatory")
_CmDSL24HrTxValidOctets_Type = PerfTotalCount
_CmDSL24HrTxValidOctets_Object = MibTableColumn
cmDSL24HrTxValidOctets = _CmDSL24HrTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 14),
    _CmDSL24HrTxValidOctets_Type()
)
cmDSL24HrTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrTxValidOctets.setStatus("mandatory")
_CmDSL24HrPortUpTime_Type = PerfTotalCount
_CmDSL24HrPortUpTime_Object = MibTableColumn
cmDSL24HrPortUpTime = _CmDSL24HrPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 5, 1, 15),
    _CmDSL24HrPortUpTime_Type()
)
cmDSL24HrPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDSL24HrPortUpTime.setStatus("mandatory")
_CmCpeDSLIntervalTable_Object = MibTable
cmCpeDSLIntervalTable = _CmCpeDSLIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6)
)
if mibBuilder.loadTexts:
    cmCpeDSLIntervalTable.setStatus("mandatory")
_CmCpeDSLIntervalEntry_Object = MibTableRow
cmCpeDSLIntervalEntry = _CmCpeDSLIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1)
)
cmCpeDSLIntervalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeDSLIntervalIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeDSLIntervalNumber"),
)
if mibBuilder.loadTexts:
    cmCpeDSLIntervalEntry.setStatus("mandatory")
_CmCpeDSLIntervalIndex_Type = Integer32
_CmCpeDSLIntervalIndex_Object = MibTableColumn
cmCpeDSLIntervalIndex = _CmCpeDSLIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 1),
    _CmCpeDSLIntervalIndex_Type()
)
cmCpeDSLIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalIndex.setStatus("mandatory")


class _CmCpeDSLIntervalNumber_Type(Integer32):
    """Custom type cmCpeDSLIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_CmCpeDSLIntervalNumber_Type.__name__ = "Integer32"
_CmCpeDSLIntervalNumber_Object = MibTableColumn
cmCpeDSLIntervalNumber = _CmCpeDSLIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 2),
    _CmCpeDSLIntervalNumber_Type()
)
cmCpeDSLIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalNumber.setStatus("mandatory")
_CmCpeDSLIntervalTxUnderruns_Type = Counter32
_CmCpeDSLIntervalTxUnderruns_Object = MibTableColumn
cmCpeDSLIntervalTxUnderruns = _CmCpeDSLIntervalTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 3),
    _CmCpeDSLIntervalTxUnderruns_Type()
)
cmCpeDSLIntervalTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalTxUnderruns.setStatus("mandatory")
_CmCpeDSLIntervalRxTruncated_Type = Counter32
_CmCpeDSLIntervalRxTruncated_Object = MibTableColumn
cmCpeDSLIntervalRxTruncated = _CmCpeDSLIntervalRxTruncated_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 4),
    _CmCpeDSLIntervalRxTruncated_Type()
)
cmCpeDSLIntervalRxTruncated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxTruncated.setStatus("mandatory")
_CmCpeDSLIntervalRxBig_Type = Counter32
_CmCpeDSLIntervalRxBig_Object = MibTableColumn
cmCpeDSLIntervalRxBig = _CmCpeDSLIntervalRxBig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 5),
    _CmCpeDSLIntervalRxBig_Type()
)
cmCpeDSLIntervalRxBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxBig.setStatus("mandatory")
_CmCpeDSLIntervalRxAborts_Type = Counter32
_CmCpeDSLIntervalRxAborts_Object = MibTableColumn
cmCpeDSLIntervalRxAborts = _CmCpeDSLIntervalRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 6),
    _CmCpeDSLIntervalRxAborts_Type()
)
cmCpeDSLIntervalRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxAborts.setStatus("mandatory")
_CmCpeDSLIntervalRxAlignmentErrors_Type = Counter32
_CmCpeDSLIntervalRxAlignmentErrors_Object = MibTableColumn
cmCpeDSLIntervalRxAlignmentErrors = _CmCpeDSLIntervalRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 7),
    _CmCpeDSLIntervalRxAlignmentErrors_Type()
)
cmCpeDSLIntervalRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxAlignmentErrors.setStatus("mandatory")
_CmCpeDSLIntervalRxCRCErrors_Type = Counter32
_CmCpeDSLIntervalRxCRCErrors_Object = MibTableColumn
cmCpeDSLIntervalRxCRCErrors = _CmCpeDSLIntervalRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 8),
    _CmCpeDSLIntervalRxCRCErrors_Type()
)
cmCpeDSLIntervalRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxCRCErrors.setStatus("mandatory")
_CmCpeDSLIntervalRxOverruns_Type = Counter32
_CmCpeDSLIntervalRxOverruns_Object = MibTableColumn
cmCpeDSLIntervalRxOverruns = _CmCpeDSLIntervalRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 9),
    _CmCpeDSLIntervalRxOverruns_Type()
)
cmCpeDSLIntervalRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxOverruns.setStatus("mandatory")
_CmCpeDSLIntervalRxValidFrames_Type = Counter32
_CmCpeDSLIntervalRxValidFrames_Object = MibTableColumn
cmCpeDSLIntervalRxValidFrames = _CmCpeDSLIntervalRxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 10),
    _CmCpeDSLIntervalRxValidFrames_Type()
)
cmCpeDSLIntervalRxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxValidFrames.setStatus("mandatory")
_CmCpeDSLIntervalTxValidFrames_Type = Counter32
_CmCpeDSLIntervalTxValidFrames_Object = MibTableColumn
cmCpeDSLIntervalTxValidFrames = _CmCpeDSLIntervalTxValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 11),
    _CmCpeDSLIntervalTxValidFrames_Type()
)
cmCpeDSLIntervalTxValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalTxValidFrames.setStatus("mandatory")
_CmCpeDSLIntervalRxNoBuffers_Type = Counter32
_CmCpeDSLIntervalRxNoBuffers_Object = MibTableColumn
cmCpeDSLIntervalRxNoBuffers = _CmCpeDSLIntervalRxNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 12),
    _CmCpeDSLIntervalRxNoBuffers_Type()
)
cmCpeDSLIntervalRxNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxNoBuffers.setStatus("mandatory")
_CmCpeDSLIntervalRxValidOctets_Type = Counter32
_CmCpeDSLIntervalRxValidOctets_Object = MibTableColumn
cmCpeDSLIntervalRxValidOctets = _CmCpeDSLIntervalRxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 13),
    _CmCpeDSLIntervalRxValidOctets_Type()
)
cmCpeDSLIntervalRxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalRxValidOctets.setStatus("mandatory")
_CmCpeDSLIntervalTxValidOctets_Type = Counter32
_CmCpeDSLIntervalTxValidOctets_Object = MibTableColumn
cmCpeDSLIntervalTxValidOctets = _CmCpeDSLIntervalTxValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 7, 6, 1, 14),
    _CmCpeDSLIntervalTxValidOctets_Type()
)
cmCpeDSLIntervalTxValidOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDSLIntervalTxValidOctets.setStatus("mandatory")
_CmIDSL_ObjectIdentity = ObjectIdentity
cmIDSL = _CmIDSL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8)
)
_CmIDSLModemTable_Object = MibTable
cmIDSLModemTable = _CmIDSLModemTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1)
)
if mibBuilder.loadTexts:
    cmIDSLModemTable.setStatus("mandatory")
_CmIDSLModemEntry_Object = MibTableRow
cmIDSLModemEntry = _CmIDSLModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1)
)
cmIDSLModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmIDSLModemEntry.setStatus("mandatory")
_CmIDSLModemIndex_Type = CmObjectPII
_CmIDSLModemIndex_Object = MibTableColumn
cmIDSLModemIndex = _CmIDSLModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 1),
    _CmIDSLModemIndex_Type()
)
cmIDSLModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemIndex.setStatus("mandatory")


class _CmIDSLModemOperState_Type(Integer32):
    """Custom type cmIDSLModemOperState based on Integer32"""
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


_CmIDSLModemOperState_Type.__name__ = "Integer32"
_CmIDSLModemOperState_Object = MibTableColumn
cmIDSLModemOperState = _CmIDSLModemOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 2),
    _CmIDSLModemOperState_Type()
)
cmIDSLModemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemOperState.setStatus("mandatory")


class _CmIDSLModemDataRate_Type(Integer32):
    """Custom type cmIDSLModemDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128,
              144)
        )
    )
    namedValues = NamedValues(
        *(("dr128Kbps", 128),
          ("dr144Kbps", 144),
          ("dr64Kbps", 64))
    )


_CmIDSLModemDataRate_Type.__name__ = "Integer32"
_CmIDSLModemDataRate_Object = MibTableColumn
cmIDSLModemDataRate = _CmIDSLModemDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 3),
    _CmIDSLModemDataRate_Type()
)
cmIDSLModemDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIDSLModemDataRate.setStatus("mandatory")


class _CmIDSLModemState_Type(Integer32):
    """Custom type cmIDSLModemState based on Integer32"""
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
        *(("activated", 4),
          ("activatedCpeDetected", 5),
          ("activating", 3),
          ("inactive", 2),
          ("none", 1))
    )


_CmIDSLModemState_Type.__name__ = "Integer32"
_CmIDSLModemState_Object = MibTableColumn
cmIDSLModemState = _CmIDSLModemState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 4),
    _CmIDSLModemState_Type()
)
cmIDSLModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemState.setStatus("mandatory")


class _CmIDSLModemTerminationMode_Type(Integer32):
    """Custom type cmIDSLModemTerminationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineTerminated", 1),
          ("networkTerminated", 2))
    )


_CmIDSLModemTerminationMode_Type.__name__ = "Integer32"
_CmIDSLModemTerminationMode_Object = MibTableColumn
cmIDSLModemTerminationMode = _CmIDSLModemTerminationMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 5),
    _CmIDSLModemTerminationMode_Type()
)
cmIDSLModemTerminationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemTerminationMode.setStatus("mandatory")
_CmIDSLModemCpeCode_Type = Integer32
_CmIDSLModemCpeCode_Object = MibTableColumn
cmIDSLModemCpeCode = _CmIDSLModemCpeCode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 6),
    _CmIDSLModemCpeCode_Type()
)
cmIDSLModemCpeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIDSLModemCpeCode.setStatus("mandatory")
_CmIDSLModemSuccessfulTrains_Type = Counter32
_CmIDSLModemSuccessfulTrains_Object = MibTableColumn
cmIDSLModemSuccessfulTrains = _CmIDSLModemSuccessfulTrains_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 7),
    _CmIDSLModemSuccessfulTrains_Type()
)
cmIDSLModemSuccessfulTrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemSuccessfulTrains.setStatus("mandatory")
_CmIDSLModemFailedTrainingAttempts_Type = Counter32
_CmIDSLModemFailedTrainingAttempts_Object = MibTableColumn
cmIDSLModemFailedTrainingAttempts = _CmIDSLModemFailedTrainingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 8),
    _CmIDSLModemFailedTrainingAttempts_Type()
)
cmIDSLModemFailedTrainingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemFailedTrainingAttempts.setStatus("mandatory")
_CmIDSLModemCpeResponses_Type = Counter32
_CmIDSLModemCpeResponses_Object = MibTableColumn
cmIDSLModemCpeResponses = _CmIDSLModemCpeResponses_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 9),
    _CmIDSLModemCpeResponses_Type()
)
cmIDSLModemCpeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemCpeResponses.setStatus("mandatory")


class _CmIDSLModemNetworkElements_Type(Integer32):
    """Custom type cmIDSLModemNetworkElements based on Integer32"""
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
        *(("cpeOnly", 7),
          ("fiveElements", 5),
          ("fourElements", 4),
          ("invalid", 9),
          ("oneElement", 1),
          ("sixElements", 6),
          ("threeElements", 3),
          ("twoElements", 2),
          ("unknown", 8))
    )


_CmIDSLModemNetworkElements_Type.__name__ = "Integer32"
_CmIDSLModemNetworkElements_Object = MibTableColumn
cmIDSLModemNetworkElements = _CmIDSLModemNetworkElements_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 10),
    _CmIDSLModemNetworkElements_Type()
)
cmIDSLModemNetworkElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLModemNetworkElements.setStatus("mandatory")
_CmIDSLModemActivationInterval_Type = Integer32
_CmIDSLModemActivationInterval_Object = MibTableColumn
cmIDSLModemActivationInterval = _CmIDSLModemActivationInterval_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 1, 1, 11),
    _CmIDSLModemActivationInterval_Type()
)
cmIDSLModemActivationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIDSLModemActivationInterval.setStatus("mandatory")
_CmCpeIDSLModemTable_Object = MibTable
cmCpeIDSLModemTable = _CmCpeIDSLModemTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2)
)
if mibBuilder.loadTexts:
    cmCpeIDSLModemTable.setStatus("mandatory")
_CmCpeIDSLModemEntry_Object = MibTableRow
cmCpeIDSLModemEntry = _CmCpeIDSLModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1)
)
cmCpeIDSLModemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmCpeIDSLModemEntry.setStatus("mandatory")
_CmCpeIDSLModemIndex_Type = CmObjectPII
_CmCpeIDSLModemIndex_Object = MibTableColumn
cmCpeIDSLModemIndex = _CmCpeIDSLModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1, 1),
    _CmCpeIDSLModemIndex_Type()
)
cmCpeIDSLModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeIDSLModemIndex.setStatus("mandatory")


class _CmCpeIDSLModemOperState_Type(Integer32):
    """Custom type cmCpeIDSLModemOperState based on Integer32"""
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


_CmCpeIDSLModemOperState_Type.__name__ = "Integer32"
_CmCpeIDSLModemOperState_Object = MibTableColumn
cmCpeIDSLModemOperState = _CmCpeIDSLModemOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1, 2),
    _CmCpeIDSLModemOperState_Type()
)
cmCpeIDSLModemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeIDSLModemOperState.setStatus("mandatory")


class _CmCpeIDSLModemDataRate_Type(Integer32):
    """Custom type cmCpeIDSLModemDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              128,
              144)
        )
    )
    namedValues = NamedValues(
        *(("dr128Kbps", 128),
          ("dr144Kbps", 144),
          ("dr64Kbps", 64))
    )


_CmCpeIDSLModemDataRate_Type.__name__ = "Integer32"
_CmCpeIDSLModemDataRate_Object = MibTableColumn
cmCpeIDSLModemDataRate = _CmCpeIDSLModemDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1, 3),
    _CmCpeIDSLModemDataRate_Type()
)
cmCpeIDSLModemDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeIDSLModemDataRate.setStatus("mandatory")


class _CmCpeIDSLModemState_Type(Integer32):
    """Custom type cmCpeIDSLModemState based on Integer32"""
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
        *(("activated", 4),
          ("activating", 3),
          ("active", 2),
          ("none", 1))
    )


_CmCpeIDSLModemState_Type.__name__ = "Integer32"
_CmCpeIDSLModemState_Object = MibTableColumn
cmCpeIDSLModemState = _CmCpeIDSLModemState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1, 4),
    _CmCpeIDSLModemState_Type()
)
cmCpeIDSLModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeIDSLModemState.setStatus("mandatory")


class _CmCpeIDSLModemTerminationMode_Type(Integer32):
    """Custom type cmCpeIDSLModemTerminationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lineTerminated", 1),
          ("networkTerminated", 2))
    )


_CmCpeIDSLModemTerminationMode_Type.__name__ = "Integer32"
_CmCpeIDSLModemTerminationMode_Object = MibTableColumn
cmCpeIDSLModemTerminationMode = _CmCpeIDSLModemTerminationMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 8, 2, 1, 5),
    _CmCpeIDSLModemTerminationMode_Type()
)
cmCpeIDSLModemTerminationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeIDSLModemTerminationMode.setStatus("mandatory")
_CmFrameRelay_ObjectIdentity = ObjectIdentity
cmFrameRelay = _CmFrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9)
)
_CmFrDlcmiTable_Object = MibTable
cmFrDlcmiTable = _CmFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1)
)
if mibBuilder.loadTexts:
    cmFrDlcmiTable.setStatus("mandatory")
_CmFrDlcmiEntry_Object = MibTableRow
cmFrDlcmiEntry = _CmFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1)
)
cmFrDlcmiEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    cmFrDlcmiEntry.setStatus("mandatory")
_CmFrDlcmiIfIndex_Type = CmObjectPII
_CmFrDlcmiIfIndex_Object = MibTableColumn
cmFrDlcmiIfIndex = _CmFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 1),
    _CmFrDlcmiIfIndex_Type()
)
cmFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiIfIndex.setStatus("mandatory")


class _CmFrDlcmiAdminState_Type(Integer32):
    """Custom type cmFrDlcmiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmFrDlcmiAdminState_Type.__name__ = "Integer32"
_CmFrDlcmiAdminState_Object = MibTableColumn
cmFrDlcmiAdminState = _CmFrDlcmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 2),
    _CmFrDlcmiAdminState_Type()
)
cmFrDlcmiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFrDlcmiAdminState.setStatus("mandatory")


class _CmFrDlcmiOperState_Type(Integer32):
    """Custom type cmFrDlcmiOperState based on Integer32"""
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


_CmFrDlcmiOperState_Type.__name__ = "Integer32"
_CmFrDlcmiOperState_Object = MibTableColumn
cmFrDlcmiOperState = _CmFrDlcmiOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 3),
    _CmFrDlcmiOperState_Type()
)
cmFrDlcmiOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiOperState.setStatus("mandatory")


class _CmFrDlcmiFirstDLCI_Type(Integer32):
    """Custom type cmFrDlcmiFirstDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 991),
    )


_CmFrDlcmiFirstDLCI_Type.__name__ = "Integer32"
_CmFrDlcmiFirstDLCI_Object = MibTableColumn
cmFrDlcmiFirstDLCI = _CmFrDlcmiFirstDLCI_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 4),
    _CmFrDlcmiFirstDLCI_Type()
)
cmFrDlcmiFirstDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiFirstDLCI.setStatus("mandatory")


class _CmFrDlcmiLMIMode_Type(Integer32):
    """Custom type cmFrDlcmiLMIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("nni", 3))
    )


_CmFrDlcmiLMIMode_Type.__name__ = "Integer32"
_CmFrDlcmiLMIMode_Object = MibTableColumn
cmFrDlcmiLMIMode = _CmFrDlcmiLMIMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 5),
    _CmFrDlcmiLMIMode_Type()
)
cmFrDlcmiLMIMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFrDlcmiLMIMode.setStatus("mandatory")


class _CmFrDlcmiDceN392_Type(Integer32):
    """Custom type cmFrDlcmiDceN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmFrDlcmiDceN392_Type.__name__ = "Integer32"
_CmFrDlcmiDceN392_Object = MibTableColumn
cmFrDlcmiDceN392 = _CmFrDlcmiDceN392_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 6),
    _CmFrDlcmiDceN392_Type()
)
cmFrDlcmiDceN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFrDlcmiDceN392.setStatus("mandatory")


class _CmFrDlcmiDceN393_Type(Integer32):
    """Custom type cmFrDlcmiDceN393 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CmFrDlcmiDceN393_Type.__name__ = "Integer32"
_CmFrDlcmiDceN393_Object = MibTableColumn
cmFrDlcmiDceN393 = _CmFrDlcmiDceN393_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 7),
    _CmFrDlcmiDceN393_Type()
)
cmFrDlcmiDceN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFrDlcmiDceN393.setStatus("mandatory")


class _CmFrDlcmiDceT392_Type(Integer32):
    """Custom type cmFrDlcmiDceT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_CmFrDlcmiDceT392_Type.__name__ = "Integer32"
_CmFrDlcmiDceT392_Object = MibTableColumn
cmFrDlcmiDceT392 = _CmFrDlcmiDceT392_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 8),
    _CmFrDlcmiDceT392_Type()
)
cmFrDlcmiDceT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFrDlcmiDceT392.setStatus("mandatory")
_CmFrDlcmiRcvUnknownDLCI_Type = Counter32
_CmFrDlcmiRcvUnknownDLCI_Object = MibTableColumn
cmFrDlcmiRcvUnknownDLCI = _CmFrDlcmiRcvUnknownDLCI_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 10),
    _CmFrDlcmiRcvUnknownDLCI_Type()
)
cmFrDlcmiRcvUnknownDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiRcvUnknownDLCI.setStatus("mandatory")
_CmFrDlcmiLMITxStatusEnquiries_Type = Counter32
_CmFrDlcmiLMITxStatusEnquiries_Object = MibTableColumn
cmFrDlcmiLMITxStatusEnquiries = _CmFrDlcmiLMITxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 11),
    _CmFrDlcmiLMITxStatusEnquiries_Type()
)
cmFrDlcmiLMITxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLMITxStatusEnquiries.setStatus("mandatory")
_CmFrDlcmiLMITxStatusResponses_Type = Counter32
_CmFrDlcmiLMITxStatusResponses_Object = MibTableColumn
cmFrDlcmiLMITxStatusResponses = _CmFrDlcmiLMITxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 12),
    _CmFrDlcmiLMITxStatusResponses_Type()
)
cmFrDlcmiLMITxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLMITxStatusResponses.setStatus("mandatory")
_CmFrDlcmiLMIRxStatusEnquiries_Type = Counter32
_CmFrDlcmiLMIRxStatusEnquiries_Object = MibTableColumn
cmFrDlcmiLMIRxStatusEnquiries = _CmFrDlcmiLMIRxStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 13),
    _CmFrDlcmiLMIRxStatusEnquiries_Type()
)
cmFrDlcmiLMIRxStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLMIRxStatusEnquiries.setStatus("mandatory")
_CmFrDlcmiLMIRxStatusResponses_Type = Counter32
_CmFrDlcmiLMIRxStatusResponses_Object = MibTableColumn
cmFrDlcmiLMIRxStatusResponses = _CmFrDlcmiLMIRxStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 14),
    _CmFrDlcmiLMIRxStatusResponses_Type()
)
cmFrDlcmiLMIRxStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLMIRxStatusResponses.setStatus("mandatory")
_CmFrDlcmiLMIRxUpdates_Type = Counter32
_CmFrDlcmiLMIRxUpdates_Object = MibTableColumn
cmFrDlcmiLMIRxUpdates = _CmFrDlcmiLMIRxUpdates_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 15),
    _CmFrDlcmiLMIRxUpdates_Type()
)
cmFrDlcmiLMIRxUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLMIRxUpdates.setStatus("mandatory")
_CmFrDlcmiUnknownLMIMessagesRcvd_Type = Counter32
_CmFrDlcmiUnknownLMIMessagesRcvd_Object = MibTableColumn
cmFrDlcmiUnknownLMIMessagesRcvd = _CmFrDlcmiUnknownLMIMessagesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 16),
    _CmFrDlcmiUnknownLMIMessagesRcvd_Type()
)
cmFrDlcmiUnknownLMIMessagesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiUnknownLMIMessagesRcvd.setStatus("mandatory")
_CmFrDlcmiLostLMISequences_Type = Counter32
_CmFrDlcmiLostLMISequences_Object = MibTableColumn
cmFrDlcmiLostLMISequences = _CmFrDlcmiLostLMISequences_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 1, 1, 17),
    _CmFrDlcmiLostLMISequences_Type()
)
cmFrDlcmiLostLMISequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrDlcmiLostLMISequences.setStatus("mandatory")
_CmFrCircuitTable_Object = MibTable
cmFrCircuitTable = _CmFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2)
)
if mibBuilder.loadTexts:
    cmFrCircuitTable.setStatus("mandatory")
_CmFrCircuitEntry_Object = MibTableRow
cmFrCircuitEntry = _CmFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1)
)
cmFrCircuitEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmFrCircuitIfIndex"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    cmFrCircuitEntry.setStatus("mandatory")
_CmFrCircuitIfIndex_Type = CmObjectPII
_CmFrCircuitIfIndex_Object = MibTableColumn
cmFrCircuitIfIndex = _CmFrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 1),
    _CmFrCircuitIfIndex_Type()
)
cmFrCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitIfIndex.setStatus("mandatory")
_CmFrCircuitDlci_Type = DLCI
_CmFrCircuitDlci_Object = MibTableColumn
cmFrCircuitDlci = _CmFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 2),
    _CmFrCircuitDlci_Type()
)
cmFrCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitDlci.setStatus("mandatory")


class _CmFrCircuitOperState_Type(Integer32):
    """Custom type cmFrCircuitOperState based on Integer32"""
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


_CmFrCircuitOperState_Type.__name__ = "Integer32"
_CmFrCircuitOperState_Object = MibTableColumn
cmFrCircuitOperState = _CmFrCircuitOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 3),
    _CmFrCircuitOperState_Type()
)
cmFrCircuitOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitOperState.setStatus("mandatory")
_CmFrCircuitFramesDroppedTxUnavail_Type = Counter32
_CmFrCircuitFramesDroppedTxUnavail_Object = MibTableColumn
cmFrCircuitFramesDroppedTxUnavail = _CmFrCircuitFramesDroppedTxUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 4),
    _CmFrCircuitFramesDroppedTxUnavail_Type()
)
cmFrCircuitFramesDroppedTxUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitFramesDroppedTxUnavail.setStatus("mandatory")
_CmFrCircuitFramesDroppedRxUnavail_Type = Counter32
_CmFrCircuitFramesDroppedRxUnavail_Object = MibTableColumn
cmFrCircuitFramesDroppedRxUnavail = _CmFrCircuitFramesDroppedRxUnavail_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 5),
    _CmFrCircuitFramesDroppedRxUnavail_Type()
)
cmFrCircuitFramesDroppedRxUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitFramesDroppedRxUnavail.setStatus("mandatory")
_CmFrCircuitFramesDroppedExcess_Type = Counter32
_CmFrCircuitFramesDroppedExcess_Object = MibTableColumn
cmFrCircuitFramesDroppedExcess = _CmFrCircuitFramesDroppedExcess_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 9, 2, 1, 6),
    _CmFrCircuitFramesDroppedExcess_Type()
)
cmFrCircuitFramesDroppedExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFrCircuitFramesDroppedExcess.setStatus("mandatory")
_CmATM_ObjectIdentity = ObjectIdentity
cmATM = _CmATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10)
)
_CmAtmVclTable_Object = MibTable
cmAtmVclTable = _CmAtmVclTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1)
)
if mibBuilder.loadTexts:
    cmAtmVclTable.setStatus("mandatory")
_CmAtmVclEntry_Object = MibTableRow
cmAtmVclEntry = _CmAtmVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1)
)
cmAtmVclEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAtmVclPII"),
)
if mibBuilder.loadTexts:
    cmAtmVclEntry.setStatus("mandatory")
_CmAtmVclPII_Type = CmObjectPII
_CmAtmVclPII_Object = MibTableColumn
cmAtmVclPII = _CmAtmVclPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 1),
    _CmAtmVclPII_Type()
)
cmAtmVclPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclPII.setStatus("mandatory")
_CmAtmVclVpi_Type = Integer32
_CmAtmVclVpi_Object = MibTableColumn
cmAtmVclVpi = _CmAtmVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 2),
    _CmAtmVclVpi_Type()
)
cmAtmVclVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAtmVclVpi.setStatus("mandatory")
_CmAtmVclVci_Type = Integer32
_CmAtmVclVci_Object = MibTableColumn
cmAtmVclVci = _CmAtmVclVci_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 3),
    _CmAtmVclVci_Type()
)
cmAtmVclVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAtmVclVci.setStatus("mandatory")


class _CmAtmVclAdminStatus_Type(Integer32):
    """Custom type cmAtmVclAdminStatus based on Integer32"""
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


_CmAtmVclAdminStatus_Type.__name__ = "Integer32"
_CmAtmVclAdminStatus_Object = MibTableColumn
cmAtmVclAdminStatus = _CmAtmVclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 4),
    _CmAtmVclAdminStatus_Type()
)
cmAtmVclAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAtmVclAdminStatus.setStatus("mandatory")


class _CmAtmVclOperStatus_Type(Integer32):
    """Custom type cmAtmVclOperStatus based on Integer32"""
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


_CmAtmVclOperStatus_Type.__name__ = "Integer32"
_CmAtmVclOperStatus_Object = MibTableColumn
cmAtmVclOperStatus = _CmAtmVclOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 5),
    _CmAtmVclOperStatus_Type()
)
cmAtmVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclOperStatus.setStatus("mandatory")
_CmAtmVclLastChange_Type = TimeTicks
_CmAtmVclLastChange_Object = MibTableColumn
cmAtmVclLastChange = _CmAtmVclLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 6),
    _CmAtmVclLastChange_Type()
)
cmAtmVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclLastChange.setStatus("mandatory")


class _CmAtmVclAalType_Type(Integer32):
    """Custom type cmAtmVclAalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("aal5", 3)
    )


_CmAtmVclAalType_Type.__name__ = "Integer32"
_CmAtmVclAalType_Object = MibTableColumn
cmAtmVclAalType = _CmAtmVclAalType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 7),
    _CmAtmVclAalType_Type()
)
cmAtmVclAalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclAalType.setStatus("mandatory")
_CmAtmVclAal5CpcsTransmitSduSize_Type = Integer32
_CmAtmVclAal5CpcsTransmitSduSize_Object = MibTableColumn
cmAtmVclAal5CpcsTransmitSduSize = _CmAtmVclAal5CpcsTransmitSduSize_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 8),
    _CmAtmVclAal5CpcsTransmitSduSize_Type()
)
cmAtmVclAal5CpcsTransmitSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclAal5CpcsTransmitSduSize.setStatus("mandatory")
_CmAtmVclAal5CpcsReceiveSduSize_Type = Integer32
_CmAtmVclAal5CpcsReceiveSduSize_Object = MibTableColumn
cmAtmVclAal5CpcsReceiveSduSize = _CmAtmVclAal5CpcsReceiveSduSize_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 9),
    _CmAtmVclAal5CpcsReceiveSduSize_Type()
)
cmAtmVclAal5CpcsReceiveSduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAtmVclAal5CpcsReceiveSduSize.setStatus("mandatory")


class _CmAtmVclRowStatus_Type(Integer32):
    """Custom type cmAtmVclRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_CmAtmVclRowStatus_Type.__name__ = "Integer32"
_CmAtmVclRowStatus_Object = MibTableColumn
cmAtmVclRowStatus = _CmAtmVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 1, 1, 10),
    _CmAtmVclRowStatus_Type()
)
cmAtmVclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAtmVclRowStatus.setStatus("mandatory")
_CmDS3AtmTable_Object = MibTable
cmDS3AtmTable = _CmDS3AtmTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2)
)
if mibBuilder.loadTexts:
    cmDS3AtmTable.setStatus("mandatory")
_CmDS3AtmEntry_Object = MibTableRow
cmDS3AtmEntry = _CmDS3AtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2, 1)
)
cmDS3AtmEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDS3AtmPII"),
)
if mibBuilder.loadTexts:
    cmDS3AtmEntry.setStatus("mandatory")
_CmDS3AtmPII_Type = CmObjectPII
_CmDS3AtmPII_Object = MibTableColumn
cmDS3AtmPII = _CmDS3AtmPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2, 1, 1),
    _CmDS3AtmPII_Type()
)
cmDS3AtmPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDS3AtmPII.setStatus("mandatory")


class _CmDS3AtmCbitParityEnable_Type(Integer32):
    """Custom type cmDS3AtmCbitParityEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CmDS3AtmCbitParityEnable_Type.__name__ = "Integer32"
_CmDS3AtmCbitParityEnable_Object = MibTableColumn
cmDS3AtmCbitParityEnable = _CmDS3AtmCbitParityEnable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2, 1, 2),
    _CmDS3AtmCbitParityEnable_Type()
)
cmDS3AtmCbitParityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDS3AtmCbitParityEnable.setStatus("mandatory")


class _CmDS3AtmCellPayloadScrambling_Type(Integer32):
    """Custom type cmDS3AtmCellPayloadScrambling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CmDS3AtmCellPayloadScrambling_Type.__name__ = "Integer32"
_CmDS3AtmCellPayloadScrambling_Object = MibTableColumn
cmDS3AtmCellPayloadScrambling = _CmDS3AtmCellPayloadScrambling_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2, 1, 3),
    _CmDS3AtmCellPayloadScrambling_Type()
)
cmDS3AtmCellPayloadScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDS3AtmCellPayloadScrambling.setStatus("mandatory")


class _CmDS3AtmCellMapping_Type(Integer32):
    """Custom type cmDS3AtmCellMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hec", 2),
          ("plcp", 1))
    )


_CmDS3AtmCellMapping_Type.__name__ = "Integer32"
_CmDS3AtmCellMapping_Object = MibTableColumn
cmDS3AtmCellMapping = _CmDS3AtmCellMapping_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 10, 2, 1, 4),
    _CmDS3AtmCellMapping_Type()
)
cmDS3AtmCellMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDS3AtmCellMapping.setStatus("mandatory")
_CmIMUX_ObjectIdentity = ObjectIdentity
cmIMUX = _CmIMUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11)
)
_CmBundleTable_Object = MibTable
cmBundleTable = _CmBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1)
)
if mibBuilder.loadTexts:
    cmBundleTable.setStatus("mandatory")
_CmBundleEntry_Object = MibTableRow
cmBundleEntry = _CmBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1)
)
cmBundleEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBundlePII"),
)
if mibBuilder.loadTexts:
    cmBundleEntry.setStatus("mandatory")
_CmBundlePII_Type = CmObjectPII
_CmBundlePII_Object = MibTableColumn
cmBundlePII = _CmBundlePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 1),
    _CmBundlePII_Type()
)
cmBundlePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundlePII.setStatus("mandatory")


class _CmBundleRowStatus_Type(Integer32):
    """Custom type cmBundleRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_CmBundleRowStatus_Type.__name__ = "Integer32"
_CmBundleRowStatus_Object = MibTableColumn
cmBundleRowStatus = _CmBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 2),
    _CmBundleRowStatus_Type()
)
cmBundleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBundleRowStatus.setStatus("mandatory")


class _CmBundleMember1PII_Type(CmObjectPII):
    """Custom type cmBundleMember1PII based on CmObjectPII"""
    defaultValue = 0


_CmBundleMember1PII_Object = MibTableColumn
cmBundleMember1PII = _CmBundleMember1PII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 3),
    _CmBundleMember1PII_Type()
)
cmBundleMember1PII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBundleMember1PII.setStatus("mandatory")
_CmBundleMember1EndPointID_Type = OctetString
_CmBundleMember1EndPointID_Object = MibTableColumn
cmBundleMember1EndPointID = _CmBundleMember1EndPointID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 4),
    _CmBundleMember1EndPointID_Type()
)
cmBundleMember1EndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember1EndPointID.setStatus("mandatory")


class _CmBundleMember1Status_Type(Integer32):
    """Custom type cmBundleMember1Status based on Integer32"""
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
        *(("active", 2),
          ("none", 1),
          ("waitForAdd", 3))
    )


_CmBundleMember1Status_Type.__name__ = "Integer32"
_CmBundleMember1Status_Object = MibTableColumn
cmBundleMember1Status = _CmBundleMember1Status_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 5),
    _CmBundleMember1Status_Type()
)
cmBundleMember1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember1Status.setStatus("mandatory")


class _CmBundleMember2PII_Type(CmObjectPII):
    """Custom type cmBundleMember2PII based on CmObjectPII"""
    defaultValue = 0


_CmBundleMember2PII_Object = MibTableColumn
cmBundleMember2PII = _CmBundleMember2PII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 6),
    _CmBundleMember2PII_Type()
)
cmBundleMember2PII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBundleMember2PII.setStatus("mandatory")
_CmBundleMember2EndPointID_Type = OctetString
_CmBundleMember2EndPointID_Object = MibTableColumn
cmBundleMember2EndPointID = _CmBundleMember2EndPointID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 7),
    _CmBundleMember2EndPointID_Type()
)
cmBundleMember2EndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember2EndPointID.setStatus("mandatory")


class _CmBundleMember2Status_Type(Integer32):
    """Custom type cmBundleMember2Status based on Integer32"""
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
        *(("active", 2),
          ("none", 1),
          ("waitForAdd", 3))
    )


_CmBundleMember2Status_Type.__name__ = "Integer32"
_CmBundleMember2Status_Object = MibTableColumn
cmBundleMember2Status = _CmBundleMember2Status_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 8),
    _CmBundleMember2Status_Type()
)
cmBundleMember2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember2Status.setStatus("mandatory")


class _CmBundleMember3PII_Type(CmObjectPII):
    """Custom type cmBundleMember3PII based on CmObjectPII"""
    defaultValue = 0


_CmBundleMember3PII_Object = MibTableColumn
cmBundleMember3PII = _CmBundleMember3PII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 9),
    _CmBundleMember3PII_Type()
)
cmBundleMember3PII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBundleMember3PII.setStatus("mandatory")
_CmBundleMember3EndPointID_Type = OctetString
_CmBundleMember3EndPointID_Object = MibTableColumn
cmBundleMember3EndPointID = _CmBundleMember3EndPointID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 10),
    _CmBundleMember3EndPointID_Type()
)
cmBundleMember3EndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember3EndPointID.setStatus("mandatory")


class _CmBundleMember3Status_Type(Integer32):
    """Custom type cmBundleMember3Status based on Integer32"""
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
        *(("active", 2),
          ("none", 1),
          ("waitForAdd", 3))
    )


_CmBundleMember3Status_Type.__name__ = "Integer32"
_CmBundleMember3Status_Object = MibTableColumn
cmBundleMember3Status = _CmBundleMember3Status_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 11),
    _CmBundleMember3Status_Type()
)
cmBundleMember3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember3Status.setStatus("mandatory")


class _CmBundleMember4PII_Type(CmObjectPII):
    """Custom type cmBundleMember4PII based on CmObjectPII"""
    defaultValue = 0


_CmBundleMember4PII_Object = MibTableColumn
cmBundleMember4PII = _CmBundleMember4PII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 12),
    _CmBundleMember4PII_Type()
)
cmBundleMember4PII.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBundleMember4PII.setStatus("mandatory")
_CmBundleMember4EndPointID_Type = OctetString
_CmBundleMember4EndPointID_Object = MibTableColumn
cmBundleMember4EndPointID = _CmBundleMember4EndPointID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 13),
    _CmBundleMember4EndPointID_Type()
)
cmBundleMember4EndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember4EndPointID.setStatus("mandatory")


class _CmBundleMember4Status_Type(Integer32):
    """Custom type cmBundleMember4Status based on Integer32"""
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
        *(("active", 2),
          ("none", 1),
          ("waitForAdd", 3))
    )


_CmBundleMember4Status_Type.__name__ = "Integer32"
_CmBundleMember4Status_Object = MibTableColumn
cmBundleMember4Status = _CmBundleMember4Status_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 11, 1, 1, 14),
    _CmBundleMember4Status_Type()
)
cmBundleMember4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBundleMember4Status.setStatus("mandatory")
_CmDataPort_ObjectIdentity = ObjectIdentity
cmDataPort = _CmDataPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12)
)
_CmCpeDataPortTable_Object = MibTable
cmCpeDataPortTable = _CmCpeDataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1)
)
if mibBuilder.loadTexts:
    cmCpeDataPortTable.setStatus("mandatory")
_CmCpeDataPortEntry_Object = MibTableRow
cmCpeDataPortEntry = _CmCpeDataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1)
)
cmCpeDataPortEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeDataPortIndex"),
)
if mibBuilder.loadTexts:
    cmCpeDataPortEntry.setStatus("mandatory")
_CmCpeDataPortIndex_Type = CmObjectPII
_CmCpeDataPortIndex_Object = MibTableColumn
cmCpeDataPortIndex = _CmCpeDataPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 1),
    _CmCpeDataPortIndex_Type()
)
cmCpeDataPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIndex.setStatus("mandatory")


class _CmCpeDataPortType_Type(Integer32):
    """Custom type cmCpeDataPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eia-530", 1),
          ("unknown", 3),
          ("v35", 2))
    )


_CmCpeDataPortType_Type.__name__ = "Integer32"
_CmCpeDataPortType_Object = MibTableColumn
cmCpeDataPortType = _CmCpeDataPortType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 2),
    _CmCpeDataPortType_Type()
)
cmCpeDataPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortType.setStatus("mandatory")


class _CmCpeDataPortForceDSR_Type(Integer32):
    """Custom type cmCpeDataPortForceDSR based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmCpeDataPortForceDSR_Type.__name__ = "Integer32"
_CmCpeDataPortForceDSR_Object = MibTableColumn
cmCpeDataPortForceDSR = _CmCpeDataPortForceDSR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 3),
    _CmCpeDataPortForceDSR_Type()
)
cmCpeDataPortForceDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortForceDSR.setStatus("mandatory")


class _CmCpeDataPortIgnoreDTR_Type(Integer32):
    """Custom type cmCpeDataPortIgnoreDTR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmCpeDataPortIgnoreDTR_Type.__name__ = "Integer32"
_CmCpeDataPortIgnoreDTR_Object = MibTableColumn
cmCpeDataPortIgnoreDTR = _CmCpeDataPortIgnoreDTR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 4),
    _CmCpeDataPortIgnoreDTR_Type()
)
cmCpeDataPortIgnoreDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortIgnoreDTR.setStatus("mandatory")


class _CmCpeDataPortIgnoreRTS_Type(Integer32):
    """Custom type cmCpeDataPortIgnoreRTS based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmCpeDataPortIgnoreRTS_Type.__name__ = "Integer32"
_CmCpeDataPortIgnoreRTS_Object = MibTableColumn
cmCpeDataPortIgnoreRTS = _CmCpeDataPortIgnoreRTS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 5),
    _CmCpeDataPortIgnoreRTS_Type()
)
cmCpeDataPortIgnoreRTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortIgnoreRTS.setStatus("mandatory")


class _CmCpeDataPortTerminalTiming_Type(Integer32):
    """Custom type cmCpeDataPortTerminalTiming based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmCpeDataPortTerminalTiming_Type.__name__ = "Integer32"
_CmCpeDataPortTerminalTiming_Object = MibTableColumn
cmCpeDataPortTerminalTiming = _CmCpeDataPortTerminalTiming_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 6),
    _CmCpeDataPortTerminalTiming_Type()
)
cmCpeDataPortTerminalTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortTerminalTiming.setStatus("mandatory")


class _CmCpeDataPortTM_Type(Integer32):
    """Custom type cmCpeDataPortTM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortTM_Type.__name__ = "Integer32"
_CmCpeDataPortTM_Object = MibTableColumn
cmCpeDataPortTM = _CmCpeDataPortTM_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 7),
    _CmCpeDataPortTM_Type()
)
cmCpeDataPortTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTM.setStatus("mandatory")


class _CmCpeDataPortLL_Type(Integer32):
    """Custom type cmCpeDataPortLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortLL_Type.__name__ = "Integer32"
_CmCpeDataPortLL_Object = MibTableColumn
cmCpeDataPortLL = _CmCpeDataPortLL_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 8),
    _CmCpeDataPortLL_Type()
)
cmCpeDataPortLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortLL.setStatus("mandatory")


class _CmCpeDataPortRL_Type(Integer32):
    """Custom type cmCpeDataPortRL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortRL_Type.__name__ = "Integer32"
_CmCpeDataPortRL_Object = MibTableColumn
cmCpeDataPortRL = _CmCpeDataPortRL_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 9),
    _CmCpeDataPortRL_Type()
)
cmCpeDataPortRL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortRL.setStatus("mandatory")


class _CmCpeDataPortDTR_Type(Integer32):
    """Custom type cmCpeDataPortDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortDTR_Type.__name__ = "Integer32"
_CmCpeDataPortDTR_Object = MibTableColumn
cmCpeDataPortDTR = _CmCpeDataPortDTR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 10),
    _CmCpeDataPortDTR_Type()
)
cmCpeDataPortDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortDTR.setStatus("mandatory")


class _CmCpeDataPortRTS_Type(Integer32):
    """Custom type cmCpeDataPortRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortRTS_Type.__name__ = "Integer32"
_CmCpeDataPortRTS_Object = MibTableColumn
cmCpeDataPortRTS = _CmCpeDataPortRTS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 11),
    _CmCpeDataPortRTS_Type()
)
cmCpeDataPortRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortRTS.setStatus("mandatory")


class _CmCpeDataPortDSR_Type(Integer32):
    """Custom type cmCpeDataPortDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortDSR_Type.__name__ = "Integer32"
_CmCpeDataPortDSR_Object = MibTableColumn
cmCpeDataPortDSR = _CmCpeDataPortDSR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 12),
    _CmCpeDataPortDSR_Type()
)
cmCpeDataPortDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortDSR.setStatus("mandatory")


class _CmCpeDataPortCTS_Type(Integer32):
    """Custom type cmCpeDataPortCTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortCTS_Type.__name__ = "Integer32"
_CmCpeDataPortCTS_Object = MibTableColumn
cmCpeDataPortCTS = _CmCpeDataPortCTS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 13),
    _CmCpeDataPortCTS_Type()
)
cmCpeDataPortCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortCTS.setStatus("mandatory")


class _CmCpeDataPortDCD_Type(Integer32):
    """Custom type cmCpeDataPortDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmCpeDataPortDCD_Type.__name__ = "Integer32"
_CmCpeDataPortDCD_Object = MibTableColumn
cmCpeDataPortDCD = _CmCpeDataPortDCD_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 14),
    _CmCpeDataPortDCD_Type()
)
cmCpeDataPortDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortDCD.setStatus("mandatory")


class _CmCpeDataPortTxClockSource_Type(Integer32):
    """Custom type cmCpeDataPortTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2))
    )


_CmCpeDataPortTxClockSource_Type.__name__ = "Integer32"
_CmCpeDataPortTxClockSource_Object = MibTableColumn
cmCpeDataPortTxClockSource = _CmCpeDataPortTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 15),
    _CmCpeDataPortTxClockSource_Type()
)
cmCpeDataPortTxClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTxClockSource.setStatus("mandatory")


class _CmCpeDataPortDTEDCE_Type(Integer32):
    """Custom type cmCpeDataPortDTEDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_CmCpeDataPortDTEDCE_Type.__name__ = "Integer32"
_CmCpeDataPortDTEDCE_Object = MibTableColumn
cmCpeDataPortDTEDCE = _CmCpeDataPortDTEDCE_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 16),
    _CmCpeDataPortDTEDCE_Type()
)
cmCpeDataPortDTEDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortDTEDCE.setStatus("mandatory")


class _CmCpeDataPortCRC_Type(Integer32):
    """Custom type cmCpeDataPortCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("crc-ccitt", 1)
    )


_CmCpeDataPortCRC_Type.__name__ = "Integer32"
_CmCpeDataPortCRC_Object = MibTableColumn
cmCpeDataPortCRC = _CmCpeDataPortCRC_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 17),
    _CmCpeDataPortCRC_Type()
)
cmCpeDataPortCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortCRC.setStatus("mandatory")


class _CmCpeDataPortClockRate_Type(Integer32):
    """Custom type cmCpeDataPortClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3136000),
    )


_CmCpeDataPortClockRate_Type.__name__ = "Integer32"
_CmCpeDataPortClockRate_Object = MibTableColumn
cmCpeDataPortClockRate = _CmCpeDataPortClockRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 18),
    _CmCpeDataPortClockRate_Type()
)
cmCpeDataPortClockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortClockRate.setStatus("mandatory")


class _CmCpeDataPortAdminState_Type(Integer32):
    """Custom type cmCpeDataPortAdminState based on Integer32"""
    defaultValue = 2

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


_CmCpeDataPortAdminState_Type.__name__ = "Integer32"
_CmCpeDataPortAdminState_Object = MibTableColumn
cmCpeDataPortAdminState = _CmCpeDataPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 19),
    _CmCpeDataPortAdminState_Type()
)
cmCpeDataPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortAdminState.setStatus("mandatory")


class _CmCpeDataPortOperState_Type(Integer32):
    """Custom type cmCpeDataPortOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("testing", 3))
    )


_CmCpeDataPortOperState_Type.__name__ = "Integer32"
_CmCpeDataPortOperState_Object = MibTableColumn
cmCpeDataPortOperState = _CmCpeDataPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 20),
    _CmCpeDataPortOperState_Type()
)
cmCpeDataPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortOperState.setStatus("mandatory")


class _CmCpeDataPortLoopbackConfig_Type(Integer32):
    """Custom type cmCpeDataPortLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLoop", 2),
          ("noLoop", 1))
    )


_CmCpeDataPortLoopbackConfig_Type.__name__ = "Integer32"
_CmCpeDataPortLoopbackConfig_Object = MibTableColumn
cmCpeDataPortLoopbackConfig = _CmCpeDataPortLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 21),
    _CmCpeDataPortLoopbackConfig_Type()
)
cmCpeDataPortLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeDataPortLoopbackConfig.setStatus("mandatory")


class _CmCpeDataPortLoopbackStatus_Type(Integer32):
    """Custom type cmCpeDataPortLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLoop", 2),
          ("noLoop", 1))
    )


_CmCpeDataPortLoopbackStatus_Type.__name__ = "Integer32"
_CmCpeDataPortLoopbackStatus_Object = MibTableColumn
cmCpeDataPortLoopbackStatus = _CmCpeDataPortLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 1, 1, 22),
    _CmCpeDataPortLoopbackStatus_Type()
)
cmCpeDataPortLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortLoopbackStatus.setStatus("mandatory")
_CmCpeDataPortIntervalTable_Object = MibTable
cmCpeDataPortIntervalTable = _CmCpeDataPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2)
)
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalTable.setStatus("mandatory")
_CmCpeDataPortIntervalEntry_Object = MibTableRow
cmCpeDataPortIntervalEntry = _CmCpeDataPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1)
)
cmCpeDataPortIntervalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeDataPortIntervalIndex"),
)
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalEntry.setStatus("mandatory")
_CmCpeDataPortIntervalIndex_Type = CmObjectPII
_CmCpeDataPortIntervalIndex_Object = MibTableColumn
cmCpeDataPortIntervalIndex = _CmCpeDataPortIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 1),
    _CmCpeDataPortIntervalIndex_Type()
)
cmCpeDataPortIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalIndex.setStatus("mandatory")


class _CmCpeDataPortIntervalIntervalNumber_Type(Integer32):
    """Custom type cmCpeDataPortIntervalIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CmCpeDataPortIntervalIntervalNumber_Type.__name__ = "Integer32"
_CmCpeDataPortIntervalIntervalNumber_Object = MibTableColumn
cmCpeDataPortIntervalIntervalNumber = _CmCpeDataPortIntervalIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 2),
    _CmCpeDataPortIntervalIntervalNumber_Type()
)
cmCpeDataPortIntervalIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalIntervalNumber.setStatus("mandatory")
_CmCpeDataPortIntervalRxFrames_Type = Counter32
_CmCpeDataPortIntervalRxFrames_Object = MibTableColumn
cmCpeDataPortIntervalRxFrames = _CmCpeDataPortIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 3),
    _CmCpeDataPortIntervalRxFrames_Type()
)
cmCpeDataPortIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalRxFrames.setStatus("mandatory")
_CmCpeDataPortIntervalRxOctets_Type = Counter32
_CmCpeDataPortIntervalRxOctets_Object = MibTableColumn
cmCpeDataPortIntervalRxOctets = _CmCpeDataPortIntervalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 4),
    _CmCpeDataPortIntervalRxOctets_Type()
)
cmCpeDataPortIntervalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalRxOctets.setStatus("mandatory")
_CmCpeDataPortIntervalRxDiscards_Type = Counter32
_CmCpeDataPortIntervalRxDiscards_Object = MibTableColumn
cmCpeDataPortIntervalRxDiscards = _CmCpeDataPortIntervalRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 5),
    _CmCpeDataPortIntervalRxDiscards_Type()
)
cmCpeDataPortIntervalRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalRxDiscards.setStatus("mandatory")
_CmCpeDataPortIntervalRxErrors_Type = Counter32
_CmCpeDataPortIntervalRxErrors_Object = MibTableColumn
cmCpeDataPortIntervalRxErrors = _CmCpeDataPortIntervalRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 6),
    _CmCpeDataPortIntervalRxErrors_Type()
)
cmCpeDataPortIntervalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalRxErrors.setStatus("mandatory")
_CmCpeDataPortIntervalTxFrames_Type = Counter32
_CmCpeDataPortIntervalTxFrames_Object = MibTableColumn
cmCpeDataPortIntervalTxFrames = _CmCpeDataPortIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 7),
    _CmCpeDataPortIntervalTxFrames_Type()
)
cmCpeDataPortIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalTxFrames.setStatus("mandatory")
_CmCpeDataPortIntervalTxOctets_Type = Counter32
_CmCpeDataPortIntervalTxOctets_Object = MibTableColumn
cmCpeDataPortIntervalTxOctets = _CmCpeDataPortIntervalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 8),
    _CmCpeDataPortIntervalTxOctets_Type()
)
cmCpeDataPortIntervalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalTxOctets.setStatus("mandatory")
_CmCpeDataPortIntervalTxDiscards_Type = Counter32
_CmCpeDataPortIntervalTxDiscards_Object = MibTableColumn
cmCpeDataPortIntervalTxDiscards = _CmCpeDataPortIntervalTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 9),
    _CmCpeDataPortIntervalTxDiscards_Type()
)
cmCpeDataPortIntervalTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalTxDiscards.setStatus("mandatory")
_CmCpeDataPortIntervalTxErrors_Type = Counter32
_CmCpeDataPortIntervalTxErrors_Object = MibTableColumn
cmCpeDataPortIntervalTxErrors = _CmCpeDataPortIntervalTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 2, 1, 10),
    _CmCpeDataPortIntervalTxErrors_Type()
)
cmCpeDataPortIntervalTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortIntervalTxErrors.setStatus("mandatory")
_CmCpeDataPortTotalTable_Object = MibTable
cmCpeDataPortTotalTable = _CmCpeDataPortTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3)
)
if mibBuilder.loadTexts:
    cmCpeDataPortTotalTable.setStatus("mandatory")
_CmCpeDataPortTotalEntry_Object = MibTableRow
cmCpeDataPortTotalEntry = _CmCpeDataPortTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1)
)
cmCpeDataPortTotalEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeDataPortTotalIndex"),
)
if mibBuilder.loadTexts:
    cmCpeDataPortTotalEntry.setStatus("mandatory")
_CmCpeDataPortTotalIndex_Type = CmObjectPII
_CmCpeDataPortTotalIndex_Object = MibTableColumn
cmCpeDataPortTotalIndex = _CmCpeDataPortTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 1),
    _CmCpeDataPortTotalIndex_Type()
)
cmCpeDataPortTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalIndex.setStatus("mandatory")
_CmCpeDataPortTotalRxFrames_Type = Counter32
_CmCpeDataPortTotalRxFrames_Object = MibTableColumn
cmCpeDataPortTotalRxFrames = _CmCpeDataPortTotalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 2),
    _CmCpeDataPortTotalRxFrames_Type()
)
cmCpeDataPortTotalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalRxFrames.setStatus("mandatory")
_CmCpeDataPortTotalRxOctets_Type = Counter32
_CmCpeDataPortTotalRxOctets_Object = MibTableColumn
cmCpeDataPortTotalRxOctets = _CmCpeDataPortTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 3),
    _CmCpeDataPortTotalRxOctets_Type()
)
cmCpeDataPortTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalRxOctets.setStatus("mandatory")
_CmCpeDataPortTotalRxDiscards_Type = Counter32
_CmCpeDataPortTotalRxDiscards_Object = MibTableColumn
cmCpeDataPortTotalRxDiscards = _CmCpeDataPortTotalRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 4),
    _CmCpeDataPortTotalRxDiscards_Type()
)
cmCpeDataPortTotalRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalRxDiscards.setStatus("mandatory")
_CmCpeDataPortTotalRxErrors_Type = Counter32
_CmCpeDataPortTotalRxErrors_Object = MibTableColumn
cmCpeDataPortTotalRxErrors = _CmCpeDataPortTotalRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 5),
    _CmCpeDataPortTotalRxErrors_Type()
)
cmCpeDataPortTotalRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalRxErrors.setStatus("mandatory")
_CmCpeDataPortTotalTxFrames_Type = Counter32
_CmCpeDataPortTotalTxFrames_Object = MibTableColumn
cmCpeDataPortTotalTxFrames = _CmCpeDataPortTotalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 6),
    _CmCpeDataPortTotalTxFrames_Type()
)
cmCpeDataPortTotalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalTxFrames.setStatus("mandatory")
_CmCpeDataPortTotalTxOctets_Type = Counter32
_CmCpeDataPortTotalTxOctets_Object = MibTableColumn
cmCpeDataPortTotalTxOctets = _CmCpeDataPortTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 7),
    _CmCpeDataPortTotalTxOctets_Type()
)
cmCpeDataPortTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalTxOctets.setStatus("mandatory")
_CmCpeDataPortTotalTxDiscards_Type = Counter32
_CmCpeDataPortTotalTxDiscards_Object = MibTableColumn
cmCpeDataPortTotalTxDiscards = _CmCpeDataPortTotalTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 8),
    _CmCpeDataPortTotalTxDiscards_Type()
)
cmCpeDataPortTotalTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalTxDiscards.setStatus("mandatory")
_CmCpeDataPortTotalTxErrors_Type = Counter32
_CmCpeDataPortTotalTxErrors_Object = MibTableColumn
cmCpeDataPortTotalTxErrors = _CmCpeDataPortTotalTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 10, 12, 3, 1, 9),
    _CmCpeDataPortTotalTxErrors_Type()
)
cmCpeDataPortTotalTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeDataPortTotalTxErrors.setStatus("mandatory")
_CmCE200_ObjectIdentity = ObjectIdentity
cmCE200 = _CmCE200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20)
)
_CmSystem_ObjectIdentity = ObjectIdentity
cmSystem = _CmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1)
)


class _CmSysObjectClass_Type(Integer32):
    """Custom type cmSysObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            256
        )
    )
    namedValues = NamedValues(
        ("system", 256)
    )


_CmSysObjectClass_Type.__name__ = "Integer32"
_CmSysObjectClass_Object = MibScalar
cmSysObjectClass = _CmSysObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 1),
    _CmSysObjectClass_Type()
)
cmSysObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysObjectClass.setStatus("mandatory")


class _CmSysOperState_Type(Integer32):
    """Custom type cmSysOperState based on Integer32"""
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


_CmSysOperState_Type.__name__ = "Integer32"
_CmSysOperState_Object = MibScalar
cmSysOperState = _CmSysOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 2),
    _CmSysOperState_Type()
)
cmSysOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysOperState.setStatus("mandatory")
_CmSysMaster_Type = Integer32
_CmSysMaster_Object = MibScalar
cmSysMaster = _CmSysMaster_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 3),
    _CmSysMaster_Type()
)
cmSysMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysMaster.setStatus("mandatory")
_CmSysTrapAddress_Type = IpAddress
_CmSysTrapAddress_Object = MibScalar
cmSysTrapAddress = _CmSysTrapAddress_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 4),
    _CmSysTrapAddress_Type()
)
cmSysTrapAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmSysTrapAddress.setStatus("obsolete")
_CmSysConfigFileName_Type = DisplayString
_CmSysConfigFileName_Object = MibScalar
cmSysConfigFileName = _CmSysConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 5),
    _CmSysConfigFileName_Type()
)
cmSysConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysConfigFileName.setStatus("mandatory")


class _CmSysCommand_Type(Integer32):
    """Custom type cmSysCommand based on Integer32"""
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
        *(("none", 1),
          ("readConfig", 2),
          ("relinquish", 6),
          ("restart", 4),
          ("saveConfig", 3),
          ("takeover", 5))
    )


_CmSysCommand_Type.__name__ = "Integer32"
_CmSysCommand_Object = MibScalar
cmSysCommand = _CmSysCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 6),
    _CmSysCommand_Type()
)
cmSysCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSysCommand.setStatus("mandatory")


class _CmSysCommandStatus_Type(Integer32):
    """Custom type cmSysCommandStatus based on Integer32"""
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
        *(("aborted", 4),
          ("failed", 6),
          ("inprogress", 3),
          ("none", 1),
          ("pending", 2),
          ("succeeded", 5))
    )


_CmSysCommandStatus_Type.__name__ = "Integer32"
_CmSysCommandStatus_Object = MibScalar
cmSysCommandStatus = _CmSysCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 7),
    _CmSysCommandStatus_Type()
)
cmSysCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysCommandStatus.setStatus("mandatory")
_CmSysVersion_Type = DisplayString
_CmSysVersion_Object = MibScalar
cmSysVersion = _CmSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 8),
    _CmSysVersion_Type()
)
cmSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysVersion.setStatus("mandatory")
_CmSysCalendarTime_Type = DisplayString
_CmSysCalendarTime_Object = MibScalar
cmSysCalendarTime = _CmSysCalendarTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 9),
    _CmSysCalendarTime_Type()
)
cmSysCalendarTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSysCalendarTime.setStatus("mandatory")
_CmSysPrimaryPII_Type = CmObjectPII
_CmSysPrimaryPII_Object = MibScalar
cmSysPrimaryPII = _CmSysPrimaryPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 10),
    _CmSysPrimaryPII_Type()
)
cmSysPrimaryPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysPrimaryPII.setStatus("mandatory")
_CmSysSecondaryPII_Type = CmObjectPII
_CmSysSecondaryPII_Object = MibScalar
cmSysSecondaryPII = _CmSysSecondaryPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 11),
    _CmSysSecondaryPII_Type()
)
cmSysSecondaryPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysSecondaryPII.setStatus("mandatory")


class _CmSysRedundancy_Type(Integer32):
    """Custom type cmSysRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("notAvailable", 3))
    )


_CmSysRedundancy_Type.__name__ = "Integer32"
_CmSysRedundancy_Object = MibScalar
cmSysRedundancy = _CmSysRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 12),
    _CmSysRedundancy_Type()
)
cmSysRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSysRedundancy.setStatus("mandatory")


class _CmSysConfigSynch_Type(Integer32):
    """Custom type cmSysConfigSynch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSaved", 2),
          ("saved", 1))
    )


_CmSysConfigSynch_Type.__name__ = "Integer32"
_CmSysConfigSynch_Object = MibScalar
cmSysConfigSynch = _CmSysConfigSynch_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 13),
    _CmSysConfigSynch_Type()
)
cmSysConfigSynch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysConfigSynch.setStatus("mandatory")
_CmSysMyPII_Type = CmObjectPII
_CmSysMyPII_Object = MibScalar
cmSysMyPII = _CmSysMyPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 14),
    _CmSysMyPII_Type()
)
cmSysMyPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysMyPII.setStatus("mandatory")


class _CmSysShelfCount_Type(Integer32):
    """Custom type cmSysShelfCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmSysShelfCount_Type.__name__ = "Integer32"
_CmSysShelfCount_Object = MibScalar
cmSysShelfCount = _CmSysShelfCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 15),
    _CmSysShelfCount_Type()
)
cmSysShelfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSysShelfCount.setStatus("mandatory")
_CmSysExpIpSubNet_Type = IpAddress
_CmSysExpIpSubNet_Object = MibScalar
cmSysExpIpSubNet = _CmSysExpIpSubNet_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 1, 16),
    _CmSysExpIpSubNet_Type()
)
cmSysExpIpSubNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSysExpIpSubNet.setStatus("mandatory")
_CmBoard_ObjectIdentity = ObjectIdentity
cmBoard = _CmBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2)
)
_CmBoardTable_Object = MibTable
cmBoardTable = _CmBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1)
)
if mibBuilder.loadTexts:
    cmBoardTable.setStatus("mandatory")
_CmBoardEntry_Object = MibTableRow
cmBoardEntry = _CmBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1)
)
cmBoardEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
)
if mibBuilder.loadTexts:
    cmBoardEntry.setStatus("mandatory")
_CmBoardIndex_Type = Integer32
_CmBoardIndex_Object = MibTableColumn
cmBoardIndex = _CmBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 1),
    _CmBoardIndex_Type()
)
cmBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardIndex.setStatus("mandatory")


class _CmBoardObjectClass_Type(Integer32):
    """Custom type cmBoardObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmBoardObjectClass_Type.__name__ = "Integer32"
_CmBoardObjectClass_Object = MibTableColumn
cmBoardObjectClass = _CmBoardObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 2),
    _CmBoardObjectClass_Type()
)
cmBoardObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardObjectClass.setStatus("mandatory")


class _CmBoardOperState_Type(Integer32):
    """Custom type cmBoardOperState based on Integer32"""
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


_CmBoardOperState_Type.__name__ = "Integer32"
_CmBoardOperState_Object = MibTableColumn
cmBoardOperState = _CmBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 3),
    _CmBoardOperState_Type()
)
cmBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardOperState.setStatus("mandatory")
_CmBoardUpTime_Type = TimeTicks
_CmBoardUpTime_Object = MibTableColumn
cmBoardUpTime = _CmBoardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 4),
    _CmBoardUpTime_Type()
)
cmBoardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardUpTime.setStatus("mandatory")
_CmBoardFileName_Type = DisplayString
_CmBoardFileName_Object = MibTableColumn
cmBoardFileName = _CmBoardFileName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 5),
    _CmBoardFileName_Type()
)
cmBoardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardFileName.setStatus("mandatory")
_CmBoardFileDate_Type = DisplayString
_CmBoardFileDate_Object = MibTableColumn
cmBoardFileDate = _CmBoardFileDate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 6),
    _CmBoardFileDate_Type()
)
cmBoardFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardFileDate.setStatus("mandatory")


class _CmBoardHwType_Type(Integer32):
    """Custom type cmBoardHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6,
              7,
              9,
              13,
              14,
              15,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("hwBufferControlModule", 4),
          ("hwCopperBaySCM", 19),
          ("hwDS3ATM-WAN", 21),
          ("hwDS3RFR-WAN", 13),
          ("hwHSSI-WAN", 9),
          ("hwIDSLModule-24", 15),
          ("hwLANModule", 20),
          ("hwSDSL10xModule", 6),
          ("hwSDSL10xModule-1", 2),
          ("hwSDSL30xModule", 7),
          ("hwSDSL30xModule-24", 14),
          ("hwSystemControlModule", 1),
          ("hwV35-Wan", 5))
    )


_CmBoardHwType_Type.__name__ = "Integer32"
_CmBoardHwType_Object = MibTableColumn
cmBoardHwType = _CmBoardHwType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 7),
    _CmBoardHwType_Type()
)
cmBoardHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardHwType.setStatus("mandatory")
_CmBoardNumPorts_Type = Integer32
_CmBoardNumPorts_Object = MibTableColumn
cmBoardNumPorts = _CmBoardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 8),
    _CmBoardNumPorts_Type()
)
cmBoardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardNumPorts.setStatus("mandatory")
_CmBoardHwVersion_Type = DisplayString
_CmBoardHwVersion_Object = MibTableColumn
cmBoardHwVersion = _CmBoardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 9),
    _CmBoardHwVersion_Type()
)
cmBoardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardHwVersion.setStatus("mandatory")
_CmBoardSwVersion_Type = DisplayString
_CmBoardSwVersion_Object = MibTableColumn
cmBoardSwVersion = _CmBoardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 10),
    _CmBoardSwVersion_Type()
)
cmBoardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardSwVersion.setStatus("mandatory")
_CmBoardPromVersion_Type = DisplayString
_CmBoardPromVersion_Object = MibTableColumn
cmBoardPromVersion = _CmBoardPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 11),
    _CmBoardPromVersion_Type()
)
cmBoardPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardPromVersion.setStatus("mandatory")


class _CmBoardRole_Type(Integer32):
    """Custom type cmBoardRole based on Integer32"""
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
        *(("active", 1),
          ("primary", 5),
          ("secondary", 6),
          ("shelfMaster", 3),
          ("standby", 4),
          ("systemMaster", 2))
    )


_CmBoardRole_Type.__name__ = "Integer32"
_CmBoardRole_Object = MibTableColumn
cmBoardRole = _CmBoardRole_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 12),
    _CmBoardRole_Type()
)
cmBoardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardRole.setStatus("mandatory")
_CmBoardConfigChange_Type = DisplayString
_CmBoardConfigChange_Object = MibTableColumn
cmBoardConfigChange = _CmBoardConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 13),
    _CmBoardConfigChange_Type()
)
cmBoardConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardConfigChange.setStatus("mandatory")


class _CmBoardCommand_Type(Integer32):
    """Custom type cmBoardCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 4),
          ("restart", 1))
    )


_CmBoardCommand_Type.__name__ = "Integer32"
_CmBoardCommand_Object = MibTableColumn
cmBoardCommand = _CmBoardCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 14),
    _CmBoardCommand_Type()
)
cmBoardCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmBoardCommand.setStatus("mandatory")
_CmBoardSerialNumber_Type = DisplayString
_CmBoardSerialNumber_Object = MibTableColumn
cmBoardSerialNumber = _CmBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 15),
    _CmBoardSerialNumber_Type()
)
cmBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardSerialNumber.setStatus("mandatory")


class _CmBoardClusterRole_Type(Integer32):
    """Custom type cmBoardClusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("expansion", 3),
          ("master", 2),
          ("notApplicable", 1))
    )


_CmBoardClusterRole_Type.__name__ = "Integer32"
_CmBoardClusterRole_Object = MibTableColumn
cmBoardClusterRole = _CmBoardClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 16),
    _CmBoardClusterRole_Type()
)
cmBoardClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardClusterRole.setStatus("mandatory")
_CmBoardInformation_Type = DisplayString
_CmBoardInformation_Object = MibTableColumn
cmBoardInformation = _CmBoardInformation_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 1, 1, 17),
    _CmBoardInformation_Type()
)
cmBoardInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBoardInformation.setStatus("mandatory")
_CmIDSLBoardTable_Object = MibTable
cmIDSLBoardTable = _CmIDSLBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2)
)
if mibBuilder.loadTexts:
    cmIDSLBoardTable.setStatus("mandatory")
_CmIDSLBoardEntry_Object = MibTableRow
cmIDSLBoardEntry = _CmIDSLBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2, 1)
)
cmIDSLBoardEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIDSLBoardIndex"),
)
if mibBuilder.loadTexts:
    cmIDSLBoardEntry.setStatus("mandatory")
_CmIDSLBoardIndex_Type = CmObjectPII
_CmIDSLBoardIndex_Object = MibTableColumn
cmIDSLBoardIndex = _CmIDSLBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2, 1, 1),
    _CmIDSLBoardIndex_Type()
)
cmIDSLBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLBoardIndex.setStatus("mandatory")


class _CmIDSLBoardTimingMode_Type(Integer32):
    """Custom type cmIDSLBoardTimingMode based on Integer32"""
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
        *(("internallyTimed", 1),
          ("locallyTimed", 2),
          ("networkTimedBackup", 5),
          ("networkTimedMaster", 4),
          ("networkTimedSlave", 3))
    )


_CmIDSLBoardTimingMode_Type.__name__ = "Integer32"
_CmIDSLBoardTimingMode_Object = MibTableColumn
cmIDSLBoardTimingMode = _CmIDSLBoardTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2, 1, 2),
    _CmIDSLBoardTimingMode_Type()
)
cmIDSLBoardTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmIDSLBoardTimingMode.setStatus("mandatory")


class _CmIDSLBoardTimingStatus_Type(Integer32):
    """Custom type cmIDSLBoardTimingStatus based on Integer32"""
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
        *(("internallyTimed", 1),
          ("locallyTimed", 2),
          ("networkTimedMaster", 4),
          ("networkTimedSlave", 3))
    )


_CmIDSLBoardTimingStatus_Type.__name__ = "Integer32"
_CmIDSLBoardTimingStatus_Object = MibTableColumn
cmIDSLBoardTimingStatus = _CmIDSLBoardTimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2, 1, 3),
    _CmIDSLBoardTimingStatus_Type()
)
cmIDSLBoardTimingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLBoardTimingStatus.setStatus("mandatory")


class _CmIDSLBoardTimingAvailable_Type(Integer32):
    """Custom type cmIDSLBoardTimingAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CmIDSLBoardTimingAvailable_Type.__name__ = "Integer32"
_CmIDSLBoardTimingAvailable_Object = MibTableColumn
cmIDSLBoardTimingAvailable = _CmIDSLBoardTimingAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 2, 2, 1, 4),
    _CmIDSLBoardTimingAvailable_Type()
)
cmIDSLBoardTimingAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmIDSLBoardTimingAvailable.setStatus("mandatory")
_CmState_ObjectIdentity = ObjectIdentity
cmState = _CmState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3)
)
_CmStateTable_Object = MibTable
cmStateTable = _CmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1)
)
if mibBuilder.loadTexts:
    cmStateTable.setStatus("mandatory")
_CmStateEntry_Object = MibTableRow
cmStateEntry = _CmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1)
)
cmStateEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmStateGenericClass"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmStateIndex"),
)
if mibBuilder.loadTexts:
    cmStateEntry.setStatus("mandatory")


class _CmStateGenericClass_Type(Integer32):
    """Custom type cmStateGenericClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              768,
              1024,
              1280,
              2304)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("link", 1280),
          ("port", 1024),
          ("shelf", 512),
          ("support", 2304),
          ("system", 256))
    )


_CmStateGenericClass_Type.__name__ = "Integer32"
_CmStateGenericClass_Object = MibTableColumn
cmStateGenericClass = _CmStateGenericClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1, 1),
    _CmStateGenericClass_Type()
)
cmStateGenericClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStateGenericClass.setStatus("mandatory")
_CmStateIndex_Type = Integer32
_CmStateIndex_Object = MibTableColumn
cmStateIndex = _CmStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1, 2),
    _CmStateIndex_Type()
)
cmStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStateIndex.setStatus("mandatory")


class _CmStateObjClass_Type(Integer32):
    """Custom type cmStateObjClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmStateObjClass_Type.__name__ = "Integer32"
_CmStateObjClass_Object = MibTableColumn
cmStateObjClass = _CmStateObjClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1, 3),
    _CmStateObjClass_Type()
)
cmStateObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStateObjClass.setStatus("mandatory")


class _CmStateOperState_Type(Integer32):
    """Custom type cmStateOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("testing", 3))
    )


_CmStateOperState_Type.__name__ = "Integer32"
_CmStateOperState_Object = MibTableColumn
cmStateOperState = _CmStateOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1, 4),
    _CmStateOperState_Type()
)
cmStateOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStateOperState.setStatus("mandatory")
_CmStateLastChange_Type = TimeTicks
_CmStateLastChange_Object = MibTableColumn
cmStateLastChange = _CmStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 3, 1, 1, 5),
    _CmStateLastChange_Type()
)
cmStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmStateLastChange.setStatus("mandatory")
_CmShelf_ObjectIdentity = ObjectIdentity
cmShelf = _CmShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4)
)
_CmShelfTable_Object = MibTable
cmShelfTable = _CmShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1)
)
if mibBuilder.loadTexts:
    cmShelfTable.setStatus("mandatory")
_CmShelfEntry_Object = MibTableRow
cmShelfEntry = _CmShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1)
)
cmShelfEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmShelfIndex"),
)
if mibBuilder.loadTexts:
    cmShelfEntry.setStatus("mandatory")
_CmShelfIndex_Type = CmObjectPII
_CmShelfIndex_Object = MibTableColumn
cmShelfIndex = _CmShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 1),
    _CmShelfIndex_Type()
)
cmShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfIndex.setStatus("mandatory")


class _CmShelfObjectClass_Type(Integer32):
    """Custom type cmShelfObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmShelfObjectClass_Type.__name__ = "Integer32"
_CmShelfObjectClass_Object = MibTableColumn
cmShelfObjectClass = _CmShelfObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 2),
    _CmShelfObjectClass_Type()
)
cmShelfObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfObjectClass.setStatus("mandatory")


class _CmShelfOperability_Type(Integer32):
    """Custom type cmShelfOperability based on Integer32"""
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


_CmShelfOperability_Type.__name__ = "Integer32"
_CmShelfOperability_Object = MibTableColumn
cmShelfOperability = _CmShelfOperability_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 3),
    _CmShelfOperability_Type()
)
cmShelfOperability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfOperability.setStatus("mandatory")
_CmShelfUpTime_Type = TimeTicks
_CmShelfUpTime_Object = MibTableColumn
cmShelfUpTime = _CmShelfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 4),
    _CmShelfUpTime_Type()
)
cmShelfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfUpTime.setStatus("mandatory")
_CmShelfMaster_Type = Integer32
_CmShelfMaster_Object = MibTableColumn
cmShelfMaster = _CmShelfMaster_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 5),
    _CmShelfMaster_Type()
)
cmShelfMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfMaster.setStatus("mandatory")
_CmShelfBoardMap_Type = OctetString
_CmShelfBoardMap_Object = MibTableColumn
cmShelfBoardMap = _CmShelfBoardMap_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 6),
    _CmShelfBoardMap_Type()
)
cmShelfBoardMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfBoardMap.setStatus("mandatory")


class _CmShelfCommand_Type(Integer32):
    """Custom type cmShelfCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("restart", 2))
    )


_CmShelfCommand_Type.__name__ = "Integer32"
_CmShelfCommand_Object = MibTableColumn
cmShelfCommand = _CmShelfCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 7),
    _CmShelfCommand_Type()
)
cmShelfCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmShelfCommand.setStatus("mandatory")


class _CmShelfShelfNumber_Type(Integer32):
    """Custom type cmShelfShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmShelfShelfNumber_Type.__name__ = "Integer32"
_CmShelfShelfNumber_Object = MibTableColumn
cmShelfShelfNumber = _CmShelfShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 4, 1, 1, 8),
    _CmShelfShelfNumber_Type()
)
cmShelfShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmShelfShelfNumber.setStatus("mandatory")
_CmFile_ObjectIdentity = ObjectIdentity
cmFile = _CmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5)
)


class _CmFileBootDevice_Type(Integer32):
    """Custom type cmFileBootDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileServer", 2),
          ("flash", 1))
    )


_CmFileBootDevice_Type.__name__ = "Integer32"
_CmFileBootDevice_Object = MibScalar
cmFileBootDevice = _CmFileBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 1),
    _CmFileBootDevice_Type()
)
cmFileBootDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFileBootDevice.setStatus("mandatory")
_CmFileFSName_Type = DisplayString
_CmFileFSName_Object = MibScalar
cmFileFSName = _CmFileFSName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 2),
    _CmFileFSName_Type()
)
cmFileFSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFileFSName.setStatus("mandatory")
_CmFileFSAddr_Type = IpAddress
_CmFileFSAddr_Object = MibScalar
cmFileFSAddr = _CmFileFSAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 3),
    _CmFileFSAddr_Type()
)
cmFileFSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFileFSAddr.setStatus("mandatory")
_CmFileFSUsername_Type = DisplayString
_CmFileFSUsername_Object = MibScalar
cmFileFSUsername = _CmFileFSUsername_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 4),
    _CmFileFSUsername_Type()
)
cmFileFSUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFileFSUsername.setStatus("mandatory")
_CmFileFSPassword_Type = DisplayString
_CmFileFSPassword_Object = MibScalar
cmFileFSPassword = _CmFileFSPassword_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 5),
    _CmFileFSPassword_Type()
)
cmFileFSPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFileFSPassword.setStatus("mandatory")
_CmFileFLASHDir_Type = DisplayString
_CmFileFLASHDir_Object = MibScalar
cmFileFLASHDir = _CmFileFLASHDir_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 6),
    _CmFileFLASHDir_Type()
)
cmFileFLASHDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmFileFLASHDir.setStatus("mandatory")
_CmFileFSDir_Type = DisplayString
_CmFileFSDir_Object = MibScalar
cmFileFSDir = _CmFileFSDir_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 5, 7),
    _CmFileFSDir_Type()
)
cmFileFSDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmFileFSDir.setStatus("mandatory")
_CmCpeBoard_ObjectIdentity = ObjectIdentity
cmCpeBoard = _CmCpeBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6)
)
_CmCpeBoardTable_Object = MibTable
cmCpeBoardTable = _CmCpeBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1)
)
if mibBuilder.loadTexts:
    cmCpeBoardTable.setStatus("mandatory")
_CmCpeBoardEntry_Object = MibTableRow
cmCpeBoardEntry = _CmCpeBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1)
)
cmCpeBoardEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmCpeBoardIndex"),
)
if mibBuilder.loadTexts:
    cmCpeBoardEntry.setStatus("mandatory")
_CmCpeBoardIndex_Type = Integer32
_CmCpeBoardIndex_Object = MibTableColumn
cmCpeBoardIndex = _CmCpeBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 1),
    _CmCpeBoardIndex_Type()
)
cmCpeBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardIndex.setStatus("mandatory")


class _CmCpeBoardObjectClass_Type(Integer32):
    """Custom type cmCpeBoardObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmCpeBoardObjectClass_Type.__name__ = "Integer32"
_CmCpeBoardObjectClass_Object = MibTableColumn
cmCpeBoardObjectClass = _CmCpeBoardObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 2),
    _CmCpeBoardObjectClass_Type()
)
cmCpeBoardObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardObjectClass.setStatus("mandatory")


class _CmCpeBoardOperState_Type(Integer32):
    """Custom type cmCpeBoardOperState based on Integer32"""
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


_CmCpeBoardOperState_Type.__name__ = "Integer32"
_CmCpeBoardOperState_Object = MibTableColumn
cmCpeBoardOperState = _CmCpeBoardOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 3),
    _CmCpeBoardOperState_Type()
)
cmCpeBoardOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardOperState.setStatus("mandatory")
_CmCpeBoardUpTime_Type = TimeTicks
_CmCpeBoardUpTime_Object = MibTableColumn
cmCpeBoardUpTime = _CmCpeBoardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 4),
    _CmCpeBoardUpTime_Type()
)
cmCpeBoardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardUpTime.setStatus("mandatory")
_CmCpeBoardFileName_Type = DisplayString
_CmCpeBoardFileName_Object = MibTableColumn
cmCpeBoardFileName = _CmCpeBoardFileName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 5),
    _CmCpeBoardFileName_Type()
)
cmCpeBoardFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardFileName.setStatus("mandatory")
_CmCpeBoardFileDate_Type = DisplayString
_CmCpeBoardFileDate_Object = MibTableColumn
cmCpeBoardFileDate = _CmCpeBoardFileDate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 6),
    _CmCpeBoardFileDate_Type()
)
cmCpeBoardFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardFileDate.setStatus("mandatory")


class _CmCpeBoardHwType_Type(Integer32):
    """Custom type cmCpeBoardHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8,
              10,
              16,
              17,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("hwCPE-IDSL", 23),
          ("hwCPE-SDSL", 22),
          ("hwCR201-10x", 3),
          ("hwCR201-30x", 8),
          ("hwCR201-IDSL", 17),
          ("hwCR201-SDSL", 10),
          ("hwNetopia-SDSL", 16))
    )


_CmCpeBoardHwType_Type.__name__ = "Integer32"
_CmCpeBoardHwType_Object = MibTableColumn
cmCpeBoardHwType = _CmCpeBoardHwType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 7),
    _CmCpeBoardHwType_Type()
)
cmCpeBoardHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardHwType.setStatus("mandatory")
_CmCpeBoardNumPorts_Type = Integer32
_CmCpeBoardNumPorts_Object = MibTableColumn
cmCpeBoardNumPorts = _CmCpeBoardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 8),
    _CmCpeBoardNumPorts_Type()
)
cmCpeBoardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardNumPorts.setStatus("mandatory")
_CmCpeBoardHwVersion_Type = DisplayString
_CmCpeBoardHwVersion_Object = MibTableColumn
cmCpeBoardHwVersion = _CmCpeBoardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 9),
    _CmCpeBoardHwVersion_Type()
)
cmCpeBoardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardHwVersion.setStatus("mandatory")
_CmCpeBoardSwVersion_Type = DisplayString
_CmCpeBoardSwVersion_Object = MibTableColumn
cmCpeBoardSwVersion = _CmCpeBoardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 10),
    _CmCpeBoardSwVersion_Type()
)
cmCpeBoardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardSwVersion.setStatus("mandatory")
_CmCpeBoardPromVersion_Type = DisplayString
_CmCpeBoardPromVersion_Object = MibTableColumn
cmCpeBoardPromVersion = _CmCpeBoardPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 11),
    _CmCpeBoardPromVersion_Type()
)
cmCpeBoardPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardPromVersion.setStatus("mandatory")
_CmCpeBoardConfigChange_Type = DisplayString
_CmCpeBoardConfigChange_Object = MibTableColumn
cmCpeBoardConfigChange = _CmCpeBoardConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 13),
    _CmCpeBoardConfigChange_Type()
)
cmCpeBoardConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardConfigChange.setStatus("mandatory")


class _CmCpeBoardCommand_Type(Integer32):
    """Custom type cmCpeBoardCommand based on Integer32"""
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
        *(("erase", 2),
          ("none", 4),
          ("restart", 1),
          ("upgrade", 3))
    )


_CmCpeBoardCommand_Type.__name__ = "Integer32"
_CmCpeBoardCommand_Object = MibTableColumn
cmCpeBoardCommand = _CmCpeBoardCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 14),
    _CmCpeBoardCommand_Type()
)
cmCpeBoardCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmCpeBoardCommand.setStatus("mandatory")
_CmCpeBoardSerialNumber_Type = DisplayString
_CmCpeBoardSerialNumber_Object = MibTableColumn
cmCpeBoardSerialNumber = _CmCpeBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 15),
    _CmCpeBoardSerialNumber_Type()
)
cmCpeBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardSerialNumber.setStatus("mandatory")
_CmCpeBoardVendorDescription_Type = DisplayString
_CmCpeBoardVendorDescription_Object = MibTableColumn
cmCpeBoardVendorDescription = _CmCpeBoardVendorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 16),
    _CmCpeBoardVendorDescription_Type()
)
cmCpeBoardVendorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardVendorDescription.setStatus("mandatory")
_CmCpeBoardGroupMap_Type = OctetString
_CmCpeBoardGroupMap_Object = MibTableColumn
cmCpeBoardGroupMap = _CmCpeBoardGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 17),
    _CmCpeBoardGroupMap_Type()
)
cmCpeBoardGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardGroupMap.setStatus("mandatory")
_CmCpeBoardManagementOptions_Type = Integer32
_CmCpeBoardManagementOptions_Object = MibTableColumn
cmCpeBoardManagementOptions = _CmCpeBoardManagementOptions_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 6, 1, 1, 18),
    _CmCpeBoardManagementOptions_Type()
)
cmCpeBoardManagementOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmCpeBoardManagementOptions.setStatus("mandatory")
_CmHSSI_ObjectIdentity = ObjectIdentity
cmHSSI = _CmHSSI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7)
)
_CmHSSITable_Object = MibTable
cmHSSITable = _CmHSSITable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1)
)
if mibBuilder.loadTexts:
    cmHSSITable.setStatus("mandatory")
_CmHSSIEntry_Object = MibTableRow
cmHSSIEntry = _CmHSSIEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1)
)
cmHSSIEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHSSIIndex"),
)
if mibBuilder.loadTexts:
    cmHSSIEntry.setStatus("mandatory")
_CmHSSIIndex_Type = Integer32
_CmHSSIIndex_Object = MibTableColumn
cmHSSIIndex = _CmHSSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 1),
    _CmHSSIIndex_Type()
)
cmHSSIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIIndex.setStatus("mandatory")
_CmHSSIIfIndex_Type = Integer32
_CmHSSIIfIndex_Object = MibTableColumn
cmHSSIIfIndex = _CmHSSIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 2),
    _CmHSSIIfIndex_Type()
)
cmHSSIIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIIfIndex.setStatus("mandatory")


class _CmHSSIDCEReady_Type(Integer32):
    """Custom type cmHSSIDCEReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 1),
          ("ready", 2))
    )


_CmHSSIDCEReady_Type.__name__ = "Integer32"
_CmHSSIDCEReady_Object = MibTableColumn
cmHSSIDCEReady = _CmHSSIDCEReady_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 3),
    _CmHSSIDCEReady_Type()
)
cmHSSIDCEReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIDCEReady.setStatus("mandatory")


class _CmHSSIDTEReady_Type(Integer32):
    """Custom type cmHSSIDTEReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 1),
          ("ready", 2))
    )


_CmHSSIDTEReady_Type.__name__ = "Integer32"
_CmHSSIDTEReady_Object = MibTableColumn
cmHSSIDTEReady = _CmHSSIDTEReady_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 4),
    _CmHSSIDTEReady_Type()
)
cmHSSIDTEReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIDTEReady.setStatus("mandatory")


class _CmHSSIDTEDCE_Type(Integer32):
    """Custom type cmHSSIDTEDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_CmHSSIDTEDCE_Type.__name__ = "Integer32"
_CmHSSIDTEDCE_Object = MibTableColumn
cmHSSIDTEDCE = _CmHSSIDTEDCE_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 5),
    _CmHSSIDTEDCE_Type()
)
cmHSSIDTEDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIDTEDCE.setStatus("mandatory")


class _CmHSSILoopback_Type(Integer32):
    """Custom type cmHSSILoopback based on Integer32"""
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
        *(("local-digital", 4),
          ("local-line", 2),
          ("none", 1),
          ("remote-line", 3))
    )


_CmHSSILoopback_Type.__name__ = "Integer32"
_CmHSSILoopback_Object = MibTableColumn
cmHSSILoopback = _CmHSSILoopback_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 6),
    _CmHSSILoopback_Type()
)
cmHSSILoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSILoopback.setStatus("mandatory")


class _CmHSSITestmode_Type(Integer32):
    """Custom type cmHSSITestmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmHSSITestmode_Type.__name__ = "Integer32"
_CmHSSITestmode_Object = MibTableColumn
cmHSSITestmode = _CmHSSITestmode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 7),
    _CmHSSITestmode_Type()
)
cmHSSITestmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSITestmode.setStatus("mandatory")


class _CmHSSISync_Type(Integer32):
    """Custom type cmHSSISync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync-off", 1),
          ("sync-on", 2))
    )


_CmHSSISync_Type.__name__ = "Integer32"
_CmHSSISync_Object = MibTableColumn
cmHSSISync = _CmHSSISync_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 8),
    _CmHSSISync_Type()
)
cmHSSISync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSISync.setStatus("mandatory")


class _CmHSSITxClockPresent_Type(Integer32):
    """Custom type cmHSSITxClockPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmHSSITxClockPresent_Type.__name__ = "Integer32"
_CmHSSITxClockPresent_Object = MibTableColumn
cmHSSITxClockPresent = _CmHSSITxClockPresent_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 9),
    _CmHSSITxClockPresent_Type()
)
cmHSSITxClockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSITxClockPresent.setStatus("mandatory")


class _CmHSSICRC_Type(Integer32):
    """Custom type cmHSSICRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("crc-16", 2)
    )


_CmHSSICRC_Type.__name__ = "Integer32"
_CmHSSICRC_Object = MibTableColumn
cmHSSICRC = _CmHSSICRC_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 10),
    _CmHSSICRC_Type()
)
cmHSSICRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHSSICRC.setStatus("mandatory")
_CmHSSIClockRate_Type = Integer32
_CmHSSIClockRate_Object = MibTableColumn
cmHSSIClockRate = _CmHSSIClockRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 11),
    _CmHSSIClockRate_Type()
)
cmHSSIClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHSSIClockRate.setStatus("mandatory")


class _CmHSSIAdminState_Type(Integer32):
    """Custom type cmHSSIAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("shutdown", 3))
    )


_CmHSSIAdminState_Type.__name__ = "Integer32"
_CmHSSIAdminState_Object = MibTableColumn
cmHSSIAdminState = _CmHSSIAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 12),
    _CmHSSIAdminState_Type()
)
cmHSSIAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIAdminState.setStatus("mandatory")


class _CmHSSIOperState_Type(Integer32):
    """Custom type cmHSSIOperState based on Integer32"""
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


_CmHSSIOperState_Type.__name__ = "Integer32"
_CmHSSIOperState_Object = MibTableColumn
cmHSSIOperState = _CmHSSIOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 7, 1, 1, 13),
    _CmHSSIOperState_Type()
)
cmHSSIOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmHSSIOperState.setStatus("mandatory")
_CmV35_ObjectIdentity = ObjectIdentity
cmV35 = _CmV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8)
)
_CmV35Table_Object = MibTable
cmV35Table = _CmV35Table_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1)
)
if mibBuilder.loadTexts:
    cmV35Table.setStatus("mandatory")
_CmV35Entry_Object = MibTableRow
cmV35Entry = _CmV35Entry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1)
)
cmV35Entry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmV35Index"),
)
if mibBuilder.loadTexts:
    cmV35Entry.setStatus("mandatory")
_CmV35Index_Type = Integer32
_CmV35Index_Object = MibTableColumn
cmV35Index = _CmV35Index_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 1),
    _CmV35Index_Type()
)
cmV35Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35Index.setStatus("mandatory")
_CmV35IfIndex_Type = Integer32
_CmV35IfIndex_Object = MibTableColumn
cmV35IfIndex = _CmV35IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 2),
    _CmV35IfIndex_Type()
)
cmV35IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35IfIndex.setStatus("mandatory")


class _CmV35DSR_Type(Integer32):
    """Custom type cmV35DSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmV35DSR_Type.__name__ = "Integer32"
_CmV35DSR_Object = MibTableColumn
cmV35DSR = _CmV35DSR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 3),
    _CmV35DSR_Type()
)
cmV35DSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35DSR.setStatus("mandatory")


class _CmV35DCD_Type(Integer32):
    """Custom type cmV35DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmV35DCD_Type.__name__ = "Integer32"
_CmV35DCD_Object = MibTableColumn
cmV35DCD = _CmV35DCD_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 4),
    _CmV35DCD_Type()
)
cmV35DCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35DCD.setStatus("mandatory")


class _CmV35CTS_Type(Integer32):
    """Custom type cmV35CTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmV35CTS_Type.__name__ = "Integer32"
_CmV35CTS_Object = MibTableColumn
cmV35CTS = _CmV35CTS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 5),
    _CmV35CTS_Type()
)
cmV35CTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35CTS.setStatus("mandatory")


class _CmV35DTR_Type(Integer32):
    """Custom type cmV35DTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmV35DTR_Type.__name__ = "Integer32"
_CmV35DTR_Object = MibTableColumn
cmV35DTR = _CmV35DTR_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 6),
    _CmV35DTR_Type()
)
cmV35DTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35DTR.setStatus("mandatory")


class _CmV35RTS_Type(Integer32):
    """Custom type cmV35RTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_CmV35RTS_Type.__name__ = "Integer32"
_CmV35RTS_Object = MibTableColumn
cmV35RTS = _CmV35RTS_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 7),
    _CmV35RTS_Type()
)
cmV35RTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35RTS.setStatus("mandatory")


class _CmV35DTEDCE_Type(Integer32):
    """Custom type cmV35DTEDCE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_CmV35DTEDCE_Type.__name__ = "Integer32"
_CmV35DTEDCE_Object = MibTableColumn
cmV35DTEDCE = _CmV35DTEDCE_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 8),
    _CmV35DTEDCE_Type()
)
cmV35DTEDCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35DTEDCE.setStatus("mandatory")


class _CmV35Sync_Type(Integer32):
    """Custom type cmV35Sync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync-off", 1),
          ("sync-on", 2))
    )


_CmV35Sync_Type.__name__ = "Integer32"
_CmV35Sync_Object = MibTableColumn
cmV35Sync = _CmV35Sync_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 9),
    _CmV35Sync_Type()
)
cmV35Sync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35Sync.setStatus("mandatory")


class _CmV35TxClockSource_Type(Integer32):
    """Custom type cmV35TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clock-ext", 1),
          ("clock-int", 2))
    )


_CmV35TxClockSource_Type.__name__ = "Integer32"
_CmV35TxClockSource_Object = MibTableColumn
cmV35TxClockSource = _CmV35TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 10),
    _CmV35TxClockSource_Type()
)
cmV35TxClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35TxClockSource.setStatus("mandatory")


class _CmV35CRC_Type(Integer32):
    """Custom type cmV35CRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("crc-CCITT", 1)
    )


_CmV35CRC_Type.__name__ = "Integer32"
_CmV35CRC_Object = MibTableColumn
cmV35CRC = _CmV35CRC_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 11),
    _CmV35CRC_Type()
)
cmV35CRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmV35CRC.setStatus("mandatory")
_CmV35ClockRate_Type = Integer32
_CmV35ClockRate_Object = MibTableColumn
cmV35ClockRate = _CmV35ClockRate_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 12),
    _CmV35ClockRate_Type()
)
cmV35ClockRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35ClockRate.setStatus("mandatory")


class _CmV35AdminState_Type(Integer32):
    """Custom type cmV35AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("shutdown", 3))
    )


_CmV35AdminState_Type.__name__ = "Integer32"
_CmV35AdminState_Object = MibTableColumn
cmV35AdminState = _CmV35AdminState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 13),
    _CmV35AdminState_Type()
)
cmV35AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35AdminState.setStatus("mandatory")


class _CmV35OperState_Type(Integer32):
    """Custom type cmV35OperState based on Integer32"""
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


_CmV35OperState_Type.__name__ = "Integer32"
_CmV35OperState_Object = MibTableColumn
cmV35OperState = _CmV35OperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 8, 1, 1, 14),
    _CmV35OperState_Type()
)
cmV35OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmV35OperState.setStatus("mandatory")
_CmTrap_ObjectIdentity = ObjectIdentity
cmTrap = _CmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9)
)
_CmTrapEventSeqNum_Type = Integer32
_CmTrapEventSeqNum_Object = MibScalar
cmTrapEventSeqNum = _CmTrapEventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 1),
    _CmTrapEventSeqNum_Type()
)
cmTrapEventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventSeqNum.setStatus("mandatory")
_CmTrapCriticalAlarmCount_Type = Integer32
_CmTrapCriticalAlarmCount_Object = MibScalar
cmTrapCriticalAlarmCount = _CmTrapCriticalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 2),
    _CmTrapCriticalAlarmCount_Type()
)
cmTrapCriticalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapCriticalAlarmCount.setStatus("mandatory")
_CmTrapMajorAlarmCount_Type = Integer32
_CmTrapMajorAlarmCount_Object = MibScalar
cmTrapMajorAlarmCount = _CmTrapMajorAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 3),
    _CmTrapMajorAlarmCount_Type()
)
cmTrapMajorAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapMajorAlarmCount.setStatus("mandatory")
_CmTrapMinorAlarmCount_Type = Integer32
_CmTrapMinorAlarmCount_Object = MibScalar
cmTrapMinorAlarmCount = _CmTrapMinorAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 4),
    _CmTrapMinorAlarmCount_Type()
)
cmTrapMinorAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapMinorAlarmCount.setStatus("mandatory")
_CmTrapWarningCount_Type = Integer32
_CmTrapWarningCount_Object = MibScalar
cmTrapWarningCount = _CmTrapWarningCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 5),
    _CmTrapWarningCount_Type()
)
cmTrapWarningCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapWarningCount.setStatus("mandatory")
_CmTrapReceiverTable_Object = MibTable
cmTrapReceiverTable = _CmTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6)
)
if mibBuilder.loadTexts:
    cmTrapReceiverTable.setStatus("obsolete")
_CmTrapReceiverEntry_Object = MibTableRow
cmTrapReceiverEntry = _CmTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1)
)
cmTrapReceiverEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapReceiverIPAddr"),
)
if mibBuilder.loadTexts:
    cmTrapReceiverEntry.setStatus("obsolete")
_CmTrapReceiverIPAddr_Type = IpAddress
_CmTrapReceiverIPAddr_Object = MibTableColumn
cmTrapReceiverIPAddr = _CmTrapReceiverIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1, 1),
    _CmTrapReceiverIPAddr_Type()
)
cmTrapReceiverIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmTrapReceiverIPAddr.setStatus("obsolete")
_CmTrapReceiverPort_Type = Integer32
_CmTrapReceiverPort_Object = MibTableColumn
cmTrapReceiverPort = _CmTrapReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1, 2),
    _CmTrapReceiverPort_Type()
)
cmTrapReceiverPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmTrapReceiverPort.setStatus("obsolete")
_CmTrapReceiverCommunity_Type = DisplayString
_CmTrapReceiverCommunity_Object = MibTableColumn
cmTrapReceiverCommunity = _CmTrapReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1, 3),
    _CmTrapReceiverCommunity_Type()
)
cmTrapReceiverCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmTrapReceiverCommunity.setStatus("obsolete")


class _CmTrapReceiverRowStatus_Type(Integer32):
    """Custom type cmTrapReceiverRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 4),
          ("createAndWait", 5),
          ("delete", 6),
          ("notInService", 2))
    )


_CmTrapReceiverRowStatus_Type.__name__ = "Integer32"
_CmTrapReceiverRowStatus_Object = MibTableColumn
cmTrapReceiverRowStatus = _CmTrapReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1, 4),
    _CmTrapReceiverRowStatus_Type()
)
cmTrapReceiverRowStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmTrapReceiverRowStatus.setStatus("obsolete")
_CmTrapReceiverOwnerString_Type = DisplayString
_CmTrapReceiverOwnerString_Object = MibTableColumn
cmTrapReceiverOwnerString = _CmTrapReceiverOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 6, 1, 5),
    _CmTrapReceiverOwnerString_Type()
)
cmTrapReceiverOwnerString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmTrapReceiverOwnerString.setStatus("obsolete")
_CmTrapEventLogTable_Object = MibTable
cmTrapEventLogTable = _CmTrapEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7)
)
if mibBuilder.loadTexts:
    cmTrapEventLogTable.setStatus("mandatory")
_CmTrapEventLogEntry_Object = MibTableRow
cmTrapEventLogEntry = _CmTrapEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1)
)
cmTrapEventLogEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
)
if mibBuilder.loadTexts:
    cmTrapEventLogEntry.setStatus("mandatory")
_CmTrapEventLogSeqNum_Type = Integer32
_CmTrapEventLogSeqNum_Object = MibTableColumn
cmTrapEventLogSeqNum = _CmTrapEventLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 1),
    _CmTrapEventLogSeqNum_Type()
)
cmTrapEventLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogSeqNum.setStatus("mandatory")


class _CmTrapEventLogType_Type(Integer32):
    """Custom type cmTrapEventLogType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47)
        )
    )
    namedValues = NamedValues(
        *(("attributeChanged", 15),
          ("boardDown", 2),
          ("boardRestart", 24),
          ("boardUp", 3),
          ("bootFileFail", 12),
          ("bootFileSucceeded", 13),
          ("coldStart", 1),
          ("configReadFail", 16),
          ("configReadSucceed", 17),
          ("configWriteFail", 18),
          ("configWriteSucceed", 19),
          ("dLCIStateDisabled", 21),
          ("dLCIStateEnabled", 22),
          ("diagnostic", 23),
          ("ds3LineStatusAlarm", 33),
          ("ds3LineStatusClear", 34),
          ("endPointConflictAlarm", 47),
          ("fallingThresholdAlert", 42),
          ("fanFault", 25),
          ("fanFaultClear", 26),
          ("idslTimingLossAlarm", 35),
          ("idslTimingLossClear", 36),
          ("linkDown", 4),
          ("linkUp", 5),
          ("loginAllowed", 11),
          ("loginFailed", 6),
          ("loginSucceeded", 7),
          ("loginSuspended", 10),
          ("loginsAvailable", 9),
          ("loginsSaturated", 8),
          ("logout", 14),
          ("loopStatusChange", 31),
          ("maintFailed", 41),
          ("maintSucceed", 40),
          ("powerSupplyClear", 28),
          ("powerSupplyFault", 27),
          ("rateFallbackAlarm", 43),
          ("rateFallbackClear", 44),
          ("redundancyChanged", 37),
          ("redundancyConflict", 39),
          ("risingThresholdAlert", 32),
          ("roleChanged", 38),
          ("stateChange", 20),
          ("testError", 30),
          ("testStatus", 29))
    )


_CmTrapEventLogType_Type.__name__ = "Integer32"
_CmTrapEventLogType_Object = MibTableColumn
cmTrapEventLogType = _CmTrapEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 2),
    _CmTrapEventLogType_Type()
)
cmTrapEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogType.setStatus("mandatory")


class _CmTrapEventLogObjectClass_Type(Integer32):
    """Custom type cmTrapEventLogObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmTrapEventLogObjectClass_Type.__name__ = "Integer32"
_CmTrapEventLogObjectClass_Object = MibTableColumn
cmTrapEventLogObjectClass = _CmTrapEventLogObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 3),
    _CmTrapEventLogObjectClass_Type()
)
cmTrapEventLogObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogObjectClass.setStatus("mandatory")
_CmTrapEventLogClassId_Type = CmObjectPII
_CmTrapEventLogClassId_Object = MibTableColumn
cmTrapEventLogClassId = _CmTrapEventLogClassId_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 4),
    _CmTrapEventLogClassId_Type()
)
cmTrapEventLogClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogClassId.setStatus("mandatory")
_CmTrapEventLogProbableCause_Type = Integer32
_CmTrapEventLogProbableCause_Object = MibTableColumn
cmTrapEventLogProbableCause = _CmTrapEventLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 5),
    _CmTrapEventLogProbableCause_Type()
)
cmTrapEventLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogProbableCause.setStatus("mandatory")


class _CmTrapEventLogSeverity_Type(Integer32):
    """Custom type cmTrapEventLogSeverity based on Integer32"""
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
        *(("critical", 6),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("none", 1),
          ("warning", 3))
    )


_CmTrapEventLogSeverity_Type.__name__ = "Integer32"
_CmTrapEventLogSeverity_Object = MibTableColumn
cmTrapEventLogSeverity = _CmTrapEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 6),
    _CmTrapEventLogSeverity_Type()
)
cmTrapEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogSeverity.setStatus("mandatory")
_CmTrapEventLogTimeTag_Type = DisplayString
_CmTrapEventLogTimeTag_Object = MibTableColumn
cmTrapEventLogTimeTag = _CmTrapEventLogTimeTag_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 7),
    _CmTrapEventLogTimeTag_Type()
)
cmTrapEventLogTimeTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogTimeTag.setStatus("mandatory")
_CmTrapEventLogText_Type = DisplayString
_CmTrapEventLogText_Object = MibTableColumn
cmTrapEventLogText = _CmTrapEventLogText_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 7, 1, 8),
    _CmTrapEventLogText_Type()
)
cmTrapEventLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapEventLogText.setStatus("mandatory")
_CmTrapAlarmLogTable_Object = MibTable
cmTrapAlarmLogTable = _CmTrapAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8)
)
if mibBuilder.loadTexts:
    cmTrapAlarmLogTable.setStatus("mandatory")
_CmTrapAlarmLogEntry_Object = MibTableRow
cmTrapAlarmLogEntry = _CmTrapAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1)
)
cmTrapAlarmLogEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapAlarmLogSeqNum"),
)
if mibBuilder.loadTexts:
    cmTrapAlarmLogEntry.setStatus("mandatory")
_CmTrapAlarmLogSeqNum_Type = Integer32
_CmTrapAlarmLogSeqNum_Object = MibTableColumn
cmTrapAlarmLogSeqNum = _CmTrapAlarmLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 1),
    _CmTrapAlarmLogSeqNum_Type()
)
cmTrapAlarmLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogSeqNum.setStatus("mandatory")


class _CmTrapAlarmLogType_Type(Integer32):
    """Custom type cmTrapAlarmLogType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47)
        )
    )
    namedValues = NamedValues(
        *(("attributeChanged", 15),
          ("boardDown", 2),
          ("boardRestart", 24),
          ("boardUp", 3),
          ("bootFileFail", 12),
          ("bootFileSucceeded", 13),
          ("coldStart", 1),
          ("configReadFail", 16),
          ("configReadSucceed", 17),
          ("configWriteFail", 18),
          ("configWriteSucceed", 19),
          ("dLCIStateDisabled", 21),
          ("dLCIStateEnabled", 22),
          ("diagnostic", 23),
          ("ds3LineStatusAlarm", 33),
          ("ds3LineStatusClear", 34),
          ("endPointConflictAlarm", 47),
          ("fallingThresholdAlert", 42),
          ("fanFault", 25),
          ("fanFaultClear", 26),
          ("idslTimingLossAlarm", 35),
          ("idslTimingLossClear", 36),
          ("linkDown", 4),
          ("linkUp", 5),
          ("loginAllowed", 11),
          ("loginFailed", 6),
          ("loginSucceeded", 7),
          ("loginSuspended", 10),
          ("loginsAvailable", 9),
          ("loginsSaturated", 8),
          ("logout", 14),
          ("loopStatusChange", 31),
          ("maintFailed", 41),
          ("maintSucceed", 40),
          ("powerSupplyClear", 28),
          ("powerSupplyFault", 27),
          ("rateFallbackAlarm", 43),
          ("rateFallbackClear", 44),
          ("redundancyChanged", 37),
          ("redundancyConflict", 39),
          ("risingThresholdAlert", 32),
          ("roleChanged", 38),
          ("stateChange", 20),
          ("testError", 30),
          ("testStatus", 29))
    )


_CmTrapAlarmLogType_Type.__name__ = "Integer32"
_CmTrapAlarmLogType_Object = MibTableColumn
cmTrapAlarmLogType = _CmTrapAlarmLogType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 2),
    _CmTrapAlarmLogType_Type()
)
cmTrapAlarmLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogType.setStatus("mandatory")


class _CmTrapAlarmLogObjectClass_Type(Integer32):
    """Custom type cmTrapAlarmLogObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmTrapAlarmLogObjectClass_Type.__name__ = "Integer32"
_CmTrapAlarmLogObjectClass_Object = MibTableColumn
cmTrapAlarmLogObjectClass = _CmTrapAlarmLogObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 3),
    _CmTrapAlarmLogObjectClass_Type()
)
cmTrapAlarmLogObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogObjectClass.setStatus("mandatory")
_CmTrapAlarmLogClassId_Type = CmObjectPII
_CmTrapAlarmLogClassId_Object = MibTableColumn
cmTrapAlarmLogClassId = _CmTrapAlarmLogClassId_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 4),
    _CmTrapAlarmLogClassId_Type()
)
cmTrapAlarmLogClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogClassId.setStatus("mandatory")
_CmTrapAlarmLogProbableCause_Type = Integer32
_CmTrapAlarmLogProbableCause_Object = MibTableColumn
cmTrapAlarmLogProbableCause = _CmTrapAlarmLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 5),
    _CmTrapAlarmLogProbableCause_Type()
)
cmTrapAlarmLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogProbableCause.setStatus("mandatory")


class _CmTrapAlarmLogSeverity_Type(Integer32):
    """Custom type cmTrapAlarmLogSeverity based on Integer32"""
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
        *(("critical", 6),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("none", 1),
          ("warning", 3))
    )


_CmTrapAlarmLogSeverity_Type.__name__ = "Integer32"
_CmTrapAlarmLogSeverity_Object = MibTableColumn
cmTrapAlarmLogSeverity = _CmTrapAlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 6),
    _CmTrapAlarmLogSeverity_Type()
)
cmTrapAlarmLogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrapAlarmLogSeverity.setStatus("mandatory")
_CmTrapAlarmLogTimeTag_Type = DisplayString
_CmTrapAlarmLogTimeTag_Object = MibTableColumn
cmTrapAlarmLogTimeTag = _CmTrapAlarmLogTimeTag_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 7),
    _CmTrapAlarmLogTimeTag_Type()
)
cmTrapAlarmLogTimeTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogTimeTag.setStatus("mandatory")
_CmTrapAlarmLogText_Type = DisplayString
_CmTrapAlarmLogText_Object = MibTableColumn
cmTrapAlarmLogText = _CmTrapAlarmLogText_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 8, 1, 8),
    _CmTrapAlarmLogText_Type()
)
cmTrapAlarmLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapAlarmLogText.setStatus("mandatory")
_CmTrapTypeLogTable_Object = MibTable
cmTrapTypeLogTable = _CmTrapTypeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9)
)
if mibBuilder.loadTexts:
    cmTrapTypeLogTable.setStatus("mandatory")
_CmTrapTypeLogEntry_Object = MibTableRow
cmTrapTypeLogEntry = _CmTrapTypeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1)
)
cmTrapTypeLogEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapTypeLogType"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapTypeLogSeqNum"),
)
if mibBuilder.loadTexts:
    cmTrapTypeLogEntry.setStatus("mandatory")


class _CmTrapTypeLogType_Type(Integer32):
    """Custom type cmTrapTypeLogType based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              47)
        )
    )
    namedValues = NamedValues(
        *(("attributeChanged", 15),
          ("boardDown", 2),
          ("boardRestart", 24),
          ("boardUp", 3),
          ("bootFileFail", 12),
          ("bootFileSucceeded", 13),
          ("coldStart", 1),
          ("configReadFail", 16),
          ("configReadSucceed", 17),
          ("configWriteFail", 18),
          ("configWriteSucceed", 19),
          ("dLCIStateDisabled", 21),
          ("dLCIStateEnabled", 22),
          ("diagnostic", 23),
          ("ds3LineStatusAlarm", 33),
          ("ds3LineStatusClear", 34),
          ("endPointConflictAlarm", 47),
          ("fallingThresholdAlert", 42),
          ("fanFault", 25),
          ("fanFaultClear", 26),
          ("idslTimingLossAlarm", 35),
          ("idslTimingLossClear", 36),
          ("linkDown", 4),
          ("linkUp", 5),
          ("loginAllowed", 11),
          ("loginFailed", 6),
          ("loginSucceeded", 7),
          ("loginSuspended", 10),
          ("loginsAvailable", 9),
          ("loginsSaturated", 8),
          ("logout", 14),
          ("loopStatusChange", 31),
          ("maintFailed", 41),
          ("maintSucceed", 40),
          ("powerSupplyClear", 28),
          ("powerSupplyFault", 27),
          ("rateFallbackAlarm", 43),
          ("rateFallbackClear", 44),
          ("redundancyChanged", 37),
          ("redundancyConflict", 39),
          ("risingThresholdAlert", 32),
          ("roleChanged", 38),
          ("stateChange", 20),
          ("testError", 30),
          ("testStatus", 29))
    )


_CmTrapTypeLogType_Type.__name__ = "Integer32"
_CmTrapTypeLogType_Object = MibTableColumn
cmTrapTypeLogType = _CmTrapTypeLogType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 1),
    _CmTrapTypeLogType_Type()
)
cmTrapTypeLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogType.setStatus("mandatory")
_CmTrapTypeLogSeqNum_Type = Integer32
_CmTrapTypeLogSeqNum_Object = MibTableColumn
cmTrapTypeLogSeqNum = _CmTrapTypeLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 2),
    _CmTrapTypeLogSeqNum_Type()
)
cmTrapTypeLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogSeqNum.setStatus("mandatory")


class _CmTrapTypeLogObjectClass_Type(Integer32):
    """Custom type cmTrapTypeLogObjectClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(256,
              512,
              513,
              514,
              768,
              769,
              770,
              771,
              772,
              773,
              774,
              775,
              776,
              777,
              778,
              779,
              780,
              781,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1280,
              1281,
              1282,
              1283,
              1284,
              1285,
              1286,
              1792,
              1793,
              1794,
              1795,
              1798,
              1799,
              1801,
              1802,
              2049,
              2304,
              2305,
              2306)
        )
    )
    namedValues = NamedValues(
        *(("board", 768),
          ("brdBufferControlModule", 772),
          ("brdCopperBaySCM", 780),
          ("brdDS3ATM-WAN", 779),
          ("brdDS3FR-WAN", 776),
          ("brdHSSI-WAN", 775),
          ("brdIDSLModule-24", 778),
          ("brdLANModule", 781),
          ("brdSDSL10xModule", 771),
          ("brdSDSL10xModule-1", 770),
          ("brdSDSL30xModule", 774),
          ("brdSDSL30xModule-24", 777),
          ("brdSystemControlModule", 769),
          ("brdV35-Wan", 773),
          ("ce150Shelf", 514),
          ("ce200Shelf", 513),
          ("cpe-IDSL", 1802),
          ("cpe-SDSL", 1801),
          ("cr", 1792),
          ("cr201-10x", 1793),
          ("cr201-30x", 1794),
          ("cr201-IDSL", 1799),
          ("cr201-SDSL", 1795),
          ("fanModule", 2306),
          ("interShelfTrunk", 1286),
          ("link", 1280),
          ("linkATM", 1285),
          ("linkDSL", 1281),
          ("linkEthernet", 1282),
          ("linkFrameRelay", 1283),
          ("linkVC", 1284),
          ("netopia-SDSL", 1798),
          ("operator", 2049),
          ("port", 1024),
          ("portDS3ATM-WAN", 1032),
          ("portDS3FR-WAN", 1030),
          ("portEthernet", 1026),
          ("portHSSI", 1029),
          ("portIDSL", 1031),
          ("portRS232", 1028),
          ("portSDSL", 1025),
          ("portV35", 1027),
          ("powerModule", 2305),
          ("service", 2304),
          ("shelf", 512),
          ("system", 256))
    )


_CmTrapTypeLogObjectClass_Type.__name__ = "Integer32"
_CmTrapTypeLogObjectClass_Object = MibTableColumn
cmTrapTypeLogObjectClass = _CmTrapTypeLogObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 3),
    _CmTrapTypeLogObjectClass_Type()
)
cmTrapTypeLogObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogObjectClass.setStatus("mandatory")
_CmTrapTypeLogClassId_Type = CmObjectPII
_CmTrapTypeLogClassId_Object = MibTableColumn
cmTrapTypeLogClassId = _CmTrapTypeLogClassId_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 4),
    _CmTrapTypeLogClassId_Type()
)
cmTrapTypeLogClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogClassId.setStatus("mandatory")
_CmTrapTypeLogProbableCause_Type = Integer32
_CmTrapTypeLogProbableCause_Object = MibTableColumn
cmTrapTypeLogProbableCause = _CmTrapTypeLogProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 5),
    _CmTrapTypeLogProbableCause_Type()
)
cmTrapTypeLogProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogProbableCause.setStatus("mandatory")


class _CmTrapTypeLogSeverity_Type(Integer32):
    """Custom type cmTrapTypeLogSeverity based on Integer32"""
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
        *(("critical", 6),
          ("information", 2),
          ("major", 5),
          ("minor", 4),
          ("none", 1),
          ("warning", 3))
    )


_CmTrapTypeLogSeverity_Type.__name__ = "Integer32"
_CmTrapTypeLogSeverity_Object = MibTableColumn
cmTrapTypeLogSeverity = _CmTrapTypeLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 6),
    _CmTrapTypeLogSeverity_Type()
)
cmTrapTypeLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogSeverity.setStatus("mandatory")
_CmTrapTypeLogTimeTag_Type = DisplayString
_CmTrapTypeLogTimeTag_Object = MibTableColumn
cmTrapTypeLogTimeTag = _CmTrapTypeLogTimeTag_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 7),
    _CmTrapTypeLogTimeTag_Type()
)
cmTrapTypeLogTimeTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogTimeTag.setStatus("mandatory")
_CmTrapTypeLogText_Type = DisplayString
_CmTrapTypeLogText_Object = MibTableColumn
cmTrapTypeLogText = _CmTrapTypeLogText_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 9, 1, 8),
    _CmTrapTypeLogText_Type()
)
cmTrapTypeLogText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapTypeLogText.setStatus("mandatory")
_CmTrapDestinationTable_Object = MibTable
cmTrapDestinationTable = _CmTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10)
)
if mibBuilder.loadTexts:
    cmTrapDestinationTable.setStatus("mandatory")
_CmTrapDestinationEntry_Object = MibTableRow
cmTrapDestinationEntry = _CmTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1)
)
cmTrapDestinationEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapDestinationIpAddr"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapDestinationPort"),
)
if mibBuilder.loadTexts:
    cmTrapDestinationEntry.setStatus("mandatory")
_CmTrapDestinationIpAddr_Type = IpAddress
_CmTrapDestinationIpAddr_Object = MibTableColumn
cmTrapDestinationIpAddr = _CmTrapDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1, 1),
    _CmTrapDestinationIpAddr_Type()
)
cmTrapDestinationIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapDestinationIpAddr.setStatus("mandatory")
_CmTrapDestinationPort_Type = Integer32
_CmTrapDestinationPort_Object = MibTableColumn
cmTrapDestinationPort = _CmTrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1, 2),
    _CmTrapDestinationPort_Type()
)
cmTrapDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrapDestinationPort.setStatus("mandatory")
_CmTrapDestinationCommunity_Type = DisplayString
_CmTrapDestinationCommunity_Object = MibTableColumn
cmTrapDestinationCommunity = _CmTrapDestinationCommunity_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1, 3),
    _CmTrapDestinationCommunity_Type()
)
cmTrapDestinationCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrapDestinationCommunity.setStatus("mandatory")


class _CmTrapDestinationRowStatus_Type(Integer32):
    """Custom type cmTrapDestinationRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 6),
          ("notInService", 2))
    )


_CmTrapDestinationRowStatus_Type.__name__ = "Integer32"
_CmTrapDestinationRowStatus_Object = MibTableColumn
cmTrapDestinationRowStatus = _CmTrapDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1, 4),
    _CmTrapDestinationRowStatus_Type()
)
cmTrapDestinationRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrapDestinationRowStatus.setStatus("mandatory")
_CmTrapDestinationOwnerString_Type = DisplayString
_CmTrapDestinationOwnerString_Object = MibTableColumn
cmTrapDestinationOwnerString = _CmTrapDestinationOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 9, 10, 1, 5),
    _CmTrapDestinationOwnerString_Type()
)
cmTrapDestinationOwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrapDestinationOwnerString.setStatus("mandatory")
_CmLoop_ObjectIdentity = ObjectIdentity
cmLoop = _CmLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10)
)
_CmLoopID_Type = Integer32
_CmLoopID_Object = MibScalar
cmLoopID = _CmLoopID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 1),
    _CmLoopID_Type()
)
cmLoopID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopID.setStatus("mandatory")
_CmLoopInterface_Type = Integer32
_CmLoopInterface_Object = MibScalar
cmLoopInterface = _CmLoopInterface_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 2),
    _CmLoopInterface_Type()
)
cmLoopInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopInterface.setStatus("mandatory")


class _CmLoopType_Type(Integer32):
    """Custom type cmLoopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("noLoop", 1),
          ("scm-CPE-BER", 5),
          ("scm-CR-Eth", 3),
          ("scm-DSLModuleEOC", 11),
          ("scm-DSLModulePort", 2),
          ("scm-WAN-Generator", 10),
          ("scm-WAN-LocalDigital", 7),
          ("scm-WAN-LocalLine", 8),
          ("scm-WAN-RemoteLine", 9))
    )


_CmLoopType_Type.__name__ = "Integer32"
_CmLoopType_Object = MibScalar
cmLoopType = _CmLoopType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 3),
    _CmLoopType_Type()
)
cmLoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopType.setStatus("mandatory")


class _CmLoopAction_Type(Integer32):
    """Custom type cmLoopAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 2),
          ("start", 3),
          ("stop", 4))
    )


_CmLoopAction_Type.__name__ = "Integer32"
_CmLoopAction_Object = MibScalar
cmLoopAction = _CmLoopAction_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 4),
    _CmLoopAction_Type()
)
cmLoopAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopAction.setStatus("mandatory")
_CmLoopDuration_Type = Integer32
_CmLoopDuration_Object = MibScalar
cmLoopDuration = _CmLoopDuration_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 5),
    _CmLoopDuration_Type()
)
cmLoopDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopDuration.setStatus("mandatory")


class _CmLoopStatus_Type(Integer32):
    """Custom type cmLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("idle", 1),
          ("inProgress", 2))
    )


_CmLoopStatus_Type.__name__ = "Integer32"
_CmLoopStatus_Object = MibScalar
cmLoopStatus = _CmLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 6),
    _CmLoopStatus_Type()
)
cmLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopStatus.setStatus("mandatory")
_CmLoopTimeElapsed_Type = TimeTicks
_CmLoopTimeElapsed_Object = MibScalar
cmLoopTimeElapsed = _CmLoopTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 7),
    _CmLoopTimeElapsed_Type()
)
cmLoopTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopTimeElapsed.setStatus("mandatory")


class _CmLoopTermCode_Type(Integer32):
    """Custom type cmLoopTermCode based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("berCountOverflow", 19),
          ("cpeDisabled", 11),
          ("cpeInitError", 8),
          ("cpeStartError", 9),
          ("dbSendError", 2),
          ("durationExpired", 3),
          ("idle", 14),
          ("inProgress", 1),
          ("lcDisabled", 12),
          ("lcInitError", 7),
          ("lcReportError", 18),
          ("lcSstartError", 10),
          ("mioDisabled", 16),
          ("mioInitError", 15),
          ("noCPEresponse", 6),
          ("noLCresponse", 5),
          ("noLinkStateChange", 13),
          ("noMIOResponse", 17),
          ("operatorStopped", 4))
    )


_CmLoopTermCode_Type.__name__ = "Integer32"
_CmLoopTermCode_Object = MibScalar
cmLoopTermCode = _CmLoopTermCode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 8),
    _CmLoopTermCode_Type()
)
cmLoopTermCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopTermCode.setStatus("mandatory")
_CmLoopTxCount_Type = Integer32
_CmLoopTxCount_Object = MibScalar
cmLoopTxCount = _CmLoopTxCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 9),
    _CmLoopTxCount_Type()
)
cmLoopTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopTxCount.setStatus("mandatory")
_CmLoopRxErrors_Type = Integer32
_CmLoopRxErrors_Object = MibScalar
cmLoopRxErrors = _CmLoopRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 10),
    _CmLoopRxErrors_Type()
)
cmLoopRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopRxErrors.setStatus("mandatory")
_CmLoopOwnerString_Type = DisplayString
_CmLoopOwnerString_Object = MibScalar
cmLoopOwnerString = _CmLoopOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 11),
    _CmLoopOwnerString_Type()
)
cmLoopOwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopOwnerString.setStatus("mandatory")
_CmLoopHistTable_Object = MibTable
cmLoopHistTable = _CmLoopHistTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12)
)
if mibBuilder.loadTexts:
    cmLoopHistTable.setStatus("mandatory")
_CmLoopHistEntry_Object = MibTableRow
cmLoopHistEntry = _CmLoopHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1)
)
cmLoopHistEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopID"),
)
if mibBuilder.loadTexts:
    cmLoopHistEntry.setStatus("mandatory")
_CmLoopHistID_Type = Integer32
_CmLoopHistID_Object = MibTableColumn
cmLoopHistID = _CmLoopHistID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 1),
    _CmLoopHistID_Type()
)
cmLoopHistID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistID.setStatus("mandatory")
_CmLoopHistInterface_Type = Integer32
_CmLoopHistInterface_Object = MibTableColumn
cmLoopHistInterface = _CmLoopHistInterface_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 2),
    _CmLoopHistInterface_Type()
)
cmLoopHistInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistInterface.setStatus("mandatory")


class _CmLoopHistType_Type(Integer32):
    """Custom type cmLoopHistType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("noLoop", 1),
          ("scm-CPE-BER", 5),
          ("scm-CR-Eth", 3),
          ("scm-DSLModuleEOC", 11),
          ("scm-DSLModulePort", 2),
          ("scm-WAN-Generator", 10),
          ("scm-WAN-LocalDigital", 7),
          ("scm-WAN-LocalLine", 8),
          ("scm-WAN-RemoteLine", 9))
    )


_CmLoopHistType_Type.__name__ = "Integer32"
_CmLoopHistType_Object = MibTableColumn
cmLoopHistType = _CmLoopHistType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 3),
    _CmLoopHistType_Type()
)
cmLoopHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistType.setStatus("mandatory")


class _CmLoopHistAction_Type(Integer32):
    """Custom type cmLoopHistAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("init", 2),
          ("start", 3),
          ("stop", 4))
    )


_CmLoopHistAction_Type.__name__ = "Integer32"
_CmLoopHistAction_Object = MibTableColumn
cmLoopHistAction = _CmLoopHistAction_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 4),
    _CmLoopHistAction_Type()
)
cmLoopHistAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistAction.setStatus("mandatory")
_CmLoopHistDuration_Type = Integer32
_CmLoopHistDuration_Object = MibTableColumn
cmLoopHistDuration = _CmLoopHistDuration_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 5),
    _CmLoopHistDuration_Type()
)
cmLoopHistDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistDuration.setStatus("mandatory")


class _CmLoopHistStatus_Type(Integer32):
    """Custom type cmLoopHistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 3),
          ("idle", 1),
          ("inProgress", 2))
    )


_CmLoopHistStatus_Type.__name__ = "Integer32"
_CmLoopHistStatus_Object = MibTableColumn
cmLoopHistStatus = _CmLoopHistStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 6),
    _CmLoopHistStatus_Type()
)
cmLoopHistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistStatus.setStatus("mandatory")
_CmLoopHistTimeElapsed_Type = TimeTicks
_CmLoopHistTimeElapsed_Object = MibTableColumn
cmLoopHistTimeElapsed = _CmLoopHistTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 7),
    _CmLoopHistTimeElapsed_Type()
)
cmLoopHistTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistTimeElapsed.setStatus("mandatory")


class _CmLoopHistTermCode_Type(Integer32):
    """Custom type cmLoopHistTermCode based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("berCountOverflow", 19),
          ("cpeDisabled", 11),
          ("cpeInitError", 8),
          ("cpeStartError", 9),
          ("dbSendError", 2),
          ("durationExpired", 3),
          ("idle", 14),
          ("inProgress", 1),
          ("lcDisabled", 12),
          ("lcInitError", 7),
          ("lcReportError", 18),
          ("lcSstartError", 10),
          ("mioDisabled", 16),
          ("mioInitError", 15),
          ("noCPEresponse", 6),
          ("noLCresponse", 5),
          ("noLinkStateChange", 13),
          ("noMIOResponse", 17),
          ("operatorStopped", 4))
    )


_CmLoopHistTermCode_Type.__name__ = "Integer32"
_CmLoopHistTermCode_Object = MibTableColumn
cmLoopHistTermCode = _CmLoopHistTermCode_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 8),
    _CmLoopHistTermCode_Type()
)
cmLoopHistTermCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistTermCode.setStatus("mandatory")
_CmLoopHistTxCount_Type = Integer32
_CmLoopHistTxCount_Object = MibTableColumn
cmLoopHistTxCount = _CmLoopHistTxCount_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 9),
    _CmLoopHistTxCount_Type()
)
cmLoopHistTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistTxCount.setStatus("mandatory")
_CmLoopHistRxErrors_Type = Integer32
_CmLoopHistRxErrors_Object = MibTableColumn
cmLoopHistRxErrors = _CmLoopHistRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 10),
    _CmLoopHistRxErrors_Type()
)
cmLoopHistRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistRxErrors.setStatus("mandatory")
_CmLoopHistOwnerString_Type = DisplayString
_CmLoopHistOwnerString_Object = MibTableColumn
cmLoopHistOwnerString = _CmLoopHistOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 11),
    _CmLoopHistOwnerString_Type()
)
cmLoopHistOwnerString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistOwnerString.setStatus("mandatory")


class _CmLoopHistTestParameter1_Type(Integer32):
    """Custom type cmLoopHistTestParameter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmLoopHistTestParameter1_Type.__name__ = "Integer32"
_CmLoopHistTestParameter1_Object = MibTableColumn
cmLoopHistTestParameter1 = _CmLoopHistTestParameter1_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 12),
    _CmLoopHistTestParameter1_Type()
)
cmLoopHistTestParameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistTestParameter1.setStatus("mandatory")


class _CmLoopHistErrorInfo_Type(Integer32):
    """Custom type cmLoopHistErrorInfo based on Integer32"""
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
        *(("eocAddr2Big", 5),
          ("illegalTestParameter1", 2),
          ("modemIsNT", 3),
          ("modemUntrained", 4),
          ("none", 1))
    )


_CmLoopHistErrorInfo_Type.__name__ = "Integer32"
_CmLoopHistErrorInfo_Object = MibTableColumn
cmLoopHistErrorInfo = _CmLoopHistErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 12, 1, 13),
    _CmLoopHistErrorInfo_Type()
)
cmLoopHistErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopHistErrorInfo.setStatus("mandatory")


class _CmLoopTestParameter1_Type(Integer32):
    """Custom type cmLoopTestParameter1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmLoopTestParameter1_Type.__name__ = "Integer32"
_CmLoopTestParameter1_Object = MibScalar
cmLoopTestParameter1 = _CmLoopTestParameter1_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 13),
    _CmLoopTestParameter1_Type()
)
cmLoopTestParameter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmLoopTestParameter1.setStatus("mandatory")


class _CmLoopErrorInfo_Type(Integer32):
    """Custom type cmLoopErrorInfo based on Integer32"""
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
        *(("eocAddr2Big", 5),
          ("illegalTestParameter1", 2),
          ("modemIsNT", 3),
          ("modemUntrained", 4),
          ("none", 1))
    )


_CmLoopErrorInfo_Type.__name__ = "Integer32"
_CmLoopErrorInfo_Object = MibScalar
cmLoopErrorInfo = _CmLoopErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 10, 14),
    _CmLoopErrorInfo_Type()
)
cmLoopErrorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmLoopErrorInfo.setStatus("mandatory")
_CmVBridge_ObjectIdentity = ObjectIdentity
cmVBridge = _CmVBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11)
)
_CmVBridgeTable_Object = MibTable
cmVBridgeTable = _CmVBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1)
)
if mibBuilder.loadTexts:
    cmVBridgeTable.setStatus("mandatory")
_CmVBridgeEntry_Object = MibTableRow
cmVBridgeEntry = _CmVBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1)
)
cmVBridgeEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmVBridgePII"),
)
if mibBuilder.loadTexts:
    cmVBridgeEntry.setStatus("mandatory")
_CmVBridgePII_Type = Integer32
_CmVBridgePII_Object = MibTableColumn
cmVBridgePII = _CmVBridgePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 1),
    _CmVBridgePII_Type()
)
cmVBridgePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgePII.setStatus("mandatory")
_CmVBridgeNMAC_Type = Integer32
_CmVBridgeNMAC_Object = MibTableColumn
cmVBridgeNMAC = _CmVBridgeNMAC_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 2),
    _CmVBridgeNMAC_Type()
)
cmVBridgeNMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNMAC.setStatus("mandatory")
_CmVBridgeNMulticast_Type = Integer32
_CmVBridgeNMulticast_Object = MibTableColumn
cmVBridgeNMulticast = _CmVBridgeNMulticast_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 3),
    _CmVBridgeNMulticast_Type()
)
cmVBridgeNMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNMulticast.setStatus("mandatory")
_CmVBridgeNUnicast_Type = Integer32
_CmVBridgeNUnicast_Object = MibTableColumn
cmVBridgeNUnicast = _CmVBridgeNUnicast_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 4),
    _CmVBridgeNUnicast_Type()
)
cmVBridgeNUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNUnicast.setStatus("mandatory")
_CmVBridgeNDSL_Type = Integer32
_CmVBridgeNDSL_Object = MibTableColumn
cmVBridgeNDSL = _CmVBridgeNDSL_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 5),
    _CmVBridgeNDSL_Type()
)
cmVBridgeNDSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNDSL.setStatus("mandatory")
_CmVBridgeNUnknownDest_Type = Integer32
_CmVBridgeNUnknownDest_Object = MibTableColumn
cmVBridgeNUnknownDest = _CmVBridgeNUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 6),
    _CmVBridgeNUnknownDest_Type()
)
cmVBridgeNUnknownDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNUnknownDest.setStatus("mandatory")
_CmVBridgeNOverflow_Type = Integer32
_CmVBridgeNOverflow_Object = MibTableColumn
cmVBridgeNOverflow = _CmVBridgeNOverflow_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 7),
    _CmVBridgeNOverflow_Type()
)
cmVBridgeNOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmVBridgeNOverflow.setStatus("mandatory")


class _CmVBridgeOption_Type(Integer32):
    """Custom type cmVBridgeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipSpecial", 2),
          ("none", 1))
    )


_CmVBridgeOption_Type.__name__ = "Integer32"
_CmVBridgeOption_Object = MibTableColumn
cmVBridgeOption = _CmVBridgeOption_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 11, 1, 1, 8),
    _CmVBridgeOption_Type()
)
cmVBridgeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmVBridgeOption.setStatus("mandatory")
_CmMAC_ObjectIdentity = ObjectIdentity
cmMAC = _CmMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12)
)
_CmMACTable_Object = MibTable
cmMACTable = _CmMACTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1)
)
if mibBuilder.loadTexts:
    cmMACTable.setStatus("mandatory")
_CmMACEntry_Object = MibTableRow
cmMACEntry = _CmMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1)
)
cmMACEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMACPII"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMACIndex"),
)
if mibBuilder.loadTexts:
    cmMACEntry.setStatus("mandatory")
_CmMACPII_Type = Integer32
_CmMACPII_Object = MibTableColumn
cmMACPII = _CmMACPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1, 1),
    _CmMACPII_Type()
)
cmMACPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMACPII.setStatus("mandatory")
_CmMACIndex_Type = Integer32
_CmMACIndex_Object = MibTableColumn
cmMACIndex = _CmMACIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1, 2),
    _CmMACIndex_Type()
)
cmMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMACIndex.setStatus("mandatory")
_CmMACMAC_Type = OctetString
_CmMACMAC_Object = MibTableColumn
cmMACMAC = _CmMACMAC_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1, 3),
    _CmMACMAC_Type()
)
cmMACMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMACMAC.setStatus("mandatory")
_CmMACTTL_Type = Integer32
_CmMACTTL_Object = MibTableColumn
cmMACTTL = _CmMACTTL_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1, 4),
    _CmMACTTL_Type()
)
cmMACTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMACTTL.setStatus("mandatory")
_CmMACDslPII_Type = Integer32
_CmMACDslPII_Object = MibTableColumn
cmMACDslPII = _CmMACDslPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 12, 1, 1, 5),
    _CmMACDslPII_Type()
)
cmMACDslPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMACDslPII.setStatus("mandatory")
_CmAlarm_ObjectIdentity = ObjectIdentity
cmAlarm = _CmAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13)
)
_CmAlarmTable_Object = MibTable
cmAlarmTable = _CmAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1)
)
if mibBuilder.loadTexts:
    cmAlarmTable.setStatus("mandatory")
_CmAlarmEntry_Object = MibTableRow
cmAlarmEntry = _CmAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1)
)
cmAlarmEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmIndex"),
)
if mibBuilder.loadTexts:
    cmAlarmEntry.setStatus("mandatory")


class _CmAlarmIndex_Type(Integer32):
    """Custom type cmAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CmAlarmIndex_Type.__name__ = "Integer32"
_CmAlarmIndex_Object = MibTableColumn
cmAlarmIndex = _CmAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 1),
    _CmAlarmIndex_Type()
)
cmAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmIndex.setStatus("mandatory")
_CmAlarmInterval_Type = Integer32
_CmAlarmInterval_Object = MibTableColumn
cmAlarmInterval = _CmAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 2),
    _CmAlarmInterval_Type()
)
cmAlarmInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmInterval.setStatus("mandatory")
_CmAlarmVariable_Type = ObjectIdentifier
_CmAlarmVariable_Object = MibTableColumn
cmAlarmVariable = _CmAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 3),
    _CmAlarmVariable_Type()
)
cmAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmVariable.setStatus("mandatory")


class _CmAlarmSampleType_Type(Integer32):
    """Custom type cmAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("absoluteValue", 1)
    )


_CmAlarmSampleType_Type.__name__ = "Integer32"
_CmAlarmSampleType_Object = MibTableColumn
cmAlarmSampleType = _CmAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 4),
    _CmAlarmSampleType_Type()
)
cmAlarmSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmSampleType.setStatus("mandatory")
_CmAlarmValue_Type = Integer32
_CmAlarmValue_Object = MibTableColumn
cmAlarmValue = _CmAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 5),
    _CmAlarmValue_Type()
)
cmAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmValue.setStatus("mandatory")


class _CmAlarmStartupAlarm_Type(Integer32):
    """Custom type cmAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1))
    )


_CmAlarmStartupAlarm_Type.__name__ = "Integer32"
_CmAlarmStartupAlarm_Object = MibTableColumn
cmAlarmStartupAlarm = _CmAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 6),
    _CmAlarmStartupAlarm_Type()
)
cmAlarmStartupAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmAlarmStartupAlarm.setStatus("mandatory")


class _CmAlarmRisingThreshold_Type(Integer32):
    """Custom type cmAlarmRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmAlarmRisingThreshold_Type.__name__ = "Integer32"
_CmAlarmRisingThreshold_Object = MibTableColumn
cmAlarmRisingThreshold = _CmAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 7),
    _CmAlarmRisingThreshold_Type()
)
cmAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmRisingThreshold.setStatus("mandatory")


class _CmAlarmFallingThreshold_Type(Integer32):
    """Custom type cmAlarmFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_CmAlarmFallingThreshold_Type.__name__ = "Integer32"
_CmAlarmFallingThreshold_Object = MibTableColumn
cmAlarmFallingThreshold = _CmAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 8),
    _CmAlarmFallingThreshold_Type()
)
cmAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmFallingThreshold.setStatus("mandatory")
_CmAlarmStatus_Type = EntryStatus
_CmAlarmStatus_Object = MibTableColumn
cmAlarmStatus = _CmAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 1, 1, 12),
    _CmAlarmStatus_Type()
)
cmAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmStatus.setStatus("mandatory")


class _CmAlarmSwitch_Type(Integer32):
    """Custom type cmAlarmSwitch based on Integer32"""
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


_CmAlarmSwitch_Type.__name__ = "Integer32"
_CmAlarmSwitch_Object = MibScalar
cmAlarmSwitch = _CmAlarmSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 2),
    _CmAlarmSwitch_Type()
)
cmAlarmSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmSwitch.setStatus("mandatory")
_CmAlarmSamplingInterval_Type = Integer32
_CmAlarmSamplingInterval_Object = MibScalar
cmAlarmSamplingInterval = _CmAlarmSamplingInterval_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 13, 3),
    _CmAlarmSamplingInterval_Type()
)
cmAlarmSamplingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAlarmSamplingInterval.setStatus("mandatory")
_CmEvent_ObjectIdentity = ObjectIdentity
cmEvent = _CmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 14)
)
_CmUserGroup_ObjectIdentity = ObjectIdentity
cmUserGroup = _CmUserGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15)
)
_CmNameTable_Object = MibTable
cmNameTable = _CmNameTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 1)
)
if mibBuilder.loadTexts:
    cmNameTable.setStatus("mandatory")
_CmNameEntry_Object = MibTableRow
cmNameEntry = _CmNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 1, 1)
)
cmNameEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNameIfName"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNamePII"),
)
if mibBuilder.loadTexts:
    cmNameEntry.setStatus("mandatory")
_CmNameIfName_Type = DisplayString
_CmNameIfName_Object = MibTableColumn
cmNameIfName = _CmNameIfName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 1, 1, 1),
    _CmNameIfName_Type()
)
cmNameIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNameIfName.setStatus("mandatory")
_CmNamePII_Type = CmObjectPII
_CmNamePII_Object = MibTableColumn
cmNamePII = _CmNamePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 1, 1, 2),
    _CmNamePII_Type()
)
cmNamePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmNamePII.setStatus("mandatory")
_CmGroupTable_Object = MibTable
cmGroupTable = _CmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 2)
)
if mibBuilder.loadTexts:
    cmGroupTable.setStatus("mandatory")
_CmGroupEntry_Object = MibTableRow
cmGroupEntry = _CmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 2, 1)
)
cmGroupEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
)
if mibBuilder.loadTexts:
    cmGroupEntry.setStatus("mandatory")


class _CmGroupName_Type(DisplayString):
    """Custom type cmGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_CmGroupName_Type.__name__ = "DisplayString"
_CmGroupName_Object = MibTableColumn
cmGroupName = _CmGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 2, 1, 1),
    _CmGroupName_Type()
)
cmGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmGroupName.setStatus("mandatory")
_CmGroupNewGrpName_Type = DisplayString
_CmGroupNewGrpName_Object = MibTableColumn
cmGroupNewGrpName = _CmGroupNewGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 2, 1, 2),
    _CmGroupNewGrpName_Type()
)
cmGroupNewGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGroupNewGrpName.setStatus("mandatory")


class _CmGroupRowStatus_Type(Integer32):
    """Custom type cmGroupRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CmGroupRowStatus_Type.__name__ = "Integer32"
_CmGroupRowStatus_Object = MibTableColumn
cmGroupRowStatus = _CmGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 2, 1, 3),
    _CmGroupRowStatus_Type()
)
cmGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmGroupRowStatus.setStatus("mandatory")
_CmMemberTable_Object = MibTable
cmMemberTable = _CmMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 3)
)
if mibBuilder.loadTexts:
    cmMemberTable.setStatus("mandatory")
_CmMemberEntry_Object = MibTableRow
cmMemberEntry = _CmMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 3, 1)
)
cmMemberEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMemberPII"),
)
if mibBuilder.loadTexts:
    cmMemberEntry.setStatus("mandatory")
_CmMemberGrpName_Type = DisplayString
_CmMemberGrpName_Object = MibTableColumn
cmMemberGrpName = _CmMemberGrpName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 3, 1, 1),
    _CmMemberGrpName_Type()
)
cmMemberGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMemberGrpName.setStatus("mandatory")
_CmMemberPII_Type = CmObjectPII
_CmMemberPII_Object = MibTableColumn
cmMemberPII = _CmMemberPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 3, 1, 2),
    _CmMemberPII_Type()
)
cmMemberPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMemberPII.setStatus("mandatory")


class _CmMemberRowStatus_Type(Integer32):
    """Custom type cmMemberRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CmMemberRowStatus_Type.__name__ = "Integer32"
_CmMemberRowStatus_Object = MibTableColumn
cmMemberRowStatus = _CmMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 15, 3, 1, 3),
    _CmMemberRowStatus_Type()
)
cmMemberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMemberRowStatus.setStatus("mandatory")
_CmMaint_ObjectIdentity = ObjectIdentity
cmMaint = _CmMaint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16)
)
_CmMaintCmdTable_Object = MibTable
cmMaintCmdTable = _CmMaintCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1)
)
if mibBuilder.loadTexts:
    cmMaintCmdTable.setStatus("mandatory")
_CmMaintCmdEntry_Object = MibTableRow
cmMaintCmdEntry = _CmMaintCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1)
)
cmMaintCmdEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMaintCmdCommand"),
)
if mibBuilder.loadTexts:
    cmMaintCmdEntry.setStatus("mandatory")


class _CmMaintCmdCommand_Type(Integer32):
    """Custom type cmMaintCmdCommand based on Integer32"""
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
        *(("bulkCPEDownload", 5),
          ("configBackup", 3),
          ("configRestore", 4),
          ("statsAuto", 1),
          ("statsManual", 2))
    )


_CmMaintCmdCommand_Type.__name__ = "Integer32"
_CmMaintCmdCommand_Object = MibTableColumn
cmMaintCmdCommand = _CmMaintCmdCommand_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 1),
    _CmMaintCmdCommand_Type()
)
cmMaintCmdCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMaintCmdCommand.setStatus("mandatory")


class _CmMaintCmdRowStatus_Type(Integer32):
    """Custom type cmMaintCmdRowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CmMaintCmdRowStatus_Type.__name__ = "Integer32"
_CmMaintCmdRowStatus_Object = MibTableColumn
cmMaintCmdRowStatus = _CmMaintCmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 2),
    _CmMaintCmdRowStatus_Type()
)
cmMaintCmdRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdRowStatus.setStatus("mandatory")
_CmMaintCmdStartTime_Type = DisplayString
_CmMaintCmdStartTime_Object = MibTableColumn
cmMaintCmdStartTime = _CmMaintCmdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 3),
    _CmMaintCmdStartTime_Type()
)
cmMaintCmdStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdStartTime.setStatus("mandatory")
_CmMaintCmdRecurrence_Type = Integer32
_CmMaintCmdRecurrence_Object = MibTableColumn
cmMaintCmdRecurrence = _CmMaintCmdRecurrence_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 4),
    _CmMaintCmdRecurrence_Type()
)
cmMaintCmdRecurrence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdRecurrence.setStatus("mandatory")
_CmMaintCmdReportingPeriod_Type = Integer32
_CmMaintCmdReportingPeriod_Object = MibTableColumn
cmMaintCmdReportingPeriod = _CmMaintCmdReportingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 5),
    _CmMaintCmdReportingPeriod_Type()
)
cmMaintCmdReportingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdReportingPeriod.setStatus("mandatory")
_CmMaintCmdPrimaryIpAddr_Type = IpAddress
_CmMaintCmdPrimaryIpAddr_Object = MibTableColumn
cmMaintCmdPrimaryIpAddr = _CmMaintCmdPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 6),
    _CmMaintCmdPrimaryIpAddr_Type()
)
cmMaintCmdPrimaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdPrimaryIpAddr.setStatus("mandatory")
_CmMaintCmdSecondaryIpAddr_Type = IpAddress
_CmMaintCmdSecondaryIpAddr_Object = MibTableColumn
cmMaintCmdSecondaryIpAddr = _CmMaintCmdSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 7),
    _CmMaintCmdSecondaryIpAddr_Type()
)
cmMaintCmdSecondaryIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdSecondaryIpAddr.setStatus("mandatory")
_CmMaintCmdDirectory_Type = DisplayString
_CmMaintCmdDirectory_Object = MibTableColumn
cmMaintCmdDirectory = _CmMaintCmdDirectory_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 8),
    _CmMaintCmdDirectory_Type()
)
cmMaintCmdDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdDirectory.setStatus("mandatory")
_CmMaintCmdBaseFileName_Type = DisplayString
_CmMaintCmdBaseFileName_Object = MibTableColumn
cmMaintCmdBaseFileName = _CmMaintCmdBaseFileName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 9),
    _CmMaintCmdBaseFileName_Type()
)
cmMaintCmdBaseFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdBaseFileName.setStatus("mandatory")
_CmMaintCmdUserName_Type = DisplayString
_CmMaintCmdUserName_Object = MibTableColumn
cmMaintCmdUserName = _CmMaintCmdUserName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 10),
    _CmMaintCmdUserName_Type()
)
cmMaintCmdUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdUserName.setStatus("mandatory")
_CmMaintCmdPassword_Type = DisplayString
_CmMaintCmdPassword_Object = MibTableColumn
cmMaintCmdPassword = _CmMaintCmdPassword_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 11),
    _CmMaintCmdPassword_Type()
)
cmMaintCmdPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintCmdPassword.setStatus("mandatory")
_CmMaintCmdPreviousTime_Type = DisplayString
_CmMaintCmdPreviousTime_Object = MibTableColumn
cmMaintCmdPreviousTime = _CmMaintCmdPreviousTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 12),
    _CmMaintCmdPreviousTime_Type()
)
cmMaintCmdPreviousTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMaintCmdPreviousTime.setStatus("mandatory")
_CmMaintCmdNextTime_Type = DisplayString
_CmMaintCmdNextTime_Object = MibTableColumn
cmMaintCmdNextTime = _CmMaintCmdNextTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 13),
    _CmMaintCmdNextTime_Type()
)
cmMaintCmdNextTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMaintCmdNextTime.setStatus("mandatory")


class _CmMaintCmdCommandStatus_Type(Integer32):
    """Custom type cmMaintCmdCommandStatus based on Integer32"""
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
        *(("aborted", 7),
          ("failed", 4),
          ("inProgress", 5),
          ("none", 1),
          ("savedToPrimary", 2),
          ("savedToSecondary", 3),
          ("succeeded", 6))
    )


_CmMaintCmdCommandStatus_Type.__name__ = "Integer32"
_CmMaintCmdCommandStatus_Object = MibTableColumn
cmMaintCmdCommandStatus = _CmMaintCmdCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 14),
    _CmMaintCmdCommandStatus_Type()
)
cmMaintCmdCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMaintCmdCommandStatus.setStatus("mandatory")


class _CmMaintCmdStatusText_Type(DisplayString):
    """Custom type cmMaintCmdStatusText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmMaintCmdStatusText_Type.__name__ = "DisplayString"
_CmMaintCmdStatusText_Object = MibTableColumn
cmMaintCmdStatusText = _CmMaintCmdStatusText_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 1, 1, 15),
    _CmMaintCmdStatusText_Type()
)
cmMaintCmdStatusText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmMaintCmdStatusText.setStatus("mandatory")


class _CmMaintStatsDelimiter_Type(DisplayString):
    """Custom type cmMaintStatsDelimiter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CmMaintStatsDelimiter_Type.__name__ = "DisplayString"
_CmMaintStatsDelimiter_Object = MibScalar
cmMaintStatsDelimiter = _CmMaintStatsDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 16, 2),
    _CmMaintStatsDelimiter_Type()
)
cmMaintStatsDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmMaintStatsDelimiter.setStatus("mandatory")
_CmProxyArp_ObjectIdentity = ObjectIdentity
cmProxyArp = _CmProxyArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 17)
)
_CmProxyArpTable_Object = MibTable
cmProxyArpTable = _CmProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 17, 1)
)
if mibBuilder.loadTexts:
    cmProxyArpTable.setStatus("mandatory")
_CmProxyArpEntry_Object = MibTableRow
cmProxyArpEntry = _CmProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 17, 1, 1)
)
cmProxyArpEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmProxyArpPII"),
)
if mibBuilder.loadTexts:
    cmProxyArpEntry.setStatus("mandatory")
_CmProxyArpPII_Type = CmObjectPII
_CmProxyArpPII_Object = MibTableColumn
cmProxyArpPII = _CmProxyArpPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 17, 1, 1, 1),
    _CmProxyArpPII_Type()
)
cmProxyArpPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmProxyArpPII.setStatus("mandatory")


class _CmProxyArpRowStatus_Type(Integer32):
    """Custom type cmProxyArpRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_CmProxyArpRowStatus_Type.__name__ = "Integer32"
_CmProxyArpRowStatus_Object = MibTableColumn
cmProxyArpRowStatus = _CmProxyArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 17, 1, 1, 2),
    _CmProxyArpRowStatus_Type()
)
cmProxyArpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmProxyArpRowStatus.setStatus("mandatory")
_CmMultiShelf_ObjectIdentity = ObjectIdentity
cmMultiShelf = _CmMultiShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18)
)
_CmTrunkIfTable_Object = MibTable
cmTrunkIfTable = _CmTrunkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1)
)
if mibBuilder.loadTexts:
    cmTrunkIfTable.setStatus("mandatory")
_CmTrunkIfEntry_Object = MibTableRow
cmTrunkIfEntry = _CmTrunkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1)
)
cmTrunkIfEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrunkIfIndex"),
)
if mibBuilder.loadTexts:
    cmTrunkIfEntry.setStatus("mandatory")
_CmTrunkIfIndex_Type = CmObjectPII
_CmTrunkIfIndex_Object = MibTableColumn
cmTrunkIfIndex = _CmTrunkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 1),
    _CmTrunkIfIndex_Type()
)
cmTrunkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfIndex.setStatus("mandatory")


class _CmTrunkIfOperState_Type(Integer32):
    """Custom type cmTrunkIfOperState based on Integer32"""
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


_CmTrunkIfOperState_Type.__name__ = "Integer32"
_CmTrunkIfOperState_Object = MibTableColumn
cmTrunkIfOperState = _CmTrunkIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 2),
    _CmTrunkIfOperState_Type()
)
cmTrunkIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfOperState.setStatus("mandatory")


class _CmTrunkIfAdminState_Type(Integer32):
    """Custom type cmTrunkIfAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CmTrunkIfAdminState_Type.__name__ = "Integer32"
_CmTrunkIfAdminState_Object = MibTableColumn
cmTrunkIfAdminState = _CmTrunkIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 3),
    _CmTrunkIfAdminState_Type()
)
cmTrunkIfAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmTrunkIfAdminState.setStatus("mandatory")
_CmTrunkIfSentPackets_Type = Counter32
_CmTrunkIfSentPackets_Object = MibTableColumn
cmTrunkIfSentPackets = _CmTrunkIfSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 4),
    _CmTrunkIfSentPackets_Type()
)
cmTrunkIfSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfSentPackets.setStatus("mandatory")
_CmTrunkIfSentError_Type = Counter32
_CmTrunkIfSentError_Object = MibTableColumn
cmTrunkIfSentError = _CmTrunkIfSentError_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 5),
    _CmTrunkIfSentError_Type()
)
cmTrunkIfSentError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfSentError.setStatus("mandatory")
_CmTrunkIfRecvPackets_Type = Counter32
_CmTrunkIfRecvPackets_Object = MibTableColumn
cmTrunkIfRecvPackets = _CmTrunkIfRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 6),
    _CmTrunkIfRecvPackets_Type()
)
cmTrunkIfRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfRecvPackets.setStatus("mandatory")
_CmTrunkIfRecvError_Type = Counter32
_CmTrunkIfRecvError_Object = MibTableColumn
cmTrunkIfRecvError = _CmTrunkIfRecvError_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 1, 1, 7),
    _CmTrunkIfRecvError_Type()
)
cmTrunkIfRecvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkIfRecvError.setStatus("mandatory")
_CmTrunkConnectionTable_Object = MibTable
cmTrunkConnectionTable = _CmTrunkConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2)
)
if mibBuilder.loadTexts:
    cmTrunkConnectionTable.setStatus("mandatory")
_CmTrunkConnectionEntry_Object = MibTableRow
cmTrunkConnectionEntry = _CmTrunkConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1)
)
cmTrunkConnectionEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrunkConnectionTrunkMaster"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrunkConnectionIndex"),
)
if mibBuilder.loadTexts:
    cmTrunkConnectionEntry.setStatus("mandatory")
_CmTrunkConnectionTrunkMaster_Type = CmObjectPII
_CmTrunkConnectionTrunkMaster_Object = MibTableColumn
cmTrunkConnectionTrunkMaster = _CmTrunkConnectionTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1, 1),
    _CmTrunkConnectionTrunkMaster_Type()
)
cmTrunkConnectionTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkConnectionTrunkMaster.setStatus("mandatory")


class _CmTrunkConnectionIndex_Type(Integer32):
    """Custom type cmTrunkConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmTrunkConnectionIndex_Type.__name__ = "Integer32"
_CmTrunkConnectionIndex_Object = MibTableColumn
cmTrunkConnectionIndex = _CmTrunkConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1, 2),
    _CmTrunkConnectionIndex_Type()
)
cmTrunkConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkConnectionIndex.setStatus("mandatory")


class _CmTrunkConnectionOperState_Type(Integer32):
    """Custom type cmTrunkConnectionOperState based on Integer32"""
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


_CmTrunkConnectionOperState_Type.__name__ = "Integer32"
_CmTrunkConnectionOperState_Object = MibTableColumn
cmTrunkConnectionOperState = _CmTrunkConnectionOperState_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1, 3),
    _CmTrunkConnectionOperState_Type()
)
cmTrunkConnectionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkConnectionOperState.setStatus("mandatory")
_CmTrunkConnectionLowPII_Type = CmObjectPII
_CmTrunkConnectionLowPII_Object = MibTableColumn
cmTrunkConnectionLowPII = _CmTrunkConnectionLowPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1, 4),
    _CmTrunkConnectionLowPII_Type()
)
cmTrunkConnectionLowPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkConnectionLowPII.setStatus("mandatory")
_CmTrunkConnectionHighPII_Type = CmObjectPII
_CmTrunkConnectionHighPII_Object = MibTableColumn
cmTrunkConnectionHighPII = _CmTrunkConnectionHighPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 2, 1, 5),
    _CmTrunkConnectionHighPII_Type()
)
cmTrunkConnectionHighPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkConnectionHighPII.setStatus("mandatory")
_CmTrunkTopoTable_Object = MibTable
cmTrunkTopoTable = _CmTrunkTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3)
)
if mibBuilder.loadTexts:
    cmTrunkTopoTable.setStatus("mandatory")
_CmTrunkTopoEntry_Object = MibTableRow
cmTrunkTopoEntry = _CmTrunkTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1)
)
cmTrunkTopoEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrunkTopoSrc"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrunkTopoDest"),
)
if mibBuilder.loadTexts:
    cmTrunkTopoEntry.setStatus("mandatory")
_CmTrunkTopoSrc_Type = CmObjectPII
_CmTrunkTopoSrc_Object = MibTableColumn
cmTrunkTopoSrc = _CmTrunkTopoSrc_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1, 1),
    _CmTrunkTopoSrc_Type()
)
cmTrunkTopoSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkTopoSrc.setStatus("mandatory")
_CmTrunkTopoDest_Type = CmObjectPII
_CmTrunkTopoDest_Object = MibTableColumn
cmTrunkTopoDest = _CmTrunkTopoDest_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1, 2),
    _CmTrunkTopoDest_Type()
)
cmTrunkTopoDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkTopoDest.setStatus("mandatory")
_CmTrunkTopoInterface_Type = CmObjectPII
_CmTrunkTopoInterface_Object = MibTableColumn
cmTrunkTopoInterface = _CmTrunkTopoInterface_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1, 3),
    _CmTrunkTopoInterface_Type()
)
cmTrunkTopoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkTopoInterface.setStatus("mandatory")


class _CmTrunkTopoNextHop_Type(Integer32):
    """Custom type cmTrunkTopoNextHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CmTrunkTopoNextHop_Type.__name__ = "Integer32"
_CmTrunkTopoNextHop_Object = MibTableColumn
cmTrunkTopoNextHop = _CmTrunkTopoNextHop_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1, 4),
    _CmTrunkTopoNextHop_Type()
)
cmTrunkTopoNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkTopoNextHop.setStatus("mandatory")


class _CmTrunkTopoHops_Type(Integer32):
    """Custom type cmTrunkTopoHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CmTrunkTopoHops_Type.__name__ = "Integer32"
_CmTrunkTopoHops_Object = MibTableColumn
cmTrunkTopoHops = _CmTrunkTopoHops_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 18, 3, 1, 5),
    _CmTrunkTopoHops_Type()
)
cmTrunkTopoHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmTrunkTopoHops.setStatus("mandatory")
_CmDHCP_ObjectIdentity = ObjectIdentity
cmDHCP = _CmDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19)
)
_CmDHCPTable_Object = MibTable
cmDHCPTable = _CmDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1)
)
if mibBuilder.loadTexts:
    cmDHCPTable.setStatus("mandatory")
_CmDHCPEntry_Object = MibTableRow
cmDHCPEntry = _CmDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1, 1)
)
cmDHCPEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmDHCPPII"),
)
if mibBuilder.loadTexts:
    cmDHCPEntry.setStatus("mandatory")
_CmDHCPPII_Type = CmObjectPII
_CmDHCPPII_Object = MibTableColumn
cmDHCPPII = _CmDHCPPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1, 1, 1),
    _CmDHCPPII_Type()
)
cmDHCPPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDHCPPII.setStatus("mandatory")


class _CmDHCPRowStatus_Type(Integer32):
    """Custom type cmDHCPRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_CmDHCPRowStatus_Type.__name__ = "Integer32"
_CmDHCPRowStatus_Object = MibTableColumn
cmDHCPRowStatus = _CmDHCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1, 1, 2),
    _CmDHCPRowStatus_Type()
)
cmDHCPRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDHCPRowStatus.setStatus("mandatory")
_CmDHCPIpAddress_Type = IpAddress
_CmDHCPIpAddress_Object = MibTableColumn
cmDHCPIpAddress = _CmDHCPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1, 1, 3),
    _CmDHCPIpAddress_Type()
)
cmDHCPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDHCPIpAddress.setStatus("mandatory")
_CmDHCPNetMask_Type = IpAddress
_CmDHCPNetMask_Object = MibTableColumn
cmDHCPNetMask = _CmDHCPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 19, 1, 1, 4),
    _CmDHCPNetMask_Type()
)
cmDHCPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDHCPNetMask.setStatus("mandatory")
_CmServiceClass_ObjectIdentity = ObjectIdentity
cmServiceClass = _CmServiceClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 20)
)


class _CmServiceClassAweight_Type(Integer32):
    """Custom type cmServiceClassAweight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmServiceClassAweight_Type.__name__ = "Integer32"
_CmServiceClassAweight_Object = MibScalar
cmServiceClassAweight = _CmServiceClassAweight_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 20, 1),
    _CmServiceClassAweight_Type()
)
cmServiceClassAweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmServiceClassAweight.setStatus("mandatory")


class _CmServiceClassBweight_Type(Integer32):
    """Custom type cmServiceClassBweight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmServiceClassBweight_Type.__name__ = "Integer32"
_CmServiceClassBweight_Object = MibScalar
cmServiceClassBweight = _CmServiceClassBweight_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 20, 2),
    _CmServiceClassBweight_Type()
)
cmServiceClassBweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmServiceClassBweight.setStatus("mandatory")


class _CmServiceClassCweight_Type(Integer32):
    """Custom type cmServiceClassCweight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmServiceClassCweight_Type.__name__ = "Integer32"
_CmServiceClassCweight_Object = MibScalar
cmServiceClassCweight = _CmServiceClassCweight_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 20, 3),
    _CmServiceClassCweight_Type()
)
cmServiceClassCweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmServiceClassCweight.setStatus("mandatory")


class _CmServiceClassDweight_Type(Integer32):
    """Custom type cmServiceClassDweight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmServiceClassDweight_Type.__name__ = "Integer32"
_CmServiceClassDweight_Object = MibScalar
cmServiceClassDweight = _CmServiceClassDweight_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 20, 4),
    _CmServiceClassDweight_Type()
)
cmServiceClassDweight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmServiceClassDweight.setStatus("mandatory")
_CmEndPoint_ObjectIdentity = ObjectIdentity
cmEndPoint = _CmEndPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21)
)
_CmEndPointPortTable_Object = MibTable
cmEndPointPortTable = _CmEndPointPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1)
)
if mibBuilder.loadTexts:
    cmEndPointPortTable.setStatus("mandatory")
_CmEndPointPortEntry_Object = MibTableRow
cmEndPointPortEntry = _CmEndPointPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1)
)
cmEndPointPortEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointPortBasePII"),
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointPortNumber"),
)
if mibBuilder.loadTexts:
    cmEndPointPortEntry.setStatus("mandatory")
_CmEndPointPortBasePII_Type = CmObjectPII
_CmEndPointPortBasePII_Object = MibTableColumn
cmEndPointPortBasePII = _CmEndPointPortBasePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 1),
    _CmEndPointPortBasePII_Type()
)
cmEndPointPortBasePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortBasePII.setStatus("mandatory")
_CmEndPointPortNumber_Type = Integer32
_CmEndPointPortNumber_Object = MibTableColumn
cmEndPointPortNumber = _CmEndPointPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 2),
    _CmEndPointPortNumber_Type()
)
cmEndPointPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortNumber.setStatus("mandatory")
_CmEndPointPortEndPointID_Type = OctetString
_CmEndPointPortEndPointID_Object = MibTableColumn
cmEndPointPortEndPointID = _CmEndPointPortEndPointID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 3),
    _CmEndPointPortEndPointID_Type()
)
cmEndPointPortEndPointID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortEndPointID.setStatus("mandatory")
_CmEndPointPortPartnerPortPII_Type = CmObjectPII
_CmEndPointPortPartnerPortPII_Object = MibTableColumn
cmEndPointPortPartnerPortPII = _CmEndPointPortPartnerPortPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 4),
    _CmEndPointPortPartnerPortPII_Type()
)
cmEndPointPortPartnerPortPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortPartnerPortPII.setStatus("mandatory")
_CmEndPointPortPartnerBundlePII_Type = CmObjectPII
_CmEndPointPortPartnerBundlePII_Object = MibTableColumn
cmEndPointPortPartnerBundlePII = _CmEndPointPortPartnerBundlePII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 5),
    _CmEndPointPortPartnerBundlePII_Type()
)
cmEndPointPortPartnerBundlePII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortPartnerBundlePII.setStatus("mandatory")
_CmEndPointPortNumMatchingEndPoint_Type = Integer32
_CmEndPointPortNumMatchingEndPoint_Object = MibTableColumn
cmEndPointPortNumMatchingEndPoint = _CmEndPointPortNumMatchingEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 1, 1, 6),
    _CmEndPointPortNumMatchingEndPoint_Type()
)
cmEndPointPortNumMatchingEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointPortNumMatchingEndPoint.setStatus("mandatory")
_CmEndPointConfigTable_Object = MibTable
cmEndPointConfigTable = _CmEndPointConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2)
)
if mibBuilder.loadTexts:
    cmEndPointConfigTable.setStatus("mandatory")
_CmEndPointConfigEntry_Object = MibTableRow
cmEndPointConfigEntry = _CmEndPointConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1)
)
cmEndPointConfigEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointConfigPII"),
)
if mibBuilder.loadTexts:
    cmEndPointConfigEntry.setStatus("mandatory")
_CmEndPointConfigPII_Type = CmObjectPII
_CmEndPointConfigPII_Object = MibTableColumn
cmEndPointConfigPII = _CmEndPointConfigPII_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 1),
    _CmEndPointConfigPII_Type()
)
cmEndPointConfigPII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointConfigPII.setStatus("mandatory")


class _CmEndPointConfigRowStatus_Type(Integer32):
    """Custom type cmEndPointConfigRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_CmEndPointConfigRowStatus_Type.__name__ = "Integer32"
_CmEndPointConfigRowStatus_Object = MibTableColumn
cmEndPointConfigRowStatus = _CmEndPointConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 2),
    _CmEndPointConfigRowStatus_Type()
)
cmEndPointConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEndPointConfigRowStatus.setStatus("mandatory")


class _CmEndPointConfigBulkDownload_Type(Integer32):
    """Custom type cmEndPointConfigBulkDownload based on Integer32"""
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


_CmEndPointConfigBulkDownload_Type.__name__ = "Integer32"
_CmEndPointConfigBulkDownload_Object = MibTableColumn
cmEndPointConfigBulkDownload = _CmEndPointConfigBulkDownload_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 3),
    _CmEndPointConfigBulkDownload_Type()
)
cmEndPointConfigBulkDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEndPointConfigBulkDownload.setStatus("mandatory")


class _CmEndPointConfigDownloadStatus_Type(Integer32):
    """Custom type cmEndPointConfigDownloadStatus based on Integer32"""
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
        *(("completed", 5),
          ("failed", 4),
          ("inProgress", 3),
          ("none", 1),
          ("notDownloadable", 6),
          ("pending", 2))
    )


_CmEndPointConfigDownloadStatus_Type.__name__ = "Integer32"
_CmEndPointConfigDownloadStatus_Object = MibTableColumn
cmEndPointConfigDownloadStatus = _CmEndPointConfigDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 4),
    _CmEndPointConfigDownloadStatus_Type()
)
cmEndPointConfigDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointConfigDownloadStatus.setStatus("mandatory")
_CmEndPointConfigDownloadStartTime_Type = DisplayString
_CmEndPointConfigDownloadStartTime_Object = MibTableColumn
cmEndPointConfigDownloadStartTime = _CmEndPointConfigDownloadStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 5),
    _CmEndPointConfigDownloadStartTime_Type()
)
cmEndPointConfigDownloadStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointConfigDownloadStartTime.setStatus("mandatory")
_CmEndPointConfigDownloadEndTime_Type = DisplayString
_CmEndPointConfigDownloadEndTime_Object = MibTableColumn
cmEndPointConfigDownloadEndTime = _CmEndPointConfigDownloadEndTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 21, 2, 1, 6),
    _CmEndPointConfigDownloadEndTime_Type()
)
cmEndPointConfigDownloadEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmEndPointConfigDownloadEndTime.setStatus("mandatory")
_CmOperator_ObjectIdentity = ObjectIdentity
cmOperator = _CmOperator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22)
)
_CmActiveSessionTable_Object = MibTable
cmActiveSessionTable = _CmActiveSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1)
)
if mibBuilder.loadTexts:
    cmActiveSessionTable.setStatus("mandatory")
_CmActiveSessionEntry_Object = MibTableRow
cmActiveSessionEntry = _CmActiveSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1)
)
cmActiveSessionEntry.setIndexNames(
    (0, "COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionSessionID"),
)
if mibBuilder.loadTexts:
    cmActiveSessionEntry.setStatus("mandatory")
_CmActiveSessionSessionID_Type = Counter32
_CmActiveSessionSessionID_Object = MibTableColumn
cmActiveSessionSessionID = _CmActiveSessionSessionID_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 1),
    _CmActiveSessionSessionID_Type()
)
cmActiveSessionSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionSessionID.setStatus("mandatory")
_CmActiveSessionOperatorName_Type = DisplayString
_CmActiveSessionOperatorName_Object = MibTableColumn
cmActiveSessionOperatorName = _CmActiveSessionOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 2),
    _CmActiveSessionOperatorName_Type()
)
cmActiveSessionOperatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionOperatorName.setStatus("mandatory")


class _CmActiveSessionContext_Type(Integer32):
    """Custom type cmActiveSessionContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 32),
          ("http", 1),
          ("serial", 8),
          ("shell", 64),
          ("snmp", 2),
          ("telnet", 4))
    )


_CmActiveSessionContext_Type.__name__ = "Integer32"
_CmActiveSessionContext_Object = MibTableColumn
cmActiveSessionContext = _CmActiveSessionContext_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 3),
    _CmActiveSessionContext_Type()
)
cmActiveSessionContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionContext.setStatus("mandatory")


class _CmActiveSessionPrivilege_Type(Integer32):
    """Custom type cmActiveSessionPrivilege based on Integer32"""
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
        *(("monitor", 2),
          ("provision", 3),
          ("security", 4),
          ("view", 1))
    )


_CmActiveSessionPrivilege_Type.__name__ = "Integer32"
_CmActiveSessionPrivilege_Object = MibTableColumn
cmActiveSessionPrivilege = _CmActiveSessionPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 4),
    _CmActiveSessionPrivilege_Type()
)
cmActiveSessionPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionPrivilege.setStatus("mandatory")
_CmActiveSessionIpAddress_Type = IpAddress
_CmActiveSessionIpAddress_Object = MibTableColumn
cmActiveSessionIpAddress = _CmActiveSessionIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 5),
    _CmActiveSessionIpAddress_Type()
)
cmActiveSessionIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionIpAddress.setStatus("mandatory")
_CmActiveSessionStartTime_Type = TimeTicks
_CmActiveSessionStartTime_Object = MibTableColumn
cmActiveSessionStartTime = _CmActiveSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 6),
    _CmActiveSessionStartTime_Type()
)
cmActiveSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionStartTime.setStatus("mandatory")
_CmActiveSessionIdleTimeout_Type = Integer32
_CmActiveSessionIdleTimeout_Object = MibTableColumn
cmActiveSessionIdleTimeout = _CmActiveSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 22, 1, 1, 7),
    _CmActiveSessionIdleTimeout_Type()
)
cmActiveSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmActiveSessionIdleTimeout.setStatus("mandatory")
_CmRadius_ObjectIdentity = ObjectIdentity
cmRadius = _CmRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23)
)


class _CmRadiusAuthentication_Type(Integer32):
    """Custom type cmRadiusAuthentication based on Integer32"""
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


_CmRadiusAuthentication_Type.__name__ = "Integer32"
_CmRadiusAuthentication_Object = MibScalar
cmRadiusAuthentication = _CmRadiusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 1),
    _CmRadiusAuthentication_Type()
)
cmRadiusAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthentication.setStatus("mandatory")


class _CmRadiusAuthKey_Type(DisplayString):
    """Custom type cmRadiusAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CmRadiusAuthKey_Type.__name__ = "DisplayString"
_CmRadiusAuthKey_Object = MibScalar
cmRadiusAuthKey = _CmRadiusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 2),
    _CmRadiusAuthKey_Type()
)
cmRadiusAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthKey.setStatus("mandatory")
_CmRadiusAuthPrimaryIpAddr_Type = IpAddress
_CmRadiusAuthPrimaryIpAddr_Object = MibScalar
cmRadiusAuthPrimaryIpAddr = _CmRadiusAuthPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 3),
    _CmRadiusAuthPrimaryIpAddr_Type()
)
cmRadiusAuthPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthPrimaryIpAddr.setStatus("mandatory")


class _CmRadiusAuthPrimaryPort_Type(Integer32):
    """Custom type cmRadiusAuthPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAuthPrimaryPort_Type.__name__ = "Integer32"
_CmRadiusAuthPrimaryPort_Object = MibScalar
cmRadiusAuthPrimaryPort = _CmRadiusAuthPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 4),
    _CmRadiusAuthPrimaryPort_Type()
)
cmRadiusAuthPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthPrimaryPort.setStatus("mandatory")
_CmRadiusAuthSecondaryIpAddr_Type = IpAddress
_CmRadiusAuthSecondaryIpAddr_Object = MibScalar
cmRadiusAuthSecondaryIpAddr = _CmRadiusAuthSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 5),
    _CmRadiusAuthSecondaryIpAddr_Type()
)
cmRadiusAuthSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthSecondaryIpAddr.setStatus("mandatory")


class _CmRadiusAuthSecondaryPort_Type(Integer32):
    """Custom type cmRadiusAuthSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAuthSecondaryPort_Type.__name__ = "Integer32"
_CmRadiusAuthSecondaryPort_Object = MibScalar
cmRadiusAuthSecondaryPort = _CmRadiusAuthSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 6),
    _CmRadiusAuthSecondaryPort_Type()
)
cmRadiusAuthSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthSecondaryPort.setStatus("mandatory")
_CmRadiusAuthTertiaryIpAddr_Type = IpAddress
_CmRadiusAuthTertiaryIpAddr_Object = MibScalar
cmRadiusAuthTertiaryIpAddr = _CmRadiusAuthTertiaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 7),
    _CmRadiusAuthTertiaryIpAddr_Type()
)
cmRadiusAuthTertiaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthTertiaryIpAddr.setStatus("mandatory")


class _CmRadiusAuthTertiaryPort_Type(Integer32):
    """Custom type cmRadiusAuthTertiaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAuthTertiaryPort_Type.__name__ = "Integer32"
_CmRadiusAuthTertiaryPort_Object = MibScalar
cmRadiusAuthTertiaryPort = _CmRadiusAuthTertiaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 8),
    _CmRadiusAuthTertiaryPort_Type()
)
cmRadiusAuthTertiaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAuthTertiaryPort.setStatus("mandatory")
_CmRadiusAcctPrimaryIpAddr_Type = IpAddress
_CmRadiusAcctPrimaryIpAddr_Object = MibScalar
cmRadiusAcctPrimaryIpAddr = _CmRadiusAcctPrimaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 9),
    _CmRadiusAcctPrimaryIpAddr_Type()
)
cmRadiusAcctPrimaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctPrimaryIpAddr.setStatus("mandatory")


class _CmRadiusAcctPrimaryPort_Type(Integer32):
    """Custom type cmRadiusAcctPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAcctPrimaryPort_Type.__name__ = "Integer32"
_CmRadiusAcctPrimaryPort_Object = MibScalar
cmRadiusAcctPrimaryPort = _CmRadiusAcctPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 10),
    _CmRadiusAcctPrimaryPort_Type()
)
cmRadiusAcctPrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctPrimaryPort.setStatus("mandatory")
_CmRadiusAcctSecondaryIpAddr_Type = IpAddress
_CmRadiusAcctSecondaryIpAddr_Object = MibScalar
cmRadiusAcctSecondaryIpAddr = _CmRadiusAcctSecondaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 11),
    _CmRadiusAcctSecondaryIpAddr_Type()
)
cmRadiusAcctSecondaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctSecondaryIpAddr.setStatus("mandatory")


class _CmRadiusAcctSecondaryPort_Type(Integer32):
    """Custom type cmRadiusAcctSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAcctSecondaryPort_Type.__name__ = "Integer32"
_CmRadiusAcctSecondaryPort_Object = MibScalar
cmRadiusAcctSecondaryPort = _CmRadiusAcctSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 12),
    _CmRadiusAcctSecondaryPort_Type()
)
cmRadiusAcctSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctSecondaryPort.setStatus("mandatory")
_CmRadiusAcctTertiaryIpAddr_Type = IpAddress
_CmRadiusAcctTertiaryIpAddr_Object = MibScalar
cmRadiusAcctTertiaryIpAddr = _CmRadiusAcctTertiaryIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 13),
    _CmRadiusAcctTertiaryIpAddr_Type()
)
cmRadiusAcctTertiaryIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctTertiaryIpAddr.setStatus("mandatory")


class _CmRadiusAcctTertiaryPort_Type(Integer32):
    """Custom type cmRadiusAcctTertiaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmRadiusAcctTertiaryPort_Type.__name__ = "Integer32"
_CmRadiusAcctTertiaryPort_Object = MibScalar
cmRadiusAcctTertiaryPort = _CmRadiusAcctTertiaryPort_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 23, 14),
    _CmRadiusAcctTertiaryPort_Type()
)
cmRadiusAcctTertiaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRadiusAcctTertiaryPort.setStatus("mandatory")
_CmSNMP_ObjectIdentity = ObjectIdentity
cmSNMP = _CmSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1996, 20, 24)
)
_CmSNMPResponseString_Type = DisplayString
_CmSNMPResponseString_Object = MibScalar
cmSNMPResponseString = _CmSNMPResponseString_Object(
    (1, 3, 6, 1, 4, 1, 1996, 20, 24, 1),
    _CmSNMPResponseString_Type()
)
cmSNMPResponseString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSNMPResponseString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cmLoginError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 1)
)
cmLoginError.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginError.setStatus(
        ""
    )

cmLoginOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 2)
)
cmLoginOK.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginOK.setStatus(
        ""
    )

cmLogout = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 3)
)
cmLogout.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLogout.setStatus(
        ""
    )

cmLoginsSaturated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 4)
)
cmLoginsSaturated.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginsSaturated.setStatus(
        ""
    )

cmLoginsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 5)
)
cmLoginsAvailable.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginsAvailable.setStatus(
        ""
    )

cmBoardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 6)
)
cmBoardUp.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmBoardUp.setStatus(
        ""
    )

cmBoardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 7)
)
cmBoardDown.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmBoardDown.setStatus(
        ""
    )

cmLoginsSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 8)
)
cmLoginsSuspended.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginsSuspended.setStatus(
        ""
    )

cmLoginsAllowed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 9)
)
cmLoginsAllowed.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoginsAllowed.setStatus(
        ""
    )

cmBootFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 10)
)
cmBootFileError.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardFileName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmBootFileError.setStatus(
        ""
    )

cmBootFileOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 11)
)
cmBootFileOK.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardFileName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmBootFileOK.setStatus(
        ""
    )

cmAttributeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 12)
)
cmAttributeChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionOperatorName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionIpAddress"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmActiveSessionContext"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmAttributeChange.setStatus(
        ""
    )

cmConfigFileReadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 13)
)
cmConfigFileReadFailed.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmConfigFileReadFailed.setStatus(
        ""
    )

cmConfigFileReadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 14)
)
cmConfigFileReadOk.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmConfigFileReadOk.setStatus(
        ""
    )

cmConfigFileWriteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 15)
)
cmConfigFileWriteFailed.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmConfigFileWriteFailed.setStatus(
        ""
    )

cmConfigFileWriteOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 16)
)
cmConfigFileWriteOk.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmConfigFileWriteOk.setStatus(
        ""
    )

cmOperStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 17)
)
cmOperStateChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmStateOperState"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNameIfName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNamePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmOperStateChange.setStatus(
        ""
    )

cmDiagnostic = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 18)
)
cmDiagnostic.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmDiagnostic.setStatus(
        ""
    )

cmBoardRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 19)
)
cmBoardRestart.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmBoardRestart.setStatus(
        ""
    )

cmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 20)
)
cmFanFailure.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmFanFailure.setStatus(
        ""
    )

cmFanFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 21)
)
cmFanFailureClear.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmFanFailureClear.setStatus(
        ""
    )

cmPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 22)
)
cmPowerSupplyFailure.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmPowerSupplyFailure.setStatus(
        ""
    )

cmPowerSupplyFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 23)
)
cmPowerSupplyFailureClear.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmPowerSupplyFailureClear.setStatus(
        ""
    )

cmLoopStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 24)
)
cmLoopStatusChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopStatus"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopID"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopInterface"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopOwnerString"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopTermCode"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopTimeElapsed"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopTxCount"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmLoopRxErrors"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNameIfName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNamePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmLoopStatusChange.setStatus(
        ""
    )

cmRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 25)
)
cmRisingAlarm.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmVariable"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmSampleType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmValue"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmRisingThreshold"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNameIfName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNamePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRisingAlarm.setStatus(
        ""
    )

cmIDSLBoardTimingLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 26)
)
cmIDSLBoardTimingLoss.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIDSLBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIDSLBoardTimingMode"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmIDSLBoardTimingLoss.setStatus(
        ""
    )

cmIDSLBoardTimingLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 27)
)
cmIDSLBoardTimingLossClear.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIDSLBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmIDSLBoardTimingMode"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmIDSLBoardTimingLossClear.setStatus(
        ""
    )

cmRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 28)
)
cmRoleChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmSysPrimaryPII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRoleChange.setStatus(
        ""
    )

cmRedundancyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 29)
)
cmRedundancyChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmSysRedundancy"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRedundancyChange.setStatus(
        ""
    )

cmRedundancyConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 30)
)
cmRedundancyConflict.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmBoardIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRedundancyConflict.setStatus(
        ""
    )

cmMaintCmdStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 31)
)
cmMaintCmdStatusChange.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMaintCmdCommand"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmMaintCmdCommandStatus"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogProbableCause"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmMaintCmdStatusChange.setStatus(
        ""
    )

cmFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 32)
)
cmFallingAlarm.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmVariable"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmSampleType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmValue"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmAlarmFallingThreshold"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNameIfName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmNamePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmGroupName"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmFallingAlarm.setStatus(
        ""
    )

cmRateFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 33)
)
cmRateFallback.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLModemIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLModemCurrentRate"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRateFallback.setStatus(
        ""
    )

cmRateFallbackClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 34)
)
cmRateFallbackClear.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLModemIndex"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmHDSLModemCurrentRate"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmRateFallbackClear.setStatus(
        ""
    )

cmEndPointConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1996, 0, 35)
)
cmEndPointConflictAlarm.setObjects(
      *(("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointPortBasePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointPortEndPointID"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmEndPointPortPartnerBundlePII"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogText"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeverity"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogType"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogObjectClass"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogClassId"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogSeqNum"),
        ("COPPER-MOUNTAIN-NETWORKS-DSL-MIB", "cmTrapEventLogTimeTag"))
)
if mibBuilder.loadTexts:
    cmEndPointConflictAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COPPER-MOUNTAIN-NETWORKS-DSL-MIB",
    **{"DLCI": DLCI,
       "PerfTotalCount": PerfTotalCount,
       "CmObjectPII": CmObjectPII,
       "EntryStatus": EntryStatus,
       "coppermountain": coppermountain,
       "cmLoginError": cmLoginError,
       "cmLoginOK": cmLoginOK,
       "cmLogout": cmLogout,
       "cmLoginsSaturated": cmLoginsSaturated,
       "cmLoginsAvailable": cmLoginsAvailable,
       "cmBoardUp": cmBoardUp,
       "cmBoardDown": cmBoardDown,
       "cmLoginsSuspended": cmLoginsSuspended,
       "cmLoginsAllowed": cmLoginsAllowed,
       "cmBootFileError": cmBootFileError,
       "cmBootFileOK": cmBootFileOK,
       "cmAttributeChange": cmAttributeChange,
       "cmConfigFileReadFailed": cmConfigFileReadFailed,
       "cmConfigFileReadOk": cmConfigFileReadOk,
       "cmConfigFileWriteFailed": cmConfigFileWriteFailed,
       "cmConfigFileWriteOk": cmConfigFileWriteOk,
       "cmOperStateChange": cmOperStateChange,
       "cmDiagnostic": cmDiagnostic,
       "cmBoardRestart": cmBoardRestart,
       "cmFanFailure": cmFanFailure,
       "cmFanFailureClear": cmFanFailureClear,
       "cmPowerSupplyFailure": cmPowerSupplyFailure,
       "cmPowerSupplyFailureClear": cmPowerSupplyFailureClear,
       "cmLoopStatusChange": cmLoopStatusChange,
       "cmRisingAlarm": cmRisingAlarm,
       "cmIDSLBoardTimingLoss": cmIDSLBoardTimingLoss,
       "cmIDSLBoardTimingLossClear": cmIDSLBoardTimingLossClear,
       "cmRoleChange": cmRoleChange,
       "cmRedundancyChange": cmRedundancyChange,
       "cmRedundancyConflict": cmRedundancyConflict,
       "cmMaintCmdStatusChange": cmMaintCmdStatusChange,
       "cmFallingAlarm": cmFallingAlarm,
       "cmRateFallback": cmRateFallback,
       "cmRateFallbackClear": cmRateFallbackClear,
       "cmEndPointConflictAlarm": cmEndPointConflictAlarm,
       "cmRegistry": cmRegistry,
       "cmCE120Platform": cmCE120Platform,
       "cmCE150Platform": cmCE150Platform,
       "cmCE200Platform": cmCE200Platform,
       "cmTransmission": cmTransmission,
       "cmHDSL": cmHDSL,
       "cmHDSLModemTable": cmHDSLModemTable,
       "cmHDSLModemEntry": cmHDSLModemEntry,
       "cmHDSLModemIndex": cmHDSLModemIndex,
       "cmHDSLModemType": cmHDSLModemType,
       "cmHDSLModemTxGain": cmHDSLModemTxGain,
       "cmHDSLModemTestMode": cmHDSLModemTestMode,
       "cmHDSLModemNoiseMargin": cmHDSLModemNoiseMargin,
       "cmHDSLModemBPSwMajorVersion": cmHDSLModemBPSwMajorVersion,
       "cmHDSLModemBPSwMinorVersion": cmHDSLModemBPSwMinorVersion,
       "cmHDSLModemBPHwVersion": cmHDSLModemBPHwVersion,
       "cmHDSLModemDataRate": cmHDSLModemDataRate,
       "cmHDSLModemCpeCode": cmHDSLModemCpeCode,
       "cmHDSLModemSuccessfulTrains": cmHDSLModemSuccessfulTrains,
       "cmHDSLModemFailedTrainingAttempts": cmHDSLModemFailedTrainingAttempts,
       "cmHDSLModemCpeResponses": cmHDSLModemCpeResponses,
       "cmHDSLModemMinRate": cmHDSLModemMinRate,
       "cmHDSLModemCurrentRate": cmHDSLModemCurrentRate,
       "cmHDSLModemCommand": cmHDSLModemCommand,
       "cmHDSLPerfIntervalTable": cmHDSLPerfIntervalTable,
       "cmHDSLPerfIntervalEntry": cmHDSLPerfIntervalEntry,
       "cmHDSLPerfIndex": cmHDSLPerfIndex,
       "cmHDSLPerfIntervalNumber": cmHDSLPerfIntervalNumber,
       "cmHDSLPerfTxUnderruns": cmHDSLPerfTxUnderruns,
       "cmHDSLPerfRxTruncated": cmHDSLPerfRxTruncated,
       "cmHDSLPerfRxBig": cmHDSLPerfRxBig,
       "cmHDSLPerfRxAborts": cmHDSLPerfRxAborts,
       "cmHDSLPerfRxAlignmentErrors": cmHDSLPerfRxAlignmentErrors,
       "cmHDSLPerfRxCRCErrors": cmHDSLPerfRxCRCErrors,
       "cmHDSLPerfRxOverruns": cmHDSLPerfRxOverruns,
       "cmHDSLPerfRxValidFrames": cmHDSLPerfRxValidFrames,
       "cmHDSLPerfTxValidFrames": cmHDSLPerfTxValidFrames,
       "cmHDSLPerfRxNoBuffers": cmHDSLPerfRxNoBuffers,
       "cmCpeHDSLModemTable": cmCpeHDSLModemTable,
       "cmCpeHDSLModemEntry": cmCpeHDSLModemEntry,
       "cmCpeHDSLModemIndex": cmCpeHDSLModemIndex,
       "cmCpeHDSLModemType": cmCpeHDSLModemType,
       "cmCpeHDSLModemTxGain": cmCpeHDSLModemTxGain,
       "cmCpeHDSLModemTestMode": cmCpeHDSLModemTestMode,
       "cmCpeHDSLModemNoiseMargin": cmCpeHDSLModemNoiseMargin,
       "cmCpeHDSLModemBPSwMajorVersion": cmCpeHDSLModemBPSwMajorVersion,
       "cmCpeHDSLModemBPSwMinorVersion": cmCpeHDSLModemBPSwMinorVersion,
       "cmCpeHDSLModemBPHwVersion": cmCpeHDSLModemBPHwVersion,
       "cmCpeHDSLModemDataRate": cmCpeHDSLModemDataRate,
       "cmSDSLTestTable": cmSDSLTestTable,
       "cmSDSLTestEntry": cmSDSLTestEntry,
       "cmSDSLTestIndex": cmSDSLTestIndex,
       "cmSDSLTestAction": cmSDSLTestAction,
       "cmSDSLTestStatus": cmSDSLTestStatus,
       "cmSDSLTestTestCompleteTime": cmSDSLTestTestCompleteTime,
       "cmSDSLTestContinuityTestResult": cmSDSLTestContinuityTestResult,
       "cmSDSLTestNearEndLoopProfile": cmSDSLTestNearEndLoopProfile,
       "cmSDSLTestDebugResult": cmSDSLTestDebugResult,
       "cmSDSLTestType": cmSDSLTestType,
       "cmSDSLTestMaxRate": cmSDSLTestMaxRate,
       "cmIface": cmIface,
       "cmIfaceTable": cmIfaceTable,
       "cmIfaceEntry": cmIfaceEntry,
       "cmIfacePII": cmIfacePII,
       "cmIfaceIfIndex": cmIfaceIfIndex,
       "cmIfaceNetModel": cmIfaceNetModel,
       "cmIfaceIpAddr": cmIfaceIpAddr,
       "cmIfaceNetMask": cmIfaceNetMask,
       "cmIfaceMacAddr": cmIfaceMacAddr,
       "cmIfaceBurnedInMacAddr": cmIfaceBurnedInMacAddr,
       "cmIfaceFarEndAddr": cmIfaceFarEndAddr,
       "cmIfaceDestPII": cmIfaceDestPII,
       "cmIfaceFwdMode": cmIfaceFwdMode,
       "cmIfaceName": cmIfaceName,
       "cmIfaceAdditionalInfo": cmIfaceAdditionalInfo,
       "cmIfaceCMCPCompatible": cmIfaceCMCPCompatible,
       "cmIfaceEncapsulationType": cmIfaceEncapsulationType,
       "cmIfaceGroupName": cmIfaceGroupName,
       "cmIfaceServiceClass": cmIfaceServiceClass,
       "cmSubIfaceTable": cmSubIfaceTable,
       "cmSubIfaceEntry": cmSubIfaceEntry,
       "cmSubIfacePII": cmSubIfacePII,
       "cmSubIfaceDestPII": cmSubIfaceDestPII,
       "cmSubIfaceName": cmSubIfaceName,
       "cmSubIfaceRowStatus": cmSubIfaceRowStatus,
       "cmSubIfacePriority": cmSubIfacePriority,
       "cmEthernet": cmEthernet,
       "cmCpeEthernetIntervalTable": cmCpeEthernetIntervalTable,
       "cmCpeEthernetIntervalEntry": cmCpeEthernetIntervalEntry,
       "cmCpeEthernetIndex": cmCpeEthernetIndex,
       "cmCpeEthernetIntervalNumber": cmCpeEthernetIntervalNumber,
       "cmCpeEthernetIntUnknowns": cmCpeEthernetIntUnknowns,
       "cmCpeEthernetRxOK": cmCpeEthernetRxOK,
       "cmCpeEthernetRxNoBufs": cmCpeEthernetRxNoBufs,
       "cmCpeEthernetRxMiss": cmCpeEthernetRxMiss,
       "cmCpeEthernetRxSkip": cmCpeEthernetRxSkip,
       "cmCpeEthernetRxRunt": cmCpeEthernetRxRunt,
       "cmCpeEthernetRxExtraData": cmCpeEthernetRxExtraData,
       "cmCpeEthernetRxCRCError": cmCpeEthernetRxCRCError,
       "cmCpeEthernetRxAlignError": cmCpeEthernetRxAlignError,
       "cmCpeEthernetRxDribbleBits": cmCpeEthernetRxDribbleBits,
       "cmCpeEthernetTxTooBig": cmCpeEthernetTxTooBig,
       "cmCpeEthernetTxNotReady": cmCpeEthernetTxNotReady,
       "cmCpeEthernetTxLossCRS": cmCpeEthernetTxLossCRS,
       "cmCpeEthernetTxSQEErr": cmCpeEthernetTxSQEErr,
       "cmCpeEthernetTxOutOfWindow": cmCpeEthernetTxOutOfWindow,
       "cmCpeEthernetTxJabber": cmCpeEthernetTxJabber,
       "cmCpeEthernetTx16Collisions": cmCpeEthernetTx16Collisions,
       "cmCpeEthernetTxCollisions": cmCpeEthernetTxCollisions,
       "cmCpeEthernetTxOK": cmCpeEthernetTxOK,
       "cmFilter": cmFilter,
       "cmFilterTable": cmFilterTable,
       "cmFilterEntry": cmFilterEntry,
       "cmFilterIndex": cmFilterIndex,
       "cmFilterFilterNumber": cmFilterFilterNumber,
       "cmFilterFunction": cmFilterFunction,
       "cmFilterSrcMask": cmFilterSrcMask,
       "cmFilterSrcAdrs": cmFilterSrcAdrs,
       "cmFilterDstMask": cmFilterDstMask,
       "cmFilterDstAdrs": cmFilterDstAdrs,
       "cmFilterIpProtocol": cmFilterIpProtocol,
       "cmFilterSrcPortCompare": cmFilterSrcPortCompare,
       "cmFilterSrcPort": cmFilterSrcPort,
       "cmFilterDstPortCompare": cmFilterDstPortCompare,
       "cmFilterDstPort": cmFilterDstPort,
       "cmFilterAction": cmFilterAction,
       "cmDSL": cmDSL,
       "cmDSLIntervalTable": cmDSLIntervalTable,
       "cmDSLIntervalEntry": cmDSLIntervalEntry,
       "cmDSLIntervalIndex": cmDSLIntervalIndex,
       "cmDSLIntervalNumber": cmDSLIntervalNumber,
       "cmDSLIntervalTxUnderruns": cmDSLIntervalTxUnderruns,
       "cmDSLIntervalRxTruncated": cmDSLIntervalRxTruncated,
       "cmDSLIntervalRxBig": cmDSLIntervalRxBig,
       "cmDSLIntervalRxAborts": cmDSLIntervalRxAborts,
       "cmDSLIntervalRxAlignmentErrors": cmDSLIntervalRxAlignmentErrors,
       "cmDSLIntervalRxCRCErrors": cmDSLIntervalRxCRCErrors,
       "cmDSLIntervalRxOverruns": cmDSLIntervalRxOverruns,
       "cmDSLIntervalRxValidFrames": cmDSLIntervalRxValidFrames,
       "cmDSLIntervalTxValidFrames": cmDSLIntervalTxValidFrames,
       "cmDSLIntervalRxNoBuffers": cmDSLIntervalRxNoBuffers,
       "cmDSLIntervalTimeTagBegin": cmDSLIntervalTimeTagBegin,
       "cmDSLIntervalTimeTagEnd": cmDSLIntervalTimeTagEnd,
       "cmDSLIntervalMinNoiseMargin": cmDSLIntervalMinNoiseMargin,
       "cmDSLIntervalRxValidOctets": cmDSLIntervalRxValidOctets,
       "cmDSLIntervalTxValidOctets": cmDSLIntervalTxValidOctets,
       "cmDSLIntervalPortUpTime": cmDSLIntervalPortUpTime,
       "cmDSLCurrentTable": cmDSLCurrentTable,
       "cmDSLCurrentEntry": cmDSLCurrentEntry,
       "cmDSLCurrentIndex": cmDSLCurrentIndex,
       "cmDSLCurrentTxUnderruns": cmDSLCurrentTxUnderruns,
       "cmDSLCurrentRxTruncated": cmDSLCurrentRxTruncated,
       "cmDSLCurrentRxBig": cmDSLCurrentRxBig,
       "cmDSLCurrentRxAborts": cmDSLCurrentRxAborts,
       "cmDSLCurrentRxAlignmentErrors": cmDSLCurrentRxAlignmentErrors,
       "cmDSLCurrentRxCRCErrors": cmDSLCurrentRxCRCErrors,
       "cmDSLCurrentRxOverruns": cmDSLCurrentRxOverruns,
       "cmDSLCurrentRxValidFrames": cmDSLCurrentRxValidFrames,
       "cmDSLCurrentTxValidFrames": cmDSLCurrentTxValidFrames,
       "cmDSLCurrentRxNoBuffers": cmDSLCurrentRxNoBuffers,
       "cmDSLCurrentMinNoiseMargin": cmDSLCurrentMinNoiseMargin,
       "cmDSLCurrentRxValidOctets": cmDSLCurrentRxValidOctets,
       "cmDSLCurrentTxValidOctets": cmDSLCurrentTxValidOctets,
       "cmDSLCurrentPortUpTime": cmDSLCurrentPortUpTime,
       "cmDSLYesterdaysTable": cmDSLYesterdaysTable,
       "cmDSLYesterdaysEntry": cmDSLYesterdaysEntry,
       "cmDSLYesterdaysIndex": cmDSLYesterdaysIndex,
       "cmDSLYesterdaysTxUnderruns": cmDSLYesterdaysTxUnderruns,
       "cmDSLYesterdaysRxTruncated": cmDSLYesterdaysRxTruncated,
       "cmDSLYesterdaysRxBig": cmDSLYesterdaysRxBig,
       "cmDSLYesterdaysRxAborts": cmDSLYesterdaysRxAborts,
       "cmDSLYesterdaysRxAlignmentErrors": cmDSLYesterdaysRxAlignmentErrors,
       "cmDSLYesterdaysRxCRCErrors": cmDSLYesterdaysRxCRCErrors,
       "cmDSLYesterdaysRxOverruns": cmDSLYesterdaysRxOverruns,
       "cmDSLYesterdaysRxValidFrames": cmDSLYesterdaysRxValidFrames,
       "cmDSLYesterdaysTxValidFrames": cmDSLYesterdaysTxValidFrames,
       "cmDSLYesterdaysRxNoBuffers": cmDSLYesterdaysRxNoBuffers,
       "cmDSLYesterdaysMinNoiseMargin": cmDSLYesterdaysMinNoiseMargin,
       "cmDSLYesterdaysRxValidOctets": cmDSLYesterdaysRxValidOctets,
       "cmDSLYesterdaysTxValidOctets": cmDSLYesterdaysTxValidOctets,
       "cmDSLYesterdaysPortUpTime": cmDSLYesterdaysPortUpTime,
       "cmDSLTodaysTable": cmDSLTodaysTable,
       "cmDSLTodaysEntry": cmDSLTodaysEntry,
       "cmDSLTodaysIndex": cmDSLTodaysIndex,
       "cmDSLTodaysTxUnderruns": cmDSLTodaysTxUnderruns,
       "cmDSLTodaysRxTruncated": cmDSLTodaysRxTruncated,
       "cmDSLTodaysRxBig": cmDSLTodaysRxBig,
       "cmDSLTodaysRxAborts": cmDSLTodaysRxAborts,
       "cmDSLTodaysRxAlignmentErrors": cmDSLTodaysRxAlignmentErrors,
       "cmDSLTodaysRxCRCErrors": cmDSLTodaysRxCRCErrors,
       "cmDSLTodaysRxOverruns": cmDSLTodaysRxOverruns,
       "cmDSLTodaysRxValidFrames": cmDSLTodaysRxValidFrames,
       "cmDSLTodaysTxValidFrames": cmDSLTodaysTxValidFrames,
       "cmDSLTodaysRxNoBuffers": cmDSLTodaysRxNoBuffers,
       "cmDSLTodaysMinNoiseMargin": cmDSLTodaysMinNoiseMargin,
       "cmDSLTodaysRxValidOctets": cmDSLTodaysRxValidOctets,
       "cmDSLTodaysTxValidOctets": cmDSLTodaysTxValidOctets,
       "cmDSLTodaysPortUpTime": cmDSLTodaysPortUpTime,
       "cmDSL24HrTable": cmDSL24HrTable,
       "cmDSL24HrEntry": cmDSL24HrEntry,
       "cmDSL24HrIndex": cmDSL24HrIndex,
       "cmDSL24HrTxUnderruns": cmDSL24HrTxUnderruns,
       "cmDSL24HrRxTruncated": cmDSL24HrRxTruncated,
       "cmDSL24HrRxBig": cmDSL24HrRxBig,
       "cmDSL24HrRxAborts": cmDSL24HrRxAborts,
       "cmDSL24HrRxAlignmentErrors": cmDSL24HrRxAlignmentErrors,
       "cmDSL24HrRxCRCErrors": cmDSL24HrRxCRCErrors,
       "cmDSL24HrRxOverruns": cmDSL24HrRxOverruns,
       "cmDSL24HrRxValidFrames": cmDSL24HrRxValidFrames,
       "cmDSL24HrTxValidFrames": cmDSL24HrTxValidFrames,
       "cmDSL24HrRxNoBuffers": cmDSL24HrRxNoBuffers,
       "cmDSL24HrMinNoiseMargin": cmDSL24HrMinNoiseMargin,
       "cmDSL24HrRxValidOctets": cmDSL24HrRxValidOctets,
       "cmDSL24HrTxValidOctets": cmDSL24HrTxValidOctets,
       "cmDSL24HrPortUpTime": cmDSL24HrPortUpTime,
       "cmCpeDSLIntervalTable": cmCpeDSLIntervalTable,
       "cmCpeDSLIntervalEntry": cmCpeDSLIntervalEntry,
       "cmCpeDSLIntervalIndex": cmCpeDSLIntervalIndex,
       "cmCpeDSLIntervalNumber": cmCpeDSLIntervalNumber,
       "cmCpeDSLIntervalTxUnderruns": cmCpeDSLIntervalTxUnderruns,
       "cmCpeDSLIntervalRxTruncated": cmCpeDSLIntervalRxTruncated,
       "cmCpeDSLIntervalRxBig": cmCpeDSLIntervalRxBig,
       "cmCpeDSLIntervalRxAborts": cmCpeDSLIntervalRxAborts,
       "cmCpeDSLIntervalRxAlignmentErrors": cmCpeDSLIntervalRxAlignmentErrors,
       "cmCpeDSLIntervalRxCRCErrors": cmCpeDSLIntervalRxCRCErrors,
       "cmCpeDSLIntervalRxOverruns": cmCpeDSLIntervalRxOverruns,
       "cmCpeDSLIntervalRxValidFrames": cmCpeDSLIntervalRxValidFrames,
       "cmCpeDSLIntervalTxValidFrames": cmCpeDSLIntervalTxValidFrames,
       "cmCpeDSLIntervalRxNoBuffers": cmCpeDSLIntervalRxNoBuffers,
       "cmCpeDSLIntervalRxValidOctets": cmCpeDSLIntervalRxValidOctets,
       "cmCpeDSLIntervalTxValidOctets": cmCpeDSLIntervalTxValidOctets,
       "cmIDSL": cmIDSL,
       "cmIDSLModemTable": cmIDSLModemTable,
       "cmIDSLModemEntry": cmIDSLModemEntry,
       "cmIDSLModemIndex": cmIDSLModemIndex,
       "cmIDSLModemOperState": cmIDSLModemOperState,
       "cmIDSLModemDataRate": cmIDSLModemDataRate,
       "cmIDSLModemState": cmIDSLModemState,
       "cmIDSLModemTerminationMode": cmIDSLModemTerminationMode,
       "cmIDSLModemCpeCode": cmIDSLModemCpeCode,
       "cmIDSLModemSuccessfulTrains": cmIDSLModemSuccessfulTrains,
       "cmIDSLModemFailedTrainingAttempts": cmIDSLModemFailedTrainingAttempts,
       "cmIDSLModemCpeResponses": cmIDSLModemCpeResponses,
       "cmIDSLModemNetworkElements": cmIDSLModemNetworkElements,
       "cmIDSLModemActivationInterval": cmIDSLModemActivationInterval,
       "cmCpeIDSLModemTable": cmCpeIDSLModemTable,
       "cmCpeIDSLModemEntry": cmCpeIDSLModemEntry,
       "cmCpeIDSLModemIndex": cmCpeIDSLModemIndex,
       "cmCpeIDSLModemOperState": cmCpeIDSLModemOperState,
       "cmCpeIDSLModemDataRate": cmCpeIDSLModemDataRate,
       "cmCpeIDSLModemState": cmCpeIDSLModemState,
       "cmCpeIDSLModemTerminationMode": cmCpeIDSLModemTerminationMode,
       "cmFrameRelay": cmFrameRelay,
       "cmFrDlcmiTable": cmFrDlcmiTable,
       "cmFrDlcmiEntry": cmFrDlcmiEntry,
       "cmFrDlcmiIfIndex": cmFrDlcmiIfIndex,
       "cmFrDlcmiAdminState": cmFrDlcmiAdminState,
       "cmFrDlcmiOperState": cmFrDlcmiOperState,
       "cmFrDlcmiFirstDLCI": cmFrDlcmiFirstDLCI,
       "cmFrDlcmiLMIMode": cmFrDlcmiLMIMode,
       "cmFrDlcmiDceN392": cmFrDlcmiDceN392,
       "cmFrDlcmiDceN393": cmFrDlcmiDceN393,
       "cmFrDlcmiDceT392": cmFrDlcmiDceT392,
       "cmFrDlcmiRcvUnknownDLCI": cmFrDlcmiRcvUnknownDLCI,
       "cmFrDlcmiLMITxStatusEnquiries": cmFrDlcmiLMITxStatusEnquiries,
       "cmFrDlcmiLMITxStatusResponses": cmFrDlcmiLMITxStatusResponses,
       "cmFrDlcmiLMIRxStatusEnquiries": cmFrDlcmiLMIRxStatusEnquiries,
       "cmFrDlcmiLMIRxStatusResponses": cmFrDlcmiLMIRxStatusResponses,
       "cmFrDlcmiLMIRxUpdates": cmFrDlcmiLMIRxUpdates,
       "cmFrDlcmiUnknownLMIMessagesRcvd": cmFrDlcmiUnknownLMIMessagesRcvd,
       "cmFrDlcmiLostLMISequences": cmFrDlcmiLostLMISequences,
       "cmFrCircuitTable": cmFrCircuitTable,
       "cmFrCircuitEntry": cmFrCircuitEntry,
       "cmFrCircuitIfIndex": cmFrCircuitIfIndex,
       "cmFrCircuitDlci": cmFrCircuitDlci,
       "cmFrCircuitOperState": cmFrCircuitOperState,
       "cmFrCircuitFramesDroppedTxUnavail": cmFrCircuitFramesDroppedTxUnavail,
       "cmFrCircuitFramesDroppedRxUnavail": cmFrCircuitFramesDroppedRxUnavail,
       "cmFrCircuitFramesDroppedExcess": cmFrCircuitFramesDroppedExcess,
       "cmATM": cmATM,
       "cmAtmVclTable": cmAtmVclTable,
       "cmAtmVclEntry": cmAtmVclEntry,
       "cmAtmVclPII": cmAtmVclPII,
       "cmAtmVclVpi": cmAtmVclVpi,
       "cmAtmVclVci": cmAtmVclVci,
       "cmAtmVclAdminStatus": cmAtmVclAdminStatus,
       "cmAtmVclOperStatus": cmAtmVclOperStatus,
       "cmAtmVclLastChange": cmAtmVclLastChange,
       "cmAtmVclAalType": cmAtmVclAalType,
       "cmAtmVclAal5CpcsTransmitSduSize": cmAtmVclAal5CpcsTransmitSduSize,
       "cmAtmVclAal5CpcsReceiveSduSize": cmAtmVclAal5CpcsReceiveSduSize,
       "cmAtmVclRowStatus": cmAtmVclRowStatus,
       "cmDS3AtmTable": cmDS3AtmTable,
       "cmDS3AtmEntry": cmDS3AtmEntry,
       "cmDS3AtmPII": cmDS3AtmPII,
       "cmDS3AtmCbitParityEnable": cmDS3AtmCbitParityEnable,
       "cmDS3AtmCellPayloadScrambling": cmDS3AtmCellPayloadScrambling,
       "cmDS3AtmCellMapping": cmDS3AtmCellMapping,
       "cmIMUX": cmIMUX,
       "cmBundleTable": cmBundleTable,
       "cmBundleEntry": cmBundleEntry,
       "cmBundlePII": cmBundlePII,
       "cmBundleRowStatus": cmBundleRowStatus,
       "cmBundleMember1PII": cmBundleMember1PII,
       "cmBundleMember1EndPointID": cmBundleMember1EndPointID,
       "cmBundleMember1Status": cmBundleMember1Status,
       "cmBundleMember2PII": cmBundleMember2PII,
       "cmBundleMember2EndPointID": cmBundleMember2EndPointID,
       "cmBundleMember2Status": cmBundleMember2Status,
       "cmBundleMember3PII": cmBundleMember3PII,
       "cmBundleMember3EndPointID": cmBundleMember3EndPointID,
       "cmBundleMember3Status": cmBundleMember3Status,
       "cmBundleMember4PII": cmBundleMember4PII,
       "cmBundleMember4EndPointID": cmBundleMember4EndPointID,
       "cmBundleMember4Status": cmBundleMember4Status,
       "cmDataPort": cmDataPort,
       "cmCpeDataPortTable": cmCpeDataPortTable,
       "cmCpeDataPortEntry": cmCpeDataPortEntry,
       "cmCpeDataPortIndex": cmCpeDataPortIndex,
       "cmCpeDataPortType": cmCpeDataPortType,
       "cmCpeDataPortForceDSR": cmCpeDataPortForceDSR,
       "cmCpeDataPortIgnoreDTR": cmCpeDataPortIgnoreDTR,
       "cmCpeDataPortIgnoreRTS": cmCpeDataPortIgnoreRTS,
       "cmCpeDataPortTerminalTiming": cmCpeDataPortTerminalTiming,
       "cmCpeDataPortTM": cmCpeDataPortTM,
       "cmCpeDataPortLL": cmCpeDataPortLL,
       "cmCpeDataPortRL": cmCpeDataPortRL,
       "cmCpeDataPortDTR": cmCpeDataPortDTR,
       "cmCpeDataPortRTS": cmCpeDataPortRTS,
       "cmCpeDataPortDSR": cmCpeDataPortDSR,
       "cmCpeDataPortCTS": cmCpeDataPortCTS,
       "cmCpeDataPortDCD": cmCpeDataPortDCD,
       "cmCpeDataPortTxClockSource": cmCpeDataPortTxClockSource,
       "cmCpeDataPortDTEDCE": cmCpeDataPortDTEDCE,
       "cmCpeDataPortCRC": cmCpeDataPortCRC,
       "cmCpeDataPortClockRate": cmCpeDataPortClockRate,
       "cmCpeDataPortAdminState": cmCpeDataPortAdminState,
       "cmCpeDataPortOperState": cmCpeDataPortOperState,
       "cmCpeDataPortLoopbackConfig": cmCpeDataPortLoopbackConfig,
       "cmCpeDataPortLoopbackStatus": cmCpeDataPortLoopbackStatus,
       "cmCpeDataPortIntervalTable": cmCpeDataPortIntervalTable,
       "cmCpeDataPortIntervalEntry": cmCpeDataPortIntervalEntry,
       "cmCpeDataPortIntervalIndex": cmCpeDataPortIntervalIndex,
       "cmCpeDataPortIntervalIntervalNumber": cmCpeDataPortIntervalIntervalNumber,
       "cmCpeDataPortIntervalRxFrames": cmCpeDataPortIntervalRxFrames,
       "cmCpeDataPortIntervalRxOctets": cmCpeDataPortIntervalRxOctets,
       "cmCpeDataPortIntervalRxDiscards": cmCpeDataPortIntervalRxDiscards,
       "cmCpeDataPortIntervalRxErrors": cmCpeDataPortIntervalRxErrors,
       "cmCpeDataPortIntervalTxFrames": cmCpeDataPortIntervalTxFrames,
       "cmCpeDataPortIntervalTxOctets": cmCpeDataPortIntervalTxOctets,
       "cmCpeDataPortIntervalTxDiscards": cmCpeDataPortIntervalTxDiscards,
       "cmCpeDataPortIntervalTxErrors": cmCpeDataPortIntervalTxErrors,
       "cmCpeDataPortTotalTable": cmCpeDataPortTotalTable,
       "cmCpeDataPortTotalEntry": cmCpeDataPortTotalEntry,
       "cmCpeDataPortTotalIndex": cmCpeDataPortTotalIndex,
       "cmCpeDataPortTotalRxFrames": cmCpeDataPortTotalRxFrames,
       "cmCpeDataPortTotalRxOctets": cmCpeDataPortTotalRxOctets,
       "cmCpeDataPortTotalRxDiscards": cmCpeDataPortTotalRxDiscards,
       "cmCpeDataPortTotalRxErrors": cmCpeDataPortTotalRxErrors,
       "cmCpeDataPortTotalTxFrames": cmCpeDataPortTotalTxFrames,
       "cmCpeDataPortTotalTxOctets": cmCpeDataPortTotalTxOctets,
       "cmCpeDataPortTotalTxDiscards": cmCpeDataPortTotalTxDiscards,
       "cmCpeDataPortTotalTxErrors": cmCpeDataPortTotalTxErrors,
       "cmCE200": cmCE200,
       "cmSystem": cmSystem,
       "cmSysObjectClass": cmSysObjectClass,
       "cmSysOperState": cmSysOperState,
       "cmSysMaster": cmSysMaster,
       "cmSysTrapAddress": cmSysTrapAddress,
       "cmSysConfigFileName": cmSysConfigFileName,
       "cmSysCommand": cmSysCommand,
       "cmSysCommandStatus": cmSysCommandStatus,
       "cmSysVersion": cmSysVersion,
       "cmSysCalendarTime": cmSysCalendarTime,
       "cmSysPrimaryPII": cmSysPrimaryPII,
       "cmSysSecondaryPII": cmSysSecondaryPII,
       "cmSysRedundancy": cmSysRedundancy,
       "cmSysConfigSynch": cmSysConfigSynch,
       "cmSysMyPII": cmSysMyPII,
       "cmSysShelfCount": cmSysShelfCount,
       "cmSysExpIpSubNet": cmSysExpIpSubNet,
       "cmBoard": cmBoard,
       "cmBoardTable": cmBoardTable,
       "cmBoardEntry": cmBoardEntry,
       "cmBoardIndex": cmBoardIndex,
       "cmBoardObjectClass": cmBoardObjectClass,
       "cmBoardOperState": cmBoardOperState,
       "cmBoardUpTime": cmBoardUpTime,
       "cmBoardFileName": cmBoardFileName,
       "cmBoardFileDate": cmBoardFileDate,
       "cmBoardHwType": cmBoardHwType,
       "cmBoardNumPorts": cmBoardNumPorts,
       "cmBoardHwVersion": cmBoardHwVersion,
       "cmBoardSwVersion": cmBoardSwVersion,
       "cmBoardPromVersion": cmBoardPromVersion,
       "cmBoardRole": cmBoardRole,
       "cmBoardConfigChange": cmBoardConfigChange,
       "cmBoardCommand": cmBoardCommand,
       "cmBoardSerialNumber": cmBoardSerialNumber,
       "cmBoardClusterRole": cmBoardClusterRole,
       "cmBoardInformation": cmBoardInformation,
       "cmIDSLBoardTable": cmIDSLBoardTable,
       "cmIDSLBoardEntry": cmIDSLBoardEntry,
       "cmIDSLBoardIndex": cmIDSLBoardIndex,
       "cmIDSLBoardTimingMode": cmIDSLBoardTimingMode,
       "cmIDSLBoardTimingStatus": cmIDSLBoardTimingStatus,
       "cmIDSLBoardTimingAvailable": cmIDSLBoardTimingAvailable,
       "cmState": cmState,
       "cmStateTable": cmStateTable,
       "cmStateEntry": cmStateEntry,
       "cmStateGenericClass": cmStateGenericClass,
       "cmStateIndex": cmStateIndex,
       "cmStateObjClass": cmStateObjClass,
       "cmStateOperState": cmStateOperState,
       "cmStateLastChange": cmStateLastChange,
       "cmShelf": cmShelf,
       "cmShelfTable": cmShelfTable,
       "cmShelfEntry": cmShelfEntry,
       "cmShelfIndex": cmShelfIndex,
       "cmShelfObjectClass": cmShelfObjectClass,
       "cmShelfOperability": cmShelfOperability,
       "cmShelfUpTime": cmShelfUpTime,
       "cmShelfMaster": cmShelfMaster,
       "cmShelfBoardMap": cmShelfBoardMap,
       "cmShelfCommand": cmShelfCommand,
       "cmShelfShelfNumber": cmShelfShelfNumber,
       "cmFile": cmFile,
       "cmFileBootDevice": cmFileBootDevice,
       "cmFileFSName": cmFileFSName,
       "cmFileFSAddr": cmFileFSAddr,
       "cmFileFSUsername": cmFileFSUsername,
       "cmFileFSPassword": cmFileFSPassword,
       "cmFileFLASHDir": cmFileFLASHDir,
       "cmFileFSDir": cmFileFSDir,
       "cmCpeBoard": cmCpeBoard,
       "cmCpeBoardTable": cmCpeBoardTable,
       "cmCpeBoardEntry": cmCpeBoardEntry,
       "cmCpeBoardIndex": cmCpeBoardIndex,
       "cmCpeBoardObjectClass": cmCpeBoardObjectClass,
       "cmCpeBoardOperState": cmCpeBoardOperState,
       "cmCpeBoardUpTime": cmCpeBoardUpTime,
       "cmCpeBoardFileName": cmCpeBoardFileName,
       "cmCpeBoardFileDate": cmCpeBoardFileDate,
       "cmCpeBoardHwType": cmCpeBoardHwType,
       "cmCpeBoardNumPorts": cmCpeBoardNumPorts,
       "cmCpeBoardHwVersion": cmCpeBoardHwVersion,
       "cmCpeBoardSwVersion": cmCpeBoardSwVersion,
       "cmCpeBoardPromVersion": cmCpeBoardPromVersion,
       "cmCpeBoardConfigChange": cmCpeBoardConfigChange,
       "cmCpeBoardCommand": cmCpeBoardCommand,
       "cmCpeBoardSerialNumber": cmCpeBoardSerialNumber,
       "cmCpeBoardVendorDescription": cmCpeBoardVendorDescription,
       "cmCpeBoardGroupMap": cmCpeBoardGroupMap,
       "cmCpeBoardManagementOptions": cmCpeBoardManagementOptions,
       "cmHSSI": cmHSSI,
       "cmHSSITable": cmHSSITable,
       "cmHSSIEntry": cmHSSIEntry,
       "cmHSSIIndex": cmHSSIIndex,
       "cmHSSIIfIndex": cmHSSIIfIndex,
       "cmHSSIDCEReady": cmHSSIDCEReady,
       "cmHSSIDTEReady": cmHSSIDTEReady,
       "cmHSSIDTEDCE": cmHSSIDTEDCE,
       "cmHSSILoopback": cmHSSILoopback,
       "cmHSSITestmode": cmHSSITestmode,
       "cmHSSISync": cmHSSISync,
       "cmHSSITxClockPresent": cmHSSITxClockPresent,
       "cmHSSICRC": cmHSSICRC,
       "cmHSSIClockRate": cmHSSIClockRate,
       "cmHSSIAdminState": cmHSSIAdminState,
       "cmHSSIOperState": cmHSSIOperState,
       "cmV35": cmV35,
       "cmV35Table": cmV35Table,
       "cmV35Entry": cmV35Entry,
       "cmV35Index": cmV35Index,
       "cmV35IfIndex": cmV35IfIndex,
       "cmV35DSR": cmV35DSR,
       "cmV35DCD": cmV35DCD,
       "cmV35CTS": cmV35CTS,
       "cmV35DTR": cmV35DTR,
       "cmV35RTS": cmV35RTS,
       "cmV35DTEDCE": cmV35DTEDCE,
       "cmV35Sync": cmV35Sync,
       "cmV35TxClockSource": cmV35TxClockSource,
       "cmV35CRC": cmV35CRC,
       "cmV35ClockRate": cmV35ClockRate,
       "cmV35AdminState": cmV35AdminState,
       "cmV35OperState": cmV35OperState,
       "cmTrap": cmTrap,
       "cmTrapEventSeqNum": cmTrapEventSeqNum,
       "cmTrapCriticalAlarmCount": cmTrapCriticalAlarmCount,
       "cmTrapMajorAlarmCount": cmTrapMajorAlarmCount,
       "cmTrapMinorAlarmCount": cmTrapMinorAlarmCount,
       "cmTrapWarningCount": cmTrapWarningCount,
       "cmTrapReceiverTable": cmTrapReceiverTable,
       "cmTrapReceiverEntry": cmTrapReceiverEntry,
       "cmTrapReceiverIPAddr": cmTrapReceiverIPAddr,
       "cmTrapReceiverPort": cmTrapReceiverPort,
       "cmTrapReceiverCommunity": cmTrapReceiverCommunity,
       "cmTrapReceiverRowStatus": cmTrapReceiverRowStatus,
       "cmTrapReceiverOwnerString": cmTrapReceiverOwnerString,
       "cmTrapEventLogTable": cmTrapEventLogTable,
       "cmTrapEventLogEntry": cmTrapEventLogEntry,
       "cmTrapEventLogSeqNum": cmTrapEventLogSeqNum,
       "cmTrapEventLogType": cmTrapEventLogType,
       "cmTrapEventLogObjectClass": cmTrapEventLogObjectClass,
       "cmTrapEventLogClassId": cmTrapEventLogClassId,
       "cmTrapEventLogProbableCause": cmTrapEventLogProbableCause,
       "cmTrapEventLogSeverity": cmTrapEventLogSeverity,
       "cmTrapEventLogTimeTag": cmTrapEventLogTimeTag,
       "cmTrapEventLogText": cmTrapEventLogText,
       "cmTrapAlarmLogTable": cmTrapAlarmLogTable,
       "cmTrapAlarmLogEntry": cmTrapAlarmLogEntry,
       "cmTrapAlarmLogSeqNum": cmTrapAlarmLogSeqNum,
       "cmTrapAlarmLogType": cmTrapAlarmLogType,
       "cmTrapAlarmLogObjectClass": cmTrapAlarmLogObjectClass,
       "cmTrapAlarmLogClassId": cmTrapAlarmLogClassId,
       "cmTrapAlarmLogProbableCause": cmTrapAlarmLogProbableCause,
       "cmTrapAlarmLogSeverity": cmTrapAlarmLogSeverity,
       "cmTrapAlarmLogTimeTag": cmTrapAlarmLogTimeTag,
       "cmTrapAlarmLogText": cmTrapAlarmLogText,
       "cmTrapTypeLogTable": cmTrapTypeLogTable,
       "cmTrapTypeLogEntry": cmTrapTypeLogEntry,
       "cmTrapTypeLogType": cmTrapTypeLogType,
       "cmTrapTypeLogSeqNum": cmTrapTypeLogSeqNum,
       "cmTrapTypeLogObjectClass": cmTrapTypeLogObjectClass,
       "cmTrapTypeLogClassId": cmTrapTypeLogClassId,
       "cmTrapTypeLogProbableCause": cmTrapTypeLogProbableCause,
       "cmTrapTypeLogSeverity": cmTrapTypeLogSeverity,
       "cmTrapTypeLogTimeTag": cmTrapTypeLogTimeTag,
       "cmTrapTypeLogText": cmTrapTypeLogText,
       "cmTrapDestinationTable": cmTrapDestinationTable,
       "cmTrapDestinationEntry": cmTrapDestinationEntry,
       "cmTrapDestinationIpAddr": cmTrapDestinationIpAddr,
       "cmTrapDestinationPort": cmTrapDestinationPort,
       "cmTrapDestinationCommunity": cmTrapDestinationCommunity,
       "cmTrapDestinationRowStatus": cmTrapDestinationRowStatus,
       "cmTrapDestinationOwnerString": cmTrapDestinationOwnerString,
       "cmLoop": cmLoop,
       "cmLoopID": cmLoopID,
       "cmLoopInterface": cmLoopInterface,
       "cmLoopType": cmLoopType,
       "cmLoopAction": cmLoopAction,
       "cmLoopDuration": cmLoopDuration,
       "cmLoopStatus": cmLoopStatus,
       "cmLoopTimeElapsed": cmLoopTimeElapsed,
       "cmLoopTermCode": cmLoopTermCode,
       "cmLoopTxCount": cmLoopTxCount,
       "cmLoopRxErrors": cmLoopRxErrors,
       "cmLoopOwnerString": cmLoopOwnerString,
       "cmLoopHistTable": cmLoopHistTable,
       "cmLoopHistEntry": cmLoopHistEntry,
       "cmLoopHistID": cmLoopHistID,
       "cmLoopHistInterface": cmLoopHistInterface,
       "cmLoopHistType": cmLoopHistType,
       "cmLoopHistAction": cmLoopHistAction,
       "cmLoopHistDuration": cmLoopHistDuration,
       "cmLoopHistStatus": cmLoopHistStatus,
       "cmLoopHistTimeElapsed": cmLoopHistTimeElapsed,
       "cmLoopHistTermCode": cmLoopHistTermCode,
       "cmLoopHistTxCount": cmLoopHistTxCount,
       "cmLoopHistRxErrors": cmLoopHistRxErrors,
       "cmLoopHistOwnerString": cmLoopHistOwnerString,
       "cmLoopHistTestParameter1": cmLoopHistTestParameter1,
       "cmLoopHistErrorInfo": cmLoopHistErrorInfo,
       "cmLoopTestParameter1": cmLoopTestParameter1,
       "cmLoopErrorInfo": cmLoopErrorInfo,
       "cmVBridge": cmVBridge,
       "cmVBridgeTable": cmVBridgeTable,
       "cmVBridgeEntry": cmVBridgeEntry,
       "cmVBridgePII": cmVBridgePII,
       "cmVBridgeNMAC": cmVBridgeNMAC,
       "cmVBridgeNMulticast": cmVBridgeNMulticast,
       "cmVBridgeNUnicast": cmVBridgeNUnicast,
       "cmVBridgeNDSL": cmVBridgeNDSL,
       "cmVBridgeNUnknownDest": cmVBridgeNUnknownDest,
       "cmVBridgeNOverflow": cmVBridgeNOverflow,
       "cmVBridgeOption": cmVBridgeOption,
       "cmMAC": cmMAC,
       "cmMACTable": cmMACTable,
       "cmMACEntry": cmMACEntry,
       "cmMACPII": cmMACPII,
       "cmMACIndex": cmMACIndex,
       "cmMACMAC": cmMACMAC,
       "cmMACTTL": cmMACTTL,
       "cmMACDslPII": cmMACDslPII,
       "cmAlarm": cmAlarm,
       "cmAlarmTable": cmAlarmTable,
       "cmAlarmEntry": cmAlarmEntry,
       "cmAlarmIndex": cmAlarmIndex,
       "cmAlarmInterval": cmAlarmInterval,
       "cmAlarmVariable": cmAlarmVariable,
       "cmAlarmSampleType": cmAlarmSampleType,
       "cmAlarmValue": cmAlarmValue,
       "cmAlarmStartupAlarm": cmAlarmStartupAlarm,
       "cmAlarmRisingThreshold": cmAlarmRisingThreshold,
       "cmAlarmFallingThreshold": cmAlarmFallingThreshold,
       "cmAlarmStatus": cmAlarmStatus,
       "cmAlarmSwitch": cmAlarmSwitch,
       "cmAlarmSamplingInterval": cmAlarmSamplingInterval,
       "cmEvent": cmEvent,
       "cmUserGroup": cmUserGroup,
       "cmNameTable": cmNameTable,
       "cmNameEntry": cmNameEntry,
       "cmNameIfName": cmNameIfName,
       "cmNamePII": cmNamePII,
       "cmGroupTable": cmGroupTable,
       "cmGroupEntry": cmGroupEntry,
       "cmGroupName": cmGroupName,
       "cmGroupNewGrpName": cmGroupNewGrpName,
       "cmGroupRowStatus": cmGroupRowStatus,
       "cmMemberTable": cmMemberTable,
       "cmMemberEntry": cmMemberEntry,
       "cmMemberGrpName": cmMemberGrpName,
       "cmMemberPII": cmMemberPII,
       "cmMemberRowStatus": cmMemberRowStatus,
       "cmMaint": cmMaint,
       "cmMaintCmdTable": cmMaintCmdTable,
       "cmMaintCmdEntry": cmMaintCmdEntry,
       "cmMaintCmdCommand": cmMaintCmdCommand,
       "cmMaintCmdRowStatus": cmMaintCmdRowStatus,
       "cmMaintCmdStartTime": cmMaintCmdStartTime,
       "cmMaintCmdRecurrence": cmMaintCmdRecurrence,
       "cmMaintCmdReportingPeriod": cmMaintCmdReportingPeriod,
       "cmMaintCmdPrimaryIpAddr": cmMaintCmdPrimaryIpAddr,
       "cmMaintCmdSecondaryIpAddr": cmMaintCmdSecondaryIpAddr,
       "cmMaintCmdDirectory": cmMaintCmdDirectory,
       "cmMaintCmdBaseFileName": cmMaintCmdBaseFileName,
       "cmMaintCmdUserName": cmMaintCmdUserName,
       "cmMaintCmdPassword": cmMaintCmdPassword,
       "cmMaintCmdPreviousTime": cmMaintCmdPreviousTime,
       "cmMaintCmdNextTime": cmMaintCmdNextTime,
       "cmMaintCmdCommandStatus": cmMaintCmdCommandStatus,
       "cmMaintCmdStatusText": cmMaintCmdStatusText,
       "cmMaintStatsDelimiter": cmMaintStatsDelimiter,
       "cmProxyArp": cmProxyArp,
       "cmProxyArpTable": cmProxyArpTable,
       "cmProxyArpEntry": cmProxyArpEntry,
       "cmProxyArpPII": cmProxyArpPII,
       "cmProxyArpRowStatus": cmProxyArpRowStatus,
       "cmMultiShelf": cmMultiShelf,
       "cmTrunkIfTable": cmTrunkIfTable,
       "cmTrunkIfEntry": cmTrunkIfEntry,
       "cmTrunkIfIndex": cmTrunkIfIndex,
       "cmTrunkIfOperState": cmTrunkIfOperState,
       "cmTrunkIfAdminState": cmTrunkIfAdminState,
       "cmTrunkIfSentPackets": cmTrunkIfSentPackets,
       "cmTrunkIfSentError": cmTrunkIfSentError,
       "cmTrunkIfRecvPackets": cmTrunkIfRecvPackets,
       "cmTrunkIfRecvError": cmTrunkIfRecvError,
       "cmTrunkConnectionTable": cmTrunkConnectionTable,
       "cmTrunkConnectionEntry": cmTrunkConnectionEntry,
       "cmTrunkConnectionTrunkMaster": cmTrunkConnectionTrunkMaster,
       "cmTrunkConnectionIndex": cmTrunkConnectionIndex,
       "cmTrunkConnectionOperState": cmTrunkConnectionOperState,
       "cmTrunkConnectionLowPII": cmTrunkConnectionLowPII,
       "cmTrunkConnectionHighPII": cmTrunkConnectionHighPII,
       "cmTrunkTopoTable": cmTrunkTopoTable,
       "cmTrunkTopoEntry": cmTrunkTopoEntry,
       "cmTrunkTopoSrc": cmTrunkTopoSrc,
       "cmTrunkTopoDest": cmTrunkTopoDest,
       "cmTrunkTopoInterface": cmTrunkTopoInterface,
       "cmTrunkTopoNextHop": cmTrunkTopoNextHop,
       "cmTrunkTopoHops": cmTrunkTopoHops,
       "cmDHCP": cmDHCP,
       "cmDHCPTable": cmDHCPTable,
       "cmDHCPEntry": cmDHCPEntry,
       "cmDHCPPII": cmDHCPPII,
       "cmDHCPRowStatus": cmDHCPRowStatus,
       "cmDHCPIpAddress": cmDHCPIpAddress,
       "cmDHCPNetMask": cmDHCPNetMask,
       "cmServiceClass": cmServiceClass,
       "cmServiceClassAweight": cmServiceClassAweight,
       "cmServiceClassBweight": cmServiceClassBweight,
       "cmServiceClassCweight": cmServiceClassCweight,
       "cmServiceClassDweight": cmServiceClassDweight,
       "cmEndPoint": cmEndPoint,
       "cmEndPointPortTable": cmEndPointPortTable,
       "cmEndPointPortEntry": cmEndPointPortEntry,
       "cmEndPointPortBasePII": cmEndPointPortBasePII,
       "cmEndPointPortNumber": cmEndPointPortNumber,
       "cmEndPointPortEndPointID": cmEndPointPortEndPointID,
       "cmEndPointPortPartnerPortPII": cmEndPointPortPartnerPortPII,
       "cmEndPointPortPartnerBundlePII": cmEndPointPortPartnerBundlePII,
       "cmEndPointPortNumMatchingEndPoint": cmEndPointPortNumMatchingEndPoint,
       "cmEndPointConfigTable": cmEndPointConfigTable,
       "cmEndPointConfigEntry": cmEndPointConfigEntry,
       "cmEndPointConfigPII": cmEndPointConfigPII,
       "cmEndPointConfigRowStatus": cmEndPointConfigRowStatus,
       "cmEndPointConfigBulkDownload": cmEndPointConfigBulkDownload,
       "cmEndPointConfigDownloadStatus": cmEndPointConfigDownloadStatus,
       "cmEndPointConfigDownloadStartTime": cmEndPointConfigDownloadStartTime,
       "cmEndPointConfigDownloadEndTime": cmEndPointConfigDownloadEndTime,
       "cmOperator": cmOperator,
       "cmActiveSessionTable": cmActiveSessionTable,
       "cmActiveSessionEntry": cmActiveSessionEntry,
       "cmActiveSessionSessionID": cmActiveSessionSessionID,
       "cmActiveSessionOperatorName": cmActiveSessionOperatorName,
       "cmActiveSessionContext": cmActiveSessionContext,
       "cmActiveSessionPrivilege": cmActiveSessionPrivilege,
       "cmActiveSessionIpAddress": cmActiveSessionIpAddress,
       "cmActiveSessionStartTime": cmActiveSessionStartTime,
       "cmActiveSessionIdleTimeout": cmActiveSessionIdleTimeout,
       "cmRadius": cmRadius,
       "cmRadiusAuthentication": cmRadiusAuthentication,
       "cmRadiusAuthKey": cmRadiusAuthKey,
       "cmRadiusAuthPrimaryIpAddr": cmRadiusAuthPrimaryIpAddr,
       "cmRadiusAuthPrimaryPort": cmRadiusAuthPrimaryPort,
       "cmRadiusAuthSecondaryIpAddr": cmRadiusAuthSecondaryIpAddr,
       "cmRadiusAuthSecondaryPort": cmRadiusAuthSecondaryPort,
       "cmRadiusAuthTertiaryIpAddr": cmRadiusAuthTertiaryIpAddr,
       "cmRadiusAuthTertiaryPort": cmRadiusAuthTertiaryPort,
       "cmRadiusAcctPrimaryIpAddr": cmRadiusAcctPrimaryIpAddr,
       "cmRadiusAcctPrimaryPort": cmRadiusAcctPrimaryPort,
       "cmRadiusAcctSecondaryIpAddr": cmRadiusAcctSecondaryIpAddr,
       "cmRadiusAcctSecondaryPort": cmRadiusAcctSecondaryPort,
       "cmRadiusAcctTertiaryIpAddr": cmRadiusAcctTertiaryIpAddr,
       "cmRadiusAcctTertiaryPort": cmRadiusAcctTertiaryPort,
       "cmSNMP": cmSNMP,
       "cmSNMPResponseString": cmSNMPResponseString}
)
