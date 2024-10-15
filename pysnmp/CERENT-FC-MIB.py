# SNMP MIB module (CERENT-FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-FC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:22 2024
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

(CerentPeriod,) = mibBuilder.importSymbols(
    "CERENT-TC",
    "CerentPeriod")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cerentFcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 100)
)
cerentFcMIB.setRevisions(
        ("1903-02-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentFcMIBObjects_ObjectIdentity = ObjectIdentity
cerentFcMIBObjects = _CerentFcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60)
)
_CerentFc_ObjectIdentity = ObjectIdentity
cerentFc = _CerentFc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1)
)
_CFcStatsTable_Object = MibTable
cFcStatsTable = _CFcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1)
)
if mibBuilder.loadTexts:
    cFcStatsTable.setStatus("current")
_CFcStatsEntry_Object = MibTableRow
cFcStatsEntry = _CFcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1)
)
cFcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cFcStatsEntry.setStatus("current")
_CFcStatsInvalidOrdSets_Type = Counter32
_CFcStatsInvalidOrdSets_Object = MibTableColumn
cFcStatsInvalidOrdSets = _CFcStatsInvalidOrdSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 10),
    _CFcStatsInvalidOrdSets_Type()
)
cFcStatsInvalidOrdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInvalidOrdSets.setStatus("current")
_CFcStatsInvalidOrdSetsHigh_Type = Counter32
_CFcStatsInvalidOrdSetsHigh_Object = MibTableColumn
cFcStatsInvalidOrdSetsHigh = _CFcStatsInvalidOrdSetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 20),
    _CFcStatsInvalidOrdSetsHigh_Type()
)
cFcStatsInvalidOrdSetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInvalidOrdSetsHigh.setStatus("current")
_CFcStatsEncodingDispErr_Type = Counter32
_CFcStatsEncodingDispErr_Object = MibTableColumn
cFcStatsEncodingDispErr = _CFcStatsEncodingDispErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 30),
    _CFcStatsEncodingDispErr_Type()
)
cFcStatsEncodingDispErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsEncodingDispErr.setStatus("current")
_CFcStatsEncodingDispErrHigh_Type = Counter32
_CFcStatsEncodingDispErrHigh_Object = MibTableColumn
cFcStatsEncodingDispErrHigh = _CFcStatsEncodingDispErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 40),
    _CFcStatsEncodingDispErrHigh_Type()
)
cFcStatsEncodingDispErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsEncodingDispErrHigh.setStatus("current")
_CFcStatsInTotalErr_Type = Counter32
_CFcStatsInTotalErr_Object = MibTableColumn
cFcStatsInTotalErr = _CFcStatsInTotalErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 50),
    _CFcStatsInTotalErr_Type()
)
cFcStatsInTotalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInTotalErr.setStatus("current")
_CFcStatsInTotalErrHigh_Type = Counter32
_CFcStatsInTotalErrHigh_Object = MibTableColumn
cFcStatsInTotalErrHigh = _CFcStatsInTotalErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 60),
    _CFcStatsInTotalErrHigh_Type()
)
cFcStatsInTotalErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInTotalErrHigh.setStatus("current")
_CFcStatsInFramesTrunc_Type = Counter32
_CFcStatsInFramesTrunc_Object = MibTableColumn
cFcStatsInFramesTrunc = _CFcStatsInFramesTrunc_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 70),
    _CFcStatsInFramesTrunc_Type()
)
cFcStatsInFramesTrunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTrunc.setStatus("current")
_CFcStatsInFramesTruncHigh_Type = Counter32
_CFcStatsInFramesTruncHigh_Object = MibTableColumn
cFcStatsInFramesTruncHigh = _CFcStatsInFramesTruncHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 80),
    _CFcStatsInFramesTruncHigh_Type()
)
cFcStatsInFramesTruncHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTruncHigh.setStatus("current")
_CFcStatsInFramesTooLong_Type = Counter32
_CFcStatsInFramesTooLong_Object = MibTableColumn
cFcStatsInFramesTooLong = _CFcStatsInFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 90),
    _CFcStatsInFramesTooLong_Type()
)
cFcStatsInFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTooLong.setStatus("current")
_CFcStatsInFramesTooLongHigh_Type = Counter32
_CFcStatsInFramesTooLongHigh_Object = MibTableColumn
cFcStatsInFramesTooLongHigh = _CFcStatsInFramesTooLongHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 100),
    _CFcStatsInFramesTooLongHigh_Type()
)
cFcStatsInFramesTooLongHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTooLongHigh.setStatus("current")
_CFcStatsInFramesBadCRC_Type = Counter32
_CFcStatsInFramesBadCRC_Object = MibTableColumn
cFcStatsInFramesBadCRC = _CFcStatsInFramesBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 110),
    _CFcStatsInFramesBadCRC_Type()
)
cFcStatsInFramesBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesBadCRC.setStatus("current")
_CFcStatsInFramesBadCRCHigh_Type = Counter32
_CFcStatsInFramesBadCRCHigh_Object = MibTableColumn
cFcStatsInFramesBadCRCHigh = _CFcStatsInFramesBadCRCHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 120),
    _CFcStatsInFramesBadCRCHigh_Type()
)
cFcStatsInFramesBadCRCHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesBadCRCHigh.setStatus("current")
_CFcStatsInFrames_Type = Counter32
_CFcStatsInFrames_Object = MibTableColumn
cFcStatsInFrames = _CFcStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 130),
    _CFcStatsInFrames_Type()
)
cFcStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFrames.setStatus("current")
_CFcStatsInFramesHigh_Type = Counter32
_CFcStatsInFramesHigh_Object = MibTableColumn
cFcStatsInFramesHigh = _CFcStatsInFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 140),
    _CFcStatsInFramesHigh_Type()
)
cFcStatsInFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesHigh.setStatus("current")
_CFcStatsInElements_Type = Counter32
_CFcStatsInElements_Object = MibTableColumn
cFcStatsInElements = _CFcStatsInElements_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 150),
    _CFcStatsInElements_Type()
)
cFcStatsInElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInElements.setStatus("current")
_CFcStatsInElementsHigh_Type = Counter32
_CFcStatsInElementsHigh_Object = MibTableColumn
cFcStatsInElementsHigh = _CFcStatsInElementsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 160),
    _CFcStatsInElementsHigh_Type()
)
cFcStatsInElementsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInElementsHigh.setStatus("current")
_CFcStatsInDiscards_Type = Counter32
_CFcStatsInDiscards_Object = MibTableColumn
cFcStatsInDiscards = _CFcStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 170),
    _CFcStatsInDiscards_Type()
)
cFcStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInDiscards.setStatus("current")
_CFcStatsInDiscardsHigh_Type = Counter32
_CFcStatsInDiscardsHigh_Object = MibTableColumn
cFcStatsInDiscardsHigh = _CFcStatsInDiscardsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 180),
    _CFcStatsInDiscardsHigh_Type()
)
cFcStatsInDiscardsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInDiscardsHigh.setStatus("current")
_CFcStatsOutFramesBadCRC_Type = Counter32
_CFcStatsOutFramesBadCRC_Object = MibTableColumn
cFcStatsOutFramesBadCRC = _CFcStatsOutFramesBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 190),
    _CFcStatsOutFramesBadCRC_Type()
)
cFcStatsOutFramesBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFramesBadCRC.setStatus("current")
_CFcStatsOutFramesBadCRCHigh_Type = Counter32
_CFcStatsOutFramesBadCRCHigh_Object = MibTableColumn
cFcStatsOutFramesBadCRCHigh = _CFcStatsOutFramesBadCRCHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 200),
    _CFcStatsOutFramesBadCRCHigh_Type()
)
cFcStatsOutFramesBadCRCHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFramesBadCRCHigh.setStatus("current")
_CFcStatsOutFrames_Type = Counter32
_CFcStatsOutFrames_Object = MibTableColumn
cFcStatsOutFrames = _CFcStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 210),
    _CFcStatsOutFrames_Type()
)
cFcStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFrames.setStatus("current")
_CFcStatsOutFramesHigh_Type = Counter32
_CFcStatsOutFramesHigh_Object = MibTableColumn
cFcStatsOutFramesHigh = _CFcStatsOutFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 220),
    _CFcStatsOutFramesHigh_Type()
)
cFcStatsOutFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFramesHigh.setStatus("current")
_CFcStatsOutElements_Type = Counter32
_CFcStatsOutElements_Object = MibTableColumn
cFcStatsOutElements = _CFcStatsOutElements_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 230),
    _CFcStatsOutElements_Type()
)
cFcStatsOutElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutElements.setStatus("current")
_CFcStatsOutElementsHigh_Type = Counter32
_CFcStatsOutElementsHigh_Object = MibTableColumn
cFcStatsOutElementsHigh = _CFcStatsOutElementsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 240),
    _CFcStatsOutElementsHigh_Type()
)
cFcStatsOutElementsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutElementsHigh.setStatus("current")
_CFcStatsOutDiscards_Type = Counter32
_CFcStatsOutDiscards_Object = MibTableColumn
cFcStatsOutDiscards = _CFcStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 250),
    _CFcStatsOutDiscards_Type()
)
cFcStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutDiscards.setStatus("current")
_CFcStatsOutDiscardsHigh_Type = Counter32
_CFcStatsOutDiscardsHigh_Object = MibTableColumn
cFcStatsOutDiscardsHigh = _CFcStatsOutDiscardsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 260),
    _CFcStatsOutDiscardsHigh_Type()
)
cFcStatsOutDiscardsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutDiscardsHigh.setStatus("current")
_CFcStatsLinkResets_Type = Counter32
_CFcStatsLinkResets_Object = MibTableColumn
cFcStatsLinkResets = _CFcStatsLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 270),
    _CFcStatsLinkResets_Type()
)
cFcStatsLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsLinkResets.setStatus("current")
_CFcStatsLinkResetsHigh_Type = Counter32
_CFcStatsLinkResetsHigh_Object = MibTableColumn
cFcStatsLinkResetsHigh = _CFcStatsLinkResetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 280),
    _CFcStatsLinkResetsHigh_Type()
)
cFcStatsLinkResetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsLinkResetsHigh.setStatus("current")
_CFcStatsGfpInSBitErr_Type = Counter32
_CFcStatsGfpInSBitErr_Object = MibTableColumn
cFcStatsGfpInSBitErr = _CFcStatsGfpInSBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 290),
    _CFcStatsGfpInSBitErr_Type()
)
cFcStatsGfpInSBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBitErr.setStatus("current")
_CFcStatsGfpInSBitErrHigh_Type = Counter32
_CFcStatsGfpInSBitErrHigh_Object = MibTableColumn
cFcStatsGfpInSBitErrHigh = _CFcStatsGfpInSBitErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 300),
    _CFcStatsGfpInSBitErrHigh_Type()
)
cFcStatsGfpInSBitErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBitErrHigh.setStatus("current")
_CFcStatsGfpInMBitErr_Type = Counter32
_CFcStatsGfpInMBitErr_Object = MibTableColumn
cFcStatsGfpInMBitErr = _CFcStatsGfpInMBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 310),
    _CFcStatsGfpInMBitErr_Type()
)
cFcStatsGfpInMBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInMBitErr.setStatus("current")
_CFcStatsGfpInMBitErrHigh_Type = Counter32
_CFcStatsGfpInMBitErrHigh_Object = MibTableColumn
cFcStatsGfpInMBitErrHigh = _CFcStatsGfpInMBitErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 320),
    _CFcStatsGfpInMBitErrHigh_Type()
)
cFcStatsGfpInMBitErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInMBitErrHigh.setStatus("current")
_CFcStatsGfpInTypeInvalid_Type = Counter32
_CFcStatsGfpInTypeInvalid_Object = MibTableColumn
cFcStatsGfpInTypeInvalid = _CFcStatsGfpInTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 330),
    _CFcStatsGfpInTypeInvalid_Type()
)
cFcStatsGfpInTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInTypeInvalid.setStatus("current")
_CFcStatsGfpInTypeInvalidHigh_Type = Counter32
_CFcStatsGfpInTypeInvalidHigh_Object = MibTableColumn
cFcStatsGfpInTypeInvalidHigh = _CFcStatsGfpInTypeInvalidHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 340),
    _CFcStatsGfpInTypeInvalidHigh_Type()
)
cFcStatsGfpInTypeInvalidHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInTypeInvalidHigh.setStatus("current")
_CFcStatsGfpInSBlkCRCErr_Type = Counter32
_CFcStatsGfpInSBlkCRCErr_Object = MibTableColumn
cFcStatsGfpInSBlkCRCErr = _CFcStatsGfpInSBlkCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 350),
    _CFcStatsGfpInSBlkCRCErr_Type()
)
cFcStatsGfpInSBlkCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBlkCRCErr.setStatus("current")
_CFcStatsGfpInSBlkCRCErrHigh_Type = Counter32
_CFcStatsGfpInSBlkCRCErrHigh_Object = MibTableColumn
cFcStatsGfpInSBlkCRCErrHigh = _CFcStatsGfpInSBlkCRCErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 1, 1, 360),
    _CFcStatsGfpInSBlkCRCErrHigh_Type()
)
cFcStatsGfpInSBlkCRCErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBlkCRCErrHigh.setStatus("current")
_CFcStatsHCTable_Object = MibTable
cFcStatsHCTable = _CFcStatsHCTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2)
)
if mibBuilder.loadTexts:
    cFcStatsHCTable.setStatus("current")
_CFcStatsHCEntry_Object = MibTableRow
cFcStatsHCEntry = _CFcStatsHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1)
)
cFcStatsHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cFcStatsHCEntry.setStatus("current")
_CFcStatsInvalidOrdSetsHC_Type = Counter64
_CFcStatsInvalidOrdSetsHC_Object = MibTableColumn
cFcStatsInvalidOrdSetsHC = _CFcStatsInvalidOrdSetsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 10),
    _CFcStatsInvalidOrdSetsHC_Type()
)
cFcStatsInvalidOrdSetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInvalidOrdSetsHC.setStatus("current")
_CFcStatsEncodingDispErrHC_Type = Counter64
_CFcStatsEncodingDispErrHC_Object = MibTableColumn
cFcStatsEncodingDispErrHC = _CFcStatsEncodingDispErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 20),
    _CFcStatsEncodingDispErrHC_Type()
)
cFcStatsEncodingDispErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsEncodingDispErrHC.setStatus("current")
_CFcStatsInTotalErrHC_Type = Counter64
_CFcStatsInTotalErrHC_Object = MibTableColumn
cFcStatsInTotalErrHC = _CFcStatsInTotalErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 30),
    _CFcStatsInTotalErrHC_Type()
)
cFcStatsInTotalErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInTotalErrHC.setStatus("current")
_CFcStatsInFramesTruncHC_Type = Counter64
_CFcStatsInFramesTruncHC_Object = MibTableColumn
cFcStatsInFramesTruncHC = _CFcStatsInFramesTruncHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 40),
    _CFcStatsInFramesTruncHC_Type()
)
cFcStatsInFramesTruncHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTruncHC.setStatus("current")
_CFcStatsInFramesTooLongHC_Type = Counter64
_CFcStatsInFramesTooLongHC_Object = MibTableColumn
cFcStatsInFramesTooLongHC = _CFcStatsInFramesTooLongHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 50),
    _CFcStatsInFramesTooLongHC_Type()
)
cFcStatsInFramesTooLongHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesTooLongHC.setStatus("current")
_CFcStatsInFramesBadCRCHC_Type = Counter64
_CFcStatsInFramesBadCRCHC_Object = MibTableColumn
cFcStatsInFramesBadCRCHC = _CFcStatsInFramesBadCRCHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 60),
    _CFcStatsInFramesBadCRCHC_Type()
)
cFcStatsInFramesBadCRCHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesBadCRCHC.setStatus("current")
_CFcStatsInFramesHC_Type = Counter64
_CFcStatsInFramesHC_Object = MibTableColumn
cFcStatsInFramesHC = _CFcStatsInFramesHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 70),
    _CFcStatsInFramesHC_Type()
)
cFcStatsInFramesHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInFramesHC.setStatus("current")
_CFcStatsInElementsHC_Type = Counter64
_CFcStatsInElementsHC_Object = MibTableColumn
cFcStatsInElementsHC = _CFcStatsInElementsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 80),
    _CFcStatsInElementsHC_Type()
)
cFcStatsInElementsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInElementsHC.setStatus("current")
_CFcStatsInDiscardsHC_Type = Counter64
_CFcStatsInDiscardsHC_Object = MibTableColumn
cFcStatsInDiscardsHC = _CFcStatsInDiscardsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 90),
    _CFcStatsInDiscardsHC_Type()
)
cFcStatsInDiscardsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsInDiscardsHC.setStatus("current")
_CFcStatsOutFramesBadCRCHC_Type = Counter64
_CFcStatsOutFramesBadCRCHC_Object = MibTableColumn
cFcStatsOutFramesBadCRCHC = _CFcStatsOutFramesBadCRCHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 100),
    _CFcStatsOutFramesBadCRCHC_Type()
)
cFcStatsOutFramesBadCRCHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFramesBadCRCHC.setStatus("current")
_CFcStatsOutFramesHC_Type = Counter64
_CFcStatsOutFramesHC_Object = MibTableColumn
cFcStatsOutFramesHC = _CFcStatsOutFramesHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 110),
    _CFcStatsOutFramesHC_Type()
)
cFcStatsOutFramesHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutFramesHC.setStatus("current")
_CFcStatsOutElementsHC_Type = Counter64
_CFcStatsOutElementsHC_Object = MibTableColumn
cFcStatsOutElementsHC = _CFcStatsOutElementsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 120),
    _CFcStatsOutElementsHC_Type()
)
cFcStatsOutElementsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutElementsHC.setStatus("current")
_CFcStatsOutDiscardsHC_Type = Counter64
_CFcStatsOutDiscardsHC_Object = MibTableColumn
cFcStatsOutDiscardsHC = _CFcStatsOutDiscardsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 130),
    _CFcStatsOutDiscardsHC_Type()
)
cFcStatsOutDiscardsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsOutDiscardsHC.setStatus("current")
_CFcStatsLinkResetsHC_Type = Counter64
_CFcStatsLinkResetsHC_Object = MibTableColumn
cFcStatsLinkResetsHC = _CFcStatsLinkResetsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 140),
    _CFcStatsLinkResetsHC_Type()
)
cFcStatsLinkResetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsLinkResetsHC.setStatus("current")
_CFcStatsGfpInSBitErrHC_Type = Counter64
_CFcStatsGfpInSBitErrHC_Object = MibTableColumn
cFcStatsGfpInSBitErrHC = _CFcStatsGfpInSBitErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 150),
    _CFcStatsGfpInSBitErrHC_Type()
)
cFcStatsGfpInSBitErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBitErrHC.setStatus("current")
_CFcStatsGfpInMBitErrHC_Type = Counter64
_CFcStatsGfpInMBitErrHC_Object = MibTableColumn
cFcStatsGfpInMBitErrHC = _CFcStatsGfpInMBitErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 160),
    _CFcStatsGfpInMBitErrHC_Type()
)
cFcStatsGfpInMBitErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInMBitErrHC.setStatus("current")
_CFcStatsGfpInTypeInvalidHC_Type = Counter64
_CFcStatsGfpInTypeInvalidHC_Object = MibTableColumn
cFcStatsGfpInTypeInvalidHC = _CFcStatsGfpInTypeInvalidHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 170),
    _CFcStatsGfpInTypeInvalidHC_Type()
)
cFcStatsGfpInTypeInvalidHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInTypeInvalidHC.setStatus("current")
_CFcStatsGfpInSBlkCRCErrHC_Type = Counter64
_CFcStatsGfpInSBlkCRCErrHC_Object = MibTableColumn
cFcStatsGfpInSBlkCRCErrHC = _CFcStatsGfpInSBlkCRCErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 2, 1, 180),
    _CFcStatsGfpInSBlkCRCErrHC_Type()
)
cFcStatsGfpInSBlkCRCErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcStatsGfpInSBlkCRCErrHC.setStatus("current")
_CFcHistTable_Object = MibTable
cFcHistTable = _CFcHistTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3)
)
if mibBuilder.loadTexts:
    cFcHistTable.setStatus("current")
_CFcHistEntry_Object = MibTableRow
cFcHistEntry = _CFcHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1)
)
cFcHistEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-FC-MIB", "cFcHistIntervalType"),
    (0, "CERENT-FC-MIB", "cFcHistIntervalNum"),
)
if mibBuilder.loadTexts:
    cFcHistEntry.setStatus("current")
_CFcHistIntervalType_Type = CerentPeriod
_CFcHistIntervalType_Object = MibTableColumn
cFcHistIntervalType = _CFcHistIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 10),
    _CFcHistIntervalType_Type()
)
cFcHistIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cFcHistIntervalType.setStatus("current")


class _CFcHistIntervalNum_Type(Integer32):
    """Custom type cFcHistIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CFcHistIntervalNum_Type.__name__ = "Integer32"
_CFcHistIntervalNum_Object = MibTableColumn
cFcHistIntervalNum = _CFcHistIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 20),
    _CFcHistIntervalNum_Type()
)
cFcHistIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cFcHistIntervalNum.setStatus("current")
_CFcHistInvalidOrdSets_Type = Counter32
_CFcHistInvalidOrdSets_Object = MibTableColumn
cFcHistInvalidOrdSets = _CFcHistInvalidOrdSets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 30),
    _CFcHistInvalidOrdSets_Type()
)
cFcHistInvalidOrdSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInvalidOrdSets.setStatus("current")
_CFcHistInvalidOrdSetsHigh_Type = Counter32
_CFcHistInvalidOrdSetsHigh_Object = MibTableColumn
cFcHistInvalidOrdSetsHigh = _CFcHistInvalidOrdSetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 40),
    _CFcHistInvalidOrdSetsHigh_Type()
)
cFcHistInvalidOrdSetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInvalidOrdSetsHigh.setStatus("current")
_CFcHistEncodingDispErr_Type = Counter32
_CFcHistEncodingDispErr_Object = MibTableColumn
cFcHistEncodingDispErr = _CFcHistEncodingDispErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 50),
    _CFcHistEncodingDispErr_Type()
)
cFcHistEncodingDispErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistEncodingDispErr.setStatus("current")
_CFcHistEncodingDispErrHigh_Type = Counter32
_CFcHistEncodingDispErrHigh_Object = MibTableColumn
cFcHistEncodingDispErrHigh = _CFcHistEncodingDispErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 60),
    _CFcHistEncodingDispErrHigh_Type()
)
cFcHistEncodingDispErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistEncodingDispErrHigh.setStatus("current")
_CFcHistInTotalErr_Type = Counter32
_CFcHistInTotalErr_Object = MibTableColumn
cFcHistInTotalErr = _CFcHistInTotalErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 70),
    _CFcHistInTotalErr_Type()
)
cFcHistInTotalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInTotalErr.setStatus("current")
_CFcHistInTotalErrHigh_Type = Counter32
_CFcHistInTotalErrHigh_Object = MibTableColumn
cFcHistInTotalErrHigh = _CFcHistInTotalErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 80),
    _CFcHistInTotalErrHigh_Type()
)
cFcHistInTotalErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInTotalErrHigh.setStatus("current")
_CFcHistInFramesTrunc_Type = Counter32
_CFcHistInFramesTrunc_Object = MibTableColumn
cFcHistInFramesTrunc = _CFcHistInFramesTrunc_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 90),
    _CFcHistInFramesTrunc_Type()
)
cFcHistInFramesTrunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTrunc.setStatus("current")
_CFcHistInFramesTruncHigh_Type = Counter32
_CFcHistInFramesTruncHigh_Object = MibTableColumn
cFcHistInFramesTruncHigh = _CFcHistInFramesTruncHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 100),
    _CFcHistInFramesTruncHigh_Type()
)
cFcHistInFramesTruncHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTruncHigh.setStatus("current")
_CFcHistInFramesTooLong_Type = Counter32
_CFcHistInFramesTooLong_Object = MibTableColumn
cFcHistInFramesTooLong = _CFcHistInFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 110),
    _CFcHistInFramesTooLong_Type()
)
cFcHistInFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTooLong.setStatus("current")
_CFcHistInFramesTooLongHigh_Type = Counter32
_CFcHistInFramesTooLongHigh_Object = MibTableColumn
cFcHistInFramesTooLongHigh = _CFcHistInFramesTooLongHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 120),
    _CFcHistInFramesTooLongHigh_Type()
)
cFcHistInFramesTooLongHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTooLongHigh.setStatus("current")
_CFcHistInFramesBadCRC_Type = Counter32
_CFcHistInFramesBadCRC_Object = MibTableColumn
cFcHistInFramesBadCRC = _CFcHistInFramesBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 130),
    _CFcHistInFramesBadCRC_Type()
)
cFcHistInFramesBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesBadCRC.setStatus("current")
_CFcHistInFramesBadCRCHigh_Type = Counter32
_CFcHistInFramesBadCRCHigh_Object = MibTableColumn
cFcHistInFramesBadCRCHigh = _CFcHistInFramesBadCRCHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 140),
    _CFcHistInFramesBadCRCHigh_Type()
)
cFcHistInFramesBadCRCHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesBadCRCHigh.setStatus("current")
_CFcHistInFrames_Type = Counter32
_CFcHistInFrames_Object = MibTableColumn
cFcHistInFrames = _CFcHistInFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 150),
    _CFcHistInFrames_Type()
)
cFcHistInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFrames.setStatus("current")
_CFcHistInFramesHigh_Type = Counter32
_CFcHistInFramesHigh_Object = MibTableColumn
cFcHistInFramesHigh = _CFcHistInFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 160),
    _CFcHistInFramesHigh_Type()
)
cFcHistInFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesHigh.setStatus("current")
_CFcHistInElements_Type = Counter32
_CFcHistInElements_Object = MibTableColumn
cFcHistInElements = _CFcHistInElements_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 170),
    _CFcHistInElements_Type()
)
cFcHistInElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInElements.setStatus("current")
_CFcHistInElementsHigh_Type = Counter32
_CFcHistInElementsHigh_Object = MibTableColumn
cFcHistInElementsHigh = _CFcHistInElementsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 180),
    _CFcHistInElementsHigh_Type()
)
cFcHistInElementsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInElementsHigh.setStatus("current")
_CFcHistInDiscards_Type = Counter32
_CFcHistInDiscards_Object = MibTableColumn
cFcHistInDiscards = _CFcHistInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 190),
    _CFcHistInDiscards_Type()
)
cFcHistInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInDiscards.setStatus("current")
_CFcHistInDiscardsHigh_Type = Counter32
_CFcHistInDiscardsHigh_Object = MibTableColumn
cFcHistInDiscardsHigh = _CFcHistInDiscardsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 200),
    _CFcHistInDiscardsHigh_Type()
)
cFcHistInDiscardsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInDiscardsHigh.setStatus("current")
_CFcHistOutFramesBadCRC_Type = Counter32
_CFcHistOutFramesBadCRC_Object = MibTableColumn
cFcHistOutFramesBadCRC = _CFcHistOutFramesBadCRC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 210),
    _CFcHistOutFramesBadCRC_Type()
)
cFcHistOutFramesBadCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFramesBadCRC.setStatus("current")
_CFcHistOutFramesBadCRCHigh_Type = Counter32
_CFcHistOutFramesBadCRCHigh_Object = MibTableColumn
cFcHistOutFramesBadCRCHigh = _CFcHistOutFramesBadCRCHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 220),
    _CFcHistOutFramesBadCRCHigh_Type()
)
cFcHistOutFramesBadCRCHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFramesBadCRCHigh.setStatus("current")
_CFcHistOutFrames_Type = Counter32
_CFcHistOutFrames_Object = MibTableColumn
cFcHistOutFrames = _CFcHistOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 230),
    _CFcHistOutFrames_Type()
)
cFcHistOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFrames.setStatus("current")
_CFcHistOutFramesHigh_Type = Counter32
_CFcHistOutFramesHigh_Object = MibTableColumn
cFcHistOutFramesHigh = _CFcHistOutFramesHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 240),
    _CFcHistOutFramesHigh_Type()
)
cFcHistOutFramesHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFramesHigh.setStatus("current")
_CFcHistOutElements_Type = Counter32
_CFcHistOutElements_Object = MibTableColumn
cFcHistOutElements = _CFcHistOutElements_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 250),
    _CFcHistOutElements_Type()
)
cFcHistOutElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutElements.setStatus("current")
_CFcHistOutElementsHigh_Type = Counter32
_CFcHistOutElementsHigh_Object = MibTableColumn
cFcHistOutElementsHigh = _CFcHistOutElementsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 260),
    _CFcHistOutElementsHigh_Type()
)
cFcHistOutElementsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutElementsHigh.setStatus("current")
_CFcHistOutDiscards_Type = Counter32
_CFcHistOutDiscards_Object = MibTableColumn
cFcHistOutDiscards = _CFcHistOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 270),
    _CFcHistOutDiscards_Type()
)
cFcHistOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutDiscards.setStatus("current")
_CFcHistOutDiscardsHigh_Type = Counter32
_CFcHistOutDiscardsHigh_Object = MibTableColumn
cFcHistOutDiscardsHigh = _CFcHistOutDiscardsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 280),
    _CFcHistOutDiscardsHigh_Type()
)
cFcHistOutDiscardsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutDiscardsHigh.setStatus("current")
_CFcHistLinkResets_Type = Counter32
_CFcHistLinkResets_Object = MibTableColumn
cFcHistLinkResets = _CFcHistLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 290),
    _CFcHistLinkResets_Type()
)
cFcHistLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistLinkResets.setStatus("current")
_CFcHistLinkResetsHigh_Type = Counter32
_CFcHistLinkResetsHigh_Object = MibTableColumn
cFcHistLinkResetsHigh = _CFcHistLinkResetsHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 300),
    _CFcHistLinkResetsHigh_Type()
)
cFcHistLinkResetsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistLinkResetsHigh.setStatus("current")
_CFcHistGfpInSBitErr_Type = Counter32
_CFcHistGfpInSBitErr_Object = MibTableColumn
cFcHistGfpInSBitErr = _CFcHistGfpInSBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 310),
    _CFcHistGfpInSBitErr_Type()
)
cFcHistGfpInSBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBitErr.setStatus("current")
_CFcHistGfpInSBitErrHigh_Type = Counter32
_CFcHistGfpInSBitErrHigh_Object = MibTableColumn
cFcHistGfpInSBitErrHigh = _CFcHistGfpInSBitErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 320),
    _CFcHistGfpInSBitErrHigh_Type()
)
cFcHistGfpInSBitErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBitErrHigh.setStatus("current")
_CFcHistGfpInMBitErr_Type = Counter32
_CFcHistGfpInMBitErr_Object = MibTableColumn
cFcHistGfpInMBitErr = _CFcHistGfpInMBitErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 330),
    _CFcHistGfpInMBitErr_Type()
)
cFcHistGfpInMBitErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInMBitErr.setStatus("current")
_CFcHistGfpInMBitErrHigh_Type = Counter32
_CFcHistGfpInMBitErrHigh_Object = MibTableColumn
cFcHistGfpInMBitErrHigh = _CFcHistGfpInMBitErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 340),
    _CFcHistGfpInMBitErrHigh_Type()
)
cFcHistGfpInMBitErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInMBitErrHigh.setStatus("current")
_CFcHistGfpInTypeInvalid_Type = Counter32
_CFcHistGfpInTypeInvalid_Object = MibTableColumn
cFcHistGfpInTypeInvalid = _CFcHistGfpInTypeInvalid_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 350),
    _CFcHistGfpInTypeInvalid_Type()
)
cFcHistGfpInTypeInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInTypeInvalid.setStatus("current")
_CFcHistGfpInTypeInvalidHigh_Type = Counter32
_CFcHistGfpInTypeInvalidHigh_Object = MibTableColumn
cFcHistGfpInTypeInvalidHigh = _CFcHistGfpInTypeInvalidHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 360),
    _CFcHistGfpInTypeInvalidHigh_Type()
)
cFcHistGfpInTypeInvalidHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInTypeInvalidHigh.setStatus("current")
_CFcHistGfpInSBlkCRCErr_Type = Counter32
_CFcHistGfpInSBlkCRCErr_Object = MibTableColumn
cFcHistGfpInSBlkCRCErr = _CFcHistGfpInSBlkCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 370),
    _CFcHistGfpInSBlkCRCErr_Type()
)
cFcHistGfpInSBlkCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBlkCRCErr.setStatus("current")
_CFcHistGfpInSBlkCRCErrHigh_Type = Counter32
_CFcHistGfpInSBlkCRCErrHigh_Object = MibTableColumn
cFcHistGfpInSBlkCRCErrHigh = _CFcHistGfpInSBlkCRCErrHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 3, 1, 380),
    _CFcHistGfpInSBlkCRCErrHigh_Type()
)
cFcHistGfpInSBlkCRCErrHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBlkCRCErrHigh.setStatus("current")
_CFcHistHCTable_Object = MibTable
cFcHistHCTable = _CFcHistHCTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4)
)
if mibBuilder.loadTexts:
    cFcHistHCTable.setStatus("current")
_CFcHistHCEntry_Object = MibTableRow
cFcHistHCEntry = _CFcHistHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1)
)
cFcHistHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CERENT-FC-MIB", "cFcHistIntervalType"),
    (0, "CERENT-FC-MIB", "cFcHistIntervalNum"),
)
if mibBuilder.loadTexts:
    cFcHistHCEntry.setStatus("current")
_CFcHistInvalidOrdSetsHC_Type = Counter64
_CFcHistInvalidOrdSetsHC_Object = MibTableColumn
cFcHistInvalidOrdSetsHC = _CFcHistInvalidOrdSetsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 10),
    _CFcHistInvalidOrdSetsHC_Type()
)
cFcHistInvalidOrdSetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInvalidOrdSetsHC.setStatus("current")
_CFcHistEncodingDispErrHC_Type = Counter64
_CFcHistEncodingDispErrHC_Object = MibTableColumn
cFcHistEncodingDispErrHC = _CFcHistEncodingDispErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 20),
    _CFcHistEncodingDispErrHC_Type()
)
cFcHistEncodingDispErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistEncodingDispErrHC.setStatus("current")
_CFcHistInTotalErrHC_Type = Counter64
_CFcHistInTotalErrHC_Object = MibTableColumn
cFcHistInTotalErrHC = _CFcHistInTotalErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 30),
    _CFcHistInTotalErrHC_Type()
)
cFcHistInTotalErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInTotalErrHC.setStatus("current")
_CFcHistInFramesTruncHC_Type = Counter64
_CFcHistInFramesTruncHC_Object = MibTableColumn
cFcHistInFramesTruncHC = _CFcHistInFramesTruncHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 40),
    _CFcHistInFramesTruncHC_Type()
)
cFcHistInFramesTruncHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTruncHC.setStatus("current")
_CFcHistInFramesTooLongHC_Type = Counter64
_CFcHistInFramesTooLongHC_Object = MibTableColumn
cFcHistInFramesTooLongHC = _CFcHistInFramesTooLongHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 50),
    _CFcHistInFramesTooLongHC_Type()
)
cFcHistInFramesTooLongHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesTooLongHC.setStatus("current")
_CFcHistInFramesBadCRCHC_Type = Counter64
_CFcHistInFramesBadCRCHC_Object = MibTableColumn
cFcHistInFramesBadCRCHC = _CFcHistInFramesBadCRCHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 60),
    _CFcHistInFramesBadCRCHC_Type()
)
cFcHistInFramesBadCRCHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesBadCRCHC.setStatus("current")
_CFcHistInFramesHC_Type = Counter64
_CFcHistInFramesHC_Object = MibTableColumn
cFcHistInFramesHC = _CFcHistInFramesHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 70),
    _CFcHistInFramesHC_Type()
)
cFcHistInFramesHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInFramesHC.setStatus("current")
_CFcHistInElementsHC_Type = Counter64
_CFcHistInElementsHC_Object = MibTableColumn
cFcHistInElementsHC = _CFcHistInElementsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 80),
    _CFcHistInElementsHC_Type()
)
cFcHistInElementsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInElementsHC.setStatus("current")
_CFcHistInDiscardsHC_Type = Counter64
_CFcHistInDiscardsHC_Object = MibTableColumn
cFcHistInDiscardsHC = _CFcHistInDiscardsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 90),
    _CFcHistInDiscardsHC_Type()
)
cFcHistInDiscardsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistInDiscardsHC.setStatus("current")
_CFcHistOutFramesBadCRCHC_Type = Counter64
_CFcHistOutFramesBadCRCHC_Object = MibTableColumn
cFcHistOutFramesBadCRCHC = _CFcHistOutFramesBadCRCHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 100),
    _CFcHistOutFramesBadCRCHC_Type()
)
cFcHistOutFramesBadCRCHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFramesBadCRCHC.setStatus("current")
_CFcHistOutFramesHC_Type = Counter64
_CFcHistOutFramesHC_Object = MibTableColumn
cFcHistOutFramesHC = _CFcHistOutFramesHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 110),
    _CFcHistOutFramesHC_Type()
)
cFcHistOutFramesHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutFramesHC.setStatus("current")
_CFcHistOutElementsHC_Type = Counter64
_CFcHistOutElementsHC_Object = MibTableColumn
cFcHistOutElementsHC = _CFcHistOutElementsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 120),
    _CFcHistOutElementsHC_Type()
)
cFcHistOutElementsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutElementsHC.setStatus("current")
_CFcHistOutDiscardsHC_Type = Counter64
_CFcHistOutDiscardsHC_Object = MibTableColumn
cFcHistOutDiscardsHC = _CFcHistOutDiscardsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 130),
    _CFcHistOutDiscardsHC_Type()
)
cFcHistOutDiscardsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistOutDiscardsHC.setStatus("current")
_CFcHistLinkResetsHC_Type = Counter64
_CFcHistLinkResetsHC_Object = MibTableColumn
cFcHistLinkResetsHC = _CFcHistLinkResetsHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 140),
    _CFcHistLinkResetsHC_Type()
)
cFcHistLinkResetsHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistLinkResetsHC.setStatus("current")
_CFcHistGfpInSBitErrHC_Type = Counter64
_CFcHistGfpInSBitErrHC_Object = MibTableColumn
cFcHistGfpInSBitErrHC = _CFcHistGfpInSBitErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 150),
    _CFcHistGfpInSBitErrHC_Type()
)
cFcHistGfpInSBitErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBitErrHC.setStatus("current")
_CFcHistGfpInMBitErrHC_Type = Counter64
_CFcHistGfpInMBitErrHC_Object = MibTableColumn
cFcHistGfpInMBitErrHC = _CFcHistGfpInMBitErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 160),
    _CFcHistGfpInMBitErrHC_Type()
)
cFcHistGfpInMBitErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInMBitErrHC.setStatus("current")
_CFcHistGfpInTypeInvalidHC_Type = Counter64
_CFcHistGfpInTypeInvalidHC_Object = MibTableColumn
cFcHistGfpInTypeInvalidHC = _CFcHistGfpInTypeInvalidHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 170),
    _CFcHistGfpInTypeInvalidHC_Type()
)
cFcHistGfpInTypeInvalidHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInTypeInvalidHC.setStatus("current")
_CFcHistGfpInSBlkCRCErrHC_Type = Counter64
_CFcHistGfpInSBlkCRCErrHC_Object = MibTableColumn
cFcHistGfpInSBlkCRCErrHC = _CFcHistGfpInSBlkCRCErrHC_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 4, 1, 180),
    _CFcHistGfpInSBlkCRCErrHC_Type()
)
cFcHistGfpInSBlkCRCErrHC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcHistGfpInSBlkCRCErrHC.setStatus("current")
_CFcAlarmTable_Object = MibTable
cFcAlarmTable = _CFcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5)
)
if mibBuilder.loadTexts:
    cFcAlarmTable.setStatus("current")
_CFcAlarmEntry_Object = MibTableRow
cFcAlarmEntry = _CFcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1)
)
cFcAlarmEntry.setIndexNames(
    (0, "CERENT-FC-MIB", "cFcAlarmIndex"),
)
if mibBuilder.loadTexts:
    cFcAlarmEntry.setStatus("current")


class _CFcAlarmIndex_Type(Integer32):
    """Custom type cFcAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CFcAlarmIndex_Type.__name__ = "Integer32"
_CFcAlarmIndex_Object = MibTableColumn
cFcAlarmIndex = _CFcAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 10),
    _CFcAlarmIndex_Type()
)
cFcAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cFcAlarmIndex.setStatus("current")


class _CFcAlarmInterval_Type(Integer32):
    """Custom type cFcAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8000),
    )


_CFcAlarmInterval_Type.__name__ = "Integer32"
_CFcAlarmInterval_Object = MibTableColumn
cFcAlarmInterval = _CFcAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 20),
    _CFcAlarmInterval_Type()
)
cFcAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmInterval.setStatus("current")
_CFcAlarmVariable_Type = ObjectIdentifier
_CFcAlarmVariable_Object = MibTableColumn
cFcAlarmVariable = _CFcAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 30),
    _CFcAlarmVariable_Type()
)
cFcAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmVariable.setStatus("current")


class _CFcAlarmSampleType_Type(Integer32):
    """Custom type cFcAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_CFcAlarmSampleType_Type.__name__ = "Integer32"
_CFcAlarmSampleType_Object = MibTableColumn
cFcAlarmSampleType = _CFcAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 40),
    _CFcAlarmSampleType_Type()
)
cFcAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmSampleType.setStatus("current")
_CFcAlarmValue_Type = Counter32
_CFcAlarmValue_Object = MibTableColumn
cFcAlarmValue = _CFcAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 50),
    _CFcAlarmValue_Type()
)
cFcAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcAlarmValue.setStatus("current")
_CFcAlarmValueHigh_Type = Counter32
_CFcAlarmValueHigh_Object = MibTableColumn
cFcAlarmValueHigh = _CFcAlarmValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 60),
    _CFcAlarmValueHigh_Type()
)
cFcAlarmValueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cFcAlarmValueHigh.setStatus("current")


class _CFcAlarmStartupAlarm_Type(Integer32):
    """Custom type cFcAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingcFcAlarm", 2),
          ("risingOrFallingcFcAlarm", 3),
          ("risingcFcAlarm", 1))
    )


_CFcAlarmStartupAlarm_Type.__name__ = "Integer32"
_CFcAlarmStartupAlarm_Object = MibTableColumn
cFcAlarmStartupAlarm = _CFcAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 70),
    _CFcAlarmStartupAlarm_Type()
)
cFcAlarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmStartupAlarm.setStatus("current")
_CFcAlarmRisingThreshold_Type = Integer32
_CFcAlarmRisingThreshold_Object = MibTableColumn
cFcAlarmRisingThreshold = _CFcAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 80),
    _CFcAlarmRisingThreshold_Type()
)
cFcAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmRisingThreshold.setStatus("current")
_CFcAlarmRisingThresholdHigh_Type = Integer32
_CFcAlarmRisingThresholdHigh_Object = MibTableColumn
cFcAlarmRisingThresholdHigh = _CFcAlarmRisingThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 90),
    _CFcAlarmRisingThresholdHigh_Type()
)
cFcAlarmRisingThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmRisingThresholdHigh.setStatus("current")
_CFcAlarmFallingThreshold_Type = Integer32
_CFcAlarmFallingThreshold_Object = MibTableColumn
cFcAlarmFallingThreshold = _CFcAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 100),
    _CFcAlarmFallingThreshold_Type()
)
cFcAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmFallingThreshold.setStatus("current")
_CFcAlarmFallingThresholdHigh_Type = Integer32
_CFcAlarmFallingThresholdHigh_Object = MibTableColumn
cFcAlarmFallingThresholdHigh = _CFcAlarmFallingThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 110),
    _CFcAlarmFallingThresholdHigh_Type()
)
cFcAlarmFallingThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmFallingThresholdHigh.setStatus("current")


class _CFcAlarmStatus_Type(Integer32):
    """Custom type cFcAlarmStatus based on Integer32"""
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


_CFcAlarmStatus_Type.__name__ = "Integer32"
_CFcAlarmStatus_Object = MibTableColumn
cFcAlarmStatus = _CFcAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 60, 1, 5, 1, 120),
    _CFcAlarmStatus_Type()
)
cFcAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cFcAlarmStatus.setStatus("current")
_CerentFcMIBConformance_ObjectIdentity = ObjectIdentity
cerentFcMIBConformance = _CerentFcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40)
)
_CerentFcMIBCompliances_ObjectIdentity = ObjectIdentity
cerentFcMIBCompliances = _CerentFcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 1)
)
_CerentFcMIBGroups_ObjectIdentity = ObjectIdentity
cerentFcMIBGroups = _CerentFcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2)
)

# Managed Objects groups

cerentFcStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2, 1)
)
cerentFcStatsGroup.setObjects(
      *(("CERENT-FC-MIB", "cFcStatsInvalidOrdSets"),
        ("CERENT-FC-MIB", "cFcStatsInvalidOrdSetsHigh"),
        ("CERENT-FC-MIB", "cFcStatsEncodingDispErr"),
        ("CERENT-FC-MIB", "cFcStatsEncodingDispErrHigh"),
        ("CERENT-FC-MIB", "cFcStatsInTotalErr"),
        ("CERENT-FC-MIB", "cFcStatsInTotalErrHigh"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTrunc"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTruncHigh"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTooLong"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTooLongHigh"),
        ("CERENT-FC-MIB", "cFcStatsInFramesBadCRC"),
        ("CERENT-FC-MIB", "cFcStatsInFramesBadCRCHigh"),
        ("CERENT-FC-MIB", "cFcStatsInFrames"),
        ("CERENT-FC-MIB", "cFcStatsInFramesHigh"),
        ("CERENT-FC-MIB", "cFcStatsInElements"),
        ("CERENT-FC-MIB", "cFcStatsInElementsHigh"),
        ("CERENT-FC-MIB", "cFcStatsInDiscards"),
        ("CERENT-FC-MIB", "cFcStatsInDiscardsHigh"),
        ("CERENT-FC-MIB", "cFcStatsOutFramesBadCRC"),
        ("CERENT-FC-MIB", "cFcStatsOutFramesBadCRCHigh"),
        ("CERENT-FC-MIB", "cFcStatsOutFrames"),
        ("CERENT-FC-MIB", "cFcStatsOutFramesHigh"),
        ("CERENT-FC-MIB", "cFcStatsOutElements"),
        ("CERENT-FC-MIB", "cFcStatsOutElementsHigh"),
        ("CERENT-FC-MIB", "cFcStatsOutDiscards"),
        ("CERENT-FC-MIB", "cFcStatsOutDiscardsHigh"),
        ("CERENT-FC-MIB", "cFcStatsLinkResets"),
        ("CERENT-FC-MIB", "cFcStatsLinkResetsHigh"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBitErr"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBitErrHigh"),
        ("CERENT-FC-MIB", "cFcStatsGfpInMBitErr"),
        ("CERENT-FC-MIB", "cFcStatsGfpInMBitErrHigh"),
        ("CERENT-FC-MIB", "cFcStatsGfpInTypeInvalid"),
        ("CERENT-FC-MIB", "cFcStatsGfpInTypeInvalidHigh"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBlkCRCErr"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBlkCRCErrHigh"))
)
if mibBuilder.loadTexts:
    cerentFcStatsGroup.setStatus("current")

cerentFcHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2, 2)
)
cerentFcHistGroup.setObjects(
      *(("CERENT-FC-MIB", "cFcHistInvalidOrdSets"),
        ("CERENT-FC-MIB", "cFcHistInvalidOrdSetsHigh"),
        ("CERENT-FC-MIB", "cFcHistEncodingDispErr"),
        ("CERENT-FC-MIB", "cFcHistEncodingDispErrHigh"),
        ("CERENT-FC-MIB", "cFcHistInTotalErr"),
        ("CERENT-FC-MIB", "cFcHistInTotalErrHigh"),
        ("CERENT-FC-MIB", "cFcHistInFramesTrunc"),
        ("CERENT-FC-MIB", "cFcHistInFramesTruncHigh"),
        ("CERENT-FC-MIB", "cFcHistInFramesTooLong"),
        ("CERENT-FC-MIB", "cFcHistInFramesTooLongHigh"),
        ("CERENT-FC-MIB", "cFcHistInFramesBadCRC"),
        ("CERENT-FC-MIB", "cFcHistInFramesBadCRCHigh"),
        ("CERENT-FC-MIB", "cFcHistInFrames"),
        ("CERENT-FC-MIB", "cFcHistInFramesHigh"),
        ("CERENT-FC-MIB", "cFcHistInElements"),
        ("CERENT-FC-MIB", "cFcHistInElementsHigh"),
        ("CERENT-FC-MIB", "cFcHistInDiscards"),
        ("CERENT-FC-MIB", "cFcHistInDiscardsHigh"),
        ("CERENT-FC-MIB", "cFcHistOutFramesBadCRC"),
        ("CERENT-FC-MIB", "cFcHistOutFramesBadCRCHigh"),
        ("CERENT-FC-MIB", "cFcHistOutFrames"),
        ("CERENT-FC-MIB", "cFcHistOutFramesHigh"),
        ("CERENT-FC-MIB", "cFcHistOutElements"),
        ("CERENT-FC-MIB", "cFcHistOutElementsHigh"),
        ("CERENT-FC-MIB", "cFcHistOutDiscards"),
        ("CERENT-FC-MIB", "cFcHistOutDiscardsHigh"),
        ("CERENT-FC-MIB", "cFcHistLinkResets"),
        ("CERENT-FC-MIB", "cFcHistLinkResetsHigh"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBitErr"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBitErrHigh"),
        ("CERENT-FC-MIB", "cFcHistGfpInMBitErr"),
        ("CERENT-FC-MIB", "cFcHistGfpInMBitErrHigh"),
        ("CERENT-FC-MIB", "cFcHistGfpInTypeInvalid"),
        ("CERENT-FC-MIB", "cFcHistGfpInTypeInvalidHigh"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBlkCRCErr"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBlkCRCErrHigh"))
)
if mibBuilder.loadTexts:
    cerentFcHistGroup.setStatus("current")

cerentFcStatsHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2, 3)
)
cerentFcStatsHCGroup.setObjects(
      *(("CERENT-FC-MIB", "cFcStatsInvalidOrdSetsHC"),
        ("CERENT-FC-MIB", "cFcStatsEncodingDispErrHC"),
        ("CERENT-FC-MIB", "cFcStatsInTotalErrHC"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTruncHC"),
        ("CERENT-FC-MIB", "cFcStatsInFramesTooLongHC"),
        ("CERENT-FC-MIB", "cFcStatsInFramesBadCRCHC"),
        ("CERENT-FC-MIB", "cFcStatsInFramesHC"),
        ("CERENT-FC-MIB", "cFcStatsInElementsHC"),
        ("CERENT-FC-MIB", "cFcStatsInDiscardsHC"),
        ("CERENT-FC-MIB", "cFcStatsOutFramesBadCRCHC"),
        ("CERENT-FC-MIB", "cFcStatsOutFramesHC"),
        ("CERENT-FC-MIB", "cFcStatsOutElementsHC"),
        ("CERENT-FC-MIB", "cFcStatsOutDiscardsHC"),
        ("CERENT-FC-MIB", "cFcStatsLinkResetsHC"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBitErrHC"),
        ("CERENT-FC-MIB", "cFcStatsGfpInMBitErrHC"),
        ("CERENT-FC-MIB", "cFcStatsGfpInTypeInvalidHC"),
        ("CERENT-FC-MIB", "cFcStatsGfpInSBlkCRCErrHC"))
)
if mibBuilder.loadTexts:
    cerentFcStatsHCGroup.setStatus("current")

cerentFcHistHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2, 4)
)
cerentFcHistHCGroup.setObjects(
      *(("CERENT-FC-MIB", "cFcHistInvalidOrdSetsHC"),
        ("CERENT-FC-MIB", "cFcHistEncodingDispErrHC"),
        ("CERENT-FC-MIB", "cFcHistInTotalErrHC"),
        ("CERENT-FC-MIB", "cFcHistInFramesTruncHC"),
        ("CERENT-FC-MIB", "cFcHistInFramesTooLongHC"),
        ("CERENT-FC-MIB", "cFcHistInFramesBadCRCHC"),
        ("CERENT-FC-MIB", "cFcHistInFramesHC"),
        ("CERENT-FC-MIB", "cFcHistInElementsHC"),
        ("CERENT-FC-MIB", "cFcHistInDiscardsHC"),
        ("CERENT-FC-MIB", "cFcHistOutFramesBadCRCHC"),
        ("CERENT-FC-MIB", "cFcHistOutFramesHC"),
        ("CERENT-FC-MIB", "cFcHistOutElementsHC"),
        ("CERENT-FC-MIB", "cFcHistOutDiscardsHC"),
        ("CERENT-FC-MIB", "cFcHistLinkResetsHC"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBitErrHC"),
        ("CERENT-FC-MIB", "cFcHistGfpInMBitErrHC"),
        ("CERENT-FC-MIB", "cFcHistGfpInTypeInvalidHC"),
        ("CERENT-FC-MIB", "cFcHistGfpInSBlkCRCErrHC"))
)
if mibBuilder.loadTexts:
    cerentFcHistHCGroup.setStatus("current")

cerentFcAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 2, 5)
)
cerentFcAlarmGroup.setObjects(
      *(("CERENT-FC-MIB", "cFcAlarmInterval"),
        ("CERENT-FC-MIB", "cFcAlarmVariable"),
        ("CERENT-FC-MIB", "cFcAlarmSampleType"),
        ("CERENT-FC-MIB", "cFcAlarmValue"),
        ("CERENT-FC-MIB", "cFcAlarmValueHigh"),
        ("CERENT-FC-MIB", "cFcAlarmStartupAlarm"),
        ("CERENT-FC-MIB", "cFcAlarmRisingThreshold"),
        ("CERENT-FC-MIB", "cFcAlarmRisingThresholdHigh"),
        ("CERENT-FC-MIB", "cFcAlarmFallingThreshold"),
        ("CERENT-FC-MIB", "cFcAlarmFallingThresholdHigh"),
        ("CERENT-FC-MIB", "cFcAlarmStatus"))
)
if mibBuilder.loadTexts:
    cerentFcAlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentFcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 40, 1, 1)
)
if mibBuilder.loadTexts:
    cerentFcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-FC-MIB",
    **{"cerentFcMIB": cerentFcMIB,
       "cerentFcMIBObjects": cerentFcMIBObjects,
       "cerentFc": cerentFc,
       "cFcStatsTable": cFcStatsTable,
       "cFcStatsEntry": cFcStatsEntry,
       "cFcStatsInvalidOrdSets": cFcStatsInvalidOrdSets,
       "cFcStatsInvalidOrdSetsHigh": cFcStatsInvalidOrdSetsHigh,
       "cFcStatsEncodingDispErr": cFcStatsEncodingDispErr,
       "cFcStatsEncodingDispErrHigh": cFcStatsEncodingDispErrHigh,
       "cFcStatsInTotalErr": cFcStatsInTotalErr,
       "cFcStatsInTotalErrHigh": cFcStatsInTotalErrHigh,
       "cFcStatsInFramesTrunc": cFcStatsInFramesTrunc,
       "cFcStatsInFramesTruncHigh": cFcStatsInFramesTruncHigh,
       "cFcStatsInFramesTooLong": cFcStatsInFramesTooLong,
       "cFcStatsInFramesTooLongHigh": cFcStatsInFramesTooLongHigh,
       "cFcStatsInFramesBadCRC": cFcStatsInFramesBadCRC,
       "cFcStatsInFramesBadCRCHigh": cFcStatsInFramesBadCRCHigh,
       "cFcStatsInFrames": cFcStatsInFrames,
       "cFcStatsInFramesHigh": cFcStatsInFramesHigh,
       "cFcStatsInElements": cFcStatsInElements,
       "cFcStatsInElementsHigh": cFcStatsInElementsHigh,
       "cFcStatsInDiscards": cFcStatsInDiscards,
       "cFcStatsInDiscardsHigh": cFcStatsInDiscardsHigh,
       "cFcStatsOutFramesBadCRC": cFcStatsOutFramesBadCRC,
       "cFcStatsOutFramesBadCRCHigh": cFcStatsOutFramesBadCRCHigh,
       "cFcStatsOutFrames": cFcStatsOutFrames,
       "cFcStatsOutFramesHigh": cFcStatsOutFramesHigh,
       "cFcStatsOutElements": cFcStatsOutElements,
       "cFcStatsOutElementsHigh": cFcStatsOutElementsHigh,
       "cFcStatsOutDiscards": cFcStatsOutDiscards,
       "cFcStatsOutDiscardsHigh": cFcStatsOutDiscardsHigh,
       "cFcStatsLinkResets": cFcStatsLinkResets,
       "cFcStatsLinkResetsHigh": cFcStatsLinkResetsHigh,
       "cFcStatsGfpInSBitErr": cFcStatsGfpInSBitErr,
       "cFcStatsGfpInSBitErrHigh": cFcStatsGfpInSBitErrHigh,
       "cFcStatsGfpInMBitErr": cFcStatsGfpInMBitErr,
       "cFcStatsGfpInMBitErrHigh": cFcStatsGfpInMBitErrHigh,
       "cFcStatsGfpInTypeInvalid": cFcStatsGfpInTypeInvalid,
       "cFcStatsGfpInTypeInvalidHigh": cFcStatsGfpInTypeInvalidHigh,
       "cFcStatsGfpInSBlkCRCErr": cFcStatsGfpInSBlkCRCErr,
       "cFcStatsGfpInSBlkCRCErrHigh": cFcStatsGfpInSBlkCRCErrHigh,
       "cFcStatsHCTable": cFcStatsHCTable,
       "cFcStatsHCEntry": cFcStatsHCEntry,
       "cFcStatsInvalidOrdSetsHC": cFcStatsInvalidOrdSetsHC,
       "cFcStatsEncodingDispErrHC": cFcStatsEncodingDispErrHC,
       "cFcStatsInTotalErrHC": cFcStatsInTotalErrHC,
       "cFcStatsInFramesTruncHC": cFcStatsInFramesTruncHC,
       "cFcStatsInFramesTooLongHC": cFcStatsInFramesTooLongHC,
       "cFcStatsInFramesBadCRCHC": cFcStatsInFramesBadCRCHC,
       "cFcStatsInFramesHC": cFcStatsInFramesHC,
       "cFcStatsInElementsHC": cFcStatsInElementsHC,
       "cFcStatsInDiscardsHC": cFcStatsInDiscardsHC,
       "cFcStatsOutFramesBadCRCHC": cFcStatsOutFramesBadCRCHC,
       "cFcStatsOutFramesHC": cFcStatsOutFramesHC,
       "cFcStatsOutElementsHC": cFcStatsOutElementsHC,
       "cFcStatsOutDiscardsHC": cFcStatsOutDiscardsHC,
       "cFcStatsLinkResetsHC": cFcStatsLinkResetsHC,
       "cFcStatsGfpInSBitErrHC": cFcStatsGfpInSBitErrHC,
       "cFcStatsGfpInMBitErrHC": cFcStatsGfpInMBitErrHC,
       "cFcStatsGfpInTypeInvalidHC": cFcStatsGfpInTypeInvalidHC,
       "cFcStatsGfpInSBlkCRCErrHC": cFcStatsGfpInSBlkCRCErrHC,
       "cFcHistTable": cFcHistTable,
       "cFcHistEntry": cFcHistEntry,
       "cFcHistIntervalType": cFcHistIntervalType,
       "cFcHistIntervalNum": cFcHistIntervalNum,
       "cFcHistInvalidOrdSets": cFcHistInvalidOrdSets,
       "cFcHistInvalidOrdSetsHigh": cFcHistInvalidOrdSetsHigh,
       "cFcHistEncodingDispErr": cFcHistEncodingDispErr,
       "cFcHistEncodingDispErrHigh": cFcHistEncodingDispErrHigh,
       "cFcHistInTotalErr": cFcHistInTotalErr,
       "cFcHistInTotalErrHigh": cFcHistInTotalErrHigh,
       "cFcHistInFramesTrunc": cFcHistInFramesTrunc,
       "cFcHistInFramesTruncHigh": cFcHistInFramesTruncHigh,
       "cFcHistInFramesTooLong": cFcHistInFramesTooLong,
       "cFcHistInFramesTooLongHigh": cFcHistInFramesTooLongHigh,
       "cFcHistInFramesBadCRC": cFcHistInFramesBadCRC,
       "cFcHistInFramesBadCRCHigh": cFcHistInFramesBadCRCHigh,
       "cFcHistInFrames": cFcHistInFrames,
       "cFcHistInFramesHigh": cFcHistInFramesHigh,
       "cFcHistInElements": cFcHistInElements,
       "cFcHistInElementsHigh": cFcHistInElementsHigh,
       "cFcHistInDiscards": cFcHistInDiscards,
       "cFcHistInDiscardsHigh": cFcHistInDiscardsHigh,
       "cFcHistOutFramesBadCRC": cFcHistOutFramesBadCRC,
       "cFcHistOutFramesBadCRCHigh": cFcHistOutFramesBadCRCHigh,
       "cFcHistOutFrames": cFcHistOutFrames,
       "cFcHistOutFramesHigh": cFcHistOutFramesHigh,
       "cFcHistOutElements": cFcHistOutElements,
       "cFcHistOutElementsHigh": cFcHistOutElementsHigh,
       "cFcHistOutDiscards": cFcHistOutDiscards,
       "cFcHistOutDiscardsHigh": cFcHistOutDiscardsHigh,
       "cFcHistLinkResets": cFcHistLinkResets,
       "cFcHistLinkResetsHigh": cFcHistLinkResetsHigh,
       "cFcHistGfpInSBitErr": cFcHistGfpInSBitErr,
       "cFcHistGfpInSBitErrHigh": cFcHistGfpInSBitErrHigh,
       "cFcHistGfpInMBitErr": cFcHistGfpInMBitErr,
       "cFcHistGfpInMBitErrHigh": cFcHistGfpInMBitErrHigh,
       "cFcHistGfpInTypeInvalid": cFcHistGfpInTypeInvalid,
       "cFcHistGfpInTypeInvalidHigh": cFcHistGfpInTypeInvalidHigh,
       "cFcHistGfpInSBlkCRCErr": cFcHistGfpInSBlkCRCErr,
       "cFcHistGfpInSBlkCRCErrHigh": cFcHistGfpInSBlkCRCErrHigh,
       "cFcHistHCTable": cFcHistHCTable,
       "cFcHistHCEntry": cFcHistHCEntry,
       "cFcHistInvalidOrdSetsHC": cFcHistInvalidOrdSetsHC,
       "cFcHistEncodingDispErrHC": cFcHistEncodingDispErrHC,
       "cFcHistInTotalErrHC": cFcHistInTotalErrHC,
       "cFcHistInFramesTruncHC": cFcHistInFramesTruncHC,
       "cFcHistInFramesTooLongHC": cFcHistInFramesTooLongHC,
       "cFcHistInFramesBadCRCHC": cFcHistInFramesBadCRCHC,
       "cFcHistInFramesHC": cFcHistInFramesHC,
       "cFcHistInElementsHC": cFcHistInElementsHC,
       "cFcHistInDiscardsHC": cFcHistInDiscardsHC,
       "cFcHistOutFramesBadCRCHC": cFcHistOutFramesBadCRCHC,
       "cFcHistOutFramesHC": cFcHistOutFramesHC,
       "cFcHistOutElementsHC": cFcHistOutElementsHC,
       "cFcHistOutDiscardsHC": cFcHistOutDiscardsHC,
       "cFcHistLinkResetsHC": cFcHistLinkResetsHC,
       "cFcHistGfpInSBitErrHC": cFcHistGfpInSBitErrHC,
       "cFcHistGfpInMBitErrHC": cFcHistGfpInMBitErrHC,
       "cFcHistGfpInTypeInvalidHC": cFcHistGfpInTypeInvalidHC,
       "cFcHistGfpInSBlkCRCErrHC": cFcHistGfpInSBlkCRCErrHC,
       "cFcAlarmTable": cFcAlarmTable,
       "cFcAlarmEntry": cFcAlarmEntry,
       "cFcAlarmIndex": cFcAlarmIndex,
       "cFcAlarmInterval": cFcAlarmInterval,
       "cFcAlarmVariable": cFcAlarmVariable,
       "cFcAlarmSampleType": cFcAlarmSampleType,
       "cFcAlarmValue": cFcAlarmValue,
       "cFcAlarmValueHigh": cFcAlarmValueHigh,
       "cFcAlarmStartupAlarm": cFcAlarmStartupAlarm,
       "cFcAlarmRisingThreshold": cFcAlarmRisingThreshold,
       "cFcAlarmRisingThresholdHigh": cFcAlarmRisingThresholdHigh,
       "cFcAlarmFallingThreshold": cFcAlarmFallingThreshold,
       "cFcAlarmFallingThresholdHigh": cFcAlarmFallingThresholdHigh,
       "cFcAlarmStatus": cFcAlarmStatus,
       "cerentFcMIBConformance": cerentFcMIBConformance,
       "cerentFcMIBCompliances": cerentFcMIBCompliances,
       "cerentFcMIBCompliance": cerentFcMIBCompliance,
       "cerentFcMIBGroups": cerentFcMIBGroups,
       "cerentFcStatsGroup": cerentFcStatsGroup,
       "cerentFcHistGroup": cerentFcHistGroup,
       "cerentFcStatsHCGroup": cerentFcStatsHCGroup,
       "cerentFcHistHCGroup": cerentFcHistHCGroup,
       "cerentFcAlarmGroup": cerentFcAlarmGroup}
)
