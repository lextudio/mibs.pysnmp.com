# SNMP MIB module (CISCO-DMN-DSG-TRANSCODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-TRANSCODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:36 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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

ciscoDSGTranscode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37)
)
ciscoDSGTranscode.setRevisions(
        ("2013-07-10 12:20",
         "2012-03-20 18:00",
         "2010-10-13 08:00",
         "2010-08-24 07:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TranscoderInfo_ObjectIdentity = ObjectIdentity
transcoderInfo = _TranscoderInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 1)
)


class _TranscoderLOIAction_Type(Integer32):
    """Custom type transcoderLOIAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blackOutput", 1),
          ("noOutput", 2))
    )


_TranscoderLOIAction_Type.__name__ = "Integer32"
_TranscoderLOIAction_Object = MibScalar
transcoderLOIAction = _TranscoderLOIAction_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 1, 1),
    _TranscoderLOIAction_Type()
)
transcoderLOIAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderLOIAction.setStatus("current")
_TranscoderTable_ObjectIdentity = ObjectIdentity
transcoderTable = _TranscoderTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2)
)
_TranscoderCfgTable_Object = MibTable
transcoderCfgTable = _TranscoderCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1)
)
if mibBuilder.loadTexts:
    transcoderCfgTable.setStatus("current")
_TranscoderCfgEntry_Object = MibTableRow
transcoderCfgEntry = _TranscoderCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1)
)
transcoderCfgEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderCfgIndex"),
)
if mibBuilder.loadTexts:
    transcoderCfgEntry.setStatus("current")


class _TranscoderCfgIndex_Type(Integer32):
    """Custom type transcoderCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TranscoderCfgIndex_Type.__name__ = "Integer32"
_TranscoderCfgIndex_Object = MibTableColumn
transcoderCfgIndex = _TranscoderCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 1),
    _TranscoderCfgIndex_Type()
)
transcoderCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgIndex.setStatus("current")


class _TranscoderCfgApplyInband_Type(Integer32):
    """Custom type transcoderCfgApplyInband based on Integer32"""
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


_TranscoderCfgApplyInband_Type.__name__ = "Integer32"
_TranscoderCfgApplyInband_Object = MibTableColumn
transcoderCfgApplyInband = _TranscoderCfgApplyInband_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 2),
    _TranscoderCfgApplyInband_Type()
)
transcoderCfgApplyInband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgApplyInband.setStatus("current")


class _TranscoderCfgVRes_Type(Integer32):
    """Custom type transcoderCfgVRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("hdOut", 4),
          ("sdOut", 5))
    )


_TranscoderCfgVRes_Type.__name__ = "Integer32"
_TranscoderCfgVRes_Object = MibTableColumn
transcoderCfgVRes = _TranscoderCfgVRes_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 3),
    _TranscoderCfgVRes_Type()
)
transcoderCfgVRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgVRes.setStatus("current")


class _TranscoderCfgCCPkt1_Type(Integer32):
    """Custom type transcoderCfgCCPkt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccCEA708", 2),
          ("ccSCTE20", 3),
          ("none", 1))
    )


_TranscoderCfgCCPkt1_Type.__name__ = "Integer32"
_TranscoderCfgCCPkt1_Object = MibTableColumn
transcoderCfgCCPkt1 = _TranscoderCfgCCPkt1_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 4),
    _TranscoderCfgCCPkt1_Type()
)
transcoderCfgCCPkt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgCCPkt1.setStatus("current")


class _TranscoderCfgCCPkt2_Type(Integer32):
    """Custom type transcoderCfgCCPkt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccCEA708", 2),
          ("ccSCTE20", 3),
          ("none", 1))
    )


_TranscoderCfgCCPkt2_Type.__name__ = "Integer32"
_TranscoderCfgCCPkt2_Object = MibTableColumn
transcoderCfgCCPkt2 = _TranscoderCfgCCPkt2_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 5),
    _TranscoderCfgCCPkt2_Type()
)
transcoderCfgCCPkt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgCCPkt2.setStatus("current")


class _TranscoderCfgCCPkt3_Type(Integer32):
    """Custom type transcoderCfgCCPkt3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccCEA708", 2),
          ("ccSCTE20", 3),
          ("none", 1))
    )


_TranscoderCfgCCPkt3_Type.__name__ = "Integer32"
_TranscoderCfgCCPkt3_Object = MibTableColumn
transcoderCfgCCPkt3 = _TranscoderCfgCCPkt3_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 6),
    _TranscoderCfgCCPkt3_Type()
)
transcoderCfgCCPkt3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgCCPkt3.setStatus("current")


class _TranscoderCfgPCRRate_Type(Integer32):
    """Custom type transcoderCfgPCRRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_TranscoderCfgPCRRate_Type.__name__ = "Integer32"
_TranscoderCfgPCRRate_Object = MibTableColumn
transcoderCfgPCRRate = _TranscoderCfgPCRRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 7),
    _TranscoderCfgPCRRate_Type()
)
transcoderCfgPCRRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgPCRRate.setStatus("current")


class _TranscoderCfgHDHRes_Type(Integer32):
    """Custom type transcoderCfgHDHRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1440,
              1920)
        )
    )
    namedValues = NamedValues(
        *(("full", 1920),
          ("threeQuarter", 1440))
    )


_TranscoderCfgHDHRes_Type.__name__ = "Integer32"
_TranscoderCfgHDHRes_Object = MibTableColumn
transcoderCfgHDHRes = _TranscoderCfgHDHRes_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 8),
    _TranscoderCfgHDHRes_Type()
)
transcoderCfgHDHRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHDHRes.setStatus("current")


class _TranscoderCfgHDBitrateMode_Type(Integer32):
    """Custom type transcoderCfgHDBitrateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr", 2))
    )


_TranscoderCfgHDBitrateMode_Type.__name__ = "Integer32"
_TranscoderCfgHDBitrateMode_Object = MibTableColumn
transcoderCfgHDBitrateMode = _TranscoderCfgHDBitrateMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 9),
    _TranscoderCfgHDBitrateMode_Type()
)
transcoderCfgHDBitrateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHDBitrateMode.setStatus("current")


class _TranscoderCfgHDBitRate_Type(Integer32):
    """Custom type transcoderCfgHDBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8000000, 25000000),
    )


_TranscoderCfgHDBitRate_Type.__name__ = "Integer32"
_TranscoderCfgHDBitRate_Object = MibTableColumn
transcoderCfgHDBitRate = _TranscoderCfgHDBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 10),
    _TranscoderCfgHDBitRate_Type()
)
transcoderCfgHDBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHDBitRate.setStatus("current")


class _TranscoderCfgHDGOP_Type(Integer32):
    """Custom type transcoderCfgHDGOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iFrameSync", 1),
          ("userGop", 2))
    )


_TranscoderCfgHDGOP_Type.__name__ = "Integer32"
_TranscoderCfgHDGOP_Object = MibTableColumn
transcoderCfgHDGOP = _TranscoderCfgHDGOP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 11),
    _TranscoderCfgHDGOP_Type()
)
transcoderCfgHDGOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHDGOP.setStatus("current")


class _TranscoderCfgHDManualGOP_Type(Integer32):
    """Custom type transcoderCfgHDManualGOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              122,
              152,
              242,
              302)
        )
    )
    namedValues = NamedValues(
        *(("manualGOP10", 10),
          ("manualGOP122", 122),
          ("manualGOP152", 152),
          ("manualGOP242", 242),
          ("manualGOP302", 302))
    )


_TranscoderCfgHDManualGOP_Type.__name__ = "Integer32"
_TranscoderCfgHDManualGOP_Object = MibTableColumn
transcoderCfgHDManualGOP = _TranscoderCfgHDManualGOP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 12),
    _TranscoderCfgHDManualGOP_Type()
)
transcoderCfgHDManualGOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHDManualGOP.setStatus("current")


class _TranscoderCfgHD32PullDown_Type(Integer32):
    """Custom type transcoderCfgHD32PullDown based on Integer32"""
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


_TranscoderCfgHD32PullDown_Type.__name__ = "Integer32"
_TranscoderCfgHD32PullDown_Object = MibTableColumn
transcoderCfgHD32PullDown = _TranscoderCfgHD32PullDown_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 13),
    _TranscoderCfgHD32PullDown_Type()
)
transcoderCfgHD32PullDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgHD32PullDown.setStatus("current")


class _TranscoderCfgHDAspectRatio_Type(Integer32):
    """Custom type transcoderCfgHDAspectRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourThird", 1),
          ("sixteenNinth", 2))
    )


_TranscoderCfgHDAspectRatio_Type.__name__ = "Integer32"
_TranscoderCfgHDAspectRatio_Object = MibTableColumn
transcoderCfgHDAspectRatio = _TranscoderCfgHDAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 14),
    _TranscoderCfgHDAspectRatio_Type()
)
transcoderCfgHDAspectRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgHDAspectRatio.setStatus("current")


class _TranscoderCfgHDARConversion_Type(Integer32):
    """Custom type transcoderCfgHDARConversion based on Integer32"""
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
        *(("auto", 2),
          ("autoAFD", 3),
          ("fourByThreeFullHeight", 7),
          ("fourByThreeLetterBox", 4),
          ("fourByThreePillarBox", 5),
          ("fourteenByNine", 6),
          ("none", 1),
          ("sixteenByNineFullWidth", 8))
    )


_TranscoderCfgHDARConversion_Type.__name__ = "Integer32"
_TranscoderCfgHDARConversion_Object = MibTableColumn
transcoderCfgHDARConversion = _TranscoderCfgHDARConversion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 15),
    _TranscoderCfgHDARConversion_Type()
)
transcoderCfgHDARConversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgHDARConversion.setStatus("current")


class _TranscoderCfgHDVideoPreproc_Type(Integer32):
    """Custom type transcoderCfgHDVideoPreproc based on Integer32"""
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
        *(("deBlock", 2),
          ("edgeEnhancement", 4),
          ("mosquito", 3),
          ("none", 1))
    )


_TranscoderCfgHDVideoPreproc_Type.__name__ = "Integer32"
_TranscoderCfgHDVideoPreproc_Object = MibTableColumn
transcoderCfgHDVideoPreproc = _TranscoderCfgHDVideoPreproc_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 16),
    _TranscoderCfgHDVideoPreproc_Type()
)
transcoderCfgHDVideoPreproc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgHDVideoPreproc.setStatus("current")


class _TranscoderCfgSDHRes_Type(Integer32):
    """Custom type transcoderCfgSDHRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(352,
              480,
              528,
              544,
              704,
              720)
        )
    )
    namedValues = NamedValues(
        *(("fiveHundredAndFourtyFour", 544),
          ("fiveHundredAndTwentyEight", 528),
          ("fourHundredAndEighty", 480),
          ("sevenHundredAndFour", 704),
          ("sevenHundredAndTwenty", 720),
          ("threeHundredAndFiftyTwo", 352))
    )


_TranscoderCfgSDHRes_Type.__name__ = "Integer32"
_TranscoderCfgSDHRes_Object = MibTableColumn
transcoderCfgSDHRes = _TranscoderCfgSDHRes_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 17),
    _TranscoderCfgSDHRes_Type()
)
transcoderCfgSDHRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDHRes.setStatus("current")


class _TranscoderCfgSDBitRateMode_Type(Integer32):
    """Custom type transcoderCfgSDBitRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr", 2))
    )


_TranscoderCfgSDBitRateMode_Type.__name__ = "Integer32"
_TranscoderCfgSDBitRateMode_Object = MibTableColumn
transcoderCfgSDBitRateMode = _TranscoderCfgSDBitRateMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 18),
    _TranscoderCfgSDBitRateMode_Type()
)
transcoderCfgSDBitRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDBitRateMode.setStatus("current")


class _TranscoderCfgSDBitRate_Type(Integer32):
    """Custom type transcoderCfgSDBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000000, 15000000),
    )


_TranscoderCfgSDBitRate_Type.__name__ = "Integer32"
_TranscoderCfgSDBitRate_Object = MibTableColumn
transcoderCfgSDBitRate = _TranscoderCfgSDBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 19),
    _TranscoderCfgSDBitRate_Type()
)
transcoderCfgSDBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDBitRate.setStatus("current")


class _TranscoderCfgSDGOP_Type(Integer32):
    """Custom type transcoderCfgSDGOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iFrameSync", 1),
          ("userGOPmn", 2))
    )


_TranscoderCfgSDGOP_Type.__name__ = "Integer32"
_TranscoderCfgSDGOP_Object = MibTableColumn
transcoderCfgSDGOP = _TranscoderCfgSDGOP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 20),
    _TranscoderCfgSDGOP_Type()
)
transcoderCfgSDGOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDGOP.setStatus("current")


class _TranscoderCfgSDManualGOP_Type(Integer32):
    """Custom type transcoderCfgSDManualGOP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              122,
              152,
              242,
              302)
        )
    )
    namedValues = NamedValues(
        *(("manualgop10", 10),
          ("manualgop122", 122),
          ("manualgop152", 152),
          ("manualgop242", 242),
          ("manualgop302", 302))
    )


_TranscoderCfgSDManualGOP_Type.__name__ = "Integer32"
_TranscoderCfgSDManualGOP_Object = MibTableColumn
transcoderCfgSDManualGOP = _TranscoderCfgSDManualGOP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 21),
    _TranscoderCfgSDManualGOP_Type()
)
transcoderCfgSDManualGOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDManualGOP.setStatus("current")


class _TranscoderCfgSD32PullDown_Type(Integer32):
    """Custom type transcoderCfgSD32PullDown based on Integer32"""
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


_TranscoderCfgSD32PullDown_Type.__name__ = "Integer32"
_TranscoderCfgSD32PullDown_Object = MibTableColumn
transcoderCfgSD32PullDown = _TranscoderCfgSD32PullDown_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 22),
    _TranscoderCfgSD32PullDown_Type()
)
transcoderCfgSD32PullDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSD32PullDown.setStatus("current")


class _TranscoderCfgSDAspectRatio_Type(Integer32):
    """Custom type transcoderCfgSDAspectRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourThird", 1),
          ("sixteenNinth", 2))
    )


_TranscoderCfgSDAspectRatio_Type.__name__ = "Integer32"
_TranscoderCfgSDAspectRatio_Object = MibTableColumn
transcoderCfgSDAspectRatio = _TranscoderCfgSDAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 23),
    _TranscoderCfgSDAspectRatio_Type()
)
transcoderCfgSDAspectRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDAspectRatio.setStatus("current")


class _TranscoderCfgSDARConversion_Type(Integer32):
    """Custom type transcoderCfgSDARConversion based on Integer32"""
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
        *(("auto", 2),
          ("autoAFD", 3),
          ("fourByThreeFullHeight", 7),
          ("fourByThreeLetterBox", 4),
          ("fourByThreePillarBox", 5),
          ("fourteenByNine", 6),
          ("none", 1),
          ("sixteenByNineFullWidth", 8))
    )


_TranscoderCfgSDARConversion_Type.__name__ = "Integer32"
_TranscoderCfgSDARConversion_Object = MibTableColumn
transcoderCfgSDARConversion = _TranscoderCfgSDARConversion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 24),
    _TranscoderCfgSDARConversion_Type()
)
transcoderCfgSDARConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderCfgSDARConversion.setStatus("current")


class _TranscoderCfgSDVideoPreproc_Type(Integer32):
    """Custom type transcoderCfgSDVideoPreproc based on Integer32"""
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
        *(("deBlock", 2),
          ("edgeEnhancement", 4),
          ("mosquito", 3),
          ("none", 1))
    )


_TranscoderCfgSDVideoPreproc_Type.__name__ = "Integer32"
_TranscoderCfgSDVideoPreproc_Object = MibTableColumn
transcoderCfgSDVideoPreproc = _TranscoderCfgSDVideoPreproc_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 1, 1, 25),
    _TranscoderCfgSDVideoPreproc_Type()
)
transcoderCfgSDVideoPreproc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderCfgSDVideoPreproc.setStatus("current")
_TranscoderStatusTable_Object = MibTable
transcoderStatusTable = _TranscoderStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2)
)
if mibBuilder.loadTexts:
    transcoderStatusTable.setStatus("current")
_TranscoderStatusEntry_Object = MibTableRow
transcoderStatusEntry = _TranscoderStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1)
)
transcoderStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderStatusIndex"),
)
if mibBuilder.loadTexts:
    transcoderStatusEntry.setStatus("current")


class _TranscoderStatusIndex_Type(Integer32):
    """Custom type transcoderStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TranscoderStatusIndex_Type.__name__ = "Integer32"
_TranscoderStatusIndex_Object = MibTableColumn
transcoderStatusIndex = _TranscoderStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1, 1),
    _TranscoderStatusIndex_Type()
)
transcoderStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderStatusIndex.setStatus("current")


class _TranscoderStatusVideoStream_Type(Integer32):
    """Custom type transcoderStatusVideoStream based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("hd1080i2500", 8),
          ("hd1080i2997", 9),
          ("hd1080i3000", 10),
          ("hd720p5000", 5),
          ("hd720p5994", 6),
          ("hd720p6000", 7),
          ("sd480i2997", 2),
          ("sd480i3000", 3),
          ("sd576i2500", 4),
          ("unknown", 1),
          ("unsupported", 11))
    )


_TranscoderStatusVideoStream_Type.__name__ = "Integer32"
_TranscoderStatusVideoStream_Object = MibTableColumn
transcoderStatusVideoStream = _TranscoderStatusVideoStream_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 2, 1, 2),
    _TranscoderStatusVideoStream_Type()
)
transcoderStatusVideoStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderStatusVideoStream.setStatus("current")
_TranscoderSubtTable_Object = MibTable
transcoderSubtTable = _TranscoderSubtTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3)
)
if mibBuilder.loadTexts:
    transcoderSubtTable.setStatus("current")
_TranscoderSubtEntry_Object = MibTableRow
transcoderSubtEntry = _TranscoderSubtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1)
)
transcoderSubtEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-TRANSCODE-MIB", "transcoderSubtIndex"),
)
if mibBuilder.loadTexts:
    transcoderSubtEntry.setStatus("current")


class _TranscoderSubtIndex_Type(Integer32):
    """Custom type transcoderSubtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TranscoderSubtIndex_Type.__name__ = "Integer32"
_TranscoderSubtIndex_Object = MibTableColumn
transcoderSubtIndex = _TranscoderSubtIndex_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 1),
    _TranscoderSubtIndex_Type()
)
transcoderSubtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transcoderSubtIndex.setStatus("current")


class _TranscoderSubtOpMode_Type(Integer32):
    """Custom type transcoderSubtOpMode based on Integer32"""
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
        *(("dvb", 4),
          ("imiText", 3),
          ("off", 1),
          ("on", 2))
    )


_TranscoderSubtOpMode_Type.__name__ = "Integer32"
_TranscoderSubtOpMode_Object = MibTableColumn
transcoderSubtOpMode = _TranscoderSubtOpMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 2),
    _TranscoderSubtOpMode_Type()
)
transcoderSubtOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtOpMode.setStatus("current")


class _TranscoderSubtLangMenu_Type(Integer32):
    """Custom type transcoderSubtLangMenu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("languageEntry", 2),
          ("languageList", 1),
          ("pmtOrder", 3))
    )


_TranscoderSubtLangMenu_Type.__name__ = "Integer32"
_TranscoderSubtLangMenu_Object = MibTableColumn
transcoderSubtLangMenu = _TranscoderSubtLangMenu_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 3),
    _TranscoderSubtLangMenu_Type()
)
transcoderSubtLangMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtLangMenu.setStatus("current")


class _TranscoderSubtLangList_Type(Integer32):
    """Custom type transcoderSubtLangList based on Integer32"""
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
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("ara", 1),
          ("ben", 3),
          ("btk", 2),
          ("bul", 4),
          ("chi", 5),
          ("cze", 6),
          ("dan", 7),
          ("dut", 8),
          ("eng", 9),
          ("fin", 10),
          ("fre", 11),
          ("ger", 12),
          ("gre", 13),
          ("heb", 14),
          ("hin", 15),
          ("hun", 16),
          ("ice", 17),
          ("ind", 18),
          ("ita", 19),
          ("jpn", 20),
          ("kor", 21),
          ("may", 22),
          ("mul", 23),
          ("nor", 24),
          ("per", 25),
          ("pol", 26),
          ("por", 27),
          ("rum", 28),
          ("rus", 29),
          ("san", 30),
          ("scc", 31),
          ("sin", 32),
          ("slo", 33),
          ("som", 35),
          ("spa", 36),
          ("swe", 37),
          ("tai", 38),
          ("tam", 39),
          ("tha", 40),
          ("tur", 41),
          ("ukr", 42),
          ("vie", 43))
    )


_TranscoderSubtLangList_Type.__name__ = "Integer32"
_TranscoderSubtLangList_Object = MibTableColumn
transcoderSubtLangList = _TranscoderSubtLangList_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 4),
    _TranscoderSubtLangList_Type()
)
transcoderSubtLangList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtLangList.setStatus("current")


class _TranscoderSubtPMTOrder_Type(Integer32):
    """Custom type transcoderSubtPMTOrder based on Integer32"""
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
        *(("eighth", 8),
          ("fifth", 5),
          ("first", 1),
          ("fourth", 4),
          ("second", 2),
          ("seventh", 7),
          ("sixth", 6),
          ("third", 3))
    )


_TranscoderSubtPMTOrder_Type.__name__ = "Integer32"
_TranscoderSubtPMTOrder_Object = MibTableColumn
transcoderSubtPMTOrder = _TranscoderSubtPMTOrder_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 5),
    _TranscoderSubtPMTOrder_Type()
)
transcoderSubtPMTOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtPMTOrder.setStatus("current")


class _TranscoderSubtManualEntry_Type(DisplayString):
    """Custom type transcoderSubtManualEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_TranscoderSubtManualEntry_Type.__name__ = "DisplayString"
_TranscoderSubtManualEntry_Object = MibTableColumn
transcoderSubtManualEntry = _TranscoderSubtManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 6),
    _TranscoderSubtManualEntry_Type()
)
transcoderSubtManualEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtManualEntry.setStatus("current")


class _TranscoderSubtImitextPos_Type(Integer32):
    """Custom type transcoderSubtImitextPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_TranscoderSubtImitextPos_Type.__name__ = "Integer32"
_TranscoderSubtImitextPos_Object = MibTableColumn
transcoderSubtImitextPos = _TranscoderSubtImitextPos_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 7),
    _TranscoderSubtImitextPos_Type()
)
transcoderSubtImitextPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtImitextPos.setStatus("current")


class _TranscoderSubtForeGround_Type(Integer32):
    """Custom type transcoderSubtForeGround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("white", 3),
          ("yellow", 2))
    )


_TranscoderSubtForeGround_Type.__name__ = "Integer32"
_TranscoderSubtForeGround_Object = MibTableColumn
transcoderSubtForeGround = _TranscoderSubtForeGround_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 8),
    _TranscoderSubtForeGround_Type()
)
transcoderSubtForeGround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtForeGround.setStatus("current")


class _TranscoderSubtBackGround_Type(Integer32):
    """Custom type transcoderSubtBackGround based on Integer32"""
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
        *(("auto", 2),
          ("none", 1),
          ("opaque", 4),
          ("semi", 5),
          ("shadow", 3))
    )


_TranscoderSubtBackGround_Type.__name__ = "Integer32"
_TranscoderSubtBackGround_Object = MibTableColumn
transcoderSubtBackGround = _TranscoderSubtBackGround_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 37, 2, 3, 1, 9),
    _TranscoderSubtBackGround_Type()
)
transcoderSubtBackGround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transcoderSubtBackGround.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-TRANSCODE-MIB",
    **{"ciscoDSGTranscode": ciscoDSGTranscode,
       "transcoderInfo": transcoderInfo,
       "transcoderLOIAction": transcoderLOIAction,
       "transcoderTable": transcoderTable,
       "transcoderCfgTable": transcoderCfgTable,
       "transcoderCfgEntry": transcoderCfgEntry,
       "transcoderCfgIndex": transcoderCfgIndex,
       "transcoderCfgApplyInband": transcoderCfgApplyInband,
       "transcoderCfgVRes": transcoderCfgVRes,
       "transcoderCfgCCPkt1": transcoderCfgCCPkt1,
       "transcoderCfgCCPkt2": transcoderCfgCCPkt2,
       "transcoderCfgCCPkt3": transcoderCfgCCPkt3,
       "transcoderCfgPCRRate": transcoderCfgPCRRate,
       "transcoderCfgHDHRes": transcoderCfgHDHRes,
       "transcoderCfgHDBitrateMode": transcoderCfgHDBitrateMode,
       "transcoderCfgHDBitRate": transcoderCfgHDBitRate,
       "transcoderCfgHDGOP": transcoderCfgHDGOP,
       "transcoderCfgHDManualGOP": transcoderCfgHDManualGOP,
       "transcoderCfgHD32PullDown": transcoderCfgHD32PullDown,
       "transcoderCfgHDAspectRatio": transcoderCfgHDAspectRatio,
       "transcoderCfgHDARConversion": transcoderCfgHDARConversion,
       "transcoderCfgHDVideoPreproc": transcoderCfgHDVideoPreproc,
       "transcoderCfgSDHRes": transcoderCfgSDHRes,
       "transcoderCfgSDBitRateMode": transcoderCfgSDBitRateMode,
       "transcoderCfgSDBitRate": transcoderCfgSDBitRate,
       "transcoderCfgSDGOP": transcoderCfgSDGOP,
       "transcoderCfgSDManualGOP": transcoderCfgSDManualGOP,
       "transcoderCfgSD32PullDown": transcoderCfgSD32PullDown,
       "transcoderCfgSDAspectRatio": transcoderCfgSDAspectRatio,
       "transcoderCfgSDARConversion": transcoderCfgSDARConversion,
       "transcoderCfgSDVideoPreproc": transcoderCfgSDVideoPreproc,
       "transcoderStatusTable": transcoderStatusTable,
       "transcoderStatusEntry": transcoderStatusEntry,
       "transcoderStatusIndex": transcoderStatusIndex,
       "transcoderStatusVideoStream": transcoderStatusVideoStream,
       "transcoderSubtTable": transcoderSubtTable,
       "transcoderSubtEntry": transcoderSubtEntry,
       "transcoderSubtIndex": transcoderSubtIndex,
       "transcoderSubtOpMode": transcoderSubtOpMode,
       "transcoderSubtLangMenu": transcoderSubtLangMenu,
       "transcoderSubtLangList": transcoderSubtLangList,
       "transcoderSubtPMTOrder": transcoderSubtPMTOrder,
       "transcoderSubtManualEntry": transcoderSubtManualEntry,
       "transcoderSubtImitextPos": transcoderSubtImitextPos,
       "transcoderSubtForeGround": transcoderSubtForeGround,
       "transcoderSubtBackGround": transcoderSubtBackGround}
)
